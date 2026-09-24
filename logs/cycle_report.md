# Daily report

**24 Sep 2026, 18:36 Israel time (15:36 UTC)** · 80 names checked · 0 traded · 58 with a problem

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 0 | 12 | 4 |
| Whole-market funds | 14 | 0 | 6 | 8 |
| Sector and country funds | 41 | 0 | 3 | 38 |
| Commodities | 9 | 0 | 1 | 8 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| Developing country bonds (EMB) · Index fund | **Sold part.** Sold 42 of 128 shares at +1.14R, 86 still held. Stop-loss raised 93.91 → 93.39. |
| US inflation-linked bonds (TIP) · Index fund | **Sold part.** Sold 3 of 10 shares at +2.11R, 7 still held. Stop-loss raised 105.79 → 105.39. |
| US dollar (UUP) · Index fund | **Sold part.** Sold 140 of 422 shares at +1.56R, 282 still held. Stop-loss raised 28.41 → 28.50. |
| US government bonds, 7-10 years (IEF) · Index fund | **Trimmed.** Sold 11 of 131 shares to bring its exposure group back under its cap, 120 still held. Stop-loss 91.28. |
| US government bonds, 20+ years (TLT) · Index fund | **Trimmed.** Sold 12 of 147 shares to bring its exposure group back under its cap, 135 still held. Stop-loss 82.41. |
| Gold (GLD) · Commodity | **Stop raised.** At -0.02R, following the price. Stop-loss raised 404.87 → 403.77. |
| US regional banks (KRE) · Sector or country | **Stop raised.** At +0.47R, following the price. Stop-loss raised 73.60 → 72.54. |
| Eli Lilly (LLY) · Company | **Stop raised.** At +0.76R, following the price. Stop-loss raised 1113.34 → 1130.70. |
| Novo Nordisk (NVO) · Company | **Stop raised.** At +0.45R, following the price. Stop-loss raised 41.27 → 41.12. |
| Procter & Gamble (PG) · Company | **Stop raised.** At +0.07R, following the price. Stop-loss raised 142.78 → 143.18. |
| S&P 500, equal weight (RSP) · Index fund | **Stop raised.** At +0.41R, following the price. Stop-loss raised 215.68 → 214.01. |
| US shopping and leisure (XLY) · Sector or country | **Stop raised.** At +0.06R, following the price. Stop-loss raised 113.36 → 113.13. |
| Exxon Mobil (XOM) · Company | **Stop raised.** At +0.38R, following the price. Stop-loss raised 153.51 → 156.50. |
| US government bonds, 7-10 years (IEF) · Index fund | **Problem.** Could not be managed: BrokerError: replace_order failed for a0068ce2-7d62-41c6-aad8-f1e291ab09a0: {"available":"120","code":40310000,"existing_qty":"123","held_for_orders":"3","message":"insufficient qty available for order (requested: 131, available: 120)","related_orders":["a0068ce2-7d62-41c6-aad8-f1e291ab09a0","d93f0fef-d9eb-4fa9-9935-04e1efb6e58c"],"symbol":"IEF"} |
| US government bonds, 20+ years (TLT) · Index fund | **Problem.** Could not be managed: BrokerError: replace_order failed for 81c2a5f6-ec9f-4db0-916c-c5d654cb3635: {"available":"135","code":40310000,"existing_qty":"135","held_for_orders":"0","message":"insufficient qty available for order (requested: 147, available: 135)","related_orders":["81c2a5f6-ec9f-4db0-916c-c5d654cb3635"],"symbol":"TLT"} |
| ASML (ASML) · Company | **Holding.** -0.14R, holding 1 shares. Stop-loss 1619.35. |
| Caterpillar (CAT) · Company | **Holding.** -0.19R, holding 2 shares. Stop-loss 757.24. |
| Taiwan (EWT) · Sector or country | **Holding.** -0.48R, holding 33 shares. Stop-loss 110.28. |
| HDFC Bank (HDB) · Company | **Holding.** -0.47R, holding 90 shares. Stop-loss 22.23. |
| JPMorgan Chase (JPM) · Company | **Holding.** -0.12R, holding 6 shares. Stop-loss 323.48. |
| Microsoft (MSFT) · Company | **Holding.** +0.12R, holding 10 shares. Stop-loss 477.77. |
| Nvidia (NVDA) · Company | **Holding.** +0.50R, holding 16 shares. Stop-loss 216.23. |
| Royal Bank of Canada (RY) · Company | **Holding.** -0.43R, holding 10 shares. Stop-loss 194.59. |
| Teva Pharmaceutical (TEVA) · Company | **Holding.** -0.03R, holding 128 shares. Stop-loss 37.12. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### ASML (ASML) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [With 2 Big Chip Stocks Offering Value, These ETFs Are Worth a Look](https://etfdb.com/leveraged-inverse-content-hub/asmu-tsmx-worth-look/)  
  <sub>ETF Database, 46 minutes ago</sub>  
  Semiconductor equities are broadly considered growth stocks. But there are occasions when some members of the group serve up value.
