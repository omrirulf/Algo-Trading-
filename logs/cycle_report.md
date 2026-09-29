# Daily report

**29 Sep 2026, 19:08 Israel time (16:08 UTC)** · 80 names checked · 0 traded · 1 with a problem

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 3 | 13 | 0 |
| Whole-market funds | 14 | 0 | 14 | 0 |
| Sector and country funds | 41 | 0 | 40 | 1 |
| Commodities | 9 | 0 | 9 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| US inflation-linked bonds (TIP) · Index fund | **Sold part.** Sold 3 of 7 shares at +3.05R, 4 still held. Stop-loss raised 104.90 → 104.79. |
| ASML (ASML) · Company | **Stop raised.** Reached +1.06R; too small to split, so only the stop moved. Stop-loss raised 1651.24 → 1733.63. |
| Caterpillar (CAT) · Company | **Stop raised.** At +0.38R, following the price. Stop-loss raised 777.80 → 780.92. |
| Developing country bonds (EMB) · Index fund | **Stop raised.** At +2.56R, following the price. Stop-loss raised 92.37 → 92.34. |
| US government bonds, 7-10 years (IEF) · Index fund | **Stop raised.** At +2.24R, following the price. Stop-loss raised 90.39 → 90.37. |
| US regional banks (KRE) · Sector or country | **Stop raised.** At +0.48R, following the price. Stop-loss raised 72.54 → 72.49. |
| Nvidia (NVDA) · Company | **Stop raised.** At +1.21R, following the price. Stop-loss raised 219.01 → 219.12. |
| Novo Nordisk (NVO) · Company | **Stop raised.** At +0.56R, following the price. Stop-loss raised 40.85 → 40.52. |
| S&P 500, equal weight (RSP) · Index fund | **Stop raised.** At +0.75R, following the price. Stop-loss raised 213.56 → 212.66. |
| US government bonds, 20+ years (TLT) · Index fund | **Stop raised.** At +2.13R, following the price. Stop-loss raised 80.00 → 79.80. |
| US dollar (UUP) · Index fund | **Stop raised.** At +1.72R, following the price. Stop-loss raised 28.50 → 28.54. |
| US shopping and leisure (XLY) · Sector or country | **Stop raised.** At +0.35R, following the price. Stop-loss raised 112.69 → 112.09. |
| Taiwan (EWT) · Sector or country | **Holding.** -0.13R, holding 33 shares. Stop-loss 110.28. |
| Gold (GLD) · Commodity | **Holding.** +0.46R, holding 10 shares. Stop-loss 393.48. |
| HDFC Bank (HDB) · Company | **Holding.** -0.74R, holding 90 shares. Stop-loss 22.23. |
| JPMorgan Chase (JPM) · Company | **Holding.** -0.17R, holding 6 shares. Stop-loss 327.15. |
| Eli Lilly (LLY) · Company | **Holding.** +0.39R, holding 4 shares. Stop-loss 1130.70. |
| Microsoft (MSFT) · Company | **Holding.** +1.04R, holding 7 shares. Stop-loss 492.61. |
| Procter & Gamble (PG) · Company | **Holding.** +0.12R, holding 14 shares. Stop-loss 143.66. |
| Royal Bank of Canada (RY) · Company | **Holding.** -0.21R, holding 10 shares. Stop-loss 195.58. |
| Teva Pharmaceutical (TEVA) · Company | **Holding.** -0.21R, holding 128 shares. Stop-loss 37.12. |
| Exxon Mobil (XOM) · Company | **Holding.** -0.04R, holding 13 shares. Stop-loss 156.50. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Alphabet (Google) (GOOGL) · Company — BULLISH, confidence 0.60

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> The company shows a strong material catalyst (a $514 B Google Cloud backlog) and solid fundamentals, while technicals are short‑term bearish and recent earnings have been mixed. Overall, the bullish fundamentals and catalyst outweigh the bearish technicals, leading to a bullish view with moderate conviction.

**Main reasons it gave:**
- $514 B Google Cloud backlog indicating strong future revenue (news)
- Profit margin 54.8% and ROE 48.7% with 24.2% YoY revenue growth (fundamentals)
- Analyst consensus strong buy with 26.7% upside price target (analyst view)
- Price below 20‑day SMA and RSI 45.9 suggest short‑term bearish momentum (technical)

<details><summary><b>News</b> — score +0.30</summary>

