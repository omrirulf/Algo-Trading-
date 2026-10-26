# Daily report

**26 Oct 2026, 18:08 Israel time (16:08 UTC)** · 80 names checked · 1 traded · 1 with a problem

**Answers with no explanation:** 17 of 66 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 5 | 10 | 1 |
| Whole-market funds | 14 | 0 | 14 | 0 |
| Sector and country funds | 41 | 1 | 40 | 0 |
| Commodities | 9 | 0 | 9 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| US company bonds, riskier (HYG) · Index fund | **Stop raised.** At +0.29R, following the price. Stop-loss raised 76.66 → 76.70. |
| JPMorgan Chase (JPM) · Company | **Stop raised.** At +0.11R, following the price. Stop-loss raised 321.20 → 323.17. |
| Royal Bank of Canada (RY) · Company | **Stop raised.** At +0.98R, following the price. Stop-loss raised 194.88 → 195.67. |
| US materials and chemicals (XLB) · Sector or country | **Stop raised.** At +0.33R, following the price. Stop-loss raised 49.68 → 50.09. |
| Exxon Mobil (XOM) · Company | **Stop raised.** At +2.75R, following the price. Stop-loss raised 174.17 → 174.71. |
| ASML (ASML) · Company | **Holding.** +0.41R, holding 3 shares. Stop-loss 1684.98. |
| Israel (EIS) · Sector or country | **Holding.** -0.21R, holding 57 shares. Stop-loss 118.59. |
| United Kingdom (EWU) · Sector or country | **Holding.** +1.61R, holding 104 shares. Stop-loss 47.23. |
| Gold (GLD) · Commodity | **Holding.** +1.35R, holding 7 shares. Stop-loss 378.03. |
| HDFC Bank (HDB) · Company | **Holding.** -0.89R, holding 60 shares. Stop-loss 21.65. |
| Eli Lilly (LLY) · Company | **Holding.** +2.18R, holding 3 shares. Stop-loss 1233.74. |
| Microsoft (MSFT) · Company | **Holding.** -0.19R, holding 9 shares. Stop-loss 509.74. |
| Nvidia (NVDA) · Company | **Holding.** +0.13R, holding 23 shares. Stop-loss 225.68. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### MercadoLibre (MELI) · Company — NEUTRAL, confidence 0.82

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “SELL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Brazil election result caused ~10% premarket drop in MELI
- Price below 20d, 50d, 200d SMAs; RSI 29.5; MACD negative
- Trailing P/E 44, forward P/E 28.8, debt/equity 168.6% indicating expensive, highly levered
- Earnings record: 3 of last 4 quarters missed expectations

<details><summary><b>News</b> — score -0.90</summary>