- [Keysight's CSG Gains Momentum: Can AI Infrastructure Drive Growth?](https://uk.finance.yahoo.com/news/keysights-csg-gains-momentum-ai-120800329.html)  
  <sub>Yahoo Finance UK, 3 hours ago</sub>  
  Keysight Technologies, Inc. KEYS is benefiting from strong momentum in its Communications Solutions Group (CSG). In the third quarter, CSG generated $1.35...
- [AMD, TER Stocks Jump After Goldman Sachs Lifts Price Targets](https://stocktwits.com/news-articles/markets/equity/amd-ter-stocks-jump-after-goldman-sachs-lifts-price-targets/cZm18P6R7lx)  
  <sub>Stocktwits, 3 hours ago</sub>  
  Shares of Teradyne, Inc. (TER) and Advanced Micro Devices Inc. (AMD) jumped on Monday after Goldman Sachs raised its price targets on both semiconductor...
- [AI Supply Chains Are The Next Thing. Two Stocks Aim To Benefit.](https://www.investors.com/news/xmtr-stock-buy-point-avnet-xometry-ai-supply-chains/)  
  <sub>Investor's Business Daily, 4 hours ago</sub>  
  Both Xometry and Avnet are using artificial intelligence to ease bottlenecks in supply chains. XMRT stock eyes a buy point.
- [European Markets Decline Amid Rising Costs and Oil Prices](https://www.gurufocus.com/news/9094991/european-markets-decline-amid-rising-costs-and-oil-prices)  
  <sub>GuruFocus, 6 hours ago</sub>  
  On September 24, 2026, European stock indices opened lower as rising borrowing costs and persistently high oil prices dampened market sentiment.
- [REG - Leverage Shares PLC Leverage Inc Gold $ Leverage Inc NVDA $ Leverage Inc Tesla $ Leverage Inc S&P500$ - IncomeShares Interest Notification Calendar](https://www.tradingview.com/news/reuters.com,2026-09-24:newsml_RSX1957Wa:0-reg-leverage-shares-plc-leverage-inc-gold-leverage-inc-nvda-leverage-inc-tesla-leverage-inc-s-p500-incomeshares-interest-notification-calendar/)  
  <sub>TradingView, 4 hours ago</sub>  
  RNS Number : 1957W Leverage Shares PLC 24 September 2026 Leverage Shares plc24 September 2026THIS NOTICE IS IMPORTANT AND REQUIRES THE IMMEDIATE ATTENTION...
- [Tech, Media & Telecom Roundup: Market Talk](https://www.wsj.com/business/tech-media-telecom-roundup-market-talk-8dfe699f)  
  <sub>WSJ, 15 hours ago</sub>  
  The latest Market Talks covering Technology, Media and Telecom. Published exclusively on Dow Jones Newswires at 4:20 ET, 12:20 ET and 16:50 ET.
- [ASML Holding stock reports EUR 9.3 billion Q2 revenue](https://www.ad-hoc-news.de/boerse/news/corporate-news/asml-holding-stock-reports-eur-9-3-billion-q2-revenue/70177711)  
  <sub>AD HOC NEWS, 2 hours ago</sub>  
  ASML Holding stock carries a EUR 43 billion to EUR 45 billion 2026 sales outlook after the Q2 margin reached 54 percent. The September 23 close was EUR...
- [ASML Oct 2026 1380.000 call (ASML261002C01380000) interactive stock chart](https://uk.finance.yahoo.com/quote/ASML261002C01380000/chart/)  
  <sub>Yahoo Finance UK, 11 hours ago</sub>  
  Interactive chart for ASML Oct 2026 1380.000 call (ASML261002C01380000) – analyse all of the data with a huge range of indicators.
- [ClearBridge International Value ADR Portfolios Q2 2026 Commentary](https://seekingalpha.com/article/4949094-clearbridge-international-value-adr-portfolios-q2-2026-commentary)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Portfolios underperformed their MSCI EAFE benchmark in Q2, as stock selection in industrials and an overweight to energy more than offset positive stock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,710.49 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 1,685.31 (+1.5%), 50d 1,719.50 (-0.5%), 200d 1,518.50 (+12.6%); 50d above 200d
Momentum: RSI(14) 51.3 | MACD -11.937 vs signal -19.863 (histogram 7.927)
Returns: 1d -2.0% | 5d +6.8% | 1m -1.7% | 3m -3.0%
52-week range: 936.19 - 1,989.44 (now 73.5% of the way up)
Volatility: ATR(14) 53.42 (3.1% of price) | annualised 20d 41.2%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 657.04B
Valuation: trailing P/E 58.72 | forward P/E 28.89 | P/B 1,461.01 | PEG 1.58
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
Price target: mean 2,115.51 (+23.7% vs last close), range 879.74 - 2,817.06
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

- [Caterpillar vs. Corning: Which Industrials Stock Is a Better Buy in 2026?](https://www.fool.com/coverage/better-buy/2026/09/24/caterpillar-vs-corning-which-industrials-stock-is-a-better-buy-in-2026/)  
  <sub>The Motley Fool, 2 hours ago</sub>  
  One generates $7.5B in free cash flow with a lower valuation multiple; the other is riding an AI boom but commands a premium price.
- [Caterpillar (CAT), What Is Behind The Fresh Attention?](https://finance.yahoo.com/markets/stocks/articles/caterpillar-cat-behind-fresh-attention-011504899.html)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  Why Caterpillar stock is back in focus Caterpillar (CAT) is drawing fresh attention after reporting robust results, updating its 2026 outlook, and expanding...
- [This Analyst Sees 34% Upside For SRPT Stock — Here's Why They Expect A Sustained Rally Next](https://stocktwits.com/news-articles/markets/equity/srpt-stock-bullish-upgrade-novartis-readthrough-other-catalysts/cZmovIpR7nb)  
  <sub>Stocktwits, 13 hours ago</sub>  
  Sarepta Therapeutics Inc. (SRPT) shares were in focus on Thursday after a new analyst upgrade as Wall Street keeps an eye on multiple potential catalysts...
- [Caterpillar (CAT) Could Be 17% Undervalued As Backlog And Power Demand Build](https://simplywall.st/stocks/us/capital-goods/nyse-cat/caterpillar/news/caterpillar-cat-could-be-17-undervalued-as-backlog-and-power)  
  <sub>Simply Wall Street, 21 hours ago</sub>  
  Caterpillar (CAT) just extended its autonomous hauling partnership with Luck Stone, rolling the technology into two more Virginia quarries after moving more...
- [CAT Oct 2026 520.000 put (CAT261030P00520000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/CAT261030P00520000/)  
  <sub>Yahoo Finance UK, 13 hours ago</sub>  
  Find the latest CAT Oct 2026 520.000 put (CAT261030P00520000) stock quote, history, news and other vital information to help you with your stock trading and...
- [CAT Dec 2026 850.000 put (CAT261218P00850000) interactive stock chart](https://uk.finance.yahoo.com/quote/CAT261218P00850000/chart/)  
  <sub>Yahoo Finance UK, 14 hours ago</sub>  
  Interactive chart for CAT Dec 2026 850.000 put (CAT261218P00850000) – analyse all of the data with a huge range of indicators.
- [Caterpillar vs. Komatsu: Which Heavy Equipment Stock is the Better Buy?](https://www.theglobeandmail.com/investing/markets/stocks/CAT-N/pressreleases/4761043/caterpillar-vs-komatsu-which-heavy-equipment-stock-is-the-better-buy/)  
  <sub>The Globe and Mail, 22 hours ago</sub>  
  Detailed price information for Caterpillar Inc (CAT-N) from The Globe and Mail including charting and trades.
- [Twelve Cat Bond I-JSS USD Inc (0P0001U7WH) interactive stock chart – Yahoo Finance](https://sg.finance.yahoo.com/quote/0P0001U7WH/chart/)  
  <sub>Yahoo Finance Singapore, 10 hours ago</sub>  
  Interactive chart for Twelve Cat Bond I-JSS USD Inc (0P0001U7WH) – analyse all of the data with a huge range of indicators.
- [CAT Oct 2026 845.000 put (CAT261023P00845000) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/CAT261023P00845000/)  
  <sub>Yahoo Finance Singapore, 10 hours ago</sub>  
  Find the latest CAT Oct 2026 845.000 put (CAT261023P00845000) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 796.85 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 803.35 (-0.8%), 50d 832.30 (-4.3%), 200d 787.37 (+1.2%); 50d above 200d
Momentum: RSI(14) 44.4 | MACD -9.403 vs signal -12.542 (histogram 3.139)
Returns: 1d -1.9% | 5d +1.8% | 1m -1.7% | 3m -19.9%
52-week range: 463.72 - 1,064.90 (now 55.4% of the way up)
Volatility: ATR(14) 23.83 (3.0% of price) | annualised 20d 26.5%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 366.29B
Valuation: trailing P/E 34.32 | forward P/E 24.61 | P/B 18.89 | PEG 1.41
Profitability: profit margin 14.5% | operating margin 22.2% | ROE 57.0%
Growth (YoY): revenue +24.0% | earnings +68.2%
Balance sheet: debt/equity 232.8% | free cash flow 5.05B
Risk: beta 1.59 | short interest 1.8% of float
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
Price target: mean 975.61 (+22.4% vs last close), range 575.00 - 1,225.00
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

### Elbit Systems (ESLT) · Company — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [This Defense Stock Has More Than Doubled In A Year – And It Just Bagged Its Second Contract This Week](https://stocktwits.com/news-articles/markets/equity/elbit-systems-eslt-stock-350-million-tank-upgrade-contract/cZgiilMResm)  
  <sub>Stocktwits, 19 hours ago</sub>  
  Elbit Systems won a $350 million contract days after it unveiled a $1.4 billion European modernization program award.
- [Defense Stocks In Focus As U.S. Iran Israel Tensions Put Rheinmetall Stock On Watch](https://simplywall.st/stocks/de/capital-goods/etr-rhm/rheinmetall-shares/news/defense-stocks-in-focus-as-us-iran-israel-tensions-put-rhein/amp)  
  <sub>Simply Wall Street, 22 hours ago</sub>  
  Geopolitical risk between the U.S., Iran, and Israel has moved from background noise to front-page driver, and markets are starting to price that in.
- [Israel stocks lower at close of trade; TA 35 down 0.26%](https://www.investing.com/news/stock-market-news/israel-stocks-lower-at-close-of-trade-ta-35-down-026-4913461)  
  <sub>Investing.com, 17 hours ago</sub>  
  Investing.com – Israel stocks were lower after the close on Wednesday, as losses in the Real Estate, Insurance and Communication sectors led shares lower.
- [Wed: Nice bucks market](https://en.globes.co.il/en/article-wed-nice-bucks-market-1001557425)  
  <sub>Globes - Israel Business News, 23 hours ago</sub>  
  The main indices dipped today but Nice bucked the market on reports of a possible acquisition of Actimize. The Tel Aviv Stock Exchange fell today.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 741.35 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 723.44 (+2.5%), 50d 762.39 (-2.8%), 200d 766.49 (-3.3%); 50d below 200d
Momentum: RSI(14) 50.3 | MACD -3.806 vs signal -9.597 (histogram 5.791)
Returns: 1d -0.2% | 5d +0.4% | 1m +1.5% | 3m -1.3%
52-week range: 454.95 - 1,014.33 (now 51.2% of the way up)
Volatility: ATR(14) 15.46 (2.1% of price) | annualised 20d 14.4%
Volume: 0.45x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 34.74B
Valuation: trailing P/E 55.74 | forward P/E 40.37 | P/B 7.86 | PEG n/a
Profitability: profit margin 7.4% | operating margin 9.6% | ROE 15.2%
Growth (YoY): revenue +15.9% | earnings +34.2%
Balance sheet: debt/equity 19.3% | free cash flow -38.48M
Risk: beta -0.30 | short interest 0.8% of float
Next earnings: 2026-11-24
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 10% | 2026-03-31 beat by 16% | 2025-12-31 beat by 16% | 2025-09-30 beat by 21%
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
Consensus: none (mean n/a on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 816.33 (+10.1% vs last close), range 518.00 - 960.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

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

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Alphabet (Google) (GOOGL) · Company — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Why Alphabet (GOOGL) Stock Is Down Today](https://finance.yahoo.com/markets/stocks/articles/why-alphabet-googl-stock-down-212205277.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Shares of online advertising giant Alphabet (NASDAQ:GOOGL) fell 3.4% in the afternoon session after sentiment weakened ahead of rival Meta Platforms Connect...
- [GOOGL Stock Steadies After Worst Drop In A Month As DeepMind Chief Says Gemini 4 Is Coming 'Much Earlier'](https://es.tradingview.com/news/stocktwits:baa7ae869094b:0-googl-stock-steadies-after-worst-drop-in-a-month-as-deepmind-chief-says-gemini-4-is-coming-much-earlier/)  
  <sub>TradingView, 10 hours ago</sub>  
  Alphabet Inc. shares inched higher in overnight trading after their worst drop in more than a month, as Google DeepMind chief Koray Kavukcuoglu said the...
- [GOOGL Expands Gemini Into Robotics As Big Tech Races To Build Physical AI — New Robot AI Can Tap Google Search For Real-World Tasks](https://stocktwits.com/news-articles/markets/equity/googl-gemini-robotics-physical-ai-google-search-real-world-tasks/cZN54nbRJcw)  
  <sub>Stocktwits, 8 hours ago</sub>  
  Google said Gemini Robotics ER 2 serves as a high-level reasoning model for robots, enabling them to plan complex tasks and work across different robotic...
- [Alphabet Stock Dips: Here's What You Need To Know](https://www.benzinga.com/trading-ideas/movers/26/09/61952854/alphabet-stock-dips-heres-what-you-need-to-know)  
  <sub>Benzinga, 22 hours ago</sub>  
  Alphabet Inc. (NASDAQ:GOOG) shares are trading lower Wednesday as a broader selloff hits companies seen as vulnerable to disruption from Meta's rapidly...
- [Nvidia Stock Falls. It Has a Google AI Chip Conundrum.](https://www.barrons.com/articles/nvidia-stock-price-ai-chips-google-2c231d8d)  
  <sub>Barron's, 19 hours ago</sub>  
  The chip maker's stock has paused in its latest effort to break out to new highs—and part of the problem is Google. Nvidia shares closed down 1.4% at...
- [QQQ is down 0.9% today, on GOOGL stock price movement](https://www.quiverquant.com/news/QQQ+is+down+0.9%25+today%2C+on+GOOGL+stock+price+movement)  
  <sub>Quiver Quantitative, 23 hours ago</sub>  
  $QQQ stock has fallen 0.9% today, according to our price data from Polygon. It has been dragged by GOOGL stock falling 3.0%.
- [Prediction: This Magnificent Seven Stock Could Soar 50% by 2027](https://247wallst.com/investing/2026/09/23/prediction-this-magnificent-seven-stock-could-soar-50-by-2027/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  GOOG trades at just 17x trailing earnings despite 82% cloud revenue growth and a $514 billion backlog supporting a path to $525.
- [COHR, AAOI, LITE, POET: Photonic Stocks Join Google Capex-Fueled AI Rally](https://stocktwits.com/news-articles/markets/equity/cohr-aaoi-lite-poet-photonic-stocks-join-google-capex-fueled-ai-rally/cZZnO3mR7x5)  
  <sub>Stocktwits, 7 hours ago</sub>  
  On Stocktwits, the retail sentiment was 'bearish' for COHR, LITE and POET, and 'neutral' for AAOI as of late Wednesday. “$LITE and other optics/networking names...
- [Tigress Raises Alphabet (GOOGL) Price Target to $485 as AI Fuels Growth. Can the Momentum Last?](https://finance.yahoo.com/technology/ai/articles/tigress-raises-alphabet-googl-price-102901909.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  AI leadership is increasingly becoming a key growth engine across Alphabet Inc. (NASDAQ:GOOGL)'s core businesses. Tigress Financial analyst Ivan Feinseth...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 337.64 (bar of 2026-09-24), from 502 daily bars
Trend: vs 20d SMA 341.77 (-1.2%), 50d 344.41 (-2.0%), 200d 338.03 (-0.1%); 50d above 200d
Momentum: RSI(14) 44.9 | MACD -0.247 vs signal -0.555 (histogram 0.308)
Returns: 1d -0.1% | 5d -2.8% | 1m -2.7% | 3m -1.8%
52-week range: 236.57 - 402.62 (now 60.9% of the way up)
Volatility: ATR(14) 8.81 (2.6% of price) | annualised 20d 26.9%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 4.13T
Valuation: trailing P/E 16.94 | forward P/E 22.66 | P/B 6.63 | PEG 1.25
Profitability: profit margin 54.8% | operating margin 34.0% | ROE 48.7%
Growth (YoY): revenue +24.2% | earnings +294.0%
Balance sheet: debt/equity 18.9% | free cash flow 22.67B
Risk: beta 1.23 | short interest 1.3% of float
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
Consensus: strong_buy (mean 1.38 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 13 strong buy, 43 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 429.46 (+27.2% vs last close), range 340.00 - 515.00
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

### HDFC Bank (HDB) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [HDB DEADLINE: SueWallSt Reminds HDFC Bank Limited Investors of Upcoming Securities Class Action Deadline](https://www.prnewswire.com/news-releases/hdb-deadline-suewallst-reminds-hdfc-bank-limited-investors-of-upcoming-securities-class-action-deadline-302888696.html)  
  <sub>PR Newswire, 1 hour ago</sub>  
  PRNewswire/ -- SueWallSt alerts investors in HDFC Bank Limited (NYSE: HDB) of a pending securities class action on behalf of purchasers of HDB securities...
- [SHAREHOLDER ALERT Bernstein Liebhard LLP Announces A](https://www.globenewswire.com/news-release/2026/09/24/3368428/0/en/shareholder-alert-bernstein-liebhard-llp-announces-a-securities-fraud-class-action-lawsuit-has-been-filed-against-hdfc-bank-limited-hdb.html)  
  <sub>GlobeNewswire, 2 hours ago</sub>  
  HDFC Bank Shareholders Between July 17, 2023 and May 26, 2026 - Contact Bernstein Liebhard For More Information Regarding Lawsuit...
- [Eli Lilly Stock Price Today (LLY) | NYSE](https://techgraph.co/stock-market/quote/lly/)  
  <sub>TechGraph, 1 hour ago</sub>  
  Eli Lilly (LLY) stock price today on NYSE. Live quote, chart, volume, 52-week range and Healthcare company snapshot on TechGraph.
- [Robbins LLP is Investigating Allegations that HDFC Bank Camouflaged Payments as Marketing Spend to Pay Higher Interest to a State Firm to Induce Deposits](https://www.financialcontent.com/article/newsfile-2026-9-23-robbins-llp-is-investigating-allegations-that-hdfc-bank-camouflaged-payments-as-marketing-spend-to-pay-higher-interest-to-a-state-firm-to-induce-deposits)  
  <sub>FinancialContent, 16 hours ago</sub>  
  San Diego, California--(Newsfile Corp. - September 23, 2026) - Shareholder rights law firm Robbins LLP reminds investors that a class...
- [Can IRDAI’s insurance reforms impact NBFCs? Jefferies warns L&T Finance, Piramal Finance, others are most](https://m.economictimes.com/markets/stocks/news/can-irdais-insurance-reforms-impact-nbfcs-jefferies-warns-lt-finance-piramal-finance-others-are-most-exposed/articleshow/134459825.cms)  
  <sub>The Economic Times, 4 hours ago</sub>  
  Insurance regulator IRDAI's proposed overhaul of the insurance sector rattled insurance stocks on Thursday, but Jefferies has warned that non banking...
- [Deadline Alert: HDFC Bank Limited (HDB) Shareholders Who](https://www.globenewswire.com/news-release/2026/09/23/3367800/0/en/deadline-alert-hdfc-bank-limited-hdb-shareholders-who-lost-money-urged-to-contact-glancy-prongay-wolke-rotter-llp-about-securities-fraud-lawsuit.html)  
  <sub>GlobeNewswire, 21 hours ago</sub>  
  LOS ANGELES, Sept. 23, 2026 (GLOBE NEWSWIRE) -- Glancy Prongay Wolke & Rotter LLP reminds investors of the upcoming October 13, 2026 deadline to file...
- [NSE listing sees India's biggest exchange near bottom of Rs 10,000 crore IPO club](https://m.economictimes.com/markets/ipos/fpos/nse-listing-sees-indias-biggest-exchange-near-bottom-of-rs-10000-crore-ipo-club/amp_articleshow/134452520.cms)  
  <sub>The Economic Times, 10 hours ago</sub>  
  NSE made a muted stock-market debut on Tuesday, listing at just about 0.8% premium to its IPO price, putting India's largest exchange among the weakest...
- [IRDAI shocker! From ICICI Bank to PB Fintech - A look at most and least impacted bank, NBFC and insurance stocks](https://www.livemint.com/market/stock-market-news/irdai-shocker-from-icici-bank-to-pb-fintech-a-look-at-most-and-least-impacted-bank-nbfc-and-insurance-stocks/amp-11790239361588.html)  
  <sub>Livemint, 6 hours ago</sub>  
  IRDAI's consultation suggests potential earnings pressure for banks and NBFCs reliant on insurance income. Analysts highlight SBI, ICICI Bank,...
- [Vietnam Stock Market Live: Ho Chi Minh’s VNI Index Falls 0.76%, HNX Index Sees Drop of 0.98% As High Selling Pressure & Strong Dollar Weigh on Investors – Check Stocks in Focus, Investor Outlook & Mor](https://sundayguardianlive.com/business/vietnam-stock-market-live-ho-chi-minhs-vni-index-falls-076-hnx-index-sees-drop-of-098-as-high-selling-pressure-strong-dollar-weigh-on-investors-check-stocks-in-focus-investor-outlook-mor-291506/amp/)  
  <sub>The Sunday Guardian, 9 hours ago</sub>  
  VNI, the benchmark index is currently trading downwards by 0.76%. Meanwhile Hanoi's HNX index has seen a 0.98% drop despite opening gains.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 22.82 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 22.83 (-0.1%), 50d 23.41 (-2.5%), 200d 27.52 (-17.1%); 50d below 200d
Momentum: RSI(14) 47.6 | MACD -0.148 vs signal -0.227 (histogram 0.079)
Returns: 1d +0.1% | 5d +1.9% | 1m -3.1% | 3m -10.7%
52-week range: 21.84 - 37.18 (now 6.4% of the way up)
Volatility: ATR(14) 0.56 (2.4% of price) | annualised 20d 39.4%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 117.24B
Valuation: trailing P/E 15.95 | forward P/E 16.40 | P/B 9.12 | PEG n/a
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
Price target: mean 30.77 (+34.9% vs last close), range 26.10 - 35.00
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

- [JP Morgan Chase & Co. (JPM) Stock forecasts](https://au.finance.yahoo.com/research/reports/MS_0P0000031C_AnalystReport_1790119985000)  
  <sub>Yahoo Finance Australia, 8 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [Jefferies Financial Group Cuts JPMorgan Chase & Co. (NYSE:JPM) Price Target to $365.00](https://www.marketbeat.com/instant-alerts/analyst-jefferies-financial-group-cuts-jpmorgan-chase-co-nyse-jpm-price-target-to-36500-2026-09-24/)  
  <sub>MarketBeat, 2 hours ago</sub>  
  Jefferies Financial Group reduced their price target on JPMorgan Chase & Co. from $370.00 to $365.00 and set a "hold" rating for the company in a report on...
- [Why Did IMAX, JPM, CSX Stocks Surge To 52-Week Highs Last Week?](https://stocktwits.com/news-articles/markets/equity/imax-jpm-csx-stocks-52-week-highs-last-week/cZZxcQ3R7C3)  
  <sub>Stocktwits, 19 hours ago</sub>  
  Citi raised the price target on CSX to $54 from $53 and maintained a Neutral rating on the shares, implying an upside of about 1.5% from its last close.
- [Bessent ‘Inadvertently’ Failed to Report Holdings of JPMorgan Stock](https://www.nytimes.com/2026/09/23/business/bessent-jp-morgan-stock.html)  
  <sub>The New York Times, 24 hours ago</sub>  
  Treasury Secretary Scott Bessent's finances were reviewed by the inspector general after Mr. Bessent incorrectly listed at least $100000 of the stock,...
- [JPMorgan Chase (JPM) Could Be 9% Undervalued After Dividend Hike And Buyback](https://simplywall.st/stocks/us/banks/nyse-jpm/jpmorgan-chase/news/jpmorgan-chase-jpm-could-be-9-undervalued-after-dividend-hik)  
  <sub>Simply Wall Street, 17 hours ago</sub>  
  Dividend hike and fresh capital moves put JPMorgan Chase in focus JPMorgan Chase (JPM) has raised its quarterly dividend to US$1.65 per share and approved a...
- [Mufg Securities Americas Inc. Boosts Stake in JPMorgan Chase & Co. $JPM](https://www.marketbeat.com/instant-alerts/filing-mufg-securities-americas-inc-boosts-stake-in-jpmorgan-chase-co-jpm-2026-09-24/)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Mufg Securities Americas Inc. lifted its stake in JPMorgan Chase & Co. (NYSE:JPM) by 9.2% in the second quarter, according to the company in its most recent...
- [JPM, BofA Eye Payments Deal — Why JPMorgan, Bank Of America And Other Banks Want Fiserv’s Debit Network](https://www.google.com/goto?url=CAES3gEB6zswFQHv9OTux_YMC5RDd93EWrYfLmNNRv_RNcHF8Qfe3XulF56CfhfHWwL0XCBI-8tTOuHBIUagY0u_vjyVimxOK1Ome5vhnXK3QBB_jDfsnK6GMFGY47eaUbfE4WJ4GgoEtOObD6bTyjuzUY5zr8b8ya7wjB4fVbZFHP1IxDqMFWQED4yK0hGYPkuDQZ0aj6u7PVZFq5L04Rp3x8PcLALg7XwoonnPdzfxwlWfP1LrTorqS6w3O99ahNHU4pEj5F9AlXzNoSP_Eyh_7mU7isDtC3huIQ6jNJfDhWM)  
  <sub>Stocktwits, 11 hours ago</sub>  
  Fiserv (FISV) share price gained 4% after-hours amid a report that several top financial institutions are looking to acquire a network owned by the firm to...
- [JPM Sep 2027 380.000 put (JPM270917P00380000) interactive stock chart](https://uk.finance.yahoo.com/quote/JPM270917P00380000/chart/)  
  <sub>Yahoo Finance UK, 13 hours ago</sub>  
  Interactive chart for JPM Sep 2027 380.000 put (JPM270917P00380000) – analyse all of the data with a huge range of indicators.
- [JPMorgan Chase & Co. $JPM is Ferguson Wellman Capital Management Inc.'s 7th Largest Position](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-is-ferguson-wellman-capital-management-incs-7th-largest-position-2026-09-24/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Ferguson Wellman Capital Management Inc. reduced its stake in shares of JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 2.8% during the 2nd quarter,...
- [JPM260925P00330000 Interactive Stock Chart | JPM Sep 2026 330.000 put Stock](https://finance.yahoo.com/chart/JPM260925P00330000)  
  <sub>Yahoo Finance, 15 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 336.45 (bar of 2026-09-24), from 502 daily bars
Trend: vs 20d SMA 351.71 (-4.3%), 50d 353.30 (-4.8%), 200d 321.11 (+4.8%); 50d above 200d
Momentum: RSI(14) 32.6 | MACD -3.472 vs signal -1.317 (histogram -2.155)
Returns: 1d -0.3% | 5d -3.7% | 1m -5.7% | 3m +0.4%
52-week range: 282.84 - 365.18 (now 65.1% of the way up)
Volatility: ATR(14) 6.76 (2.0% of price) | annualised 20d 17.8%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 894.35B
Valuation: trailing P/E 14.43 | forward P/E 13.46 | P/B 2.53 | PEG 1.58
Profitability: profit margin 34.9% | operating margin 50.4% | ROE 17.8%
Growth (YoY): revenue +30.4% | earnings +46.9%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.97 | short interest 1.0% of float
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
Price target: mean 375.14 (+11.5% vs last close), range 305.00 - 436.00
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

- [Eli Lilly and Co Stock (LLY) Moved Up by 3.73% on Sep 24: A Full Analysis](https://www.tradingkey.com/news/market-movers/262185188-market-movers-lly-20260924)  
  <sub>TradingKey, 54 minutes ago</sub>  
  FDA approved Eli Lilly's once-weekly basal insulin Onswik for type 2 diabetes.Eli Lilly reported $65.18B annual revenue and $20.64B net profit.
- [Lilly's FDA-approved weekly insulin could mean over 300 fewer shots a year than daily insulin](https://www.stocktitan.net/news/LLY/u-s-food-and-drug-administration-fda-approves-lilly-s-onswik-tm-7ef9xmbyiabi.html)  
  <sub>Stock Titan, 4 hours ago</sub>  
  Eli Lilly (LLY) received U.S. FDA approval on September 24, 2026, for Onswik, a once-weekly basal insulin for adults with type 2 diabetes.
- [Eli Lilly (LLY) Targets Up To Five New Medicines In Research Deal](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-lly/eli-lilly/news/eli-lilly-lly-targets-up-to-five-new-medicines-in-research-d)  
  <sub>Simply Wall Street, 5 hours ago</sub>  
  Eli Lilly (NYSE: LLY) agreed a research collaboration and licensing deal with InnoCare Pharma to pursue up to five new medicines. The partners plan to...
- [Lilly wins FDA nod for once-weekly insulin product, Onswik](https://seekingalpha.com/news/4646525-lilly-wins-fda-nod-once-weekly-insulin-onswik)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Eli Lilly (LLY) wins FDA approval for once-weekly insulin product, Onswik, for adults with type 2 diabetes, backed by Phase 3 QWINT data. Read more here.
- [LLY Looks 26.0% Undervalued on GF Value™ After FDA Approval of W](https://www.gurufocus.com/news/9095167/lly-looks-260-undervalued-on-gf-value-after-fda-approval-of-weekly-insulin)  
  <sub>GuruFocus, 3 hours ago</sub>  
  On September 24, 2026, Eli Lilly and Co (NYSE: LLY) announced that the U.S. Food and Drug Administration has approved Onswik, a novel basal insulin designed...
- [Why NBIS Stock Has Gained Over 10% Today?](https://stocktwits.com/news-articles/markets/equity/nbis-stock-jumps-after-ex-openai-researchers-fund-discloses-major-stake/cZgiqlCRet3)  
  <sub>Stocktwits, 4 hours ago</sub>  
  Nebius Group stock gained over 10% after a regulatory filing revealed a significant stake in the AI infrastructure company by hedge fund Situational...
- [LLY Jan 2029 900.000 put (LLY290119P00900000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/LLY290119P00900000/)  
  <sub>Yahoo Finance UK, 13 hours ago</sub>  
  Find the latest LLY Jan 2029 900.000 put (LLY290119P00900000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Eli Lilly Stock Price Today (LLY) | NYSE](https://techgraph.co/stock-market/quote/lly/)  
  <sub>TechGraph, 1 hour ago</sub>  
  Eli Lilly (LLY) stock price today on NYSE. Live quote, chart, volume, 52-week range and Healthcare company snapshot on TechGraph.
- [VKTX Stock Heads Toward Worst Day In Over A Year Just Days After Promising Weight Loss Drug Data — Here’s What’s Driving The Selloff](https://www.tradingview.com/news/stocktwits:533f502a2094b:0-vktx-stock-heads-toward-worst-day-in-over-a-year-just-days-after-promising-weight-loss-drug-data-here-s-what-s-driving-the-selloff/)  
  <sub>TradingView, 2 hours ago</sub>  
  Shares of Viking Therapeutics (VKTX) fell more than 12% in pre-market trading on Thursday, putting them on track for their worst session in more than a year...
- [LLY Looks 26.0% Undervalued on GF Value™ After FDA Approval of O](https://www.gurufocus.com/news/9095221/lly-looks-260-undervalued-on-gf-value-after-fda-approval-of-onswik)  
  <sub>GuruFocus, 3 hours ago</sub>  
  On September 24, 2026, Eli Lilly and Co (NYSE: LLY) announced that the U.S. Food and Drug Administration (FDA) approved Onswik, a once-weekly basal insulin...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,192.91 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 1,151.95 (+3.6%), 50d 1,177.08 (+1.3%), 200d 1,068.42 (+11.7%); 50d above 200d
Momentum: RSI(14) 57.8 | MACD -6.227 vs signal -11.268 (histogram 5.041)
Returns: 1d +3.6% | 5d +4.8% | 1m -4.3% | 3m +6.8%
52-week range: 714.59 - 1,280.34 (now 84.5% of the way up)
Volatility: ATR(14) 31.98 (2.7% of price) | annualised 20d 24.1%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.06T
Valuation: trailing P/E 40.02 | forward P/E 25.20 | P/B 31.39 | PEG 1.16
Profitability: profit margin 33.5% | operating margin 54.2% | ROE 102.3%
Growth (YoY): revenue +47.7% | earnings +26.2%
Balance sheet: debt/equity 162.1% | free cash flow 11.07B
Risk: beta 0.50 | short interest 0.9% of float
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
Price target: mean 1,325.39 (+11.1% vs last close), range 930.00 - 1,600.00
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

### MercadoLibre (MELI) · Company — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,774.46 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 1,895.25 (-6.4%), 50d 1,873.48 (-5.3%), 200d 1,848.09 (-4.0%); 50d above 200d
Momentum: RSI(14) 38.1 | MACD -24.967 vs signal -6.236 (histogram -18.731)
Returns: 1d -1.4% | 5d -3.5% | 1m -8.9% | 3m +6.9%
52-week range: 1,546.81 - 2,510.97 (now 23.6% of the way up)
Volatility: ATR(14) 58.03 (3.3% of price) | annualised 20d 27.2%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 89.96B
Valuation: trailing P/E 48.09 | forward P/E 31.43 | P/B 11.48 | PEG 1.00
Profitability: profit margin 5.3% | operating margin 6.7% | ROE 27.5%
Growth (YoY): revenue +49.8% | earnings -10.9%
Balance sheet: debt/equity 168.6% | free cash flow 353.38M
Risk: beta 1.31 | short interest 1.6% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 1 beat, 3 missed
  2026-06-30 beat by 4% | 2026-03-31 missed by 7% | 2025-12-31 missed by 6% | 2025-09-30 missed by 13%
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
Consensus: buy (mean 1.58 on a 1=strong buy to 5=strong sell scale, 25 analysts)
Ratings: 4 strong buy, 16 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 2,272.28 (+28.1% vs last close), range 1,750.00 - 2,800.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

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

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Microsoft (MSFT) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 494.23 (bar of 2026-09-24), from 502 daily bars
Trend: vs 20d SMA 499.30 (-1.0%), 50d 473.44 (+4.4%), 200d 431.92 (+14.4%); 50d above 200d
Momentum: RSI(14) 52.0 | MACD 5.437 vs signal 7.685 (histogram -2.247)
Returns: 1d -1.3% | 5d -0.7% | 1m +0.5% | 3m +40.1%
52-week range: 352.83 - 542.07 (now 74.7% of the way up)
Volatility: ATR(14) 10.98 (2.2% of price) | annualised 20d 22.8%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.67T
Valuation: trailing P/E 27.50 | forward P/E 20.87 | P/B 8.30 | PEG 1.62
Profitability: profit margin 40.3% | operating margin 45.1% | ROE 34.0%
Growth (YoY): revenue +17.7% | earnings +31.7%
Balance sheet: debt/equity 29.1% | free cash flow 16.55B
Risk: beta 1.11 | short interest 1.0% of float
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
Price target: mean 577.26 (+16.8% vs last close), range 440.00 - 870.00
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
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Nvidia (NVDA) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [NVIDIA Corporation (NVDA) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/NVDA/)  
  <sub>Yahoo! Finance Canada, 3 hours ago</sub>  
  Valuation Measures · Market Cap. 5.45T · Enterprise Value. 5.42T · Trailing P/E. 28.93 · Forward P/E. 25.25 · PEG Ratio (5yr expected). 0.49 · Price/Sales (ttm).
- [Nvidia’s Immense Dividend Hike Puts Dividend Growth Stocks in the Spotlight](https://www.morningstar.com/stocks/nvidias-immense-dividend-hike-puts-dividend-growth-stocks-spotlight)  
  <sub>Morningstar, 3 hours ago</sub>  
  Lost in a torrent of news about Nvidia NVDA this year—its role in financing $500 billion in artificial intelligence investments, its forecasts of 70%...
- [NVDA Stock Posts Biggest Jump In 14 Months On $12 Trillion Valuation Call From Raymond James – ‘Supply Is The Primary Constraint’](https://stocktwits.com/news-articles/markets/equity/nvda-stock-12-trillion-valuation-raymond-james-supply-constraints/cZYo4liRJqf)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Raymond James raised its price target on Nvidia to $515 from $352, the biggest increase and the highest target among the analysts covering the results on TheFly...
- [1 Volatile Stock to Own for Decades and 2 That Underwhelm](https://stockstory.org/us/stocks/nasdaq/nvda/news/buy-or-sell/1-volatile-stock-to-own-for-decades-and-2-that-underwhelm)  
  <sub>StockStory, 6 hours ago</sub>  
  Market swings can be tough to stomach, and volatile stocks often experience exaggerated moves in both directions. While many thrive during risk-on...
- [NVIDIA Stock Looks Expensive Until You Price The Vera Rubin Ramp](https://www.trefis.com/data/companies/NVDA/no-login-required/4swp4ezE/NVIDIA-Stock-Looks-Expensive-Until-You-Price-The-Vera-Rubin-Ramp)  
  <sub>Trefis, 5 hours ago</sub>  
  NVIDIA (NVDA) stock trades near $225, about 28.3 times its adjusted earnings over the past twelve months. Adjusted here means normalized net income with...
- [Here's How Much $100 Invested In NVIDIA 5 Years Ago Would Be Worth Today](https://www.benzinga.com/news/26/09/61974391/here-s-how-much-100-invested-nvidia-5-years-ago-would-be-worth-today)  
  <sub>Benzinga, 23 minutes ago</sub>  
  NVIDIA (NASDAQ:NVDA) has outperformed the market over the past 5 years by 48.74% on an annualized basis producing an average annual return of 60.79%.
- [NVDA 260925 335.00C (NVDA260925C335000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/NVDA260925C335000-US)  
  <sub>Moomoo, 10 hours ago</sub>  
  Track real-time NVDA 260925 335.00C (NVDA260925C335000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [NVIDIA (NVDA) Could Be 20% Undervalued On Its Expanding AI Narrative](https://simplywall.st/stocks/us/semiconductors/nasdaq-nvda/nvidia/news/nvidia-nvda-could-be-20-undervalued-on-its-expanding-ai-narr/amp)  
  <sub>Simply Wall Street, 2 hours ago</sub>  
  IonQ's decision to install its Superion 256 quantum computer at the NVIDIA Accelerated Quantum Research Center puts NVIDIA (NVDA) directly at the...
- [Can Nvidia stock really hit $333 in September 2027?](https://uk.finance.yahoo.com/news/nvidia-stock-really-hit-333-060700090.html)  
  <sub>Yahoo Finance UK, 9 hours ago</sub>  
  Nvidia (NASDAQ: NVDA) stock is no longer going gangbusters. While it's up around 900% over five years, it's climbed just 28% in the last 12 months.
- [NVDA Stock Eyes Third Weekly Gains: Why Japan Wants Nvidia’s Rubin Chips To Power Its Next Robotics Boom](https://stocktwits.com/news-articles/markets/equity/nvda-stock-eyes-third-weekly-gains-why-japan-wants-nvidia-s-rubin-chips-to-power-its-next-robotics-boom/cZZE3cQR7sb)  
  <sub>Stocktwits, 10 hours ago</sub>  
  NVDA Stock Eyes Third Weekly Gains: Why Japan Wants Nvidia's Rubin Chips To Power Its Next Robotics Boom. Nvidia partners with Japan's Noetra to build an AI...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 221.52 (bar of 2026-09-24), from 502 daily bars
Trend: vs 20d SMA 221.75 (-0.1%), 50d 215.56 (+2.8%), 200d 199.26 (+11.2%); 50d above 200d
Momentum: RSI(14) 51.7 | MACD 1.992 vs signal 1.775 (histogram 0.217)
Returns: 1d -1.8% | 5d +1.0% | 1m +4.0% | 3m +13.2%
52-week range: 165.17 - 235.74 (now 79.8% of the way up)
Volatility: ATR(14) 6.03 (2.7% of price) | annualised 20d 45.5%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 5.35T
Valuation: trailing P/E 27.97 | forward P/E 14.13 | P/B 23.36 | PEG 0.49
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
Price target: mean 327.70 (+47.9% vs last close), range 180.00 - 515.00
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

- [Novo Nordisk (NVO) Shares Dropped, So What Is Driving Attention Now?](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-nvo/novo-nordisk/news/novo-nordisk-nvo-shares-dropped-so-what-is-driving-attention)  
  <sub>Simply Wall Street, 4 hours ago</sub>  
  Novo Nordisk (NYSE:NVO) has been drawing attention after recent returns turned negative across multiple time frames, including the past month and past 3...
- [Novo Nordisk: Capital Markets Day Reveals Its Next Growth Engine (NYSE:NVO)](https://seekingalpha.com/article/4949408-novo-nordisk-capital-markets-day-reveals-its-next-growth-engine)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Novo Nordisk A/S's 2030 pipeline targets, Wegovy pill growth and Q2 sales show major upside. Click for this NVO stock update.
- [NVO Stock On Track For Worst Week In Over 6 Months After Strategy Day — Direct US Listing Talks, Drug Approval Fail To Halt Slip](https://finance.yahoo.com/markets/stocks/articles/nvo-stock-track-worst-week-203618741.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  On Wednesday, CEO Mike Doustdar told the Financial Times that Novo is open to a direct NYSE listing instead of ADRs, but that there is no active process.
- [HIMS Stock Gained Nearly 6% On Wednesday — Barclays Sees Breakout Potential After Novo Partnership](https://stocktwits.com/news-articles/markets/equity/hims-stock-gains-nearly-6-percent-as-barclays-sees-breakout-potential-after-novo-partnership/cZKK7ffR7eJ)  
  <sub>Stocktwits, 6 hours ago</sub>  
  Shares of Hims & Hers Health (HIMS) gained nearly 6% in afternoon trading on Wednesday after Barclays turned more bullish on the telehealth company.
- [Novo Nordisk A/S Stock (NVO) Closed Down by 3.12% on Sep 23: Key Drivers Unveiled](https://www.tradingkey.com/news/market-movers/262183539-market-movers-nvo-20260923)  
  <sub>TradingKey, 19 hours ago</sub>  
  Novo Nordisk shares dropped following disappointing long-term revenue growth targets.Intensifying competition, patent cliff risks, and market share losses...
- [Novo Nordisk (NVO) Falls More Steeply Than Broader Market: What Investors Need to Know](https://finance.yahoo.com/markets/stocks/articles/novo-nordisk-nvo-falls-more-214505073.html)  
  <sub>Yahoo Finance, 17 hours ago</sub>  
  Novo Nordisk (NVO) closed at $38.17 in the latest trading session, marking a -3.12% move from the prior day. The stock's performance was behind the S&P...
- [Novo Nordisk open to direct New York listing, CEO says](https://finance.yahoo.com/markets/stocks/articles/novo-nordisk-open-direct-york-161200331.html)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  Novo Nordisk (NYSE:NVO) (NYSE:NVO), the Danish drugmaker, would be open to considering a direct listing of its shares on the New York Stock Exchange,...
- [NVO Oct 2026 32.000 put (NVO261023P00032000) stock historical prices and data](https://sg.finance.yahoo.com/quote/NVO261023P00032000/history/)  
  <sub>Yahoo Finance Singapore, 19 hours ago</sub>  
  Discover historical prices for NVO261023P00032000 stock on Yahoo Finance. View daily, weekly or monthly formats back to when NVO Oct 2026 32.000 put stock...
- [NVO Oct 2026 54.000 call (NVO261023C00054000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/NVO261023C00054000/)  
  <sub>Yahoo Finance UK, 24 hours ago</sub>  
  Find the latest NVO Oct 2026 54.000 call (NVO261023C00054000) stock quote, history, news and other vital information to help you with your stock trading and...
- [VLO Stock Heads For Best Year Since 1982 — Michael Burry Says It Has Become A ‘Huge Position’](https://stocktwits.com/news-articles/markets/equity/vlo-stock-best-year-1982-michael-burry-huge-position/cZtlx8lRBR0)  
  <sub>Stocktwits, 4 hours ago</sub>  
  Burry recovered his initial investment “and then some” for charity, while retaining a sizable stake that is “deep into house's money.”

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 38.40 (bar of 2026-09-24), from 502 daily bars
Trend: vs 20d SMA 43.49 (-11.7%), 50d 46.05 (-16.6%), 200d 45.97 (-16.5%); 50d above 200d
Momentum: RSI(14) 28.8 | MACD -1.971 vs signal -1.389 (histogram -0.582)
Returns: 1d +0.6% | 5d -11.1% | 1m -21.1% | 3m -19.4%
52-week range: 35.29 - 63.98 (now 10.9% of the way up)
Volatility: ATR(14) 1.32 (3.4% of price) | annualised 20d 39.8%
Volume: 0.64x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 169.63B
Valuation: trailing P/E 9.85 | forward P/E 11.36 | P/B 4.98 | PEG 2.81
Profitability: profit margin 35.3% | operating margin 42.5% | ROE 59.8%
Growth (YoY): revenue +2.1% | earnings -20.6%
Balance sheet: debt/equity 63.3% | free cash flow 37.67B
Risk: beta 0.34 | short interest 1.0% of float
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
Price target: mean 46.30 (+20.6% vs last close), range 39.65 - 62.75
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

- [Procter & Gamble (PG): Buy, Sell, or Hold Post Q2 Earnings?](https://www.tradingview.com/news/stockstory:4a27b3d7e094b:0-procter-gamble-pg-buy-sell-or-hold-post-q2-earnings/)  
  <sub>TradingView, 11 hours ago</sub>  
  Procter & Gamble currently trades at $147.39 per share and has shown little upside over the past six months, posting a middling return of 3%. The stock also...
- [Envestnet Asset Management Inc. Reduces Position in Procter & Gamble Company (The) $PG](https://www.marketbeat.com/instant-alerts/filing-envestnet-asset-management-inc-reduces-position-in-procter-gamble-company-the-pg-2026-09-24/)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Envestnet Asset Management Inc. decreased its position in Procter & Gamble Company (The) (NYSE:PG - Free Report) by 0.7% during the 2nd quarter,...
- [The Steelers Stock Report: Week 2 vs. The Patriots](https://www.steelcurtainnetwork.com/the-steelers-stock-report-week-2-vs-the-patriots/)  
  <sub>Steel Curtain Network, 2 hours ago</sub>  
  Welcome back to the Steelers Weekly Stock Report — where we track the rise and fall of momentum across the Steelers organization. Every week, the Steelers'...
- [3 Stocks With Pricing Power When Inflation And Rates Stay High](https://finance.yahoo.com/markets/stocks/articles/3-stocks-pricing-power-inflation-051636183.html)  
  <sub>Yahoo Finance, 10 hours ago</sub>  
  Bond yields are surging, oil is above $100, and rate expectations keep shifting, so the hunt is on for businesses that can still defend pricing and cash...
- [PG&E Corp. stock underperforms Wednesday when compared to competitors](https://www.marketwatch.com/data-news/pg-e-corp-stock-underperforms-wednesday-when-compared-to-competitors-a8529d77-095a96c36237?mod=goog_fin_scmw)  
  <sub>MarketWatch, 18 hours ago</sub>  
  slipped 3.65% to $12.41 Wednesday, on what proved to be an all-around rough trading session for the stock market, with the S&P 500 Index.
- [Procter & Gamble Tokenized Stock price today, PGX to USD chart, marketcap and volume](https://cryptoslate.com/coins/procter-gamble-tokenized-stock/)  
  <sub>CryptoSlate, 16 hours ago</sub>  
  Procter & Gamble Tokenized Stock price is $150.58 on Sep 24, 2026. Market cap $453.42K; 24h volume $34.28K.
- [Procter & Gamble stock reports 1.5 percent growth](https://www.ad-hoc-news.de/boerse/news/corporate-news/procter-and-gamble-stock-reports-1-5-percent-growth/70178185)  
  <sub>AD HOC NEWS, 39 minutes ago</sub>  
  Procter & Gamble stock posted USD 1.43 quarterly EPS against USD 1.41 consensus. Its USD 147.84 intraday quote on September 24, 2026, sits below the USD...
- [QRG Capital Management Inc. Purchases 28,048 Shares of Procter & Gamble Company (The) $PG](https://www.marketbeat.com/instant-alerts/filing-qrg-capital-management-inc-purchases-28048-shares-of-procter-gamble-company-the-pg-2026-09-23/)  
  <sub>MarketBeat, 16 hours ago</sub>  
  QRG Capital Management Inc. boosted its holdings in shares of Procter & Gamble Company (The) (NYSE:PG - Free Report) by 8.2% during the second quarter,...
- [Is the "AI" Chip Stock Momentum Rally Over?](https://finance.yahoo.com/technology/ai/articles/ai-chip-stock-momentum-rally-203300074.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Is the chip and "AI" tech stock momentum rally over for 2026? For That answer, let's bring in our Chief Equity Strategist and Economist, John Blank.
- [Fund Review: Bandhan Medium to Long Term Fund](https://www.business-standard.com/amp/finance/personal-finance/fund-review-bandhan-medium-to-long-term-fund-126092400883_1.html)  
  <sub>Business Standard, 4 hours ago</sub>  
  Fund Review: Bandhan Medium to Long Term Fund. Fund Review: Bandhan Medium to Long Term Fund. fiscal prudence money market. Representative Image.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 147.65 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 145.78 (+1.3%), 50d 146.11 (+1.1%), 200d 147.48 (+0.1%); 50d below 200d
Momentum: RSI(14) 56.3 | MACD 0.404 vs signal 0.131 (histogram 0.273)
Returns: 1d +0.2% | 5d +0.4% | 1m +0.7% | 3m -2.9%
52-week range: 138.04 - 167.20 (now 33.0% of the way up)
Volatility: ATR(14) 2.28 (1.5% of price) | annualised 20d 13.5%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 342.97B
Valuation: trailing P/E 22.31 | forward P/E 19.95 | P/B 6.43 | PEG 3.79
Profitability: profit margin 18.4% | operating margin 22.1% | ROE 30.3%
Growth (YoY): revenue +1.5% | earnings -15.5%
Balance sheet: debt/equity 64.5% | free cash flow 13.28B
Risk: beta 0.38 | short interest 1.2% of float
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
Price target: mean 160.61 (+8.8% vs last close), range 143.00 - 186.00
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

- [BCE Inc. (BCE.TO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/BCE.TO/)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  Find the latest BCE Inc. (BCE.TO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Royal Bank of Canada admits £475m notes to LSE trading](https://ca.investing.com/news/stock-market-news/royal-bank-of-canada-admits-475m-notes-to-lse-trading-93CH-4851838)  
  <sub>Investing.com Canada, 2 hours ago</sub>  
  LONDON - Royal Bank of Canada has admitted £475 million floating rate senior notes due September 2027 to trading on the London Stock Exchange's main market,...
- [Why Did Royal Bank of Canada (TSX:RY) Fall 2.027% on 23 September 2026?](https://kalkine.ca/news/financial/why-did-royal-bank-of-canada-tsxry-fall-2027-on-23-september-2026)  
  <sub>kalkine.ca, 16 minutes ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Royal Bank of Canada stock falls 2.03 percent ahead of the open](https://www.ad-hoc-news.de/boerse/news/corporate-news/royal-bank-of-canada-stock-falls-2-03-percent-ahead-of-the-open/70173814)  
  <sub>AD HOC NEWS, 10 hours ago</sub>  
  At the close on September 23, 2026, Royal Bank of Canada stock stood at CAD 281.35 in Toronto after falling 2.03 percent. The S&P/TSX Composite dropped 1.61...
- [Royal Bank of Canada announces NVCC subordinated debenture issue](https://www.theglobeandmail.com/investing/markets/stocks/RY/pressreleases/4765475/royal-bank-of-canada-announces-nvcc-subordinated-debenture-issue/)  
  <sub>The Globe and Mail, 18 hours ago</sub>  
  Detailed price information for Royal Bank of Canada (RY-N) from The Globe and Mail including charting and trades.
- [How Investors Are Reacting To Ligand Pharmaceuticals (LGND) Ryjunea Royalty Rights Deal](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nasdaq-lgnd/ligand-pharmaceuticals/news/how-investors-are-reacting-to-ligand-pharmaceuticals-lgnd-ry)  
  <sub>Simply Wall Street, 20 hours ago</sub>  
  Ligand Pharmaceuticals agreed to pay Sydnexis US$23 million upfront to acquire a 100% royalty interest on Ryjunea net sales in Europe, the Middle East,...
- [Royal Bank of Canada (TSX:RY): What Is Driving the Latest Story?](https://kalkinemedia.com/ca/stocks/bluechip/royal-bank-of-canada-tsxry-what-is-driving-the-latest-story)  
  <sub>Kalkine Media, 5 hours ago</sub>  
  Royal Bank of Canada coverage examines a current company development, its banking and capital markets operations and the S&P/TSX 60 backdrop in the latest...
- [Royal Bank of Canada Announces an Offering of $1.5 Billion of Non-Viability Contingent Capital Subordinated Debentures](https://www.marketscreener.com/news/royal-bank-of-canada-announces-an-offering-of-1-5-billion-of-non-viability-contingent-capital-subor-ce785adeda80f620)  
  <sub>www.marketscreener.com, 18 hours ago</sub>  
  Royal Bank of Canada announced an offering of $1.5 billion of non-viability contingent capital subordinated debentures through its Canadian Medium Term Note...
- [Royal Bank of Canada admits £475m notes to LSE trading By Investing.com](https://in.investing.com/news/stock-market-news/royal-bank-of-canada-admits-475m-notes-to-lse-trading-93CH-5604965)  
  <sub>Investing.com India, 2 hours ago</sub>  
  LONDON - Royal Bank of Canada has admitted £475 million floating rate senior notes due September 2027 to trading on the London Stock Exchange's main market,...
- [Royal Bank of Canada stock ends the day 1.50 percent lower](https://www.ad-hoc-news.de/boerse/news/nebenwerte/royal-bank-of-canada-stock-ends-the-day-1-50-percent-lower/70170510)  
  <sub>AD HOC NEWS, 18 hours ago</sub>  
  At the close on September 23, 2026, Royal Bank of Canada stock traded at USD 200.86 on the NYSE, down 1.50 percent. The session range was USD 20.51 to USD...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 198.63 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 205.23 (-3.2%), 50d 208.59 (-4.8%), 200d 185.18 (+7.3%); 50d above 200d
Momentum: RSI(14) 35.9 | MACD -1.895 vs signal -1.247 (histogram -0.648)
Returns: 1d -0.4% | 5d -1.8% | 1m -2.6% | 3m -1.7%
52-week range: 143.64 - 217.87 (now 74.1% of the way up)
Volatility: ATR(14) 3.36 (1.7% of price) | annualised 20d 18.8%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 274.99B
Valuation: trailing P/E 17.56 | forward P/E 15.63 | P/B 2.88 | PEG 2.26
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
Price target: mean 208.89 (+5.2% vs last close), range 184.01 - 226.43
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

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 39.54 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 37.75 (+4.7%), 50d 35.79 (+10.5%), 200d 33.32 (+18.7%); 50d above 200d
Momentum: RSI(14) 61.6 | MACD 0.957 vs signal 0.828 (histogram 0.129)
Returns: 1d +1.4% | 5d +2.6% | 1m +7.1% | 3m +15.5%
52-week range: 18.34 - 40.06 (now 97.6% of the way up)
Volatility: ATR(14) 1.23 (3.1% of price) | annualised 20d 32.8%
Volume: 0.31x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 46.12B
Valuation: trailing P/E 65.90 | forward P/E 12.99 | P/B 5.94 | PEG 0.73
Profitability: profit margin 4.1% | operating margin 4.0% | ROE 9.7%
Growth (YoY): revenue -0.8% | earnings n/a
Balance sheet: debt/equity 217.8% | free cash flow 2.22B
Risk: beta 0.80 | short interest n/a of float
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
Price target: mean 44.00 (+11.3% vs last close), range 40.00 - 50.00
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

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Toyota (TM) · Company — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Toyota's Akio Toyoda is the fourth in his family inducted into the Automotive Hall of Fame.](https://www.stocktitan.net/news/TM/toyota-motor-corporation-chairman-akio-toyoda-inducted-into-the-sd7sdm73fg9l.html)  
  <sub>Stock Titan, 4 hours ago</sub>  
  Toyota Motor (TM) Chairman Akio Toyoda was inducted into the Automotive Hall of Fame in Detroit. The induction took place the night before September 24,...
- [TransCode Therapeutics, Inc. (RNAZ) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RNAZ/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Find the latest TransCode Therapeutics, Inc. (RNAZ) stock quote, history, news and other vital information to help you with your stock trading and...
- [Liquidity Mapping Around (TM) Price Events](https://news.stocktradersdaily.com/news_release/139/Liquidity_Mapping_Around_TM_Price_Events_092326115202_1790221922.html)  
  <sub>Stock Traders Daily, 15 hours ago</sub>  
  Key findings for Toyota Motor Corporation (NYSE: TM). Near-Term Weak Sentiment May Signal Resumption of Long-Term Weakness After Neutral Shift...
- [EU car market grows in August, with BEVs taking 21.7% share (F:NYSE)](https://seekingalpha.com/news/4646411-eu-car-market-grows-in-august-with-bevs-taking-217-share)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  EU new passenger car registrations rose 4.5% Y/Y to 708,211 units in August, extending the market's growth streak to seven consecutive months as demand for...
- [Honda Motor Eyes First New North American Factory in Nearly 20 Years With $2.5 Billion Ohio Hybrid Plant: Report](https://www.benzinga.com/news/travel/26/09/61972939/honda-motor-eyes-first-new-north-american-factory-in-nearly-20-years-with-2-5-billion-ohio-hybrid-plant-report)  
  <sub>Benzinga, 57 minutes ago</sub>  
  Honda is reportedly weighing a $1.8B-$2.5B U.S. hybrid plant, potentially in Ohio, with operations targeted for 2030.
- [Stockton vs Penn St.-Abington - Men's Soccer - 9/23/2026 - Box Score](https://njacsports.com/boxscore.aspx?id=7ltyipP022aUJKmSgYVs3wXi7up73ghniwD5ElWyd07J7BNseBaMQePf0fY%2F3yUPJZZ%2FUDYxbgFxk5f%2FA1FZfVybJlbt1wRctFe8arxtW%2F9UApHWW4AmoTgbYGCe6GIfyErpvvgOLy9W07mvO3nD%2BES%2BiGNqmNVL2U55bGz9IVI%3D&path=msoc)  
  <sub>New Jersey Athletic Conference, 14 hours ago</sub>  
  Scoring Summary. Time, Team, Description. 46:32, PSA, Shane Lachawiec (1) Assisted By: Aramis Shire knocked in after long throw into the box. 61:02, Stock...
- [TM stock heads into the open after a 0.14 percent drop](https://www.ad-hoc-news.de/boerse/news/corporate-news/tm-stock-heads-into-the-open-after-a-0-14-percent-drop/70173371)  
  <sub>AD HOC NEWS, 11 hours ago</sub>  
  At the close on September 23, 2026, TM stock ended at USD 192.22 on the NYSE. The ADR traded from USD 191.67 to USD 193.51, while the S&P 500 fell 0.61...
- [Spring & Stitch Introduces Indoor Trampoline Ottoman (TM) as Families Seek Alternatives to Excessive Screen Time](https://markets.businessinsider.com/news/stocks/spring-stitch-introduces-indoor-trampoline-ottoman-tm-as-families-seek-alternatives-to-excessive-screen-time-1036568561)  
  <sub>markets.businessinsider.com, 20 hours ago</sub>  
  Spring & Stitch is highlighting its Trampoline Ottoman™ as an indoor way for kids to incorporate more movement and family interaction into t...
- [Lilly's FDA-approved weekly insulin could mean over 300 fewer shots a year than daily insulin](https://www.stocktitan.net/news/LLY/u-s-food-and-drug-administration-fda-approves-lilly-s-onswik-tm-7ef9xmbyiabi.html)  
  <sub>Stock Titan, 4 hours ago</sub>  
  Eli Lilly (LLY) received U.S. FDA approval on September 24, 2026, for Onswik, a once-weekly basal insulin for adults with type 2 diabetes.
- [Onco-Innovations Limited (ONCO.NE) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/ONCO.NE/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Find the latest Onco-Innovations Limited (ONCO.NE) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 186.62 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 194.07 (-3.8%), 50d 189.57 (-1.6%), 200d 201.94 (-7.6%); 50d below 200d
Momentum: RSI(14) 40.7 | MACD 0.089 vs signal 1.295 (histogram -1.206)
Returns: 1d -2.0% | 5d -2.9% | 1m -3.7% | 3m +11.2%
52-week range: 166.50 - 248.29 (now 24.6% of the way up)
Volatility: ATR(14) 3.34 (1.8% of price) | annualised 20d 21.6%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 220.99B
Valuation: trailing P/E 8.36 | forward P/E 11.83 | P/B 15.18 | PEG n/a
Profitability: profit margin 8.6% | operating margin 7.9% | ROE 12.4%
Growth (YoY): revenue +10.4% | earnings +86.9%
Balance sheet: debt/equity 115.0% | free cash flow -3.60T
Risk: beta 0.34 | short interest 0.1% of float
Next earnings: 2026-11-05
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 44% | 2026-03-31 beat by 12% | 2025-12-31 beat by 27% | 2025-09-30 beat by 24%
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
Consensus: strong_buy (mean 1.50 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 2 strong buy, 2 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 234.08 (+25.4% vs last close), range 230.00 - 239.31
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

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 757,877 shares
Distinct insiders: 0 buying, 0 selling
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

- [XOM|Exxon Mobil Corp|Price:163.220|Chg%:+1.990](https://www.tradingkey.com/markets/stocks/xom)  
  <sub>TradingKey, 6 hours ago</sub>  
  Valero shares declined due to profit-taking and valuation re-evaluations by investors. • The company reported an annual revenue of $115.97B and net profit of...
- [Exxon Mobil Corporation (XOM) Stock Price Today: $162.78](https://pluang.com/en/asset/usstock/XOM/10068)  
  <sub>Pluang, 6 hours ago</sub>  
  Key Stats ... Track Exxon Mobil Corporation (XOM) stock price today on Pluang, updated in real time with live charts and market data. Over the past 52 weeks,...
- [Analysts Have Conflicting Sentiments on These NA Companies: Huntsman (HUN) and Exxon Mobil (XOM)](https://www.theglobeandmail.com/investing/markets/stocks/XOM/pressreleases/4776372/analysts-have-conflicting-sentiments-on-these-na-companies-huntsman-hun-and-exxon-mobil-xom/)  
  <sub>The Globe and Mail, 2 hours ago</sub>  
  Detailed price information for Exxonmobil Holdings Corp (XOM-N) from The Globe and Mail including charting and trades.
- [XOM Jan 2029 105.000 put (XOM290119P00105000) interactive stock chart](https://uk.finance.yahoo.com/quote/XOM290119P00105000/chart/)  
  <sub>Yahoo Finance UK, 7 hours ago</sub>  
  Interactive chart for XOM Jan 2029 105.000 put (XOM290119P00105000) – analyse all of the data with a huge range of indicators.
- [US-Israel Strikes On Iran Send Nasdaq, S&P 500 Futures Lower As Offensive Continues Across The Middle East — LMT, RTX, XOM, USO, BATL On Traders' Radar Today](https://stocktwits.com/news-articles/markets/equity/nasdaq-sp-500-futures-decline-us-israel-strikes-on-iran-crude-oil-price-soars/cZd35CDRIcM)  
  <sub>Stocktwits, 2 hours ago</sub>  
  Data from Stocktwits showed that retail sentiment on SPY has remained 'bullish', while it hovered in the 'bearish' territory on QQQ.
- [Should Record Oil Output Require Action From ExxonMobil (XOM) Investors?](https://simplywall.st/stocks/us/energy/nyse-xom/exxonmobil-holdings/news/should-record-oil-output-require-action-from-exxonmobil-xom)  
  <sub>Simply Wall Street, 14 hours ago</sub>  
  ExxonMobil Holdings recently reported record oil output and revenue, delivered with lower capital spending and supported by higher production from high...
- [ExxonMobil Corporation $XOM Shares Purchased by Envestnet Portfolio Solutions Inc.](https://www.marketbeat.com/instant-alerts/filing-exxonmobil-corporation-xom-shares-purchased-by-envestnet-portfolio-solutions-inc-2026-09-23/)  
  <sub>MarketBeat, 16 hours ago</sub>  
  Envestnet Portfolio Solutions Inc. grew its stake in shares of ExxonMobil Corporation (NYSE:XOM - Free Report) by 13.6% during the second quarter,...
- [3 Companies With a Strong History of Dividend Growth](https://www.tradingview.com/news/zacks:d3d3992a3094b:0-3-companies-with-a-strong-history-of-dividend-growth/)  
  <sub>TradingView, 16 hours ago</sub>  
  Dividends come with many great perks, with the payouts essentially reflecting a form of 'payday' in the market.And several stocks with a strong history of...
- [If Hormuz Stays Shut, How High Can Exxon Go?](https://247wallst.com/investing/2026/09/23/if-hormuz-stays-shut-how-high-can-exxon-go/?tpid=1665925&tv=link&tc=in_content)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  XOM sits 35% higher year-to-date at $159 but shed 6% last week on diplomatic hopes for a Hormuz reopening that hasn't materialized.
- [XOM Oct 2026 155.000 put (XOM261030P00155000) interactive stock chart](https://uk.finance.yahoo.com/quote/XOM261030P00155000/chart/)  
  <sub>Yahoo Finance UK, 13 hours ago</sub>  
  Interactive chart for XOM Oct 2026 155.000 put (XOM261030P00155000) – analyse all of the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 164.22 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 162.35 (+1.1%), 50d 158.89 (+3.4%), 200d 147.57 (+11.3%); 50d above 200d
Momentum: RSI(14) 54.3 | MACD 1.159 vs signal 1.711 (histogram -0.553)
Returns: 1d +1.9% | 5d +0.6% | 1m +0.1% | 3m +20.0%
52-week range: 110.64 - 171.47 (now 88.1% of the way up)
Volatility: ATR(14) 3.83 (2.3% of price) | annualised 20d 28.8%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 675.26B
Valuation: trailing P/E 21.14 | forward P/E 15.15 | P/B 2.60 | PEG 1.36
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
Price target: mean 171.91 (+4.7% vs last close), range 142.00 - 200.00
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

### Farm goods basket (DBA) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [As AI Faces a Number of Critical Bottlenecks, Exposures Now Available in One Ticker Via xETFs AI Bottlenecks ETF (NECK)](https://sg.finance.yahoo.com/news/ai-faces-number-critical-bottlenecks-151900321.html)  
  <sub>Yahoo Finance Singapore, 24 hours ago</sub>  
  The development of Artificial Intelligence (“AI”) is only as fast as its slowest physical input; NECK provides targeted exposure to companies in Memory;...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 28.53 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 28.90 (-1.3%), 50d 28.29 (+0.8%), 200d 27.08 (+5.4%); 50d above 200d
Momentum: RSI(14) 48.8 | MACD 0.068 vs signal 0.175 (histogram -0.106)
Returns: 1d -0.1% | 5d -1.0% | 1m +0.8% | 3m +7.4%
52-week range: 25.44 - 29.49 (now 76.4% of the way up)
Volatility: ATR(14) 0.29 (1.0% of price) | annualised 20d 14.8%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

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

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 27.60M | fund size: 787.57M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Top ETFs: Live Prices, Returns & Trends](https://www.tradingkey.com/markets/etf/top?page=7)  
  <sub>TradingKey, 22 hours ago</sub>  
  View the latest market data on top ETFs to watch, from price movements and trading volume to historical returns and performance trends.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 33.31 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 32.40 (+2.8%), 50d 30.75 (+8.3%), 200d 27.84 (+19.6%); 50d above 200d
Momentum: RSI(14) 64.9 | MACD 0.731 vs signal 0.800 (histogram -0.069)
Returns: 1d +1.3% | 5d +0.4% | 1m +7.6% | 3m +25.9%
52-week range: 22.07 - 33.68 (now 96.8% of the way up)
Volatility: ATR(14) 0.47 (1.4% of price) | annualised 20d 18.1%
Volume: 0.32x the 20-day average
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
Three-year record: +13.6% a year | beta to the market 1.05
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
  Natural gas: 3,298.0 billion cubic feet, +44.0 on the week (a build), 71% percentile over 52 weeks
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
Share count change: 1 week: +1.7% (29.90M) over 7d
Shares outstanding: 55.14M | fund size: 1.84B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Best Performing ETFs: Top Returns at a Glance](https://www.tradingkey.com/markets/etf/best-performing?page=3)  
  <sub>TradingKey, 22 hours ago</sub>  
  View TradingKey's list of the best performing ETFs, including price changes, trading volume, multi-period returns, and performance charts.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 92.47 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 93.89 (-1.5%), 50d 94.56 (-2.2%), 200d 95.62 (-3.3%); 50d below 200d
Momentum: RSI(14) 32.4 | MACD -0.526 vs signal -0.436 (histogram -0.091)
Returns: 1d -0.2% | 5d -0.6% | 1m -2.5% | 3m -4.2%
52-week range: 92.47 - 97.74 (now 0.0% of the way up)
Volatility: ATR(14) 0.46 (0.5% of price) | annualised 20d 6.5%
Volume: 0.77x the 20-day average
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
Three-year record: +9.4% a year | beta to the market 1.08
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
Share count change: 1 week: -0.4% (-53.90M) over 7d
Shares outstanding: 159.52M | fund size: 14.75B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Just how high will the U.S. 10-year yield rise by year-end?](https://seekingalpha.com/news/4646648-just-how-high-will-the-u-s-10-year-yield-rise-by-year-end)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  The U.S. 10-year Treasury yield (US10Y) has climbed to a 19-year high, topping 5.15% and marking its strongest reading since July 2007.
- [Daily ETF Flows: IGV & MAGS See Inflows](https://www.etf.com/sections/daily-etf-flows/daily-etf-flows-igv-mags-see-inflows)  
  <sub>ETF.com, 18 hours ago</sub>  
  Here are the daily ETF fund flows for September 22, 2026.
- [U.S. ETF Express | MicroSectors Gold Miners -3X Inverse Leveraged ETNs Was the Top Gainer, Rising 13.86%](https://www.moomoo.com/news/post/1000121731/us-etf-express-microsectors-gold-miners-3x-inverse-leveraged-etns)  
  <sub>Moomoo, 18 hours ago</sub>  
  TopGainers/Losers643 U.S. ETFs rose and 5498 fell today.The top gainer was $MicroSectors Gold Miners -3X Inverse Leveraged ETNs(GDXD.
- [Treasury Yields Surge as Stocks Fall and Dollar Rises](https://mottcapitalmanagement.com/treasury-yields-and-stock-market/)  
  <sub>Mott Capital Management, 18 hours ago</sub>  
  Treasury yields surged after strong PMI data as the S&P 500 fell, the dollar strengthened, and signs of widening credit spreads emerged.
- [BNP Paribas sees deficits, rate burden, and midterms lifting long-end yields](https://seekingalpha.com/news/4646610-bnp-paribas-sees-deficits-rate-burden-and-midterms-lifting-long-end-yields)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  A popular market narrative attributes much of that move to fiscal deficits. According to analysis from BNP Paribas, the evidence so far points in the...
- [Exchange Traded Funds Top 10 Volume Leaders](https://www.bitget.com/amp/news/detail/12560605865522)  
  <sub>Bitget, 17 hours ago</sub>  
  NET % VOL STOCK (Symbol) LAST CHG CHG 100s Direxion Semicon Br 3x SOXS 33.66 1.24 3.82 81571120 GrShr 2x Sh NVDA Daily NVD 3.72 0.11 3.05 80616293 ProS...
- [iShares 20+ Year Treasury Bond ETF (TLT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TLT/)  
  <sub>Yahoo! Finance Canada, 13 hours ago</sub>  
  Find the latest iShares 20+ Year Treasury Bond ETF (TLT) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 77.95 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 78.93 (-1.2%), 50d 79.30 (-1.7%), 200d 80.00 (-2.6%); 50d below 200d
Momentum: RSI(14) 28.1 | MACD -0.346 vs signal -0.271 (histogram -0.076)
Returns: 1d -0.2% | 5d -0.6% | 1m -2.2% | 3m -2.4%
52-week range: 77.95 - 81.28 (now 0.0% of the way up)
Volatility: ATR(14) 0.26 (0.3% of price) | annualised 20d 4.7%
Volume: 0.51x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: High Yield Bond
Yield: 5.9%
Credit quality: BB 57.9%, B 32.2%, Below B 8.3%, BBB 1.1%
Three-year record: +8.3% a year | beta to the market 0.67
Cost and size: expense ratio 0.49% | net assets 16.19B
What it is made of: Bonds 98.6%, Cash 1.2%, Preferred 0.2%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 1.3%
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
Share count change: 1 week: -0.1% (-21.79M) over 7d
Shares outstanding: 205.89M | fund size: 16.05B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Your Bond ETF Lost Money. The Next ETF You Buy Could Matter More](https://www.benzinga.com/etfs/specialty-etfs/26/09/61956369/your-bond-etf-lost-money-the-next-etf-you-buy-could-matter-more)  
  <sub>Benzinga, 20 hours ago</sub>  
  Bond ETFs are down as Treasury yields rise. Here's how tax-loss harvesting could give investors a chance to reset interest-rate exposure.
- [Best Performing ETFs: Top Returns at a Glance](https://www.tradingkey.com/markets/etf/best-performing?page=3)  
  <sub>TradingKey, 22 hours ago</sub>  
  View TradingKey's list of the best performing ETFs, including price changes, trading volume, multi-period returns, and performance charts.
- [Daily ETF Flows: IGV MAGS See Inflows](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-igv-mags-210351200.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Top 10 Creations (All ETFs). Ticker. Name. Net Flows ($, mm). AUM ($, mm). AUM % Change. IVV · iShares Core S&P 500 ETF. 11,691.50. 868,900.07. 1.35%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 89.90 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 91.65 (-1.9%), 50d 92.56 (-2.9%), 200d 94.71 (-5.1%); 50d below 200d
Momentum: RSI(14) 27.6 | MACD -0.685 vs signal -0.563 (histogram -0.123)
Returns: 1d -0.3% | 5d -0.9% | 1m -3.3% | 3m -5.1%
52-week range: 89.90 - 97.99 (now 0.0% of the way up)
Volatility: ATR(14) 0.45 (0.5% of price) | annualised 20d 5.9%
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
Three-year record: +3.3% a year | beta to the market 1.16
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
Share count change: 1 week: -0.2% (-96.04M) over 7d
Shares outstanding: 458.94M | fund size: 41.26B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [iShares Russell 2000 ETF (Dinari Tokenized ETF) (IWM) Price Prediction for 2026 to 2031](https://www.bybit.com/en/price-prediction/ishares-russell-2000-etf-dinari-tokenized-etf/)  
  <sub>Bybit, 19 hours ago</sub>  
  IWM Price Prediction 2028. Forecast data for 2028 places iShares Russell 2000 ETF (Dinari Tokenized ETF)'s expected price at approximately $310.75. Historically...
- [BofA identifies Russell 2000 stocks positioned for Fed hiking cycles (IWM:NYSEARCA)](https://seekingalpha.com/news/4646016-bofa-identifies-russell-2000-stocks-positioned-for-fed-hiking-cycles)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  BofA flags Russell 2000 small-cap stocks built for Fed rate hikes, using value and profitability factors.
- [Nasdaq 100 Slips, 10-Year Yields Hit 19-Year Highs: Stock Market Today](https://www.tradingview.com/news/benzinga:61150b18e094b:0-nasdaq-100-slips-10-year-yields-hit-19-year-highs-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks slid at midday Wednesday as the 10-year Treasury yield surged to its highest level since 2007, after blowout September PMI data cemented bets...
- [Exchange-Traded Funds, US Equities Decline After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-us-equities-171556743.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV were lower. Actively traded Invesco QQQ Trust (QQQ) shed 1.2%.
- [Daily ETF Flows: IGV & MAGS See Inflows](https://www.etf.com/sections/daily-etf-flows/daily-etf-flows-igv-mags-see-inflows)  
  <sub>ETF.com, 18 hours ago</sub>  
  Ticker, Name, Net Flows ($, mm), AUM ($, mm), AUM % Change. IVV · iShares Core S&P 500 ETF, 11,691.50, 868,900.07, 1.35%. IWM · iShares Russell 2000 ETF...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 279.61 (bar of 2026-09-24), from 502 daily bars
Trend: vs 20d SMA 289.40 (-3.4%), 50d 294.23 (-5.0%), 200d 275.52 (+1.5%); 50d above 200d
Momentum: RSI(14) 31.8 | MACD -3.807 vs signal -3.028 (histogram -0.779)
Returns: 1d -0.8% | 5d -2.0% | 1m -6.6% | 3m -6.5%
52-week range: 229.11 - 305.09 (now 66.5% of the way up)
Volatility: ATR(14) 3.48 (1.2% of price) | annualised 20d 13.0%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Small Blend
What it holds: P/E 17.30 | P/B 2.13 | P/S 1.31 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +19.1% a year | beta to the market 1.24
Cost and size: expense ratio 0.19% | net assets 80.46B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: JFrog Ltd Ordinary Shares 0.3%, Moog Inc Class A 0.3%, BlackRock Cash Funds Treasury SL Agency 0.3%, UMB Financial Corp 0.3%, Glaukos Corp 0.3%
Sector mix: Healthcare 21.0%, Financial services 18.1%, Technology 13.8%, Industrials 13.2%
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
Rolled up from the 5 largest holdings, 1.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.5% above the current prices
Holdings read: FROG, MOG-A, XTSLA, UMBF, GKOS
Recent rating changes among them:
  - FROG: 2026-09-04 DA Davidson: main, Buy -> Buy
  - MOG-A: 2026-09-15 Guggenheim: init, ? -> Neutral
  - UMBF: 2026-09-14 UBS: init, ? -> Neutral
  - GKOS: 2026-09-22 Jefferies: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 19.6% of open interest (496,762 contracts)
Change on the week: +6.0% of open interest
Crowding: 30% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 281.05M | fund size: 78.59B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 103.44 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 105.12 (-1.6%), 50d 105.94 (-2.4%), 200d 108.69 (-4.8%); 50d below 200d
Momentum: RSI(14) 31.9 | MACD -0.581 vs signal -0.502 (histogram -0.079)
Returns: 1d -0.4% | 5d -1.0% | 1m -2.6% | 3m -5.5%
52-week range: 103.44 - 112.92 (now 0.0% of the way up)
Volatility: ATR(14) 0.58 (0.6% of price) | annualised 20d 7.0%
Volume: 0.40x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Corporate Bond
Yield: 4.7%
Credit quality: A 46.6%, BBB 40.2%, AA 12.3%, AAA 1.0%
Three-year record: +5.0% a year | beta to the market 1.35
Cost and size: expense ratio 0.14% | net assets 32.04B
What it is made of: Bonds 98.9%, Cash 1.1%, Convertible 0.0%
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
Direction: money going out (1 week)
Share count change: 1 week: -0.7% (-215.62M) over 7d
Shares outstanding: 305.07M | fund size: 31.56B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Should NYLIM U.S. Large Cap R&D Leaders ETF (LRND) Be on Your Investing Radar?](https://finance.yahoo.com/markets/stocks/articles/nylim-u-large-cap-r-092003860.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Launched on February 8, 2022, the NYLIM U.S. Large Cap R&D Leaders ETF (LRND) is a passively managed exchange traded fund designed to provide a broad...
- [Dow Jones Futures Fall As Treasury Yields, Oil Prices Keep Rising. Meta, Everpure, Grail Are Early Movers.](https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-treasury-yields-soar-palantir-palo-alto-buy-signal/)  
  <sub>Investor's Business Daily, 3 hours ago</sub>  
  Dow Jones futures fell early Thursday, along with S&P 500 futures and especially Nasdaq futures. The 30-year Treasury yield hit a fresh long-term high while...
- [Dow Jones Futures: Stocks Fall As Treasury Yields Soar; Palantir Flashes Buy Signal](https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-stocks-fall-as-treasury-yields-soar-palantir-flashes-buy-signal/)  
  <sub>Investor's Business Daily, 18 hours ago</sub>  
  Dow Jones futures: The stock market fell as Treasury yields skyrocketed and oil prices rose, but Palantir and Palo Alto flashed buy signals.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 210.32 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 215.97 (-2.6%), 50d 217.09 (-3.1%), 200d 205.13 (+2.5%); 50d above 200d
Momentum: RSI(14) 32.5 | MACD -1.947 vs signal -1.288 (histogram -0.659)
Returns: 1d -0.5% | 5d -0.9% | 1m -5.2% | 3m -0.0%
52-week range: 182.18 - 222.77 (now 69.3% of the way up)
Volatility: ATR(14) 1.80 (0.9% of price) | annualised 20d 8.8%
Volume: 0.38x the 20-day average
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
Three-year record: +16.1% a year | beta to the market 0.83
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
Weighted price target: -2.3% above the current prices
Holdings read: MRNA, VEEV, ZBRA, CRL, DASH
Recent rating changes among them:
  - MRNA: 2026-09-03 Rothschild & Co: down, Neutral -> Sell
  - VEEV: 2026-08-28 Citigroup: main, Neutral -> Neutral
  - ZBRA: 2026-09-15 Needham: main, Buy -> Buy
  - CRL: 2026-09-11 Evercore ISI Group: main, Outperform -> Outperform
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
Share count change: 1 week: +1.1% (1.07B) over 7d
Shares outstanding: 474.25M | fund size: 99.74B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [iShares 20+ Year Treasury Bond ETF (TLT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TLT/)  
  <sub>Yahoo! Finance Canada, 13 hours ago</sub>  
  Find the latest iShares 20+ Year Treasury Bond ETF (TLT) stock quote, history, news and other vital information to help you with your stock trading and...
- [Top ETFs: Live Prices, Returns & Trends](https://www.tradingkey.com/markets/etf/top?page=37)  
  <sub>TradingKey, 13 hours ago</sub>  
  View the latest market data on top ETFs to watch, from price movements and trading volume to historical returns and performance trends.
- [(SHY) Price Dynamics and Execution-Aware Positioning](https://news.stocktradersdaily.com/news_release/8/SHY_Price_Dynamics_and_Execution-Aware_Positioning_092326034002_1790192402.html)  
  <sub>Stock Traders Daily, 24 hours ago</sub>  
  Price-action only: Ishares 1-3 Year Treasury Bond Etf (SHY) movements set the tone for institutional models. (SHY) Price Dynamics and Execution-Aware...
- [BNP Paribas sees deficits, rate burden, and midterms lifting long-end yields](https://seekingalpha.com/news/4646610-bnp-paribas-sees-deficits-rate-burden-and-midterms-lifting-long-end-yields)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  A popular market narrative attributes much of that move to fiscal deficits. According to analysis from BNP Paribas, the evidence so far points in the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 81.11 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 81.53 (-0.5%), 50d 81.78 (-0.8%), 200d 82.32 (-1.5%); 50d below 200d
Momentum: RSI(14) 27.1 | MACD -0.194 vs signal -0.159 (histogram -0.036)
Returns: 1d -0.0% | 5d -0.2% | 1m -1.1% | 3m -1.2%
52-week range: 81.11 - 83.18 (now 0.0% of the way up)
Volatility: ATR(14) 0.11 (0.1% of price) | annualised 20d 1.9%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Short Government
Yield: 3.6%
Credit quality: AA 100.0% | US government debt 99.2%
Three-year record: +4.0% a year | beta to the market 0.22
Cost and size: expense ratio 0.15% | net assets 25.91B
What it is made of: Bonds 99.2%, Cash 0.8%
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
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 29.2% of open interest (4,433,736 contracts)
Change on the week: +0.5% of open interest
Crowding: 95% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.1% (17.34M) over 7d
Shares outstanding: 318.83M | fund size: 25.86B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Technical Reactions to TIP Trends in Macro Strategies](https://news.stocktradersdaily.com/news_release/78/Technical_Reactions_to_TIP_Trends_in_Macro_Strategies_092326113402_1790220842.html)  
  <sub>Stock Traders Daily, 16 hours ago</sub>  
  Key findings for Ishares Tips Bond Etf (NYSE: TIP). Full Alignment in Neutral Sentiment Favors Wait-and-See Approach; No clear price positioning signal...
- [Bonds are getting thumped as yields surge. Here’s what it means for the 60/40 portfolio](https://www.cnbc.com/2026/09/23/bonds-get-thumped-as-yields-surge-what-it-means-for-60/40-portfolio.html)  
  <sub>CNBC, 19 hours ago</sub>  
  For the long-term investor, it doesn't hurt to check duration and credit quality, as well as shop around for inflation protection.
- [One Tech Tip: iOS 27 comes with revamped screen time controls and other useful new features](https://www.barchart.com/story/news/4768698/one-tech-tip-ios-27-comes-with-revamped-screen-time-controls-and-other-useful-new-features)  
  <sub>Barchart.com, 11 hours ago</sub>  
  Apple's latest operating system, iOS 27, introduces a more advanced Siri assistant and several new features for iPhone users.
- [Best Performing ETFs: Top Returns at a Glance](https://www.tradingkey.com/markets/etf/best-performing?page=43)  
  <sub>TradingKey, 8 hours ago</sub>  
  View TradingKey's list of the best performing ETFs, including price changes, trading volume, multi-period returns, and performance charts.
- [LTPZ: Avoiding Longer-Maturity Inflation Protection Allocations (NYSEARCA:LTPZ)](https://seekingalpha.com/article/4949125-ltpz-avoiding-longer-maturity-inflation-protection-allocations)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Summary. PIMCO 15+ Year U.S. TIPS ETF (LTPZ) offers high real yield but carries significant duration risk in time of current rate uncertainty.
- [Precision Trading with Pimco 1-5 Year U.s. Tips Index Exchange-traded Fund (STPZ) Risk Zones](https://news.stocktradersdaily.com/news_release/150/Precision_Trading_with_Pimco_1-5_Year_U.s._Tips_Index_Exchange-traded_Fund_STPZ_Risk_Zones_092326082202_1790209322.html)  
  <sub>Stock Traders Daily, 19 hours ago</sub>  
  Key findings for Pimco 1-5 Year U.s. Tips Index Exchange-traded Fund (NASDAQ: STPZ). Full Alignment in Neutral Sentiment Favors Wait-and-See Approach...
- [Top ETFs: Live Prices, Returns & Trends](https://www.tradingkey.com/markets/etf/top?page=59)  
  <sub>TradingKey, 5 hours ago</sub>  
  View the latest market data on top ETFs to watch, from price movements and trading volume to historical returns and performance trends.
- [Making $150K at 45 and Maxing Your 401(k)? These 3 ETFs Put the Rest of Your Savings to Work](https://247wallst.com/investing/etf/2026/09/23/making-150k-at-45-and-maxing-your-401k-these-3-etfs-put-the-rest-of-your-savings-to-work/)  
  <sub>24/7 Wall St., 17 hours ago</sub>  
  Once your 401(k) hits its ceiling, your after-tax dollars face a completely different set of rules, and most investors at this income level get the next...
- [Just how high will the U.S. 10-year yield rise by year-end?](https://seekingalpha.com/news/4646648-just-how-high-will-the-u-s-10-year-yield-rise-by-year-end)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  The U.S. 10-year Treasury yield (US10Y) has climbed to a 19-year high, topping 5.15% and marking its strongest reading since July 2007.
- [BNP Paribas sees deficits, rate burden, and midterms lifting long-end yields](https://seekingalpha.com/news/4646610-bnp-paribas-sees-deficits-rate-burden-and-midterms-lifting-long-end-yields)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  A popular market narrative attributes much of that move to fiscal deficits. According to analysis from BNP Paribas, the evidence so far points in the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 104.53 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 106.27 (-1.6%), 50d 106.94 (-2.3%), 200d 109.54 (-4.6%); 50d below 200d
Momentum: RSI(14) 26.6 | MACD -0.614 vs signal -0.460 (histogram -0.154)
Returns: 1d -0.3% | 5d -0.8% | 1m -2.5% | 3m -4.4%
52-week range: 104.53 - 112.20 (now 0.0% of the way up)
Volatility: ATR(14) 0.40 (0.4% of price) | annualised 20d 4.6%
Volume: 0.35x the 20-day average
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
Three-year record: +3.8% a year | beta to the market 0.68
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
Share count change: 1 week: +0.2% (22.98M) over 7d
Shares outstanding: 142.11M | fund size: 14.85B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [iShares 20+ Year Treasury Bond ETF (TLT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TLT/)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  iShares 20+ Year Treasury Bond ETF (TLT) · -0.52% · -1.94% · -6.86% · -8.42% · -9.92% · -45.77% · -1.58%.
- [Biggest Long-Bond ETF Hits Record Low as Traders Dump Treasuries](https://www.bloomberg.com/news/articles/2026-09-23/biggest-long-bond-etf-hits-record-low-as-traders-dump-treasuries)  
  <sub>Bloomberg, 19 hours ago</sub>  
  Shares of the largest exchange-traded fund tracking long-dated Treasuries closed at a record low as the yearslong bond market selloff shows few signs of...
- [TLT: Long Bonds Getting Interesting (NASDAQ:TLT)](https://seekingalpha.com/article/4949270-tlt-long-bonds-getting-interesting)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  Summary. iShares 20+ Year Treasury Bond ETF offers nearly 4.9% yield as long-term Treasury yields reach multi-year highs amid persistent inflation and...
- [Treasury Yield Surge Could Be A ‘Headwind’ For Risk Assets, Says Verdence CIO – Flags Pressure On AI Funding](https://www.google.com/goto?url=CAES3QEB6zswFTedQkZMPy9b3fBR4yP-Ny71XHiQ2Ja570yfuX-aOkdaoW5wu-nC3vpYwDjLFZs346wGwQewzzXPEZuY6QMkN7Y4jMud0HIz4OQKll6h66tMyhN_e08aysH1Y24WBvOrQ7L8PC7bGjZ-rnow0TgZ_toxc_dVq79wW8ZRQcBMZx6lYw7m5LYG0IvcDqd80w3VpE1tbSUzYfDwfJflp9Qy3eMuq1dWdkDijVtoDqXL8UAEjG-UBs7h-IqboEiz21r71PO7mfqUOg8-xUgEzPyQflGYZJroRKUJLQ)  
  <sub>TradingView, 2 hours ago</sub>  
  Verdence Capital Advisors Chief Investment Officer Megan Horneman said Thursday that the whole Treasury yield curve is becoming a “headwind” for risk assets...
- [Surging bond yields mark end of decade-long TINA era (TLT:NASDAQ)](https://seekingalpha.com/news/4646707-surging-bond-yields-mark-end-of-decade-long-tina-era)  
  <sub>Seeking Alpha, 37 minutes ago</sub>  
  TINA is fading as bond yields surge: 84% of fixed income now yields 4%+.
- [iShares 20+ Year Treasury Bond stock Analysis: September 2026 Bearish Trend Update](https://en.cryptonomist.ch/2026/09/24/ishares-20-year-treasury-bond-stock-sinks-to-80-46-as-20-year-yields-near-5-3/)  
  <sub>The Cryptonomist, 4 hours ago</sub>  
  Explore the latest bearish trend in iShares 20+ Year Treasury Bond stock as TLT hits record lows amid rising Treasury yields.
- [Nasdaq, Dow, S&P 500 Futures Slip As Chip Selloff Overshadows Strong Earnings Season: NFLX, SNDK, SPCX, MRVL Stocks In Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-dow-s-and-p-500-futures-slip-as-chip-selloff-overshadows-strong-earnings-season/cZZ7beBR7tP)  
  <sub>Stocktwits, 8 hours ago</sub>  
  U.S. markets bled amid rising AI concerns after Taiwan Semiconductor Manufacturing massively hiked its capital expenditures for 2026.
- [Traders price in 4 Fed rate hikes by June 2027 as bitcoin slides below $83,000](https://cryptonews.net/news/finance/33488508/)  
  <sub>Cryptonews.net, 5 hours ago</sub>  
  U.S. Treasury yields across the entire curve are pushing to new highs as traders prepare for a longer stretch of tighter monetary policy.
- [Daily ETF Flows: IGV MAGS See Inflows](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-igv-mags-210351200.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Top 10 Creations (All ETFs). Ticker. Name. Net Flows ($, mm). AUM ($, mm). AUM % Change. IVV · iShares Core S&P 500 ETF. 11,691.50. 868,900.07. 1.35%.
- [US 10-Year Yield Hits Nearly Two-Decade-High: El-Erian Says It ‘Shouldn't Be As Big A Surprise’](https://www.tradingview.com/news/stocktwits:d8694a10c094b:0-us-10-year-yield-hits-nearly-two-decade-high-el-erian-says-it-shouldn-t-be-as-big-a-surprise/)  
  <sub>TradingView, 14 hours ago</sub>  
  The U.S. 10-year Treasury yield surged about 13 to 17 basis points in a single day on Wednesday to close at 5.11%, notching its highest level since July...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 79.82 (bar of 2026-09-24), from 502 daily bars
Trend: vs 20d SMA 81.58 (-2.2%), 50d 82.35 (-3.1%), 200d 85.72 (-6.9%); 50d below 200d
Momentum: RSI(14) 34.2 | MACD -0.516 vs signal -0.446 (histogram -0.071)
Returns: 1d -0.8% | 5d -2.4% | 1m -4.4% | 3m -8.6%
52-week range: 79.82 - 92.06 (now 0.0% of the way up)
Volatility: ATR(14) 0.73 (0.9% of price) | annualised 20d 9.7%
Volume: 0.39x the 20-day average
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
Three-year record: +0.5% a year | beta to the market 2.39
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
Shares outstanding: 109.70M | fund size: 8.76B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 28.72 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 28.21 (+1.8%), 50d 28.22 (+1.8%), 200d 27.73 (+3.6%); 50d above 200d
Momentum: RSI(14) 73.7 | MACD 0.117 vs signal 0.047 (histogram 0.071)
Returns: 1d +0.2% | 5d +1.1% | 1m +2.7% | 3m +0.6%
52-week range: 26.47 - 28.72 (now 100.0% of the way up)
Volatility: ATR(14) 0.11 (0.4% of price) | annualised 20d 4.9%
Volume: 0.13x the 20-day average
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
Share count change: 1 week: -1.1% (-3.32M) over 7d
Shares outstanding: 10.50M | fund size: 301.49M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [(VGK) Movement Within Algorithmic Entry Frameworks](https://news.stocktradersdaily.com/news_release/81/VGK_Movement_Within_Algorithmic_Entry_Frameworks_092426064811_1790246891.html)  
  <sub>Stock Traders Daily, 8 hours ago</sub>  
  Key findings for Vanguard Ftse Europe Etf (NYSE: VGK). Neutral Near and Mid-Term Readings Could Moderate Long-Term Positive Bias; Support is being tested.
- [Top ETFs: Live Prices, Returns & Trends](https://www.tradingkey.com/markets/etf/top?page=142)  
  <sub>TradingKey, 10 hours ago</sub>  
  View the latest market data on top ETFs to watch, from price movements and trading volume to historical returns and performance trends.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 87.56 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 90.19 (-2.9%), 50d 90.55 (-3.3%), 200d 87.45 (+0.1%); 50d above 200d
Momentum: RSI(14) 35.2 | MACD -0.831 vs signal -0.519 (histogram -0.312)
Returns: 1d -0.5% | 5d -1.2% | 1m -5.5% | 3m +0.7%
52-week range: 77.90 - 93.19 (now 63.1% of the way up)
Volatility: ATR(14) 0.92 (1.0% of price) | annualised 20d 11.7%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Europe Stock
What it holds: P/E 17.85 | P/B 2.31 | P/S 1.64 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +18.7% a year | beta to the market 0.90
Cost and size: expense ratio 0.06% | net assets 39.06B
What it is made of: Stocks 99.0%, Cash 0.7%, Other 0.3%
Largest holdings: ASML Holding NV 4.0%, HSBC Holdings PLC 2.2%, Roche Holding AG Ordinary Shares new 1.9%, Novartis AG Registered Shares 1.7%, Shell PLC 1.6%
Sector mix: Financial services 25.3%, Industrials 19.8%, Healthcare 12.1%, Technology 9.0%
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
Rolled up from the 5 largest holdings, 11.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 65.7% | hold 34.3% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.3% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, NOVN.SW, SHEL.L
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 4.7% of open interest (626,488 contracts)
Change on the week: -0.4% of open interest
Crowding: 95% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: -0.0% (-8.61M) over 7d
Shares outstanding: 438.21M | fund size: 38.37B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 59.73 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 60.41 (-1.1%), 50d 59.75 (-0.0%), 200d 57.76 (+3.4%); 50d above 200d
Momentum: RSI(14) 46.6 | MACD -0.011 vs signal 0.068 (histogram -0.079)
Returns: 1d -0.6% | 5d +0.9% | 1m -0.4% | 3m +1.3%
52-week range: 52.42 - 61.44 (now 81.0% of the way up)
Volatility: ATR(14) 0.66 (1.1% of price) | annualised 20d 14.0%
Volume: 0.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Diversified Emerging Mkts
What it holds: P/E 15.91 | P/B 2.13 | P/S 1.86 | 3y earnings growth n/a
Yield: 2.3%
Three-year record: +18.8% a year | beta to the market 0.75
Cost and size: expense ratio 0.06% | net assets 168.36B
What it is made of: Stocks 95.3%, Cash 4.6%, Other 0.1%, Preferred 0.0%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 14.7%, Tencent Holdings Ltd 2.9%, Alibaba Group Holding Ltd Ordinary Shares 2.2%, MediaTek Inc 1.5%, Delta Electronics Inc 0.9%
Sector mix: Technology 31.8%, Financial services 20.2%, Consumer cyclical 9.9%, Basic materials 7.9%
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
Rolled up from the 5 largest holdings, 22.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +35.1% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 2308.TW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 3.3% of open interest (1,310,241 contracts)
Change on the week: -0.9% of open interest
Crowding: 37% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 1.42B | fund size: 84.70B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

## Sector and country funds

### Argentina (ARGT) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 90.12 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 94.56 (-4.7%), 50d 93.77 (-3.9%), 200d 92.70 (-2.8%); 50d above 200d
Momentum: RSI(14) 34.2 | MACD -0.585 vs signal 0.070 (histogram -0.655)
Returns: 1d -1.1% | 5d -3.5% | 1m -5.0% | 3m -0.7%
52-week range: 67.55 - 102.94 (now 63.8% of the way up)
Volatility: ATR(14) 1.83 (2.0% of price) | annualised 20d 16.5%
Volume: 0.18x the 20-day average
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
Three-year record: +31.0% a year | beta to the market 0.50
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.54 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +32.7% above the current prices
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
Share count change: 1 week: +3.1% (23.75M) over 7d
Shares outstanding: 8.82M | fund size: 794.52M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Top ETFs: Live Prices, Returns & Trends](https://www.tradingkey.com/markets/etf/top?page=138)  
  <sub>TradingKey, 9 hours ago</sub>  
  View the latest market data on top ETFs to watch, from price movements and trading volume to historical returns and performance trends.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 122.74 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 124.15 (-1.1%), 50d 122.30 (+0.4%), 200d 122.14 (+0.5%); 50d above 200d
Momentum: RSI(14) 47.6 | MACD 0.544 vs signal 0.605 (histogram -0.061)
Returns: 1d -1.7% | 5d -0.4% | 1m +1.1% | 3m +1.9%
52-week range: 94.16 - 137.69 (now 65.6% of the way up)
Volatility: ATR(14) 1.92 (1.6% of price) | annualised 20d 22.5%
Volume: 0.23x the 20-day average
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
Three-year record: +34.6% a year | beta to the market 1.07
Cost and size: expense ratio 0.59% | net assets 897.28M
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.19 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.9% above the current prices
Holdings read: TEVA, LUMI.TA, POLI.TA, TSEM.TA, ESLT.TA
Recent rating changes among them:
  - TEVA: 2026-09-23 Oppenheimer: init, ? -> Outperform
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

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 2.55M | fund size: 312.97M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 44.49 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 44.68 (-0.4%), 50d 43.61 (+2.0%), 200d 39.18 (+13.6%); 50d above 200d
Momentum: RSI(14) 50.6 | MACD 0.323 vs signal 0.453 (histogram -0.130)
Returns: 1d -0.2% | 5d +0.7% | 1m -0.1% | 3m +17.1%
52-week range: 31.57 - 45.76 (now 91.1% of the way up)
Volatility: ATR(14) 0.69 (1.5% of price) | annualised 20d 21.9%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

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
Rolled up from the 5 largest holdings, 47.4% of the fund by weight
Ratings by weight: buy 90.3% | hold 9.7% | sell 0.0% (mean 2.26 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -2.3% above the current prices
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

```text
Direction: money going out (1 week)
Share count change: 1 week: -1.6% (-13.75M) over 7d
Shares outstanding: 18.59M | fund size: 827.00M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 28.22 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 29.43 (-4.1%), 50d 29.47 (-4.2%), 200d 28.56 (-1.2%); 50d above 200d
Momentum: RSI(14) 36.6 | MACD -0.318 vs signal -0.166 (histogram -0.152)
Returns: 1d -0.5% | 5d -0.9% | 1m -6.1% | 3m +1.1%
52-week range: 24.95 - 30.43 (now 59.7% of the way up)
Volatility: ATR(14) 0.40 (1.4% of price) | annualised 20d 18.1%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 21.06 | P/B 2.81 | P/S 3.39 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +14.2% a year | beta to the market 0.96
Cost and size: expense ratio 0.50% | net assets 1.33B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: BHP Group Ltd 16.3%, Commonwealth Bank of Australia 13.0%, National Australia Bank Ltd 5.9%, Westpac Banking Corp 5.7%, ANZ Group Holdings Ltd 5.5%
Sector mix: Financial services 41.1%, Basic materials 26.7%, Consumer cyclical 6.5%, Healthcare 5.2%
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
Rolled up from the 5 largest holdings, 46.4% of the fund by weight
Ratings by weight: buy 0.0% | hold 59.6% | sell 40.4% (mean 3.48 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -5.2% above the current prices
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
Direction: flat (1 week)
Share count change: 1 week: -0.0% (-241.23K) over 7d
Shares outstanding: 45.89M | fund size: 1.29B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Canada (EWC) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 59.20 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 60.90 (-2.8%), 50d 60.70 (-2.5%), 200d 57.53 (+2.9%); 50d above 200d
Momentum: RSI(14) 36.8 | MACD -0.356 vs signal -0.131 (histogram -0.226)
Returns: 1d -0.8% | 5d -1.1% | 1m -4.7% | 3m +3.3%
52-week range: 49.72 - 62.64 (now 73.4% of the way up)
Volatility: ATR(14) 0.66 (1.1% of price) | annualised 20d 13.7%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 19.49 | P/B 2.83 | P/S 2.79 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +23.7% a year | beta to the market 0.79
Cost and size: expense ratio 0.50% | net assets 6.85B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Royal Bank of Canada 9.0%, The Toronto-Dominion Bank 6.3%, Shopify Inc Registered Shs -A- Subord Vtg 5.7%, Bank of Montreal 3.7%, Bank of Nova Scotia 3.6%
Sector mix: Financial services 39.2%, Energy 17.9%, Basic materials 16.1%, Industrials 8.8%
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

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.1% (3.64M) over 7d
Shares outstanding: 113.29M | fund size: 6.71B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Sweden (EWD) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Best Performing ETFs: Top Returns at a Glance](https://www.tradingkey.com/markets/etf/best-performing?page=47)  
  <sub>TradingKey, 7 hours ago</sub>  
  View TradingKey's list of the best performing ETFs, including price changes, trading volume, multi-period returns, and performance charts.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 50.64 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 52.27 (-3.1%), 50d 52.16 (-2.9%), 200d 51.32 (-1.3%); 50d above 200d
Momentum: RSI(14) 38.3 | MACD -0.417 vs signal -0.230 (histogram -0.187)
Returns: 1d -1.3% | 5d -0.8% | 1m -5.5% | 3m +3.7%
52-week range: 45.38 - 54.72 (now 56.3% of the way up)
Volatility: ATR(14) 0.70 (1.4% of price) | annualised 20d 15.0%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.99 | P/B 2.88 | P/S 2.90 | 3y earnings growth n/a
Yield: 3.4%
Three-year record: +21.0% a year | beta to the market 1.19
Cost and size: expense ratio 0.51% | net assets 755.74M
What it is made of: Stocks 98.9%, Cash 1.1%
Largest holdings: Spotify Technology SA 10.2%, Investor AB Class B 9.5%, Volvo AB Class B 7.1%, Atlas Copco AB Class A 6.9%, Sandvik AB 5.3%
Sector mix: Industrials 46.0%, Financial services 24.9%, Communication services 13.9%, Technology 6.2%
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
Rolled up from the 4 largest holdings, 29.5% of the fund by weight
Ratings by weight: buy 82.1% | hold 17.9% | sell 0.0% (mean 1.97 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.4% above the current prices
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

```text
Direction: money going out (1 week)
Share count change: 1 week: -0.6% (-4.45M) over 7d
Shares outstanding: 14.63M | fund size: 741.02M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 41.67 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 43.16 (-3.4%), 50d 43.01 (-3.1%), 200d 42.38 (-1.7%); 50d above 200d
Momentum: RSI(14) 34.6 | MACD -0.386 vs signal -0.193 (histogram -0.192)
Returns: 1d -0.5% | 5d -1.8% | 1m -5.6% | 3m +2.8%
52-week range: 38.08 - 44.59 (now 55.2% of the way up)
Volatility: ATR(14) 0.47 (1.1% of price) | annualised 20d 13.2%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

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
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.85 on a 1=strong buy to 5=strong sell scale)
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

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 79.50M | fund size: 3.31B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Best Performing ETFs: Top Returns at a Glance](https://www.tradingkey.com/markets/etf/best-performing?page=33)  
  <sub>TradingKey, 14 hours ago</sub>  
  View TradingKey's list of the best performing ETFs, including price changes, trading volume, multi-period returns, and performance charts.
- [Best SpaceX ETFs and Funds for UK Investors in 2026](https://www.moneymagpie.com/investment-articles/best-spacex-etfs)  
  <sub>MoneyMagpie, 24 hours ago</sub>  
  SpaceX is now listed and in the Nasdaq-100. Compare the best SpaceX ETFs and funds for UK investors, and how to buy them on eToro.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 59.66 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 61.31 (-2.7%), 50d 61.70 (-3.3%), 200d 57.80 (+3.2%); 50d above 200d
Momentum: RSI(14) 38.3 | MACD -0.496 vs signal -0.315 (histogram -0.180)
Returns: 1d -0.5% | 5d -1.5% | 1m -4.9% | 3m +1.4%
52-week range: 50.31 - 63.35 (now 71.7% of the way up)
Volatility: ATR(14) 0.76 (1.3% of price) | annualised 20d 17.6%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

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
Rolled up from the 5 largest holdings, 50.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.02 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.6% above the current prices
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

```text
Direction: money going out (1 week)
Share count change: 1 week: -0.7% (-7.65M) over 7d
Shares outstanding: 18.51M | fund size: 1.10B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Asian stocks mixed amid Wall Street drag; NSE debuts and Chinese stocks fall despite trade truce](https://seekingalpha.com/news/4646421-asian-stocks-mixed-amid-wall-street-drag-nse-debuts-and-chinese-stocks-fall-despite-trade-truce)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  Asian stock markets traded mixed on Thursday, following overnight losses on Wall Street as strong economic data, a weak Treasury auction, and energy-driven...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 95.42 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 96.86 (-1.5%), 50d 95.14 (+0.3%), 200d 89.90 (+6.1%); 50d above 200d
Momentum: RSI(14) 45.3 | MACD 0.413 vs signal 0.630 (histogram -0.217)
Returns: 1d -1.7% | 5d -1.6% | 1m +0.6% | 3m +3.0%
52-week range: 78.36 - 98.56 (now 84.5% of the way up)
Volatility: ATR(14) 1.37 (1.4% of price) | annualised 20d 16.0%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

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
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.9% above the current prices
Holdings read: 8306.T, 7203.T, 8316.T, 8035.T, 6857.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 4.3% of open interest (22,625 contracts)
Change on the week: +1.5% of open interest
Crowding: 38% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -1.3% (-282.91M) over 7d
Shares outstanding: 230.73M | fund size: 22.02B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 60.12 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 61.57 (-2.4%), 50d 62.67 (-4.1%), 200d 61.56 (-2.3%); 50d above 200d
Momentum: RSI(14) 36.7 | MACD -0.833 vs signal -0.741 (histogram -0.093)
Returns: 1d -0.4% | 5d +0.1% | 1m -6.4% | 3m -3.3%
52-week range: 53.86 - 65.08 (now 55.8% of the way up)
Volatility: ATR(14) 0.68 (1.1% of price) | annualised 20d 13.0%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 24.65 | P/B 4.25 | P/S 2.78 | 3y earnings growth n/a
Yield: 1.7%
Three-year record: +13.5% a year | beta to the market 0.91
Cost and size: expense ratio 0.50% | net assets 2.42B
What it is made of: Stocks 99.0%, Cash 1.0%
Largest holdings: Roche Holding AG Ordinary Shares new 13.6%, Novartis AG Registered Shares 12.4%, Nestle SA 11.1%, UBS Group AG Registered Shares 6.8%, Compagnie Financiere Richemont SA Class A 4.6%
Sector mix: Healthcare 37.5%, Financial services 20.6%, Consumer defensive 13.3%, Industrials 11.8%
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
Rolled up from the 5 largest holdings, 48.5% of the fund by weight
Ratings by weight: buy 74.5% | hold 25.5% | sell 0.0% (mean 2.40 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.8% above the current prices
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

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 28.62M | fund size: 1.72B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 67.03 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 67.77 (-1.1%), 50d 68.15 (-1.6%), 200d 64.00 (+4.7%); 50d above 200d
Momentum: RSI(14) 44.3 | MACD -0.449 vs signal -0.387 (histogram -0.062)
Returns: 1d -0.4% | 5d +1.2% | 1m -3.2% | 3m -0.9%
52-week range: 55.33 - 71.61 (now 71.9% of the way up)
Volatility: ATR(14) 0.87 (1.3% of price) | annualised 20d 14.5%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.97 | P/B 2.54 | P/S 1.84 | 3y earnings growth n/a
Yield: 4.1%
Three-year record: +25.0% a year | beta to the market 1.14
Cost and size: expense ratio 0.50% | net assets 626.66M
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ASML Holding NV 21.8%, ING Groep NV 9.0%, Prosus NV Ordinary Shares - Class N 5.1%, Nebius Group NV Shs Class-A- 4.3%, ASM International NV 4.0%
Sector mix: Technology 31.5%, Financial services 21.4%, Industrials 10.8%, Consumer defensive 10.7%
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
Rolled up from the 5 largest holdings, 44.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +31.1% above the current prices
Holdings read: ASML.AS, INGA.AS, PRX.AS, NBIS, ASM.AS
Recent rating changes among them:
  - NBIS: 2026-09-24 BNP Paribas: up, Neutral -> Outperform
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
Shares outstanding: 5.55M | fund size: 372.02M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Spain (EWP) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 60.35 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 61.67 (-2.1%), 50d 61.50 (-1.9%), 200d 57.35 (+5.2%); 50d above 200d
Momentum: RSI(14) 41.6 | MACD -0.313 vs signal -0.108 (histogram -0.205)
Returns: 1d +0.0% | 5d -0.8% | 1m -4.6% | 3m +3.4%
52-week range: 48.25 - 63.23 (now 80.8% of the way up)
Volatility: ATR(14) 0.80 (1.3% of price) | annualised 20d 16.2%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 16.28 | P/B 2.22 | P/S 1.82 | 3y earnings growth n/a
Yield: 2.7%
Three-year record: +34.6% a year | beta to the market 0.87
Cost and size: expense ratio 0.50% | net assets 2.26B
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Banco Santander SA 19.2%, Banco Bilbao Vizcaya Argentaria SA 14.0%, Iberdrola SA 12.1%, CaixaBank SA 4.6%, Industria De Diseno Textil SA Share From Split 4.4%
Sector mix: Financial services 45.4%, Utilities 20.0%, Industrials 14.4%, Technology 5.9%
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
Rolled up from the 5 largest holdings, 54.5% of the fund by weight
Ratings by weight: buy 52.0% | hold 48.0% | sell 0.0% (mean 2.19 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +2.7% above the current prices
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

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 37.35M | fund size: 2.25B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 112.53 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 110.04 (+2.3%), 50d 104.73 (+7.4%), 200d 87.03 (+29.3%); 50d above 200d
Momentum: RSI(14) 58.4 | MACD 1.981 vs signal 1.846 (histogram 0.135)
Returns: 1d +0.0% | 5d +3.8% | 1m +8.9% | 3m +7.5%
52-week range: 60.03 - 115.64 (now 94.4% of the way up)
Volatility: ATR(14) 2.33 (2.1% of price) | annualised 20d 28.1%
Volume: 0.37x the 20-day average
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
Three-year record: +46.4% a year | beta to the market 1.30
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
Share count change: 1 week: -6.4% (-782.55M) over 7d
Shares outstanding: 101.88M | fund size: 11.46B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 47.00 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 48.00 (-2.1%), 50d 47.99 (-2.1%), 200d 46.55 (+1.0%); 50d above 200d
Momentum: RSI(14) 38.8 | MACD -0.247 vs signal -0.109 (histogram -0.138)
Returns: 1d -0.2% | 5d -1.0% | 1m -4.3% | 3m +3.4%
52-week range: 41.04 - 49.39 (now 71.4% of the way up)
Volatility: ATR(14) 0.47 (1.0% of price) | annualised 20d 11.5%
Volume: 0.25x the 20-day average
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
Three-year record: +18.7% a year | beta to the market 0.68
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
Ratings by weight: buy 57.5% | hold 42.5% | sell 0.0% (mean 1.82 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.8% above the current prices
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
Direction: money coming in (1 week)
Share count change: 1 week: +0.7% (26.88M) over 7d
Shares outstanding: 79.51M | fund size: 3.74B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 72.32 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 75.30 (-4.0%), 50d 75.79 (-4.6%), 200d 75.71 (-4.5%); 50d above 200d
Momentum: RSI(14) 34.4 | MACD -0.858 vs signal -0.534 (histogram -0.324)
Returns: 1d -1.5% | 5d -0.8% | 1m -6.3% | 3m -2.0%
52-week range: 64.39 - 81.23 (now 47.1% of the way up)
Volatility: ATR(14) 1.25 (1.7% of price) | annualised 20d 15.0%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 12.68 | P/B 1.98 | P/S 1.49 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +11.4% a year | beta to the market 1.05
Cost and size: expense ratio 0.50% | net assets 1.82B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Grupo Mexico SAB de CV Class B 16.6%, Grupo Financiero Banorte SAB de CV Class O 11.1%, Fomento Economico Mexicano SAB de CV Units Cons. Of 1 Shs-B- And 4 Shs-D- 8.3%, America Movil SAB de CV Ordinary Shares - Class B 7.2%, Cemex SAB de CV 4.4%
Sector mix: Basic materials 27.3%, Consumer defensive 24.4%, Financial services 19.7%, Industrials 11.7%
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
Rolled up from the 5 largest holdings, 47.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.92 on a 1=strong buy to 5=strong sell scale)
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

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 18.90M | fund size: 1.37B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [5 ETF Areas That Have Nearly Doubled in First Nine Months of 2026](https://www.tradingview.com/news/zacks:a024337c6094b:0-5-etf-areas-that-have-nearly-doubled-in-first-nine-months-of-2026/)  
  <sub>TradingView, 4 hours ago</sub>  
  The year 2026 has been all about heightened geopolitical tensions due to the U.S.-Iran war and the AI boom, as well as risks associated with its investments...
- [US Stocks Slide as Tanker Hit Near Hormuz Rekindles Oil Supply Fears](https://finance.biggo.com/news/a889e221-2279-449a-abe8-510e0031157d)  
  <sub>BigGo Finance, 21 hours ago</sub>  
  US stocks opened lower on September 23 after a cargo ship was struck by an unidentified projectile near the Strait of Hormuz, reporting two casualties…

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 182.59 (bar of 2026-09-24), from 502 daily bars
Trend: vs 20d SMA 183.07 (-0.3%), 50d 174.40 (+4.7%), 200d 153.49 (+19.0%); 50d above 200d
Momentum: RSI(14) 51.0 | MACD 2.339 vs signal 2.343 (histogram -0.004)
Returns: 1d -1.7% | 5d +0.1% | 1m +1.4% | 3m -10.9%
52-week range: 78.87 - 219.20 (now 73.9% of the way up)
Volatility: ATR(14) 6.51 (3.6% of price) | annualised 20d 46.5%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.41 | P/B 1.83 | P/S 1.70 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +50.5% a year | beta to the market 2.50
Cost and size: expense ratio 0.59% | net assets 27.72B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: SK hynix Inc 23.7%, Samsung Electronics Co Ltd 22.2%, SK Square 2.9%, Samsung Electro-Mechanics Co Ltd 2.7%, KB Financial Group Inc 2.0%
Sector mix: Technology 54.6%, Industrials 17.0%, Financial services 11.1%, Consumer cyclical 5.1%
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

```text
Direction: money going out (1 week)
Share count change: 1 week: -5.9% (-1.68B) over 7d
Shares outstanding: 146.08M | fund size: 26.67B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 36.93 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 37.39 (-1.2%), 50d 36.14 (+2.2%), 200d 36.23 (+1.9%); 50d below 200d
Momentum: RSI(14) 49.7 | MACD 0.482 vs signal 0.618 (histogram -0.136)
Returns: 1d -1.2% | 5d -1.5% | 1m +5.0% | 3m +9.1%
52-week range: 28.79 - 41.73 (now 62.9% of the way up)
Volatility: ATR(14) 0.79 (2.2% of price) | annualised 20d 23.1%
Volume: 0.31x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.48 | P/B 1.79 | P/S 1.28 | 3y earnings growth n/a
Yield: 4.1%
Three-year record: +13.5% a year | beta to the market 0.84
Cost and size: expense ratio 0.59% | net assets 8.17B
What it is made of: Stocks 96.5%, Cash 2.7%, Preferred 0.8%
Largest holdings: Vale SA 10.1%, Nu Holdings Ltd Ordinary Shares Class A 9.5%, Itau Unibanco Holding SA Participating Preferred 7.7%, Petroleo Brasileiro SA Petrobras Participating Preferred 7.0%, Petroleo Brasileiro SA Petrobras 6.6%
Sector mix: Financial services 34.1%, Energy 17.4%, Basic materials 14.5%, Utilities 12.4%
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
Rolled up from the 5 largest holdings, 40.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.0% above the current prices
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

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 200.55M | fund size: 7.41B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 65.51 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 69.60 (-5.9%), 50d 67.42 (-2.8%), 200d 69.25 (-5.4%); 50d below 200d
Momentum: RSI(14) 36.5 | MACD -0.410 vs signal 0.244 (histogram -0.654)
Returns: 1d -1.4% | 5d -3.0% | 1m -8.2% | 3m +5.4%
52-week range: 60.43 - 81.60 (now 24.0% of the way up)
Volatility: ATR(14) 1.31 (2.0% of price) | annualised 20d 21.7%
Volume: 0.16x the 20-day average
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
Three-year record: +28.2% a year | beta to the market 1.02
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
Weighted price target: +27.1% above the current prices
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
Shares outstanding: 7.90M | fund size: 517.57M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [VanEck Gold Miners ETF (GDX) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GDX/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  VanEck Gold Miners ETF Overview VanEck / Equity Precious Metals · Raising target price to $57.00 · Agnico Eagle Earnings: Higher Gold Price Drives a Strong...
- [GDXJ 260925 155.00C (GDXJ260925C155000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/GDXJ260925C155000-US)  
  <sub>Moomoo, 21 hours ago</sub>  
  Track real-time GDXJ 260925 155.00C (GDXJ260925C155000) stock options chain data and pricing information and news on moomoo App for your options trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 91.32 (bar of 2026-09-24), from 502 daily bars
Trend: vs 20d SMA 96.78 (-5.6%), 50d 89.56 (+2.0%), 200d 90.93 (+0.4%); 50d below 200d
Momentum: RSI(14) 44.6 | MACD 0.445 vs signal 1.509 (histogram -1.064)
Returns: 1d -2.4% | 5d -4.8% | 1m -13.5% | 3m +20.7%
52-week range: 68.28 - 115.84 (now 48.4% of the way up)
Volatility: ATR(14) 3.42 (3.7% of price) | annualised 20d 42.2%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Equity Precious Metals
What it holds: P/E 12.84 | P/B 2.68 | P/S 4.10 | 3y earnings growth n/a
Yield: 0.6%
Three-year record: +52.0% a year | beta to the market 0.83
Cost and size: expense ratio 0.51% | net assets 30.54B
What it is made of: Stocks 100.0%
Largest holdings: Newmont Corp 10.7%, Agnico Eagle Mines Ltd 10.7%, Barrick Mining Corp 7.4%, Wheaton Precious Metals Corp 5.8%, Anglogold Ashanti PLC 5.3%
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
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.9% above the current prices
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

```text
Direction: flat (1 week)
Share count change: 1 week: -0.0% (-12.49M) over 7d
Shares outstanding: 323.14M | fund size: 29.51B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [iShares Expanded Tech-Software Sector ETF (IGV) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/IGV/)  
  <sub>Yahoo Finance Singapore, 17 hours ago</sub>  
  iShares Expanded Tech-Software Sector ETF (IGV) · 2.99% · 4.58% · 28.02% · 1.04% · -7.13% · 28.38% · 965.02%. Key events. Baseline. Advanced chart.
- [Daily ETF Flows: IGV & MAGS See Inflows](https://www.etf.com/sections/daily-etf-flows/daily-etf-flows-igv-mags-see-inflows)  
  <sub>ETF.com, 18 hours ago</sub>  
  Here are the daily ETF fund flows for September 22, 2026.
- [My Research](https://www.bespokepremium.com/interactive/posts/think-big-blog/softwares-recovery-is-still-loading)  
  <sub>Bespoke Investment Group, 20 hours ago</sub>  
  It's been just over a year since the iShares Software ETF (IGV) peaked on September 22, 2025, and getting back to that level has been a work in progress.
- [$IGV: Potential Cup-with-Handle Pattern for CBOE:IGV by Brent_Calver](https://www.tradingview.com/chart/IGV/MZJ2z7AR-IGV-Potential-Cup-with-Handle-Pattern/)  
  <sub>TradingView, 20 hours ago</sub>  
  Overview IGV is the Expanded Tech-Software Sector ETF. Software has lagged while AI chips, hardware, optics, and other AI-related stocks have surged.
- [Palo Alto Networks Surges 3%, What's Going On?](https://www.benzinga.com/markets/tech/26/09/61954696/palo-alto-networks-surges-3-whats-going-on)  
  <sub>Benzinga, 21 hours ago</sub>  
  Palo Alto Networks stock gains over 3% as the cybersecurity leader debuts its AI-powered Unit 42 security scanner and earns top analyst backing.
- [Software's Recovery Is Still Loading - TalkMarkets](https://t.co/UTcnn5RnwX)  
  <sub>Howl.link, 21 hours ago</sub>  
  The iShares Software ETF IGV sits 9.4% below its peak as sector recovery remains fragmented.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 107.44 (bar of 2026-09-24), from 502 daily bars
Trend: vs 20d SMA 105.74 (+1.6%), 50d 101.14 (+6.2%), 200d 93.68 (+14.7%); 50d above 200d
Momentum: RSI(14) 57.3 | MACD 1.431 vs signal 1.357 (histogram 0.074)
Returns: 1d -0.6% | 5d +1.6% | 1m +5.5% | 3m +26.8%
52-week range: 74.67 - 117.08 (now 77.3% of the way up)
Volatility: ATR(14) 2.61 (2.4% of price) | annualised 20d 42.7%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Technology
What it holds: P/E 34.20 | P/B 8.09 | P/S 9.07 | 3y earnings growth n/a
Yield: 0.0%
Three-year record: +16.2% a year | beta to the market 1.21
Cost and size: expense ratio 0.38% | net assets 15.74B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Palantir Technologies Inc Ordinary Shares - Class A 10.3%, Palo Alto Networks Inc 9.7%, Microsoft Corp 9.2%, CrowdStrike Holdings Inc Class A 7.4%, Salesforce Inc 6.6%
Sector mix: Technology 94.4%, Communication services 3.8%, Financial services 1.5%, Consumer cyclical 0.2%
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
Rolled up from the 5 largest holdings, 43.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +5.2% above the current prices
Holdings read: PLTR, PANW, MSFT, CRWD, CRM
Recent rating changes among them:
  - PLTR: 2026-09-23 Rosenblatt: main, Buy -> Buy
  - PANW: 2026-09-21 Morgan Stanley: main, Overweight -> Overweight
  - MSFT: 2026-09-23 Stifel: up, Hold -> Buy
  - CRWD: 2026-09-21 Morgan Stanley: main, Overweight -> Overweight
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

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 12.50M | fund size: 1.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Best Performing ETFs: Top Returns at a Glance](https://www.tradingkey.com/markets/etf/best-performing?page=3)  
  <sub>TradingKey, 22 hours ago</sub>  
  View TradingKey's list of the best performing ETFs, including price changes, trading volume, multi-period returns, and performance charts.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 47.53 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 48.80 (-2.6%), 50d 49.18 (-3.4%), 200d 50.07 (-5.1%); 50d below 200d
Momentum: RSI(14) 36.7 | MACD -0.458 vs signal -0.355 (histogram -0.102)
Returns: 1d -1.1% | 5d +0.1% | 1m -3.7% | 3m -4.2%
52-week range: 45.42 - 55.29 (now 21.3% of the way up)
Volatility: ATR(14) 0.46 (1.0% of price) | annualised 20d 13.4%
Volume: 0.25x the 20-day average
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
Three-year record: +3.0% a year | beta to the market 0.56
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
Direction: flat (1 week)
Share count change: 1 week: +0.2% (10.90M) over 7d
Shares outstanding: 139.11M | fund size: 6.61B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Xtr.-USD Corp.Bd Dur.SRI PAB R (FXYLD.DE) latest stock news and headlines – Yahoo Finance](https://sg.finance.yahoo.com/quote/FXYLD.DE/news/)  
  <sub>Yahoo Finance Singapore, 9 hours ago</sub>  
  Xtr.-USD Corp.Bd Dur.SRI PAB R (FXYLD.DE). 15.63 +0.02 (+0.15%). At close: 7:38:20 pm GMT+2. Related ETF news. Tech retreats as Treasury yields and oil...
- [UBS BBG EO Inf.Lnkd 10+ UETF N (FRC4.HM) latest stock news and headlines – Yahoo Finance](https://sg.finance.yahoo.com/quote/FRC4.HM/news/)  
  <sub>Yahoo Finance Singapore, 17 hours ago</sub>  
  UBS BBG EO Inf.Lnkd 10+ UETF N (FRC4.HM). 14.42 +0.04 (+0.25%). At close: 8:07:13 am GMT+2. Related ETF news. Tech retreats as Treasury yields and oil...
- [Top ETFs: Live Prices, Returns & Trends](https://www.tradingkey.com/markets/etf/top?page=9)  
  <sub>TradingKey, 21 hours ago</sub>  
  View the latest market data on top ETFs to watch, from price movements and trading volume to historical returns and performance trends.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 212.46 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 221.44 (-4.1%), 50d 233.95 (-9.2%), 200d 230.32 (-7.8%); 50d above 200d
Momentum: RSI(14) 28.0 | MACD -6.584 vs signal -6.347 (histogram -0.237)
Returns: 1d -0.7% | 5d -1.3% | 1m -9.0% | 3m -10.0%
52-week range: 198.23 - 253.22 (now 25.9% of the way up)
Volatility: ATR(14) 3.80 (1.8% of price) | annualised 20d 14.3%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

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
Rolled up from the 5 largest holdings, 57.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.75 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.4% above the current prices
Holdings read: GE, RTX, BA, GD, LMT
Recent rating changes among them:
  - GE: 2026-09-23 Jefferies: main, Buy -> Buy
  - RTX: 2026-09-23 Bernstein: main, Market Perform -> Market Perform
  - BA: 2026-09-21 Jefferies: main, Buy -> Buy
  - GD: 2026-09-23 Bernstein: main, Market Perform -> Market Perform
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

```text
Direction: flat (1 week)
Share count change: 1 week: +0.2% (31.90M) over 7d
Shares outstanding: 63.04M | fund size: 13.39B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Best Performing ETFs: Top Returns at a Glance](https://www.tradingkey.com/markets/etf/best-performing?page=16)  
  <sub>TradingKey, 20 hours ago</sub>  
  View TradingKey's list of the best performing ETFs, including price changes, trading volume, multi-period returns, and performance charts.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 79.12 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 82.62 (-4.2%), 50d 85.36 (-7.3%), 200d 81.14 (-2.5%); 50d above 200d
Momentum: RSI(14) 27.5 | MACD -1.711 vs signal -1.436 (histogram -0.276)
Returns: 1d -0.8% | 5d -1.3% | 1m -8.9% | 3m -7.2%
52-week range: 68.14 - 90.01 (now 50.2% of the way up)
Volatility: ATR(14) 1.22 (1.5% of price) | annualised 20d 15.3%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Industrials
What it holds: P/E 20.28 | P/B 4.25 | P/S 1.45 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +12.4% a year | beta to the market 1.28
Cost and size: expense ratio 0.37% | net assets 2.20B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Union Pacific Corp 17.8%, Uber Technologies Inc 15.4%, CSX Corp 9.4%, United Parcel Service Inc Class B 5.6%, Norfolk Southern Corp 4.9%
Sector mix: Industrials 83.8%, Technology 16.2%
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
Rolled up from the 5 largest holdings, 53.1% of the fund by weight
Ratings by weight: buy 90.8% | hold 9.2% | sell 0.0% (mean 1.84 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.3% above the current prices
Holdings read: UNP, UBER, CSX, UPS, NSC
Recent rating changes among them:
  - UNP: 2026-09-16 UBS: up, Neutral -> Buy
  - UBER: 2026-09-09 Scotiabank: init, ? -> Sector Outperform
  - CSX: 2026-09-18 B of A Securities: main, Buy -> Buy
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

```text
Direction: money coming in (1 week)
Share count change: 1 week: +3.5% (73.19M) over 7d
Shares outstanding: 27.61M | fund size: 2.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Bulls Can’t Go Wrong With This Sector for Q4](https://www.schaeffersresearch.com/content/bgs/2026/09/23/bulls-can-t-go-wrong-with-this-sector-for-q4)  
  <sub>Schaeffer's Investment Research, 23 hours ago</sub>  
  Wall Street gears up to enter the fourth and final quarter of 2026, but many stocks are at a crossroads.
- [Form 4 iShares Russell 2000 ETF For: 23 September By Investing.com](https://ca.investing.com/news/stock-market-news/form-4-ishares-russell-2000-etf-for-23-september-93CH-4850293)  
  <sub>Investing.com Canada, 23 hours ago</sub>  
  This pricing supplement, which is not complete and may be changed, relates to an effective Registration Statement under the Securities Act of 1933.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 70.21 (bar of 2026-09-24), from 502 daily bars
Trend: vs 20d SMA 73.24 (-4.1%), 50d 75.03 (-6.4%), 200d 70.47 (-0.4%); 50d above 200d
Momentum: RSI(14) 26.6 | MACD -1.112 vs signal -0.772 (histogram -0.340)
Returns: 1d -0.2% | 5d -3.5% | 1m -5.5% | 3m -6.1%
52-week range: 58.14 - 77.93 (now 61.0% of the way up)
Volatility: ATR(14) 1.18 (1.7% of price) | annualised 20d 15.0%
Volume: 0.38x the 20-day average
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
Three-year record: +23.3% a year | beta to the market 1.04
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
Weighted price target: +22.5% above the current prices
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
Share count change: 1 week: +3.0% (113.17M) over 7d
Shares outstanding: 55.73M | fund size: 3.91B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 36.87 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 38.13 (-3.3%), 50d 37.79 (-2.4%), 200d 38.14 (-3.3%); 50d below 200d
Momentum: RSI(14) 29.4 | MACD -0.286 vs signal -0.111 (histogram -0.175)
Returns: 1d -0.9% | 5d -1.0% | 1m -5.5% | 3m -3.2%
52-week range: 35.83 - 41.03 (now 20.0% of the way up)
Volatility: ATR(14) 0.30 (0.8% of price) | annualised 20d 8.0%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.00 | P/B 1.81 | P/S 3.04 | 3y earnings growth n/a
Yield: 2.7%
Three-year record: +1.8% a year | beta to the market 0.18
Cost and size: expense ratio 0.75% | net assets 638.50M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Al Rajhi Bank 14.1%, Saudi Arabian Oil Co 11.1%, Saudi National Bank 8.8%, Saudi Telecom Co 6.0%, Saudi Arabian Mining Co 4.4%
Sector mix: Financial services 41.9%, Basic materials 12.7%, Energy 12.1%, Communication services 8.8%
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
Rolled up from the 5 largest holdings, 44.4% of the fund by weight
Ratings by weight: buy 90.0% | hold 10.0% | sell 0.0% (mean 2.08 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.0% above the current prices
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
Direction: money coming in (1 week)
Share count change: 1 week: +1.9% (11.61M) over 7d
Shares outstanding: 17.17M | fund size: 632.90M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Sell on the Pop Prospects: September 22 Edition](https://etfdb.com/news/2026/09/23/sell-on-the-pop-prospects-sep-22-edit/)  
  <sub>ETF Database, 18 hours ago</sub>  
  Here is a look at ETFs that currently offer attractive short selling opportunities. The ETFs included in this list are rated as sell candidates for two...
- [KraneShares CSI China Internet ETF (KWEB) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/KWEB/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest KraneShares CSI China Internet ETF (KWEB) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 52.72 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 53.77 (-2.0%), 50d 54.47 (-3.2%), 200d 57.13 (-7.7%); 50d below 200d
Momentum: RSI(14) 41.1 | MACD -0.483 vs signal -0.436 (histogram -0.048)
Returns: 1d -0.9% | 5d +0.8% | 1m -4.0% | 3m +2.5%
52-week range: 50.48 - 66.99 (now 13.5% of the way up)
Volatility: ATR(14) 0.62 (1.2% of price) | annualised 20d 15.0%
Volume: 0.81x the 20-day average
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
Three-year record: +10.0% a year | beta to the market 0.44
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +52.3% above the current prices
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
Direction: money going out (1 week)
Share count change: 1 week: -1.3% (-81.59M) over 7d
Shares outstanding: 116.80M | fund size: 6.16B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [This Unstoppable ETF Is Down 12% From Its High -- and History Says Now Is a Smart Time to Invest](https://finance.yahoo.com/markets/stocks/articles/unstoppable-etf-down-12-high-155000262.html)  
  <sub>Yahoo Finance, 24 hours ago</sub>  
  You would have a hard time finding an exchange traded fund (ETF) that has performed better than the VanEck Semiconductor ETF (NASDAQ: SMH) over the years.
- [S&P 500, Dow, Nasdaq Drop As Yields Spike Amid Calls For More Rate Hikes — AMZN, GOOGL, NFLX, SPCX, RKLB In Focus](https://es.tradingview.com/news/stocktwits:5983a7ca0094b:0-s-p-500-dow-nasdaq-drop-as-yields-spike-amid-calls-for-more-rate-hikes-amzn-googl-nflx-spcx-rklb-in-focus/)  
  <sub>TradingView, 18 hours ago</sub>  
  U.S. stock indices ended lower on Wednesday as Treasury yields jumped following hawkish remarks from Federal Reserve officials, while latest purchasing...
- [AMD Is Up 187% This Year: Take Profits, or Buy More?](https://247wallst.com/investing/2026/09/23/amd-is-up-187-this-year-take-profits-or-buy-more/?tpid=1666446&tv=link&tc=in_content)  
  <sub>24/7 Wall St., 20 hours ago</sub>  
  Advanced Micro Devices (NASDAQ:AMD | AMD Price Prediction) has been one of the year's most striking stock stories, with a run that has left the...
- [S&P 500, Nasdaq End Week Higher Following Strong SK Hynix Debut — META, SKHVY, CRCL, BA, DAL In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-nasdaq-end-week-higher-following-strong-sk-hynix-debut-meta-skhvy-crcl-ba-dal-in-focus/cZmr12VR78N)  
  <sub>Stocktwits, 8 hours ago</sub>  
  U.S. stock indices ended higher on Friday following a strong debut from South Korean memory chip maker SK Hynix as investors prepare for the earnings...
- [Best Nvidia ETFs for UK Investors in 2026](https://www.moneymagpie.com/investment-articles/best-nvidia-etfs-for-uk-investors-in-2026)  
  <sub>MoneyMagpie, 24 hours ago</sub>  
  Nvidia beat analysts' forecasts again when it reported on 26 August 2026, and guided to around $108 billion of revenue for the following quarter.
- [S&P 500, Dow End Lower As Oil Prices Rise Amid US-Iran Crisis — PSKY, GOOGL, IREN, AMD, NVDA, AVGO In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-dow-end-lower-as-oil-prices-rise-amid-us-iran-crisis/cZZiiqPR7H7)  
  <sub>Stocktwits, 8 hours ago</sub>  
  The S&P 500 and Dow ended lower on Monday over worries about soaring oil prices, while chipmaker stocks staged a comeback.
- [S&P 500, Dow End Lower As Middle East Tensions Spur Oil Rally Ahead Of Key Inflation Data — META, QCOM, BE, AMZN, AVGO In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-dow-end-lower-as-middle-east-tensions-spur-oil-rally/cZtEOUNRJyE)  
  <sub>Stocktwits, 15 hours ago</sub>  
  The U.S. struck targets near Kharg Island and the port city of Jask, Fox News reported.
- [S&P 500, Nasdaq, Dow Drop As US-Iran War Jitters, Inflation Risk Spur Tech Selloffs — SMCI, AMZN, OPEN, SEGG, TSLA In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-nasdaq-dow-drop-as-us-iran-war-jitters-inflation-risk-spur-tech-selloffs-smci-amzn-open-segg-tsla-in-focus/cZ06yd5R7cQ)  
  <sub>Stocktwits, 9 hours ago</sub>  
  U.S. stock indices dropped on Wednesday as renewed energy cost concerns tied to rising US-Iran war signals, along with signs of persistent inflation...
- [S&P 500, Nasdaq, Dow End Higher Led By Chipmaker Stocks As Investors Look Past US-Iran Hostility — ORCL, SBUX, WULF, PANW, FATE In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-nasdaq-dow-end-higher-led-by-chipmaker-stocks-as-investors-look-past-us-iran-hostility/cZmY9vSR7nz)  
  <sub>Stocktwits, 21 hours ago</sub>  
  U.S. stock indices ended higher on Thursday as chipmaker stocks rebounded sharply ahead of SK Hynix's highly anticipated Nasdaq debut on July 10,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 591.33 (bar of 2026-09-24), from 502 daily bars
Trend: vs 20d SMA 566.69 (+4.3%), 50d 564.95 (+4.7%), 200d 492.05 (+20.2%); 50d above 200d
Momentum: RSI(14) 57.2 | MACD 6.884 vs signal 1.474 (histogram 5.410)
Returns: 1d -1.7% | 5d +5.5% | 1m +6.4% | 3m -7.2%
52-week range: 321.06 - 668.91 (now 77.7% of the way up)
Volatility: ATR(14) 16.58 (2.8% of price) | annualised 20d 36.5%
Volume: 0.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Technology
What it holds: P/E 37.78 | P/B 11.07 | P/S 13.20 | 3y earnings growth n/a
Yield: 0.2%
Three-year record: +63.1% a year | beta to the market 2.06
Cost and size: expense ratio 0.35% | net assets 67.79B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: NVIDIA Corp 22.6%, Taiwan Semiconductor Manufacturing Co Ltd ADR 9.7%, Broadcom Inc 6.1%, Micron Technology Inc 5.5%, Advanced Micro Devices Inc 5.4%
Sector mix: Technology 100.0%
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
Rolled up from the 5 largest holdings, 49.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +38.4% above the current prices
Holdings read: NVDA, TSM, AVGO, MU, AMD
Recent rating changes among them:
  - NVDA: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - TSM: 2026-09-02 Stifel: init, ? -> Buy
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-09-24 Rosenblatt: main, Buy -> Buy
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

```text
Direction: money going out (1 week)
Share count change: 1 week: -9.3% (-6.89B) over 7d
Shares outstanding: 113.71M | fund size: 67.24B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [(TUR) Volatility Zones as Tactical Triggers](https://news.stocktradersdaily.com/news_release/98/TUR_Volatility_Zones_as_Tactical_Triggers_092426020803_1790230083.html)  
  <sub>Stock Traders Daily, 13 hours ago</sub>  
  Price-action only: Ishares Msci Turkey Etf (TUR) movements set the tone for institutional models. (TUR) Volatility Zones as Tactical Triggers.
- [Best Performing ETFs: Top Returns at a Glance](https://www.tradingkey.com/markets/etf/best-performing?page=39)  
  <sub>TradingKey, 11 hours ago</sub>  
  View TradingKey's list of the best performing ETFs, including price changes, trading volume, multi-period returns, and performance charts.
- [United States Oil Fund, LP (USO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/USO/)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Find the latest United States Oil Fund, LP (USO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [ProShares UltraPro QQQ (TQQQ) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TQQQ/)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  Find the latest ProShares UltraPro QQQ (TQQQ) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 36.37 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 39.15 (-7.1%), 50d 39.18 (-7.2%), 200d 39.30 (-7.4%); 50d below 200d
Momentum: RSI(14) 35.2 | MACD -0.685 vs signal -0.328 (histogram -0.357)
Returns: 1d -3.0% | 5d +0.5% | 1m -10.1% | 3m -8.1%
52-week range: 31.90 - 43.74 (now 37.8% of the way up)
Volatility: ATR(14) 0.79 (2.2% of price) | annualised 20d 35.9%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.81 | P/B 1.21 | P/S 0.66 | 3y earnings growth n/a
Yield: 2.1%
Three-year record: +1.9% a year | beta to the market 0.44
Cost and size: expense ratio 0.59% | net assets 225.08M
What it is made of: Stocks 100.4%, Cash -0.4%
Largest holdings: Aselsan Elektronik Sanayi Ve Ticaret AS 11.2%, Tupras-Turkiye Petrol Rafineleri AS 9.7%, Bim Birlesik Magazalar AS 8.7%, Akbank TAS 5.6%, Turk Hava Yollari AO 4.4%
Sector mix: Industrials 31.2%, Financial services 14.7%, Consumer defensive 11.9%, Basic materials 11.1%
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
Rolled up from the 5 largest holdings, 39.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.0% above the current prices
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

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 15.65M | fund size: 569.19M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Vanguard Real Estate ETF vs State Street SPDR: Diversification or Cost](https://www.fool.com/coverage/etfs/2026/09/23/vanguard-real-estate-etf-vs-state-street-spdr-diversification-or-cost/)  
  <sub>The Motley Fool, 11 hours ago</sub>  
  Comparing the Vanguard Real Estate ETF (VNQ -1.47%) and the State Street Real Estate Select Sector SPDR ETF (XLRE -1.55%) highlights a choice between the...
- [VNQ Mar 2027 88.000 put (VNQ270319P00088000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/VNQ270319P00088000/chart/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Interactive Chart for VNQ Mar 2027 88.000 put (VNQ270319P00088000), analyze all the data with a huge range of indicators.
- [New bill seeks to give first-time homebuyers up to $50K](https://seekingalpha.com/news/4646432-homeownership-promise-act-first-time-homebuyers)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  First-time homebuyers could get up to $50,000 from the federal government for a down payment on a house under a new bill introduced by Sen.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 91.32 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 94.99 (-3.9%), 50d 97.34 (-6.2%), 200d 94.33 (-3.2%); 50d above 200d
Momentum: RSI(14) 28.4 | MACD -1.487 vs signal -1.168 (histogram -0.319)
Returns: 1d -0.1% | 5d -2.3% | 1m -7.8% | 3m -5.9%
52-week range: 87.00 - 100.95 (now 31.0% of the way up)
Volatility: ATR(14) 1.18 (1.3% of price) | annualised 20d 12.5%
Volume: 0.45x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Real Estate
What it holds: P/E 30.19 | P/B 2.59 | P/S 4.94 | 3y earnings growth n/a
Yield: 3.6%
Three-year record: +10.8% a year | beta to the market 0.98
Cost and size: expense ratio 0.13% | net assets 70.82B
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.70 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.7% above the current prices
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

```text
Direction: money coming in (1 week)
Share count change: 1 week: +0.5% (343.64M) over 7d
Shares outstanding: 754.88M | fund size: 68.94B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 153.69 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 160.03 (-4.0%), 50d 157.51 (-2.4%), 200d 137.63 (+11.7%); 50d above 200d
Momentum: RSI(14) 41.3 | MACD -1.160 vs signal -0.285 (histogram -0.875)
Returns: 1d -1.0% | 5d -0.3% | 1m -6.4% | 3m +2.7%
52-week range: 95.86 - 169.55 (now 78.5% of the way up)
Volatility: ATR(14) 4.12 (2.7% of price) | annualised 20d 21.9%
Volume: 0.42x the 20-day average
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
Three-year record: +30.7% a year | beta to the market 1.12
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
Ratings by weight: buy 52.0% | hold 48.0% | sell 0.0% (mean 2.18 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -17.4% above the current prices
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
Direction: flat (1 week)
Share count change: 1 week: -0.4% (-44.36M) over 7d
Shares outstanding: 72.08M | fund size: 11.08B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### US house builders (XHB) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Homebuilders Warn Affordability Headwinds Are Hitting the Housing Market. Berkshire Is Doubling Down on the Sector](https://www.investopedia.com/homebuilders-warn-affordability-headwinds-are-hitting-the-housing-market-berkshire-is-doubling-down-on-the-sector-brk-12137256)  
  <sub>Investopedia, 18 hours ago</sub>  
  Some of America's largest homebuilders are warning about headwinds to the U.S. housing market. That's not stopping Berkshire Hathaway from boosting its bets...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 96.29 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 99.86 (-3.6%), 50d 104.60 (-7.9%), 200d 106.50 (-9.6%); 50d below 200d
Momentum: RSI(14) 33.5 | MACD -2.549 vs signal -2.441 (histogram -0.108)
Returns: 1d -0.8% | 5d -0.5% | 1m -9.4% | 3m -15.7%
52-week range: 94.86 - 121.36 (now 5.4% of the way up)
Volatility: ATR(14) 2.08 (2.2% of price) | annualised 20d 18.7%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 19.52 | P/B 2.34 | P/S 1.36 | 3y earnings growth n/a
Yield: 0.8%
Three-year record: +10.2% a year | beta to the market 1.46
Cost and size: expense ratio 0.35% | net assets 1.33B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Installed Building Products Inc 4.4%, Owens-Corning Inc 4.3%, Allegion PLC 4.3%, Champion Homes Inc 4.1%, Williams-Sonoma Inc 3.9%
Sector mix: Consumer cyclical 60.7%, Industrials 37.9%, Real estate 1.5%
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
Rolled up from the 5 largest holdings, 20.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 78.9% | hold 21.1% | sell 0.0% (mean 2.15 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.8% above the current prices
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

```text
Direction: money coming in (1 week)
Share count change: 1 week: +1.3% (17.05M) over 7d
Shares outstanding: 13.74M | fund size: 1.32B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 49.75 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 51.50 (-3.4%), 50d 51.72 (-3.8%), 200d 50.48 (-1.4%); 50d above 200d
Momentum: RSI(14) 36.5 | MACD -0.637 vs signal -0.429 (histogram -0.208)
Returns: 1d -1.1% | 5d -1.2% | 1m -7.1% | 3m -2.8%
52-week range: 42.23 - 53.67 (now 65.7% of the way up)
Volatility: ATR(14) 0.76 (1.5% of price) | annualised 20d 13.7%
Volume: 0.49x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Natural Resources
What it holds: P/E 24.59 | P/B 3.00 | P/S 2.01 | 3y earnings growth n/a
Yield: 1.6%
Three-year record: +10.9% a year | beta to the market 0.82
Cost and size: expense ratio 0.08% | net assets 8.75B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Linde PLC 13.1%, Newmont Corp 7.8%, Freeport-McMoRan Inc 6.3%, Corteva Inc 4.9%, Air Products and Chemicals Inc 4.8%
Sector mix: Basic materials 84.5%, Consumer cyclical 15.5%
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
Rolled up from the 5 largest holdings, 37.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.70 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.3% above the current prices
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

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 71.92M | fund size: 3.58B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### US media and communication (XLC) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Meta Maps Out Muse Monetization Strategy: Tap With ETFs or Stock?](https://www.tradingview.com/news/zacks:990adb934094b:0-meta-maps-out-muse-monetization-strategy-tap-with-etfs-or-stock/)  
  <sub>TradingView, 4 hours ago</sub>  
  Meta META CEO Mark Zuckerberg outlined the company's plans to monetize its rapidly growing Muse AI agent during the Meta Connect conference on Sept.
- [Best Performing ETFs: Top Returns at a Glance](https://www.tradingkey.com/markets/etf/best-performing?page=145)  
  <sub>TradingKey, 10 hours ago</sub>  
  View TradingKey's list of the best performing ETFs, including price changes, trading volume, multi-period returns, and performance charts.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 113.31 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 112.48 (+0.7%), 50d 111.31 (+1.8%), 200d 113.97 (-0.6%); 50d below 200d
Momentum: RSI(14) 53.0 | MACD 0.479 vs signal 0.470 (histogram 0.009)
Returns: 1d +0.7% | 5d +0.3% | 1m +0.9% | 3m +6.4%
52-week range: 105.38 - 120.08 (now 53.9% of the way up)
Volatility: ATR(14) 1.89 (1.7% of price) | annualised 20d 22.1%
Volume: 0.44x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Communications
What it holds: P/E 15.38 | P/B 2.92 | P/S 2.06 | 3y earnings growth n/a
Yield: 1.3%
Three-year record: +21.4% a year | beta to the market 0.85
Cost and size: expense ratio 0.08% | net assets 22.43B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Meta Platforms Inc Class A 16.8%, Alphabet Inc Class A 10.3%, Alphabet Inc Class C 8.2%, AT&T Inc 5.3%, Verizon Communications Inc 5.0%
Sector mix: Communication services 100.0%
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
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.54 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.4% above the current prices
Holdings read: META, GOOGL, GOOG, T, VZ
Recent rating changes among them:
  - META: 2024-09-30 Cantor Fitzgerald: reit, Overweight -> Overweight
  - GOOGL: 2026-09-18 Tigress Financial: main, Strong Buy -> Strong Buy
  - GOOG: 2026-07-23 JP Morgan: main, Overweight -> Overweight
  - T: 2026-09-21 BNP Paribas: up, Neutral -> Outperform
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

```text
Direction: flat (1 week)
Share count change: 1 week: +0.3% (55.60M) over 7d
Shares outstanding: 195.50M | fund size: 22.15B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Energy ETF chart flashes bullish signal from put-call ratio (XLE:NYSEARCA)](https://seekingalpha.com/news/4646465-energy-etf-chart-flashes-bullish-signal-from-put-call-ratio)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  XLE outlook: i3 Invest's put-call ratio chart shows past contrarian buy spikes often preceded strong energy ETF rallies.
- [Leading And Lagging Sectors For September 24, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61970129/leading-and-lagging-sectors-september-24-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLE) State Street Energy Select Sector SPDR ETF 63.0000 0.630 1.01 320.6K (NYSE:XLP) State...
- [State Street Energy Select Sector SPDR ETF Price Today | xXLE Live Price, Chart & Market Cap](https://www.okx.com/en-eu/price/state-street-energy-select-sector-spdr-etf-xxle)  
  <sub>OKX, 8 hours ago</sub>  
  The State Street Energy Select Sector SPDR ETF (XLE) seeks to provide investment results that correspond generally to the price and yield performance of the...
- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance Singapore, 19 hours ago</sub>  
  Find the latest State Street Health Care Select Sector SPDR ETF (XLV) stock quote, history, news and other vital information to help you with your stock...
- [Five energy stocks with long-running Sell Quant ratings (XLE:NYSEARCA)](https://seekingalpha.com/news/4646552-five-energy-stocks-with-long-running-sell-quant-ratings)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Energy stocks update: 5 names with 60+ days of Sell/Strong Sell Quant Ratings (GEL, VTOL, CLB, SOC, BTU).
- [Best Performing ETFs: Top Returns at a Glance](https://www.tradingkey.com/markets/etf/best-performing?page=145)  
  <sub>TradingKey, 10 hours ago</sub>  
  View TradingKey's list of the best performing ETFs, including price changes, trading volume, multi-period returns, and performance charts.
- [SLB Expands Oman Footprint with Bisat-B Facility Project - SLB (NYSE:SLB)](https://www.benzinga.com/markets/large-cap/26/09/61951012/slb-expands-oman-footprint-with-bisat-b-facility-project)  
  <sub>Benzinga, 23 hours ago</sub>  
  SLB's Oman contract covers a 19-month Bisat-B expansion and four years of maintenance support as OQEP adds production capacity.
- [Trader James Caldwell Claims to Liquidate Semiconductor Holdings for $7 Million, Retires at 56 Achieving Financial Freedom](https://www.ababnews.com/news/a019cd41-dd69-45e9-924f-6a5a641ddfd8)  
  <sub>https://www.ababnews.com/, 14 hours ago</sub>  
  James Caldwell posted that he has retired at 56, achieving financial freedom, and has sold all positions in Micron, Arm, and AMD, cashing out $7 million.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 63.21 (bar of 2026-09-24), from 502 daily bars
Trend: vs 20d SMA 64.04 (-1.3%), 50d 61.67 (+2.5%), 200d 56.06 (+12.8%); 50d above 200d
Momentum: RSI(14) 50.4 | MACD 0.329 vs signal 0.787 (histogram -0.459)
Returns: 1d +1.3% | 5d -2.0% | 1m +1.9% | 3m +16.9%
52-week range: 42.61 - 65.93 (now 88.3% of the way up)
Volatility: ATR(14) 1.29 (2.0% of price) | annualised 20d 22.1%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Equity Energy
What it holds: P/E 17.74 | P/B 2.58 | P/S 1.68 | 3y earnings growth n/a
Yield: 2.4%
Three-year record: +15.0% a year | beta to the market -0.07
Cost and size: expense ratio 0.08% | net assets 41.44B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ExxonMobil Holdings Corp 19.9%, Chevron Corp 14.9%, ConocoPhillips 6.2%, Marathon Petroleum Corp 5.4%, Phillips 66 5.3%
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
US inventories, week ending 2026-09-18 (published the following Wednesday)
  Crude oil: 426.4 million barrels, +3.0 on the week (a build), 58% percentile over 52 weeks
  Petrol: 206.0 million barrels, -1.7 on the week (a draw), 8% percentile over 52 weeks -- low for the time of year
  Diesel: 107.4 million barrels, -0.4 on the week (a draw), 33% percentile over 52 weeks
  Natural gas: 3,298.0 billion cubic feet, +44.0 on the week (a build), 71% percentile over 52 weeks
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
Rolled up from the 5 largest holdings, 51.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.4% above the current prices
Holdings read: XOM, CVX, COP, MPC, PSX
Recent rating changes among them:
  - XOM: 2026-09-03 Piper Sandler: main, Neutral -> Neutral
  - CVX: 2026-09-03 BMO Capital: main, Outperform -> Outperform
  - COP: 2026-09-14 UBS: main, Buy -> Buy
  - MPC: 2026-09-22 Jefferies: down, Buy -> Hold
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

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 186.42M | fund size: 11.78B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Interest Rates Are Rising. Here's the ETF I'd Buy to Profit From It.](https://finance.yahoo.com/markets/stocks/articles/interest-rates-rising-heres-etf-084800912.html)  
  <sub>Yahoo Finance, 7 hours ago</sub>  
  There's a misconception that rising interest rates are a negative for U.S. stocks. In reality, it's a little more complicated than that.
- [Xtr.-USD Corp.Bd Dur.SRI PAB R (FXYLD.DE) latest stock news and headlines – Yahoo Finance](https://sg.finance.yahoo.com/quote/FXYLD.DE/news/)  
  <sub>Yahoo Finance Singapore, 9 hours ago</sub>  
  Xtr.-USD Corp.Bd Dur.SRI PAB R (FXYLD.DE). 15.63 +0.02 (+0.15%). At close: 7:38:20 pm GMT+2. Related ETF news. Tech retreats as Treasury yields and oil...
- [Bulls Can’t Go Wrong With This Sector for Q4](https://www.schaeffersresearch.com/content/bgs/2026/09/23/bulls-can-t-go-wrong-with-this-sector-for-q4)  
  <sub>Schaeffer's Investment Research, 23 hours ago</sub>  
  Wall Street gears up to enter the fourth and final quarter of 2026, but many stocks are at a crossroads.
- [Best Performing ETFs: Top Returns at a Glance](https://www.tradingkey.com/markets/etf/best-performing?page=145)  
  <sub>TradingKey, 10 hours ago</sub>  
  View TradingKey's list of the best performing ETFs, including price changes, trading volume, multi-period returns, and performance charts.
- [UBS BBG EO Inf.Lnkd 10+ UETF N (FRC4.HM) latest stock news and headlines – Yahoo Finance](https://sg.finance.yahoo.com/quote/FRC4.HM/news/)  
  <sub>Yahoo Finance Singapore, 17 hours ago</sub>  
  UBS BBG EO Inf.Lnkd 10+ UETF N (FRC4.HM). 14.42 +0.04 (+0.25%). At close: 8:07:13 am GMT+2. Related ETF news. Tech retreats as Treasury yields and oil...
- [Sector Update: Financial](https://www.bitget.com/amp/news/detail/12560605864723)  
  <sub>Bitget, 18 hours ago</sub>  
  03:31 PM EDT, 09/23/2026 (MT Newswires) -- Financial stocks declined in late Wednesday afternoon trading with the NYSE Financial Index falling 0.8% and the...
- [Sector Update: Financial Stocks Edge Higher Pre-Bell Thursday](https://finance.yahoo.com/markets/stocks/articles/sector-financial-stocks-edge-higher-132243262.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Financial stocks were edging higher pre-bell Thursday, with the State Street Financial Select Sector SPDR ETF (XLF) advancing by 0.2%.
- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Thursday Amid Ongoing Middle East Tensions Before US-China Talks](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131757956.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.4%, and the actively t.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 54.32 (bar of 2026-09-24), from 502 daily bars
Trend: vs 20d SMA 56.74 (-4.3%), 50d 57.08 (-4.8%), 200d 53.72 (+1.1%); 50d above 200d
Momentum: RSI(14) 27.2 | MACD -0.673 vs signal -0.335 (histogram -0.337)
Returns: 1d -0.4% | 5d -2.8% | 1m -6.8% | 3m +1.6%
52-week range: 47.81 - 58.56 (now 60.6% of the way up)
Volatility: ATR(14) 0.73 (1.3% of price) | annualised 20d 13.1%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

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
Rolled up from the 5 largest holdings, 41.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.78 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.5% above the current prices
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

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 883.44M | fund size: 47.99B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Thursday Amid Ongoing Middle East Tensions Before US-China Talks](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131757956.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.4%, and the actively t.
- [State Street Technology Select Sector SPDR ETF (XLK) Stock Price Today: $193.06](https://pluang.com/en/asset/usstock/XLK/10985)  
  <sub>Pluang, 5 hours ago</sub>  
  About State Street Technology Select Sector SPDR ETF ... XLK tracks the Technology Select Sector Index, providing targeted exposure to the largest and most...
- [These are the industrials stocks with persistent Sell or Strong Sell Quant ratings (XLI:NYSEARCA)](https://seekingalpha.com/news/4646654-these-are-the-industrials-stocks-with-persistent-sell-or-strong-sell-quant-ratings)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  S&P 500 industrials slip as rates and oil rise. See 9 stocks with 60+ days of Sell/Strong Sell Quant Ratings and key sector trends—read now.
- [Best Performing ETFs: Top Returns at a Glance](https://www.tradingkey.com/markets/etf/best-performing?page=146)  
  <sub>TradingKey, 10 hours ago</sub>  
  View TradingKey's list of the best performing ETFs, including price changes, trading volume, multi-period returns, and performance charts.
- [The Anti-AI ETF? Wedbush Wants to Own What AI Can’t Replace](https://www.tradingview.com/news/benzinga:179c6fa5b094b:0-the-anti-ai-etf-wedbush-wants-to-own-what-ai-can-t-replace/)  
  <sub>TradingView, 24 hours ago</sub>  
  Wedbush is betting that there is still an investment-friendly economy beyond artificial intelligence.The firm recently filed for the Wedbush Analog Economy...
- [State Street SPDR S&P Biotech ETF (XBI) stock price, news, quote and history](https://au.finance.yahoo.com/quote/XBI/)  
  <sub>Yahoo Finance Australia, 15 hours ago</sub>  
  Find the latest State Street SPDR S&P Biotech ETF (XBI) stock quote, history, news and other vital information to help you with your stock trading and...
- [Bloom Energy Sinks 6% as Traders Take Profits on a 190% YTD Run; Generac and Cummins Pull Back](https://247wallst.com/investing/2026/09/24/bloom-energy-sinks-6-as-traders-take-profits-on-a-190-ytd-run-generac-and-cummins-pull-back/)  
  <sub>24/7 Wall St., 1 hour ago</sub>  
  Bloom Energy (NYSE:BE) is sinking in morning trading, giving back a piece of one of the year's most explosive rallies. Shares are at $258.36, down 6%,...
- [What's Going On With GE Vernova Stock Wednesday?](https://www.benzinga.com/markets/equities/26/09/61952112/whats-going-on-with-ge-vernova-stock-wednesday-2)  
  <sub>Benzinga, 23 hours ago</sub>  
  GE Vernova trades near key support around $897 as analysts maintain a consensus Buy with an average price target of $1187.83.
- [Is Micron a Value Stock? Why a Value ETF Holds 23% In MU - Micron Technology (NASDAQ:MU)](https://www.benzinga.com/markets/tech/26/09/61951487/micron-value-stock-vlue-etf-23-percent-weight)  
  <sub>Benzinga, 23 hours ago</sub>  
  The iShares MSCI USA Value Factor ETF holds 23% in Micron, which trades at 7.5 times forward earnings ahead of Sept. 30 results.
- [State Street Consumer Discretionary Select Sector SPDR ETF (XLY) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLY/)  
  <sub>Yahoo Finance Singapore, 5 hours ago</sub>  
  Find the latest State Street Consumer Discretionary Select Sector SPDR ETF (XLY) stock quote, history, news and other vital information to help you with...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 168.48 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 172.53 (-2.4%), 50d 178.29 (-5.5%), 200d 171.87 (-2.0%); 50d above 200d
Momentum: RSI(14) 32.1 | MACD -2.899 vs signal -2.840 (histogram -0.059)
Returns: 1d -1.0% | 5d -0.1% | 1m -5.9% | 3m -6.5%
52-week range: 147.83 - 186.51 (now 53.4% of the way up)
Volatility: ATR(14) 2.34 (1.4% of price) | annualised 20d 13.3%
Volume: 0.43x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Industrials
What it holds: P/E 28.43 | P/B 6.75 | P/S 3.00 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +20.4% a year | beta to the market 1.02
Cost and size: expense ratio 0.08% | net assets 31.95B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Caterpillar Inc 6.7%, GE Aerospace 6.4%, RTX Corp 5.1%, GE Vernova Inc 4.4%, Union Pacific Corp 3.2%
Sector mix: Industrials 92.8%, Technology 6.7%, Basic materials 0.3%, Consumer cyclical 0.2%
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
Rolled up from the 5 largest holdings, 25.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.7% above the current prices
Holdings read: CAT, GE, RTX, GEV, UNP
Recent rating changes among them:
  - CAT: 2024-10-14 JP Morgan: main, Overweight -> Overweight
  - GE: 2026-09-23 Jefferies: main, Buy -> Buy
  - RTX: 2026-09-23 Bernstein: main, Market Perform -> Market Perform
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

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 136.63M | fund size: 23.02B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Exchange-Traded Funds, US Equities Decline After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-us-equities-171556743.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV were lower. Actively traded Invesco QQQ Trust (QQQ) shed 1.2%.
- [Leading And Lagging Sectors For September 24, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61970129/leading-and-lagging-sectors-september-24-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLE) State Street Energy Select Sector SPDR ETF 63.0000 0.630 1.01 320.6K (NYSE:XLP) State...
- [Best Performing ETFs: Top Returns at a Glance](https://www.tradingkey.com/markets/etf/best-performing?page=145)  
  <sub>TradingKey, 10 hours ago</sub>  
  View TradingKey's list of the best performing ETFs, including price changes, trading volume, multi-period returns, and performance charts.
- [Is Micron a Value Stock? Why a Value ETF Holds 23% In MU - Micron Technology (NASDAQ:MU)](https://www.benzinga.com/markets/tech/26/09/61951487/micron-value-stock-vlue-etf-23-percent-weight)  
  <sub>Benzinga, 23 hours ago</sub>  
  The iShares MSCI USA Value Factor ETF holds 23% in Micron, which trades at 7.5 times forward earnings ahead of Sept. 30 results.
- [Apple’s AI Bet Is Getting Bigger. So Is the Valuation Risk Hiding Inside These ETFs - Apple (NASDAQ:AAPL)](https://www.benzinga.com/etfs/sector-etfs/26/09/61956571/apples-ai-bet-is-getting-bigger-so-is-the-valuation-risk-hiding-inside-these-etfs)  
  <sub>Benzinga, 20 hours ago</sub>  
  Apple's on-device AI push is growing, but its rich valuation creates a bigger risk for Apple-heavy ETFs like GXPT, FTEC and VGT.
- [Bulls Can’t Go Wrong With This Sector for Q4](https://www.schaeffersresearch.com/content/bgs/2026/09/23/bulls-can-t-go-wrong-with-this-sector-for-q4)  
  <sub>Schaeffer's Investment Research, 23 hours ago</sub>  
  Wall Street gears up to enter the fourth and final quarter of 2026, but many stocks are at a crossroads.
- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Thursday Amid Ongoing Middle East Tensions Before US-China Talks](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131757956.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.4%, and the actively t.
- [Sector Update: Tech Stocks Fall Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-tech-stocks-fall-afternoon-194312684.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Tech stocks fell late Wednesday afternoon with the State Street Technology Select Sector SPDR ETF (XLK) declining 0.5% and the State Street SPDR S&P...
- [Sector Update: Tech Stocks Fall Wednesday Afternoon](https://finance.yahoo.com/technology/articles/sector-tech-stocks-fall-wednesday-175128323.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Tech stocks fell Wednesday afternoon, with the State Street Technology Select Sector SPDR ETF (XLK)

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 192.90 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 187.27 (+3.0%), 50d 183.77 (+5.0%), 200d 163.18 (+18.2%); 50d above 200d
Momentum: RSI(14) 60.4 | MACD 2.178 vs signal 1.337 (histogram 0.840)
Returns: 1d -1.3% | 5d +4.9% | 1m +7.1% | 3m +5.4%
52-week range: 127.50 - 198.21 (now 92.5% of the way up)
Volatility: ATR(14) 3.47 (1.8% of price) | annualised 20d 22.4%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

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
Rolled up from the 5 largest holdings, 45.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.55 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.5% above the current prices
Holdings read: NVDA, AAPL, MSFT, AVGO, MU
Recent rating changes among them:
  - NVDA: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - AAPL: 2026-09-23 B of A Securities: reit, Buy -> Buy
  - MSFT: 2026-09-23 Stifel: up, Hold -> Buy
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-09-24 Rosenblatt: main, Buy -> Buy
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
Share count change: 1 week: -5.4% (-6.92B) over 7d
Shares outstanding: 623.25M | fund size: 120.22B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [State Street Consumer Discretionary Select Sector SPDR ETF (XLY) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLY/)  
  <sub>Yahoo Finance Singapore, 5 hours ago</sub>  
  State Street Consumer Discretionary Select Sector SPDR ETF (XLY) · 0.43% · -6.24% · 0.48% · -7.34% · -6.99% · 20.13% · 774.27%. Key events.
- [Better Consumer Staples ETF: Vanguard's VDC vs. State Street's XLP](https://www.fool.com/coverage/etfs/2026/09/23/better-consumer-staples-etf-vanguard-s-vdc-vs-state-street-s-xlp/)  
  <sub>The Motley Fool, 18 hours ago</sub>  
  Comparing the State Street Consumer Staples Select Sector SPDR ETF (XLP -0.36%) and Vanguard Consumer Staples ETF (VDC -0.36%) reveals two defensive giants...
- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Thursday Amid Ongoing Middle East Tensions Before US-China Talks](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131757956.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.4%, and the actively t.
- [Leading And Lagging Sectors For September 24, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61970129/leading-and-lagging-sectors-september-24-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLE) State Street Energy Select Sector SPDR ETF 63.0000 0.630 1.01 320.6K (NYSE:XLP) State...
- [Best Performing ETFs: Top Returns at a Glance](https://www.tradingkey.com/markets/etf/best-performing?page=145)  
  <sub>TradingKey, 10 hours ago</sub>  
  View TradingKey's list of the best performing ETFs, including price changes, trading volume, multi-period returns, and performance charts.
- [XLV vs. PJP: How Broad Healthcare Diversification Stacks Up to Pharma Stocks](https://www.fool.com/coverage/etfs/2026/09/23/xlv-vs-pjp-how-broad-healthcare-diversification-stacks-up-to-pharma-stocks/)  
  <sub>The Motley Fool, 17 hours ago</sub>  
  XLV's broader diversification and lower fees appeal to cost-conscious investors, while PJP's concentrated pharma bet has outperformed over the past year.
- [Xtr.-USD Corp.Bd Dur.SRI PAB R (FXYLD.DE) latest stock news and headlines – Yahoo Finance](https://sg.finance.yahoo.com/quote/FXYLD.DE/news/)  
  <sub>Yahoo Finance Singapore, 9 hours ago</sub>  
  Xtr.-USD Corp.Bd Dur.SRI PAB R (FXYLD.DE). 15.63 +0.02 (+0.15%). At close: 7:38:20 pm GMT+2. Related ETF news. Tech retreats as Treasury yields and oil...
- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance Singapore, 19 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) · 0.61% · -3.33% · 16.60% · 9.04% · 23.27% · 27.38% · 580.30%. Key events. Baseline. Advanced...
- [UBS BBG EO Inf.Lnkd 10+ UETF N (FRC4.HM) latest stock news and headlines – Yahoo Finance](https://sg.finance.yahoo.com/quote/FRC4.HM/news/)  
  <sub>Yahoo Finance Singapore, 17 hours ago</sub>  
  UBS BBG EO Inf.Lnkd 10+ UETF N (FRC4.HM). 14.42 +0.04 (+0.25%). At close: 8:07:13 am GMT+2. Related ETF news. Tech retreats as Treasury yields and oil...
- [Top ETFs: Live Prices, Returns & Trends](https://www.tradingkey.com/markets/etf/top?page=44)  
  <sub>TradingKey, 10 hours ago</sub>  
  View the latest market data on top ETFs to watch, from price movements and trading volume to historical returns and performance trends.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 82.44 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 84.03 (-1.9%), 50d 84.81 (-2.8%), 200d 83.63 (-1.4%); 50d above 200d
Momentum: RSI(14) 39.2 | MACD -0.737 vs signal -0.540 (histogram -0.197)
Returns: 1d +0.0% | 5d -1.1% | 1m -5.7% | 3m -2.4%
52-week range: 75.60 - 90.01 (now 47.5% of the way up)
Volatility: ATR(14) 0.98 (1.2% of price) | annualised 20d 10.8%
Volume: 0.38x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Consumer Defensive
What it holds: P/E 25.14 | P/B 4.58 | P/S 1.36 | 3y earnings growth n/a
Yield: 2.6%
Three-year record: +8.6% a year | beta to the market 0.49
Cost and size: expense ratio 0.08% | net assets 14.52B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Walmart Inc 9.8%, Costco Wholesale Corp 8.9%, Coca-Cola Co 7.3%, Procter & Gamble Co 7.2%, Philip Morris International Inc 6.2%
Sector mix: Consumer defensive 98.2%, Consumer cyclical 1.8%
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
Rolled up from the 5 largest holdings, 39.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.5% above the current prices
Holdings read: WMT, COST, KO, PG, PM
Recent rating changes among them:
  - WMT: 2026-09-10 DA Davidson: main, Buy -> Buy
  - COST: 2026-09-23 BTIG: reit, Buy -> Buy
  - KO: 2026-07-30 Argus Research: main, Buy -> Buy
  - PG: 2026-08-07 Argus Research: down, Buy -> Hold
  - PM: 2026-09-23 UBS: main, Neutral -> Neutral
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
Shares outstanding: 210.17M | fund size: 17.33B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 39.49 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 42.07 (-6.1%), 50d 43.48 (-9.2%), 200d 44.50 (-11.2%); 50d below 200d
Momentum: RSI(14) 22.6 | MACD -0.937 vs signal -0.692 (histogram -0.246)
Returns: 1d -0.6% | 5d -4.4% | 1m -8.6% | 3m -13.3%
52-week range: 39.49 - 47.73 (now 0.0% of the way up)
Volatility: ATR(14) 0.63 (1.6% of price) | annualised 20d 14.7%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Utilities
What it holds: P/E 19.02 | P/B 2.14 | P/S 2.65 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +11.9% a year | beta to the market 0.43
Cost and size: expense ratio 0.08% | net assets 21.84B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: NextEra Energy Inc 13.0%, Southern Co 7.5%, Duke Energy Corp 7.1%, Constellation Energy Corp 6.7%, American Electric Power Co Inc 5.1%
Sector mix: Utilities 100.0%
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
Rolled up from the 5 largest holdings, 39.4% of the fund by weight
Ratings by weight: buy 80.9% | hold 19.1% | sell 0.0% (mean 2.06 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.5% above the current prices
Holdings read: NEE, SO, DUK, CEG, AEP
Recent rating changes among them:
  - NEE: 2026-09-18 Morgan Stanley: main, Overweight -> Overweight
  - SO: 2026-09-18 Morgan Stanley: main, Underweight -> Underweight
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

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 163.27M | fund size: 6.45B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### US health care (XLV) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance Singapore, 19 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) · 0.61% · -3.33% · 16.60% · 9.04% · 23.27% · 27.38% · 580.30%. Key events. Baseline. Advanced...
- [XLV vs. PJP: How Broad Healthcare Diversification Stacks Up to Pharma Stocks](https://www.fool.com/coverage/etfs/2026/09/23/xlv-vs-pjp-how-broad-healthcare-diversification-stacks-up-to-pharma-stocks/)  
  <sub>The Motley Fool, 17 hours ago</sub>  
  XLV's broader diversification and lower fees appeal to cost-conscious investors, while PJP's concentrated pharma bet has outperformed over the past year.
- [3 Healthcare ETFs for FDA-Approved Profits](https://www.theglobeandmail.com/investing/markets/stocks/MRK/pressreleases/4758698/3-healthcare-etfs-for-fda-approved-profits/)  
  <sub>The Globe and Mail, 24 hours ago</sub>  
  Detailed price information for Merck & Company (MRK-N) from The Globe and Mail including charting and trades.
- [Healthcare Stocks Slipped As Biotech Took The Bigger Hit](https://finimize.com/content/healthcare-stocks-slipped-as-biotech-took-the-bigger-hit)  
  <sub>Finimize, 20 hours ago</sub>  
  The iShares Biotechnology ETF fell 2.1% as Astrana flagged a possible data breach and Immunovant halted a lupus program after a trial miss.
- [Best Performing ETFs: Top Returns at a Glance](https://www.tradingkey.com/markets/etf/best-performing?page=145)  
  <sub>TradingKey, 10 hours ago</sub>  
  View TradingKey's list of the best performing ETFs, including price changes, trading volume, multi-period returns, and performance charts.
- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Thursday Amid Ongoing Middle East Tensions Before US-China Talks](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131757956.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.4%, and the actively t.
- [Top ETFs: Live Prices, Returns & Trends](https://www.tradingkey.com/markets/etf/top?page=68)  
  <sub>TradingKey, 2 hours ago</sub>  
  View the latest market data on top ETFs to watch, from price movements and trading volume to historical returns and performance trends.
- [3 ETFs That Could Deliver 11%+ Returns, According to the AI Analyst](https://www.tipranks.com/news/3-etfs-that-could-deliver-11-returns-according-to-the-ai-analyst)  
  <sub>TipRanks, 16 hours ago</sub>  
  TipRanks' ETF AI Analyst has an Outperform rating on the Schwab U.S. Dividend Equity ETF ($SCHD), Health Care Select Sector SPDR Fund ($XLV), and Vanguard...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 170.24 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 169.47 (+0.5%), 50d 167.30 (+1.8%), 200d 156.14 (+9.0%); 50d above 200d
Momentum: RSI(14) 55.5 | MACD 0.179 vs signal 0.323 (histogram -0.144)
Returns: 1d +0.9% | 5d +1.5% | 1m -2.6% | 3m +11.0%
52-week range: 134.13 - 175.68 (now 86.9% of the way up)
Volatility: ATR(14) 2.39 (1.4% of price) | annualised 20d 13.8%
Volume: 0.53x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

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
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.4% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-09-22 TD Cowen: reit, Buy -> Buy
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

```text
Direction: money going out (1 week)
Share count change: 1 week: -0.7% (-328.94M) over 7d
Shares outstanding: 259.88M | fund size: 44.24B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [State Street Consumer Discretionary Select Sector SPDR ETF (XLY) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLY/)  
  <sub>Yahoo Finance Singapore, 5 hours ago</sub>  
  State Street Consumer Discretionary Select Sector SPDR ETF (XLY) · 0.43% · -6.24% · 0.48% · -7.34% · -6.99% · 20.13% · 774.27%. Key events.
- [Consumer discretionary stocks with long-running Strong Sell Quant ratings (XLY:NYSEARCA)](https://seekingalpha.com/news/4646725-consumer-discretionary-stocks-with-long-running-strong-sell-quant-ratings)  
  <sub>Seeking Alpha, 8 minutes ago</sub>  
  Mixed 2026 consumer discretionary outlook: see 4 stocks flagged Strong Sell by Quant Ratings (LCID, EVGO, WHR, SERV) and related ETFs—read now.
- [Best Performing ETFs: Top Returns at a Glance](https://www.tradingkey.com/markets/etf/best-performing?page=145)  
  <sub>TradingKey, 10 hours ago</sub>  
  View TradingKey's list of the best performing ETFs, including price changes, trading volume, multi-period returns, and performance charts.
- [Sector Update: Consumer Stocks Retreat Late Afternoon](https://ca.finance.yahoo.com/news/sector-consumer-stocks-retreat-afternoon-194623415.html)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Consumer stocks were lower late Wednesday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) decreasing 0.5% and the State...
- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Thursday Amid Ongoing Middle East Tensions Before US-China Talks](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131757956.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.4%, and the actively t.
- [Sector Update: Consumer](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-191320076.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Consumer stocks were lower late Wednesday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) decreasing 0.5% and the State...
- [Exchange-Traded Funds, US Equities Decline After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-us-equities-171556743.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV were lower. Actively traded Invesco QQQ Trust (QQQ) shed 1.2%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 109.79 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 113.40 (-3.2%), 50d 115.04 (-4.6%), 200d 116.72 (-5.9%); 50d below 200d
Momentum: RSI(14) 36.4 | MACD -1.568 vs signal -1.281 (histogram -0.286)
Returns: 1d -0.8% | 5d -0.3% | 1m -7.2% | 3m -4.6%
52-week range: 105.66 - 124.52 (now 21.9% of the way up)
Volatility: ATR(14) 1.60 (1.5% of price) | annualised 20d 16.0%
Volume: 0.24x the 20-day average
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
Three-year record: +12.7% a year | beta to the market 1.16
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.78 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.3% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, BKNG
Recent rating changes among them:
  - AMZN: 2026-09-03 Wells Fargo: main, Overweight -> Overweight
  - TSLA: 2026-09-16 Goldman Sachs: reit, Neutral -> Neutral
  - HD: 2026-09-09 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-09-24 Evercore ISI Group: main, Outperform -> Outperform
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
Direction: money coming in (1 week)
Share count change: 1 week: +0.6% (122.54M) over 7d
Shares outstanding: 202.77M | fund size: 22.26B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Sugar (CANE) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 11.24 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 11.39 (-1.3%), 50d 10.72 (+4.9%), 200d 9.92 (+13.3%); 50d above 200d
Momentum: RSI(14) 52.1 | MACD 0.114 vs signal 0.194 (histogram -0.080)
Returns: 1d -1.1% | 5d -1.3% | 1m -0.0% | 3m +20.9%
52-week range: 9.02 - 11.82 (now 79.5% of the way up)
Volatility: ATR(14) 0.21 (1.9% of price) | annualised 20d 25.3%
Volume: 0.65x the 20-day average
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
Cost of holding this fund instead of sugar itself: -8.9% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +20.9%, commodity +37.6%, gap -16.7% | 6 months: fund +5.5%, commodity +19.9%, gap -14.4% | 12 months: fund +10.1%, commodity +19.0%, gap -8.9%
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
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 18.5% of open interest (1,219,523 contracts)
Change on the week: -0.2% of open interest
Crowding: 98% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +2.9% (1.65M) over 7d
Shares outstanding: 5.21M | fund size: 58.63M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 19.80 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 19.99 (-1.0%), 50d 18.87 (+4.9%), 200d 18.08 (+9.5%); 50d above 200d
Momentum: RSI(14) 54.6 | MACD 0.287 vs signal 0.386 (histogram -0.099)
Returns: 1d +0.2% | 5d -0.9% | 1m +3.0% | 3m +19.1%
52-week range: 16.47 - 20.29 (now 87.0% of the way up)
Volatility: ATR(14) 0.32 (1.6% of price) | annualised 20d 18.8%
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
Cost of holding this fund instead of corn itself: -11.8% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +19.1%, commodity +27.7%, gap -8.6% | 6 months: fund +6.9%, commodity +13.3%, gap -6.4% | 12 months: fund +12.4%, commodity +24.2%, gap -11.8%
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
Direction: money going out (1 week)
Share count change: 1 week: -1.1% (-1.83M) over 7d
Shares outstanding: 8.17M | fund size: 161.70M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 40.53 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 39.76 (+1.9%), 50d 39.57 (+2.4%), 200d 37.20 (+9.0%); 50d above 200d
Momentum: RSI(14) 56.5 | MACD 0.167 vs signal 0.055 (histogram 0.112)
Returns: 1d -0.2% | 5d +5.0% | 1m +1.2% | 3m +11.6%
52-week range: 28.62 - 41.05 (now 95.9% of the way up)
Volatility: ATR(14) 0.68 (1.7% of price) | annualised 20d 27.6%
Volume: 0.16x the 20-day average
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
Cost of holding this fund instead of copper itself: -5.8% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +11.6%, commodity +11.3%, gap +0.3% | 6 months: fund +21.5%, commodity +22.2%, gap -0.7% | 12 months: fund +41.6%, commodity +47.4%, gap -5.8%
A commodity fund holds futures, not copper, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 22.5% of open interest (289,463 contracts)
Change on the week: -5.1% of open interest
Crowding: 40% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -5.4% (-42.59M) over 7d
Shares outstanding: 18.51M | fund size: 750.17M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Gold (GLD) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Zacks Investment Ideas feature highlights: GLD, QQQ, USO, MU and TWLO](https://finance.yahoo.com/markets/stocks/articles/zacks-investment-ideas-feature-highlights-093400194.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Chicago, IL – September 24, 2026 – Today, Zacks Investment Ideas feature highlights Gold ETF GLD, Nasdaq 100 Index ETF QQQ, United States Oil Fund ETF USO,...
- [Return Driver, Diversifier or Hedge? The Real Truth About Gold in Your Portfolio](https://www.kiplinger.com/investing/gold/golds-true-role-in-your-portfolio)  
  <sub>Kiplinger, 2 hours ago</sub>  
  To decide whether gold is right for you, consider three roles it could play: As a return driver, as a diversifier or as a hedge.
- [Gold ETFs Just Had Their 2nd-Biggest Month Ever](https://www.etf.com/sections/news/gold-etfs-just-had-their-2nd-biggest-month-ever)  
  <sub>ETF.com, 19 hours ago</sub>  
  In August, investors poured roughly $18 billion into gold ETFs, the second-largest monthly inflow in history, driving global holdings to an all-time record.
- [Gold slides as rate hike expectations boost Treasury yields to multiyear highs (GLD:NYSEARCA)](https://seekingalpha.com/news/4646367-gold-slides-as-rate-hike-expectations-boost-treasury-yields-to-multiyear-highs)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Gold futures fell sharply as the US dollar strengthened and Treasury yields rose, as Federal Reserve policymakers reaffirmed support for last week's rate...
- [SPDR Gold Trust Slips Wednesday: What's Happening?](https://www.benzinga.com/trading-ideas/movers/26/09/61955386/spdr-gold-trust-slips-wednesday-whats-happening)  
  <sub>Benzinga, 21 hours ago</sub>  
  SPDR Gold Trust (NYSE:GLD) shares are trading lower Wednesday afternoon as gold bullion prices decline under pressure from a strengthening U.S. dollar,...
- [SPDR Gold ETF Options Spot-On: On September 23rd, 380.48K Contracts Were Traded, With 5.35 Million Open Interest](https://news.futunn.com/en/post/1000116867/spdr-gold-etf-options-spot-on-on-september-23rd-380)  
  <sub>富途牛牛, 18 hours ago</sub>  
  OnSeptember 23rd ET, $SPDR Gold ETF(GLD.US)$ had active options trading, with a total trading volume of 380.48K options for the day, of which put options...
- [VanEck Gold Miners ETF (GDX) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GDX/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Find the latest VanEck Gold Miners ETF (GDX) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Rejoice! The Summer Stock Slump is Over](https://sg.finance.yahoo.com/news/rejoice-summer-stock-slump-over-173100996.html)  
  <sub>Yahoo Finance Singapore, 22 hours ago</sub>  
  As the summer chop fades and historical tailwinds align, patient investors who weathered the consolidation phase are well-positioned to capitaliz.
- [Day 488: Rate Hike + Trump 2.0 Day 611](https://www.moomoo.com/community/feed/day-488-rate-hike-trump-2-0-day-611-117326677999622)  
  <sub>Moomoo, 16 minutes ago</sub>  
  Market Recap | Thursday, September 24, 2026 Yields at a 19-year high, and this time oil isn't cooperating The bond market just broke through a gen...
- [TD Cowen Maintains Kinross Gold(KGC.US) With Buy Rating, Raises Target Price to $35](https://news.futunn.com/en/post/1000175960/td-cowen-maintains-kinross-gold-kgcus-with-buy-rating-raises)  
  <sub>富途牛牛, 1 hour ago</sub>  
  TDCowen analyst Steven Green maintains $Kinross Gold(KGC.US)$ with a buy rating, and adjusts the target price from $22 to $35.According to TipRanks data,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 389.40 (bar of 2026-09-24), from 502 daily bars
Trend: vs 20d SMA 400.68 (-2.8%), 50d 394.82 (-1.4%), 200d 416.39 (-6.5%); 50d below 200d
Momentum: RSI(14) 42.1 | MACD -1.797 vs signal -0.244 (histogram -1.553)
Returns: 1d -0.9% | 5d -2.2% | 1m -9.0% | 3m +5.4%
52-week range: 343.32 - 495.90 (now 30.2% of the way up)
Volatility: ATR(14) 7.17 (1.8% of price) | annualised 20d 23.1%
Volume: 0.27x the 20-day average
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
Measured: 3 months: fund +5.4%, commodity +6.0%, gap -0.6% | 6 months: fund -6.5%, commodity -5.8%, gap -0.7% | 12 months: fund +12.4%, commodity +12.4%, gap -0.0%
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
Shares outstanding: 260.30M | fund size: 101.36B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 57.08 (bar of 2026-09-24), from 502 daily bars
Trend: vs 20d SMA 59.10 (-3.4%), 50d 57.30 (-0.4%), 200d 65.93 (-13.4%); 50d below 200d
Momentum: RSI(14) 44.9 | MACD 0.010 vs signal 0.220 (histogram -0.209)
Returns: 1d -1.9% | 5d -3.2% | 1m -8.4% | 3m +9.0%
52-week range: 39.82 - 105.60 (now 26.2% of the way up)
Volatility: ATR(14) 1.82 (3.2% of price) | annualised 20d 41.0%
Volume: 0.38x the 20-day average
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
Cost of holding this fund instead of silver itself: -1.5% a year -- a steady drag
Measured: 3 months: fund +9.0%, commodity +9.3%, gap -0.3% | 6 months: fund -12.5%, commodity -11.9%, gap -0.6% | 12 months: fund +42.8%, commodity +44.3%, gap -1.5%
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
Share count change: 1 week: -4.6% (-1.62B) over 7d
Shares outstanding: 582.90M | fund size: 33.27B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Soybeans (SOYB) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [주목할 ETF TOP: 실시간 시세와 수익률 비교](https://www.tradingkey.com/kr/markets/etf/top?page=117)  
  <sub>TradingKey, 2 hours ago</sub>  
  주목할 ETF의 최신 시세와 등락률, 거래량, 과거 수익률 및 성과 추이를 확인하고 주요 시장 흐름을 살펴보세요.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 27.93 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 27.66 (+1.0%), 50d 26.41 (+5.8%), 200d 24.46 (+14.2%); 50d above 200d
Momentum: RSI(14) 61.7 | MACD 0.487 vs signal 0.538 (histogram -0.051)
Returns: 1d -0.2% | 5d -0.1% | 1m +7.7% | 3m +15.9%
52-week range: 21.46 - 28.14 (now 96.9% of the way up)
Volatility: ATR(14) 0.34 (1.2% of price) | annualised 20d 17.5%
Volume: 0.08x the 20-day average
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
Cost of holding this fund instead of soybeans itself: -1.4% a year -- a steady drag
Measured: 3 months: fund +15.9%, commodity +17.0%, gap -1.0% | 6 months: fund +16.1%, commodity +12.5%, gap +3.5% | 12 months: fund +28.9%, commodity +30.3%, gap -1.4%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

```text
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 21.9% of open interest (1,104,880 contracts)
Change on the week: -2.2% of open interest
Crowding: 88% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -1.7% (-786.57K) over 7d
Shares outstanding: 1.65M | fund size: 46.06M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 11.48 (bar of 2026-09-24), from 502 daily bars
Trend: vs 20d SMA 10.50 (+9.3%), 50d 10.27 (+11.8%), 200d 11.45 (+0.3%); 50d below 200d
Momentum: RSI(14) 70.3 | MACD 0.159 vs signal 0.063 (histogram 0.097)
Returns: 1d +5.6% | 5d +11.2% | 1m +12.2% | 3m -2.3%
52-week range: 9.63 - 16.90 (now 25.5% of the way up)
Volatility: ATR(14) 0.32 (2.8% of price) | annualised 20d 36.7%
Volume: 1.48x the 20-day average
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
Cost of holding this fund instead of natural gas itself: -23.2% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -2.3%, commodity -0.9%, gap -1.4% | 6 months: fund -3.2%, commodity +12.2%, gap -15.4% | 12 months: fund -7.1%, commodity +16.1%, gap -23.2%
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
Direction: money coming in (1 week)
Share count change: 1 week: +1.2% (7.89M) over 7d
Shares outstanding: 56.32M | fund size: 646.69M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [United States Oil Fund, LP (USO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/USO/)  
  <sub>Yahoo! Finance Canada, 10 hours ago</sub>  
  Find the latest United States Oil Fund, LP (USO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Zacks Investment Ideas feature highlights: GLD, QQQ, USO, MU and TWLO](https://finance.yahoo.com/markets/stocks/articles/zacks-investment-ideas-feature-highlights-093400194.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Chicago, IL – September 24, 2026 – Today, Zacks Investment Ideas feature highlights Gold ETF GLD, Nasdaq 100 Index ETF QQQ, United States Oil Fund ETF USO,...
- [Saudi oil exports surge to highest since start of Iran war on Hormuz ramp-up (USO:NYSEARCA)](https://seekingalpha.com/news/4646702-saudis-oil-exports-surge-to-highest-since-start-of-iran-war-on-hormuz-ramp-up)  
  <sub>Seeking Alpha, 59 minutes ago</sub>  
  Saudi Arabia's crude oil shipments in September jumped to the highest level since the start of the Iran war, Bloomberg reported.
- [VLO Stock Heads For Best Year Since 1982 — Michael Burry Says It Has Become A ‘Huge Position’](https://stocktwits.com/news-articles/markets/equity/vlo-stock-best-year-1982-michael-burry-huge-position/cZtlx8lRBR0)  
  <sub>Stocktwits, 5 hours ago</sub>  
  Burry recovered his initial investment “and then some” for charity, while retaining a sizable stake that is “deep into house's money.”
- [Oil Groups Join Chris Wright to Oppose Diesel Export Ban, Urge Trump Not to Weaken US Influence: Warn it Could Raise Fuel Costs, Hurt American Refiners](https://www.tradingview.com/news/benzinga:84291744e094b:0-oil-groups-join-chris-wright-to-oppose-diesel-export-ban-urge-trump-not-to-weaken-us-influence-warn-it-could-raise-fuel-costs-hurt-american-refiners/)  
  <sub>TradingView, 5 hours ago</sub>  
  Industry groups and businesses have urged President Donald Trump to rescind the plan to ban or limit exports of diesel, which has been pushed back against...
- [IONQ’s Breakthrough Ignites Quantum Computing Stocks](https://www.benzinga.com/Opinion/26/09/61952084/ionqs-breakthrough-ignites-quantum-computing-stocks)  
  <sub>Benzinga, 23 hours ago</sub>  
  Quantum Computing Breakthrough Please click here for an enlarged chart of IONQ Inc (NYSE:IONQ). Note the following: This article is about the big picture,...
- [Trump Reportedly Says Oil Prices Won’t Tumble Until After Midterms, While Iran Signals More Intense War — USO, UCO Rise](https://stocktwits.com/news-articles/markets/equity/trump-reportedly-says-oil-prices-wont-tumble-until-after-midterms-while-iran-signals-more-intense-war-uso-uco-rise/cZt7k6WRJC2)  
  <sub>Stocktwits, 15 hours ago</sub>  
  President Donald Trump reportedly said on Wednesday that energy prices elevated by the Iran war are unlikely to come down until after the midterm elections,...
- [Crude oil rebounds after losing streak; diesel futures drop after export restriction talk](https://seekingalpha.com/news/4646401-crude-oil-rebounds-after-losing-streak-diesel-futures-drop-after-export-restriction-talk)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  Crude oil turned higher but diesel fell after Energy Secretary Chris Wright said the Trump administration is considering restrictions on diesel imports but...
- [Rejoice! The Summer Stock Slump is Over](https://sg.finance.yahoo.com/news/rejoice-summer-stock-slump-over-173100996.html)  
  <sub>Yahoo Finance Singapore, 22 hours ago</sub>  
  As the summer chop fades and historical tailwinds align, patient investors who weathered the consolidation phase are well-positioned to capitaliz.
- [United States Oil Fund LP (Derivatives) Price (USO/USD) Today | Live Price, Market Cap & Chart](https://www.binance.com/en/price/united-states-oil-fund-derivatives)  
  <sub>Binance, 17 hours ago</sub>  
  Real-time United States Oil Fund LP (Derivatives) market data. Track live USO price movements, market cap, trading volume, and other key metrics to stay...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 154.94 (bar of 2026-09-24), from 502 daily bars
Trend: vs 20d SMA 147.44 (+5.1%), 50d 135.09 (+14.7%), 200d 112.84 (+37.3%); 50d above 200d
Momentum: RSI(14) 61.1 | MACD 5.488 vs signal 6.319 (histogram -0.831)
Returns: 1d +4.1% | 5d -0.2% | 1m +22.8% | 3m +41.7%
52-week range: 66.17 - 161.86 (now 92.8% of the way up)
Volatility: ATR(14) 5.19 (3.4% of price) | annualised 20d 44.6%
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

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

```text
US inventories, week ending 2026-09-18 (published the following Wednesday)
  Crude oil: 426.4 million barrels, +3.0 on the week (a build), 58% percentile over 52 weeks
  Petrol: 206.0 million barrels, -1.7 on the week (a draw), 8% percentile over 52 weeks -- low for the time of year
  Diesel: 107.4 million barrels, -0.4 on the week (a draw), 33% percentile over 52 weeks
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
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 5.4% of open interest (1,955,764 contracts)
Change on the week: -0.3% of open interest
Crowding: 98% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +5.1% (96.23M) over 7d
Shares outstanding: 12.78M | fund size: 1.98B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":"User is not authorized to access this resource","type":"invalid_request_error","param":null,"code":"invalid_api_key"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Teucrium Commodity Trust resumes accepting redemptions for 7RCC Spot Bitcoin and Carbon Credit Futures ETF](https://www.tradingview.com/news/tradingview:bf0df3d6a66c2:0-teucrium-commodity-trust-resumes-accepting-redemptions-for-7rcc-spot-bitcoin-and-carbon-credit-futures-etf/)  
  <sub>TradingView, 2 hours ago</sub>  
  Teucrium Commodity Trust announced it will resume accepting redemption orders for the 7RCC Spot Bitcoin and Carbon Credit Futures ETF after outstanding...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (+0.07 on the week) | 5-year 5.01% (+0.15 on the week) | 10-year 5.14% (+0.13 on the week) | 30-year 5.43% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +1.10 points -- upward sloping (normal)
US dollar index: 101.31 (+1.00 on the week)
Volatility (VIX): 15.94 (-1.8 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.71% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 25.71 (bar of 2026-09-24), from 501 daily bars
Trend: vs 20d SMA 26.73 (-3.8%), 50d 25.54 (+0.7%), 200d 23.03 (+11.7%); 50d above 200d
Momentum: RSI(14) 46.3 | MACD 0.110 vs signal 0.319 (histogram -0.209)
Returns: 1d +0.1% | 5d -3.2% | 1m +0.9% | 3m +15.0%
52-week range: 19.88 - 28.00 (now 71.8% of the way up)
Volatility: ATR(14) 0.60 (2.3% of price) | annualised 20d 32.4%
Volume: 0.24x the 20-day average
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
Cost of holding this fund instead of wheat itself: -11.4% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +15.0%, commodity +19.9%, gap -4.9% | 6 months: fund +13.3%, commodity +18.6%, gap -5.3% | 12 months: fund +24.8%, commodity +36.2%, gap -11.4%
A commodity fund holds futures, not wheat, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

```text
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 0.8% of open interest (485,138 contracts)
Change on the week: -1.8% of open interest
Crowding: 90% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -0.5% (-1.88M) over 7d
Shares outstanding: 13.80M | fund size: 354.78M
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