- [Cathie Wood Sells GOOGL Stock, Keeps Buying AVAV Shares For Second Straight Day](https://stocktwits.com/news-articles/markets/equity/cathie-wood-ark-invest-buys-avav-stock-again-trims-googl-stake-sells-iridium/cZtYg1iRB2Y)  
  <sub>Stocktwits, 12 hours ago</sub>  
  Cathie Wood's ARK Invest bought another 9037 AeroVironment shares Tuesday, extending its AVAV buying to a second consecutive session.
- [Cloudflare CEO Says “Everything Wrong” Online Is Google’s Fault, and Lets Sites Cut Off Its AI Training](https://www.tikr.com/blog/cloudflare-ceo-says-everything-wrong-online-is-googles-fault-and-lets-sites-cut-off-its-ai-training)  
  <sub>TIKR.com, 5 hours ago</sub>  
  Alphabet spent $91 billion on capex last year to build AI. Now Cloudflare wants Google to ask before training. Here's what the bill could look like.
- [Alphabet: Buy Before It Cashes In On Its TPUs (NASDAQ:GOOGL)](https://seekingalpha.com/article/4950475-alphabet-stock-buy-before-it-cashes-in-on-its-tpus)  
  <sub>Seeking Alpha, 13 hours ago</sub>  
  Google Cloud's accelerating growth, Gemini adoption, and $514B backlog provide substantial AI-driven revenue visibility for Alphabet. Read why GOOGL stock...
- [GOOGL Oct 2026 357.500 call (GOOGL261007C00357500) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GOOGL261007C00357500/)  
  <sub>Yahoo! Finance Canada, 8 hours ago</sub>  
  Find the latest GOOGL Oct 2026 357.500 call (GOOGL261007C00357500) stock quote, history, news and other vital information to help you with your stock...
- [How Has Alphabet Stock’s Story Changed?](https://www.trefis.com/stock/googl/articles/616790/how-has-alphabet-stocks-story-changed/2026-09-28)  
  <sub>Trefis, 19 hours ago</sub>  
  Alphabet's management has changed what it talks about on its earnings calls. In April 2024, managing its own cost base was a major strategic focus.
- [Wall Street upgrades Google (GOOGL) stock price target for next 12 months](https://finbold.com/wall-street-upgrades-google-googl-stock-price-target-for-next-12-months/)  
  <sub>Finbold, 20 hours ago</sub>  
  Despite GOOGL stock falling 16.5% since early May 2026, Champion expects Google's price to rally towards its ATH over the next 12 months.
- [Billionaire Money Managers Have Chosen Their 2 Favorite AI Stocks (and It's Not Nvidia or Alphabet)](https://www.theglobeandmail.com/investing/markets/stocks/GOOGL/pressreleases/4851338/billionaire-money-managers-have-chosen-their-2-favorite-ai-stocks-and-its-not-nvidia-or-alphabet/)  
  <sub>The Globe and Mail, 3 hours ago</sub>  
  Detailed price information for Alphabet Cl A (GOOGL-Q) from The Globe and Mail including charting and trades.
- [Berkshire’s Heavy Bet on Alphabet Has an Investment Logic Different From Apple](https://nai500.com/blog/2026/09/berkshires-heavy-bet-on-alphabet-has-an-investment-logic-different-from-apple/)  
  <sub>NAI500, 7 hours ago</sub>  
  Warren Buffett recently stepped down as chairman of Berkshire Hathaway, and he had no prior history of holding technology companies.
- [Alphabet (GOOGL) Flags $514 Billion Cloud Backlog As Revenue Mix Starts To Shift](https://simplywall.st/stocks/us/media/nasdaq-googl/alphabet/news/alphabet-googl-flags-514-billion-cloud-backlog-as-revenue-mi)  
  <sub>Simply Wall Street, 7 hours ago</sub>  
  Alphabet (NasdaqGS:GOOGL) reported that Google Cloud now carries a stated backlog of about $514b tied to long-term contracts.
- [Why Is Alphabet (NASDAQ:GOOGL) Suddenly a Must-Watch Communication Stocks Stock Today?](https://kalkinemedia.com/us/stocks/communication/why-is-alphabet-nasdaqgoogl-suddenly-a-must-watch-communication-stocks-stock-today)  
  <sub>Kalkine Media, 2 hours ago</sub>  
  Alphabet (NASDAQ:GOOGL) enters today's market discussion as sector themes, operations, and broader conditions draw attention.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 338.96 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 341.96 (-0.9%), 50d 343.95 (-1.5%), 200d 338.43 (+0.2%); 50d above 200d
Momentum: RSI(14) 45.9 | MACD -0.451 vs signal -0.333 (histogram -0.118)
Returns: 1d -1.1% | 5d -3.5% | 1m -2.2% | 3m -5.2%
52-week range: 236.57 - 402.62 (now 61.7% of the way up)
Volatility: ATR(14) 8.21 (2.4% of price) | annualised 20d 25.8%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 4.15T
Valuation: trailing P/E 17.02 | forward P/E 22.49 | P/B 6.66 | PEG 1.25
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: strong_buy (mean 1.38 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 13 strong buy, 43 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 429.55 (+26.7% vs last close), range 340.00 - 515.00
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

### MercadoLibre (MELI) · Company — BULLISH, confidence 0.60

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Positive credit‑growth news for MELI’s fintech platform, a strong analyst consensus (buy) with a +32.8% price‑target premium, and recent insider purchases outweigh the bearish technicals (price below key SMAs, low volume) and mixed fundamentals (high valuation, high debt). The net view is a modest buy signal with medium conviction.

**Main reasons it gave:**
- Credit growth in MELI's fintech business reported (positive catalyst)
- Analyst consensus strong buy with mean price target +32.8% above last close
- Insider purchases: 124 shares by officer and 600 shares by director
- Technical indicators show price below 20‑day, 50‑day, 200‑day SMAs and low volume

<details><summary><b>News</b> — score +0.80</summary>

- [3 Profitable Stocks Worth Investigating](https://finance.yahoo.com/markets/stocks/articles/3-profitable-stocks-worth-investigating-101602369.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Profitability is a key measure of business strength. Companies with high margins have proven they can generate consistent earnings while maintaining...
- [Chris Brown Ft. Kehlani - Over Again (Official Lyric Video) Type Song Meli Stock (ApHv9CL3XR)](https://media.unisba.ac.id/ac0b168c/196fdacfIDAcAz4aPT9eCxU)  
  <sub>Unisba Media, 9 hours ago</sub>  
  ECHOIXx presents a late-night R&B experience. If you love smooth R&B, emotional slow jams, and soulful late-night music, this track is made for you.
- [MercadoLibre stock last traded at USD 1,712.41 on September 28, 2026](https://www.ad-hoc-news.de/boerse/news/nachboerse/mercadolibre-stock-last-traded-at-usd-1-712-41-on-september-28-2026/70195539)  
  <sub>AD HOC NEWS, 18 hours ago</sub>  
  MELI, US58733R1023. MercadoLibre stock last traded at USD 1,712.41 on September 28, 2026. Published on 09/28/2026 at 23:01 | Editorial responsibility:...
- [MercadoLibre's Credit Growth Strengthens Its Fintech Ecosystem](https://www.theglobeandmail.com/investing/markets/stocks/AMZN/pressreleases/4857924/mercadolibres-credit-growth-strengthens-its-fintech-ecosystem/)  
  <sub>The Globe and Mail, 31 minutes ago</sub>  
  MercadoLibre, Inc.'s MELI credit business continued to expand in the second quarter of 2026, reinforcing the connection between its fintech platform and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 1,711.59 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 1,855.21 (-7.7%), 50d 1,866.20 (-8.3%), 200d 1,842.01 (-7.1%); 50d above 200d
Momentum: RSI(14) 32.5 | MACD -42.764 vs signal -23.630 (histogram -19.135)
Returns: 1d -0.0% | 5d -6.3% | 1m -13.0% | 3m +0.8%
52-week range: 1,546.81 - 2,501.31 (now 17.3% of the way up)
Volatility: ATR(14) 56.59 (3.3% of price) | annualised 20d 26.7%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 86.77B
Valuation: trailing P/E 47.60 | forward P/E 30.62 | P/B 11.08 | PEG 1.00
Profitability: profit margin 5.3% | operating margin 6.7% | ROE 27.5%
Growth (YoY): revenue +49.8% | earnings -10.9%
Balance sheet: debt/equity 168.6% | free cash flow 353.38M
Risk: beta 1.31 | short interest 1.6% of float
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

```text
Consensus: buy (mean 1.56 on a 1=strong buy to 5=strong sell scale, 25 analysts)
Ratings: 4 strong buy, 16 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 2,272.28 (+32.8% vs last close), range 1,750.00 - 2,800.00
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

### Toyota (TM) · Company — BEARISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Negative sales news and bearish technicals outweigh bullish fundamentals and analyst outlook, leading to a short‑term bearish view with moderate confidence.

**Main reasons it gave:**
- Toyota global sales fell 6.4% YoY, with a 23% decline in China sales for August (Seeking Alpha, Investing.com)
- Price below 20‑day, 50‑day, and 200‑day SMAs; RSI 40.6; MACD negative; volume 0.15× 20‑day average (Technicals)
- Trailing P/E 8.49 suggests cheap valuation but debt/equity 115% and negative free cash flow (Fundamentals)
- Analyst consensus strong buy with mean price target +26% but recent downgrades (Analyst view)
- Four consecutive earnings beats (Earnings record)

<details><summary><b>News</b> — score -0.80</summary>

- [Clinics are expected to compare heart-monitor software with their current workflow.](https://www.stocktitan.net/news/AIMLF/aiml-subsidiary-neural-cloud-enters-strategic-partnership-with-rks-vgwaca89ssod.html)  
  <sub>Stock Titan, 3 hours ago</sub>  
  RKS Medical is expected to introduce NeuralCloud to clinics for pre-regulatory pilots; AIML extended expiry dates for 44.2 million warrants to November...
- [Update: US Equity Futures Slightly Higher Pre-Bell Amid Elevated Treasury Yields, Lack of Progress in US-Iran Talks](https://ca.finance.yahoo.com/news/us-equity-futures-slightly-higher-125440523.html)  
  <sub>Yahoo! Finance Canada, 2 hours ago</sub>  
  Updates with economic data, recent oil price movement, world markets' overview and corporate stock.
- [Toyota global sales drop for 7th straight month amid China slump, output falls 5.9% (TM:NYSE)](https://seekingalpha.com/news/4647844-toyota-global-sales-drop-for-7th-straight-month-amid-china-slump-output-falls-59)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  The world's biggest automaker, Toyota (TM),) on Tuesday said global sales fell 6.4% from a year ​earlier to 790,743 vehicles and production ​was down 5.9%...
- [(HBIL) Risk-Controlled Trading Report (HBIL:CA)](https://news.stocktradersdaily.com/canada/hbil-risk-controlled-trading-report_20260929_c06945)  
  <sub>Stock Traders Daily, 3 hours ago</sub>  
  Risk-Controlled Trading Report for Hamilton U.S. T-Bill YIELD MAXIMIZER TM ETF (HBIL) with Key Buy and Sell Indicators.
- [Toyota stock falls as China sales drop on fuel price surge By Investing.com](https://za.investing.com/news/stock-market-news/toyota-stock-falls-as-china-sales-drop-on-fuel-price-surge-93CH-4481888)  
  <sub>Investing.com South Africa, 5 hours ago</sub>  
  Investing.com - Toyota Motor (NYSE:TM) reported a 23% decline in China sales for August, marking the seventh consecutive monthly drop as rising fuel prices...
- [A construction panel sheds nearly a quarter of its weight, easing handling and lowering shipping costs.](https://www.stocktitan.net/news/XERI/xeriant-achieves-nearly-25-nex-board-tm-weight-k40i2ellpdft.html)  
  <sub>Stock Titan, 3 hours ago</sub>  
  Panels support sample fulfillment for homebuilders and commercial construction firms evaluating NexBoard as a universal panel. Production continues.
- [GM tech costs to fall by $20B through 2031 after rollback of fuel economy standards](https://seekingalpha.com/news/4647852-gm-tech-costs-fuel-economy-standards)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  NHTSA's new CAFE rule cuts automakers' tech costs $60.6B by 2031, lowering 2031 vehicle costs by $1289.
- [Learn to Evaluate (HBIL.U) using the Charts (HBIL.U:CA)](https://news.stocktradersdaily.com/canada/learn-to-evaluate-hbilu-using-the-charts_20260929_75c5b7)  
  <sub>Stock Traders Daily, 3 hours ago</sub>  
  Learn to Evaluate Hamilton U.S. T-Bill YIELD MAXIMIZER TM ETF HBIL.U using the Charts.
- [Charged gas stayed apart from chamber walls for about a second in earlier, low-temperature tests.](https://www.stocktitan.net/news/AMFN/american-fusion-inc-otcqb-amfn-outlines-texatron-tm-plasma-2u6tq4v8gvyx.html)  
  <sub>Stock Titan, 3 hours ago</sub>  
  Texatron has not demonstrated fusion ignition, net energy gain or direct electricity conversion; testing aims to measure plasma conditions and confinement.
- [Sensex Today Ends 242 Points Lower | Nifty Below 22,750 | Tata Chemicals Down 4.5%](https://www.equitymaster.com/indian-share-markets/09/29/2026/Sensex-Today-Ends-242-Points-Lower--Nifty-Below-22750--Tata-Chemicals-Down-45?utm_source=homepage&utm_medium=website&utm_campaign=Content&utm_content=TM)  
  <sub>Equitymaster, 4 hours ago</sub>  
  The BSE Sensex ends 242 points lower, while Nifty ended 64 points lower, down at 22716.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.80</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 185.84 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 193.16 (-3.8%), 50d 190.45 (-2.4%), 200d 201.77 (-7.9%); 50d below 200d
Momentum: RSI(14) 40.6 | MACD -0.854 vs signal 0.300 (histogram -1.154)
Returns: 1d -1.3% | 5d -3.2% | 1m -4.4% | 3m +10.3%
52-week range: 166.50 - 248.29 (now 23.6% of the way up)
Volatility: ATR(14) 3.23 (1.7% of price) | annualised 20d 22.2%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 220.07B
Valuation: trailing P/E 8.49 | forward P/E 11.78 | P/B 14.74 | PEG n/a
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: strong_buy (mean 1.50 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 2 strong buy, 2 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 234.08 (+26.0% vs last close), range 230.00 - 239.31
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

### Elbit Systems (ESLT) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bearish technicals, strong earnings record and modest upside in analyst targets, but high valuation and weak insider buying. Contradictory inputs lead to a neutral stance with low conviction.

**Main reasons it gave:**
- RSI 33.6 and price below 20‑day, 50‑day, 200‑day SMAs indicate bearish technicals
- Four consecutive earnings beats show strong earnings record
- Trailing P/E 52.4 and forward P/E 38.0 suggest expensive valuation
- Insider sales by CEO and officers, no distinct insider buying

<details><summary><b>News</b> — score +0.00</summary>

- [Is EmbraerEmpresa Brasileira de Aeronautica (EMBJ) Outperforming Other Aerospace Stocks This Year?](https://finance.yahoo.com/markets/stocks/articles/embraerempresa-brasileira-aeronautica-embj-outperforming-124004104.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Here is how Embraer (EMBJ) and Elbit Systems (ESLT) have performed compared to their sector so far this year.
- [A Look at Elbit Systems Ltd (ESLT) After 4.2% Decline -- GF Value $384.57 vs Price $704.27](https://www.gurufocus.com/news/9100525/a-look-at-elbit-systems-ltd-eslt-after-42-decline-gf-value-38457-vs-price-70427)  
  <sub>GuruFocus, 17 hours ago</sub>  
  On September 28, 2026, Elbit Systems Ltd (ESLT) shares fell 4.2%, closing at $704.27. This decline comes amid a 52-week trading range of $453.00 to $1016.06...
- [ESLT270319C00670000 Interactive Stock Chart | ESLT Mar 2027 670.000 call Stock](https://finance.yahoo.com/chart/ESLT270319C00670000)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [Are Options Traders Betting on a Big Move in OSI Systems Stock?](https://finance.yahoo.com/markets/options/articles/options-traders-betting-big-move-160000249.html)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  Investors need to pay close attention to OSIS stock based on the movements in the options market lately.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.70</summary>

```text
Last close 698.13 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 724.95 (-3.7%), 50d 760.68 (-8.2%), 200d 771.03 (-9.5%); 50d below 200d
Momentum: RSI(14) 33.6 | MACD -7.720 vs signal -7.017 (histogram -0.702)
Returns: 1d -0.9% | 5d -6.3% | 1m -1.5% | 3m -8.0%
52-week range: 454.95 - 1,014.33 (now 43.5% of the way up)
Volatility: ATR(14) 16.71 (2.4% of price) | annualised 20d 20.2%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 32.71B
Valuation: trailing P/E 52.41 | forward P/E 38.02 | P/B 7.40 | PEG n/a
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
Price target: mean 816.33 (+16.9% vs last close), range 518.00 - 960.00
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

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

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

_Not available today._

</details>

### ASML (ASML) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [ASML Holding N.V. (ASML) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/ASML/)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  72,645.90% · Previous Close 1,743.94 · Open 1,747.75 · Bid 1,732.10 x 100 · Ask 1,743.30 x 200 · Day's Range 1,735.50 - 1,784.56 · 52 Week Range 935.41 -...
- [Why Everyone Is Watching ASML Holding (ENXTAM:ASML) Today](https://simplywall.st/stocks/nl/semiconductors/ams-asml/asml-holding-shares/news/why-everyone-is-watching-asml-holding-enxtamasml-today/amp)  
  <sub>Simply Wall Street, 2 hours ago</sub>  
  ASML's role in the AI equipment cycle ASML Holding (ENXTAM:ASML) is in focus as investors track how AI chip demand, large fab buildouts, and government...
- [ASML Holding NV (0QB8) Receives a Buy from UBS](https://www.theglobeandmail.com/investing/markets/stocks/ASML-Q/pressreleases/4854323/asml-holding-nv-0qb8-receives-a-buy-from-ubs/)  
  <sub>The Globe and Mail, 2 hours ago</sub>  
  In a report released today, Francois Xavier Bouvignies from UBS maintained a Buy rating on ASML Holding NV, with a price target of €2,350.00.
- [Stock Futures Drift as Treasury Selloff Continues](https://www.marketscreener.com/news/stock-futures-drift-as-treasury-selloff-continues-ce785addda8df121)  
  <sub>marketscreener.com, 6 hours ago</sub>  
  By Joe Stonor Stock futures moved sideways and 10-year Treasury yields held close to multiyear highs in cautious early European trade, as oil prices rose...
- [Why is ASML NV ADR stock rising today? By Investing.com](https://in.investing.com/news/stock-market-news/why-is-asml-nv-adr-stock-rising-today-93CH-5611241)  
  <sub>Investing.com India, 26 minutes ago</sub>  
  Investing.com -- ASML Holding NV ADR stock rose 2.5% in morning trading to reach $1,815.84, lifted by a Buy rating reiteration from UBS analyst...
- [ASML (ASML) Increases Despite Market Slip: Here's What You Need to Know](https://finance.yahoo.com/markets/stocks/articles/asml-asml-increases-despite-market-205005742.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  In the most recent trading session, ASML (ASML) closed at $1, indicating a +1.58% shift from the previous trading day.
- [Tether Just Made A Bigger Bet On XXI After Buying SoftBank’s Entire Stake](https://stocktwits.com/news-articles/markets/equity/xxi-stock-rises-tether-buys-softbank-stake-twenty-one-capital/cZXDCnlRen3)  
  <sub>Stocktwits, 11 hours ago</sub>  
  Tether International, the controlling shareholder of Twenty One Capital (XXI), announced on Wednesday that it has bought out SoftBank's entire stake in the...
- [ASML Holding stock reports Q2 revenue of EUR 9.33 billion](https://www.ad-hoc-news.de/boerse/news/corporate-news/asml-holding-stock-reports-q2-revenue-of-eur-9-33-billion/70197688)  
  <sub>AD HOC NEWS, 4 hours ago</sub>  
  ASML Holding stock was trading at EUR 1595.10 at Lang & Schwarz on September 29, 2026 at 1:06 p.m. CEST. UBS raised its target to EUR 2350.
- [ASML Stock Analysis 2026: 41% Upside Predicted – Is It Too Late To Buy? 📊🚀 Televoto Grande Fratello Vip Percentuali Oggi (6ilxFSK1sY)](https://media.unisba.ac.id/a19b3933/402477d1PQIxPhtDOSVYGwk/?share=telegram&nb=1)  
  <sub>Unisba Media, 16 hours ago</sub>  
  ASML Holding N.V. (ASML) stock analysis for 2026 – Here's everything investors need to know!. ASML just raised debito pubblico degli stati uniti...
- [JBL Q4 Earnings Coming Up: How Should You Play the Stock?](https://uk.finance.yahoo.com/news/jbl-q4-earnings-coming-play-111200465.html)  
  <sub>Yahoo Finance UK, 3 hours ago</sub>  
  Jabil, Inc. JBL is scheduled to report fourth-quarter fiscal 2026 earnings on Sept. 30. The Zacks Consensus Estimate for sales and earnings is pegged at...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,838.28 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 1,697.35 (+8.3%), 50d 1,720.03 (+6.9%), 200d 1,531.82 (+20.0%); 50d above 200d
Momentum: RSI(14) 63.4 | MACD 13.475 vs signal -5.382 (histogram 18.858)
Returns: 1d +3.8% | 5d +5.2% | 1m +8.4% | 3m -7.6%
52-week range: 936.19 - 1,989.44 (now 85.6% of the way up)
Volatility: ATR(14) 53.38 (2.9% of price) | annualised 20d 42.5%
Volume: 0.38x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 706.01B
Valuation: trailing P/E 63.67 | forward P/E 31.23 | P/B 1,579.54 | PEG 1.58
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
Price target: mean 2,113.66 (+15.0% vs last close), range 877.94 - 2,811.31
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

- [Stock-Split Watch: Is Caterpillar Next?](https://finance.yahoo.com/markets/stocks/articles/stock-split-watch-caterpillar-next-123100126.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Soaring more than 76% over the past year as of this writing, Caterpillar (NYSE: CAT) stock has given investors a lot to celebrate, especially compared to...
- [Caterpillar's agreed purchase covers a dealer with 37 locations; regulators must approve.](https://www.stocktitan.net/news/CAT/caterpillar-inc-enters-into-agreement-to-acquire-fabick-cat-q22f8ffrmrzf.html)  
  <sub>Stock Titan, 33 minutes ago</sub>  
  Fabick serves parts of Missouri and Illinois, all of Wisconsin and Michigan's Upper Peninsula. The deal needs regulatory approval and is expected to close...
- [Can CAT Stock Surge Again On A $72B Data Center Backlog?](https://www.trefis.com/stock/cat/articles/616801/can-cat-stock-surge-again-on-a-72b-data-center-backlog/2026-09-28)  
  <sub>Trefis, 20 hours ago</sub>  
  You want to know what could send Caterpillar (CAT) stock higher again. For one part of Caterpillar, buyers are not the problem. Some customers of its Power...
- [Caterpillar Inc. (CAT) Is a Trending Stock: Facts to Know Before Betting on It](https://finance.yahoo.com/markets/stocks/articles/caterpillar-inc-cat-trending-stock-120004301.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Recently, Zacks.com users have been paying close attention to Caterpillar (CAT). This makes it worthwhile to examine what the stock has in store.
- [How Caterpillar Inc. (CAT) Affects Rotational Strategy Timing](https://news.stocktradersdaily.com/news_release/40/How_Caterpillar_Inc._CAT_Affects_Rotational_Strategy_Timing_092926124002_1790656802.html)  
  <sub>Stock Traders Daily, 14 hours ago</sub>  
  Key findings for Caterpillar Inc. (NYSE: CAT). Neutral Near and Mid-Term Readings Could Moderate Long-Term Positive Bias; No clear price positioning signal...
- [Michael Burry shifts AI shorts to puts while Anthropic reveals $42B loss](https://www.tradingview.com/news/seekingalpha:33765b542094b:0-michael-burry-shifts-ai-shorts-to-puts-while-anthropic-reveals-42b-loss/)  
  <sub>TradingView, 7 hours ago</sub>  
  Michael Burry has intensified his bearish positioning on AI, shifting several stock shorts into long-dated put options as Anthropic NASDAQ:ANTHROPIC...
- [Shareholder Cat Price | SHCAT Price Today, Live Chart, USD converter, Market Capitalization](https://cryptorank.io/price/shareholder-cat)  
  <sub>CryptoRank, 58 minutes ago</sub>  
  Current Shareholder Cat (SHCAT) token data: Price $ 0.0000164, Trading Volume $ 0.00, Market Cap $ 0.00, Circ. Supply , Total Supply 100.00B. Official links...
- [Robinhood Chain’s Bundle Cat ($BUN) Rallies 180% This Week as Broader Memecoins Slip 4.5%](https://coingape.com/robinhood-chains-bundle-cat-bun-rallies-180-this-week-as-broader-memecoins-slip-4-5/)  
  <sub>CoinGape, 7 hours ago</sub>  
  Bundle Cat ($BUN), the first Mosh protocol token on Robinhood Chain, jumped 40% in 24 hours and 180% weekly as its locked-supply model draws investors.
- [GEV Stock Edges Higher Overnight: Growing Backlog Shows 'AI Data Centers Cannot Wait For The Grid,' Says Strategist](https://stocktwits.com/news-articles/markets/equity/gev-stock-edges-higher-overnight-growing-backlog-shows-ai-data-centers-cannot-wait-for-the-grid-says-strategist/cZZnWuuR7x7)  
  <sub>Stocktwits, 17 hours ago</sub>  
  GE Vernova's total backlog grew to more than $176 billion in the second quarter, a 37% increase year-on-year.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 823.41 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 805.58 (+2.2%), 50d 827.21 (-0.5%), 200d 791.73 (+4.0%); 50d above 200d
Momentum: RSI(14) 52.8 | MACD -3.217 vs signal -8.039 (histogram 4.821)
Returns: 1d +0.4% | 5d +1.9% | 1m +2.9% | 3m -22.7%
52-week range: 471.61 - 1,064.90 (now 59.3% of the way up)
Volatility: ATR(14) 21.62 (2.6% of price) | annualised 20d 25.4%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 378.50B
Valuation: trailing P/E 35.49 | forward P/E 25.43 | P/B 19.52 | PEG 1.42
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
Price target: mean 975.61 (+18.5% vs last close), range 575.00 - 1,225.00
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

- [HDB DCF Analysis: Intrinsic Value $33 vs Price $22](https://www.gurufocus.com/news/9101341/hdb-dcf-analysis-intrinsic-value-33-vs-price-22)  
  <sub>GuruFocus, 3 hours ago</sub>  
  On September 29, 2026, we conducted a discounted cash flow (DCF) analysis for HDFC Bank Ltd (HDB), which has seen a significant decline in its stock price...
- [HDB INVESTOR DEADLINE: HDFC Bank Limited Investors with Substantial Losses Have Opportunity to Lead the HDFC Shareholder Class Action Lawsuit Before October 13, 2023](https://www.newsfilecorp.com/release/316385/HDB-INVESTOR-DEADLINE-HDFC-Bank-Limited-Investors-with-Substantial-Losses-Have-Opportunity-to-Lead-the-HDFC-Shareholder-Class-Action-Lawsuit-Before-October-13-2023)  
  <sub>TMX Newsfile, 19 hours ago</sub>  
  San Francisco, California--(Newsfile Corp. - September 28, 2026) - Hagens Berman, a national law firm noted for its preeminent work...
- [Deadline Alert: HDFC Bank Limited (HDB) Shareholders Who](https://www.globenewswire.com/news-release/2026/09/28/3370246/0/en/deadline-alert-hdfc-bank-limited-hdb-shareholders-who-lost-money-urged-to-contact-glancy-prongay-wolke-rotter-llp-about-securities-fraud-lawsuit.html)  
  <sub>GlobeNewswire, 19 hours ago</sub>  
  LOS ANGELES, Sept. 28, 2026 (GLOBE NEWSWIRE) -- Glancy Prongay Wolke & Rotter LLP reminds investors of the upcoming October 13, 2026 deadline to file...
- [Investor alert! Nifty cracks below key 200-week moving average for the first time since Covid](https://m.economictimes.com/markets/stocks/news/investor-alert-nifty-cracks-below-key-200-week-moving-average-for-the-first-time-since-covid/articleshow/134565786.cms)  
  <sub>The Economic Times, 3 hours ago</sub>  
  Nifty slipped below its 200-week moving average near 22600 for the first time since the Covid crash, hitting 22569 intraday. Analysts are watching whether...
- [HDB Financial Services CS Dipti Khandelwal resigns effective Oct 30](https://scanx.trade/stock-market-news/companies/hdb-financial-services-cs-dipti-khandelwal-resigns-effective-oct-30/52210964)  
  <sub>scanx.trade, 8 hours ago</sub>  
  Dipti Jayesh Khandelwal resigned as Company Secretary and Head Legal of HDB Financial Services. Resignation effective October 30, 2026, after being tendered...
- [Singapore Housing Market Cools as Prices Rise and Borrowing Costs Increase](https://www.rprealtyplus.com/news-views/singapore-housing-market-cools-as-prices-rise-and-borrowing-costs-increase-127018.html)  
  <sub>Realty Plus Magazine, 10 hours ago</sub>  
  Singapore's housing market is losing momentum as private prices rise slowly, HDB values decline, inventory tightens and borrowing costs begin moving higher.
- [These large-caps have ‘strong buy’ & ‘buy’ recos and an upside potential of over 25% according to analysts](https://m.economictimes.com/markets/stocks/news/these-large-caps-have-strong-buy-buy-recos-and-an-upside-potential-of-over-25-according-to-analysts/articleshow/134549195.cms)  
  <sub>The Economic Times, 20 hours ago</sub>  
  What is happening in the stock markets shouldn't surprise you. There are headwinds blowing in from every direction. The geopolitical situation, the global...
- [Vietnam Stock Market Live: VNI Index VN-Index Falls 0.92% to 1,768.67 ; HNX Index Turns Red by 0.15% After Slight Opening Gains – Check Stocks in Focus, Investor Outlook & More](https://sundayguardianlive.com/business/vietnam-stock-market-live-vni-index-vn-index-falls-092-to-176867-hnx-index-turns-red-by-015-after-slight-opening-gains-check-stocks-in-focus-investor-outlook-more-294952/)  
  <sub>The Sunday Guardian, 11 hours ago</sub>  
  This morning, Vietnam's benchmark VNI Index is trading down by nearly 0.25%. While the HNX index of Hanoi is seeing a 0.33% dip, despite opening in green.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 22.53 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 22.83 (-1.3%), 50d 23.19 (-2.8%), 200d 27.26 (-17.4%); 50d below 200d
Momentum: RSI(14) 44.9 | MACD -0.154 vs signal -0.164 (histogram 0.010)
Returns: 1d +0.5% | 5d -3.8% | 1m -2.4% | 3m -12.8%
52-week range: 21.84 - 37.18 (now 4.5% of the way up)
Volatility: ATR(14) 0.52 (2.3% of price) | annualised 20d 35.8%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 115.79B
Valuation: trailing P/E 15.76 | forward P/E 16.19 | P/B 9.07 | PEG n/a
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
Price target: mean 30.52 (+35.5% vs last close), range 26.10 - 35.00
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

- [JPMorgan Chase (JPM) Stock May Trade At A Discount Following Record Dealmaking News](https://simplywall.st/stocks/us/banks/nyse-jpm/jpmorgan-chase/news/jpmorgan-chase-jpm-stock-may-trade-at-a-discount-following-r)  
  <sub>Simply Wall Street, 3 hours ago</sub>  
  JPMorgan Chase has delivered a very strong 150.1% share price gain over the past three years, and that kind of move naturally puts the focus on what the...
- [Will JPMorgan’s (JPM) New Notes and Preferred Dividend Clarify Its AI-Era Deposit Strategy?](https://finance.yahoo.com/markets/stocks/articles/jpmorgan-jpm-notes-preferred-dividend-100603155.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  In late September 2026, JPMorgan Chase issued a series of callable senior unsecured fixed- and step-up-rate notes totaling several tens of millions of US...
- [Analysts Offer Insights on Financial Companies: Visa (V), Pinnacle Financial Partners (PNFP) and JPMorgan Chase (JPM)](https://www.theglobeandmail.com/investing/markets/stocks/JPM-N/pressreleases/4853701/analysts-offer-insights-on-financial-companies-visa-v-pinnacle-financial-partners-pnfp-and-jpmorgan-chase-jpm/)  
  <sub>The Globe and Mail, 2 hours ago</sub>  
  Detailed price information for JP Morgan Chase & Company (JPM-N) from The Globe and Mail including charting and trades.
- [Baypointe Partners LLC Sells 5,000 Shares of JPMorgan Chase & Co. $JPM](https://www.marketbeat.com/instant-alerts/filing-baypointe-partners-llc-sells-5000-shares-of-jpmorgan-chase-co-jpm-2026-09-29/)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Baypointe Partners LLC lessened its holdings in JPMorgan Chase & Co. (NYSE:JPM) by 20.0% during the second quarter, according to the company in its most...
- [(JPM) Movement as an Input in Quant Signal Sets](https://news.stocktradersdaily.com/news_release/22/JPM_Movement_as_an_Input_in_Quant_Signal_Sets_092926013803_1790660283.html)  
  <sub>Stock Traders Daily, 13 hours ago</sub>  
  Key findings for Jpmorgan Chase & Co. (NYSE: JPM). Weak Near and Mid-Term Sentiment Could Challenge Long-Term Positive Outlook; A mid-channel oscillation...
- [BAC Gains 17.4% in 6 Months: Should You Invest in the Stock Now?](https://finance.yahoo.com/markets/stocks/articles/bac-gains-17-4-6-132300963.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  Shares of Bank of America BAC have gained 17.4% over the past six months, supported by improving fundamentals and a favorable operating backdrop.
- [Is JPMorgan Chase (NYSE:JPM) in the Spotlight for the Right Reasons Today?](https://kalkinemedia.com/us/stocks/financial/is-jpmorgan-chase-nysejpm-in-the-spotlight-for-the-right-reasons-today)  
  <sub>Kalkine Media, 2 hours ago</sub>  
  JPMorgan Chase (NYSE:JPM) enters today's market discussion as sector themes, operations, and broader conditions draw attention.
- [Top Wall Street Banks Kick Off Q2 Earnings Next Week — Here's What Analysts Expect](https://stocktwits.com/news-articles/markets/equity/top-wall-street-banks-kick-off-q2-earnings-next-week-here-s-what-analysts-expect/cZmrm9pR78o)  
  <sub>Stocktwits, 15 hours ago</sub>  
  The State Street SPDR S&P Bank ETF is trading near a record high, up 12% in 2026. U.S. consumer spending in June showed its strongest growth since April...
- [22,514 Shares in JPMorgan Chase & Co. $JPM Acquired by Markowski Investments](https://www.marketbeat.com/instant-alerts/filing-22514-shares-in-jpmorgan-chase-co-jpm-acquired-by-markowski-investments-2026-09-29/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Markowski Investments bought a new position in shares of JPMorgan Chase & Co. (NYSE:JPM) during the 2nd quarter, according to the company in its most recent...
- [J.P. Morgan Drops Sharp Take on Magnificent 7 Stocks](https://finance.yahoo.com/markets/stocks/articles/j-p-morgan-drops-sharp-080910133.html)  
  <sub>Yahoo Finance, 7 hours ago</sub>  
  This article first appeared on GuruFocus. J.P. Morgan says the Magnificent Seven's painful valuation reset may be largely complete, potentially removing one...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 335.39 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 349.18 (-3.9%), 50d 353.18 (-5.0%), 200d 321.57 (+4.3%); 50d above 200d
Momentum: RSI(14) 35.0 | MACD -4.382 vs signal -2.592 (histogram -1.790)
Returns: 1d -0.4% | 5d -1.4% | 1m -6.2% | 3m +2.5%
52-week range: 282.84 - 365.18 (now 63.8% of the way up)
Volatility: ATR(14) 6.45 (1.9% of price) | annualised 20d 19.1%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 891.53B
Valuation: trailing P/E 14.38 | forward P/E 13.42 | P/B 2.52 | PEG 1.57
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
Price target: mean 375.81 (+12.1% vs last close), range 305.00 - 436.00
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

- [LLY Vs NVO: Foundayo Beats Novo’s Oral Semaglutide On Weight Loss, Blood Sugar In New Finding](https://finance.yahoo.com/healthcare/articles/lly-vs-nvo-foundayo-beats-102114784.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  Lilly's Foundayo 17.2 mg achieved a 1.5% greater weight loss and a 0.3% greater reduction in A1C than oral semaglutide 25 mg after 52 weeks.
- [An indirect comparison found over 3 times the odds of losing 20% of body weight on Lilly's drug versus Wegovy](https://www.stocktitan.net/news/LLY/lilly-s-zepbound-tirzepatide-10-mg-and-15-mg-was-associated-with-oqdbuj3qe1fm.html)  
  <sub>Stock Titan, 4 hours ago</sub>  
  Eli Lilly (LLY) reported an indirect comparison associating Zepbound 10 mg and 15 mg with greater weight loss than Wegovy HD.
- [4 stocks to watch on Tuesday: AMD, NFLX, LLY, and MNDY (SPX:)](https://seekingalpha.com/news/4648008-4-stocks-to-watch-on-tuesday-amd-nflx-lly-and-mndy)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Stock index futures were mixed on Tuesday as investors awaited key economic releases later in the day after technology stocks came under pressure in the...
- [Did FDA Approvals And Medicare Expansion Just Shift Eli Lilly's (LLY) Stock Narrative?](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-lly/eli-lilly/news/did-fda-approvals-and-medicare-expansion-just-shift-eli-lill)  
  <sub>Simply Wall Street, 15 hours ago</sub>  
  Eli Lilly secured recent FDA approvals for Olumiant in adolescents with severe alopecia areata and once-weekly insulin Onswik for adults with type 2...
- [Eli Lilly's Foundayo Shows Superior Weight Loss Results; LLY Sto](https://www.gurufocus.com/news/9101102/eli-lillys-foundayo-shows-superior-weight-loss-results-lly-stock-modestly-undervalued)  
  <sub>GuruFocus, 6 hours ago</sub>  
  On September 29, 2026, Eli Lilly and Co (NYSE: LLY) announced that its oral weight-loss drug, Foundayo (orforglipron) 17.2 mg, demonstrated superior...
- [If You Invested $1000 In Eli Lilly Stock 10 Years Ago, You Would Have This Much Today](https://www.benzinga.com/news/26/09/62037462/if-you-invested-1000-eli-lilly-stock-10-years-ago-you-would-have-much-today)  
  <sub>Benzinga, 16 hours ago</sub>  
  Eli Lilly (NYSE:LLY) has outperformed the market over the past 10 years by 17.2% on an annualized basis producing an average annual return of 30.75%.
- [(LLY) Movement Within Algorithmic Entry Frameworks](https://news.stocktradersdaily.com/news_release/38/LLY_Movement_Within_Algorithmic_Entry_Frameworks_092926014802_1790660882.html)  
  <sub>Stock Traders Daily, 13 hours ago</sub>  
  Key findings for Eli Lilly And Company (NYSE: LLY). Strong Sentiment Across All Horizons Supports Overweight Bias; Support is being tested.
- [Is Eli Lilly (NYSE:LLY) the Healthcare Stocks Stock Everyone's Talking About Today?](https://kalkinemedia.com/us/stocks/healthcare/is-eli-lilly-nyselly-the-healthcare-stocks-stock-everyones-talking-about-today)  
  <sub>Kalkine Media, 2 hours ago</sub>  
  Eli Lilly (NYSE:LLY) enters today's market discussion as sector themes, operations, and broader conditions draw attention.
- [What Could Eli Lilly (LLY) New Cancer Win And Deal Shift Mean?](https://finance.yahoo.com/healthcare/articles/could-eli-lilly-lly-cancer-070844552.html)  
  <sub>Yahoo Finance, 8 hours ago</sub>  
  Eli Lilly (NYSE:LLY) received FDA Breakthrough Therapy designation for its next-generation KRAS G12C inhibitor olomorasib in advanced pancreatic cancer.
- [Lilly's Foundayo showed a 0.3% greater drop in a blood-sugar measure than semaglutide.](https://www.stocktitan.net/news/LLY/lilly-s-foundayo-orforglipron-17-2-mg-showed-greater-weight-loss-and-a8k1j35auhc4.html)  
  <sub>Stock Titan, 8 hours ago</sub>  
  Eli Lilly (LLY) reported an indirect comparison showing greater weight loss and A1C reduction with Foundayo than with oral semaglutide.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,170.04 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 1,151.98 (+1.6%), 50d 1,177.99 (-0.7%), 200d 1,071.99 (+9.1%); 50d above 200d
Momentum: RSI(14) 51.2 | MACD -0.412 vs signal -5.855 (histogram 5.443)
Returns: 1d -1.2% | 5d -0.0% | 1m -0.4% | 3m -2.5%
52-week range: 726.51 - 1,280.34 (now 80.1% of the way up)
Volatility: ATR(14) 31.17 (2.7% of price) | annualised 20d 18.1%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.04T
Valuation: trailing P/E 39.34 | forward P/E 24.61 | P/B 30.79 | PEG 1.14
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
Price target: mean 1,328.83 (+13.6% vs last close), range 930.00 - 1,600.00
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

- [Microsoft Corporation (MSFT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/MSFT/)  
  <sub>Yahoo! Finance Canada, 10 hours ago</sub>  
  575,016.89% · Previous Close 516.17 · Open 505.42 · Bid 503.25 x 100 · Ask 530.00 x 8500 · Day's Range 502.22 - 513.33 · 52 Week Range 349.20 - 553.72 · Volume...
- [Microsoft Stock Has Multiple Engines Driving Its Next Leg Higher](https://247wallst.com/investing/2026/09/29/microsoft-stock-has-multiple-engines-driving-its-next-leg-higher/)  
  <sub>24/7 Wall St., 41 minutes ago</sub>  
  Azure is accelerating past 40% growth, Copilot seats are doubling quarter over quarter, and a commercial backlog approaching $700 billion sits waiting to...
- [Microsoft: Still Great Business, But AI Raises Serious Questions (NASDAQ:MSFT)](https://seekingalpha.com/article/4950617-microsoft-still-great-business-but-ai-raises-serious-questions)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Microsoft is a Hold as current valuation demands extremely high growth rates, with AI revenue still a small fraction of total sales. Read more on MSFT...
- [Analysts Offer Insights on Technology Companies: Marvell (MRVL) and Microsoft (MSFT)](https://www.theglobeandmail.com/investing/markets/stocks/MSFT/pressreleases/4850789/analysts-offer-insights-on-technology-companies-marvell-mrvl-and-microsoft-msft/)  
  <sub>The Globe and Mail, 3 hours ago</sub>  
  Detailed price information for Microsoft Corp (MSFT-Q) from The Globe and Mail including charting and trades.
- [Should Copilot Relaunch Require Action From Microsoft (MSFT) Investors?](https://simplywall.st/stocks/us/software/nasdaq-msft/microsoft/news/should-copilot-relaunch-require-action-from-microsoft-msft-i/amp)  
  <sub>Simply Wall Street, 7 hours ago</sub>  
  Microsoft has relaunched and expanded its Copilot platform into a unified workspace that blends Office apps, coding tools, and autonomous agents under a mix...
- [MSFT Stock Gains 3% — Microsoft Unveils AI Cybersecurity Model To Combat Real-Time Threats](https://stocktwits.com/news-articles/markets/equity/microsoft-unveils-ai-cybersecurity-model-to-combat-real-time-threats/cZZxqM3R76s)  
  <sub>Stocktwits, 18 hours ago</sub>  
  MSFT Stock: Retail View. Retail sentiment on Stocktwits was 'bearish' with 'low' message volumes. Retail traders were now focusing attention on the company's...
- [Why Is Microsoft (NASDAQ:MSFT) Suddenly a Must-Watch Bluechip Stocks Stock Today?](https://kalkinemedia.com/us/stocks/bluechip/why-is-microsoft-nasdaqmsft-suddenly-a-must-watch-bluechip-stocks-stock-today)  
  <sub>Kalkine Media, 2 hours ago</sub>  
  Microsoft (NASDAQ:MSFT) enters today's market discussion as sector themes, operations, and broader conditions draw attention.
- [(MSFT) Risk Channels and Responsive Allocation](https://news.stocktradersdaily.com/news_release/139/MSFT_Risk_Channels_and_Responsive_Allocation_092926021603_1790662563.html)  
  <sub>Stock Traders Daily, 12 hours ago</sub>  
  Price-action only: Microsoft Corporation (MSFT) movements set the tone for institutional models. (MSFT) Risk Channels and Responsive Allocation.
- [Microsoft Corporation (MSFT) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/MSFT/)  
  <sub>Yahoo Finance Singapore, 24 hours ago</sub>  
  575,016.89% · Previous close 516.17 · Open 505.42 · Bid 503.25 x 100 · Ask 530.00 x 8500 · Day's range 502.22 - 513.33 · 52-week range 349.20 - 553.72 · Volume...
- [Microsoft is Edging Into Overvalued Territory Now](https://247wallst.com/investing/2026/09/29/microsoft-is-edging-into-overvalued-territory-now/?tpid=1669930&tv=link&tc=in_content)  
  <sub>24/7 Wall St., 4 hours ago</sub>  
  Azure is growing at 43% and Microsoft just closed at its highest price of the year, yet the cash flow math behind that rally raises a question the stock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 512.56 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 500.09 (+2.5%), 50d 480.32 (+6.7%), 200d 432.32 (+18.6%); 50d above 200d
Momentum: RSI(14) 60.1 | MACD 7.308 vs signal 7.410 (histogram -0.102)
Returns: 1d +0.7% | 5d +2.9% | 1m -0.2% | 3m +37.4%
52-week range: 352.83 - 542.07 (now 84.4% of the way up)
Volatility: ATR(14) 11.88 (2.3% of price) | annualised 20d 24.7%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.81T
Valuation: trailing P/E 28.54 | forward P/E 21.65 | P/B 8.61 | PEG 1.62
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
Price target: mean 577.26 (+12.6% vs last close), range 440.00 - 870.00
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

- [NVIDIA Corporation (NVDA) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/NVDA/)  
  <sub>Yahoo! Finance Canada, 8 hours ago</sub>  
  523,008.59% · Previous Close 225.07 · Open 229.70 · Bid 218.18 x 100 · Ask 228.94 x 700 · Day's Range 228.04 - 233.21 · 52 Week Range 164.27 - 236.54 · Volume...
- [Nvidia's record buyback shows chipmaker's stock is too cheap for CEO Huang to resist](https://www.cnbc.com/2026/09/29/nvidia-buyback-shows-chipmaker-stock-is-too-cheap-for-huang-to-resist.html)  
  <sub>CNBC, 4 hours ago</sub>  
  Nvidia is bolstering its stock buyback program to historic levels at a time when it's earnings multiple is cheap compared to its peers.
- [What Could Push NVDA Stock Higher From Here?](https://www.trefis.com/data/companies/NVDA/no-login-required/8xb1AIGS/What-Could-Push-NVDA-Stock-Higher-From-Here-)  
  <sub>Trefis, 4 hours ago</sub>  
  At $228.86, NVIDIA (NVDA) looks set up for roughly 57% of upside over the next three years under a conservative scenario. That is a move large enough to...
- [Nvidia Stock Is at Its Cheapest Valuation Since 2015](https://247wallst.com/investing/2026/09/29/nvidia-stock-is-at-its-cheapest-valuation-since-2015/)  
  <sub>24/7 Wall St., 56 minutes ago</sub>  
  NVDA trades at 17x forward earnings, its cheapest since 2015 and well below its 30x historical average, yet the stock sits near its 52-week high.
- [NVIDIA Announces a $150 Billion Share Repurchase Authorization Increase](https://nvidianews.nvidia.com/news/nvidia-announces-a-150-billion-share-repurchase-authorization-increase)  
  <sub>NVIDIA Newsroom, 22 hours ago</sub>  
  NVIDIA today announced that its Board of Directors has authorized an additional $150 billion under the company's existing share repurchase program,...
- [NVIDIA Just Strengthened the Case for Its Massive Stock Price Upside](https://www.marketbeat.com/articles/nvda-new-but-back-plan-ups-investors-potential/)  
  <sub>MarketBeat, 53 minutes ago</sub>  
  NVIDIA NASDAQ: NVDA strengthened the case for massive share price upside by announcing a record-breaking $150 billion share buyback authorization.
- [What's Going On With NVIDIA Stock Tuesday? - NVIDIA (NASDAQ:NVDA)](https://www.benzinga.com/markets/tech/26/09/62043155/nvidia-explores-insurance-shield-for-chip-backed-loans-as-ai-financing-push-expands)  
  <sub>Benzinga, 5 hours ago</sub>  
  NVIDIA Corp. (NASDAQ:NVDA) stock traded higher by almost 1% during Tuesday's premarket session as traders lean into a steady risk tone for mega-cap tech.
- [NVDA Stock Eyes Worst First Half Since 2022: Retail Patience Wears Thin As Board Member Trims Stake For Third Time This Year](https://stocktwits.com/news-articles/markets/equity/nvda-stock-eyes-worst-first-half-since-2022-retail-patience-wears-thin-as-board-member-trims-stake-for-third-time-this-year/cZ1QIRnR7ie)  
  <sub>Stocktwits, 10 hours ago</sub>  
  NVDA Stock Eyes Worst First Half Since 2022: Retail Patience Wears Thin As Board Member Trims Stake For Third Time This Year. Nvidia shares are up a mere 4.7%...
- [NVIDIA's Stock Gains 1.7% as It Unveils Historic Buyback](https://www.tradingview.com/news/zacks:2c3b0e3c5094b:0-nvidia-s-stock-gains-1-7-as-it-unveils-historic-buyback/)  
  <sub>TradingView, 4 hours ago</sub>  
  NVIDIA Corporation NVDA has announced a massive expansion of its share repurchase program on Sept. 28, authorizing an additional $150 billion for stock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 230.86 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 222.82 (+3.6%), 50d 217.05 (+6.4%), 200d 199.93 (+15.5%); 50d above 200d
Momentum: RSI(14) 60.4 | MACD 2.966 vs signal 2.234 (histogram 0.732)
Returns: 1d +0.9% | 5d +0.9% | 1m +6.1% | 3m +15.4%
52-week range: 165.17 - 235.74 (now 93.1% of the way up)
Volatility: ATR(14) 5.89 (2.5% of price) | annualised 20d 27.8%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 5.57T
Valuation: trailing P/E 29.15 | forward P/E 14.72 | P/B 24.34 | PEG 0.48
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
  - 2026-09-29 Rosenblatt: main, Buy -> Buy
  - 2026-09-10 Piper Sandler: init, ? -> Overweight
  - 2026-09-04 Rosenblatt: main, Buy -> Buy
  - 2026-09-04 Needham: reit, Buy -> Buy
  - 2026-08-27 Citigroup: main, Buy -> Buy
  - 2026-08-27 Mizuho: main, Outperform -> Outperform
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

- [Novo vs. Pfizer: Which Large Drugmaker Offers Better Growth Prospects?](https://finance.yahoo.com/healthcare/articles/novo-vs-pfizer-large-drugmaker-131400444.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Novo NVO and Pfizer PFE are both pharmaceutical giants based in Denmark and the United States, respectively, with broad portfolios spanning major...
- [Novo says Ozempic outperforms Lilly’s Mounjaro in cutting major cardiovascular events](https://seekingalpha.com/news/4647907-novo-says-ozempic-2-mg-cut-major-cardiovascular-events-compared-with-lillys-mounjaro)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Novo Nordisk (NVO) says Ozempic 2 mg cut stroke and major CV event risk versus Lilly's (LLY) Mounjaro in an analysis of real-world claims data.
- [CRM Stock Snags Second Rating Downgrade This Month – Analyst Says Risk/Reward On Salesforce Balanced In Absence Of Notable Growth Inflection](https://stocktwits.com/news-articles/markets/equity/crm-stock-snags-second-rating-downgrade-this-month-analyst-says-risk-reward-on-salesforce-balanced-in-absence-of-notable-growth-inflection/cZZSaJ1R7vI)  
  <sub>Stocktwits, 12 hours ago</sub>  
  Shares of Salesforce (CRM) edged lower in Tuesday's premarket trade after Morgan Stanley moved away from its bullish stance on the business software company...
- [Nasdaq Futures Tread Water After Monday Rout: MU, NVTS, NVO, KOD, SMMT, ASTS Stocks In Focus](https://finance.yahoo.com/markets/stocks/articles/nasdaq-futures-tread-water-monday-083136345.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  President Trump and Speaker Mike Johnson are hosting key AI leaders, including Jensen Huang, Dario Amodei, and Alex Karp in Washington.
- [BMO reiterates Novo Nordisk stock rating on Hengrui licensing deal By Investing.com](https://ca.investing.com/news/stock-market-news/bmo-reiterates-novo-nordisk-stock-rating-on-hengrui-licensing-deal-93CH-4858320)  
  <sub>Investing.com Canada, 17 minutes ago</sub>  
  Investing.com - BMO Capital reiterated a Market Perform rating on Novo Nordisk (NYSE:NVO) with a $47.00 price target following the company's licensing...
- [Novo Nordisk Stock Analysis: Bearish Trend Meets Oversold Bounce](https://en.cryptonomist.ch/2026/09/29/novo-nordisk-stock-is-oversold-but-is-the-70-collapse-from-its-peak-over/)  
  <sub>The Cryptonomist, 4 hours ago</sub>  
  Discover a detailed Novo Nordisk stock analysis showing bearish trends and oversold conditions with key support and resistance levels for informed trading.
- [A DKK 15 billion buyback plan is underway at Novo Nordisk (NVO), with shares already repurchased.](https://www.stocktitan.net/sec-filings/NVO/6-k-novo-nordisk-a-s-current-report-foreign-issuer-1eb24c9b633c.html)  
  <sub>Stock Titan, 23 hours ago</sub>  
  Under the programme begun in May, Novo Nordisk repurchased 20.62 million B shares for DKK 6.14 billion. It now holds 1.1% of its share capital as treasury...
- [Novo Nordisk strikes $2.6B obesity drug deal with China's Hengrui (NVO:NYSE)](https://seekingalpha.com/news/4647845-novo-nordisk-strikes-26b-obesity-drug-deal-with-chinas-hengrui)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  Jiangsu Hengrui Pharmaceuticals (JHPCY) has agreed to license global rights to its experimental obesity drug HRS-1596 to Novo Nordisk (NVO) in a deal worth...
- [Novo Resources stock falls 6.67 percent as drilling plans expand](https://www.ad-hoc-news.de/boerse/news/nebenwerte/novo-resources-stock-falls-6-67-percent-as-drilling-plans-expand/70197038)  
  <sub>AD HOC NEWS, 6 hours ago</sub>  
  NVO, CA6529281069. Novo Resources stock falls 6.67 percent as drilling plans expand. Published on 09/29/2026 at 10:28 | Editorial responsibility: Rafael...
- [SLS Stock In Spotlight After Vanguard Capital Discloses 5.19% Stake – Retail Calls It ‘Huge Vote Of Conviction’ As AML Trial Readout Nears](https://stocktwits.com/news-articles/markets/equity/sls-stock-in-spotlight-after-vanguard-capital-discloses-beneficial-stake/cZN4WEaRJPY)  
  <sub>Stocktwits, 16 hours ago</sub>  
  A new Schedule 13G filing showed Vanguard Capital Management owned 9.67 million SLS shares as of June 30, 2026.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 38.20 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 42.43 (-10.0%), 50d 45.34 (-15.7%), 200d 45.84 (-16.7%); 50d below 200d
Momentum: RSI(14) 29.4 | MACD -2.107 vs signal -1.719 (histogram -0.388)
Returns: 1d -1.3% | 5d -3.0% | 1m -16.2% | 3m -20.3%
52-week range: 35.29 - 63.98 (now 10.1% of the way up)
Volatility: ATR(14) 1.17 (3.1% of price) | annualised 20d 40.3%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 168.68B
Valuation: trailing P/E 9.57 | forward P/E 11.38 | P/B 4.95 | PEG 4.32
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
Price target: mean 46.19 (+20.9% vs last close), range 39.56 - 62.60
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

- [Procter & Gamble (PG) Stock May Be 24% Undervalued After Q1 Sales Slip](https://simplywall.st/stocks/us/household/nyse-pg/procter-gamble/news/procter-gamble-pg-stock-may-be-24-undervalued-after-q1-sales)  
  <sub>Simply Wall Street, 4 hours ago</sub>  
  Procter & Gamble has delivered a 22.1% total return over the past 5 years, which puts fresh focus on whether the current share price around US$149 is...
- [EPR Properties (EPR-PG) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/EPR-PG/)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  Find the latest EPR Properties (EPR-PG) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Living Off Dividends at 65: 3 Stocks That Raised Payouts for Longer Than 30 Years](https://247wallst.com/investing/2026/09/29/living-off-dividends-at-65-3-stocks-that-raised-payouts-for-longer-than-30-years/)  
  <sub>24/7 Wall St., 3 hours ago</sub>  
  For a 65-year-old investor who is planning to live on portfolio income rather than trade around it, an unbroken record of annual dividend increases matters...
- [Is Procter & Gamble (NYSE:PG) the Bluechip Stocks Stock Everyone's Talking About Today?](https://kalkinemedia.com/us/stocks/bluechip/is-procter-gamble-nysepg-the-bluechip-stocks-stock-everyones-talking-about-today)  
  <sub>Kalkine Media, 2 hours ago</sub>  
  Procter & Gamble (NYSE:PG) enters today's market discussion as sector themes, operations, and broader conditions draw attention.
- [The Stock Market Just Flashed a Warning Signal Seen Only a Handful of Times in 150 Years. Here's Where I'd Put Money Right Now.](https://www.fool.com/investing/2026/09/29/the-stock-market-just-flashed-a-warning-signal-seen-only-a-handful-of-times-in-150-years-here-s-where-i-d-put-money-right-now/)  
  <sub>The Motley Fool, 4 hours ago</sub>  
  The Shiller CAPE ratio -- a metric that shows how expensive stocks are relative to a decade of earnings -- recently hit its second-highest level on record...
- [How (PG) Movements Inform Risk Allocation Models](https://news.stocktradersdaily.com/news_release/16/How_PG_Movements_Inform_Risk_Allocation_Models_092926024202_1790664122.html)  
  <sub>Stock Traders Daily, 12 hours ago</sub>  
  Key findings for Procter & Gamble Company (the) (NYSE: PG). Full Alignment in Neutral Sentiment Favors Wait-and-See Approach; A mid-channel oscillation...
- [Top dow jones movers in Monday's session](https://www.chartmill.com/news/SHW/Chartmill-55462-Top-dow-jones-movers-in-Mondays-session)  
  <sub>ChartMill, 20 hours ago</sub>  
  Curious about the dow jones stocks that are in motion on Monday? Join us as we explore the top movers within the dow jones index during today's session.
- [Procter & Gamble (PG) Advances While Market Declines: Some Information for Investors](https://finance.yahoo.com/markets/stocks/articles/procter-gamble-pg-advances-while-205003197.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Procter & Gamble (PG) closed the most recent trading day at $148.95, moving +1.86% from the previous trading session. The stock outpaced the S&P 500's daily...
- [PG&E Corp. stock underperforms Monday when compared to competitors](https://www.marketwatch.com/data-news/pg-e-corp-stock-underperforms-monday-when-compared-to-competitors-3f8044ff-82430aac7f10?mod=mw_quote_news)  
  <sub>MarketWatch, 18 hours ago</sub>  
  Shares of PG&E Corp. PCG. +0.16%. slipped 3.16% to $11.95 Monday, on what proved to be an all-around dismal trading session for the stock market,...
- [PG&E Corporation stock trades flat as review reshapes plans](https://www.ad-hoc-news.de/boerse/news/corporate-news/pg-and-e-corporation-stock-trades-flat-as-review-reshapes-plans/70198511)  
  <sub>AD HOC NEWS, 2 hours ago</sub>  
  PG&E Corporation stock stood at EUR 10.55 at Lang & Schwarz on September 29, 2026. PG&E reaffirmed USD 1.64-1.66 core EPS guidance and will defer USD 2.0...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 147.93 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 146.40 (+1.0%), 50d 145.93 (+1.4%), 200d 147.62 (+0.2%); 50d below 200d
Momentum: RSI(14) 54.9 | MACD 0.548 vs signal 0.321 (histogram 0.227)
Returns: 1d -0.7% | 5d -0.2% | 1m +2.9% | 3m +0.9%
52-week range: 138.04 - 167.20 (now 33.9% of the way up)
Volatility: ATR(14) 2.37 (1.6% of price) | annualised 20d 15.5%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 343.85B
Valuation: trailing P/E 22.35 | forward P/E 19.99 | P/B 6.45 | PEG 3.79
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
Price target: mean 160.61 (+8.6% vs last close), range 143.00 - 186.00
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

- [Royal Bank Of Canada (NYSE:RY) Stock Has Consensus Price Target of $225.00 According to Brokerages](https://www.marketbeat.com/instant-alerts/consensus-royal-bank-of-canada-nyse-ry-stock-has-consensus-price-target-of-22500-according-to-brokerages-2026-09-29/)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Royal Bank Of Canada (NYSE:RY - Get Free Report) (TSE:RY) has received a consensus recommendation of "Moderate Buy" from the thirteen analysts that are...
- [How Investors Are Reacting To Royal Bank of Canada (TSX:RY) Balancing New Debt Issuance With Dividend Hike](https://finance.yahoo.com/markets/stocks/articles/investors-reacting-royal-bank-canada-210924007.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Royal Bank of Canada recently completed several fixed-income deals, including CA$1.50 billion in fixed-to-floating subordinated NVCC notes due 2036 and...
- [RBC Global Asset Management Inc. announces September 2026 cash distributions for ETF Series of RBC Funds](https://www.tradingview.com/news/prnewswire:a43680e41b330:0-rbc-global-asset-management-inc-announces-september-2026-cash-distributions-for-etf-series-of-rbc-funds/)  
  <sub>TradingView, 3 hours ago</sub>  
  TORONTO, Sept. 29, 2026 /CNW/ -- RBC Global Asset Management Inc. ("RBC GAM Inc.") today announced September 2026 cash distributions for unitholders of ETF...
- [Barlow’s Research Roundup: ‘Supercycle’ ahead for Canadian bank stocks, says BofA analyst](https://www.theglobeandmail.com/investing/markets/inside-the-market/article-barlows-research-roundup-supercycle-ahead-for-canadian-bank-stocks/)  
  <sub>The Globe and Mail, 2 hours ago</sub>  
  Daily roundup of research and analysis from The Globe and Mail's market strategist Scott Barlow. Bank Supercycle. BofA Securities analyst Ebrahim Poonawala...
- [Royal Bank of Canada stock follows record Q3 earnings](https://www.ad-hoc-news.de/boerse/news/corporate-news/royal-bank-of-canada-stock-follows-record-q3-earnings/70196620)  
  <sub>AD HOC NEWS, 8 hours ago</sub>  
  Royal Bank of Canada stock was last at CAD 285.07 on September 29, 2026, after Q3 adjusted EPS reached CAD 4.28. Analysts set a CAD 292.86 average target.
- [How Much Would You Need to Feel Free to Work Less?](https://ca.finance.yahoo.com/news/much-feel-free-less-201000834.html)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Written by Amy Legate-Wolfe at The Motley Fool Canada. Financial freedom doesn't have to mean retiring at 45 and never answering another email.
- [Why Is Royal Bank of Canada (TSX:RY) in Canadian Banking Focus?](https://kalkinemedia.com/ca/stocks/financial/why-is-royal-bank-of-canada-tsxry-in-canadian-banking-focus)  
  <sub>Kalkine Media, 4 hours ago</sub>  
  Royal Bank of Canada operates across financial services and remains part of the S&P/TSX 60 amid regulatory capital and dividend activity.
- [RBC Appoints Director to Head Quantum Technologies Strategy](https://www.marketscreener.com/news/rbc-appoints-director-to-head-quantum-technologies-strategy-ce785adcd18cf727)  
  <sub>marketscreener.com, 22 hours ago</sub>  
  Royal Bank of Canada has appointed Elizabeth Iwasawa as director of Quantum, a newly-created role, the company said on Monday. Iwasawa, who was previously...
- [Canadian Imperial Bank of Commerce (CM.TO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/CM.TO/)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Find the latest Canadian Imperial Bank of Commerce (CM.TO) stock quote, history, news and other vital information to help you with your stock trading and...
- [Royal Bank of Canada stock at CAD 285.07 on September 28, 2026](https://www.ad-hoc-news.de/boerse/news/nachboerse/royal-bank-of-canada-stock-at-cad-285-07-on-september-28-2026/70195506)  
  <sub>AD HOC NEWS, 18 hours ago</sub>  
  Royal Bank of Canada stock last traded at CAD 285.07 on the TSX on September 28, 2026, down 0.20 percent. The bank announced two capital offerings with...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 199.62 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 204.59 (-2.4%), 50d 207.54 (-3.8%), 200d 185.95 (+7.4%); 50d above 200d
Momentum: RSI(14) 38.9 | MACD -1.988 vs signal -1.575 (histogram -0.414)
Returns: 1d -0.7% | 5d -2.1% | 1m -2.3% | 3m -3.5%
52-week range: 143.64 - 217.87 (now 75.4% of the way up)
Volatility: ATR(14) 3.04 (1.5% of price) | annualised 20d 17.4%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 276.37B
Valuation: trailing P/E 17.81 | forward P/E 15.81 | P/B 2.91 | PEG 2.26
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
Price target: mean 208.20 (+4.3% vs last close), range 183.40 - 225.68
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

- [Teva Pharmaceutical Industries Limited (TEVA) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TEVA/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Teva Pharmaceutical Industries Limited (TEVA) · -1.62% · 6.70% · 35.28% · 24.58% · 102.71% · 289.97% · 4,190.21%. Key Events. Baseline. Advanced Chart. Loading...
- [Teva Pharmaceutical: 3 Numbers That Explain This Generic-Drug Turnaround](https://www.fool.com/investing/2026/09/29/teva-pharmaceutical-numbers-explain-turnaround/)  
  <sub>The Motley Fool, 5 hours ago</sub>  
  Teva Pharmaceuticals (TEVA -0.79%) recently hit a new 52-week high of $40.79 per share and has surged 110% in the last year. It's the drugmaker's turnaround...
- [Teva's Branded Drugs Take Center Stage in Its Growth Strategy](https://www.tradingview.com/news/zacks:ff08146d3094b:0-teva-s-branded-drugs-take-center-stage-in-its-growth-strategy/)  
  <sub>TradingView, 3 hours ago</sub>  
  Teva Pharmaceutical Industries Limited's TEVA business was heavily dependent on generic medicines for decades. That model provided scale but also exposed...
- [FDA approves a medicine to help prevent bone complications in adults whose cancer has spread to bone](https://www.stocktitan.net/news/TEVA/teva-continues-biosimilar-momentum-with-u-s-fda-approval-of-vy3dtaqd96l3.html)  
  <sub>Stock Titan, 19 hours ago</sub>  
  DEGEVMA is Teva's second FDA-approved similar medicine in 2026. With PONLIMSI, the pair spans Xgeva and Prolia uses; U.S. launches are expected in coming...
- [Teva Pharmaceutical Industries Gains FDA Nod for Degevma Biosimi](https://www.gurufocus.com/news/9100393/teva-pharmaceutical-industries-gains-fda-nod-for-degevma-biosimilar-ticker-teva)  
  <sub>GuruFocus, 17 hours ago</sub>  
  On September 28, 2026, Teva Pharmaceutical Industries Ltd (NYSE: TEVA) announced FDA approval for Degevma, a new biosimilar to Xgeva designed to prevent...
- [Teva Pharmaceutical Industries Limited (TEVA) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/TEVA/)  
  <sub>Yahoo Finance UK, 16 hours ago</sub>  
  Teva Pharmaceutical Industries Limited (TEVA) · -2.95% · 6.70% · 35.28% · 24.58% · 112.00% · 305.00% · 4,190.21%. Key events. Baseline. Advanced chart. Loading...
- [(TEVA) Price Dynamics and Execution-Aware Positioning](https://news.stocktradersdaily.com/news_release/132/TEVA_Price_Dynamics_and_Execution-Aware_Positioning_092826092403_1790645043.html)  
  <sub>Stock Traders Daily, 17 hours ago</sub>  
  Price-action only: Teva Pharmaceutical Industries Limited American Depositary Shares (TEVA) movements set the tone for institutional models.
- [Teva Pharmaceutical Industries Limited (TEVA) latest stock news and headlines](https://uk.finance.yahoo.com/quote/TEVA/news/)  
  <sub>Yahoo Finance UK, 17 hours ago</sub>  
  Teva Pharmaceutical Industries Limited (TEVA).

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 38.86 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 38.21 (+1.7%), 50d 36.39 (+6.8%), 200d 33.53 (+15.9%); 50d above 200d
Momentum: RSI(14) 55.4 | MACD 0.822 vs signal 0.874 (histogram -0.052)
Returns: 1d -0.1% | 5d -1.7% | 1m +6.6% | 3m +14.7%
52-week range: 18.95 - 40.22 (now 93.6% of the way up)
Volatility: ATR(14) 1.18 (3.0% of price) | annualised 20d 32.3%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 45.32B
Valuation: trailing P/E 64.77 | forward P/E 12.77 | P/B 5.84 | PEG n/a
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
Price target: mean 44.00 (+13.2% vs last close), range 40.00 - 50.00
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

- [Can ExxonMobil Holdings (XOM) Stay Cheap With Cash Flow Growing?](https://finance.yahoo.com/markets/stocks/articles/exxonmobil-holdings-xom-stay-cheap-042708728.html)  
  <sub>Yahoo Finance, 10 hours ago</sub>  
  ExxonMobil Holdings has ridden a powerful multi year run, and with the stock near recent highs the key question is whether the cash the business can...
- [ExxonMobil (NYSE:XOM) Stock Sold by Rep. Kevin Hern](https://www.marketbeat.com/instant-alerts/congress-exxonmobil-nyse-xom-stock-sold-by-rep-kevin-hern-2026-09-29/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Representative Kevin Hern (Republican-Oklahoma) recently sold shares of ExxonMobil Corporation (NYSE:XOM). In a filing disclosed on September 25th,...
- [ExxonMobil Got a $180 Target as Trump Weighed a Diesel Export Ban. Here’s What It Means for the Stock](https://www.tikr.com/blog/exxonmobil-got-a-180-target-as-trump-weighed-a-diesel-export-ban-heres-what-it-means-for-the-stock)  
  <sub>TIKR.com, 12 minutes ago</sub>  
  ExxonMobil's refining arm earned more in the second quarter than in the first half of 2025, and TD Cowen expects another jump in the third quarter.
- [Understanding Momentum Shifts in (XOM)](https://news.stocktradersdaily.com/news_release/150/Understanding_Momentum_Shifts_in_XOM_092926033402_1790667242.html)  
  <sub>Stock Traders Daily, 11 hours ago</sub>  
  Price-action only: Exxon Mobil Corporation (XOM) movements set the tone for institutional models. Understanding Momentum Shifts in (XOM)
- [Imperial Oil: Another Rainy Day Stock (NYSE:IMO)](https://seekingalpha.com/article/4950529-imperial-oil-another-rainy-day-stock)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  As a mature, thermal-focused company, Imperial Oil offers defensible cash flow and dividends. Click here to find out why IMO stock is a Buy.
- [Exxon Mobil Holdings (XOM) Gains As Market Dips: What You Should Know](https://finance.yahoo.com/markets/stocks/articles/exxon-mobil-holdings-xom-gains-204504735.html?.tsrc=rss)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Exxon Mobil Holdings (XOM) closed at $162.53 in the latest trading session, marking a +1.21% move from the prior day. The stock's performance was ahead of...
- [Why Can't Investors Stop Watching Exxon Mobil (NYSE:XOM) Today?](https://kalkinemedia.com/us/stocks/oil-gas/why-cant-investors-stop-watching-exxon-mobil-nysexom-today)  
  <sub>Kalkine Media, 2 hours ago</sub>  
  Highlights. Exxon Mobil is in focus in todays oil and gas stocks discussion. Broader market themes include technology strength, changing yields,...
- [MRNA, LNTH, BMY, CAPR, RARE Stocks In Focus — These FDA Decisions Could Shape August Trading](https://stocktwits.com/news-articles/markets/equity/mrna-lnth-bmy-capr-rare-stocks-in-focus-these-fda-decisions-could-shape-august-trading/cZoTYS7RJ30)  
  <sub>Stocktwits, 11 hours ago</sub>  
  Moderna is seeking approval for mRNA-1010, its experimental mRNA-based seasonal flu vaccine for adults 50 and older.Capricor is seeking full approval for...
- [CVX vs XOM: valuation, momentum, and which side the pairs trade favors](https://www.investing.com/news/stock-market-news/cvx-vs-xom-valuation-momentum-and-which-side-the-pairs-trade-favors-93CH-4920997)  
  <sub>Investing.com, 20 hours ago</sub>  
  Investing.com -- TD's call for a rotation into Exxon Mobil (XOM) over Chevron (CVX) is a momentum call dressed up as a pairs trade — and the data pushes...
- [Imperial Oil benefits from vertical integration amid market skepticism despite strong earnings.](https://pluang.com/en/news-feed/imperial-oil-saham-hari-hujan)  
  <sub>Pluang, 8 hours ago</sub>  
  Imperial Oil, majority-owned by ExxonMobil, leverages vertical integration to avoid thermal oil discounts, supporting stable cash flow and dividends.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 160.70 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 162.76 (-1.3%), 50d 159.98 (+0.5%), 200d 148.42 (+8.3%); 50d above 200d
Momentum: RSI(14) 48.8 | MACD 0.403 vs signal 0.965 (histogram -0.561)
Returns: 1d -1.1% | 5d +1.3% | 1m +2.5% | 3m +17.5%
52-week range: 110.64 - 171.47 (now 82.3% of the way up)
Volatility: ATR(14) 3.63 (2.3% of price) | annualised 20d 26.2%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 660.78B
Valuation: trailing P/E 20.68 | forward P/E 14.44 | P/B 2.55 | PEG 1.38
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
Price target: mean 172.55 (+7.4% vs last close), range 142.00 - 200.00
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

> No material macro surprise, no decisive technical break, flat fund flows, and no analyst coverage. Fundamentals are mixed (decent yield and historical performance but high cash holdings and expense ratio). Overall view remains neutral.

**Main reasons it gave:**
- US Treasury yields rose across the curve (+0.09 to +0.28)
- Dollar index up (+0.79%)
- Price below 20‑day SMA and MACD negative (RSI 43.1)
- Fund flows flat (share count unchanged)

<details><summary><b>News</b> — score +0.00</summary>

- [Invesco DB Agriculture Fund (DBA) Stock Price Today: $28.25](https://pluang.com/en/asset/usstock/DBA/10770)  
  <sub>Pluang, 7 hours ago</sub>  
  Buy and sell Invesco DB Agriculture Fund stock securely on Pluang with real-time prices, live charts, and detailed market trend information.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 28.24 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 28.78 (-1.9%), 50d 28.34 (-0.4%), 200d 27.11 (+4.1%); 50d above 200d
Momentum: RSI(14) 43.1 | MACD -0.022 vs signal 0.079 (histogram -0.101)
Returns: 1d -0.1% | 5d -1.1% | 1m -3.3% | 3m +5.9%
52-week range: 25.44 - 29.49 (now 69.0% of the way up)
Volatility: ATR(14) 0.28 (1.0% of price) | annualised 20d 13.2%
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
Shares outstanding: 27.60M | fund size: 779.29M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- US Treasury yields rose modestly across the curve (+0.09 to 3‑month, +0.28 to 10‑year) indicating no macro surprise
- Energy inventories showed builds in crude (+3.0 MMb, 58th percentile) and natural gas (+53 Bcf, 73rd percentile), bearish for energy prices
- EIA forecast projects WTI price decline to $79 in six months, but fund's oil exposure is modest (8.9% of holdings)
- Technical indicators are neutral: price below 20‑day SMA (-1.6%), RSI 50.4, MACD negative, with low volume
- Fund flows flat (share count unchanged at +0.0% over 1 week) indicating no net demand shift

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 32.17 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 32.70 (-1.6%), 50d 31.04 (+3.6%), 200d 28.03 (+14.8%); 50d above 200d
Momentum: RSI(14) 50.4 | MACD 0.451 vs signal 0.640 (histogram -0.189)
Returns: 1d -1.0% | 5d -0.8% | 1m +4.5% | 3m +20.6%
52-week range: 22.07 - 33.68 (now 87.0% of the way up)
Volatility: ATR(14) 0.50 (1.5% of price) | annualised 20d 19.5%
Volume: 0.20x the 20-day average
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
Three-year record: +14.0% a year | beta to the market 1.05
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
US inventories, week ending 2026-09-18 (published the following Wednesday)
  Crude oil: 426.4 million barrels, +3.0 on the week (a build), 58% percentile over 52 weeks
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
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 111.40M | fund size: 3.58B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Rising Treasury yields and low credit quality weigh on the fund, but flat flows and no clear macro surprise keep the outlook neutral.

**Main reasons it gave:**
- 10-year Treasury yield rose 0.28% on the week, pressuring high-yield bonds
- Fund credit quality is low (57.9% BB, 32.2% B, 8.3% below B)
- Technical trend is bearish: price below 20‑day, 50‑day, and 200‑day SMAs
- Fund flows flat over the past week (0% net change)

<details><summary><b>News</b> — score +0.00</summary>

- [Higher rates are wreaking havoc on these two ETFs. Traders see one bouncing back](https://www.cnbc.com/amp/2026/09/29/higher-rates-are-wreaking-havoc-on-these-two-etfs-traders-see-one-bouncing-back.html)  
  <sub>CNBC, 3 hours ago</sub>  
  The relentless surge in rates is breaking the back of two key macro trades that had been holding firm.
- [Junk bonds are heading for worst month since 2022 after punishing global selloff](https://www.marketwatch.com/story/junk-bonds-are-heading-for-worst-month-since-2022-after-punishing-global-selloff-12b70a3e)  
  <sub>MarketWatch, 54 minutes ago</sub>  
  U.S. junk bonds are getting badly bruised in September, with their high yields so far failing to provide enough cushion this month to withstand heightened...
- [Gold drops 4% amid rising yields; traders bulli...](https://pluang.com/en/news-feed/tingginya-suku-bunga-berdampak-pada-etf-hyg-dan-gld-pedagang-optimis-salah-satu)  
  <sub>Pluang, 3 hours ago</sub>  
  Gold prices fell 4% to their lowest since early August as 10-year and 30-year Treasury yields rose above 5.3% and 5.4%, respectively.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 77.36 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 78.53 (-1.5%), 50d 79.15 (-2.3%), 200d 79.94 (-3.2%); 50d below 200d
Momentum: RSI(14) 21.1 | MACD -0.456 vs signal -0.343 (histogram -0.113)
Returns: 1d -0.2% | 5d -1.7% | 1m -3.0% | 3m -3.3%
52-week range: 77.36 - 81.28 (now 0.0% of the way up)
Volatility: ATR(14) 0.27 (0.3% of price) | annualised 20d 4.7%
Volume: 0.63x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.30</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 195.60M | fund size: 15.13B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, technicals show no decisive break, positioning is ambiguous, analyst coverage is thin despite bullish rating.

**Main reasons it gave:**
- US Treasury yields rose across the curve (+0.09 to +0.28) with no policy surprise
- IWM price below 20‑day (287.06) and 50‑day (293.45) SMAs, RSI 30.7, no decisive breakout on volume
- CFTC shows net short 26% of open interest, short reduced by 6.4% week, crowded short (5% percentile) – ambiguous
- Analyst coverage thin (1.7% of fund) despite 100% buy rating and +24% price target

<details><summary><b>News</b> — score +0.00</summary>

- [2026-09-28 ETF Investment Daily - High Interest Rates Weigh on Valuations; Small-Cap Real Estate Under Pressure; Energy Premium Diverges](https://www.moomoo.com/community/feed/2026-09-28-etf-investment-daily-report-high-interest-rates-117349683101701)  
  <sub>Moomoo, 22 hours ago</sub>  
  Share Link: Daily Morning Brief · Macro ETF Radar] Looking back at Friday after the weekend market closure, SPY rose 0.54%, up 1.27% over the past fi...
- [Exchange-Traded Funds Lower as US Equities Decline After Midday](https://finance.yahoo.com/markets/articles/exchange-traded-funds-lower-us-172613363.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV fell. Actively traded Invesco QQQ Trust (QQQ) shed 1%.
- [Behavioral Patterns of IWM and Institutional Flows](https://www.google.com/goto?url=CAESuwEB6zswFZxPMWhT2hxPLBKYhxFbUIZhILJzW4PVzBko2N8VFhL9DpBl-VyZlwObMo2trGo85mw7cXiaxCPczdrEpPYvM6XXBY1XfnzW_4cZrtgIM9MLeBYuN9Hd-1laACtvf8bfbhrr9-ilawDHg7eU8hoqb7hofFaSLb-aNWItxLSfcMqckZSaka827BLN_9m5M1VvdTSUJpUrq3s8fXULgE2zc3lOkt6zbioVfRFOjju3_ipoABeiLt99)  
  <sub>Stock Traders Daily, 11 hours ago</sub>  
  Key findings for Ishares Russell 2000 Etf (NYSE: IWM). Weak Near and Mid-Term Sentiment Could Challenge Long-Term Positive Outlook...
- [S&P 500: Why I'm 'Taking 5%' In Treasuries, And Trading The Rest (SPX)](https://www.google.com/goto?url=CAESnQEB6zswFRkJkvHDcqIpic156we4y6jtfB_8oHVqM3qOgan0m4Z2K8enf7gtNN3vZB7XU6DwapIVnF-MIKdecLmmtI41iuDkhLfe8vddbMpJ5GqHy9uaX7-XYXc7VVeTic36viMBtaH8fa7k0jUqe8vck5yOeXFzpeoeZXMaV8D4YDaoTZjno4W63C9GD1gGre9-O7npqQU2fJ2HNV49)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  I am deploying a tactical 'barbell' strategy, pairing hedged fixed income with short-term ETF and options trading to navigate today's risky market.
- [How to Buy Hims & Hers Health Stock (HIMS)](https://www.fool.com/investing/how-to-invest/stocks/how-to-invest-in-hims-and-hers-health-stock/)  
  <sub>The Motley Fool, 19 hours ago</sub>  
  Hims & Hers Health is a newer telemedicine player, but it is rapidly growing revenue and profits from a diverse lineup of services.
- [iShares 20+ Year Treasury Bond ETF (TLT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TLT/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest iShares 20+ Year Treasury Bond ETF (TLT) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 278.71 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 287.06 (-2.9%), 50d 293.45 (-5.0%), 200d 275.94 (+1.0%); 50d above 200d
Momentum: RSI(14) 30.7 | MACD -4.077 vs signal -3.446 (histogram -0.631)
Returns: 1d -0.5% | 5d -3.0% | 1m -5.8% | 3m -7.2%
52-week range: 229.11 - 305.09 (now 65.3% of the way up)
Volatility: ATR(14) 3.41 (1.2% of price) | annualised 20d 12.2%
Volume: 0.24x the 20-day average
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
Weighted price target: +24.0% above the current prices
Holdings read: FROG, MOG-A, XTSLA, UMBF, GKOS
Recent rating changes among them:
  - FROG: 2026-09-04 DA Davidson: main, Buy -> Buy
  - MOG-A: 2026-09-15 Guggenheim: init, ? -> Neutral
  - UMBF: 2026-09-28 Morgan Stanley: main, Overweight -> Overweight
  - GKOS: 2026-09-22 Jefferies: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 26.0% of open interest (415,047 contracts)
Change on the week: -6.4% of open interest
Crowding: 5% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 281.05M | fund size: 78.33B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral

**Main reasons it gave:**
- Fund flows flat (share count +0.0% over 1 week)
- Technicals: RSI 25.6 (oversold) and negative MACD, but no decisive break; volume 0.57x 20‑day average
- Macro: Treasury yields up modestly, no rate surprise; inflation 3.4% and unemployment 4.1% in line with expectations
- Fund basics unchanged: yield 4.7%, credit quality stable, expense ratio 0.14%

<details><summary><b>News</b> — score +0.00</summary>

- [Inside IG Bond ETFs: The Hidden AI Bet](https://etfdb.com/thematic-investing-content-hub/inside-ig-bond-etfs-hidden-ai-bet/)  
  <sub>ETF Database, 39 minutes ago</sub>  
  Retail investors buy corporate bond ETFs expecting steady coupons and ballast against stock market volatility.
- [Bond ETF Options Surge as Yields Hit 20-Year High](https://www.briefs.co/news/options-trading-in-bond-etfs-surges-as-long-term-yields-rise/)  
  <sub>Briefs Finance, 16 hours ago</sub>  
  Options volume in TLT, LQD and HYG spikes as Treasury yields climb, pushing hedging costs and implied volatility to multi-month highs.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 102.38 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 104.46 (-2.0%), 50d 105.60 (-3.0%), 200d 108.54 (-5.7%); 50d below 200d
Momentum: RSI(14) 25.6 | MACD -0.818 vs signal -0.611 (histogram -0.206)
Returns: 1d -0.1% | 5d -2.6% | 1m -3.7% | 3m -6.1%
52-week range: 102.38 - 112.92 (now 0.0% of the way up)
Volatility: ATR(14) 0.59 (0.6% of price) | annualised 20d 7.5%
Volume: 0.57x the 20-day average
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
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 293.50M | fund size: 30.05B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Slightly bearish due to net short positioning, but fundamentals and flows are neutral.

**Main reasons it gave:**
- Large speculators net short 29.8% of open interest, down 0.6% week-over-week
- Crowding at 92% percentile indicates extreme short positioning
- Fund's credit quality AA 100% and expense ratio 0.15% unchanged
- RSI 32.5 and price below 20‑day SMA indicate weak momentum
- 10‑year Treasury yield up 0.28% week, raising rates

<details><summary><b>News</b> — score +0.00</summary>

- [iShares 20+ Year Treasury Bond ETF (TLT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TLT/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest iShares 20+ Year Treasury Bond ETF (TLT) stock quote, history, news and other vital information to help you with your stock trading and...
- [Pantheon Macro highlights higher upside risks but still sees the Fed remaining on hold](https://seekingalpha.com/news/4648009-pantheon-macro-highlights-higher-upside-risks-but-still-sees-the-fed-to-remain-on-hold)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Pantheon Macroeconomics has lifted its near-term projections for both growth and inflation after a run of firmer data. Learn more here.
- [Is Wall Street's Zervos the magic touch Bessent needs to rein in bond rout? (TLT:NASDAQ)](https://seekingalpha.com/news/4647749-is-wall-streets-zervos-the-magic-touch-bessent-needs-to-rein-in-bond-rout)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  Treasury taps economist David Zervos as Mideast conflict, oil spikes and inflation fears push Treasury yields above 5.2%.
- [U.S. 10-year clears 5.25%, but where will it finish in 2026?](https://seekingalpha.com/news/4647725-us-10-year-clears-525-but-where-will-it-finish-in-2026)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  U.S. Treasury yields open the week as a central market focus after the benchmark 10-year note (US10Y) pushed through 5.25%. Learn more information here.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 81.11 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 81.37 (-0.3%), 50d 81.71 (-0.7%), 200d 82.29 (-1.4%); 50d below 200d
Momentum: RSI(14) 32.5 | MACD -0.186 vs signal -0.173 (histogram -0.013)
Returns: 1d +0.0% | 5d -0.3% | 1m -0.9% | 3m -1.2%
52-week range: 81.09 - 83.18 (now 1.2% of the way up)
Volatility: ATR(14) 0.11 (0.1% of price) | annualised 20d 2.1%
Volume: 0.25x the 20-day average
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.25</summary>

```text
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 29.8% of open interest (4,539,374 contracts)
Change on the week: -0.6% of open interest
Crowding: 92% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.25</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 209.30M | fund size: 16.98B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, no decisive technical breakout, mixed analyst and insider signals, fundamentals modestly positive.

**Main reasons it gave:**
- Analyst rating mean 2.11 (bullish) and price target +12.9% above current price
- CFTC speculators net long 6% of open interest, 100% crowding percentile, weekly increase +1.3%
- Fund basics: P/E 17.85, yield 2.8%, three‑year record +18.6% per year
- Technicals: price below 20‑day SMA, RSI 38, no decisive breakout
- Macro: Treasury yields rose across the curve, VIX up to 15.9, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs Investing in Boliden AB Stocks](https://www.tradingview.com/symbols/MUN-BWJ/etfs/)  
  <sub>TradingView, 17 hours ago</sub>  
  Explore funds investing in BWJ in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 87.89 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 89.50 (-1.8%), 50d 90.57 (-3.0%), 200d 87.58 (+0.3%); 50d above 200d
Momentum: RSI(14) 38.0 | MACD -0.782 vs signal -0.645 (histogram -0.137)
Returns: 1d -0.6% | 5d -1.7% | 1m -4.4% | 3m -0.7%
52-week range: 77.90 - 93.19 (now 65.3% of the way up)
Volatility: ATR(14) 0.91 (1.0% of price) | annualised 20d 12.5%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

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
Rolled up from the 5 largest holdings, 11.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 65.7% | hold 34.3% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.9% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, NOVN.SW, SHEL.L
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.15</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 6.0% of open interest (487,063 contracts)
Change on the week: +1.3% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 282.09M | fund size: 24.79B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals show short‑term weakness, analyst coverage thin despite bullish price target, positioning modestly net‑long, fundamentals solid but not a catalyst.

**Main reasons it gave:**
- US Treasury yields rose across the curve (+0.28% on 10‑year) indicating higher rates, which pressures emerging markets
- Dollar index up 0.79% on the week, adding headwinds for EM equities
- VWO price below 20‑day (60.29) and 50‑day (59.88) SMAs, RSI 44.3, MACD negative, showing short‑term weakness
- Analyst coverage thin (22.2% of fund) despite bullish price target +36.8% for top holdings
- CFTC positioning net long modest at 4.6% of open interest, with only a +1.3% weekly increase

<details><summary><b>News</b> — score +0.00</summary>

- [FRDM: Downgrading To Buy After An 85% Run, It Is Now A Memory Fund (BATS:FRDM)](https://seekingalpha.com/article/4950381-frdm-downgrading-to-buy-after-an-85-percent-run-it-is-now-a-memory-fund)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Freedom 100 Emerging Markets ETF is rated a Buy after an 85% rally driven by Korean memory and Taiwanese AI hardware exposure. Read more on FRDM ETF here.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 59.51 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 60.29 (-1.3%), 50d 59.88 (-0.6%), 200d 57.87 (+2.8%); 50d above 200d
Momentum: RSI(14) 44.3 | MACD -0.069 vs signal 0.031 (histogram -0.100)
Returns: 1d -0.3% | 5d -2.6% | 1m -2.1% | 3m -0.3%
52-week range: 52.42 - 61.44 (now 78.6% of the way up)
Volatility: ATR(14) 0.63 (1.1% of price) | annualised 20d 13.9%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

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
Rolled up from the 5 largest holdings, 22.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +36.8% above the current prices
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
Shares outstanding: 1.42B | fund size: 84.39B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 91.39 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 93.30 (-2.1%), 50d 94.29 (-3.1%), 200d 95.54 (-4.4%); 50d below 200d
Momentum: RSI(14) 25.2 | MACD -0.747 vs signal -0.551 (histogram -0.195)
Returns: 1d +0.0% | 5d -2.5% | 1m -3.7% | 3m -5.2%
52-week range: 91.34 - 97.74 (now 0.7% of the way up)
Volatility: ATR(14) 0.48 (0.5% of price) | annualised 20d 7.1%
Volume: 0.34x the 20-day average
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
Share count change: 1 week: +1.4% (204.96M) over 7d
Shares outstanding: 162.15M | fund size: 14.82B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [2026-09-28 ETF Investment Daily - High Interest Rates Weigh on Valuations; Small-Cap Real Estate Under Pressure; Energy Premium Diverges](https://www.moomoo.com/community/feed/2026-09-28-etf-investment-daily-report-high-interest-rates-117349683101701)  
  <sub>Moomoo, 22 hours ago</sub>  
  Share Link: Daily Morning Brief · Macro ETF Radar] Looking back at Friday after the weekend market closure, SPY rose 0.54%, up 1.27% over the past fi...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 89.43 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 91.04 (-1.8%), 50d 92.27 (-3.1%), 200d 94.58 (-5.5%); 50d below 200d
Momentum: RSI(14) 27.2 | MACD -0.788 vs signal -0.655 (histogram -0.133)
Returns: 1d -0.1% | 5d -1.9% | 1m -3.7% | 3m -5.4%
52-week range: 89.43 - 97.99 (now 0.0% of the way up)
Volatility: ATR(14) 0.46 (0.5% of price) | annualised 20d 6.5%
Volume: 0.34x the 20-day average
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
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 146.00M | fund size: 13.06B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Should Goldman Sachs Equal Weight U.S. Large Cap Equity ETF (GSEW) Be on Your Investing Radar?](https://finance.yahoo.com/markets/stocks/articles/goldman-sachs-equal-weight-u-092002712.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Style Box ETF report for GSEW.
- [Michael Burry, Peter Schiff Flag S&P 500 Risk: 5 ETFs to Consider - Invesco QQQ Trust, Series 1 (NASDAQ:Q](https://www.benzinga.com/etfs/broad-u-s-equity-etfs/26/09/62052549/michael-burry-peter-schiff-flag-sp-500-risk-5-etfs-consider)  
  <sub>Benzinga, 14 minutes ago</sub>  
  Michael Burry agrees with Peter Schiff's S&P 500 breadth warning as Treasury yields rise. Five ETFs to consider amid growing Fed hike bets.
- [Forget SPY: Invesco's Fund Gives the Smallest S&P 500 Company the Same Say as the Largest](https://247wallst.com/investing/etf/2026/09/28/forget-spy-invescos-fund-gives-the-smallest-sp-500-company-the-same-say-as-the-largest/)  
  <sub>24/7 Wall St., 17 hours ago</sub>  
  SPY hands most of your money to a handful of giants, but one rival fund treats the smallest S&P 500 company as an equal to the largest.
- [Invesco's equal-weight S&P 500 ETF spreads risk evenly, unlike SPY's giant-focused holdings.](https://pluang.com/en/news-feed/invesco-etf-berikan-porsi-setara-perusahaan-terkecil-sp-500)  
  <sub>Pluang, 16 hours ago</sub>  
  Invesco's S&P 500 Equal Weight ETF (RSP) gives the smallest and largest companies in the S&P 500 equal weight, unlike the SPDR S&P 500 ETF (SPY),...
- [Forget SPY: Invesco’s Fund Gives the Smallest S&P 500 Company the Same Say as the Largest](https://www.aol.com/articles/forget-spy-invesco-fund-gives-221141000.html)  
  <sub>AOL.com, 17 hours ago</sub>  
  SPY hands most of your money to a handful of giants, but one rival fund treats the smallest S&P 500 company as an equal to the largest.
- [SA analyst warns that tech stocks could join the market selloff](https://www.tradingview.com/news/seekingalpha:39a6c0e2c094b:0-sa-analyst-warns-that-tech-stocks-could-join-the-market-selloff/)  
  <sub>TradingView, 19 hours ago</sub>  
  Wall Street extended its decline Monday as rising Treasury yields and oil prices kept pressure on equities following President Donald Trump's rejection of...
- [$700 Billion S&P 500 Sell-Off Meets $100 Oil: Are Investors Rotating Into Value ETFs?](https://www.benzinga.com/etfs/broad-u-s-equity-etfs/26/09/62031962/700-billion-sp-500-sell-off-meets-100-oil-are-investors-rotating-into-value-etfs)  
  <sub>Benzinga, 21 hours ago</sub>  
  S&P 500 erases nearly $700 billion as Treasury yields hit 19-year highs and oil nears $100, putting growth, value and energy ETFs in focus.
- [Nvidia Tops $5.4T, Outvalues Russell 2000: Burry’s AI Warning Put ETFs in Focus - Invesco QQQ Trust, Seri](https://www.benzinga.com/etfs/sector-etfs/26/09/62025654/nvidia-tops-5-4t-outvalues-russell-2000-michael-burrys-ai-warning-raises-etf-questions)  
  <sub>Benzinga, 24 hours ago</sub>  
  Nvidia's $5.4T market cap tops the Russell 2000 as Michael Burry questions AI's future, raising fresh concerns over mega-cap concentration in ETFs.
- [Rates and Breadth Are a Problem, but a Fourth-Quarter Turn Is Setting Up](https://pro.thestreet.com/market-commentary/rates-and-breadth-are-a-problem-but-a-fourth-quarter-turn-is-setting-up)  
  <sub>TheStreet Pro, 5 hours ago</sub>  
  Much of the market is already oversold, and the election may trigger a turning point.
- [Symptoms of a Split Market](https://www.brownstoneresearch.com/first-signal/symptoms-of-a-split-market/)  
  <sub>Brownstone Research, 22 hours ago</sub>  
  Indexes look great, your brokerage statement may not.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 209.02 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 213.92 (-2.3%), 50d 216.87 (-3.6%), 200d 205.52 (+1.7%); 50d above 200d
Momentum: RSI(14) 31.3 | MACD -2.203 vs signal -1.729 (histogram -0.474)
Returns: 1d -0.3% | 5d -1.8% | 1m -5.3% | 3m -1.8%
52-week range: 182.18 - 222.77 (now 66.1% of the way up)
Volatility: ATR(14) 1.79 (0.9% of price) | annualised 20d 9.1%
Volume: 0.33x the 20-day average
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
Weighted price target: -2.1% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 155.55M | fund size: 32.51B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [3 Top-Performing Global Fixed Income ETFs](https://global.morningstar.com/en-ca/etfs/3-top-performing-global-fixed-income-etfs)  
  <sub>Morningstar, 22 hours ago</sub>  
  Exchange-traded funds focused on global bonds can be a core part of most investors' portfolios, offering low-cost exposure to the US bond market and other...
- [Tax-Dodging Strategy Used by ETFs on IRS Watchlist, Agency Says](https://www.bloomberg.com/news/articles/2026-09-28/tax-dodging-strategy-used-by-etfs-on-irs-watchlist-agency-says?srnd=phx-money)  
  <sub>Bloomberg, 22 hours ago</sub>  
  A tax avoidance strategy used by some exchange traded funds is on the IRS's radar.
- [(TIPS) Risk-Controlled Trading Report (TIPS:CA)](https://news.stocktradersdaily.com/canada/tips-risk-controlled-trading-report_20260929_009787)  
  <sub>Stock Traders Daily, 11 hours ago</sub>  
  Risk-Controlled Trading Report for BMO US TIPS Index ETF (TIPS) with Key Buy and Sell Indicators.
- [US Needs to Return to 'The Days of Tip O'Neill and Reagan:' Father in Bucks County USA](https://mb.ntd.com/ntdplus/us-needs-to-return-to-the-days-of-tip-oneill-and-reagan-father-in-bucks-county-usa_1175564.html)  
  <sub>NTD News, 11 hours ago</sub>  
  Paul Martino, who appears in the documentary Bucks County, USA, joined NTD's Steve Lance to discuss the film, his daughter, and her best friend,...
- [Treasury Takes Aim at Wall Street Tax Trades in New Notice](https://www.bloomberg.com/news/articles/2026-09-28/treasury-takes-aim-at-wall-street-tax-trades-in-new-notice?srnd=phx-money)  
  <sub>Bloomberg, 21 hours ago</sub>  
  The US Treasury Department took a big step toward curbing a Wall Street boom in investment strategies that help cut tax bills, with a notice signaling...
- [UBS(Lux)Fund Solutions – Bloomberg TIPS 10+ UCITS ETF(USD)A-dis (LSE: UBTL) Stock Price, News & Analysis](https://kalkine.com.au/company/lse-ubtl/)  
  <sub>Kalkine, 15 hours ago</sub>  
  Get the latest UBS(Lux)Fund Solutions – Bloomberg TIPS 10+ UCITS ETF(USD)A-dis (LSE: UBTL) stock price, financials, earnings updates, charts, news,...
- [The 12.49% Yield Junk Bond ETF Lending Money to Companies Banks Won’t Touch](https://247wallst.com/investing/etf/2026/09/29/the-12-49-yield-junk-bond-etf-lending-money-to-companies-banks-wont-touch/)  
  <sub>24/7 Wall St., 5 hours ago</sub>  
  XCCC invests at the riskiest end of the traditional corporate bond market, where investors receive substantially higher yields in exchange for accepting...
- [Soaring Yields Lead Traders to Snap Up Options on BlackRock ETFs](https://www.bloomberg.com/news/articles/2026-09-28/soaring-yields-lead-traders-to-snap-up-options-on-blackrock-etfs?srnd=homepage-americas)  
  <sub>Bloomberg, 19 hours ago</sub>  
  Traders are piling into options tied to fixed-income ETFs at a record pace, in a rush to position portfolios with yields on 10-year and 30-year Treasuries...
- [Is Yatirim Details Market Making Trades in ISMDL ETF](https://www.tipranks.com/news/company-announcements/is-yatirim-details-market-making-trades-in-ismdl-etf)  
  <sub>TipRanks, 21 minutes ago</sub>  
  An announcement from Is Yatirim Menkul Degerler AS ( ($TR:ISMEN) ) is now available. Is Yatirim Menkul Degerler AS disclosed details of its market making...
- [Looking for AI Exposure? 3 Best Vanguard ETFs with 23%+ Upside](https://www.tipranks.com/news/looking-for-ai-exposure-3-best-vanguard-etfs-with-23-upside)  
  <sub>TipRanks, 2 hours ago</sub>  
  AI growth is creating new opportunities in the tech sector. Investors looking to benefit from this trend can use Vanguard ETFs to gain exposure to some of...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 103.97 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 105.73 (-1.7%), 50d 106.65 (-2.5%), 200d 109.43 (-5.0%); 50d below 200d
Momentum: RSI(14) 25.2 | MACD -0.755 vs signal -0.591 (histogram -0.164)
Returns: 1d -0.1% | 5d -1.5% | 1m -2.8% | 3m -5.0%
52-week range: 103.97 - 112.20 (now 0.0% of the way up)
Volatility: ATR(14) 0.40 (0.4% of price) | annualised 20d 4.7%
Volume: 0.20x the 20-day average
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
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 177.70M | fund size: 18.48B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [iShares 20+ Year Treasury Bond ETF (TLT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TLT/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  iShares 20+ Year Treasury Bond ETF (TLT) · -3.89% · -5.14% · -8.20% · -10.52% · -11.56% · -45.44% · -3.83%.
- [TLT ETF Slips As Resurgence In War Risk, Elevated Oil Prices Build Case For Rate Hikes](https://stocktwits.com/news-articles/markets/equity/us-treasury-yield-etfs-drop-as-resurgence-in-war-risk-elevated-oil-prices-build-case-for-rate-hikes/cZmoWmwR7VO)  
  <sub>Stocktwits, 12 hours ago</sub>  
  TLT ETF Slips As Resurgence In War Risk, Elevated Oil Prices Build Case For Rate Hikes · TLT ETF has seen outflows in five out of six months ending June 2026.
- [MOVE Index Tops 100: Bond Volatility Gauge Jumps 35% - iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT)](https://www.benzinga.com/markets/bonds/26/09/62051889/move-index-bond-volatility-vix-september-2026)  
  <sub>Benzinga, 29 minutes ago</sub>  
  The MOVE Index jumped 35% in September, a move seen only 8 times since 2008, while the VIX sits near 16. TLT is down nearly 10% in 2026.
- [Michael Burry Weighs Peter Schiff’s S&P 500 Crash Warning As UBS Flags Fed Risk — Rare October Hike Odds Hit 70%](https://www.tradingview.com/news/stocktwits:e67feb521094b:0-michael-burry-weighs-peter-schiff-s-s-p-500-crash-warning-as-ubs-flags-fed-risk-rare-october-hike-odds-hit-70/)  
  <sub>TradingView, 8 hours ago</sub>  
  The Big Short” investor Michael Burry said that he cannot dismiss economist Peter Schiff's warning about weakness beneath the S&P 500's near-record level,...
- [Bond ETF Options Surge as Yields Hit 20-Year High](https://www.briefs.co/news/options-trading-in-bond-etfs-surges-as-long-term-yields-rise/)  
  <sub>Briefs Finance, 16 hours ago</sub>  
  Options volume in TLT, LQD and HYG spikes as Treasury yields climb, pushing hedging costs and implied volatility to multi-month highs.
- [Bond MFs Lose Billions as Bond ETFs Attract $12B: Doom Loop Risk Grows](https://www.benzinga.com/etfs/specialty-etfs/26/09/62027852/bond-investors-are-fleeing-mutual-funds-for-etfs-why-12b-in-etf-inflows-matters-now)  
  <sub>Benzinga, 23 hours ago</sub>  
  Bond mutual funds lost $6.5B while bond ETFs attracted billions, fueling concerns over a potential fixed-income “doom loop.”
- [Scott Bessent Hires 'Wall Street Geek' David Zervos to Advise Treasury Amid Rising Yields: 'Whether It’s Trade, Whether It’s War, He’s Stepped Up'](https://www.tradingview.com/news/benzinga:39866546e094b:0-scott-bessent-hires-wall-street-geek-david-zervos-to-advise-treasury-amid-rising-yields-whether-it-s-trade-whether-it-s-war-he-s-stepped-up/)  
  <sub>TradingView, 7 hours ago</sub>  
  Treasury Secretary Scott Bessent appointed Jefferies strategist David Zervos as a department counselor to advise the agency on rising bond yields.
- [Market Strategist Kristina Hooper Sees Risk Building Around AI Capex Over Surging Treasury Yields](https://www.tradingview.com/news/stocktwits:81ee7bf99094b:0-market-strategist-kristina-hooper-sees-risk-building-around-ai-capex-over-surging-treasury-yields/)  
  <sub>TradingView, 20 hours ago</sub>  
  Mounting pressure from soaring U.S. Treasury yields threatens to undermine capital investments in artificial intelligence and resilient consumer expenditure...
- [Soaring Yields Lead Traders to Snap Up Options on BlackRock ETFs](https://www.livemint.com/market/soaring-yields-lead-traders-to-snap-up-options-on-blackrock-etfs-11790628378886.html)  
  <sub>Livemint, 18 hours ago</sub>  
  Traders are piling into options tied to fixed-income ETFs at a record pace, in a rush to position portfolios with yields on 10-year and 30-year Treasuries...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 78.29 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 80.94 (-3.3%), 50d 82.02 (-4.5%), 200d 85.57 (-8.5%); 50d below 200d
Momentum: RSI(14) 26.8 | MACD -0.892 vs signal -0.617 (histogram -0.275)
Returns: 1d -0.4% | 5d -4.2% | 1m -5.5% | 3m -9.4%
52-week range: 78.29 - 92.06 (now 0.0% of the way up)
Volatility: ATR(14) 0.74 (0.9% of price) | annualised 20d 10.5%
Volume: 0.37x the 20-day average
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
Shares outstanding: 109.70M | fund size: 8.59B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 28.77 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 28.32 (+1.6%), 50d 28.24 (+1.9%), 200d 27.74 (+3.7%); 50d above 200d
Momentum: RSI(14) 72.8 | MACD 0.156 vs signal 0.100 (histogram 0.056)
Returns: 1d +0.2% | 5d +1.0% | 1m +2.1% | 3m +1.3%
52-week range: 26.47 - 28.77 (now 100.0% of the way up)
Volatility: ATR(14) 0.10 (0.4% of price) | annualised 20d 4.7%
Volume: 0.12x the 20-day average
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
Share count change: 1 week: -0.8% (-2.54M) over 7d
Shares outstanding: 10.44M | fund size: 300.27M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data unreachable: The read operation timed out

## Sector and country funds

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> neutral

**Main reasons it gave:**
- Price below 20‑day, 50‑day, and 200‑day SMAs (‑7.8% to ‑7.0%)
- RSI 25.5 (oversold) but MACD negative (‑1.684 vs ‑0.698)
- Analyst consensus 100% buy with +39.9% price target
- Share count +4.3% in past week indicating inflows
- Macro yields rising, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 86.13 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 93.38 (-7.8%), 50d 93.38 (-7.8%), 200d 92.65 (-7.0%); 50d above 200d
Momentum: RSI(14) 25.5 | MACD -1.684 vs signal -0.698 (histogram -0.987)
Returns: 1d -0.4% | 5d -7.3% | 1m -8.2% | 3m -5.7%
52-week range: 67.55 - 102.94 (now 52.5% of the way up)
Volatility: ATR(14) 1.83 (2.1% of price) | annualised 20d 18.8%
Volume: 0.33x the 20-day average
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
Three-year record: +29.3% a year | beta to the market 0.50
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 51.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +39.9% above the current prices
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
Share count change: 1 week: +4.3% (32.52M) over 7d
Shares outstanding: 9.19M | fund size: 791.71M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall due to flat fund flows, no macro surprise, and technicals lacking a decisive bullish breakout despite a strong analyst view and solid fundamentals.

**Main reasons it gave:**
- Analyst view: 100% buy rating (mean 1.19) and +19.7% price target
- Fund flows flat over the week, indicating no net demand
- Technicals: price below 20‑day, 50‑day SMAs, negative MACD, low volume, no bullish breakout
- Macro: rising US yields, stronger dollar, higher VIX, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 121.32 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 124.03 (-2.2%), 50d 122.52 (-1.0%), 200d 122.42 (-0.9%); 50d above 200d
Momentum: RSI(14) 43.5 | MACD -0.046 vs signal 0.417 (histogram -0.463)
Returns: 1d -0.0% | 5d -4.3% | 1m -1.6% | 3m +0.5%
52-week range: 97.88 - 137.69 (now 58.9% of the way up)
Volatility: ATR(14) 1.81 (1.5% of price) | annualised 20d 21.0%
Volume: 0.49x the 20-day average
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
Three-year record: +33.3% a year | beta to the market 1.07
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

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

```text
Rolled up from the 5 largest holdings, 37.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.19 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.7% above the current prices
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
Shares outstanding: 2.55M | fund size: 309.38M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; mixed signals with no material macro surprise, modest outflows, slight short‑term technical weakness, but solid fundamentals and bullish analyst coverage.

**Main reasons it gave:**
- Fund flows: -0.6% share count (≈$5M) outflow over 1 week
- Technical: price 1.8% below 20‑day SMA, MACD histogram -0.164 indicating short‑term weakness
- Analyst coverage: 90.3% buy, price target +0.6% above current price
- Fundamentals: P/E 13.47, dividend yield 3.3%, 3‑yr return 43.7% per year
- Macro: US Treasury yields rose across curve; market expects ~4 quarter‑point hikes in 2 years

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 44.03 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 44.85 (-1.8%), 50d 43.95 (+0.2%), 200d 39.39 (+11.8%); 50d above 200d
Momentum: RSI(14) 45.9 | MACD 0.190 vs signal 0.354 (histogram -0.164)
Returns: 1d -1.4% | 5d -3.4% | 1m +1.3% | 3m +14.0%
52-week range: 31.78 - 45.76 (now 87.6% of the way up)
Volatility: ATR(14) 0.66 (1.5% of price) | annualised 20d 19.6%
Volume: 0.45x the 20-day average
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
Three-year record: +43.7% a year | beta to the market 0.73
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
Weighted price target: +0.6% above the current prices
Holdings read: PKO.WA, PKN.WA, PEO.WA, PZU.WA, KGH.WA
Recent rating changes among them: none reported
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
Share count change: 1 week: -0.6% (-4.91M) over 7d
Shares outstanding: 18.97M | fund size: 835.43M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; analyst view is bearish but no macro surprise or decisive technical break, and fund flows are flat.

**Main reasons it gave:**
- Analyst rating: 40.4% sell, price target -5.9% below current price
- Flat fund flows: share count unchanged over the week
- Technical indicators: price below 20‑day and 50‑day SMAs, RSI 38.2, negative MACD
- RBA raised cash rate to 4.60% (expected, no surprise)

<details><summary><b>News</b> — score +0.00</summary>

- [Liquidity Mapping Around (EWA) Price Events](https://news.stocktradersdaily.com/news_release/38/Liquidity_Mapping_Around_EWA_Price_Events_092926101202_1790691122.html)  
  <sub>Stock Traders Daily, 5 hours ago</sub>  
  Key findings for Ishares Msci Australia Etf (NYSE: EWA). Weak Near and Mid-Term Sentiment Could Challenge Long-Term Positive Outlook...
- [RBA delivers fourth rate hike of 2026 to 4.60% as inflation pressures mount](https://seekingalpha.com/news/4647847-rba-delivers-fourth-rate-hike-of-2026-to-460-as-inflation-pressures-mount)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  The Reserve Bank of Australia ((RBA)) unanimously raised its cash rate target by 25 basis points to 4.60% at its September 2026 meeting, matching market...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 28.31 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 29.13 (-2.8%), 50d 29.46 (-3.9%), 200d 28.61 (-1.0%); 50d above 200d
Momentum: RSI(14) 38.2 | MACD -0.343 vs signal -0.253 (histogram -0.090)
Returns: 1d -0.7% | 5d -2.7% | 1m -5.6% | 3m +0.5%
52-week range: 24.95 - 30.43 (now 61.3% of the way up)
Volatility: ATR(14) 0.36 (1.3% of price) | annualised 20d 18.6%
Volume: 0.22x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.50</summary>

```text
Rolled up from the 5 largest holdings, 46.4% of the fund by weight
Ratings by weight: buy 0.0% | hold 59.6% | sell 40.4% (mean 3.48 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -5.9% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 63.60M | fund size: 1.80B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Most macro and technical factors are neutral; analyst view is modestly bullish (+6.4% price target) but covers only ~28% of the fund; fundamentals are solid but not extraordinary; fund flows are flat, indicating no net demand.

**Main reasons it gave:**
- Analyst view: 74.3% buy, weighted price target +6.4% above current price
- Fund fundamentals: P/E 19.49, 3‑year record +22.7% per year, low beta 0.79
- Fund flows flat: share count unchanged over the past week
- Technicals: price below 20‑day and 50‑day SMA, RSI 34.7, negative MACD

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 58.74 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 60.43 (-2.8%), 50d 60.73 (-3.3%), 200d 57.65 (+1.9%); 50d above 200d
Momentum: RSI(14) 34.7 | MACD -0.496 vs signal -0.284 (histogram -0.212)
Returns: 1d -0.6% | 5d -3.3% | 1m -4.8% | 3m +1.9%
52-week range: 49.72 - 62.64 (now 69.8% of the way up)
Volatility: ATR(14) 0.64 (1.1% of price) | annualised 20d 14.6%
Volume: 0.12x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 28.3% of the fund by weight
Ratings by weight: buy 74.3% | hold 25.7% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.4% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 94.80M | fund size: 5.57B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: technicals show slight bearish momentum, macro environment is risk‑off with rising US yields and expectations of further Fed hikes, and fund flows are flat. Analyst coverage is positive but limited, and fundamentals are modestly attractive, leading to no clear directional catalyst.

**Main reasons it gave:**
- Technical momentum negative: price below 20‑day SMA (51.80) and RSI 38.6
- Fund flows flat: share count unchanged (+0.0% over 1 week)
- Macro environment: US yields rising (10‑yr 5.25% +0.28) and market expects further Fed hikes
- Analyst coverage limited to 29.5% of fund but shows 82% buy rating and +11.7% price target

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 50.46 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 51.80 (-2.6%), 50d 52.26 (-3.4%), 200d 51.38 (-1.8%); 50d above 200d
Momentum: RSI(14) 38.6 | MACD -0.429 vs signal -0.304 (histogram -0.125)
Returns: 1d -1.0% | 5d -3.3% | 1m -6.0% | 3m +1.0%
52-week range: 45.38 - 54.72 (now 54.4% of the way up)
Volatility: ATR(14) 0.71 (1.4% of price) | annualised 20d 16.7%
Volume: 0.31x the 20-day average
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
Weighted price target: +11.7% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 7.65M | fund size: 386.04M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, technical not decisive, flat fund flows, analyst view bullish but limited coverage, fundamentals moderate.

**Main reasons it gave:**
- Analyst view: 78% buy, price target +15.7% (covers 45.5% of fund)
- Technical: price below 20d, 50d, 200d SMAs; RSI 37.9; MACD negative; volume 0.08x average
- Fund flows: flat (0% change) over past week
- Macro: yields rose modestly, no policy surprise; VIX stable at 15.89
- Fundamentals: moderate valuations (P/E 18.4) and strong 3‑year record (+19.3% per year)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 41.86 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 42.73 (-2.0%), 50d 43.09 (-2.9%), 200d 42.40 (-1.3%); 50d above 200d
Momentum: RSI(14) 37.9 | MACD -0.383 vs signal -0.288 (histogram -0.096)
Returns: 1d -0.6% | 5d -1.9% | 1m -6.1% | 3m +1.2%
52-week range: 38.08 - 44.59 (now 58.1% of the way up)
Volatility: ATR(14) 0.46 (1.1% of price) | annualised 20d 13.7%
Volume: 0.08x the 20-day average
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
Three-year record: +19.3% a year | beta to the market 0.98
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.87 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.7% above the current prices
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
Shares outstanding: 79.50M | fund size: 3.33B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows modest bullish fundamentals and analyst coverage, but flat flows and neutral technicals keep the overall stance neutral.

**Main reasons it gave:**
- Analyst view: 100% buy rating on 50.9% of fund, weighted price target +11.3% above current
- Fund flows: flat share count change (+0.0% over 1 week)
- Fund fundamentals: P/E 15.25, yield 3.0%, three‑year annualized return +29.5% per year
- Technical: price below 20‑day SMA, RSI 38.1, low volume (0.25× 20‑day average)
- Macro: yields up modestly, VIX 15.9, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 59.53 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 60.87 (-2.2%), 50d 61.69 (-3.5%), 200d 57.94 (+2.8%); 50d above 200d
Momentum: RSI(14) 38.1 | MACD -0.535 vs signal -0.411 (histogram -0.124)
Returns: 1d -0.8% | 5d -2.0% | 1m -4.3% | 3m +0.5%
52-week range: 50.31 - 63.35 (now 70.7% of the way up)
Volatility: ATR(14) 0.71 (1.2% of price) | annualised 20d 16.9%
Volume: 0.25x the 20-day average
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
Three-year record: +29.5% a year | beta to the market 0.88
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
Weighted price target: +11.3% above the current prices
Holdings read: UCG.MI, ISP.MI, ENEL.MI, RACE.MI, ENI.MI
Recent rating changes among them:
  - RACE.MI: 2026-07-31 UBS: main, Buy -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 8.55M | fund size: 509.02M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals show mixed signals near 52‑week high with low volume, analyst view bullish but thin coverage, positioning slightly bearish, fund flows flat.

**Main reasons it gave:**
- Technicals: price above 50‑day SMA but below 20‑day SMA, RSI 48.1, MACD below signal
- Analyst view: 100% buy rating for top holdings but only 17% of fund weight
- Positioning: net long 3.6% of open interest, down 0.7% week‑over‑week
- Macro: no policy surprise, yields up modestly, USD index up 0.79% on week

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 96.25 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 97.22 (-1.0%), 50d 95.62 (+0.7%), 200d 90.18 (+6.7%); 50d above 200d
Momentum: RSI(14) 48.1 | MACD 0.317 vs signal 0.530 (histogram -0.214)
Returns: 1d -0.6% | 5d -2.6% | 1m +0.4% | 3m +3.2%
52-week range: 78.36 - 98.78 (now 87.6% of the way up)
Volatility: ATR(14) 1.43 (1.5% of price) | annualised 20d 19.1%
Volume: 0.39x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.8% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 227.85M | fund size: 21.93B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data unreachable: The read operation timed out

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, weak technicals, but bullish analyst view; overall neutral stance.

**Main reasons it gave:**
- Technical: price 59.79 below 20‑day SMA 60.99 (‑2.0%) and 50‑day SMA 62.48 (‑4.3%)
- Momentum: RSI 36.1 indicating weak price momentum and volume 0.25× 20‑day average
- Macro: no policy or data surprise; yields up modestly, VIX up modestly, inflation 3.4% in line with expectations
- Fund flows: flat share count change (+0.0% week) indicating no net demand
- Analyst view: 74.5% buy rating, price target +10.4% above current, covering 48.5% of fund

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 59.79 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 60.99 (-2.0%), 50d 62.48 (-4.3%), 200d 61.62 (-3.0%); 50d above 200d
Momentum: RSI(14) 36.1 | MACD -0.708 vs signal -0.710 (histogram 0.002)
Returns: 1d -1.0% | 5d -2.3% | 1m -5.6% | 3m -4.9%
52-week range: 54.57 - 65.08 (now 49.7% of the way up)
Volatility: ATR(14) 0.68 (1.1% of price) | annualised 20d 14.0%
Volume: 0.25x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 48.5% of the fund by weight
Ratings by weight: buy 74.5% | hold 25.5% | sell 0.0% (mean 2.40 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.4% above the current prices
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
Shares outstanding: 28.62M | fund size: 1.71B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, flat fund flows, mixed technicals, and a bullish analyst view that is not enough to shift the call.

**Main reasons it gave:**
- Yield curve remains upward sloping (+1.16 points) – no rate surprise
- Macro data in line with expectations (inflation 3.4%, unemployment 4.1%)
- Fund flows flat (0.0% share count change) – no net demand shift
- Technical indicators mixed: price above SMAs but MACD negative and low volume
- Analyst coverage overwhelmingly bullish (100% buy, +25.6% price target) but macro unchanged

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 68.63 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 67.72 (+1.3%), 50d 68.23 (+0.6%), 200d 64.19 (+6.9%); 50d above 200d
Momentum: RSI(14) 54.4 | MACD -0.125 vs signal -0.271 (histogram 0.147)
Returns: 1d +0.8% | 5d +0.1% | 1m +0.2% | 3m -2.4%
52-week range: 55.33 - 71.61 (now 81.7% of the way up)
Volatility: ATR(14) 0.90 (1.3% of price) | annualised 20d 16.7%
Volume: 0.02x the 20-day average
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
Three-year record: +24.9% a year | beta to the market 1.14
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 44.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.62 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.6% above the current prices
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
Shares outstanding: 5.55M | fund size: 380.90M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data unreachable: The read operation timed out

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, technicals show no decisive break, flows flat, analyst view mixed, fundamentals moderate.

**Main reasons it gave:**
- US Treasury yields rose across the curve (+0.09% to +0.28% on the week) with no policy surprise
- Price below 20‑day and 50‑day SMAs, RSI 39.7, MACD below signal, and volume at 0.08× 20‑day average
- Fund flows flat (share count unchanged over the week), indicating no net demand
- Analyst coverage split 52% buy, 48% hold with a modest +2% price target
- Fund fundamentals moderate (P/E 16.28, expense ratio 0.5%)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 59.85 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 61.36 (-2.5%), 50d 61.64 (-2.9%), 200d 57.52 (+4.0%); 50d above 200d
Momentum: RSI(14) 39.7 | MACD -0.359 vs signal -0.207 (histogram -0.153)
Returns: 1d -1.3% | 5d -2.8% | 1m -4.0% | 3m +0.8%
52-week range: 48.33 - 63.23 (now 77.3% of the way up)
Volatility: ATR(14) 0.81 (1.4% of price) | annualised 20d 17.6%
Volume: 0.08x the 20-day average
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
Three-year record: +34.9% a year | beta to the market 0.87
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

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
Shares outstanding: 37.35M | fund size: 2.24B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows mixed signals: technicals are bearish (price below key SMAs, low RSI, negative MACD), while analyst coverage is strongly bullish (100% buy rating with a +16.6% price target). Fund flows are flat, indicating no net demand shift, and there are no macro surprises. The combination of these balanced factors leads to a neutral overall stance.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs (‑4% to ‑5%)
- RSI 36.3 and MACD negative indicating weak momentum
- Analyst coverage 100% buy with +16.6% price target
- Rating change: GMEXICOB.MX downgraded from Buy to Neutral
- Fund flows flat over the past week (no net creation/redemption)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 71.95 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 74.52 (-3.4%), 50d 75.62 (-4.9%), 200d 75.79 (-5.1%); 50d below 200d
Momentum: RSI(14) 36.3 | MACD -0.964 vs signal -0.722 (histogram -0.242)
Returns: 1d -0.6% | 5d -3.4% | 1m -5.9% | 3m -4.4%
52-week range: 64.39 - 81.23 (now 44.9% of the way up)
Volatility: ATR(14) 1.23 (1.7% of price) | annualised 20d 17.1%
Volume: 0.39x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

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
Rolled up from the 5 largest holdings, 47.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.6% above the current prices
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
Shares outstanding: 18.90M | fund size: 1.36B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, flat fund flows, mixed technicals, and no analyst rating.

**Main reasons it gave:**
- Fund flows flat (0% change) – no net demand
- US Treasury yields rose modestly across curve (+0.09 to +0.28) – no surprise
- Price above 20d, 50d, 200d SMAs but MACD below signal and low volume – mixed technicals
- Analyst view covers 53.5% of fund but provides no rating – neutral

<details><summary><b>News</b> — score +0.00</summary>

- [India vs. China ETFs: A Tale of Two Emerging Markets in 2026](https://www.tradingview.com/news/zacks:00bfb7167094b:0-india-vs-china-etfs-a-tale-of-two-emerging-markets-in-2026/)  
  <sub>TradingView, 3 hours ago</sub>  
  Wall Street is in good shape this year despite the Iran war, rising oil prices, soaring inflation and bond yields. Artificial Intelligence (AI) has been...
- [Stocktwits Passport Portfolio: QQQ Weekly Rally Leaves SPY, DIA And Asia In The Dust](https://stocktwits.com/news-articles/markets/equity/stocktwits-passport-portfolio-qqq-weekly-rally-leaves-spy-dia-and-asia-in-the-dust/cZMazMoRBaW)  
  <sub>Stocktwits, 21 hours ago</sub>  
  The tech-heavy Nasdaq index surged past its American and Asian counterparts as AI stayed in focus this week.
- [Asian markets extend losses on Wall Street sell-off and rising yields; RBA hikes rates](https://seekingalpha.com/news/4647837-asian-markets-extend-losses-on-wall-street-sell-off-and-rising-yields-rba-hikes-rates)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  Asian equity markets traded lower on Tuesday, tracking overnight weakness on Wall Street as rising U.S. Treasury yields and sustained high oil prices dented...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 186.02 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 183.75 (+1.2%), 50d 175.76 (+5.8%), 200d 154.84 (+20.1%); 50d above 200d
Momentum: RSI(14) 53.3 | MACD 2.160 vs signal 2.290 (histogram -0.131)
Returns: 1d +1.3% | 5d -3.4% | 1m +3.2% | 3m -7.9%
52-week range: 80.10 - 219.20 (now 76.1% of the way up)
Volatility: ATR(14) 6.27 (3.4% of price) | annualised 20d 47.6%
Volume: 0.27x the 20-day average
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
Three-year record: +49.2% a year | beta to the market 2.50
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 75.60M | fund size: 14.06B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, flat flows; analyst view bullish but limited coverage, fundamentals attractive but not a catalyst.

**Main reasons it gave:**
- Analyst coverage of top holdings (40.9% weight) shows 100% buy rating and +31.3% price target
- Technicals: price below 20‑day SMA, MACD histogram negative, RSI 42.3 indicating short‑term bearish momentum
- Fund flows flat over the past week, indicating no net investor conviction
- Fundamentals: low P/E 10.48 and 4.1% dividend yield suggest attractive valuation

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 36.13 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 37.60 (-3.9%), 50d 36.25 (-0.3%), 200d 36.31 (-0.5%); 50d below 200d
Momentum: RSI(14) 42.3 | MACD 0.145 vs signal 0.431 (histogram -0.286)
Returns: 1d -0.2% | 5d -5.6% | 1m +1.6% | 3m +4.7%
52-week range: 28.79 - 41.73 (now 56.8% of the way up)
Volatility: ATR(14) 0.75 (2.1% of price) | annualised 20d 24.1%
Volume: 0.32x the 20-day average
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
Weighted price target: +31.3% above the current prices
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
Shares outstanding: 200.55M | fund size: 7.25B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technicals are bearish (price below 20‑, 50‑ and 200‑day SMAs, negative MACD) while analyst coverage is strongly bullish (100 % buy, +30.6 % price target) and fundamentals are attractive (low P/E 9.31, high yield 7.1 %). Fund flows are flat, indicating no net demand. No macro surprise or decisive technical break on heavy volume is present, so the overall view remains neutral.

**Main reasons it gave:**
- Technical: price below 20‑, 50‑, 200‑day SMAs and negative MACD
- Analyst view: 100% buy rating with +30.6% price target for top holdings
- Fundamentals: low P/E 9.31 and high yield 7.1% suggest attractive valuation
- Fund flows flat (0% change) indicating no net demand

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 64.54 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 68.63 (-6.0%), 50d 67.70 (-4.7%), 200d 69.23 (-6.8%); 50d below 200d
Momentum: RSI(14) 35.7 | MACD -0.927 vs signal -0.275 (histogram -0.652)
Returns: 1d +0.1% | 5d -6.7% | 1m -8.7% | 3m +2.1%
52-week range: 60.43 - 81.60 (now 19.4% of the way up)
Volatility: ATR(14) 1.33 (2.1% of price) | annualised 20d 26.5%
Volume: 0.33x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 45.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.98 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.6% above the current prices
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
Shares outstanding: 7.90M | fund size: 509.86M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – bullish analyst coverage and modest inflows are offset by bearish technicals and a macro backdrop that is unfavourable for gold miners.

**Main reasons it gave:**
- Analyst coverage of top holdings (40% weight) is 100% buy with +18.5% price target
- Fund flows: share count up 3% in the past week, indicating net inflows
- Technicals: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 41; MACD negative
- Macro: Treasury yields up across the curve and dollar index up 0.79% on the week, typically bearish for gold miners

<details><summary><b>News</b> — score +0.00</summary>

- [VanEck UCITS ETFs Plc - Net Asset Value(s)](https://uk.finance.yahoo.com/news/vaneck-ucits-etfs-plc-net-060000129.html)  
  <sub>Yahoo Finance UK, 9 hours ago</sub>  
  Fund Name. NAV Date. Ticker Symbol. ISIN. Shares in Issue. Net Asset Value. NAV per Share. VanEck Emerging Markets High Yield Bond UCITS ETF. 2026-09-28.
- [GDX 261002 93.50C (GDX261002C93500) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/GDX261002C93500-US?chain_id=Name1K9-3FXPhg.1kvd400&global_content=%7B%22promote_id%22%3A13764,%22sub_promote_id%22%3A57,%22f%22%3A%22www.moomoo.com%2Fhans%2Fstock%2FYSWY-US%2Ffinancials-key-indicators%22%7D)  
  <sub>Moomoo, 19 hours ago</sub>  
  Track real-time GDX 261002 93.50C (GDX261002C93500) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [Form 4 VanEck Gold Miners ETF For: 28 September By Investing.com](https://au.investing.com/news/stock-market-news/form-4-vaneck-gold-miners-etf-for-28-september-93CH-4662936)  
  <sub>Investing.com Australia, 11 hours ago</sub>  
  Term Sheet. (To the Prospectus dated May 15, 2025, the Prospectus Supplement dated May 15, 2025 and Product Supplement EQUITY SUN-1 dated January 2, 2026).
- [[Quiddity Index] MV Global Gold Miners Dec26 Rebal: No Changes Likely; Vault-Genesis Deal Flows](https://www.smartkarma.com/insights/quiddity-index-mv-global-gold-miners-dec26-rebal-no-changes-likely-vault-genesis-deal-flows)  
  <sub>Smartkarma, 23 hours ago</sub>  
  For now, no changes are expected for the GDX ETF rebal in December 2026. Between now and then, there will be ad hoc changes due to the expected completion...
- [Nasdaq 100 Sinks, Oil Rallies as Trump Rejects Iran's Hormuz Plan: Stock Market Today](https://www.benzinga.com/markets/market-summary/26/09/62030720/oil-surges-nasdaq-slumps-trump-rejects-iran-deal-markets-monday)  
  <sub>Benzinga, 22 hours ago</sub>  
  Stocks slipped at midday Monday as oil surged and yields hit a 19-year high after Trump rejected Iran's Hormuz plan; MongoDB tumbled 18%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 88.62 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 95.20 (-6.9%), 50d 90.70 (-2.3%), 200d 91.06 (-2.7%); 50d below 200d
Momentum: RSI(14) 41.1 | MACD -0.670 vs signal 0.641 (histogram -1.311)
Returns: 1d +0.8% | 5d -9.4% | 1m -11.1% | 3m +17.5%
52-week range: 68.28 - 115.84 (now 42.8% of the way up)
Volatility: ATR(14) 3.34 (3.8% of price) | annualised 20d 43.6%
Volume: 0.24x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.5% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, AU
Recent rating changes among them:
  - NEM: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - AEM.TO: 2026-09-16 RBC Capital: main, Sector Perform -> Sector Perform
  - ABX.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - WPM.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - AU: 2026-09-16 RBC Capital: main, Outperform -> Outperform
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
Share count change: 1 week: +3.0% (862.42M) over 7d
Shares outstanding: 328.99M | fund size: 29.15B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst consensus, flat fund flows, high valuation in a rising‑rate environment, and mixed technicals.

**Main reasons it gave:**
- Analyst consensus 100% buy with weighted price target +7% above current price
- Fund flows flat: share count unchanged (+0.0% over 7 days)
- High valuation (P/E 34.2) amid rising yields and expected Fed hikes
- Technicals: price above 50‑day and 200‑day SMA, but MACD below signal and low volume

<details><summary><b>News</b> — score +0.00</summary>

- [Surviving The SaaSpocalypse: 3 Top Software Stocks Flipping The AI Script](https://seekingalpha.com/article/4950346-surviving-the-saaspocalypse-3-top-software-stocks-flipping-the-ai-script)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Software stocks crushed the Nasdaq in the past 3 months while showing AI-fueled growth, undermining the SaaSpocalypse narrative. Discover 3 top software...
- [BlackBerry Jumps 4% as Record QNX Revenue Lifts Full-Year Outlook; Mobileye and Aptiv Dip](https://247wallst.com/investing/2026/09/28/blackberry-jumps-5-as-record-qnx-revenue-lifts-full-year-outlook-mobileye-and-aptiv-dip/)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  BlackBerry is surging while its closest automotive technology peers slide lower, and the gap between them points to something specific buried inside the...
- [ServiceNOW, A Bellwether For The AI Vs. Software Trade (NYSE:NOW)](https://seekingalpha.com/article/4950394-servicenow-a-bellwether-for-the-ai-vs-software-trade)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  ServiceNow may surprise investors as AI makes its move toward a software story. Read what could be next for the stock.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 104.93 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 105.06 (-0.1%), 50d 101.87 (+3.0%), 200d 93.61 (+12.1%); 50d above 200d
Momentum: RSI(14) 50.9 | MACD 1.020 vs signal 1.253 (histogram -0.233)
Returns: 1d -0.5% | 5d -1.7% | 1m -4.2% | 3m +15.8%
52-week range: 74.67 - 117.08 (now 71.4% of the way up)
Volatility: ATR(14) 2.50 (2.4% of price) | annualised 20d 32.4%
Volume: 0.20x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 43.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +7.0% above the current prices
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

> Neutral overall as no material macro surprise or decisive technical break occurred; technicals are bearish but low volume, modest inflows and thin analyst coverage provide limited bullish bias.

**Main reasons it gave:**
- Price 46.88 below 20‑day SMA 48.38, 50‑day SMA 49.09, 200‑day SMA 49.95
- Share count up 0.6% (≈39.6M) in past week
- Analyst coverage thin (24.7% of fund), 100% buy rating, +35% price target
- Macro unchanged: yields up modestly, dollar stronger, VIX low

<details><summary><b>News</b> — score +0.00</summary>

- [RINDA to MXN: iShares MSCI India Index ETF rStock Price in Mexican Peso](https://www.coingecko.com/en/coins/ishares-msci-india-index-etf-rstock/mxn)  
  <sub>CoinGecko, 9 hours ago</sub>  
  Get live charts for RINDA to MXN. Convert iShares MSCI India Index ETF rStock (RINDA) to Mexican Peso (MXN).

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 46.88 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 48.38 (-3.1%), 50d 49.09 (-4.5%), 200d 49.95 (-6.2%); 50d below 200d
Momentum: RSI(14) 32.9 | MACD -0.546 vs signal -0.428 (histogram -0.118)
Returns: 1d -0.5% | 5d -2.9% | 1m -5.4% | 3m -5.1%
52-week range: 45.42 - 55.29 (now 14.7% of the way up)
Volatility: ATR(14) 0.46 (1.0% of price) | annualised 20d 14.0%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

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
Rolled up from the 5 largest holdings, 24.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.36 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +35.0% above the current prices
Holdings read: HDFCBANK.NS, RELIANCE.NS, ICICIBANK.NS, BHARTIARTL.NS, INFY.NS
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
Share count change: 1 week: +0.6% (39.65M) over 7d
Shares outstanding: 140.79M | fund size: 6.60B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: strong analyst bullishness (+28% price target) is offset by flat fund flows, no macro surprise, and technicals showing a downtrend with low volume despite oversold RSI.

**Main reasons it gave:**
- Flat fund flows: share count unchanged (+0.0% over 1 week)
- Macro: yields up across curve, VIX low at 15.9, no data surprise
- Technical: price below 20‑day, 50‑day, 200‑day SMAs; RSI 25.8 (oversold) with low volume
- Analyst view: 100% buy, price target +28.4% above current

<details><summary><b>News</b> — score +0.00</summary>

- [What's Going On With Boeing Stock Tuesday? - Boeing (NYSE:BA)](https://www.benzinga.com/markets/large-cap/26/09/62043724/boeing-737-max-10-certification-delayed-over-new-software-issue)  
  <sub>Benzinga, 4 hours ago</sub>  
  Boeing (BA) edges higher premarket following a 6.9% drop. Explore stock price targets, technical indicators, and key support levels.
- [U.S. military set to fully withdraw from Iraq after two decades](https://seekingalpha.com/news/4647853-us-military-set-to-fully-withdraw-from-iraq)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  US troops will fully exit Iraq, raising concerns over the country's security outlook. Read more.
- [Semis Edge Higher After VIX Spike](https://www.moomoo.com/community/feed/semis-edge-higher-after-vix-spike-117351396540422)  
  <sub>Moomoo, 15 hours ago</sub>  
  Tap the related stocks on the image above to add them to your Watchlist. Market Recap Cash benchmarks, as of their last trade, closed lower: $S&P 500 ...
- [Positioning Portfolios for the Midterm Elections](https://www.zacks.com/stock/news/2997027/positioning-portfolios-for-the-midterm-elections)  
  <sub>Zacks Investment Research, 19 hours ago</sub>  
  In this episode of ETF Spotlight, I speak with Matt Bartolini, Global Head of Research at State Street Global Advisors, about portfolio positioning...
- [Trump denies report on potential sanctions relief for Iran](https://seekingalpha.com/news/4647869-trump-denies-report-on-potential-sanctions-relief-for-iran)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Trump denies offering Iran sanctions relief or asset unfreezing for nuclear concessions as Hormuz talks stall.
- [Trump considers Iran sanctions relief for nuclear concessions - report (ITA:BATS)](https://seekingalpha.com/news/4647710-trump-considers-iran-sanctions-relief-for-nuclear-concessions-report)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  U.S. President Donald Trump is open to unfreezing Iranian assets and easing economic sanctions, provided Tehran delivers verifiable concessions on its...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 208.95 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 217.17 (-3.8%), 50d 232.33 (-10.1%), 200d 230.48 (-9.3%); 50d above 200d
Momentum: RSI(14) 25.8 | MACD -6.278 vs signal -6.279 (histogram 0.001)
Returns: 1d -0.1% | 5d -2.4% | 1m -10.3% | 3m -13.8%
52-week range: 198.23 - 253.22 (now 19.5% of the way up)
Volatility: ATR(14) 3.95 (1.9% of price) | annualised 20d 14.2%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

```text
Rolled up from the 5 largest holdings, 57.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.75 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +28.4% above the current prices
Holdings read: GE, RTX, BA, GD, LMT
Recent rating changes among them:
  - GE: 2026-09-23 Jefferies: main, Buy -> Buy
  - RTX: 2026-09-23 Bernstein: main, Market Perform -> Market Perform
  - BA: 2026-09-21 Jefferies: main, Buy -> Buy
  - GD: 2026-09-23 Bernstein: main, Market Perform -> Market Perform
  - LMT: 2026-09-08 UBS: up, Neutral -> Buy
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
Share count change: 1 week: +0.0% (5.59M) over 7d
Shares outstanding: 63.75M | fund size: 13.32B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, flat fund flows, and mixed technicals. Analyst coverage is strongly bullish but there is no material catalyst to shift the fund’s direction.

**Main reasons it gave:**
- Analyst consensus 90.8% buy with weighted price target +26.6% (bullish)
- Technical indicators: price below 20‑day, 50‑day and 200‑day SMAs, RSI 30.3 (oversold) but no decisive break
- Fund flows flat (0% change) indicating no net demand
- Macro data stable: modest yield increases, inflation 3.4% below Fed target, no surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Uber Just Fell 13% in a Month. Is It Time to Sell, or Should You Buy the Dip?](https://247wallst.com/investing/2026/09/28/uber-just-fell-13-in-a-month-is-it-time-to-sell-or-should-you-buy-the-dip/)  
  <sub>24/7 Wall St., 20 hours ago</sub>  
  Uber slid while big tech climbed, and its closest rivals fell even harder, which turns a rough month into a question about whether the pressure comes from...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 79.04 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 81.24 (-2.7%), 50d 84.60 (-6.6%), 200d 81.22 (-2.7%); 50d above 200d
Momentum: RSI(14) 30.3 | MACD -1.684 vs signal -1.581 (histogram -0.104)
Returns: 1d -0.0% | 5d -1.4% | 1m -8.5% | 3m -8.9%
52-week range: 68.14 - 90.01 (now 49.8% of the way up)
Volatility: ATR(14) 1.17 (1.5% of price) | annualised 20d 15.5%
Volume: 0.13x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 53.1% of the fund by weight
Ratings by weight: buy 90.8% | hold 9.2% | sell 0.0% (mean 1.84 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.6% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 2.80M | fund size: 221.31M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst view and net inflows versus bearish technicals and higher‑rate macro backdrop. No clear policy surprise or decisive technical break, so the overall stance remains neutral.

**Main reasons it gave:**
- US Treasury yields rose across the curve (+0.09 to +0.28) indicating higher rates and risk‑off sentiment
- KSA price below 20‑day, 50‑day, and 200‑day SMAs with RSI 27.4 and negative MACD, showing bearish technical momentum
- Analyst coverage of top holdings (44.4% weight) is 90% buy with +18% price target, indicating bullish outlook
- Fund flows show 1.4% share‑count increase over the week, reflecting net inflows

<details><summary><b>News</b> — score +0.00</summary>

- [Saudi Arabia restarts oil exports through Hormuz-bypassing pipeline (USO:NYSEARCA)](https://seekingalpha.com/news/4647743-saudi-arabia-restarts-oil-exports-through-hormuz-bypassing-pipeline)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Saudi Arabia resumes East-West pipeline exports via Yanbu after drone attacks, easing oil supply fears and price risk as Hormuz stays vulnerable.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 36.37 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 37.68 (-3.5%), 50d 37.79 (-3.8%), 200d 38.13 (-4.6%); 50d below 200d
Momentum: RSI(14) 27.4 | MACD -0.379 vs signal -0.238 (histogram -0.141)
Returns: 1d -1.6% | 5d -2.6% | 1m -7.4% | 3m -2.5%
52-week range: 35.83 - 41.03 (now 10.3% of the way up)
Volatility: ATR(14) 0.31 (0.8% of price) | annualised 20d 8.8%
Volume: 0.54x the 20-day average
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
Weighted price target: +18.0% above the current prices
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
Share count change: 1 week: +1.4% (8.54M) over 7d
Shares outstanding: 17.25M | fund size: 627.45M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro policy surprise, no decisive technical break, and only modest fund inflows. Analyst coverage is bullish but limited to ~32% of the fund, and fundamentals are stable but not a catalyst. Overall, the evidence does not justify a directional tilt.

**Main reasons it gave:**
- US Treasury yields rose modestly across the curve (+0.09 to +0.28) with no surprise
- Technicals show price below 20d, 50d, 200d SMAs and low volume (0.21x avg), no decisive break
- Fund flows show modest share count increase (+0.7% week) indicating slight demand
- Analyst coverage covers 32.2% of fund, rating 100% buy with +56% price target

<details><summary><b>News</b> — score +0.00</summary>

- [Stocktwits Passport Portfolio: QQQ Weekly Rally Leaves SPY, DIA And Asia In The Dust](https://stocktwits.com/news-articles/markets/equity/stocktwits-passport-portfolio-qqq-weekly-rally-leaves-spy-dia-and-asia-in-the-dust/cZMazMoRBaW)  
  <sub>Stocktwits, 21 hours ago</sub>  
  The tech-heavy Nasdaq index surged past its American and Asian counterparts as AI stayed in focus this week.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 52.01 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 53.35 (-2.5%), 50d 54.40 (-4.4%), 200d 56.95 (-8.7%); 50d below 200d
Momentum: RSI(14) 36.3 | MACD -0.527 vs signal -0.443 (histogram -0.084)
Returns: 1d -1.0% | 5d -4.1% | 1m -5.8% | 3m +1.9%
52-week range: 50.48 - 66.99 (now 9.2% of the way up)
Volatility: ATR(14) 0.59 (1.1% of price) | annualised 20d 15.4%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

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
Rolled up from the 5 largest holdings, 32.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.40 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +56.4% above the current prices
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
Direction: money coming in (1 week)
Share count change: 1 week: +0.7% (42.85M) over 7d
Shares outstanding: 119.85M | fund size: 6.23B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- 10-year Treasury yield up 0.28% this week, raising risk‑free rates
- SMH technical trend bullish but volume at 0.27x 20‑day average, no decisive breakout
- Fund flows flat (0% share count change), indicating no net demand
- SMH high beta (2.06) makes it vulnerable to higher yields and risk‑off sentiment

<details><summary><b>News</b> — score +0.00</summary>

- [VanEck Semiconductor ETF (SMH) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/SMH/)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  VanEck Semiconductor ETF (SMH) · 0.67% · 8.48% · 60.32% · 65.15% · 86.44% · 360.68% · 1,130.79%. Key Events. Baseline. Advanced Chart. Loading chart for SMH.
- [If I Had Only $500 per Month to Invest, These Are the 2 ETFs I'd Buy](https://www.fool.com/investing/2026/09/29/if-i-had-only-500-per-month-to-invest-etfs-buy/)  
  <sub>The Motley Fool, 3 hours ago</sub>  
  The S&P 500 is still sitting near all-time highs, but that doesn't mean that every equity ETF is a buy right now. Here are two that I believe are still...
- [Bet on These ETFs as AMD Agrees to Buy World Labs for $8.2B](https://www.tradingview.com/news/zacks:ed1f40703094b:0-bet-on-these-etfs-as-amd-agrees-to-buy-world-labs-for-8-2b/)  
  <sub>TradingView, 3 hours ago</sub>  
  Advanced Micro Devices AMD has recently announced an agreement to acquire San Francisco-based AI research firm World Labs in an $8.2 billion all-stock...
- [Korea launches its own version of popular US fund Roundhill Memory ETF DRAM](https://www.kedglobal.com/stocks/newsView/ked202609290005)  
  <sub>KED Global, 2 hours ago</sub>  
  South Korean retail investors' appetite for US-listed memory semiconductor exchange traded funds (ETF) is prompting the launch of a local version aimed a.
- [VanEck Semiconductor ETF: A Top Growth Pick Amid AI Boom](https://intellectia.ai/news/stock/vaneck-semiconductor-etf-a-top-growth-pick-amid-ai-boom)  
  <sub>Intellectia AI, 11 hours ago</sub>  
  Strong ETF Performance**: The VanEck Semiconductor ETF (NASDAQ: SMH) tracks top U.S.-listed chip stocks, with its top five holdings, including Nvi...
- [$44B Rush Back into Equity Funds: Are Investors Betting on AI ETFs Again?](https://www.tradingview.com/news/benzinga:9c3dbff52094b:0-44b-rush-back-into-equity-funds-are-investors-betting-on-ai-etfs-again/)  
  <sub>TradingView, 18 hours ago</sub>  
  Global equity funds attracted $44.1 billion in the week ending Sept. 23 — a dramatic U-turn — as ETF flows suggest a familiar trade may be driving the...
- [S&P 500, Dow, Nasdaq Drop Under Pressure From Elevated Yields As Investors Shrug Off Trump’s Iran Sanction Relief — NVDA, BA, AMD, NVTS, CBRS In Focus](https://www.tradingview.com/news/stocktwits:341c009e9094b:0-s-p-500-dow-nasdaq-drop-under-pressure-from-elevated-yields-as-investors-shrug-off-trump-s-iran-sanction-relief-nvda-ba-amd-nvts-cbrs-in-focus/)  
  <sub>TradingView, 16 hours ago</sub>  
  U.S. stock indices ended Monday lower as elevated Treasury yields continued to dampen the demand for riskier assets, while media reports suggested President...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 611.85 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 573.94 (+6.6%), 50d 567.82 (+7.8%), 200d 495.63 (+23.5%); 50d above 200d
Momentum: RSI(14) 63.2 | MACD 11.123 vs signal 5.802 (histogram 5.321)
Returns: 1d +2.0% | 5d +0.7% | 1m +10.6% | 3m -6.7%
52-week range: 322.66 - 668.91 (now 83.5% of the way up)
Volatility: ATR(14) 15.88 (2.6% of price) | annualised 20d 32.4%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 49.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.34 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +33.7% above the current prices
Holdings read: NVDA, TSM, AVGO, MU, AMD
Recent rating changes among them:
  - NVDA: 2026-09-29 Rosenblatt: main, Buy -> Buy
  - TSM: 2026-09-02 Stifel: init, ? -> Buy
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-09-28 Wedbush: reit, Outperform -> Outperform
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
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 11.67M | fund size: 7.14B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst view is offset by downtrend technicals, flat fund flows, and no macro catalyst.

**Main reasons it gave:**
- Technical: price below 20‑day, 50‑day, 200‑day SMAs; RSI 29.1, MACD negative
- Fund flows: share count unchanged (+0.0% over 7 days)
- Analyst view: 100% buy rating, +23.4% price target covering 39.5% of fund
- Macro: US Treasury yields up, dollar stronger; no policy surprise for Turkey

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 34.83 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 38.25 (-8.9%), 50d 38.93 (-10.5%), 200d 39.33 (-11.4%); 50d below 200d
Momentum: RSI(14) 29.1 | MACD -1.038 vs signal -0.650 (histogram -0.388)
Returns: 1d -1.7% | 5d -6.7% | 1m -14.8% | 3m -10.4%
52-week range: 31.90 - 43.74 (now 24.8% of the way up)
Volatility: ATR(14) 0.75 (2.2% of price) | annualised 20d 35.7%
Volume: 0.32x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 39.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.4% above the current prices
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
Shares outstanding: 15.65M | fund size: 545.17M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals show a downtrend with low volume, analyst coverage is limited to ~40% of the fund despite bullish ratings, and fund flows are flat. These factors balance out, leading to a neutral overall view.

**Main reasons it gave:**
- 10-year Treasury yield up 0.28% on the week, pressuring REIT valuations
- Price below 20‑day, 50‑day and 200‑day SMAs; RSI 25.2 indicates oversold but trend remains down
- Analyst coverage only 39.9% of fund, despite 100% buy ratings and +19% price target
- Fund flows flat over the past week, indicating no net demand shift

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 90.46 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 93.76 (-3.5%), 50d 96.70 (-6.4%), 200d 94.37 (-4.1%); 50d above 200d
Momentum: RSI(14) 25.2 | MACD -1.703 vs signal -1.409 (histogram -0.295)
Returns: 1d -0.1% | 5d -3.4% | 1m -7.0% | 3m -6.2%
52-week range: 87.00 - 100.95 (now 24.8% of the way up)
Volatility: ATR(14) 1.12 (1.2% of price) | annualised 20d 11.8%
Volume: 0.29x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.1% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2024-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - PLD: 2026-09-01 Wells Fargo: main, Overweight -> Overweight
  - EQIX: 2026-09-21 Rothschild & Co: init, ? -> Buy
  - AMT: 2026-08-20 Barclays: up, Equal-Weight -> Overweight
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
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 370.18M | fund size: 33.49B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral

**Main reasons it gave:**
- No macro surprise: yields rose modestly, no policy shift
- Technical indicators: price below 20‑day/50‑day SMA, negative MACD, low volume
- Analyst view: weighted price target -18.3% (downside) despite neutral rating distribution
- Fund flows: +1.2% share count increase (modest inflow) but not strong enough to drive a call

<details><summary><b>News</b> — score +0.00</summary>

- [State Street SPDR S&P Biotech ETF (XBI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XBI/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  State Street SPDR S&P Biotech ETF (XBI) · -1.02% · -3.55% · 30.96% · 28.44% · 59.89% · 22.60% · 849.15%. Key Events. Baseline. Advanced Chart.
- [SPDR S&P Biotech ETF (XBI) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/XBI/)  
  <sub>Yahoo Finance UK, 4 hours ago</sub>  
  In seeking to track the performance of the S&P Biotechnology Select Industry Index (the "index"), the fund employs a sampling strategy. It generally invests...
- [Is State Street SPDR S&P Biotech ETF (XBI) a Strong ETF Right Now?](https://sg.finance.yahoo.com/news/state-street-spdr-p-biotech-092002157.html)  
  <sub>Yahoo Finance Singapore, 6 hours ago</sub>  
  Making its debut on 01/31/2006, smart beta exchange traded fund State Street SPDR S&P Biotech ETF (XBI) provides investors broad exposure to the Health Care...
- [How (XBI) Movements Inform Risk Allocation Models](https://news.stocktradersdaily.com/news_release/139/How_XBI_Movements_Inform_Risk_Allocation_Models_092926032803_1790666883.html)  
  <sub>Stock Traders Daily, 12 hours ago</sub>  
  Price-action only: Spdr Biotech Etf (XBI) movements set the tone for institutional models. How (XBI) Movements Inform Risk Allocation Models.
- [Biotech Stocks Need A Shot In The Arm After Brutal July: Could AstraZeneca-Bristol Myers Megadeal Be The Cure?](https://stocktwits.com/news-articles/markets/equity/biotech-stocks-brutal-july-astrazeneca-bristol-myers-megadeal-cure/cZoRxFHRJ5V)  
  <sub>Stocktwits, 23 hours ago</sub>  
  A potential AstraZeneca-Bristol Myers deal worth $400 billion would create one of the world's largest drugmakers and combine major cancer franchises.
- [Why Did AMD, HPE, MRNA Stocks Surge To 52-Week Highs Last Week?](https://stocktwits.com/news-articles/markets/equity/why-did-amd-hpe-mrna-stocks-surge-to-52-week-highs-last-week/cZMS1RURBfm)  
  <sub>Stocktwits, 23 hours ago</sub>  
  Advanced Micro Devices (AMD), Hewlett Packard Enterprise (HPE) and Moderna (MRNA) surged to fresh 52-week highs Friday as investors piled into AI...
- [Biotech Bull Market Opportunities: Away From The Madding Crowd Of Compute? - TalkMarkets](https://t.co/MioCvOKXb0)  
  <sub>Howl.Link, 12 hours ago</sub>  
  Source: DepositPhotos. Both of the major biotech ETFS are outperforming Tech and the S&P 500: BB up 25%, XBI up 29% YTD.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 155.38 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 158.52 (-2.0%), 50d 157.87 (-1.6%), 200d 138.33 (+12.3%); 50d above 200d
Momentum: RSI(14) 45.1 | MACD -1.033 vs signal -0.595 (histogram -0.439)
Returns: 1d -0.8% | 5d -4.0% | 1m -4.3% | 3m -1.8%
52-week range: 99.40 - 169.55 (now 79.8% of the way up)
Volatility: ATR(14) 4.12 (2.7% of price) | annualised 20d 25.0%
Volume: 0.37x the 20-day average
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
Three-year record: +29.5% a year | beta to the market 1.12
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

<details><summary><b>What analysts and big funds say</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.20</summary>

```text
Rolled up from the 5 largest holdings, 9.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 43.2% | hold 56.8% | sell 0.0% (mean 2.28 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -18.3% above the current prices
Holdings read: MRNA, TWST, APGE, KYMR, HALO
Recent rating changes among them:
  - MRNA: 2026-09-03 Rothschild & Co: down, Neutral -> Sell
  - TWST: 2026-09-18 BWS Financial: main, Sell -> Sell
  - APGE: 2026-08-13 Truist Securities: main, Hold -> Hold
  - KYMR: 2026-09-22 Stifel: main, Buy -> Buy
  - HALO: 2026-09-02 HC Wainwright & Co.: reit, Buy -> Buy
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
Share count change: 1 week: +1.2% (130.76M) over 7d
Shares outstanding: 73.61M | fund size: 11.44B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: mixed evidence with modest bullish analyst view (thin coverage), recent outflows, bearish technicals, and a tightening macro environment without any surprise data.

**Main reasons it gave:**
- Fund flows: 1‑week share count down 2.0% (outflows)
- Analyst coverage thin (20.9% weight) but bullish (78.9% buy, +21.8% price target)
- Technical trend below 20‑, 50‑, 200‑day SMAs, RSI 39.8 (bearish momentum)
- Macro: yields rising across curve, VIX up to 15.9 (elevated volatility, no surprise data)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 96.94 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 98.59 (-1.7%), 50d 103.77 (-6.6%), 200d 106.33 (-8.8%); 50d below 200d
Momentum: RSI(14) 39.8 | MACD -1.990 vs signal -2.205 (histogram 0.215)
Returns: 1d -0.4% | 5d -2.5% | 1m -7.3% | 3m -16.1%
52-week range: 94.86 - 121.36 (now 7.8% of the way up)
Volatility: ATR(14) 2.09 (2.2% of price) | annualised 20d 22.9%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

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
Rolled up from the 5 largest holdings, 20.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 78.9% | hold 21.1% | sell 0.0% (mean 2.15 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.8% above the current prices
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
Share count change: 1 week: -2.0% (-26.99M) over 7d
Shares outstanding: 13.54M | fund size: 1.31B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall call due to mixed signals: bearish technicals, flat fund flows, limited analyst coverage despite bullish ratings, and a neutral macro backdrop.

**Main reasons it gave:**
- Technical indicators show price below 20‑day, 50‑day, and 200‑day SMAs, RSI 33.5, and negative MACD, indicating bearish momentum
- Fund flows are flat over the past week, indicating no net demand shift
- Analyst coverage of top holdings (37% of fund) is 100% buy with a +14.9% price target, but limited coverage reduces impact
- Macro environment shows rising yields and expectations of further rate hikes, with no surprise data, providing a neutral backdrop

<details><summary><b>News</b> — score +0.00</summary>

- [The 'Funflation' Effect: What It May Mean for Retail Stocks](https://etfdb.com/equity-etf-content-hub/funflation-effect-means-retail/)  
  <sub>ETF Database, 2 hours ago</sub>  
  Inflation may be a burden on the wallets of businesses and consumers alike, but “funflation” already sounds like a much more whimsical prospect.
- [ValuEngine Weekly Commentary: Sector And ETF Performance](https://seekingalpha.com/article/4950576-valuengine-weekly-commentary-sector-etf-performance)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  U.S. equity markets were mixed this week, with technology and growth-related areas leading, while several defensive and rate-sensitive sectors moved lower.
- [State Street Health Care Select Sector SPDR ETF (XLV) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Find the latest State Street Health Care Select Sector SPDR ETF (XLV) stock quote, history, news and other vital information to help you with your stock...
- [8 Of 11 Sectors Fall In Monday Trading As Defensives Lead](https://www.benzinga.com/etfs/sector-etfs/26/09/62026085/8-of-11-sectors-fall-in-monday-trading-as-defensives-lead)  
  <sub>Benzinga, 24 hours ago</sub>  
  Three sectors are higher and eight are lower in Monday's regular session, with defensive and cyclical sectors split across the top three positions.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 49.08 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 50.80 (-3.4%), 50d 51.66 (-5.0%), 200d 50.60 (-3.0%); 50d above 200d
Momentum: RSI(14) 33.5 | MACD -0.718 vs signal -0.566 (histogram -0.152)
Returns: 1d -0.8% | 5d -2.9% | 1m -7.7% | 3m -3.4%
52-week range: 42.23 - 53.67 (now 59.9% of the way up)
Volatility: ATR(14) 0.73 (1.5% of price) | annualised 20d 14.5%
Volume: 0.37x the 20-day average
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
Three-year record: +10.1% a year | beta to the market 0.82
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
Weighted price target: +14.9% above the current prices
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
Shares outstanding: 71.92M | fund size: 3.53B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as bullish analyst view and solid fundamentals are offset by recent outflows and short‑term technical weakness, with no material macro surprise.

**Main reasons it gave:**
- Fund flows show net outflows of -1.8% share count (-$408M) in the past week
- Analyst coverage of top holdings (45.5% weight) is 100% buy with a weighted price target +17.7% above current
- Technical indicators show price below 20‑day, 50‑day, and 200‑day SMAs, RSI 45.8, and MACD negative, indicating short‑term weakness
- Macro data: yields rose modestly, VIX up, no major surprise in inflation or policy

<details><summary><b>News</b> — score +0.00</summary>

- [ValuEngine Weekly Commentary: Sector And ETF Performance](https://seekingalpha.com/article/4950576-valuengine-weekly-commentary-sector-etf-performance)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  U.S. equity markets were mixed this week, with technology and growth-related areas leading, while several defensive and rate-sensitive sectors moved lower.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 110.90 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 112.51 (-1.4%), 50d 111.34 (-0.4%), 200d 113.88 (-2.6%); 50d below 200d
Momentum: RSI(14) 45.8 | MACD 0.149 vs signal 0.397 (histogram -0.247)
Returns: 1d -0.3% | 5d -2.3% | 1m -1.8% | 3m +3.5%
52-week range: 105.38 - 120.08 (now 37.6% of the way up)
Volatility: ATR(14) 1.75 (1.6% of price) | annualised 20d 21.4%
Volume: 0.27x the 20-day average
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
Three-year record: +21.1% a year | beta to the market 0.85
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.56 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.7% above the current prices
Holdings read: META, GOOGL, GOOG, T, VZ
Recent rating changes among them:
  - META: 2024-09-30 Cantor Fitzgerald: reit, Overweight -> Overweight
  - GOOGL: 2026-09-28 Piper Sandler: reit, Overweight -> Overweight
  - GOOG: 2026-07-23 JP Morgan: main, Overweight -> Overweight
  - T: 2026-09-28 Morgan Stanley: main, Overweight -> Overweight
  - VZ: 2026-07-27 TD Cowen: main, Buy -> Buy
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
Share count change: 1 week: -1.8% (-408.39M) over 7d
Shares outstanding: 198.62M | fund size: 22.03B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- Analyst consensus 100% buy with +7.2% price target (bullish bias)
- Crude oil inventories built 3.0 mb (58th percentile) indicating bearish pressure on oil price
- EIA forecasts WTI price falling ~10% over six months (bearish)
- Technicals: price below 20‑day SMA, RSI 42, MACD negative, low volume – no decisive bullish break
- Fund flows flat (no net inflow/outflow) indicating neutral demand

<details><summary><b>News</b> — score +0.00</summary>

- [ValuEngine Weekly Commentary: Sector And ETF Performance](https://seekingalpha.com/article/4950576-valuengine-weekly-commentary-sector-etf-performance)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  U.S. equity markets were mixed this week, with technology and growth-related areas leading, while several defensive and rate-sensitive sectors moved lower.
- [Cruise Stocks Rally as Carnival's Q3 Results Land: Carnival Surges 12%, Royal Caribbean Gains 7%, Norwegian Rises 5%](https://247wallst.com/investing/2026/09/29/cruise-stocks-rally-as-carnivals-q3-results-land-carnival-surges-12-royal-caribbean-gains-7-norwegian-rises-5/)  
  <sub>24/7 Wall St., 1 hour ago</sub>  
  Carnival surged 6% after CEO Josh Weinstein reported record Q3 top- and bottom-line results, lifting rivals Royal Caribbean and Norwegian 3% each.
- [$700 Billion S&P 500 Sell-Off Meets $100 Oil: Are Investors Rotating Into Value ETFs?](https://www.benzinga.com/etfs/broad-u-s-equity-etfs/26/09/62031962/700-billion-sp-500-sell-off-meets-100-oil-are-investors-rotating-into-value-etfs)  
  <sub>Benzinga, 21 hours ago</sub>  
  S&P 500 erases nearly $700 billion as Treasury yields hit 19-year highs and oil nears $100, putting growth, value and energy ETFs in focus.
- [Exus is said to buy 715 MW of solar projects amid data center demand (XLE:NYSEARCA)](https://seekingalpha.com/news/4648066-exus-is-said-to-buy-715-mw-of-solar-projects-amid-data-center-demand)  
  <sub>Seeking Alpha, 48 minutes ago</sub>  
  Exus Renewables' 715-MW solar acquisition in Louisiana and Wisconsin highlights data-center-driven power demand and fast interconnection advantages—read...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 61.55 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 63.84 (-3.6%), 50d 61.92 (-0.6%), 200d 56.30 (+9.3%); 50d above 200d
Momentum: RSI(14) 42.1 | MACD -0.072 vs signal 0.411 (histogram -0.483)
Returns: 1d -0.9% | 5d -0.4% | 1m -1.8% | 3m +15.9%
52-week range: 42.61 - 65.93 (now 81.2% of the way up)
Volatility: ATR(14) 1.24 (2.0% of price) | annualised 20d 20.4%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.40</summary>

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

<details><summary><b>Does this company beat its own forecasts</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.40</summary>

```text
US inventories, week ending 2026-09-18 (published the following Wednesday)
  Crude oil: 426.4 million barrels, +3.0 on the week (a build), 58% percentile over 52 weeks
  Petrol: 206.0 million barrels, -1.7 on the week (a draw), 8% percentile over 52 weeks -- low for the time of year
  Diesel: 107.4 million barrels, -0.4 on the week (a draw), 33% percentile over 52 weeks
  Natural gas: 3,351.0 billion cubic feet, +53.0 on the week (a build), 73% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 51.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +7.2% above the current prices
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
Shares outstanding: 186.42M | fund size: 11.47B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, mixed technicals, bullish analyst view not enough to shift stance, flat fund flows.

**Main reasons it gave:**
- No macro surprise: yields rose modestly (10‑yr +0.28% on week) and Fed policy unchanged
- Technical indicators weak: price below 20‑day SMA, RSI 27.4 (oversold) but no decisive break
- Analyst view bullish (100% buy, +14% price target) but not enough to outweigh neutral macro/technical
- Fund flows flat (share count +0.0% week), indicating no net demand shift

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Financial Select Sector SPDR ETF (XLF) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLF/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  State Street Financial Select Sector SPDR ETF (XLF) · -3.06% · -6.73% · 13.34% · -1.06% · 0.61% · 42.23% · 184.43%. Key Events. Baseline.
- [Ten financial stocks that outperformed in September (XLF:NYSEARCA)](https://seekingalpha.com/news/4647958-ten-financial-stocks-that-outperformed-in-september)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Top 10 financial stocks for Sept 2026 ranked by 1-month gains (SECZ, PS, HOOD, COIN + more) with key ratings—see the list and act now.
- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Tuesday as Investors Weigh Tech Rebound](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131149164.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.2% and the actively trad.
- [ValuEngine Weekly Commentary: Sector And ETF Performance](https://seekingalpha.com/article/4950576-valuengine-weekly-commentary-sector-etf-performance)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  U.S. equity markets were mixed this week, with technology and growth-related areas leading, while several defensive and rate-sensitive sectors moved lower.
- [S&P 500 Nears Record Close. Why Are 27 Stocks Hitting New Lows?](https://www.ebc.com/forex/sp-500-27-stocks-new-lows-market-breadth)  
  <sub>EBC Financial Group, 11 hours ago</sub>  
  The S&P 500 is near a record, yet 27 stocks hit 52-week lows. See what weak breadth, equal-weight losses and higher yields reveal.
- [ETFs Are Buying Berkshire Hathaway (BRK.B) on Friday](https://www.gurufocus.com/news/9101139/etfs-are-buying-berkshire-hathaway-brkb-on-friday?ref=etf-fund-related)  
  <sub>GuruFocus, 3 hours ago</sub>  
  Last Friday, 22 ETFs were buying Berkshire Hathaway (BRK.B) shares while 9 were selling, for a net inflow of $204.9 million. ETF activity reversed a modest...
- [Wall Street’s Financials Slipped As Treasury Yields Pushed Higher](https://finimize.com/content/wall-streets-financials-slipped-as-treasury-yields-pushed-higher)  
  <sub>Finimize, 15 hours ago</sub>  
  The 10-year US Treasury yield rose to 5.24% while the NYSE Financial Index fell 0.5% in Monday afternoon trading.
- [Bank of America Adds AI Tools to AskGPS, CashPro Platforms](https://www.benzinga.com/markets/large-cap/26/09/62031157/bank-of-america-adds-ai-tools-to-askgps-cashpro-platforms)  
  <sub>Benzinga, 22 hours ago</sub>  
  BofA unveils AI-driven treasury tools AskGPS Intelligence Hub and CashPro Payments Insights while BAC shares slide with broader market.
- [State Street SPDR S&P Biotech ETF (XBI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XBI/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Find the latest State Street SPDR S&P Biotech ETF (XBI) stock quote, history, news and other vital information to help you with your stock trading and...
- [Ares Management Stock: Is ARES Underperforming the Financial Service Sector?](https://www.inkl.com/news/ares-management-stock-is-ares-underperforming-the-financial-service-sector)  
  <sub>inkl, 23 hours ago</sub>  
  Although Ares Management has underperformed relative to the financial service sector over the past year, Wall Street analysts maintain a moderately…

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 53.96 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 56.22 (-4.0%), 50d 56.96 (-5.3%), 200d 53.73 (+0.4%); 50d above 200d
Momentum: RSI(14) 27.4 | MACD -0.819 vs signal -0.543 (histogram -0.277)
Returns: 1d -0.4% | 5d -1.5% | 1m -7.1% | 3m +0.6%
52-week range: 47.81 - 58.56 (now 57.2% of the way up)
Volatility: ATR(14) 0.70 (1.3% of price) | annualised 20d 13.5%
Volume: 0.24x the 20-day average
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
Three-year record: +19.4% a year | beta to the market 0.71
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 41.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.78 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.0% above the current prices
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
Shares outstanding: 883.44M | fund size: 47.67B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: analyst view modestly bullish but limited to 25.8% of the fund; fund flows flat indicating no net demand; technicals show price below short‑term SMAs and low RSI, suggesting weakness; fundamentals show high valuation for an industrial fund, tempering optimism; macro data unchanged with no surprise rate or inflation moves.

**Main reasons it gave:**
- Flat fund flows (share count +0.0% over 1 week) indicating neutral demand
- Price below 20‑day SMA (170.90) and 50‑day SMA (177.51) with RSI 36.3, showing technical weakness
- Analyst coverage limited to 25.8% of fund, all buy with +23.3% price target, providing modest bullish bias
- Macro environment unchanged: yields up, no surprise inflation or unemployment data

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Tuesday as Investors Weigh Tech Rebound](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131149164.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.2% and the actively trad.
- [ValuEngine Weekly Commentary: Sector And ETF Performance](https://seekingalpha.com/article/4950576-valuengine-weekly-commentary-sector-etf-performance)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  U.S. equity markets were mixed this week, with technology and growth-related areas leading, while several defensive and rate-sensitive sectors moved lower.
- [State Street SPDR S&P Biotech ETF (XBI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XBI/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Find the latest State Street SPDR S&P Biotech ETF (XBI) stock quote, history, news and other vital information to help you with your stock trading and...
- [GE Aerospace Secures Polish Defense Deal, But Broad Industrial Pullback Weighs on Shares](https://www.benzinga.com/markets/large-cap/26/09/62030830/ge-aerospace-secures-polish-defense-deal-but-broad-industrial-pullback-weighs-on-shares)  
  <sub>Benzinga, 22 hours ago</sub>  
  GE Aerospace Poland expansion adds local military engine support as industrial weakness and valuation pressure shares.
- [Why Is Rocket Lab Stock Falling Today?](https://www.aol.com/articles/why-rocket-lab-stock-falling-153417000.html)  
  <sub>AOL.com, 23 hours ago</sub>  
  Rocket Lab Corporation (NASDAQ: RKLB ) shares are trading lower Monday premarket, down about 1%, as aerospace and defense names slide—led by a sharper drop...
- [8 Of 11 Sectors Fall In Monday Trading As Defensives Lead](https://www.benzinga.com/etfs/sector-etfs/26/09/62026085/8-of-11-sectors-fall-in-monday-trading-as-defensives-lead)  
  <sub>Benzinga, 24 hours ago</sub>  
  Three sectors are higher and eight are lower in Monday's regular session, with defensive and cyclical sectors split across the top three positions.
- [Exchange-Traded Funds Lower as US Equities Decline After Midday](https://finance.yahoo.com/markets/articles/exchange-traded-funds-lower-us-172613363.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV fell. Actively traded Invesco QQQ Trust (QQQ) shed 1%.
- [State Street Financial Select Sector SPDR ETF (XLF) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLF/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Find the latest State Street Financial Select Sector SPDR ETF (XLF) stock quote, history, news and other vital information to help you with your stock...
- [SPDR S&P Biotech ETF (XBI) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/XBI/)  
  <sub>Yahoo Finance UK, 4 hours ago</sub>  
  Find the latest SPDR S&P Biotech ETF (XBI) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [State Street Health Care Select Sector SPDR ETF (XLV) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Find the latest State Street Health Care Select Sector SPDR ETF (XLV) stock quote, history, news and other vital information to help you with your stock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 168.89 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 170.90 (-1.2%), 50d 177.51 (-4.9%), 200d 172.17 (-1.9%); 50d above 200d
Momentum: RSI(14) 36.3 | MACD -2.435 vs signal -2.644 (histogram 0.209)
Returns: 1d +0.1% | 5d -0.8% | 1m -4.7% | 3m -8.8%
52-week range: 147.83 - 186.51 (now 54.4% of the way up)
Volatility: ATR(14) 2.27 (1.3% of price) | annualised 20d 12.5%
Volume: 0.24x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 25.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.77 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.3% above the current prices
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
Shares outstanding: 136.63M | fund size: 23.07B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral

**Main reasons it gave:**
- Fund flows flat: share count unchanged (+0.0% over 1 week)
- No macro catalyst: Treasury yields rose modestly, no policy surprise
- Technical indicators bullish but weak: price above 20‑day/50‑day/200‑day SMAs, RSI 62.8, volume 0.30× 20‑day average
- Recent news shows tech stocks falling, XLK down ~1% in recent sessions

<details><summary><b>News</b> — score +0.00</summary>

- [ValuEngine Weekly Commentary: Sector And ETF Performance](https://seekingalpha.com/article/4950576-valuengine-weekly-commentary-sector-etf-performance)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  U.S. equity markets were mixed this week, with technology and growth-related areas leading, while several defensive and rate-sensitive sectors moved lower.
- [Sector Update: Tech Stocks Fall Late Afternoon](https://ca.finance.yahoo.com/news/sector-tech-stocks-fall-afternoon-195704336.html)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Tech stocks were lower late Monday afternoon, with the State Street Technology Select Sector SPDR ETF (XLK) down 1% and the State Street SPDR S&P...
- [The Bond Bloodbath May Not Be Over](https://moneyandmarkets.com/the-bond-bloodbath-may-not-be-over/)  
  <sub>Money & Markets, 20 hours ago</sub>  
  Bonds and utilities have taken a beating as yields surged, but my system suggests it's still too early to call a reversal.
- ['An AI Operating System, Not a Chatbot': Oppenheimer Hails Microsoft's Enterprise Advantage](https://www.benzinga.com/markets/tech/26/09/62027202/an-ai-operating-system-not-a-chatbot-oppenheimer-hails-microsofts-enterprise-advantage)  
  <sub>Benzinga, 23 hours ago</sub>  
  Microsoft Corp. (NASDAQ: MSFT) stock remains a primary focus for investors as the company converts Copilot into a full-scale workplace AI platform.
- [Exchange-Traded Funds Lower as US Equities Decline After Midday](https://finance.yahoo.com/markets/articles/exchange-traded-funds-lower-us-172613363.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV fell. Actively traded Invesco QQQ Trust (QQQ) shed 1%.
- [CGGR: Lower Quality Active Growth ETF, But Better Positioned Than It Seems](https://seekingalpha.com/article/4950531-cggr-lower-quality-active-growth-etf-better-positioned-than-it-seems)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Capital Group Growth ETF's lower tech exposure has contributed to inferior returns since its February 2022 inception. Find out why CGGR is a Hold.
- [Sector Update: Tech Stocks Fall Monday Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-tech-stocks-fall-monday-175300431.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Tech stocks were lower Monday afternoon, with the State Street Technology Select Sector SPDR ETF (XLK) down 0.7% and the State Street SPDR S&P Semiconductor...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 195.65 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 189.32 (+3.3%), 50d 185.25 (+5.6%), 200d 164.15 (+19.2%); 50d above 200d
Momentum: RSI(14) 62.8 | MACD 2.986 vs signal 2.275 (histogram 0.711)
Returns: 1d +0.6% | 5d -0.3% | 1m +5.4% | 3m +2.7%
52-week range: 127.50 - 198.21 (now 96.4% of the way up)
Volatility: ATR(14) 3.20 (1.6% of price) | annualised 20d 18.7%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

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
Rolled up from the 5 largest holdings, 45.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.55 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.2% above the current prices
Holdings read: NVDA, AAPL, MSFT, AVGO, MU
Recent rating changes among them:
  - NVDA: 2026-09-29 Rosenblatt: main, Buy -> Buy
  - AAPL: 2026-09-23 B of A Securities: reit, Buy -> Buy
  - MSFT: 2026-09-23 Stifel: up, Hold -> Buy
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-09-28 Wedbush: reit, Outperform -> Outperform
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
Share count change: 1 week: +0.0% (0.00) over 12d
Shares outstanding: 272.06M | fund size: 53.23B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst consensus is offset by weak technicals, rising yields, and flat fund flows.

**Main reasons it gave:**
- 10-year Treasury yield rose 28 bps to 5.25% this week
- RSI(14) at 36 indicating weak momentum
- Analyst consensus: 100% buy rating with weighted price target +13.3% above current price
- Fund flows flat: share count unchanged over the past week

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Consumer Staples Select Sector SPDR ETF (XLP) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLP/)  
  <sub>Yahoo! Finance Canada, 12 hours ago</sub>  
  State Street Consumer Staples Select Sector SPDR ETF (XLP) ... This price reflects trading activity during the overnight session on the Blue Ocean ATS, available...
- [ValuEngine Weekly Commentary: Sector And ETF Performance](https://seekingalpha.com/article/4950576-valuengine-weekly-commentary-sector-etf-performance)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  U.S. equity markets were mixed this week, with technology and growth-related areas leading, while several defensive and rate-sensitive sectors moved lower.
- [Costco Earnings Ignite Case for Consumer Staples](https://etfdb.com/sector-investing-content-hub/costco-earnings-ignite-consumer-staples/)  
  <sub>ETF Database, 22 hours ago</sub>  
  Costco's earnings report and fiscal year operating results showcase why the consumer staples sector still has room for growth.
- [State Street Health Care Select Sector SPDR ETF (XLV) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) ... This price reflects trading activity during the overnight session on the Blue Ocean ATS, available 8 PM...
- [Global X Uranium UCITS ETF (URNUL.XC) latest stock news and headlines](https://au.finance.yahoo.com/quote/URNUL.XC/news/)  
  <sub>Yahoo Finance Australia, 20 hours ago</sub>  
  Get the latest Global X Uranium UCITS ETF (URNUL.XC) stock news and headlines to help you in your trading and investment decisions.
- [$700 Billion S&P 500 Sell-Off Meets $100 Oil: Are Investors Rotating Into Value ETFs?](https://www.benzinga.com/etfs/broad-u-s-equity-etfs/26/09/62031962/700-billion-sp-500-sell-off-meets-100-oil-are-investors-rotating-into-value-etfs)  
  <sub>Benzinga, 21 hours ago</sub>  
  S&P 500 erases nearly $700 billion as Treasury yields hit 19-year highs and oil nears $100, putting growth, value and energy ETFs in focus.
- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Tuesday as Investors Weigh Tech Rebound](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131149164.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.2% and the actively trad.
- [Sector Update: Consumer Stocks Mixed Monday Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-mixed-monday-180230880.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Consumer stocks were mixed Monday afternoon with the State Street Consumer Staples Select Sector SPDR ETF (XLP) rising 0.2% and the State Street Consumer...
- [Sector Update: Consumer](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-173410750.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Consumer stocks were mixed Monday afternoon with the State Street Consumer Staples Select Sector SPDR ETF (XLP) rising 0.1% and the State Street Consumer...
- [Sector Update: Consumer Stocks Mixed Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-mixed-afternoon-195108050.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Consumer stocks were mixed late Monday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) rising 0.3% and the State Street...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 81.31 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 83.32 (-2.4%), 50d 84.58 (-3.9%), 200d 83.71 (-2.9%); 50d above 200d
Momentum: RSI(14) 36.0 | MACD -0.858 vs signal -0.703 (histogram -0.156)
Returns: 1d -1.2% | 5d -1.7% | 1m -4.8% | 3m -2.1%
52-week range: 75.60 - 90.01 (now 39.6% of the way up)
Volatility: ATR(14) 0.98 (1.2% of price) | annualised 20d 11.4%
Volume: 0.32x the 20-day average
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
Three-year record: +8.4% a year | beta to the market 0.49
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 39.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.3% above the current prices
Holdings read: WMT, COST, KO, PG, PM
Recent rating changes among them:
  - WMT: 2026-09-29 Mizuho: main, Outperform -> Outperform
  - COST: 2026-09-28 Deutsche Bank: main, Buy -> Buy
  - KO: 2026-09-28 JP Morgan: main, Overweight -> Overweight
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
Shares outstanding: 210.17M | fund size: 17.09B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as macro pressure on rate‑sensitive utilities offsets bullish analyst coverage and solid fundamentals.

**Main reasons it gave:**
- 10‑year Treasury yield rose 28 bps this week, pressuring rate‑sensitive utilities
- XLU price below 20‑day, 50‑day and 200‑day SMAs; RSI 23.9 shows bearish momentum
- Fund flows flat (0 % change) over the past week, indicating no net demand
- Analyst coverage 39.4 % of fund weight shows 80.9 % buy rating and +25.9 % price target, but macro pressure dominates

<details><summary><b>News</b> — score +0.00</summary>

- [ValuEngine Weekly Commentary: Sector And ETF Performance](https://seekingalpha.com/article/4950576-valuengine-weekly-commentary-sector-etf-performance)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  U.S. equity markets were mixed this week, with technology and growth-related areas leading, while several defensive and rate-sensitive sectors moved lower.
- [$700 Billion S&P 500 Sell-Off Meets $100 Oil: Are Investors Rotating Into Value ETFs?](https://www.benzinga.com/etfs/broad-u-s-equity-etfs/26/09/62031962/700-billion-sp-500-sell-off-meets-100-oil-are-investors-rotating-into-value-etfs)  
  <sub>Benzinga, 21 hours ago</sub>  
  S&P 500 erases nearly $700 billion as Treasury yields hit 19-year highs and oil nears $100, putting growth, value and energy ETFs in focus.
- [State Street Health Care Select Sector SPDR ETF (XLV) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Find the latest State Street Health Care Select Sector SPDR ETF (XLV) stock quote, history, news and other vital information to help you with your stock...
- [The Bond Bloodbath May Not Be Over](https://moneyandmarkets.com/the-bond-bloodbath-may-not-be-over/)  
  <sub>Money & Markets, 20 hours ago</sub>  
  Bonds and utilities have taken a beating as yields surged, but my system suggests it's still too early to call a reversal.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 39.31 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 41.41 (-5.1%), 50d 43.03 (-8.6%), 200d 44.43 (-11.5%); 50d below 200d
Momentum: RSI(14) 23.9 | MACD -1.086 vs signal -0.890 (histogram -0.196)
Returns: 1d +0.2% | 5d -3.0% | 1m -8.0% | 3m -13.3%
52-week range: 39.25 - 47.73 (now 0.8% of the way up)
Volatility: ATR(14) 0.59 (1.5% of price) | annualised 20d 13.9%
Volume: 0.49x the 20-day average
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
Three-year record: +11.0% a year | beta to the market 0.43
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
Weighted price target: +25.9% above the current prices
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

> No material macro or data surprise, flat fund flows, and technicals lack decisive break; despite a strongly bullish analyst view, the overall picture remains neutral.

**Main reasons it gave:**
- Analyst view: 100% buy rating, weighted price target +10.9% above current price
- Fund flows flat: 0% share count change over 1 week
- Technicals: price above 200‑day SMA (+8.1%) but low volume (0.25× avg) and recent 1‑day decline (-1.2%)
- Macro: Treasury yields up across curve, no surprise data releases

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Health Care Select Sector SPDR ETF (XLV) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) ... This price reflects trading activity during the overnight session on the Blue Ocean ATS, available 8 PM...
- [These ten healthcare stocks posted the biggest September gains (XLV:NYSEARCA)](https://seekingalpha.com/news/4647929-these-ten-healthcare-stocks-posted-the-biggest-september-gains)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Top 10 healthcare stocks surging in Sept 2026—KOD, GRAL, SDGR lead with big 1-month gains, plus Quant Ratings and ETF ideas.
- [ValuEngine Weekly Commentary: Sector And ETF Performance](https://seekingalpha.com/article/4950576-valuengine-weekly-commentary-sector-etf-performance)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  U.S. equity markets were mixed this week, with technology and growth-related areas leading, while several defensive and rate-sensitive sectors moved lower.
- [8 Of 11 Sectors Fall In Monday Trading As Defensives Lead](https://www.benzinga.com/etfs/sector-etfs/26/09/62026085/8-of-11-sectors-fall-in-monday-trading-as-defensives-lead)  
  <sub>Benzinga, 24 hours ago</sub>  
  Three sectors are higher and eight are lower in Monday's regular session, with defensive and cyclical sectors split across the top three positions.
- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Tuesday as Investors Weigh Tech Rebound](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131149164.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.2% and the actively trad.
- [XHE: Health Care Equipment Likely To Underperform Amid Higher Rates (Downgrade)](https://seekingalpha.com/article/4950473-xhe-health-care-equipment-likely-to-underperform-amid-higher-rates-downgrade-hold?source=feed_all_articles)  
  <sub>Seeking Alpha, 13 hours ago</sub>  
  I downgrade the State Street SPDR S&P Health Care Equipment ETF to a Hold. I expect XHE to underperform IVV into 2027, as its factor mix heavy in expensive...
- [Biotech Bull Market Opportunities: Away From The Madding Crowd Of Compute? - TalkMarkets](https://t.co/MioCvOKXb0)  
  <sub>Howl.Link, 12 hours ago</sub>  
  Biotech ETFs are outperforming the S&P 500 as innovation and M&A fuel a sector breakout.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 169.24 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 169.16 (+0.0%), 50d 168.11 (+0.7%), 200d 156.51 (+8.1%); 50d above 200d
Momentum: RSI(14) 50.7 | MACD 0.409 vs signal 0.354 (histogram 0.055)
Returns: 1d -1.2% | 5d -0.4% | 1m -1.1% | 3m +6.7%
52-week range: 135.90 - 175.68 (now 83.8% of the way up)
Volatility: ATR(14) 2.42 (1.4% of price) | annualised 20d 13.8%
Volume: 0.25x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.9% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-09-28 JP Morgan: main, Overweight -> Overweight
  - JNJ: 2026-09-29 JP Morgan: main, Neutral -> Neutral
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
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 197.42M | fund size: 33.41B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 114.11 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 111.43 (+2.4%), 50d 105.98 (+7.7%), 200d 88.00 (+29.7%); 50d above 200d
Momentum: RSI(14) 60.1 | MACD 2.199 vs signal 2.081 (histogram 0.118)
Returns: 1d -0.1% | 5d -0.9% | 1m +5.8% | 3m +5.1%
52-week range: 60.03 - 115.64 (now 97.2% of the way up)
Volatility: ATR(14) 2.20 (1.9% of price) | annualised 20d 27.0%
Volume: 0.20x the 20-day average
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
Weighted price target: +29.0% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 85.00M | fund size: 9.70B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### United Kingdom (EWU) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: The read operation timed out (gave up after 2 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 46.74 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 47.73 (-2.1%), 50d 48.03 (-2.7%), 200d 46.63 (+0.2%); 50d above 200d
Momentum: RSI(14) 36.4 | MACD -0.293 vs signal -0.191 (histogram -0.102)
Returns: 1d -1.1% | 5d -2.0% | 1m -3.7% | 3m +1.3%
52-week range: 41.34 - 49.39 (now 67.0% of the way up)
Volatility: ATR(14) 0.46 (1.0% of price) | annualised 20d 11.7%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

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
Rolled up from the 5 largest holdings, 36.0% of the fund by weight
Ratings by weight: buy 69.5% | hold 30.5% | sell 0.0% (mean 2.17 on a 1=strong buy to 5=strong sell scale)
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
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 67.80M | fund size: 3.17B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 70.12 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 72.78 (-3.7%), 50d 74.68 (-6.1%), 200d 70.55 (-0.6%); 50d above 200d
Momentum: RSI(14) 31.4 | MACD -1.167 vs signal -0.932 (histogram -0.235)
Returns: 1d -0.6% | 5d -1.5% | 1m -5.6% | 3m -6.3%
52-week range: 58.14 - 77.93 (now 60.5% of the way up)
Volatility: ATR(14) 1.15 (1.6% of price) | annualised 20d 16.4%
Volume: 0.18x the 20-day average
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
Weighted price target: +22.4% above the current prices
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
Share count change: 1 week: +1.8% (68.22M) over 7d
Shares outstanding: 56.11M | fund size: 3.93B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [The 'Funflation' Effect: What It May Mean for Retail Stocks](https://etfdb.com/equity-etf-content-hub/funflation-effect-means-retail/)  
  <sub>ETF Database, 2 hours ago</sub>  
  Inflation may be a burden on the wallets of businesses and consumers alike, but “funflation” already sounds like a much more whimsical prospect.
- [ValuEngine Weekly Commentary: Sector And ETF Performance](https://seekingalpha.com/article/4950576-valuengine-weekly-commentary-sector-etf-performance)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  U.S. equity markets were mixed this week, with technology and growth-related areas leading, while several defensive and rate-sensitive sectors moved lower.
- [Carnival jumps on strong results but trails travel stocks in Quant ratings (XLY:NYSEARCA)](https://seekingalpha.com/news/4648064-carnival-jumps-on-strong-results-but-trails-travel-stocks-in-quant-ratings)  
  <sub>Seeking Alpha, 52 minutes ago</sub>  
  Carnival's latest quarterly performance has put renewed focus on cruise operators within the broader travel sector, with strong bookings, record revenue and...
- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Tuesday as Investors Weigh Tech Rebound](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131149164.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.2% and the actively trad.
- [Sector Update: Consumer Stocks Mixed Monday Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-mixed-monday-180230880.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Consumer stocks were mixed Monday afternoon with the State Street Consumer Staples Select Sector SPDR ETF (XLP) rising 0.2% and the State Street Consumer...
- [Sector Update: Consumer](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-173410750.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Consumer stocks were mixed Monday afternoon with the State Street Consumer Staples Select Sector SPDR ETF (XLP) rising 0.1% and the State Street Consumer...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 108.88 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 112.12 (-2.9%), 50d 114.58 (-5.0%), 200d 116.55 (-6.6%); 50d below 200d
Momentum: RSI(14) 33.9 | MACD -1.640 vs signal -1.414 (histogram -0.227)
Returns: 1d -0.1% | 5d -3.1% | 1m -7.1% | 3m -7.2%
52-week range: 105.66 - 124.52 (now 17.1% of the way up)
Volatility: ATR(14) 1.53 (1.4% of price) | annualised 20d 15.5%
Volume: 0.25x the 20-day average
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
Weighted price target: +27.1% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, BKNG
Recent rating changes among them:
  - AMZN: 2026-09-03 Wells Fargo: main, Overweight -> Overweight
  - TSLA: 2026-09-28 JP Morgan: main, Neutral -> Neutral
  - HD: 2026-09-09 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-09-29 JP Morgan: main, Overweight -> Overweight
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
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 120.25M | fund size: 13.09B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- Crowded long position (100% percentile) among large speculators
- Heavy cost of holding fund vs sugar (-10.3% annual) indicating drag on long exposure
- Recent outflows: share count down 1.5% over 7 days
- No macro surprise; yields up modestly, no policy shift

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 11.41 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 11.38 (+0.2%), 50d 10.84 (+5.2%), 200d 9.95 (+14.6%); 50d above 200d
Momentum: RSI(14) 56.8 | MACD 0.084 vs signal 0.130 (histogram -0.047)
Returns: 1d +1.6% | 5d +1.8% | 1m +1.8% | 3m +16.5%
52-week range: 9.02 - 11.82 (now 85.4% of the way up)
Volatility: ATR(14) 0.19 (1.7% of price) | annualised 20d 22.1%
Volume: 0.41x the 20-day average
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
Cost of holding this fund instead of sugar itself: -10.3% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +16.5%, commodity +32.1%, gap -15.6% | 6 months: fund +8.9%, commodity +21.9%, gap -13.0% | 12 months: fund +9.1%, commodity +19.4%, gap -10.3%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 18.9% of open interest (1,147,767 contracts)
Change on the week: +0.4% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -1.5% (-892.57K) over 7d
Shares outstanding: 5.18M | fund size: 59.15M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral

**Main reasons it gave:**
- No macro surprise: inflation 3.4% in line with expectations, yields rose modestly across the curve
- Technical: price above 50‑day and 200‑day SMA but below 20‑day SMA; RSI 47.8 (neutral)
- Positioning: net long 21.8% of OI, crowding at 95th percentile, weekly change -0.7% of OI
- Cost of holding: heavy roll cost -12.6% annual, tailwind for short

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 19.50 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 19.92 (-2.2%), 50d 19.02 (+2.5%), 200d 18.12 (+7.6%); 50d above 200d
Momentum: RSI(14) 47.8 | MACD 0.147 vs signal 0.275 (histogram -0.128)
Returns: 1d -0.2% | 5d -2.4% | 1m -2.3% | 3m +16.4%
52-week range: 16.47 - 20.29 (now 79.2% of the way up)
Volatility: ATR(14) 0.30 (1.5% of price) | annualised 20d 15.2%
Volume: 0.14x the 20-day average
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
Cost of holding this fund instead of corn itself: -12.6% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +16.4%, commodity +26.0%, gap -9.7% | 6 months: fund +6.6%, commodity +14.2%, gap -7.6% | 12 months: fund +10.6%, commodity +23.3%, gap -12.6%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.10</summary>

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
Direction: flat (1 week)
Share count change: 1 week: -0.2% (-378.47K) over 7d
Shares outstanding: 8.36M | fund size: 162.90M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data unreachable: The read operation timed out

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals show no decisive break, speculator net‑long is modest, heavy roll cost and recent outflows offset bullish sentiment.

**Main reasons it gave:**
- Positioning: large speculators net long 27.4% of open interest, up 4.9% week‑over‑week (moderate bullish sentiment)
- Cost of holding: -5.4% annual roll cost (heavy cost, bearish for long positions)
- Fund flows: 1.2% share count decline over 7 days (outflows indicating reduced demand)
- Technicals: price near 20‑day/50‑day SMA, RSI 48.5, MACD barely positive, low volume (no decisive break)
- Macro: dollar index up 0.79% and Treasury yields rising, adding pressure on copper

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 39.70 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 39.85 (-0.4%), 50d 39.74 (-0.1%), 200d 37.35 (+6.3%); 50d above 200d
Momentum: RSI(14) 48.5 | MACD 0.161 vs signal 0.159 (histogram 0.002)
Returns: 1d +0.1% | 5d -4.2% | 1m +0.1% | 3m +5.2%
52-week range: 30.00 - 41.43 (now 84.9% of the way up)
Volatility: ATR(14) 0.69 (1.7% of price) | annualised 20d 29.6%
Volume: 0.19x the 20-day average
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
Cost of holding this fund instead of copper itself: -5.4% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +5.2%, commodity +7.1%, gap -1.9% | 6 months: fund +18.2%, commodity +21.1%, gap -2.9% | 12 months: fund +35.2%, commodity +40.6%, gap -5.4%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

```text
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 27.4% of open interest (301,657 contracts)
Change on the week: +4.9% of open interest
Crowding: 88% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -1.2% (-8.69M) over 7d
Shares outstanding: 18.49M | fund size: 733.97M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- Silver price below 20‑day, 50‑day and 200‑day SMAs, indicating a downtrend
- US Treasury yields rose across the curve and dollar index up, raising opportunity cost for non‑yielding assets
- Cost of holding fund -1.4% annual drag, a modest negative for long exposure
- Positioning net long 12.5% with -0.2% weekly change, showing no strong crowding or directional shift

<details><summary><b>News</b> — score +0.00</summary>

- [Should You Invest in Gold and Silver ETFs When Markets Are Falling?](https://www.indmoney.com/blog/mutual-funds/gold-silver-etfs-falling-market)  
  <sub>INDmoney, 5 hours ago</sub>  
  Should you buy gold or silver ETFs in a falling market? Compare their risks, portfolio roles and key checks using the September 2026 sell-off.
- [Pan American Silver Corp. (PAAS) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/PAAS/)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  Find the latest Pan American Silver Corp. (PAAS) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Comex Update: 400oz Gold Contract Cancelled; Silver Demand Strengthens](https://seekingalpha.com/article/4950568-comex-update-400oz-gold-contract-cancelled-silver-demand-strengthens)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  Since January of 2025, the gold market has seen elevated delivery volume far surpassing what had been seen in years past. Read more here.
- [Silver Price Outlook: Treasury Yields, China Supply and Key Levels](https://www.equiti.com/uae-en/news/trade-reviews/silver-price-outlook-treasury-yields-china-exports/)  
  <sub>www.equiti.com, 4 hours ago</sub>  
  Silver faces pressure from rising Treasury yields and ETF outflows, while tighter Chinese export rules support physical supply concerns.
- [Silver ETFs Slide Nearly 4% As Oil Surge Triggers Bullion Sell-off](https://www.tradingview.com/news/moodys:f50eb34246d41:0-silver-etfs-slide-nearly-4-as-oil-surge-triggers-bullion-sell-off/)  
  <sub>TradingView, 24 hours ago</sub>  
  The decline in domestic precious-metal ETFs track a sharp correction in international bullion pricesGold and silver exchange-traded funds (ETFs) came under...
- [Gold And Silver Just Got Slammed... But Something Doesn't Add Up](https://seekingalpha.com/article/4950329-gold-silver-just-got-slammed-something-doesnt-add-up)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Gold and silver investors woke up to another ugly morning. Gold fell below $4,200 an ounce in early trading, down nearly 3% at one point, while silver was...
- [Silver Price Falls Rs 2,601 to Rs 2.25 Lakh on MCX](https://hdfcsky.com/news/silver-price-today-mcx-silver-falls-1-14percent-to-rs-2-25-lakh)  
  <sub>HDFC Sky, 9 hours ago</sub>  
  Silver prices fell Rs 2601 to Rs 2,24841 per kg on MCX as participants cut bets. Global silver also declined 0.15% to USD 60.55 an ounce.
- [Nuclear Energy Ambitions Opens Up Growth for Uranium Miners](https://www.etftrends.com/gold-silver-content-hub/nuclear-energy-ambitions-growth-uranium-miners/)  
  <sub>ETF Trends, 21 hours ago</sub>  
  Uranium mining equities have been back on the rise as of late. Key Takeaways: Recent insights from the Sprott team show that uranium miners and junior...
- [Bears Take Over Mining Stocks Sentiment Monday September 28th](https://www.investorideas.com/news/2026/mining/09283-bears-take-over-mining-stocks-sentiment-monday-september-28th.asp)  
  <sub>Investorideas.com, 24 hours ago</sub>  
  Gold and silver fall Monday as leveraged bearish ETFs ZSL, JDST and DUST make the NYSE top gainers list amid rate-hike speculation.
- [Why are gold and silver prices falling? How oil prices, US interest rates are driving the decline | Business News](https://www.hindustantimes.com/business/why-gold-and-silver-prices-are-falling-amid-rising-oil-prices-and-higher-us-interest-rates-101790655662228.html)  
  <sub>Hindustan Times, 10 hours ago</sub>  
  Gold and silver prices are falling as higher oil prices, US Treasury yields and a stronger dollar raise concerns over further Fed rate hikes.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 55.04 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 58.38 (-5.7%), 50d 57.63 (-4.5%), 200d 65.95 (-16.5%); 50d below 200d
Momentum: RSI(14) 39.9 | MACD -0.528 vs signal -0.038 (histogram -0.490)
Returns: 1d +0.2% | 5d -9.4% | 1m -8.3% | 3m +2.9%
52-week range: 42.37 - 105.60 (now 20.0% of the way up)
Volatility: ATR(14) 1.79 (3.2% of price) | annualised 20d 41.7%
Volume: 0.34x the 20-day average
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
Cost of holding this fund instead of silver itself: -1.4% a year -- a steady drag
Measured: 3 months: fund +2.9%, commodity +3.3%, gap -0.4% | 6 months: fund -13.3%, commodity -12.6%, gap -0.7% | 12 months: fund +31.5%, commodity +32.9%, gap -1.4%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 12.5% of open interest (106,474 contracts)
Change on the week: -0.2% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 341.45M | fund size: 18.80B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals not decisive, mixed fundamentals

**Main reasons it gave:**
- Crowded long position (97th percentile) with modest weekly increase (+1.9% OI)
- Fund outflows: share count down 0.9% over 7 days
- Cost of holding fund is a slight drag (-1.3% annual)
- Crop condition steady (58% good/excellent, down 4 points vs last year)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 27.50 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 27.80 (-1.1%), 50d 26.57 (+3.5%), 200d 24.55 (+12.0%); 50d above 200d
Momentum: RSI(14) 52.5 | MACD 0.311 vs signal 0.443 (histogram -0.132)
Returns: 1d +0.5% | 5d -2.1% | 1m +1.1% | 3m +12.7%
52-week range: 21.46 - 28.14 (now 90.4% of the way up)
Volatility: ATR(14) 0.34 (1.2% of price) | annualised 20d 16.9%
Volume: 0.39x the 20-day average
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
Cost of holding this fund instead of soybeans itself: -1.3% a year -- a steady drag
Measured: 3 months: fund +12.7%, commodity +16.0%, gap -3.3% | 6 months: fund +13.8%, commodity +11.7%, gap +2.1% | 12 months: fund +26.5%, commodity +27.8%, gap -1.3%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.10</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 23.8% of open interest (1,114,328 contracts)
Change on the week: +1.9% of open interest
Crowding: 97% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -0.9% (-407.75K) over 7d
Shares outstanding: 1.66M | fund size: 45.67M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, mixed fundamentals and positioning lead to a neutral stance.

**Main reasons it gave:**
- Positioning: net short 3.6% of OI, weekly increase +1.9% (slight bearish sentiment)
- Cost of holding: -23% annual roll cost (tailwind for short)
- Inventory build: +53 BCF (73% percentile) indicating bearish supply
- Technicals: price below 20‑day SMA, 50‑day SMA below 200‑day SMA (mixed bearish)
- Price outlook: EIA forecasts 7% rise over six months (bullish)

<details><summary><b>News</b> — score +0.00</summary>

- [Markets shrug at Trump’s nuclear relief offer to Iran](https://seekingalpha.com/news/4647741-markets-shrug-at-trump-s-nuclear-relief-offer-to-iran)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Kalshi odds show low confidence in a near U.S.-Iran nuclear deal despite Trump hinting at sanctions relief.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 10.45 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 10.56 (-1.0%), 50d 10.29 (+1.6%), 200d 11.39 (-8.2%); 50d below 200d
Momentum: RSI(14) 48.5 | MACD 0.145 vs signal 0.115 (histogram 0.030)
Returns: 1d -3.1% | 5d -3.7% | 1m +1.2% | 3m -10.8%
52-week range: 9.63 - 16.90 (now 11.3% of the way up)
Volatility: ATR(14) 0.37 (3.6% of price) | annualised 20d 43.3%
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
Cost of holding this fund instead of natural gas itself: -23.0% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -10.8%, commodity -7.5%, gap -3.3% | 6 months: fund -10.5%, commodity +4.9%, gap -15.4% | 12 months: fund -16.2%, commodity +6.8%, gap -23.0%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.30</summary>

```text
US inventories, week ending 2026-09-18 (published the following Wednesday)
  Natural gas: 3,351.0 billion cubic feet, +53.0 on the week (a build), 73% percentile over 52 weeks
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
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 12.08M | fund size: 126.34M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows no strong directional catalyst. A modest bearish bias comes from a crude inventory build and a bearish EIA price outlook, while positioning is neutral due to a crowded long with minimal change. No macro surprise or decisive technical break is present.

**Main reasons it gave:**
- Crude inventories built 3.0 million barrels (bearish)
- EIA forecasts WTI price to fall to $84.5 in 3 months (bearish)
- Saudi Arabia restarts Hormuz‑bypassing pipeline exports, easing supply concerns (bearish)
- CFTC large speculators net long 5.5% of OI, crowding at 98th percentile (neutral)

<details><summary><b>News</b> — score +0.00</summary>

- [USO ETF Parent Has a New Suitor: Is a Bidding War Brewing? - United States Oil Fund (ARCA:USO)](https://www.benzinga.com/etfs/specialty-etfs/26/09/62034960/uso-etf-parent-has-a-new-suitor-is-a-bidding-war-brewing)  
  <sub>Benzinga, 19 hours ago</sub>  
  Simplify has raised its bid for Marygold, fueling a potential bidding war for USCF's $6B ETF platform after Madison Dearborn's bid.
- [Berkshire’s Delta Bet Shows Why Quality Matters In Airline Stocks](https://seekingalpha.com/article/4950620-berkshires-delta-bet-shows-why-quality-matters-in-airline-stocks)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Berkshire's $5.4B Delta stake signals airline confidence. Airline valuations remain modest at 9–11x forward earnings. See here for more details.
- [Simplify Tops Madison Dearborn With a Rival Bid for USCF](https://www.etf.com/sections/features/simplify-tops-madison-dearborn-rival-bid-uscf)  
  <sub>ETF.com, 20 hours ago</sub>  
  A bidding war has broken out for the firm behind USO.
- [Oil Rises; Meta’s Muse Trade Extends To CPU Stocks Like Intel, AMD, Arm, Qualcomm](https://www.benzinga.com/Opinion/26/09/62031079/oil-rises-meta-muse-trade-extends-to-cpu-stocks-like-intel-amd-arm-qualcomm)  
  <sub>Benzinga, 22 hours ago</sub>  
  Iran Hopium Dashed Please click here for an enlarged chart of the United States Oil ETF (NYSE:USO). Note the following: The chart shows that this morning in...
- [Saudi Arabia restarts oil exports through Hormuz-bypassing pipeline (USO:NYSEARCA)](https://seekingalpha.com/news/4647743-saudi-arabia-restarts-oil-exports-through-hormuz-bypassing-pipeline)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Saudi Arabia resumes East-West pipeline exports via Yanbu after drone attacks, easing oil supply fears and price risk as Hormuz stays vulnerable.
- [Iran's Supreme Leader Says US Won't Dare to Advance Beyond Arabian Sea While Trump Confirms Talks With Me](https://www.benzinga.com/news/politics/26/09/62041379/irans-supreme-leader-says-us-wont-dare-to-advance-beyond-arabian-sea-while-trump-confirms-talks-with-mediators)  
  <sub>Benzinga, 7 hours ago</sub>  
  Iran's leader says enemies will be expelled from the Middle East after Hormuz strikes as reports say eight U.S. Marines were injured.
- ['Open the Strait': Texas firms warn Middle East chaos reigniting inflation (US10Y:) (US10Y:) (TLT:NASDAQ)](https://seekingalpha.com/news/4647727-open-the-strait-texas-firms-warn-middle-east-chaos-reigniting-inflation)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Escalating war in the Middle East and spiking energy (USO) (BNO) prices threaten to reignite domestic inflation and disrupt commercial planning,...
- [Markets shrug at Trump’s nuclear relief offer to Iran](https://seekingalpha.com/news/4647741-markets-shrug-at-trump-s-nuclear-relief-offer-to-iran)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Kalshi odds show low confidence in a near U.S.-Iran nuclear deal despite Trump hinting at sanctions relief.
- [Dow Soars Over 600 Points, Crude Oil Prices Plummet Amid A Pause In Iran Strikes](https://stocktwits.com/news-articles/markets/equity/dow-soars-crude-oil-prices-plummet-amid-pause-us-iran-strikes/cZZxStUR76d)  
  <sub>Stocktwits, 11 hours ago</sub>  
  The S&P 500 index gained about 0.8%, while the Nasdaq Composite rose about 0.7%.
- [Trump denies report on potential sanctions relief for Iran](https://seekingalpha.com/news/4647869-trump-denies-report-on-potential-sanctions-relief-for-iran)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  Trump denies offering Iran sanctions relief or asset unfreezing for nuclear concessions as Hormuz talks stall.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 147.40 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 149.96 (-1.7%), 50d 136.59 (+7.9%), 200d 114.01 (+29.3%); 50d above 200d
Momentum: RSI(14) 52.5 | MACD 3.951 vs signal 5.342 (histogram -1.391)
Returns: 1d -1.7% | 5d +2.3% | 1m +13.6% | 3m +38.5%
52-week range: 66.17 - 161.86 (now 84.9% of the way up)
Volatility: ATR(14) 5.37 (3.6% of price) | annualised 20d 45.6%
Volume: 0.42x the 20-day average
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
US inventories, week ending 2026-09-18 (published the following Wednesday)
  Crude oil: 426.4 million barrels, +3.0 on the week (a build), 58% percentile over 52 weeks
  Petrol: 206.0 million barrels, -1.7 on the week (a draw), 8% percentile over 52 weeks -- low for the time of year
  Diesel: 107.4 million barrels, -0.4 on the week (a draw), 33% percentile over 52 weeks
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
Share count change: 1 week: +0.0% (0.00) over 11d
Shares outstanding: 119.10M | fund size: 17.56B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise or decisive technical break; mixed signals lead to a neutral stance.

**Main reasons it gave:**
- Technical indicators (RSI 38.5, MACD negative) suggest bearish momentum
- CFTC positioning shows net short decreasing by 1.7% of open interest, a modest bullish signal
- Cost of holding is heavy (-13.2% annual), bearish for long positions
- Fund flows positive (+1.6% share count) indicating demand for exposure

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 24.90 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 26.29 (-5.3%), 50d 25.56 (-2.6%), 200d 23.12 (+7.7%); 50d above 200d
Momentum: RSI(14) 38.5 | MACD -0.145 vs signal 0.101 (histogram -0.246)
Returns: 1d -0.3% | 5d -4.2% | 1m -11.1% | 3m +13.0%
52-week range: 19.88 - 28.00 (now 61.8% of the way up)
Volatility: ATR(14) 0.55 (2.2% of price) | annualised 20d 22.4%
Volume: 0.18x the 20-day average
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
Cost of holding this fund instead of wheat itself: -13.2% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +13.0%, commodity +18.2%, gap -5.2% | 6 months: fund +7.1%, commodity +13.1%, gap -6.0% | 12 months: fund +18.9%, commodity +32.1%, gap -13.2%
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
Share count change: 1 week: +1.6% (5.60M) over 7d
Shares outstanding: 14.23M | fund size: 354.30M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Higher rates are wreaking havoc on these two ETFs. Traders see one bouncing back](https://www.cnbc.com/amp/2026/09/29/higher-rates-are-wreaking-havoc-on-these-two-etfs-traders-see-one-bouncing-back.html)  
  <sub>CNBC, 4 hours ago</sub>  
  The relentless surge in rates is breaking the back of two key macro trades that had been holding firm.
- [A Bullion Bounce Would Propel This ETF](https://www.etftrends.com/leveraged-inverse-content-hub/bullion-bounce-propel-ugld-etf/)  
  <sub>ETF Trends, 3 hours ago</sub>  
  If central bank softens its tone on rate hikes, gold and the related ETFs could benefit. That'd be good news for UGLD.
- [Comex Update: 400oz Gold Contract Cancelled; Silver Demand Strengthens](https://seekingalpha.com/article/4950568-comex-update-400oz-gold-contract-cancelled-silver-demand-strengthens)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  Since January of 2025, the gold market has seen elevated delivery volume far surpassing what had been seen in years past. Read more here.
- [Gold drops 4% amid rising yields; traders bulli...](https://pluang.com/en/news-feed/tingginya-suku-bunga-berdampak-pada-etf-hyg-dan-gld-pedagang-optimis-salah-satu)  
  <sub>Pluang, 4 hours ago</sub>  
  Gold prices fell 4% to their lowest since early August as 10-year and 30-year Treasury yields rose above 5.3% and 5.4%, respectively.
- [CFTC CoTs: Managed Money No Longer Driving Price Moves](https://seekingalpha.com/article/4950553-cftc-cots-managed-money-no-longer-driving-price-moves)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  Managed Money started accumulating in May and was buying into the price weakness. After the recent peak in late August, Managed Money has been dropping...
- [Gold & Silver Just Got Slammed... But Something Doesn't Add Up](https://seekingalpha.com/article/4950329-gold-silver-just-got-slammed-something-doesnt-add-up?source=feed_all_articles)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Gold and silver investors woke up to another ugly morning. Gold fell below $4,200 an ounce in early trading, down nearly 3% at one point, while silver was...
- [GLD 8-K & SEC Filings](https://finance.yahoo.com/sec-filing/GLD/0001437749-26-031296_1222333)  
  <sub>Yahoo Finance, 15 hours ago</sub>  
  SEC Gov • Sep 28, 2026. GLD : 8-K : Corporate Changes & Voting Matters. Exhibits Related Filings. Copyright © 2026 Yahoo. All rights reserved.
- [Gold Price Forecast — XAU/USD ($4,146) Plunges 3.3% as 5.22% Yields — $4,000 Test or $4,300 Rebound After PCE](https://www.tradingnews.com/news/gold-4146-usd-breaks-below-4200-usd-as-oil-rips-to-96-usd)  
  <sub>TradingNEWS, 23 hours ago</sub>  
  Trading News Gold drops 3.3% to $4146 an ounce, its lowest since August 5, as the 10-year Treasury hits 5.22% and October hike odds jump to 70.3% | That's.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.09 on the week) | 5-year 5.07% (+0.23 on the week) | 10-year 5.25% (+0.28 on the week) | 30-year 5.58% (+0.28 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 101.39 (+0.79 on the week)
Volatility (VIX): 15.89 (+1.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.81% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 381.34 (bar of 2026-09-29), from 501 daily bars
Trend: vs 20d SMA 396.43 (-3.8%), 50d 395.90 (-3.7%), 200d 416.35 (-8.4%); 50d below 200d
Momentum: RSI(14) 38.5 | MACD -3.973 vs signal -1.647 (histogram -2.326)
Returns: 1d +0.9% | 5d -4.7% | 1m -6.7% | 3m +3.5%
52-week range: 352.46 - 495.90 (now 20.1% of the way up)
Volatility: ATR(14) 7.45 (2.0% of price) | annualised 20d 24.7%
Volume: 0.37x the 20-day average
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
Cost of holding this fund instead of gold itself: -1.3% a year -- a steady drag
Measured: 3 months: fund +3.5%, commodity +3.9%, gap -0.4% | 6 months: fund -8.0%, commodity -6.6%, gap -1.4% | 12 months: fund +10.0%, commodity +11.3%, gap -1.3%
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
Shares outstanding: 260.30M | fund size: 99.26B
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

