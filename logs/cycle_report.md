# Daily report

**20 Oct 2026, 18:52 Israel time (15:52 UTC)** · 80 names checked · 0 traded · 0 with a problem

**Answers with no explanation:** 17 of 65 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

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
| ASML (ASML) · Company | **Stop raised.** At -0.04R, following the price. Stop-loss raised 1750.37 → 1750.24. |
| Eli Lilly (LLY) · Company | **Stop raised.** At +2.45R, following the price. Stop-loss raised 1195.64 → 1224.49. |
| US materials and chemicals (XLB) · Sector or country | **Stop raised.** At +0.00R, following the price. Stop-loss raised 49.50 → 49.58. |
| Argentina (ARGT) · Sector or country | **Holding.** -0.15R, holding 80 shares. Stop-loss 86.01. |
| United Kingdom (EWU) · Sector or country | **Holding.** +1.68R, holding 104 shares. Stop-loss 47.23. |
| Gold (GLD) · Commodity | **Holding.** +0.58R, holding 10 shares. Stop-loss 387.99. |
| Alphabet (Google) (GOOGL) · Company | **Holding.** -0.53R, holding 14 shares. Stop-loss 338.49. |
| HDFC Bank (HDB) · Company | **Holding.** -0.15R, holding 4 shares. Stop-loss 22.82. |
| US company bonds, riskier (HYG) · Index fund | **Holding.** -0.23R, holding 158 shares. Stop-loss 76.66. |
| Defence and aerospace (ITA) · Sector or country | **Holding.** -0.15R, holding 33 shares. Stop-loss 201.78. |
| Nvidia (NVDA) · Company | **Holding.** -0.06R, holding 23 shares. Stop-loss 228.84. |
| Royal Bank of Canada (RY) · Company | **Holding.** +0.49R, holding 17 shares. Stop-loss 192.77. |
| Teva Pharmaceutical (TEVA) · Company | **Holding.** +0.87R, holding 86 shares. Stop-loss 39.51. |
| US media and communication (XLC) · Sector or country | **Holding.** -0.46R, holding 60 shares. Stop-loss 108.76. |
| Exxon Mobil (XOM) · Company | **Holding.** +1.87R, holding 9 shares. Stop-loss 170.88. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Elbit Systems (ESLT) · Company — BULLISH, confidence 0.75

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> The $235M European rocket artillery contract provides a strong, material catalyst that is corroborated by a solid earnings beat record and bullish technical momentum, while high valuation and thin volume temper the upside.

**Main reasons it gave:**
- $235M European rocket artillery contract announced
- Four consecutive earnings beats in last four quarters
- Technical momentum bullish (RSI 61.8, MACD above signal) but thin volume (0.34x 20‑day avg)
- High valuation (trailing P/E 56.8) tempers upside

<details><summary><b>News</b> — score +0.90</summary>