- [Why Is MercadoLibre Stock Sinking Monday?](https://www.benzinga.com/trading-ideas/movers/26/10/62585424/why-is-mercadolibre-stock-sinking-monday)  
  <sub>Benzinga, 3 hours ago</sub>  
  MercadoLibre (MELI) stock drops 9% premarket after Lula's Brazil election win sparks a sell-off ahead of upcoming Q3 earnings.
- [Why is MercadoLibre stock plunging today?](https://www.investing.com/news/stock-market-news/why-is-mercadolibre-stock-plunging-today-93CH-4971742)  
  <sub>Investing.com, 5 hours ago</sub>  
  Investing.com -- Shares of MercadoLibre fell 10.8% in pre-open trading after Brazil's presidential election delivered a result that caught financial markets...
- [Brazilian Stocks Tumble as Lula Wins Surprise Fourth Term: Nu Holdings Sinks 25%, Petrobras Tumbles 21%, MercadoLibre Drops 15%](https://finance.yahoo.com/markets/stocks/articles/brazilian-stocks-tumble-lula-wins-132206701.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  Nu Holdings and Petrobras drop 25% and 21% as Lula's fourth-term win fuels fears of tax hikes and state intervention. The iShares MSCI Brazil ETF sank 28%,...
- [These consumer stocks are falling after the election results in Brazil (ABEV:NYSE)](https://seekingalpha.com/news/4657099-these-consumer-stocks-are-falling-after-the-election-results-in-brazil)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Brazil election shock hits Ambev, Arcos Dorados, MercadoLibre and JBS as investors fear currency and fiscal risks.
- [MercadoLibre Inc Stock (MELI) Opened Down by 12.71% on Oct 26: Facts Behind the Movement](https://www.tradingkey.com/news/market-movers/262239508-market-movers-meli-20261026)  
  <sub>TradingKey, 59 minutes ago</sub>  
  MercadoLibre faced downward pressure from political and macroeconomic developments in Brazil.Aggressive strategic reinvestments have placed noticeable...
- [Update: Meta Launches $35 Billion Stock, Preferred Offerings; Plans Potential $60 Billion ATM Stock Offering](https://ca.finance.yahoo.com/news/meta-launches-35-billion-stock-122202450.html)  
  <sub>Yahoo! Finance Canada, 2 hours ago</sub>  
  (Updates with stock price moves in the first paragraph and details of the potential offering in the fifth paragraph.) Meta Platforms (META) stock gained...
- [MELI Nov 2026 2280.000 call (MELI261113C02280000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/MELI261113C02280000/)  
  <sub>Yahoo Finance UK, 5 hours ago</sub>  
  Find the latest MELI Nov 2026 2280.000 call (MELI261113C02280000) stock quote, history, news and other vital information to help you with your stock trading...
- [RTX Corporation (RTX) stock price, news, quote and history - Yahoo Finance](https://sg.finance.yahoo.com/quote/RTX/latest-news/)  
  <sub>Yahoo Finance Singapore, 1 hour ago</sub>  
  Find the latest RTX Corporation (RTX) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Robinhood Markets, Inc. (HOOD) latest stock news and headlines – Yahoo Finance](https://sg.finance.yahoo.com/quote/HOOD/news/)  
  <sub>Yahoo Finance Singapore, 3 hours ago</sub>  
  Get the latest Robinhood Markets, Inc. (HOOD) stock news and headlines to help you in your trading and investment decisions.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.90</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 1,620.05 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 1,815.04 (-10.7%), 50d 1,854.84 (-12.7%), 200d 1,822.41 (-11.1%); 50d above 200d
Momentum: RSI(14) 29.5 | MACD -16.373 vs signal -2.583 (histogram -13.790)
Returns: 1d -10.5% | 5d -11.9% | 1m -7.6% | 3m -13.0%
52-week range: 1,546.81 - 2,360.76 (now 9.0% of the way up)
Volatility: ATR(14) 66.61 (4.1% of price) | annualised 20d 55.4%
Volume: 2.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.40</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 82.13B
Valuation: trailing P/E 44.06 | forward P/E 28.81 | P/B 10.48 | PEG 0.99
Profitability: profit margin 5.3% | operating margin 6.7% | ROE 27.5%
Growth (YoY): revenue +49.8% | earnings -10.9%
Balance sheet: debt/equity 168.6% | free cash flow 353.38M
Risk: beta 1.31 | short interest 1.8% of float
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: buy (mean 1.62 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 4 strong buy, 16 buy, 6 hold, 0 sell, 0 strong sell
Price target: mean 2,273.86 (+40.4% vs last close), range 1,750.00 - 2,800.00
Recent rating changes:
  - 2026-10-13 Citigroup: main, Neutral -> Neutral
  - 2026-10-12 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-10-06 Susquehanna: main, Positive -> Positive
  - 2026-09-03 BTIG: reit, Buy -> Buy
  - 2026-08-11 JP Morgan: main, Neutral -> Neutral
  - 2026-08-06 Cantor Fitzgerald: main, Overweight -> Overweight
Institutional ownership: 80.1%
Largest holders: Capital Research Global Investors (6.2%), BAILLIE GIFFORD & CO (6.0%), Capital International Investors (3.7%), Capital World Investors (3.5%), Morgan Stanley (2.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

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

### Elbit Systems (ESLT) · Company — BULLISH, confidence 0.78

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Strong, ticker‑specific news of new $200M Asia‑Pacific airborne contracts and a $235M European deal provides a clear catalyst. This is reinforced by four consecutive earnings beats and supportive technicals (price up 4.8% on low volume, RSI 63.8, MACD strongly positive). Fundamentals show solid growth but high valuation, and analyst consensus is neutral, so overall view is bullish with moderate‑high conviction.

**Main reasons it gave:**
- Awarded $200M Asia‑Pacific airborne contracts (new revenue catalyst)
- Four consecutive earnings beats (strong earnings momentum)
- Price rose 4.8% on low volume; RSI 63.8; MACD bullish
- Revenue +15.9% YoY, trailing P/E 58 (expensive valuation)

<details><summary><b>News</b> — score +0.90</summary>

- [Elbit Systems Ltd. (ESLT) latest stock news and headlines – Yahoo Finance](https://sg.finance.yahoo.com/quote/ESLT/news/)  
  <sub>Yahoo Finance Singapore, 6 hours ago</sub>  
  Elbit Systems Ltd. (ESLT).
- [Elbit's contracts worth about $200 million cover helicopter sensors, training-system upgrades and cockpit displays.](https://www.stocktitan.net/news/ESLT/elbit-systems-awarded-approximately-200-million-in-contracts-for-06f3uqjeyp3c.html)  
  <sub>Stock Titan, 7 hours ago</sub>  
  Elbit Systems (ESLT) was awarded approximately $200 million in contracts to supply airborne intelligence and training solutions to an Asia-Pacific country.
- [An Asia-Pacific country awards Elbit Systems (ESLT) airborne contracts spanning up to five years.](https://www.stocktitan.net/sec-filings/ESLT/6-k-elbit-systems-ltd-current-report-foreign-issuer-78097a13f6dc.html)  
  <sub>Stock Titan, 5 hours ago</sub>  
  Elbit Systems Ltd. (ESLT) was awarded contracts valued at approximately $200 million by a country in Asia-Pacific for airborne ISTAR and training solutions.
- [ESLT stock pre-market at EUR 655.50: defense systems provider](https://www.ad-hoc-news.de/boerse/news/vorboerse/eslt-stock-pre-market-at-eur-655-50-defense-systems-provider/70412526)  
  <sub>ad-hoc-news.de, 8 hours ago</sub>  
  The company supplies defense, homeland-security and aerospace systems to government and commercial customers. At Lang & Schwarz the stock trades pre-market...
- [Elbit wins USD 200.00 million contracts as Elbit Systems stock trades at EUR 677.50](https://www.ad-hoc-news.de/boerse/news/corporate-news/elbit-wins-usd-200-00-million-contracts-as-elbit-systems-stock-trades-at-eur-677-50/70414952)  
  <sub>ad-hoc-news.de, 31 minutes ago</sub>  
  Elbit wins USD 200.00 million airborne contracts on October 26, 2026. Elbit Systems stock costs EUR 677.50 during trading on October 26, 2026.
- [Elbit Systems completes ISE acquisition while Elbit Systems stock trades at EUR 654.75](https://www.ad-hoc-news.de/boerse/news/corporate-news/elbit-systems-completes-ise-acquisition-while-elbit-systems-stock-trades/70413111)  
  <sub>ad-hoc-news.de, 6 hours ago</sub>  
  Elbit Systems completed ISE acquisition on October 20, 2026, adding underwater robotics. Elbit Systems stock costs EUR 654.75 on October 26, 2026.
- [Weekly Recap: $235M G‑to‑G EXTRA‑MR/PULS deal and shares rise pre‑Nov17](https://www.tradingview.com/news/tradingview:e94d900785f25:0-weekly-recap-235m-g-to-g-extra-mr-puls-deal-and-shares-rise-pre-nov17/)  
  <sub>TradingView, 4 hours ago</sub>  
  Elbit Systems Ltd (NASDAQ:ESLT) won a $235M, three-year European government-to-government rocket and artillery deal and will open a Laser Warning Systems...
- [Elbit Systems stock trades at EUR 657.50 as Sweden center is planned](https://www.ad-hoc-news.de/boerse/news/corporate-news/elbit-systems-stock-trades-at-eur-657-50-as-sweden-center-is-planned/70410556)  
  <sub>ad-hoc-news.de, 22 hours ago</sub>  
  Elbit Systems stock trades at EUR 657.50 in weekend trading on October 25, 2026. Sweden center plans were announced October 14.
- [ESLT Stock In Focus After Elbit Systems Secures $200M In Asia-Pacific Contracts](https://newsable.asianetnews.com/markets/eslt-stock-in-focus-after-elbit-systems-secures-200m-in-asia-pacific-contracts-articleshow-kkilq0z)  
  <sub>Asianet Newsable, 2 hours ago</sub>  
  Elbit's new contract will also supply head-up display (HUD) systems with high-resolution displays, enhanced video capabilities, and low power consumption...
- [Elbit Systems awarded $200M in contracts for airborne ISTAR](https://www.tipranks.com/news/the-fly/elbit-systems-awarded-200m-in-contracts-for-airborne-istar-thefly-news)  
  <sub>TipRanks, 5 hours ago</sub>  
  Elbit Systems (ESLT) announced that it was awarded contracts in an aggregate value of approximately $200M from a country in Asia-Pacific for the supply of...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.40</summary>

```text
Last close 770.77 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 709.17 (+8.7%), 50d 722.06 (+6.7%), 200d 783.81 (-1.7%); 50d below 200d
Momentum: RSI(14) 63.8 | MACD 8.714 vs signal 0.171 (histogram 8.542)
Returns: 1d +4.8% | 5d +1.5% | 1m +4.9% | 3m -5.8%
52-week range: 454.95 - 1,014.33 (now 56.5% of the way up)
Volatility: ATR(14) 20.44 (2.7% of price) | annualised 20d 40.9%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 36.12B
Valuation: trailing P/E 58.00 | forward P/E 41.41 | P/B 8.17 | PEG n/a
Profitability: profit margin 7.4% | operating margin 9.6% | ROE 15.2%
Growth (YoY): revenue +15.9% | earnings +34.2%
Balance sheet: debt/equity 19.3% | free cash flow -38.48M
Risk: beta -0.30 | short interest 0.8% of float
Next earnings: 2026-11-24
```

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.10</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 10% | 2026-03-31 beat by 16% | 2025-12-31 beat by 16% | 2025-09-30 beat by 21%
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
Consensus: hold (mean 2.67 on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 802.17 (+4.1% vs last close), range 518.00 - 960.00
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

### Alphabet (Google) (GOOGL) · Company — BULLISH, confidence 0.60

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Fundamentals are strong (low P/E, high margins, high ROE) and analyst consensus is overwhelmingly bullish with a +34% price target. Technicals show oversold conditions (RSI 31.3) that could support a bounce despite the current downtrend. Recent ETF buying adds demand. News is mixed but leans slightly bearish due to price‑drop concerns, which tempers conviction.

**Main reasons it gave:**
- Trailing P/E 16.06 and profit margin 54.8% indicate strong fundamentals
- Analyst consensus strong_buy, mean price target $429 (+34% vs last close)
- RSI 31.3 suggests oversold condition, potential bounce
- ETFs purchased $116M of GOOGL shares, showing institutional buying

<details><summary><b>News</b> — score -0.10</summary>

- [Ahead of Earnings, Is Alphabet Stock a Buy, a Sell, or Fairly Valued?](https://global.morningstar.com/en-nd/stocks/ahead-earnings-is-alphabet-stock-buy-sell-or-fairly-valued-2)  
  <sub>Morningstar, 5 hours ago</sub>  
  Medium. Alphabet Earnings Release Date. Wednesday, Oct. 28, 2026, after the close of trading. What to Watch for in Alphabet's Q3 Earnings.
- [Here’s How Much Traders See Google Parent Alphabet’s Stock Moving After Earnings](https://www.investopedia.com/here-is-how-much-traders-see-google-parent-alphabet-stock-moving-after-earnings-googl-q3-fy2026-12184290)  
  <sub>Investopedia, 59 minutes ago</sub>  
  Google parent Alphabet is due to report earnings after the closing bell Wednesday, with traders expecting a big move from the stock to follow.
- [ETFs Are Buying Alphabet (GOOGL) on Thursday](https://finance.yahoo.com/markets/stocks/articles/etfs-buying-alphabet-googl-thursday-110106286.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  ETFs bought $116.0 million of Alphabet (GOOGL) shares on Thursday.
- [Hyperscaler Earnings Previews: Alphabet, Microsoft And Amazon - Maybe The Bearish Sentiment Will Help](https://www.google.com/goto?url=CAESvgEB6zswFSRF-RTRNl4vC7KJ2_CMnUaw0oI5tTUgksTjcrWikuTHTQWM_SLi0iVazHS3Y-GhqH1G3946Oz9NtMwxfeuD9LIva_13YJiUa414AmHW6WK3M43shU_8tyiNNwbbAoKcvySGnFDOL60jfu82_vChAprPt2XD2uvp_Jje-pVMF4csMbxK3B0ziB4bWAR3p5bq6pOkj3VxWd7_YwTmG4Veq_ylzizNT5Jy_wd-GiEA6XK56iCXYzohyPNK)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  The name of the game for mega-cap tech seems to be about sector capital, free cash flow and capex growth, debt issuance and the ability to raise capital.
- [Microsoft, Alphanet, Amazon Earnings Meet Fed Rate Decision: 3 Charts To Watch This Week](https://www.tradingview.com/news/stocktwits:a13f02de1094b:0-microsoft-alphanet-amazon-earnings-meet-fed-rate-decision-3-charts-to-watch-this-week/)  
  <sub>TradingView, 3 hours ago</sub>  
  Microsoft (MSFT), Alphabet (GOOG, GOOGL) and Amazon (AMZN) are slated to report earnings this week, with investors looking for more clues on where the AI...
- [Alphabet Cl A (GOOGL-Q) Press Releases](https://www.theglobeandmail.com/investing/markets/stocks/GOOGL-Q/pressreleases/)  
  <sub>The Globe and Mail, 2 hours ago</sub>  
  Alphabet GOOGL is set to report third-quarter 2026 results on Oct. 28. For third-quarter 2026, the Zacks Consensus Estimate for earnings is pegged at $2.94...
- [Google Earnings Date: When Does Alphabet Report Earnings? Time, Results History and Stock Reaction](https://www.google.com/goto?url=CAESkAEB6zswFWWrRwJd6gSBAfnREHAu0s1HiBRktfdtjG_oCU82pmLQGE-T9ck9dF_oCRPO_Yio2Sd1t1_rrSuJ0d7nBOs1tahpPqMOD2g-Y96tkTclMTLQB3ur9N-KVc0esR_9AVXFy826hPb9Y2MGPfCnU1hGYZM3A_o2yUa_gMWJj5gldeknfKOx0dYLi-anMdQ)  
  <sub>MEXC, 7 hours ago</sub>  
  Alphabet, Google's parent company, will report its Q3 2026 results (July–September 2026) after the US market closes on Wednesday, October 28, 2026.
- [Google Drops Below $330 to Near Three-Month Low Ahead of Earnings, GOOGL Could Fall Another 15%](https://www.tradingkey.com/analysis/stocks/us-stocks/262239444-google-drops-near-3-month-low-ahead-earnings-tradingkey)  
  <sub>TradingKey, 1 hour ago</sub>  
  TradingKey - Google parent Alphabet (GOOGL) will report its Q3 2026 financial results after the market close on October 28 ET, but its stock price remains...
- [$GOOG, $GOOGL Stock Losses: BFA Law Reminds Alphabet](https://www.globenewswire.com/news-release/2026/10/26/3387895/0/en/goog-googl-stock-losses-bfa-law-reminds-alphabet-investors-with-losses-of-the-ongoing-securities-fraud-class-action-that-alleges-ai-progress-misrepresentations.html)  
  <sub>GlobeNewswire, 5 hours ago</sub>  
  BFA Law Reminds Alphabet Investors with Losses of the Ongoing Securities Fraud Class Action that Alleges AI Progress Misrepresentations...
- [Alphabet (GOOGL) Pushes Google Play Into Cars With Native In Vehicle Integration](https://finance.yahoo.com/technology/ai/articles/alphabet-googl-pushes-google-play-140835659.html)  
  <sub>Yahoo Finance, 34 minutes ago</sub>  
  Alphabet (NasdaqGS: GOOGL) is integrating Google Play directly into XPENG vehicles, extending its software reach into in-car systems.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 320.18 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 341.96 (-6.4%), 50d 342.43 (-6.5%), 200d 341.29 (-6.2%); 50d above 200d
Momentum: RSI(14) 31.3 | MACD -4.918 vs signal -1.604 (histogram -3.314)
Returns: 1d -0.0% | 5d -7.0% | 1m -6.9% | 3m -4.1%
52-week range: 259.92 - 402.62 (now 42.2% of the way up)
Volatility: ATR(14) 8.25 (2.6% of price) | annualised 20d 20.9%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.70</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 3.92T
Valuation: trailing P/E 16.06 | forward P/E 20.85 | P/B 6.29 | PEG 1.12
Profitability: profit margin 54.8% | operating margin 34.0% | ROE 48.7%
Growth (YoY): revenue +24.2% | earnings +294.0%
Balance sheet: debt/equity 18.9% | free cash flow 22.67B
Risk: beta 1.21 | short interest 1.4% of float
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

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

```text
Consensus: strong_buy (mean 1.38 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 13 strong buy, 43 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 429.12 (+34.0% vs last close), range 340.00 - 500.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

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

### Procter & Gamble (PG) · Company — BULLISH, confidence 0.60

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “Buy”, so the main reasons below are all it gave.

**Main reasons it gave:**
- ETFs bought $82.8M of PG (34 ETFs net buyers)
- IRON Financial increased stake by 105.7% in Q3
- PG dividend raised 3% to 2.61% yield
- Price above 20‑day, 50‑day, 200‑day SMAs; RSI 62.1 (bullish technicals)

<details><summary><b>News</b> — score +0.60</summary>

- [ETFs Bought $82.8 Million of Procter & Gamble (PG) on Oct. 22](https://finance.yahoo.com/markets/stocks/articles/etfs-bought-82-8-million-110138645.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  Thirty-four ETFs bought Procter & Gamble shares versus 15 that sold on Thursday.
- [PG vs. CL: Which Household Giant Deserves Your Retirement Dollars?](https://247wallst.com/investing/2026/10/26/pg-vs-cl-which-household-giant-deserves-your-retirement-dollars/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  P&G yields 2.61% and raised its quarterly dividend 3%, outpacing Colgate's 2.15% yield and 1.9% raise. P&G has paid dividends for 136 straight years and...
- [Health Care CEO Paul Gama sells 4,331 Procter & Gamble (PG) shares at $161.27.](https://www.stocktitan.net/sec-filings/PG/form-4-procter-gamble-co-insider-trading-activity-6fcc305e10bb.html)  
  <sub>Stock Titan, 45 minutes ago</sub>  
  After the October 23, 2026 sale, Gama held 46793 shares directly and 1184 through the Retirement Plan Trustee. No Rule 10b5-1 plan is reported.
- [Procter & Gamble CEO- Health Care Sold Shares Worth Over $698K](https://www.tradingview.com/news/tradingview:2ad7f8bb8439b:0-procter-gamble-ceo-health-care-sold-shares-worth-over-698k/)  
  <sub>TradingView, 37 minutes ago</sub>  
  Gama Paul, an officer with the title CEO- Health Care, sold 4331 shares of Procter & Gamble common stock at $161.27 per share for $698460.
- [Procter & Gamble Company (The) $PG Stock: IRON Financial LLC Raises Stake](https://www.marketbeat.com/instant-alerts/filing-procter-gamble-company-the-pg-stock-iron-financial-llc-raises-stake-2026-10-26/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  IRON Financial LLC increased its stake in Procter & Gamble Company (The) (NYSE:PG - Free Report) by 105.7% during the 3rd quarter, according to its most...
- [Is This Safe-Haven Stock Overvalued? The Hidden Risk Facing Colgate-Palmolive on Oct. 30](https://247wallst.com/investing/2026/10/26/is-this-safe-haven-stock-overvalued-the-hidden-risk-facing-colgate-palmolive-on-oct-30/)  
  <sub>24/7 Wall St., 42 minutes ago</sub>  
  CL has surged 21.87% year to date but now trades at ~24x 2026 EPS. That is a demanding multiple for a company guiding just 1% to 4% organic growth.
- [Take the Zacks Approach to Beat the Markets: Honda Motor, Accenture, CACI in Focus](https://www.tradingview.com/news/zacks:721dfa30d094b:0-take-the-zacks-approach-to-beat-the-markets-honda-motor-accenture-caci-in-focus/)  
  <sub>TradingView, 4 hours ago</sub>  
  The three benchmark Wall Street indexes delivered mixed performance for the week ended October 23. The tech-focused Nasdaq Composite fell 0.7%, while the...
- [2 Safe S&P 500 Dividend Stocks Boomers Can Buy and Hold Forever](https://247wallst.com/investing/2026/10/26/2-safe-sp-500-dividend-stocks-boomers-can-buy-and-hold-forever/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  One of these household-name S&P 500 stocks has raised its dividend every single year for seven decades, and both pay their checks from cash left over after...
- [PG Oct 2026 157.500 put (PG261030P00157500) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/PG261030P00157500/)  
  <sub>Yahoo! Finance Canada, 12 hours ago</sub>  
  Find the latest PG Oct 2026 157.500 put (PG261030P00157500) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.30</summary>

```text
Last close 160.28 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 153.32 (+4.5%), 50d 148.68 (+7.8%), 200d 148.61 (+7.9%); 50d above 200d
Momentum: RSI(14) 62.1 | MACD 3.860 vs signal 3.077 (histogram 0.783)
Returns: 1d -0.5% | 5d +1.6% | 1m +9.6% | 3m +7.7%
52-week range: 138.04 - 167.20 (now 76.3% of the way up)
Volatility: ATR(14) 3.06 (1.9% of price) | annualised 20d 28.8%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 371.49B
Valuation: trailing P/E 24.14 | forward P/E 21.71 | P/B 6.84 | PEG 4.14
Profitability: profit margin 18.2% | operating margin 27.1% | ROE 29.6%
Growth (YoY): revenue +4.0% | earnings +0.8%
Balance sheet: debt/equity 70.3% | free cash flow 12.66B
Risk: beta 0.38 | short interest 1.1% of float
Next earnings: 2027-01-21
```

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.20</summary>

```text
Earnings record, last 4 quarters: 1 beat, 3 in line
  2026-09-30 beat by 3% | 2026-06-30 in line | 2026-06-30 in line | 2026-03-31 in line
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: buy (mean 2.08 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 5 strong buy, 9 buy, 11 hold, 0 sell, 0 strong sell
Price target: mean 172.35 (+7.5% vs last close), range 143.00 - 190.00
Recent rating changes:
  - 2026-10-26 Piper Sandler: main, Neutral -> Neutral
  - 2026-10-23 Freedom Broker: up, Hold -> Buy
  - 2026-10-23 UBS: main, Buy -> Buy
  - 2026-10-23 Citigroup: main, Buy -> Buy
  - 2026-10-23 BNP Paribas: main, Outperform -> Outperform
  - 2026-10-23 JP Morgan: main, Overweight -> Overweight
Institutional ownership: 71.9%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.4%), Geode Capital Management, LLC (2.9%), Vanguard Portfolio Management LLC (2.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 156,293 shares in 42 transaction(s) | sold 48,751 shares in 16
Net: +107,542 shares (+5.3% of insider holdings) | insiders hold 2,155,538 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-10-05 WHALEY SUSAN STREET (Officer): 2,369 shares, 344.31K
  - 2026-10-05 GAMA PAUL (Officer): 2,225 shares, 323.38K
  - 2026-10-05 SCHULTEN ANDRE (Chief Financial Officer): 3,914 shares, 568.86K
  - 2026-08-24 JANZARUK MATTHEW W. (Officer): 359 shares, 52.14K
(40 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

> The news includes a ticker‑specific catalyst (humanoid robot testing) and a bullish target price, technicals show modest upside despite thin volume, fundamentals are cheap on valuation though leveraged, analyst consensus remains bullish with a sizable price‑target upside, insiders show no activity, and the company has a strong earnings‑beat record. These independent dimensions align toward a positive short‑term move.

**Main reasons it gave:**
- Toyota testing humanoid robots in factories (ticker‑specific catalyst)
- Barron's target price $236.88 implies ~19% upside vs current $198.95
- Four consecutive earnings beats indicate strong earnings momentum
- Trailing P/E 8.74 suggests cheap valuation relative to peers
- Thin trading volume (0.16x 20‑day average) tempers technical bullishness

<details><summary><b>News</b> — score +0.50</summary>

- [Toyota and Honda test humanoid robots in Japanese factories (TM:NYSE)](https://seekingalpha.com/news/4657066-toyota-and-honda-test-humanoid-robots-in-japanese-factories)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Toyota Motor (TM) and Honda Motor (HMC) are testing humanoid robots in Japanese factories on tasks ranging from wire harness installation to final...
- [Gentex Stock After Q3 Earnings: Buy, Hold or Sell the Stock?](https://finance.yahoo.com/markets/stocks/articles/gentex-stock-q3-earnings-buy-123100155.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Gentex Corporation GNTX is leveraging advanced automotive technologies, product diversification and new customer programs to drive growth and strengthen...
- [US Demand For EVs May Be Gone Forever](https://247wallst.com/investing/2026/10/26/us-demand-for-evs-may-be-gone-forever/)  
  <sub>24/7 Wall St., 38 minutes ago</sub>  
  EV sales in the US fell 30% through the first three quarters of this year. Meanwhile, several manufacturers walked away from EV production altogether,...
- [Buy, Hold or Sell Ford Stock Before Q3 Earnings Release?](https://finance.yahoo.com/markets/stocks/articles/buy-hold-sell-ford-stock-124300966.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Ford F is slated to release third-quarter 2026 results on Oct. 28, after the closing bell. The Zacks Consensus Estimate for the to-be-reported quarter's EPS...
- [BYD Has Already Lapped Tesla — Now It Says Toyota Is Next And US Market Doesn't Matter](https://stocktwits.com/news-articles/markets/equity/byd-tesla-toyota-next-us-market-dont-matter/cZZ2Dc3R7A9)  
  <sub>Stocktwits, 21 hours ago</sub>  
  BYD's European market share more than doubled to 2.8% in May, surpassing Ford, Tesla and Nissan.
- [Audi CEO Defends 200,000-SUV Georgia Plant Announced By Trump: 'If the American President Invites You...'](https://www.benzinga.com/markets/tech/26/10/62583283/audi-ceo-defends-200000-suv-georgia-plant-announced-by-trump-if-the-american-president-invites-you)  
  <sub>Benzinga, 5 hours ago</sub>  
  Audi CEO defends a planned 200000-unit U.S. facility, while officials warn expansion must not come at the expense of German jobs.
- [When (RMAX) Moves Investors should Listen (RMAX:CA)](https://news.stocktradersdaily.com/canada/when-rmax-moves-investors-should-listen_20261026_e99784)  
  <sub>Stock Traders Daily, 4 hours ago</sub>  
  Check the time stamp on this data. Updated Proprietary Signals for Hamilton REITs YIELD MAXIMIZER TM ETF (RMAX:CA) available here.
- [3 Foreign Auto Stocks to Buy as Hybrids and EVs Gain Momentum](https://finance.yahoo.com/markets/stocks/articles/3-foreign-auto-stocks-buy-122200370.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  As the foreign auto industry faces uneven demand, Toyota, Honda and Polestar stand out for their hybrid and EV strengths.
- [Form 4 TOYOTA MOTOR CORP/: Masashi Asakura (Senior Fellow) For: 25 September](https://in.investing.com/news/stock-market-news/form-4-toyota-motor-corp-masashi-asakura-senior-fellow-for-25-september-93CH-5653024)  
  <sub>Investing.com India, 14 hours ago</sub>  
  FORM 4, UNITED STATES SECURITIES AND EXCHANGE COMMISSION Washington, D.C. 20549. STATEMENT OF CHANGES IN BENEFICIAL OWNERSHIP
- [Barron's cites USD 236.88 target for Toyota Motor stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/barron-s-cites-usd-236-88-target-for-toyota-motor-stock/70415077)  
  <sub>ad-hoc-news.de, 5 minutes ago</sub>  
  Toyota reports second-quarter results on November 5, 2026. Toyota Motor stock costs EUR 178.00 on October 26, 2026 and its NYSE price is USD 198.82.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.30</summary>

```text
Last close 198.95 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 189.33 (+5.1%), 50d 191.63 (+3.8%), 200d 199.34 (-0.2%); 50d below 200d
Momentum: RSI(14) 63.7 | MACD 2.193 vs signal 0.823 (histogram 1.369)
Returns: 1d +1.1% | 5d +2.5% | 1m +4.5% | 3m +6.8%
52-week range: 166.50 - 248.29 (now 39.7% of the way up)
Volatility: ATR(14) 3.09 (1.6% of price) | annualised 20d 19.5%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 234.33B
Valuation: trailing P/E 8.74 | forward P/E 12.61 | P/B 15.98 | PEG n/a
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

```text
Consensus: none (mean n/a on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 2 strong buy, 2 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 234.08 (+17.7% vs last close), range 230.00 - 239.31
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

### Caterpillar (CAT) · Company — BULLISH, confidence 0.58

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Fundamentals are strong (high margins, solid growth, reasonable forward P/E) and earnings record shows four straight beats, while analyst consensus is strongly buy with a high price target. News is mixed but net slightly bullish due to institutional buying and a large backlog, despite a UBS target cut. Technicals are bearish (price below all SMAs, low RSI, thin volume) which tempers conviction. Insider activity is neutral. Overall view leans bullish with moderate conviction.

**Main reasons it gave:**
- UBS cut CAT price target to $750, citing valuation concerns (news)
- UniSuper added 44,390 CAT shares to its portfolio (news)
- Backlog of $72B with 59% expected to ship within 12 months (news)
- RSI 27 (oversold) and price below 20/50/200 SMA (technical)
- Four consecutive earnings beats (earnings record)

<details><summary><b>News</b> — score +0.20</summary>

- [Red Cat Holdings, Inc. (RCAT) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/RCAT/latest-news/)  
  <sub>Yahoo Finance UK, 6 hours ago</sub>  
  Red Cat Holdings, Inc. (RCAT).
- [UBS cuts Caterpillar stock price target on valuation concerns](https://www.investing.com/news/analyst-ratings/ubs-cuts-caterpillar-stock-price-target-on-valuation-concerns-93CH-4971903)  
  <sub>Investing.com, 4 hours ago</sub>  
  Investing.com - UBS lowered its price target on Caterpillar Inc. (NYSE:CAT) to $750 from $825 while keeping a Neutral rating on the stock.
- [CAT Stock Analysis: What to Know](https://journalarta.com/en/2026/10/26/cat-stock-analysis-drops-2-42-rsi-oversold/)  
  <sub>JournalArta, 7 hours ago</sub>  
  On October 23, 2026: price 687.00 USD, trend downtrend, RSI 26.7, support 687.00, resistance 863.44. technical analysis of cat stock. CAT Stock Analysis...
- [Fund Update: 44,390 CATERPILLAR (CAT) shares added to UniSuper Management Pty Ltd portfolio](https://www.quiverquant.com/news/Fund+Update%3A+44%2C390+CATERPILLAR++%28CAT%29+shares+added+to+UniSuper+Management+Pty+Ltd+portfolio)  
  <sub>Quiver Quantitative, 3 hours ago</sub>  
  UniSuper Management Pty Ltd has added 44390 shares of $CAT to their portfolio, per a new SEC 13F fi.
- [Can Caterpillar’s $72B Backlog Save Its Stock From a 10% Slump?](https://247wallst.com/investing/2026/10/25/can-caterpillars-72b-backlog-save-its-stock-from-a-10-slump/)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  CAT's $72 billion backlog, with 59% expected to ship within 12 months, anchors the bull case after shares fell 15% over the past month.
- [1 of Wall Street’s favorite stocks worth investigating and 2 we find risky](https://www.theglobeandmail.com/investing/markets/stocks/CAT/pressreleases/8449496/1-of-wall-streets-favorite-stocks-worth-investigating-and-2-we-find-risky/)  
  <sub>The Globe and Mail, 10 hours ago</sub>  
  Detailed price information for Caterpillar Inc (CAT-N) from The Globe and Mail including charting and trades.
- [Toromont Industries Ltd. (TIH.TO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TIH.TO/)  
  <sub>Yahoo! Finance Canada, 10 hours ago</sub>  
  Find the latest Toromont Industries Ltd. (TIH.TO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [IONS Stock Heads Toward Biggest Single-Day Slump In Over 5 Years – Retail Calls It ‘Opportunity Of A Lifetime’](https://stocktwits.com/news-articles/markets/equity/ions-stock-crashes-ionis-astrazeneca-heart-disease-trial-misses-primary-endpoint/cZmovhVR7nR)  
  <sub>Stocktwits, 21 hours ago</sub>  
  Shares of Ionis Pharmaceuticals (IONS) crashed more than 20% in pre-market trading on Thursday, tracking their lowest levels in seven months,...
- [Caterpillar (CAT) Turns The Page In Resource Industries As Denise Johnson Retires](https://simplywall.st/stocks/us/capital-goods/nyse-cat/caterpillar/news/caterpillar-cat-turns-the-page-in-resource-industries-as-den)  
  <sub>Simply Wall Street, 19 hours ago</sub>  
  Caterpillar (NYSE:CAT) announced that Resource Industries group president Denise Johnson will retire after a long tenure with the company.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 687.72 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 774.44 (-11.2%), 50d 796.36 (-13.6%), 200d 809.02 (-15.0%); 50d below 200d
Momentum: RSI(14) 27.0 | MACD -31.656 vs signal -22.027 (histogram -9.629)
Returns: 1d +0.1% | 5d -5.2% | 1m -16.3% | 3m -18.2%
52-week range: 522.73 - 1,064.90 (now 30.4% of the way up)
Volatility: ATR(14) 26.26 (3.8% of price) | annualised 20d 36.2%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 316.13B
Valuation: trailing P/E 29.60 | forward P/E 21.11 | P/B 16.30 | PEG 1.20
Profitability: profit margin 14.5% | operating margin 22.2% | ROE 57.0%
Growth (YoY): revenue +24.0% | earnings +68.2%
Balance sheet: debt/equity 232.8% | free cash flow 5.05B
Risk: beta 1.58 | short interest 1.9% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.40</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 31% | 2026-03-31 beat by 19% | 2025-12-31 beat by 9% | 2025-09-30 beat by 8%
```

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

```text
Consensus: buy (mean 2.00 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 1 strong buy, 15 buy, 12 hold, 1 sell, 0 strong sell
Price target: mean 945.76 (+37.5% vs last close), range 575.00 - 1,155.00
Recent rating changes:
  - 2026-10-26 Wells Fargo: main, Overweight -> Overweight
  - 2026-10-14 Oppenheimer: main, Outperform -> Outperform
  - 2026-10-12 Citigroup: main, Buy -> Buy
  - 2026-10-05 Truist Securities: main, Buy -> Buy
  - 2026-09-10 Freedom Broker: up, Hold -> Buy
  - 2026-08-11 Evercore ISI Group: main, Outperform -> Outperform
Institutional ownership: 73.5%
Largest holders: Blackrock Inc. (8.3%), State Street Corporation (7.5%), Vanguard Capital Management LLC (6.5%), State Farm Mutual Automobile Insurance Co (3.2%), Vanguard Portfolio Management LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

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

### Teva Pharmaceutical (TEVA) · Company — NEUTRAL, confidence 0.45

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> mixed signals: bullish analyst consensus (+20% target) and positive earnings record offset by negative news (Zacks downgrade) and bearish technicals (MACD below signal, low volume); fundamentals are mixed with high trailing P/E but low forward P/E and strong cash flow.

**Main reasons it gave:**
- Zacks downgrade to Strong Sell (negative news)
- Technical MACD below signal and low volume (bearish technical)
- Analyst consensus strong buy with mean target $47.58 (+20% upside) (bullish analyst)
- High trailing P/E 65.86 and debt/equity 217.8% (mixed fundamentals)
- 3 beats and 1 miss in last 4 quarters (positive earnings record)

<details><summary><b>News</b> — score -0.30</summary>

- [What's Shifting and What's Staying the Same](https://www.pharmexec.com/shorts/what-shifting-staying-same)  
  <sub>Pharmaceutical Executive, 5 hours ago</sub>  
  This week on Market Movers Rx, we break down the key stock movers on the week, from gains at Carl Zeiss Meditec and Moderna to declines for Humana and Teva...
- [Is Teva Pharmaceutical Industries (TEVA) Still Undervalued Following Its Recent Pullback?](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-teva/teva-pharmaceutical-industries/news/is-teva-pharmaceutical-industries-teva-still-undervalued-fol)  
  <sub>Simply Wall Street, 2 hours ago</sub>  
  Teva Pharmaceutical Industries Stock Moves Set Against Recent Performance Teva Pharmaceutical Industries (NYSE:TEVA) has drawn fresh attention after a mixed...
- [Baron Health Care Fund Q3 2026 Top Contributors And Detractors](https://seekingalpha.com/article/4957408-baron-health-care-fund-q3-2026-top-contributors-and-detractors)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  TMO's organic growth of 5% exceeded consensus by 200 basis points, and management raised full-year organic growth guidance/. MTD's local-currency sales grew...
- [Zacks downgrades Teva stock to Strong Sell below yearly high](https://www.ad-hoc-news.de/boerse/news/corporate-news/zacks-downgrades-teva-stock-to-strong-sell-below-yearly-high/70415017)  
  <sub>ad-hoc-news.de, 14 minutes ago</sub>  
  Second-quarter revenue reached USD 4.15 billion, up 4.01 percent. Teva stock was USD 39.72 on October 26, 2026, up 0.79 percent from USD 39.41.
- [TEVA270319C00025000 interactive stock chart | TEVA Mar 2027 25.000 call stock - Yahoo Finance](https://sg.finance.yahoo.com/chart/TEVA270319C00025000/)  
  <sub>Yahoo Finance Singapore, 12 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [JPMorgan Chase & Co. Upgrades Dr. Reddy's Laboratories (NYSE:RDY) to Neutral](https://www.marketbeat.com/instant-alerts/analyst-jpmorgan-chase-co-upgrades-dr-reddys-laboratories-nyse-rdy-to-neutral-2026-10-26/)  
  <sub>MarketBeat, 2 hours ago</sub>  
  JPMorgan Chase & Co. upgraded Dr. Reddy's Laboratories from an "underweight" rating to a "neutral" rating in a report on Monday.
- [ASTS Slides 13% On SpaceX 800 MHz Deal, But CEO Says Carriers Already Hold 1,000 MHz For Its Satellites](https://stocktwits.com/news-articles/markets/equity/asts-slides-13-on-space-x-800-m-hz-deal-but-ceo-says-carriers-already-hold-1-000-m-hz-for-its-satellites/cZD6CRCRBnS)  
  <sub>Stocktwits, 21 hours ago</sub>  
  ASTS CEO Abel Avellan said in a post on X that American operators hold about 1000 MHz of low- and mid-band spectrum that can be tuned onto the AST network.
- [Piper Sandler sets USD 44.00 target for Teva stock ahead of results](https://www.ad-hoc-news.de/boerse/news/corporate-news/piper-sandler-sets-usd-44-00-target-for-teva-stock-ahead-of-results/70413103)  
  <sub>ad-hoc-news.de, 6 hours ago</sub>  
  Teva posted USD 4.14 billion revenue and a USD 576.00 million loss in the second quarter. Teva stock last stood at USD 39.41 on October 23, 2026.
- [Dr. Reddy's Laboratories Ltd (NYSE:RDY) Stock Has Consensus Target Price of $492.90](https://www.marketbeat.com/instant-alerts/consensus-dr-reddys-laboratories-ltd-nyse-rdy-stock-has-consensus-target-price-of-49290-2026-10-25/)  
  <sub>MarketBeat, 16 hours ago</sub>  
  Dr. Reddy's Laboratories Ltd (NYSE:RDY - Get Free Report) has earned an average recommendation of "Hold" from the five analysts that are presently covering...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 39.51 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 40.21 (-1.7%), 50d 38.74 (+2.0%), 200d 34.41 (+14.8%); 50d above 200d
Momentum: RSI(14) 47.8 | MACD 0.438 vs signal 0.685 (histogram -0.247)
Returns: 1d +0.3% | 5d -4.3% | 1m +0.8% | 3m +24.8%
52-week range: 18.95 - 41.50 (now 91.2% of the way up)
Volatility: ATR(14) 1.09 (2.8% of price) | annualised 20d 23.4%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 46.09B
Valuation: trailing P/E 65.86 | forward P/E 12.80 | P/B 5.94 | PEG 0.71
Profitability: profit margin 4.1% | operating margin 4.0% | ROE 9.7%
Growth (YoY): revenue -0.8% | earnings n/a
Balance sheet: debt/equity 217.8% | free cash flow 2.22B
Risk: beta 0.82 | short interest 2.6% of float
Next earnings: 2026-11-03
```

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.15</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-06-30 missed by 92% | 2026-03-31 beat by 9% | 2025-12-31 beat by 39% | 2025-09-30 beat by 17%
```

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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

```text
Consensus: strong_buy (mean 1.46 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 4 strong buy, 8 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 47.58 (+20.4% vs last close), range 42.00 - 55.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

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

### ASML (ASML) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [ASML reports transactions under its current share buyback program](https://www.google.com/goto?url=CAESowEB6zswFVyRPPNy07nlatkqir6Ojat1Acfj-nNKoNrdiA2XTnx9Ob-T2Sp25KqdlOEVEKt7_tcpvTIbNCoL9hNirEqjkLcIa5QS_rn4a6_aN71nx7o00D1z-yz2NNyvhUCg6chi51i89zLQkbuUq4lJmmoQybT5zwqjX2IUKIpmlHzZ0bKIivPFMr4veoagXN8CQEjvebfnrIAoc0_gfbLEBkES)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  ASML reports transactions under its current share buyback program VELDHOVEN, the Netherlands – ASML Holding N.V. (ASML) reports the following transactions,...
- [4 Stocks This Top Fidelity Manager Likes as the US Market Gets More Expensive](https://global.morningstar.com/en-nd/stocks/4-stocks-this-top-fidelity-manager-likes-us-market-gets-more-expensive)  
  <sub>Morningstar, 8 hours ago</sub>  
  Key Takeaways. The valuation gap between US and European stocks is creating significant buying opportunities, says Fidelity's Marcel Stötzel. ASML...
- [Here’s How Much Traders See Microsoft Stock Moving After Earnings](https://www.google.com/goto?url=CAESsgEB6zswFRzTOsuYYjxkYjuGwY4WG0mXqF1PmssbcJQUlXaX55zZk5yXj2UAY7dHhijmaILi2fyM_Z5OSg0OcMTcdluQ3mQ4r2KW_y2BLoz9nhYJHzF_y9uqsz9PrVzoKWvBTeijsPjM2UKtlqsjK-egsamCD8Xq6F3Vv2KXvpm-Ud5c78MG3S-42mt8yQ59JokZvTfC2Pvqg7C6Ktz7933pko2Xh1_UjcDLgEjHksuW4exM)  
  <sub>Investopedia, 2 hours ago</sub>  
  Microsoft is set to report earnings Wednesday afternoon, with traders expecting a move that could bring the stock back near its recent record.
- [ASML Holding To Go Ex-Dividend On October 27th, 2026 With 2.10767 USD Dividend Per Share](https://www.moomoo.com/news/post/1002298189/asml-holding-to-go-ex-dividend-on-october-27th-2026)  
  <sub>Moomoo, 7 hours ago</sub>  
  October25th (Eastern Time) - $ASML Holding(ASML.US)$ is trading ex-dividend on October 27th, 2026.Shareholders of record on October 27th, 2026 will receive...
- [ASML (ASML) Q2 2026 Earnings Preview: $7.94 EPS Expected, 8% Options Swing; Triangle at $1,800](https://www.tradingkey.com/analysis/stocks/us-stocks/262030125-asml-q2-2026-earnings-preview-eps-triangle-breakout-1800-tradingkey)  
  <sub>TradingKey, 20 hours ago</sub>  
  ASML reports Q2 2026 earnings this morning. Consensus: EPS $7.94, revenue $10.27B. Options pricing an 8.36% swing either way. The stock has pulled back 11%...
- [ASML Q3 Earnings Crush 2025 Levels as AI Demand Drives €11.7 Billion Revenue](https://cryptorank.io/news/feed/4a189-asml-q3-earnings-crush-2025-levels-as-ai-demand-drives-117-billion-revenue)  
  <sub>CryptoRank, 15 hours ago</sub>  
  ASML reported €11.7 billion in Q3 revenue and nearly €5 billion in profit as AI demand surged.
- [ASML Oct 2026 1465.000 call (ASML261030C01465000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScgHrOzAVdohlYXkbQukq70FN2ajrnQuYG0iN16JnkucJzq5RiOLmHwob8hz2_sn6NeWwHrcnychUpYHYhQ5xwcMdOPM4lTQY_ihKXz1t_uuBGz_HMmBxsa8RjjRmdgnUZBXtycDyQinq2Y-cRICTGus__Q)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  Find the latest ASML Oct 2026 1465.000 call (ASML261030C01465000) stock quote, history, news and other vital information to help you with your stock trading...
- [What ASML Holders Bought Into](https://simplywall.st/stocks/nl/semiconductors/ams-asml/asml-holding-shares/news/what-asml-holders-bought-into)  
  <sub>Simply Wall Street, 17 hours ago</sub>  
  If you looked at ASML a year ago, you saw the only EUV supplier positioned between a bullish camp arguing for accelerating AI-driven tool demand and a...
- [Why ASML is a buy After Terafab Deal?](https://www.google.com/goto?url=CAESqgEB6zswFfUPN923AHThcE5yIZK3zv218QQK_bMkMmwdhp792i8Q4NekdMMl_INJ7i6Pm1e4HA8gC1gWyfrGztg9q-rWOMbObt_yr17Vfl37EurAvVR5oEmL-pO5EWUwZ6cRKCAyJ4iJyjUXdP2lp-Q1J4ikMd1ttEpYrRvaogLD3sG90m6Vcu579yrga9qZAyG_IRdW_l1bbUbz3jepNudVfplFen6nayHEQA)  
  <sub>TradingKey, 24 hours ago</sub>  
  TradingKey - The CEO of Tesla and SpaceX, Elon Musk, has revealed his intent to work with ASML Holdings NV (NASDAQ: ASML) in the production of chips for...
- [ASML Jun 2028 900.000 call (ASML280616C00900000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/ASML280616C00900000/)  
  <sub>Yahoo Finance UK, 15 hours ago</sub>  
  Find the latest ASML Jun 2028 900.000 call (ASML280616C00900000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,598.09 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 1,723.65 (-7.3%), 50d 1,717.81 (-7.0%), 200d 1,590.01 (+0.5%); 50d above 200d
Momentum: RSI(14) 39.0 | MACD -39.725 vs signal -21.059 (histogram -18.666)
Returns: 1d +1.7% | 5d -3.0% | 1m -8.4% | 3m +1.0%
52-week range: 966.57 - 1,989.44 (now 61.7% of the way up)
Volatility: ATR(14) 54.16 (3.4% of price) | annualised 20d 38.6%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 615.92B
Valuation: trailing P/E 39.32 | forward P/E 25.43 | P/B 1,372.16 | PEG 0.89
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
Price target: mean 2,145.62 (+34.3% vs last close), range 865.47 - 2,843.01
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

### HDFC Bank (HDB) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Employee stock options at HDFC Bank (HDB) carry a Rs. 692.80 grant price and vest in four stages.](https://www.stocktitan.net/sec-filings/HDB/6-k-hdfc-bank-ltd-current-report-foreign-issuer-c6ebcb2d0654.html)  
  <sub>Stock Titan, 4 hours ago</sub>  
  HDFC Bank (HDB), through its Governance, Nomination and Remuneration Committee, granted 1,302,379 equity stock options on October 24, 2026, under Employees'...
- [Stock market on October 26th: Market leans towards red, VN-Index falls more than 10 points.](https://www.vietnam.vn/en/chung-khoan-ngay-26-10-thi-truong-nghieng-ve-sac-do-vn-index-giam-hon-10-diem)  
  <sub>Vietnam.vn, 5 hours ago</sub>  
  On October 26th, the Vietnamese stock market was shrouded in red as selling pressure intensified across the board, primarily in the banking and securities...
- [Hidden value: Why SGX consumer stocks deserve a closer look](https://www.businesstimes.com.sg/companies-markets/uncovering-the-singapore-bourse/hidden-value-why-sgx-consumer-stocks-deserve-closer-look)  
  <sub>The Business Times, 16 hours ago</sub>  
  Fund money is quietly moving from the consumer names everyone knows to the ones they have overlooked Read more at The Business Times.
- [HDB Financial Services seeks shareholder nod for Jimmy Tata, director re-appointments](https://scanx.trade/stock-market-news/companies/hdb-financial-services-appoints-jimmy-tata-renews-two-independent/54226532)  
  <sub>scanx.trade, 3 hours ago</sub>  
  HDB Financial Services issued a postal ballot notice on October 22, 2026, for director appointments. Remote e-voting for shareholders runs from October 28,...
- [HDB stock pre-market at EUR 19.80: Indian bank before the Xetra open](https://www.ad-hoc-news.de/boerse/news/vorboerse/hdb-stock-pre-market-at-eur-19-80-indian-bank-before-the-xetra-open/70412098)  
  <sub>ad-hoc-news.de, 8 hours ago</sub>  
  The Indian bank provides services to individual and corporate clients in four markets. At Lang & Schwarz the stock trades pre-market at EUR 19.80 on October...
- [Stock market on October 26: VN-Index loses more than 10 points, profit-taking pressure increases.](https://www.vietnam.vn/en/chung-khoan-26-10-vn-index-mat-hon-10-diem-ap-luc-chot-loi-gia-tang)  
  <sub>Vietnam.vn, 4 hours ago</sub>  
  The VN-Index fell 10.6 points on October 26th, dropping to 1763.55 points as selling pressure intensified in the banking, technology, and many large-cap...
- [Citi cuts HDFC Bank target from INR 970 to INR 880 for HDFC Bank stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/citi-cuts-hdfc-bank-target-from-inr-970-to-inr-880-for-hdfc-bank-stock/70414995)  
  <sub>ad-hoc-news.de, 16 minutes ago</sub>  
  Second-quarter profit rose 4.7 percent to INR 195.10 billion on October 17, 2026. HDFC Bank stock costs EUR 19.55 on October 26, 2026.
- [Bajaj Finance, Bajaj Housing Finance, Jio Finance Share Latest News, Bajaj Finserv, Share Anelysis Severe Thunderstorm Warning (wey0tSAASd)](https://media.unisba.ac.id/ae6b80b1/d9242cb3PQ4wOjsdTRc-Xjs)  
  <sub>Unisba Media, 20 hours ago</sub>  
  bajaj finance, bajaj housing finance, jio finance share latest news, bajaj finserv, share anelysis. Topics Covered. jio finance. jio finance share.
- [Financial stocks plummeted, VN-Index loses more than 10 points.](https://www.vietnam.vn/en/co-phieu-tai-chinh-giam-sau-vn-index-mat-hon-10-diem)  
  <sub>Vietnam.vn, 4 hours ago</sub>  
  The VN-Index plunged into the red on October 26th, losing more than 10 points to near the 1763 mark under strong selling pressure. Financial stocks fell...
- [Citi cuts target for HDFC Bank stock from INR 970 to INR 880](https://www.ad-hoc-news.de/boerse/news/corporate-news/citi-cuts-target-for-hdfc-bank-stock-from-inr-970-to-inr-880/70413053)  
  <sub>ad-hoc-news.de, 7 hours ago</sub>  
  HDFC Bank stock trades at EUR 19.70 on October 26, 2026. Second-quarter profit rose 4.7 percent year over year to INR 195.1 billion.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 21.81 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 22.59 (-3.5%), 50d 22.82 (-4.4%), 200d 26.04 (-16.3%); 50d below 200d
Momentum: RSI(14) 40.1 | MACD -0.122 vs signal -0.053 (histogram -0.069)
Returns: 1d -1.3% | 5d -5.5% | 1m -5.2% | 3m -7.5%
52-week range: 21.81 - 37.13 (now 0.0% of the way up)
Volatility: ATR(14) 0.54 (2.5% of price) | annualised 20d 28.7%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 112.13B
Valuation: trailing P/E 14.07 | forward P/E 15.78 | P/B 8.68 | PEG n/a
Profitability: profit margin 26.5% | operating margin 38.5% | ROE 11.0%
Growth (YoY): revenue +80.8% | earnings +21.3%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.41 | short interest 0.7% of float
Next earnings: 2027-01-16
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
Price target: mean 30.30 (+39.0% vs last close), range 26.20 - 33.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 0 shares
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

- [JPMorgan (JPM) Stock Could Be 33% Undervalued Following JPM Coin Expansion](https://finance.yahoo.com/markets/stocks/articles/jpmorgan-jpm-stock-could-33-140811654.html)  
  <sub>Yahoo Finance, 34 minutes ago</sub>  
  JPMorgan Chase has turned heads with a very strong 157.1% share price gain over the past three years, and the core question now is whether the returns it...
- [Can French stocks rebound despite persistent political risks? JPM weighs in](https://ng.investing.com/news/stock-market-news/can-french-stocks-rebound-despite-persistent-political-risks-jpm-weighs-in-2756844)  
  <sub>Investing.com Nigeria, 4 hours ago</sub>  
  Investing.com -- France's political backdrop remains "challenging" ahead of next year's elections, JPMorgan strategists say, but they argue investor...
- [Is JPMorgan Chase (JPM) Undervalued As Bond Issuance And Earnings Strength Meet A Pullback?](https://simplywall.st/stocks/us/banks/nyse-jpm/jpmorgan-chase/news/is-jpmorgan-chase-jpm-undervalued-as-bond-issuance-and-earni)  
  <sub>Simply Wall Street, 2 hours ago</sub>  
  JPMorgan Chase (JPM) has been active in the bond market in October 2026, issuing a series of fixed and floating rate notes with maturities extending to 2056...
- [Vest Financial LLC Buys 21,084 Shares of JPMorgan Chase & Co. $JPM](https://www.marketbeat.com/instant-alerts/filing-vest-financial-llc-buys-21084-shares-of-jpmorgan-chase-co-jpm-2026-10-26/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Vest Financial LLC boosted its stake in JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 8.3% in the third quarter, according to the company in its most...
- [J P Morgan Chase & Co Depositary Shares, each representing a 1/400th interest in a share of 4.55% Non-Cumulative Preferred Stock, Series JJ Estimates – BOATS:JPM/PK](https://www.tradingview.com/symbols/BOATS-JPM/PK/financials-estimates/?category=cash_flow)  
  <sub>TradingView, 18 hours ago</sub>  
  See how J P Morgan Chase & Co Depositary Shares, each representing a 1/400th interest in a share of 4.55% Non-Cumulative Preferred Stock,...
- [Chase cardholders can now invest Ultimate Rewar...](https://pluang.com/en/news-feed/jp-morgan-investasi-poin-chase)  
  <sub>Pluang, 2 hours ago</sub>  
  Chase has introduced a new feature allowing cardholders with eligible Chase Ultimate Rewards cards to redeem points as cash directly into J.P. Morgan...
- [Buybacks reach 88M shares at Prudential (PUK), which intends to cancel the repurchased shares.](https://www.stocktitan.net/sec-filings/PUK/6-k-prudential-plc-current-report-foreign-issuer-8143c005329f.html)  
  <sub>Stock Titan, 4 hours ago</sub>  
  Prudential plc (PUK) purchased ordinary shares from JP Morgan Securities plc under arrangements announced on January 6, 2026 and September 2, 2026,...
- [ETFs Bought $64.3 Million of JPMorgan (JPM) on Oct. 22](https://finance.yahoo.com/markets/stocks/articles/etfs-bought-64-3-million-110155404.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  38 ETFs bought JPMorgan shares versus 10 that sold, for a net inflow of $64.3 million.
- [JPMorgan Chase (NYSE:JPM) Lifts Interest Income Outlook as Lending Offsets Trading Slowdown](https://kalkinemedia.com/us/stocks/financial/jpmorgan-chase-nysejpm-lifts-interest-income-outlook-as-lending-offsets-trading-slowdown)  
  <sub>Kalkine Media, 1 hour ago</sub>  
  JPMorgan Chase (NYSE:JPM) raised its net interest income outlook as consumer banking grew, while slower trading and lower repurchases drew attention.
- [What is Erste Group Bank's Forecast for JPM FY2026 Earnings?](https://www.marketbeat.com/instant-alerts/estimates-what-is-erste-group-banks-forecast-for-jpm-fy2026-earnings-2026-10-26/)  
  <sub>MarketBeat, 9 hours ago</sub>  
  JPMorgan Chase & Co. (NYSE:JPM - Free Report) - Stock analysts at Erste Group Bank lowered their FY2026 EPS estimates for shares of JPMorgan Chase & Co. in...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 335.35 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 333.64 (+0.5%), 50d 344.86 (-2.8%), 200d 322.54 (+4.0%); 50d above 200d
Momentum: RSI(14) 47.0 | MACD -2.415 vs signal -3.218 (histogram 0.802)
Returns: 1d +1.1% | 5d +0.5% | 1m -2.2% | 3m -6.1%
52-week range: 282.84 - 365.18 (now 63.8% of the way up)
Volatility: ATR(14) 6.24 (1.9% of price) | annualised 20d 13.7%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 890.56B
Valuation: trailing P/E 14.07 | forward P/E 13.13 | P/B 2.53 | PEG 1.41
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
Price target: mean 372.26 (+11.0% vs last close), range 312.00 - 425.00
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

- [LLY vs. MRK: Which Stock Offers the More Compelling Investment Case?](https://www.theglobeandmail.com/investing/markets/stocks/MRK/pressreleases/8455370/lly-vs-mrk-which-stock-offers-the-more-compelling-investment-case/)  
  <sub>The Globe and Mail, 9 minutes ago</sub>  
  Detailed price information for Merck & Company (MRK-N) from The Globe and Mail including charting and trades.
- [Lilly (LLY) Q3 Earnings Preview: What You Should Know Beyond the Headline Estimates](https://finance.yahoo.com/healthcare/articles/lilly-lly-q3-earnings-preview-121506507.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Looking beyond Wall Street's top-and-bottom-line estimate forecasts for Lilly (LLY), delve into some of its key metrics to gain a deeper insight into the...
- [4 stocks to watch on Monday: VZ, META, LLY, and XYZ (SP500:)](https://seekingalpha.com/news/4657125-4-stocks-to-watch-on-monday-vz-meta-lly-and-xyz)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Stock futures rise ahead of the Fed rate decision. Get key updates on Verizon, Meta, Eli Lilly and Block to spot timely market-moving opportunities.
- [Eli Lilly Stock Gets a Lift as New Lung Cancer Data Raises Hopes](https://www.tradingview.com/news/gurufocus:a522fce55094b:0-eli-lilly-stock-gets-a-lift-as-new-lung-cancer-data-raises-hopes/)  
  <sub>TradingView, 2 hours ago</sub>  
  Eli Lilly NYSE:LLY shares climbed nearly 1% in pre-market trading after clinical data showed its experimental drug olomorasib shrank tumors in 62% of...
- [Futures Rise; Musk Warning, Meta News In Focus](https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-microsoft-google-amazon-earnings-what-to-do/)  
  <sub>Investor's Business Daily, 1 hour ago</sub>  
  Dow Jones futures rose modestly early Monday, along with S&P 500 futures and Nasdaq futures. Microsoft, Google, Amazon, Sandisk and Eli Lilly headline a...
- [LLY Golden Cross Formed: Stock Drops 2.54% (October 23, 2026)](https://journalarta.com/en/2026/10/26/lly-golden-cross-formed-stock-drops-2-54-october-23-2026/)  
  <sub>JournalArta, 7 hours ago</sub>  
  On October 23, 2026: price 1273.46 USD, trend uptrend, RSI 62.1, support 1142.85, resistance 1306.69. technical analysis of lly stock.
- [LLY Nov 2026 1270.000 call (LLY261127C01270000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/LLY261127C01270000/)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>  
  Find the latest LLY Nov 2026 1270.000 call (LLY261127C01270000) stock quote, history, news and other vital information to help you with your stock trading...
- [3 Massive Catalysts That Could Ignite an Eli Lilly Stock Rally on Oct 29](https://247wallst.com/investing/2026/10/25/3-massive-catalysts-that-could-ignite-an-eli-lilly-stock-rally-on-oct-29/)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  Lilly brings 5 consecutive EPS beats to Oct 29 earnings, but Q3 estimates dropped from $9.87 to $6.67 due to acquired IPR&D charges.
- [Eli Lilly (LLY) Reports Promising Lung Cancer Trial Results Targ](https://www.gurufocus.com/news/9141485/eli-lilly-lly-reports-promising-lung-cancer-trial-results-targeting-kras-mutation)  
  <sub>GuruFocus, 13 hours ago</sub>  
  On October 25, 2026, Eli Lilly and Co (NYSE: LLY) announced encouraging clinical trial outcomes for its lung cancer drug olomorasib, demonstrating a 62%...
- [Eli Lilly (LLY) Reported A 79.3% Response Rate In Phase 1 Ovarian Cancer](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-lly/eli-lilly/news/eli-lilly-lly-reported-a-793-response-rate-in-phase-1-ovaria)  
  <sub>Simply Wall Street, 7 hours ago</sub>  
  Eli Lilly (NYSE:LLY) reported Phase 1 data for sofetabart mipitecan (Sofe-M) plus bevacizumab in platinum-sensitive ovarian cancer.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,281.70 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 1,209.79 (+5.9%), 50d 1,188.64 (+7.8%), 200d 1,085.92 (+18.0%); 50d above 200d
Momentum: RSI(14) 63.4 | MACD 31.621 vs signal 22.078 (histogram 9.543)
Returns: 1d +0.6% | 5d +3.3% | 1m +8.3% | 3m +5.0%
52-week range: 813.53 - 1,306.69 (now 94.9% of the way up)
Volatility: ATR(14) 37.17 (2.9% of price) | annualised 20d 31.0%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.14T
Valuation: trailing P/E 43.02 | forward P/E 27.14 | P/B 33.73 | PEG 1.23
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
Price target: mean 1,331.55 (+3.9% vs last close), range 930.00 - 1,600.00
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

- [Ahead of Earnings Is Microsoft Stock a Buy, a Sell, or Fairly Valued?](https://global.morningstar.com/en-nd/stocks/ahead-earnings-is-microsoft-stock-buy-sell-or-fairly-valued-2)  
  <sub>Morningstar, 4 hours ago</sub>  
  With cloud growth expected to accelerate, here's what we'll be looking for in Microsoft earnings.
- [Microsoft (MSFT) Sees $184.2 Million in Net ETF Buying on Oct. 22](https://finance.yahoo.com/markets/stocks/articles/microsoft-msft-sees-184-2-110053044.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  ETFs bought $184.2 million of Microsoft stock on Thursday, with 54 funds buying and 19 selling.
- [Here’s How Much Traders See Microsoft Stock Moving After Earnings](https://www.investopedia.com/here-is-how-much-traders-see-microsoft-stock-moving-after-earnings-msft-q1-fy2027-12184775)  
  <sub>Investopedia, 2 hours ago</sub>  
  Microsoft is set to report earnings Wednesday afternoon, with traders expecting a move that could bring the stock back near its recent record.
- [Truist Financial Maintains Microsoft(MSFT.US) With Buy Rating, Raises Target Price to $600](https://www.moomoo.com/news/post/1002360326/truist-financial-maintains-microsoft-msftus-with-buy-rating-raises-target)  
  <sub>Moomoo, 1 hour ago</sub>  
  TruistFinancial analyst Terry Tillman maintains $Microsoft(MSFT.US)$ with a buy rating, and adjusts the target price from $575 to $600.
- [Microsoft, Alphabet, Amazon Earnings Meet Fed Rate Decision: 3 Charts To Watch This Week](https://www.tradingview.com/news/stocktwits:a13f02de1094b:0-microsoft-alphabet-amazon-earnings-meet-fed-rate-decision-3-charts-to-watch-this-week/)  
  <sub>TradingView, 3 hours ago</sub>  
  Microsoft (MSFT), Alphabet (GOOG, GOOGL) and Amazon (AMZN) are slated to report earnings this week, with investors looking for more clues on where the AI...
- [Hyperscaler Earnings Previews: Alphabet, Microsoft And Amazon - Maybe The Bearish Sentiment Will Help](https://seekingalpha.com/article/4957392-hyperscaler-earnings-previews-alphabet-microsoft-amazon-maybe-bearish-sentiment-will-help)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  The name of the game for mega-cap tech seems to be about sector capital, free cash flow and capex growth, debt issuance and the ability to raise capital.
- [MSFT Fairly Valued by DCF at $543](https://www.gurufocus.com/news/9142070)  
  <sub>GuruFocus, 3 hours ago</sub>  
  On October 26, 2026, we delve into the DCF analysis for Microsoft Corp (MSFT), a company that has shown a mixed price performance recently. The stock has...
- [MSFT Stock Rises Premarket Ahead Of Q4 Results: CapEx, Azure Growth In Focus](https://stocktwits.com/news-articles/markets/equity/msft-stock-rises-premarket-ahead-of-q4-results-cap-ex-azure-growth-in-focus/cZNR8GoRJRW)  
  <sub>Stocktwits, 21 hours ago</sub>  
  Corning forecast earnings per share in the range between $0.85 and $0.89 in Q3, and at a midpoint of $0.87, it is slightly ahead of a consensus estimate of...
- [A Quick Look at Today's Ratings for Microsoft(MSFT.US), With a Forecast Between $600 to $636](https://news.futunn.com/en/post/1002293742/a-quick-look-at-today-s-ratings-for-microsoft-msftus)  
  <sub>富途牛牛, 2 hours ago</sub>  
  OnOct 26, major Wall Street analysts update their ratings for $Microsoft(MSFT.US)$, with price targets ranging from $600 to $636.Morgan Stanley analyst Adam...
- [Microsoft FY27 Q1 Earnings Preview: Azure, Capex and What to Watch](https://coindcx.com/blog/us-stock/microsoft-fy27-q1-earnings-preview)  
  <sub>CoinDCX, 3 hours ago</sub>  
  Microsoft reports FY27 Q1 results on Oct 28. Analysts expect $4.71 EPS on $90.6B revenue, with Azure guided at 44% to 45%. Key watchpoints for traders.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 528.41 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 527.66 (+0.1%), 50d 509.09 (+3.8%), 200d 436.77 (+21.0%); 50d above 200d
Momentum: RSI(14) 55.0 | MACD 6.624 vs signal 8.886 (histogram -2.263)
Returns: 1d +0.7% | 5d -1.0% | 1m +2.4% | 3m +34.3%
52-week range: 352.83 - 543.45 (now 92.1% of the way up)
Volatility: ATR(14) 11.00 (2.1% of price) | annualised 20d 19.1%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.92T
Valuation: trailing P/E 29.44 | forward P/E 22.29 | P/B 8.87 | PEG 1.70
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
  2026-06-30 beat by 10% | 2026-06-30 beat by 10% | 2026-03-31 beat by 3% | 2026-03-31 beat by 3%
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
Price target: mean 601.73 (+13.9% vs last close), range 440.00 - 870.00
Recent rating changes:
  - 2026-10-26 Scotiabank: main, Sector Outperform -> Sector Outperform
  - 2026-10-21 Guggenheim: reit, Buy -> Buy
  - 2026-10-20 BMO Capital: main, Outperform -> Outperform
  - 2026-10-19 Bernstein: main, Outperform -> Outperform
  - 2026-10-16 StoneX: main, Buy -> Buy
  - 2026-10-15 UBS: main, Buy -> Buy
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

- [NVDA Stock Ticks Higher Overnight: a16z Data Shows GPU Rental Prices Rising Sharply, Even For Older Chips](https://finance.yahoo.com/markets/stocks/articles/nvda-stock-ticks-higher-overnight-070231737.html)  
  <sub>Yahoo Finance, 8 hours ago</sub>  
  Rising rental rates across Nvidia's GPU lineup point to resilient demand for AI computing power.
- [Prediction: This Could Trigger NVDA’s Next Breakout by 2027](https://247wallst.com/investing/2026/10/26/prediction-this-could-trigger-nvdas-next-breakout-by-2027/)  
  <sub>24/7 Wall St., 9 minutes ago</sub>  
  NVIDIA just posted triple-digit revenue growth and Wall Street keeps raising its price targets, yet the stock is drifting lower. One upcoming catalyst could...
- [1 Unstoppable Stock-Split Stock to Buy Before It Joins Nvidia, Alphabet, Microsoft, and Apple in the $3 Trillion Club](https://www.fool.com/investing/2026/10/26/1-stock-split-stock-buy-nvidia-alphabet-3-trillion/)  
  <sub>The Motley Fool, 2 hours ago</sub>  
  A high-quality company will typically create tremendous long-term value, sending its stock price soaring into the hundreds or even thousands of dollars.
- [NVDA Stock Slips to $210.96, Lowest Close in 20 Sessions, on AI Financing Fears](https://www.fxleaders.com/news/2026/10/26/nvda-stock-slips-to-210-96-lowest-close-in-20-sessions-on-ai-financing-fears/)  
  <sub>FXLeaders, 2 hours ago</sub>  
  Nvidia (NASDAQ: NVDA) closed Friday at $210.96, down -0.59%, marking its lowest close in 20 trading days, as AI financing fears weigh on chip stocks.
- [Nvidia Or AMD On This Dip? Pick The Safest (NASDAQ:AMD)](https://seekingalpha.com/article/4957465-nvidia-or-amd-on-this-dip-pick-the-safest)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Nvidia (NVDA) remains my clear 'Buy' over AMD (AMD), supported by superior margins, scale, and integrated AI systems. NVDA's gross margin, profitability,...
- [Nvidia (NVDA) Stock Still Looks Reasonable Following Its 7x Five Year Run](https://finance.yahoo.com/markets/stocks/articles/nvidia-nvda-stock-still-looks-010644376.html)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  NVIDIA has been one of the defining AI hardware stories of the past few years, and after a huge multi year rally the live question is whether the current...
- [Meta Launches $35B Stock Offering, Plans Another $60B Program In 2027: Nvidia, AMD, Broadcom Eye Up To $5B Investment](https://www.tradingview.com/news/stocktwits:0a60c7843094b:0-meta-launches-35b-stock-offering-plans-another-60b-program-in-2027-nvidia-amd-broadcom-eye-up-to-5b-investment/)  
  <sub>TradingView, 2 hours ago</sub>  
  Meta Platforms (META) was in focus on Monday after the company announced $35 billion in concurrent stock offerings, with Nvidia (NVDA), Advanced Micro...
- [Elon Musk’s Warning of ‘Guppy-Level Death’ Sends Neocloud Stocks Tumbling](https://www.investopedia.com/market-update-neocloud-stocks-slide-after-elon-musk-warns-of-guppy-level-death-spcx-tsla-nvda-crwv-iren-apld-12194203)  
  <sub>Investopedia, 2 hours ago</sub>  
  Shares of neoclouds that offer AI infrastructure for rent are falling after a post by Elon Musk added fuel to worries about their financial health.
- [The Mixed Blessing From Tech Earnings Weighing on Nvidia Stock](https://www.barrons.com/articles/nvidia-stock-price-tech-earnings-ai-32f46282)  
  <sub>Barron's, 5 hours ago</sub>  
  Nvidia stock has fallen back over the past month but Elon Musk is still a big fan of the company's hardware.
- [AI Bubble on Watch Starting With Nvidia](http://www.baystreet.ca/articles/stockstowatch.aspx?articleid=124826)  
  <sub>Baystreet.ca, 5 hours ago</sub>  
  Between August and last week, CoreWeave (CRWV) broke down from its key $85-$90 support zone (based on the 50- and 200-day moving averages).

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 215.65 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 224.88 (-4.1%), 50d 222.29 (-3.0%), 200d 203.82 (+5.8%); 50d above 200d
Momentum: RSI(14) 43.7 | MACD -2.753 vs signal -0.949 (histogram -1.804)
Returns: 1d +2.2% | 5d -0.7% | 1m -4.2% | 3m +9.5%
52-week range: 165.17 - 239.24 (now 68.2% of the way up)
Volatility: ATR(14) 5.99 (2.8% of price) | annualised 20d 29.9%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 5.21T
Valuation: trailing P/E 27.27 | forward P/E 13.55 | P/B 22.74 | PEG 0.26
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
Earnings record, last 4 quarters: 4 beats
  2026-09-30 beat by 4% | 2026-06-30 beat by 4% | 2026-06-30 beat by 4% | 2026-03-31 beat by 4%
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
Price target: mean 328.95 (+52.5% vs last close), range 180.00 - 515.00
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

### Novo Nordisk (NVO) · Company — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 429: {"error":{"message":"Model busy, retry later","type":"invalid_request_error","param":null,"code":"engine_overloaded"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Novozymes (CPSE:NSIS B) Stock Looks Reasonable After Its 64% Run](https://finance.yahoo.com/markets/stocks/articles/novozymes-cpse-nsis-b-stock-002240527.html)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  Novozymes has rewarded shareholders with a solid run in recent years, which naturally raises a simple question for anyone looking at the chart today.
- [SRRK Stock Gains After Company Drops Troubled Novo Nordisk-Owned Plant From FDA Filing](https://stocktwits.com/news-articles/markets/equity/srrk-stock-gains-after-company-drops-troubled-novo-nordisk-owned-plant-from-fda-filing/cZY97AgRJVf)  
  <sub>Stocktwits, 21 hours ago</sub>  
  Scholar Rock still expects a decision on its application by the September 30 target date.In September 2025, the FDA rejected Scholar Rock's original...
- [NVO290119C00030000 interactive stock chart | NVO Jan 2029 30.000 call stock - Yahoo Finance](https://sg.finance.yahoo.com/chart/NVO290119C00030000)  
  <sub>Yahoo Finance Singapore, 22 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [3 Massive Catalysts That Could Ignite an Eli Lilly Stock Rally on Oct 29](https://247wallst.com/investing/2026/10/25/3-massive-catalysts-that-could-ignite-an-eli-lilly-stock-rally-on-oct-29/)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  Lilly brings 5 consecutive EPS beats to Oct 29 earnings, but Q3 estimates dropped from $9.87 to $6.67 due to acquired IPR&D charges.
- [Should You Buy Viking Therapeutics Stock Ahead of Q3 Results?](https://finance.yahoo.com/markets/stocks/articles/buy-viking-therapeutics-stock-ahead-130200051.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Viking Therapeutics VKTX is set to report third-quarter 2026 earnings on Oct. 28, after market close. Because the company has no marketed drugs in its...
- [LLY vs. MRK: Which Stock Offers the More Compelling Investment Case?](https://finance.yahoo.com/healthcare/articles/lly-vs-mrk-stock-offers-123000815.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Eli Lilly LLY and Merck MRK are leading global pharmaceutical companies with blockbuster drug portfolios and promising pipelines.
- [FDA proposal weighs on Novo Nordisk stock as downward price move persists](https://tradersunion.com/news/stocks/show/3964274-novo-nordisk-slides-1-03percent-to/)  
  <sub>Traders Union, 7 hours ago</sub>  
  Novo Nordisk trades at $39.03 today, down 1.03%. Get the latest on NVO price action, FDA news, and technical outlook.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 39.06 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 38.41 (+1.7%), 50d 41.77 (-6.5%), 200d 44.60 (-12.4%); 50d below 200d
Momentum: RSI(14) 45.7 | MACD -0.611 vs signal -0.973 (histogram 0.362)
Returns: 1d +0.0% | 5d +1.7% | 1m +0.7% | 3m -23.4%
52-week range: 35.29 - 63.98 (now 13.1% of the way up)
Volatility: ATR(14) 0.81 (2.1% of price) | annualised 20d 20.0%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 172.31B
Valuation: trailing P/E 9.55 | forward P/E 11.35 | P/B 5.20 | PEG 4.36
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
Price target: mean 45.06 (+15.4% vs last close), range 39.71 - 61.74
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

### Royal Bank of Canada (RY) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Royal Bank of Canada (RY) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RY/)  
  <sub>Yahoo! Finance Canada, 3 hours ago</sub>  
  3,398.61% · Previous Close 202.06 · Open 201.24 · Bid -- · Ask 211.72 x 20000 · Day's Range 199.19 - 201.50 · 52 Week Range 143.38 - 218.57 · Volume 4,317,853...
- [LLY vs. MRK: Which Stock Offers the More Compelling Investment Case?](https://www.theglobeandmail.com/investing/markets/stocks/MRK/pressreleases/8455370/lly-vs-mrk-which-stock-offers-the-more-compelling-investment-case/)  
  <sub>The Globe and Mail, 8 minutes ago</sub>  
  Detailed price information for Merck & Company (MRK-N) from The Globe and Mail including charting and trades.
- [Royal Bank of Canada's Dividend Analysis](https://finance.yahoo.com/markets/stocks/articles/royal-bank-canadas-dividend-analysis-110027578.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [IDFC First Bank Posts Q2 FY27 Earnings Call Audio for Investors](https://www.theglobeandmail.com/investing/markets/markets-news/Tipranks/8454883/idfc-first-bank-posts-q2-fy27-earnings-call-audio-for-investors/)  
  <sub>The Globe and Mail, 23 minutes ago</sub>  
  The latest announcement is out from IDFC First Bank Ltd. ( (IN:IDFCFIRSTB) ). IDFC First Bank has notified stock exchanges that it has published the audio...
- [3 Canadian Bank Stocks Facing A Bank Of Canada Rate Reset](https://finance.yahoo.com/markets/stocks/articles/3-canadian-bank-stocks-facing-111118005.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  Canadian bank stocks are back in the spotlight as the Bank of Canada signals a tighter path for interest rates, and higher borrowing costs ripple through...
- [Royal Bank of Canada dividend goes ex: Royal Bank of Canada stock yields 3.50 percent](https://www.ad-hoc-news.de/boerse/news/corporate-news/royal-bank-of-canada-dividend-goes-ex-royal-bank-of-canada-stock-yields-3-50-percent/70414159)  
  <sub>ad-hoc-news.de, 4 hours ago</sub>  
  RBC posted CAD 4.28 adjusted EPS in fiscal third quarter 2026, up 11.00 percent. Royal Bank of Canada stock costs EUR 179.00 on October 26, 2026.
- [Enterprise Products to Report Q3 Earnings: What's in the Cards?](https://www.theglobeandmail.com/investing/markets/stocks/XOM/pressreleases/8454106/enterprise-products-to-report-q3-earnings-whats-in-the-cards/)  
  <sub>The Globe and Mail, 1 hour ago</sub>  
  Detailed price information for Exxonmobil Holdings Corp (XOM-N) from The Globe and Mail including charting and trades.
- [Can Royal Bank Of Canada (TSX:RY) Trade At A Discount After A 185% Run?](https://simplywall.st/stocks/ca/banks/tsx-ry/royal-bank-of-canada-shares/news/can-royal-bank-of-canada-tsxry-trade-at-a-discount-after-a-1)  
  <sub>Simply Wall Street, 21 hours ago</sub>  
  Royal Bank of Canada has delivered powerful long term returns, so the real question now is whether the current share price still lines up with the returns...
- [Zacks Investment Ideas feature highlights: Bloom Energy, SanDisk, AMD, CoreWeave, Nebius, NVIDIA and SpaceX's](https://www.theglobeandmail.com/investing/markets/stocks/CRWV/pressreleases/8455390/zacks-investment-ideas-feature-highlights-bloom-energy-sandisk-amd-coreweave-nebius-nvidia-and-spacexs/)  
  <sub>The Globe and Mail, 6 minutes ago</sub>  
  Detailed price information for Coreweave Cl A (CRWV-Q) from The Globe and Mail including charting and trades.
- [Senco Gold to Acquire 68% Stake in Melorra Owner for Rs 68 Crore](https://www.theglobeandmail.com/investing/markets/markets-news/Tipranks/8454887/senco-gold-to-acquire-68-stake-in-melorra-owner-for-rs-68-crore/)  
  <sub>The Globe and Mail, 23 minutes ago</sub>  
  Senco Gold Limited ( (IN:SENCO) ) has provided an update. Senco Gold Limited has executed definitive agreements to acquire a 68% equity stake in August...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 201.47 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 196.50 (+2.5%), 50d 202.01 (-0.3%), 200d 188.51 (+6.9%); 50d above 200d
Momentum: RSI(14) 55.8 | MACD -0.178 vs signal -1.443 (histogram 1.265)
Returns: 1d +0.1% | 5d +2.6% | 1m -0.3% | 3m -5.1%
52-week range: 145.41 - 217.87 (now 77.4% of the way up)
Volatility: ATR(14) 2.93 (1.5% of price) | annualised 20d 16.5%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 278.92B
Valuation: trailing P/E 17.61 | forward P/E 15.80 | P/B 2.93 | PEG 1.89
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
Earnings record, last 4 quarters: 1 beat, 3 in line
  2026-09-30 in line | 2026-06-30 in line | 2026-06-30 in line | 2026-03-31 beat by 3%
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
Price target: mean 212.25 (+5.4% vs last close), range 185.25 - 233.45
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

### Exxon Mobil (XOM) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Can Exxon’s $4.5 Billion Refining Windfall Defy Dropping Crude Prices on Oct. 30?](https://finance.yahoo.com/energy/articles/exxon-4-5-billion-refining-115535226.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Exxon Mobil (NYSE:XOM) reports third-quarter results on Oct. 30. A projected $4.5 billion refining boost runs into lower average crude prices,...
- [SpaceX, CoreWeave, Ambev, XP, Exxon, and More Stocks That Explain Today’s Market](https://www.barrons.com/articles/stock-movers-5b85a74c)  
  <sub>Barron's, 5 hours ago</sub>  
  SpaceX rises but neocloud stocks CoreWeave, Nebius, and IREN slide after Elon Musk says they face “guppy-level death and consolidation.”
- [Why Did XOM, COP, CVX Jump To 52-Week Highs Last Week?](https://stocktwits.com/news-articles/markets/equity/why-did-xom-cop-cvx-jump-to-52-week-highs-last-week/cZUdVAARBUz)  
  <sub>Stocktwits, 12 hours ago</sub>  
  Exxon Mobil, ConocoPhillips and Chevron stocks surged to annual highs after Brent crude futures maturing in December climbed over $116 per barrel on Friday,...
- [ETFs Bought $1.41 Billion of ExxonMobil (XOM) on Oct. 22](https://www.gurufocus.com/news/9141926/etfs-bought-141-billion-of-exxonmobil-xom-on-oct-22?utm_source=yahoo_finance&utm_medium=syndication&utm_campaign=headlines&r=caf6fe0e0db70d936033da5461e60141)  
  <sub>GuruFocus, 4 hours ago</sub>  
  ETF flows into ExxonMobil turned sharply positive in Thursday's session, snapping a one-day selloff, as 51 ETFs bought the stock against 12 that sold for a...
- [Avantis U.S. Large Cap Value (AVLV) Adds Exxon Mobil on Oct. 22](https://finance.yahoo.com/markets/stocks/articles/avantis-u-large-cap-value-110333049.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  The fund bought $569.1 million of Exxon Mobil as part of $713.9 million in net buying across 161 increased positions.
- [ExxonMobil (NYSE:XOM) Hits New 1-Year High - Still a Buy?](https://www.marketbeat.com/instant-alerts/price-exxonmobil-nyse-xom-hits-new-1-year-high-still-a-buy-2026-10-26/)  
  <sub>MarketBeat, 35 minutes ago</sub>  
  ExxonMobil Corporation (NYSE:XOM - Get Free Report) shares reached a new 52-week high during trading on Monday. The stock traded as high as $183.75 and last...
- [What Capital Group Dividend Value (CGDV) Bought: Exxon Mobil Leads on Oct. 22](https://finance.yahoo.com/markets/stocks/articles/capital-group-dividend-value-cgdv-110350448.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  The fund added $519.0 million in new buying across 50 positions, led by a $501.3 million stake in Exxon Mobil.
- [ExxonMobil Holdings (XOM) Draws Earnings Focus, Is The Upside Already Priced In?](https://simplywall.st/stocks/us/energy/nyse-xom/exxonmobil-holdings/news/exxonmobil-holdings-xom-draws-earnings-focus-is-the-upside-a)  
  <sub>Simply Wall Street, 17 hours ago</sub>  
  ExxonMobil Holdings (XOM) is back in focus as investors watch for its October 30 earnings release, with expectations of an earnings beat following upward...
- [ExxonMobil Corporation $XOM Shares Bought by NTV Asset Management LLC](https://www.marketbeat.com/instant-alerts/filing-exxonmobil-corporation-xom-shares-bought-by-ntv-asset-management-llc-2026-10-26/)  
  <sub>MarketBeat, 5 hours ago</sub>  
  NTV Asset Management LLC lifted its holdings in shares of ExxonMobil Corporation (NYSE:XOM - Free Report) by 8.6% during the third quarter, according to its...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 183.10 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 171.88 (+6.5%), 50d 166.24 (+10.1%), 200d 153.46 (+19.3%); 50d above 200d
Momentum: RSI(14) 75.8 | MACD 4.997 vs signal 4.039 (histogram 0.958)
Returns: 1d -0.1% | 5d +2.7% | 1m +14.0% | 3m +19.6%
52-week range: 113.68 - 183.21 (now 99.8% of the way up)
Volatility: ATR(14) 3.81 (2.1% of price) | annualised 20d 18.4%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 752.89B
Valuation: trailing P/E 23.56 | forward P/E 14.80 | P/B 2.90 | PEG 1.58
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
Price target: mean 179.41 (-2.0% vs last close), range 142.00 - 206.00
Recent rating changes:
  - 2026-10-19 Barclays: main, Overweight -> Overweight
  - 2026-10-15 Morgan Stanley: main, Overweight -> Overweight
  - 2026-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - 2026-09-28 TD Cowen: main, Buy -> Buy
  - 2026-09-03 Piper Sandler: main, Neutral -> Neutral
  - 2026-08-19 Morgan Stanley: main, Overweight -> Overweight
Institutional ownership: 67.3%
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

> Neutral overall: no macro surprise, technicals not decisive, flows flat, fundamentals modestly positive.

**Main reasons it gave:**
- Technical: price below 20‑day (28.23) and 50‑day (28.52) SMA, RSI 30.4 (oversold) but no decisive break
- Fund flows flat: share count unchanged (0% change) over 1 week and 1 month
- Fund basics: 3‑year record +12.7% per year, yield 3.2%, expense ratio 0.85%, cash 47% of assets
- Macro: Treasury yields down modestly, VIX unchanged, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 27.58 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 28.23 (-2.3%), 50d 28.52 (-3.3%), 200d 27.33 (+0.9%); 50d above 200d
Momentum: RSI(14) 30.4 | MACD -0.168 vs signal -0.100 (histogram -0.068)
Returns: 1d -1.0% | 5d -2.2% | 1m -3.4% | 3m -0.9%
52-week range: 25.44 - 29.49 (now 52.8% of the way up)
Volatility: ATR(14) 0.25 (0.9% of price) | annualised 20d 9.4%
Volume: 0.80x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 27.60M | fund size: 761.21M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals bullish but low volume, flat fund flows, mixed energy inventory signals, and bearish EIA crude price outlook offset by limited fund exposure.

**Main reasons it gave:**
- No macro surprise: yields fell slightly, inflation near target
- Technicals bullish but low volume, no decisive break
- Fund flows flat, indicating no net demand shift
- Energy inventories mixed: crude draw bullish, gas build bearish
- EIA price outlook bearish for crude, but fund exposure limited

<details><summary><b>News</b> — score +0.00</summary>

- [4 of the Smartest ETFs to Buy When Inflation Is Running Hot](https://www.fool.com/investing/2026/10/25/4-smartest-etfs-to-buy-when-inflation-running-hot/)  
  <sub>The Motley Fool, 23 hours ago</sub>  
  These funds each provide a different approach to inflation protection in your portfolio.
- [HGER: A Primer On The Harbor Commodity All-Weather Strategy ETF](https://seekingalpha.com/article/4952552-hger-primer-on-harbor-commodity-all-weather-strategy-etf)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  The Harbor Commodity All-Weather Strategy ETF tracks a rules-based index that weights commodity futures by inflation sensitivity and roll costs.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 33.79 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 33.12 (+2.0%), 50d 32.47 (+4.1%), 200d 29.02 (+16.4%); 50d above 200d
Momentum: RSI(14) 61.3 | MACD 0.414 vs signal 0.392 (histogram 0.022)
Returns: 1d -0.9% | 5d +0.3% | 1m +3.6% | 3m +18.2%
52-week range: 22.36 - 34.10 (now 97.4% of the way up)
Volatility: ATR(14) 0.47 (1.4% of price) | annualised 20d 13.9%
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
Yield: 2.3%
Three-year record: +15.9% a year | beta to the market 1.05
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
US inventories, week ending 2026-10-16 (published the following Wednesday)
  Crude oil: 412.5 million barrels, -3.1 on the week (a draw), 15% percentile over 52 weeks
  Natural gas: 3,644.0 billion cubic feet, +77.0 on the week (a build), 87% percentile over 52 weeks -- high for the time of year
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 111.40M | fund size: 3.76B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows significant outflows (-11.4% in one month) and technical weakness (price below 50‑day and 200‑day SMAs, low volume, no decisive break). Macro conditions suggest further Fed tightening, which pressures emerging‑market bonds. Fundamentals are modestly positive (5.4% yield, mixed credit quality, strong performance), but not enough to offset the negative flow and macro backdrop. Overall, the view remains neutral.

**Main reasons it gave:**
- 1‑month outflows of -11.4% (-$1.66B) indicating strong investor redemptions
- Price below 50‑day (92.83) and 200‑day (95.04) SMAs, low volume (0.17× 20‑day avg) and no decisive technical break
- Macro: Fed likely to raise rates further (market pricing ~3 hikes) with inflation at 3.7% above target
- Fundamentals: Yield 5.4% with mixed credit quality (33.5% BBB, 25.3% BB, 19.5% B) and 88% US government debt exposure

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 91.64 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 91.13 (+0.6%), 50d 92.83 (-1.3%), 200d 95.04 (-3.6%); 50d below 200d
Momentum: RSI(14) 47.8 | MACD -0.296 vs signal -0.484 (histogram 0.188)
Returns: 1d -0.0% | 5d +0.6% | 1m -0.6% | 3m -3.7%
52-week range: 90.14 - 97.74 (now 19.8% of the way up)
Volatility: ATR(14) 0.49 (0.5% of price) | annualised 20d 5.7%
Volume: 0.17x the 20-day average
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.50</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -0.5% (-63.53M) over 7d | 1 month: -11.4% (-1.66B) over 30d
Shares outstanding: 141.38M | fund size: 12.96B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, yields slightly down, technicals modestly bullish but no decisive break, positioning modestly bearish but not extreme, fundamentals stable.

**Main reasons it gave:**
- Fed target unchanged at 4.00% with no policy surprise
- Treasury yields slipped slightly across the curve (10‑year -0.17% week‑over‑week)
- Technical indicators show modest bullish momentum (RSI 61.8, MACD positive) but no decisive break
- CFTC positioning shows large speculators net short 35.9% of OI, up 2% week‑over‑week, indicating modest bearish sentiment

<details><summary><b>News</b> — score +0.00</summary>

- [AI could push trading of U.S. investment-grade bonds higher – Barclays](https://seekingalpha.com/news/4657251-ai-could-push-trading-of-us-investment-grade-bonds-higher-barclays)  
  <sub>Seeking Alpha, 18 minutes ago</sub>  
  Barclays says AI could lift electronic trading in investment-grade bonds to 65%, boosting efficiency but raising volatility risks.
- [Black Monday Calls, $110 Oil, A Chip Rout: 3 Charts to Watch This Week](https://stocktwits.com/news-articles/markets/equity/black-monday-oil-prices-memory-chips-market-outlook/cZx8ZyaRBMj)  
  <sub>Stocktwits, 21 hours ago</sub>  
  Calls for a “Black Monday” crash spread across social media over the weekend, but U.S. stock futures were pointing higher early Monday, the 39th anniversary...
- [Beyond AI: 5 market rotations to watch](https://www.home.saxo/en-gb/content/articles/equities/beyond-ai-5-market-rotations-to-watch-26102026)  
  <sub>Saxo, 8 hours ago</sub>  
  AI spending is becoming a double-edged sword: Meta was punished for spending more, while Tesla fell despite cutting its investment plans.
- [What To Expect In Markets This Week: GOOGL, MSFT, AMZN, INTC, HOOD, LLY Earnings, Fed Meeting And More](https://fr.tradingview.com/news/stocktwits:ef3220335094b:0-what-to-expect-in-markets-this-week-googl-msft-amzn-intc-hood-lly-earnings-fed-meeting-and-more/)  
  <sub>TradingView, 23 hours ago</sub>  
  U.S. markets are heading into one of the busiest weeks of the earnings season, with a fresh batch of corporate results arriving alongside several closely...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 91.17 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 89.83 (+1.5%), 50d 91.03 (+0.1%), 200d 93.96 (-3.0%); 50d below 200d
Momentum: RSI(14) 61.8 | MACD 0.041 vs signal -0.239 (histogram 0.280)
Returns: 1d +0.1% | 5d +1.2% | 1m +1.3% | 3m -2.6%
52-week range: 88.92 - 97.99 (now 24.8% of the way up)
Volatility: ATR(14) 0.49 (0.5% of price) | annualised 20d 5.3%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Long Government
Yield: 4.1%
Credit quality: AA 100.0% | US government debt 99.7%
Three-year record: +4.2% a year | beta to the market 1.16
Cost and size: expense ratio 0.15% | net assets 41.56B
What it is made of: Bonds 99.7%, Cash 0.3%
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 146.00M | fund size: 13.31B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: yields down modestly, Fed target unchanged
- Technical indicators mixed: price above 20‑day SMA but below 50‑day SMA, RSI neutral
- CFTC positioning shows net short 11.4% of open interest, increasing 9.2% week‑over‑week
- Analyst coverage thin (2% of fund) but bullish with +15.7% price target

<details><summary><b>News</b> — score +0.00</summary>

- [iShares Russell 2000 (IWM) Buys $2.6 Million More Jackson Financial on Thursday](https://finance.yahoo.com/markets/stocks/articles/ishares-russell-2000-iwm-buys-110504294.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. iShares Russell 2000 Index Fund (IWM) was almost entirely on the buy side in ETF activity on Thursday, Oct. 22,...
- [The AI Selloff Is Close To A Bottom: I’m Buying It (NASDAQ:SMH)](https://seekingalpha.com/article/4957460-the-ai-selloff-is-close-to-a-bottom-im-buying-it)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  The AI-driven selloff in the VanEck Semiconductor ETF has seen capital rotate out of SMH into Financials, Industrials, and Software.
- [Rotation Risk and Earnings Discipline | Weekly Options](https://www.moomoo.com/community/feed/rotation-risk-and-earnings-discipline-weekly-options-117506597519366)  
  <sub>Moomoo, 5 hours ago</sub>  
  By Luke Wu | October 26, 2026 Cross-Asset Volatility Broader asset volatility picked up last week, but the pressure is coming from rates and commoditi...
- [Weekly Signal | QQQ Tests Support Ahead of Big Tech Earnings and the Fed](https://www.moomoo.com/community/feed/weekly-signal-qqq-tests-support-ahead-of-big-tech-earnings-117505738866694)  
  <sub>Moomoo, 9 hours ago</sub>  
  Last week, we noted that hedge funds had unwound all of their AI buying since January 2025 in just five trading days. But there was an important twist...
- [Beyond AI: 5 market rotations to watch](https://www.home.saxo/en-mena/content/articles/equities/beyond-ai-5-market-rotations-to-watch-26102026)  
  <sub>Saxo, 7 hours ago</sub>  
  AI spending is becoming a double-edged sword: Meta was punished for spending more, while Tesla fell despite cutting its investment plans.
- [IWM Nov 2026 281.000 call (IWM261106C00281000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/IWM261106C00281000/chart/)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Interactive Chart for IWM Nov 2026 281.000 call (IWM261106C00281000), analyze all the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 278.12 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 277.10 (+0.4%), 50d 285.87 (-2.7%), 200d 278.33 (-0.1%); 50d above 200d
Momentum: RSI(14) 47.9 | MACD -2.685 vs signal -3.410 (histogram 0.725)
Returns: 1d +0.9% | 5d +2.5% | 1m -1.4% | 3m -5.2%
52-week range: 229.11 - 305.09 (now 64.5% of the way up)
Volatility: ATR(14) 3.62 (1.3% of price) | annualised 20d 14.9%
Volume: 0.23x the 20-day average
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
Three-year record: +20.0% a year | beta to the market 1.27
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.89 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.7% above the current prices
Holdings read: XTSLA, TWST, MOG-A, FROG, TXG
Recent rating changes among them:
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MOG-A: 2026-10-13 JP Morgan: main, Overweight -> Overweight
  - FROG: 2026-10-21 Truist Securities: main, Buy -> Buy
  - TXG: 2026-10-13 TD Cowen: main, Hold -> Hold
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-20, published the following Friday)
Large speculators: net short 11.4% of open interest (466,789 contracts)
Change on the week: +9.2% of open interest
Crowding: 73% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 281.05M | fund size: 78.17B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No clear macro catalyst, flat fund flows, technicals show no decisive break, fundamentals are solid but not a strong driver.

**Main reasons it gave:**
- Fund flows flat: 0% change in share count over 1 week and 1 month
- Technical trend: price below 200‑day SMA, low volume, no decisive break
- Macro: Treasury yields fell modestly but market expects ~3 quarter‑point hikes in next 2 years
- Fund basics: solid credit quality (A 46.7%, BBB 40.5%) and 4.9% yield, but price near lower 52‑week range

<details><summary><b>News</b> — score +0.00</summary>

- [AI could push trading of U.S. investment-grade bonds higher – Barclays](https://seekingalpha.com/news/4657251-ai-could-push-trading-of-us-investment-grade-bonds-higher-barclays)  
  <sub>Seeking Alpha, 21 minutes ago</sub>  
  Barclays says AI could lift electronic trading in investment-grade bonds to 65%, boosting efficiency but raising volatility risks.
- [Rotation Risk and Earnings Discipline | Weekly Options](https://www.moomoo.com/community/feed/rotation-risk-and-earnings-discipline-weekly-options-117506597519366)  
  <sub>Moomoo, 5 hours ago</sub>  
  By Luke Wu | October 26, 2026 Cross-Asset Volatility Broader asset volatility picked up last week, but the pressure is coming from rates and commoditi...
- [2026 Tax-Loss Harvesting Opportunities With VanEck ETFs](https://seekingalpha.com/article/4957428-2026-tax-loss-harvesting-opportunities-with-vaneck-etfs)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Tax-loss harvesting may work best when you swap into a similar, not identical, fund to stay compliant with the wash-sale rule. We screened US-listed ETFs...
- [Beyond AI: 5 market rotations to watch](https://www.home.saxo/en-mena/content/articles/equities/beyond-ai-5-market-rotations-to-watch-26102026)  
  <sub>Saxo, 8 hours ago</sub>  
  AI spending is becoming a double-edged sword: Meta was punished for spending more, while Tesla fell despite cutting its investment plans.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 104.24 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 102.79 (+1.4%), 50d 104.24 (+0.0%), 200d 107.81 (-3.3%); 50d below 200d
Momentum: RSI(14) 58.7 | MACD -0.040 vs signal -0.334 (histogram 0.294)
Returns: 1d +0.4% | 5d +1.3% | 1m +1.0% | 3m -2.4%
52-week range: 101.83 - 112.92 (now 21.7% of the way up)
Volatility: ATR(14) 0.64 (0.6% of price) | annualised 20d 5.9%
Volume: 0.15x the 20-day average
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 293.50M | fund size: 30.59B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals modestly bullish but low volume, positioning modestly bearish, analyst view thin with slight bullish tilt but price target below current. Overall neutral.

**Main reasons it gave:**
- Macro: yields down slightly, no policy surprise
- Technicals: price above 20d, 50d, 200d SMAs, but volume 0.37x 20‑day average
- Positioning: net short 19.2% of open interest, up 2% week‑over‑week
- Analyst view: thin coverage (1.4% weight) with 58% buy, price target -7.1% vs current

<details><summary><b>News</b> — score +0.00</summary>

- [Invesco S&P 500 Equal Weight ETF Shs Cert Deposito Arg Repr 0.0333333333 Shs Estimates – BCBA:RSP](https://www.tradingview.com/symbols/BCBA-RSP/financials-estimates/)  
  <sub>TradingView, 10 hours ago</sub>  
  Explore reported financial data and analyst estimates across the income statement, balance sheet, cash flow statement, and valuation metrics.
- [A Patient Died in an Early CAR-T Trial for MS. How the News Reached the Public Matters Too.](https://www.moomoo.com/community/feed/a-patient-died-in-an-early-car-t-trial-for-117502289248262)  
  <sub>Moomoo, 23 hours ago</sub>  
  A patient died in an early trial of a promising new class of treatment, and how that news reaches the public matters as much as the news itself. Brist...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.10</summary>

```text
Last close 217.57 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 213.06 (+2.1%), 50d 215.25 (+1.1%), 200d 207.38 (+4.9%); 50d above 200d
Momentum: RSI(14) 60.4 | MACD 0.923 vs signal 0.156 (histogram 0.767)
Returns: 1d +0.5% | 5d +2.0% | 1m +3.1% | 3m -0.1%
52-week range: 182.18 - 222.77 (now 87.2% of the way up)
Volatility: ATR(14) 2.02 (0.9% of price) | annualised 20d 10.0%
Volume: 0.37x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.16</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.16</summary>

```text
Rolled up from the 5 largest holdings, 1.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 58.3% | hold 41.7% | sell 0.0% (mean 2.22 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -7.1% above the current prices
Holdings read: MRNA, P, ILMN, CRWD, RVTY
Recent rating changes among them:
  - MRNA: 2026-10-26 Piper Sandler: reit, Overweight -> Overweight
  - P: 2026-10-12 Guggenheim: main, Buy -> Buy
  - ILMN: 2026-10-19 Canaccord Genuity: main, Hold -> Hold
  - CRWD: 2026-10-22 Mizuho: main, Outperform -> Outperform
  - RVTY: 2026-10-13 TD Cowen: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-20, published the following Friday)
Large speculators: net short 19.2% of open interest (1,935,470 contracts)
Change on the week: +2.0% of open interest
Crowding: 62% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 155.55M | fund size: 33.84B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no material macro surprise, stable fundamentals, modest bearish positioning but not decisive, and mixed technicals.

**Main reasons it gave:**
- Large speculators net short 28.4% of open interest, up 1.7% week‑over‑week (modest bearish pressure)
- US Treasury yields fell slightly across the curve this week (3‑month -0.03, 5‑year -0.13, 10‑year -0.17)
- Price 81.49 is just above 20‑day SMA (81.24) and 50‑day SMA (81.47) but below 200‑day SMA (82.14); RSI 60, MACD positive, volume low
- Fund basics unchanged: short‑government fund, AA credit quality, 3.6% yield, expense ratio 0.15%

<details><summary><b>News</b> — score +0.00</summary>

- [The Federal Reserve and the European Central Bank are expected to jointly pause rate hikes, yet why does global capital remain under pressure? JPMorgan Outlook: The logic of continued tightening continues to weigh on equities and bonds.](https://news.futunn.com/en/post/1002248784/the-federal-reserve-and-the-european-central-bank-are-expected)  
  <sub>富途牛牛, 11 hours ago</sub>  
  JPMorgan'slatest research report indicates that the key trading theme in financial markets, linked to this week's monetary policy decisions by the European...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.49 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 81.24 (+0.3%), 50d 81.47 (+0.0%), 200d 82.14 (-0.8%); 50d below 200d
Momentum: RSI(14) 60.0 | MACD 0.017 vs signal -0.037 (histogram 0.054)
Returns: 1d -0.0% | 5d +0.2% | 1m +0.3% | 3m -0.6%
52-week range: 81.05 - 83.18 (now 20.4% of the way up)
Volatility: ATR(14) 0.11 (0.1% of price) | annualised 20d 1.4%
Volume: 0.13x the 20-day average
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-20, published the following Friday)
Large speculators: net short 28.4% of open interest (4,533,571 contracts)
Change on the week: +1.7% of open interest
Crowding: 93% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 209.30M | fund size: 17.05B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, modest speculator short bias, solid fundamentals but no new catalyst, technicals lack decisive break.

**Main reasons it gave:**
- CFTC data: large speculators net short 35.9% of open interest in 10Y note futures
- US Treasury yields up modestly: 10-year down 0.17% on the week
- Technical: price above 20‑day SMA (104.88) and 50‑day SMA (105.76) but below 200‑day SMA (108.94)
- Fund basics: AA credit quality, 4.7% yield, expense ratio 0.18%

<details><summary><b>News</b> — score +0.00</summary>

- [The Search for a Sure Thing Beyond Bonds or Cash](https://www.bloomberg.com/news/articles/2026-10-26/clo-etfs-how-to-invest-as-rising-interest-rates-hurt-bonds?srnd=phx-money)  
  <sub>Bloomberg.com, 4 hours ago</sub>  
  As rising rates punish bonds, a little-known corner of the ETF universe has been offering investors more juice than cash.
- [Defiance Launches AIBN: The First U.S.-Listed ETF Dedicated to the Bonds Funding the AI Buildout](https://www.tipranks.com/news/defiance-launches-aibn-the-first-u-s-listed-etf-dedicated-to-the-bonds-funding-the-ai-buildout)  
  <sub>TipRanks, 4 hours ago</sub>  
  The Debt Behind the Data Centers The Defiance AI Infrastructure Bond ETF (NYSE Arca: AIBN) began trading on October 20, 2026, and the simplest way to...
- [3 Best Vanguard ETFs for a Simple 60/40 Portfolio](https://www.tipranks.com/news/3-best-vanguard-etfs-for-a-simple-60-40-portfolio)  
  <sub>TipRanks, 1 hour ago</sub>  
  Building a simple 60/40 portfolio with Vanguard ETFs could be an appealing way to pursue long-term growth without taking unnecessary risks.
- [Morgan Stanley’s Bitcoin ETF Draws Fresh Cash as BTC Nears $80K and Rally Cools](https://www.tipranks.com/news/cryptocurrencies/morgan-stanleys-bitcoin-etf-draws-fresh-cash-as-btc-nears-80k-and-rally-cools)  
  <sub>TipRanks, 4 hours ago</sub>  
  Morgan Stanley's flagship crypto vehicle, the Morgan Stanley Bitcoin Trust ETF, saw fresh capital inflows this week as investors continued to test the...
- [Ford Stock (F) Set for Near 7% Move After Q3 Earnings This Week, Say Options Traders](https://www.tipranks.com/news/ford-stock-f-set-for-near-7-move-after-q3-earnings-this-week-say-options-traders)  
  <sub>TipRanks, 58 minutes ago</sub>  
  Ford Motor Company ($F) reports its Q3 earnings later this week – October 28. Its share price is down 8.5% in the year-to-date, hit by slumping U.S. sales,...
- [Why Is Penny Stock Stratum (SRTM) Up 33% Today?](https://www.tipranks.com/news/why-is-penny-stock-stratum-srtm-up-33-today)  
  <sub>TipRanks, 1 hour ago</sub>  
  Stratum stock rallied nearly 33% following a new letter of intent for a strategic collaboration with Ocean Power Technologies to explore marine AI data...
- [SoundHound AI Stock: Why Analysts See 145%+ Upside](https://www.tipranks.com/news/soundhound-ai-stock-why-analysts-see-145-upside)  
  <sub>TipRanks, 1 hour ago</sub>  
  SoundHound AI ($SOUN) stock is down 55% year-to-date as investors are worried about ongoing losses and a high valuation. Analysts have a Moderate Buy...
- [BigBear.ai Holdings Will Report Q3 Earnings Tomorrow. Ahead of It, Who Owns BBAI Stock?](https://www.tipranks.com/news/bigbear-ai-holdings-will-report-q3-earnings-tomorrow-ahead-of-it-who-owns-bbai-stock)  
  <sub>TipRanks, 1 hour ago</sub>  
  BigBear.ai Holdings ($BBAI) will report Q3 2026 results tomorrow, October 27. Wall Street expects BigBear.ai to report a Q3 loss of $0.05 per share,...
- [Stock offering removes overhang on Meta, says Piper Sandler](https://www.tipranks.com/news/the-fly/stock-offering-removes-overhang-on-meta-says-piper-sandler-thefly-news)  
  <sub>TipRanks, 1 hour ago</sub>  
  Piper Sandler notes that Meta has announced a $35B equity offering and announced plans for a $60B at-the-market program upon the commencement of trading of...
- [Options Volatility and Implied Earnings Moves Today, October 26, 2026](https://www.tipranks.com/news/options-volatility-and-implied-earnings-moves-today-october-26-2026)  
  <sub>TipRanks, 3 hours ago</sub>  
  Today, several major companies are expected to report earnings: Alliance Resource (ARLP), Amkor (AMKR), Cadence Design (CDNS), Celestica (CLS),...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 106.28 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 104.88 (+1.3%), 50d 105.76 (+0.5%), 200d 108.94 (-2.4%); 50d below 200d
Momentum: RSI(14) 65.0 | MACD 0.173 vs signal -0.099 (histogram 0.273)
Returns: 1d +0.0% | 5d +1.0% | 1m +1.7% | 3m -1.3%
52-week range: 103.98 - 112.03 (now 28.6% of the way up)
Volatility: ATR(14) 0.40 (0.4% of price) | annualised 20d 3.7%
Volume: 0.42x the 20-day average
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 177.70M | fund size: 18.89B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro or technical catalyst; positioning and fundamentals remain largely unchanged.

**Main reasons it gave:**
- US Treasury yields fell modestly this week (10‑year down 0.17%)
- CFTC data shows net short on UST bond futures decreased by 4.2% of OI, still at 34% (no material shift)
- Technical indicators (RSI 64.9, MACD positive) show modest bullish momentum but no decisive break
- Fund basics unchanged (yield 5.0%, AA credit quality, stable expense ratio) – no fundamental catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [Weekly Recap: TLT inflows and elevated long-end yields](https://www.tradingview.com/news/tradingview:d40871abdceee:0-weekly-recap-tlt-inflows-and-elevated-long-end-yields/)  
  <sub>TradingView, 4 hours ago</sub>  
  Investors boosted allocations into iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT), shifting cash into long-dated U.S. Treasuries as elevated long-end...
- [Nasdaq Futures Slip Amid Tech Selloff While S&P 500, Dow Edge Higher Ahead Of Crucial Earnings Week: IREN, CRWV, NBIS, MRNA, EWZ In Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-futures-slip-amid-tech-selloff-while-s-and-p-500-dow-edge-higher-ahead-of-crucial-earnings-week-iren-crwv-nbis-mrna-ewz-in-focus/cZUdNRYRBUx)  
  <sub>Stocktwits, 12 hours ago</sub>  
  Technology stocks sold off sharply last week amid growing concerns around artificial intelligence's sustainability and debt woes.
- [RiverNorth/DoubleLine preferreds offer high yie...](https://pluang.com/en/news-feed/peluang-alpha-di-preferred-stock-lagging-opp)  
  <sub>Pluang, 23 hours ago</sub>  
  The RiverNorth/DoubleLine Strategic Opportunity Fund preferred stocks (OPP-A and OPP-B) are trading below par despite strong fundamentals and...
- [AI could push trading of U.S. investment-grade bonds higher – Barclays](https://seekingalpha.com/news/4657251-ai-could-push-trading-of-us-investment-grade-bonds-higher-barclays)  
  <sub>Seeking Alpha, 20 minutes ago</sub>  
  Barclays says AI could lift electronic trading in investment-grade bonds to 65%, boosting efficiency but raising volatility risks.
- [Beyond AI: 5 market rotations to watch](https://www.home.saxo/en-gb/content/articles/equities/beyond-ai-5-market-rotations-to-watch-26102026)  
  <sub>Saxo, 8 hours ago</sub>  
  AI spending is becoming a double-edged sword: Meta was punished for spending more, while Tesla fell despite cutting its investment plans.
- [U.S. underlying growth set to slow after strong private demand in Q3, Pantheon says (SP500:)](https://seekingalpha.com/news/4657160-us-underlying-growth-set-to-slow-after-strong-private-demand-in-q3-pantheon-says)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Pantheon sees Q3 GDP growth near 2.5% as strong private demand masks slowing momentum.
- [Catch The Alpha At The Bottoms: OPP’s Lagging Preferred Stocks](https://seekingalpha.com/article/4957333-catch-alpha-at-bottoms-opp-lagging-preferred-stocks)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  The RiverNorth/DoubleLine Strategic Opportunity Fund preferreds lag TLT's recovery, offering an attractive alpha capture opportunity as spreads narrow.
- [What To Expect In Markets This Week: GOOGL, MSFT, AMZN, INTC, HOOD, LLY Earnings, Fed Meeting And More](https://fr.tradingview.com/news/stocktwits:ef3220335094b:0-what-to-expect-in-markets-this-week-googl-msft-amzn-intc-hood-lly-earnings-fed-meeting-and-more/)  
  <sub>TradingView, 23 hours ago</sub>  
  U.S. markets are heading into one of the busiest weeks of the earnings season, with a fresh batch of corporate results arriving alongside several closely...
- [Bonds Rally Again, Oil Tops $100, Metals Get Slammed, and Paper Palladium Continues to Explode](https://peakprosperity.com/bonds-rally-again-oil-tops-100-metals-get-slammed-and-paper-palladium-continues-to-explode/)  
  <sub>Peak Prosperity, 23 hours ago</sub>  
  Bonds rallied again as yields fell and TLT gained, while crude oil closed above $100. Gold and silver declined sharply, but paper palladium open interest...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.76 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 78.93 (+3.6%), 50d 80.55 (+1.5%), 200d 84.75 (-3.5%); 50d below 200d
Momentum: RSI(14) 64.9 | MACD 0.287 vs signal -0.224 (histogram 0.511)
Returns: 1d +0.5% | 5d +2.9% | 1m +3.1% | 3m -2.9%
52-week range: 77.11 - 92.02 (now 31.2% of the way up)
Volatility: ATR(14) 0.82 (1.0% of price) | annualised 20d 10.8%
Volume: 0.17x the 20-day average
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: ULTRA UST BOND - CHICAGO BOARD OF TRADE (positions as of 2026-10-20, published the following Friday)
Large speculators: net short 34.0% of open interest (2,364,949 contracts)
Change on the week: -4.2% of open interest
Crowding: 45% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 109.70M | fund size: 8.97B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US dollar index flat (+0.01% on the week) – no currency catalyst
- Treasury yields down modestly across the curve – no rate surprise
- Technicals: price near 52‑week high (95.5% of range) but no decisive breakout; RSI 59.9, MACD histogram -0.032
- CFTC positioning: net long 6.4% of OI with weekly increase +2.4% and crowding at 85th percentile – modest bullish bias but high crowding suggests caution
- Fundamentals: 3.2% yield, cash‑only holdings, expense ratio 0.75% – neutral outlook

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.01 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 28.96 (+0.2%), 50d 28.50 (+1.8%), 200d 27.89 (+4.0%); 50d above 200d
Momentum: RSI(14) 59.9 | MACD 0.120 vs signal 0.152 (histogram -0.032)
Returns: 1d +0.2% | 5d +0.0% | 1m +1.4% | 3m +1.5%
52-week range: 26.47 - 29.13 (now 95.5% of the way up)
Volatility: ATR(14) 0.11 (0.4% of price) | annualised 20d 5.0%
Volume: 0.16x the 20-day average
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
Share count change: 1 week: +0.8% (3.57M) over 7d | 1 month: +42.1% (128.34M) over 30d
Shares outstanding: 14.92M | fund size: 432.93M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst consensus 67.6% buy with +18.9% price target (covers only 12% of fund)
- CFTC speculators net short 1.5% decreasing by 1.2% (bullish shift)
- Technical MACD bullish crossover but price below 50‑day SMA and low volume
- No macro surprise; yields down modestly, Fed policy unchanged

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 86.92 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 86.51 (+0.5%), 50d 88.95 (-2.3%), 200d 87.84 (-1.0%); 50d above 200d
Momentum: RSI(14) 47.4 | MACD -0.489 vs signal -0.690 (histogram 0.201)
Returns: 1d +0.8% | 5d +0.6% | 1m -1.9% | 3m -2.6%
52-week range: 77.90 - 93.19 (now 59.0% of the way up)
Volatility: ATR(14) 0.91 (1.0% of price) | annualised 20d 13.3%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

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
Rolled up from the 5 largest holdings, 12.1% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 67.6% | hold 32.4% | sell 0.0% (mean 2.03 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.9% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, SHEL.L, NOVN.SW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-10-20, published the following Friday)
Large speculators: net short 1.5% of open interest (493,553 contracts)
Change on the week: -1.2% of open interest
Crowding: 42% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 282.09M | fund size: 24.52B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technical indicators bearish but no decisive break, analyst view bullish but thin coverage, positioning slightly bearish, fundamentals unchanged.

**Main reasons it gave:**
- Macro: No policy or rate surprise; yields unchanged, normal upward curve
- Technical: Price below 20‑day, 50‑day, 200‑day SMAs; RSI 27.8 (oversold) but no decisive break on volume
- Analyst view: 100% buy rating on top 5 holdings (23.5% weight) with +50% price target, but coverage thin
- Positioning: CFTC net long 2.1% of OI, down 0.7% week‑over‑week, indicating slight bearish sentiment

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 56.48 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 58.86 (-4.0%), 50d 59.75 (-5.5%), 200d 58.32 (-3.2%); 50d above 200d
Momentum: RSI(14) 27.8 | MACD -0.790 vs signal -0.508 (histogram -0.281)
Returns: 1d -0.6% | 5d -2.7% | 1m -6.1% | 3m -2.2%
52-week range: 52.42 - 61.44 (now 45.0% of the way up)
Volatility: ATR(14) 0.66 (1.2% of price) | annualised 20d 14.8%
Volume: 0.32x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 23.5% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +50.1% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 2308.TW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-10-20, published the following Friday)
Large speculators: net long 2.1% of open interest (1,051,211 contracts)
Change on the week: -0.7% of open interest
Crowding: 27% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 1.42B | fund size: 80.10B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [HYG Oct 2026 73.000 put (HYG261030P00073000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/HYG261030P00073000/)  
  <sub>Yahoo! Finance Canada, 9 hours ago</sub>  
  Find the latest HYG Oct 2026 73.000 put (HYG261030P00073000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Rotation Risk and Earnings Discipline | Weekly Options](https://www.moomoo.com/community/feed/rotation-risk-and-earnings-discipline-weekly-options-117506597519366)  
  <sub>Moomoo, 5 hours ago</sub>  
  By Luke Wu | October 26, 2026 Cross-Asset Volatility Broader asset volatility picked up last week, but the pressure is coming from rates and commoditi...
- [Nasdaq futures up 160 points: 5 things to know before Wall Street opens](https://invezz.com/ng/news/2026/10/26/nasdaq-futures-up-160-points-5-things-to-know-before-wall-street-opens/)  
  <sub>Invezz, 2 hours ago</sub>  
  US stock futures were in the green on Monday, with all three indexes seeming set to begin the week on a high at the opening bell.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 77.29 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 77.07 (+0.3%), 50d 78.23 (-1.2%), 200d 79.60 (-2.9%); 50d below 200d
Momentum: RSI(14) 46.2 | MACD -0.311 vs signal -0.403 (histogram 0.092)
Returns: 1d +0.3% | 5d +0.6% | 1m -0.7% | 3m -2.7%
52-week range: 76.81 - 81.28 (now 10.7% of the way up)
Volatility: ATR(14) 0.30 (0.4% of price) | annualised 20d 3.8%
Volume: 0.17x the 20-day average
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 195.60M | fund size: 15.12B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Brazil (EWZ) · Sector or country — BEARISH, confidence 0.75

**Result:** ACCEPTED · 210 shares · submitted sell 210 EWZ @ ~33.36, stop 36.81

**In the model's own words:** no explanation. It wrote only “MACRO”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Lula's re‑election triggers ~27% pre‑market drop in EWZ
- RSI 28.4 and MACD negative signal strong bearish momentum
- Price below 20‑day, 50‑day, and 200‑day SMAs confirms downtrend
- Volume 2.33× 20‑day average indicates heavy selling pressure

<details><summary><b>News</b> — score +0.00</summary>

- [Brazil Stocks Dive As President Lula Wins Re-Election](https://www.investors.com/news/brazil-stocks-dive-as-president-lula-wins-re-election/)  
  <sub>Investor's Business Daily, 3 hours ago</sub>  
  Brazil stocks are diving as President Luiz Inácio Lula da Silva narrowly won re-election Sunday vs. Flávio Bolsonaro.
- [Software & Services ETF (XSW) Hits New 52-Week High](https://ca.finance.yahoo.com/news/software-services-etf-xsw-hits-100000492.html)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  State Street SPDR S&P Software & Services ETF XSW is probably on the radar for investors seeking momentum. The fund just hit a 52-week high and has surged...
- [Brazilian Stocks Set for Record Crash After Lula Win - iShares MSCI Brazil ETF (ARCA:EWZ)](https://www.benzinga.com/markets/latin-america/26/10/62586956/brazilian-stocks-record-crash-lula-election-ewz)  
  <sub>Benzinga, 3 hours ago</sub>  
  Brazilian stocks head for a record crash as EWZ sinks 25% premarket after Lula's run-off win, erasing its 2026 rally. Bank and fintech ADRs lead losses.
- [Brazilian Assets Sold Off: Brazil ETFs Drop Over 27% as Lula’s Re-Election Shatters Fiscal Consolidation Expectations, Bank and Oil Stocks Tumble](https://www.tradingkey.com/analysis/stocks/us-stocks/262239407-brazil-assets-selloff-lula-reelection-etf-banks-oil-stocks-tradingkey)  
  <sub>TradingKey, 2 hours ago</sub>  
  TradingKey - On October 26, Eastern Time, Brazilian President Lula defeated Flávio Bolsonaro in the second round of the presidential election,...
- [The iShares MSCI Brazil ETF gains 1.77%, but daily MACD histogram stays negative](https://en.cryptonomist.ch/2026/10/26/ishares-msci-brazil-etf-closes-42-59/)  
  <sub>The Cryptonomist, 5 hours ago</sub>  
  The iShares MSCI Brazil ETF retains a bullish daily structure, but momentum does not offer unanimous confirmation. EWZ stands above its daily exponential...
- [Nasdaq Futures Slip Amid Tech Selloff While S&P 500, Dow Edge Higher Ahead Of Crucial Earnings Week: IREN, CRWV, NBIS, MRNA, EWZ In Focus](https://www.tradingview.com/news/stocktwits:64f2fdbb0094b:0-nasdaq-futures-slip-amid-tech-selloff-while-s-p-500-dow-edge-higher-ahead-of-crucial-earnings-week-iren-crwv-nbis-mrna-ewz-in-focus/)  
  <sub>TradingView, 12 hours ago</sub>  
  U.S. stock futures tracked mixed overnight late on Sunday, as last week's sharp selloff in technology stocks weighed on the Nasdaq even as markets brace for...
- [Brazil ETFs Crash After Lula Win: Key Trading Signals to Watch on Monday - iShares MSCI Brazil ETF (ARCA](https://www.benzinga.com/etfs/emerging-market-etfs/26/10/62586099/brazil-etfs-lula-win-key-technical-trading-signals)  
  <sub>Benzinga, 3 hours ago</sub>  
  EWZ and FLBR plunged premarket Monday, after Lula's win. Key VWAP signals could reveal a rebound or further downside at market open.
- [Brazil stocks brace for selloff after Lula's win; EWZ ETF falls 27% in premarket](https://invezz.com/news/2026/10/26/brazil-stocks-brace-for-selloff-after-lulas-win-ewz-etf-falls-27-in-premarket/)  
  <sub>Invezz, 4 hours ago</sub>  
  Investors are bracing for heightened volatility across Brazilian financial markets after leftist President Luiz Inácio Lula da Silva secured a surprise...
- [Brazil ETF EWZ Drops 18% as Dollar Nears R$5.50 After Lula’s Reelection](https://t.co/9sbGbK78MI)  
  <sub>Howl.Link, 31 minutes ago</sub>  
  Luiz Inácio Lula da Silva just won his reelection in Brazil, and the financial markets immediately hit the panic button. Financial analyst Rafael pointed...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 33.22 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 41.05 (-19.1%), 50d 38.44 (-13.6%), 200d 37.19 (-10.7%); 50d above 200d
Momentum: RSI(14) 28.4 | MACD 0.426 vs signal 1.151 (histogram -0.724)
Returns: 1d -22.0% | 5d -20.8% | 1m -9.8% | 3m -7.9%
52-week range: 30.48 - 43.54 (now 21.0% of the way up)
Volatility: ATR(14) 1.72 (5.2% of price) | annualised 20d 95.1%
Volume: 2.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.59</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.59</summary>

```text
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.83 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +35.5% above the current prices
Holdings read: VALE3.SA, ITUB4, NU, PETR4, PETR3.SA
Recent rating changes among them:
  - NU: 2026-10-20 UBS: main, Buy -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 200.55M | fund size: 6.66B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst view bullish: 100% buy rating, +42% price target
- Fund flows net outflows of -4.9% over the month
- Technical trend down: price below 20d, 50d, 200d SMAs, RSI 30.7
- Fund fundamentals moderate: P/E 13.9, low yield, no clear catalyst
- Macro unchanged: yields up modestly, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.87 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 87.10 (-6.0%), 50d 90.96 (-10.0%), 200d 92.23 (-11.2%); 50d below 200d
Momentum: RSI(14) 30.7 | MACD -1.533 vs signal -1.316 (histogram -0.217)
Returns: 1d -6.0% | 5d -5.9% | 1m -7.6% | 3m -12.1%
52-week range: 74.25 - 102.94 (now 26.6% of the way up)
Volatility: ATR(14) 2.17 (2.6% of price) | annualised 20d 35.0%
Volume: 0.69x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

```text
Rolled up from the 5 largest holdings, 49.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +42.0% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, PAM
Recent rating changes among them:
  - MELI: 2026-10-13 Citigroup: main, Neutral -> Neutral
  - YPF: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-10-13 UBS: main, Neutral -> Neutral
  - PAM: 2026-09-01 JP Morgan: main, Neutral -> Neutral
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
Share count change: 1 week: +1.6% (10.87M) over 7d | 1 month: -4.9% (-35.55M) over 30d
Shares outstanding: 8.38M | fund size: 686.24M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall despite bullish analyst view and solid fundamentals, because technicals are weak and macro shows no surprise.

**Main reasons it gave:**
- Analyst rating 100% buy with mean 2.17 and price target +3.4% above current price
- Fund flows: net monthly inflow of +1.9% shares but weekly outflow of -0.1%
- Technicals: price below 20‑day SMA (43.99) and 50‑day SMA (44.38), RSI 47.1, volume 0.08× 20‑day average
- Macro: yields up slightly, inflation 3.7% near expectations, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 43.81 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 43.99 (-0.4%), 50d 44.38 (-1.3%), 200d 40.22 (+8.9%); 50d above 200d
Momentum: RSI(14) 47.1 | MACD -0.060 vs signal -0.031 (histogram -0.028)
Returns: 1d +0.7% | 5d -0.6% | 1m -2.3% | 3m +6.2%
52-week range: 32.56 - 45.76 (now 85.2% of the way up)
Volatility: ATR(14) 0.67 (1.5% of price) | annualised 20d 21.4%
Volume: 0.08x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 47.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.17 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +3.4% above the current prices
Holdings read: PKO.WA, PKN.WA, PEO.WA, PZU.WA, ALE.WA
Recent rating changes among them: none reported
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
Share count change: 1 week: -0.1% (-743.37K) over 7d | 1 month: +1.9% (15.24M) over 30d
Shares outstanding: 18.93M | fund size: 829.42M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall call; no macro surprise, flat fund flows, modestly bearish analyst view, technicals slightly bullish but low volume, fundamentals moderate.

**Main reasons it gave:**
- Analyst view: 40.5% sell rating, weighted price target -7% (slightly bearish)
- Fund flows: flat net creations/redemptions (0% change) over past week and month
- Technicals: price above 20‑day SMA (+2.2%) and MACD positive, but volume only 0.26× 20‑day average
- Macro: US yields fell modestly, no policy surprise, VIX unchanged (neutral risk environment)
- Fundamentals: moderate valuation (P/E 20.3), 3% dividend yield, strong 3‑year performance (+16%/yr)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.29 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 28.66 (+2.2%), 50d 29.15 (+0.5%), 200d 28.83 (+1.6%); 50d above 200d
Momentum: RSI(14) 58.1 | MACD 0.061 vs signal -0.051 (histogram 0.112)
Returns: 1d +0.6% | 5d +1.6% | 1m +3.0% | 3m -0.1%
52-week range: 24.95 - 30.43 (now 79.2% of the way up)
Volatility: ATR(14) 0.30 (1.0% of price) | annualised 20d 11.9%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

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

<details><summary><b>What analysts and big funds say</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.20</summary>

```text
Rolled up from the 5 largest holdings, 45.9% of the fund by weight
Ratings by weight: buy 0.0% | hold 59.5% | sell 40.5% (mean 3.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -7.0% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 63.60M | fund size: 1.86B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Most macro and fund‑flow signals are neutral; technicals show modest upside but low volume; analyst coverage is modestly bullish (+2.9% price target) while fundamentals are solid but not a catalyst.

**Main reasons it gave:**
- Analyst coverage of top holdings: 79.8% buy, weighted price target +2.9% above current price
- Technicals: price above 20‑day and 50‑day SMA, RSI 56.5, MACD positive, but volume at 0.31× 20‑day average
- Fund flows flat over past month (0% change in share count)
- Macro: US Treasury yields down modestly, no policy surprise; VIX stable at 18.3

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 60.83 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 59.60 (+2.1%), 50d 60.48 (+0.6%), 200d 58.18 (+4.5%); 50d above 200d
Momentum: RSI(14) 56.5 | MACD 0.259 vs signal 0.028 (histogram 0.231)
Returns: 1d +0.2% | 5d +0.9% | 1m +2.1% | 3m +1.7%
52-week range: 49.72 - 62.64 (now 86.0% of the way up)
Volatility: ATR(14) 0.68 (1.1% of price) | annualised 20d 14.5%
Volume: 0.31x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 29.3% of the fund by weight
Ratings by weight: buy 79.8% | hold 20.2% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +2.9% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 94.80M | fund size: 5.77B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, flat fund flows, mixed technical signals, and a bullish analyst view that is not enough to shift the overall stance.

**Main reasons it gave:**
- Fund flows flat: 0% share count change over week and month
- Analyst coverage 28.9% of fund weight, 100% buy rating with +15.6% price target
- Technicals: price 0.3% above 20‑day SMA but 1.6% below 50‑day SMA, RSI 47.5, low volume (0.13× 20‑day avg)
- Macro: yields down modestly, curve normal, VIX 18.3 (elevated but stable)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 50.68 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 50.51 (+0.3%), 50d 51.66 (-1.9%), 200d 51.49 (-1.6%); 50d above 200d
Momentum: RSI(14) 47.5 | MACD -0.189 vs signal -0.247 (histogram 0.058)
Returns: 1d +0.6% | 5d -0.4% | 1m -1.6% | 3m -1.3%
52-week range: 45.38 - 54.72 (now 56.7% of the way up)
Volatility: ATR(14) 0.66 (1.3% of price) | annualised 20d 13.7%
Volume: 0.13x the 20-day average
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.96 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.6% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 7.65M | fund size: 387.70M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Macro: yields fell across curve, no policy surprise (Fed target unchanged)
- Fund flows flat: share count unchanged (+0.0% week, +0.0% month)
- Technical: price above 20‑day SMA (+0.5%) but below 50‑day (-2.4%) and 200‑day (-1.9%) SMA, low volume (0.2× 20‑day avg)
- Analyst view: 78.7% buy rating on top holdings (45.4% weight) with +21.5% price target
- Fundamentals: P/E 17.6, dividend yield 2%, 3‑yr annualized return 19.8%

<details><summary><b>News</b> — score +0.00</summary>

- [European stocks edge higher to kick off busy central bank week](https://seekingalpha.com/news/4657032-european-stocks-edge-higher-to-kick-off-busy-central-bank-week)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  European equity markets traded slightly higher on Monday, with both the STOXX 50 and STOXX 600 gaining 0.3% as investors prepared for a heavy week of policy...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 41.46 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 41.24 (+0.5%), 50d 42.47 (-2.4%), 200d 42.27 (-1.9%); 50d above 200d
Momentum: RSI(14) 48.2 | MACD -0.264 vs signal -0.355 (histogram 0.091)
Returns: 1d +1.3% | 5d +1.0% | 1m -1.9% | 3m -1.1%
52-week range: 38.08 - 44.59 (now 51.8% of the way up)
Volatility: ATR(14) 0.51 (1.2% of price) | annualised 20d 15.1%
Volume: 0.20x the 20-day average
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
Three-year record: +19.8% a year | beta to the market 0.98
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 45.4% of the fund by weight
Ratings by weight: buy 78.7% | hold 21.3% | sell 0.0% (mean 1.96 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.5% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 79.50M | fund size: 3.30B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: technicals show a downtrend with price below key moving averages and weak momentum, while analyst coverage is strongly bullish and fundamentals are modestly positive. No macro surprise or decisive technical break on heavy volume, and fund flows are flat, leading to a neutral stance.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs (downtrend)
- RSI 38.1 and low volume indicating weak momentum
- Analyst view 100% buy with +23% price target (bullish)
- Fund flows flat over past month (no net inflows/outflows)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 55.69 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 56.62 (-1.6%), 50d 59.60 (-6.6%), 200d 58.13 (-4.2%); 50d above 200d
Momentum: RSI(14) 38.1 | MACD -1.199 vs signal -1.229 (histogram 0.030)
Returns: 1d +1.3% | 5d +0.5% | 1m -7.8% | 3m -7.9%
52-week range: 50.70 - 63.35 (now 39.4% of the way up)
Volatility: ATR(14) 0.82 (1.5% of price) | annualised 20d 19.7%
Volume: 0.16x the 20-day average
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
Weighted price target: +23.0% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 8.55M | fund size: 476.11M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise, mixed technicals, modest insider positioning, and thin analyst coverage.

**Main reasons it gave:**
- Fed target unchanged at 4.00% and yields down modestly
- Price below 20‑day and 50‑day SMAs, RSI 41.4, MACD negative
- CFTC net long 2.3% of OI, +4.7% change, crowding 28th percentile
- Analyst coverage thin (17% weight) despite 100% buy rating and +31% price target

<details><summary><b>News</b> — score +0.00</summary>

- [Tech sell-off pressures Asian stocks, eyes on key central bank decisions and mega-cap earnings](https://seekingalpha.com/news/4657017-tech-sell-off-pressures-asian-stocks-ahead-of-central-bank-policy-week)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  Asian markets slip as AI and chip stocks retreat before Fed, ECB, BOJ decisions and big tech earnings.
- [Nikkei 225 outlook ahead of key Japan earnings, BoJ decision](https://invezz.com/au/news/2026/10/26/nikkei-225-outlook-ahead-of-key-japan-earnings-boj-decision/)  
  <sub>Invezz, 10 hours ago</sub>  
  The Nikkei 225 Index Index remained on edge on Monday morning as investors waited for key corporate earnings and the Bank of Japan (BoJ) interest rate...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 94.71 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 96.64 (-2.0%), 50d 96.64 (-2.0%), 200d 91.60 (+3.4%); 50d above 200d
Momentum: RSI(14) 41.4 | MACD -0.663 vs signal -0.342 (histogram -0.321)
Returns: 1d +0.6% | 5d -0.3% | 1m -3.3% | 3m +5.4%
52-week range: 79.49 - 99.32 (now 76.8% of the way up)
Volatility: ATR(14) 1.22 (1.3% of price) | annualised 20d 12.3%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +31.0% above the current prices
Holdings read: 8306.T, 7203.T, 8035.T, 8316.T, 6857.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-20, published the following Friday)
Large speculators: net long 2.3% of open interest (25,143 contracts)
Change on the week: +4.7% of open interest
Crowding: 28% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 227.85M | fund size: 21.58B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise, flat fund flows, and modest bullish technicals with low volume. Analyst view is moderately bullish but not enough to shift the overall stance.

**Main reasons it gave:**
- Flat fund flows: share count unchanged over 1 week and 1 month
- Technical momentum bullish (RSI 65, MACD positive) but volume only 0.16x 20‑day average
- Analyst view: 64.8% buy rating, weighted price target +4.2% above current price
- Fundamentals solid (P/E 24.08, yield 1.8%) but not a catalyst
- Macro unchanged: yields down modestly, inflation 3.7% above target, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 63.17 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 60.82 (+3.9%), 50d 61.55 (+2.6%), 200d 61.72 (+2.4%); 50d below 200d
Momentum: RSI(14) 65.0 | MACD 0.643 vs signal 0.216 (histogram 0.427)
Returns: 1d +0.2% | 5d +1.9% | 1m +4.1% | 3m -0.1%
52-week range: 55.06 - 65.08 (now 81.0% of the way up)
Volatility: ATR(14) 0.64 (1.0% of price) | annualised 20d 14.4%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

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
Rolled up from the 5 largest holdings, 48.2% of the fund by weight
Ratings by weight: buy 64.8% | hold 35.2% | sell 0.0% (mean 2.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.2% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 28.62M | fund size: 1.81B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall due to lack of macro surprise, weak technicals, and flat fund flows despite bullish analyst coverage limited to <50% of the fund.

**Main reasons it gave:**
- Price 64.22 below 20‑day SMA 66.04 (-2.8%) and 50‑day SMA 67.39 (-4.7%)
- RSI 37.7 indicating weak momentum
- Flat fund flows (0% change week and month) showing no net demand
- No macro surprise; yields down modestly, VIX unchanged at 18.30

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 64.22 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 66.04 (-2.8%), 50d 67.39 (-4.7%), 200d 64.96 (-1.1%); 50d above 200d
Momentum: RSI(14) 37.7 | MACD -0.919 vs signal -0.753 (histogram -0.166)
Returns: 1d +0.7% | 5d -0.8% | 1m -5.6% | 3m -1.4%
52-week range: 55.33 - 71.61 (now 54.6% of the way up)
Volatility: ATR(14) 0.91 (1.4% of price) | annualised 20d 17.5%
Volume: 0.02x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

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
Rolled up from the 5 largest holdings, 46.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.59 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +48.6% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 5.55M | fund size: 356.42M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no news, flat flows, no macro surprise, technicals weak but not decisive, modestly positive analyst view and fundamentals.

**Main reasons it gave:**
- Analyst ratings: 51.5% buy, 48.5% hold, weighted price target +11% above price
- Fund flows flat: share count unchanged over 1 month
- Technical: price 1.3% below 20‑day SMA, RSI 38.5, volume 0.08× 20‑day average
- Macro: Treasury yields fell modestly, no policy surprise, VIX 18.3 (elevated but stable)
- Fundamentals: P/E 15.94, three‑year return +33.8% per year, yield 2.8%

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 57.45 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 58.18 (-1.3%), 50d 60.39 (-4.9%), 200d 57.92 (-0.8%); 50d above 200d
Momentum: RSI(14) 38.5 | MACD -0.761 vs signal -0.801 (histogram 0.040)
Returns: 1d -0.1% | 5d +0.2% | 1m -6.1% | 3m -5.0%
52-week range: 49.37 - 63.23 (now 58.3% of the way up)
Volatility: ATR(14) 0.80 (1.4% of price) | annualised 20d 16.0%
Volume: 0.08x the 20-day average
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
Three-year record: +33.8% a year | beta to the market 0.88
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
Ratings by weight: buy 51.5% | hold 48.5% | sell 0.0% (mean 2.32 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.0% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 37.35M | fund size: 2.15B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: yields up modestly, inflation 3.7% in line with expectations
- Flat fund flows: share count unchanged over week and month
- Technical momentum bearish: MACD negative, RSI 40.1, price below 20‑day and 50‑day SMA
- Analyst consensus: 100% buy rating with +43.5% price target for top holdings

<details><summary><b>News</b> — score +0.00</summary>

- [EWT Nov 2026 106.000 call (EWT261120C00106000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/EWT261120C00106000/)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Find the latest EWT Nov 2026 106.000 call (EWT261120C00106000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 105.82 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 111.40 (-5.0%), 50d 110.15 (-3.9%), 200d 92.54 (+14.3%); 50d above 200d
Momentum: RSI(14) 40.1 | MACD -1.557 vs signal -0.497 (histogram -1.061)
Returns: 1d +0.9% | 5d -1.3% | 1m -7.8% | 3m +12.6%
52-week range: 60.03 - 118.00 (now 79.0% of the way up)
Volatility: ATR(14) 2.40 (2.3% of price) | annualised 20d 28.2%
Volume: 0.37x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

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
Rolled up from the 5 largest holdings, 39.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.35 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +43.5% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 85.00M | fund size: 8.99B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise, technicals mixed, analyst view bullish but not decisive, flows flat, fundamentals modestly positive

**Main reasons it gave:**
- Technical: price above 20‑day and 50‑day SMAs, MACD positive, but below 200‑day SMA, low volume
- Analyst view: 90.9% buy rating, weighted price target +6.6% above current price
- Fund flows: flat share count, indicating neutral demand
- Macro: Treasury yields stable, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 75.61 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 73.21 (+3.3%), 50d 74.46 (+1.5%), 200d 76.11 (-0.7%); 50d below 200d
Momentum: RSI(14) 59.7 | MACD 0.453 vs signal 0.045 (histogram 0.408)
Returns: 1d +0.5% | 5d +0.3% | 1m +3.1% | 3m -1.5%
52-week range: 65.37 - 81.23 (now 64.6% of the way up)
Volatility: ATR(14) 1.26 (1.7% of price) | annualised 20d 17.1%
Volume: 0.45x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

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
Rolled up from the 5 largest holdings, 47.8% of the fund by weight
Ratings by weight: buy 90.9% | hold 9.1% | sell 0.0% (mean 2.13 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.6% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 18.90M | fund size: 1.43B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Flat fund flows (0% change) indicating no net demand
- Technical indicators show price below 20‑day, 50‑day, and 200‑day SMAs and RSI 37, but no decisive break on heavy volume
- Macro data shows no surprise: inflation 3.7% near target, Fed unchanged, yields modestly up
- Tech sell‑off pressures Asian stocks, weighing on EWY's technology‑heavy holdings

<details><summary><b>News</b> — score +0.00</summary>

- [KORU: South Korea's Daily Returns, Amplified By A Factor Of 3x](https://seekingalpha.com/article/4952305-koru-south-koreas-daily-returns-amplified-by-factor-of-3x)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  The Direxion Daily MSCI South Korea Bull 3x ETF offers 3x daily leveraged exposure to the MSCI Korea 25/50 Index, targeting active traders with good risk...
- [EWY Oct 2026 155.000 call (EWY261030C00155000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/EWY261030C00155000/chart/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Interactive Chart for EWY Oct 2026 155.000 call (EWY261030C00155000), analyze all the data with a huge range of indicators.
- [SK Hynix Q3 Preview: Record Profits, Bottom Valuation — What Could Reignite the Rally?](https://www.moomoo.com/community/feed/sk-hynix-q3-preview-record-profits-bottom-valuation-what-could-117505816395782)  
  <sub>Moomoo, 9 hours ago</sub>  
  SK hynix (SKHY.US)$ will release its fiscal third-quarter results for 2026 on October 28. Since listing on the Nasdaq in mid-July 2026, the stock has...
- [Tech sell-off pressures Asian stocks, eyes on key central bank decisions and mega-cap earnings](https://seekingalpha.com/news/4657017-tech-sell-off-pressures-asian-stocks-ahead-of-central-bank-policy-week)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  Asian markets slip as AI and chip stocks retreat before Fed, ECB, BOJ decisions and big tech earnings.
- [How to Invest in South Korean Stocks from Singapore (2026 Guide)](https://www.smallcapasia.com/how-to-invest-in-south-korean-stocks-from-singapore-2026-guide/)  
  <sub>SmallCap Asia, 6 hours ago</sub>  
  This article is for educational purposes only and does not constitute financial advice or a recommendation to buy or sell any security. Investors should.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 153.38 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 169.36 (-9.4%), 50d 176.77 (-13.2%), 200d 161.65 (-5.1%); 50d above 200d
Momentum: RSI(14) 37.0 | MACD -8.238 vs signal -6.333 (histogram -1.905)
Returns: 1d +1.4% | 5d -2.0% | 1m -18.1% | 3m +1.3%
52-week range: 88.53 - 219.20 (now 49.6% of the way up)
Volatility: ATR(14) 6.08 (4.0% of price) | annualised 20d 43.2%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 75.60M | fund size: 11.60B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, flat fund flows, price below key moving averages, and no decisive technical breakout despite bullish analyst consensus.

**Main reasons it gave:**
- Flat fund flows (0% change over 1 week and 1 month)
- Price below 20‑day, 50‑day, and 200‑day SMAs
- No macro surprise in recent data (inflation 3.7% in line with expectations, Fed target unchanged)
- Analyst consensus 100% buy with +35.7% price target but no decisive technical breakout

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 63.78 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 63.91 (-0.2%), 50d 67.26 (-5.2%), 200d 68.73 (-7.2%); 50d below 200d
Momentum: RSI(14) 44.1 | MACD -0.698 vs signal -0.846 (histogram 0.147)
Returns: 1d +1.0% | 5d -1.3% | 1m -4.1% | 3m +2.9%
52-week range: 60.43 - 81.60 (now 15.8% of the way up)
Volatility: ATR(14) 1.20 (1.9% of price) | annualised 20d 21.7%
Volume: 0.36x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

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
Rolled up from the 5 largest holdings, 43.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.04 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +35.7% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 7.90M | fund size: 503.86M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; technicals are bearish but no decisive macro catalyst, analyst view remains bullish, and modest outflows suggest mixed sentiment.

**Main reasons it gave:**
- Price below 20‑day, 50‑day, and 200‑day SMAs (downtrend)
- RSI 36.7 and MACD negative, indicating bearish momentum
- Net outflow of ~1% over the past month (money going out)
- Analyst consensus still buy with +24.3% price target, but three top holdings downgraded to Hold
- No macro surprise; yields stable and VIX unchanged

<details><summary><b>News</b> — score +0.00</summary>

- [2026 Tax-Loss Harvesting Opportunities With VanEck ETFs](https://seekingalpha.com/article/4957428-2026-tax-loss-harvesting-opportunities-with-vaneck-etfs)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Tax-loss harvesting may work best when you swap into a similar, not identical, fund to stay compliant with the wash-sale rule. We screened US-listed ETFs...
- [Gold Miners Go From Record Month to Washout in 21 Sessions](https://beincrypto.com/gold-miners-etf-oversold-since-july/)  
  <sub>BeInCrypto, 9 hours ago</sub>  
  Nearly 92% of stocks in the VanEck Gold Miners ETF (GDX) now trade below their 50-day moving average. The share last ran this high in late July,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 81.07 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 86.23 (-6.0%), 50d 92.69 (-12.5%), 200d 90.89 (-10.8%); 50d above 200d
Momentum: RSI(14) 36.7 | MACD -2.513 vs signal -2.017 (histogram -0.496)
Returns: 1d +1.1% | 5d -6.2% | 1m -12.7% | 3m +9.2%
52-week range: 68.28 - 115.84 (now 26.9% of the way up)
Volatility: ATR(14) 2.98 (3.7% of price) | annualised 20d 37.9%
Volume: 0.37x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

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
Rolled up from the 5 largest holdings, 40.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.71 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.3% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, FNV.TO
Recent rating changes among them:
  - NEM: 2026-10-22 Freedom Broker: down, Buy -> Hold
  - AEM.TO: 2026-10-22 Freedom Broker: down, Buy -> Hold
  - ABX.TO: 2026-10-22 Freedom Broker: down, Buy -> Hold
  - WPM.TO: 2026-10-08 UBS: main, Buy -> Buy
  - FNV.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
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
Share count change: 1 week: +1.9% (471.83M) over 7d | 1 month: -1.0% (-255.72M) over 30d
Shares outstanding: 319.98M | fund size: 25.94B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals modestly bullish but low volume, flat fund flows, analyst view positive but limited coverage.

**Main reasons it gave:**
- US Treasury yields down slightly across the curve, no rate surprise
- Technicals show price above 20‑day, 50‑day, 200‑day SMAs but low volume (0.24x 20‑day avg) and modest momentum (RSI 59, MACD barely positive)
- Fund flows flat over the past week and month, indicating no net demand shift
- Analyst coverage of top holdings uniformly buy with a +16.5% price target, covering 42.9% of the fund

<details><summary><b>News</b> — score +0.00</summary>

- [iShares Tech-Software ETF (IGV) Sells $30.1 Million More Palantir on Thursday](https://finance.yahoo.com/markets/stocks/articles/ishares-tech-software-etf-igv-110408734.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. In Thursday's session, zero ETFs were buying versus one selling, as iShares Expanded Tech-Software Sector ETF...
- [Software ETFs: Hidden Gems Amid the AI Selloff?](https://www.tradingview.com/news/zacks:a4dbe975f094b:0-software-etfs-hidden-gems-amid-the-ai-selloff/)  
  <sub>TradingView, 4 hours ago</sub>  
  U.S. software stocks surged last week, erasing fears of a broad-based tech sector selloff. State Street Technology Select Sector SPDR ETF XLK fell 1.8% last...
- [Beyond AI: 5 market rotations to watch](https://www.home.saxo/content/articles/equities/beyond-ai-5-market-rotations-to-watch-26102026)  
  <sub>Saxo, 8 hours ago</sub>  
  AI spending is becoming a double-edged sword: Meta was punished for spending more, while Tesla fell despite cutting its investment plans.
- [The Technical Signals Behind (IGV) That Institutions Follow](https://news.stocktradersdaily.com/news_releases/The_Technical_Signals_Behind_IGV_That_Institutions_Follow_102526073602_1792971362.html)  
  <sub>Stock Traders Daily, 19 hours ago</sub>  
  Price-action only: Ishares Expanded Tech-software Sector Etf (IGV) movements set the tone for institutional models. The Technical Signals Behind (IGV) That...
- [This Week's Market Watch (October 26 - October 30)](https://www.moomoo.com/community/feed/this-week-s-market-watch-october-26-october-30-117506467233798)  
  <sub>Moomoo, 6 hours ago</sub>  
  AI Selloff: Verdict Week — 4 Tests in 5 Days Last week, AI stocks were hit by a concentrated selloff — hedge funds dumped tech at -3.3 standard devi...
- [ETFs Are Net Sellers of CrowdStrike (CRWD) on Oct. 22](https://www.gurufocus.com/news/9141954/etfs-are-net-sellers-of-crowdstrike-crwd-on-oct-22)  
  <sub>GuruFocus, 4 hours ago</sub>  
  IGV led the move, cutting its CrowdStrike (CRWD) stake by 2.27%, as ETF activity on Thursday produced a net $15.2 million in selling.
- [ETFs Are Net Sellers of Oracle (ORCL) on Oct. 22](https://finance.yahoo.com/markets/stocks/articles/etfs-net-sellers-oracle-orcl-110303262.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. IGV drove the day's ETF activity in Oracle (ORCL), as funds sold a net $10.7 million of the stock on Thursday.
- [ETFs Are Net Sellers of Palo Alto Networks (PANW) on Oct. 22](https://www.gurufocus.com/news/9141955/etfs-are-net-sellers-of-palo-alto-networks-panw-on-oct-22)  
  <sub>GuruFocus, 4 hours ago</sub>  
  In Thursday's session, 45 ETFs were buying Palo Alto Networks (PANW) shares versus 15 selling, yet ETF activity was net negative by dollar value,...
- [Stocktwits Tech Watch: More Big Earnings, Apple’s Touch-Screen MacBook And Intel Results In Focus](https://www.tradingview.com/news/stocktwits:b1e5e150e094b:0-stocktwits-tech-watch-more-big-earnings-apple-s-touch-screen-macbook-and-intel-results-in-focus/)  
  <sub>TradingView, 6 hours ago</sub>  
  The market will enter the thick of the third-quarter earnings season this week, with Big Tech heavyweights Microsoft (MSFT), Alphabet (GOOGL), Amazon (AMZN)...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 111.84 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 108.90 (+2.7%), 50d 106.46 (+5.1%), 200d 93.86 (+19.2%); 50d above 200d
Momentum: RSI(14) 59.3 | MACD 0.977 vs signal 0.962 (histogram 0.015)
Returns: 1d +1.1% | 5d +5.5% | 1m +5.5% | 3m +21.9%
52-week range: 74.67 - 117.08 (now 87.6% of the way up)
Volatility: ATR(14) 2.70 (2.4% of price) | annualised 20d 28.8%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

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
Rolled up from the 5 largest holdings, 42.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.5% above the current prices
Holdings read: PANW, PLTR, CRWD, MSFT, ORCL
Recent rating changes among them:
  - PANW: 2026-10-15 Citigroup: main, Buy -> Buy
  - PLTR: 2026-10-23 Piper Sandler: main, Overweight -> Overweight
  - CRWD: 2026-10-22 Mizuho: main, Outperform -> Outperform
  - MSFT: 2026-10-26 Scotiabank: main, Sector Outperform -> Sector Outperform
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 12.50M | fund size: 1.40B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst view on a thin slice of the fund, bearish outflows, neutral fundamentals, no macro surprise, and technicals showing no decisive break.

**Main reasons it gave:**
- Fund flows: -11.2% share count over 1 month (outflows)
- Analyst view: 100% buy rating on 23.7% of fund, weighted price target +29.4%
- Technicals: price below 50‑day and 200‑day SMA, RSI 45.4, no decisive break
- Macro: US Treasury yields up slightly, VIX 18.30 (no surprise)

<details><summary><b>News</b> — score +0.00</summary>

- [Trading Systems Reacting to (INDA) Volatility](https://www.google.com/goto?url=CAEStgEB6zswFa-PEBA4-2gHFK8AyTymBHqghGF2U-55S9ui5HnR-aqBoYhjTzYjEFUgOGDtYENSAexvwQuZ-icNQ33t1MZY7sjgm5uRvnXgjhlxBAVbxASM0DR6LIOUDeFQbUFKjyRMzacBo_ApDiaXqpLNRU3VLu1RbSvhaeStQDYi-gOan2hjgsZ3PpnXYArtHARsqeqEnJ7sORGyz1NEdruWNTUbR2-qJpHkojtixWFzZHO7cF52cg)  
  <sub>Stock Traders Daily, 19 hours ago</sub>  
  Price-action only: Ishares Msci India Etf (INDA) movements set the tone for institutional models. Trading Systems Reacting to (INDA) Volatility.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 46.83 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 46.84 (-0.0%), 50d 48.07 (-2.6%), 200d 49.30 (-5.0%); 50d below 200d
Momentum: RSI(14) 45.4 | MACD -0.218 vs signal -0.296 (histogram 0.078)
Returns: 1d +0.8% | 5d -1.2% | 1m -2.2% | 3m -5.2%
52-week range: 45.42 - 54.83 (now 14.9% of the way up)
Volatility: ATR(14) 0.53 (1.1% of price) | annualised 20d 16.3%
Volume: 0.37x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 23.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.35 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +29.4% above the current prices
Holdings read: HDFCBANK.NS, ICICIBANK.NS, RELIANCE.NS, BHARTIARTL.NS, INFY.NS
Recent rating changes among them: none reported
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
Direction: money going out (1 month)
Share count change: 1 week: -0.4% (-26.13M) over 7d | 1 month: -11.2% (-729.99M) over 30d
Shares outstanding: 123.52M | fund size: 5.78B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst coverage (+0.45) vs bearish fund outflows (-0.35) and modestly negative fundamentals (-0.10) net to neutral.

**Main reasons it gave:**
- Fund flows show net outflows of -5.9% over the past month (12.22B fund size)
- Technical indicators show price below 20‑day, 50‑day, and 200‑day SMAs and RSI 42.3, indicating a downtrend
- Analyst coverage of top holdings (53.9% weight) is 100% buy with a +29.3% price target
- Macro data shows no surprise; yields stable, curve normal, VIX at 18.3 (elevated but unchanged)

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs to Buy as Lockheed Shares Jump Post Q3 Earnings Beat, Record Backlog](https://www.tradingview.com/news/zacks:8a0e78644094b:0-etfs-to-buy-as-lockheed-shares-jump-post-q3-earnings-beat-record-backlog/)  
  <sub>TradingView, 4 hours ago</sub>  
  Shares of Lockheed Martin LMT have gained 9.6% following the defense giant's better-than-expected third-quarter 2026 results on Oct. 22.
- [JEDI: A High-Risk Bet On Defense Tech Growth (NYSEARCA:JEDI)](https://seekingalpha.com/article/4957417-jedi-a-high-risk-bet-on-defense-tech-growth)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Defiance Drone and Modern Warfare ETF offers high-growth defense tech exposure but carries elevated risk due to its focus on emerging,...
- [BioNTech, Bristol Myers announces data from Phase 2 ROSETTA Lung-107 trial](https://www.tipranks.com/news/the-fly/biontech-bristol-myers-announces-data-from-phase-2-rosetta-lung-107-trial-thefly-news)  
  <sub>TipRanks, 18 hours ago</sub>  
  BioNTech (BNTX) and Bristol Myers Squibb Company (BMY) announced first data from the global Phase 2 ROSETTA Lung-107 clinical trial evaluating pumitamig,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 205.98 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 206.27 (-0.1%), 50d 217.67 (-5.4%), 200d 229.46 (-10.2%); 50d below 200d
Momentum: RSI(14) 42.3 | MACD -3.331 vs signal -4.007 (histogram 0.676)
Returns: 1d +1.9% | 5d -0.9% | 1m -3.7% | 3m -15.9%
52-week range: 198.23 - 253.22 (now 14.1% of the way up)
Volatility: ATR(14) 4.07 (2.0% of price) | annualised 20d 15.3%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

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
Rolled up from the 5 largest holdings, 53.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +29.3% above the current prices
Holdings read: GE, RTX, BA, HWM, LMT
Recent rating changes among them:
  - GE: 2026-10-21 UBS: main, Buy -> Buy
  - RTX: 2026-10-21 UBS: main, Neutral -> Neutral
  - BA: 2026-10-19 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - HWM: 2026-10-15 RBC Capital: main, Outperform -> Outperform
  - LMT: 2026-10-26 Morgan Stanley: up, Equal-Weight -> Overweight
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
Share count change: 1 week: -0.2% (-18.90M) over 7d | 1 month: -5.9% (-763.37M) over 30d
Shares outstanding: 59.34M | fund size: 12.22B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; analyst view is bullish but not supported by macro or technical catalysts, flows are flat, fundamentals are moderate.

**Main reasons it gave:**
- Analyst coverage: 100% buy rating for 51.6% of fund weight, weighted price target +27.2% above current price
- Technical indicators: price above 20‑day SMA and MACD above signal, but below 50‑day and 200‑day SMA with low volume (0.16× 20‑day average)
- Macro environment: modest yield declines, inflation 3.7% and unemployment 4.2% near expectations, no policy surprise
- Fund flows: share count flat over the past week and month, indicating no net inflows or outflows

<details><summary><b>News</b> — score +0.00</summary>

- [Trading the Move, Not the Narrative: (IYT) Edition](https://news.stocktradersdaily.com/news_release/98/Trading_the_Move,_Not_the_Narrative:_IYT_Edition_102526080001_1792972801.html)  
  <sub>Stock Traders Daily, 19 hours ago</sub>  
  Key findings for Ishares U.s. Transportation Etf (NYSE: IYT). Neutral Near and Mid-Term Readings Could Moderate Long-Term Positive Bias...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 80.65 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 79.90 (+0.9%), 50d 81.93 (-1.6%), 200d 81.62 (-1.2%); 50d above 200d
Momentum: RSI(14) 50.5 | MACD -0.252 vs signal -0.533 (histogram 0.281)
Returns: 1d +0.6% | 5d +1.6% | 1m +1.6% | 3m -7.3%
52-week range: 68.14 - 90.01 (now 57.2% of the way up)
Volatility: ATR(14) 1.37 (1.7% of price) | annualised 20d 17.6%
Volume: 0.16x the 20-day average
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
Three-year record: +14.2% a year | beta to the market 1.32
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
Weighted price target: +27.2% above the current prices
Holdings read: UNP, UBER, CSX, DAL, UAL
Recent rating changes among them:
  - UNP: 2026-10-23 Citigroup: main, Buy -> Buy
  - UBER: 2026-10-16 Guggenheim: reit, Buy -> Buy
  - CSX: 2026-10-23 Citigroup: main, Neutral -> Neutral
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 2.80M | fund size: 225.83M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as technicals are bullish but on low volume, analyst view is modestly bullish on a thin slice, fundamentals are moderately positive, while fund flows show notable outflows indicating bearish demand. No macro surprise or decisive technical break is present.

**Main reasons it gave:**
- Technicals: price above 20‑day, 50‑day, and 200‑day SMAs with bullish MACD but volume only 0.26× 20‑day average
- Analyst view: 59.8% buy rating and +9.7% price target on 5.7% of fund weight
- Fund flows: -5.2% share count in 1 week and -7.5% in 1 month indicating outflows
- Macro: Treasury yields down slightly, no policy surprise, VIX stable

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 73.18 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 70.16 (+4.3%), 50d 72.27 (+1.3%), 200d 70.88 (+3.3%); 50d above 200d
Momentum: RSI(14) 62.4 | MACD -0.032 vs signal -0.611 (histogram 0.579)
Returns: 1d +1.0% | 5d +5.7% | 1m +2.3% | 3m -4.7%
52-week range: 58.63 - 77.93 (now 75.4% of the way up)
Volatility: ATR(14) 1.27 (1.7% of price) | annualised 20d 18.0%
Volume: 0.26x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 5.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 59.8% | hold 40.2% | sell 0.0% (mean 2.24 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.7% above the current prices
Holdings read: UBSI, FIBK, ONB, HWC, EWBC
Recent rating changes among them:
  - UBSI: 2026-10-26 Piper Sandler: main, Overweight -> Overweight
  - FIBK: 2026-10-05 Barclays: main, Underweight -> Underweight
  - ONB: 2026-10-22 TD Cowen: main, Buy -> Buy
  - HWC: 2026-10-21 Keefe, Bruyette & Woods: main, Market Perform -> Market Perform
  - EWBC: 2026-10-22 Citigroup: main, Buy -> Buy
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
Share count change: 1 week: -5.2% (-205.91M) over 7d | 1 month: -7.5% (-307.73M) over 30d
Shares outstanding: 51.52M | fund size: 3.77B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals lack a decisive break, and while analyst sentiment and fund flows are positive, they are insufficient to tilt the overall view.

**Main reasons it gave:**
- US Treasury yields fell modestly across the curve, no policy surprise
- Technical indicators show downtrend with RSI 26 (oversold) but volume below average, no decisive break
- Analyst coverage: 90.3% buy rating and +23.5% price target, indicating bullish sentiment
- Fund flows: share count increased 4.5% over the past week, showing net inflows

<details><summary><b>News</b> — score +0.00</summary>

- [investingLive Asia-Pacific market news: Brazil ETF slumps on Lula win](https://investinglive.com/news/investinglive-asia-pacific-market-news-brazil-etf-slumps-on-lula-win/)  
  <sub>investingLive, 11 hours ago</sub>  
  Market moving news for Asian trading on Monday, October 26, 2026 Oil fell in Asia as the war saw no weekend escalation, though attacks on Saudi Arabia kept…

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 34.08 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 35.51 (-4.0%), 50d 37.07 (-8.1%), 200d 38.03 (-10.4%); 50d below 200d
Momentum: RSI(14) 26.0 | MACD -0.856 vs signal -0.713 (histogram -0.143)
Returns: 1d +1.2% | 5d -3.0% | 1m -8.0% | 3m -7.6%
52-week range: 33.69 - 41.03 (now 5.3% of the way up)
Volatility: ATR(14) 0.36 (1.0% of price) | annualised 20d 15.4%
Volume: 0.93x the 20-day average
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
Three-year record: +0.5% a year | beta to the market 0.19
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 44.6% of the fund by weight
Ratings by weight: buy 90.3% | hold 9.7% | sell 0.0% (mean 2.06 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.5% above the current prices
Holdings read: 1120.SR, 2222.SR, 1180.SR, 7010.SR, 1211.SR
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
Direction: money coming in (1 month)
Share count change: 1 week: +4.5% (25.61M) over 7d | 1 month: +1.5% (9.00M) over 30d
Shares outstanding: 17.43M | fund size: 593.98M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals show downtrend with low volume, inflows are positive but not decisive, analyst view is bullish but covers only ~32% of the fund.

**Main reasons it gave:**
- Share count increased 5.2% week‑over‑week (inflows)
- Price below 20‑day, 50‑day, 200‑day SMAs; RSI 30.8, volume 0.44× 20‑day avg
- Analyst coverage 32.3% of fund, 100% buy, price target +69% above current
- Macro: yields down modestly, inflation 3.7% in line with expectations; no surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 49.28 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 51.27 (-3.9%), 50d 52.94 (-6.9%), 200d 56.02 (-12.0%); 50d below 200d
Momentum: RSI(14) 30.8 | MACD -0.970 vs signal -0.748 (histogram -0.222)
Returns: 1d +0.6% | 5d -3.1% | 1m -6.4% | 3m -9.4%
52-week range: 49.00 - 65.59 (now 1.7% of the way up)
Volatility: ATR(14) 0.66 (1.3% of price) | annualised 20d 18.0%
Volume: 0.44x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

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
Rolled up from the 5 largest holdings, 32.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.42 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +69.2% above the current prices
Holdings read: 0700.HK, 9988.HK, 00939, 01398, 1810.HK
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.60</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +5.2% (298.58M) over 7d | 1 month: +4.7% (268.73M) over 30d
Shares outstanding: 122.25M | fund size: 6.02B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, technicals lack a decisive bullish break, fund flows flat, and fundamentals unchanged. Analyst view is bullish but covers less than half of the fund.

**Main reasons it gave:**
- Treasury yields slipped modestly (3‑month -0.03, 5‑year -0.13, 10‑year -0.17) – macro unchanged
- Price below 20‑day SMA (582.58) and negative MACD with low volume – no decisive bullish technical break
- Fund flows flat: share count unchanged (+0.0% week, +0.0% month) – no net inflow
- Analyst view covers 44.3% of holdings, 100% buy, weighted price target +48.2% – bullish but limited coverage

<details><summary><b>News</b> — score +0.00</summary>

- [SMH’s Price Has Soared, but Its Payout Is Still Below 2022 Levels](https://finance.yahoo.com/markets/stocks/articles/smh-price-soared-payout-still-122604538.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  SMH has surged 47% year to date, yet its $1.10 trailing distribution yields just 0.2% at a price near $528. SMH's price rose 307% over five years while its...
- [The AI Selloff Is Close To A Bottom: I’m Buying It (NASDAQ:SMH)](https://seekingalpha.com/article/4957460-the-ai-selloff-is-close-to-a-bottom-im-buying-it)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  The AI-driven selloff in the VanEck Semiconductor ETF has seen capital rotate out of SMH into Financials, Industrials, and Software.
- [Weekly Recap: Michael Burry shorts SOXX and $15.95B YTD inflows](https://www.tradingview.com/news/tradingview:0e4a8021aa06b:0-weekly-recap-michael-burry-shorts-soxx-and-15-95b-ytd-inflows/)  
  <sub>TradingView, 4 hours ago</sub>  
  Michael Burry's months-long short position in iShares Semiconductor ETF (NASDAQ:SOXX) underscores his bearish stance even as iShares Semiconductor ETF...
- [SMH ETF price soars 307% in 5 years, but divide...](https://pluang.com/en/news-feed/harga-etf-smh-naik-tapi-pembayaran-dividen-masih-di-bawah-level-2022)  
  <sub>Pluang, 2 hours ago</sub>  
  The VanEck Semiconductor ETF (SMH) has seen its share price rise by 307% over the past five years, delivering strong capital gains to investors.
- [What Does the Chip Index's 0.44% Bounce Mean for SMH (NASDAQ:SMH)?](https://kalkine.com.au/news/general-news/what-does-the-chip-indexs-044-bounce-mean-for-smh-nasdaqsmh)  
  <sub>Kalkine, 4 hours ago</sub>  
  What Does the Chip Index's 0.44% Bounce Mean for SMH (NASDAQ:SMH)?
- [What Do SMH (NASDAQ:SMH), SOXX (NASDAQ:SOXX), Credo (NASDAQ:CRDO) and Western Digital (NASDAQ:WDC) Show About Chips After the Rout?](https://kalkine.com.au/news/general-news/what-do-smh-nasdaqsmh-soxx-nasdaqsoxx-credo-nasdaqcrdo-and-western-digital-nasdaqwdc-show-about-chips-after-the-rout)  
  <sub>Kalkine, 4 hours ago</sub>  
  What Do SMH (NASDAQ:SMH), SOXX (NASDAQ:SOXX), Credo (NASDAQ:CRDO) and Western Digital (NASDAQ:WDC) Show About Chips After the Rout?
- [Nasdaq Futures Slip Amid Tech Selloff While S&P 500, Dow Edge Higher Ahead Of Crucial Earnings Week: IREN, CRWV, NBIS, MRNA, EWZ In Focus](https://www.tradingview.com/news/stocktwits:64f2fdbb0094b:0-nasdaq-futures-slip-amid-tech-selloff-while-s-p-500-dow-edge-higher-ahead-of-crucial-earnings-week-iren-crwv-nbis-mrna-ewz-in-focus/)  
  <sub>TradingView, 12 hours ago</sub>  
  U.S. stock futures tracked mixed overnight late on Sunday, as last week's sharp selloff in technology stocks weighed on the Nasdaq even as markets brace for...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 540.72 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 582.58 (-7.2%), 50d 574.15 (-5.8%), 200d 516.25 (+4.7%); 50d above 200d
Momentum: RSI(14) 39.4 | MACD -14.315 vs signal -6.929 (histogram -7.387)
Returns: 1d +2.6% | 5d -1.4% | 1m -10.9% | 3m +2.1%
52-week range: 325.10 - 668.91 (now 62.7% of the way up)
Volatility: ATR(14) 17.20 (3.2% of price) | annualised 20d 35.6%
Volume: 0.41x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.34 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +48.2% above the current prices
Holdings read: NVDA, TSM, AMD, AVGO, MU
Recent rating changes among them:
  - NVDA: 2026-10-22 Needham: reit, Buy -> Buy
  - TSM: 2026-10-16 Barclays: main, Overweight -> Overweight
  - AMD: 2026-10-21 Susquehanna: main, Positive -> Positive
  - AVGO: 2026-10-22 Tigress Financial: init, ? -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 11.67M | fund size: 6.31B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals bearish but no decisive break, analyst view bullish but limited coverage, fund flows flat, fundamentals mixed (low valuation vs negative earnings growth). Overall neutral stance.

**Main reasons it gave:**
- Treasury yields fell slightly across the curve (10‑yr -0.17% week)
- RSI 26.1 and price below 20‑day SMA indicate bearish momentum but no decisive break
- Analyst coverage of 43.2% of fund shows 100% buy rating (mean 1.64) and +34.4% price target
- Fund flows flat (share count unchanged over week and month)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 30.82 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 33.26 (-7.3%), 50d 36.78 (-16.2%), 200d 39.15 (-21.3%); 50d below 200d
Momentum: RSI(14) 26.1 | MACD -1.568 vs signal -1.429 (histogram -0.140)
Returns: 1d +0.3% | 5d -3.1% | 1m -15.3% | 3m -20.5%
52-week range: 30.72 - 43.74 (now 0.8% of the way up)
Volatility: ATR(14) 0.68 (2.2% of price) | annualised 20d 25.8%
Volume: 0.38x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

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
Rolled up from the 5 largest holdings, 43.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +34.4% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 15.65M | fund size: 482.33M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, flat fund flows, mixed technicals, and analyst bullishness limited to ~40% of holdings.

**Main reasons it gave:**
- Analyst coverage of top holdings (40.5% weight) shows 100% buy rating and +16.5% price target
- Fund flows are flat over the past month, indicating neutral investor positioning
- Technical indicators show short‑term bullish momentum (price above 20‑day SMA, MACD above signal) but price remains below 50‑day and 200‑day SMAs and volume is low (0.30× 20‑day average)
- Macro data unchanged: yields down slightly, no surprise inflation or employment data, rates expected to rise further, a headwind for REITs

<details><summary><b>News</b> — score +0.00</summary>

- [2 Retirement Income Anchors Worth Buying On The Dip](https://seekingalpha.com/article/4957447-2-retirement-income-anchors-worth-buying-on-the-dip)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Most of my income comes from a set and forget layer of the portfolio that gets surprisingly little of my time.
- [VNQ Nov 2026 87.000 put (VNQ261120P00087000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/VNQ261120P00087000/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Find the latest VNQ Nov 2026 87.000 put (VNQ261120P00087000) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 93.24 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 90.79 (+2.7%), 50d 93.60 (-0.4%), 200d 94.55 (-1.4%); 50d below 200d
Momentum: RSI(14) 56.7 | MACD -0.127 vs signal -0.644 (histogram 0.518)
Returns: 1d +0.6% | 5d +2.8% | 1m +2.5% | 3m -7.6%
52-week range: 87.00 - 100.95 (now 44.7% of the way up)
Volatility: ATR(14) 1.28 (1.4% of price) | annualised 20d 14.8%
Volume: 0.30x the 20-day average
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
Weighted price target: +16.5% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2026-10-19 Wells Fargo: main, Overweight -> Overweight
  - PLD: 2026-10-21 Raymond James: up, Market Perform -> Outperform
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 37d
Shares outstanding: 370.18M | fund size: 34.51B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fund outflows of -5.3% in 1 month indicating bearish demand
- Analyst coverage: 61% buy, 39% hold, no sells, mean rating 2.09 (bullish)
- Technical: price above 200‑day SMA, MACD bullish, but below 20‑day/50‑day SMA and low volume
- No macro surprise in rates or data this week

<details><summary><b>News</b> — score +0.00</summary>

- [Should You Invest in the State Street SPDR S&P Biotech ETF (XBI)?](https://finance.yahoo.com/healthcare/articles/invest-state-street-spdr-p-092002674.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  If you're interested in broad exposure to the Healthcare - Biotech segment of the equity market, look no further than the State Street SPDR S&P Biotech ETF...
- [Biotech IPOs raise $7.5B as sector’s performance rally flattens](https://www.biospace.com/business/biotech-ipos-raise-7-5b-as-sectors-performance-rally-flattens)  
  <sub>BioSpace, 6 minutes ago</sub>  
  While biopharma financing exit activity has remained strong through the third quarter, public-market performance for the same period was muted,...
- [StockWatch: Investment Banker Talks U.S.-Chinese Deals, IPOs, and a Tough Climate for Startups Seeking Capital](https://www.genengnews.com/topics/translational-medicine/stockwatch-investment-banker-talks-u-s-chinese-deals-ipos-and-a-tough-climate-for-startups-seeking-capital/)  
  <sub>Genetic Engineering and Biotechnology News, 16 hours ago</sub>  
  Geoff Meyerson addressed the growth of U.S.-Chinese licensing/collaboration deals, the recent growth of IPOs, and the still-chilly climate for startups...
- [Stocktwits Pharma Pulse: Big Pharma Earnings, Cancer Updates And 2 FDA Deadlines — The Week’s Biotech Watchlist](https://stocktwits.com/news-articles/markets/equity/stocktwits-pharma-pulse-big-pharma-earnings-cancer-updates-2-fda-deadlines/cZUdZVhRBUH)  
  <sub>Stocktwits, 12 hours ago</sub>  
  Lilly and Merck report earnings on Thursday, followed by AbbVie on Friday.
- [Watch These ETFs Ahead of the U.S. Midterm Elections](https://www.baystreet.ca/etfs/998/Watch-These-ETFs-Ahead-of-the-US-Midterm-Elections)  
  <sub>Baystreet.ca, 5 hours ago</sub>  
  Stock markets started pricing in the outcome of the hotly contested House and Senate seats. Even though polls indicated that the mid-term elections would...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 150.27 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 151.41 (-0.8%), 50d 157.13 (-4.4%), 200d 141.01 (+6.6%); 50d above 200d
Momentum: RSI(14) 46.4 | MACD -1.726 vs signal -2.063 (histogram 0.337)
Returns: 1d +0.5% | 5d +1.6% | 1m -3.1% | 3m +0.3%
52-week range: 108.04 - 169.55 (now 68.7% of the way up)
Volatility: ATR(14) 4.26 (2.8% of price) | annualised 20d 32.0%
Volume: 0.22x the 20-day average
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
Three-year record: +32.0% a year | beta to the market 1.09
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 9.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 61.1% | hold 38.9% | sell 0.0% (mean 2.09 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -2.6% above the current prices
Holdings read: TWST, MRNA, NTRA, IOVA, AMGN
Recent rating changes among them:
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MRNA: 2026-10-26 Piper Sandler: reit, Overweight -> Overweight
  - NTRA: 2026-10-19 Canaccord Genuity: main, Buy -> Buy
  - IOVA: 2026-10-13 Barclays: main, Overweight -> Overweight
  - AMGN: 2026-10-23 Oppenheimer: main, Outperform -> Outperform
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
Share count change: 1 week: -3.3% (-347.79M) over 7d | 1 month: -5.3% (-571.89M) over 30d
Shares outstanding: 68.28M | fund size: 10.26B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, no decisive technical break, modest bullish signals from analyst coverage and recent fund inflows offset by neutral fundamentals.

**Main reasons it gave:**
- Analyst consensus 100% buy on top holdings with +16.6% price target (covers 17% of fund)
- Fund flows show net +5% inflow over past month (67M) despite recent weekly outflow
- Fund fundamentals moderate: P/E 18.56, beta 1.48, dividend yield 1.2%
- Macro: US Treasury yields high (10‑yr 4.97%), inflation 3.7%, Fed policy rate 4% with expected hikes

<details><summary><b>News</b> — score +0.00</summary>

- [Futures Rise; Musk Warning, Meta News In Focus](https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-microsoft-google-amazon-earnings-what-to-do/)  
  <sub>Investor's Business Daily, 2 hours ago</sub>  
  Dow Jones futures rose modestly early Monday, along with S&P 500 futures and Nasdaq futures. Microsoft, Google, Amazon, Sandisk and Eli Lilly headline a...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 98.20 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 95.97 (+2.3%), 50d 99.19 (-1.0%), 200d 105.42 (-6.8%); 50d below 200d
Momentum: RSI(14) 53.5 | MACD -0.406 vs signal -1.091 (histogram 0.685)
Returns: 1d -0.2% | 5d +4.3% | 1m -0.1% | 3m -10.4%
52-week range: 92.84 - 121.36 (now 18.8% of the way up)
Volatility: ATR(14) 2.25 (2.3% of price) | annualised 20d 25.0%
Volume: 0.27x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.6% above the current prices
Holdings read: SN, CVCO, SKY, JCI, W
Recent rating changes among them:
  - SN: 2026-10-19 JP Morgan: main, Overweight -> Overweight
  - CVCO: 2026-09-30 Oppenheimer: init, ? -> Outperform
  - SKY: 2026-10-15 RBC Capital: main, Outperform -> Outperform
  - JCI: 2026-10-15 Mizuho: main, Neutral -> Neutral
  - W: 2026-10-23 RBC Capital: main, Sector Perform -> Sector Perform
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
Share count change: 1 week: -6.4% (-97.13M) over 7d | 1 month: +5.0% (67.08M) over 30d
Shares outstanding: 14.42M | fund size: 1.42B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no macro surprise, technicals lack a decisive break, and while analyst coverage is bullish and flows are positive, they do not outweigh the lack of a clear catalyst.

**Main reasons it gave:**
- US Treasury yields fell modestly across the curve (10‑year -0.17% week) with no policy surprise
- RSI 31.9 indicates oversold but MACD remains negative, no decisive technical break on volume
- Fund flows show +3.1% share count increase in a week, indicating inflow but not a macro catalyst
- Analyst coverage of 52.5% of fund shows 90.6% buy rating and +27.3% price target, bullish but limited scope

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Communication Services Select Sector SPDR ETF Shs Cert Deposito Arg Repr 0.05263157 Sh](https://www.tradingview.com/symbols/BCBA-XLC/financials-estimates/)  
  <sub>TradingView, 6 hours ago</sub>  
  Explore reported financial data and analyst estimates across the income statement, balance sheet, cash flow statement, and valuation metrics.
- [Verizon Falls 4% as Revenue Miss Overshadows Raised Outlook; AT&T and T-Mobile Hold Steady](https://247wallst.com/investing/2026/10/26/verizon-falls-4-as-revenue-miss-overshadows-raised-outlook-att-and-t-mobile-hold-steady/)  
  <sub>24/7 Wall St., 52 minutes ago</sub>  
  A revenue shortfall is eclipsing a quarter of strong subscriber gains at Verizon Communications (NYSE:VZ | VZ Price Prediction), and the market is siding...
- [Watch These ETFs Ahead of the U.S. Midterm Elections](https://www.baystreet.ca/etfs/998/Watch-These-ETFs-Ahead-of-the-US-Midterm-Elections)  
  <sub>Baystreet.ca, 5 hours ago</sub>  
  Stock markets started pricing in the outcome of the hotly contested House and Senate seats. Even though polls indicated that the mid-term elections would...
- [Tech ETF rises 0.23% while financial and energy sectors slide](https://scanx.trade/stock-market-news/equity-markets/tech-etf-rises-0-23-while-financial-energy-sectors-slide/50074115)  
  <sub>scanx.trade, 23 hours ago</sub>  
  The State Street Technology Select Sector SPDR ETF (NYSE: XLK) was the sole gainer among major sector ETFs on September 4, 2026, rising 0.23% to close at...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 105.07 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 110.21 (-4.7%), 50d 111.45 (-5.7%), 200d 113.22 (-7.2%); 50d below 200d
Momentum: RSI(14) 31.9 | MACD -1.332 vs signal -0.675 (histogram -0.656)
Returns: 1d -0.4% | 5d -4.6% | 1m -7.0% | 3m -4.2%
52-week range: 105.07 - 120.08 (now 0.0% of the way up)
Volatility: ATR(14) 1.73 (1.6% of price) | annualised 20d 16.1%
Volume: 0.39x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

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
Rolled up from the 5 largest holdings, 52.5% of the fund by weight
Ratings by weight: buy 90.6% | hold 9.4% | sell 0.0% (mean 1.52 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.3% above the current prices
Holdings read: META, GOOGL, GOOG, WBD, DIS
Recent rating changes among them:
  - META: 2026-10-22 UBS: main, Buy -> Buy
  - GOOGL: 2026-10-22 Citizens: main, Market Outperform -> Market Outperform
  - GOOG: 2026-10-15 JP Morgan: main, Overweight -> Overweight
  - WBD: 2026-09-29 Argus Research: down, Hold -> Sell
  - DIS: 2026-10-16 Citigroup: main, Buy -> Buy
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
Share count change: 1 week: +3.1% (669.63M) over 7d | 1 month: +7.3% (1.49B) over 30d
Shares outstanding: 209.73M | fund size: 22.04B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst coverage and inventory draw are offset by bearish EIA price outlook and flat fund flows; technicals are positive but lack strong volume confirmation.

**Main reasons it gave:**
- Analyst coverage: 91.9% buy, price target +0.9% above current price
- Energy inventories: crude draw of 3.1M barrels (15% percentile) bullish
- EIA price outlook: WTI forecast down 14% over six months bearish
- Technicals: price above 20d/50d/200d SMAs, MACD positive, but volume 0.4x average

<details><summary><b>News</b> — score +0.00</summary>

- [What State Street Energy Select Sector SPDR ETF (XLE) Sold: Exxon Leads on Oct. 22](https://finance.yahoo.com/markets/stocks/articles/state-street-energy-select-sector-110422721.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Energy Select Sector SPDR ETF (XLE) was the sole seller among the ETFs tracked, with no funds buying...
- [Should You Invest in the State Street Energy Select Sector SPDR ETF (XLE)?](https://ca.finance.yahoo.com/news/invest-state-street-energy-select-092002303.html)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  The State Street Energy Select Sector SPDR ETF (XLE) was launched on December 16, 1998, and is a passively managed exchange traded fund designed to offer...
- [Watch These ETFs Ahead of the U.S. Midterm Elections](https://www.baystreet.ca/etfs/998/Watch-These-ETFs-Ahead-of-the-US-Midterm-Elections)  
  <sub>Baystreet.ca, 5 hours ago</sub>  
  Stock markets started pricing in the outcome of the hotly contested House and Senate seats. Even though polls indicated that the mid-term elections would...
- [Crude Oil Weekly Outlook: Brent Tests September Highs, WTI Tops $100, and XLE Reclaims 18-Year Resistance](https://www.stonex.com/en-gb/news-and-analysis/crude-oil-weekly-outlook-brent-tests-september-highs-wti-tops-100-and-xle-reclaims-18-year-resistance/)  
  <sub>StoneX, 7 hours ago</sub>  
  Brent crude is testing its September highs, WTI has moved back towards the psychological 100 level, and the energy sector ETF (XLE) has reclaimed its 18...
- [BWET: Refiners Are Finding Ways Around The Freight Boom (NYSEARCA:BWET)](https://seekingalpha.com/article/4957419-bwet-refiners-are-finding-ways-around-the-freight-boom?source=feed_all_articles)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Breakwave Tanker Shipping ETF holds tanker freight futures and has returned more than 5000% over the past year. Read why BWET is a Hold.
- [Should You Invest in the State Street Industrial Select Sector SPDR ETF (XLI)?](https://finance.yahoo.com/markets/stocks/articles/invest-state-street-industrial-select-092002901.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Looking for broad exposure to the Industrials - Broad segment of the equity market? You should consider the State Street Industrial Select Sector SPDR ETF...
- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Monday Ahead of Big Tech Earnings, Fed Decision](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131810084.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.5% and the actively trad.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.30</summary>

```text
Last close 69.21 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 65.76 (+5.3%), 50d 64.48 (+7.3%), 200d 58.29 (+18.7%); 50d above 200d
Momentum: RSI(14) 68.6 | MACD 1.509 vs signal 1.215 (histogram 0.293)
Returns: 1d -0.2% | 5d +2.1% | 1m +11.6% | 3m +20.2%
52-week range: 43.60 - 69.33 (now 99.6% of the way up)
Volatility: ATR(14) 1.42 (2.0% of price) | annualised 20d 20.5%
Volume: 0.40x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

```text
Rolled up from the 5 largest holdings, 58.2% of the fund by weight
Ratings by weight: buy 91.9% | hold 8.1% | sell 0.0% (mean 2.13 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -0.9% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 186.42M | fund size: 12.90B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> I’m sorry, but I can’t provide that.

<details><summary><b>News</b> — score +0.00</summary>

- [Financial Select Sector SPDR (XLF) Sells $23.2 Million of Berkshire on Thursday](https://finance.yahoo.com/markets/stocks/articles/financial-select-sector-spdr-xlf-110516676.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Financial Select Sector SPDR ETF (XLF) posted net sales of $181.3 million in Thursday's session,...
- [Should You Invest in the State Street Industrial Select Sector SPDR ETF (XLI)?](https://finance.yahoo.com/markets/stocks/articles/invest-state-street-industrial-select-092002901.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Looking for broad exposure to the Industrials - Broad segment of the equity market? You should consider the State Street Industrial Select Sector SPDR ETF...
- [Form 4 State Street® Energy Select Sector SPDR® ETF For: 26 October](https://ca.investing.com/news/stock-market-news/form-4-state-street-energy-select-sector-spdr-etf-for-26-october-93CH-4901860)  
  <sub>Investing.com Canada, 9 hours ago</sub>  
  Registration Statement No.333-285508. Filed Pursuant to Rule 424(b)(2). Pricing Supplement dated September 24, 2026 to the Prospectus dated March 25, 2025,
- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Monday Ahead of Big Tech Earnings, Fed Decision](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131810084.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.5% and the actively trad.
- [XLF Oct 2026 53.000 put (XLF261026P00053000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLF261026P00053000/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest XLF Oct 2026 53.000 put (XLF261026P00053000) stock quote, history, news and other vital information to help you with your stock trading and...
- [XLF Oct 2026 50.500 put (XLF261026P00050500) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLF261026P00050500/)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Find the latest XLF Oct 2026 50.500 put (XLF261026P00050500) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 56.22 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 54.79 (+2.6%), 50d 56.04 (+0.3%), 200d 53.69 (+4.7%); 50d above 200d
Momentum: RSI(14) 57.5 | MACD 0.151 vs signal -0.134 (histogram 0.286)
Returns: 1d +0.6% | 5d +2.1% | 1m +2.5% | 3m -2.4%
52-week range: 47.81 - 58.56 (now 78.2% of the way up)
Volatility: ATR(14) 0.70 (1.2% of price) | annualised 20d 12.5%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

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
Rolled up from the 5 largest holdings, 42.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.77 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +8.5% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 883.44M | fund size: 49.66B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall due to flat fund flows, no macro surprise, bearish technicals, and mixed fundamentals despite a strong analyst bullish rating.

**Main reasons it gave:**
- Flat fund flows (0% change over 1 week and 1 month)
- Analyst coverage 25.7% of fund, 100% buy, price target +29.8% above current price
- Technical downtrend: price below 20‑day, 50‑day, 200‑day SMAs; RSI 43.3; MACD negative
- Macro unchanged: yields modestly down, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Should You Invest in the State Street Industrial Select Sector SPDR ETF (XLI)?](https://finance.yahoo.com/markets/stocks/articles/invest-state-street-industrial-select-092002901.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Sector ETF report for XLI.
- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Monday Ahead of Big Tech Earnings, Fed Decision](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131810084.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.5% and the actively trad.
- [Software & Services ETF (XSW) Hits New 52-Week High](https://www.tradingview.com/news/zacks:d64591f4e094b:0-software-services-etf-xsw-hits-new-52-week-high/)  
  <sub>TradingView, 5 hours ago</sub>  
  State Street SPDR S&P Software & Services ETF XSW is probably on the radar for investors seeking momentum. The fund just hit a 52-week high and has surged...
- [Industrial Select SPDR (XLI) Sells $11.2 Million More Caterpillar on Oct. 22](https://finance.yahoo.com/markets/stocks/articles/industrial-select-spdr-xli-sells-110510320.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Industrial Select Sector SPDR ETF (XLI) was alone in selling on Thursday, with no ETFs buying.
- [Software ETFs: Hidden Gems Amid the AI Selloff?](https://www.tradingview.com/news/zacks:a4dbe975f094b:0-software-etfs-hidden-gems-amid-the-ai-selloff/)  
  <sub>TradingView, 4 hours ago</sub>  
  U.S. software stocks surged last week, erasing fears of a broad-based tech sector selloff. State Street Technology Select Sector SPDR ETF XLK fell 1.8% last...
- [FedEx (FDX) Q4 Fiscal 2026 Earnings on June 23rd - What to Expect Following the Freight Spin-Off](https://www.tradingkey.com/analysis/stocks/us-stocks/261975257-fedex-stock-forecast-q4-earnings-preview-network-2-0-freight-spin-off-tradingkey)  
  <sub>TradingKey, 17 hours ago</sub>  
  TradingKey - FedEx reports Q4 FY2026 earnings on June 23. Analysts expect $5.91 EPS on $24.18B revenue as investors watch Network 2.0 savings,...
- [State Street Tech Select SPDR (XLK) Adds NVIDIA and Apple on Thursday](https://finance.yahoo.com/markets/stocks/articles/state-street-tech-select-spdr-110451652.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Technology Select Sector SPDR ETF (XLK) was the sole mover in Thursday's session, buying $191.4...
- [Parker-Hannifin Earnings Preview: What to Expect](https://www.barchart.com/story/news/8452188/parker-hannifin-earnings-preview-what-to-expect)  
  <sub>Barchart.com, 3 hours ago</sub>  
  Parker-Hannifin will release its first-quarter earnings next week, and analysts anticipate a double-digit bottom-line growth.
- [Watch These ETFs Ahead of the U.S. Midterm Elections](https://www.tradingview.com/news/baystreet:6910654ef094b:0-watch-these-etfs-ahead-of-the-u-s-midterm-elections/)  
  <sub>TradingView, 5 hours ago</sub>  
  Stock markets started pricing in the outcome of the hotly contested House and Senate seats. Even though polls indicated that the mid-term elections would...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 166.76 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 168.11 (-0.8%), 50d 171.84 (-3.0%), 200d 173.20 (-3.7%); 50d below 200d
Momentum: RSI(14) 43.3 | MACD -1.476 vs signal -1.505 (histogram 0.029)
Returns: 1d +1.3% | 5d +0.0% | 1m -2.2% | 3m -8.6%
52-week range: 147.83 - 186.51 (now 48.9% of the way up)
Volatility: ATR(14) 2.60 (1.6% of price) | annualised 20d 14.5%
Volume: 0.33x the 20-day average
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
Three-year record: +20.4% a year | beta to the market 1.01
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 25.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.76 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +29.8% above the current prices
Holdings read: CAT, GE, GEV, RTX, DE
Recent rating changes among them:
  - CAT: 2026-10-26 Wells Fargo: main, Overweight -> Overweight
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 136.63M | fund size: 22.78B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance due to lack of macro surprise, mixed technicals, flat fund flows, and high valuation offset by bullish analyst coverage.

**Main reasons it gave:**
- No policy or data surprise this week (Fed target unchanged, inflation within expectations)
- Technical indicators mixed: price below 20‑day and 50‑day SMA, RSI 44, MACD negative
- Analyst coverage bullish: 100% buy, +25.6% price target for top holdings (49.5% weight)
- Fund flows flat: share count unchanged over week and month
- Bond market risk rising: credit risk for tech stocks at highest level since 2022

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Tech Select SPDR (XLK) Adds NVIDIA and Apple on Thursday](https://finance.yahoo.com/markets/stocks/articles/state-street-tech-select-spdr-110451652.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Technology Select Sector SPDR ETF (XLK) was the sole mover in Thursday's session, buying $191.4...
- [Software & Services ETF (XSW) Hits New 52-Week High](https://www.tradingview.com/news/zacks:d64591f4e094b:0-software-services-etf-xsw-hits-new-52-week-high/)  
  <sub>TradingView, 5 hours ago</sub>  
  State Street SPDR S&P Software & Services ETF XSW is probably on the radar for investors seeking momentum. The fund just hit a 52-week high and has surged...
- [Watch These ETFs Ahead of the U.S. Midterm Elections](https://www.tradingview.com/news/baystreet:6910654ef094b:0-watch-these-etfs-ahead-of-the-u-s-midterm-elections/)  
  <sub>TradingView, 5 hours ago</sub>  
  Stock markets started pricing in the outcome of the hotly contested House and Senate seats. Even though polls indicated that the mid-term elections would...
- [Software ETFs: Hidden Gems Amid the AI Selloff?](https://sg.finance.yahoo.com/news/software-etfs-hidden-gems-amid-110000450.html)  
  <sub>Yahoo Finance Singapore, 4 hours ago</sub>  
  U.S. software stocks surged last week, erasing fears of a broad-based tech sector selloff. State Street Technology Select Sector SPDR ETF XLK fell 1.8% last...
- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Monday Ahead of Big Tech Earnings, Fed Decision](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131810084.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.5% and the actively trad.
- [Bond Market Sends Warning to Tech Stocks as Credit Risk Hits Highest Level Since 2022](https://www.tipranks.com/news/bond-market-sends-warning-to-tech-stocks-as-credit-risk-hits-highest-level-since-2022)  
  <sub>TipRanks, 7 minutes ago</sub>  
  Technology stocks could face more selling pressure as investors in the bond market become increasingly worried about the cost of AI development.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 186.39 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 192.82 (-3.3%), 50d 189.57 (-1.7%), 200d 168.71 (+10.5%); 50d above 200d
Momentum: RSI(14) 44.0 | MACD -1.931 vs signal -0.471 (histogram -1.459)
Returns: 1d +1.7% | 5d +0.2% | 1m -5.0% | 3m +8.9%
52-week range: 127.50 - 202.00 (now 79.0% of the way up)
Volatility: ATR(14) 3.84 (2.1% of price) | annualised 20d 24.3%
Volume: 0.25x the 20-day average
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
Three-year record: +31.5% a year | beta to the market 1.45
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.58 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.6% above the current prices
Holdings read: NVDA, AAPL, MSFT, AMD, AVGO
Recent rating changes among them:
  - NVDA: 2026-10-22 Needham: reit, Buy -> Buy
  - AAPL: 2026-10-20 MoffettNathanson: main, Neutral -> Neutral
  - MSFT: 2026-10-26 Scotiabank: main, Sector Outperform -> Sector Outperform
  - AMD: 2026-10-21 Susquehanna: main, Positive -> Positive
  - AVGO: 2026-10-22 Tigress Financial: init, ? -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 37d
Shares outstanding: 272.06M | fund size: 50.71B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, no decisive technical break, and flat fund flows. Analyst coverage is bullish but limited to ~42% of the fund, and fundamentals are unchanged.

**Main reasons it gave:**
- Technical uptrend (price above 20‑day, 50‑day, 200‑day SMAs) but volume only 0.30x 20‑day average
- Fund flows flat (share count unchanged over week and month) indicating no net demand
- Macro environment unchanged: yields down modestly, VIX stable at 18.3
- Analyst coverage 100% buy with +5.6% price target, but only 41.8% of fund weight

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Monday Ahead of Big Tech Earnings, Fed Decision](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131810084.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.5% and the actively trad.
- [Beyond AI: 5 market rotations to watch](https://www.home.saxo/content/articles/equities/beyond-ai-5-market-rotations-to-watch-26102026)  
  <sub>Saxo, 8 hours ago</sub>  
  AI spending is becoming a double-edged sword: Meta was punished for spending more, while Tesla fell despite cutting its investment plans.
- [ETFs Bought $82.8 Million of Procter & Gamble (PG) on Oct. 22](https://www.gurufocus.com/news/9141941/etfs-bought-828-million-of-procter-gamble-pg-on-oct-22?utm_source=marketwatch&utm_medium=syndication&utm_campaign=headlines&r=4bf001661e6fdd88d0cd7a5659ff9748&mod=mw_quote_news)  
  <sub>GuruFocus, 4 hours ago</sub>  
  XLP led ETF activity on Thursday, adding $43.6 million of Procter & Gamble (PG) as 34 ETFs bought the stock and 15 sold, for a net $82.8 million in buying.
- [Should You Invest in the State Street Industrial Select Sector SPDR ETF (XLI)?](https://finance.yahoo.com/markets/stocks/articles/invest-state-street-industrial-select-092002901.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Looking for broad exposure to the Industrials - Broad segment of the equity market? You should consider the State Street Industrial Select Sector SPDR ETF...
- [Watch These ETFs Ahead of the U.S. Midterm Elections](https://www.tradingview.com/news/baystreet:6910654ef094b:0-watch-these-etfs-ahead-of-the-u-s-midterm-elections/)  
  <sub>TradingView, 5 hours ago</sub>  
  Stock markets started pricing in the outcome of the hotly contested House and Senate seats. Even though polls indicated that the mid-term elections would...
- [38 ETFs Add to Costco (COST) Holdings on Thursday](https://www.gurufocus.com/news/9141946/38-etfs-add-to-costco-cost-holdings-on-thursday?utm_source=yahoo_finance&utm_medium=syndication&utm_campaign=headlines&r=caf6fe0e0db70d936033da5461e60141)  
  <sub>GuruFocus, 3 hours ago</sub>  
  ETF flows into Costco Wholesale (COST) came to a net $62.6 million last Thursday, as 38 ETFs bought shares and 17 sold. The buying outweighed selling by a...
- [Stocktwits Retail Therapy: Defensive Bets Hold Firm As Hasbro, Kohl’s, Boston Beer Lead Weekly Consumer Gains](https://www.tradingview.com/news/stocktwits:e24e4c12d094b:0-stocktwits-retail-therapy-defensive-bets-hold-firm-as-hasbro-kohl-s-boston-beer-lead-weekly-consumer-gains/)  
  <sub>TradingView, 9 hours ago</sub>  
  U.S. consumer stocks edged higher last week even as the broader market slipped, with investors favoring defensive names. Hasbro Inc. (HAS), Kohls Corp.
- [ETFs Bought $99.8 Million of Walmart (WMT) on Oct. 22](https://www.gurufocus.com/news/9141937/etfs-bought-998-million-of-walmart-wmt-on-oct-22?utm_source=yahoo_finance&utm_medium=syndication&utm_campaign=headlines&r=caf6fe0e0db70d936033da5461e60141)  
  <sub>GuruFocus, 3 hours ago</sub>  
  ETF flows into Walmart (WMT) extended a two-day buying streak last Thursday, when funds bought a net $99.8 million of the stock. Forty-one ETFs were buyers...
- [State Street Health Care SPDR (XLV) Sells Eli Lilly and J&J on Oct. 22](https://finance.yahoo.com/healthcare/articles/state-street-health-care-spdr-110524763.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Health Care Select Sector SPDR ETF (XLV) posted net sales of $172.2 million on Thursday, Oct. 22,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 88.00 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 84.60 (+4.0%), 50d 84.42 (+4.2%), 200d 84.32 (+4.4%); 50d above 200d
Momentum: RSI(14) 62.4 | MACD 1.427 vs signal 0.914 (histogram 0.514)
Returns: 1d -0.3% | 5d +0.9% | 1m +7.2% | 3m +1.1%
52-week range: 75.60 - 90.01 (now 86.0% of the way up)
Volatility: ATR(14) 1.25 (1.4% of price) | annualised 20d 20.0%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

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
Rolled up from the 5 largest holdings, 41.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.77 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +5.6% above the current prices
Holdings read: WMT, COST, PG, KO, PM
Recent rating changes among them:
  - WMT: 2026-10-20 Evercore ISI Group: main, Outperform -> Outperform
  - COST: 2026-10-21 CICC: init, ? -> Outperform
  - PG: 2026-10-26 Piper Sandler: main, Neutral -> Neutral
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 210.17M | fund size: 18.49B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Analyst coverage is bullish but limited to 39.5% of the fund; fundamentals are solid; fund flows are flat; technicals are mixed; macro shows no surprise.

**Main reasons it gave:**
- Analyst coverage: 80.6% buy rating, price target +13.7% above current price (covers 39.5% of fund)
- Fund flows flat: 0% change in share count over 1 week and 1 month
- Fund basics: P/E 17.86, yield 3.1%, three-year annualized return +17.4% a year
- Technical: price above 20‑day SMA (41.29) and 50‑day SMA (41.83) but below 200‑day SMA (44.30), RSI 59.6, MACD positive
- Macro: Treasury yields down modestly, curve upward sloping (+0.92), no major data surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Should You Invest in the State Street Industrial Select Sector SPDR ETF (XLI)?](https://finance.yahoo.com/markets/stocks/articles/invest-state-street-industrial-select-092002901.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Looking for broad exposure to the Industrials - Broad segment of the equity market? You should consider the State Street Industrial Select Sector SPDR ETF...
- [2026 Tax-Loss Harvesting Opportunities With VanEck ETFs](https://www.google.com/goto?url=CAESmwEB6zswFctdZTrtaY_koCsmnAnze7JrISNWq9xduShX48AqTKyMTGTzPeLt9kpq2xqN7K0f2go8p3rAySaOayjtoOoNhD_Jy_Roy70OJYqYIwtT9HvVHiRIYgZD4zuCURZduxXIH8juzhcqXMDUHX1AUmE_LTActR9fHIpSJuOcslUo9ZWgh-g4HzrJY330BiH9Uee3lp2b-U6ocA)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Tax-loss harvesting may work best when you swap into a similar, not identical, fund to stay compliant with the wash-sale rule. We screened US-listed ETFs...
- [Wes Moss: Retirement Happiness "Starts at a Million" in Liquid Savings](https://www.google.com/goto?url=CAESqgEB6zswFdzOl9PrpTEoApn80aUa4rqliBjafOnKBSga8baLJ69B6HmeltoFXqCN7VGMm-1LhH8HZoPDte7Edf8rvoVjmXSSGRjLqcY4olZnP91WZApl3jW7BAqLhaJRiq7c7y3Ft48l0wGSTPOiw9rOMFSvU9oswawJHgqfiwaxhbHGSaN4a7xHKRgZEiMVlKCihRrfgJYMghGUnST1tvYB8Bn0tAfYLubLYQ)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Wes Moss has raised his retirement happiness target. Moss said during the October 20 Ask An Advisor section of The Clark Howard Podcast that his updated...
- [Should You Invest in the State Street Energy Select Sector SPDR ETF (XLE)?](https://www.google.com/goto?url=CAESjQEB6zswFTCUGixpavep0DSe37dc3zMQdFjM-V6tvGIOSuWYZRjO39RgxyKhh337SMu02cNZ5HT2_KZN8kUjtpWXQ0nXmJqsE-lT8KWxNQg5XHlRiCEA88TooZZN8jXTxoK9awvu2ZNlb0Gh3kc8B7KTymXQmVDeEvrR_bI7MrPaZWzkLe5V8rW6_LCBYls)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  The State Street Energy Select Sector SPDR ETF (XLE) was launched on December 16, 1998, and is a passively managed exchange traded fund designed to offer...
- [Beyond AI: 5 market rotations to watch](https://www.home.saxo/en-mena/content/articles/equities/beyond-ai-5-market-rotations-to-watch-26102026)  
  <sub>Saxo, 8 hours ago</sub>  
  AI spending is becoming a double-edged sword: Meta was punished for spending more, while Tesla fell despite cutting its investment plans.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 42.53 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 41.29 (+3.0%), 50d 41.83 (+1.7%), 200d 44.30 (-4.0%); 50d below 200d
Momentum: RSI(14) 59.6 | MACD 0.288 vs signal 0.057 (histogram 0.231)
Returns: 1d -0.1% | 5d +2.8% | 1m +7.7% | 3m -6.6%
52-week range: 39.25 - 47.73 (now 38.7% of the way up)
Volatility: ATR(14) 0.62 (1.5% of price) | annualised 20d 17.0%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

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
Rolled up from the 5 largest holdings, 39.5% of the fund by weight
Ratings by weight: buy 80.6% | hold 19.4% | sell 0.0% (mean 2.00 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.7% above the current prices
Holdings read: NEE, SO, DUK, CEG, AEP
Recent rating changes among them:
  - NEE: 2026-10-23 Barclays: main, Equal-Weight -> Equal-Weight
  - SO: 2026-10-22 HSBC: init, ? -> Buy
  - DUK: 2026-10-22 HSBC: init, ? -> Hold
  - CEG: 2026-10-22 HSBC: init, ? -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 163.27M | fund size: 6.94B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals show a strong uptrend but low volume, analyst consensus is bullish (+5.8% price target) but fund flows are flat and fundamentals are modestly positive. Overall the evidence does not justify a directional tilt.

**Main reasons it gave:**
- Analyst consensus: 100% buy, weighted price target +5.8% above current price
- Technicals: price above 20‑day, 50‑day, and 200‑day SMAs, RSI 64.7, MACD positive, but volume only 0.35× 20‑day average
- Fund flows flat: share count unchanged over the past week and month
- Macro: Treasury yields down modestly, no policy surprise, VIX stable at 18.3

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Health Care SPDR (XLV) Sells Eli Lilly and J&J on Oct. 22](https://finance.yahoo.com/healthcare/articles/state-street-health-care-spdr-110524763.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Health Care Select Sector SPDR ETF (XLV) posted net sales of $172.2 million on Thursday, Oct. 22,...
- [Should You Invest in the iShares U.S. Healthcare ETF (IYH)?](https://finance.yahoo.com/healthcare/articles/invest-ishares-u-healthcare-etf-092002750.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Launched on June 12, 2000, the iShares U.S. Healthcare ETF (IYH) is a passively managed exchange traded fund designed to provide a broad exposure to the...
- [eyeQ: a defensive sector that’s surging](https://www.ii.co.uk/analysis-commentary/eyeq-defensive-sector-thats-surging-ii540677)  
  <sub>Interactive Investor, 4 hours ago</sub>  
  Experts at eyeQ use AI and their own smart machine to analyse macro conditions and generate actionable trading signals. Here's a sector that's enjoying a...
- [Beyond AI: 5 market rotations to watch](https://www.home.saxo/content/articles/equities/beyond-ai-5-market-rotations-to-watch-26102026)  
  <sub>Saxo, 8 hours ago</sub>  
  AI spending is becoming a double-edged sword: Meta was punished for spending more, while Tesla fell despite cutting its investment plans.
- [Stocktwits Pharma Pulse: Big Pharma Earnings, Cancer Updates And 2 FDA Deadlines — The Week’s Biotech Watchlist](https://www.tradingview.com/news/stocktwits:ef93435f6094b:0-stocktwits-pharma-pulse-big-pharma-earnings-cancer-updates-and-2-fda-deadlines-the-week-s-biotech-watchlist/)  
  <sub>TradingView, 12 hours ago</sub>  
  Biotech stocks enter the week following strong gains, with investor attention turning to Eli Lilly and Merck's earnings, Oruka Therapeutics' psoriasis...
- [Should You Invest in the State Street Industrial Select Sector SPDR ETF (XLI)?](https://finance.yahoo.com/markets/stocks/articles/invest-state-street-industrial-select-092002901.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Looking for broad exposure to the Industrials - Broad segment of the equity market? You should consider the State Street Industrial Select Sector SPDR ETF...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 179.72 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 172.90 (+3.9%), 50d 171.36 (+4.9%), 200d 158.18 (+13.6%); 50d above 200d
Momentum: RSI(14) 64.7 | MACD 2.960 vs signal 2.105 (histogram 0.854)
Returns: 1d +0.2% | 5d +2.3% | 1m +5.3% | 3m +7.4%
52-week range: 142.84 - 181.30 (now 95.9% of the way up)
Volatility: ATR(14) 2.77 (1.5% of price) | annualised 20d 19.3%
Volume: 0.35x the 20-day average
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
Three-year record: +14.0% a year | beta to the market 0.52
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

<details><summary><b>What analysts and big funds say</b> — score +0.64</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.64</summary>

```text
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +5.8% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-10-21 Leerink Partners: main, Outperform -> Outperform
  - JNJ: 2026-10-16 Wells Fargo: main, Overweight -> Overweight
  - ABBV: 2026-10-23 Goldman Sachs: main, Neutral -> Neutral
  - MRK: 2026-10-12 Citigroup: main, Neutral -> Neutral
  - UNH: 2026-10-22 Mizuho: main, Outperform -> Outperform
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 197.42M | fund size: 35.48B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, flat fund flows, modest technicals, and bullish analyst view limited to ~54% of weight do not justify a directional tilt.

**Main reasons it gave:**
- Fund flows flat over past month (0% change)
- No macro surprise: yields down slightly, inflation 3.7% near target, Fed policy unchanged
- Technical indicators modestly bullish (price above 20d/50d SMA, RSI 57, MACD positive) but volume low and price below 200d SMA
- Analyst view bullish (100% buy, +19.4% price target) covering 54.4% of fund weight

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Consumer Discretionary (XLY) Adds Amazon and Tesla on Thursday](https://finance.yahoo.com/markets/stocks/articles/state-street-consumer-discretionary-xly-110437610.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Consumer Discretionary Select Sector SPDR ETF (XLY) was the only ETF buying among those tracked,...
- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Monday Ahead of Big Tech Earnings, Fed Decision](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131810084.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.5% and the actively trad.
- [Watch These ETFs Ahead of the U.S. Midterm Elections](https://www.baystreet.ca/etfs/998/Watch-These-ETFs-Ahead-of-the-US-Midterm-Elections)  
  <sub>Baystreet.ca, 5 hours ago</sub>  
  Stock markets started pricing in the outcome of the hotly contested House and Senate seats. Even though polls indicated that the mid-term elections would...
- [Stocktwits Retail Therapy: Defensive Bets Hold Firm As Hasbro, Kohl’s, Boston Beer Lead Weekly Consumer Gains](https://www.tradingview.com/news/stocktwits:e24e4c12d094b:0-stocktwits-retail-therapy-defensive-bets-hold-firm-as-hasbro-kohl-s-boston-beer-lead-weekly-consumer-gains/)  
  <sub>TradingView, 9 hours ago</sub>  
  U.S. consumer stocks edged higher last week even as the broader market slipped, with investors favoring defensive names. Hasbro Inc. (HAS), Kohls Corp.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 114.89 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 112.27 (+2.3%), 50d 113.37 (+1.3%), 200d 115.72 (-0.7%); 50d below 200d
Momentum: RSI(14) 57.4 | MACD 0.625 vs signal 0.223 (histogram 0.402)
Returns: 1d +1.6% | 5d +0.4% | 1m +3.9% | 3m +2.1%
52-week range: 105.66 - 124.52 (now 48.9% of the way up)
Volatility: ATR(14) 1.65 (1.4% of price) | annualised 20d 14.9%
Volume: 0.25x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 54.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.4% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, TJX
Recent rating changes among them:
  - AMZN: 2026-10-19 Morgan Stanley: main, Overweight -> Overweight
  - TSLA: 2026-10-26 Barclays: up, Equal-Weight -> Overweight
  - HD: 2026-09-09 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-10-26 BTIG: reit, Buy -> Buy
  - TJX: 2026-10-22 Wolfe Research: init, ? -> Peer Perform
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 120.25M | fund size: 13.82B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 121.60 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 120.01 (+1.3%), 50d 122.20 (-0.5%), 200d 123.19 (-1.3%); 50d below 200d
Momentum: RSI(14) 52.5 | MACD -0.464 vs signal -0.789 (histogram 0.326)
Returns: 1d +1.5% | 5d +1.6% | 1m -1.1% | 3m +2.4%
52-week range: 99.40 - 137.69 (now 58.0% of the way up)
Volatility: ATR(14) 1.77 (1.5% of price) | annualised 20d 16.7%
Volume: 0.26x the 20-day average
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
Weighted price target: +21.9% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 2.55M | fund size: 310.07M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 47.72 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 46.94 (+1.7%), 50d 47.64 (+0.2%), 200d 46.92 (+1.7%); 50d above 200d
Momentum: RSI(14) 55.4 | MACD 0.107 vs signal -0.039 (histogram 0.147)
Returns: 1d +0.4% | 5d +0.8% | 1m +0.9% | 3m -0.2%
52-week range: 41.34 - 49.39 (now 79.3% of the way up)
Volatility: ATR(14) 0.47 (1.0% of price) | annualised 20d 13.0%
Volume: 0.15x the 20-day average
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
Three-year record: +20.1% a year | beta to the market 0.71
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
Ratings by weight: buy 59.1% | hold 40.9% | sell 0.0% (mean 2.13 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.5% above the current prices
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 67.80M | fund size: 3.24B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Should You Invest in the State Street Industrial Select Sector SPDR ETF (XLI)?](https://finance.yahoo.com/markets/stocks/articles/invest-state-street-industrial-select-092002901.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Looking for broad exposure to the Industrials - Broad segment of the equity market? You should consider the State Street Industrial Select Sector SPDR ETF...
- [When the Price of (XLB) Talks, People Listen (XLB:CA)](https://news.stocktradersdaily.com/canada/when-the-price-of-xlb-talks,-people-listen_20261026_99658b)  
  <sub>Stock Traders Daily, 44 minutes ago</sub>  
  When the Price of iShares Core Canadian Long Term Bond Index ETF XLB Talks, People Listen.
- [What to Expect From Air Products and Chemicals' Next Quarterly Earnings Report](https://www.barchart.com/story/news/8455550/what-to-expect-from-air-products-and-chemicals-next-quarterly-earnings-report)  
  <sub>Barchart.com, 15 minutes ago</sub>  
  Air Products and Chemicals will release its fourth-quarter earnings next week, and analysts anticipate a single-digit bottom-line growth.
- [State Street Consumer Discretionary (XLY) Adds Amazon and Tesla on Thursday](https://finance.yahoo.com/markets/stocks/articles/state-street-consumer-discretionary-xly-110437610.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Consumer Discretionary Select Sector SPDR ETF (XLY) was the only ETF buying among those tracked,...
- [Watch These Etfs Ahead Of The U.S. Midterm Elections](https://menafn.com/1111866080/Watch-These-Etfs-Ahead-Of-The-US-Midterm-Elections)  
  <sub>Menafn, 5 hours ago</sub>  
  Watch These Etfs Ahead Of The U.S. Midterm Elections. Stock markets started pricing in the outcome of the hotly contested House and Senate seats.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 51.41 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 50.02 (+2.8%), 50d 50.99 (+0.8%), 200d 51.00 (+0.8%); 50d below 200d
Momentum: RSI(14) 60.4 | MACD 0.260 vs signal -0.017 (histogram 0.277)
Returns: 1d +0.2% | 5d +0.9% | 1m +3.2% | 3m -1.8%
52-week range: 42.23 - 53.67 (now 80.2% of the way up)
Volatility: ATR(14) 0.70 (1.4% of price) | annualised 20d 12.2%
Volume: 0.29x the 20-day average
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
Weighted price target: +14.3% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 71.92M | fund size: 3.70B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Macro: yields down slightly, inflation 3.7% in line, no data surprise
- Technicals: price 4.7% below 20‑day SMA, RSI 40.3, MACD below signal
- Positioning: net long 21.9% of OI, crowding 98th percentile, weekly change -0.2%
- Cost of holding: -6.5% annual roll cost, heavy negative carry
- Fund flows: share count down 15.6% over month, indicating outflows

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 11.48 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 12.04 (-4.7%), 50d 11.61 (-1.1%), 200d 10.18 (+12.8%); 50d above 200d
Momentum: RSI(14) 40.3 | MACD 0.155 vs signal 0.240 (histogram -0.086)
Returns: 1d -5.5% | 5d -6.3% | 1m +2.4% | 3m +20.0%
52-week range: 9.02 - 12.47 (now 71.3% of the way up)
Volatility: ATR(14) 0.23 (2.0% of price) | annualised 20d 31.0%
Volume: 0.70x the 20-day average
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
Cost of holding this fund instead of sugar itself: -6.5% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +20.0%, commodity +31.5%, gap -11.5% | 6 months: fund +22.3%, commodity +38.3%, gap -16.1% | 12 months: fund +18.6%, commodity +25.1%, gap -6.5%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-10-20, published the following Friday)
Large speculators: net long 21.9% of open interest (1,210,639 contracts)
Change on the week: -0.2% of open interest
Crowding: 98% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +2.0% (978.16K) over 7d | 1 month: -15.6% (-9.36M) over 30d
Shares outstanding: 4.40M | fund size: 50.50M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- CFTC net long fell 4.4% of open interest this week
- Fund share count down 10.5% over the past month (outflows)
- Cost of holding -6.3% per year (heavy roll cost)
- RSI(14) at 25.6 (oversold) with volume at 0.18x 20‑day average

<details><summary><b>News</b> — score +0.00</summary>

- [Corn Falling with Spillover Pressure from Soybeans](https://www.barchart.com/story/news/8453102/corn-falling-with-spillover-pressure-from-soybeans)  
  <sub>Barchart.com, 3 hours ago</sub>  
  Corn prices are down 3 to 5 cents so far on Monday. Futures failed to see buying into the weekend, with contracts down 1 ¼ to 4 ½ cents on Friday.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 17.61 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 18.49 (-4.8%), 50d 19.22 (-8.4%), 200d 18.18 (-3.1%); 50d above 200d
Momentum: RSI(14) 25.6 | MACD -0.440 vs signal -0.350 (histogram -0.090)
Returns: 1d -0.4% | 5d -2.2% | 1m -10.7% | 3m -2.6%
52-week range: 16.47 - 20.29 (now 29.9% of the way up)
Volatility: ATR(14) 0.27 (1.5% of price) | annualised 20d 16.3%
Volume: 0.18x the 20-day average
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
Cost of holding this fund instead of corn itself: -6.3% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -2.6%, commodity -1.0%, gap -1.6% | 6 months: fund -4.9%, commodity -1.5%, gap -3.3% | 12 months: fund -0.3%, commodity +6.0%, gap -6.3%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.20</summary>

```text
Corn rated good or excellent: 56% of the US crop (week 42 of 2026)
Direction over 3 weeks: steady, +2 points
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
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-10-20, published the following Friday)
Large speculators: net long 9.0% of open interest (1,835,658 contracts)
Change on the week: -4.4% of open interest
Crowding: 67% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +3.5% (4.37M) over 7d | 1 month: -10.5% (-15.05M) over 30d
Shares outstanding: 7.31M | fund size: 128.82M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, mixed technicals, modest bearish positioning and cost drag, but overall no clear directional catalyst.

**Main reasons it gave:**
- Positioning shows net long 14.6% and decreased 4.9% week‑over‑week, indicating a crowded short
- Cost of holding drag of -3.4% per year, a tailwind for short positions
- Technicals mixed: price below 20‑day SMA (39.68) and 50‑day SMA (39.79) but above 200‑day SMA (37.84)
- Macro data unchanged: inflation 3.7% above target, yields down slightly, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 39.30 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 39.68 (-1.0%), 50d 39.79 (-1.2%), 200d 37.84 (+3.9%); 50d above 200d
Momentum: RSI(14) 46.6 | MACD -0.185 vs signal -0.084 (histogram -0.101)
Returns: 1d +0.6% | 5d -0.7% | 1m -3.2% | 3m +2.5%
52-week range: 30.53 - 41.43 (now 80.5% of the way up)
Volatility: ATR(14) 0.58 (1.5% of price) | annualised 20d 17.5%
Volume: 0.32x the 20-day average
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
Cost of holding this fund instead of copper itself: -3.4% a year -- a steady drag
Measured: 3 months: fund +2.5%, commodity +3.3%, gap -0.8% | 6 months: fund +6.4%, commodity +8.5%, gap -2.1% | 12 months: fund +25.1%, commodity +28.5%, gap -3.4%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.25</summary>

```text
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-10-20, published the following Friday)
Large speculators: net long 14.6% of open interest (327,119 contracts)
Change on the week: -4.9% of open interest
Crowding: 2% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.25</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +4.0% (28.12M) over 7d | 1 month: +0.2% (1.17M) over 30d
Shares outstanding: 18.54M | fund size: 728.49M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral – no macro surprise, technicals not decisive, modest bearish tilt in positioning, modest cost drag, flat fund flows.

**Main reasons it gave:**
- US Treasury yields and Fed target unchanged; no macro policy surprise
- Price below 20‑day, 50‑day, and 200‑day SMAs and RSI 32.3, but no decisive break on heavy volume
- Large speculators net long 3.1% of OI, weekly change -2.1% indicating slight shift toward short
- Cost of holding -1.1% annual drag, modest negative for long positions
- Fund flows flat over 1 month, indicating no net inflow or outflow

<details><summary><b>News</b> — score +0.00</summary>

- [2026 Tax-Loss Harvesting Opportunities With VanEck ETFs](https://seekingalpha.com/article/4957428-2026-tax-loss-harvesting-opportunities-with-vaneck-etfs)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Tax-loss harvesting may work best when you swap into a similar, not identical, fund to stay compliant with the wash-sale rule. We screened US-listed ETFs...
- [What Newmont’s Outperformance and Extreme Short Data Reveal About Gold](https://www.google.com/goto?url=CAESvQEB6zswFXkcN0zUSIWnAFGD7FMLEWtkY418bivfg-mI1JRTqLZyMR0uL9PVanqhatLpgZ09TnKYQOwe3YNH7YJlS-OzZacbVTwnyFGnz3f4LF0poT_RH1K9J2BmUX1YDfTv9982bHquu33C0Kbl90mzD6N6QR0mWg6JOw83PjGC_VCsag4Ewe7HW6_wGRmcObKxXdTJJ_9srw-v3kYv7wAYlrk8bI4PjoNWuXG4NkKFzQvYFiyUDHUCOeIhTz8)  
  <sub>Benzinga, 4 hours ago</sub>  
  Gold and silver hit extreme oversold levels as analysts signal selloff exhaustion. Discover why top traders are turning bullish.
- [News by CNBC TV18 on TradingView, 2026-10-26 — cnbctv:673f7b4a3094b:0](https://www.google.com/goto?url=CAEScwHrOzAVCjpSoM_naBQdyx7y5HyWqMLeFBVUPHd8qnKW-FsBF5xGQlDLY9m3GiddQrCPdoBSjXIF2DqGRdjT_TfVVJWXO0d_zAszvnaX6ES0_TI_wdFXqMb_uRN7SxqYG9pacURa5A8F6iLtH3FeYeE_znc)  
  <sub>TradingView, 9 hours ago</sub>  
  Silver prices have fallen sharply from their January 2026 record highs, raising questions about whether the correction offers an opportunity for investors...
- [Gold dips below $4,000 as long liquidation swamps ETF buying, Saxo Bank says](https://www.google.com/goto?url=CAESrAEB6zswFTBkSMI286t1GBDvYFa5gCuIXxAOievaGkD972TU-8XrkfOGBNe68RZzR5ksy5HFwyC6tmZaIiuzlZh97SYtzCK2bR1ZzpAzdFdSTw6TVezZLl9x_YzNbNRgUMRQQxUaZK3HJO95dUlgkaSwETl5ri4_KQCtUrpRQXhBeku8QNyNBfPfYZssjz6toOOuGvK1Uyb3IxNKLyfWFRouvsHNWp-5r_WzDV8p)  
  <sub>investingLive, 14 hours ago</sub>  
  Saxo Bank says long liquidation and momentum selling pushed gold briefly below $4000 despite a US Treasury rally, while silver fell toward an 11-month low…
- [Silver prices fall 53% from peak: Should buyers wait or buy now? Here’s the Outlook](https://www.google.com/goto?url=CAES1QEB6zswFYzr8OFYUHuRdZne8tkpvOBA06ny9drTbWjlajQ5Uh1GR9iztgmX8tQcDdx6WiNvD9GbAWhIKoGtJaIhq37Vn_KIEXlhtB8O2CmeMNzD9YDRFpkT7O52JScgEQzs_LfP0j6EBH0dLihEraldddmPH_ntKPPOf4187Fx_3NN6DW3il-BHpMW7JOYsWmIJlMlOk7iOubDN1ozkHe2knPYqPg3MtD2aBm2-s_Oxe-w86ImOSdR3TZeYo3V6BE9mmrut9YjiA-F3Ya9jOnwPwWexKnA)  
  <sub>Moneycontrol.com, 10 hours ago</sub>  
  Silver prices face a crucial test, trading 53 percent below their all-time high as Middle East tensions and persistent inflation, driven largely by elevated...
- [Silver Rate Today in Anand 26th October 2026 : 1 KG, Todays Silver Price in Anand](https://www.google.com/goto?url=CAESfAHrOzAVxvdtnHmZZu73Fptks0IykK7DQkkOnGogJQomlSnoSEosyhNWeihOckguP7lGlI8ChetRvgTd177wmkplZwNu_g7SUF_qtMDx2Qp1Eaxk1zi0A1GblZvWtRR9zyP78qnQ4YKH5sahhZHr5fwk7D99K4sRpqmaLWE)  
  <sub>Business Today, 1 hour ago</sub>  
  Silver Price in Anand Today 26th October 2026: Find updated 1 KG Silver rate today in Anand 26th October 2026. Also check latest gold price related news,...
- [Silver Rate Today Live, Latest Silver Price In India](https://www.google.com/goto?url=CAESYgHrOzAVsr5AC57Fox6NGitsxF_xHm73dtvxxiVd6iSNjFzx1mT6p9wMk8i7d3YVV1gK2bnhL88nlmQm0QrkZPYBiuGVzw6jRGniNPWCNP59eUObGzSY7BgAVblOGRSACm1Y)  
  <sub>NDTV Profit, 7 hours ago</sub>  
  Track the silver rates today in India with live updates. Check the latest silver prices, daily movements, historical trends, news and key market insights on...
- [5 new fund offers (NFOs) open this week: ICICI Prudential, Kotak, Invesco among AMCs launching schemes](https://www.google.com/goto?url=CAES5AEB6zswFcujeXrs_e4DLb6fDsMy-OHzUJwcBoFUrUWcrxCn1WozDr006hq0ohKwXVifwa2Jp7U8MuPPWEOC8glp6sfF9DvE-p9-9VBcaunfJ5xy-ScV5Q7hmB33Hx8K2hd2AUzRrqd8aZV26ouZBNJdv0qLfYXSlt6uWFNUaW2Y-MLDPeYY9_YtYBh88qBgKJJOlaRvbA80WsN57eLOK7IDjVvOe7iAe_J-w_NjNhnIO41J0HiabkdWLNkOG5BbqlFuMLnSWbOA-_gqGW-hU-3vez-b9unlI5NmJTf7w_SC-NmGBe8)  
  <sub>Upstox, 12 hours ago</sub>  
  Check this week's mutual fund NFOs from ICICI Prudential, Kotak, Invesco and UTI, along with six schemes closing on October 26, 2026.
- [Silver Rate Today In Coimbatore Live, Latest Silver Price](https://www.google.com/goto?url=CAESgwEB6zswFQLEi2qDb9sceIHH9m8op5HLe5AfLWUtf7Z4G9-GETUX5x9W-X6ZJNPAZVJoU_QLTRmPfzdklVkP0XYwAFPq6B7W4LXN45B-KG5A0klsgM6gbg1gJw_E3ZABpj7ki7m3WEkS_wc18n81ZdRaMS_6PNbtdwJn3wKkGSvs7xQZnQ)  
  <sub>NDTV Profit, 13 hours ago</sub>  
  Track the silver rates today in Coimbatore with live updates. Check the latest silver prices, daily movements, historical trends, news and key market...
- [Silver Rate Today In Indore Live, Latest Silver Price](https://www.google.com/goto?url=CAESfwHrOzAVcjxKcmZ9uSeUw6NSpidUl7OmLGxHKj9QoTx8jENQhmGrsJjC1MHsDS-UNBOKHx2xXSSB2e5wJiAaEvgBZuOkS4wyim1a-RUEq74sRoehbgnLhyDw-aK-5Feb5eZGG21E4VtIJCo7Bi5sBLqTabokeFvMYpAKH6xe2yw)  
  <sub>NDTV Profit, 18 hours ago</sub>  
  Track the silver rates today in Indore with live updates. Check the latest silver prices, daily movements, historical trends, news and key market insights...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 48.90 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 52.84 (-7.4%), 50d 56.80 (-13.9%), 200d 64.85 (-24.6%); 50d below 200d
Momentum: RSI(14) 32.3 | MACD -2.004 vs signal -1.678 (histogram -0.326)
Returns: 1d +0.4% | 5d -5.1% | 1m -15.9% | 3m -5.4%
52-week range: 42.40 - 105.60 (now 10.3% of the way up)
Volatility: ATR(14) 1.53 (3.1% of price) | annualised 20d 36.8%
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
Cost of holding this fund instead of silver itself: -1.1% a year -- a steady drag
Measured: 3 months: fund -5.4%, commodity -5.4%, gap -0.0% | 6 months: fund -28.4%, commodity -27.7%, gap -0.7% | 12 months: fund +10.7%, commodity +11.8%, gap -1.1%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

```text
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-10-20, published the following Friday)
Large speculators: net long 3.1% of open interest (113,992 contracts)
Change on the week: -2.1% of open interest
Crowding: 2% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 341.45M | fund size: 16.70B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US Treasury yields unchanged; inflation 3.7% within expectations
- Technicals: price 26.32 below 20‑day SMA (27.14) and 50‑day SMA (27.23), RSI 33.4 (oversold), but above 200‑day SMA (25.02)
- Large speculators net long 20.2% of open interest, down 3.1% week‑over‑week
- Fund share count up 3.2% over the month, indicating inflows
- US soybean crop condition steady at 57% good/excellent, slight 1‑point decline

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 26.32 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 27.14 (-3.0%), 50d 27.23 (-3.3%), 200d 25.02 (+5.2%); 50d above 200d
Momentum: RSI(14) 33.4 | MACD -0.210 vs signal -0.100 (histogram -0.110)
Returns: 1d -1.8% | 5d -1.7% | 1m -5.1% | 3m +2.4%
52-week range: 21.71 - 28.14 (now 71.7% of the way up)
Volatility: ATR(14) 0.30 (1.1% of price) | annualised 20d 11.6%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.20</summary>

```text
Cost of holding this fund instead of soybeans itself: -0.8% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +2.4%, commodity +2.6%, gap -0.2% | 6 months: fund +6.7%, commodity +5.6%, gap +1.1% | 12 months: fund +18.2%, commodity +19.0%, gap -0.8%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.20</summary>

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
Share count change: 1 week: +2.0% (876.29K) over 7d | 1 month: +3.2% (1.38M) over 30d
Shares outstanding: 1.70M | fund size: 44.78M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise (inflation 3.7% in line with expectations)
- Technical trend below SMAs and RSI 33.7 (bearish but no decisive break)
- Heavy cost of holding (-16.9% annual) tailwinds short
- US natural gas inventories built 77 BCF, 87th percentile (bearish)
- EIA forecast expects price to fall ~18% over six months (bearish)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 9.51 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 10.53 (-9.8%), 50d 10.47 (-9.2%), 200d 11.23 (-15.3%); 50d below 200d
Momentum: RSI(14) 33.7 | MACD -0.195 vs signal -0.020 (histogram -0.174)
Returns: 1d -0.8% | 5d -9.1% | 1m -14.6% | 3m -3.0%
52-week range: 9.51 - 16.90 (now 0.0% of the way up)
Volatility: ATR(14) 0.36 (3.8% of price) | annualised 20d 40.1%
Volume: 0.31x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.70</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.70</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.70</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.70</summary>

```text
Cost of holding this fund instead of natural gas itself: -16.9% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -3.0%, commodity +13.6%, gap -16.5% | 6 months: fund -9.4%, commodity +18.5%, gap -27.9% | 12 months: fund -26.5%, commodity -9.6%, gap -16.9%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.70</summary>

```text
US inventories, week ending 2026-10-16 (published the following Wednesday)
  Natural gas: 3,644.0 billion cubic feet, +77.0 on the week (a build), 87% percentile over 52 weeks -- high for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.70</summary>

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
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-10-20, published the following Friday)
Large speculators: net short 9.2% of open interest (1,710,685 contracts)
Change on the week: -1.9% of open interest
Crowding: 2% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 12.08M | fund size: 114.90M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- EIA forecast projects WTI price falling to $100 this month, far below current $165.21 (bearish)
- U.S. crude inventories draw of 3.1 million barrels (bullish)
- Technicals: price above 20‑day, 50‑day, 200‑day SMAs; RSI 64.6 (bullish trend)
- Large speculators net long 2% of OI, weekly change –0.2% (slightly bearish positioning)
- Top economist warns oil could surge to $150 if Middle East conflict widens (potential bullish news)

<details><summary><b>News</b> — score +0.00</summary>

- [USO Jan 2027 143.000 put (USO270115P00143000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/USO270115P00143000/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Find the latest USO Jan 2027 143.000 put (USO270115P00143000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Top Economist Warns 'Oil at 150' Could Deal a 'Significant Blow' to the Global Economy if Iran Conflict Widens: 'We Don't Have These Two Other Things That We Had Before...'](https://www.tradingview.com/news/benzinga:e3fe7bb35094b:0-top-economist-warns-oil-at-150-could-deal-a-significant-blow-to-the-global-economy-if-iran-conflict-widens-we-don-t-have-these-two-other-things-that-we-had-before/)  
  <sub>TradingView, 2 hours ago</sub>  
  Oil prices face the risk of surging to $150 per barrel if Middle East conflicts widen, according to Mohamed El-Erian, despite President Donald Trump ruling...
- [USO Jan 2028 290.000 put (USO280121P00290000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/USO280121P00290000/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest USO Jan 2028 290.000 put (USO280121P00290000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Biggest Earnings Week, Then Elections, And Iran: What Happens? Maybe Rally (SPX)](https://seekingalpha.com/article/4957363-biggest-earnings-week-then-elections-and-iran-what-happens-maybe-rally)  
  <sub>Seeking Alpha, 13 hours ago</sub>  
  Despite election uncertainty, I see markets positioned for a pre-election rally. Click here to read more about the market.
- [USO Oct 2026 129.000 put (USO261028P00129000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/USO261028P00129000/chart/)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  Interactive Chart for USO Oct 2026 129.000 put (USO261028P00129000), analyze all the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.50</summary>

```text
Last close 165.21 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 153.51 (+7.6%), 50d 147.24 (+12.2%), 200d 122.08 (+35.3%); 50d above 200d
Momentum: RSI(14) 64.6 | MACD 5.262 vs signal 4.072 (histogram 1.190)
Returns: 1d -2.6% | 5d +2.7% | 1m +11.4% | 3m +37.1%
52-week range: 66.17 - 169.53 (now 95.8% of the way up)
Volatility: ATR(14) 5.07 (3.1% of price) | annualised 20d 34.6%
Volume: 0.62x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.70</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.70</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.70</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.70</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.70</summary>

```text
US inventories, week ending 2026-10-16 (published the following Wednesday)
  Crude oil: 412.5 million barrels, -3.1 on the week (a draw), 15% percentile over 52 weeks
  Petrol: 205.3 million barrels, -3.0 on the week (a draw), 8% percentile over 52 weeks -- low for the time of year
  Diesel: 104.3 million barrels, +1.7 on the week (a build), 25% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.70</summary>

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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 36d
Shares outstanding: 119.10M | fund size: 19.68B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: yields unchanged, inflation 3.7% in line with expectations
- Technicals: price below 20d, 50d, 200d SMAs, RSI 23.1 (oversold) but no breakout
- Cost of holding: -10.1% annual roll cost, heavy drag on long positions
- Positioning: net short 10.1% of OI, down 3.6% on week, indicating slight reduction in bearish bets

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 22.53 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 24.19 (-6.9%), 50d 25.43 (-11.4%), 200d 23.50 (-4.1%); 50d above 200d
Momentum: RSI(14) 23.1 | MACD -0.718 vs signal -0.549 (histogram -0.169)
Returns: 1d -1.3% | 5d -5.7% | 1m -11.7% | 3m -8.5%
52-week range: 19.88 - 28.00 (now 32.6% of the way up)
Volatility: ATR(14) 0.44 (2.0% of price) | annualised 20d 17.2%
Volume: 1.24x the 20-day average
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
Cost of holding this fund instead of wheat itself: -10.1% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -8.5%, commodity -7.3%, gap -1.2% | 6 months: fund -5.0%, commodity -1.2%, gap -3.8% | 12 months: fund +9.6%, commodity +19.7%, gap -10.1%
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
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-10-20, published the following Friday)
Large speculators: net short 10.1% of open interest (516,379 contracts)
Change on the week: -3.6% of open interest
Crowding: 53% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +6.7% (17.69M) over 7d | 1 month: -9.8% (-30.58M) over 30d
Shares outstanding: 12.44M | fund size: 280.30M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Selling $300,000 of GLD Bought Five Years Ago Means a $162,713 Gain Taxed as a Collectible, Not a Stock](https://247wallst.com/investing/etf/2026/10/25/selling-300000-of-gld-bought-five-years-ago-means-a-162713-gain-taxed-as-a-collectible-not-a-stock/)  
  <sub>24/7 Wall St., 18 hours ago</sub>  
  GLD trades like a stock but the IRS does not treat it like one, and the difference in your tax bill when you finally sell could be far larger than you...
- [GLD Nov 2026 376.000 call (GLD261113C00376000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/GLD261113C00376000/chart/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Interactive Chart for GLD Nov 2026 376.000 call (GLD261113C00376000), analyze all the data with a huge range of indicators.
- [2026 Tax-Loss Harvesting Opportunities With VanEck ETFs](https://seekingalpha.com/article/4957428-2026-tax-loss-harvesting-opportunities-with-vaneck-etfs)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Tax-loss harvesting may work best when you swap into a similar, not identical, fund to stay compliant with the wash-sale rule. We screened US-listed ETFs...
- [Why Did AAPL, KO, KDP Stocks Hit 52-Week Highs Today?](https://stocktwits.com/news-articles/markets/equity/why-did-aapl-ko-kdp-stocks-hit-52-week-highs-today/cZxyRFLRBDA)  
  <sub>Stocktwits, 3 hours ago</sub>  
  Apple Inc. (AAPL), Coca-Cola Co. (KO) and Keurig Dr Pepper (KDP) hit fresh 52-week highs on Thursday as investors reacted to strong demand for Apple's new...
- [What Newmont’s Outperformance and Extreme Short Data Reveal About Gold](https://www.benzinga.com/markets/commodities/26/10/62584567/what-newmonts-outperformance-and-extreme-short-data-reveal-about-gold)  
  <sub>Benzinga, 4 hours ago</sub>  
  Gold and silver hit extreme oversold levels as analysts signal selloff exhaustion. Discover why top traders are turning bullish.
- [Gold News: XAUUSD Gets Fed-Week Relief, but Inflation Keeps Bears in Control](https://www.fxempire.com/forecasts/article/gold-news-xauusd-gets-fed-week-relief-but-inflation-keeps-bears-in-control-1640273)  
  <sub>FXEmpire, 4 hours ago</sub>  
  Gold edges higher before the Fed decision, but December hike odds, PCE inflation and key XAUUSD resistance keep the broader outlook bearish.
- [GLD Oct 2026 392.000 put (GLD261021P00392000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/GLD261021P00392000/chart/)  
  <sub>Yahoo! Finance Canada, 8 hours ago</sub>  
  Interactive Chart for GLD Oct 2026 392.000 put (GLD261021P00392000), analyze all the data with a huge range of indicators.
- [Selling GLD ETF gains taxed as collectibles at up to 28%, not as regular stock gains.](https://pluang.com/en/news-feed/jual-gld-300000-dolar-untung-pajak-kolektibel-bukan-saham)  
  <sub>Pluang, 19 hours ago</sub>  
  Investors selling SPDR Gold Shares (GLD) realize gains taxed as collectibles, not stocks, due to IRS rules treating gold holdings differently.
- [BB Stock Slips Overnight: Retail Debates CEO's Share Sale Amid Strong QNX Demand](https://stocktwits.com/news-articles/markets/equity/bb-stock-slips-overnight-retail-debates-ceo-s-share-sale-amid-strong-qnx-demand/cZxy2y4RBDD)  
  <sub>Stocktwits, 22 hours ago</sub>  
  BlackBerry (BB) stock dipped overnight as investors weighed CEO John Giamatteo's planned sale of 99000 shares worth about $865000 against strong QNX demand.
- [HGER: A Primer On The Harbor Commodity All-Weather Strategy ETF](https://seekingalpha.com/article/4952552-hger-primer-on-harbor-commodity-all-weather-strategy-etf)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  The Harbor Commodity All-Weather Strategy ETF tracks a rules-based index that weights commodity futures by inflation sensitivity and roll costs.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (-0.03 on the week) | 5-year 4.80% (-0.13 on the week) | 10-year 4.97% (-0.17 on the week) | 30-year 5.28% (-0.19 on the week)
Yield curve, 10-year minus 3-month: +0.92 points -- upward sloping (normal)
US dollar index: 101.99 (+0.01 on the week)
Volatility (VIX): 18.30 (-0.1 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.65% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 368.56 (bar of 2026-10-26), from 500 daily bars
Trend: vs 20d SMA 378.63 (-2.7%), 50d 393.85 (-6.4%), 200d 413.99 (-11.0%); 50d below 200d
Momentum: RSI(14) 36.5 | MACD -5.597 vs signal -4.822 (histogram -0.775)
Returns: 1d +0.5% | 5d -2.9% | 1m -6.3% | 3m -0.2%
52-week range: 362.32 - 495.90 (now 4.7% of the way up)
Volatility: ATR(14) 5.66 (1.5% of price) | annualised 20d 17.5%
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
Cost of holding this fund instead of gold itself: -0.1% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund -0.2%, commodity -0.0%, gap -0.2% | 6 months: fund -14.3%, commodity -14.0%, gap -0.3% | 12 months: fund -2.7%, commodity -2.6%, gap -0.1%
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

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 260.30M | fund size: 95.94B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- CFTC positioning unavailable: [Errno 104] Connection reset by peer

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