- [42,705 shares are held for Harel’s own account within its reported Elbit Systems (ESLT) stake.](https://www.stocktitan.net/sec-filings/ESLT/schedule-13g-elbit-systems-ltd-passive-investment-disclosure-5-c8996272bfc5.html)  
  <sub>Stock Titan, 5 hours ago</sub>  
  Public holdings account for 2351970 shares and client accounts for 29854. Harel says the report does not admit ownership beyond 42705 shares.
- [Lobbying Update: $190,000 of ELBIT SYSTEMS OF AMERICA LLC lobbying was just disclosed](https://www.quiverquant.com/news/Lobbying+Update%3A+%24190%2C000+of+ELBIT+SYSTEMS+OF+AMERICA+LLC+lobbying+was+just+disclosed)  
  <sub>Quiver Quantitative, 8 hours ago</sub>  
  of ELBIT SYSTEMS OF AMERICA LLC lobbying was just disclosed, from Q3 of 2026, in a new Lobb.
- [Elbit Systems Wins $235M Contract To Supply Rocket Artillery Systems To European Customer: What Investors Need To Know](https://stocktwits.com/news-articles/markets/equity/elbit-systems-wins-235-m-contract-to-supply-rocket-artillery-systems-to-european-customer-what-investors-need-to-know/cZx8ZAKRBMS)  
  <sub>Stocktwits, 16 hours ago</sub>  
  Elbit Systems (ESLT) drew investor attention on Monday after the defense technology company announced a $235 million contract to supply EXTRA-MR rockets and...
- [Can Ondas' EASA Certification Boost Its Airborne Defense Prospects?](https://finance.yahoo.com/technology/articles/ondas-easa-certification-boost-airborne-123000385.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  ONDS' EASA certification for its AMPS missile protection system boosts its airborne defense prospects, while acquisitions and strong orders fuel growth...
- [Elbit Systems Secures $235 Million European Defense Deal](https://www.benzinga.com/news/contracts/26/10/62442703/elbit-systems-secures-235-million-european-defense-deal)  
  <sub>Benzinga, 23 hours ago</sub>  
  Elbit Systems Ltd. (NASDAQ:ESLT) stock edged higher on Monday. The company announced a $235 million contract to supply rocket artillery systems to a...
- [SEC Filings for Oct 20, 2026 - 10-K, 10-Q, 8-K Forms](https://www.stocktitan.net/sec-filings/2026-10-20/)  
  <sub>Stock Titan, 4 hours ago</sub>  
  SEC filings for October 20, 2026 including 10-K annual reports, 10-Q quarterly reports, 8-K material events, and Form 4 insider trades.
- [Elbit Systems wins USD 235 million deal as stock trades at EUR 674.75](https://www.ad-hoc-news.de/boerse/news/corporate-news/elbit-systems-wins-usd-235-million-deal-as-stock-trades-at-eur-674-75/70370017)  
  <sub>ad-hoc-news.de, 7 hours ago</sub>  
  Elbit Systems won a USD 235.0 million European rocket contract on October 19, 2026. Elbit Systems stock trades at EUR 674.75.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 754.47 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 706.15 (+6.8%), 50d 724.80 (+4.1%), 200d 781.90 (-3.5%); 50d below 200d
Momentum: RSI(14) 61.8 | MACD 2.456 vs signal -8.326 (histogram 10.782)
Returns: 1d -0.7% | 5d +13.0% | 1m +0.5% | 3m -4.8%
52-week range: 454.95 - 1,014.33 (now 53.5% of the way up)
Volatility: ATR(14) 19.83 (2.6% of price) | annualised 20d 40.1%
Volume: 0.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 35.36B
Valuation: trailing P/E 56.77 | forward P/E 40.54 | P/B 8.00 | PEG n/a
Profitability: profit margin 7.4% | operating margin 9.6% | ROE 15.2%
Growth (YoY): revenue +15.9% | earnings +34.2%
Balance sheet: debt/equity 19.3% | free cash flow -38.48M
Risk: beta -0.30 | short interest 0.8% of float
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: hold (mean 2.67 on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 802.17 (+6.3% vs last close), range 518.00 - 960.00
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

### MercadoLibre (MELI) · Company — BULLISH, confidence 0.60

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> The news includes a material catalyst (one‑hour delivery rollout and prescription‑medicine entry) that outweighs recent institutional sell‑offs. Insider purchases (officer and director) add a positive signal. Technicals show modest bullish momentum despite thin volume. Fundamentals are mixed (high growth but high valuation and leverage) and earnings record is weak (3 misses of 4). Overall net positive outlook leads to a bullish signal with moderate conviction.

**Main reasons it gave:**
- One‑hour delivery rollout in São Paulo and entry into prescription medicines (NEWS)
- Insider purchases: 124 shares by officer, 600 shares by director (INSIDER ACTIVITY)
- Technical bullish signals: price above 20‑day SMA, positive MACD, RSI 52.7 (TECHNICALS)
- Institutional position cuts: CWA Asset Management down 10.1%, James Hambro down 15.5% (NEWS)
- Earnings record: 3 of last 4 quarters missed consensus (EARNINGS RECORD)

<details><summary><b>News</b> — score +0.50</summary>

- [MercadoLibre, Inc. $MELI Stock: CWA Asset Management Group LLC Decreases Position](https://www.marketbeat.com/instant-alerts/filing-mercadolibre-inc-meli-stock-cwa-asset-management-group-llc-decreases-position-2026-10-20/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  CWA Asset Management Group LLC cut its position in MercadoLibre, Inc. (NASDAQ:MELI - Free Report) by 10.1% during the third quarter, according to its most...
- [How One Hour Delivery At MercadoLibre (MELI) Has Changed Its Investment Story](https://simplywall.st/stocks/us/retail/nasdaq-meli/mercadolibre/news/how-one-hour-delivery-at-mercadolibre-meli-has-changed-its-i)  
  <sub>Simply Wall Street, 13 hours ago</sub>  
  MercadoLibre recently rolled out one-hour delivery in São Paulo and moved into selling prescription medicines, while reporting strong Q2 revenue alongside...
- [MercadoLibre Stock Is Down 13% Over the Past Year. Can 109.7% Upside Change That?](https://www.tikr.com/blog/mercadolibre-stock-is-down-13-over-the-past-year-can-109-7-upside-change-that)  
  <sub>TIKR.com, 24 hours ago</sub>  
  Here's why MercadoLibre is sacrificing margins for growth and why the model still sees the stock doubling.
- [MELI stock pre-market at EUR 1,639.10: commerce and fintech group](https://www.ad-hoc-news.de/boerse/news/vorboerse/meli-stock-pre-market-at-eur-1-639-10-commerce-and-fintech-group/70369361)  
  <sub>ad-hoc-news.de, 8 hours ago</sub>  
  MercadoLibre combines online commerce with payments and financial services. At Lang & Schwarz the stock trades pre-market at EUR 1639.10 on October 20,...
- [MELI271217C02540000 Interactive Stock Chart | MELI Dec 2027 2540.000 call Stock](https://ca.finance.yahoo.com/chart/MELI271217C02540000)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [James Hambro & Partners LLP Sells 1,310 Shares of MercadoLibre, Inc. $MELI](https://www.marketbeat.com/instant-alerts/filing-james-hambro-partners-llp-sells-1310-shares-of-mercadolibre-inc-meli-2026-10-19/)  
  <sub>MarketBeat, 21 hours ago</sub>  
  James Hambro & Partners LLP lessened its holdings in shares of MercadoLibre, Inc. (NASDAQ:MELI - Free Report) by 15.5% during the 3rd quarter, according to...
- [Jefferies keeps Buy rating for MercadoLibre stock at USD 2,600 target](https://www.ad-hoc-news.de/boerse/news/corporate-news/jefferies-keeps-buy-rating-for-mercadolibre-stock-at-usd-2-600-target/70370890)  
  <sub>ad-hoc-news.de, 6 hours ago</sub>  
  Second-quarter revenue reached USD 10.17 billion, up 49.80 percent year over year. MercadoLibre stock was at EUR 1638.20 on October 20, 2026.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 1,856.68 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 1,809.32 (+2.6%), 50d 1,861.01 (-0.2%), 200d 1,830.14 (+1.5%); 50d above 200d
Momentum: RSI(14) 52.7 | MACD 4.426 vs signal -2.061 (histogram 6.487)
Returns: 1d +0.9% | 5d -1.0% | 1m +2.0% | 3m +3.2%
52-week range: 1,546.81 - 2,360.76 (now 38.1% of the way up)
Volatility: ATR(14) 54.13 (2.9% of price) | annualised 20d 41.0%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 94.13B
Valuation: trailing P/E 50.49 | forward P/E 32.78 | P/B 12.02 | PEG 1.00
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
Price target: mean 2,270.01 (+22.3% vs last close), range 1,750.00 - 2,800.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

_Not available today._

</details>

### JPMorgan Chase (JPM) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Moderately bullish view driven by solid fundamentals, positive earnings record, and analyst consensus, tempered by neutral news and slightly bearish technicals.

**Main reasons it gave:**
- 3 earnings beats and 1 miss in the last 4 quarters
- Trailing P/E 14.22, forward P/E 13.27, ROE 18%, revenue growth 10.2% YoY
- Analyst consensus buy (mean rating 2.04) with price target +9.9% above current price
- Price near 52‑week high (68% of range) with volume at 0.22× 20‑day average, RSI 50.3

<details><summary><b>News</b> — score +0.00</summary>

- [JPMorgan Chase & Co. (JPM) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/JPM/)  
  <sub>Yahoo Finance UK, 10 hours ago</sub>  
  JPMorgan Chase & Co. (JPM) · -0.23% · -4.62% · 7.49% · 3.51% · 12.09% · 97.86% · 6,545.98%. Key events. Baseline. Advanced chart. Loading...
- [JPMorgan Chase & Co. $JPM Stock: Robertson Stephens Wealth Management LLC Raises Holdings](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-stock-robertson-stephens-wealth-management-llc-raises-holdings-2026-10-20/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Robertson Stephens Wealth Management LLC increased its position in JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 7.5% during the third quarter,...
- [JPMorgan Chase & Co. (JPM) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/JPM/)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  JPMorgan Chase & Co. (JPM) · -0.23% · -4.62% · 7.49% · 3.51% · 12.09% · 97.86% · 6,545.98%. Key Events. Baseline. Advanced Chart. Loading...
- [Chase hosts more than 1,000 scam workshops a year. Free sessions will run across the lower 48 states this November.](https://www.stocktitan.net/news/JPM/chase-launches-fraud-scam-prevention-fwb0b2112sdd.html)  
  <sub>Stock Titan, 21 hours ago</sub>  
  More than 1 million customers have been served through Chase's financial-wellness initiatives; November workshops will cover phishing and gift-card scams.
- [If You Invested $1000 In JPMorgan Chase Stock 10 Years Ago, You Would Have This Much Today](https://www.benzinga.com/news/26/10/62456725/if-you-invested-1000-jpmorgan-chase-stock-10-years-ago-you-would-have-much-today)  
  <sub>Benzinga, 15 hours ago</sub>  
  JPMorgan Chase (NYSE:JPM) has outperformed the market over the past 10 years by 3.5% on an annualized basis producing an average annual return of 17.1%.
- [JPMorgan Chase & Co. $JPM Stock: Birch Hill Investment Advisors LLC Lowers Holdings](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-stock-birch-hill-investment-advisors-llc-lowers-holdings-2026-10-20/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Birch Hill Investment Advisors LLC decreased its position in shares of JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 6.3% during the 3rd quarter,...
- [Bespoke | My Research](https://www.bespokepremium.com/think-big-blog/q3-2026-earnings-conference-call-recaps-jpmorgan-jpm/)  
  <sub>Bespoke Investment Group, 18 hours ago</sub>  
  Bespoke's Conference Call Recaps use AI to summarize lengthy earnings calls. The commentary below is AI-generated and then edited by Bespoke for quality...
- [Understanding the Setup: (JPM) and Scalable Risk](https://news.stocktradersdaily.com/news_release/149/Understanding_the_Setup:_JPM_and_Scalable_Risk_101926054801_1792446481.html)  
  <sub>Stock Traders Daily, 21 hours ago</sub>  
  Price-action only: Jpmorgan Chase & Co. (JPM) movements set the tone for institutional models. Understanding the Setup: (JPM) and Scalable Risk.
- [JPMorgan Chase & Co.'s (JPM) "Outperform" Rating Reaffirmed at Royal Bank Of Canada](https://www.marketbeat.com/instant-alerts/analyst-jpmorgan-chase-co-nyse-jpm-given-outperform-rating-at-royal-bank-of-canada-2026-10-14/)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Royal Bank Of Canada reaffirmed an "outperform" rating and set a $370.00 price target on shares of JPMorgan Chase & Co. in a research note on Wednesday.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 338.91 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 334.67 (+1.3%), 50d 347.22 (-2.4%), 200d 322.49 (+5.1%); 50d above 200d
Momentum: RSI(14) 50.3 | MACD -2.822 vs signal -4.064 (histogram 1.241)
Returns: 1d +1.6% | 5d +2.3% | 1m -3.7% | 3m -2.7%
52-week range: 282.84 - 365.18 (now 68.1% of the way up)
Volatility: ATR(14) 6.67 (2.0% of price) | annualised 20d 15.8%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 900.01B
Valuation: trailing P/E 14.22 | forward P/E 13.27 | P/B 2.56 | PEG 1.57
Profitability: profit margin 34.6% | operating margin 42.6% | ROE 18.0%
Growth (YoY): revenue +10.2% | earnings +9.9%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 1.01 | short interest 0.9% of float
Next earnings: 2027-01-14
```

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-09-30 missed by 7% | 2026-06-30 beat by 4% | 2026-03-31 beat by 8% | 2025-12-31 beat by 3%
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: buy (mean 2.04 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 5 strong buy, 10 buy, 11 hold, 0 sell, 0 strong sell
Price target: mean 372.57 (+9.9% vs last close), range 312.00 - 425.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Toyota (TM) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> The news includes a material, ticker‑specific catalyst (Toyota’s installation of mobile hydrogen fueling devices for heavy‑duty fuel‑cell trucks) and a sizable share‑buyback, both bullish. Technicals show modest momentum (RSI 63.5, MACD positive) but thin volume, tempering the signal. Fundamentals are mixed: cheap trailing P/E (8.65) and strong earnings growth (+86.9% YoY) support a bullish view, while high debt/equity (115%) and negative free cash flow add risk. Analyst consensus remains positive (median price target +18.8% vs. current price) despite recent downgrades. No insider activity is present, yielding a neutral insider score. Overall, the positive catalyst and valuation outweigh the negatives, leading to a moderate bullish call.

**Main reasons it gave:**
- Toyota installed two mobile hydrogen fueling devices for heavy‑duty fuel‑cell trucks
- Toyota announced a 35.55 million share buyback
- Trailing P/E of 8.65 indicates cheap valuation relative to earnings
- Analyst median price target +18.8% above current price

<details><summary><b>News</b> — score +0.40</summary>

- [Should Value Investors Buy Toyota Motor (TM) Stock?](https://ca.finance.yahoo.com/news/value-investors-buy-toyota-motor-124002446.html)  
  <sub>Yahoo! Finance Canada, 2 hours ago</sub>  
  Here at Zacks, our focus is on the proven Zacks Rank system, which emphasizes earnings estimates and estimate revisions to find great stocks.
- [Toyota-powered trucks refueled in about eight minutes for up to 450 miles. Their power systems emit only water.](https://www.stocktitan.net/news/TM/toyota-achieves-heavy-duty-hydrogen-truck-4eer1n8vei85.html)  
  <sub>Stock Titan, 2 hours ago</sub>  
  Toyota (TM) installed two mobile hydrogen fueling devices at its North American Parts Center California to support heavy-duty fuel cell trucks.
- [How to Take Advantage of moves in (RMAX) (RMAX:CA)](https://news.stocktradersdaily.com/canada/how-to-take-advantage-of-moves-in-rmax-_20261020_4122eb)  
  <sub>Stock Traders Daily, 2 hours ago</sub>  
  When Investors Make Decisions in Hamilton REITs YIELD MAXIMIZER TM ETF RMAX Opportunities Surface.
- [Google Research and Synaptics add a second board for AI developers](https://www.stocktitan.net/news/SYNA/synaptics-and-google-research-expand-the-coralboard-tm-l1qi7tislcwq.html)  
  <sub>Stock Titan, 2 hours ago</sub>  
  The SL board pairs a 1 TOPS NPU with 2GB DDR4. Synaptics' Torq compiler, now available for Coralboard, supports widely used machine-learning frameworks.
- [Toyota Motor stock: Erste Group cuts FY2027 estimate for Toyota Motor stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/toyota-motor-stock-erste-group-cuts-fy2027-estimate-for-toyota-motor-stock/70374202)  
  <sub>ad-hoc-news.de, 1 hour ago</sub>  
  Toyota booked USD 84.87 billion in first-quarter revenue. Toyota Motor stock costs EUR 174.50 on October 20, 2026, plus 0.29 percent versus the Xetra close.
- [Subaru plans to introduce software-defined vehicles in the next few years (FUJHY:OTCMKTS)](https://seekingalpha.com/news/4654361-subaru-plans-to-introduce-software-defined-vehicles-in-the-next-few-years)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  Subaru plans software-defined vehicles in late 2020s, using an AMD co-developed ECU across gas, hybrid and EVs for affordable long-life updates—read more.
- [Toyota (TSE:7203) Stock Could Be 39% Overvalued After EU Rules Push](https://finance.yahoo.com/markets/stocks/articles/toyota-tse-7203-stock-could-181326404.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Toyota Motor has delivered a 5 year share return that raises a straightforward question for anyone looking at the ticker today. Are the cash flows that the...
- [Johnson & Johnson's heart catheter halves treatment time and limits blood-flow blockage](https://www.stocktitan.net/news/JNJ/johnson-johnson-launches-next-generation-shockwave-tm-c2-aero-fly-sdtpq1o7m421.html)  
  <sub>Stock Titan, 3 hours ago</sub>  
  Next-generation intravascular lithotripsy (IVL) catheter delivers pulses at 2 Hz, improving efficiency in calcium modification treatment of coronary artery...
- [(HBIL) Market Insights and Trading Signals (HBIL:CA)](https://news.stocktradersdaily.com/canada/hbil-market-insights-and-trading-signals_20261019_6a2811)  
  <sub>Stock Traders Daily, 15 hours ago</sub>  
  Market Insights Report for Hamilton U.S. T-Bill YIELD MAXIMIZER TM ETF (HBIL) with Key Trading Signals.
- [Toyota reports 35.55 million share buyback. Toyota Motor stock is valued at USD 231.2 billion](https://www.ad-hoc-news.de/boerse/news/corporate-news/toyota-reports-35-55-million-share-buyback-toyota-motor-stock-is-valued-at-usd-231-2-billion/70369853)  
  <sub>ad-hoc-news.de, 8 hours ago</sub>  
  Toyota's first-quarter revenue was USD 84.87 billion. Toyota Motor stock costs EUR 174.50 on October 20, 2026 at USD 231.2 billion value.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.15</summary>

```text
Last close 196.97 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 187.69 (+4.9%), 50d 191.02 (+3.1%), 200d 199.71 (-1.4%); 50d below 200d
Momentum: RSI(14) 63.5 | MACD 0.873 vs signal -0.559 (histogram 1.432)
Returns: 1d +1.5% | 5d +4.4% | 1m +2.3% | 3m +9.5%
52-week range: 166.50 - 248.29 (now 37.3% of the way up)
Volatility: ATR(14) 3.04 (1.5% of price) | annualised 20d 21.4%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.05</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 231.99B
Valuation: trailing P/E 8.65 | forward P/E 12.48 | P/B 15.79 | PEG n/a
Profitability: profit margin 8.6% | operating margin 7.9% | ROE 12.4%
Growth (YoY): revenue +10.4% | earnings +86.9%
Balance sheet: debt/equity 115.0% | free cash flow -3.60T
Risk: beta 0.38 | short interest 0.1% of float
Next earnings: 2026-11-05
```

</details>

<details><summary><b>What this fund holds</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.05</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 44% | 2026-03-31 beat by 12% | 2025-12-31 beat by 27% | 2025-09-30 beat by 24%
```

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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: none (mean n/a on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 2 strong buy, 2 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 234.08 (+18.8% vs last close), range 230.00 - 239.31
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

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

### Microsoft (MSFT) · Company — BULLISH, confidence 0.50

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Profit margin 40.3%, operating margin 45.1%, ROE 34% (FUNDAMENTALS)
- Four consecutive earnings beats (10%, 3%, 6%, 5%) (EARNINGS RECORD)
- Net insider buying of 263,995 shares (+4.7% of holdings) (INSIDER ACTIVITY)
- Mixed news: AI chip production boost vs UK AI data center pull-out (NEWS)
- Technical concerns: price near 52‑week high with low volume (0.16× 20‑day avg) and MACD below signal (TECHNICALS)

<details><summary><b>News</b> — score +0.10</summary>

- [Microsoft, Alphabet and Goldman Sachs join objections to OKX-ICE tokenized stock trading](https://www.coindesk.com/business/2026/10/19/microsoft-alphabet-and-goldman-sachs-join-objections-to-okx-ice-tokenized-stock-trading)  
  <sub>CoinDesk, 2 hours ago</sub>  
  Microsoft (MSFT), Alphabet (GOOG, GOOGL) and Goldman Sachs (GS) have objected to having tokenized versions of their shares traded on OKXICE, adding to...
- [Microsoft (MSFT) Pulls Out Of UK AI Data Center Project After Power Delays](https://simplywall.st/stocks/us/software/nasdaq-msft/microsoft/news/microsoft-msft-pulls-out-of-uk-ai-data-center-project-after)  
  <sub>Simply Wall Street, 6 hours ago</sub>  
  Microsoft (NasdaqGS:MSFT) has exited plans to anchor the Nscale AI data center project in the UK due to power connection delays. The withdrawal affects a...
- [Microsoft Pays Cash For AI. CoreWeave Borrows.](https://www.trefis.com/stock/msft/articles/619450/microsoft-pays-cash-for-ai-coreweave-borrows/2026-10-20)  
  <sub>Trefis, 5 hours ago</sub>  
  The AI build-out is running partly on borrowed money, and borrowed money isn't cheap: the 10-year Treasury yields 5.1%, with inflation back at 3.7%.
- [MSFT 261019 557.50C (MSFT261019C557500) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/MSFT261019C557500-US)  
  <sub>Moomoo, 13 hours ago</sub>  
  Track real-time MSFT 261019 557.50C (MSFT261019C557500) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [MSFT Stock Hits Highest Level This Year: Microsoft To Reportedly Hike Production Of AI Chips](https://stocktwits.com/news-articles/markets/equity/microsoft-to-reportedly-hike-production-of-ai-chips/cZojwJgRJO6)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Microsoft (MSFT) share price jumped 2% on Monday to its highest level in over nine months as it prepares a push in its AI silicon strategy by boosting...
- [MSFT Oct 2026 500.000 put (MSFT261014P00500000) interactive stock chart](https://uk.finance.yahoo.com/quote/MSFT261014P00500000/chart/)  
  <sub>Yahoo Finance UK, 7 hours ago</sub>  
  Interactive chart for MSFT Oct 2026 500.000 put (MSFT261014P00500000) – analyse all of the data with a huge range of indicators.
- [Microsoft (MSFT) Stock Rebounds as Azure Growth and AI Monetizat](https://www.gurufocus.com/news/9130264/microsoft-msft-stock-rebounds-as-azure-growth-and-ai-monetization-drive-optimism)  
  <sub>GuruFocus, 17 hours ago</sub>  
  On October 19, 2026, Microsoft Corp (MSFT) experienced renewed investor interest following Morgan Stanley's commentary emphasizing the need for the company...
- [Microsoft faces higher bar for continued momentum, Morgan Stanley says (MSFT:NASDAQ)](https://seekingalpha.com/news/4654357-microsoft-faces-higher-bar-for-continued-momentum-morgan-stanley-says)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  Microsoft stock rebound faces a higher bar, says Morgan Stanley: Azure mid-40% growth, better 365/Copilot monetization & disciplined costs.
- [Not Anthropic. Not OpenAI. This Is the Artificial Intelligence (AI) Stock I'd Buy Before the Next Mega-IPO.](https://www.theglobeandmail.com/investing/markets/stocks/MSFT/pressreleases/8229197/not-anthropic-not-openai-this-is-the-artificial-intelligence-ai-stock-id-buy-before-the-next-mega-ipo/)  
  <sub>The Globe and Mail, 2 hours ago</sub>  
  Detailed price information for Microsoft Corp (MSFT-Q) from The Globe and Mail including charting and trades.
- [Responsive Playbooks and the MSFT Inflection](https://news.stocktradersdaily.com/news_release/35/Responsive_Playbooks_and_the_MSFT_Inflection_101926062601_1792448761.html)  
  <sub>Stock Traders Daily, 20 hours ago</sub>  
  Key findings for Microsoft Corporation (NASDAQ: MSFT). Conflicting Sentiment Across Horizons Suggests Choppy Conditions; No clear price positioning signal...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 531.89 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 523.51 (+1.6%), 50d 506.72 (+5.0%), 200d 435.80 (+22.1%); 50d above 200d
Momentum: RSI(14) 58.4 | MACD 10.109 vs signal 10.734 (histogram -0.626)
Returns: 1d -0.3% | 5d -2.1% | 1m +6.0% | 3m +36.3%
52-week range: 352.83 - 543.45 (now 93.9% of the way up)
Volatility: ATR(14) 11.45 (2.2% of price) | annualised 20d 21.7%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.95T
Valuation: trailing P/E 29.63 | forward P/E 22.44 | P/B 8.93 | PEG 1.62
Profitability: profit margin 40.3% | operating margin 45.1% | ROE 34.0%
Growth (YoY): revenue +17.7% | earnings +31.7%
Balance sheet: debt/equity 29.1% | free cash flow 16.55B
Risk: beta 1.10 | short interest 0.8% of float
Next earnings: 2026-10-28
```

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.50</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 10% | 2026-03-31 beat by 3% | 2025-06-30 beat by 6% | 2025-03-31 beat by 5%
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
Consensus: strong_buy (mean 1.34 on a 1=strong buy to 5=strong sell scale, 53 analysts)
Ratings: 13 strong buy, 41 buy, 3 hold, 0 sell, 0 strong sell
Price target: mean 599.28 (+12.7% vs last close), range 440.00 - 870.00
Recent rating changes:
  - 2026-10-19 Bernstein: main, Outperform -> Outperform
  - 2026-10-16 StoneX: main, Buy -> Buy
  - 2026-10-15 UBS: main, Buy -> Buy
  - 2026-10-15 Citigroup: main, Buy -> Buy
  - 2026-10-15 Mizuho: main, Outperform -> Outperform
  - 2026-10-15 Jefferies: main, Buy -> Buy
Institutional ownership: 75.8%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.5%), State Street Corporation (4.2%), Geode Capital Management, LLC (2.5%), FMR, LLC (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

_Not available today._

</details>

### Procter & Gamble (PG) · Company — NEUTRAL, confidence 0.45

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: positive news (product launch, modest institutional buy) and analyst view offset by bearish technicals (overbought RSI, thin volume) and high valuation with low earnings growth. Net effect is slight positive but not strong enough for a directional bias.

**Main reasons it gave:**
- New Head & Shoulders Scalp Care collection launch (product catalyst)
- Sumitomo Mitsui DS Asset Management increased stake by 1.4% (institutional buy)
- RSI 70.2 and volume 0.15x 20‑day average (overbought, thin volume)
- High valuation (forward P/E 21.4, PEG 3.79) with earnings growth -15.5% YoY (mixed fundamentals)

<details><summary><b>News</b> — score +0.35</summary>

- [Procter & Gamble's (PG) "Outperform" Rating Reiterated at Royal Bank Of Canada](https://www.marketbeat.com/instant-alerts/analyst-procter-gambles-pg-outperform-rating-reiterated-at-royal-bank-of-canada-2026-10-20/)  
  <sub>MarketBeat, 1 hour ago</sub>  
  Royal Bank Of Canada reiterated an "outperform" rating and issued a $166.00 price target on shares of Procter & Gamble in a research note on Tuesday.
- [Meet the Dividend King Stock That Yields More Than Quintuple the Nasdaq-100. Here's Why It's a Buy in October.](https://finance.yahoo.com/markets/stocks/articles/meet-dividend-king-stock-yields-235000504.html)  
  <sub>Yahoo Finance, 15 hours ago</sub>  
  Procter & Gamble has built an impressive track record of dividends.
- [The Zacks Analyst Blog Highlights Meta Platforms, Lam Research, Texas Instruments, Tesla, Netflix, Procter & Gamble and GE Aerospace](https://www.theglobeandmail.com/investing/markets/stocks/PG/pressreleases/8233138/the-zacks-analyst-blog-highlights-meta-platforms-lam-research-texas-instruments-tesla-netflix-procter-gamble-and-ge-aerospace/)  
  <sub>The Globe and Mail, 55 minutes ago</sub>  
  Detailed price information for Procter & Gamble (PG-N) from The Globe and Mail including charting and trades.
- [Price to book forward of The Hartford Insurance Group, Inc. Depositary Shares each representing a 1/1000th interest in a share of 6.000% Non-Cumulative Preferred Stock, Series G – NYSE:HIG/PG](https://www.tradingview.com/symbols/NYSE-HIG/PG/financials-statistics-and-ratios/price-book-fwd/)  
  <sub>TradingView, 15 hours ago</sub>  
  Price to book forward, quarterly and annual stats of The Hartford Insurance Group, Inc. Depositary Shares each representing a 1/1000th interest in a share...
- [Sumitomo Mitsui DS Asset Management Company Ltd Buys 8,378 Shares of Procter & Gamble Company (The) $PG](https://www.marketbeat.com/instant-alerts/filing-sumitomo-mitsui-ds-asset-management-company-ltd-buys-8378-shares-of-procter-gamble-company-the-pg-2026-10-20/)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Sumitomo Mitsui DS Asset Management Company Ltd increased its stake in shares of Procter & Gamble Company (The) (NYSE:PG - Free Report) by 1.4% during the...
- [PG Oct 2026 155.000 put (PG261023P00155000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/PG261023P00155000/)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Find the latest PG Oct 2026 155.000 put (PG261023P00155000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Procter & Gamble Company (The) $PG Stock: Talbot Financial LLC Cuts Holdings](https://www.marketbeat.com/instant-alerts/filing-procter-gamble-company-the-pg-stock-talbot-financial-llc-cuts-holdings-2026-10-19/)  
  <sub>MarketBeat, 21 hours ago</sub>  
  Talbot Financial LLC reduced its stake in Procter & Gamble Company (The) (NYSE:PG - Free Report) by 12.9% in the 3rd quarter, according to its most recent...
- [PG Oct 2026 100.000 call (PG261030C00100000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/PG261030C00100000/)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Find the latest PG Oct 2026 100.000 call (PG261030C00100000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Why Is Procter & Gamble (PG) Refreshing Its Scalp Care Playbook Now?](https://finance.yahoo.com/markets/stocks/articles/why-procter-gamble-pg-refreshing-151504571.html)  
  <sub>Yahoo Finance, 24 hours ago</sub>  
  Procter & Gamble (NYSE:PG) has introduced a Head & Shoulders Scalp Care Collection focused on distinct scalp health needs. The new regimens use clinically...
- [PG Oct 2026 85.000 put (PG261023P00085000) Interactive Stock Chart](https://www.google.com/goto?url=CAESdgHrOzAV_YK7ccjb3MPKOEDH60RRAx35Mtr0-5WTsnaFq46TZbVltX3Vk1N5rJKKT46p6DJJqlh3j4tHiLhSFbvBupdYGxDT5f7Bp8KkHqIf8MUjYNW8YLSorgcsfy0tsOa84kJ4mRD4-ePYxYgy5FKRITCuZFc)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Interactive Chart for PG Oct 2026 85.000 put (PG261023P00085000), analyze all the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 158.38 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 150.50 (+5.2%), 50d 147.35 (+7.5%), 200d 148.18 (+6.9%); 50d below 200d
Momentum: RSI(14) 70.2 | MACD 3.147 vs signal 2.105 (histogram 1.043)
Returns: 1d +0.4% | 5d +3.5% | 1m +8.4% | 3m +6.2%
52-week range: 138.04 - 167.20 (now 69.8% of the way up)
Volatility: ATR(14) 2.52 (1.6% of price) | annualised 20d 18.7%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.25</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 368.16B
Valuation: trailing P/E 23.93 | forward P/E 21.43 | P/B 6.90 | PEG 3.79
Profitability: profit margin 18.4% | operating margin 22.1% | ROE 30.3%
Growth (YoY): revenue +1.5% | earnings -15.5%
Balance sheet: debt/equity 64.5% | free cash flow 13.28B
Risk: beta 0.38 | short interest 1.1% of float
Next earnings: 2026-10-22
```

</details>

<details><summary><b>What this fund holds</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.25</summary>

```text
Earnings record, last 4 quarters: 4 in line
  2026-06-30 in line | 2026-03-31 in line | 2025-06-30 in line | 2025-03-31 in line
```

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: buy (mean 2.16 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 5 strong buy, 8 buy, 12 hold, 0 sell, 0 strong sell
Price target: mean 162.13 (+2.4% vs last close), range 143.00 - 186.00
Recent rating changes:
  - 2026-10-20 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-14 Citigroup: main, Buy -> Buy
  - 2026-10-06 Evercore ISI Group: up, In-Line -> Outperform
  - 2026-10-06 RBC Capital: main, Outperform -> Outperform
  - 2026-09-30 TD Cowen: reit, Hold -> Hold
  - 2026-08-07 Argus Research: down, Buy -> Hold
Institutional ownership: 71.8%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.4%), Geode Capital Management, LLC (2.9%), Vanguard Portfolio Management LLC (2.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

```text
Last 180 days: bought 156,293 shares in 42 transaction(s) | sold 48,751 shares in 16
Net: +107,542 shares (+5.3% of insider holdings) | insiders hold 2,138,478 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-10-05 GAMA PAUL (Officer): 2,225 shares, 323.38K
  - 2026-10-05 WHALEY SUSAN STREET (Officer): 2,369 shares, 344.31K
  - 2026-10-05 SCHULTEN ANDRE (Chief Financial Officer): 3,914 shares, 568.86K
  - 2026-08-24 JANZARUK MATTHEW W. (Officer): 359 shares, 52.14K
(40 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

_Not available today._

</details>

### Caterpillar (CAT) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technicals show bearish price action (price below 20‑, 50‑ and 200‑day SMAs, low volume, negative MACD) while there is no material news catalyst. Fundamentals and analyst sentiment are positive, and the company has a strong earnings‑beat record, but those factors are longer‑term and the earnings date is still a week away. The mixed signals lead to a neutral short‑term view with modest conviction.

**Main reasons it gave:**
- Price below 20‑, 50‑ and 200‑day SMA and volume at 0.25× 20‑day average (bearish technicals)
- No material news catalyst in the past 24 hours
- Four consecutive earnings beats (8‑31% beats) indicate strong earnings momentum
- Analyst consensus buy with mean price target +29% above current price

<details><summary><b>News</b> — score +0.00</summary>

- [Caterpillar Inc. (CAT) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/CAT/)  
  <sub>Yahoo Finance UK, 9 hours ago</sub>  
  45,144.04% · Previous close 730.76 · Open 739.50 · Bid -- · Ask 727.48 x 4000 · Day's range 718.44 - 740.00 · 52-week range 510.21 - 1,073.46 · Volume 2,462,224...
- [Why is Red Cat stock sliding today?](https://www.google.com/goto?url=CAESmwEB6zswFWsun26SHxA2Px776DAyxgu4k0vNS8ff4-sWgMyiTHlhF77W0bbaA47OCNzqE0Dcr8OOZ5fWSerwlOBItxQ7mXrbxrsAwDs5o1noMSgaCDSlSjwrib_wUHinA8Gg3onR1t_92oP3-hSecx_yFYe4S5k5nkhqZZpUIXz0Evf9jBH7KW1zkugwC1hBZQJK9O2L7MV60sKzwA)  
  <sub>Investing.com, 1 hour ago</sub>  
  Investing.com -- Red Cat Holdings stock slipped 1.9% in pre-open trading today as the initial enthusiasm surrounding its proposed acquisition of Austrian...
- [Caterpillar vs. Deere: The Better Heavy Equipment Stock for the Data Center Boom](https://www.barchart.com/story/news/8227235/caterpillar-vs-deere-the-better-heavy-equipment-stock-for-the-data-center-boom)  
  <sub>Barchart.com, 3 hours ago</sub>  
  Caterpillar and Deere offer two ways to invest in heavy machinery. But which stock stands out on earnings, valuation, dividends, and growth potential?
- [Is Caterpillar (CAT) Stock Outpacing Its Industrial Products Peers This Year?](https://finance.yahoo.com/markets/stocks/articles/caterpillar-cat-stock-outpacing-industrial-124003351.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Investors interested in Industrial Products stocks should always be looking to find the best-performing companies in the group. Has Caterpillar (CAT) been...
- [CAT Stock Analysis: Explained](https://journalarta.com/en/2026/10/20/cat-stock-analysis-drops-0-68-rsi-oversold/)  
  <sub>JournalArta, 6 hours ago</sub>  
  On October 19, 2026: price 725.79 USD, trend downtrend, RSI 29.9, support 725.79, resistance 863.44. technical analysis of cat stock. CAT Stock Analysis...
- [CAT 261023 1025.00C (CAT261023C1025000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/CAT261023C1025000-US)  
  <sub>Moomoo, 16 hours ago</sub>  
  Track real-time CAT 261023 1025.00C (CAT261023C1025000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [Needham reiterates Red Cat stock rating on Steyr Motors deal](https://www.investing.com/news/analyst-ratings/needham-reiterates-red-cat-stock-rating-on-steyr-motors-deal-93CH-4959677)  
  <sub>Investing.com, 3 hours ago</sub>  
  Investing.com - Needham reiterated a Buy rating and $15.00 price target on Red Cat Holdings Inc. (NASDAQ:RCAT) following the company's acquisition...
- [Red Cat Holdings Stock Price: RCAT Stock Chart, Market Cap & News Today](https://www.coingecko.com/en/stocks/red-cat-holdings)  
  <sub>CoinGecko, 6 hours ago</sub>  
  Red Cat Holdings (RCAT) is down 7.0% today, trading at $4.63 with a daily range of $4.63 to $5.15. Over the past year, Red Cat Holdings hit a 52-week high of...
- [(CAT) Movement as an Input in Quant Signal Sets](https://news.stocktradersdaily.com/news_release/11/CAT_Movement_as_an_Input_in_Quant_Signal_Sets_101926045002_1792443002.html)  
  <sub>Stock Traders Daily, 22 hours ago</sub>  
  Key findings for Caterpillar Inc. (NYSE: CAT). Weak Near and Mid-Term Sentiment Could Challenge Long-Term Positive Outlook; No clear price positioning...
- [Caterpillar, Cummins, Quanta Services poised to gain from 2027 data-center growth: UBS (CAT:NYSE)](https://seekingalpha.com/news/4654330-caterpillar-cummins-quanta-services-poised-to-gain-from-2027-data-center-growth-ubs)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  UBS sees AI data center demand accelerating in 2027, boosting CAT, CMI & PWR despite supply constraints.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 731.31 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 796.73 (-8.2%), 50d 808.30 (-9.5%), 200d 807.17 (-9.4%); 50d above 200d
Momentum: RSI(14) 32.0 | MACD -22.547 vs signal -12.701 (histogram -9.847)
Returns: 1d +0.8% | 5d -5.4% | 1m -10.4% | 3m -17.8%
52-week range: 513.91 - 1,064.90 (now 39.5% of the way up)
Volatility: ATR(14) 26.86 (3.7% of price) | annualised 20d 32.7%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 336.16B
Valuation: trailing P/E 31.48 | forward P/E 22.44 | P/B 17.33 | PEG 1.42
Profitability: profit margin 14.5% | operating margin 22.2% | ROE 57.0%
Growth (YoY): revenue +24.0% | earnings +68.2%
Balance sheet: debt/equity 232.8% | free cash flow 5.05B
Risk: beta 1.58 | short interest 1.9% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 31% | 2026-03-31 beat by 19% | 2025-12-31 beat by 9% | 2025-09-30 beat by 8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: buy (mean 2.04 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 1 strong buy, 15 buy, 12 hold, 1 sell, 0 strong sell
Price target: mean 945.76 (+29.3% vs last close), range 575.00 - 1,155.00
Recent rating changes:
  - 2026-10-14 Oppenheimer: main, Outperform -> Outperform
  - 2026-10-12 Citigroup: main, Buy -> Buy
  - 2026-10-05 Truist Securities: main, Buy -> Buy
  - 2026-09-10 Freedom Broker: up, Hold -> Buy
  - 2026-08-11 Evercore ISI Group: main, Outperform -> Outperform
  - 2026-08-06 DA Davidson: main, Neutral -> Neutral
Institutional ownership: 73.5%
Largest holders: Blackrock Inc. (8.3%), State Street Corporation (7.5%), Vanguard Capital Management LLC (6.5%), State Farm Mutual Automobile Insurance Co (3.2%), Vanguard Portfolio Management LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

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

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

_Not available today._

</details>

### Novo Nordisk (NVO) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals across dimensions with no material catalyst; slight bearish tilt but overall uncertainty leads to a neutral stance.

**Main reasons it gave:**
- Share buyback expanded to 1.2% treasury stake (Globe and Mail)
- Price below 50‑day and 200‑day SMA, volume 0.21× 20‑day avg (Technical data)
- Earnings record: 2 misses, 1 beat, 1 in‑line (Earnings record)
- Low trailing P/E 9.24, high ROE 59.8% (Fundamentals)

<details><summary><b>News</b> — score -0.10</summary>

- [Novo Nordisk (NVO) Stock Sinks As Market Gains: Here's Why](https://finance.yahoo.com/markets/stocks/articles/novo-nordisk-nvo-stock-sinks-204502570.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>
- [Novo Nordisk Expands 2026 Share Buyback, Lifting Treasury Stake to 1.2%](https://www.theglobeandmail.com/investing/markets/stocks/NVO/pressreleases/8230821/novo-nordisk-expands-2026-share-buyback-lifting-treasury-stake-to-12/)  
  <sub>The Globe and Mail, 2 hours ago</sub>  
  Detailed price information for Novo Nordisk A/S ADR (NVO-N) from The Globe and Mail including charting and trades.
- [How to Buy Novo Nordisk Stock (NVO) in 2026](https://www.fool.com/investing/how-to-invest/stocks/how-to-invest-in-novo-nordisk-stock/)  
  <sub>The Motley Fool, 19 hours ago</sub>  
  How to buy Novo Nordisk stock · Open your brokerage account: Log in to your brokerage account where you handle your investments. · Search for the stock: Enter...
- [Forget Eli Lilly and Novo: This Biotech Could Be a Surprising Winner in the Weight Loss Market](https://www.theglobeandmail.com/investing/markets/stocks/NVO/pressreleases/8199394/forget-eli-lilly-and-novo-this-biotech-could-be-a-surprising-winner-in-the-weight-loss-market/)  
  <sub>The Globe and Mail, 24 hours ago</sub>  
  Detailed price information for Novo Nordisk A/S ADR (NVO-N) from The Globe and Mail including charting and trades.
- [PSKY Beats Q2 Estimates, Raises 2026 Outlook As CEO Stands Firm On $110B WBD Deal — But Stock Slips After-Hours](https://www.google.com/goto?url=CAES7gEB6zswFbfnThfS0aazK0DvUxOJXzk37kV1VYgJ66fBWfiNlVaRurmb2YBqmSUYbcLHCRS9myc2vmY9FZuB9g-3hae8SRKiNFDJEL-pkdL6thkC4rlsjaV5EXrPZrCOPtRUEnnigCbHNv23-EBSD34agfOD-mSPiOHhoiDvUEqkSV5pur5pg2hWjL3C03hi2BtotwziT9xb5DSLctZ-FIXJWQe3oCd8nAtkjwGnntc4p27Ib9DIS0xHxM-EY--eQo54OyJ3h_mUb6dgkrMY-JtLmiqWXdWqAC_rxzRre_SGnT268BrAWfVklLzEeGOn)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Paramount Skydance Corp. (PSKY) reported its financial results for the second quarter ended June 30 on Tuesday, beating analyst expectations on both...
- [Can Viking Therapeutics Carve Out a Place in the Obesity Market?](https://finance.yahoo.com/healthcare/articles/viking-therapeutics-carve-place-obesity-121500319.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>
- [Biotech Stocks To Watch And Pharma Industry News](https://www.investors.com/news/technology/biotech-and-pharma-industry-and-stock-news-merk-bristol-myers-amgn-gilead/)  
  <sub>Investor's Business Daily, 21 hours ago</sub>  
  Bookmark this page for the latest news and stock analysis for Eli Lilly (LLY), Novo Nordisk (NVO), Merck (MRK), Johnson & Johnson (JNJ), Pfizer (PFE) and...
- [Novo Nordisk A/S (NYSE: NVO) Holds Zacks Rank #3 As Earnings Estimates Slide And Valuation Looks Attractive](https://www.foreignpolicyjournal.com/2026/10/19/novo-nordisk-a-s-nyse-nvo-holds-zacks-rank-3-as-earnings-estimates-slide-and-valuation-looks-attractive/)  
  <sub>Foreign Policy Journal, 15 hours ago</sub>  
  Novo Nordisk A/S (NYSE: NVO) has become one of the most closely watched stocks among visitors to Zacks.com, drawing significant investor attention amid a.
- [Novo Nordisk shares technical analysis: Tracking seller momentum near $37.68 support](https://tradersunion.com/news/stocks/show/3886496-novo-nordisk-drops-1-03percent-to/)  
  <sub>Traders Union, 7 hours ago</sub>  
  Novo Nordisk trades at $38.42 today, down 1.03%, as shares stay below key averages and bearish momentum continues.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 39.28 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 38.29 (+2.6%), 50d 42.36 (-7.3%), 200d 44.94 (-12.6%); 50d below 200d
Momentum: RSI(14) 46.7 | MACD -0.968 vs signal -1.367 (histogram 0.399)
Returns: 1d +2.2% | 5d +3.2% | 1m -1.3% | 3m -18.5%
52-week range: 35.29 - 63.98 (now 13.9% of the way up)
Volatility: ATR(14) 0.91 (2.3% of price) | annualised 20d 22.5%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 173.32B
Valuation: trailing P/E 9.24 | forward P/E 11.46 | P/B 5.25 | PEG 4.32
Profitability: profit margin 35.3% | operating margin 42.5% | ROE 59.8%
Growth (YoY): revenue +2.1% | earnings -20.6%
Balance sheet: debt/equity 63.3% | free cash flow 37.67B
Risk: beta 0.38 | short interest 1.0% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

```text
Earnings record, last 4 quarters: 1 beat, 1 in line, 2 missed
  2026-06-30 missed by 6% | 2026-03-31 beat by 23% | 2025-12-31 in line | 2025-09-30 missed by 7%
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

<details><summary><b>What analysts and big funds say</b> — score -0.20</summary>

```text
Consensus: hold (mean 2.71 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 0 strong buy, 3 buy, 10 hold, 1 sell, 0 strong sell
Price target: mean 45.32 (+15.4% vs last close), range 39.95 - 62.10
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

<details><summary><b>What analysts say about what this fund holds</b> — score -0.20</summary>

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

### ASML (ASML) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [ASML (ASML) Stock Looks About Right With AI Demand In Focus](https://simplywall.st/stocks/us/semiconductors/nasdaq-asml/asml-holding/news/asml-asml-stock-looks-about-right-with-ai-demand-in-focus)  
  <sub>Simply Wall Street, 2 hours ago</sub>  
  ASML Holding has delivered very strong multi year returns, and the question now is whether the current share price can still be explained by its earnings...
- [ASML Stock Gains Over 5% — Why Bernstein Thinks ASML Holding Can Keep Climbing After Nearly 140% Run In The Past Year](https://stocktwits.com/news-articles/markets/equity/asml-stock-why-bernstein-sees-more-upside-after-140-percent-rally/cZm11SiR7lF)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Shares of ASML Holding NV (ASML) surged nearly 5.5% on Monday after Bernstein significantly raised its price target on the semiconductor equipment maker.
- [Apple vs. ASML: Which Tech Stock Is a Better Buy in 2026?](https://www.fool.com/coverage/better-buy/2026/10/20/apple-vs-asml-which-tech-stock-is-a-better-buy-in-2026/)  
  <sub>The Motley Fool, 3 hours ago</sub>  
  Apple's 26.9% net margin and $98.8 billion in free cash flow contrast sharply with ASML's 29.4% margin and leaner balance sheet, revealing two distinct...
- [Applied Materials vs. ASML: Which Can Carry a Bigger Research Bill?](https://finance.yahoo.com/technology/articles/applied-materials-vs-asml-carry-185657266.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Keeping a semiconductor-equipment franchise valuable for ten years requires repeated invention. Our 10 Best Semiconductor Stocks to Buy for the Next Decade...
- [AI chip demand powers another strong quarter, demand elevated until 2030 | 2026-10-20 | Investing News](https://stockhouse.com/news/the-market-online-news/2026/10/20/ai-chip-demand-powers-another-strong-quarter-demand-elevated-until-2030)  
  <sub>Stockhouse, 8 hours ago</sub>  
  ASML (NASDAQ:ASML) reported Q3 2026 net sales of €11.7 billion and net income of €5.0 billion, driven by demand for chipmaking equipment.
- [Intel Stock Surges After an Upgrade. ‘Our Confidence Is Building,’ Says JPMorgan](https://www.investopedia.com/market-update-intel-stock-surges-after-an-upgrade-our-confidence-is-building-says-jpmorgan-intc-12181991)  
  <sub>Investopedia, 23 hours ago</sub>  
  Intel shares surged Monday after an upgrade to “neutral” from “underweight,” by longtime bear JPMorgan. JPMorgan analysts said their “confidence is building...
- [ASML's Order Book Stretches to 2030, but Its Factory Floors Set the Pace](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/asml-s-order-book-stretches-to-2030-but-its-factory-floors-set-the-pace/70371412)  
  <sub>ad-hoc-news.de, 5 hours ago</sub>  
  ASML shares fell Thursday despite Q3 net sales of EUR 11.7 billion and raised 2026 guidance, as delivery capacity lags customer demand into 2027-2028.
- [ASML Holding N.V. - New York Registry Shares Price Today | xASML Live Price, Chart & Market Cap](https://www.okx.com/en-eu/price/asml-holding-n-v----new-york-registry-shares-xasml)  
  <sub>OKX, 23 hours ago</sub>  
  OKX Europe - Oct 19, 2026 - The live price of ASML Holding N.V. - New York Registry Shares is €1498.56. xASML price has decreased by - in 24hrs,...
- [Silicon Motion Technology Corporation (SIMO) latest stock news and headlines](https://au.finance.yahoo.com/quote/SIMO/news/)  
  <sub>Yahoo Finance Australia, 15 hours ago</sub>  
  Get the latest Silicon Motion Technology Corporation (SIMO) stock news and headlines to help you in your trading and investment decisions.
- [Is the AI Trade Cracking? What CoreWeave, Paul Tudor Jones, and ASML Are Telling Us](https://www.fool.com/investing/2026/10/19/is-the-ai-trade-cracking-what-coreweave-paul-tudor/)  
  <sub>The Motley Fool, 20 hours ago</sub>  
  A rough day for AI stocks had several causes, and the signals from CoreWeave, ASML, and a famous investor don't all point the same way.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,646.12 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 1,753.18 (-6.1%), 50d 1,736.01 (-5.2%), 200d 1,582.51 (+4.0%); 50d above 200d
Momentum: RSI(14) 38.5 | MACD -21.117 vs signal -1.543 (histogram -19.575)
Returns: 1d -0.1% | 5d -4.2% | 1m -3.8% | 3m -8.6%
52-week range: 966.57 - 1,989.44 (now 66.4% of the way up)
Volatility: ATR(14) 52.66 (3.2% of price) | annualised 20d 28.4%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 634.44B
Valuation: trailing P/E 40.50 | forward P/E 26.22 | P/B 1,414.62 | PEG 1.58
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
Price target: mean 2,152.83 (+30.8% vs last close), range 870.63 - 2,859.97
Recent rating changes:
  - 2026-10-15 JP Morgan: main, Overweight -> Overweight
  - 2026-07-16 JP Morgan: main, Overweight -> Overweight
  - 2026-07-16 Wells Fargo: main, Overweight -> Overweight
  - 2026-07-16 RBC Capital: main, Outperform -> Outperform
  - 2026-07-14 RBC Capital: main, Outperform -> Outperform
  - 2026-07-06 Bernstein: main, Outperform -> Outperform
Institutional ownership: 20.3%
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

### Alphabet (Google) (GOOGL) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [GOOGL Stock Earnings Preview: What to Expect From Alphabet’s Q3 2026 Report](https://www.barchart.com/story/news/8224355/googl-stock-earnings-preview-what-to-expect-from-alphabets-q3-2026-report)  
  <sub>Barchart.com, 4 hours ago</sub>  
  A tougher year-over-year comparison in Google Search could put pressure on revenue growth, while increased spending to expand AI infrastructure may weigh on...
- [Fund Update: 515,645 GOOGLE (GOOGL) shares added to Cardano Risk Management B.V. portfolio](https://www.quiverquant.com/news/Fund+Update%3A+515%2C645+GOOGLE+%28GOOGL%29+shares+added+to+Cardano+Risk+Management+B.V.+portfolio)  
  <sub>Quiver Quantitative, 1 hour ago</sub>  
  Cardano Risk Management B.V. has added 515645 shares of $GOOGL to their portfolio, per a new SEC 13.
- [Google Partners With Xcel Energy To Fuel New AI Data Center With Clean Power](https://www.tikr.com/blog/google-xcel-energy-ai-data-center-clean-power)  
  <sub>TIKR.com, 1 hour ago</sub>  
  Google and Xcel Energy propose a clean power plan for a new Minnesota AI data center. Here's what it means for Alphabet stock.
- [How Investors May Respond To Google (GOOGL) London Cloud Outage](https://finance.yahoo.com/markets/stocks/articles/investors-may-respond-google-googl-121243894.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  A recent outage at Alphabet's Google Cloud London region caused serious network disruption, affecting major UK banks, fintechs and public services that rely...
- [Investor Alert: Alphabet (GOOG, GOOGL) has been Sued for Securities Fraud Over Alleged Misstatements made to Investors](https://www.morningstar.com/news/pr-newswire/20261020ny74456/investor-alert-alphabet-goog-googl-has-been-sued-for-securities-fraud-over-alleged-misstatements-made-to-investors)  
  <sub>Morningstar, 5 hours ago</sub>  
  Investor Alert: Alphabet (GOOG, GOOGL) has been Sued for Securities Fraud Over Alleged Misstatements made to Investors...
- [Alphabet (GOOGL) Stock Quotes, Company News And Chart Analysis](https://www.investors.com/news/technology/alphabet-googl-stock-quotes-company-news-google-stock-chart-analysis/)  
  <sub>Investor's Business Daily, 21 hours ago</sub>  
  Alphabet (GOOGL) Stock Quotes, Company News And Chart Analysis · IBD STAFF · Updated 01:40 PM ET 10/19/2026. Alphabet Cl A (GOOGL).
- [Alphabet Stock Slipped After Q2 Earnings. Here's What Investors Need to See in Q3.](https://www.fool.com/investing/2026/10/19/alphabet-q3-earnings-expectations/)  
  <sub>The Motley Fool, 15 hours ago</sub>  
  Wall Street can be a little impatient with the massive amounts of money that technology companies are spending on artificial intelligence. Alphabet (GOOGL...
- [GOOGL Stock Technicals: Gains 1.05% on Monday, Golden Cross Formed](https://journalarta.com/en/2026/10/20/googl-stock-technicals-gains-1-05-on-monday-golden-cross-formed/)  
  <sub>JournalArta, 7 hours ago</sub>  
  On October 19, 2026: price 344.18 USD, trend sideways, RSI 48.1, support 337.83, resistance 353.78. technical analysis of googl stock.
- [Price-Driven Insight from (GOOGL) for Rule-Based Strategy](https://news.stocktradersdaily.com/news_release/17/Price-Driven_Insight_from_GOOGL_for_Rule-Based_Strategy_102026034801_1792482481.html)  
  <sub>Stock Traders Daily, 11 hours ago</sub>  
  Key findings for Alphabet Inc. (NASDAQ: GOOGL). Weak Near-Term Sentiment Could Challenge Long-Term Strength; A mid-channel oscillation pattern is in play.
- [Brokers Suggest Investing in Alphabet (GOOGL): Read This Before Placing a Bet](https://finance.yahoo.com/markets/stocks/articles/brokers-suggest-investing-alphabet-googl-123004368.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The recommendations of Wall Street analysts are often relied on by investors when deciding whether to buy, sell, or hold a stock. Media reports about these...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 343.57 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 345.50 (-0.6%), 50d 344.10 (-0.2%), 200d 341.20 (+0.7%); 50d above 200d
Momentum: RSI(14) 47.6 | MACD 0.376 vs signal 0.932 (histogram -0.556)
Returns: 1d -0.2% | 5d -2.9% | 1m -3.2% | 3m +0.4%
52-week range: 250.46 - 402.62 (now 61.2% of the way up)
Volatility: ATR(14) 8.35 (2.4% of price) | annualised 20d 21.9%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 4.20T
Valuation: trailing P/E 17.24 | forward P/E 22.39 | P/B 6.75 | PEG 1.25
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
Ratings: 13 strong buy, 43 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 430.05 (+25.2% vs last close), range 340.00 - 515.00
Recent rating changes:
  - 2026-10-19 Keybanc: main, Overweight -> Overweight
  - 2026-10-15 JP Morgan: main, Overweight -> Overweight
  - 2026-10-14 UBS: main, Neutral -> Neutral
  - 2026-10-12 Cantor Fitzgerald: reit, Overweight -> Overweight
  - 2026-10-08 Needham: reit, Buy -> Buy
  - 2026-10-06 Wells Fargo: main, Overweight -> Overweight
Institutional ownership: 81.1%
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

- [HDFC Bank Limited $HDB Stock Holdings Boosted by Value Partners Investments Inc.](https://www.marketbeat.com/instant-alerts/filing-hdfc-bank-limited-hdb-stock-holdings-boosted-by-value-partners-investments-inc-2026-10-19/)  
  <sub>MarketBeat, 15 hours ago</sub>  
  Value Partners Investments Inc. grew its position in shares of HDFC Bank Limited (NYSE:HDB - Free Report) by 85.3% in the 3rd quarter, according to the...
- [HDFC Bank Ltd (HDB) (Q2 2027) Earnings Call Highlights: Deposits Surge 18. ...](https://finance.yahoo.com/markets/stocks/articles/hdfc-bank-ltd-hdb-q2-010104657.html)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  HDFC Bank Ltd (HDB) posted robust 18.8% deposit growth and 15.3% AUM expansion in Q2 FY27, with management signaling NIM has bottomed and GNPA improving to...
- [Is HDB Undervalued? DCF Says Worth $30](https://www.gurufocus.com/news/9131419/is-hdb-undervalued-dcf-says-worth-30)  
  <sub>GuruFocus, 3 hours ago</sub>  
  On October 20, 2026, we conducted a DCF analysis for HDFC Bank Ltd (HDB) amidst a challenging price performance context, with the stock down 35.7%...
- [HDFC Bank ADR Falls After Quarterly Profit Miss and Ownership Overhang](https://www.quiverquant.com/news/HDFC+Bank+ADR+Falls+After+Quarterly+Profit+Miss+and+Ownership+Overhang)  
  <sub>Quiver Quantitative, 22 hours ago</sub>  
  HDFC Bank Limited (HDB) is down 3.1% today. Here is some analysis on what might have caused this pri.
- [TRXB (TRXB) Stock Price Today, Live Chart & News](https://techgraph.co/stock-market/quote/trxb/)  
  <sub>TechGraph, 4 hours ago</sub>  
  TRXB (TRXB) stock price today on NYSE. Live chart, share price, market cap, 52-week range, dividends and news on TechGraph.
- [HDFC Bank: Neutral View Is Justified By In-Line Results And Leadership Transition (HDB)](https://seekingalpha.com/article/4955177-hdfc-bank-neutral-view-is-justified-by-in-line-results-and-leadership-transition)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  HDFC Bank Limited remains a Hold, as Q2FY27 earnings were in line, with muted sequential growth and mixed operational trends. Learn more about HDB stock...
- [HDB stock at EUR 20.60 pre-market before the Xetra open](https://www.ad-hoc-news.de/boerse/news/vorboerse/hdb-stock-at-eur-20-60-pre-market-before-the-xetra-open/70368879)  
  <sub>ad-hoc-news.de, 9 hours ago</sub>  
  HDFC Bank provides banking and financial services through physical and digital channels. At Lang & Schwarz the stock trades pre-market at EUR 20.60 on...
- [HDFC Bank Ltd Stock (HDB) Moved Down by 3.61% on Oct 19: What Signal Does It Send?](https://www.tradingkey.com/news/market-movers/262224139-market-movers-hdb-20261019)  
  <sub>TradingKey, 22 hours ago</sub>  
  HDFC Bank ADRs fell due to second-quarter net profit missing analyst expectations.Margin compression, higher funding costs, and leadership transition...
- [HDFC Bank (NYSE:HDB) Shares Gap Down - Should You Sell?](https://www.marketbeat.com/instant-alerts/price-hdfc-bank-nyse-hdb-shares-gap-down-should-you-sell-2026-10-19/)  
  <sub>MarketBeat, 23 hours ago</sub>  
  HDFC Bank Limited (NYSE:HDB - Get Free Report) gapped down before the market opened on Monday. The stock had previously closed at $23.84, but opened at...
- [Is HDFC Bank Ltd (HDB) a Bargain After 3.2% Drop? GF Value Says Undervalued](https://www.gurufocus.com/news/9130395/is-hdfc-bank-ltd-hdb-a-bargain-after-32-drop-gf-value-says-undervalued)  
  <sub>GuruFocus, 17 hours ago</sub>  
  On October 19, 2026, HDFC Bank Ltd (HDB) shares fell by 3.2% to $23.08. This decline comes amidst a challenging year for the bank, with its share price down...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 23.42 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 22.71 (+3.2%), 50d 22.90 (+2.3%), 200d 26.27 (-10.8%); 50d below 200d
Momentum: RSI(14) 55.5 | MACD 0.093 vs signal -0.053 (histogram 0.146)
Returns: 1d +1.5% | 5d +2.9% | 1m -1.0% | 3m +1.1%
52-week range: 21.84 - 37.18 (now 10.3% of the way up)
Volatility: ATR(14) 0.58 (2.5% of price) | annualised 20d 30.7%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 120.39B
Valuation: trailing P/E 15.11 | forward P/E 16.96 | P/B 9.39 | PEG n/a
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
Price target: mean 30.30 (+29.3% vs last close), range 26.20 - 33.00
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

### Eli Lilly (LLY) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Eli Lilly stock hits all-time high at 1293.11 USD](https://www.investing.com/news/company-news/eli-lilly-stock-hits-alltime-high-at-129311-usd-93CH-4960361)  
  <sub>Investing.com, 57 minutes ago</sub>  
  Eli Lilly's stock reached an all-time high of $1,293.11, marking a significant milestone for the pharmaceutical giant. The stock currently trades at...
- [Eli Lilly (LLY) Sees $85.4 Million in Net ETF Buying on Oct. 16](https://finance.yahoo.com/markets/stocks/articles/eli-lilly-lly-sees-85-110159074.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  37 ETFs bought LLY shares versus 14 that sold, for a net inflow of $85.4 million.
- [Eli Lilly and Co Stock (LLY) Opened Up by 5.01% on Oct 20: A Full Analysis](https://www.tradingkey.com/news/market-movers/262225983-market-movers-lly-20261020)  
  <sub>TradingKey, 55 minutes ago</sub>  
  Eli Lilly's metabolic drugs and pipeline advancements drove strong investor sentiment.The company reported $65.18B in annual revenue and $20.64B net profit.
- [Is Eli Lilly Stock Too Dependent On Two Drugs?](https://www.trefis.com/stock/lly/articles/619389/is-eli-lilly-stock-too-dependent-on-two-drugs/2026-10-20)  
  <sub>Trefis, 5 hours ago</sub>  
  Two drugs, Mounjaro and Zepbound, accounted for $14.9 billion of Eli Lilly's (LLY) $23.0 billion in revenue during fiscal Q2 2026. This leaves Eli Lilly...
- [1 Unpopular Stock That Should Get More Attention and 2 Facing Challenges](https://stockstory.org/us/stocks/nyse/lly/news/buy-or-sell/1-unpopular-stock-that-should-get-more-attention-and-2-facing-challenges)  
  <sub>StockStory, 5 hours ago</sub>  
  When Wall Street turns bearish on a stock, it's worth paying attention. These calls stand out because analysts rarely issue grim ratings on companies for...
- [Eli Lilly (LLY) Sued By Pennsylvania Over Insulin Price Inflation](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-lly/eli-lilly/news/eli-lilly-lly-sued-by-pennsylvania-over-insulin-price-inflat)  
  <sub>Simply Wall Street, 5 hours ago</sub>  
  Pennsylvania filed a lawsuit against Eli Lilly (NYSE:LLY) and other defendants on Oct. 20, 2026, alleging coordinated insulin price inflation.
- [Eli Lilly (LLY) Stock Dips While Market Gains: Key Facts](https://finance.yahoo.com/markets/stocks/articles/eli-lilly-lly-stock-dips-204502799.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  In the latest trading session, Eli Lilly (LLY) closed at $1,240.34, marking a -1.33% move from the previous day. The stock fell short of the S&P 500,...
- [Eli Lilly, IBD Stock Of The Day, Rides Foundayo, Medicare Bridge To Buy Point](https://www.investors.com/research/ibd-stock-of-the-day/eli-lilly-stock-foundayo-medicare-bridge-buy-point/)  
  <sub>Investor's Business Daily, 20 hours ago</sub>  
  Eli Lilly stock is holding near a buy point after surging last week as investors rotated out of AI stocks into fast-growth healthcare names.
- [One holder reports sole voting power over 90.1M Eli Lilly (LLY) shares.](https://www.stocktitan.net/sec-filings/LLY/schedule-13g-a-eli-lilly-co-amended-passive-investment-disclosure-fa3bf3c33ba2.html)  
  <sub>Stock Titan, 20 hours ago</sub>  
  The September 30, 2026 stake uses 941357065 shares outstanding on August 3, 2026. None were deemed owned through rights to acquire shares.
- [Prediction: Eli Lilly Stock Could Be a Long-Term Winner for Investors](https://247wallst.com/investing/2026/10/19/prediction-eli-lilly-stock-could-be-a-long-term-winner-for-investors/)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  Eli Lilly just crushed earnings again and sits within striking distance of its all-time high, but a looming price war with Novo Nordisk and a dangerously...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,302.00 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 1,189.13 (+9.5%), 50d 1,182.84 (+10.1%), 200d 1,081.85 (+20.3%); 50d above 200d
Momentum: RSI(14) 71.8 | MACD 24.264 vs signal 10.940 (histogram 13.324)
Returns: 1d +5.0% | 5d +11.6% | 1m +11.8% | 3m +12.0%
52-week range: 799.57 - 1,302.00 (now 100.0% of the way up)
Volatility: ATR(14) 37.34 (2.9% of price) | annualised 20d 31.8%
Volume: 0.50x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.16T
Valuation: trailing P/E 43.71 | forward P/E 27.58 | P/B 34.26 | PEG 1.14
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
Price target: mean 1,329.92 (+2.1% vs last close), range 930.00 - 1,600.00
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
(24 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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
  <sub>Yahoo! Finance Canada, 12 hours ago</sub>  
  NVIDIA Corporation (NVDA) · -4.08% · -2.33% · 7.64% · 16.40% · 18.49% · 873.93% · 496,105.71%. Key Events. Baseline. Advanced Chart. Loading chart for NVDA.
- [Dear Nvidia Stock Fans, Mark Your Calendars for October 20](https://www.barchart.com/story/news/8234359/dear-nvidia-stock-fans-mark-your-calendars-for-october-20)  
  <sub>Barchart.com, 27 minutes ago</sub>  
  Nvidia (NVDA), the bellwether of the AI trade, will hold its GTC Berlin AI Conference today. CEO Jensen Huang is scheduled to speak, and the market will not...
- [NVIDIA Corporation (NVDA) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/NVDA/)  
  <sub>Yahoo Finance UK, 14 hours ago</sub>  
  NVIDIA Corporation (NVDA) · -4.08% · -2.33% · 7.64% · 16.40% · 18.49% · 873.93% · 496,105.71%. Key events. Baseline. Advanced chart. Loading chart for NVDA.
- [Not Even Rumors of a Big China Chip Purchase Can Lift Nvidia Stock](https://www.barrons.com/articles/nvidia-stock-china-boost-chips-033f27b7)  
  <sub>Barron's, 55 minutes ago</sub>  
  Nvidia stock was falling on Tuesday as selling continued to hit AI and chip stocks after a brief reprieve on Monday from a two-week rout.
- [Congressman Sells Nvidia Stock Again: 7 Sales in 2026 Add to Trades Since 2022](https://www.benzinga.com/news/politics/26/10/62456282/congressman-sells-nvidia-stock-again-7-sales-in-2026-add-to-trades-since-2022)  
  <sub>Benzinga, 16 hours ago</sub>  
  A member of Congress has been selling Nvidia stock consistently in 2026 and in each year since 2022. Here's a look at the history.
- [NVIDIA Keeps Falling and Wall Street Won’t Move Its Target. Is It Time To Buy?](https://247wallst.com/investing/2026/10/20/nvidia-keeps-falling-and-wall-street-wont-move-its-target-is-it-time-to-buy/)  
  <sub>24/7 Wall St., 3 hours ago</sub>  
  NVIDIA just doubled its revenue yet the stock keeps sliding, and Wall Street still refuses to budge its price target. Something in that gap between the...
- [Nvidia secures $35B in orders for new export-compliant GPU from Chinese tech giants: report (NVDA:NASDAQ)](https://seekingalpha.com/news/4654626-nvidia-secures-35b-in-orders-for-new-export-compliant-gpu-from-chinese-tech-giants-report)  
  <sub>Seeking Alpha, 33 minutes ago</sub>  
  Nvidia secures $35B+ China orders for RTX Pro 5500 export-compliant GPUs as ByteDance, Alibaba, Tencent face supply limits—read what it means for NVDA.
- [Nvidia Stock Hasn’t Been This Cheap in 7 Years. Only 1 Explanation Makes Sense.](https://www.theglobeandmail.com/investing/markets/stocks/NVDA/pressreleases/8221868/nvidia-stock-hasnt-been-this-cheap-in-7-years-only-1-explanation-makes-sense/)  
  <sub>The Globe and Mail, 5 hours ago</sub>  
  Detailed price information for Nvidia Corp (NVDA-Q) from The Globe and Mail including charting and trades.
- [Nvidia Stock Could Be Headed for a Significant Revaluation](https://247wallst.com/investing/2026/10/19/nvidia-stock-could-be-headed-for-a-significant-revaluation/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  NVDA posted 106% revenue growth to $96 billion yet trades at just 14x forward earnings, a valuation cheaper than the average S&P 500 stock despite far...
- [Is Nvidia (NVDA) Stock Priced Right?](https://finance.yahoo.com/markets/stocks/articles/nvidia-nvda-stock-priced-180722414.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Chip stocks fell sharply last week, and Nvidia (NASDAQ:NVDA) dropped nearly 2% with them. Yahoo Finance reported that investors were worried about heavily...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 217.70 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 227.10 (-4.1%), 50d 222.94 (-2.4%), 200d 203.27 (+7.1%); 50d above 200d
Momentum: RSI(14) 42.3 | MACD -1.217 vs signal 1.026 (histogram -2.243)
Returns: 1d +0.3% | 5d -4.7% | 1m -4.3% | 3m +2.7%
52-week range: 165.17 - 239.24 (now 70.9% of the way up)
Volatility: ATR(14) 5.92 (2.7% of price) | annualised 20d 23.5%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 5.26T
Valuation: trailing P/E 27.53 | forward P/E 13.68 | P/B 22.96 | PEG 0.48
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
  2026-09-30 beat by 4% | 2026-09-30 beat by 4% | 2026-06-30 beat by 4% | 2026-06-30 beat by 4%
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
Price target: mean 328.72 (+51.0% vs last close), range 180.00 - 515.00
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

### Royal Bank of Canada (RY) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [(RY) Market Dynamics and Trading Signals (RY:CA)](https://news.stocktradersdaily.com/canada/ry-market-dynamics-and-trading-signals_20261020_a11026)  
  <sub>Stock Traders Daily, 3 hours ago</sub>  
  Market Dynamics Report for Royal Bank of Canada (RY) Featuring Key Trading Signals.
- [Royal Bank Of Canada $RY Stock Sold by Value Partners Investments Inc.](https://www.marketbeat.com/instant-alerts/filing-royal-bank-of-canada-ry-stock-sold-by-value-partners-investments-inc-2026-10-19/)  
  <sub>MarketBeat, 15 hours ago</sub>  
  Value Partners Investments Inc. reduced its holdings in shares of Royal Bank Of Canada (NYSE:RY - Free Report) (TSE:RY) by 12.0% in the 3rd quarter,...
- [The Toronto-Dominion Bank (TD) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TD/)  
  <sub>Yahoo! Finance Canada, 12 hours ago</sub>  
  Find the latest The Toronto-Dominion Bank (TD) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Royal Bank of Canada stock falls Monday, underperforms market](https://www.marketwatch.com/data-news/royal-bank-of-canada-stock-falls-monday-underperforms-market-4b41ba1b-2a853691200f)  
  <sub>MarketWatch, 18 hours ago</sub>  
  slipped 0.89% to C$277.51 Monday, in what proved to be an all-around poor trading session for the Canadian market, with the S&P/TSX Composite Index.
- [3 AI Stocks to Buy Amid This Deep Correction](https://www.theglobeandmail.com/investing/markets/stocks/FIX/pressreleases/8233963/3-ai-stocks-to-buy-amid-this-deep-correction/)  
  <sub>The Globe and Mail, 36 minutes ago</sub>  
  Sandisk's revenue more than quadrupled year over year, and its stock buyback program has expanded sharply. Nebius is commanding higher rates from...
- [Assenagon Asset Management S.A. Sells 1,544,185 Shares of Royal Bank Of Canada $RY](https://www.marketbeat.com/instant-alerts/filing-assenagon-asset-management-sa-sells-1544185-shares-of-royal-bank-of-canada-ry-2026-10-20/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Assenagon Asset Management S.A. decreased its position in shares of Royal Bank Of Canada (NYSE:RY - Free Report) (TSE:RY) by 97.1% during the 3rd quarter,...
- [RBC launches quantum strategy: what it means for Royal Bank of Canada stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/rbc-launches-quantum-strategy-what-it-means-for-royal-bank-of-canada-stock/70371851)  
  <sub>ad-hoc-news.de, 5 hours ago</sub>  
  RBC appoints a quantum director and signs two university partnerships. Royal Bank of Canada stock costs EUR 175.24 on October 20, 2026.
- [RY Jan 2029 220.000 call (RY290119C00220000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RY290119C00220000/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Find the latest RY Jan 2029 220.000 call (RY290119C00220000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Zacks Investment Ideas feature highlights: Taiwan Semiconductor Manufacturing](https://www.theglobeandmail.com/investing/markets/stocks/TSM/pressreleases/8234395/zacks-investment-ideas-feature-highlights-taiwan-semiconductor-manufacturing/)  
  <sub>The Globe and Mail, 25 minutes ago</sub>  
  Detailed price information for Taiwan Semiconductor ADR (TSM-N) from The Globe and Mail including charting and trades.
- [IDMO: This International Momentum ETF Has A Hidden Risk, But It's Still A Buy](https://seekingalpha.com/article/4955389-idmo-this-international-momentum-etf-has-a-hidden-risk-but-its-still-a-buy)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  Invesco S&P International Developed Momentum ETF maintains a 'buy' rating for long-term investors despite a recent fall from its September highs.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 198.71 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 196.24 (+1.3%), 50d 202.98 (-2.1%), 200d 187.89 (+5.8%); 50d above 200d
Momentum: RSI(14) 51.1 | MACD -1.889 vs signal -2.704 (histogram 0.815)
Returns: 1d +1.2% | 5d +2.1% | 1m -3.6% | 3m -6.0%
52-week range: 145.41 - 217.87 (now 73.6% of the way up)
Volatility: ATR(14) 2.96 (1.5% of price) | annualised 20d 17.8%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 275.10B
Valuation: trailing P/E 17.37 | forward P/E 15.67 | P/B 2.90 | PEG 2.26
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
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-09-30 in line | 2026-06-30 in line | 2026-03-31 beat by 3% | 2025-12-31 beat by 6%
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
Price target: mean 212.32 (+6.8% vs last close), range 185.31 - 233.52
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

### Teva Pharmaceutical (TEVA) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Among initial responders, week-44 remission was 58% for ulcerative colitis and 84% for Crohn’s on the higher dose.](https://www.google.com/goto?url=CAEStAEB6zswFWh7DpF9b2IEPA8oFoSBpTAAW5qt2o_bigo3dMuWQ3ylsugyjRB48lpTye0f_lVY3RsrPwdRGnxE7nBMwP_NFdVfC9UrwUDEVvzE4FU2kavvDI1Ra3Zjkqa7zW8PKNcyJej88OmpxOlKF6wE2_GAP5-bobDI3-tz479QnXWXc1rx2QvbOpf_E71QsOF9ncQDH_KkqkQaXadW1TCCByMVxzTCD10WL_ecvcncWur86bo)  
  <sub>Stock Titan, 3 hours ago</sub>  
  Teva (TEVA) and Sanofi reported that investigational duvakitug maintained efficacy through 44 weeks of maintenance treatment in a phase 2b extension.
- [Alvotech wins FDA for Humira biosimilar process (ALVO:NASDAQ)](https://seekingalpha.com/news/4654551-alvotech-wins-fda-humira-biosimilar-process)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Alvotech (ALVO) stock gains as the FDA OKs new manufacturing process for Simlandi, the company's Humira biosimilar marketed with Teva (TEVA).
- [Trump Endorses Netanyahu. What Investors Need To Know About The Israeli Election.](https://www.investors.com/news/israel-elections-trump-netanyahu-stocks/)  
  <sub>Investor's Business Daily, 23 hours ago</sub>  
  President Donald Trump endorsed Israeli Prime Minister Benjamin Netanyahu ahead of the latter's upcoming election.
- [TEVA Oct 2026 37.000 put (TEVA261030P00037000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/TEVA261030P00037000/chart/)  
  <sub>Yahoo! Finance Canada, 13 hours ago</sub>  
  Interactive Chart for TEVA Oct 2026 37.000 put (TEVA261030P00037000), analyze all the data with a huge range of indicators.
- [Teva stock: At USD 41.29, Teva stock sits 1.74 percent below its 52-week high](https://www.ad-hoc-news.de/boerse/news/corporate-news/teva-stock-at-usd-41-29-teva-stock-sits-1-74-percent-below-its-52-week-high/70364220)  
  <sub>ad-hoc-news.de, 24 hours ago</sub>  
  Teva stock costs USD 41.29 on October 19, 2026, down 0.51 percent on the NYSE. Revenue reached USD 4.14 billion in the second quarter ended June 30, 2026.
- [Deckers Outdoor Corporation (DECK) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/DECK/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Find the latest Deckers Outdoor Corporation (DECK) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Ultragenyx Pharmaceutical Enters Settlement With Navinta Over Dojolvi](https://finance.yahoo.com/healthcare/articles/ultragenyx-pharmaceutical-enters-settlement-navinta-145134451.html)  
  <sub>Yahoo Finance, 24 hours ago</sub>  
  Ultragenyx Pharmaceutical (RARE) and Baylor Research Institute have entered into a settlement agreement with Navinta to resolve patent litigation related to...
- [Migraine Market is Expected to Expand at 6% Growth Rate by 2036, Owing to the Development of Novel Mechanisms beyond CGRP, including PACAP-targeted Therapies, TRPA1 Antagonists, and Next-generation Neuromuscular Approaches | DelveInsight](https://www.google.com/goto?url=CAESjQEB6zswFau6xezmLwZuRPPqRHwSvLBNRYsE4BQc2EynnWzwNU3DMfg8m_UdbntviTu4LjiTsFv8CVpUdVCgMQnaBRXEWAv5KOU1Rum0SCYQkuexaLtmDaOueEehswJRZTYiPiPrLAcf2JPS--m2ackwEjIa8oEjzNQIhygPnr-HIa7SnUdTB_jjpK4Y3PE)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  The migraine market is expected to grow steadily over the forecast period (2026–2036) driven by the rising global prevalence of migraine,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 41.30 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 40.11 (+3.0%), 50d 38.49 (+7.3%), 200d 34.25 (+20.6%); 50d above 200d
Momentum: RSI(14) 63.4 | MACD 0.882 vs signal 0.839 (histogram 0.042)
Returns: 1d -0.0% | 5d +0.1% | 1m +3.1% | 3m +37.0%
52-week range: 18.95 - 41.50 (now 99.1% of the way up)
Volatility: ATR(14) 1.07 (2.6% of price) | annualised 20d 26.3%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 48.17B
Valuation: trailing P/E 68.83 | forward P/E 13.39 | P/B 6.21 | PEG n/a
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
Price target: mean 47.58 (+15.2% vs last close), range 42.00 - 55.00
Recent rating changes:
  - 2026-10-15 Barclays: main, Overweight -> Overweight
  - 2026-10-12 JP Morgan: main, Overweight -> Overweight
  - 2026-10-01 TD Cowen: init, ? -> Buy
  - 2026-09-23 Oppenheimer: init, ? -> Outperform
  - 2026-09-09 Leerink Partners: init, ? -> Outperform
  - 2026-09-04 UBS: main, Buy -> Buy
Institutional ownership: 26.9%
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

- [Fund Update: New $109.0M $XOM stock position opened by Sumitomo Mitsui DS Asset Management Company, Ltd](https://www.quiverquant.com/news/Fund+Update%3A+New+%24109.0M+%24XOM+stock+position+opened+by+Sumitomo+Mitsui+DS+Asset+Management+Company%2C+Ltd)  
  <sub>Quiver Quantitative, 4 hours ago</sub>  
  Sumitomo Mitsui DS Asset Management Company, Ltd has opened a new $109.0M position in $XOM, per a ne.
- [ExxonMobil Corporation (NYSE:XOM) Stock Has Consensus Target Price of $167.30 According to Brokerages](https://www.marketbeat.com/instant-alerts/consensus-exxonmobil-corporation-nyse-xom-stock-has-consensus-target-price-of-16730-according-to-brokerages-2026-10-20/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Shares of ExxonMobil Corporation (NYSE:XOM - Get Free Report) have been assigned an average recommendation of "Hold" from the twenty-five ratings firms that...
- [Analysts Conflicted on These Energy Names: Exxon Mobil (XOM) and Liberty Energy (LBRT)](https://www.theglobeandmail.com/investing/markets/stocks/XOM/pressreleases/8226400/analysts-conflicted-on-these-energy-names-exxon-mobil-xom-and-liberty-energy-lbrt/)  
  <sub>The Globe and Mail, 3 hours ago</sub>  
  Detailed price information for Exxonmobil Holdings Corp (XOM-N) from The Globe and Mail including charting and trades.
- [Better Oil Stock: Chevron (CVX) vs. ExxonMobil (XOM)](https://finance.yahoo.com/energy/articles/better-oil-stock-chevron-cvx-191500321.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Chevron (NYSE: CVX) and ExxonMobil (NYSE: XOM) are two of the world's largest integrated energy companies. They both own upstream exploration and extraction...
- [Why Did XOM, CVX, MPC Stocks Surge To 52-Week Highs Today?](https://stocktwits.com/news-articles/markets/equity/why-did-xom-cvx-mpc-stocks-surge-to-52-week-highs-today/cZxq1SXRBua)  
  <sub>Stocktwits, 11 hours ago</sub>  
  XOM stock clocked an annual high of $179.30 on Monday during trading hours, before closing about 0.4% down. CVX stock surged to a 52-week high of $225.67,...
- [CVX, XOM Stocks Hit 52-Week Highs: What's Fueling The Surge? - Chevron (NYSE:CVX)](https://www.benzinga.com/markets/equities/26/10/62458379/chevron-exxonmobil-stocks-hit-52-week-highs-as-fresh-us-israel-threats-against-iran-push-brent-crude-to-5-month-highs)  
  <sub>Benzinga, 7 hours ago</sub>  
  Chevron Corp. (NYSE:CVX) and ExxonMobil Holdings Corp. (NYSE:XOM) shares climbed to fresh 52-week highs on Monday as renewed U.S. and Israeli threats...
- [XOM RSI Overbought: Explained](https://journalarta.com/en/2026/10/20/xom-rsi-overbought-stock-drops-0-39-october-19-2026/)  
  <sub>JournalArta, 6 hours ago</sub>  
  On October 19, 2026: price 178.28 USD, trend uptrend, RSI 71.1, support 158.71, resistance 178.98. technical analysis of xom stock. XOM RSI Overbought...
- [ExxonMobil Corporation $XOM Stock: Retirement Planning Group LLC Grows Position](https://www.marketbeat.com/instant-alerts/filing-exxonmobil-corporation-xom-stock-retirement-planning-group-llc-grows-position-2026-10-20/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Retirement Planning Group LLC lifted its position in ExxonMobil Corporation (NYSE:XOM - Free Report) by 27.7% during the third quarter, according to the...
- [Technical Reactions to XOM Trends in Macro Strategies](https://news.stocktradersdaily.com/news_release/40/Technical_Reactions_to_XOM_Trends_in_Macro_Strategies_101926074401_1792453441.html)  
  <sub>Stock Traders Daily, 19 hours ago</sub>  
  Key findings for Exxon Mobil Corporation (NYSE: XOM). Strong Sentiment Across All Horizons Supports Overweight Bias; A mid-channel oscillation pattern is in...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 175.46 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 167.95 (+4.5%), 50d 164.51 (+6.7%), 200d 152.27 (+15.2%); 50d above 200d
Momentum: RSI(14) 63.8 | MACD 4.096 vs signal 3.051 (histogram 1.045)
Returns: 1d -1.6% | 5d +0.8% | 1m +10.8% | 3m +13.6%
52-week range: 112.70 - 178.98 (now 94.7% of the way up)
Volatility: ATR(14) 3.66 (2.1% of price) | annualised 20d 19.1%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 721.48B
Valuation: trailing P/E 22.58 | forward P/E 14.45 | P/B 2.78 | PEG 1.38
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
Price target: mean 178.36 (+1.7% vs last close), range 142.00 - 206.00
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

> Neutral overall as macro, technicals, flows and fundamentals show no clear directional bias.

**Main reasons it gave:**
- Technical indicators (RSI 43.4, MACD negative) show slight bearish momentum but no decisive break
- Macro data: yields down slightly, dollar weaker, VIX modestly higher, no surprise
- Fund flows flat over the past week and month, indicating no net inflows or outflows
- Analyst coverage absent (no ratings or price targets for holdings)
- Fund fundamentals: moderate 3.2% yield and strong 3-year record, but 47% cash allocation limits upside

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange Traded Concepts to Close and Liquidate The xETFs TSLA Daily Income ETF (NYSE: TYYY)](https://www.streetinsider.com/Press+Releases/Exchange+Traded+Concepts+to+Close+and+Liquidate+The+xETFs+TSLA+Daily+Income+ETF+%28NYSE%3A+TYYY%29/27207185.html)  
  <sub>StreetInsider, 2 hours ago</sub>  
  OKLAHOMA CITY , Oct. 20, 2026 /PRNewswire/ -- After careful consideration, Exchange Traded Concepts, LLC, the Fund's investment adviser has recommended,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 28.18 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 28.36 (-0.6%), 50d 28.50 (-1.1%), 200d 27.30 (+3.2%); 50d above 200d
Momentum: RSI(14) 43.4 | MACD -0.078 vs signal -0.054 (histogram -0.024)
Returns: 1d -0.1% | 5d -0.9% | 1m -1.7% | 3m -0.2%
52-week range: 25.44 - 29.49 (now 67.7% of the way up)
Volatility: ATR(14) 0.24 (0.9% of price) | annualised 20d 9.1%
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
Three-year record: +13.6% a year | beta to the market 0.35
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 27.60M | fund size: 777.77M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Crude oil inventories draw of 8.6 million barrels (low level, bullish)
- EIA price outlook predicts WTI down 14% over six months (bearish)
- Technical: price near 52‑week high (+15% vs 200‑day SMA) but volume 0.21× 20‑day avg (no strong momentum)
- Fund flows flat (0% change in share count)
- Macro: yields down modestly, VIX up 2.4 points, dollar down 0.61 (no surprise data)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 33.21 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 32.91 (+0.9%), 50d 32.16 (+3.3%), 200d 28.80 (+15.3%); 50d above 200d
Momentum: RSI(14) 55.8 | MACD 0.375 vs signal 0.367 (histogram 0.008)
Returns: 1d -1.4% | 5d -0.8% | 1m +1.9% | 3m +11.2%
52-week range: 22.11 - 33.74 (now 95.4% of the way up)
Volatility: ATR(14) 0.48 (1.5% of price) | annualised 20d 16.0%
Volume: 0.21x the 20-day average
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
Three-year record: +15.8% a year | beta to the market 1.05
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
US inventories, week ending 2026-10-09 (published the following Wednesday)
  Crude oil: 415.6 million barrels, -8.6 on the week (a draw), 15% percentile over 52 weeks
  Natural gas: 3,567.0 billion cubic feet, +67.0 on the week (a build), 83% percentile over 52 weeks
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 111.40M | fund size: 3.70B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, policy change, or decisive technical break; fund fundamentals remain solid despite modest outflows.

**Main reasons it gave:**
- Fund flows: -11.8% share count decline over past month
- Technicals: price below 50‑day SMA (91.44 vs 93.10) and 200‑day SMA (95.14)
- Macro: US Treasury yields fell modestly (10‑yr -0.14% week) with no policy surprise
- Fund basics: yield 5.4% with mixed credit quality (BBB 33.5%, BB 25.3%)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 91.44 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 91.22 (+0.2%), 50d 93.10 (-1.8%), 200d 95.14 (-3.9%); 50d below 200d
Momentum: RSI(14) 44.6 | MACD -0.493 vs signal -0.666 (histogram 0.173)
Returns: 1d +0.4% | 5d +0.2% | 1m -2.5% | 3m -3.8%
52-week range: 90.14 - 97.74 (now 17.1% of the way up)
Volatility: ATR(14) 0.53 (0.6% of price) | annualised 20d 7.6%
Volume: 0.31x the 20-day average
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
Three-year record: +9.7% a year | beta to the market 1.10
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -0.7% (-91.58M) over 7d | 1 month: -11.8% (-1.74B) over 31d
Shares outstanding: 141.28M | fund size: 12.92B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, no decisive technical breakout, and flat fund flows keep the outlook neutral.

**Main reasons it gave:**
- 10-year Treasury yield fell 15 bps this week, supporting bond prices but within expectations
- CFTC positioning shows net short 37.9% with a slight decrease of -0.6% on the week, indicating modest bearish bias but a small bullish shift
- Fund flows flat over the past month, indicating no new demand pressure
- Technical indicators (price just above 20‑day SMA, RSI 52.6, MACD near zero) show no decisive momentum

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 90.38 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 89.62 (+0.8%), 50d 91.20 (-0.9%), 200d 94.07 (-3.9%); 50d below 200d
Momentum: RSI(14) 52.6 | MACD -0.265 vs signal -0.497 (histogram 0.232)
Returns: 1d +0.3% | 5d +0.9% | 1m -0.8% | 3m -2.9%
52-week range: 88.92 - 97.99 (now 16.1% of the way up)
Volatility: ATR(14) 0.49 (0.5% of price) | annualised 20d 6.3%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Long Government
Yield: 4.1%
Credit quality: AA 100.0% | US government debt 99.7%
Three-year record: +3.7% a year | beta to the market 1.16
Cost and size: expense ratio 0.15% | net assets 41.56B
What it is made of: Bonds 99.7%, Cash 0.3%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.05</summary>

```text
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 37.9% of open interest (5,819,512 contracts)
Change on the week: -0.6% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.05</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 146.00M | fund size: 13.20B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error waiting for selector "#main" failed: timeout 30000ms exceeded)

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance due to lack of material macro surprise, mixed technical signals, modest bearish positioning, and thin analyst coverage.

**Main reasons it gave:**
- Macro data unchanged: yields modestly down, VIX up modestly, inflation 3.7% in line with expectations
- Technical: price below 20‑day and 200‑day SMAs, RSI 43.8, MACD slightly negative, low volume
- Positioning: net short 20.6% of open interest, short position increased 4.2% week‑over‑week
- Analyst coverage thin: only 2% of fund covered, 100% buy but limited weight

<details><summary><b>News</b> — score +0.00</summary>

- [What iShares Russell 2000 (IWM) Sold: Moog Leads on Friday](https://finance.yahoo.com/markets/stocks/articles/ishares-russell-2000-iwm-sold-110434611.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  The ETF sold $482.6 million of stock on Friday, with Moog Inc. Class A the largest sale at $1.9 million.
- [Calamos Extends Autocallable Leadership through CAYN—World’s First Indexed Least-Of Autocallable Income ETF](https://www.advisorhub.com/resources/calamos-extends-autocallable-leadership-through-cayn-worlds-first-indexed-least-of-autocallable-income-etf/)  
  <sub>AdvisorHub, 16 hours ago</sub>  
  Calamos continues to innovate in autocallable ETFs with an indexed approach to the popular “least-of” (also known as “worst-of”) autocallable income...
- [Wells Fargo says small caps are unfavorable; economic conditions do not support them (IWM:NYSEARCA)](https://seekingalpha.com/news/4654336-wells-fargo-says-small-caps-are-unfavorable-economic-conditions-do-not-support-them)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Small-cap stocks are losing momentum as the Federal Reserve tightens monetary policy, with the Russell 2000 (IWM) falling 5.5% over five consecutive weeks...
- [WisdomTree US SmallCap Dividend Fund lags peers but offers 2.4% yield and broad diversification.](https://pluang.com/en/news-feed/des-diversifikasi-bagus-tapi-ada-pilihan-lebih-baik)  
  <sub>Pluang, 15 hours ago</sub>  
  The WisdomTree US SmallCap Dividend Fund (DES) provides exposure to small-cap stocks with a 2.4% dividend yield and a value investment focus.
- [Price-Driven Insight from (IWM) for Rule-Based Strategy](https://news.stocktradersdaily.com/news_release/139/Price-Driven_Insight_from_IWM_for_Rule-Based_Strategy_101926080802_1792454882.html)  
  <sub>Stock Traders Daily, 19 hours ago</sub>  
  Key findings for Ishares Russell 2000 Etf (NYSE: IWM). Weak Near-Term Sentiment Could Challenge Long-Term Strength; No clear price positioning signal...
- [Stock Market Today: Nasdaq 100 Rises as AI Chip Rout Reverses, SanDisk Jumps 7%](https://www.tradingview.com/news/benzinga:e9b29a8b4094b:0-stock-market-today-nasdaq-100-rises-as-ai-chip-rout-reverses-sandisk-jumps-7/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks diverged at midday Monday as a rebound in AI chip and infrastructure names lifted the Nasdaq 100 by 1.7% and the S&P 500 by 0.7%, while the Dow...
- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-us-172542006.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.5%. US equity indexes rose amid...
- [DES: Good Diversifier, But There Are Better Options (NYSEARCA:DES)](https://seekingalpha.com/article/4955340-des-good-diversifier-but-there-are-better-options)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  The WisdomTree US SmallCap Dividend Fund offers diversified small-cap exposure with a 2.4% yield and a value tilt. Learn more.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 276.33 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 278.05 (-0.6%), 50d 287.99 (-4.1%), 200d 277.91 (-0.6%); 50d above 200d
Momentum: RSI(14) 43.8 | MACD -3.921 vs signal -3.867 (histogram -0.055)
Returns: 1d +1.9% | 5d -0.1% | 1m -3.2% | 3m -5.9%
52-week range: 229.11 - 305.09 (now 62.1% of the way up)
Volatility: ATR(14) 3.85 (1.4% of price) | annualised 20d 16.1%
Volume: 0.39x the 20-day average
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
Three-year record: +17.4% a year | beta to the market 1.27
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

<details><summary><b>What analysts and big funds say</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.15</summary>

```text
Rolled up from the 5 largest holdings, 2.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.87 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.9% above the current prices
Holdings read: XTSLA, TWST, MOG-A, FROG, TXG
Recent rating changes among them:
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MOG-A: 2026-10-13 JP Morgan: main, Overweight -> Overweight
  - FROG: 2026-10-14 UBS: main, Buy -> Buy
  - TXG: 2026-10-13 TD Cowen: main, Hold -> Hold
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 20.6% of open interest (444,784 contracts)
Change on the week: +4.2% of open interest
Crowding: 22% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 281.05M | fund size: 77.66B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fund flows flat: 0.0% change week‑over‑week
- Treasury yields slipped modestly, no rate surprise
- Price near 52‑week low (101.83) with neutral RSI (50.5) and low volume
- Yield 4.9% close to 10‑yr Treasury 5.08%, high credit quality (A 46.7%, BBB 40.5%)

<details><summary><b>News</b> — score +0.00</summary>

- [Understanding Momentum Shifts in (LQD)](https://news.stocktradersdaily.com/news_release/21/Understanding_Momentum_Shifts_in_LQD_102026061602_1792491362.html)  
  <sub>Stock Traders Daily, 9 hours ago</sub>  
  Price-action only: Ishares Iboxx Usd Investment Grade Corporate Bond Etf (LQD) movements set the tone for institutional models.
- [BGB: Tactical Opportunity With Liquidation Potential (NYSE:BGB)](https://seekingalpha.com/article/4955251-bgb-tactical-opportunity-with-liquidation-potential)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  The Blackstone Strategic Credit 2027 Term Fund offers a floating-rate, high-yield portfolio with a current ~5% discount & ~8% yield. Learn more about BGB...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 103.37 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 102.65 (+0.7%), 50d 104.42 (-1.0%), 200d 107.95 (-4.2%); 50d below 200d
Momentum: RSI(14) 50.5 | MACD -0.367 vs signal -0.600 (histogram 0.233)
Returns: 1d +0.5% | 5d +0.8% | 1m -1.6% | 3m -3.1%
52-week range: 101.83 - 112.92 (now 13.9% of the way up)
Volatility: ATR(14) 0.63 (0.6% of price) | annualised 20d 7.0%
Volume: 0.46x the 20-day average
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
Three-year record: +5.5% a year | beta to the market 1.35
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 293.50M | fund size: 30.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US Treasury yields unchanged this week (3‑month +0.02, 10‑year -0.14) – no macro surprise
- Price above 20‑day SMA (211.73) and 200‑day SMA (206.95) but RSI 58.4 and low volume (0.34× 20‑day avg) – no decisive technical breakout
- CFTC positioning shows net short 21.2% of open interest, +0.3% change – slight bearish bias but modest
- Analyst coverage thin (1.4% of fund) with 78.5% buy rating but ambiguous price target – limited guidance
- Fund basics: P/E 20.26, low expense ratio 0.20%, three‑year return +16.5% – average fundamentals

<details><summary><b>News</b> — score +0.00</summary>

- [RSP vs. VOO: Is Equal-Weight the Answer to a Top-Heavy S 500 in 2026?](https://finance.yahoo.com/markets/stocks/articles/rsp-vs-voo-equal-weight-190234178.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  VOO, the Vanguard S&P 500 ETF, is market-cap weighted — the bigger a company, the bigger its slice. That's why its top 10 holdings now make up roughly 40%...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 215.90 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 211.73 (+2.0%), 50d 215.62 (+0.1%), 200d 206.95 (+4.3%); 50d above 200d
Momentum: RSI(14) 58.4 | MACD 0.048 vs signal -0.643 (histogram 0.690)
Returns: 1d +1.2% | 5d +1.2% | 1m +1.5% | 3m +1.5%
52-week range: 182.18 - 222.77 (now 83.1% of the way up)
Volatility: ATR(14) 2.00 (0.9% of price) | annualised 20d 10.3%
Volume: 0.34x the 20-day average
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
Three-year record: +16.5% a year | beta to the market 0.84
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

<details><summary><b>What analysts and big funds say</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.00</summary>

```text
Rolled up from the 5 largest holdings, 1.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 78.5% | hold 21.5% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -6.4% above the current prices
Holdings read: MRNA, P, ILMN, CRWD, RVTY
Recent rating changes among them:
  - MRNA: 2026-10-15 Goldman Sachs: main, Neutral -> Neutral
  - P: 2026-10-12 Guggenheim: main, Buy -> Buy
  - ILMN: 2026-10-19 Canaccord Genuity: main, Hold -> Hold
  - CRWD: 2026-10-16 Keybanc: main, Overweight -> Overweight
  - RVTY: 2026-10-13 TD Cowen: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.05</summary>

```text
Contract: E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 21.2% of open interest (1,931,607 contracts)
Change on the week: +0.3% of open interest
Crowding: 35% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.05</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 155.55M | fund size: 33.58B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material surprise in policy, data, or technical break. Small positive shift in positioning and stable fundamentals offset by modest bearish net short.

**Main reasons it gave:**
- Fed's hawkish rate hike and expectations of further tightening (NEWS)
- US Treasury yields down across the curve (MACRO)
- Positioning shows net short 30% of OI, decreasing by 2% this week (POSITIONING)
- Fund basics: AA credit quality, low beta 0.24, stable yield 3.6% (FUND BASICS)
- Technicals near neutral: RSI 53, MACD near zero, low volume (TECHNICALS)

<details><summary><b>News</b> — score +0.00</summary>

- [The Weekly Spread: What Shaped Yields And The Dollar This Week](https://stocktwits.com/news-articles/markets/equity/the-weekly-spread-what-shaped-yields-and-the-dollar-this-week/cZtDZlBRBES)  
  <sub>Stocktwits, 15 hours ago</sub>  
  A hawkish interest rate hike by the Federal Reserve and expectations of further tightening propelled the U.S. dollar to its strongest weekly gain since June...
- [Yield stabilization could extend equity rally into year-end - JPMorgan (TLT:NASDAQ)](https://seekingalpha.com/news/4654363-yield-stabilization-could-extend-equity-rally-into-year-end-jpmorgan)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  JPMorgan says stabilizing bond yields could stop equity valuation compression and extend the stock market rally into year-end.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.35 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 81.18 (+0.2%), 50d 81.51 (-0.2%), 200d 82.17 (-1.0%); 50d below 200d
Momentum: RSI(14) 53.3 | MACD -0.040 vs signal -0.087 (histogram 0.047)
Returns: 1d +0.0% | 5d +0.2% | 1m +0.1% | 3m -0.6%
52-week range: 81.05 - 83.18 (now 13.8% of the way up)
Volatility: ATR(14) 0.11 (0.1% of price) | annualised 20d 1.5%
Volume: 0.06x the 20-day average
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
Three-year record: +4.0% a year | beta to the market 0.24
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 30.0% of open interest (4,554,153 contracts)
Change on the week: -2.0% of open interest
Crowding: 87% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 209.30M | fund size: 17.03B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, positioning shows modest net short with little change, and fund flows are flat, so no material catalyst for a directional call.

**Main reasons it gave:**
- Treasury yields slipped modestly (10‑yr -0.14% week) and inflation at 3.7% near expectations – no macro surprise
- Technical indicators show no decisive break: price below 50‑day and 200‑day SMA, low volume (0.23× 20‑day avg)
- CFTC positioning: net short 37.9% of open interest, unchanged week‑over‑week (-0.6% change) – slight bearish bias but not extreme
- Fund flows flat over the past month, indicating no new demand for TIP exposure

<details><summary><b>News</b> — score +0.00</summary>

- [F/m Investments Launches First 30-Year TIPS ETF: RTHY](https://www.businesswire.com/news/home/20261020106036/en/Fm-Investments-Launches-First-30-Year-TIPS-ETF-RTHY)  
  <sub>Business Wire, 2 hours ago</sub>  
  F/m Investments (“F/m”), a $20 billion investment firm and innovative provider of exchange-traded funds (ETFs), announced the launch of the F/m Long-Term...
- [Michigan MERS seeds new F/m Investments long-duration TIPS ETF](https://www.pionline.com/asset-management/exchange-traded-funds/pi-michigan-mers-seeds-fm-investments-tips-etf/)  
  <sub>Pensions & Investments, 20 hours ago</sub>  
  Michigan MERS has committed $25 million as the seed investor in F/m Investments' new long-dated TIPS ETF, with plans to grow the allocation through...
- [FMPI ETF Holdings List — TSX:FMPI](https://www.tradingview.com/symbols/TSX-FMPI/holdings/)  
  <sub>TradingView, 12 hours ago</sub>  
  Explore Fidelity Global Income Portfolio ETF Series units Trust Units holdings with weight, market value, and other helpful data to make more informed...
- [RTHY (RTHY) Stock News](https://www.stocktitan.net/news/RTHY/)  
  <sub>Stock Titan, 2 hours ago</sub>  
  F/m Investments launched the F/m Long-Term Treasury Inflation-Protected Security ETF (Nasdaq: RTHY), focused exclusively on 30-year U.S. inflation-protected...
- [TIPS vs. Dividend Stocks: Which Keeps More Buying Power in Retirement?](https://247wallst.com/investing/2026/10/20/tips-vs-dividend-stocks-which-keeps-more-buying-power-in-retirement/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  PG's 2.76% forward yield is nominal and board-voted each quarter, while TIPS lock in a 2.74% real yield the U.S. Treasury is legally obligated to pay.
- [Are bonds finally a buy? It depends](https://www.moomoo.com/community/feed/are-bonds-finally-a-buy-it-depends-117471220727814)  
  <sub>Moomoo, 11 hours ago</sub>  
  With broader market uncertainty making headlines, some investors are asking whether it is finally time to add bonds to their portfolios. The US 10-yea...
- [TIPS Now Pay 2.8% Above Inflation. Here's The Hurdle That Sets For S&P 500 Investors](https://www.benzinga.com/Opinion/26/10/62452412/tips-now-pay-2-8-above-inflation-heres-the-hurdle-that-sets-for-sp500-investors)  
  <sub>Benzinga, 19 hours ago</sub>  
  Key Takeaways The 10-year Treasury Inflation-Protected Securities (TIPS) yield closed at 2.78% on Oct. 15, up from 1.71% a year earlier, yet the S&P 500...
- [Hrgovic says Joshua, Fury done, tips Itauma for undisputed crown](https://ng.headtopics.com/news/hrgovic-says-joshua-fury-done-tips-itauma-for-undisputed-88986919)  
  <sub>Head Topics, 15 hours ago</sub>  
  Croatian heavyweight Filip Hrgovic says Anthony Joshua and Tyson Fury are nearing the end of their careers, while tipping Moses Itauma for future undispute.
- [SCHD vs. VIG vs. JEPI: Which Dividend ETF Offers the Highest Yield?](https://www.tipranks.com/news/schd-vs-vig-vs-jepi-which-dividend-etf-offers-the-highest-yield)  
  <sub>TipRanks, 2 hours ago</sub>  
  Dividend ETFs are a popular way for investors to earn regular income. Among the popular options are Schwab U.S. Dividend Equity ETF ($SCHD),...
- [3 ETFs with 10%+ Growth Potential, According to AI Analyst](https://www.tipranks.com/news/3-etfs-with-10-growth-potential-according-to-ai-analyst)  
  <sub>TipRanks, 18 hours ago</sub>  
  Exchange-traded funds (ETFs) offer a critical entry point into financial markets. For investors looking to tap into the growth potential of U.S. companies,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 105.51 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 104.55 (+0.9%), 50d 105.83 (-0.3%), 200d 109.02 (-3.2%); 50d below 200d
Momentum: RSI(14) 56.6 | MACD -0.128 vs signal -0.362 (histogram 0.235)
Returns: 1d +0.2% | 5d +0.9% | 1m -0.2% | 3m -2.1%
52-week range: 103.98 - 112.20 (now 18.7% of the way up)
Volatility: ATR(14) 0.40 (0.4% of price) | annualised 20d 4.7%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Inflation-Protected Bond
Yield: 4.7%
Credit quality: AA 100.0% | US government debt 100.0%
Three-year record: +4.1% a year | beta to the market 0.71
Cost and size: expense ratio 0.18% | net assets 14.23B
What it is made of: Bonds 100.0%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 37.9% of open interest (5,819,512 contracts)
Change on the week: -0.6% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 177.70M | fund size: 18.75B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, modest technical move, mixed insider and fundamental signals.

**Main reasons it gave:**
- Large speculators net short 29.8% of open interest (insider data)
- 10‑year Treasury yield down 0.14% on the week; yield curve remains upward sloping
- Technical trend above 20‑day SMA but below 200‑day SMA; low volume
- Fund basics: 5% yield, AA credit quality, low expense ratio, modest 3‑year return

<details><summary><b>News</b> — score +0.00</summary>

- [TLT, EDV and VGLT Make the Same Bet on Long Bonds. One Swings Far Harder Than the Others](https://247wallst.com/investing/etf/2026/10/19/tlt-edv-and-vglt-make-the-same-bet-on-long-bonds-one-swings-far-harder-than-the-others/)  
  <sub>24/7 Wall St., 16 hours ago</sub>  
  Three funds hold government-backed bonds, yet their five-year losses tell a wildly different story. Understanding why one swings so much harder could change...
- [If Rates Keep Rising, So Will These 5 ETFs. Introducing My Bond Hedge Roster (NASDAQ:TLT)](https://seekingalpha.com/article/4955422-if-rates-keep-rising-so-will-these-5-etfs-introducing-my-bond-hedge-roster)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Simplify Interest Rate Hedge ETF (PFIX) offers convex, asymmetric upside during rate spikes, best sized at 1–3% for tactical hedging, not as a buy-and-hold.
- [Long bond ETFs EDV, TLT, and VGLT show vastly d...](https://pluang.com/en/news-feed/tlt-edv-dan-vglt-membuat-pertaruhan-yang-sama-pada-obligasi-jangka-panjang-satu)  
  <sub>Pluang, 15 hours ago</sub>  
  Three ETFs—EDV, TLT, and VGLT—hold long-term U.S. Treasury bonds but differ significantly in price volatility and losses over five years.
- [Investors Just Poured Nearly $12 Billion Into This Battered ETF — and the Reason Could Surprise Wall Street](https://247wallst.com/investing/etf/2026/10/19/investors-just-poured-nearly-12-billion-into-this-battered-etf-and-the-reason-could-surprise-wall-street/)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  Billions keep flowing into a Treasury ETF that has lost ground for years, and the investors driving that trade are not the ones most people would expect.
- [Bond gains amid high crude and inflation data h...](https://pluang.com/en/news-feed/apa-arti-korelasi-rekor-antara-obligasi-dan-minyak-untuk-saham)  
  <sub>Pluang, 23 hours ago</sub>  
  Last week, the semiconductor ETF SMH closed down for its longest streak in 25 years, signaling potential broader market weakness. Despite this, bond prices...
- [Dow, S&P 500, Nasdaq Edge Higher Amid Tech Rebound As Q3 Earnings Season Forges Ahead: DJT, AMZN, CBRS, CRWV Stocks In Focus](https://www.tradingview.com/news/stocktwits:ee6aa3eed094b:0-dow-s-p-500-nasdaq-edge-higher-amid-tech-rebound-as-q3-earnings-season-forges-ahead-djt-amzn-cbrs-crwv-stocks-in-focus/)  
  <sub>TradingView, 11 hours ago</sub>  
  U.S. stock futures climbed into positive territory late Monday as technology stocks rebounded after a sharp selloff last week.Meanwhile, markets are keenly...
- [BofA Is Sticking With an October Rate Hike Even as Markets Bet Against It](https://www.aol.com/articles/bofa-sticking-october-rate-hike-131228000.html)  
  <sub>AOL.com, 2 hours ago</sub>  
  Markets give a Fed rate hike in October just a one-in-five shot, but Bank of America is betting the consensus has it wrong, and the most rate-sensitive bond...
- [Yield stabilization could extend equity rally into year-end - JPMorgan (TLT:NASDAQ)](https://seekingalpha.com/news/4654363-yield-stabilization-could-extend-equity-rally-into-year-end-jpmorgan)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  JPMorgan says stabilizing bond yields could stop equity valuation compression and extend the stock market rally into year-end.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 80.18 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 78.57 (+2.1%), 50d 80.63 (-0.6%), 200d 84.88 (-5.5%); 50d below 200d
Momentum: RSI(14) 56.5 | MACD -0.302 vs signal -0.701 (histogram 0.399)
Returns: 1d +0.9% | 5d +2.3% | 1m -2.0% | 3m -3.9%
52-week range: 77.11 - 92.06 (now 20.5% of the way up)
Volatility: ATR(14) 0.82 (1.0% of price) | annualised 20d 11.8%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Long Government
Yield: 5.0%
Credit quality: AA 100.0% | US government debt 99.6%
Three-year record: +1.8% a year | beta to the market 2.31
Cost and size: expense ratio 0.15% | net assets 46.23B
What it is made of: Bonds 99.6%, Cash 0.4%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: ULTRA UST BOND - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 29.8% of open interest (2,397,995 contracts)
Change on the week: +0.4% of open interest
Crowding: 87% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 109.70M | fund size: 8.80B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Dollar index down 0.61% on the week
- UUP price near 91% of 52‑week high with low volume
- Large speculators net long 4% of open interest, up 2.3% week‑over‑week
- Fund inflows +41.6% over the past month indicating strong demand

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 28.89 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 28.90 (-0.0%), 50d 28.44 (+1.6%), 200d 27.86 (+3.7%); 50d above 200d
Momentum: RSI(14) 55.2 | MACD 0.158 vs signal 0.187 (histogram -0.029)
Returns: 1d -0.4% | 5d -0.4% | 1m +1.4% | 3m +1.6%
52-week range: 26.47 - 29.13 (now 91.1% of the way up)
Volatility: ATR(14) 0.13 (0.4% of price) | annualised 20d 5.5%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Trading--Miscellaneous
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +3.7% a year | beta to the market -11.39
Cost and size: expense ratio 0.75% | net assets 431.14M
What it is made of: Cash 100.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 49.4%
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
Rolled up from the 1 largest holdings, 49.4% of the fund by weight
Ratings by weight: buy n/a | hold n/a | sell n/a (mean n/a on a 1=strong buy to 5=strong sell scale)
Weighted price target: n/a above the current prices
Holdings read: AGPXX
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: USD INDEX - ICE FUTURES U.S. (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 4.0% of open interest (51,816 contracts)
Change on the week: +2.3% of open interest
Crowding: 85% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.3% (1.33M) over 7d | 1 month: +41.6% (126.43M) over 31d
Shares outstanding: 14.90M | fund size: 430.43M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst coverage thin (12% of fund) with 67.6% buy rating and +17.8% price target
- CFTC positioning net short 0.3% of open interest, change -0.4% on week (small reduction)
- Technical indicators mixed: price above 20‑day SMA (+0.6%) but below 50‑day SMA (-2.3%), RSI 49
- Macro data unchanged: inflation 3.7% and rates stable, no surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Vanguard FTSE Europe ETF expected to drop 7-14% amid European stagflation concerns](https://pluang.com/en/news-feed/stagflasi-di-eropa-dan-vgk-turun)  
  <sub>Pluang, 19 hours ago</sub>  
  The Vanguard FTSE Europe ETF (VGK) is predicted to decline by 7-14% due to expected stagflation in Europe, characterized by rising inflation and weak...
- [I Have A View: Stagflation In Europe And VGK Lower Than It Is Now. (NYSEARCA:VGK)](https://seekingalpha.com/article/4955299-stagflation-in-europe-could-drive-vgk-lower-than-it-is-now)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  I expect something similar to inflation stagflation in Europe to pressure the Vanguard FTSE Europe ETF (VGK) below current levels. VGK's risk premium and...
- [ETFs Investing in KONE Oyj Class B Stocks](https://www.tradingview.com/symbols/XETR-KC4/etfs/)  
  <sub>TradingView, 21 hours ago</sub>  
  Explore funds investing in KC4 in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 87.32 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 86.79 (+0.6%), 50d 89.39 (-2.3%), 200d 87.80 (-0.5%); 50d above 200d
Momentum: RSI(14) 49.0 | MACD -0.678 vs signal -0.923 (histogram 0.245)
Returns: 1d +1.0% | 5d +1.2% | 1m -2.1% | 3m -2.0%
52-week range: 77.90 - 93.19 (now 61.6% of the way up)
Volatility: ATR(14) 0.93 (1.1% of price) | annualised 20d 13.9%
Volume: 0.16x the 20-day average
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
Three-year record: +18.1% a year | beta to the market 0.90
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 12.1% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 67.6% | hold 32.4% | sell 0.0% (mean 2.02 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.8% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, SHEL.L, NOVN.SW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 0.3% of open interest (480,891 contracts)
Change on the week: -0.4% of open interest
Crowding: 65% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 282.09M | fund size: 24.63B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst view covers only 23.5% of fund but shows 100% buy rating and +46.4% price target
- CFTC speculators net long 2.8% of open interest, down -1.5% week
- Technicals: price below 20‑day and 50‑day SMA, RSI 40, MACD negative
- Macro: US yields up slightly, dollar down, VIX up; no major surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Better Emerging Markets ETF: Schwab's SCHE vs. Vanguard's VWO](https://www.fool.com/coverage/etfs/2026/10/19/better-emerging-markets-etf-schwab-s-sche-vs-vanguard-s-vwo/)  
  <sub>The Motley Fool, 21 hours ago</sub>  
  The choice between the Schwab Emerging Markets Equity ETF (SCHE -0.08%) and Vanguard FTSE Emerging Markets ETF (VWO +0.00%) centers on portfolio depth,...
- [ETFs Investing in Sany Heavy Industry Co., Ltd. Class H Stocks](https://www.tradingview.com/symbols/GETTEX-1741/etfs/)  
  <sub>TradingView, 21 hours ago</sub>  
  Explore funds investing in 1741 in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 58.39 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 59.44 (-1.8%), 50d 60.01 (-2.7%), 200d 58.29 (+0.2%); 50d above 200d
Momentum: RSI(14) 40.0 | MACD -0.443 vs signal -0.270 (histogram -0.173)
Returns: 1d +0.6% | 5d -2.2% | 1m -4.5% | 3m -0.7%
52-week range: 52.42 - 61.44 (now 66.2% of the way up)
Volatility: ATR(14) 0.64 (1.1% of price) | annualised 20d 14.2%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Diversified Emerging Mkts
What it holds: P/E 16.13 | P/B 2.13 | P/S 1.85 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +17.1% a year | beta to the market 0.75
Cost and size: expense ratio 0.06% | net assets 164.66B
What it is made of: Stocks 95.8%, Cash 4.0%, Other 0.1%, Preferred 0.0%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 15.7%, Tencent Holdings Ltd 2.8%, Alibaba Group Holding Ltd Ordinary Shares 2.1%, MediaTek Inc 1.9%, Delta Electronics Inc 0.9%
Sector mix: Technology 33.8%, Financial services 19.5%, Consumer cyclical 9.3%, Industrials 7.5%
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
Rolled up from the 5 largest holdings, 23.5% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +46.4% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 2308.TW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 2.8% of open interest (1,042,945 contracts)
Change on the week: -1.5% of open interest
Crowding: 33% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 1.42B | fund size: 82.80B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Is Invesco Bloomberg Enhanced Fallen Angels ETF (IFLN) a Strong ETF Right Now?](https://finance.yahoo.com/markets/stocks/articles/invesco-bloomberg-enhanced-fallen-angels-092013395.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Designed to provide broad exposure to the High-Yield/Junk Bond ETFs category of the market, the Invesco Bloomberg Enhanced Fallen Angels ETF (IFLN) is a...
- [Corporate Bonds Flash Warning](https://realmoney.thestreet.com/market-commentary/corporate-bonds-flash-warning)  
  <sub>RealMoney Pro, 34 minutes ago</sub>  
  Quick update on diesel, which continues to be an issue for the economy and bonds: The Russian diesel deal was too small to matter. There's no evidence that...
- [AI’s 2008 Moment: Buy The Debt, Not The Dip](https://seekingalpha.com/article/4955322-ais-2008-moment-buy-the-debt-not-the-dip)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  Buying preferred debt over equity offers a framework for today's AI-driven credit stress. Read about bond ideas for Meta, Oracle and Google.
- [How (JNK) Movements Inform Risk Allocation Models](https://news.stocktradersdaily.com/news_release/52/How_JNK_Movements_Inform_Risk_Allocation_Models_102026052402_1792488242.html)  
  <sub>Stock Traders Daily, 9 hours ago</sub>  
  Price-action only: Spdr Bloomberg High Yield Bond Etf (JNK) movements set the tone for institutional models. How (JNK) Movements Inform Risk Allocation...
- [BGB: Tactical Opportunity With Liquidation Potential (NYSE:BGB)](https://seekingalpha.com/article/4955251-bgb-tactical-opportunity-with-liquidation-potential)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  The Blackstone Strategic Credit 2027 Term Fund offers a floating-rate, high-yield portfolio with a current ~5% discount & ~8% yield. Learn more about BGB...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 76.99 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 77.23 (-0.3%), 50d 78.44 (-1.8%), 200d 79.67 (-3.4%); 50d below 200d
Momentum: RSI(14) 36.7 | MACD -0.427 vs signal -0.468 (histogram 0.041)
Returns: 1d +0.2% | 5d -0.1% | 1m -2.1% | 3m -3.2%
52-week range: 76.81 - 81.28 (now 4.0% of the way up)
Volatility: ATR(14) 0.31 (0.4% of price) | annualised 20d 4.5%
Volume: 0.23x the 20-day average
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
Three-year record: +8.1% a year | beta to the market 0.70
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 195.60M | fund size: 15.06B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; analyst view is bullish but limited to ~38% of the fund, technicals are mixed, and there are no macro surprises or net flow changes.

**Main reasons it gave:**
- Analyst consensus 100% buy on top holdings with +19.5% price target
- Technical picture mixed: price above 20‑day SMA but below 50‑day and 200‑day SMA, RSI 52.2
- Fund flows flat over the past week and month, indicating no net demand shift
- Macro environment unchanged: stable yields, dollar down, VIX modestly higher, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 121.54 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 120.45 (+0.9%), 50d 122.42 (-0.7%), 200d 123.10 (-1.3%); 50d below 200d
Momentum: RSI(14) 52.2 | MACD -0.894 vs signal -1.072 (histogram 0.178)
Returns: 1d +1.5% | 5d +2.4% | 1m -4.8% | 3m +1.6%
52-week range: 98.34 - 137.69 (now 59.0% of the way up)
Volatility: ATR(14) 1.78 (1.5% of price) | annualised 20d 17.3%
Volume: 0.64x the 20-day average
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
Three-year record: +37.0% a year | beta to the market 1.09
Cost and size: expense ratio 0.59% | net assets 874.00M
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 37.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.17 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.5% above the current prices
Holdings read: TEVA, LUMI.TA, POLI.TA, TSEM.TA, ESLT.TA
Recent rating changes among them:
  - TEVA: 2026-10-15 Barclays: main, Overweight -> Overweight
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 2.55M | fund size: 309.93M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Analyst consensus is fully bullish (100% buy, +3.3% price target) while recent fund flows show net outflows of -2.9% over the past month (share count down 1.7% weekly), creating opposing pressures. Technicals are mixed: price sits above the 200‑day SMA and MACD line is above its signal, but price is below the 50‑day SMA and volume is only 0.17× the 20‑day average, offering no decisive breakout. No macro surprise or major news is present. The net effect is a neutral directional call.

**Main reasons it gave:**
- Analyst consensus: 100% buy rating, weighted price target +3.3% above current price
- Fund flows: net outflows of -2.9% over the past month (share count down 1.7% weekly)
- Technicals: price above 200‑day SMA and MACD line above signal, but price below 50‑day SMA and volume at 0.17× 20‑day average

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 44.08 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 44.10 (-0.1%), 50d 44.39 (-0.7%), 200d 40.06 (+10.0%); 50d above 200d
Momentum: RSI(14) 49.1 | MACD -0.036 vs signal -0.058 (histogram 0.022)
Returns: 1d -0.0% | 5d -0.9% | 1m -3.5% | 3m +6.6%
52-week range: 32.56 - 45.76 (now 87.3% of the way up)
Volatility: ATR(14) 0.64 (1.4% of price) | annualised 20d 19.3%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.22 | P/B 2.06 | P/S 1.40 | 3y earnings growth n/a
Yield: 3.3%
Three-year record: +38.8% a year | beta to the market 0.64
Cost and size: expense ratio 0.59% | net assets 833.96M
What it is made of: Stocks 99.1%, Cash 0.9%
Largest holdings: PKO Bank Polski SA 16.2%, Orlen SA 12.7%, Bank Polska Kasa Opieki SA 7.4%, Powszechny Zaklad Ubezpieczen SA 6.0%, Allegro.EU SA Ordinary Shares 4.9%
Sector mix: Financial services 46.9%, Energy 13.3%, Consumer cyclical 13.2%, Basic materials 6.2%
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
Rolled up from the 5 largest holdings, 47.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.18 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +3.3% above the current prices
Holdings read: PKO.WA, PKN.WA, PEO.WA, PZU.WA, ALE.WA
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
Direction: money going out (1 month)
Share count change: 1 week: -1.7% (-14.64M) over 7d | 1 month: -2.9% (-24.50M) over 31d
Shares outstanding: 18.68M | fund size: 823.53M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: mixed analyst view, flat fund flows, solid fundamentals but no macro surprise and modest technicals.

**Main reasons it gave:**
- Analyst rating: 59.5% hold, 40.5% sell; weighted price target -6.6% below current price
- Fund flows flat (0% change) indicating no net demand
- Three‑year record of +14% per year and moderate valuation (P/E 20.31) suggest solid fundamentals
- Technical trend above 20‑day and 50‑day SMA, but low volume and modest momentum (RSI 58, MACD near zero) indicate limited upside

<details><summary><b>News</b> — score +0.00</summary>

- [Why (EWA) Price Action Is Critical for Tactical Trading](https://news.stocktradersdaily.com/news_release/1/Why_EWA_Price_Action_Is_Critical_for_Tactical_Trading_102026021802_1792477082.html)  
  <sub>Stock Traders Daily, 13 hours ago</sub>  
  Key findings for Ishares Msci Australia Etf (NYSE: EWA). Neutral Near and Mid-Term Readings Could Moderate Long-Term Positive Bias...
- [IAF: Trades In Financial Exposure For Consumer Discretionary (NYSE:IAF)](https://seekingalpha.com/article/4955383-iaf-trades-in-financial-exposure-for-consumer-discretionary)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  The abrdn Australia Equity Fund offers a sector shift from financials to consumer discretionary versus EWA. Read why IAF is a Hold.
- [abrdn Australia Equity Fund offers limited sect...](https://pluang.com/en/news-feed/analisis-pergeseran-sektor-iaf-finansial-ke-konsumer-australia)  
  <sub>Pluang, 9 hours ago</sub>  
  The abrdn Australia Equity Fund (IAF) shifts sector exposure from financials to consumer discretionary compared to the EWA ETF, but this change offers...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.23 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 28.51 (+2.5%), 50d 29.20 (+0.1%), 200d 28.78 (+1.6%); 50d above 200d
Momentum: RSI(14) 58.0 | MACD -0.047 vs signal -0.164 (histogram 0.117)
Returns: 1d +1.4% | 5d +1.6% | 1m +0.7% | 3m +1.3%
52-week range: 24.95 - 30.43 (now 78.1% of the way up)
Volatility: ATR(14) 0.33 (1.1% of price) | annualised 20d 14.9%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 20.31 | P/B 2.65 | P/S 3.31 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +14.0% a year | beta to the market 0.98
Cost and size: expense ratio 0.50% | net assets 1.21B
What it is made of: Stocks 99.2%, Cash 0.8%
Largest holdings: BHP Group Ltd 15.4%, Commonwealth Bank of Australia 12.6%, National Australia Bank Ltd 6.1%, Westpac Banking Corp 6.0%, ANZ Group Holdings Ltd 5.8%
Sector mix: Financial services 42.0%, Basic materials 25.4%, Consumer cyclical 6.5%, Healthcare 5.6%
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

<details><summary><b>What analysts and big funds say</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.40</summary>

```text
Rolled up from the 5 largest holdings, 45.9% of the fund by weight
Ratings by weight: buy 0.0% | hold 59.5% | sell 40.5% (mean 3.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -6.6% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 63.60M | fund size: 1.86B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral call based on lack of macro surprise, flat fund flows, modest analyst optimism without rating changes, and technicals showing price above moving averages but low volume.

**Main reasons it gave:**
- Fund flows flat (0% change over 1 week and 1 month)
- No macro surprise; yields stable and VIX modestly up
- Analyst view: 79.8% buy, weighted price target +3.5% above current, no rating changes
- Technicals: price above 20d/50d/200d SMAs, RSI 59.2, MACD positive, but volume 0.16x 20‑day average
- Fundamentals: moderate valuation (P/E 18.94) and strong 3‑year record (+24%/yr) but no new catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [World Markets Watchlist: October 19, 2026](https://www.etftrends.com/china-insights-content-hub/world-markets-watchlist-october-19-2026/)  
  <sub>ETF Trends, 17 hours ago</sub>  
  Our global markets watchlist tracks nine prominent indexes from economies around the world. The list includes the S&P 500 from the U.S..

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.10</summary>

```text
Last close 60.99 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 59.31 (+2.8%), 50d 60.56 (+0.7%), 200d 58.05 (+5.0%); 50d above 200d
Momentum: RSI(14) 59.2 | MACD 0.045 vs signal -0.249 (histogram 0.294)
Returns: 1d +1.2% | 5d +1.8% | 1m +0.9% | 3m +2.9%
52-week range: 49.72 - 62.64 (now 87.2% of the way up)
Volatility: ATR(14) 0.71 (1.2% of price) | annualised 20d 16.2%
Volume: 0.16x the 20-day average
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
Three-year record: +24.0% a year | beta to the market 0.80
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
Ratings by weight: buy 79.8% | hold 20.2% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +3.5% above the current prices
Holdings read: RY, TD, SHOP, BMO.TO, BNS.TO
Recent rating changes among them:
  - RY: 2025-08-29 Argus Research: main, Buy -> Buy
  - TD: 2026-06-01 RBC Capital: main, Outperform -> Outperform
  - SHOP: 2026-10-16 RBC Capital: main, Outperform -> Outperform
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 94.80M | fund size: 5.78B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, flat fund flows, modest technical signals, and positive but limited analyst coverage lead to a neutral stance.

**Main reasons it gave:**
- Analyst view: 81.7% buy rating for 28.9% of fund, weighted price target +13.6% above current
- Fund flows flat (0% change) indicating no net inflow or outflow
- Technicals: price just above 20‑day SMA, RSI 51, MACD near zero, low volume
- Macro: yields down modestly, VIX up modestly, no policy or data surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 51.13 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 50.64 (+1.0%), 50d 51.83 (-1.4%), 200d 51.49 (-0.7%); 50d above 200d
Momentum: RSI(14) 51.0 | MACD -0.178 vs signal -0.336 (histogram 0.157)
Returns: 1d +0.5% | 5d -0.1% | 1m -1.2% | 3m +1.7%
52-week range: 45.38 - 54.72 (now 61.6% of the way up)
Volatility: ATR(14) 0.69 (1.3% of price) | annualised 20d 15.0%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.64 | P/B 2.82 | P/S 2.83 | 3y earnings growth n/a
Yield: 3.6%
Three-year record: +18.8% a year | beta to the market 1.25
Cost and size: expense ratio 0.51% | net assets 947.21M
What it is made of: Stocks 99.1%, Cash 0.9%
Largest holdings: Spotify Technology SA 9.7%, Investor AB Class B 9.6%, Atlas Copco AB Class A 7.1%, Volvo AB Class B 6.8%, Sandvik AB 5.3%
Sector mix: Industrials 46.3%, Financial services 25.6%, Communication services 13.5%, Technology 6.1%
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
Rolled up from the 4 largest holdings, 28.9% of the fund by weight
Ratings by weight: buy 81.7% | hold 18.3% | sell 0.0% (mean 2.01 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.6% above the current prices
Holdings read: SPOT, ATCO-A.ST, VOLV-B.ST, SAND.ST
Recent rating changes among them:
  - SPOT: 2026-10-20 Rosenblatt: main, Neutral -> Neutral
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 7.65M | fund size: 391.14M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, modest bullish analyst view and fundamentals, but technicals lack a decisive break.

**Main reasons it gave:**
- Analyst view: 78.7% buy rating and +19.1% price target
- Fund flows: flat share count change (0% week, 0% month)
- Technicals: price just above 20‑day SMA (+0.1%) but below 50‑day and 200‑day SMAs, low volume
- Macro: no surprise data; yields stable, dollar down, VIX modestly higher
- Fundamentals: strong 3‑year record (+19.4% per year) with moderate valuation (P/E 17.6)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 41.40 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 41.37 (+0.1%), 50d 42.68 (-3.0%), 200d 42.31 (-2.1%); 50d above 200d
Momentum: RSI(14) 46.4 | MACD -0.366 vs signal -0.455 (histogram 0.089)
Returns: 1d +0.9% | 5d +0.5% | 1m -2.8% | 3m +0.2%
52-week range: 38.08 - 44.59 (now 51.1% of the way up)
Volatility: ATR(14) 0.50 (1.2% of price) | annualised 20d 15.2%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.64 | P/B 1.86 | P/S 1.23 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +19.4% a year | beta to the market 0.98
Cost and size: expense ratio 0.49% | net assets 1.47B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Siemens AG 12.1%, SAP SE 11.5%, Allianz SE 9.6%, Siemens Energy AG Ordinary Shares 6.7%, Deutsche Telekom AG 5.4%
Sector mix: Industrials 28.9%, Financial services 22.9%, Technology 16.4%, Healthcare 7.2%
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
Rolled up from the 5 largest holdings, 45.4% of the fund by weight
Ratings by weight: buy 78.7% | hold 21.3% | sell 0.0% (mean 1.92 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.1% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 79.50M | fund size: 3.29B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, flat fund flows, bearish technicals, but strong analyst consensus and moderate fundamentals.

**Main reasons it gave:**
- Analyst consensus 100% buy with +21.5% price target
- Fund flows flat (0% change week/month)
- Technical indicators bearish: price below 20‑day, 50‑day, 200‑day SMAs, RSI 35, low volume
- Macro backdrop unchanged: yields stable, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 55.98 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 57.53 (-2.7%), 50d 60.22 (-7.0%), 200d 58.13 (-3.7%); 50d above 200d
Momentum: RSI(14) 35.0 | MACD -1.269 vs signal -1.239 (histogram -0.029)
Returns: 1d +1.1% | 5d -1.2% | 1m -8.6% | 3m -8.3%
52-week range: 50.66 - 63.35 (now 41.9% of the way up)
Volatility: ATR(14) 0.81 (1.4% of price) | annualised 20d 17.8%
Volume: 0.14x the 20-day average
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
Three-year record: +27.1% a year | beta to the market 0.88
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
Weighted price target: +21.5% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 8.55M | fund size: 478.63M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: Fed policy unchanged and inflation within expectations
- Technical indicators mixed: price below 20‑day and 50‑day SMAs but above 200‑day SMA, RSI 44.3, MACD negative
- Positioning shows small net short (2.4% of OI) with low crowding (15th percentile) and modest increase (+5.8%)
- Analyst coverage thin (17% of fund) despite 100% buy rating and +25% price target

<details><summary><b>News</b> — score +0.00</summary>

- [Form 4 iShares MSCI Japan ETF For: 20 October By Investing.com](https://ca.investing.com/news/stock-market-news/form-4-ishares-msci-japan-etf-for-20-october-93CH-4889731)  
  <sub>Investing.com Canada, 8 hours ago</sub>  
  Filed Pursuant to Rule 424(b)(2). Registration No. 333-289203. Pricing Supplement dated October 16, 2026. (To Equity Index Underlying Supplement dated July...
- [Asia Markets Roundup (Japan Yen, India Equities, Nidec, Malaysia AI Exports)](https://www.heygotrade.com/en/news/asia-markets-roundup-japan-yen-india-equities-nidec-malaysia-ai-exports/)  
  <sub>Gotrade, 23 hours ago</sub>  
  Gotrade News - Asian markets opened the week mixed on Monday, October 19, 2026, as Nidec sank to a decade low on an accounting-liability report, India's.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 95.70 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 97.07 (-1.4%), 50d 96.88 (-1.2%), 200d 91.36 (+4.8%); 50d above 200d
Momentum: RSI(14) 44.3 | MACD -0.373 vs signal 0.006 (histogram -0.379)
Returns: 1d +0.8% | 5d -1.7% | 1m -2.3% | 3m +3.8%
52-week range: 79.49 - 99.32 (now 81.8% of the way up)
Volatility: ATR(14) 1.29 (1.3% of price) | annualised 20d 16.4%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Japan Stock
What it holds: P/E 15.27 | P/B 1.98 | P/S 1.37 | 3y earnings growth n/a
Yield: 3.7%
Three-year record: +20.1% a year | beta to the market 0.83
Cost and size: expense ratio 0.49% | net assets 23.53B
What it is made of: Stocks 99.1%, Cash 0.9%
Largest holdings: Mitsubishi UFJ Financial Group Inc 4.7%, Toyota Motor Corp 3.3%, Tokyo Electron Ltd 3.1%, Sumitomo Mitsui Financial Group Inc 3.0%, Advantest Corp 3.0%
Sector mix: Industrials 22.8%, Technology 22.0%, Financial services 19.3%, Consumer cyclical 11.1%
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
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.0% above the current prices
Holdings read: 8306.T, 7203.T, 8035.T, 8316.T, 6857.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 2.4% of open interest (23,701 contracts)
Change on the week: +5.8% of open interest
Crowding: 15% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 227.85M | fund size: 21.81B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, flat fund flows, modest analyst bullishness but no decisive technical break on strong volume.

**Main reasons it gave:**
- Analyst coverage: 64.8% buy, weighted price target +4% above current price
- Technicals: price above 20‑day, 50‑day, 200‑day SMAs; RSI 66.9; MACD positive; volume 0.46× 20‑day average
- Fund flows flat over the past month, indicating no net demand shift
- Macro: modest yield declines, dollar down, VIX modestly higher; no surprise data

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 62.83 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 60.25 (+4.3%), 50d 61.58 (+2.0%), 200d 61.66 (+1.9%); 50d below 200d
Momentum: RSI(14) 66.9 | MACD 0.199 vs signal -0.275 (histogram 0.474)
Returns: 1d +1.3% | 5d +4.9% | 1m +3.3% | 3m +0.7%
52-week range: 55.06 - 65.08 (now 77.6% of the way up)
Volatility: ATR(14) 0.69 (1.1% of price) | annualised 20d 14.4%
Volume: 0.46x the 20-day average
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
Three-year record: +14.3% a year | beta to the market 0.91
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 48.2% of the fund by weight
Ratings by weight: buy 64.8% | hold 35.2% | sell 0.0% (mean 2.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.0% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 28.62M | fund size: 1.80B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error waiting for selector "#main" failed: timeout 30000ms exceeded)

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals not decisive, flows flat, analyst view bullish but limited coverage.

**Main reasons it gave:**
- No macro news or data surprise in the past 24h
- Price below 20-day and 50-day SMAs, RSI 39.1, MACD negative
- Fund flows flat (share count unchanged week-to-week)
- Analyst ratings 100% buy for top 5 holdings covering 46.7% of fund

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 65.12 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 66.70 (-2.4%), 50d 67.89 (-4.1%), 200d 64.87 (+0.4%); 50d above 200d
Momentum: RSI(14) 39.1 | MACD -0.789 vs signal -0.589 (histogram -0.200)
Returns: 1d +0.6% | 5d -1.4% | 1m -4.0% | 3m -4.5%
52-week range: 55.33 - 71.61 (now 60.1% of the way up)
Volatility: ATR(14) 0.93 (1.4% of price) | annualised 20d 16.8%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.85 | P/B 2.55 | P/S 1.87 | 3y earnings growth n/a
Yield: 4.2%
Three-year record: +23.2% a year | beta to the market 1.09
Cost and size: expense ratio 0.50% | net assets 710.44M
What it is made of: Stocks 98.9%, Cash 1.1%
Largest holdings: ASML Holding NV 23.6%, ING Groep NV 9.1%, Nebius Group NV Shs Class-A- 4.9%, Prosus NV Ordinary Shares - Class N 4.6%, ASM International NV 4.4%
Sector mix: Technology 33.4%, Financial services 21.5%, Consumer defensive 10.4%, Industrials 9.6%
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
Rolled up from the 5 largest holdings, 46.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.58 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +44.1% above the current prices
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 5.55M | fund size: 361.42M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, modest analyst bullishness, and technicals lacking decisive break.

**Main reasons it gave:**
- Analyst coverage: 51.5% buy, 48.5% hold, weighted price target +8% (moderate bullish bias)
- Fund flows flat: share count unchanged (+0.0% week, +0.0% month)
- Technicals: price below 20‑day SMA (-1.2%), RSI 41.7 (neutral), volume 0.15× 20‑day average
- Macro: Treasury yields fell modestly, VIX rose to 17.6 (no major surprise)

<details><summary><b>News</b> — score +0.00</summary>

- [西班牙ETF-iShares MSCI收跌1.61%，成交额1000.34万美元](https://finance.sina.com.cn/stock/usstock/notice/2026-10-20/doc-inivvhfv7574863.shtml)  
  <sub>新浪财经, 18 hours ago</sub>  
  10月20日，西班牙ETF-iShares MSCI（EWP）收跌1.61%，报57.33美元，成交额1000.34万美元，市值19.99亿美元。行情数据• 开盘价：57.53美元• 最高价：57.7.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 58.10 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 58.79 (-1.2%), 50d 60.79 (-4.4%), 200d 57.86 (+0.4%); 50d above 200d
Momentum: RSI(14) 41.7 | MACD -0.830 vs signal -0.853 (histogram 0.023)
Returns: 1d +1.3% | 5d -0.4% | 1m -5.4% | 3m -3.4%
52-week range: 49.21 - 63.23 (now 63.4% of the way up)
Volatility: ATR(14) 0.81 (1.4% of price) | annualised 20d 17.1%
Volume: 0.15x the 20-day average
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
Three-year record: +33.1% a year | beta to the market 0.88
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
Weighted price target: +8.0% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 37.35M | fund size: 2.17B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, technicals show weak momentum, analyst view bullish but limited coverage, flows flat.

**Main reasons it gave:**
- Technicals: price below 20-day SMA and RSI 39.8, MACD negative (weak momentum)
- Analyst coverage: 100% buy rating but only 39.1% of fund weight
- Fund flows: flat share count over past month (no net inflows/outflows)
- Macro: no policy surprise; yields stable, dollar down, VIX modestly higher

<details><summary><b>News</b> — score +0.00</summary>

- [Taiwan's Stock Pickers Are Walking Out to Bet Their Own Money](https://www.theglobeandmail.com/investing/markets/stocks/UMC-N/pressreleases/8203888/taiwan-s-stock-pickers-are-walking-out-to-bet-their-own-money/)  
  <sub>The Globe and Mail, 22 hours ago</sub>  
  Detailed price information for United Microelectronics Corp ADR (UMC-N) from The Globe and Mail including charting and trades.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 107.51 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 112.95 (-4.8%), 50d 110.17 (-2.4%), 200d 91.74 (+17.2%); 50d above 200d
Momentum: RSI(14) 39.8 | MACD -0.584 vs signal 0.642 (histogram -1.227)
Returns: 1d +0.2% | 5d -5.2% | 1m -7.0% | 3m +5.7%
52-week range: 60.03 - 118.00 (now 81.9% of the way up)
Volatility: ATR(14) 2.33 (2.2% of price) | annualised 20d 24.0%
Volume: 0.34x the 20-day average
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
Three-year record: +41.4% a year | beta to the market 1.26
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 39.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.35 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +41.4% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 85.00M | fund size: 9.14B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, modest bullish technicals on low volume, flat fund flows, and mixed but generally positive fundamentals and analyst coverage.

**Main reasons it gave:**
- US Treasury yields modestly lower (10-yr -0.14% week-over-week)
- Dollar index fell 0.61% on the week, supporting MXN exposure
- Technical indicators bullish (RSI 62.5, MACD positive) but volume low (0.38x 20-day avg)
- Analyst view: 90.9% buy rating on 47.8% of fund, price target +4.9% above current
- Fund flows flat (share count unchanged over week and month)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 76.09 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 72.75 (+4.6%), 50d 74.51 (+2.1%), 200d 76.01 (+0.1%); 50d below 200d
Momentum: RSI(14) 62.5 | MACD 0.168 vs signal -0.411 (histogram 0.579)
Returns: 1d +1.0% | 5d +3.9% | 1m +3.2% | 3m -0.8%
52-week range: 65.07 - 81.23 (now 68.2% of the way up)
Volatility: ATR(14) 1.27 (1.7% of price) | annualised 20d 19.7%
Volume: 0.38x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Focused Region
What it holds: P/E 12.17 | P/B 1.90 | P/S 1.42 | 3y earnings growth n/a
Yield: 3.5%
Three-year record: +14.3% a year | beta to the market 1.07
Cost and size: expense ratio 0.50% | net assets 1.49B
What it is made of: Stocks 99.4%, Cash 0.6%
Largest holdings: Grupo Mexico SAB de CV Class B 16.4%, Grupo Financiero Banorte SAB de CV Class O 11.1%, Fomento Economico Mexicano SAB de CV Units Cons. Of 1 Shs-B- And 4 Shs-D- 8.8%, America Movil SAB de CV Ordinary Shares - Class B 7.2%, Wal - Mart de Mexico SAB de CV 4.4%
Sector mix: Basic materials 26.8%, Consumer defensive 24.8%, Financial services 19.5%, Industrials 12.1%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 47.8% of the fund by weight
Ratings by weight: buy 90.9% | hold 9.1% | sell 0.0% (mean 2.15 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.9% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 18.90M | fund size: 1.44B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no material macro surprise, flat fund flows, no analyst rating, technicals bearish but not decisive, fundamentals mixed.

**Main reasons it gave:**
- Fund flows flat with no net inflow or outflow over the past month
- Analyst view provides no rating or price target for the top holdings
- Technical indicators show price below 20‑day and 50‑day SMAs, RSI 34.3, indicating bearish momentum but no decisive break on heavy volume
- Fundamentals show low P/E 10.41 and strong 3‑year record (+39.9%/yr) but high beta 2.48, suggesting mixed outlook

<details><summary><b>News</b> — score +0.00</summary>

- [Ishares Msci South Korea ETF (Derivatives) Price (EWY/USD) Today | Live Price, Market Cap & Chart](https://www.binance.com/en/price/ishares-msci-south-korea-etf-derivatives)  
  <sub>Binance, 20 hours ago</sub>  
  The current price of Ishares Msci South Korea ETF (Derivatives) (EWY) is $157.26. Top cryptocurrency prices are updated in real-time on Binance's price...
- [Samsung Appears to Be a Good Bet Ahead of Q3: ETFs in Focus](https://www.tradingview.com/news/zacks:97396f452094b:0-samsung-appears-to-be-a-good-bet-ahead-of-q3-etfs-in-focus/)  
  <sub>TradingView, 23 hours ago</sub>  
  Samsung Electronics projects optimistic third-quarter earnings of 2026, helped by growth in memory chips. This highlights how surging artificial...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 155.24 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 175.84 (-11.7%), 50d 178.61 (-13.1%), 200d 160.74 (-3.4%); 50d above 200d
Momentum: RSI(14) 34.3 | MACD -7.147 vs signal -3.807 (histogram -3.340)
Returns: 1d -0.9% | 5d -6.8% | 1m -17.9% | 3m -8.9%
52-week range: 88.53 - 219.20 (now 51.1% of the way up)
Volatility: ATR(14) 6.41 (4.1% of price) | annualised 20d 40.7%
Volume: 0.37x the 20-day average
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
Three-year record: +39.9% a year | beta to the market 2.48
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 75.60M | fund size: 11.74B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, flat fund flows, price near 52‑week high with low volume, and fundamentals are solid but lack a clear catalyst. Analyst view is bullish but covers only ~40% of the fund, so overall call remains neutral.

**Main reasons it gave:**
- Fund flows flat: 0% share count change over 7d and 31d
- Technicals: price near 52‑week high (95.5% of range) with low volume (0.62× 20‑day avg)
- Macro: US dollar down 0.61% on week, US yields fell modestly, no surprise data
- Fundamentals: low valuation (P/E 10.73) but no clear macro catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [Form 4 iShares MSCI Brazil ETF For: 20 October By Investing.com](https://ca.investing.com/news/stock-market-news/form-4-ishares-msci-brazil-etf-for-20-october-93CH-4891299)  
  <sub>Investing.com Canada, 29 minutes ago</sub>  
  The information in this preliminary pricing supplement is not complete and may be changed. This preliminary pricing supplement and the accompanying product...
- [Long EWZ: Low Valuation, Resilient Winner (NYSEARCA:EWZ)](https://seekingalpha.com/article/4955292-long-ewz-low-valuation-resilient-winner)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Bullish on iShares MSCI Brazil ETF (EWZ): low valuations, rate cuts, and commodity tailwinds plus 4% USD yield.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 42.93 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 40.41 (+6.2%), 50d 37.95 (+13.1%), 200d 37.04 (+15.9%); 50d above 200d
Momentum: RSI(14) 66.6 | MACD 1.408 vs signal 1.393 (histogram 0.015)
Returns: 1d +2.4% | 5d +0.1% | 1m +12.8% | 3m +17.2%
52-week range: 29.94 - 43.54 (now 95.5% of the way up)
Volatility: ATR(14) 1.01 (2.3% of price) | annualised 20d 50.8%
Volume: 0.62x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.73 | P/B 1.84 | P/S 1.40 | 3y earnings growth n/a
Yield: 3.9%
Three-year record: +17.4% a year | beta to the market 0.83
Cost and size: expense ratio 0.59% | net assets 8.64B
What it is made of: Stocks 97.5%, Cash 2.0%, Preferred 0.5%
Largest holdings: Vale SA 8.9%, Itau Unibanco Holding SA Participating Preferred 8.4%, Nu Holdings Ltd Ordinary Shares Class A 8.1%, Petroleo Brasileiro SA Petrobras Participating Preferred 7.5%, Petroleo Brasileiro SA Petrobras 7.0%
Sector mix: Financial services 34.4%, Energy 18.1%, Basic materials 13.0%, Utilities 12.8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.83 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.9% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 200.55M | fund size: 8.61B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, mixed technicals, flat flows, limited analyst coverage despite bullish rating

**Main reasons it gave:**
- No macro surprise in recent data releases (inflation, unemployment, jobless claims in line with expectations)
- Technical indicators mixed: price above 20‑day SMA but below 50‑day and 200‑day SMA, RSI neutral at 50.7, MACD near zero
- Fund flows flat over the past week and month (0% change in share count)
- Analyst coverage limited to 43.4% of the fund despite bullish rating and +31% price target

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 65.50 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 64.28 (+1.9%), 50d 67.58 (-3.1%), 200d 68.87 (-4.9%); 50d below 200d
Momentum: RSI(14) 50.7 | MACD -0.736 vs signal -1.089 (histogram 0.353)
Returns: 1d +1.4% | 5d +1.8% | 1m -4.0% | 3m +4.0%
52-week range: 60.43 - 81.60 (now 23.9% of the way up)
Volatility: ATR(14) 1.23 (1.9% of price) | annualised 20d 26.5%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.44 | P/B 2.00 | P/S 1.73 | 3y earnings growth n/a
Yield: 7.9%
Three-year record: +25.3% a year | beta to the market 1.07
Cost and size: expense ratio 0.59% | net assets 473.79M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Anglogold Ashanti PLC 12.7%, Gold Fields Ltd 8.7%, Naspers Ltd Class N 8.4%, Firstrand Ltd 7.4%, Standard Bank Group Ltd 6.2%
Sector mix: Basic materials 39.1%, Financial services 34.4%, Consumer cyclical 12.8%, Communication services 6.4%
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
Rolled up from the 5 largest holdings, 43.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.00 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +31.0% above the current prices
Holdings read: AU, GFI.JO, NPN.JO, FSR.JO, SBK.JO
Recent rating changes among them:
  - AU: 2026-10-15 Goldman Sachs: init, ? -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 7.90M | fund size: 517.45M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, technicals ambiguous, fund outflows but not decisive, analyst view bullish but limited coverage, macro signals mixed.

**Main reasons it gave:**
- 10-year yield down 14 bps this week
- Dollar index down 0.61% this week
- Fund outflows: -8.9% over past month
- Analyst consensus: 100% buy, price target +16.4% above current
- Price below 20-day SMA; MACD histogram +0.071; volume 0.25x 20-day avg

<details><summary><b>News</b> — score +0.00</summary>

- [VanEck Gold Miners ETF (ASX:GDX): A 68-Company Gold and Silver Miner Portfolio Led by Newmont and Agnico Eagle](https://kalkine.com.au/news/mutual-funds-etfs/vaneck-gold-miners-etf-asxgdx-a-68-company-gold-and-silver-miner-portfolio-led-by-newmont-and-agnico-eagle)  
  <sub>Kalkine, 4 hours ago</sub>  
  VanEck Gold Miners ETF (ASX:GDX): A 68-Company Gold and Silver Miner Portfolio Led by Newmont and Agnico Eagle.
- [(GDX) Risk Channels and Responsive Allocation](https://news.stocktradersdaily.com/news_release/150/GDX_Risk_Channels_and_Responsive_Allocation_102026032601_1792481161.html)  
  <sub>Stock Traders Daily, 12 hours ago</sub>  
  Price-action only: Vaneck Gold Miners Etf (GDX) movements set the tone for institutional models. (GDX) Risk Channels and Responsive Allocation.
- [Gold Edges Down In Dotcom 2.0 Crash](https://www.canadianminingreport.com/news/custom/gold-edges-down-in-dotcom-2-0-crash)  
  <sub>Canadian Mining Report, 19 hours ago</sub>  
  Looks at gold's declines, the dotcom 2.0 AI stock crash, US CPI, PPI Inflation, major market, sectors and metals price performance, large AI, chip stocks...
- [VanEck Morningstar Wide Moat ETF (ASX:MOAT): 58 US Companies Selected for Competitive Advantages](https://kalkine.com.au/news/mutual-funds-etfs/vaneck-morningstar-wide-moat-etf-asxmoat-58-us-companies-selected-for-competitive-advantages)  
  <sub>Kalkine, 4 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Discipline and Rules-Based Execution in GDXJ Response](https://news.stocktradersdaily.com/news_release/151/Discipline_and_Rules-Based_Execution_in_GDXJ_Response_102026032801_1792481281.html)  
  <sub>Stock Traders Daily, 12 hours ago</sub>  
  Price-action only: Vaneck Junior Gold Miners Etf (GDXJ) movements set the tone for institutional models. Discipline and Rules-Based Execution in GDXJ...
- [Stock Market Today: Nasdaq 100 Rises as AI Chip Rout Reverses, SanDisk Jumps 7%](https://www.tradingview.com/news/benzinga:e9b29a8b4094b:0-stock-market-today-nasdaq-100-rises-as-ai-chip-rout-reverses-sandisk-jumps-7/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks diverged at midday Monday as a rebound in AI chip and infrastructure names lifted the Nasdaq 100 by 1.7% and the S&P 500 by 0.7%, while the Dow...
- [Global X Semiconductor ETF (ASX:SEMI): A 31-Company Chip Portfolio Led by Micron, NVIDIA and TSMC](https://kalkine.com.au/news/mutual-funds-etfs/global-x-semiconductor-etf-asxsemi-a-31-company-chip-portfolio-led-by-micron-nvidia-and-tsmc)  
  <sub>Kalkine, 4 hours ago</sub>  
  Global X Semiconductor ETF (ASX:SEMI): A 31-Company Chip Portfolio Led by Micron, NVIDIA and TSMC.
- [Vanguard Global Aggregate Bond Index (Hedged) ETF (ASX:VBND): A 14,718-Security Bond Portfolio at a 0.20% Fee](https://kalkine.com.au/news/mutual-funds-etfs/vanguard-global-aggregate-bond-index-hedged-etf-asxvbnd-a-14718-security-bond-portfolio-at-a-020-fee)  
  <sub>Kalkine, 4 hours ago</sub>  
  Vanguard Global Aggregate Bond Index (Hedged) ETF (ASX:VBND): A 14718-Security Bond Portfolio at a 0.20% Fee.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 87.62 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 88.16 (-0.6%), 50d 93.31 (-6.1%), 200d 91.07 (-3.8%); 50d above 200d
Momentum: RSI(14) 46.6 | MACD -1.643 vs signal -1.715 (histogram 0.071)
Returns: 1d +1.3% | 5d +0.4% | 1m -7.2% | 3m +14.3%
52-week range: 68.28 - 115.84 (now 40.7% of the way up)
Volatility: ATR(14) 2.95 (3.4% of price) | annualised 20d 39.6%
Volume: 0.25x the 20-day average
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
Three-year record: +46.3% a year | beta to the market 0.81
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 40.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.4% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, FNV.TO
Recent rating changes among them:
  - NEM: 2026-10-19 Barclays: main, Overweight -> Overweight
  - AEM.TO: 2026-10-19 Barclays: main, Overweight -> Overweight
  - ABX.TO: 2026-10-16 CIBC: down, Outperformer -> Neutral
  - WPM.TO: 2026-10-08 UBS: main, Buy -> Buy
  - FNV.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
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
Direction: money going out (1 month)
Share count change: 1 week: +1.5% (398.20M) over 7d | 1 month: -8.9% (-2.56B) over 31d
Shares outstanding: 299.57M | fund size: 26.25B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals lack decisive break, fund flows flat, analyst view bullish but not enough to outweigh neutral macro and technicals.

**Main reasons it gave:**
- Analyst consensus 100% buy with +21.6% price target
- Fund flows flat with no net share creation or redemption
- Technical: price below 20‑day SMA, MACD below signal, low volume
- Macro: yields down modestly, no policy surprise, VIX elevated

<details><summary><b>News</b> — score +0.00</summary>

- [AI’s Great Rotation: When Users Beat Builders](https://etfdb.com/equity-etf-content-hub/ai-great-rotation-when-users-beat-builders/)  
  <sub>ETF Database, 1 hour ago</sub>  
  The past quarter brought shifts in market sentiment and ETF trends. Within equities, the most striking reversal occurred inside the AI trade.
- [What iShares Expanded Tech-Software (IGV) Sold: Palantir Leads on Friday](https://finance.yahoo.com/markets/stocks/articles/ishares-expanded-tech-software-igv-110421783.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. iShares Expanded Tech-Software Sector ETF (IGV) reported $746.5 million in gross ETF activity last Friday,...
- [IGV 261023 111.00C (IGV261023C111000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/IGV261023C111000-US)  
  <sub>Moomoo, 23 hours ago</sub>  
  Track real-time IGV 261023 111.00C (IGV261023C111000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [ETFs Are Net Sellers of Palo Alto Networks (PANW) on Oct. 16](https://www.gurufocus.com/news/9131246/etfs-are-net-sellers-of-palo-alto-networks-panw-on-oct-16)  
  <sub>GuruFocus, 5 hours ago</sub>  
  ETF flows showed net selling of $87.4 million in Palo Alto Networks (PANW) last Friday, even though more funds traded the other way in smaller amounts.
- [4 Stocks With Demand So Sticky That the AI Sell-Off Barely Touched Them at All](https://www.inkl.com/news/4-stocks-with-demand-so-sticky-that-the-ai-sell-off-barely-touched-them-at-all)  
  <sub>inkl, 4 hours ago</sub>  
  AI hardware stocks slid on demand fears, but Chaikin Analytics says sticky-demand software and chip names like Palantir, ServiceNow, CrowdStrike and…
- [PLTR, CRM Stocks Can't Stop Sliding While Chip Stocks Shine: Wall Street Isn't Writing Them Off Yet](https://stocktwits.com/news-articles/markets/equity/pltr-crm-stocks-can-t-stop-sliding-while-chip-stocks-shine-wall-street-isn-t-writing-them-off-yet/cZKvnFGR79L)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Retail traders say institutional investors are selling software to invest in chip stocks, which have been rallying hard.
- [ETFs Are Net Sellers of Palantir (PLTR) on Oct. 16](https://www.gurufocus.com/news/9131237/etfs-are-net-sellers-of-palantir-pltr-on-oct-16)  
  <sub>GuruFocus, 5 hours ago</sub>  
  On Friday, 28 ETFs were buying Palantir (PLTR) shares versus 26 selling, but the sellers moved more money: ETF activity produced a net outflow of $154.1...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 107.19 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 108.25 (-1.0%), 50d 106.01 (+1.1%), 200d 93.75 (+14.3%); 50d above 200d
Momentum: RSI(14) 49.7 | MACD 0.622 vs signal 1.222 (histogram -0.599)
Returns: 1d +1.1% | 5d -3.4% | 1m +0.1% | 3m +20.4%
52-week range: 74.67 - 117.08 (now 76.7% of the way up)
Volatility: ATR(14) 2.79 (2.6% of price) | annualised 20d 28.5%
Volume: 0.20x the 20-day average
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
Three-year record: +13.9% a year | beta to the market 1.22
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 42.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.6% above the current prices
Holdings read: PANW, PLTR, CRWD, MSFT, ORCL
Recent rating changes among them:
  - PANW: 2026-10-15 Citigroup: main, Buy -> Buy
  - PLTR: 2026-10-15 Mizuho: main, Outperform -> Outperform
  - CRWD: 2026-10-16 Keybanc: main, Overweight -> Overweight
  - MSFT: 2026-10-19 Bernstein: main, Outperform -> Outperform
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 12.50M | fund size: 1.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst view (thin coverage), bearish fund outflows, modest fundamentals, and mixed technicals. No material macro surprise or decisive technical break.

**Main reasons it gave:**
- Net outflows of -3.4% in one week and -13.9% in one month
- Analyst coverage thin (23.7% of fund weight) despite 100% buy rating and +29% price target
- Price above 20‑day SMA but below 50‑day and 200‑day SMA
- Fund fundamentals modest: P/E 21.36, expense ratio 0.61%, 3‑year return +2.4% per year

<details><summary><b>News</b> — score +0.00</summary>

- [World Markets Watchlist: October 19, 2026](https://www.etftrends.com/china-insights-content-hub/world-markets-watchlist-october-19-2026/)  
  <sub>ETF Trends, 17 hours ago</sub>  
  Our global markets watchlist tracks nine prominent indexes from economies around the world. The list includes the S&P 500 from the U.S..
- [Asia Markets Roundup (Japan Yen, India Equities, Nidec, Malaysia AI Exports)](https://www.heygotrade.com/en/news/asia-markets-roundup-japan-yen-india-equities-nidec-malaysia-ai-exports/)  
  <sub>Gotrade, 23 hours ago</sub>  
  Gotrade News - Asian markets opened the week mixed on Monday, October 19, 2026, as Nidec sank to a decade low on an accounting-liability report, India's.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 47.84 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 46.98 (+1.8%), 50d 48.31 (-1.0%), 200d 49.44 (-3.2%); 50d below 200d
Momentum: RSI(14) 53.9 | MACD -0.201 vs signal -0.437 (histogram 0.237)
Returns: 1d +0.9% | 5d +1.3% | 1m -1.4% | 3m -0.8%
52-week range: 45.42 - 55.29 (now 24.5% of the way up)
Volatility: ATR(14) 0.52 (1.1% of price) | annualised 20d 15.9%
Volume: 0.40x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.30</summary>

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
Rolled up from the 5 largest holdings, 23.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.35 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +29.1% above the current prices
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
Direction: money going out (1 month)
Share count change: 1 week: -3.4% (-207.14M) over 7d | 1 month: -13.9% (-939.28M) over 31d
Shares outstanding: 122.02M | fund size: 5.84B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Fund flows flat (0% change), technicals mixed, macro data unchanged, analyst view bullish but limited coverage

**Main reasons it gave:**
- Fund flows flat: 0% share count change over 1 week and 1 month
- Technicals mixed: price above 20‑day SMA (+1.3%) but below 50‑day SMA (-2.1%) and 200‑day SMA (-1.0%)
- Macro data unchanged: yields down modestly, VIX up 2.4 points, inflation 3.7% above Fed target
- Analyst coverage bullish (+26.9% price target) but only covers 51.6% of fund

<details><summary><b>News</b> — score +0.00</summary>

- [United Brings Meal Preorders to 420 More Flights Ahead of Earnings](https://www.benzinga.com/markets/large-cap/26/10/62443620/united-brings-meal-preorders-to-420-more-flights-ahead-of-earnings)  
  <sub>Benzinga, 23 hours ago</sub>  
  United Airlines slid after adding 420 daily flights to meal preorders, ahead of Q3 EPS seen at 2.59 vs 2.78 YoY.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 80.73 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 79.66 (+1.3%), 50d 82.48 (-2.1%), 200d 81.55 (-1.0%); 50d above 200d
Momentum: RSI(14) 50.8 | MACD -0.515 vs signal -0.805 (histogram 0.289)
Returns: 1d +1.7% | 5d +1.1% | 1m +1.1% | 3m -8.2%
52-week range: 68.14 - 90.01 (now 57.6% of the way up)
Volatility: ATR(14) 1.20 (1.5% of price) | annualised 20d 15.0%
Volume: 0.18x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 51.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.9% above the current prices
Holdings read: UNP, UBER, CSX, DAL, UAL
Recent rating changes among them:
  - UNP: 2026-10-07 Citigroup: main, Buy -> Buy
  - UBER: 2026-10-16 Guggenheim: reit, Buy -> Buy
  - CSX: 2026-10-07 Citigroup: main, Neutral -> Neutral
  - DAL: 2026-10-12 UBS: main, Buy -> Buy
  - UAL: 2026-10-16 UBS: main, Buy -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 2.80M | fund size: 226.04M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: modest bullish analyst view (thin coverage, +10.9% price target) is offset by net outflows and a weak banking sector, while fundamentals and macro data show no clear catalyst.

**Main reasons it gave:**
- Bank sector on longest losing streak since 2008 (KBE down 8.6%)
- Fund flows show net outflows of -1.1% weekly and -3.2% monthly
- Analyst coverage thin (5.7% of fund) but weighted price target +10.9% bullish
- Technical indicators neutral: RSI 51.5, price near 20‑day SMA, no decisive break

<details><summary><b>News</b> — score +0.00</summary>

- [(KRE) Movement as an Input in Quant Signal Sets](https://news.stocktradersdaily.com/news_release/151/KRE_Movement_as_an_Input_in_Quant_Signal_Sets_102026055201_1792489921.html)  
  <sub>Stock Traders Daily, 9 hours ago</sub>  
  Key findings for Spdr S&p Regional Banking Etf (NYSE: KRE). Neutral Near and Mid-Term Readings Could Moderate Long-Term Positive Bias...
- [Bank Stocks Log Longest Losing Streak Since 2008 - Bank of America (NYSE:BAC)](https://www.benzinga.com/markets/equities/26/10/62463829/bank-stocks-longest-losing-streak-since-2008-kbw-nasdaq-bank-index)  
  <sub>Benzinga, 2 hours ago</sub>  
  The KBW Nasdaq Bank Index, which tracks 24 of the largest U.S. lenders, has fallen for six straight weeks — its longest losing run since July 2008.
- [Banks are the most sold-off since the financial crisis](https://seekingalpha.com/news/4654263-banks-are-the-most-sold-off-since-the-financial-crisis)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  Bank stocks slide for 6 straight weeks as KBE drops 8.6%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 70.99 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 69.92 (+1.5%), 50d 72.70 (-2.4%), 200d 70.78 (+0.3%); 50d above 200d
Momentum: RSI(14) 51.5 | MACD -0.807 vs signal -1.050 (histogram 0.243)
Returns: 1d +2.5% | 5d +2.8% | 1m -1.4% | 3m -6.1%
52-week range: 58.63 - 77.93 (now 64.0% of the way up)
Volatility: ATR(14) 1.27 (1.8% of price) | annualised 20d 18.1%
Volume: 0.47x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Financial
What it holds: P/E 12.02 | P/B 1.21 | P/S 3.59 | 3y earnings growth n/a
Yield: 2.3%
Three-year record: +22.2% a year | beta to the market 1.04
Cost and size: expense ratio 0.35% | net assets 3.73B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: United Bankshares Inc 1.1%, First Interstate BancSystem Inc 1.1%, Old National Bancorp 1.1%, Hancock Whitney Corp 1.1%, East West Bancorp Inc 1.1%
Sector mix: Financial services 100.0%
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
Rolled up from the 5 largest holdings, 5.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 59.8% | hold 40.2% | sell 0.0% (mean 2.24 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.9% above the current prices
Holdings read: UBSI, FIBK, ONB, HWC, EWBC
Recent rating changes among them:
  - UBSI: 2026-07-27 Keefe, Bruyette & Woods: main, Market Perform -> Market Perform
  - FIBK: 2026-10-05 Barclays: main, Underweight -> Underweight
  - ONB: 2026-10-09 RBC Capital: main, Sector Perform -> Sector Perform
  - HWC: 2026-10-05 Barclays: main, Overweight -> Overweight
  - EWBC: 2026-10-14 Cantor Fitzgerald: main, Overweight -> Overweight
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
Share count change: 1 week: -1.1% (-44.01M) over 7d | 1 month: -3.2% (-124.07M) over 31d
Shares outstanding: 53.36M | fund size: 3.79B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: technicals show a downtrend with RSI 23.6 (oversold) but no decisive breakout; analyst view is bullish (90% buy, +21.9% price target) while fund flows indicate net outflows and fundamentals are modest. These factors offset each other, leading to a neutral stance.

**Main reasons it gave:**
- RSI 23.6 indicates oversold but price remains below 20‑day, 50‑day, and 200‑day SMAs
- Analyst coverage 44.6% shows 90.3% buy rating and +21.9% price target
- Fund flows show net outflow of -2% over the past month
- Fund fundamentals: P/E 14.08, three‑year return +0.7% per year, expense ratio 0.75%

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 34.73 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 36.11 (-3.8%), 50d 37.37 (-7.1%), 200d 38.08 (-8.8%); 50d below 200d
Momentum: RSI(14) 23.6 | MACD -0.673 vs signal -0.568 (histogram -0.105)
Returns: 1d -1.2% | 5d -3.0% | 1m -6.5% | 3m -6.4%
52-week range: 34.73 - 41.03 (now 0.0% of the way up)
Volatility: ATR(14) 0.33 (0.9% of price) | annualised 20d 12.7%
Volume: 1.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.08 | P/B 1.70 | P/S 2.84 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +0.7% a year | beta to the market 0.19
Cost and size: expense ratio 0.75% | net assets 588.43M
What it is made of: Stocks 99.6%, Cash 0.4%
Largest holdings: Al Rajhi Bank 14.1%, Saudi Arabian Oil Co 11.5%, Saudi National Bank 8.6%, Saudi Telecom Co 6.1%, Saudi Arabian Mining Co 4.3%
Sector mix: Financial services 42.2%, Energy 12.5%, Basic materials 12.4%, Communication services 9.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 44.6% of the fund by weight
Ratings by weight: buy 90.3% | hold 9.7% | sell 0.0% (mean 2.06 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.9% above the current prices
Holdings read: 1120.SR, 2222.SR, 1180.SR, 7010.SR, 1211.SR
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.25</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +2.4% (13.85M) over 7d | 1 month: -2.0% (-11.77M) over 31d
Shares outstanding: 16.69M | fund size: 579.77M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data unreachable: The read operation timed out

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: strong analyst bullish view on top holdings (+60% price target) and attractive fundamentals (low P/E 11.4, P/B 1.33, dividend yield 2.1%) are offset by bearish technicals (price below 20‑, 50‑ and 200‑day SMAs, RSI 38.4, low volume) and recent net outflows of ~3% over the past month. No macro surprise data (inflation 3.7% and Fed target unchanged) further supports a neutral stance.

**Main reasons it gave:**
- No macro surprise: inflation 3.7% and Fed target unchanged
- Technical downtrend: price below 20‑, 50‑ and 200‑day SMAs, RSI 38.4, low volume
- Fund flows: net outflow of 3% over past month
- Analyst ratings: 100% buy for top holdings, price target +60% above current
- Fund basics: low P/E 11.4, P/B 1.33, dividend yield 2.1%

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 51.01 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 51.97 (-1.9%), 50d 53.39 (-4.5%), 200d 56.28 (-9.4%); 50d below 200d
Momentum: RSI(14) 38.4 | MACD -0.602 vs signal -0.562 (histogram -0.041)
Returns: 1d +0.3% | 5d -2.2% | 1m -5.5% | 3m -4.8%
52-week range: 50.48 - 65.59 (now 3.5% of the way up)
Volatility: ATR(14) 0.63 (1.2% of price) | annualised 20d 16.8%
Volume: 0.36x the 20-day average
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
Three-year record: +8.5% a year | beta to the market 0.45
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 32.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +59.7% above the current prices
Holdings read: 0700.HK, 9988.HK, 00939, 01398, 1810.HK
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
Direction: money going out (1 month)
Share count change: 1 week: +2.9% (165.83M) over 7d | 1 month: -3.0% (-183.30M) over 31d
Shares outstanding: 116.91M | fund size: 5.96B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – technicals show bearish momentum, analyst view is bullish but limited to 44% of the fund, fund flows are flat, and macro data show no surprise.

**Main reasons it gave:**
- Technical indicators show bearish momentum (RSI 38, MACD negative, price below 20‑day and 50‑day SMA)
- Analyst coverage is bullish but only covers 44% of the fund with a +46.3% price target
- Fund flows flat, indicating no net demand for the ETF
- Macro data shows no surprise; yields stable, VIX modestly elevated

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 553.01 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 595.94 (-7.2%), 50d 578.02 (-4.3%), 200d 513.19 (+7.8%); 50d above 200d
Momentum: RSI(14) 38.0 | MACD -7.453 vs signal 1.547 (histogram -8.999)
Returns: 1d +0.8% | 5d -6.0% | 1m -7.2% | 3m -5.8%
52-week range: 325.10 - 668.91 (now 66.3% of the way up)
Volatility: ATR(14) 16.76 (3.0% of price) | annualised 20d 26.6%
Volume: 0.32x the 20-day average
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
Three-year record: +53.9% a year | beta to the market 2.00
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
Weighted price target: +46.3% above the current prices
Holdings read: NVDA, TSM, AMD, AVGO, MU
Recent rating changes among them:
  - NVDA: 2026-10-01 Cantor Fitzgerald: reit, Overweight -> Overweight
  - TSM: 2026-10-16 Barclays: main, Overweight -> Overweight
  - AMD: 2026-10-20 Wedbush: reit, Outperform -> Outperform
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 11.67M | fund size: 6.45B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error waiting for selector "#main" failed: timeout 30000ms exceeded)

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst coverage 43.2% of fund with 100% buy rating and +30% price target
- Fund flows flat (0% change) over the past week and month
- Fund fundamentals mixed: low P/E 11.69 but three-year return -1.9% per year and expense ratio 0.59%
- Technicals show price below 20d, 50d, 200d SMAs, RSI 33.4 (oversold) with low volume and no decisive breakout
- Macro unchanged: yields modestly down, VIX up modestly, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Direxion Daily Semiconductor Bull 3X Shares (SOXL) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/SOXL/)  
  <sub>Yahoo! Finance Canada, 13 hours ago</sub>  
  Find the latest Direxion Daily Semiconductor Bull 3X Shares (SOXL) stock quote, history, news and other vital information to help you with your stock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 32.71 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 34.32 (-4.7%), 50d 37.42 (-12.6%), 200d 39.25 (-16.7%); 50d below 200d
Momentum: RSI(14) 33.4 | MACD -1.374 vs signal -1.315 (histogram -0.060)
Returns: 1d +2.9% | 5d -4.1% | 1m -13.1% | 3m -17.8%
52-week range: 31.80 - 43.74 (now 7.6% of the way up)
Volatility: ATR(14) 0.67 (2.0% of price) | annualised 20d 26.1%
Volume: 0.31x the 20-day average
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
Three-year record: -1.9% a year | beta to the market 0.61
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 43.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.0% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 15.65M | fund size: 511.91M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, limited analyst coverage, technicals below medium‑term averages, mixed fundamentals.

**Main reasons it gave:**
- Upward sloping yield curve (+1.00) with modest weekly declines in Treasury yields, no rate surprise
- Price below 50‑day (94.02) and 200‑day (94.47) SMAs, low volume (0.26× 20‑day avg) indicating lack of bullish momentum
- Analyst coverage only 40.5% of fund despite 100% buy rating and +17.3% price target, limiting impact
- Fund flows flat (0% net creation/redemption) indicating no strong demand shift

<details><summary><b>News</b> — score +0.00</summary>

- [Arbor Realty Trust PFDs Get Sell Ratings (NYSE:ABR.PR.D)](https://seekingalpha.com/article/4955276-arbor-realty-trust-pfds-get-sell-ratings)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Arbor Realty Trust and its preferreds suffered sharp price declines amid analyst downgrades and persistent rate pressures. Read more on ABR preferreds here.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 92.18 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 90.49 (+1.9%), 50d 94.02 (-2.0%), 200d 94.47 (-2.4%); 50d below 200d
Momentum: RSI(14) 52.1 | MACD -0.676 vs signal -1.126 (histogram 0.450)
Returns: 1d +1.6% | 5d +1.1% | 1m -1.7% | 3m -6.9%
52-week range: 87.00 - 100.95 (now 37.1% of the way up)
Volatility: ATR(14) 1.26 (1.4% of price) | annualised 20d 16.0%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Real Estate
What it holds: P/E 28.36 | P/B 2.42 | P/S 4.59 | 3y earnings growth n/a
Yield: 3.8%
Three-year record: +10.6% a year | beta to the market 0.98
Cost and size: expense ratio 0.13% | net assets 66.42B
What it is made of: Stocks 99.0%, Cash 0.7%, Other 0.3%
Largest holdings: Vanguard Real Estate II Index 14.5%, Welltower Inc 9.1%, Prologis Inc 6.9%, Equinix Inc 5.7%, American Tower Corp 4.3%
Sector mix: Real estate 99.5%, Communication services 0.4%, Energy 0.1%, Industrials 0.0%
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
Rolled up from the 5 largest holdings, 40.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.3% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2026-10-19 Wells Fargo: main, Overweight -> Overweight
  - PLD: 2026-10-20 Baird: main, Neutral -> Neutral
  - EQIX: 2026-10-20 Guggenheim: reit, Buy -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 370.18M | fund size: 34.12B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals lack decisive break, analyst coverage thin, fundamentals cheap, fund flows slightly bearish overall.

**Main reasons it gave:**
- Macro: no rate or policy surprise; yields stable and VIX modestly elevated
- Technical: price above 20‑day SMA but below 50‑day SMA, low volume
- Analyst view: thin coverage (9.2% of fund) with 61% buy rating but price target -7.8% vs current
- Fund flows: net outflow of -3% over the month indicating slight bearish pressure
- Fundamentals: low P/B 0.21 and strong 3‑year return +27.4% a year

<details><summary><b>News</b> — score +0.00</summary>

- [Why $55 Million Flowed Into a Triple-Leveraged Biotech ETF Worth Less Than $600 Million](https://finance.yahoo.com/markets/stocks/articles/why-55-million-flowed-triple-084850127.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  LABU absorbed $55 million, which represented 9% of its $597 million in assets, dwarfing XBI's proportional inflow of 3% despite XBI receiving $304 million.
- [$55M flows into volatile triple-leveraged biote...](https://pluang.com/en/news-feed/mengapa-55-juta-dolar-mengalir-ke-etf-biotech-leveraged-tiga-kali)  
  <sub>Pluang, 6 hours ago</sub>  
  Traders poured $54.6 million into the Direxion Daily S&P Biotech Bull 3X ETF (LABU) on October 14, 2026, marking the largest inflow relative to its $597...
- [(XBI) as a Liquidity Pulse for Institutional Tactics](https://news.stocktradersdaily.com/news_release/35/XBI_as_a_Liquidity_Pulse_for_Institutional_Tactics_101926073802_1792453082.html)  
  <sub>Stock Traders Daily, 19 hours ago</sub>  
  Key findings for Spdr Biotech Etf (NYSE: XBI). Weak Near and Mid-Term Sentiment Could Challenge Long-Term Positive Outlook; No clear price positioning...
- [Form 4 iShares Biotechnology ETF For: 20 October By Investing.com](https://in.investing.com/news/stock-market-news/form-4-ishares-biotechnology-etf-for-20-october-93CH-5642272)  
  <sub>Investing.com India, 4 hours ago</sub>  
  The information in this preliminary pricing supplement is not complete and may be changed. This preliminary pricing supplement and the accompanying...
- [XBI Jun 2027 230.000 call (XBI270617C00230000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XBI270617C00230000/)  
  <sub>Yahoo! Finance Canada, 23 hours ago</sub>  
  Find the latest XBI Jun 2027 230.000 call (XBI270617C00230000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 153.01 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 152.33 (+0.4%), 50d 157.67 (-3.0%), 200d 140.44 (+8.9%); 50d above 200d
Momentum: RSI(14) 50.1 | MACD -2.470 vs signal -2.383 (histogram -0.086)
Returns: 1d +3.5% | 5d +4.2% | 1m -3.3% | 3m +0.6%
52-week range: 107.32 - 169.55 (now 73.4% of the way up)
Volatility: ATR(14) 4.47 (2.9% of price) | annualised 20d 34.8%
Volume: 0.42x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Health
What it holds: P/E n/a | P/B 0.21 | P/S 0.12 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +27.4% a year | beta to the market 1.09
Cost and size: expense ratio 0.35% | net assets 10.36B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Twist Bioscience Corp 2.2%, Moderna Inc 2.0%, Natera Inc 1.8%, Iovance Biotherapeutics Inc 1.6%, Amgen Inc 1.5%
Sector mix: Healthcare 99.3%, Financial services 0.7%
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

<details><summary><b>What analysts and big funds say</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.15</summary>

```text
Rolled up from the 5 largest holdings, 9.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 61.1% | hold 38.9% | sell 0.0% (mean 2.09 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -7.8% above the current prices
Holdings read: TWST, MRNA, NTRA, IOVA, AMGN
Recent rating changes among them:
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MRNA: 2026-10-15 Goldman Sachs: main, Neutral -> Neutral
  - NTRA: 2026-10-19 Canaccord Genuity: main, Buy -> Buy
  - IOVA: 2026-10-13 Barclays: main, Overweight -> Overweight
  - AMGN: 2026-10-13 Guggenheim: main, Neutral -> Neutral
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +6.6% (677.31M) over 7d | 1 month: -3.0% (-334.18M) over 31d
Shares outstanding: 71.80M | fund size: 10.99B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No clear macro surprise, policy shift, or decisive technical break; sector data shows housing weakness but fund flows are positive and analyst view is bullish for a thin slice, leading to a neutral overall stance.

**Main reasons it gave:**
- Homebuilder confidence index fell to 29, lowest since 2012 (sector weakness)
- Fund flows: +9.5% net inflow over past month ($126.39M) indicating demand
- Analyst coverage: 17% of fund weight, buy rating, price target +17.5% (thin coverage)
- Technical: price below 50‑day and 200‑day SMA, RSI 49.3 (downtrend)

<details><summary><b>News</b> — score +0.00</summary>

- [XHB vs ITB: Holdings, Fees and Exposure to Mortgage Rates](https://www.ebc.com/forex/xhb-vs-itb-holdings-fees-mortgage-rates)  
  <sub>EBC Financial Group, 6 hours ago</sub>  
  The SPDR S&P Homebuilders ETF (XHB) and iShares U.S. Home Construction ETF (ITB) both track U.S. housing-related stocks, but their portfolios differ in...
- [Homebuilder Gauge Hits 2012 Low: XHB Hits 2020 Lows vs. SPY - State Street SPDR S&P 500 ETF Trust (ARCA:S](https://www.benzinga.com/trading-ideas/technicals/26/10/62449236/homebuilder-sentiment-2012-low-xhb-spy-pandemic-lows)  
  <sub>Benzinga, 21 hours ago</sub>  
  Builder confidence fell to 29, lowest since 2012, while the XHB/SPY ratio sits near its weakest level since April 2020 as rates top 7%.
- [It's a rough housing market, and Goldman Sachs expects it to get worse](https://longbridge.com/news/302383900)  
  <sub>Longbridge, 7 hours ago</sub>  
  Goldman Sachs economists predict the U.S. housing market will deteriorate, with affordability headwinds dominating by 2027. High mortgage rates create...
- [BlackRock® Canada Announces October Cash Distributions for the iShares® ETFs](https://www.manilatimes.net/2026/10/20/tmt-newswire/globenewswire/blackrock-canada-announces-october-cash-distributions-for-the-ishares-etfs/2449460/amp)  
  <sub>The Manila Times, 6 hours ago</sub>  
  TORONTO, Oct. 20, 2026 (GLOBE NEWSWIRE) -- BlackRock Asset Management Canada Limited ('BlackRock Canada”), an indirect, wholly-owned subsidiary of BlackRock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 96.62 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 95.90 (+0.8%), 50d 100.11 (-3.5%), 200d 105.57 (-8.5%); 50d below 200d
Momentum: RSI(14) 49.3 | MACD -1.349 vs signal -1.642 (histogram 0.293)
Returns: 1d +2.6% | 5d +2.1% | 1m -0.4% | 3m -9.6%
52-week range: 92.84 - 121.36 (now 13.3% of the way up)
Volatility: ATR(14) 2.22 (2.3% of price) | annualised 20d 23.8%
Volume: 0.42x the 20-day average
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
Three-year record: +9.0% a year | beta to the market 1.48
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.5% above the current prices
Holdings read: SN, CVCO, SKY, JCI, W
Recent rating changes among them:
  - SN: 2026-10-19 JP Morgan: main, Overweight -> Overweight
  - CVCO: 2026-09-30 Oppenheimer: init, ? -> Outperform
  - SKY: 2026-10-15 RBC Capital: main, Outperform -> Outperform
  - JCI: 2026-10-15 Mizuho: main, Neutral -> Neutral
  - W: 2026-10-20 Piper Sandler: main, Overweight -> Overweight
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
Direction: money coming in (1 month)
Share count change: 1 week: -0.2% (-2.31M) over 7d | 1 month: +9.5% (126.39M) over 31d
Shares outstanding: 15.07M | fund size: 1.46B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise in policy or data releases (Fed target unchanged, yields stable)
- Technical indicators show price above SMAs and positive MACD but low volume, no decisive break
- Fund flows flat over past month, indicating neutral demand
- Energy inventories show crude draw (bullish) while EIA forecast predicts falling oil prices (bearish), netting to mixed fundamentals

<details><summary><b>News</b> — score +0.00</summary>

- [Sector Update: Energy Stocks Decline Monday Afternoon](https://ca.finance.yahoo.com/news/sector-energy-stocks-decline-monday-173905976.html)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Energy stocks were lower Monday afternoon, with the NYSE Energy Sector Index decreasing 0.7% and the State Street Energy Select Sector SPDR ETF (XLE) down...
- [A Tech Wreck Could Create the Next Winners](https://moneyandmarkets.com/a-tech-wreck-could-create-the-next-winners/)  
  <sub>Money & Markets, 21 hours ago</sub>  
  With the AI infrastructure boom due for a shakeout, today's losses could lay the groundwork for tomorrow's winners.
- [An Oil Refiner Is Beating Nvidia This Year: Analyst Thinks It Can Rally 16% More From Here](https://www.tradingview.com/news/stocktwits:5a0255e74094b:0-an-oil-refiner-is-beating-nvidia-this-year-analyst-thinks-it-can-rally-16-more-from-here/)  
  <sub>TradingView, 14 hours ago</sub>  
  Energy stocks have rallied sharply in 2026 since the U.S.-Iran war began in February, which led to a sharp uptick in oil prices.Marathon Petroleum Corp.
- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Tuesday as AI Stocks Retreat, Oil Prices Rise](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-130913751.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.2% and the actively tr.
- [Stock Market Today: Nasdaq 100 Rises as AI Chip Rout Reverses, SanDisk Jumps 7%](https://www.benzinga.com/markets/equities/26/10/62446593/stock-market-today-sandisk-jumps-nasdaq-100-rises-ai-chip-rout-reverses)  
  <sub>Benzinga, 22 hours ago</sub>  
  Tech rebounded from last week's rout as chip stocks bounced and steel maker Cleveland-Cliffs soared on earnings, while the 10-year yield climbed to 5.14%.
- [What's Going On With Exxon Stock On Monday?](https://www.tradingview.com/news/benzinga:d4df4ed74094b:0-what-s-going-on-with-exxon-stock-on-monday/)  
  <sub>TradingView, 21 hours ago</sub>  
  ExxonMobil Holdings NYSE:XOM shares are trading slightly lower after closing near a 52-week high on Friday, as crude prices retreated from five-month highs...
- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://ca.finance.yahoo.com/news/exchange-traded-funds-higher-us-172542006.html)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.5%. US equity indexes rose amid...
- [Weekly Market Commentary](https://t.co/603IYOry11)  
  <sub>Howl.link, 23 hours ago</sub>  
  U.S. equities fell as the Nasdaq dropped 5.54% amid a sharp rotation from tech into defensive sectors.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 67.11 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 64.45 (+4.1%), 50d 63.88 (+5.1%), 200d 57.84 (+16.0%); 50d above 200d
Momentum: RSI(14) 61.7 | MACD 1.247 vs signal 0.889 (histogram 0.358)
Returns: 1d -1.0% | 5d -0.1% | 1m +7.4% | 3m +13.4%
52-week range: 43.35 - 68.24 (now 95.5% of the way up)
Volatility: ATR(14) 1.31 (2.0% of price) | annualised 20d 19.8%
Volume: 0.62x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Equity Energy
What it holds: P/E 17.51 | P/B 2.47 | P/S 1.70 | 3y earnings growth n/a
Yield: 2.5%
Three-year record: +18.5% a year | beta to the market -0.03
Cost and size: expense ratio 0.08% | net assets 39.13B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ExxonMobil Holdings Corp 24.0%, Chevron Corp 18.1%, ConocoPhillips 6.7%, Valero Energy Corp 4.7%, Marathon Petroleum Corp 4.7%
Sector mix: Energy 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.10</summary>

```text
US inventories, week ending 2026-10-09 (published the following Wednesday)
  Crude oil: 415.6 million barrels, -8.6 on the week (a draw), 15% percentile over 52 weeks
  Petrol: 208.3 million barrels, +3.5 on the week (a build), 21% percentile over 52 weeks
  Diesel: 102.6 million barrels, -2.5 on the week (a draw), 12% percentile over 52 weeks -- low for the time of year
  Natural gas: 3,567.0 billion cubic feet, +67.0 on the week (a build), 83% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 58.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +1.7% above the current prices
Holdings read: XOM, CVX, COP, VLO, MPC
Recent rating changes among them:
  - XOM: 2026-10-19 Barclays: main, Overweight -> Overweight
  - CVX: 2026-10-15 Morgan Stanley: main, Overweight -> Overweight
  - COP: 2026-10-20 Susquehanna: main, Positive -> Positive
  - VLO: 2026-10-14 Wells Fargo: main, Overweight -> Overweight
  - MPC: 2026-10-14 Wells Fargo: main, Overweight -> Overweight
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 186.42M | fund size: 12.51B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, technicals not decisive, limited analyst coverage, sector pressure keep outlook neutral.

**Main reasons it gave:**
- Treasury yields slipped modestly; dollar down 0.61% week; VIX up modestly – no macro surprise.
- Fund flows flat: share count unchanged week over week.
- Technicals show modest uptrend but price below 50‑day SMA and volume at 0.18× 20‑day average.
- Analyst view bullish on top holdings (100% buy) but covers only 42.7% of fund.
- Bank stocks have fallen for six straight weeks, sector under pressure.

<details><summary><b>News</b> — score +0.00</summary>

- [Financial Select Sector SPDR (XLF) Buys $57.8 Million More Berkshire on Oct. 16](https://finance.yahoo.com/markets/stocks/articles/financial-select-sector-spdr-xlf-110447945.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Financial Select Sector SPDR ETF (XLF) extended its run of broad additions, lifting all 76 of its...
- [Cboe and NYSE Roll Out Pre-Market Trading for Key Stock Options](https://www.tradingview.com/news/financemagnates:97e0b3d90094b:0-cboe-and-nyse-roll-out-pre-market-trading-for-key-stock-options/)  
  <sub>TradingView, 23 hours ago</sub>  
  Cboe Global Markets launched extended trading hours for options on 24 stocks and five exchange-traded funds on Monday, 19 October, giving traders access...
- [Banks are the most sold-off since the financial crisis](https://seekingalpha.com/news/4654263-banks-are-the-most-sold-off-since-the-financial-crisis)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  Bank stocks slide for 6 straight weeks as KBE drops 8.6%.
- [Bank Stocks Fell 13% to 14% in the Month Before Q3 Earnings](https://www.openingbelldailynews.com/p/bank-stocks-fall-before-q3-2026-earnings-chart)  
  <sub>Opening Bell Daily, 17 hours ago</sub>  
  Every big bank stock fell in the month before Q3 2026 earnings, with Bank of America, Goldman and Morgan Stanley down 13% to 14% as the S&P 500 rose.
- [Webcast: What asset classes look attractive today? | ETF Trends](https://www.advisorperspectives.com/webinars/2026/11/13/what-asset-classes-look-attractive-today?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 19 hours ago</sub>  
  2026 has been eventful. Where can investors find opportunity? Energy prices have risen, interest rates have risen, and the market continues to become more...
- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Tuesday as AI Stocks Retreat, Oil Prices Rise](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-130913751.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.2% and the actively tr.
- [Stock Market Today: Nasdaq 100 Rises as AI Chip Rout Reverses, SanDisk Jumps 7%](https://www.tradingview.com/news/benzinga:e9b29a8b4094b:0-stock-market-today-nasdaq-100-rises-as-ai-chip-rout-reverses-sandisk-jumps-7/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks diverged at midday Monday as a rebound in AI chip and infrastructure names lifted the Nasdaq 100 by 1.7% and the S&P 500 by 0.7%, while the Dow...
- [Sector Update: Financial Stocks Lower in Afternoon Trading](https://finance.yahoo.com/markets/stocks/articles/sector-financial-stocks-lower-afternoon-175033120.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Financial stocks declined in Monday afternoon trading, with the NYSE Financial Index decreasing 0.8% and the State Street Financial Select Sector SPDR ETF...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 55.88 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 54.46 (+2.6%), 50d 56.19 (-0.5%), 200d 53.69 (+4.1%); 50d above 200d
Momentum: RSI(14) 57.2 | MACD -0.157 vs signal -0.437 (histogram 0.280)
Returns: 1d +1.5% | 5d +1.9% | 1m -0.0% | 3m -0.3%
52-week range: 47.81 - 58.56 (now 75.1% of the way up)
Volatility: ATR(14) 0.71 (1.3% of price) | annualised 20d 12.3%
Volume: 0.18x the 20-day average
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
Three-year record: +20.1% a year | beta to the market 0.75
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 42.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.77 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +7.8% above the current prices
Holdings read: BRK-B, JPM, V, MA, BAC
Recent rating changes among them:
  - BRK-B: 2026-08-10 UBS: main, Buy -> Buy
  - JPM: 2026-10-15 Citigroup: main, Neutral -> Neutral
  - V: 2026-10-12 Baird: main, Outperform -> Outperform
  - MA: 2026-10-09 Baird: main, Outperform -> Outperform
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 883.44M | fund size: 49.37B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, mixed technicals, and analyst view bullish but limited to ~26% of holdings.

**Main reasons it gave:**
- Flat fund flows: share count unchanged (+0% week, +0% month)
- No macro surprise: yields stable, dollar down modestly, VIX modestly up but no shock
- Technical indicators mixed: price below 20d/50d/200d SMAs, RSI 43, MACD histogram positive but low volume
- Analyst view bullish but limited coverage: 25.7% of fund weighted, all buy with +25.6% price target

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Tuesday as AI Stocks Retreat, Oil Prices Rise](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-130913751.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.2% and the actively tr.
- [XLK vs. SOXX: Broad Tech Exposure or Semiconductor Bet?](https://www.theglobeandmail.com/investing/markets/stocks/AAPL-Q/pressreleases/8230399/xlk-vs-soxx-broad-tech-exposure-or-semiconductor-bet/)  
  <sub>The Globe and Mail, 2 hours ago</sub>  
  Key Points. State Street Technology Select Sector SPDR ETF has a lower expense ratio than iShares Semiconductor ETF. The iShares fund delivered higher...
- [Should You Invest in the State Street Technology Select Sector SPDR ETF (XLK)?](https://www.google.com/goto?url=CAESoQEB6zswFSCmfS22DL56E7MlTMnZVuU5_Q0sZgTSUi6GP4wglne0lEHiDxQtzAWwQNvsnGo9IAF1y4pVcUc_x_O2-o3pBqDdVaSsavmqPq5n5UL0ONeearBjD5AO52vY1Jr7thSHVWHzvkjmTeuPgej9XuP1dZw0BjX7Gi6Fn1WFYR4CgFNG1FlOUfLcm8UY2t5WxMRfsXl9KTAOSvMg7EL7xg)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  The State Street Technology Select Sector SPDR ETF (XLK) was launched on December 16, 1998, and is a passively managed exchange traded fund designed to...
- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://ca.finance.yahoo.com/news/exchange-traded-funds-higher-us-172542006.html)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.5%. US equity indexes rose amid...
- [If I Could Only Buy One Sector Right Now, It Wouldn't Be Tech](https://seekingalpha.com/article/4955003-if-i-could-only-buy-one-sector-right-now-it-wouldnt-be-tech)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Industrials benefit from hard-asset TOLL advantages, AI exposure without pure-play risk, and ignored cyclical tailwinds. Read more on industrial stocks...
- [Webcast: What asset classes look attractive today? | ETF Trends](https://www.advisorperspectives.com/webinars/2026/11/13/what-asset-classes-look-attractive-today?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 19 hours ago</sub>  
  2026 has been eventful. Where can investors find opportunity? Energy prices have risen, interest rates have risen, and the market continues to become more...
- [9 Of 11 Sectors Fall As Growth Leads](https://www.benzinga.com/etfs/sector-etfs/26/10/62441939/9-of-11-sectors-fall-as-growth-leads)  
  <sub>Benzinga, 24 hours ago</sub>  
  Monday's regular session has nine sectors lower and two higher, with growth sectors occupying the top two positions. The leaders are separated rather than...
- [ValuEngine Weekly Market Commentary](https://www.google.com/goto?url=CAEShwEB6zswFbSAqSQ63b1BhEeTqEHEnAINJmKPYJOvrwoy5g79txN_sezAhRG5xOct0MZR_h4e-HbRk-C2LkXewIW0HkKGUJR7XvJjr5iLsNg5mV0FvVK9VTjuEYTaHMiHA3oBkLmoJTzQVFJnatNDWebId-Vmc4E6glAvwvzCVRHk_0666IZUd1g)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  US equity markets faced significant selling pressure this week, with sharp declines in tech and growth-oriented stocks contrasting with strong gains across...
- [What State Street Technology SPDR (XLK) Sold: NVIDIA Leads on Oct. 16](https://finance.yahoo.com/markets/stocks/articles/state-street-technology-spdr-xlk-110536665.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Technology Select Sector SPDR ETF (XLK) was the only ETF selling in last Friday's reported activity,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 167.83 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 168.75 (-0.5%), 50d 173.41 (-3.2%), 200d 173.08 (-3.0%); 50d above 200d
Momentum: RSI(14) 43.0 | MACD -1.418 vs signal -1.562 (histogram 0.144)
Returns: 1d +0.7% | 5d -0.5% | 1m -1.3% | 3m -6.2%
52-week range: 147.83 - 186.51 (now 51.7% of the way up)
Volatility: ATR(14) 2.50 (1.5% of price) | annualised 20d 13.4%
Volume: 0.62x the 20-day average
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
Three-year record: +19.4% a year | beta to the market 1.01
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 25.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.78 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.6% above the current prices
Holdings read: CAT, GE, GEV, RTX, DE
Recent rating changes among them:
  - CAT: 2026-10-14 Oppenheimer: main, Outperform -> Outperform
  - GE: 2026-09-30 Wells Fargo: main, Overweight -> Overweight
  - GEV: 2026-10-14 Susquehanna: main, Positive -> Positive
  - RTX: 2026-10-15 RBC Capital: main, Outperform -> Outperform
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 136.63M | fund size: 22.93B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Macro: yields down slightly, inflation 3.7% and unemployment 4.2% within expectations
- Technical: price below 20‑day SMA, RSI 40.5, MACD negative, no decisive break
- Fund flows: flat share count, no net inflows or outflows
- Fundamentals: high valuations (P/E 32, P/B 11.9) suggest limited upside

<details><summary><b>News</b> — score +0.00</summary>

- [Should You Invest in the State Street Technology Select Sector SPDR ETF (XLK)?](https://finance.yahoo.com/markets/stocks/articles/invest-state-street-technology-select-092002564.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  The State Street Technology Select Sector SPDR ETF (XLK) was launched on December 16, 1998, and is a passively managed exchange traded fund designed to...
- [XLK vs. SOXX: Broad Tech Exposure or Semiconductor Bet?](https://www.theglobeandmail.com/investing/markets/stocks/AAPL-Q/pressreleases/8230399/xlk-vs-soxx-broad-tech-exposure-or-semiconductor-bet/)  
  <sub>The Globe and Mail, 2 hours ago</sub>  
  Key Points. State Street Technology Select Sector SPDR ETF has a lower expense ratio than iShares Semiconductor ETF. The iShares fund delivered higher...
- [Amazon Jumps 5% as Morgan Stanley Names It Top Pick on Faster AWS Growth; Microsoft and Alphabet Edge Higher](https://247wallst.com/investing/2026/10/19/amazon-jumps-5-as-morgan-stanley-names-it-top-pick-on-faster-aws-growth-microsoft-and-alphabet-edge-higher/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  Morgan Stanley named $AMZN a top pick, raising its price target to $350 and sending shares up 5% on faster AWS growth expectations.
- [A Tech Wreck Could Create the Next Winners](https://moneyandmarkets.com/a-tech-wreck-could-create-the-next-winners/)  
  <sub>Money & Markets, 21 hours ago</sub>  
  With the AI infrastructure boom due for a shakeout, today's losses could lay the groundwork for tomorrow's winners.
- [9 Of 11 Sectors Fall As Growth Leads](https://www.benzinga.com/etfs/sector-etfs/26/10/62441939/9-of-11-sectors-fall-as-growth-leads)  
  <sub>Benzinga, 24 hours ago</sub>  
  Monday's regular session has nine sectors lower and two higher, with growth sectors occupying the top two positions. The leaders are separated rather than...
- [ProPetro Appoints Kyle Crowley as Independent Director](https://www.bitget.com/amp/news/detail/12560605982587)  
  <sub>Bitget, 18 hours ago</sub>  
  ProPetro appointed Kyle Crowley as an independent director, effective October 16, 2026. Crowley brings over 30 years of power-sector experience | Bitget...
- [What State Street Technology SPDR (XLK) Sold: NVIDIA Leads on Oct. 16](https://finance.yahoo.com/markets/stocks/articles/state-street-technology-spdr-xlk-110536665.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Technology Select Sector SPDR ETF (XLK) was the only ETF selling in last Friday's reported activity,...
- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://ca.finance.yahoo.com/news/exchange-traded-funds-higher-us-172542006.html)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.5%. US equity indexes rose amid...
- [Sector Update: Tech Stocks Rise Late Afternoon](https://ca.finance.yahoo.com/news/sector-tech-stocks-rise-afternoon-194654951.html)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Tech stocks were higher late Monday afternoon, with the State Street Technology Select Sector SPDR ETF (XLK) rising 1.7% and the State Street SPDR S&P...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 186.79 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 194.90 (-4.2%), 50d 189.90 (-1.6%), 200d 167.93 (+11.2%); 50d above 200d
Momentum: RSI(14) 40.5 | MACD -0.658 vs signal 1.261 (histogram -1.920)
Returns: 1d +0.4% | 5d -4.8% | 1m -4.1% | 3m +3.6%
52-week range: 127.50 - 202.00 (now 79.6% of the way up)
Volatility: ATR(14) 3.73 (2.0% of price) | annualised 20d 19.7%
Volume: 0.54x the 20-day average
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
Three-year record: +30.0% a year | beta to the market 1.45
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 49.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.5% above the current prices
Holdings read: NVDA, AAPL, MSFT, AMD, AVGO
Recent rating changes among them:
  - NVDA: 2026-10-01 Cantor Fitzgerald: reit, Overweight -> Overweight
  - AAPL: 2026-10-20 Loop Capital: down, Buy -> Hold
  - MSFT: 2026-10-19 Bernstein: main, Outperform -> Outperform
  - AMD: 2026-10-20 Wedbush: reit, Outperform -> Outperform
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 33d
Shares outstanding: 272.06M | fund size: 50.82B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Flat fund flows (0% change week/month) indicating no net demand
- Analyst consensus: 100% buy with +4.6% price target, covering 41.8% of fund
- Technical indicators: RSI 70.8 (overbought) and low volume, no decisive break
- Macro data: inflation 3.7% and stable yields, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Tuesday as AI Stocks Retreat, Oil Prices Rise](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-130913751.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.2% and the actively tr.
- [Should You Invest in the State Street Consumer Discretionary Select Sector SPDR ETF (XLY)?](https://finance.yahoo.com/markets/stocks/articles/invest-state-street-consumer-discretionary-092002564.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Launched on December 16, 1998, the State Street Consumer Discretionary Select Sector SPDR ETF (XLY) is a passively managed exchange traded fund designed to...
- [XLV: Safe Haven, But That Cuts Both Ways (NYSEARCA:XLV)](https://seekingalpha.com/article/4955254-xlv-safe-haven-but-that-cuts-both-ways)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF hits new highs as a safe-haven amid tech volatility. Learn more about the XLV ETF here.
- [A Tech Wreck Could Create the Next Winners](https://moneyandmarkets.com/a-tech-wreck-could-create-the-next-winners/)  
  <sub>Money & Markets, 21 hours ago</sub>  
  With the AI infrastructure boom due for a shakeout, today's losses could lay the groundwork for tomorrow's winners.
- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance Singapore, 15 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) · 2.13% · 4.31% · 18.04% · 13.47% · 22.60% · 36.41% · 607.91%. Key events. Baseline. Advanced chart.
- [Sector Update: Consumer](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-191424137.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Consumer stocks were mixed late Monday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) down 0.2% and the State Street...
- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-us-172542006.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.5%. US equity indexes rose amid...
- [Webcast: What asset classes look attractive today? | ETF Trends](https://www.advisorperspectives.com/webinars/2026/11/13/what-asset-classes-look-attractive-today?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 19 hours ago</sub>  
  2026 has been eventful. Where can investors find opportunity? Energy prices have risen, interest rates have risen, and the market continues to become more...
- [Stock Market Today: Nasdaq 100 Rises as AI Chip Rout Reverses, SanDisk Jumps 7%](https://www.tradingview.com/news/benzinga:e9b29a8b4094b:0-stock-market-today-nasdaq-100-rises-as-ai-chip-rout-reverses-sandisk-jumps-7/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks diverged at midday Monday as a rebound in AI chip and infrastructure names lifted the Nasdaq 100 by 1.7% and the S&P 500 by 0.7%, while the Dow...
- [ValuEngine Weekly Market Commentary](https://seekingalpha.com/article/4955311-valuengine-weekly-market-commentary)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  US equity markets faced significant selling pressure this week, with sharp declines in tech and growth-oriented stocks contrasting with strong gains across...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 87.82 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 83.36 (+5.4%), 50d 84.19 (+4.3%), 200d 84.10 (+4.4%); 50d above 200d
Momentum: RSI(14) 70.8 | MACD 1.019 vs signal 0.286 (histogram 0.732)
Returns: 1d +0.7% | 5d +4.3% | 1m +7.2% | 3m +4.1%
52-week range: 75.60 - 90.01 (now 84.8% of the way up)
Volatility: ATR(14) 1.13 (1.3% of price) | annualised 20d 14.9%
Volume: 0.50x the 20-day average
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
Three-year record: +12.1% a year | beta to the market 0.48
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 41.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.6% above the current prices
Holdings read: WMT, COST, PG, KO, PM
Recent rating changes among them:
  - WMT: 2026-10-20 Evercore ISI Group: main, Outperform -> Outperform
  - COST: 2026-10-15 Tigress Financial: main, Buy -> Buy
  - PG: 2026-10-20 RBC Capital: reit, Outperform -> Outperform
  - KO: 2026-10-16 Barclays: main, Overweight -> Overweight
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 210.17M | fund size: 18.46B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, flat fund flows; analyst view bullish but not enough to outweigh neutral macro backdrop.

**Main reasons it gave:**
- Analyst coverage: 80.6% buy, price target +16% above current price
- Fundamentals: P/E 17.86, yield 3.1%, beta 0.40
- Technicals: price above 20‑day SMA, MACD positive, but volume 0.16× 20‑day average
- Macro: yields high but down 0.14% on 10‑yr, no rate surprise; VIX up modestly to 17.63
- Fund flows: flat share count, no net inflows or outflows

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Utilities SPDR (XLU) Sells NextEra and Southern on Oct. 16](https://finance.yahoo.com/markets/stocks/articles/state-street-utilities-spdr-xlu-110515050.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Utilities Select Sector SPDR ETF (XLU) was the sole mover in Friday's session, recording $183.7...
- [Stock Market Today: Nasdaq 100 Rises as AI Chip Rout Reverses, SanDisk Jumps 7%](https://www.tradingview.com/news/benzinga:e9b29a8b4094b:0-stock-market-today-nasdaq-100-rises-as-ai-chip-rout-reverses-sandisk-jumps-7/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks diverged at midday Monday as a rebound in AI chip and infrastructure names lifted the Nasdaq 100 by 1.7% and the S&P 500 by 0.7%, while the Dow...
- [Webcast: What asset classes look attractive today? | ETF Trends](https://www.advisorperspectives.com/webinars/2026/11/13/what-asset-classes-look-attractive-today?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 19 hours ago</sub>  
  2026 has been eventful. Where can investors find opportunity? Energy prices have risen, interest rates have risen, and the market continues to become more...
- [ValuEngine Weekly Market Commentary](https://seekingalpha.com/article/4955311-valuengine-weekly-market-commentary)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  US equity markets faced significant selling pressure this week, with sharp declines in tech and growth-oriented stocks contrasting with strong gains across...
- [State Street Energy Select Sector SPDR ETF (XLE) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLE/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest State Street Energy Select Sector SPDR ETF (XLE) stock quote, history, news and other vital information to help you with your stock trading...
- [AI chips reversed course to lead the Nasdaq higher, as SanDisk (SNDK.US) soared 7%, igniting a tech rebound.](https://news.futunn.com/en/post/1001579792/ai-chips-reversed-course-to-lead-the-nasdaq-higher-as)  
  <sub>富途牛牛, 14 hours ago</sub>  
  OnMonday, U.S. stocks were mixed, with the Nasdaq rising 1.7%. AI chip and memory stocks led the gains, with SanDisk up nearly 7%.
- [State Street Consumer Staples Select Sector SPDR ETF (XLP) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLP/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Find the latest State Street Consumer Staples Select Sector SPDR ETF (XLP) stock quote, history, news and other vital information to help you with your...
- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance Singapore, 15 hours ago</sub>  
  Find the latest State Street Health Care Select Sector SPDR ETF (XLV) stock quote, history, news and other vital information to help you with your stock...
- [Weekly Market Commentary](https://t.co/603IYOry11)  
  <sub>Howl.link, 23 hours ago</sub>  
  U.S. equities fell as the Nasdaq dropped 5.54% amid a sharp rotation from tech into defensive sectors.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 41.94 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 40.68 (+3.1%), 50d 41.95 (-0.0%), 200d 44.30 (-5.3%); 50d below 200d
Momentum: RSI(14) 55.9 | MACD 0.060 vs signal -0.185 (histogram 0.245)
Returns: 1d +1.4% | 5d +0.2% | 1m +3.1% | 3m -8.7%
52-week range: 39.25 - 47.73 (now 31.7% of the way up)
Volatility: ATR(14) 0.66 (1.6% of price) | annualised 20d 18.3%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Utilities
What it holds: P/E 17.86 | P/B 2.04 | P/S 2.49 | 3y earnings growth n/a
Yield: 3.1%
Three-year record: +15.5% a year | beta to the market 0.40
Cost and size: expense ratio 0.08% | net assets 21.33B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: NextEra Energy Inc 12.7%, Southern Co 7.7%, Duke Energy Corp 7.2%, Constellation Energy Corp 6.7%, American Electric Power Co Inc 5.2%
Sector mix: Utilities 100.0%
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
Ratings by weight: buy 80.6% | hold 19.4% | sell 0.0% (mean 2.01 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.0% above the current prices
Holdings read: NEE, SO, DUK, CEG, AEP
Recent rating changes among them:
  - NEE: 2026-10-19 Barclays: main, Equal-Weight -> Equal-Weight
  - SO: 2026-10-16 Barclays: main, Equal-Weight -> Equal-Weight
  - DUK: 2026-10-13 JP Morgan: main, Neutral -> Neutral
  - CEG: 2026-10-16 CIBC: init, ? -> Outperformer
  - AEP: 2026-10-20 BTIG: up, Neutral -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 163.27M | fund size: 6.85B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, flat fund flows, strong but non‑decisive technicals, and uniformly positive analyst coverage.

**Main reasons it gave:**
- Analyst coverage of top holdings: 100% buy, weighted price target +5% above current price
- Fund flows flat (0% change) over the past week and month, indicating no net demand shift
- Technicals: price above 20‑day, 50‑day and 200‑day SMAs; RSI 68.7; MACD positive; volume 0.47× 20‑day average; at 52‑week high
- Macro: yields unchanged (10‑yr 5.08% down 0.14), VIX up 2.4 points to 17.63, dollar index down 0.61, no policy or data surprise

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance Singapore, 15 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) · 2.13% · 4.31% · 18.04% · 13.47% · 22.60% · 36.41% · 607.91%. Key events. Baseline. Advanced chart.
- [State Street Health Care SPDR (XLV) Buys $25 Million More Eli Lilly on Oct. 16](https://finance.yahoo.com/healthcare/articles/state-street-health-care-spdr-110529619.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Health Care Select Sector SPDR ETF (XLV) extended its run of broad additions on Friday,...
- [XLV: Safe Haven, But That Cuts Both Ways (NYSEARCA:XLV)](https://seekingalpha.com/article/4955254-xlv-safe-haven-but-that-cuts-both-ways)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF hits new highs as a safe-haven amid tech volatility. Learn more about the XLV ETF here.
- [Stock picks in the health care equipment and services sector by Oppenheimer (IHF:NYSEARCA)](https://seekingalpha.com/news/4654303-stock-picks-in-the-health-care-equipment-and-services-sector-by-oppenheimer)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  Oppenheimer upgrades health care providers/services to overweight, citing a technical rebound and strong ETF gains.
- [Stock Market Today: Nasdaq 100 Rises as AI Chip Rout Reverses, SanDisk Jumps 7%](https://www.tradingview.com/news/benzinga:e9b29a8b4094b:0-stock-market-today-nasdaq-100-rises-as-ai-chip-rout-reverses-sandisk-jumps-7/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks diverged at midday Monday as a rebound in AI chip and infrastructure names lifted the Nasdaq 100 by 1.7% and the S&P 500 by 0.7%, while the Dow...
- [Healthcare ETFs to Buy as JNJ Slips 6% Despite Q3 Earnings Beat](https://finance.yahoo.com/healthcare/articles/healthcare-etfs-buy-jnj-slips-124600612.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Johnson & Johnson's Q3 earnings beat fails to prevent a 6% stock drop, but three healthcare ETFs offer diversified exposure to its growth potential.
- [Sector Update: Healthcare](https://finance.yahoo.com/healthcare/articles/sector-healthcare-171612833.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Healthcare stocks were lower Monday afternoon, with the NYSE Healthcare Index decreasing 0.7% and the State Street Health Care Select Sector SPDR ETF (XLV)...
- [Sector Update: Healthcare Stocks Decline Late Afternoon](https://finance.yahoo.com/healthcare/articles/sector-healthcare-stocks-decline-afternoon-195502048.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Healthcare stocks fell late Monday afternoon, with the NYSE Healthcare Index declining 0.7% and the State Street Health Care Select Sector SPDR ETF (XLV)...
- [Sector Update: Healthcare Stocks Softer Monday Afternoon](https://finance.yahoo.com/healthcare/articles/sector-healthcare-stocks-softer-monday-175237973.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Healthcare stocks fell Monday afternoon with the NYSE Healthcare Index declining 0.6% and the State Street Health Care Select Sector SPDR ETF (XLV) dropping...
- [Weekly Market Commentary](https://t.co/603IYOry11)  
  <sub>Howl.link, 23 hours ago</sub>  
  U.S. equities fell as the Nasdaq dropped 5.54% amid a sharp rotation from tech into defensive sectors.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 179.38 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 170.95 (+4.9%), 50d 170.42 (+5.3%), 200d 157.74 (+13.7%); 50d above 200d
Momentum: RSI(14) 68.7 | MACD 2.125 vs signal 1.084 (histogram 1.041)
Returns: 1d +2.1% | 5d +5.7% | 1m +6.1% | 3m +12.5%
52-week range: 142.84 - 179.38 (now 100.0% of the way up)
Volatility: ATR(14) 2.86 (1.6% of price) | annualised 20d 18.1%
Volume: 0.47x the 20-day average
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
Three-year record: +12.3% a year | beta to the market 0.52
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +5.0% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-10-12 RBC Capital: reit, Outperform -> Outperform
  - JNJ: 2026-10-16 Wells Fargo: main, Overweight -> Overweight
  - ABBV: 2026-10-13 RBC Capital: reit, Outperform -> Outperform
  - MRK: 2026-10-12 Citigroup: main, Neutral -> Neutral
  - UNH: 2026-10-20 RBC Capital: main, Outperform -> Outperform
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 197.42M | fund size: 35.41B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no policy surprise, mixed fundamentals, bullish technicals with low volume, flat fund flows, and analyst view bullish but limited coverage.

**Main reasons it gave:**
- Fed target unchanged at 4.0% with no policy surprise
- Technical indicators bullish but volume low (0.38x 20‑day average)
- Analyst coverage 54.4% of fund, 100% buy rating, price target +17.3% above current
- Fund flows flat, share count unchanged over 1 week and 1 month

<details><summary><b>News</b> — score +0.00</summary>

- [Should You Invest in the State Street Consumer Discretionary Select Sector SPDR ETF (XLY)?](https://finance.yahoo.com/markets/stocks/articles/invest-state-street-consumer-discretionary-092002564.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Launched on December 16, 1998, the State Street Consumer Discretionary Select Sector SPDR ETF (XLY) is a passively managed exchange traded fund designed to...
- [What State Street Consumer Discretionary SPDR (XLY) Sold: Amazon Leads on Oct. 16](https://finance.yahoo.com/markets/stocks/articles/state-street-consumer-discretionary-spdr-110450115.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Consumer Discretionary Select Sector SPDR ETF (XLY) was the sole fund in Friday's ETF activity,...
- [General Motors Sinks 6% Despite Earnings Beat and New Buyback as Outlook Narrows; Ford Slips, Tesla Barely Budges](https://247wallst.com/investing/2026/10/20/general-motors-sinks-8-despite-earnings-beat-and-new-buyback-as-outlook-narrows-ford-slips-tesla-barely-budges/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  General Motors (NYSE:GM | GM Price Prediction) coupled a Q3 2026 earnings beat with a fresh buyback, yet its full-year outlook is drawing sellers.
- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Tuesday as AI Stocks Retreat, Oil Prices Rise](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-130913751.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.2% and the actively tr.
- [Sector Update: Consumer](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-191424137.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Consumer stocks were mixed late Monday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) down 0.2% and the State Street...
- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://ca.finance.yahoo.com/news/exchange-traded-funds-higher-us-172542006.html)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.5%. US equity indexes rose amid...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 116.13 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 111.40 (+4.2%), 50d 113.69 (+2.1%), 200d 115.86 (+0.2%); 50d below 200d
Momentum: RSI(14) 64.3 | MACD 0.374 vs signal -0.291 (histogram 0.665)
Returns: 1d +1.5% | 5d +3.4% | 1m +3.5% | 3m +1.9%
52-week range: 105.66 - 124.52 (now 55.5% of the way up)
Volatility: ATR(14) 1.58 (1.4% of price) | annualised 20d 15.3%
Volume: 0.38x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 54.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.3% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, TJX
Recent rating changes among them:
  - AMZN: 2026-10-19 Morgan Stanley: main, Overweight -> Overweight
  - TSLA: 2026-10-20 Cantor Fitzgerald: reit, Overweight -> Overweight
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 120.25M | fund size: 13.96B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Argentina (ARGT) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 87.51 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 87.80 (-0.3%), 50d 91.43 (-4.3%), 200d 92.39 (-5.3%); 50d below 200d
Momentum: RSI(14) 43.1 | MACD -1.171 vs signal -1.329 (histogram 0.159)
Returns: 1d +0.6% | 5d -1.3% | 1m -5.3% | 3m -9.2%
52-week range: 70.49 - 102.94 (now 52.4% of the way up)
Volatility: ATR(14) 1.76 (2.0% of price) | annualised 20d 29.1%
Volume: 0.17x the 20-day average
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
Three-year record: +30.6% a year | beta to the market 0.45
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
Weighted price target: +32.0% above the current prices
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
Direction: money going out (1 month)
Share count change: 1 week: +0.2% (1.45M) over 7d | 1 month: -6.6% (-50.28M) over 31d
Shares outstanding: 8.15M | fund size: 713.14M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 47.74 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 46.84 (+1.9%), 50d 47.69 (+0.1%), 200d 46.86 (+1.9%); 50d above 200d
Momentum: RSI(14) 56.5 | MACD -0.012 vs signal -0.214 (histogram 0.202)
Returns: 1d +0.8% | 5d +2.0% | 1m +0.1% | 3m +1.1%
52-week range: 41.34 - 49.39 (now 79.5% of the way up)
Volatility: ATR(14) 0.51 (1.1% of price) | annualised 20d 13.4%
Volume: 0.10x the 20-day average
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
Three-year record: +19.0% a year | beta to the market 0.71
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
Weighted price target: +13.2% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 67.80M | fund size: 3.24B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Defense Stocks Are Tumbling as Wall Street Bets on a Democratic Sweep](https://247wallst.com/investing/2026/10/20/defense-stocks-are-tumbling-as-wall-street-bets-on-a-democratic-sweep/)  
  <sub>24/7 Wall St., 13 minutes ago</sub>  
  The ITA defense ETF has dropped 18% since August as Polymarket prices Democratic House control at 91%, with Northrop down 34% from its 52-week high.
- [L3Harris Technologies Looks Attractive as Defense Selloff Loses Steam: Chart of the Day](https://www.barrons.com/articles/l3harris-technologies-stock-attractive-defense-selloff-loses-steam-chart-8e00b267)  
  <sub>Barron's, 27 minutes ago</sub>  
  Despite multiple active conflicts stretching from Ukraine to the Middle East, defense stocks have been under pressure in recent months.
- [GE Aerospace Falls 4% Despite Earnings Beat and Raised Outlook as Costs Climb; RTX Edges Higher, Boeing Barely Moves](https://247wallst.com/investing/2026/10/20/ge-aerospace-falls-4-despite-earnings-beat-and-raised-outlook-as-costs-climb-rtx-edges-higher-boeing-barely-moves/)  
  <sub>24/7 Wall St., 1 hour ago</sub>  
  A beat-and-raise quarter from GE Aerospace (NYSE:GE | GE Price Prediction) is running into a jump in engine-related costs. GE Aerospace stock fell 4%,...
- [U.S. defense stocks rocked by prospect of Democratic midterm victory](https://en.fnnews.com/news/202610200401350280)  
  <sub>파이낸셜뉴스, 20 hours ago</sub>  
  [Financial News] A U.S. Patriot missile battery is deployed at the base of the 3rd Warsaw Anti-Aircraft Missile Brigade in Sochaczew, Poland, on Dec.
- [Palantir Rises 5% on Knox Partnership for Federal Cloud Software; Leidos Edges Higher, Booz Allen Hamilton Slips](https://247wallst.com/investing/2026/10/19/palantir-rises-5-on-knox-partnership-for-federal-cloud-software-leidos-edges-higher-booz-allen-hamilton-slips/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  Palantir jumped 5% after Knox Systems partnered to speed FedRAMP authorization, combining Knox's managed federal cloud path with Palantir's accredited...
- [Lockheed Martin stock flashes a risky pattern as two key threats emerge](https://invezz.com/uk/news/2026/10/20/lockheed-martin-stock-flashes-a-risky-pattern-as-two-key-threats-emerge/)  
  <sub>Invezz, 3 hours ago</sub>  
  Lockheed Martin stock is struggling this year as concerns about US politics and competition rise. After peaking at $683 in March, LMT dropped to the current...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 208.03 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 207.92 (+0.1%), 50d 221.47 (-6.1%), 200d 229.93 (-9.5%); 50d below 200d
Momentum: RSI(14) 42.0 | MACD -3.603 vs signal -4.723 (histogram 1.119)
Returns: 1d +0.1% | 5d +2.0% | 1m -3.8% | 3m -10.0%
52-week range: 198.23 - 253.22 (now 17.8% of the way up)
Volatility: ATR(14) 3.67 (1.8% of price) | annualised 20d 15.0%
Volume: 0.43x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Industrials
What it holds: P/E 31.87 | P/B 5.88 | P/S 2.95 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +25.0% a year | beta to the market 0.98
Cost and size: expense ratio 0.37% | net assets 12.14B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: GE Aerospace 21.0%, RTX Corp 16.2%, Boeing Co 7.5%, Howmet Aerospace Inc 4.6%, Lockheed Martin Corp 4.6%
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
Rolled up from the 5 largest holdings, 53.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.70 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.5% above the current prices
Holdings read: GE, RTX, BA, HWM, LMT
Recent rating changes among them:
  - GE: 2026-09-30 Wells Fargo: main, Overweight -> Overweight
  - RTX: 2026-10-15 RBC Capital: main, Outperform -> Outperform
  - BA: 2026-10-19 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - HWM: 2026-10-15 RBC Capital: main, Outperform -> Outperform
  - LMT: 2026-10-15 RBC Capital: main, Sector Perform -> Sector Perform
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
Direction: money going out (1 month)
Share count change: 1 week: -1.2% (-140.89M) over 7d | 1 month: -8.3% (-1.10B) over 31d
Shares outstanding: 58.03M | fund size: 12.07B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Should You Invest in the State Street Consumer Discretionary Select Sector SPDR ETF (XLY)?](https://finance.yahoo.com/markets/stocks/articles/invest-state-street-consumer-discretionary-092002564.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Launched on December 16, 1998, the State Street Consumer Discretionary Select Sector SPDR ETF (XLY) is a passively managed exchange traded fund designed to...
- [The S&P 500 Mirage: What Dalio, Damodaran & Burry See Beneath The Rally (NYSEARCA:SPY)](https://seekingalpha.com/article/4955491-the-s-and-p-500-mirage-what-dalio-damodaran-and-burry-see-beneath-the-rally)  
  <sub>Seeking Alpha, 39 minutes ago</sub>  
  I remain cautious on broad S&P 500 (SPY) exposure due to high concentration risk and AI-driven capital expenditure pressures.
- [BlackRock® Canada Announces October Cash Distributions for the iShares® ETFs](https://www.manilatimes.net/2026/10/20/tmt-newswire/globenewswire/blackrock-canada-announces-october-cash-distributions-for-the-ishares-etfs/2449460/amp)  
  <sub>The Manila Times, 6 hours ago</sub>  
  TORONTO, Oct. 20, 2026 (GLOBE NEWSWIRE) -- BlackRock Asset Management Canada Limited ('BlackRock Canada”), an indirect, wholly-owned subsidiary of BlackRock...
- [ValuEngine Weekly Market Commentary](https://seekingalpha.com/article/4955311-valuengine-weekly-market-commentary)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  US equity markets faced significant selling pressure this week, with sharp declines in tech and growth-oriented stocks contrasting with strong gains across...
- [BlackRock Canada Announces October 2026 Cash Distributions for iShares ETFs Listed on TSX and Cboe Canada](https://www.quiverquant.com/news/BlackRock+Canada+Announces+October+2026+Cash+Distributions+for+iShares+ETFs+Listed+on+TSX+and+Cboe+Canada)  
  <sub>Quiver Quantitative, 6 hours ago</sub>  
  BlackRock Canada announces October 2026 cash distributions for various iShares ETFs, payable on October 30, 2026. Quiver AI Summary.
- [Ball Stock: 11 Straight Green Days, Up 13%](https://www.trefis.com/stock/ball/articles/619335/ball-stock-11-straight-green-days-up-13/2026-10-20)  
  <sub>Trefis, 10 hours ago</sub>  
  Ball stock is on an 11-day winning streak, up 13.3% since the run began. That added about $2.0 billion to the company's market value, which now stands at...
- [26 ETFs Add to PPG Industries (PPG) on Oct. 16](https://www.gurufocus.com/news/9131215/26-etfs-add-to-ppg-industries-ppg-on-oct-16?utm_source=yahoo_finance&utm_medium=syndication&utm_campaign=headlines&r=caf6fe0e0db70d936033da5461e60141)  
  <sub>GuruFocus, 4 hours ago</sub>  
  ETF flows into PPG Industries turned positive last Friday after a single day of modest net selling, with a net $154.5 million added. Twenty-six ETFs bought...
- [What State Street Consumer Discretionary SPDR (XLY) Sold: Amazon Leads on Oct. 16](https://finance.yahoo.com/markets/stocks/articles/state-street-consumer-discretionary-spdr-110450115.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Consumer Discretionary Select Sector SPDR ETF (XLY) was the sole fund in Friday's ETF activity,...
- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance Singapore, 15 hours ago</sub>  
  Find the latest State Street Health Care Select Sector SPDR ETF (XLV) stock quote, history, news and other vital information to help you with your stock...
- [Weekly Market Commentary](https://t.co/603IYOry11)  
  <sub>Howl.link, 23 hours ago</sub>  
  U.S. equities fell as the Nasdaq dropped 5.54% amid a sharp rotation from tech into defensive sectors.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 51.19 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 49.69 (+3.0%), 50d 51.09 (+0.2%), 200d 50.92 (+0.5%); 50d above 200d
Momentum: RSI(14) 60.5 | MACD -0.015 vs signal -0.328 (histogram 0.313)
Returns: 1d +0.5% | 5d +2.9% | 1m +3.0% | 3m +0.7%
52-week range: 42.23 - 53.67 (now 78.3% of the way up)
Volatility: ATR(14) 0.71 (1.4% of price) | annualised 20d 13.0%
Volume: 0.45x the 20-day average
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
Three-year record: +11.2% a year | beta to the market 0.85
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.71 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.5% above the current prices
Holdings read: LIN, NEM, FCX, ECL, SHW
Recent rating changes among them:
  - LIN: 2026-10-15 RBC Capital: main, Outperform -> Outperform
  - NEM: 2026-10-19 Barclays: main, Overweight -> Overweight
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 71.92M | fund size: 3.68B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Weekly Market Commentary](https://t.co/603IYOry11)  
  <sub>Howl.link, 23 hours ago</sub>  
  U.S. equities fell as the Nasdaq dropped 5.54% amid a sharp rotation from tech into defensive sectors.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 110.72 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 111.42 (-0.6%), 50d 111.86 (-1.0%), 200d 113.43 (-2.4%); 50d below 200d
Momentum: RSI(14) 47.3 | MACD -0.326 vs signal -0.220 (histogram -0.106)
Returns: 1d +0.6% | 5d -1.4% | 1m -3.5% | 3m +1.4%
52-week range: 105.38 - 120.08 (now 36.3% of the way up)
Volatility: ATR(14) 1.71 (1.5% of price) | annualised 20d 16.3%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Communications
What it holds: P/E 16.28 | P/B 3.24 | P/S 2.42 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +18.8% a year | beta to the market 0.85
Cost and size: expense ratio 0.08% | net assets 22.53B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Meta Platforms Inc Class A 22.2%, Alphabet Inc Class A 11.6%, Alphabet Inc Class C 9.3%, Warner Bros. Discovery Inc Ordinary Shares - Class A 4.9%, The Walt Disney Co 4.5%
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
Rolled up from the 5 largest holdings, 52.5% of the fund by weight
Ratings by weight: buy 90.6% | hold 9.4% | sell 0.0% (mean 1.52 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.4% above the current prices
Holdings read: META, GOOGL, GOOG, WBD, DIS
Recent rating changes among them:
  - META: 2026-10-20 Rosenblatt: main, Buy -> Buy
  - GOOGL: 2026-10-19 Keybanc: main, Overweight -> Overweight
  - GOOG: 2026-10-15 JP Morgan: main, Overweight -> Overweight
  - WBD: 2026-09-29 Argus Research: down, Hold -> Sell
  - DIS: 2026-10-16 Citigroup: main, Buy -> Buy
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
Direction: money coming in (1 month)
Share count change: 1 week: +0.1% (13.22M) over 7d | 1 month: +2.9% (629.78M) over 31d
Shares outstanding: 204.22M | fund size: 22.61B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Cost of holding -8.4% annual (heavy roll cost)
- Fund outflows: -15.8% share count over past month
- Positioning: net long 22% of open interest, 100th percentile crowding
- Technical momentum modest: RSI 62.3, MACD histogram 0.009, volume 0.30x 20‑day average

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 12.26 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 11.90 (+3.0%), 50d 11.51 (+6.5%), 200d 10.13 (+21.0%); 50d above 200d
Momentum: RSI(14) 62.3 | MACD 0.287 vs signal 0.279 (histogram 0.009)
Returns: 1d +0.1% | 5d -1.0% | 1m +10.2% | 3m +26.1%
52-week range: 9.02 - 12.47 (now 93.9% of the way up)
Volatility: ATR(14) 0.20 (1.7% of price) | annualised 20d 22.6%
Volume: 0.30x the 20-day average
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
Cost of holding this fund instead of sugar itself: -8.4% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +26.1%, commodity +39.2%, gap -13.1% | 6 months: fund +33.0%, commodity +52.8%, gap -19.8% | 12 months: fund +24.0%, commodity +32.4%, gap -8.4%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 22.0% of open interest (1,179,144 contracts)
Change on the week: +0.2% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -2.6% (-1.39M) over 7d | 1 month: -15.8% (-9.93M) over 31d
Shares outstanding: 4.30M | fund size: 52.77M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals lack decisive break, but fundamentals and positioning are modestly bearish; overall uncertainty leads to a neutral call.

**Main reasons it gave:**
- Cost of holding fund is -7.2% per year, heavy roll cost for longs
- Positioning net long fell 4.4% week, indicating bearish shift
- Fund flows show net outflows over month (-13.4%)
- Crop condition stable with slight improvement (+2 points), indicating more supply
- Technicals show price below 20‑day and 50‑day SMAs, RSI 27.1, but no decisive break on volume

<details><summary><b>News</b> — score +0.00</summary>

- [Corn Starting Tuesday with a Slight Bounce](https://www.barchart.com/story/news/8229742/corn-starting-tuesday-with-a-slight-bounce)  
  <sub>Barchart.com, 3 hours ago</sub>  
  Corn prices are steady to 1 ¼ cents higher on Tuesday morning. Futures were disappointed in a 2 year low in export shipments, as contracts were down 1 ¼ to...
- [Corn Falls Out of Bed on Monday as Exports Disappoint](https://www.barchart.com/story/news/8207467/corn-falls-out-of-bed-on-monday-as-exports-disappoint)  
  <sub>Barchart.com, 17 hours ago</sub>  
  Corn futures were disappointed in a 2 year low in export shipments, as contracts were down 1 ¼ to 7 ¼ cents across the board. The CmdtyView national average...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 17.92 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 18.88 (-5.1%), 50d 19.24 (-6.9%), 200d 18.18 (-1.5%); 50d above 200d
Momentum: RSI(14) 27.1 | MACD -0.368 vs signal -0.251 (histogram -0.117)
Returns: 1d -0.5% | 5d -3.1% | 1m -11.6% | 3m -2.0%
52-week range: 16.47 - 20.29 (now 37.8% of the way up)
Volatility: ATR(14) 0.28 (1.6% of price) | annualised 20d 16.0%
Volume: 0.15x the 20-day average
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
Cost of holding this fund instead of corn itself: -7.2% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -2.0%, commodity +0.0%, gap -2.0% | 6 months: fund -1.5%, commodity +1.8%, gap -3.3% | 12 months: fund +2.1%, commodity +9.3%, gap -7.2%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.50</summary>

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
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 13.4% of open interest (1,845,260 contracts)
Change on the week: -4.4% of open interest
Crowding: 78% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +1.4% (1.75M) over 7d | 1 month: -13.4% (-19.80M) over 31d
Shares outstanding: 7.16M | fund size: 128.23M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Macro: inflation 3.7% and unemployment 4.2% on target, no surprise
- Technicals: price 39.72 just below 20‑day SMA, RSI 48.7, MACD near zero, no decisive break
- Positioning: net long 19.5% of OI, down 0.7% week‑over‑week
- Cost of holding: -5.2% annual roll cost, heavy negative for long
- Fund flows: net outflows of 6.2% over past month, indicating reduced demand

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 39.72 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 39.94 (-0.5%), 50d 39.86 (-0.4%), 200d 37.79 (+5.1%); 50d above 200d
Momentum: RSI(14) 48.7 | MACD -0.038 vs signal 0.019 (histogram -0.058)
Returns: 1d +0.4% | 5d -1.8% | 1m -2.3% | 3m +1.2%
52-week range: 30.53 - 41.43 (now 84.4% of the way up)
Volatility: ATR(14) 0.56 (1.4% of price) | annualised 20d 16.7%
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

```text
Cost of holding this fund instead of copper itself: -5.2% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +1.2%, commodity +2.5%, gap -1.3% | 6 months: fund +8.7%, commodity +10.2%, gap -1.5% | 12 months: fund +28.9%, commodity +34.1%, gap -5.2%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 19.5% of open interest (313,832 contracts)
Change on the week: -0.7% of open interest
Crowding: 15% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +1.7% (12.09M) over 7d | 1 month: -6.2% (-47.18M) over 31d
Shares outstanding: 18.05M | fund size: 716.97M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Bearish technicals and heavy roll cost suggest downside, but no clear macro surprise or decisive technical break, so the signal remains neutral.

**Main reasons it gave:**
- Cost of holding -5.5% annual, heavy roll cost
- Positioning net long 5.2% and down -2% week, crowding short
- Technicals price below 20‑day, 50‑day, 200‑day SMAs, RSI 40.7
- Macro: yields modestly higher, no surprise, VIX elevated

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 52.30 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 54.33 (-3.7%), 50d 57.50 (-9.0%), 200d 65.27 (-19.9%); 50d below 200d
Momentum: RSI(14) 40.7 | MACD -1.632 vs signal -1.422 (histogram -0.210)
Returns: 1d +1.5% | 5d -2.2% | 1m -12.3% | 3m -3.0%
52-week range: 42.40 - 105.60 (now 15.7% of the way up)
Volatility: ATR(14) 1.49 (2.9% of price) | annualised 20d 39.1%
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
Cost of holding this fund instead of silver itself: -5.5% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -3.0%, commodity -3.0%, gap -0.0% | 6 months: fund -23.6%, commodity -23.8%, gap +0.2% | 12 months: fund +11.3%, commodity +16.8%, gap -5.5%
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
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 5.2% of open interest (108,433 contracts)
Change on the week: -2.0% of open interest
Crowding: 8% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 341.45M | fund size: 17.86B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data HTTP 502: <html>
<head><title>502 Bad Gateway</title></head>
<body>
<center><h1>502 Bad Gateway</h1></center>
</body>
</html>


### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Macro data (inflation 3.7%, unemployment 4.2%) in line with expectations, no surprise
- Technicals: price near 52‑week high, RSI 38.6, MACD negative, low volume, no decisive break
- Fund flows: share count up 2.3% in the past week, modest inflows
- Crop condition: slight deterioration over 3 weeks (-1 point), marginally bullish

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 26.77 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 27.37 (-2.2%), 50d 27.12 (-1.3%), 200d 24.93 (+7.4%); 50d above 200d
Momentum: RSI(14) 38.6 | MACD -0.107 vs signal 0.015 (histogram -0.122)
Returns: 1d -0.0% | 5d -2.0% | 1m -4.8% | 3m +2.5%
52-week range: 21.71 - 28.14 (now 78.7% of the way up)
Volatility: ATR(14) 0.29 (1.1% of price) | annualised 20d 10.6%
Volume: 0.29x the 20-day average
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
Cost of holding this fund instead of soybeans itself: 0.2% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +2.5%, commodity +1.3%, gap +1.3% | 6 months: fund +8.2%, commodity +6.3%, gap +1.9% | 12 months: fund +22.7%, commodity +22.5%, gap +0.2%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 23.3% of open interest (1,072,235 contracts)
Change on the week: +0.3% of open interest
Crowding: 92% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +2.3% (1.02M) over 7d | 1 month: +1.7% (763.51K) over 31d
Shares outstanding: 1.69M | fund size: 45.12M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Technical price below 20‑day, 50‑day, and 200‑day SMAs indicating bearish trend
- Large speculators net short 7.3% of open interest, up 0.7% week
- Cost of holding -11.8% annual, heavy negative carry for longs
- US natural gas inventories built 67 BCF, 83% percentile (bearish supply signal)
- No macro surprise: Fed target unchanged, inflation 3.7% and unemployment 4.2%

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 10.36 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 10.80 (-4.1%), 50d 10.49 (-1.2%), 200d 11.26 (-8.0%); 50d below 200d
Momentum: RSI(14) 44.2 | MACD 0.057 vs signal 0.116 (histogram -0.059)
Returns: 1d -1.0% | 5d -9.2% | 1m +1.0% | 3m -2.3%
52-week range: 9.63 - 16.90 (now 10.0% of the way up)
Volatility: ATR(14) 0.36 (3.5% of price) | annualised 20d 45.2%
Volume: 0.25x the 20-day average
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
Cost of holding this fund instead of natural gas itself: -11.8% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -2.3%, commodity +1.9%, gap -4.2% | 6 months: fund -5.4%, commodity +10.5%, gap -15.9% | 12 months: fund -12.7%, commodity -0.9%, gap -11.8%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.50</summary>

```text
US inventories, week ending 2026-10-09 (published the following Wednesday)
  Natural gas: 3,567.0 billion cubic feet, +67.0 on the week (a build), 83% percentile over 52 weeks
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
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 7.3% of open interest (1,741,163 contracts)
Change on the week: +0.7% of open interest
Crowding: 12% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 12.08M | fund size: 125.20M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected)

### Oil (USO) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, no decisive technical break, and mixed fundamentals.

**Main reasons it gave:**
- CFTC positioning: net long 2.1% of OI, down 0.7% week‑over‑week (slight bearish tilt)
- EIA inventories: crude draw 8.6 M bbl (15th percentile) and diesel draw 2.5 M bbl (12th percentile) – bullish pressure
- EIA price outlook: WTI forecast $100 now vs USO price $158.5 – bearish outlook
- Technicals: price above 20‑day SMA, RSI 61, no decisive break

<details><summary><b>News</b> — score +0.00</summary>

- [United States Oil Fund, LP (USO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/USO/)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  Find the latest United States Oil Fund, LP (USO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Trump Administration's Last-Ditch Effort To Avoid A Global Diesel And Energy Crisis Failed](https://seekingalpha.com/article/4955413-trump-administrations-last-ditch-effort-to-avoid-global-diesel-and-energy-crisis-failed)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Global diesel and refined product shortages are mounting due to Middle East disruptions and Ukrainian attacks on Russian refining capacity.
- [Top Oil Analyst Warns Iran Escalation Risk Could Rise After Midterm Elections, Says ‘Finish-the-Job’ Camp](https://www.benzinga.com/markets/commodities/26/10/62462972/top-oil-analyst-warns-iran-escalation-risk-could-rise-after-midterm-elections-says-finish-the-job-camp-is-pushing-trump-as-brent-crude-hits-5-month-high)  
  <sub>Benzinga, 3 hours ago</sub>  
  Analyst warns U.S.-Iran tensions may escalate after midterms, threatening tanker routes, Strait of Hormuz traffic and global oil prices.
- [Sector Update: Energy Stocks Edge Higher Premarket Tuesday](https://ca.finance.yahoo.com/news/sector-energy-stocks-edge-higher-132507446.html)  
  <sub>Yahoo! Finance Canada, 2 hours ago</sub>  
  Energy stocks were edging higher premarket Tuesday, with the State Street Energy Select Sector SPDR ETF (XLE) advancing by 1%.
- [Oil Prices Diverge As Traders Weigh Russian Diesel Relief Against Saudi Supply Risks: USO, UCO, In Focus](https://stocktwits.com/news-articles/markets/equity/oil-prices-diverge-as-traders-weigh-russian-diesel-relief-against-saudi-supply-risks-uso-uco-in-focus/cZxBfVCRBoL)  
  <sub>Stocktwits, 15 hours ago</sub>  
  USO fell 1.5%, and UCO dropped 1.8%, while retail sentiment was 'neutral' on USO and 'bullish' on UCO. Brent futures declined nearly 1.5%, while WTI futures...
- [GraniteShares launches 4x leveraged commodity ETPs as oil scrapes the $100 mark again](https://www.etfstream.com/articles/graniteshares-launches-4x-leveraged-commodity-etps-as-oil-scrapes-the-usd100-mark-again)  
  <sub>ETF Stream, 24 hours ago</sub>  
  US short and leveraged specialist GraniteShares is making its debut in the commodity segment with three new exchange-traded products (ETPs) designed to...
- [CVX, XOM Stocks Hit 52-Week Highs: What's Fueling The Surge? - Chevron (NYSE:CVX)](https://www.benzinga.com/markets/equities/26/10/62458379/chevron-exxonmobil-stocks-hit-52-week-highs-as-fresh-us-israel-threats-against-iran-push-brent-crude-to-5-month-highs)  
  <sub>Benzinga, 8 hours ago</sub>  
  Chevron and Exxon hit 52-week highs as Iran tensions drove oil above $110, raising fears of Middle East supply disruptions.
- [Crude closes mixed after Houthis claim more attacks on Saudi airports, oil facilities (USO:NYSEARCA)](https://seekingalpha.com/news/4654447-crude-closes-mixed-after-houthis-claim-more-attacks-on-saudi-airports-oil-facilities)  
  <sub>Seeking Alpha, 15 hours ago</sub>  
  Crude oil futures closed mixed following attacks by Yemen's Iran-aligned Houthis on a ‌Yemeni military training camp and renewed attacks on Saudi energy,...
- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://ca.finance.yahoo.com/news/exchange-traded-funds-higher-us-172542006.html)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.5%. US equity indexes rose amid...
- [USO Oct 2026 162.000 call (USO261021C00162000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/USO261021C00162000/chart/)  
  <sub>Yahoo! Finance Canada, 23 hours ago</sub>  
  Interactive Chart for USO Oct 2026 162.000 call (USO261021C00162000), analyze all the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 158.51 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 150.57 (+5.3%), 50d 144.19 (+9.9%), 200d 120.17 (+31.9%); 50d above 200d
Momentum: RSI(14) 61.4 | MACD 3.862 vs signal 2.934 (histogram 0.928)
Returns: 1d -1.4% | 5d +3.5% | 1m +7.0% | 3m +20.4%
52-week range: 66.17 - 161.86 (now 96.5% of the way up)
Volatility: ATR(14) 5.01 (3.2% of price) | annualised 20d 35.3%
Volume: 0.98x the 20-day average
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

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.15</summary>

```text
US inventories, week ending 2026-10-09 (published the following Wednesday)
  Crude oil: 415.6 million barrels, -8.6 on the week (a draw), 15% percentile over 52 weeks
  Petrol: 208.3 million barrels, +3.5 on the week (a build), 21% percentile over 52 weeks
  Diesel: 102.6 million barrels, -2.5 on the week (a draw), 12% percentile over 52 weeks -- low for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

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

<details><summary><b>Buying and selling by company insiders</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.15</summary>

```text
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 2.1% of open interest (1,900,179 contracts)
Change on the week: -0.7% of open interest
Crowding: 35% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 10d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 119.10M | fund size: 18.88B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Treasury yields moved modestly; Fed target unchanged (no macro surprise)
- Price 23.66 below 20‑day SMA 24.72 and 50‑day SMA 25.56; RSI 31.6, MACD negative (no decisive technical break)
- Large speculators net short 6.4% of OI, down 0.6% week‑over‑week (positioning not extreme)
- Cost of holding -11.8% annual, heavy carry but structural (no directional signal)

<details><summary><b>News</b> — score +0.00</summary>

- [WEAT Mar 2027 30.000 call (WEAT270319C00030000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/WEAT270319C00030000/chart/)  
  <sub>Yahoo! Finance Canada, 23 hours ago</sub>  
  Interactive Chart for WEAT Mar 2027 30.000 call (WEAT270319C00030000), analyze all the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 23.66 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 24.72 (-4.3%), 50d 25.56 (-7.4%), 200d 23.44 (+0.9%); 50d above 200d
Momentum: RSI(14) 31.6 | MACD -0.490 vs signal -0.391 (histogram -0.099)
Returns: 1d -0.9% | 5d -2.6% | 1m -10.1% | 3m -9.0%
52-week range: 19.88 - 28.00 (now 46.6% of the way up)
Volatility: ATR(14) 0.45 (1.9% of price) | annualised 20d 16.9%
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
Cost of holding this fund instead of wheat itself: -11.8% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -9.0%, commodity -8.1%, gap -0.9% | 6 months: fund +2.2%, commodity +7.1%, gap -5.0% | 12 months: fund +16.8%, commodity +28.7%, gap -11.8%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 6.4% of open interest (506,774 contracts)
Change on the week: -0.6% of open interest
Crowding: 58% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +1.6% (4.38M) over 7d | 1 month: -13.8% (-44.90M) over 31d
Shares outstanding: 11.82M | fund size: 279.75M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Forget GLD. Investors Sent $500 Million to the Cheaper SPDR Gold Fund](https://247wallst.com/investing/etf/2026/10/19/forget-gld-investors-sent-500-million-to-the-cheaper-spdr-gold-fund/)  
  <sub>24/7 Wall St., 17 hours ago</sub>  
  Investors poured half a billion dollars into a gold fund that most people have never heard of, bypassing the world's most famous bullion ETF for a quiet...
- [Behavioral Patterns of GLD and Institutional Flows](https://news.stocktradersdaily.com/news_release/10/Behavioral_Patterns_of_GLD_and_Institutional_Flows_102026033602_1792481762.html)  
  <sub>Stock Traders Daily, 12 hours ago</sub>  
  Price-action only: Spdr Gold Shares Etf (GLD) movements set the tone for institutional models. Behavioral Patterns of GLD and Institutional Flows.
- [Form 4 Yorkville America Investment Trust For: 20 October By Investing.com](https://ca.investing.com/news/stock-market-news/form-4-yorkville-america-investment-trust-for-20-october-93CH-4890118)  
  <sub>Investing.com Canada, 5 hours ago</sub>  
  Karen Shupe Commonwealth Fund Services, Inc. 8730 Stony Point Parkway, Suite 205. Richmond, VA 23235 (804) 267-7400. (Address and Telephone Number of...
- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://ca.finance.yahoo.com/news/exchange-traded-funds-higher-us-172542006.html)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.5%. US equity indexes rose amid...
- [GLD NTA 19-10-2026 $3.88928](https://www.businessdesk.co.nz/nzx-announcements/gld-etf-units/482032/)  
  <sub>BusinessDesk | NZ, 18 hours ago</sub>  
  View the full NZX announcement for Smart Gold ETF (GLD): GLD NTA 19-10-2026 $3.88928. Financial updates and company disclosures on BusinessDesk.
- [Inflation Heats Up, Silver Sinks - What Is The Market Telling Us?](https://seekingalpha.com/article/4955257-inflation-heats-up-silver-sinks-what-market-telling-us)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Price inflation is accelerating again, yet gold and silver have been struggling. Silver showed some early improvement Monday morning, reaching $58.
- [India Gold Market Flips To Premium As Demand Improves And Supplies Tighten](https://seekingalpha.com/article/4955224-india-gold-market-flips-premium-demand-improves-supplies-tighten)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Gold traded at a premium in India last week for the first time in three months. This reflects the combined effect of tightening supply and improving demand.
- [United States Oil Fund, LP (USO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/USO/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Find the latest United States Oil Fund, LP (USO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Cboe extends trading hours to single-stock and ETF options](https://www.thetradenews.com/cboe-extends-trading-hours-to-single-stock-and-etf-options/)  
  <sub>The TRADE, 1 hour ago</sub>  
  Cboe has expanded its offering for select multi-listed equity and exchange-traded fund (ETF) options, which are now available to trade during extended...
- [NYSE introduces extended trading hours for NYSE American options](https://qz.com/nyse-extended-trading-hours-american-options-102026)  
  <sub>Quartz, 2 hours ago</sub>  
  An early session runs 7:30 a.m. to 9:25 a.m. ET and a late session runs 4:00 p.m. to 4:15 p.m. ET for eligible symbols.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.08% (+0.02 on the week) | 5-year 4.89% (-0.12 on the week) | 10-year 5.08% (-0.14 on the week) | 30-year 5.41% (-0.15 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 101.57 (-0.61 on the week)
Volatility (VIX): 17.63 (+2.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.74% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 379.36 (bar of 2026-10-20), from 501 daily bars
Trend: vs 20d SMA 382.35 (-0.8%), 50d 396.34 (-4.3%), 200d 414.80 (-8.5%); 50d below 200d
Momentum: RSI(14) 43.3 | MACD -4.026 vs signal -4.472 (histogram 0.445)
Returns: 1d -0.1% | 5d -0.6% | 1m -4.8% | 3m +0.1%
52-week range: 362.32 - 495.90 (now 12.8% of the way up)
Volatility: ATR(14) 5.71 (1.5% of price) | annualised 20d 20.9%
Volume: 0.39x the 20-day average
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
Measured: 3 months: fund +0.1%, commodity +0.3%, gap -0.2% | 6 months: fund -11.7%, commodity -11.8%, gap +0.1% | 12 months: fund -2.5%, commodity -1.2%, gap -1.3%
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
Contract: GOLD - COMMODITY EXCHANGE INC. (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 27.0% of open interest (396,345 contracts)
Change on the week: -1.0% of open interest
Crowding: 50% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 260.30M | fund size: 98.75B
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

