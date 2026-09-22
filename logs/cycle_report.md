# Daily report

**22 Sep 2026, 18:45 Israel time (15:45 UTC)** · 80 names checked · 2 traded · 0 with a problem

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 1 | 15 | 0 |
| Whole-market funds | 14 | 0 | 14 | 0 |
| Sector and country funds | 41 | 2 | 39 | 0 |
| Commodities | 9 | 1 | 8 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| Nvidia (NVDA) · Company | **Sold part.** Sold 7 of 23 shares at +1.04R, 16 still held. Stop-loss raised 212.84 → 216.23. |
| Alphabet (Google) (GOOGL) · Company | **Stop raised.** At +0.74R, following the price. Stop-loss raised 338.00 → 341.79. |
| Eli Lilly (LLY) · Company | **Stop raised.** At +0.43R, following the price. Stop-loss raised 1105.32 → 1113.34. |
| Microsoft (MSFT) · Company | **Stop raised.** At +0.23R, following the price. Stop-loss raised 471.19 → 474.94. |
| Novo Nordisk (NVO) · Company | **Stop raised.** At +0.09R, following the price. Stop-loss raised 42.61 → 42.26. |
| US dollar (UUP) · Index fund | **Stop raised.** At +0.56R, following the price. Stop-loss raised 28.23 → 28.30. |
| US government bonds, 7-10 years (IEF) · Index fund | **Problem.** Could not be managed: BrokerError: replace_order failed for 32c29f09-baec-438c-8305-6a67e9ec01b1: {"code":42210000,"message":"order parameters are not changed"} |
| Teva Pharmaceutical (TEVA) · Company | **Problem.** Could not be managed: BrokerError: replace_order failed for aae42775-8f36-4d39-8228-5fe42162cef5: {"code":42210000,"message":"qty cannot be changed for advanced orders"} |
| US inflation-linked bonds (TIP) · Index fund | **Problem.** Could not be managed: BrokerError: replace_order failed for 1f8497f7-ba59-40ac-8e2c-7506f8fd35e0: {"code":42210000,"message":"order parameters are not changed"} |
| US government bonds, 20+ years (TLT) · Index fund | **Problem.** Could not be managed: BrokerError: replace_order failed for 63f75c03-a0f4-40d6-8e7f-75dec0e75a06: {"code":42210000,"message":"order parameters are not changed"} |
| Developing country bonds (EMB) · Index fund | **Holding.** -0.54R, holding 128 shares. Stop-loss 94.05. |
| Gold (GLD) · Commodity | **Holding.** -0.51R, holding 10 shares. Stop-loss 404.87. |
| US government bonds, 7-10 years (IEF) · Index fund | **Holding.** -0.03R, holding 131 shares. Stop-loss 91.61. |
| S&P 500, equal weight (RSP) · Index fund | **Holding.** -0.16R, holding 14 shares. Stop-loss 215.78. |
| US inflation-linked bonds (TIP) · Index fund | **Holding.** +0.48R, holding 10 shares. Stop-loss 106.08. |
| US government bonds, 20+ years (TLT) · Index fund | **Holding.** -0.51R, holding 147 shares. Stop-loss 82.41. |
| US shopping and leisure (XLY) · Sector or country | **Holding.** -0.67R, holding 63 shares. Stop-loss 113.36. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### ASML (ASML) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> News is mostly generic AI-ecosystem commentary, but the tape is firm: +8.5% over 5 days, 50d above 200d, MACD histogram turning positive, and Samsung High-NA EUV plus a \u20ac12bn buyback give a real company-specific support. Fundamentals are strong (21% revenue growth, 54% ROE, low leverage) though richly valued at 59x trailing, and earnings on 2026-10-14 is close enough to add event risk. Consensus is strong buy with ~23% upside to target, but that prior is already priced and there are no fresh rating changes. Volume at 0.29x average and an 8.5% weekly run argue for modest conviction rather than chasing.

**Main reasons it gave:**
- +8.5% 5-day return, price above 20d/50d/200d with 50d>200d golden-cross structure
- MACD histogram positive (+5.36) while RSI still neutral at 53.5
- Samsung High-NA EUV plans and \u20ac12bn buyback cited as company-specific support
- Revenue +21.3%, earnings +28.5% YoY, ROE 53.9%, debt/equity 9.1%
- Earnings 2026-10-14 approaching; record is 2 beats, 1 in line, 1 miss
- Volume only 0.29x 20-day average and trailing P/E 59 limit conviction

<details><summary><b>News</b> — score +0.30</summary>

- [Nvidia and AMD Can't Make AI Chips Without This Growth Stock. Here's Why It Could Soar.](https://finance.yahoo.com/technology/ai/articles/nvidia-amd-cant-ai-chips-123500916.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  ASML is one of the most important companies in the AI semiconductor ecosystem.
- [ASML (ASML) Surpasses Market Returns: Some Facts Worth Knowing](https://finance.yahoo.com/markets/stocks/articles/asml-asml-surpasses-market-returns-214505850.html)  
  <sub>Yahoo Finance, 17 hours ago</sub>  
  In the latest close session, ASML (ASML) was up +1.87% at $1,711.32. The stock outperformed the S&P 500, which registered a daily gain of 1.49%.
- [ASML Watch: What ASML Holding's Latest Moves Mean for Technology Stocks Investors](https://kalkinemedia.com/us/stocks/technology/asml-watch-what-asml-holdings-latest-moves-mean-for-technology-stocks-investors)  
  <sub>Kalkine Media, 9 hours ago</sub>  
  Chip-spending caution brought critical equipment suppliers into focus. ASML Holding brings a company-specific advanced semiconductor manufacturing equipment...
- [S&P 500, Dow Edge Higher As Bank Earnings Offset Middle East Oil Concerns — AAPL, SKHY, ASML, PYPL In Focus](https://www.google.com/goto?url=CAES4gEB6zswFX0uiOQ-ibSpj4fT9BYQZL9twfyjn4QY8hG6bxgF92VlgkQLWPC9IoPtuQhpj4_HsZu-_rAxEIzJjBWdqiwXVEfnYJh0-RUn-zUh9oegHhFSGxz4rJUwjRcM9dtJONb1nluUT5Bf7BEax6a4ptL9J4P2j5f0RXjLcbHTQoO68gnwgoDjU_TE7YfjZRb09IfF_zT_s5pA05FO9HsJieOtGZ-lNZwM40SgUwE-T9you7iM4kXWiHg_UFAUVdvbUAPCmHiyCJVqNXtsO7c75qJX6t2xYmqtUJa5NWAl_ttI)  
  <sub>Stocktwits, 20 hours ago</sub>  
  Cooler-than-expected producer prices contributed to hopes for easing inflation on Wednesday.
- [Here's How Much $1000 Invested In ASML Holding 15 Years Ago Would Be Worth Today](https://www.benzinga.com/news/26/09/61899618/here-s-how-much-1000-invested-asml-holding-15-years-ago-would-be-worth-today)  
  <sub>Benzinga, 24 hours ago</sub>  
  ASML Holding (NASDAQ:ASML) has outperformed the market over the past 15 years by 13.41% on an annualized basis producing an average annual return of 26.75%.
- [ASML stock ends the day 3.08 percent higher at USD 1,679.92](https://www.ad-hoc-news.de/boerse/news/nebenwerte/asml-stock-ends-the-day-3-08-percent-higher-at-usd-1-679-92/70147430)  
  <sub>AD HOC NEWS, 18 hours ago</sub>  
  At the close on September 21, 2026, ASML stock finished at USD 1679.92 on Nasdaq, up 3.08 percent. The shares traded between USD 1635.00 and USD 1684.80 on...
- [ASML Stock Rises on AI Rally and Samsung EUV Plans](https://www.markets.com/news/asml-stock-rises-ai-rally-samsung-high-na-euv)  
  <sub>Markets.com, 23 hours ago</sub>  
  ASML stock rose 3% as semiconductor shares rallied. Samsung's High-NA EUV plans, stronger chip demand and a €12 billion buyback support the outlook.
- [AMD, TER Stocks Jump After Goldman Sachs Lifts Price Targets](https://stocktwits.com/news-articles/markets/equity/amd-ter-stocks-jump-after-goldman-sachs-lifts-price-targets/cZm18P6R7lx)  
  <sub>Stocktwits, 17 hours ago</sub>  
  Shares of Teradyne, Inc. (TER) and Advanced Micro Devices Inc. (AMD) jumped on Monday after Goldman Sachs raised its price targets on both semiconductor...
- [ASML Adds 1% as 110 EUV Tools Test Factory Throughput](https://finance.yahoo.com/technology/articles/asml-adds-1-110-euv-194501828.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  This article first appeared on GuruFocus. ASML Holding (NASDAQ:ASML), the advanced-lithography equipment leader, faced a very different AI-chip bottleneck:...
- [ASML Holding stock gains 1.87 percent as earnings near](https://www.ad-hoc-news.de/boerse/news/corporate-news/asml-holding-stock-gains-1-87-percent-as-earnings-near/70153396)  
  <sub>AD HOC NEWS, 6 hours ago</sub>  
  ASML Holding stock closed at USD 1711.32 on September 21, 2026, up 1.87 percent. Zacks expects USD 12.59 EPS for Q3 2026.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.45</summary>

```text
Last close 1,727.28 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 1,686.13 (+2.4%), 50d 1,720.45 (+0.4%), 200d 1,515.41 (+14.0%); 50d above 200d
Momentum: RSI(14) 53.5 | MACD -16.766 vs signal -22.121 (histogram 5.356)
Returns: 1d +0.9% | 5d +8.5% | 1m -2.1% | 3m -2.9%
52-week range: 936.19 - 1,989.44 (now 75.1% of the way up)
Volatility: ATR(14) 54.44 (3.2% of price) | annualised 20d 40.2%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 663.45B
Valuation: trailing P/E 59.38 | forward P/E 29.10 | P/B 1,471.33 | PEG 1.54
Profitability: profit margin 30.1% | operating margin 37.1% | ROE 53.9%
Growth (YoY): revenue +21.3% | earnings +28.5%
Balance sheet: debt/equity 9.1% | free cash flow 8.44B
Risk: beta 1.36 | short interest 0.4% of float
Next earnings: 2026-10-14
```

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.40</summary>

```text
Earnings record, last 4 quarters: 2 beats, 1 in line, 1 missed
  2026-06-30 beat by 9% | 2026-03-31 beat by 7% | 2025-12-31 missed by 5% | 2025-09-30 in line
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

```text
Consensus: strong_buy (mean 1.40 on a 1=strong buy to 5=strong sell scale, 16 analysts)
Ratings: 7 strong buy, 31 buy, 3 hold, 1 sell, 0 strong sell
Price target: mean 2,129.07 (+23.3% vs last close), range 885.37 - 2,835.12
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

### Elbit Systems (ESLT) · Company — NEUTRAL, confidence 0.42

**In the model's own words:**

> ESLT presents conflicting signals that argue for a neutral stance. The fundamental picture is attractive: strong 34.2% YoY earnings growth, consistent 4-quarter beat streak, modest leverage (19.3% debt/equity), and solid 15.2% ROE support the business quality. However, the valuation is stretched at 55.5x trailing P/E and 40.2x forward P/E for an aerospace & defense name, leaving limited margin for error. Technicals show a stock below both its 50d and 200d moving averages (-3.2% and -3.5% respectively), with momentum deteriorating (RSI at 48.9, MACD histogram positive but from deeply negative levels). The analyst consensus of Hold with a mean target 10.6% above the current price reflects cautious optimism, but no fresh rating changes suggest conviction is absent; the wide target range (518-960) indicates disagreement. Insider activity is mixed and weak: April sales by the CEO and officers were likely related to compensation vesting or planned diversification rather than a bearish signal, but the lack of any buying in the past 180 days offers no countervailing support. Volume is running 0.75x average, suggesting thin conviction even from long holders. The lack of any news catalyst and the proximity of earnings (60+ days out) mean near-term price action will be driven by technicals and sentiment rather than fresh information. Low conviction reflects the conflicting dimensions and lack of a clear directional catalyst.

**Main reasons it gave:**
- Stretched trailing P/E of 55.5x despite 34% earnings growth limits upside room
- Four consecutive earnings beats suggest execution capability but gains already priced in
- Trading below 50d and 200d moving averages with deteriorating momentum signals
- Hold consensus with modest 10.6% mean upside implies limited near-term catalyst
- No insider buying in 180 days while officers sold in April, neutral rather than bullish signal

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 738.10 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 722.27 (+2.2%), 50d 762.20 (-3.2%), 200d 765.16 (-3.5%); 50d below 200d
Momentum: RSI(14) 48.9 | MACD -4.964 vs signal -11.114 (histogram 6.151)
Returns: 1d -1.7% | 5d +0.9% | 1m -0.4% | 3m -4.4%
52-week range: 454.95 - 1,014.33 (now 50.6% of the way up)
Volatility: ATR(14) 16.87 (2.3% of price) | annualised 20d 15.8%
Volume: 0.75x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.55</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 34.59B
Valuation: trailing P/E 55.54 | forward P/E 40.20 | P/B 7.83 | PEG n/a
Profitability: profit margin 7.4% | operating margin 9.6% | ROE 15.2%
Growth (YoY): revenue +15.9% | earnings +34.2%
Balance sheet: debt/equity 19.3% | free cash flow -38.48M
Risk: beta -0.30 | short interest 0.8% of float
Next earnings: 2026-11-24
```

</details>

<details><summary><b>What this fund holds</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.55</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 10% | 2026-03-31 beat by 16% | 2025-12-31 beat by 16% | 2025-09-30 beat by 21%
```

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

<details><summary><b>What analysts and big funds say</b> — score +0.15</summary>

```text
Consensus: hold (mean 2.67 on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 816.33 (+10.6% vs last close), range 518.00 - 960.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.15</summary>

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

### JPMorgan Chase (JPM) · Company — NEUTRAL, confidence 0.42

**In the model's own words:**

> JPM presents a complex near-term picture. Fundamentally, the bank is in excellent shape: 4 consecutive earnings beats, strong YoY growth (revenue +30.4%, earnings +46.9%), attractive valuation (forward P/E 13.59), and a 17.8% ROE. The $20B QIA partnership for asset management is a positive strategic catalyst. However, technicals are deteriorating: the stock has fallen 3.6% in one day and 3.7% over 5 days, trading 4% below both its 20-day and 50-day moving averages, with RSI at 35 (oversold territory) and a negative MACD histogram of -1.529. Volume is light at 0.45x the 20-day average, suggesting the selloff lacks conviction but also lacks buying support. The analyst consensus is solidly bullish (mean 2.12, 10.6% upside to target), yet this prior is already reflected in the price and provides limited edge. Insider activity shows net buying of 738,651 shares but this came from 22 transactions spread over 6 months—not a concentrated, urgent signal. The recent news is mixed: the QIA deal is positive, but today's decline appears tactical (Dow weakness, sector headwinds) rather than fundamental. With earnings not due until October 13, the near-term driver is technicals, which argue for caution. The conflicting signals—solid fundamentals and analyst backing versus technical weakness and light volume—warrant a neutral stance with moderate conviction until either the technical picture stabilizes or new catalysts emerge.

**Main reasons it gave:**
- 4 consecutive earnings beats and +46.9% YoY earnings growth
- RSI 35 and price 4% below 20d/50d SMA, suggesting technical weakness
- Forward P/E 13.59 and 17.8% ROE support valuation strength
- $20B QIA partnership expands asset management footprint
- Volume 0.45x 20-day average indicates light conviction behind selloff

<details><summary><b>News</b> — score +0.30</summary>

- [Dow Falls 134 Points On Losses For Shares Of Cisco, JPMorgan Chase](https://www.moomoo.com/news/post/1000033490/dow-falls-134-points-on-losses-for-shares-of-cisco)  
  <sub>Moomoo, 57 minutes ago</sub>  
  Thisarticle was automatically generated by MarketWatch using technology from Automated Insights. The Dow Jones Industrial Average is falling Tuesday morning...
- [Will JPM's $20B QIA Partnership Strengthen Asset Management Business?](https://www.zacks.com/stock/news/2993826/will-jpms-20b-qia-partnership-strengthen-asset-management-business)  
  <sub>Zacks Investment Research, 34 minutes ago</sub>  
  JPM will manage a $15 billion public equities mandate and launch a $5 billion private-markets initiative. The partnership could expand JPMAM's institutional...
- [Is JPMorgan Chase (NYSE:JPM) Stock Worth Watching Today?](https://kalkinemedia.com/us/stocks/bluechip/is-jpmorgan-chase-nysejpm-stock-worth-watching-today)  
  <sub>Kalkine Media, 2 hours ago</sub>  
  JPMorgan Chase (NYSE:JPM) enters Monday with banking activity as regulators examine trading-firm exposures.
- [JPMorgan Raises its Dividend: A Look at Yield, Capital, and Shareholder Returns](https://finance.yahoo.com/markets/stocks/articles/jpmorgan-raises-dividend-look-yield-015332265.html)  
  <sub>Yahoo Finance, 13 hours ago</sub>  
  JPMorgan Chase & Co. (NYSE:JPM)'s latest dividend increase gives shareholders another reason to focus on the bank's ability to return capital while...
- [Brazil stocks break electoral pattern amid tighter race, J.P. Morgan says](https://valorinternational.globo.com/markets/news/2026/09/22/brazil-stocks-break-electoral-pattern-amid-tighter-race-jp-morgan-says.ghtml)  
  <sub>Valor International, 4 hours ago</sub>  
  Since July 1, when Flávio Bolsonaro reached his lowest point on betting platforms, MSCI Brazil has risen by an average of 0.20% on each day the candidate...
- [Why Did IMAX, JPM, CSX Stocks Surge To 52-Week Highs Last Week?](https://stocktwits.com/news-articles/markets/equity/imax-jpm-csx-stocks-52-week-highs-last-week/cZZxcQ3R7C3)  
  <sub>Stocktwits, 21 hours ago</sub>  
  Citi raised the price target on CSX to $54 from $53 and maintained a Neutral rating on the shares, implying an upside of about 1.5% from its last close.
- [Bcwm LLC Sells 3,763 Shares of JPMorgan Chase & Co. $JPM](https://www.marketbeat.com/instant-alerts/filing-bcwm-llc-sells-3763-shares-of-jpmorgan-chase-co-jpm-2026-09-22/)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Bcwm LLC reduced its position in shares of JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 13.5% in the 2nd quarter, according to its most recent filing...
- [JPM: AI Investment Surge May Reach $1 Trillion, Says JPMorgan CE](https://www.gurufocus.com/news/9091131/jpm-ai-investment-surge-may-reach-1-trillion-says-jpmorgan-ceo-jamie-dimon)  
  <sub>GuruFocus, 8 hours ago</sub>  
  On September 22, 2026, JPMorgan CEO Jamie Dimon highlighted the ongoing surge in artificial intelligence (AI) investments, predicting that spending within...
- [JP Morgan Sees Brent Staying in Low $100s Even if Hormuz Reopens in June](https://energynow.com/2026/05/jp-morgan-sees-brent-staying-in-low-100s-even-if-hormuz-reopens-in-june/)  
  <sub>EnergyNow.com, 12 hours ago</sub>  
  (Reuters) - JP Morgan expects Brent crude to remain in the low-$100s for much of…
- [A lithium producer plans to reach 830,000 tonnes of capacity](https://www.stocktitan.net/news/SGML/sigma-lithium-announces-j-p-morgan-initiated-equity-research-le3evuou77nu.html)  
  <sub>Stock Titan, 17 hours ago</sub>  
  J.P. Morgan sees a lithium deficit through 2029 as Sigma expects 240000 tonnes of concentrate within 12 months and 330000 tonnes in FY27.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.55</summary>

```text
Last close 339.50 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 353.65 (-4.0%), 50d 353.61 (-4.0%), 200d 320.89 (+5.8%); 50d above 200d
Momentum: RSI(14) 35.0 | MACD -1.834 vs signal -0.305 (histogram -1.529)
Returns: 1d -3.6% | 5d -3.7% | 1m -3.4% | 3m +1.6%
52-week range: 282.84 - 365.18 (now 68.8% of the way up)
Volatility: ATR(14) 7.13 (2.1% of price) | annualised 20d 18.1%
Volume: 0.45x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.75</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 902.45B
Valuation: trailing P/E 14.55 | forward P/E 13.59 | P/B 2.55 | PEG 1.63
Profitability: profit margin 34.9% | operating margin 50.4% | ROE 17.8%
Growth (YoY): revenue +30.4% | earnings +46.9%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.97 | short interest 1.0% of float
Next earnings: 2026-10-13
```

</details>

<details><summary><b>What this fund holds</b> — score +0.75</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.75</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 4% | 2026-03-31 beat by 8% | 2025-12-31 beat by 3% | 2025-09-30 beat by 4%
```

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.75</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.75</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.75</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.65</summary>

```text
Consensus: buy (mean 2.12 on a 1=strong buy to 5=strong sell scale, 21 analysts)
Ratings: 4 strong buy, 9 buy, 10 hold, 0 sell, 1 strong sell
Price target: mean 375.38 (+10.6% vs last close), range 305.00 - 436.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.65</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.15</summary>

```text
Last 180 days: bought 969,320 shares in 22 transaction(s) | sold 230,669 shares in 20
Net: +738,651 shares (+7.7% of insider holdings) | insiders hold 10,393,508 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-10 LEOPOLD ROBIN (Officer): 2,500 shares, 882.03K
  - 2026-08-11 LEOPOLD ROBIN (Officer): 2,500 shares, 903.52K
  - 2026-06-22 FRIEDMAN STACEY R. (General Counsel): 5,467 shares, 1.81M
  - 2026-05-20 FRIEDMAN STACEY R. (General Counsel): 5,468 shares, 1.64M
(11 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.15</summary>

_Not available today._

</details>

### Caterpillar (CAT) · Company — NEUTRAL, confidence 0.40

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> CAT has a strong fundamental story — 4 straight beats, +24% revenue, data-center power demand past a $72B backlog — but the tape is soft: -18% over three months, below the 50d SMA, RSI 47, volume a quarter of normal. News flow is mostly filler (a cat-names listicle, a Red Cat insider story, unrelated MRNA), and the only fresh analyst action is a Bernstein Hold reiteration. Valuation is rich (34.7x trailing, 19x book, 233% debt/equity) and insider flow is 8 sellers vs 1 token director buy. Bullish fundamentals against a broken short-term trend equals low conviction; no tradable edge for the next few days.

**Main reasons it gave:**
- 4 consecutive EPS beats, most recent by 31%; revenue +24% YoY
- CEO cites demand exceeding $72B backlog on data-center power
- Price -18.1% over 3 months, below 50d SMA, RSI 47, volume 0.25x average
- Bernstein maintains Hold; consensus mean target +21% but ratings split 14 buy/12 hold-or-worse
- CEO sold $26.2M in August; only insider buy is a 250-share director purchase

<details><summary><b>News</b> — score +0.15</summary>

- [Get Paid 8.0% A Year To Wait For CAT Stock To Go On Sale](https://www.trefis.com/data/companies/CAT/no-login-required/vnCbjr6I/Get-Paid-8-0-A-Year-To-Wait-For-CAT-Stock-To-Go-On-Sale)  
  <sub>Trefis, 9 hours ago</sub>  
  Get paid a hefty income stream today for simply agreeing to buy a global industrial powerhouse at a deep discount, a payment you keep no matter what happens...
- [Caterpillar’s CEO Says Demand Runs Past Its $72B Backlog. Here’s What That Means for the Stock](https://finance.yahoo.com/markets/stocks/articles/caterpillar-ceo-says-demand-runs-235023123.html)  
  <sub>Yahoo Finance, 15 hours ago</sub>  
  Caterpillar (CAT) supplies the engines and turbines increasingly running data centers as permanent power plants, not backup, and its CEO just told investors...
- [Is Caterpillar (NYSE:CAT) Stock Worth Watching Today?](https://kalkinemedia.com/us/stocks/industrial/is-caterpillar-nysecat-stock-worth-watching-today)  
  <sub>Kalkine Media, 2 hours ago</sub>  
  Highlights. Caterpillar enters Monday with equipment demand as manufacturing signals stay mixed. Industrial Stocks remains shaped by rates, energy moves and...
- [Bernstein Sticks to Its Hold Rating for Caterpillar (CAT)](https://www.google.com/goto?url=CAESxAEB6zswFUZbV5xVJoEeFSp3riy5tKkWAlYSGf_I-zYiRhu9vo3jiTfzJSBTFCXDqAm5bYxEHFsq46rLT9l0dY8TIFQ9BcmnJvoM5nvJ1D63Uv1ANoAmFtDBwfpKBvqswPR08DtTomZ8so8THRtgwbZjw4rzhmvqJfBXKaoshiJDxrlzQDB2kLOxKWbe2lMjYWgrwYBUaJKN-eVr48SF5gHlS_gMNIsckIeWy2S_O7DNrVvNhJUo5rZb5A6o-ozNcihaI2kY)  
  <sub>The Globe and Mail, 4 hours ago</sub>  
  Bernstein analyst Chad Dillard maintained a Hold rating on Caterpillar today and set a price target of $1,002.00. Dillard covers the Industrials sector,...
- [These are the 10 most popular cat names in America](https://www.wgrz.com/article/news/nation-world/most-popular-cat-names-2026/507-6a575dcf-2812-4e65-89fe-14b7e6b7c931)  
  <sub>WGRZ, 3 hours ago</sub>  
  WASHINGTON — If you have a cat named Luna, you're in good company. The name has held the top spot on U.S. News & World Report's annual list of the most...
- [MRNA Stock Rallies Over 40% In June: Moderna Bets Its Future On Cancer, Autoimmune Disease And AI-Powered mRNA](https://stocktwits.com/news-articles/markets/equity/mrna-bets-on-cancer-autoimmune-ai-powered-mrna/cZ1Bz9FR7h4)  
  <sub>Stocktwits, 9 hours ago</sub>  
  Cancer was a key focus, with programs targeting solid tumors, Lynch syndrome, melanoma, and non-small cell lung cancer.
- [3 Stocks That Pay Dividends and Offer AI Exposure](https://www.tradingview.com/news/zacks:f30bb8cf2094b:0-3-stocks-that-pay-dividends-and-offer-ai-exposure/)  
  <sub>TradingView, 16 hours ago</sub>  
  Dividends come with many great perks, with the payouts essentially reflecting a form of 'payday' in the market. Technology sector stocks are often...
- [Chasing A National Championship—Opportunity Still Knocks In Clearwater And Englewood Beach](https://www.powerboatnation.com/chasing-a-national-championship-opportunity-still-knocks-in-clearwater-and-englewood-beach/)  
  <sub>Powerboat Nation, 2 hours ago</sub>  
  If the American Power Boat Association Offshore National Championship ended today—as in before this weekend's Clearwater 'Nationals'—results would rest on...
- [Caterpillar stock gains 0.93 percent as earnings top estimates](https://www.ad-hoc-news.de/boerse/news/corporate-news/caterpillar-stock-gains-0-93-percent-as-earnings-top-estimates/70153685)  
  <sub>AD HOC NEWS, 5 hours ago</sub>  
  Caterpillar stock closed at USD 816.50 on September 21, 2026, while Q2 EPS reached USD 8.17. Revenue rose 23.7 percent year over year.
- [Red Cat CEO Just Sold $1.6 Million of Stock. Wall Street Sees 144% Rally Ahead.](https://www.barchart.com/story/news/4714038/red-cat-ceo-just-sold-1-6-million-of-stock-wall-street-sees-144-rally-ahead)  
  <sub>Barchart.com, 23 hours ago</sub>  
  Red Cat shares have tumbled from their 52-week high as CEO Jeffrey Thompson sells $1.6 million worth of stock, putting insider activity in focus.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 805.66 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 803.75 (+0.2%), 50d 834.91 (-3.5%), 200d 786.35 (+2.5%); 50d above 200d
Momentum: RSI(14) 47.0 | MACD -9.932 vs signal -13.428 (histogram 3.496)
Returns: 1d -1.3% | 5d +2.8% | 1m -2.7% | 3m -18.1%
52-week range: 463.72 - 1,064.90 (now 56.9% of the way up)
Volatility: ATR(14) 23.99 (3.0% of price) | annualised 20d 26.0%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.45</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 370.34B
Valuation: trailing P/E 34.74 | forward P/E 24.88 | P/B 19.09 | PEG 1.42
Profitability: profit margin 14.5% | operating margin 22.2% | ROE 57.0%
Growth (YoY): revenue +24.0% | earnings +68.2%
Balance sheet: debt/equity 232.8% | free cash flow 5.05B
Risk: beta 1.59 | short interest 1.8% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.45</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 31% | 2026-03-31 beat by 19% | 2025-12-31 beat by 9% | 2025-09-30 beat by 8%
```

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
Consensus: buy (mean 2.14 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 1 strong buy, 13 buy, 12 hold, 1 sell, 1 strong sell
Price target: mean 975.61 (+21.1% vs last close), range 575.00 - 1,225.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.15</summary>

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

<details><summary><b>Who is positioned how</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

_Not available today._

</details>

### HDFC Bank (HDB) · Company — NEUTRAL, confidence 0.35

**In the model's own words:**

> HDB faces conflicting signals that warrant a neutral stance. The technical picture is weakly positive (RSI 52, MACD histogram positive, price above 20d SMA) but volume is below average at 0.26x, and the stock trades 15.5% below its 200d MA in a downtrend structure. Fundamentals are solid: 16.3x trailing P/E with 18% earnings growth, 33.3% operating margins, and a 2-beat, 2-in-line earnings record showing resilience though recent quarters have aligned with consensus rather than surprised. Analyst consensus is buy with a +32% mean price target, but recent rating changes (JP Morgan downgrade to Neutral in July 2024) and the wide dispersion (26.10-35.00 range) suggest disagreement. The news block contains material noise: multiple shareholder lawsuit alerts and a vague reference to 'CEO search' supporting shares, but these are neither fresh catalysts nor independently corroborated; the lawsuit items appear boilerplate and lack specificity. No insider buying or selling over 180 days is neutral, not bullish. With earnings scheduled for Oct 17 (25 days out), near-term catalysts are limited. The stock's 52-week positioning (9.6% from lows, 38% below highs) and elevated volatility (37.6% annualized) reflect uncertainty rather than conviction. Positive momentum and valuation do not overcome thin volume, technical breakdown structure, and absence of a clear, material, ticker-specific catalyst.

**Main reasons it gave:**
- Stock 15.5% below 200-day MA with 50d below 200d, indicating medium-term weakness
- Trailing P/E 16.3x with 18% earnings growth supports valuation, but recent beats have given way to in-line results
- Analyst consensus buy with +32% price target, but JP Morgan downgrade and wide target range (26.10-35.00) signal disagreement
- Volume at 0.26x average creates timing risk despite positive RSI and MACD structure
- No insider activity and multiple lawsuit alerts lacking specificity do not provide directional conviction

<details><summary><b>News</b> — score +0.10</summary>

- [HDFC BANK LIMITED (HDB) SHAREHOLDER ALERT Bernstein](https://www.google.com/goto?url=CAES-AEB6zswFSfTaNtkVhD3clbp8ZH9h9zYGIRU7-XTkm4lyMPTaGBgZ-np6cglSIbqOORQq-0LCjI8weV5ULgF5HJkOBeGytBXp168V5-5pW3DIZyc8zqXrEnhauz95vXIqfAy49fA3nYiKx_IwsuD6zgJ3zOYYGpKyuNqXzLqgNNKJ_3sc0SWRwzYWcPsRdTJZJkHQy_4Zs9UISlz7EoWc7frcKmIJCEQ23ADJXhuOItJMTlkPDjsye2qDeLzmbTwpkLfIuV9tr9j_MHaJBaarlCmo2Ak1ygkbqHwhWUFxPZCgB1Xcsc3C31LGIQw9lJBeMAosxmrRqePeA)  
  <sub>GlobeNewswire, 23 minutes ago</sub>  
  HDFC Bank Shareholders Between July 17, 2023 and May 26, 2026 - Contact Bernstein Liebhard For More Information Regarding Lawsuit...
- [Avoiding Lag: Real-Time Signals in (HDB) Movement](https://news.stocktradersdaily.com/news_release/134/Avoiding_Lag:_Real-Time_Signals_in_HDB_Movement_092126055002_1790027402.html)  
  <sub>Stock Traders Daily, 21 hours ago</sub>  
  Key findings for Hdfc Bank Limited (NYSE: HDB). Positive Near-Term Sentiment May Begin to Shift Broader Weak Alignment; Resistance is being tested.
- [NSE’s ₹226 billion IPO gets subdued demand from retail crowd](https://www.tradingview.com/news/moodys:f660a36026eeb:0-nse-s-226-billion-ipo-gets-subdued-demand-from-retail-crowd/)  
  <sub>TradingView, 8 hours ago</sub>  
  National Stock Exchange of India Ltd.'s ₹226 billion ($2.4 billion) initial public offering drew subdued demand particularly from retail investors as...
- [HDFC Bank stock gains as CEO search supports shares](https://www.ad-hoc-news.de/boerse/news/nebenwerte/hdfc-bank-stock-gains-as-ceo-search-supports-shares/70151734)  
  <sub>AD HOC NEWS, 9 hours ago</sub>  
  HDB, US40415F1012. HDFC Bank stock gains as CEO search supports shares. Published on 09/22/2026 at 08:17 | Editorial responsibility: Rafael Müller,...
- [Short-term headwinds, long-term calm: 6 mid-cap stocks from different sectors with upside potential of up](https://economictimes.indiatimes.com/markets/stocks/news/short-term-headwinds-long-term-calm-6-mid-cap-stocks-from-different-sectors-with-upside-potential-of-up-to-22/articleshow/134407728.cms)  
  <sub>The Economic Times, 6 hours ago</sub>  
  This is not the time to expect that every stock you own will do well; or that you will make quick and easy gains. If you are entering the market,...
- [Firefighter, 2 others taken to hospital after fire at Ang Mo Kio HDB flat, Singapore News](https://www.asiaone.com/singapore/ang-mo-kio-hdb-fire-firefighter-2-taken-hospital)  
  <sub>AsiaOne, 3 hours ago</sub>  
  A firefighter and two people were taken to the hospital after a fire broke out at a HDB unit in Ang Mo Kio.The incident occurred at Blk 254 Ang Mo Kio...
- [HDB Financial Services - Negative Breakout: These 9 stocks cross below their 200 DMAs](https://m.economictimes.com/markets/stocks/news/negative-breakout-these-9-stocks-cross-below-their-200-dmas/hdb-financial-services/slideshow/134400522.cms)  
  <sub>The Economic Times, 12 hours ago</sub>  
  In the Nifty500 pack, nine stocks' closing prices crossed below their 200-day moving averages (DMA) on September 21, according to technical scan data from...
- [Deadline Alert: HDFC Bank Limited (HDB) Shareholders Who](https://www.globenewswire.com/news-release/2026/09/21/3365830/0/en/deadline-alert-hdfc-bank-limited-hdb-shareholders-who-lost-money-urged-to-contact-glancy-prongay-wolke-rotter-llp-about-securities-fraud-lawsuit.html)  
  <sub>GlobeNewswire, 20 hours ago</sub>  
  LOS ANGELES, Sept. 21, 2026 (GLOBE NEWSWIRE) -- Glancy Prongay Wolke & Rotter LLP reminds investors of the upcoming October 13, 2026 deadline to file...
- [Vietnam stocks fall below 1,800 on first day as emerging market](https://www.google.com/goto?url=CAESnQEB6zswFeXEmxgNvYDCGMd8-rCz9OfLuSKlIPM5fWErSYz4fmAg03WX-ej6lXKfhKburaF8R-wLJwgYZP8b5-CYBynDKWNAX4l-Bg5UZhy5d00aP-OoIVuCs4XFgZsP4YRY-bqEVgKTMrMqraHuWnooXOmVr8aF6_7LVl9aU3BdQuBdG0aKdcoDcorvstWNjRwEHiysJDNXOMNsDAJE)  
  <sub>Báo VietNamNet, 22 hours ago</sub>  
  Vietnamese stocks fell 0.88% on the day the market officially joined FTSE Russell's secondary emerging-market category, with the VN-Index slipping below...
- [HDBank interest rates today, deposit 500 million and receive 75 million VND in interest](https://news.laodong.vn/kinh-doanh/lai-suat-hdbank-hom-nay-gui-500-trieu-nhan-75-trieu-dong-tien-lai-1771084.ldo)  
  <sub>Laodong.vn, 2 hours ago</sub>  
  According to records on September 22, 2026 at Ho Chi Minh City Development Joint Stock Commercial Bank (HDBank), online deposit products have higher listed...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 23.31 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 22.90 (+1.8%), 50d 23.48 (-0.8%), 200d 27.58 (-15.5%); 50d below 200d
Momentum: RSI(14) 52.0 | MACD -0.111 vs signal -0.238 (histogram 0.127)
Returns: 1d -1.5% | 5d +3.2% | 1m -1.3% | 3m -6.9%
52-week range: 21.84 - 37.18 (now 9.6% of the way up)
Volatility: ATR(14) 0.55 (2.4% of price) | annualised 20d 37.6%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.45</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 119.76B
Valuation: trailing P/E 16.30 | forward P/E 16.75 | P/B 9.31 | PEG n/a
Profitability: profit margin 26.8% | operating margin 33.3% | ROE 13.8%
Growth (YoY): revenue +16.6% | earnings +18.1%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.40 | short interest 0.7% of float
Next earnings: 2026-10-17
```

</details>

<details><summary><b>What this fund holds</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.45</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-06-30 in line | 2026-03-31 in line | 2025-12-31 beat by 61% | 2025-09-30 beat by 10%
```

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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

```text
Consensus: buy (mean 1.75 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 1 strong buy, 2 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 30.77 (+32.1% vs last close), range 26.10 - 35.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

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

### MercadoLibre (MELI) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> News flow is generic filler (price recaps, comparison listicles, FCF-yield blurb) with no ticker-specific catalyst. Technicals are weak: price below 20/50/200d SMAs, MACD deeply negative, RSI 40, -6.4% over a month, though 50d still above 200d and volume is thin. Fundamentals are mixed: 49.8% revenue growth and 27.5% ROE against declining earnings, 168% debt/equity, 48x trailing P/E, and a poor record of 3 misses in the last 4 quarters. Analysts remain constructive with a ~26% target gap, but recent actions are reiterations, not fresh upgrades. Two small open-market insider buys months ago are mildly positive but stale. Conflicting inputs with no catalyst argue for no directional call.

**Main reasons it gave:**
- Price below 20d (-5.6%), 50d (-4.0%) and 200d SMA with MACD histogram -18.5
- 3 misses in last 4 quarters vs consensus
- Revenue +49.8% YoY but earnings -10.9%, trailing P/E 48.9, D/E 168.6%
- Analyst mean target 2,264.88 (+25.8%) but only reiterations recently
- News items are price recaps and comparison listicles, no catalyst

<details><summary><b>News</b> — score +0.05</summary>

- [Is MercadoLibre Stock As Cheap As Its Cash Says?](https://www.trefis.com/stock/meli/articles/615992/is-mercadolibre-stock-as-cheap-as-its-cash-says/2026-09-21)  
  <sub>Trefis, 20 hours ago</sub>  
  MercadoLibre (MELI) produced free cash flow worth 13.7% of its market value over the past twelve months, about three times the 4.5% yield of the median S&P...
- [Alibaba vs. MercadoLibre: Which Consumer Stock Is a Better Buy in 2026?](https://www.fool.com/coverage/better-buy/2026/09/21/alibaba-vs-mercadolibre-which-consumer-stock-is-a-better-buy-in-2026/)  
  <sub>The Motley Fool, 14 hours ago</sub>  
  Alibaba trades at a steep valuation discount while MercadoLibre sustains 39% revenue growth, a classic value-versus-growth showdown with starkly different...
- [MELI stock ends the day 2.07 percent lower at the close](https://www.ad-hoc-news.de/boerse/news/nebenwerte/meli-stock-ends-the-day-2-07-percent-lower-at-the-close/70147349)  
  <sub>AD HOC NEWS, 18 hours ago</sub>  
  On September 21, 2026, MELI stock closed at USD 1787.39 on the Nasdaq, down 2.07 percent from the prior session, while the Nasdaq 100 slipped modestly.
- [MercadoLibre stock gains 3.53 percent as valuation stays elevated](https://www.ad-hoc-news.de/boerse/news/corporate-news/mercadolibre-stock-gains-3-53-percent-as-valuation-stays-elevated/70155036)  
  <sub>AD HOC NEWS, 3 hours ago</sub>  
  MercadoLibre stock traded at USD 1824.00 on September 22, 2026, with a market value of USD 92.292 billion. Revenue reached USD 28.9 billion in fiscal 2025.
- [MercadoLibre stock heads into the open after a 1.6 percent gain](https://www.ad-hoc-news.de/boerse/news/corporate-news/mercadolibre-stock-heads-into-the-open-after-a-1-6-percent-gain/70150484)  
  <sub>AD HOC NEWS, 11 hours ago</sub>  
  MELI, US58733R1023. MercadoLibre stock heads into the open after a 1.6 percent gain. Published on 09/22/2026 at 06:34 | Editorial responsibility: Rafael...
- [Here's How Much $1000 Invested In MercadoLibre 10 Years Ago Would Be Worth Today](https://www.benzinga.com/news/26/09/61923556/here-s-how-much-1000-invested-mercadolibre-10-years-ago-would-be-worth-today)  
  <sub>Benzinga, 25 minutes ago</sub>  
  MercadoLibre (NASDAQ:MELI) has outperformed the market over the past 10 years by 11.73% on an annualized basis producing an average annual return of 25.36%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 1,800.49 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 1,906.44 (-5.6%), 50d 1,875.50 (-4.0%), 200d 1,849.93 (-2.7%); 50d above 200d
Momentum: RSI(14) 40.6 | MACD -20.039 vs signal -1.533 (histogram -18.506)
Returns: 1d -1.1% | 5d -1.6% | 1m -6.4% | 3m +13.7%
52-week range: 1,546.81 - 2,510.97 (now 26.3% of the way up)
Volatility: ATR(14) 59.57 (3.3% of price) | annualised 20d 29.1%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 91.28B
Valuation: trailing P/E 48.90 | forward P/E 31.90 | P/B 11.65 | PEG 0.98
Profitability: profit margin 5.3% | operating margin 6.7% | ROE 27.5%
Growth (YoY): revenue +49.8% | earnings -10.9%
Balance sheet: debt/equity 168.6% | free cash flow 353.38M
Risk: beta 1.31 | short interest 1.6% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

```text
Earnings record, last 4 quarters: 1 beat, 3 missed
  2026-06-30 beat by 4% | 2026-03-31 missed by 7% | 2025-12-31 missed by 6% | 2025-09-30 missed by 13%
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

```text
Consensus: buy (mean 1.58 on a 1=strong buy to 5=strong sell scale, 24 analysts)
Ratings: 4 strong buy, 15 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 2,264.88 (+25.8% vs last close), range 1,750.00 - 2,800.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.15</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.15</summary>

_Not available today._

</details>

### Procter & Gamble (PG) · Company — NEUTRAL, confidence 0.35

**In the model's own words:**

> Procter & Gamble presents a mixed picture with conflicting signals across dimensions. The news flow is generic sector commentary and product updates lacking material catalysts—a product refresh and dividend mentions are routine for a defensive name. Technicals show modest positive momentum (RSI 55.4, MACD positive, stock above key moving averages) but also concerning weakness: volume is 0.15x average (well below normal), the stock sits only 32% up from its 52-week low, and the 3-month return is negative despite recent strength. Fundamentals reveal a valuation concern: forward P/E of 19.91 paired with earnings declining 15.5% YoY and a PEG of 3.75 (elevated) suggest the market is pricing in recovery that has not yet appeared. The 4-quarter earnings record of all "in line" results offers no reassurance that consensus expectations will be beaten. Analyst consensus is constructive with a mean 9% upside to target, but recent downgrades from Argus and HSBC (Buy to Hold in late July/early August) signal softening conviction among research. Insider activity shows net buying of 50k shares, but this came entirely through compensation (24 grants/options excluded) with only 10 distinct officers selling and zero buying independently—the net purchase signal is weakened by its reliance on vesting. The contrast between analyst targets (+9%) and recent downgrades, combined with volume collapse and negative near-term momentum, argues against high conviction in either direction. A defensive dividend play on a stalled earnings trajectory does not justify directional conviction above base rate.

**Main reasons it gave:**
- Volume collapsed to 0.15x average despite modest price strength
- Earnings down 15.5% YoY while stock valued at 3.75x PEG
- Recent Argus and HSBC downgrades to Hold signal dimming analyst confidence
- Four consecutive quarters of in-line (not beat) earnings on undemanding consensus
- Insider net buying driven by vesting grants, no independent executive purchases

<details><summary><b>News</b> — score +0.05</summary>

- [PG vs. CL: Which Consumer Staples Giant Has Stronger Market Position?](https://sg.finance.yahoo.com/news/pg-vs-cl-consumer-staples-143700151.html)  
  <sub>Yahoo Finance Singapore, 34 minutes ago</sub>  
  The Procter & Gamble Company PG and Colgate-Palmolive Company CL are two of the world's most established consumer staples companies, but their competitive...
- [Procter & Gamble (PG) Refreshes Dandruff Care With HydraZinc Complex](https://simplywall.st/stocks/us/household/nyse-pg/procter-gamble/news/procter-gamble-pg-refreshes-dandruff-care-with-hydrazinc-com/amp)  
  <sub>Simply Wall Street, 5 hours ago</sub>  
  Procter & Gamble (NYSE:PG) has rolled out a new HydraZinc Complex across its Head & Shoulders dandruff care range. The HydraZinc formulation is described as...
- [John Osher Built a $475 Million Toothbrush by Starting at 80 Cents While Rivals Started at $79](https://247wallst.com/investing/2026/09/22/john-osher-built-a-475-million-toothbrush-by-starting-at-80-cents-while-rivals-started-at-79/)  
  <sub>24/7 Wall St., 5 hours ago</sub>  
  John Osher ignored how every competitor priced electric toothbrushes and flipped the entire exercise on its head, starting from a number that made engineers...
- [2 Rock-Solid Dividend Stocks to Buy in September Even as Oil Surges Past $100 Per Barrel.](https://www.fool.com/investing/2026/09/22/2-dividend-stocks-buy-september-oil-surges/)  
  <sub>The Motley Fool, 7 hours ago</sub>  
  Higher gas prices are squeezing household budgets -- but Coca-Cola and Procter & Gamble continue to pay generous dividends.
- [4 Stocks to Buy Before They Bounce Back](https://www.morningstar.com/podcasts/the-morning-filter/4-stocks-buy-before-they-bounce-back)  
  <sub>Morningstar, 19 hours ago</sub>  
  What mattered in the market last week. Earnings to have on radar: Costco COST and Darden Restaurants DRI. Which of these stock picks we still like today and...
- [PG&E Corp. stock underperforms Monday when compared to competitors](https://www.google.com/goto?url=CAESyAEB6zswFZUMpxzJLMd7SY0HBjYGclouIhMtBfL2V1nYVYfHS5H74Pcv0JeU9pj936hCYhVAieB1Y_xfeJG6MGELUn7uQ1WjGTCXhG7Ku_5MgINg_qh-04Vn7nT4EkGxHmZIdFL_XY4vaHgdyEUkkXPwgVJTDTwzBN_aYjhqdmdatZhsfRhit1zee2cDVHSz_Mk19oXSipAKoTZ2yVmgTmt8urNIhSOC72f63FP4tJBYNOqDYuXNjmEV_45taEJWv2NVdx6UepmoWA)  
  <sub>MarketWatch, 18 hours ago</sub>  
  Shares of PG&E Corp. PCG slipped 1.97% to $12.94 Monday, on what proved to be an all-around favorable trading session for the stock market, with the S&P 500...
- [SMGXF Stock Price and Chart — OTC:SMGXF](https://www.tradingview.com/symbols/OTC-SMGXF/)  
  <sub>TradingView, 20 hours ago</sub>  
  Track STEAMSHIPS TRADING CO LTD stock price today with the live chart. Find SMGXF news, trading ideas, forecasts, financials, and more.
- [Procter & Gamble stock falls 0.21 percent as volume growth lags](https://www.google.com/goto?url=CAESuQEB6zswFR0W1YoDAWLCVRxrjeaFXSrdUR1x_jBi6lXwNr8IzZUuSL4Pxb11Yve1aKPxBMfPvnNbsqnI1BmUP__SP9inNW6MfR5MlnS0a2gZgF4WcFCKIhbM0faodDZ4Bc4uhN2yGE9uFTcT5AkB0XEU7p9K_PVY8jSho0zpSeWhl1ZkIlbWTTWPpl3oLcYJK6Xl6SCPQOBllyoTBsDlg0bZza8anW7qNTFkfYArVaJOa7r07Ry_jgDjoQ)  
  <sub>AD HOC NEWS, 3 hours ago</sub>  
  Procter & Gamble stock traded at USD 146.08 on September 22, 2026, below its USD 167.25 yearly high. Fiscal 2026 organic sales rose 1 percent.
- [The Zacks Analyst Blog Highlights Procter & Gamble, Sandisk, Analog Devices, Monarch Cement and SUNation Energy](https://www.google.com/goto?url=CAESngEB6zswFS3mUUukj_qFgPrH-8fpqq5KqccWZ_zdblB4BL6EeaJtlDy-lz0odY4o-EW-G8xGke5yzDz71RNLalKCF57JBX5UPJ9cPp8456W-8y5UV6xyhMLEkDPPebwqbMovbh6Qh7UPzkxfo1Y0Js73gEbosjDZHuGUfzTCBYRzpfNzo_xZVZQySHgAh3ZBVYG8qdD_KU1vJkqir1bMcw)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Chicago, IL – September 22, 2026 – Zacks.com announces the list of stocks featured in the Analyst Blog. Every day the Zacks Equity Research analysts discuss...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.15</summary>

```text
Last close 147.37 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 145.67 (+1.2%), 50d 146.08 (+0.9%), 200d 147.46 (-0.1%); 50d below 200d
Momentum: RSI(14) 55.4 | MACD 0.310 vs signal 0.062 (histogram 0.248)
Returns: 1d +0.9% | 5d +0.5% | 1m +1.9% | 3m -2.3%
52-week range: 138.04 - 167.20 (now 32.0% of the way up)
Volatility: ATR(14) 2.23 (1.5% of price) | annualised 20d 13.9%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.25</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 342.28B
Valuation: trailing P/E 22.26 | forward P/E 19.91 | P/B 6.42 | PEG 3.75
Profitability: profit margin 18.4% | operating margin 22.1% | ROE 30.3%
Growth (YoY): revenue +1.5% | earnings -15.5%
Balance sheet: debt/equity 64.5% | free cash flow 13.28B
Risk: beta 0.38 | short interest 1.2% of float
Next earnings: 2026-10-22
```

</details>

<details><summary><b>What this fund holds</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.25</summary>

```text
Earnings record, last 4 quarters: 4 in line
  2026-06-30 in line | 2026-03-31 in line | 2025-12-31 in line | 2025-09-30 in line
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

```text
Consensus: buy (mean 2.20 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 6 strong buy, 7 buy, 12 hold, 0 sell, 0 strong sell
Price target: mean 160.61 (+9.0% vs last close), range 143.00 - 186.00
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

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

_Not available today._

</details>

### Royal Bank of Canada (RY) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> News is entirely auto-generated price-action filler (200-day MA crossing stories, daily close recaps) with no ticker-specific catalyst. Technicals are mixed: price above the 200d by 10% and 50d above 200d, but below both 20d and 50d SMAs with MACD negative and RSI 44, and volume at 0.24x average, so the 'upward momentum confirmed' framing is not supported by the tape. Fundamentals are solid but fully valued at ~16x forward with a price target only 2.4% above spot; earnings not until December. Issuer buybacks are not insider conviction. No edge either way.

**Main reasons it gave:**
- News flow is auto-generated close recaps and MA-crossing listicles, no company catalyst
- Price below 20d (-1.0%) and 50d (-2.5%) SMAs with MACD histogram -0.187, RSI 43.9
- Volume 0.24x 20-day average — thin, low-information tape
- Mean price target 208.70, only +2.4% vs last close; no rating change since Aug 2025
- Insider 'purchases' are issuer buyback blocks, not executive open-market buys

<details><summary><b>News</b> — score +0.05</summary>

- [Royal Bank of Canada (TSE:RY) Share Price Crosses Above 200 Day Moving Average - Here's What Happened](https://www.marketbeat.com/instant-alerts/price-royal-bank-of-canada-tse-ry-share-price-crosses-above-200-day-moving-average-heres-what-happened-2026-09-22/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Royal Bank of Canada (TSE:RY) Stock Passes Above 200 Day Moving Average - Here's What Happened.
- [Royal Bank of Canada stock rises Monday, outperforms market](https://www.marketwatch.com/data-news/royal-bank-of-canada-stock-rises-monday-outperforms-market-d9da3d00-ae5d487094ed?mod=mw_quote_news)  
  <sub>MarketWatch, 19 hours ago</sub>  
  Trading volume of 1.6 M shares remained below its 50-day average volume of 3.2 M. Editor's Note: This story was auto-generated by Automated Insights,...
- [RY stock ends the day slightly higher at the close on the NYSE](https://www.ad-hoc-news.de/boerse/news/nebenwerte/ry-stock-ends-the-day-slightly-higher-at-the-close-on-the-nyse/70147630)  
  <sub>AD HOC NEWS, 17 hours ago</sub>  
  On September 21, 2026, RY stock closed at USD 203.30 on the NYSE, up about 1.2 percent from the prior session while trading within a roughly USD 20.51 to...
- [Royal Bank of Canada stock gains 1.42 percent as earnings remain in view](https://www.ad-hoc-news.de/boerse/news/corporate-news/royal-bank-of-canada-stock-gains-1-42-percent-as-earnings-remain-in-view/70154208)  
  <sub>AD HOC NEWS, 5 hours ago</sub>  
  Royal Bank of Canada stock closed at USD 206.19 on September 21, 2026, up 1.42 percent. Quarterly EPS reached CAD 4.28 on revenue of CAD 18.54 billion.
- [Royal Bank of Canada stock gains 1.42 percent ahead of the open](https://www.ad-hoc-news.de/boerse/news/corporate-news/royal-bank-of-canada-stock-gains-1-42-percent-ahead-of-the-open/70151943)  
  <sub>AD HOC NEWS, 9 hours ago</sub>  
  At the close on September 21, 2026, Royal Bank of Canada stock reached USD 206.19, while its TSX listing closed at CAD 284.93; the next ex-dividend date is...
- [Royal Bank of Canada stock forecast: Upward momentum confirmed despite short-term risks](https://tradersunion.com/news/stocks/show/3432441-royal-bank-of-canada-down/)  
  <sub>Traders Union, 1 hour ago</sub>  
  Highlights. Shares of Royal Bank of Canada moved above the 200-day moving average, an event watched by momentum-driven traders.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 203.72 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 205.87 (-1.0%), 50d 208.98 (-2.5%), 200d 185.01 (+10.1%); 50d above 200d
Momentum: RSI(14) 43.9 | MACD -1.204 vs signal -1.017 (histogram -0.187)
Returns: 1d -1.2% | 5d -0.2% | 1m -0.7% | 3m +0.4%
52-week range: 143.64 - 217.87 (now 80.9% of the way up)
Volatility: ATR(14) 3.21 (1.6% of price) | annualised 20d 16.4%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 282.04B
Valuation: trailing P/E 17.96 | forward P/E 15.95 | P/B 2.95 | PEG 2.26
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

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-09-30 in line | 2026-06-30 in line | 2026-03-31 beat by 3% | 2026-03-31 beat by 3%
```

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

<details><summary><b>What analysts and big funds say</b> — score +0.10</summary>

```text
Consensus: buy (mean 2.13 on a 1=strong buy to 5=strong sell scale, 3 analysts)
Ratings: 4 strong buy, 5 buy, 5 hold, 0 sell, 1 strong sell
Price target: mean 208.70 (+2.4% vs last close), range 181.14 - 227.60
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.05</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.05</summary>

_Not available today._

</details>

### Toyota (TM) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> News flow is almost entirely irrelevant noise (unrelated tickers matched on 'TM' string, price recaps) with no ticker-specific catalyst. Technicals are mixed-to-soft: below 20d and 200d SMA, 50d below 200d, MACD negative histogram, RSI ~49, very thin volume. Fundamentals are supportive — 8.5x trailing P/E, +10% revenue, four straight beats — and consensus targets imply ~22% upside, but that prior is stale and already priced. No insider activity. Conflicting dimensions with no catalyst warrant NEUTRAL.

**Main reasons it gave:**
- No ticker-specific news; headlines are unrelated 'TM'/trademark string matches
- Price below 20d and 200d SMA with 50d under 200d, MACD histogram -0.80
- Four consecutive earnings beats, latest by 44%
- Trailing P/E 8.5 with revenue +10.4% and earnings +86.9% YoY
- Analyst mean target 234 (+21.7%) but only 4 analysts and last change a 2025 downgrade

<details><summary><b>News</b> — score +0.00</summary>

- [Some B2B studies remove up to 59.6% of responses. RIWI launched a human check.](https://www.stocktitan.net/news/RWCRF/riwi-launches-verify-human-tm-a-browser-based-human-verification-ajncn1igg76g.html)  
  <sub>Stock Titan, 3 hours ago</sub>  
  RIWI's browser-based service uses behavioural, device and session signals, with optional on-device facial analysis, and is onboarding paying customers.
- [Promino Reports Strength in Revenue as New Inventory and Kroger Distribution Drive Growth](https://finance.yahoo.com/healthcare/articles/promino-reports-strength-revenue-inventory-110000385.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  August generates approximately 34% of Promino's year-to-date net revenue as new proprietary Rejuvenate formula reaches expanded U.S. retail...
- [Most construction blueprints went from hours to about 3–5 seconds](https://www.stocktitan.net/news/IGCRF/integrated-quantum-technologies-announces-first-customer-engagement-btwd44l53rko.html)  
  <sub>Stock Titan, 3 hours ago</sub>  
  VEIL improved Pivotly's model performance by about 5-8 percentage points and produced a production-ready workflow; no broader deployment agreement exists.
- [TM stock ends the day 1.23 percent lower at the close](https://www.ad-hoc-news.de/boerse/news/nebenwerte/tm-stock-ends-the-day-1-23-percent-lower-at-the-close/70147673)  
  <sub>AD HOC NEWS, 17 hours ago</sub>  
  On September 21, 2026, TM stock closed at USD 191.53 on the NYSE, down 1.23 percent from the prior close, as the ADRs of Toyota Motor tracked a softer tone...
- [(SWIN) Market Insights and Trading Signals (SWIN:CA)](https://news.stocktradersdaily.com/canada/swin-market-insights-and-trading-signals_20260921_a4df49)  
  <sub>Stock Traders Daily, 14 hours ago</sub>  
  Market Insights Report for HAMILTON CHAMPIONS TM Enhanced U.S. Dividend ETF (SWIN) with Key Trading Signals.
- [4 Dividend-Friendly Auto Stocks to Weather the Industry Challenges](https://www.google.com/goto?url=CAESzgEB6zswFVSW0-TgL25rxPVqogYTmmKAZwXUXahGcecP3PNw0-Kfc6wCPEkBBCUtMb7NYtl7I2gK8l-zec5pYlU20nPFfmcbK0rdyxf55VzMfp995cqquOd3P4jro3sZUS7v0ubJD6q-B1tn0OwDWIlgIIginsye6tLVDIkRDgWgskFIAuO_gDhhux4jNrOnZNJxnGJhpuMIe1V_A_-R0uq_YoNqssqlS-ezE7WJWDeUVDkI--UXdCmlEPikfCBSk35oX2miEsujJ20bw8_2-Q)  
  <sub>The Globe and Mail, 23 hours ago</sub>  
  Detailed price information for Toyota Motor Corp Ord ADR (TM-N) from The Globe and Mail including charting and trades.
- [Carnatic musician T M Krishna moves Supreme Court against Centre's directive to sing six stanzas of Vande...](https://www.google.com/goto?url=CAES5AEB6zswFZvvrWPuEgrdevgINCKUzBGY2WLI3_3Knw6M2oOT9mU1ZGdP-Va-ci6fjufgyAC5Bpq7XesY0Fs5apCrDjcBvJkuGcg0DEudGtt6R2YtfkxxJbD7aTVyRfMeRfGH6J89KjiIX-ywMlplB3jZX1oKucpuaFMml4rDnKZbgEhf6QGJVc9ZO8Wtl-nVMw76wuluoEaqhf1fZRBt-Q68v8lKxq1Bbgh_L4y7VFsNXCXoiTkU6R6BbULus-EOrd8y236IGQK8PB916JaN2EoXg89RKeJOmvcFHr7-IXgAw-CMvGU)  
  <sub>Moneycontrol.com, 8 hours ago</sub>  
  Krishna has challenged the Centre's circular on the singing of Vande Mataram as well as the recent amendment to the Prevention of Insults to National Honour...
- [Bruce Lee is among the inspirations behind Be Water's seven bottle messages](https://www.stocktitan.net/news/INKW/more-than-water-the-story-and-inspiration-behind-be-water-7cubz1bxjmbt.html)  
  <sub>Stock Titan, 3 hours ago</sub>  
  Greene Concepts (INKW) outlines the purpose and inspiration behind its premium artesian spring water brand, Be Water™, emphasizing values-based branding...
- [Toyota stock heads into the open after a 2.97 percent gain](https://www.ad-hoc-news.de/boerse/news/corporate-news/toyota-stock-heads-into-the-open-after-a-2-97-percent-gain/70152020)  
  <sub>AD HOC NEWS, 9 hours ago</sub>  
  TM, US8923313071. Toyota stock heads into the open after a 2.97 percent gain. Published on 09/22/2026 at 08:40 | Editorial responsibility: Rafael Müller,...
- [Sensex Today Ends 329 Points Lower | Nifty Below 23,350 | LTM Ltd Down 4%](https://www.equitymaster.com/indian-share-markets/09/22/2026/Sensex-Today-Ends-329-Points-Lower--Nifty-Below-23350--LTM-Ltd-Down-4?utm_source=homepage&utm_medium=website&utm_campaign=Content&utm_content=TM)  
  <sub>Equitymaster, 5 hours ago</sub>  
  The BSE Sensex ends 329 points lower, while Nifty ended 85 points lower, down at 23329.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 192.38 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 194.49 (-1.1%), 50d 189.40 (+1.6%), 200d 202.00 (-4.8%); 50d below 200d
Momentum: RSI(14) 49.5 | MACD 0.833 vs signal 1.629 (histogram -0.795)
Returns: 1d -0.1% | 5d -1.6% | 1m -2.5% | 3m +15.0%
52-week range: 166.50 - 248.29 (now 31.6% of the way up)
Volatility: ATR(14) 3.25 (1.7% of price) | annualised 20d 20.2%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.45</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 227.82B
Valuation: trailing P/E 8.54 | forward P/E 12.19 | P/B 15.64 | PEG n/a
Profitability: profit margin 8.6% | operating margin 7.9% | ROE 12.4%
Growth (YoY): revenue +10.4% | earnings +86.9%
Balance sheet: debt/equity 115.0% | free cash flow -3.60T
Risk: beta 0.34 | short interest 0.1% of float
Next earnings: 2026-11-05
```

</details>

<details><summary><b>What this fund holds</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.45</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 44% | 2026-03-31 beat by 12% | 2025-12-31 beat by 27% | 2025-09-30 beat by 24%
```

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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: strong_buy (mean 1.50 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 2 strong buy, 2 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 234.08 (+21.7% vs last close), range 230.00 - 239.31
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

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

### Exxon Mobil (XOM) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> News is dominated by a crude-driven 3% selloff on easing supply fears, which is macro rather than company-specific; one headline is about an unrelated ticker (XMTR) and should be ignored. Technicals are mixed: below 20d SMA with negative MACD histogram and RSI 46, but still above 50d/200d and +14% over 3 months, on very thin volume. Fundamentals are solid (forward P/E 14.8, low leverage, strong FCF, 2 beats/2 in line) with earnings over a month away. Analyst consensus is a lukewarm buy with 15 holds and a recent BofA downgrade; target implies only ~7%. Insider data is internally inconsistent (aggregate net buying but zero distinct insiders) and carries little weight. No clear directional edge.

**Main reasons it gave:**
- -3.2% drop attributed to crude retreat on recovering Saudi exports, a macro not company factor
- Below 20d SMA with MACD histogram -0.864 and RSI 46, but 50d above 200d
- Forward P/E 14.76, D/E 15.9%, FCF $20.7B, earnings +112.8% YoY
- Consensus skewed to hold (15 of 22) with BofA downgrade in July; target only +7.4%
- Insider block shows aggregate net buying but 0 distinct buyers/sellers — unreliable

<details><summary><b>News</b> — score -0.30</summary>

- [Exxon Mobil Holdings (XOM) Stock Drops Despite Market Gains: Important Facts to Note](https://www.google.com/goto?url=CAESlwEB6zswFccMlyaKPChj_DFNrb0l4iH6QWgM435G8iyF_G07apryffg9_iNxfgT1MiT1_beYKQt2g1yC__8IoA-QibU801s3XcM93saVFbJiqT-V6Pqi_ttYko8jzoVwGbGlLGuhLzLuoWEOPygLwMTKFVPZikjMOLyrY-cNbwQYHf0KhFcZPpiz7XeTAd67wqQf3_Fax0d-)  
  <sub>Yahoo Finance, 17 hours ago</sub>  
  In the latest trading session, Exxon Mobil Holdings (XOM) closed at $158.30, marking a -3.2% move from the previous day. The stock's change was less than...
- [XOM|Exxon Mobil Corp|Price:158.300|Chg%:-5.240](https://www.tradingkey.com/markets/stocks/xom)  
  <sub>TradingKey, 8 hours ago</sub>  
  Exxon Mobil Corp News · Phillips 66 Stock (PSX) Moved Down by 3.80% on Sep 21: What Signal Does It Send? • Phillips 66 stock pulled back due to broader energy...
- [Is Exxon Mobil (NYSE:XOM) Stock Worth Watching Today?](https://kalkinemedia.com/us/stocks/energy/is-exxon-mobil-nysexom-stock-worth-watching-today)  
  <sub>Kalkine Media, 2 hours ago</sub>  
  Exxon Mobil (NYSE:XOM) enters Monday with energy positioning as crude retreats with supply routes improving.
- [ExxonMobil Stock Falls Monday: What's Happening?](https://www.benzinga.com/trading-ideas/movers/26/09/61899671/exxonmobil-stock-falls-monday-whats-happening)  
  <sub>Benzinga, 24 hours ago</sub>  
  ExxonMobil Corp. (NYSE:XOM) shares are trading lower Monday morning as global benchmark crude prices retreat amid recovering Saudi Arabian export volumes...
- [ExxonMobil Falls as Crude Prices Retreat on Easing Supply Fears](https://www.quiverquant.com/news/ExxonMobil+Falls+as+Crude+Prices+Retreat+on+Easing+Supply+Fears)  
  <sub>Quiver Quantitative, 22 hours ago</sub>  
  ExxonMobil Holdings Corp. (XOM) is down 3.3% today. Here is some analysis on what might have caused.
- [ExxonMobil Holdings Corp (XOM) Shares Fall 3.2% -- What GF Score of 72 Tells Investors](https://www.gurufocus.com/news/9090511)  
  <sub>GuruFocus, 18 hours ago</sub>  
  On September 21, 2026, ExxonMobil Holdings Corp (XOM) shares declined by 3.2%, bringing the current price to $158.30. This drop is notable within the...
- [Rosenblatt raises Xometry stock price target to $120 on AI strength](https://uk.investing.com/news/stock-market-news/rosenblatt-raises-xometry-stock-price-target-to-120-on-ai-strength-93CH-4877439)  
  <sub>Investing.com UK, 3 hours ago</sub>  
  Investing.com - Rosenblatt raised its price target on Xometry Inc (NASDAQ:XMTR) to $120 from $110 on Monday while maintaining a Buy rating on the shares.
- [ExxonMobil (NYSE:XOM) Stock Price Down 3.1% - What's Next?](https://www.marketbeat.com/instant-alerts/price-exxonmobil-nyse-xom-stock-price-down-31-whats-next-2026-09-21/)  
  <sub>MarketBeat, 18 hours ago</sub>  
  Shares of ExxonMobil Corporation (NYSE:XOM - Get Free Report) traded down 3.1% during mid-day trading on Monday . The stock traded as low as $157.94 and...
- [This Energy Stock Could Give ExxonMobil a Run: Should You Buy?](https://www.theglobeandmail.com/investing/markets/stocks/XOM/pressreleases/4714760/this-energy-stock-could-give-exxonmobil-a-run-should-you-buy/)  
  <sub>The Globe and Mail, 23 hours ago</sub>  
  Detailed price information for Exxonmobil Holdings Corp (XOM-N) from The Globe and Mail including charting and trades.
- [ExxonMobil Nears a Venezuela Return After 19 Years. Here’s Where the Stock Could Go](https://www.tikr.com/blog/exxonmobil-nears-a-venezuela-return-after-19-years-heres-where-the-stock-could-go)  
  <sub>TIKR.com, 16 hours ago</sub>  
  Current Price: $163.54; Target Price (Mid): ~$170; Street Target: ~$171; Potential Total Return: ~4%; Annualized IRR: ~1% / year.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 159.16 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 162.07 (-1.8%), 50d 158.47 (+0.4%), 200d 147.32 (+8.0%); 50d above 200d
Momentum: RSI(14) 46.2 | MACD 0.952 vs signal 1.817 (histogram -0.864)
Returns: 1d +0.5% | 5d -6.0% | 1m -3.6% | 3m +13.9%
52-week range: 110.64 - 171.47 (now 79.8% of the way up)
Volatility: ATR(14) 3.84 (2.4% of price) | annualised 20d 28.3%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 654.45B
Valuation: trailing P/E 20.48 | forward P/E 14.76 | P/B 2.52 | PEG 1.40
Profitability: profit margin 9.1% | operating margin 15.9% | ROE 12.6%
Growth (YoY): revenue +44.1% | earnings +112.8%
Balance sheet: debt/equity 15.9% | free cash flow 20.67B
Risk: beta 0.17 | short interest 1.1% of float
Next earnings: 2026-10-30
```

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.35</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-06-30 in line | 2026-03-31 beat by 14% | 2025-12-31 in line | 2025-09-30 beat by 2%
```

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
Consensus: buy (mean 2.32 on a 1=strong buy to 5=strong sell scale, 22 analysts)
Ratings: 3 strong buy, 7 buy, 15 hold, 0 sell, 0 strong sell
Price target: mean 170.91 (+7.4% vs last close), range 142.00 - 200.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.05</summary>

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

### Alphabet (Google) (GOOGL) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Alphabet Inc. (GOOGL) is Attracting Investor Attention: Here is What You Should Know](https://finance.yahoo.com/markets/stocks/articles/alphabet-inc-googl-attracting-investor-130005253.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Recently, Zacks.com users have been paying close attention to Alphabet (GOOGL). This makes it worthwhile to examine what the stock has in store.
- [What's Going On With Alphabet Stock Tuesday? - Alphabet (NASDAQ:GOOGL), Alphabet (NASDAQ:GOOG)](https://www.benzinga.com/markets/tech/26/09/61915624/if-theres-a-problem-with-google-search-theres-a-problem-with-google-stock-analyst)  
  <sub>Benzinga, 4 hours ago</sub>  
  Evercore's Mark Mahaney says Google Search is strengthening as Gemini closes the gap on ChatGPT. See why analysts remain bullish.
- [How More Pieces Are Falling Into Place For Google's Nvidia AI Chip Challenge](https://www.investors.com/news/technology/google-stock-tpu-blackstone-cloud-growth-nvidia/)  
  <sub>Investor's Business Daily, 3 hours ago</sub>  
  Google stock could benefit as AI chip business emerges as new cloud computing growth engine and rival to Nvidia GPUs.
- [Is Most-Watched Stock Alphabet Inc. (GOOG) Worth Betting on Now?](https://finance.yahoo.com/markets/stocks/articles/most-watched-stock-alphabet-inc-130002067.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Alphabet (GOOG) has been one of the stocks most watched by Zacks.com users lately. So, it is worth exploring what lies ahead for the stock.
- [Is Alphabet (NASDAQ:GOOGL) Stock Worth Watching Today?](https://kalkinemedia.com/us/stocks/growth/is-alphabet-nasdaqgoogl-stock-worth-watching-today)  
  <sub>Kalkine Media, 2 hours ago</sub>  
  Alphabet (NASDAQ:GOOGL) enters Monday with search, cloud and artificial intelligence spending under fresh trade attention.
- [Wells Fargo Says Building AI Is Getting More Expensive — Here's Why It Hiked Price Targets For GOOGL, AMZN And META](https://stocktwits.com/news-articles/markets/equity/wells-fargo-sees-ai-more-expensive-not-red-flag-googl-amzn-meta/cZZSJKOR7vT)  
  <sub>Stocktwits, 18 hours ago</sub>  
  Wells Fargo analyst Ken Gawrelski raised the firm's price targets on Alphabet Inc. (GOOG, GOOGL), Amazon.com Inc. (AMZN) and Meta Platforms Inc. (META) on...
- [Not Micron. Not Alphabet. Here's My Top Artificial Intelligence (AI) Stock Pick for the Next 3 Years.](https://www.theglobeandmail.com/investing/markets/stocks/GOOGL/pressreleases/4724288/not-micron-not-alphabet-heres-my-top-artificial-intelligence-ai-stock-pick-for-the-next-3-years/)  
  <sub>The Globe and Mail, 8 hours ago</sub>  
  Detailed price information for Alphabet Cl A (GOOGL-Q) from The Globe and Mail including charting and trades.
- [Google: The One-Stop AI Shop (NASDAQ:GOOG)](https://seekingalpha.com/article/4948364-google-the-one-stop-ai-shop)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Google stands as a one-stop shop for AI, spanning silicon, software, cloud, and telecom offerings. Read what investors should know about the tech giant's AI...
- [Berkshire Hathaway boosts Alphabet stake 83%, s...](https://pluang.com/en/news-feed/kepercayaan-ku-pada-akumulasi-berkelanjutan-alphabet-setelah-buffett-beli)  
  <sub>Pluang, 13 minutes ago</sub>  
  Berkshire Hathaway increased its investment in Alphabet by 83%, making it the company's third-largest holding. This move highlights confidence in Alphabet's...
- [AVAV Stock Rebounds After-Hours On Record Sales And $1.5B Backlog — CEO Says FY27 ‘Off To A Strong Start’](https://stocktwits.com/news-articles/markets/equity/avav-stock-rebounds-after-hours-on-record-sales-and-1-5-b-backlog-ceo-says-fy-27-off-to-a-strong-start/cZt7K4YRJCR)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Chief Executive Wahid Nawabi said fiscal 2027 “is off to a strong start, with record first-quarter revenue and funded backlog and landmark strategic wins.”

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 358.84 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 342.83 (+4.7%), 50d 345.66 (+3.8%), 200d 337.89 (+6.2%); 50d above 200d
Momentum: RSI(14) 61.3 | MACD 1.689 vs signal -0.754 (histogram 2.443)
Returns: 1d +1.1% | 5d +4.0% | 1m +4.1% | 3m +3.7%
52-week range: 236.57 - 402.62 (now 73.6% of the way up)
Volatility: ATR(14) 8.46 (2.4% of price) | annualised 20d 23.5%
Volume: 0.41x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 4.39T
Valuation: trailing P/E 18.02 | forward P/E 24.11 | P/B 7.05 | PEG 1.27
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
Price target: mean 429.46 (+19.7% vs last close), range 340.00 - 515.00
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

### Eli Lilly (LLY) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [LLY Stock Gains As CEO Says Foundayo Wins One-Third Of New GLP-1 Pill Starts, Breaks Ground On $6.5B Houston Plant](https://finance.yahoo.com/healthcare/articles/lly-stock-gains-ceo-says-194919636.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Eli Lilly & Company (LLY) broke ground at a new facility in Houston on Monday as it builds more factory capacity for Foundayo, its newly launched obesity...
- [His Bet On Home Depot Made Ken Langone A Billionaire. Now He Sees Eli Lilly Stock Hitting $2,000](https://247wallst.com/investing/2026/09/22/his-bet-on-home-depot-made-ken-langone-a-billionaire-now-he-sees-eli-lilly-stock-hitting-2000/)  
  <sub>24/7 Wall St., 60 minutes ago</sub>  
  Ken Langone predicts Eli Lilly (LLY) hits $2,000 within 3-4 years, a ~73% gain from $1,154, while Home Depot (HD) sits down 25% over one year.
- [Ken Langone predicts Eli Lilly stock will hit $2,000 in 3-4 years, rivaling his Home Depot gains.](https://pluang.com/en/news-feed/ken-langone-prediksi-saham-eli-lilly-capai-2000)  
  <sub>Pluang, 44 minutes ago</sub>  
  Ken Langone, co-founder of Home Depot, stated that Eli Lilly stock could reach $2000 within the next 3 to 4 years, challenging the long-term success of his...
- [ATAI Stock Slips After Blockbuster Week: Cathie Wood Calls $3.8B Lilly Deal ‘Well-Deserved’ Return For Shareholders](https://stocktwits.com/news-articles/markets/equity/atai-cathie-wood-lilly-deal-well-deserved-return-shareholders/cZZLrZTR7MA)  
  <sub>Stocktwits, 6 hours ago</sub>  
  ARKG sold 1.12 million ATAI shares last week but still held 3.19 million shares as of Friday.
- [Eli Lilly & Co (LLY) Receives a Buy from Barclays](https://www.theglobeandmail.com/investing/markets/stocks/LLY/pressreleases/4725475/eli-lilly-co-lly-receives-a-buy-from-barclays/)  
  <sub>The Globe and Mail, 7 hours ago</sub>  
  Detailed price information for Eli Lilly and Company (LLY-N) from The Globe and Mail including charting and trades.
- [Eli Lilly CEO Says Foundayo Wins One-Third of New Oral GLP-1 Patients as Company Captures 70% of New Seni](https://www.benzinga.com/news/health-care/26/09/61915766/eli-lilly-ceo-says-foundayo-wins-one-third-of-new-oral-glp-1-patients-as-company-captures-70-of-new-seniors-growing-week-on-week)  
  <sub>Benzinga, 4 hours ago</sub>  
  Eli Lilly and Co.'s (NYSE:LLY) CEO Dave Ricks announced a significant increase in the use of GLP-1 treatments among seniors, following Medicare's July...
- [What Lilly Stock's Breast Cancer Drug Approval Means For Shareholders](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-lly/eli-lilly/news/what-lilly-stocks-breast-cancer-drug-approval-means-for-shar)  
  <sub>Simply Wall Street, 20 hours ago</sub>  
  Eli Lilly received full U.S. FDA approval for Inluriyo, an oral estrogen receptor antagonist, in combination with Verzenio for adults with ER+, HER2–,...
- [Eli Lilly’s Tough Month: One of The Biggest Global Banks Says 37% Gains Begin Soon](https://www.aol.com/articles/eli-lilly-tough-month-one-113421000.html)  
  <sub>AOL.com, 4 hours ago</sub>  
  Eli Lilly just posted a quarter that crushed estimates on every major metric, yet the stock has spent the past month getting punished anyway.
- [Guggenheim Boosts Eli Lilly Price Target Amid Strong Weight Loss Drug Demand](https://finance.yahoo.com/markets/stocks/articles/guggenheim-boosts-eli-lilly-price-031933331.html)  
  <sub>Yahoo Finance, 12 hours ago</sub>  
  Key Stats for Eli Lilly StockPrice change for Eli Lilly stock in last 6 months: 27%$LLY Stock Price as of Sep. 21: $1,16552-Week High: $1292$LLY Stock Price...
- [TD Cowen reiterates Buy on Eli Lilly stock, $1,250 target on approval](https://in.investing.com/news/stock-market-news/td-cowen-reiterates-buy-on-eli-lilly-stock-1250-target-on-approval-93CH-5600738)  
  <sub>Investing.com India, 5 hours ago</sub>  
  Investing.com - TD Cowen reiterated a Buy rating and $1,250 price target on Eli Lilly (NYSE:LLY) stock following the approval of its Inluriyo combination...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,173.94 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 1,155.14 (+1.6%), 50d 1,176.73 (-0.2%), 200d 1,067.64 (+10.0%); 50d above 200d
Momentum: RSI(14) 53.6 | MACD -8.566 vs signal -12.162 (histogram 3.596)
Returns: 1d +0.8% | 5d +3.3% | 1m -6.5% | 3m +6.0%
52-week range: 714.59 - 1,280.34 (now 81.2% of the way up)
Volatility: ATR(14) 30.41 (2.6% of price) | annualised 20d 19.8%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.05T
Valuation: trailing P/E 39.37 | forward P/E 24.80 | P/B 30.89 | PEG 1.14
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
Price target: mean 1,325.39 (+12.9% vs last close), range 930.00 - 1,600.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

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

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Microsoft (MSFT) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Microsoft (MSFT) Stock Looks Reasonable Despite Its 75% Five Year Run](https://finance.yahoo.com/markets/stocks/articles/microsoft-msft-stock-looks-reasonable-211138209.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Microsoft closed at US$493.78 after a strong multi year run, and with the stock dipping over the past week, the real question for investors is whether that...
- [Analyst Sees More Upside for Microsoft Stock Following Management Meeting](https://www.benzinga.com/trading-ideas/movers/26/09/61923311/analyst-sees-more-upside-for-microsoft-stock-following-management-meeting)  
  <sub>Benzinga, 28 minutes ago</sub>  
  Microsoft Corp (NASDAQ:MSFT) shares are trading slightly lower Tuesday, pulling back modestly even as Oppenheimer reiterated an Outperform rating and raised...
- [MSFT Sees Fresh Price Target Cuts Days Before Quarterly Report – Citi Sees Strong Q4 But Expects Higher Capex Spend In Q1](https://stocktwits.com/news-articles/markets/equity/msft-sees-fresh-price-target-cuts-days-before-quarterly-report-citi-sees-strong-q4-but-expects-higher-capex-spend-in-q1/cZZPPT1R7AF)  
  <sub>Stocktwits, 6 hours ago</sub>  
  Wells Fargo said that amid cloud market-share and capital-spending concerns, the setup for the company's Q4 is mixed. Citi said it remains positive on...
- [Wall Street analyst updates Microsoft stock price target](https://www.google.com/goto?url=CAEShwEB6zswFWpuk5lk-S6afOB-eIIGUkPBEvTkI4a5ZrPnVRWj9h0PmSRWEJ37t_lTuc8CjLJZt5NNhdnOgI8-zEzf3CpQAP0eN_diwZNQTXplcLvO8D8Eo1W6tiS7m2nzhs21r4znCMxdOh_K7atrt7NKv4LMHNl-v2tFxpJ6kf-c0AupoHIxwf4)  
  <sub>Finbold, 28 minutes ago</sub>  
  Oppenheimer has raised its Microsoft (NASDAQ: MSFT) stock price target to $570 from $515 while reiterating its 'Outperform' rating.
- [$MSFT: Microsoft Is Compressing — Is The Market Preparing For Expansion?](https://www.moomoo.com/community/feed/msft-microsoft-is-compressing-is-the-market-preparing-for-expansion-117314426896389)  
  <sub>Moomoo, 4 hours ago</sub>  
  Microsoft (MSFT.US)$What's Actually Happening Here? For anyone who finds standard technical jargon confusing, here is the short version of what $MSF...
- [How AI Cloud Expansion At Microsoft (MSFT) Has Changed Its Investment Story](https://www.google.com/goto?url=CAESuQEB6zswFU1OhLOum_bSVALUTr8qAYh9vK4siqMnTwqFf7BrS1lkQQjA2sVdyN5Yq-_M1StD7RiPlKYR-j4P1TUmfGk-gsYi4EWDqAsl7op7z7p4W9XjKC6IRhkywNyWZ0S1mkRcy7MWFFaE2LxxiWPe9Uj09tjcRqaYxfi8oqGPEBB4LVht9j2zzqsDxgM-vcKpu5rg7_T8sv7Gg-OQTbv7EB2c4dHe3eLiMLdNNiimlUh9py0RgvEPBA)  
  <sub>Simply Wall Street, 11 hours ago</sub>  
  Microsoft expanded its AI-heavy cloud footprint through new Azure partnerships in payments, telecoms and scientific research, while its board approved a...
- [Is It Too Late To Buy Microsoft Stock After Its Summer Run?](https://www.trefis.com/stock/msft/articles/615998/is-it-too-late-to-buy-microsoft-stock-after-its-summer-run/2026-09-21)  
  <sub>Trefis, 24 hours ago</sub>  
  Microsoft (MSFT) stock is up about 30% in three months, including a 19% jump in the two trading days after its July report. That makes buying now feel late.
- [The 'Slow Down AI' Movement Could Actually Be Bullish for These Stocks](https://www.theglobeandmail.com/investing/markets/stocks/MSFT/pressreleases/4735229/the-slow-down-ai-movement-could-actually-be-bullish-for-these-stocks/)  
  <sub>The Globe and Mail, 7 minutes ago</sub>  
  Detailed price information for Microsoft Corp (MSFT-Q) from The Globe and Mail including charting and trades.
- [MSFT Stock Jumps 3% After-Hours — Lower-Than-Expected Q4 Capex, Strong Azure Sales Boost Sentiment](https://stocktwits.com/news-articles/markets/equity/msft-stock-jumps-3-after-hours-lower-than-expected-q4-capex-strong-azure-sales-boost-sentiment/cZNT9ukRJTF)  
  <sub>Stocktwits, 12 hours ago</sub>  
  Microsoft Azure cloud-computing revenue increased 43% during the fiscal fourth quarter, above expectations of 40%.
- [Microsoft (MSFT) Laps the Stock Market: Here's Why](https://finance.yahoo.com/markets/stocks/articles/microsoft-msft-laps-stock-market-214503698.html)  
  <sub>Yahoo Finance, 17 hours ago</sub>  
  Microsoft (MSFT) closed at $501.61 in the latest trading session, marking a +1.59% move from the prior day. The stock outpaced the S&P 500's daily gain of...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 496.47 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 498.89 (-0.5%), 50d 469.12 (+5.8%), 200d 431.75 (+15.0%); 50d above 200d
Momentum: RSI(14) 53.9 | MACD 6.239 vs signal 8.742 (histogram -2.503)
Returns: 1d -1.0% | 5d -0.1% | 1m +2.7% | 3m +32.8%
52-week range: 352.83 - 542.07 (now 75.9% of the way up)
Volatility: ATR(14) 10.75 (2.2% of price) | annualised 20d 22.9%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.69T
Valuation: trailing P/E 27.64 | forward P/E 20.97 | P/B 8.33 | PEG 1.60
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
Consensus: strong_buy (mean 1.36 on a 1=strong buy to 5=strong sell scale, 52 analysts)
Ratings: 14 strong buy, 38 buy, 3 hold, 0 sell, 0 strong sell
Price target: mean 575.34 (+15.9% vs last close), range 440.00 - 870.00
Recent rating changes:
  - 2026-09-21 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-09-15 Citizens: reit, Market Outperform -> Market Outperform
  - 2026-09-04 Stifel: main, Hold -> Hold
  - 2026-09-01 B of A Securities: main, Buy -> Buy
  - 2026-08-12 Wells Fargo: main, Overweight -> Overweight
  - 2026-08-05 Tigress Financial: main, Buy -> Buy
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

- [NVIDIA Corporation (NVDA) Is a Trending Stock: Facts to Know Before Betting on It](https://finance.yahoo.com/markets/stocks/articles/nvidia-corporation-nvda-trending-stock-130004378.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Nvidia (NVDA) has received quite a bit of attention from Zacks.com users lately. Therefore, it is wise to be aware of the facts that can impact the stock's...
- [Nvidia stock valuation hits decade low despite profit boom](https://qz.com/nvidia-stock-valuation-decade-low-earnings-092226)  
  <sub>Quartz, 2 hours ago</sub>  
  Nvidia $NVDA stock is trading near its lowest valuation in more than a decade, according to Bloomberg, even as the chipmaker's revenue and net income are...
- [NVIDIA (NVDA.US) Stock Flashes a "Warning Signal": Valuation Hits Lowest Level in Over a Decade, What Is the Market Worried About?](https://www.moomoo.com/news/post/1000022614/nvidia-nvdaus-stock-flashes-a-warning-signal-valuation-hits-lowest)  
  <sub>Moomoo, 4 hours ago</sub>  
  Zhitong Finance APP has learned that NVIDIA (NVDA.US) shares are sending a warning signal about whether its profit growth can be sustained.
- [Nvidia: Trucks, Tokens, And A 28x Multiple](https://seekingalpha.com/article/4948600-nvidia-trucks-tokens-and-a-28x-multiple)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Nvidia Corporation Strong Buy: $108B revenue guide, 74% gross margin, Rubin platform upside and AI cloud risks. Click for this NVDA stock update.
- [NVDA Stock Is A ‘Bargain’ Trading 30% Below $280 Fair Value, Morningstar Says](https://stocktwits.com/news-articles/markets/equity/nvda-stock-bargain-trading-30-percent-below-fair-value/cZN43deRJP5)  
  <sub>Stocktwits, 9 hours ago</sub>  
  NVDA Stock Is A 'Bargain' Trading 30% Below $280 Fair Value, Morningstar Says. According to the research firm, NVDA now fits the profile of a “growth-at-...
- [Can Apple Overtake NVIDIA as the World's Most Valuable Company?](https://www.marketbeat.com/articles/can-apple-overtake-nvidia-as-the-worlds-most-valuable-company/)  
  <sub>MarketBeat, 43 minutes ago</sub>  
  For most of the past two years, NVIDIA Corporation NASDAQ: NVDA has stood at the summit of the stock market. As the chipmaker whose processors power much of...
- [Nvidia Price Prediction: Wall Street and Our Model Finally Agree](https://247wallst.com/investing/2026/09/22/nvidia-price-prediction-wall-street-and-our-model-finally-agree/)  
  <sub>24/7 Wall St., 38 minutes ago</sub>  
  NVDA targets $310 over 12 months, implying 40% upside from $228, with both our model and Wall Street consensus aligned on a BUY. AMD trades at a trailing...
- [Bull of the Day: NVIDIA Corp. (NVDA)](https://www.tradingview.com/news/zacks:d237027b6094b:0-bull-of-the-day-nvidia-corp-nvda/)  
  <sub>TradingView, 5 hours ago</sub>  
  NVIDIA Corp. NVDA is back to being a Zacks Rank #1 (Strong Buy).Are you in?NVIDIA is the leading AI and accelerated computing company in the world.
- [QUICK SPARK: Wall Street Is Moving Nvidia Onto Crypto Rails. 24/7 Trading Is Next](https://www.benzinga.com/crypto/cryptocurrency/26/09/61918726/nvidia-crypto-trading-rails)  
  <sub>Benzinga, 2 hours ago</sub>  
  Nvidia Corp (NASDAQ:NVDA) may be a Wall Street stock, but the way investors trade it, is starting to look increasingly like crypto.
- [Nvidia Stock Missed the AI Agent Rally. Here’s What Could Turn It Around.](https://www.barrons.com/articles/nvidia-stock-price-meta-ai-chips-rally-11911927)  
  <sub>Barron's, 3 hours ago</sub>  
  stock was left out of the latest chip rally sparked by Meta Platforms' · META. +11.43%. Muse agent. It's a sign that the market isn't seeing the chip...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 228.86 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 220.53 (+3.8%), 50d 215.11 (+6.4%), 200d 198.85 (+15.1%); 50d above 200d
Momentum: RSI(14) 59.4 | MACD 2.018 vs signal 1.602 (histogram 0.416)
Returns: 1d +0.7% | 5d +7.9% | 1m +6.6% | 3m +14.4%
52-week range: 165.17 - 235.74 (now 90.3% of the way up)
Volatility: ATR(14) 6.22 (2.7% of price) | annualised 20d 45.3%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 5.53T
Valuation: trailing P/E 28.93 | forward P/E 14.59 | P/B 24.13 | PEG 0.47
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
Price target: mean 327.70 (+43.2% vs last close), range 180.00 - 515.00
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
Last 180 days: bought 2,452,825 shares in 17 transaction(s) | sold 5,023,547 shares in 8
Net: -2,570,722 shares (-0.3% of insider holdings) | insiders hold 965,687,040 shares
Distinct insiders: 0 buying, 4 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-04 STEVENS MARK A (Director): 1,022,239 shares, 235.64M
  - 2026-09-02 STEVENS MARK A (Director): 1,848,501 shares, 410.84M
  - 2026-08-31 TETER TIMOTHY S (General Counsel): 30,000 shares, 6.54M
  - 2026-06-18 STEVENS MARK A (Director): 885,000 shares, 186.00M
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

- [Why Novo Nordisk Stock Just Crashed](https://finance.yahoo.com/markets/stocks/articles/why-novo-nordisk-stock-just-161429665.html)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  Novo Nordisk (NYSE: NVO) stock tumbled 8.1% through 11:35 a.m. ET Monday, and it has only itself to blame. Novo, you see, just told investors what to expect...
- [Novo and UNICEF expand partnership to support a healthier start for more than 80 million children](https://www.stocktitan.net/news/NVO/novo-and-unicef-expand-partnership-to-support-a-healthier-start-for-7fkm6ox7o6ak.html)  
  <sub>Stock Titan, 3 hours ago</sub>  
  Novo Nordisk (NVO) and UNICEF will expand their global partnership with a four-year childhood overweight and obesity prevention programme from 2027 to 2030,...
- [Novo eyes hair-loss market amid plans to diversify (NVO:NYSE)](https://seekingalpha.com/news/4645467-novo-eyes-hair-loss-market-amid-plans-diversify)  
  <sub>Seeking Alpha, 25 minutes ago</sub>  
  Novo Nordisk (NVO) announces plans to target the hair-loss market as part of its post-Wegovy strategy, boosting Veradermics (MANE) and Absci (ABSI).
- [Novo Nordisk’s stock tumbles as doubts persist about Ozempic maker’s strategy](https://www.marketwatch.com/story/novo-nordisk-stock-tumbles-as-ozempic-maker-sets-out-2030-goals-8a5a8d2d)  
  <sub>MarketWatch, 19 hours ago</sub>  
  Novo Nordisk CEO Mike Doustdar poses for a photo at Novo Nordisk's headquarters in Bagsvaerd, Denmark, in August. The stock tumbled on Monday after the drug...
- [Why Is Novo Nordisk Stock Climbing Premarket Today?](https://stocktwits.com/news-articles/markets/equity/why-is-novo-nordisk-stock-climbing-premarket-today/cZ0SCUBRex5)  
  <sub>Stocktwits, 18 hours ago</sub>  
  The UAE launch marks the start of Novo's global rollout, with additional launches planned later this year.
- [Why Novo Stock Is Tumbling After Drugmaker Unveils Ambitious Growth Plan](https://www.barrons.com/articles/novo-stock-growth-plan-wegovy-ozempic-5d86fa59)  
  <sub>Barron's, 20 hours ago</sub>  
  plans to launch at least five new “multi-blockbusters” by the end of the decade as part of an ambitious plan to stoke growth and counter slowing sales.
- [NVO Looks 61.9% Undervalued on GF Value™ as Dividend Remains Att](https://www.gurufocus.com/news/9091319/nvo-looks-619-undervalued-on-gf-value-as-dividend-remains-attractive)  
  <sub>GuruFocus, 4 hours ago</sub>  
  On September 22, 2026, Novo Nordisk AS (NYSE: NVO) CEO Mike Doustdar highlighted the company's need to strengthen investor trust amid looming patent...
- [Novo Nordisk (NYSE:NVO) Stock Sinks Nearly 8% as US$23 Billion Obesity Plan Fails to Win Over Investors](https://stocksdownunder.com/novo-nordisk-stock-sinks-8-obesity-plan/)  
  <sub>Stocks Down Under, 20 hours ago</sub>  
  Novo Nordisk stock is down about 8% today near April lows after its $23 billion pipeline plan and 2030 obesity targets failed to win over investors.
- [Goldman Sachs Sticks to Their Hold Rating for Novo Nordisk (0QIU)](https://www.theglobeandmail.com/investing/markets/stocks/NVO-N/pressreleases/4729089/goldman-sachs-sticks-to-their-hold-rating-for-novo-nordisk-0qiu/)  
  <sub>The Globe and Mail, 4 hours ago</sub>  
  Detailed price information for Novo Nordisk A/S ADR (NVO-N) from The Globe and Mail including charting and trades.
- [Morgan Stanley Downgrades Novo Nordisk (NYSE: NVO) As Semaglutide Patent Cliff Threatens Terminal Value](https://www.foreignpolicyjournal.com/2026/09/21/morgan-stanley-downgrades-novo-nordisk-nyse-nvo-as-semaglutide-patent-cliff-threatens-terminal-value/)  
  <sub>Foreign Policy Journal, 21 hours ago</sub>  
  Novo Nordisk A/S (NYSE: NVO) received a downgrade to Underweight from Morgan Stanley on September 11, 2026, sending shares down an additional 2% following...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 39.53 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 44.47 (-11.1%), 50d 46.51 (-15.0%), 200d 46.07 (-14.2%); 50d above 200d
Momentum: RSI(14) 30.5 | MACD -1.565 vs signal -1.097 (histogram -0.468)
Returns: 1d -0.7% | 5d -7.0% | 1m -15.4% | 3m -16.6%
52-week range: 35.29 - 63.98 (now 14.8% of the way up)
Volatility: ATR(14) 1.37 (3.5% of price) | annualised 20d 42.8%
Volume: 0.89x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 174.60B
Valuation: trailing P/E 9.81 | forward P/E 11.86 | P/B 5.12 | PEG 3.10
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
Price target: mean 46.65 (+18.0% vs last close), range 39.43 - 63.15
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

- [Teva’s comeback is real. The harder part is still ahead](https://www.calcalistech.com/ctechnews/article/p1rnr2p6o)  
  <sub>CTech, 7 hours ago</sub>  
  Last week, Richard Francis stood on the famous floor of the New York Stock Exchange, surrounded by a long line of senior Teva executives, and rang the bell...
- [Teva CEO Details Biopharma Pivot, $700M Savings Plan and Growth Pipeline](https://finance.yahoo.com/healthcare/articles/teva-ceo-details-biopharma-pivot-090251701.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Interested in Teva Pharmaceutical Industries Ltd.? Here are five stocks we like better. Teva is accelerating its shift toward biopharmaceuticals while...
- [Teva Pharmaceutical Industries Ltd (TEVA) Stock Up 3.5% but GF V](https://www.gurufocus.com/news/9090563/teva-pharmaceutical-industries-ltd-teva-stock-up-35-but-gf-value-says-overvalued-gf-score-47100)  
  <sub>GuruFocus, 17 hours ago</sub>  
  On September 21, 2026, Teva Pharmaceutical Industries Ltd (TEVA) shares rose 3.5% to a current price of $40.06. The stock has seen a significant price...
- [Teva stock hits 52-week high at $39.71](https://www.investing.com/news/company-news/teva-stock-hits-52week-high-at-3971-93CH-4909436)  
  <sub>Investing.com, 23 hours ago</sub>  
  Teva Pharmaceutical Industries Ltd ADR has reached a significant milestone, as its stock hit a 52-week high of $39.71. This marks a notable achievement for...
- [Teva Pharmaceutical Industries (TEVA), Why Is It Back In The Spotlight?](https://finance.yahoo.com/healthcare/articles/teva-pharmaceutical-industries-teva-why-191135979.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Teva Pharmaceutical Industries (NYSE:TEVA) is back in focus after its U.S. affiliate shared fresh Phase 3 SOLARIS data on investigational olanzapine LAI...
- [Teva at U.S. All Stars Conference: growth plan gains traction By Investing.com](https://in.investing.com/news/stock-market-news/teva-at-us-all-stars-conference-growth-plan-gains-traction-93CH-5600523)  
  <sub>Investing.com India, 7 hours ago</sub>  
  On Tuesday, 22 September 2026, Teva Pharmaceutical Industries Ltd. (TEVA) used the U.S. All Stars Conference to argue that its long turnaround has moved...
- [Teva Pharmaceutical Industries (NYSE:TEVA) Sets New 52-Week High - Still a Buy?](https://www.marketbeat.com/instant-alerts/price-teva-pharmaceutical-industries-nyse-teva-sets-new-52-week-high-still-a-buy-2026-09-21/)  
  <sub>MarketBeat, 22 hours ago</sub>  
  Teva Pharmaceutical Industries Ltd. (NYSE:TEVA - Get Free Report)'s share price hit a new 52-week high on Monday . The company traded as high as $39.72 and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 39.77 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 37.72 (+5.4%), 50d 35.65 (+11.6%), 200d 33.27 (+19.5%); 50d above 200d
Momentum: RSI(14) 64.6 | MACD 0.997 vs signal 0.807 (histogram 0.190)
Returns: 1d -0.7% | 5d +1.3% | 1m +6.5% | 3m +19.8%
52-week range: 18.34 - 40.06 (now 98.7% of the way up)
Volatility: ATR(14) 1.20 (3.0% of price) | annualised 20d 32.8%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 46.38B
Valuation: trailing P/E 66.28 | forward P/E 13.09 | P/B 5.98 | PEG 0.71
Profitability: profit margin 4.1% | operating margin 4.0% | ROE 9.7%
Growth (YoY): revenue -0.8% | earnings n/a
Balance sheet: debt/equity 217.8% | free cash flow 2.22B
Risk: beta 0.80 | short interest n/a of float
Next earnings: 2026-11-04
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
Consensus: buy (mean 1.67 on a 1=strong buy to 5=strong sell scale, 2 analysts)
Ratings: 2 strong buy, 1 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 41.00 (+3.1% vs last close), range 40.00 - 42.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

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

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

## Whole-market funds

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.35

**In the model's own words:**

> IWM has retreated 2.8% from its 50-day moving average and 4.4% over the month, with RSI at 40.4 and negative MACD histogram indicating weakening momentum. The technical picture shows downside pressure after a strong run to the 76th percentile of the 52-week range. However, macro backdrop remains supportive: Treasury yields have declined slightly on the long end, the yield curve is normally sloped, and the Fed is expected to cut rates modestly over the next two years. The dollar has strengthened week-on-week, which can weigh on small-cap performance. Volatility remains calm at VIX 14.4. Fund fundamentals show elevated valuation (P/E 17.3, P/B 2.13) with a high beta of 1.24, making the fund sensitive to both market moves and rate changes. The analyst slice covering 1.7% of holdings shows all buy ratings with +24% upside, but this is too thin to drive conviction on the full fund. CFTC positioning shows large speculators net short at the 30th percentile of crowding—neutral terrain with a modest increase in shorts on the week. Fund flows data is insufficient. A recent Seeking Alpha note warned of unprofitable small-cap growth and biotech risk with weak momentum—a view not contradicted by the technicals, though built on thin analyst coverage. The combination of moderately negative technicals, stretched valuation, and positioning that is neither extreme nor clearly supportive justifies a neutral stance with slight bearish lean, pending clarification from either a technical rebound or macro catalyst.

**Main reasons it gave:**
- Price 2.8% below 50-day MA with negative MACD and RSI 40.4 suggesting momentum weakness
- P/E 17.3 and P/B 2.13 valuations elevated relative to small-cap historical norms
- Large speculators net short 19.6% of open interest with +6% weekly increase in shorts
- Fed rate path priced to ~4 quarter-point cuts over two years, providing modest tailwind but not offset by current technicals

<details><summary><b>News</b> — score -0.25</summary>

- [IWO ETF: An Unprofitable Small-Cap Tilt Warrants Caution (NYSEARCA:IWO)](https://seekingalpha.com/article/4948479-iwo-unprofitable-small-cap-tilt-warrants-caution)  
  <sub>Seeking Alpha, 12 hours ago</sub>  
  Sell-rated iShares Russell 2000 ETF (IWO): unprofitable small-cap growth, biotech-heavy risk, weak momentum & downside signals. See more here.
- [Exchange-Traded Funds Rise as US Equities Advance After Midday](https://www.moomoo.com/news/post/76545775/exchange-traded-funds-rise-as-us-equities-advance-after-midday)  
  <sub>Moomoo, 21 hours ago</sub>  
  BroadMarket IndicatorsBroad-market exchange-traded funds IWM and IVV were higher. Actively traded Invesco QQQ Trust (QQQ) added 2.5%.US equity indexes rose...
- [Daily ETF Flows: COWZ Gobbles Up Assets](https://www.etf.com/sections/daily-etf-flows/daily-etf-flows-cowz-gobbles-assets)  
  <sub>ETF.com, 17 hours ago</sub>  
  Here are the daily ETF fund flows for September 18, 2026.
- [6 Best Vanguard ETFs for 2026 and How to Invest](https://www.fool.com/investing/how-to-invest/etfs/top-vanguard-etfs/)  
  <sub>The Motley Fool, 10 hours ago</sub>  
  Vanguard ETFs (exchange-traded funds) have become synonymous with low-cost, long-term investing, and remain among the most widely held ETFs worldwide.
- [Nasdaq 100 Rallies, Intel Soars 14%: Stock Market Today](https://www.tradingview.com/news/benzinga:0886239d6094b:0-nasdaq-100-rallies-intel-soars-14-stock-market-today/)  
  <sub>TradingView, 21 hours ago</sub>  
  U.S. equities extended their winning streak to a third session Monday, with a fourth consecutive slide in crude oil relieving pressure on Treasury yields...
- [Ameriprise keeps S&P 500 year-end target at 8,000 despite higher-for-longer rate risks](https://www.bitget.com/amp/news/detail/12560605853460)  
  <sub>Bitget, 18 hours ago</sub>  
  Ameriprise kept its 2026 year-end S&P 500 target at 8000, citing improving earnings expectations despite higher yields. Full-year 2026 S&P 500 | Bitget...
- [September Stagnation Marked By Record-Low Yields, High Duration Risk And High Valuations](https://seekingalpha.com/article/4948565-september-stagnation-marked-by-record-low-yields-high-duration-risk-high-valuations)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Over the first nine months of 2026, we have witnessed a fascinating macro paradox: a surging US stock market decoupling completely from the bond market.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.25</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 286.65 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 291.20 (-1.6%), 50d 294.80 (-2.8%), 200d 275.22 (+4.2%); 50d above 200d
Momentum: RSI(14) 40.4 | MACD -3.265 vs signal -2.683 (histogram -0.581)
Returns: 1d +0.4% | 5d +0.5% | 1m -4.4% | 3m -2.9%
52-week range: 229.11 - 305.09 (now 75.7% of the way up)
Volatility: ATR(14) 3.44 (1.2% of price) | annualised 20d 11.6%
Volume: 0.45x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

```text
Fund type: Small Blend
What it holds: P/E 17.30 | P/B 2.13 | P/S 1.31 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +17.4% a year | beta to the market 1.24
Cost and size: expense ratio 0.19% | net assets 80.46B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: JFrog Ltd Ordinary Shares 0.3%, Moog Inc Class A 0.3%, BlackRock Cash Funds Treasury SL Agency 0.3%, UMB Financial Corp 0.3%, Glaukos Corp 0.3%
Sector mix: Healthcare 21.0%, Financial services 18.1%, Technology 13.8%, Industrials 13.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 1.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.0% above the current prices
Holdings read: FROG, MOG-A, XTSLA, UMBF, GKOS
Recent rating changes among them:
  - FROG: 2026-09-04 DA Davidson: main, Buy -> Buy
  - MOG-A: 2026-09-15 Guggenheim: init, ? -> Neutral
  - UMBF: 2026-09-14 UBS: init, ? -> Neutral
  - GKOS: 2026-08-20 BTIG: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 19.6% of open interest (496,762 contracts)
Change on the week: +6.0% of open interest
Crowding: 30% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 281.05M | fund size: 80.56B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Farm goods basket (DBA) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> DBA is a commodity-focused fund holding primarily short-term Treasuries (43.1% in AGPXX, 4.4% in TBLL) and 46.2% cash, with only 2% in actual commodities exposure. The fund's construction makes it largely a fixed income vehicle rather than an agricultural commodity play despite its ticker. Near-term technicals show weak momentum (RSI 50.3, MACD histogram negative, volume 0.17x average) with price 0.9% below the 20-day SMA, and the fund sits near the top of its 52-week range (78.6%). Macro backdrop is calm (VIX 14.42, down 2.8 on the week) with a normal upward-sloping yield curve. The news about record diesel prices and grain strength is real but represents less than 10% of the fund's actual holdings, making macro agricultural stress largely irrelevant to DBA's returns—the fund benefits from falling short-term rates more than commodity prices. The positive Trump-Xi summit sentiment supporting grains is offset by the fund's heavy Treasury weighting, which would suffer if rate expectations shift. The 3-year record of +12.7% annually reflects the recent Treasury rally, not commodity strength, and the current price action lacks conviction to change the directional call. This is not a pure-play commodity fund.

**Main reasons it gave:**
- Fund is 46.2% cash and 47.5% short-term Treasuries, not agricultural commodities
- Momentum indicators deteriorating: RSI neutral, MACD histogram negative, volume well below average
- Record diesel prices and grain strength largely irrelevant to fund's Treasury-focused holdings
- Price near 52-week highs with weak follow-through, no conviction from technicals

<details><summary><b>News</b> — score +0.15</summary>

- [US Diesel Prices Surge Past $6.50: The Agriculture ETFs Caught in the Crossfire](https://www.benzinga.com/etfs/sector-etfs/26/09/61908038/us-diesel-prices-surge-past-6-50-the-agriculture-etfs-caught-in-the-crossfire)  
  <sub>Benzinga, 19 hours ago</sub>  
  U.S. diesel prices hit a record $6.50 a gallon, putting fresh pressure on farmers. Here's what soaring fuel costs could mean for agriculture ETFs.
- [U.S. grains rally ahead of 'positive' Trump-Xi summit, continued Russia-Ukraine fighting](https://seekingalpha.com/news/4645187-us-grains-rally-ahead-of-positive-trump-xi-summit-continued-russia-ukraine-fighting)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  US grain futures rose after initial US-China trade talks were called positive by both sides, raising hopes the Trump-Xi meeting will include Chinese...
- [US diesel hits record $6.51 as supply deficit deepens despite WTI drop](https://scanx.trade/stock-market-news/commodities/newsom-signs-e15-gas-bill-california-fuel-prices-top-6-iran-tensions/51532724)  
  <sub>scanx.trade, 19 hours ago</sub>  
  US diesel prices hit a record high of $6.51/gal on Sep 21, 2026, driven by geopolitical tensions and infrastructure damage. Farm fuel costs rose by $11/acre...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 28.62 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 28.89 (-0.9%), 50d 28.28 (+1.2%), 200d 27.07 (+5.8%); 50d above 200d
Momentum: RSI(14) 50.3 | MACD 0.094 vs signal 0.203 (histogram -0.108)
Returns: 1d -0.2% | 5d -0.9% | 1m +1.1% | 3m +7.6%
52-week range: 25.44 - 29.49 (now 78.6% of the way up)
Volatility: ATR(14) 0.30 (1.1% of price) | annualised 20d 14.7%
Volume: 0.17x the 20-day average
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
Three-year record: +12.7% a year | beta to the market 0.35
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 27.60M | fund size: 790.05M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> DBC is a broad commodity basket that has rallied sharply off its 52-week lows (90.4% of the way up from the range), supported by a three-month return of +20.1%. However, momentum is rolling over: RSI at 58.3 is elevated but not extreme, MACD histogram has turned negative, and volume is well below average at 0.27x the 20-day mean, suggesting the rally is losing conviction. The technical picture shows the price above all three moving averages with the 50d above the 200d, which is structurally bullish, but the recent 5-day drawdown of -3.3% and weak volume argue against adding exposure here. On the macro side, the dollar strengthened +0.93 on the week to 100.58, which headwinds commodities priced in dollars; Treasury yields moved marginally with the long end lower, which is neutral for commodities. The Fed's rate path shows the market pricing roughly 4 quarter-point hikes over two years, consistent with a slow normalization. Energy inventories show a crude draw (bullish signal) at the 38th percentile, but natural gas built (bearish) at the 71st percentile. The EIA outlook is mixed: WTI crude is forecast to fall 10% over six months to $70 by year-end, which tempers bullish sentiment, while natural gas is expected to rise 7%, supporting some holdings. The fund holds 44.8% cash and only 8.9% Brent crude futures as its largest single commodity position, making it a defensive basket with limited beta to any single commodity move. No news, no analyst coverage, and no clear flow data to assess conviction. The rally has been substantial but is showing fatigue; the macro backdrop offers no clear catalyst, and the technical structure, while not broken, is losing momentum on light volume. A modest risk-off tone from the dollar strength and the EIA's bearish six-month WTI view offsets the constructive seasonal backdrop and recent outperformance.

**Main reasons it gave:**
- MACD histogram turned negative despite price strength, divergence warns of momentum fade
- EIA crude outlook falls 10% over six months to $70, tempering upside
- US dollar index +0.93 on the week headwinds dollar-priced commodities
- Volume at 0.27x 20-day average on recent weakness signals lower conviction in rally
- Crude oil draw at 38th percentile (bullish signal) but natural gas build at 71st percentile (bearish)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.35</summary>

```text
Last close 32.56 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 32.24 (+1.0%), 50d 30.65 (+6.2%), 200d 27.79 (+17.2%); 50d above 200d
Momentum: RSI(14) 58.3 | MACD 0.714 vs signal 0.812 (histogram -0.098)
Returns: 1d -0.1% | 5d -3.3% | 1m +4.2% | 3m +20.1%
52-week range: 22.07 - 33.68 (now 90.4% of the way up)
Volatility: ATR(14) 0.47 (1.4% of price) | annualised 20d 19.2%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Commodities Broad Basket
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 2.4%
Three-year record: +13.8% a year | beta to the market 1.05
Cost and size: expense ratio 0.85% | net assets 1.80B
What it is made of: Other 50.6%, Cash 44.8%, Bonds 2.7%, Stocks 1.9%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 40.8%, Brent Crude Future Nov 26 8.9%, Invesco Short Term Treasury ETF 6.2%, Mini Ibovespa Future Dec 26 1.9%
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
US inventories, week ending 2026-09-11 (published the following Wednesday)
  Crude oil: 423.4 million barrels, -0.6 on the week (a draw), 38% percentile over 52 weeks
  Natural gas: 3,298.0 billion cubic feet, +44.0 on the week (a build), 71% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.10</summary>

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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 54.45M | fund size: 1.77B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> HYG is a high-yield bond fund facing mixed signals that do not support a directional call. On the positive side, the macro backdrop remains supportive: the yield curve is normal and upward-sloping, the dollar has strengthened, and the VIX is calm at 14.42, indicating low volatility and risk appetite. The Fed's recent discount window modernization, mentioned in the news, supports banking resilience. The fund's 5.9% yield remains attractive in absolute terms. However, technical deterioration and soft fund dynamics outweigh these supports. Price is now 10% of the way up from the 52-week low, sitting below all major moving averages (20d, 50d, 200d), with the 50d below the 200d signaling a downtrend. Momentum has rolled over: RSI at 39.4 is in oversold territory but the MACD remains in sell mode with negative histogram. Returns are negative across 1m (-1.2%) and 3m (-1.5%) timeframes. Critically, volume is only 0.17x the 20-day average, indicating weak conviction and shallow liquidity behind any move. Fund flow direction is unknown and share count readings are too sparse to assess conviction from inflows or outflows. The news is neutral to mixed: comparisons to fallen angels and term fund structures are contextual, and the analyst note flagging neutral sentiment and a wait-and-see approach aligns with this assessment. Treasuries have moved modestly; the short end ticked up 5bp on the week while the long end eased, a pattern that historically supports credit but is not decisive in isolation. Credit spreads themselves are not provided. The fund's 0.67 beta to the market and large cash position provide some stability, but the technical picture argues against initiating a bullish stance, while the macro environment lacks a clear trigger for a bearish call. This is a hold and monitor posture.

**Main reasons it gave:**
- Price below 20d, 50d, and 200d moving averages; 50d below 200d
- RSI oversold at 39.4 with MACD histogram negative
- Volume 0.17x average; weak conviction behind price action
- VIX calm, curve normal, and 5.9% yield supportive but insufficient to overcome technicals
- Neutral analyst sentiment; unknown fund flow direction

<details><summary><b>News</b> — score +0.00</summary>

- [Precision Trading with Ishares Iboxx Usd High Yield Corporate Bond Etf (HYG) Risk Zones](https://news.stocktradersdaily.com/news_release/22/Precision_Trading_with_Ishares_Iboxx_Usd_High_Yield_Corporate_Bond_Etf_HYG_Risk_Zones_092126085002_1790038202.html)  
  <sub>Stock Traders Daily, 18 hours ago</sub>  
  Key findings for Ishares Iboxx Usd High Yield Corporate Bond Etf (NYSE: HYG). Full Alignment in Neutral Sentiment Favors Wait-and-See Approach...
- [HYBR11 ETF Holdings List — BMFBOVESPA:HYBR11](https://www.tradingview.com/symbols/BMFBOVESPA-HYBR11/holdings/)  
  <sub>TradingView, 18 hours ago</sub>  
  Explore Nu iBoxx High Yield Hedge Carry BRL ETF holdings with weight, market value, and other helpful data to make more informed decisions for HYBR11...
- [FALN: The Benefits And Risks Of This Fallen Angels Bond ETF](https://seekingalpha.com/article/4943886-faln-benefits-and-risks-of-this-fallen-angels-bond-etf)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  iShares Fallen Angels USD Bond ETF: strategy, duration/rate risk vs. HYG, returns since 2016, and FALN vs. ANGL. Learn more about the FALN ETF here.
- [FTHY: Anticipated Termination Coming But Likely To Seek Perpetual Structure (NYSE:FTHY)](https://seekingalpha.com/article/4948468-fthy-anticipated-termination-coming-but-likely-to-seek-perpetual-structure)  
  <sub>Seeking Alpha, 14 hours ago</sub>  
  First Trust High Yield Opportunities 2027 Term Fund (FTHY): discount widening, weak coverage, and a likely tender offer/perpetual vote. See more here.
- [Fed's discount window modernization supports banks, broader market resilience: Governor Jefferson (TLT:NASDAQ)](https://seekingalpha.com/news/4645436-feds-discount-window-modernization-supports-banks-broader-market-resilience-governor-jefferson)  
  <sub>Seeking Alpha, 33 minutes ago</sub>  
  Fed's modernization efforts will ensure that the discount window supports individual banking institutions and broader market resilience, according to the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 78.68 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 79.05 (-0.5%), 50d 79.35 (-0.9%), 200d 80.01 (-1.7%); 50d below 200d
Momentum: RSI(14) 39.4 | MACD -0.266 vs signal -0.243 (histogram -0.024)
Returns: 1d -0.0% | 5d +0.4% | 1m -1.2% | 3m -1.5%
52-week range: 78.38 - 81.32 (now 10.0% of the way up)
Volatility: ATR(14) 0.22 (0.3% of price) | annualised 20d 4.3%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 206.39M | fund size: 16.24B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> LQD is the largest investment-grade corporate bond ETF with a solid 4.7% yield and high-quality portfolio (59% A-rated or better). The fund's fundamentals are in-line with market averages with no idiosyncratic catalyst. Technicals show a fund in a mild downtrend: price is 3.4% below its 200-day moving average, RSI at 44.9 indicates neither oversold nor overbought conditions, and MACD histogram has just turned positive but remains in negative territory overall. The 52-week range places the fund near its lows (8.9% up from bottom), suggesting limited upside momentum. Volume is light at 0.21x average. Macro backdrop is stable: the yield curve is normally sloped at +0.95, VIX is calm at 14.42, and the Fed has signaled a path of modest further easing (market prices roughly 4 quarter-point cuts over two years). Recent inflation at 3.4% and unemployment at 4.1% are neither surprising nor recessionary. The discount window modernization comment from Fed Governor Jefferson provides minor support for financial stability but does not constitute a material surprise. With no macro catalyst, no technical breakdown or breakout, no analyst or positioning data showing conviction, and the fund trading with weak momentum and below moving averages, a modest near-term consolidation seems most likely. The yield support is real but insufficient to overcome the technical headwinds without a rate surprise or credit catalyst.

**Main reasons it gave:**
- Price 3.4% below 200-day MA in downtrend
- RSI 44.9 and MACD histogram near zero shows weak momentum
- Yield curve normal and VIX calm—no macro urgency
- 4.7% yield provides support but insufficient to break technical resistance

<details><summary><b>News</b> — score +0.00</summary>

- [LQD: Largest Investment-Grade Corporate Bond ETF In The Market, Weak Investment Thesis](https://seekingalpha.com/article/4948567-lqd-largest-investment-grade-corporate-bond-etf-in-the-market-weak-investment-thesis)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  LQD yields 4.8% with a high-quality portfolio, and a duration of 7.7 years, with fundamentals in-line with market averages. Read more on the LQD ETF here.
- [iShares iBoxx $ Inv Grade Corporate Bond ETF of...](https://pluang.com/en/news-feed/lqd-etf-obligasi-korporasi-investment-grade-terbesar-dengan-teori-lemah)  
  <sub>Pluang, 4 hours ago</sub>  
  The iShares iBoxx $ Investment Grade Corporate Bond ETF (LQD) is the largest ETF in the investment-grade corporate bond market, managing $27.5 billion in...
- [Fed's discount window modernization supports banks, broader market resilience: Governor Jefferson (TLT:NASDAQ)](https://seekingalpha.com/news/4645436-feds-discount-window-modernization-supports-banks-broader-market-resilience-governor-jefferson)  
  <sub>Seeking Alpha, 32 minutes ago</sub>  
  Fed's modernization efforts will ensure that the discount window supports individual banking institutions and broader market resilience, according to the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 105.04 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 105.35 (-0.3%), 50d 106.03 (-0.9%), 200d 108.73 (-3.4%); 50d below 200d
Momentum: RSI(14) 44.9 | MACD -0.418 vs signal -0.464 (histogram 0.046)
Returns: 1d -0.0% | 5d +0.7% | 1m -0.8% | 3m -3.5%
52-week range: 104.28 - 112.92 (now 8.9% of the way up)
Volatility: ATR(14) 0.49 (0.5% of price) | annualised 20d 6.4%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.05</summary>

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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 306.32M | fund size: 32.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> SHY is a short-duration government bond fund holding nearly all US Treasuries with a 3.6% yield. The macro backdrop shows a normally sloped curve with the 3-month at 4.01% and 10-year at 4.96%; the 2-year at 4.76% prices roughly 4 quarter-point cuts over the next two years, which is consistent with inflation at 3.4% and unemployment at 4.1%. The dollar rallied sharply (+0.93 on the week) on hawkish Fed expectations, but this affects SHY's total return only through the negligible currency exposure of a US government bond fund. Technicals are uniformly weak: price is 1.2% below the 200-day moving average, RSI at 33.8 is in oversold territory but volume is light at 0.32x average, momentum histogram is negative, and returns are flat to down across all horizons. The 52-week range places the fund near its lows. CFTC positioning in the 2-year note shows net large-speculator shorts at 29.2% of open interest, at the 95th percentile of crowding—which by the prompt's logic is as often a sign of an exhausted move as its middle. Fund flows data is insufficient. The weakness in technicals combined with crowded short positioning creates a modest contrarian case for stabilization, but SHY's returns are driven by yield carry and duration risk, not mean reversion. With the curve normal, yields stable week-over-week at the short end, and no policy surprise, there is no macro catalyst. A weak bounce is plausible on technicals alone, but conviction must remain low given the absence of a decisive driver.

**Main reasons it gave:**
- 3-month yield stable at 4.01% with no Fed surprise this week
- Large speculators crowded short (95th percentile) in 2Y note—extremes often exhaust
- RSI 33.8 in oversold on light volume, technical bounce possible but not confirmed
- Price 1.2% below 200d SMA with flat 5d and 1m returns, no uptrend

<details><summary><b>News</b> — score +0.00</summary>

- [The Weekly Spread: What Shaped Yields And The Dollar This Week](https://stocktwits.com/news-articles/markets/equity/the-weekly-spread-what-shaped-yields-and-the-dollar-this-week/cZtDZlBRBES)  
  <sub>Stocktwits, 6 hours ago</sub>  
  A hawkish interest rate hike by the Federal Reserve and expectations of further tightening propelled the U.S. dollar to its strongest weekly gain since June...
- [Fed's discount window modernization supports banks, broader market resilience: Governor Jefferson (TLT:NASDAQ)](https://seekingalpha.com/news/4645436-feds-discount-window-modernization-supports-banks-broader-market-resilience-governor-jefferson)  
  <sub>Seeking Alpha, 31 minutes ago</sub>  
  Fed's modernization efforts will ensure that the discount window supports individual banking institutions and broader market resilience, according to the...
- [A Record ETF Year Takes Shape as Inflows Near $1.5 Trillion](https://www.etf.com/sections/weekly-etf-flows/record-etf-year-takes-shape-inflows-near-15-trillion)  
  <sub>ETF.com, 17 hours ago</sub>  
  US-listed ETFs took in $91.9 billion last week, pushing 2026 inflows to about $1.47 trillion, nearly matching all of last year's record with three months to...
- [Bitcoin ETFs Could Triple Gold Funds Within 5 Years](https://etfdb.com/coinshares-crypto-etf-hub/coinshares-channel/bitcoin-etfs-triple-gold-funds/)  
  <sub>ETF Database, 23 hours ago</sub>  
  U.S. spot bitcoin exchange-traded funds needed less than two years to approach $120 billion in assets, a pace that took gold ETFs well over a decade to...
- [NEAR: Low-Risk Multisector Bond ETF (BATS:NEAR)](https://seekingalpha.com/article/4948373-near-low-risk-multisector-bond-etf)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Explore iShares NEAR ETF: actively managed short-duration, investment-grade bonds with ~4.5% yield, low risk, and strong returns—see if it fits now.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 81.31 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 81.59 (-0.3%), 50d 81.80 (-0.6%), 200d 82.33 (-1.2%); 50d below 200d
Momentum: RSI(14) 33.8 | MACD -0.172 vs signal -0.147 (histogram -0.025)
Returns: 1d +0.0% | 5d -0.0% | 1m -0.8% | 3m -0.8%
52-week range: 81.24 - 83.18 (now 3.6% of the way up)
Volatility: ATR(14) 0.10 (0.1% of price) | annualised 20d 1.9%
Volume: 0.32x the 20-day average
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 29.2% of open interest (4,433,736 contracts)
Change on the week: +0.5% of open interest
Crowding: 95% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 319.03M | fund size: 25.94B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> VWO is a diversified emerging-markets fund holding 95.3% stocks with a 0.75 market beta and three-year annualized returns of +17.6%. The technical picture shows the fund near 52-week highs (94.4% of range), trading above its 20d, 50d, and 200d moving averages with a normal positive slope to the curve. Recent price action is mixed: +2.9% over 5 days but flat on the month (+0.8%), with RSI at 56.4 (mid-range, neither extended nor weak) and MACD just rolling over into negative territory. Volume is notably light at 0.30x the 20-day average, which dampens conviction in any directional move. The macro backdrop is supportive: the yield curve is normal (not inverted), the dollar has strengthened modestly (+0.93 on the week), VIX is calm at 14.42, and inflation expectations remain contained at 2.3% over 10 years. US jobless claims at 196k are stable. However, analyst coverage is thin (22.2% of holdings), showing 100% buy ratings with +34.4% upside, but this applies to only the five largest holdings and cannot be confidently extrapolated to the full fund. CFTC positioning in EM futures shows net long at 37th percentile—within normal range with a modest net reduction of 0.9 percentage points on the week, suggesting no exceptional conviction among large speculators. Fund flows data is unavailable (too few readings). The macro environment offers no clear catalyst for a directional shift: rates and inflation are stable, policy is on a known path, and the fund sits at the high end of its range on light volume. Technical strength is real but late in the move, and thin analyst coverage prevents a stronger bullish lean.

**Main reasons it gave:**
- Trading near 52-week highs on light volume; MACD rolling negative despite price strength
- Thin analyst coverage (22.2% of fund) limits conviction on the +34.4% target cited
- EM futures positioning at 37th percentile crowding with net reduction on the week
- Macro backdrop stable but not catalytic: normal yield curve, contained inflation, no rate surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Daily ETF Flows: COWZ Gobbles Up Assets](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-cowz-gobbles-210028745.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Top 10 Creations (All ETFs). Ticker. Name. Net Flows ($, mm). AUM ($, mm). AUM % Change. IVV · iShares Core S&P 500 ETF. 8,519.50. 845,149.30. 1.01%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.35</summary>

```text
Last close 60.93 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 60.49 (+0.7%), 50d 59.76 (+2.0%), 200d 57.73 (+5.5%); 50d above 200d
Momentum: RSI(14) 56.4 | MACD 0.094 vs signal 0.101 (histogram -0.006)
Returns: 1d -0.3% | 5d +2.9% | 1m +0.8% | 3m +2.7%
52-week range: 52.42 - 61.44 (now 94.4% of the way up)
Volatility: ATR(14) 0.62 (1.0% of price) | annualised 20d 13.1%
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
Three-year record: +17.6% a year | beta to the market 0.75
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 22.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.34 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +34.4% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 2308.TW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 3.3% of open interest (1,310,241 contracts)
Change on the week: -0.9% of open interest
Crowding: 37% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 1.42B | fund size: 86.41B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise this cycle: US yields little changed, VIX calm at 14.4, curve normally sloped. VGK sits just below its 20d and 50d SMAs with negative MACD and RSI 42, but still above the 200d and up 2.2% over three months — a mild consolidation, not a break, and volume is only 0.29x average. Dollar up 0.93 on the week is a modest headwind for unhedged European equity. Holdings valuation is reasonable (P/E 17.9, 2.8% yield) and the thin analyst roll-up over 11.4% of the fund is constructive but not decisive. EAFE speculative net long at the 95th percentile argues against chasing upside. ECB note on Chinese competition to German industry is a slow-burn structural point, not a catalyst.

**Main reasons it gave:**
- Price below 20d and 50d SMA but 1.9% above 200d; RSI 42, MACD histogram -0.23
- Volume 0.29x 20-day average — no conviction behind the pullback
- 10y -4bp, 30y -7bp, VIX -2.8 to 14.4: no rate or vol surprise
- EAFE spec net long at 95th percentile of 52 weeks, crowded long
- Dollar index +0.93 on the week, headwind for unhedged Europe exposure

<details><summary><b>News</b> — score -0.10</summary>

- [Germany faces two-front squeeze from Chinese factory strength, ECB says (DAX:NASDAQ)](https://seekingalpha.com/news/4645393-germany-faces-two-front-squeeze-from-chinese-factory-strength-ecb-says)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  ECB analysis: China's move up the value chain pressures Germany's autos, machinery and capital goods as China rivals exports and imports less from Europe.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 89.11 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 90.53 (-1.6%), 50d 90.59 (-1.6%), 200d 87.43 (+1.9%); 50d above 200d
Momentum: RSI(14) 42.2 | MACD -0.649 vs signal -0.423 (histogram -0.226)
Returns: 1d -0.1% | 5d +0.2% | 1m -3.9% | 3m +2.2%
52-week range: 77.90 - 93.19 (now 73.3% of the way up)
Volatility: ATR(14) 0.87 (1.0% of price) | annualised 20d 11.4%
Volume: 0.29x the 20-day average
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
Three-year record: +17.6% a year | beta to the market 0.90
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 11.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 65.7% | hold 34.3% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.7% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, NOVN.SW, SHEL.L
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 4.7% of open interest (626,488 contracts)
Change on the week: -0.4% of open interest
Crowding: 95% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 441.87M | fund size: 39.38B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 93.82 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 94.09 (-0.3%), 50d 94.65 (-0.9%), 200d 95.65 (-1.9%); 50d below 200d
Momentum: RSI(14) 45.3 | MACD -0.383 vs signal -0.394 (histogram 0.011)
Returns: 1d +0.0% | 5d +0.9% | 1m -1.0% | 3m -2.5%
52-week range: 92.95 - 97.74 (now 18.2% of the way up)
Volatility: ATR(14) 0.39 (0.4% of price) | annualised 20d 5.7%
Volume: 0.30x the 20-day average
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
Three-year record: +8.9% a year | beta to the market 1.08
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 159.90M | fund size: 15.00B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [The Technical Signals Behind (IEF) That Institutions Follow](https://news.stocktradersdaily.com/news_release/12/The_Technical_Signals_Behind_IEF_That_Institutions_Follow_092126110002_1790046002.html)  
  <sub>Stock Traders Daily, 16 hours ago</sub>  
  Price-action only: Ishares 7-10 Year Treasury Bond Etf (IEF) movements set the tone for institutional models. The Technical Signals Behind (IEF) That...
- [The Bond Market's Big Re-Steepening](https://finance.yahoo.com/markets/options/articles/bond-markets-big-steepening-040150357.html)  
  <sub>Yahoo Finance, 11 hours ago</sub>  
  The Federal Reserve's rate hike last week, its first in three years, capped a shift that had been building in the bond market for months.
- [Fed's discount window modernization supports banks, broader market resilience: Governor Jefferson (TLT:NASDAQ)](https://www.google.com/goto?url=CAESvQEB6zswFUlCT17hgEJHU1nutb0_0Ft_rDrgc4DzamZIxSxvuuYbQKUGGCEFb8pfqUCYGouY8HADBe3VGvJ6SLUxzBtIP-YPY2_xg-17-jGOL07-zugexnf44pUxkanNW05VNdyPNp3xqb0Z1v7u7sHi0qWFjtXNgXctvJ8ohCXrkxGRVinPKwYMYvvbJf11UurqsiGQKw8j0XzPQttPuMvehKlnzgaGjetUFI8-IffLNcW7kj9nAXhBTpahyIQ)  
  <sub>Seeking Alpha, 32 minutes ago</sub>  
  Fed's modernization efforts will ensure that the discount window supports individual banking institutions and broader market resilience, according to the...
- [Capital Flows in US Equities and Insights into the Derivatives Market Amid Accumulating Macro Risks: The Interplay Between Hedge Fund De-leveraging and Long-Term Capital Inflows](https://www.google.com/goto?url=CAESnwEB6zswFQYrBjF-0HQezhrMpJyt_61-4sSh69POK8mKIidPfO-p6lpBVRn0b8WIi1cpxYQVPRwRwZhX0_fofZ7M9muZgEFciuvMAmScnNGZDTXu-Ub3DRp-n5voxc-_HMaJifQkjjvwpEiMG5FwJp9VLpWcN8j3i3uakhia1pPBPK5p-bYeOzJXamacFNniXEI9x3VYtSwAmyGlG0TcOSs)  
  <sub>富途牛牛, 11 hours ago</sub>  
  MainpointsAccumulating macro risks have prompted hedge funds to reduce their equity holdings, but robust long-term inflows have provided support.
- [Yardeni Research Says Warsh 'Fails First Credibility Test' As 30-Year Treasury Yield Tops 5%](https://stocktwits.com/news-articles/markets/equity/yardeni-research-says-warsh-fails-first-credibility-test-as-30-year-treasury-yield-tops-5/cZNPMioRJc5)  
  <sub>Stocktwits, 22 hours ago</sub>  
  The yield on the 30-year U.S. Treasury bond spiked over 5%, touching levels not seen since the global financial crisis of 2007 after the Federal Reserve's...
- [Applovin Stock In Focus Amid Reportedly Ongoing SEC Probe; Convequity Says Wait For The Dip Before Investing](https://www.google.com/goto?url=CAESjwEB6zswFas79ZG0xjQtlaT4P_bpGVMU9a2YN2ppAAuqumRWSx5zfQ4CUKZSAsHSxKoEZK_-G5VwEMS0uPXseRh2zqz--et9GmqtcAb_pdHbzs08T4V4X-Lzx1TFCFAYnEya9vlqX8kV2aIXSv1eHmdcCRc8yTwK00ompg672kaXeWtw-eBKJfj3vXto_Ri3-A)  
  <sub>Stocktwits, 18 hours ago</sub>  
  The SEC stated to Bloomberg News that an “investigation involving AppLovin is still active and ongoing”.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 91.14 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 91.88 (-0.8%), 50d 92.66 (-1.6%), 200d 94.75 (-3.8%); 50d below 200d
Momentum: RSI(14) 37.8 | MACD -0.553 vs signal -0.517 (histogram -0.037)
Returns: 1d -0.0% | 5d +0.4% | 1m -1.8% | 3m -3.2%
52-week range: 90.73 - 97.99 (now 5.7% of the way up)
Volatility: ATR(14) 0.38 (0.4% of price) | annualised 20d 5.5%
Volume: 0.35x the 20-day average
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 460.82M | fund size: 42.00B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Invesco S&P 500 Equal Weight ETF declares quarterly distribution of $0.7951](https://www.tradingview.com/news/seekingalpha:f3a141f84094b:0-invesco-s-p-500-equal-weight-etf-declares-quarterly-distribution-of-0-7951/)  
  <sub>TradingView, 21 hours ago</sub>  
  Content provided by Seeking Alpha is intended for information purposes only, and that Seeking Alpha does not offer any personalist investment advice and is...
- [S&P 500 Snapshot: Stocks Edge Lower for 2nd Straight Week](https://etfdb.com/fixed-income-content-hub/stocks-lower-for-2nd-straight-week-s-p-500-snapshot/)  
  <sub>ETF Database, 22 hours ago</sub>  
  The S&P 500 wrapped up the week with a fractional loss of nearly 1%, ending lower for a second straight week.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 212.57 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 216.61 (-1.9%), 50d 217.18 (-2.1%), 200d 205.05 (+3.7%); 50d above 200d
Momentum: RSI(14) 37.6 | MACD -1.674 vs signal -1.103 (histogram -0.571)
Returns: 1d -0.1% | 5d -0.6% | 1m -4.1% | 3m +1.8%
52-week range: 182.18 - 222.77 (now 74.9% of the way up)
Volatility: ATR(14) 1.86 (0.9% of price) | annualised 20d 8.7%
Volume: 0.44x the 20-day average
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
Three-year record: +14.8% a year | beta to the market 0.83
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
Weighted price target: -1.1% above the current prices
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 475.10M | fund size: 100.99B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [‘The Sell Button Won’t Work’: Why Rate Hikes No Longer Save Debt Markets](https://www.benzinga.com/markets/bonds/26/09/61916030/the-sell-button-wont-work-why-rate-hikes-no-longer-save-debt-markets)  
  <sub>Benzinga, 3 hours ago</sub>  
  Forget Fed rate hikes: Macro analysts reveal why fiscal dominance and massive deficits make gold and real assets the ultimate hedges.
- [3 Best Dividend ETFs Paying 9%+ Yields](https://www.tipranks.com/news/3-best-dividend-etfs-paying-9-yields-2)  
  <sub>TipRanks, 14 minutes ago</sub>  
  Dividend ETFs continue to attract income-seeking investors, but some options stand out more than others. Based on TipRanks' High Dividend Yield ETFs tool,...
- [Ethereum ETF Inflow Signals Investors Doubling Down on Ether’s Rally](https://www.tipranks.com/news/cryptocurrencies/ethereum-etf-inflow-signals-investors-doubling-down-on-ethers-rally)  
  <sub>TipRanks, 4 hours ago</sub>  
  Ethereum ETF pulls in fresh cash as traders chase rally The VanEck Ethereum ETF, ETHV, saw a fresh influx of capital on September 18, 2026, with net flows...
- [Trump’s Munitions Claim: Implications for Aerospace & Defense ETFs](https://www.tipranks.com/news/catalyst/trumps-munitions-claim-implications-for-aerospace-defense-etfs)  
  <sub>TipRanks, 3 hours ago</sub>  
  President Trump has posted a new announcement on Truth Social, the social media platform. He wrote: “The cowards and traitors would love to say the United...
- [Bitcoin ETF Giant IBIT Draws Fresh Inflows as BTC Rallies Above $86K](https://www.tipranks.com/news/cryptocurrencies/bitcoin-etf-giant-ibit-draws-fresh-inflows-as-btc-rallies-above-86k)  
  <sub>TipRanks, 5 hours ago</sub>  
  Bitcoin ETF inflows are picking up again as IShares Bitcoin Trust Registered's IBIT logged fresh demand on September 21, 2026.
- [XRP ETF Outflows Hint at Profit-Taking Even as Token’s Rally Stays Intact](https://www.google.com/goto?url=CAESrwEB6zswFV9KRIvzEl-55H5Niu3giwFCR7bIep-NbfhDVI9K3kYFE98ERmEdJmWCc39KCWxsFIc3yvwpVuUB3JkE8IaDy9-ufqiFMCathLhl2DODhK7EYVDc4xO5ZL6gOkkBgfgZjKLiAOhJCGiAA_4p2-0m_cLtx5tVmvhwUmVhL9pCfUngkRXM3USOrzRprz3FKtOOom20E76-lEhguS1_2H_4jAfu_epvpCxF1fpM)  
  <sub>TipRanks, 16 hours ago</sub>  
  XRP ETF Sees a Jolt of Outflows as Traders Lock In Gains The Volatility Shares Trust XRP ETF, XRPI, recorded net outflows of $1429614 on September 15, 2026,...
- [3 Best ETFs Offering 10%+ Upside, Picked by AI Analyst](https://www.tipranks.com/news/3-best-etfs-offering-10-upside-picked-by-ai-analyst)  
  <sub>TipRanks, 19 hours ago</sub>  
  Exchange-traded funds (ETFs) remain a key way to capture growth opportunities in the market. Investors seeking exposure to industries such as tech,...
- [Evolve Sets September 2026 Payouts Across UltraYield ETFs and Income Funds](https://www.google.com/goto?url=CAEStgEB6zswFSJRR64OeIq15dka2S85zdSb9MJ2n8yFP3v8KN9-Yh4QGT58n1__fsPSIjn374xrsczu4dbWDET-bgPIoGQhkX6pIzdMfdP_qVTtk1bLz2TvX3dUgsdS3I_zSEYu1n9rRiQb-8bkqr2hbGb6IQsiBwa0WW6sIX1kI9B95rXEQ_gpoGEzR0gM89yivwm2f9HKRW4Ylfp8qcmtdd_jaYHW6jbpgcJOfIj1HJkDq6pwvo2ADQ)  
  <sub>TipRanks, 18 hours ago</sub>  
  The latest update is out from Evolve US Equity UltraYield ETF Trust Units -Hedged- ( ($TSE:BIGY) ). Evolve Funds Group Inc. has declared September 2026 cash...
- [Bitcoin ETF EZBC Draws Fresh Inflows as Price Rally Lures Mainstream Investors](https://www.google.com/goto?url=CAEStQEB6zswFb5HPd2wz8S6Au_ZAFyKsj-PHniObrHNl-D6JVUpBTvuXy8A3cjMOQNZwhgyRaLPC8Iz11Ff4UB7fLgM0B3sBlrB8AydepH-xVHBMfhbEC9N1HB6se_l8nMatBM14TEymuUE9YjW_ZoCN4zyWNEr5rCES7i7mfDccpLB4PRQZFPN3K3tOWUDHeWpMj9kd-d6zdYwQEbBH9lXD5QuG7eDiLISMxhf6lXQ5SWay6jBD5VB)  
  <sub>TipRanks, 19 hours ago</sub>  
  Bitcoin ETF pulls in fresh cash as price surge accelerates The Franklin Bitcoin ETF, EZBC, recorded net inflows of $4569300 on September 15, 2026,...
- [Bitcoin Keeps Climbing While Covered Call ETF YBTC Sees Investors Trim Exposure](https://www.tipranks.com/news/cryptocurrencies/bitcoin-keeps-climbing-while-covered-call-etf-ybtc-sees-investors-trim-exposure)  
  <sub>TipRanks, 21 hours ago</sub>  
  Bitcoin Options ETF Sees Modest Outflow as Rally Marches On The Roundhill Bitcoin Covered Call Strategy ETF, YBTC, recorded net outflows of $526953 on...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 105.61 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 106.46 (-0.8%), 50d 107.03 (-1.3%), 200d 109.58 (-3.6%); 50d below 200d
Momentum: RSI(14) 35.7 | MACD -0.487 vs signal -0.408 (histogram -0.078)
Returns: 1d -0.1% | 5d -0.2% | 1m -1.4% | 3m -3.0%
52-week range: 105.27 - 112.20 (now 4.9% of the way up)
Volatility: ATR(14) 0.35 (0.3% of price) | annualised 20d 4.2%
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
Three-year record: +3.4% a year | beta to the market 0.68
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 142.60M | fund size: 15.06B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [TLT ETF Slips As Resurgence In War Risk, Elevated Oil Prices Build Case For Rate Hikes](https://stocktwits.com/news-articles/markets/equity/us-treasury-yield-etfs-drop-as-resurgence-in-war-risk-elevated-oil-prices-build-case-for-rate-hikes/cZmoWmwR7VO)  
  <sub>Stocktwits, 15 hours ago</sub>  
  TLT ETF Slips As Resurgence In War Risk, Elevated Oil Prices Build Case For Rate Hikes · TLT ETF has seen outflows in five out of six months ending June 2026.
- [Fed's discount window modernization supports banks, broader market resilience: Governor Jefferson (TLT:NASDAQ)](https://seekingalpha.com/news/4645436-feds-discount-window-modernization-supports-banks-broader-market-resilience-governor-jefferson)  
  <sub>Seeking Alpha, 32 minutes ago</sub>  
  Fed's modernization efforts will ensure that the discount window supports individual banking institutions and broader market resilience, according to the...
- [A Record ETF Year Takes Shape as Inflows Near $1.5 Trillion](https://finance.yahoo.com/markets/stocks/articles/record-etf-takes-shape-inflows-210017196.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  US-listed ETFs took in $91.9 billion last week, pushing 2026 inflows to about $1.47 trillion, nearly matching last year's record with three months to spare.
- [S&P 500, Nasdaq, Dow Futures Ease After Another Record Close As AI Momentum Cushions Iran's Expanding Strikes: MRVL, AVGO, MSFT, PANW In Focus](https://stocktwits.com/news-articles/markets/equity/sp500-nasdaq-dow-futures-ease-after-another-record-close-ai-momentum-cushions-iran-strikes/cZ0SoqTReDV)  
  <sub>Stocktwits, 6 hours ago</sub>  
  U.S. President Donald Trump said in a post on Truth Social on Tuesday that the U.S. and Iran deal negotiations are ongoing, dismissing reports of strained...
- [Dow Drops To Record Worst Week In Six Months Amid Elevated Yields, Oil — NVDA, TSLA, SPCX, ONON In Focus](https://stocktwits.com/news-articles/markets/equity/dow-drops-to-record-worst-week-in-six-months-amid-elevated-yields-oil-nvda-tsla-spcx-onon-in-focus/cZtHOYsRBEK)  
  <sub>Stocktwits, 14 hours ago</sub>  
  An interest rate hike amid soaring energy costs and rising inflation concerns has weighed on the Dow.
- [Nasdaq, S&P 500 Futures Rise As Chip Rally Counters Iran Jitters Ahead Of Big Tech Earnings: Why IREN, ACHR, TSLA, BA Stocks Are Drawing Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-s-and-p-500-futures-rise-as-chip-rally-counters-iran-jitters-ahead-of-big-tech-earnings/cZZ1tCdR7HO)  
  <sub>Stocktwits, 17 hours ago</sub>  
  The VanEck Semiconductor ETF was up 0.41% at close, reversing three consecutive days of declines. However, tensions in the Middle East continued to rise...
- [BlackRock's $16.6 Billion Bond Fund Pays 6% Monthly. BND Pays 4% and Made 2% Last Year](https://247wallst.com/investing/etf/2026/09/21/blackrocks-16-6-billion-bond-fund-pays-6-monthly-bnd-pays-4-and-made-2-last-year/)  
  <sub>24/7 Wall St., 18 hours ago</sub>  
  Your core bond fund may be paying you far less than it should while quietly losing ground in today's rate environment. A massive active ETF from BlackRock...
- [Bond Panic? Great! This 13% Payer Is on Sale (for 91 Cents on the Dollar)](https://contrarianoutlook.com/bond-panic-great-this-13-payer-is-on-sale-for-91-cents-on-the-dollar/)  
  <sub>Contrarian Outlook, 6 hours ago</sub>  
  In one corner of the income market, a “rubber band” is stretched about as far as it can go. When it snaps back, I expect it to catapult the prices of a...
- [S&P 500, Nasdaq, Dow Futures Retreat After Rally Fueled By SpaceX, US-Iran Deal As Fed Meeting Looms: TSLA, PLAY, FISV In Focus](https://stocktwits.com/news-articles/markets/equity/sp500-nasdaq-dow-futures-retreat-after-rally-fueled-by-spacex-us-iran-deal-as-fed-meeting-looms/cZKW76IR7ER)  
  <sub>Stocktwits, 20 hours ago</sub>  
  The Dow index jumped to a new all-time intraday high on Monday, while the Nasdaq jumped to its best close since the end of March.
- [The Bond Market's Big Re-Steepening](https://finance.yahoo.com/markets/options/articles/bond-markets-big-steepening-040150357.html)  
  <sub>Yahoo Finance, 11 hours ago</sub>  
  The Federal Reserve's rate hike last week, its first in three years, capped a shift that had been building in the bond market for months.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 81.75 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 81.90 (-0.2%), 50d 82.51 (-0.9%), 200d 85.80 (-4.7%); 50d below 200d
Momentum: RSI(14) 48.0 | MACD -0.363 vs signal -0.429 (histogram 0.066)
Returns: 1d -0.1% | 5d +1.3% | 1m -0.4% | 3m -5.2%
52-week range: 80.71 - 92.06 (now 9.2% of the way up)
Volatility: ATR(14) 0.66 (0.8% of price) | annualised 20d 9.0%
Volume: 0.23x the 20-day average
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
Three-year record: -0.4% a year | beta to the market 2.39
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 109.70M | fund size: 8.97B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 28.50 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 28.17 (+1.2%), 50d 28.21 (+1.1%), 200d 27.73 (+2.8%); 50d above 200d
Momentum: RSI(14) 67.5 | MACD 0.081 vs signal 0.026 (histogram 0.054)
Returns: 1d +0.1% | 5d +1.0% | 1m +2.2% | 3m +0.2%
52-week range: 26.47 - 28.60 (now 95.5% of the way up)
Volatility: ATR(14) 0.10 (0.3% of price) | annualised 20d 4.6%
Volume: 0.07x the 20-day average
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
Contract: USD INDEX - ICE FUTURES U.S. (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 11.2% of open interest (43,744 contracts)
Change on the week: -21.9% of open interest
Crowding: 50% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 10.53M | fund size: 300.02M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Taiwan (EWT) · Sector or country — BULLISH, confidence 0.35

**Result:** ACCEPTED · 33 shares · submitted buy 33 EWT @ ~114.82, stop 110.28

**In the model's own words:**

> EWT is at 99% of its 52-week range after +8% in five days, with 50d above 200d and MACD positive but RSI 65 and volume only 0.4x average -- a strong trend rather than a fresh catalyst. No macro surprise this week: yields flat to slightly lower at the long end, VIX calm at 14.4, though a firmer dollar (+0.93) and a bond market pricing hikes are mild headwinds for a high-beta (1.30) Taiwan tech basket. Analyst roll-up is unanimous buy with +27% targets, but covers only 38% of the fund and is dominated by TSMC at 22%. Flows direction unknown, so no behavioural read. Trend-following long at modest size; no policy or data shock justifies more.

**Main reasons it gave:**
- Price at 99.2% of 52-week range, +32.7% above 200d SMA, 50d above 200d
- 5d +8.0% and 1m +10.5% but on 0.40x average volume
- RSI 65.3 with MACD above signal -- momentum intact, not yet extreme
- Analyst roll-up 100% buy, +27.2% weighted target, but only 38% coverage and 22% is TSMC
- VIX 14.4 and flat long-end yields -- no macro surprise; dollar +0.93 a mild EM headwind

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.55</summary>

```text
Last close 115.20 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 109.82 (+4.9%), 50d 104.57 (+10.2%), 200d 86.80 (+32.7%); 50d above 200d
Momentum: RSI(14) 65.3 | MACD 2.195 vs signal 1.856 (histogram 0.340)
Returns: 1d -0.4% | 5d +8.0% | 1m +10.5% | 3m +9.5%
52-week range: 60.03 - 115.64 (now 99.2% of the way up)
Volatility: ATR(14) 2.27 (2.0% of price) | annualised 20d 26.3%
Volume: 0.40x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Greater China Region
What it holds: P/E 27.26 | P/B 4.29 | P/S 2.54 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +43.5% a year | beta to the market 1.30
Cost and size: expense ratio 0.59% | net assets 11.76B
What it is made of: Stocks 99.6%, Cash 0.4%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 22.1%, MediaTek Inc 6.0%, Delta Electronics Inc 4.0%, Hon Hai Precision Industry Co Ltd 3.3%, ASE Technology Holding Co Ltd 2.6%
Sector mix: Technology 73.9%, Financial services 14.0%, Basic materials 3.8%, Industrials 2.8%
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
Rolled up from the 5 largest holdings, 38.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.35 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.2% above the current prices
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 105.25M | fund size: 12.12B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.35

**In the model's own words:**

> ITA has suffered a sustained pullback: down 10.1% over one month and 9.5% over three months, with price now 7.3% below the 200-day moving average and RSI at 29 signalling oversold conditions. The technicals show a deteriorating trend against all major moving averages, though the pullback has been orderly rather than panicked. Macro conditions remain stable—yields are flat to down on the week, the dollar has strengthened modestly, and the VIX at 14.4 reflects calm. The fund's valuation metrics (P/E 34.7, P/B 6.6) are elevated but not unusual for a quality industrials basket with strong three-year performance (+25.8% annualized). Analyst consensus on the 57.5% of holdings covered is decisively bullish: 100% buy ratings with a weighted +26.7% price target, and a recent upgrade of Lockheed Martin (a 4.7% position) to Buy provides a tailwind. The $1.2B Army missile contract for Lockheed Martin is sector-supportive but immaterial to fund returns—a single holding's win is noise in a 99.8% stock fund. Fund flows data is incomplete. The case for a bounce rests on oversold technicals, unanimous analyst sentiment on the five largest holdings, and an intact macro backdrop, but the fund's recent underperformance and elevated multiples argue for caution. This is a setup where conviction is warranted neither for a strong call nor for a full reversal; a modest bullish lean reflects the technical extreme and analyst consensus without ignoring the valuation and recent trend.

**Main reasons it gave:**
- RSI 29 signals oversold after -10.1% month pullback
- analyst consensus 100% buy with +26.7% weighted price target on 57.5% of fund
- price 7.3% below 200-day MA, all moving averages bearish
- elevated P/E 34.7 and P/B 6.6 valuations persist through drawdown
- LMT upgrade to Buy and $1.2B contract support sector but minor to fund composition

<details><summary><b>News</b> — score +0.15</summary>

- [Should You Invest in the iShares U.S. Aerospace & Defense ETF (ITA)?](https://finance.yahoo.com/markets/stocks/articles/invest-ishares-u-aerospace-defense-102002161.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Sector ETF report for ITA.
- [Lockheed Martin Lands $1.2 Billion Army Missile Deal](https://www.benzinga.com/news/contracts/26/09/61913994/lockheed-martin-lands-1-2-billion-army-missile-deal)  
  <sub>Benzinga, 5 hours ago</sub>  
  Lockheed Martin wins $1.2B U.S. Army contract for PrSM Increment 2 missiles targeting moving maritime targets.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 213.44 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 222.51 (-4.1%), 50d 234.40 (-8.9%), 200d 230.28 (-7.3%); 50d above 200d
Momentum: RSI(14) 29.0 | MACD -6.658 vs signal -6.296 (histogram -0.362)
Returns: 1d -1.2% | 5d -0.3% | 1m -10.1% | 3m -9.5%
52-week range: 198.23 - 253.22 (now 27.7% of the way up)
Volatility: ATR(14) 4.11 (1.9% of price) | annualised 20d 14.8%
Volume: 0.40x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

```text
Fund type: Industrials
What it holds: P/E 34.66 | P/B 6.62 | P/S 3.21 | 3y earnings growth n/a
Yield: 0.5%
Three-year record: +25.8% a year | beta to the market 0.99
Cost and size: expense ratio 0.37% | net assets 13.63B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: GE Aerospace 21.6%, RTX Corp 17.2%, Boeing Co 9.1%, General Dynamics Corp 4.8%, Lockheed Martin Corp 4.7%
Sector mix: Industrials 100.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 57.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.75 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.7% above the current prices
Holdings read: GE, RTX, BA, GD, LMT
Recent rating changes among them:
  - GE: 2026-07-23 Bernstein: main, Outperform -> Outperform
  - RTX: 2026-08-03 Bernstein: main, Market Perform -> Market Perform
  - BA: 2026-09-21 Jefferies: main, Buy -> Buy
  - GD: 2026-09-08 UBS: main, Neutral -> Neutral
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 63.73M | fund size: 13.60B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — BEARISH, confidence 0.32

**Result:** ACCEPTED · 53 shares · submitted sell 53 KRE @ ~71.35, stop 73.81

**In the model's own words:**

> Regional banks are in a clear short-term downtrend (below 20d and 50d SMAs, RSI 31, MACD below signal) against a macro backdrop where the 2-year at 4.76% versus a 4.00% target prices further tightening -- an unfriendly rate path for deposit-funded lenders, with the 10-year near 5%. Nothing here is a fresh surprise: the week's long-end moves were small, VIX fell to 14, and the decline came on light volume (0.47x), so this is drift rather than a break. Valuation is undemanding (P/E 12.6, P/B 1.27) and the thin analyst roll-up (7.1% of the fund) skews positive with a +21% weighted target, which caps downside conviction. The headline items drawing 2023 analogies are speculative framing rather than new information and I do not weight them as evidence.

**Main reasons it gave:**
- Price below 20d (-3.0%) and 50d (-5.1%) SMAs with RSI 31.4 and negative MACD histogram
- 2-year 4.76% vs 4.00% Fed target implies further hikes priced -- headwind for regional bank funding costs
- 10-year 4.96%, long end actually fell slightly on the week: no fresh rate shock this cycle
- Decline occurring on 0.47x average volume with VIX down 2.8 to 14.4 -- no stress confirmation
- Holdings cheap at P/E 12.6 / P/B 1.27 with thin (7.1% weight) analyst roll-up 74% buy, +20.8% target

<details><summary><b>News</b> — score -0.15</summary>

- [KRE Lost 36% in Five Weeks in 2023. Another Rate Hike Shock May be Coming](https://www.google.com/goto?url=CAESrwEB6zswFflG_40mEBDbRbWPgQ0Htv5HOsPBeL5sFqF5glxwJK9DS_F6QFntSf6LiH4NIdYttN27_kXcR6Q6lPgOpJoIkFjtBePJn1ncRCp8cqZg5Zi7N_SjoQ36oFLuz3dhVhD3Pw7Jv0E2qjGXEO6LmPzzI3l5DIpxkrRA0n4Whl-Dn_iM7ZMW8ySl6AMBPChIp8BhzTWnHFUtYLnFZodhGczYRqDTBJ6tSekFbKFt)  
  <sub>24/7 Wall St., 20 hours ago</sub>  
  The Fed just raised rates again, and regional banks are carrying the same vulnerabilities that wiped out a third of KRE's value in five weeks three years...
- [Regional bank ETF KRE fell 36% in five weeks in 2023; rate hikes may trigger similar risks again.](https://www.google.com/goto?url=CAESqAEB6zswFQIk4ynsqcscFiwVkawuNT6lolfMHeUWBR0hVMgIyx3mjyQxfBnNW-YGeqzpmd-eeQhzXDKlzZEkP-SyzCNwCestd7WS4sq_RV825rHB6JmMNOWgUOZST8u_a8uTVe3snMOqq_uWLcR54LfX0_4RBusoCl-0j0aLt4T7pGOHDqPlvKAE9F5tV6f6DCcVR5ljyt20-ynBAQL-tCDp9s9j4oT0LxA)  
  <sub>Pluang, 20 hours ago</sub>  
  The SPDR S&P Regional Banking ETF (KRE) dropped 36% in five weeks during 2023 due to failures of key regional banks. With the Fed raising rates again in...
- [SPDR S&P Regional Banking ETF declares quarterly distribution of $0.4125](https://www.google.com/goto?url=CAESvwEB6zswFSXsglEKY5Z-Xn2J8QHNXa4qduD3Nb3WqnrcCYr8nF562gX8Caqp7RCANXIGj35IUyKm7dDfcL-UbRYH06BS6jqmTNHKhENNKsHUWSvcz_zb_HPr700h2fNAYJ8JtNPTfUmSWl_i0lbjDRMIWU5xXvDXrwAUPw5o9IBAbdbSGH_xegFtsrQh0a8Fp8xfb7m-gmzWBVveUWSVuGbi4Wbbq959ksXjauRG19yeEJGtLRKqFnSrUT84lwkJBQ)  
  <sub>TradingView, 21 hours ago</sub>  
  Content provided by Seeking Alpha is intended for information purposes only, and that Seeking Alpha does not offer any personalist investment advice and is...
- [Fed's discount window modernization supports banks, broader market resilience: Governor Jefferson (TLT:NASDAQ)](https://seekingalpha.com/news/4645436-feds-discount-window-modernization-supports-banks-broader-market-resilience-governor-jefferson)  
  <sub>Seeking Alpha, 35 minutes ago</sub>  
  Fed's modernization efforts will ensure that the discount window supports individual banking institutions and broader market resilience, according to the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.15</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 71.43 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 73.67 (-3.0%), 50d 75.24 (-5.1%), 200d 70.42 (+1.4%); 50d above 200d
Momentum: RSI(14) 31.4 | MACD -0.822 vs signal -0.607 (histogram -0.215)
Returns: 1d -0.8% | 5d -3.5% | 1m -4.6% | 3m -2.3%
52-week range: 58.14 - 77.93 (now 67.2% of the way up)
Volatility: ATR(14) 1.22 (1.7% of price) | annualised 20d 14.7%
Volume: 0.47x the 20-day average
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
Three-year record: +22.6% a year | beta to the market 1.04
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
Ratings by weight: buy 74.3% | hold 25.7% | sell 0.0% (mean 1.88 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.8% above the current prices
Holdings read: CFR, SSB, BPOP, PNFP, UMBF
Recent rating changes among them:
  - CFR: 2026-09-08 Morgan Stanley: up, Underweight -> Overweight
  - SSB: 2026-07-28 Citigroup: main, Buy -> Buy
  - BPOP: 2026-09-22 Citigroup: main, Buy -> Buy
  - PNFP: 2026-09-08 Morgan Stanley: init, ? -> Overweight
  - UMBF: 2026-09-14 UBS: init, ? -> Neutral
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 55.14M | fund size: 3.94B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.28

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Strong uptrend (above all major SMAs, near 52-week highs, +6.3% in five days, MACD positive) and calm vol with VIX down 2.8 argue for risk-on, but there is no macro catalyst: yields barely moved, the curve is normally sloped, and the 2-year still prices tightening rather than cuts with inflation at 3.4%. Volume on the advance is only 0.51x average, and RSI 65.7 with the fund 95.9% of the way up its range leaves little cushion at a 33x P/E and 1.50 beta. Holdings analyst view is supportive but covers only 45.7% of the fund and reflects consensus already in price. The single-holding AI headlines (AMD, Micron) are noise for a basket call. Slight positive tilt, not enough for a directional bet.

**Main reasons it gave:**
- Price 4.6% above 20d and 19.8% above 200d SMA, 95.9% of 52-week range
- Advance on 0.51x average volume; RSI 65.7 near overbought
- VIX 14.42, down 2.8 on week -- calm backdrop, no rate surprise (10y -0.04)
- 2-year 4.76% vs 4.00% target prices hikes, inflation still 3.4%
- Holdings roll-up 100% buy, +24.4% target, but only 45.7% coverage; P/E 33 and beta 1.50

<details><summary><b>News</b> — score +0.15</summary>

- [AI Optimism Returns, Pushing Inflation Risks Into The Background](https://seekingalpha.com/article/4948604-ai-optimism-returns-pushing-inflation-risks-background)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Monday's AI-fueled optimism spilled over to stocks generally. The SPDR S&P 500 ETF, for example, rallied to just below its record close from early August.
- [State Street Technology Select Sector SPDR ETF declares quarterly distribution of $0.2207](https://www.tradingview.com/news/seekingalpha:1d686bdb8094b:0-state-street-technology-select-sector-spdr-etf-declares-quarterly-distribution-of-0-2207/)  
  <sub>TradingView, 21 hours ago</sub>  
  Content provided by Seeking Alpha is intended for information purposes only, and that Seeking Alpha does not offer any personalist investment advice and is...
- [The Strange Pair That Led the Market Higher](https://moneyandmarkets.com/the-strange-pair-that-led-the-market-higher/amp/)  
  <sub>Money & Markets, 20 hours ago</sub>  
  Only two sectors finished higher last week, and the unusual pairing tells us plenty about where investors are finding safety...
- [Micron, Nvidia lead $1T market-cap stocks by Quant ratings as AMD joins the club (XLK:NYSEARCA)](https://seekingalpha.com/news/4645012-micron-nvidia-lead-1t-market-cap-stocks-by-quant-ratings-as-amd-joins-the-club)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  AMD joins the $1T club as AI chip stocks surge. See Seeking Alpha Quant ratings for trillion-dollar giants and top Strong Buys—check the list now.
- [Custom Chips May Outpace GPUs By 2027 (NYSE:SHOC)](https://seekingalpha.com/article/4948575-custom-chips-may-outpace-gpus-by-2027)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Strive US Semiconductor ETF offers diversified exposure to both GPU and custom chip growth. Read why SHOC ETF may outperform peers.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.45</summary>

```text
Last close 195.28 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 186.71 (+4.6%), 50d 183.58 (+6.4%), 200d 162.94 (+19.8%); 50d above 200d
Momentum: RSI(14) 65.7 | MACD 1.994 vs signal 1.126 (histogram 0.868)
Returns: 1d +0.2% | 5d +6.3% | 1m +6.5% | 3m +6.0%
52-week range: 127.50 - 198.21 (now 95.9% of the way up)
Volatility: ATR(14) 3.40 (1.7% of price) | annualised 20d 21.7%
Volume: 0.51x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Technology
What it holds: P/E 33.01 | P/B 11.41 | P/S 8.77 | 3y earnings growth n/a
Yield: 0.4%
Three-year record: +31.6% a year | beta to the market 1.50
Cost and size: expense ratio 0.08% | net assets 121.44B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: NVIDIA Corp 14.4%, Apple Inc 12.5%, Microsoft Corp 10.1%, Broadcom Inc 4.7%, Micron Technology Inc 4.0%
Sector mix: Technology 100.0%
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
Rolled up from the 5 largest holdings, 45.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.56 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.4% above the current prices
Holdings read: NVDA, AAPL, MSFT, AVGO, MU
Recent rating changes among them:
  - NVDA: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - AAPL: 2026-09-18 Evercore ISI Group: main, Outperform -> Outperform
  - MSFT: 2026-09-21 Cantor Fitzgerald: main, Overweight -> Overweight
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-09-18 RBC Capital: reit, Outperform -> Outperform
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 640.16M | fund size: 125.01B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWA is an Australian equity fund trading near its 52-week highs with mixed technicals and no significant macro catalyst. The fund holds 99.5% stocks dominated by financials (41.1%) and basic materials (26.7%), concentrated in BHP, CBA, NAB, Westpac and ANZ. Technicals are soft: price is 1.9% below its 20-day moving average, RSI sits at 44.5 (not yet oversold but below neutral), MACD is negative with histogram deteriorating, and momentum is sluggish despite a modest 3.6% three-month return. Volume is well below average at 0.18x the 20-day baseline, suggesting weak conviction in the move. The macro backdrop is benign but not supportive: the US dollar has strengthened 0.93% this week to 100.58, which is headwind for an Australian equity fund; Treasury yields are stable with the curve normal but the rate path suggests continued Fed tightness through 2026. Fund basics show reasonable valuation at a 21x P/E and 2.8% yield, but analyst coverage of the top 46% of holdings is mixed—59.6% rated hold, 40.4% rated sell, with a weighted price target implying 6.8% downside to current prices. The near-term setup lacks a clear bullish catalyst: macro is not supportive, technicals are deteriorating, analyst consensus is cautious, and flows are untracked. The modest recent intra-fund rally and low volatility environment argue against a bearish call, but the evidence does not justify conviction in either direction.

**Main reasons it gave:**
- Analyst consensus weighted to hold and sell over top 46% of fund, with -6.8% price target to current prices
- USD strength this week headwind for AUD-denominated equity returns
- RSI 44.5 and negative MACD histogram signal weakening momentum despite 52-week highs
- Volume at 0.18x 20-day average—thin conviction behind recent move
- Price 1.9% below 20d SMA, below 50d SMA despite normal yield curve backdrop

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 29.02 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 29.57 (-1.9%), 50d 29.49 (-1.6%), 200d 28.56 (+1.6%); 50d above 200d
Momentum: RSI(14) 44.5 | MACD -0.216 vs signal -0.118 (histogram -0.099)
Returns: 1d -0.1% | 5d +0.5% | 1m -3.7% | 3m +3.6%
52-week range: 24.95 - 30.43 (now 74.3% of the way up)
Volatility: ATR(14) 0.37 (1.3% of price) | annualised 20d 17.3%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.05</summary>

```text
Fund type: Focused Region
What it holds: P/E 21.06 | P/B 2.81 | P/S 3.39 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +12.8% a year | beta to the market 0.96
Cost and size: expense ratio 0.50% | net assets 1.33B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: BHP Group Ltd 16.3%, Commonwealth Bank of Australia 13.0%, National Australia Bank Ltd 5.9%, Westpac Banking Corp 5.7%, ANZ Group Holdings Ltd 5.5%
Sector mix: Financial services 41.1%, Basic materials 26.7%, Consumer cyclical 6.5%, Healthcare 5.2%
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

<details><summary><b>What analysts and big funds say</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.35</summary>

```text
Rolled up from the 5 largest holdings, 46.4% of the fund by weight
Ratings by weight: buy 0.0% | hold 59.6% | sell 40.4% (mean 3.48 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -6.8% above the current prices
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 46.17M | fund size: 1.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWC is a focused Canadian equity fund with moderate fundamentals and mixed technicals. The fund trades at reasonable valuations (P/E 19.49, P/B 2.83) with a 1.2% yield, benefiting from a strong three-year track record (+21.9% annualized). Technicals show the fund near 52-week highs (84.6% of range) but momentum is neutral: RSI at 48 and MACD histogram negative, with price slightly below the 20-day moving average. The fund is now 5.5% above its 200-day MA with the 50-day MA above it, suggesting a long-term uptrend, but recent weakness (down 2.8% over one month, up only 0.6% over five days) indicates loss of momentum. Analyst coverage of the largest holdings (28.3% of fund) shows 74% buy-rated with a modest +4.5% price target above current levels, a muted endorsement. The macro backdrop is stable: the Fed is on hold with rates priced for modest hikes ahead, the dollar strengthened modestly (+0.93 on the week), and volatility remains calm (VIX 14.42). However, no fresh catalyst has emerged to justify a directional tilt. The fund holds significant financials exposure (39.2%) and energy (17.9%), which benefit from stable rates but lack a near-term driver. Volume is below average (0.50x 20-day), suggesting thin interest. Without a material data surprise, policy shift, or decisive technical break, the balanced risk-reward supports a neutral stance.

**Main reasons it gave:**
- RSI 48 and negative MACD histogram signal neutral momentum despite uptrend structure
- Analyst roll-up shows 74% buy-rated with only +4.5% upside on 28.3% fund coverage
- Price near 52-week highs with 2.8% monthly decline suggests momentum loss
- Macro stable with no fresh catalyst; CAD financial and energy sectors lack near-term drivers
- Below-average volume reflects muted demand

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 60.65 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 61.12 (-0.8%), 50d 60.72 (-0.1%), 200d 57.50 (+5.5%); 50d above 200d
Momentum: RSI(14) 48.0 | MACD -0.194 vs signal -0.058 (histogram -0.135)
Returns: 1d +0.4% | 5d +0.6% | 1m -2.8% | 3m +5.2%
52-week range: 49.72 - 62.64 (now 84.6% of the way up)
Volatility: ATR(14) 0.65 (1.1% of price) | annualised 20d 13.6%
Volume: 0.50x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Focused Region
What it holds: P/E 19.49 | P/B 2.83 | P/S 2.79 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +21.9% a year | beta to the market 0.79
Cost and size: expense ratio 0.50% | net assets 6.85B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Royal Bank of Canada 9.0%, The Toronto-Dominion Bank 6.3%, Shopify Inc Registered Shs -A- Subord Vtg 5.7%, Bank of Montreal 3.7%, Bank of Nova Scotia 3.6%
Sector mix: Financial services 39.2%, Energy 17.9%, Basic materials 16.1%, Industrials 8.8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 28.3% of the fund by weight
Ratings by weight: buy 74.3% | hold 25.7% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.5% above the current prices
Holdings read: RY, TD, SHOP, BMO.TO, BNS.TO
Recent rating changes among them:
  - RY: 2025-08-29 Argus Research: main, Buy -> Buy
  - TD: 2026-06-01 RBC Capital: main, Outperform -> Outperform
  - SHOP: 2026-09-11 Bernstein: init, ? -> Outperform
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 113.71M | fund size: 6.90B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWD is a Swedish-focused equity fund trading near recent highs with mixed technical signals and no macro catalyst. The technical picture shows price above the 200-day MA (supportive) but below both 20- and 50-day SMAs, RSI at mid-range 48.7, and MACD negative with narrowing histogram—a picture of consolidation rather than momentum. Monthly returns of -3.0% against 3-month gains of +6.7% suggest the recent rally has lost steam. Macro conditions are benign: USD strength, normal yield curve, falling volatility, and a rate path that prices about 4 quarter-point hikes over two years. FUND BASICS show modest leverage (beta 1.19) with a reasonable P/E of 14.99 and a 3.4% yield. ANALYST VIEW is constructively biased at 82.1% buy-weighted and a +9.3% price target, but this roll-up covers only 29.5% of the fund and offers limited insight into the full portfolio. The lack of recent news, unknown fund flow direction, and absence of insider positioning data leave conviction low. The fund is neither broken nor compelling: technicals are neutral, fundamentals are fair, sentiment is constructive but not urgent, and no macro surprise has occurred. This warrants a modest cautious posture while acknowledging upside optionality from analyst targets.

**Main reasons it gave:**
- Price below 20d and 50d SMAs despite 52-week 71.3% positioning and +6.7% 3-month return
- RSI 48.7 and negative MACD histogram signal consolidation not momentum
- Analyst roll-up 82.1% buy-weighted with +9.3% target but covering only 29.5% of fund
- P/E 14.99 and 3.4% yield offer fair valuation in context of normal yield curve and benign macro
- No macro surprise, policy shift, or technical breakout to justify elevated conviction

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 52.04 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 52.50 (-0.9%), 50d 52.16 (-0.2%), 200d 51.32 (+1.4%); 50d above 200d
Momentum: RSI(14) 48.7 | MACD -0.295 vs signal -0.172 (histogram -0.123)
Returns: 1d +0.5% | 5d +1.5% | 1m -3.0% | 3m +6.7%
52-week range: 45.38 - 54.72 (now 71.3% of the way up)
Volatility: ATR(14) 0.67 (1.3% of price) | annualised 20d 15.8%
Volume: 0.97x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.99 | P/B 2.88 | P/S 2.90 | 3y earnings growth n/a
Yield: 3.4%
Three-year record: +19.6% a year | beta to the market 1.19
Cost and size: expense ratio 0.51% | net assets 755.74M
What it is made of: Stocks 98.9%, Cash 1.1%
Largest holdings: Spotify Technology SA 10.2%, Investor AB Class B 9.5%, Volvo AB Class B 7.1%, Atlas Copco AB Class A 6.9%, Sandvik AB 5.3%
Sector mix: Industrials 46.0%, Financial services 24.9%, Communication services 13.9%, Technology 6.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 4 largest holdings, 29.5% of the fund by weight
Ratings by weight: buy 82.1% | hold 17.9% | sell 0.0% (mean 1.97 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.3% above the current prices
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 14.83M | fund size: 771.50M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWI is an Italian equities fund with strong fundamental valuations (P/E 15.25, P/B 1.85) and a 3.0% yield, supported by analyst consensus showing 100% buy-rated holdings with a +10.9% weighted price target across the 51% of the fund covered. The macro backdrop is stable: Treasury yields moved marginally this week with the curve remaining normal (+0.95 points), the dollar strengthened modestly (+0.93), and volatility declined to a calm 14.42. However, technicals present conflicting signals. The fund trades 1.4-1.8% below its 20d and 50d SMAs and is underperforming its own three-year trend, with RSI at 43.7 (neither oversold nor overbought) and MACD below its signal line suggesting weakening momentum. Volume is only 0.54x the 20-day average, indicating thin conviction behind the recent -3.6% monthly decline. The fund sits at 79.2% of its 52-week range, neither at an extreme. No material macro surprise has occurred this week, and no catalyst or data release has shifted expectations materially. While analyst coverage is constructive and valuations are reasonable, the lack of recent price action, light flows data, and absence of a specific catalyst argue against a directional lean. The technical weakness is soft rather than severe, and there is no evidence of either forced selling or institutional accumulation.

**Main reasons it gave:**
- Italian equities trading 1.4-1.8% below near-term moving averages with weak momentum
- Analysts 100% buy-rated on largest holdings with +10.9% average price target
- Stable macro backdrop with normal yield curve and modest dollar strength
- Below-average volume suggesting weak conviction behind recent declines
- No material policy, rate or data surprise this cycle

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 60.64 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 61.51 (-1.4%), 50d 61.74 (-1.8%), 200d 57.77 (+5.0%); 50d above 200d
Momentum: RSI(14) 43.7 | MACD -0.369 vs signal -0.259 (histogram -0.109)
Returns: 1d -1.0% | 5d -0.2% | 1m -3.6% | 3m +2.1%
52-week range: 50.31 - 63.35 (now 79.2% of the way up)
Volatility: ATR(14) 0.73 (1.2% of price) | annualised 20d 16.6%
Volume: 0.54x the 20-day average
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
Three-year record: +28.5% a year | beta to the market 0.88
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

<details><summary><b>What analysts and big funds say</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.55</summary>

```text
Rolled up from the 5 largest holdings, 50.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.03 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.9% above the current prices
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 18.83M | fund size: 1.14B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.25

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> EWJ sits at 99.5% of its 52-week range with trend intact above 20/50/200d SMAs, but momentum is flattening (MACD histogram 0.007, RSI 58.7) and volume is only 0.46x average, so the breakout is not decisive. Macro is benign rather than catalytic: VIX 14.4 and lower long yields help, but a stronger dollar (+0.93) is a headwind for unhedged Japan exposure and the 2-year prices a hiking path. Holdings are reasonably valued (P/E 19, 3.7% yield) and analyst coverage on the top 17% is uniformly buy with +19.7% targets, though that slice is thin. Spec positioning is mid-range. No policy or data surprise this cycle, so no side warranted beyond a mild upward tilt.

**Main reasons it gave:**
- Price at 99.5% of 52-week range but volume only 0.46x 20-day average
- MACD histogram 0.007 -- momentum essentially flat despite uptrend
- Dollar index +0.93 on the week, a headwind for unhedged Japan exposure
- VIX 14.4, down 2.8, calm backdrop with no policy or data surprise
- CFTC Nikkei spec net long at 38th percentile -- no crowding extreme

<details><summary><b>News</b> — score +0.10</summary>

- [Asian stocks mostly rise on tech rally, lower yields, and US-China trade hopes](https://seekingalpha.com/news/4645224-asian-stocks-mostly-rise-on-tech-rally-lower-yields-and-us-china-trade-hopes)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  Asian stock markets delivered a mixed performance on Tuesday, picking up momentum from overnight gains on Wall Street. A fresh rally in technology shares...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.30</summary>

```text
Last close 98.45 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 96.94 (+1.6%), 50d 95.14 (+3.5%), 200d 89.85 (+9.6%); 50d above 200d
Momentum: RSI(14) 58.7 | MACD 0.713 vs signal 0.707 (histogram 0.007)
Returns: 1d +0.5% | 5d +1.6% | 1m +3.4% | 3m +6.1%
52-week range: 78.36 - 98.56 (now 99.5% of the way up)
Volatility: ATR(14) 1.32 (1.3% of price) | annualised 20d 14.5%
Volume: 0.46x the 20-day average
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
Three-year record: +18.8% a year | beta to the market 0.86
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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.7% above the current prices
Holdings read: 8306.T, 7203.T, 8316.T, 8035.T, 6857.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.05</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 4.3% of open interest (22,625 contracts)
Change on the week: +1.5% of open interest
Crowding: 38% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.05</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 234.29M | fund size: 23.07B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWL is a focused Switzerland equity fund trading with mixed technical signals and absent macro catalysts. Technicals show mild weakness: price is below all major moving averages (20d, 50d, 200d), RSI is sub-50 at 43.7 indicating weak momentum, and MACD remains negative though histogram is narrowing. The 1-month return of -5.1% and below-average volume suggest lack of conviction. Macro backdrop is stable with a normalized yield curve, calm volatility (VIX 14.4), and no recent data surprises; the dollar's +0.93 week move is modest. Fund fundamentals show elevated valuation multiples (P/E 24.65, P/B 4.25) typical of Swiss large-cap quality names, with 1.7% yield and a 3-year record of +12.1% annually. Analyst coverage of the largest 48.5% of holdings shows 74.5% buy-rated at a weighted +9.8% upside target, providing mild support. Fund flows data is unavailable, limiting insight into recent investor conviction. The weighted analyst view and recovery from oversold RSI argue against a bearish call, but the technical breakdown, absence of any positive news catalyst, and lack of macro tailwind prevent a bullish stance. The position between moving averages, near the middle of its 52-week range, and with stable macro conditions supports a holding pattern.

**Main reasons it gave:**
- Price below 20d, 50d, and 200d moving averages with momentum RSI at 43.7
- Analyst consensus bullish on 48.5% of holdings, weighted target +9.8% above current prices
- No macro catalyst; stable yields, low volatility, and normalized curve
- 1-month return of -5.1% with below-average volume suggests weak demand
- P/E of 24.65 and P/B of 4.25 price premium typical of quality holdings, not compelling at current levels

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 61.08 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 61.84 (-1.2%), 50d 62.73 (-2.6%), 200d 61.56 (-0.8%); 50d above 200d
Momentum: RSI(14) 43.7 | MACD -0.777 vs signal -0.706 (histogram -0.071)
Returns: 1d +0.4% | 5d +1.4% | 1m -5.1% | 3m -0.7%
52-week range: 53.86 - 65.08 (now 64.3% of the way up)
Volatility: ATR(14) 0.68 (1.1% of price) | annualised 20d 13.8%
Volume: 0.65x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Focused Region
What it holds: P/E 24.65 | P/B 4.25 | P/S 2.78 | 3y earnings growth n/a
Yield: 1.7%
Three-year record: +12.1% a year | beta to the market 0.91
Cost and size: expense ratio 0.50% | net assets 2.42B
What it is made of: Stocks 99.0%, Cash 1.0%
Largest holdings: Roche Holding AG Ordinary Shares new 13.6%, Novartis AG Registered Shares 12.4%, Nestle SA 11.1%, UBS Group AG Registered Shares 6.8%, Compagnie Financiere Richemont SA Class A 4.6%
Sector mix: Healthcare 37.5%, Financial services 20.6%, Consumer defensive 13.3%, Industrials 11.8%
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
Rolled up from the 5 largest holdings, 48.5% of the fund by weight
Ratings by weight: buy 74.5% | hold 25.5% | sell 0.0% (mean 2.40 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.8% above the current prices
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 28.62M | fund size: 1.75B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWN (Euronext N.V.) is a Netherlands-focused equity fund trading near recent highs with modestly positive technicals but insufficient conviction drivers for a directional call. Technicals show the fund above its 20, 50, and 200-day moving averages with a 6.8% gain over 200 days, but momentum is neutral (RSI 52.1, MACD histogram near zero) and recent performance is mixed (-1.7% over one month despite +3% over five days). The fund is near the top of its 52-week range at 79.6%, which typically warrants caution. Macro backdrop is stable with a normal upward-sloping yield curve, contained inflation expectations, and falling volatility (VIX down 2.8 this week), but Treasury yields are essentially flat across the week with no fresh surprise. The analyst consensus on the five largest holdings (44% of the fund) is unanimously bullish with a weighted price target 29.7% above current prices, which is encouraging but applies to less than half the fund and carries no independent timing signal. A new Sell rating on NBIS (Nebius, 4.3% of the fund) from Rothschild yesterday is a minor headwind. Fund basics show reasonable valuation (P/E 18.97) and a strong three-year track record (+23.3% annualized), but these move slowly and do not justify a fresh view. Volume is well below average (0.17x) and flows data are insufficient. The call is NEUTRAL because there is no material catalyst: no macro surprise, no technical break, and analyst sentiment—while positive—is rolled up from less than half the fund and offers no directional edge on timing.

**Main reasons it gave:**
- Near 52-week high (79.6%) with neutral momentum (RSI 52.1, MACD flat)
- Analyst consensus +29.7% price target but covers only 44% of fund weight
- Macro stable with flat weekly yields and declining volatility, no surprise
- Volume 0.17x average and flows data insufficient

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.15</summary>

```text
Last close 68.29 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 67.94 (+0.5%), 50d 68.18 (+0.2%), 200d 63.96 (+6.8%); 50d above 200d
Momentum: RSI(14) 52.1 | MACD -0.368 vs signal -0.356 (histogram -0.013)
Returns: 1d +0.6% | 5d +3.0% | 1m -1.7% | 3m +0.6%
52-week range: 55.33 - 71.61 (now 79.6% of the way up)
Volatility: ATR(14) 0.90 (1.3% of price) | annualised 20d 14.6%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.97 | P/B 2.54 | P/S 1.84 | 3y earnings growth n/a
Yield: 4.1%
Three-year record: +23.3% a year | beta to the market 1.14
Cost and size: expense ratio 0.50% | net assets 626.66M
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ASML Holding NV 21.8%, ING Groep NV 9.0%, Prosus NV Ordinary Shares - Class N 5.1%, Nebius Group NV Shs Class-A- 4.3%, ASM International NV 4.0%
Sector mix: Technology 31.5%, Financial services 21.4%, Industrials 10.8%, Consumer defensive 10.7%
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
Rolled up from the 5 largest holdings, 44.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +29.7% above the current prices
Holdings read: ASML.AS, INGA.AS, PRX.AS, NBIS, ASM.AS
Recent rating changes among them:
  - NBIS: 2026-09-21 Rothschild & Co: init, ? -> Sell
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 5.55M | fund size: 379.01M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWP is a Spain-focused equity fund trading near 52-week highs with moderate positive fundamentals but lacking near-term catalysts. The fund's valuation (P/E 16.28, P/B 2.22) is reasonable for a developed market and its 3-year record is strong at +33.6% annually, but current technicals show early signs of exhaustion: RSI at 47.9 is neutral-to-bearish, MACD histogram is negative, and the fund has underperformed over the past month (-2.4%) despite a strong 3-month run (+4.0%). It is trading 87.7% of the way to its 52-week high, leaving limited upside before resistance. The analyst view of the top 5 holdings (54.5% of the fund) is modestly bullish with a +1.5% weighted price target and buy ratings on 52% of that weight, but this is thin conviction. Macro backdrop is benign: the yield curve is normal, the dollar has strengthened slightly (+0.93 on the week), volatility is calm at 14.42, and inflation remains elevated at 3.4% with the Fed on hold. The bond market prices only modest rate cuts ahead. No macro surprise has occurred, and there is no sector-specific catalyst in the news. Volume is below average at 0.54x the 20-day mean, suggesting weak conviction behind the current price level. The fund's 2.7% yield and financial-services-heavy composition (45.4%) are reasonable but not compelling in a world where rates remain sticky. With technicals rolling over, valuation extended, and no fresh catalyst, the case for directional movement is weak.

**Main reasons it gave:**
- RSI 47.9 and negative MACD histogram suggest early bearish divergence despite near 52-week highs
- Fund at 87.7% of 52-week range with -2.4% one-month return despite +4% three-month gain
- Analyst target of +1.5% weighted upside on top 5 holdings (54.5% of fund) provides only modest support
- Volume 0.54x 20-day average indicates weak conviction behind current price level
- No macro catalyst present: sticky inflation at 3.4%, normal yield curve, calm volatility

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 61.38 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 61.87 (-0.8%), 50d 61.50 (-0.2%), 200d 57.32 (+7.1%); 50d above 200d
Momentum: RSI(14) 47.9 | MACD -0.173 vs signal -0.040 (histogram -0.133)
Returns: 1d -0.1% | 5d +0.5% | 1m -2.4% | 3m +4.0%
52-week range: 48.25 - 63.23 (now 87.7% of the way up)
Volatility: ATR(14) 0.77 (1.3% of price) | annualised 20d 15.1%
Volume: 0.54x the 20-day average
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
Three-year record: +33.6% a year | beta to the market 0.87
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 54.5% of the fund by weight
Ratings by weight: buy 52.0% | hold 48.0% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +1.5% above the current prices
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 37.35M | fund size: 2.29B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWU tracks UK-listed equities with a 3.1% yield and solid three-year performance of +18% annually. Technicals show the fund trading 1.3% below its 20-day MA and 0.9% below its 50-day MA, with RSI at 44 and a negative MACD histogram suggesting fading momentum. The fund sits 77.7% of the way through its 52-week range, near midcycle. No meaningful macro catalyst has emerged: Treasury yields are stable with the curve upward-sloping, the dollar has strengthened modestly (+0.93% on the week), and VIX has compressed to 14.42. US inflation at 3.4% and unemployment at 4.1% remain within the recent range, and the Fed rate path prices only modest further tightening. Analyst coverage of the top 5 holdings (36% of the fund) leans bullish at 57.5% buy-rated with a +11.2% weighted price target, but this roll-up is thin relative to the full fund and does not override the technical retracement and steady macro backdrop. Recent 1-month and 5-day returns are negative, volume is below average, and there is no news catalyst to interrupt the sidelong consolidation. The absence of recent share count data prevents a read on fund flows. The positioning is neither clearly bullish nor bearish, warranting a neutral stance with modest upside bias from analyst sentiment alone.

**Main reasons it gave:**
- RSI 44 and negative MACD histogram indicate fading momentum
- Price 1.3% below 20-day MA and 0.9% below 50-day MA
- Analyst coverage of top 5 holdings shows +11.2% weighted price target but covers only 36% of fund
- Macro backdrop stable with no rate or policy surprises; dollar +0.93% on the week
- Volume 0.66x 20-day average on recent weakness

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 47.53 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 48.14 (-1.3%), 50d 47.99 (-0.9%), 200d 46.54 (+2.1%); 50d above 200d
Momentum: RSI(14) 44.0 | MACD -0.168 vs signal -0.068 (histogram -0.100)
Returns: 1d -0.3% | 5d -0.6% | 1m -2.9% | 3m +4.3%
52-week range: 41.04 - 49.39 (now 77.7% of the way up)
Volatility: ATR(14) 0.45 (0.9% of price) | annualised 20d 11.2%
Volume: 0.66x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 36.0% of the fund by weight
Ratings by weight: buy 57.5% | hold 42.5% | sell 0.0% (mean 2.18 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.2% above the current prices
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 79.92M | fund size: 3.80B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EZA is a South African-focused ETF with a rich 7.1% yield and attractive valuations (P/E 9.31, P/B 2.24) that offer structural appeal. Analyst coverage of its top 45.6% is uniformly bullish with a +21.8% weighted price target, and the three-year track record of +28.3% annualized returns demonstrates execution. However, the technical picture offers little support for a directional move here and now. Price is down 2% from its 20-day SMA despite being up 7.4% over three months, and momentum is weak: RSI at 48 shows no directional conviction, MACD is below signal with a -0.432 histogram, and volume is only 0.50x the 20-day average. The fund is positioned only 38.7% of the way up its 52-week range, suggesting it has not yet participated in the broader risk-on moves that might lift emerging market equities. Macro conditions are mixed: the dollar has strengthened sharply (+0.93 on the week to 100.58), which headwinds South African assets and the rand-denominated holdings; the Fed rate path still prices 4 quarter-point hikes, which keeps global financial conditions restrictive; and the VIX at 14.42 indicates calm but not conviction. Treasury yields at the long end have dipped slightly, but the curve is normally sloped and there is no policy surprise to anchor a tactical call. The fund's no news and unknown flow direction leave behavioral signals absent. The case for EZA is fundamentally sound—cheap equity, high yield, solid coverage—but it is a matter of patience and price, not timing. A sustained break above the 20-day SMA on volume would be required to shift conviction higher.

**Main reasons it gave:**
- Uniform buy ratings and +21.8% weighted price target among top 5 holdings covering 45.6% of fund
- Valuation floor: P/E 9.31, P/B 2.24, 7.1% yield
- Momentum and trend both weak: RSI 48, MACD below signal, price below 20d SMA on 0.5x volume
- Dollar strength +0.93 on week headwinds emerging market rand-denominated assets
- No flow data and no news; technical recovery needed to confirm bullish thesis

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 68.63 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 70.06 (-2.0%), 50d 67.42 (+1.8%), 200d 69.27 (-0.9%); 50d below 200d
Momentum: RSI(14) 48.0 | MACD 0.010 vs signal 0.442 (histogram -0.432)
Returns: 1d +0.6% | 5d -0.4% | 1m -5.4% | 3m +7.4%
52-week range: 60.43 - 81.60 (now 38.7% of the way up)
Volatility: ATR(14) 1.25 (1.8% of price) | annualised 20d 21.3%
Volume: 0.50x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.55</summary>

```text
Fund type: Focused Region
What it holds: P/E 9.31 | P/B 2.24 | P/S 1.92 | 3y earnings growth n/a
Yield: 7.1%
Three-year record: +28.3% a year | beta to the market 1.02
Cost and size: expense ratio 0.59% | net assets 578.49M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Anglogold Ashanti PLC 13.7%, Gold Fields Ltd 9.9%, Naspers Ltd Class N 8.8%, Firstrand Ltd 7.1%, Standard Bank Group Ltd 6.1%
Sector mix: Basic materials 41.0%, Financial services 33.2%, Consumer cyclical 12.8%, Communication services 6.2%
```

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

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.65</summary>

```text
Rolled up from the 5 largest holdings, 45.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.82 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.8% above the current prices
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 7.90M | fund size: 542.18M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> INDA faces mixed signals with no clear macro catalyst to drive a directional view. The fund's technicals are weak: price is down 3.6% from its 200-day moving average, momentum is flagging (RSI 43.5, MACD below signal), and the 50-day is below the 200-day, signaling deteriorating trend. Volume is subdued at 0.24x the 20-day average, suggesting low conviction. The 1-month and 3-month returns are modestly negative, and the fund sits only 29% of the way up its 52-week range, well off recent highs. On the positive side, analyst coverage of the largest holdings (24.7% of the fund, a thin sample) shows 100% buy ratings with a +30.8% weighted price target, and the fund's three-year beta of 0.56 provides some stability. However, the valuations are stretched (P/E 22.87, P/B 3.14, P/S 2.72), and fund flows data is unavailable. The macro backdrop is benign but unremarkable: the US yield curve is normalizing with a +0.95 slope, the dollar has strengthened 0.93 this week, inflation expectations remain anchored at 2.3%, and the VIX at 14.42 reflects calm markets. There is no rate surprise, no policy catalyst, and no technical break to justify a conviction move. The stretched valuations and weakening technicals offset the positive analyst view, leaving no persuasive reason to bet directionally when the broader setup offers no edge.

**Main reasons it gave:**
- Price 3.6% below 200-day MA with 50d below 200d
- RSI 43.5 and MACD histogram negative signal weakening momentum
- Valuation elevated at P/E 22.87, P/B 3.14 relative to growth backdrop
- Analyst buy ratings and +30.8% price target on largest 24.7% of holdings offset by thin coverage
- Subdued volume at 0.24x 20-day average suggests low conviction in direction

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 48.31 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 48.95 (-1.3%), 50d 49.21 (-1.8%), 200d 50.10 (-3.6%); 50d below 200d
Momentum: RSI(14) 43.5 | MACD -0.398 vs signal -0.325 (histogram -0.072)
Returns: 1d -0.4% | 5d +1.5% | 1m -2.7% | 3m -1.5%
52-week range: 45.42 - 55.29 (now 29.3% of the way up)
Volatility: ATR(14) 0.44 (0.9% of price) | annualised 20d 14.6%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

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
Rolled up from the 5 largest holdings, 24.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.36 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.8% above the current prices
Holdings read: HDFCBANK.NS, RELIANCE.NS, ICICIBANK.NS, BHARTIARTL.NS, INFY.NS
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 139.94M | fund size: 6.76B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> KSA presents a mixed picture with offsetting signals. On the bullish side, analyst coverage of the fund's five largest holdings (44.4% of the fund) shows 90% buy-rated securities with a weighted price target of +15.8% above current levels, and the fund trades at reasonable valuations (P/E 15.0, yield 2.7%). However, multiple headwinds constrain conviction. Technically, the fund is below all major moving averages (20d, 50d, 200d), momentum is weakly negative (RSI 36, MACD histogram -0.165), and volume is 0.33x the 20-day average—signs of waning interest. Returns are down over 1-month and 3-month horizons despite the bullish analyst view, suggesting sentiment has turned cautious. The dollar strengthened +0.93 this week to 100.58, which is a headwind for emerging market exposure. Volatility is calm at 14.42 VIX, reducing urgency in either direction. The macro backdrop is stable but not supportive: yields are flat to slightly down on the week, the Fed is on hold, and the upward-sloping curve offers no special tailwind to Saudi equities. The fund's low beta (0.18) and three-year return of +1.5% annually reflect its defensive positioning within the EM universe. Analyst optimism on the largest holdings does not overcome the technical deterioration and regional headwinds. This is a hold for existing positions rather than a new entry point.

**Main reasons it gave:**
- Analysts rate 90% of top-5 holdings as buy with +15.8% price target
- Price below 20d, 50d, and 200d moving averages; RSI 36 indicates weak momentum
- Dollar index +0.93 on week, headwind to emerging market exposure
- Volume 0.33x 20-day average; 1m and 3m returns negative despite bullish analyst view
- Flow data unavailable; no recent rating changes among major holdings

<details><summary><b>News</b> — score +0.00</summary>

- [(KSA) as a Liquidity Pulse for Institutional Tactics](https://www.google.com/goto?url=CAESvAEB6zswFfazaLi1jeS5MtAUjq5M9Rp0cTMY5gWkxxKphaszEBeXtXHM-I9ZgUsIGUrVH3UeNRsohvw3iFpNbObIqMLApBZNEOWStXkjJUYlXx2D5G2sckrZJP7LOon_n-kaehpwHvWqqCDB8hKRZxMe5SXkOyEDBcSBIG9U8j84Okt7X0PllGfiDtv2Y0aEEyPCoPlAgfyYX9k3ieLUdeRv7sK0zwvxYQLtDHYDw6wyDJ5G53kvKnPhGQoURw)  
  <sub>Stock Traders Daily, 7 hours ago</sub>  
  Key findings for Ishares Msci Saudi Arabia Etf (NYSE: KSA). Neutral Sentiment in Near Term Could Moderate Mid-Term Weakness; A mid-channel oscillation...
- [Bet on These Nuclear ETFs to Ride the AI Data Center Boom Now](https://www.tradingview.com/news/zacks:0431ede44094b:0-bet-on-these-nuclear-etfs-to-ride-the-ai-data-center-boom-now/)  
  <sub>TradingView, 2 hours ago</sub>  
  The rapid expansion of artificial intelligence (AI) data centers is fundamentally reshaping global electricity demand. To this end, Gartner projected last...
- [Saudi Exchange clears Albilad Capital as market maker for three ETFs](https://enterpriseam.com/ksa/2026/09/22/saudi-exchange-clears-albilad-capital-as-market-maker-for-three-etfs/)  
  <sub>EnterpriseAM, 15 hours ago</sub>  
  Albilad will quote its own ETFs. Albilad Capital has been cleared to make markets in three of its ETFs. The Saudi Exchange approved Albilad Capital as a...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 37.28 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 38.26 (-2.6%), 50d 37.79 (-1.4%), 200d 38.14 (-2.3%); 50d below 200d
Momentum: RSI(14) 36.0 | MACD -0.231 vs signal -0.066 (histogram -0.165)
Returns: 1d +0.3% | 5d -0.4% | 1m -2.7% | 3m -2.4%
52-week range: 35.83 - 41.03 (now 27.9% of the way up)
Volatility: ATR(14) 0.29 (0.8% of price) | annualised 20d 8.5%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.00 | P/B 1.81 | P/S 3.04 | 3y earnings growth n/a
Yield: 2.7%
Three-year record: +1.5% a year | beta to the market 0.18
Cost and size: expense ratio 0.75% | net assets 638.50M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Al Rajhi Bank 14.1%, Saudi Arabian Oil Co 11.1%, Saudi National Bank 8.8%, Saudi Telecom Co 6.0%, Saudi Arabian Mining Co 4.4%
Sector mix: Financial services 41.9%, Basic materials 12.7%, Energy 12.1%, Communication services 8.8%
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
Rolled up from the 5 largest holdings, 44.4% of the fund by weight
Ratings by weight: buy 90.0% | hold 10.0% | sell 0.0% (mean 2.06 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.8% above the current prices
Holdings read: 1120.SR, 2222.SR, 1180.SR, 7010.SR, 1211.SR
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 17.02M | fund size: 634.49M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.25

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise this cycle: yields little changed, curve normally sloped, VIX calm at 14.4 and falling. The technical picture is constructive -- price above 20/50/200d, 50d above 200d, +11% in five days, MACD crossed positive -- but the move came on volume at 0.41x average and 3-month return is still -3.3%, so the breakout is not decisively confirmed. Analyst roll-up is uniformly bullish (100% buy, +35% targets) but covers only 49% of the fund and is a slow-moving input. Valuation is rich (P/E 37.8, beta 2.06) and the priced rate path implies hikes rather than cuts, a headwind for long-duration growth. News flow is noise -- price listings, an index-inclusion mechanic and a promotional piece on a rival ETF. Flows unknown. Slight bullish tilt from trend only.

**Main reasons it gave:**
- Price +7.0% over 20d SMA and +22.9% over 200d, 50d above 200d
- 5-day return +11.0% but on volume 0.41x 20-day average
- VIX 14.42, down 2.8 on week; 10y -4bp, no rate or data surprise
- Analyst roll-up 100% buy, +34.9% weighted target, but only 49.2% coverage
- Holdings P/E 37.78 with beta 2.06 and 2-year at 4.76% pricing hikes

<details><summary><b>News</b> — score +0.00</summary>

- [VanEck Semiconductor ETF (Derivatives) Price (SMH/USD) Today | Live Price, Market Cap & Chart](https://www.binance.com/en/price/vaneck-semiconductor-etf-derivatives)  
  <sub>Binance, 18 hours ago</sub>  
  The current price of VanEck Semiconductor ETF (Derivatives) (SMH) is $596.53. Top cryptocurrency prices are updated in real-time on Binance's price directory.
- [SK Hynix ADR Inclusions in the SMH ETF, VanEck Semi UCITS ETF, and KODEX US Semi ETF Rebalances](https://www.smartkarma.com/insights/sk-hynix-adr-inclusions-in-the-smh-etf-vaneck-semi-ucits-etf-and-kodex-us-semi-etf-rebalances)  
  <sub>Smartkarma, 17 hours ago</sub>  
  There are several notable ETFs (SMH ETF, VanEck Semiconductor UCITS ETF, and KODEX US Semiconductor ETF) that will include SK Hynix (SKHY US) ADRs in their...
- [VanEck Semiconductor ETF Outperforms S and P 500 in 2026](https://suaragarut.id/en/vaneck-semiconductor-etf-outperforms-index)  
  <sub>SuaraGarut.ID, 5 hours ago</sub>  
  The VanEck Semiconductor ETF (SMH) generated a total return of approximately 59 percent in 2026, outperforming the S and P 500 index's 12 percent gain with...
- [PSI: A Semiconductor ETF Built Around More Than Nvidia (NYSEARCA:PSI)](https://seekingalpha.com/article/4948533-psi-a-semiconductor-etf-built-around-more-than-nvidia)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  Summary. Invesco Semiconductors ETF earns a Buy rating for its differentiated, non-market cap-weighted approach to semiconductor and AI exposure.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.35</summary>

```text
Last close 601.62 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 562.34 (+7.0%), 50d 564.80 (+6.5%), 200d 489.68 (+22.9%); 50d above 200d
Momentum: RSI(14) 62.5 | MACD 3.524 vs signal -1.466 (histogram 4.990)
Returns: 1d +0.9% | 5d +11.0% | 1m +7.4% | 3m -3.3%
52-week range: 321.06 - 668.91 (now 80.7% of the way up)
Volatility: ATR(14) 16.78 (2.8% of price) | annualised 20d 35.3%
Volume: 0.41x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Technology
What it holds: P/E 37.78 | P/B 11.07 | P/S 13.20 | 3y earnings growth n/a
Yield: 0.2%
Three-year record: +58.0% a year | beta to the market 2.06
Cost and size: expense ratio 0.35% | net assets 67.79B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: NVIDIA Corp 22.6%, Taiwan Semiconductor Manufacturing Co Ltd ADR 9.7%, Broadcom Inc 6.1%, Micron Technology Inc 5.5%, Advanced Micro Devices Inc 5.4%
Sector mix: Technology 100.0%
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
Rolled up from the 5 largest holdings, 49.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +34.9% above the current prices
Holdings read: NVDA, TSM, AVGO, MU, AMD
Recent rating changes among them:
  - NVDA: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - TSM: 2026-09-02 Stifel: init, ? -> Buy
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-09-18 RBC Capital: reit, Outperform -> Outperform
  - AMD: 2026-09-10 Piper Sandler: init, ? -> Overweight
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 118.34M | fund size: 71.19B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> TUR is a focused Turkey equity fund down 8.2% over the past month, now trading 4.8% below its 200-day moving average with RSI at 39.7 and negative MACD histogram, indicating intermediate downtrend momentum. However, several factors temper a bearish conviction: (1) The fund's valuation remains compressed at P/E 13.81 and P/B 1.21, with a 2.1% yield providing income support. (2) Analyst coverage of the top 39.5% of holdings shows 100% buy ratings with +17.2% weighted price targets, suggesting meaningful undervaluation at current levels. (3) Macro conditions show a stable Fed path with calm volatility (VIX 14.42), and the curve remains normally upward-sloping. (4) The dollar strength (+0.93 on the week to 100.58) is a headwind for Turkey exposure given currency sensitivity, but this is reflected in the recent drawdown. The weak volume (0.32x average) and lack of recent news suggest a consolidation phase rather than a definitive break. The fund's three-year beta of 0.44 indicates lower systematic risk, and the mid-range positioning in the 52-week range (46.3%) does not suggest capitulation. A modest tilt to neutral rather than outright bullish reflects the technical weakness and momentum deterioration, partially offset by valuation and analyst support.

**Main reasons it gave:**
- P/E 13.81 and P/B 1.21 valuations compressed vs analyst +17.2% target
- Price 4.8% below 200-day SMA with RSI 39.7 and negative MACD histogram
- Dollar strength +0.93 to 100.58 headwind for Turkish assets
- 100% buy ratings on 39.5% of fund holdings by weight
- Weak volume 0.32x average suggests consolidation not capitulation

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 37.38 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 39.34 (-5.0%), 50d 39.22 (-4.7%), 200d 39.28 (-4.8%); 50d below 200d
Momentum: RSI(14) 39.7 | MACD -0.570 vs signal -0.240 (histogram -0.330)
Returns: 1d -0.7% | 5d -3.5% | 1m -8.2% | 3m -6.6%
52-week range: 31.90 - 43.74 (now 46.3% of the way up)
Volatility: ATR(14) 0.75 (2.0% of price) | annualised 20d 34.6%
Volume: 0.32x the 20-day average
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
Three-year record: +3.2% a year | beta to the market 0.44
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.2% above the current prices
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 15.65M | fund size: 585.00M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> VNQ is trading below its 20-, 50-, and 200-day moving averages, with momentum deteriorating (RSI 37.1, MACD histogram negative). Returns are negative across 1-month (-4.8%) and 3-month (-4.2%) timeframes. The technical picture is weak and suggests downward pressure. Offsetting this, the broader macro environment shows a normalized yield curve (+0.95 spread), calming volatility (VIX -2.8 to 14.42), and a 3.6% yield that remains attractive at current rates. Analyst consensus on the fund's largest holdings is unanimously bullish with a 16.6% weighted price target, and recent rating changes include upgrades (EQIX, AMT). News flow highlights pockets of momentum in mid-cap and small-cap REITs, though some small-cap names lag. The fund's fundamentals remain solid (beta 0.98, 3-year return 8.9% annualized), but near-term technicals are clearly broken and volume is light (0.28x average). The weak momentum and price deterioration outweigh the longer-term bullish backdrop and analyst positivity, warranting a cautious stance. A technical recovery to the 50-day SMA or a clear rate surprise lower would alter this view.

**Main reasons it gave:**
- RSI 37.1 with MACD histogram negative indicates momentum deterioration
- Price trading 3.8% below 50-day SMA in downtrend; 1-month return -4.8%
- Analyst consensus unanimously bullish with 16.6% weighted price target on top 5 holdings
- Yield curve normal and VIX low provide supportive macro backdrop
- Light volume (0.28x average) suggests conviction is weak on both sides

<details><summary><b>News</b> — score +0.20</summary>

- [Real estate stocks with the strongest dividend growth grades (VNQ:NYSEARCA)](https://seekingalpha.com/news/4645336-real-estate-stocks-with-the-strongest-dividend-growth-grades)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Screen the top 7 real estate stocks with A+ dividend growth grades—CTRE, CURB, DRH, LB, MRP, NMRK, WELL—plus key REIT ETFs.
- [Vanguard Real Estate ETF To Go Ex-Dividend On September 23rd, 2026 With 0.8046 USD Dividend Per Share](https://www.moomoo.com/news/post/76552332/vanguard-real-estate-etf-to-go-ex-dividend-on-september)  
  <sub>Moomoo, 10 hours ago</sub>  
  September21st (Eastern Time) - $Vanguard Real Estate ETF(VNQ.US)$ is trading ex-dividend on September 23rd, 2026.Shareholders of record on September 23rd,...
- [BXDC, SAFE lead 10 small-cap U.S. REITs with weak momentum grades](https://seekingalpha.com/news/4645428-bxdc-safe-lead-10-small-cap-us-reits-with-weak-momentum-grades)  
  <sub>Seeking Alpha, 10 minutes ago</sub>  
  Small-cap U.S. REIT momentum is lagging: see the weakest Quant Momentum Grades, YTD returns, and key names like BXDC and SAFE—review the list now.
- [Agree Realty: Perfect Balance, Limited Appeal Of Fixed Income (NYSE:ADC)](https://seekingalpha.com/article/4948540-agree-realty-perfect-balance-limited-appeal-of-fixed-income)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  Agree Realty Corporation maintains strong fundamentals, with robust credit metrics and a portfolio of 2824 retail properties. Read more on ADC stock here.
- [Mid-cap REIT momentum is building: 10 stocks in the watchlist (XLRE:NYSEARCA)](https://seekingalpha.com/news/4644793-mid-cap-reit-momentum-is-building-10-stocks-in-the-watchlist)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  Top mid-cap U.S. REITs are surging with A-range momentum grades—see the leaders, YTD gains, and key REIT ETFs to watch.
- [4 REITs with A+ momentum grades lead the small-cap stocks list](https://seekingalpha.com/news/4644791-4-reits-with-a-momentum-grades-lead-the-small-cap-stocks-list)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  Discover top small-cap U.S. REIT stocks with A-range momentum grades and strong YTD gains—see the leaders and REIT ETFs to watch.
- [JLL, DOC among 10 large and mega-cap REITs with strong momentum (XLRE:NYSEARCA)](https://seekingalpha.com/news/4644794-jll-doc-among-10-large--and-mega-cap-reits-with-strong-momentum)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  Large- and mega-cap U.S. REIT stocks are showing some powerful momentum, with several names carrying A-range Momentum Grades that point to stronger...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 93.76 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 95.50 (-1.8%), 50d 97.51 (-3.8%), 200d 94.33 (-0.6%); 50d above 200d
Momentum: RSI(14) 37.1 | MACD -1.187 vs signal -1.052 (histogram -0.135)
Returns: 1d -0.1% | 5d -0.4% | 1m -4.8% | 3m -4.2%
52-week range: 87.00 - 100.95 (now 48.5% of the way up)
Volatility: ATR(14) 1.07 (1.1% of price) | annualised 20d 9.9%
Volume: 0.28x the 20-day average
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
Three-year record: +8.9% a year | beta to the market 0.98
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

<details><summary><b>What analysts and big funds say</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.55</summary>

```text
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.70 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.6% above the current prices
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 761.95M | fund size: 71.44B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XHB is a consumer cyclical housing/building products fund with elevated beta (1.46) in a macro environment that offers mixed signals. On the positive side: the yield curve is normal and upward-sloping, volatility is calm (VIX 14.4), and the fund bounced +1.8% in the last day. Analysts covering the top 20.9% of holdings are bullish (73.5% buy-rated, +18.8% price target), and recent rating changes show stability or initiation rather than downgrades. However, technicals are deteriorating. The fund sits 7.4% below its 200-day MA with the 50d below 200d (a bear cross), RSI at 41.8 (not yet oversold but weak), and MACD slightly negative. Price action shows -7.3% over one month and -8.8% over three months. The 52-week range shows the fund trading near the bottom of its range (14.6% of the way up from low to high), and volume is thin at 0.27x average. Macro backdrop is stable but not bullish: near-term yields flat to up, inflation still elevated at 3.4%, and the Fed pricing in further hikes. Treasury yield curve slope is normal at +0.95, which is neutral for a cyclical. No clear catalyst has emerged this week beyond a routine distribution announcement. The thin analyst coverage and thin volume limit conviction. The technical deterioration and positioning in the bottom quartile of the year's range argue against a bullish lean, but the normal macro conditions and analyst support prevent a bearish call.

**Main reasons it gave:**
- Fund down 7.4% vs 200-day MA with 50d below 200d
- 73.5% buy ratings on top holdings with +18.8% target, though only 20.9% covered
- Trading 14.6% of 52-week range from bottom; thin volume 0.27x average
- Normal yield curve +0.95 and calm VIX 14.4, but macro backdrop offers no fresh tailwind
- RSI 41.8 and MACD slightly negative; -1.7% vs 20-day MA

<details><summary><b>News</b> — score +0.00</summary>

- [SPDR S&P Homebuilders ETF declares quarterly distribution of $0.5358](https://www.tradingview.com/news/seekingalpha:9c06a2cec094b:0-spdr-s-p-homebuilders-etf-declares-quarterly-distribution-of-0-5358/)  
  <sub>TradingView, 21 hours ago</sub>  
  Content provided by Seeking Alpha is intended for information purposes only, and that Seeking Alpha does not offer any personalist investment advice and is...
- [ETFs Investing in Installed Building Products, Inc. Stocks](https://www.tradingview.com/symbols/GETTEX-2IL/etfs/)  
  <sub>TradingView, 15 hours ago</sub>  
  Explore funds investing in 2IL in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 98.72 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 100.44 (-1.7%), 50d 104.87 (-5.9%), 200d 106.56 (-7.4%); 50d below 200d
Momentum: RSI(14) 41.8 | MACD -2.441 vs signal -2.388 (histogram -0.053)
Returns: 1d +1.8% | 5d +1.0% | 1m -7.3% | 3m -8.8%
52-week range: 94.86 - 121.36 (now 14.6% of the way up)
Volatility: ATR(14) 2.20 (2.2% of price) | annualised 20d 20.4%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 19.52 | P/B 2.34 | P/S 1.36 | 3y earnings growth n/a
Yield: 0.8%
Three-year record: +7.6% a year | beta to the market 1.46
Cost and size: expense ratio 0.35% | net assets 1.33B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Installed Building Products Inc 4.4%, Owens-Corning Inc 4.3%, Allegion PLC 4.3%, Champion Homes Inc 4.1%, Williams-Sonoma Inc 3.9%
Sector mix: Consumer cyclical 60.7%, Industrials 37.9%, Real estate 1.5%
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
Rolled up from the 5 largest holdings, 20.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 73.5% | hold 26.5% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.8% above the current prices
Holdings read: IBP, OC, ALLE, SKY, WSM
Recent rating changes among them:
  - IBP: 2026-09-15 Stifel: init, ? -> Buy
  - OC: 2026-09-11 Wells Fargo: main, Overweight -> Overweight
  - ALLE: 2026-08-10 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - SKY: 2026-08-06 UBS: main, Buy -> Buy
  - WSM: 2026-09-09 Evercore ISI Group: main, In-Line -> In-Line
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 13.82M | fund size: 1.36B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLB exhibits mixed signals that do not support a directional conviction. Technicals show deteriorating momentum with RSI at 38.2 (oversold), a negative MACD histogram, and the price trading 3% below its 20-day and 50-day moving averages, but notably the fund has recovered 68.9% of its 52-week range from lows, suggesting no capitulation. The recent 1-day gain of 0.8% on subdued volume (0.36x average) lacks conviction. Macro conditions remain benign: yields are stable with an upward-sloping curve, the dollar has strengthened modestly, and the VIX at 14.42 shows calm. The Fed's rate-cut expectations (4 quarter-point hikes priced over two years) and market inflation expectations at 2.3% provide a neutral backdrop for materials. Fund fundamentals show reasonable valuation (P/E 24.59, yield 1.6%) with a three-year record of +9.2% annually and low beta (0.82), but no compelling catalyst. Analyst sentiment on the five largest holdings (37% of the fund) is solidly bullish with a 100% buy rating and a +13.1% weighted price target, providing some support. However, the news flow is generic ETF recommendation content with no material catalyst, and fund flows data is insufficient to read conviction. The combination of oversold technicals, subdued recent performance (-6.4% in one month), and lack of a macro or policy catalyst argues against conviction in either direction at this time.

**Main reasons it gave:**
- Momentum deteriorated with RSI 38.2 and negative MACD histogram despite slight daily bounce
- Analyst roll-up shows 100% buy rating and +13.1% price target on 37% of fund
- Price trading 3% below 20d and 50d moving averages with subdued volume
- Fund flows data insufficient to assess conviction; no policy or macro catalyst present
- One-month return of -6.4% contrasts with three-year annual gain of +9.2%

<details><summary><b>News</b> — score +0.00</summary>

- [Should You Invest in the iShares U.S. Basic Materials ETF (IYM)?](https://finance.yahoo.com/markets/stocks/articles/invest-ishares-u-basic-materials-102002460.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  If you're interested in broad exposure to the Materials - Broad segment of the equity market, look no further than the iShares U.S. Basic Materials ETF...
- [Basic Materials Sector Still Shows Promise In 2026, But Proceed With Caution](https://seekingalpha.com/article/4948499-basic-materials-sector-still-shows-promise-in-2026-but-proceed-with-caution)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Top XLB holdings like Newmont, Freeport-McMoran, Linde, Corteva, and Nucor have delivered strong YTD performance. Learn why XLB ETF is a hold.
- [Leading And Lagging Sectors For September 22, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61919139/leading-and-lagging-sectors-september-22-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLB) State Street Materials Select Sector SPDR ETF 49.9500 0.240 0.48 2.2K (NYSE:XLP) State...
- [Staples ETF Widens Gap Over Discretionary in 2026](https://www.etftrends.com/sector-investing-content-hub/staples-etf-widens-gap-over-discretionary-in-2026/)  
  <sub>ETF Trends, 3 hours ago</sub>  
  State Street's staples ETF is outpacing its discretionary counterpart by more than 13 percentage points as household budgets tighten.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 50.11 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 51.68 (-3.0%), 50d 51.74 (-3.1%), 200d 50.45 (-0.7%); 50d above 200d
Momentum: RSI(14) 38.2 | MACD -0.612 vs signal -0.380 (histogram -0.232)
Returns: 1d +0.8% | 5d -1.2% | 1m -6.4% | 3m -1.5%
52-week range: 42.23 - 53.67 (now 68.9% of the way up)
Volatility: ATR(14) 0.76 (1.5% of price) | annualised 20d 13.0%
Volume: 0.36x the 20-day average
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
Three-year record: +9.2% a year | beta to the market 0.82
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
Weighted price target: +13.1% above the current prices
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 71.92M | fund size: 3.60B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — NEUTRAL, confidence 0.25

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise this week: yields little changed, curve normal, VIX calm at 14.4, and the only policy note is a 2-year still pricing hikes. XLC trades modestly above its 20/50d averages with RSI 57.7 and a mild positive MACD, but the 50d remains below the 200d and volume is 0.41x average -- a drift, not a break. Holdings analyst roll-up is constructive (100% buy weight, +11% targets) but covers only 45% of the fund and is slow-moving. News is constituent-level noise (PSKY/WBD deal, TMUS downgrade) that the basket dilutes. Flow direction unknown, so no behavioural read.

**Main reasons it gave:**
- 50d SMA still below 200d despite price +2% over 20d SMA
- Volume 0.41x 20-day average -- no conviction behind the move
- VIX 14.42, down 2.8 on the week; 10y -4bp, no rate surprise
- Analyst roll-up 100% buy weight, +11.1% targets, but only 45.5% coverage
- Fund P/E 15.4 with 3y return +19.3%/yr, beta 0.85

<details><summary><b>News</b> — score +0.00</summary>

- [Paramount Skydance Rises 4% on 12-State Settlement, Warner Bros. Discovery Holds Flat as $110B Deal Nears Its Close](https://www.google.com/goto?url=CAES1AEB6zswFQnMml_UulFytciQNLXCe-vIIiokyF5cpe3F76K_OTqe8Dk6xTRXXuVoLF1BC8L8wEGpR8lTsP5i1sXtE1Rs2Yq8FdBFqTHY11TclpMps4GIsjrncy_LYHi94DQivJGL5XOehpaUEMXL_YMufSZi0QYhRGOVyiBbmwfG6bWGJSCUs523tzxEA7pIEM8Gi_GtGko75JQQCckVuL2201Ybxgz-BnCEQycKZp7Gnn-JLprpejBd1RKSEXcZQT-bcObwUAOYx3lcvVnHyYbhAAr76Q)  
  <sub>24/7 Wall St., 17 minutes ago</sub>  
  PSKY surged 8% after a 12-state settlement cleared its $110B WBD acquisition path; WBD held flat, already up 8% over the prior month. XLC's 0.4% gain versus...
- [These five communication services stocks score highest on dividend growth (XLC:NYSEARCA)](https://seekingalpha.com/news/4644863-these-five-communication-services-stocks-score-highest-on-dividend-growth)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  Top communication services dividend growth stocks ranked: GOOGL, META, MTCH, NYT & TMUS plus key ETFs—see who leads and invest smarter today.
- [Leading And Lagging Sectors For September 22, 2026](https://www.google.com/goto?url=CAESngEB6zswFc2twsODRLTV3NPiiEaRHCIizLuRrw7GeMyfQfDCP3TtAYtO2sH_QgboABb7_WZKj6VYKuP77Ud9fLbH0ZCrC2T14Ufj19qBwSSke242_5EGQVZ1wMkxTbeLCtIC_iM6vSb9bTmeK6VKALn8GbcU8PyFFdqSXEX2PhmlulsF4mjnXPz8HijLA8DqQkC9LYvXkPhssEfmVT9NtQ)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLB) State Street Materials Select Sector SPDR ETF 49.9500 0.240 0.48 2.2K (NYSE:XLP) State...
- [T-Mobile Stock Slips To More Than Two-Year Low — JPMorgan Cuts Target Ahead Of Q3 Citing Softer Service Revenue Outlook](https://www.tradingview.com/news/stocktwits:a31866873094b:0-t-mobile-stock-slips-to-more-than-two-year-low-jpmorgan-cuts-target-ahead-of-q3-citing-softer-service-revenue-outlook/)  
  <sub>TradingView, 23 hours ago</sub>  
  T-Mobile US Inc. (TMUS) shares slipped as much as 3% on Monday, to their lowest level in more than two years.JPMorgan analyst Sebastiano Petti lowered the...
- [Billionaire Investor More Than Doubles Live Nation Stake](https://www.google.com/goto?url=CAESqgEB6zswFZlc6lrQFs2gqnqxdMht-A4bzbA_KTvNApkG9TwzdYyuEYWv5bTDFF8oeftPAptAVU3pnXvQXeLrXUP7yN06xPwiuAUp87iMkjJdCHWABWaKA9s1X_Gr04zufB5RLU7oLAYsKqi5H03X7xYpjkfM-Y5Ddexv16qgfbkmIZFt6lbwEN3yIMZanOZAUwlFPwTcZn-I3kEcZW8hWptHgxbMGKBrHfiP1A)  
  <sub>Benzinga, 21 hours ago</sub>  
  Dan Loeb's Third Point raised its Live Nation stake 144% in Q2 while making Warner Bros Discovery its largest holding at June 30.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 114.79 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 112.58 (+2.0%), 50d 111.31 (+3.1%), 200d 113.99 (+0.7%); 50d below 200d
Momentum: RSI(14) 57.7 | MACD 0.642 vs signal 0.503 (histogram 0.139)
Returns: 1d +0.0% | 5d +0.7% | 1m +3.0% | 3m +7.0%
52-week range: 105.38 - 120.08 (now 64.0% of the way up)
Volatility: ATR(14) 1.84 (1.6% of price) | annualised 20d 21.0%
Volume: 0.41x the 20-day average
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
Three-year record: +19.3% a year | beta to the market 0.85
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.54 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.1% above the current prices
Holdings read: META, GOOGL, GOOG, T, VZ
Recent rating changes among them:
  - META: 2024-09-30 Cantor Fitzgerald: reit, Overweight -> Overweight
  - GOOGL: 2026-09-18 Tigress Financial: main, Strong Buy -> Strong Buy
  - GOOG: 2026-07-23 JP Morgan: main, Overweight -> Overweight
  - T: 2026-09-21 BNP Paribas: up, Neutral -> Outperform
  - VZ: 2026-07-27 TD Cowen: main, Buy -> Buy
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 202.30M | fund size: 23.22B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLE trades near multi-year highs (85% through its 52-week range) on a 11.7% gain over 200 days, but technical momentum has stalled with price below its 20-day moving average, RSI neutral at 45.7, and MACD histogram negative. The macro backdrop is mixed: oil prices have slipped this week (WTI to $93.51), the EIA forecasts a 10% decline in crude over the next six months to $70/barrel by end of 2027, and crude inventories drew last week but sit only at the 38th percentile. Petrol is notably tight at the 13th percentile, which supports refiner margins for holdings like MPC and PSX. Analyst coverage of the fund's top five holdings—51.7% of the fund—shows all buy ratings with a +6.4% price target, though Jefferies downgraded MPC from Buy to Hold on 2026-09-22, the day of this close. The energy sector itself shows no fundamental repricing; valuations (P/E 17.74) are unchanged and the fund's three-year return of +15.1% annually reflects prior upside already captured. VIX is calm at 14.4, rates are stable with the yield curve normal, and the dollar has strengthened 93 basis points this week—typically a headwind for energy. Neither fund flows nor positioning data is available to confirm conviction. The news cycle repeats that XLE is concentrated in oil and gas (not surprising for an energy ETF), and one day of modest price weakness does not constitute a catalyst. A technical breakdown from here or continued price weakness would argue bearish, but the current setup favors waiting for either trend confirmation or a catalyst—rate shock, geopolitical event, or EIA surprise—before taking a directional call.

**Main reasons it gave:**
- Oil prices fell to $93.51 as of publication; EIA forecasts WTI declining to $70 by end of 2027
- Price below 20-day SMA at 62.45 vs 64.02, RSI 45.7 neutral, MACD histogram negative
- Petrol inventories at 13th percentile support refiner margins
- Analyst coverage of top 51.7% of fund shows 100% buy ratings with +6.4% price target, though MPC downgraded to Hold on 2026-09-22
- Fund at 85% of 52-week range with three-year annualized return of 15.1% already achieved; no fresh catalyst evident

<details><summary><b>News</b> — score -0.15</summary>

- [XLE Is 91% Oil and Gas. Investors Buying "Energy" May Own Less Than They Think](https://247wallst.com/investing/etf/2026/09/21/xle-is-91-oil-and-gas-investors-buying-energy-may-own-less-than-they-think/)  
  <sub>24/7 Wall St., 19 hours ago</sub>  
  The ticker says energy, but the fund's holdings tell a much narrower story than most investors expect before they buy in. By Omor Ibne Ehsan.
- [Oil Slid, Sending Energy ETFs Lower Before The Open](https://finimize.com/content/oil-slid-sending-energy-etfs-lower-before-the-open)  
  <sub>Finimize, 2 hours ago</sub>  
  WTI fell to $93.51 a barrel and Brent to $98.50, while TotalEnergies signed an MOU with Venezuela's PDVSA and Solaris lined up $1 billion of notes due 2032.
- [XLE ETF is 91% oil and gas, not broad energy ex...](https://pluang.com/en/news-feed/xle-91-persen-minyak-dan-gas-pemodal-energi-mungkin-milik-kurang-dari-yang)  
  <sub>Pluang, 19 hours ago</sub>  
  The Energy Select Sector SPDR Fund (XLE) is heavily concentrated in large-cap U.S. oil and gas companies like ExxonMobil and Chevron, making up 91% of its...
- [The Fed Is Watching AI Inflation. Here's What ETF Investors Should Watch](https://www.tradingview.com/news/benzinga:92e972516094b:0-the-fed-is-watching-ai-inflation-here-s-what-etf-investors-should-watch/)  
  <sub>TradingView, 23 hours ago</sub>  
  ETF investors have an unusual second-order trade due to exorbitant AI spending.Chicago Fed President Austan Goolsbee warned Monday that a surge in AI...
- [Large-cap energy stocks with long-running Strong Buy Quant ratings (XLE:NYSEARCA)](https://seekingalpha.com/news/4645377-large-cap-energy-stocks-with-long-running-strong-buy-quant-ratings)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Screen of large-cap energy stocks with 60+ days of Strong Buy Quant Ratings—NESR, PARR, PBF, PSX, DINO, CVX—plus key energy ETFs.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.15</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 62.45 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 64.02 (-2.5%), 50d 61.44 (+1.6%), 200d 55.90 (+11.7%); 50d above 200d
Momentum: RSI(14) 45.7 | MACD 0.591 vs signal 1.042 (histogram -0.451)
Returns: 1d -0.0% | 5d -5.3% | 1m -1.9% | 3m +14.7%
52-week range: 42.61 - 65.93 (now 85.1% of the way up)
Volatility: ATR(14) 1.31 (2.1% of price) | annualised 20d 21.8%
Volume: 0.50x the 20-day average
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
Three-year record: +15.1% a year | beta to the market -0.07
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
US inventories, week ending 2026-09-11 (published the following Wednesday)
  Crude oil: 423.4 million barrels, -0.6 on the week (a draw), 38% percentile over 52 weeks
  Petrol: 207.7 million barrels, +0.8 on the week (a build), 13% percentile over 52 weeks -- low for the time of year
  Diesel: 107.9 million barrels, +1.6 on the week (a build), 33% percentile over 52 weeks
  Natural gas: 3,298.0 billion cubic feet, +44.0 on the week (a build), 71% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 51.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.4% above the current prices
Holdings read: XOM, CVX, COP, MPC, PSX
Recent rating changes among them:
  - XOM: 2026-09-03 Piper Sandler: main, Neutral -> Neutral
  - CVX: 2026-09-03 BMO Capital: main, Outperform -> Outperform
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 186.42M | fund size: 11.64B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.25

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise this cycle: yields barely moved (10y -4bp), curve normally sloped, VIX fell to 14.4 and inflation/claims data were in line. The only notable change is price itself -- XLF is 4-5% under both its 20d and 50d SMAs with RSI 29 and a negative MACD histogram, but that break came on light volume (0.61x) and the 50d remains above the 200d, so it reads as a pullback within an uptrend rather than a decisive breakdown. Holdings are reasonably valued (P/E 16.4) and analyst coverage of the top 41.5% is unanimously buy with ~14% upside, a mild offset. The one live macro headwind is a 2-year at 4.76% pricing hikes rather than cuts, which cuts both ways for banks. News flow was sector roundups and single-name stories, which carry no information for the basket. No side justified.

**Main reasons it gave:**
- RSI(14) 29.1 and price 4.3%/4.4% below 20d/50d SMA, but 50d still above 200d
- Breakdown on 0.61x average volume -- no heavy-volume confirmation
- 10y yield -4bp on week, VIX -2.8 to 14.4, curve +0.95 normal: no rate or policy surprise
- 2-year 4.76% vs 4.00% target prices ~4 hikes -- ambiguous for financials
- Top-5 holdings (41.5% of fund) 100% buy-rated with +13.8% weighted target, coverage thin relative to fund

<details><summary><b>News</b> — score +0.00</summary>

- [Leading And Lagging Sectors For September 22, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61919139/leading-and-lagging-sectors-september-22-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLB) State Street Materials Select Sector SPDR ETF 49.9500 0.240 0.48 2.2K (NYSE:XLP) State...
- [Northern Trust Stock: Is NTRS Outperforming the Financial Sector?](https://finance.yahoo.com/markets/stocks/articles/northern-trust-stock-ntrs-outperforming-160739477.html)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  Northern Trust Corporation (NTRS), headquartered in Chicago, Illinois, offers wealth management, asset servicing, asset management, and banking solutions.
- [Sector Update: Financial Stocks Advance Monday Afternoon](https://www.moomoo.com/news/post/76546999/sector-update-financial-stocks-advance-monday-afternoon)  
  <sub>Moomoo, 21 hours ago</sub>  
  Financialstocks were advancing in Monday afternoon trading, with the NYSE Financial Index rising 0.6% and the State Street Financial Select Sector SPDR ETF...
- [Why do investors keep ignoring higher yields and oil prices?](https://invezz.com/au/news/2026/09/22/why-do-investors-keep-ignoring-higher-yields-and-oil-prices/)  
  <sub>Invezz, 1 hour ago</sub>  
  Historically, two financial forces have consistently struck fear into equity markets: higher oil prices and a sharp increase in the government bond yields.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 54.65 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 57.12 (-4.3%), 50d 57.15 (-4.4%), 200d 53.71 (+1.8%); 50d above 200d
Momentum: RSI(14) 29.1 | MACD -0.476 vs signal -0.172 (histogram -0.304)
Returns: 1d -2.2% | 5d -3.9% | 1m -4.9% | 3m +1.4%
52-week range: 47.81 - 58.56 (now 63.7% of the way up)
Volatility: ATR(14) 0.75 (1.4% of price) | annualised 20d 13.7%
Volume: 0.61x the 20-day average
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
Three-year record: +18.8% a year | beta to the market 0.71
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 41.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.8% above the current prices
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 883.44M | fund size: 48.28B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLI is trading below its 20d, 50d and 200d moving averages, with momentum deeply in bearish territory: RSI at 34.5 signals oversold conditions, MACD is negative with a widening histogram, and the fund has declined 5.9% over one month and 4.8% over three months. Volume is below average, which undercuts the significance of the technical breakdown. The macro backdrop is stable with a normal upward-sloping yield curve, the dollar has strengthened but modestly, and the VIX has fallen to a calm 14.42, suggesting no acute risk-off event is driving the weakness. Analyst coverage of the five largest holdings (25.8% of the fund) is uniformly bullish, with a weighted price target 24.5% above current levels and a recent buy upgrade for Union Pacific. Fund basics show a P/E of 28.43, elevated but consistent with prior growth, and a three-year record of +19% annualized return. The fund pays a 1.2% yield and has substantial net assets. The bearish technicals and oversold reading suggest a bounce is possible from here, but the timing of a macro turn is uncertain and the fund's valuation leaves limited margin of safety. No policy surprise, inflation surprise, or decisive technical break on volume has occurred to justify a directional call. The weakness appears tactical rather than structural, but the combination of momentum damage and elevated valuation argues for patience before adding exposure.

**Main reasons it gave:**
- RSI 34.5 and MACD negative; price 5% below 50d SMA
- Analyst roll-up shows 100% buy ratings with +24.5% price target on largest 25.8% of fund
- P/E 28.43 elevated; three-year return 19% annualized sustains valuation
- Macro backdrop stable: VIX 14.4, normal yield curve, no data surprises
- Volume 0.51x 20d average undercuts technical breakdown significance

<details><summary><b>News</b> — score +0.00</summary>

- [Four industrial stocks with persistent Strong Buy Quant signals (XLI:NYSEARCA)](https://seekingalpha.com/news/4645451-four-industrial-stocks-with-persistent-strong-buy-quant-signals)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Industrial stock picks: 4 names with 60+ days of Strong Buy Quant Ratings (ATI, SNDR, FA, KNX).
- [Leading And Lagging Sectors For September 22, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61919139/leading-and-lagging-sectors-september-22-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLB) State Street Materials Select Sector SPDR ETF 49.9500 0.240 0.48 2.2K (NYSE:XLP) State...
- [State Street Industrial Select Sector SPDR ETF declares quarterly distribution of $0.4550](https://www.tradingview.com/news/seekingalpha:1551123ce094b:0-state-street-industrial-select-sector-spdr-etf-declares-quarterly-distribution-of-0-4550/)  
  <sub>TradingView, 21 hours ago</sub>  
  Content provided by Seeking Alpha is intended for information purposes only, and that Seeking Alpha does not offer any personalist investment advice and is...
- [XTN: Transportation Likely To Lag Into 2027 Amid Macro Pressures And Factor Weaknesses](https://seekingalpha.com/article/4948496-xtn-transportation-likely-to-lag-into-2027-given-macro-pressures-factor-weaknesses)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  Summary. I initiate coverage of the State Street SPDR S&P Transportation ETF with a Hold rating. I believe XTN will underperform IVV into 2027 as higher...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.65</summary>

```text
Last close 169.63 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 173.01 (-1.9%), 50d 178.52 (-5.0%), 200d 171.80 (-1.3%); 50d above 200d
Momentum: RSI(14) 34.5 | MACD -2.939 vs signal -2.833 (histogram -0.106)
Returns: 1d -0.2% | 5d +0.5% | 1m -5.9% | 3m -4.8%
52-week range: 147.83 - 186.51 (now 56.4% of the way up)
Volatility: ATR(14) 2.39 (1.4% of price) | annualised 20d 13.0%
Volume: 0.51x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Industrials
What it holds: P/E 28.43 | P/B 6.75 | P/S 3.00 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +19.0% a year | beta to the market 1.02
Cost and size: expense ratio 0.08% | net assets 31.95B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Caterpillar Inc 6.7%, GE Aerospace 6.4%, RTX Corp 5.1%, GE Vernova Inc 4.4%, Union Pacific Corp 3.2%
Sector mix: Industrials 92.8%, Technology 6.7%, Basic materials 0.3%, Consumer cyclical 0.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

```text
Rolled up from the 5 largest holdings, 25.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.5% above the current prices
Holdings read: CAT, GE, RTX, GEV, UNP
Recent rating changes among them:
  - CAT: 2024-10-14 JP Morgan: main, Overweight -> Overweight
  - GE: 2026-07-23 Bernstein: main, Outperform -> Outperform
  - RTX: 2026-08-03 Bernstein: main, Market Perform -> Market Perform
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 136.63M | fund size: 23.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLP has outperformed discretionary YTD (+6.6% vs broader market advance) and carries a low beta of 0.49, making it a defensive anchor. The fund's largest holdings are all rated Buy by consensus with a weighted price target 12.9% above current levels, and the 2.6% yield supports downside. However, technicals show weakness: price sits below all major moving averages (20d, 50d, 200d), RSI at 41.5 signals oversold conditions but momentum is negative (MACD histogram deteriorating), and recent returns are down across 1m (-3.7%) and 5d (-1.1%) timeframes despite today's +1.0% bounce. Volume is below average at 0.48x 20-day, suggesting limited conviction behind the move. The macro backdrop remains stable: yields flat to modestly lower this week, the curve normal at +95bp, the dollar firming slightly (+0.93), and the VIX calm at 14.4. Inflation at 3.4% with the Fed holding at 4.0% creates no urgent catalyst. The fund is trading defensively—a rational position in a calm macro environment—but has not broken decisively to either side. Analyst support for holdings is strong but not sufficient to overcome near-term technical deterioration and lack of volume conviction.

**Main reasons it gave:**
- Price below 20d, 50d and 200d moving averages despite recent outperformance
- Analyst consensus +12.9% price target on 39.6% of fund weight, all Buy rated
- RSI 41.5 with negative MACD histogram, volume 0.48x average on +1.0% bounce
- Fund yield 2.6% with low beta 0.49 provides defensive properties in stable macro
- No clear fund flow data; macro backdrop calm with normal yield curve and contained inflation expectations

<details><summary><b>News</b> — score +0.15</summary>

- [Staples ETF Widens Gap Over Discretionary in 2026](https://www.etftrends.com/sector-investing-content-hub/staples-etf-widens-gap-over-discretionary-in-2026/)  
  <sub>ETF Trends, 3 hours ago</sub>  
  The State Street Consumer Staples Select Sector SPDR ETF (XLP) has climbed 6.6% so far in 2026, according to State Street data as of September 21.
- [Inflation Pressures May Persist: ETFs Worth Watching Now](https://www.google.com/goto?url=CAESmAEB6zswFQFMKbiiRl9dZFlggHARpNA0SXN2yfLL0mIr0syhBjxs9BP9BtonxaQ_IAzjpR4wdzqXwpSaDyQzgrTS8VhG4gfa-2gvBFhJ9HQz3tmNUK5UqK1kNK9yMHxoyivfrgssOaUXDfxebJ6yeyud1DPaFbLzEC8a874QItiNYuTWL6yyM0wQvTsomlBep6PAUEk4ZBoEXA)  
  <sub>Zacks Investment Research, 19 minutes ago</sub>  
  From strong demand and AI spending to higher oil prices and war costs, multiple forces could keep inflation elevated for longer, putting ETFs in focus.
- [Leading And Lagging Sectors For September 22, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61919139/leading-and-lagging-sectors-september-22-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLB) State Street Materials Select Sector SPDR ETF 49.9500 0.240 0.48 2.2K (NYSE:XLP) State...
- [Hormel Foods Stock: Is HRL Underperforming the Consumer Defensive Sector?](https://finance.yahoo.com/markets/stocks/articles/hormel-foods-stock-hrl-underperforming-184803592.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  With a market cap of $11.5 billion, Hormel Foods Corporation (HRL) is a global branded food company. The company owns a broad portfolio of well-known brands...
- [State Street Consumer Disc Sel Sect SPDR ETF declares quarterly distribution of $0.2441](https://www.tradingview.com/news/seekingalpha:2683e83b6094b:0-state-street-consumer-disc-sel-sect-spdr-etf-declares-quarterly-distribution-of-0-2441/)  
  <sub>TradingView, 21 hours ago</sub>  
  Content provided by Seeking Alpha is intended for information purposes only, and that Seeking Alpha does not offer any personalist investment advice and is...
- [Exchange-Traded Funds Rise as US Equities Advance After Midday](https://www.moomoo.com/news/post/76545775/exchange-traded-funds-rise-as-us-equities-advance-after-midday)  
  <sub>Moomoo, 21 hours ago</sub>  
  BroadMarket IndicatorsBroad-market exchange-traded funds IWM and IVV were higher. Actively traded Invesco QQQ Trust (QQQ) added 2.5%.US equity indexes rose...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 82.77 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 84.25 (-1.8%), 50d 84.84 (-2.4%), 200d 83.61 (-1.0%); 50d above 200d
Momentum: RSI(14) 41.5 | MACD -0.688 vs signal -0.485 (histogram -0.203)
Returns: 1d +1.0% | 5d -1.1% | 1m -3.7% | 3m -1.1%
52-week range: 75.60 - 90.01 (now 49.8% of the way up)
Volatility: ATR(14) 0.98 (1.2% of price) | annualised 20d 11.7%
Volume: 0.48x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Consumer Defensive
What it holds: P/E 25.14 | P/B 4.58 | P/S 1.36 | 3y earnings growth n/a
Yield: 2.6%
Three-year record: +7.6% a year | beta to the market 0.49
Cost and size: expense ratio 0.08% | net assets 14.52B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Walmart Inc 9.8%, Costco Wholesale Corp 8.9%, Coca-Cola Co 7.3%, Procter & Gamble Co 7.2%, Philip Morris International Inc 6.2%
Sector mix: Consumer defensive 98.2%, Consumer cyclical 1.8%
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
Rolled up from the 5 largest holdings, 39.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.9% above the current prices
Holdings read: WMT, COST, KO, PG, PM
Recent rating changes among them:
  - WMT: 2026-09-10 DA Davidson: main, Buy -> Buy
  - COST: 2026-09-16 Oppenheimer: reit, Outperform -> Outperform
  - KO: 2026-07-30 Argus Research: main, Buy -> Buy
  - PG: 2026-08-07 Argus Research: down, Buy -> Hold
  - PM: 2026-07-30 Citigroup: main, Buy -> Buy
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 210.17M | fund size: 17.40B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLU sits at an inflection point with mixed signals. The technicals are weak: price is 8.5% below the 200-day moving average, RSI at 29.7 signals oversold conditions, MACD remains negative though histogram is tightening, and volume is subormal at 0.37x average. The one-month drawdown of 4.8% and three-month of 9.6% reflect a material selloff. However, offsetting bearish technicals is a compelling fundamental setup: the fund's top five holdings (39.4% of the fund) carry analyst consensus of 81% buy-rated and a weighted price target 21.9% above current levels, with no sell ratings. Valuations remain reasonable for utilities at 19.0x P/E with a 2.8% yield. The macro backdrop is neutral: the Fed is on hold at 4.0% target, the bond market prices modest easing ahead (4 quarter-point cuts over two years), Treasury yields are stable week-over-week, the dollar has strengthened modestly, and the VIX at 14.4 is calm. The oversold technical picture and strong analyst conviction on the largest holdings suggest potential upside, but the broken technical trend, weak recent momentum, and below-average volume preclude a bullish call. No clear macro catalyst has emerged to drive a directional move; the Fed's AI inflation watch mentioned in one headline does not constitute a policy surprise. The risk system will treat this as a weak signal.

**Main reasons it gave:**
- Price 8.5% below 200-day moving average with negative MACD and RSI 29.7 signals oversold technicals
- Analyst consensus 81% buy on largest 5 holdings with +21.9% weighted price target
- Utilities valuation at 19.0x P/E with 2.8% yield remains reasonable
- Sub-average volume and 4.8% one-month drawdown signal weak conviction to sell

<details><summary><b>News</b> — score +0.10</summary>

- [The Fed Is Watching AI Inflation. Here's What ETF Investors Should Watch](https://www.google.com/goto?url=CAESuwEB6zswFR0wSuLUALtQ0As0mQ17ih58fhwZ-i6gmaLUwgeBeY1R7KC4Kw7OLY9Gi19YNmjckOAoP-j9kHOXlvRXEViDNf6uhk5WVCwZ6oxJ45A_Llr39kRa2IBZBCtf08U8-21vNyI9kxo8yKgrtYspsPaj2geDvE2ugT2iIx6wUyg4Edbzmq_mA-VWdgLpkvayKjm5eexQtTA4Z0UORhkA8p-4LmZxjUHDGZCka5WKN3Y0wQCJl55GCsPa)  
  <sub>TradingView, 23 hours ago</sub>  
  ETF investors have an unusual second-order trade due to exorbitant AI spending.Chicago Fed President Austan Goolsbee warned Monday that a surge in AI...
- [Should You Invest in the iShares U.S. Utilities ETF (IDU)?](https://finance.yahoo.com/markets/stocks/articles/invest-ishares-u-utilities-etf-102001914.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  If you're interested in broad exposure to the Utilities - Broad segment of the equity market, look no further than the iShares U.S. Utilities ETF (IDU),...
- [The Strange Pair That Led the Market Higher](https://moneyandmarkets.com/the-strange-pair-that-led-the-market-higher/amp/)  
  <sub>Money & Markets, 20 hours ago</sub>  
  Only two sectors finished higher last week, and the unusual pairing tells us plenty about where investors are finding safety...
- [Leading And Lagging Sectors For September 22, 2026](https://www.google.com/goto?url=CAESngEB6zswFU40QRlDFI6bcGpTnka5JKKFvyq9JqlYyxufI-Bm4yIgNzfQ63e0I-qDE0WTKVgV7D5Rb3_zYTe6aIl2bTozxRPp0eyVhoczuGjU_rTxoWnBD46Whyg7BlA5R7etFiKAm8Yn6Rv0hHDq0S7ibKcFAWb1_paPzg2TSwFbh9mW1T6V1bBhayG8IGLGiwDwyaVKjqyEH9TPtHsU_g)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLB) State Street Materials Select Sector SPDR ETF 49.9500 0.240 0.48 2.2K (NYSE:XLP) State...
- [How Is AES Corporation's Stock Performance Compared to Other Utility Stocks](https://www.google.com/goto?url=CAESrwEB6zswFYmFTM9ukb1QF7DY_QjakmjTCbmX9VUMh2BFKXkgB_JelvssKotq9kUuWYCpyENcT6R2bJavL8RBdpyKoI01xWP3F0ZMUFFLorvZQPMR16i44Oaf2n4jlDtlYdOQ3Tcl4M-7iY5jGiRrlTX7wyKxferOuVNvwNp7v-yxU5xcyYzh65KVskEaJzrHM2nz1LbT7Nw-x7OnFD6DDGCTNqnplbad9D7Urv3a3SO5)  
  <sub>Barchart.com, 6 hours ago</sub>  
  AES Corporation has rallied other utility stocks, yet analysts remain skeptical about the stock's outlook.
- [State Street Utilities Select Sector SPDR ETF declares quarterly distribution of $0.3004](https://www.google.com/goto?url=CAESzwEB6zswFRfb8eFONEeCUyv7MCXQNtzJlsgfTxBuewnV-azdAQLnvgdwlaOMRT3WaXLYOi9yUTXkE8wIm9QuVazVIr3nJC2aZFPhL5g9XNzARBYKViQiETrJbzJla7etZyvfPOKOKovOD-6AkHczrE60f9F3JkakAD62F6yi30QL1SZ7xVlicSzHoMco_ANaTbo8JAUAks8EQd-KjOplGbMriF8PPdr-rmUfShOahZ7Jb51W579M6U_GRaMpzxMEvjPQUgSPJuGy4YRao2Owpbc)  
  <sub>TradingView, 21 hours ago</sub>  
  Content provided by Seeking Alpha is intended for information purposes only, and that Seeking Alpha does not offer any personalist investment advice and is...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 40.74 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 42.31 (-3.7%), 50d 43.62 (-6.6%), 200d 44.52 (-8.5%); 50d below 200d
Momentum: RSI(14) 29.7 | MACD -0.759 vs signal -0.614 (histogram -0.144)
Returns: 1d +0.2% | 5d -1.4% | 1m -4.8% | 3m -9.6%
52-week range: 40.66 - 47.73 (now 1.1% of the way up)
Volatility: ATR(14) 0.60 (1.5% of price) | annualised 20d 13.3%
Volume: 0.37x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.55</summary>

```text
Fund type: Utilities
What it holds: P/E 19.02 | P/B 2.14 | P/S 2.65 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +11.5% a year | beta to the market 0.43
Cost and size: expense ratio 0.08% | net assets 21.84B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: NextEra Energy Inc 13.0%, Southern Co 7.5%, Duke Energy Corp 7.1%, Constellation Energy Corp 6.7%, American Electric Power Co Inc 5.1%
Sector mix: Utilities 100.0%
```

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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 39.4% of the fund by weight
Ratings by weight: buy 80.9% | hold 19.1% | sell 0.0% (mean 2.06 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.9% above the current prices
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 163.27M | fund size: 6.65B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro catalyst in the window and no fund-relevant news. Price sits just below all three major moving averages with negative MACD and RSI near 39, but on light volume and within a 3-month range of roughly flat — drift, not a decisive break. Macro backdrop is mixed but not surprising: long yields slightly lower, dollar firmer (+0.93, a headwind for an Argentine equity basket), VIX calm at 14.4. Holdings analyst roll-up is strongly positive (100% buy weight, +31% weighted target) but covers only 51% of a fund that is 25% MercadoLibre, so it is as much a single-name read as a fund read. Flows direction unknown, so the behavioural dimension is unscored. Nothing here clears the bar for a directional macro call.

**Main reasons it gave:**
- Close 91.80 below 20d/50d/200d SMAs; MACD histogram -0.511, RSI 39.4
- Volume only 0.56x 20-day average — no conviction behind the drift
- Dollar index +0.93 on the week, a headwind for Argentine ADR basket
- Holdings roll-up 100% buy weight, +31.4% weighted target but only 51.1% coverage and 25% MELI concentration
- VIX 14.4 and no macro release or policy surprise in the window

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 91.80 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 94.86 (-3.2%), 50d 93.87 (-2.2%), 200d 92.72 (-1.0%); 50d above 200d
Momentum: RSI(14) 39.4 | MACD -0.267 vs signal 0.245 (histogram -0.511)
Returns: 1d -0.6% | 5d -2.9% | 1m -1.1% | 3m -0.8%
52-week range: 67.55 - 102.94 (now 68.5% of the way up)
Volatility: ATR(14) 1.79 (2.0% of price) | annualised 20d 16.0%
Volume: 0.56x the 20-day average
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
Three-year record: +27.9% a year | beta to the market 0.50
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 51.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.54 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +31.4% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, BMA
Recent rating changes among them:
  - MELI: 2026-09-03 BTIG: reit, Buy -> Buy
  - YPF: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-06-25 JP Morgan: main, Overweight -> Overweight
  - BMA: 2026-06-25 JP Morgan: main, Overweight -> Overweight
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 8.81M | fund size: 809.16M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Israel equity fund in a mild uptrend (above 20/50/200d, 50d>200d, RSI 55.6, MACD positive) but no macro catalyst this cycle: yields little changed, VIX calm at 14.4, curve normally sloped. Analyst roll-up is supportive (100% buy, +14.4% target) but covers only 37.6% of the fund and is concentrated in Teva and two banks. Volume at 0.23x average and a -1.4% day argue against reading the trend as decisive. Flows direction unknown. Default to NEUTRAL with a slight positive tilt.

**Main reasons it gave:**
- Price above 20d/50d/200d SMAs with 50d>200d and positive MACD histogram
- Volume only 0.23x 20-day average — weak conviction behind the move
- Analyst roll-up 100% buy, +14.4% weighted target, but only 37.6% coverage
- Macro quiet: 10y -4bp, VIX 14.4 (-2.8), curve +0.95 normal
- No fund or macro news in past 24 hours; flow direction unknown

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.30</summary>

```text
Last close 125.90 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 124.20 (+1.4%), 50d 122.27 (+3.0%), 200d 122.07 (+3.1%); 50d above 200d
Momentum: RSI(14) 55.6 | MACD 0.829 vs signal 0.637 (histogram 0.191)
Returns: 1d -1.4% | 5d +2.7% | 1m +2.5% | 3m +5.4%
52-week range: 94.16 - 137.69 (now 72.9% of the way up)
Volatility: ATR(14) 1.81 (1.4% of price) | annualised 20d 20.8%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.89 | P/B 2.43 | P/S 2.45 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +34.0% a year | beta to the market 1.07
Cost and size: expense ratio 0.59% | net assets 897.28M
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Teva Pharmaceutical Industries Ltd ADR 10.1%, Bank Leumi Le-Israel BM 9.0%, Bank Hapoalim BM 8.1%, Tower Semiconductor Ltd 5.5%, Elbit Systems Ltd 4.8%
Sector mix: Financial services 36.1%, Technology 18.1%, Healthcare 10.7%, Industrials 10.0%
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
Rolled up from the 5 largest holdings, 37.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.25 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.4% above the current prices
Holdings read: TEVA, LUMI.TA, POLI.TA, TSEM.TA, ESLT.TA
Recent rating changes among them:
  - TEVA: 2026-09-09 Leerink Partners: init, ? -> Outperform
  - TSEM.TA: 2026-09-18 Barclays: init, ? -> Overweight
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 2.55M | fund size: 321.05M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Strong uptrend near 52-week highs (+15.8% vs 200d, 50d above 200d) but momentum is flattening (MACD histogram negative, RSI 56.9, volume 0.27x average) and the weighted analyst price target sits slightly below current prices, implying the rally has run past consensus fair value. Macro is quiet: yields little changed, VIX calm at 14.4, but the dollar firmed +0.93 on the week, a mild headwind for an unhedged Polish equity fund, and the priced rate path points to hikes rather than cuts. No macro or policy surprise and no news this cycle, so no basis for a directional call. Valuation remains cheap (P/E 13.5, 3.3% yield), which keeps the medium-term tilt constructive without justifying a timing bet.

**Main reasons it gave:**
- Price at 96.9% of 52-week range, +17% in 3 months
- MACD histogram -0.060 with volume 0.27x 20-day average
- Weighted price target 2.3% below current price across 47.4% of fund
- Dollar index +0.93 on the week; 2-year at 4.76% prices hikes
- Holdings P/E 13.5 and 3.3% yield, VIX calm at 14.4

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.25</summary>

```text
Last close 45.33 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 44.73 (+1.3%), 50d 43.55 (+4.1%), 200d 39.13 (+15.8%); 50d above 200d
Momentum: RSI(14) 56.9 | MACD 0.437 vs signal 0.497 (histogram -0.060)
Returns: 1d -0.8% | 5d +1.0% | 1m +2.0% | 3m +17.0%
52-week range: 31.57 - 45.76 (now 96.9% of the way up)
Volatility: ATR(14) 0.66 (1.5% of price) | annualised 20d 20.3%
Volume: 0.27x the 20-day average
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
Three-year record: +42.9% a year | beta to the market 0.73
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

<details><summary><b>What analysts and big funds say</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.05</summary>

```text
Rolled up from the 5 largest holdings, 47.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.14 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -2.3% above the current prices
Holdings read: PKO.WA, PKN.WA, PEO.WA, PZU.WA, KGH.WA
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 19.09M | fund size: 865.05M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise this week: US yields little changed, VIX calm at 14.4, curve normally sloped. EWG is chopping below its 20d and 50d SMAs with negative MACD and RSI 42, but sits just above the 200d and up 3.8% over three months -- a drift, not a break, and volume is 0.16x average. Analyst roll-up on 45.5% of the fund is constructive (78% buy, +16% weighted target) and holdings valuation is unremarkable at 18.4x. The single news item, an ECB note on Chinese competition in German autos/machinery/capital goods, is a slow structural headwind rather than a datable catalyst, though it argues against leaning long into an industrials-heavy (28.7%) basket. A firmer dollar (+0.93) is a mild drag on unhedged euro exposure for USD holders. Net: stand aside.

**Main reasons it gave:**
- Price below 20d (-1.9%) and 50d (-1.1%) SMAs with MACD histogram -0.14 and RSI 42
- US 10y -4bp, VIX -2.8 to 14.4, curve +0.95 normal -- no rate or policy surprise
- Analyst roll-up over 45.5% of fund: 78% buy, weighted target +16.2%
- ECB flags Chinese competition squeezing German autos/machinery -- structural, not a catalyst
- Dollar index +0.93 on the week, a headwind for unhedged euro exposure
- Volume at 0.16x 20-day average -- no conviction behind the drift

<details><summary><b>News</b> — score -0.20</summary>

- [Germany faces two-front squeeze from Chinese factory strength, ECB says (DAX:NASDAQ)](https://seekingalpha.com/news/4645393-germany-faces-two-front-squeeze-from-chinese-factory-strength-ecb-says)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  ECB analysis: China's move up the value chain pressures Germany's autos, machinery and capital goods as China rivals exports and imports less from Europe.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 42.53 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 43.33 (-1.9%), 50d 43.01 (-1.1%), 200d 42.38 (+0.3%); 50d above 200d
Momentum: RSI(14) 42.3 | MACD -0.275 vs signal -0.135 (histogram -0.140)
Returns: 1d -0.2% | 5d +0.0% | 1m -3.8% | 3m +3.8%
52-week range: 38.08 - 44.59 (now 68.4% of the way up)
Volatility: ATR(14) 0.44 (1.0% of price) | annualised 20d 12.5%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.40 | P/B 1.94 | P/S 1.28 | 3y earnings growth n/a
Yield: 1.9%
Three-year record: +18.2% a year | beta to the market 0.98
Cost and size: expense ratio 0.49% | net assets 1.82B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Siemens AG 12.1%, SAP SE 11.3%, Allianz SE 10.0%, Siemens Energy AG Ordinary Shares 6.4%, Deutsche Telekom AG 5.6%
Sector mix: Industrials 28.7%, Financial services 23.2%, Technology 15.9%, Consumer cyclical 7.4%
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
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.85 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.2% above the current prices
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 79.50M | fund size: 3.38B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> EWW is drifting below all three major moving averages (-2.4% vs 20d, -2.8% vs 50d/200d) with negative MACD and RSI at 40.6, but volume is only 0.21x average and volatility is low, so there is no decisive break. Macro is mixed rather than surprising: a firmer dollar (+0.93 on the week) is a mild headwind for Mexican equities, and the 2-year at 4.76% vs a 4.00% Fed target prices hikes rather than cuts, but nothing moved sharply this week and VIX fell to 14.4. Holdings are cheap (P/E 12.7, 3.2% yield) and sell-side coverage on the top 47.6% of the fund is unanimously buy with +16.6% targets, which offsets the soft tape. No macro or data catalyst to justify a directional call; flow data is unavailable.

**Main reasons it gave:**
- Price below 20d/50d/200d SMAs with MACD histogram -0.267 and RSI 40.6
- Volume just 0.21x 20-day average — no conviction behind the drift
- Dollar index +0.93 on the week, a headwind for peso-denominated equities
- Holdings P/E 12.68 and 3.2% yield, cheap versus global peers
- Rolled-up analyst view on 47.6% of fund: 100% buy, +16.6% weighted target
- No macro release or policy surprise this week; VIX down to 14.4

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 73.75 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 75.59 (-2.4%), 50d 75.86 (-2.8%), 200d 75.69 (-2.6%); 50d above 200d
Momentum: RSI(14) 40.6 | MACD -0.715 vs signal -0.448 (histogram -0.267)
Returns: 1d +0.1% | 5d -0.4% | 1m -4.7% | 3m -1.3%
52-week range: 64.39 - 81.23 (now 55.6% of the way up)
Volatility: ATR(14) 1.23 (1.7% of price) | annualised 20d 15.1%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

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
Rolled up from the 5 largest holdings, 47.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.06 on a 1=strong buy to 5=strong sell scale)
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 18.90M | fund size: 1.39B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> EWY is in a strong uptrend (+24.8% vs 200d, 50d>200d, RSI 58.5, MACD positive) but the move is extended after +7.9% in five days with annualised 20d volatility of 45% and thin volume, and the fund is effectively a levered bet on two memory/semi names (SK hynix + Samsung = 46%). Macro is benign but not a catalyst: yields little changed, VIX down to 14.4, curve normal, though a firmer dollar (+0.93) and a priced Fed hiking path are headwinds for Korean equity. Valuation is cheap (P/E 10.4) but that is a slow-moving fact. No policy or data surprise this cycle, so no directional edge. Analyst roll-up carries no usable ratings or targets and flow direction is unknown, so both left null. News items are generic ETF-flow and regional roundups.

**Main reasons it gave:**
- Price +4.3% over 20d SMA and +24.8% over 200d, 50d above 200d
- 5-day return +7.9% on volume just 0.37x average — extended, low-conviction thrust
- Annualised 20d volatility 45%, beta 2.50, 46% of fund in SK hynix and Samsung
- Macro quiet: 10y -4bp, VIX 14.4 (-2.8), curve +0.95 normal; dollar +0.93 a mild EM headwind
- Holdings P/E 10.4 with no analyst ratings/targets available and unknown flow direction

<details><summary><b>News</b> — score +0.10</summary>

- [A Record ETF Year Takes Shape as Inflows Near $1.5 Trillion](https://finance.yahoo.com/markets/stocks/articles/record-etf-takes-shape-inflows-210017196.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  US-listed ETFs took in $91.9 billion last week, pushing 2026 inflows to about $1.47 trillion, nearly matching last year's record with three months to spare.
- [Asian stocks mostly rise on tech rally, lower yields, and US-China trade hopes](https://seekingalpha.com/news/4645224-asian-stocks-mostly-rise-on-tech-rally-lower-yields-and-us-china-trade-hopes)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  Asian stock markets delivered a mixed performance on Tuesday, picking up momentum from overnight gains on Wall Street. A fresh rally in technology shares...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.35</summary>

```text
Last close 190.43 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 182.52 (+4.3%), 50d 173.96 (+9.5%), 200d 152.57 (+24.8%); 50d above 200d
Momentum: RSI(14) 58.5 | MACD 2.541 vs signal 2.230 (histogram 0.312)
Returns: 1d +0.7% | 5d +7.9% | 1m +6.8% | 3m -0.9%
52-week range: 78.87 - 219.20 (now 79.5% of the way up)
Volatility: ATR(14) 6.59 (3.5% of price) | annualised 20d 45.2%
Volume: 0.37x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.41 | P/B 1.83 | P/S 1.70 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +45.5% a year | beta to the market 2.50
Cost and size: expense ratio 0.59% | net assets 27.72B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: SK hynix Inc 23.7%, Samsung Electronics Co Ltd 22.2%, SK Square 2.9%, Samsung Electro-Mechanics Co Ltd 2.7%, KB Financial Group Inc 2.0%
Sector mix: Technology 54.6%, Industrials 17.0%, Financial services 11.1%, Consumer cyclical 5.1%
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 152.34M | fund size: 29.01B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise this cycle: US yields little changed, VIX calm at 14.4, curve normally sloped. The offsetting facts are a firmer dollar (+0.93 on the week) and a 2-year pricing a hiking path, both mild headwinds for Brazilian equities, versus solid momentum (1m +7.9%, above all key SMAs) and cheap holdings (P/E 10.5, 4.1% yield, +23.7% weighted target upside). MACD histogram has just rolled negative on very light volume (0.27x) and the 50d remains below the 200d, so the breakout is not decisive. Analyst roll-up covers only 41% of the fund and includes a downgrade of NU. No news and no flow direction available. NEUTRAL with a slight constructive tilt.

**Main reasons it gave:**
- Dollar index +0.93 on the week, a headwind for Brazil equity in USD terms
- VIX 14.4, down 2.8, and 10y yield -4bp: no rate or policy surprise
- Price +7.9% 1m and above 20/50/200d SMAs, but 50d still below 200d and MACD histogram negative
- Volume 0.27x 20-day average, weak confirmation of the move
- Holdings P/E 10.5, 4.1% yield, weighted analyst target +23.7% but only 41% coverage

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.25</summary>

```text
Last close 37.85 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 37.36 (+1.3%), 50d 36.13 (+4.7%), 200d 36.22 (+4.5%); 50d below 200d
Momentum: RSI(14) 58.6 | MACD 0.614 vs signal 0.660 (histogram -0.045)
Returns: 1d -0.6% | 5d +0.2% | 1m +7.9% | 3m +10.8%
52-week range: 28.79 - 41.73 (now 70.0% of the way up)
Volatility: ATR(14) 0.77 (2.0% of price) | annualised 20d 22.3%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.48 | P/B 1.79 | P/S 1.28 | 3y earnings growth n/a
Yield: 4.1%
Three-year record: +11.5% a year | beta to the market 0.84
Cost and size: expense ratio 0.59% | net assets 8.17B
What it is made of: Stocks 96.5%, Cash 2.7%, Preferred 0.8%
Largest holdings: Vale SA 10.1%, Nu Holdings Ltd Ordinary Shares Class A 9.5%, Itau Unibanco Holding SA Participating Preferred 7.7%, Petroleo Brasileiro SA Petrobras Participating Preferred 7.0%, Petroleo Brasileiro SA Petrobras 6.6%
Sector mix: Financial services 34.1%, Energy 17.4%, Basic materials 14.5%, Utilities 12.4%
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 40.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.7% above the current prices
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 200.55M | fund size: 7.59B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No fresh macro catalyst: yields essentially flat to slightly lower at the long end, VIX calm at 14.4, and the dollar firmer on the week (+0.93) — a mild headwind for gold miners. Technicals are mixed: still +7.8% over the 50d and +5.4% over the 200d after a +23% quarter, but price is below the 20d SMA, MACD histogram is negative, RSI is mid-range, 1m return -6.9%, and volume is only 0.26x average, so the bounce lacks conviction. Fund basics are supportive (P/E 12.8, 100% buy ratings across the top 40% of weight, +9.7% weighted target) but those are slow-moving and already reflect a big run. Record Chinese gold imports are a genuine demand datum, offset by the dollar and a priced hiking path (2y 4.76% vs 4.00% target). Nothing here clears the bar for a directional macro timing call. Flow direction unavailable, so no behavioural read.

**Main reasons it gave:**
- Dollar index +0.93 on the week, gold snapped three-session win streak
- Price -2.2% vs 20d SMA with MACD histogram -0.984 and 1m return -6.9%
- Volume only 0.26x 20-day average on the bounce
- Top-5 holdings 100% buy by weight, +9.7% weighted price target (39.9% coverage)
- VIX 14.4 and flat-to-lower long yields — no rate or policy surprise this week

<details><summary><b>News</b> — score +0.05</summary>

- [China's gold imports surpass 1,000-ton mark on strong domestic demand](https://seekingalpha.com/news/4645254-china-gold-imports-surpass-1000-ton-mark-on-strong-domestic-demand)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Chinese gold imports reached record highs this year, bolstered by a retreat in international bullion prices and a strengthening yuan.
- [‘The Sell Button Won’t Work’: Why Rate Hikes No Longer Save Debt Markets](https://www.benzinga.com/markets/bonds/26/09/61916030/the-sell-button-wont-work-why-rate-hikes-no-longer-save-debt-markets)  
  <sub>Benzinga, 3 hours ago</sub>  
  Forget Fed rate hikes: Macro analysts reveal why fiscal dominance and massive deficits make gold and real assets the ultimate hedges.
- [Nasdaq 100 Rallies, Intel Soars 14%: Stock Market Today](https://www.tradingview.com/news/benzinga:0886239d6094b:0-nasdaq-100-rallies-intel-soars-14-stock-market-today/)  
  <sub>TradingView, 21 hours ago</sub>  
  U.S. equities extended their winning streak to a third session Monday, with a fourth consecutive slide in crude oil relieving pressure on Treasury yields...
- [Gold snaps three-session win streak as dollar rises, oil prices fall (GLD:NYSEARCA)](https://seekingalpha.com/news/4645199-gold-snaps-three-session-win-streak-as-dollar-rises-oil-prices-fall)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Gold futures turned lower, snapping a three-session winning streak, as the market returned its focus to US yields and the Federal Reserve's interest rate...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.05</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 95.71 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 97.82 (-2.2%), 50d 88.80 (+7.8%), 200d 90.81 (+5.4%); 50d below 200d
Momentum: RSI(14) 52.0 | MACD 0.986 vs signal 1.970 (histogram -0.984)
Returns: 1d +1.4% | 5d +1.7% | 1m -6.9% | 3m +23.2%
52-week range: 68.28 - 115.84 (now 57.7% of the way up)
Volatility: ATR(14) 3.25 (3.4% of price) | annualised 20d 38.9%
Volume: 0.26x the 20-day average
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
Three-year record: +49.2% a year | beta to the market 0.83
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.7% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, AU
Recent rating changes among them:
  - NEM: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - AEM.TO: 2026-09-16 RBC Capital: main, Sector Perform -> Sector Perform
  - ABX.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - WPM.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 319.25M | fund size: 30.56B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Uptrend intact (50d>200d, +21% 3m) but momentum is fading — MACD histogram negative, RSI mid-range, volume just 0.38x average, and annualised 20d vol of 42.7% is high for a calm-VIX tape. Macro gives no surprise: yields little changed, curve normally sloped, VIX down to 14.4, though a 2-year at 4.76% versus a 4.00% target implies a tightening path that is unhelpful for a P/E 34 growth basket, and the dollar firmed. News is stock-level noise (BlackBerry design win, Cramer call, listicles) rather than sector macro; one item is an ETF promotion piece and carries no weight. Analyst roll-up is constructive but covers only 43% of the fund and 100% buy weight is more a fact about coverage bias than about upside. No catalyst to justify a side.

**Main reasons it gave:**
- MACD below signal (histogram -0.120) with RSI 54.8 — momentum cooling after +21.4% 3m run
- Volume 0.38x 20-day average; 20d annualised vol 42.7% despite VIX 14.4
- Yields nearly unchanged on the week, curve +0.95 normal — no rate surprise
- 2-year 4.76% vs 4.00% Fed target prices further hikes, a headwind to P/E 34.2 holdings
- Analyst roll-up 100% buy but only 43.2% of fund covered, +9.4% weighted target
- News flow is single-name (BB, ORCL) and ETF-promotion, not sector macro

<details><summary><b>News</b> — score +0.10</summary>

- [BlackBerry Jumps 7% as Coretura Selects QNX-Based Alloy Kore for Truck Platform; Aptiv Edges Higher, Mobileye Barely Budges](https://247wallst.com/investing/2026/09/22/blackberry-jumps-7-as-coretura-selects-qnx-based-alloy-kore-for-truck-platform-aptiv-edges-higher-mobileye-barely-budges/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Coretura just handed BlackBerry its first named design win for Alloy Kore, sending shares surging well past the broader software sector, but the deal comes...
- [AI Is Reshaping SaaS—These 2 Software ETFs Offer Different Ways to Play It](https://www.marketbeat.com/articles/ai-is-reshaping-saasthese-2-software-etfs-offer-different-ways-to-play-it/)  
  <sub>MarketBeat, 23 hours ago</sub>  
  Salesforce's expanded OpenAI partnership highlights AI's impact on SaaS, boosting interest in software ETFs IGV and WCLD, which have rallied but differ in...
- [Buy These 4 Cybersecurity Stocks, Skip These 2: Josh Brown Names Names](https://www.tradingview.com/news/benzinga:be089c112094b:0)  
  <sub>TradingView, 22 hours ago</sub>  
  Ritholtz Wealth Management CEO Josh Brown and colleague Sean Russo used their latest “The Best Stocks in the Market” column at CNBC to stake out a clear...
- [BlackBerry Climbs 5% on Cramer Buy Call Ahead of Earnings; Aptiv Inches Higher, Mobileye Sits Tight](https://247wallst.com/investing/2026/09/21/blackberry-climbs-5-on-cramer-buy-call-ahead-of-earnings-aptiv-inches-higher-mobileye-sits-tight/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  A Cramer lightning-round call just sent BlackBerry shares surging ahead of a quarterly report that could either validate the QNX software story or unwind...
- [Oracle Stock Tops S&P 500 Winners Today: PLTR, CRM, PANW Also Rally As Analyst Sees ‘Anthropic Fear Trade’ Unwinding](https://stocktwits.com/news-articles/markets/equity/oracle-stock-tops-s-and-p-500-winners-today-pltr-crm-panw-also-rally-as-analyst-sees-anthropic-fear-trade-unwinding/cZJpAS8RIHT)  
  <sub>Stocktwits, 7 hours ago</sub>  
  Shares of software companies appear to be rebounding from record lows, with analysts projecting the upward swing could be sustained.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.15</summary>

```text
Last close 105.98 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 105.14 (+0.8%), 50d 100.57 (+5.4%), 200d 93.68 (+13.1%); 50d above 200d
Momentum: RSI(14) 54.8 | MACD 1.193 vs signal 1.313 (histogram -0.120)
Returns: 1d -1.1% | 5d +0.4% | 1m +2.5% | 3m +21.4%
52-week range: 74.67 - 117.79 (now 72.6% of the way up)
Volatility: ATR(14) 2.74 (2.6% of price) | annualised 20d 42.7%
Volume: 0.38x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

```text
Fund type: Technology
What it holds: P/E 34.20 | P/B 8.09 | P/S 9.07 | 3y earnings growth n/a
Yield: 0.0%
Three-year record: +14.0% a year | beta to the market 1.21
Cost and size: expense ratio 0.38% | net assets 15.74B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Palantir Technologies Inc Ordinary Shares - Class A 10.3%, Palo Alto Networks Inc 9.7%, Microsoft Corp 9.2%, CrowdStrike Holdings Inc Class A 7.4%, Salesforce Inc 6.6%
Sector mix: Technology 94.4%, Communication services 3.8%, Financial services 1.5%, Consumer cyclical 0.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 43.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.4% above the current prices
Holdings read: PLTR, PANW, MSFT, CRWD, CRM
Recent rating changes among them:
  - PLTR: 2026-09-15 UBS: main, Buy -> Buy
  - PANW: 2026-09-21 Morgan Stanley: main, Overweight -> Overweight
  - MSFT: 2026-09-21 Cantor Fitzgerald: main, Overweight -> Overweight
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 12.50M | fund size: 1.32B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Transports are in a clear short-term downtrend (-8.2% in a month, below 20/50d SMAs, MACD negative) but RSI 30 is oversold near the 200d and volume is light, so this looks like a drawdown rather than a confirmed break. Macro is mixed-to-restrictive: 2y at 4.76% prices hikes rather than cuts, inflation still 3.4%, dollar firming -- unhelpful for a cyclical, high-beta (1.28) basket -- but VIX fell to 14.4 and the curve is normally sloped, so no shock. Analyst roll-up on 53% of the fund is genuinely constructive (91% buy, +27% targets, UNP upgrade). Only news item is a third-party Hold rating on a different transport ETF, opinion not data. No macro surprise this cycle; default NEUTRAL.

**Main reasons it gave:**
- Price 6.6% below 50d SMA with negative MACD but RSI 30.3 oversold near 200d SMA
- Volume 0.23x 20-day average -- no conviction behind the decline
- 2-year at 4.76% vs 4.00% Fed target prices tightening, inflation still 3.4%
- Analyst roll-up over 53% of fund: 91% buy, +26.6% weighted target, UNP upgraded by UBS
- VIX 14.42 and -2.8 on week; normal +0.95 curve -- no macro shock

<details><summary><b>News</b> — score -0.10</summary>

- [XTN: Transportation Likely To Lag Into 2027 Amid Macro Pressures And Factor Weaknesses](https://seekingalpha.com/article/4948496-xtn-transportation-likely-to-lag-into-2027-given-macro-pressures-factor-weaknesses)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  Summary. I initiate coverage of the State Street SPDR S&P Transportation ETF with a Hold rating. I believe XTN will underperform IVV into 2027 as higher...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 79.90 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 83.04 (-3.8%), 50d 85.53 (-6.6%), 200d 81.13 (-1.5%); 50d above 200d
Momentum: RSI(14) 30.3 | MACD -1.634 vs signal -1.364 (histogram -0.270)
Returns: 1d +0.1% | 5d -2.3% | 1m -8.2% | 3m -4.8%
52-week range: 68.14 - 90.01 (now 53.8% of the way up)
Volatility: ATR(14) 1.26 (1.6% of price) | annualised 20d 15.8%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.05</summary>

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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 27.47M | fund size: 2.19B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise this cycle: US yields little changed, VIX calm at 14.4, curve normally sloped. MCHI sits mid-range technically — above the 20d but below the 50d and 5.3% under a declining 200d, with 50d<200d and volume at a third of average, so no decisive break. Valuation is cheap (P/E 11.9, P/B 1.39) and sell-side targets on the top five holdings imply +48%, but that roll-up covers only 32% of the fund and analyst targets on Chinese megacaps are chronically optimistic. The lone news item is single-holding Alibaba chatter, not a macro driver. A firmer dollar (+0.93 on the week) is a mild headwind for EM equity. Flows direction unknown, so no behavioural read.

**Main reasons it gave:**
- 50d SMA below 200d, price 5.3% under 200d, only 22% of 52-week range
- VIX 14.4 and 10y -4bp on the week — no rate or policy surprise
- Holdings P/E 11.9 / P/B 1.39 with 2.0% yield
- Analyst roll-up +47.7% target but covers only 32.2% of fund by weight
- Volume 0.34x 20-day average — no conviction behind recent move

<details><summary><b>News</b> — score +0.05</summary>

- [Alibaba stock forms a bullish pattern as it unveils new advanced AI chip](https://invezz.com/au/news/2026/09/22/alibaba-stock-forms-a-bullish-pattern-as-it-unveils-new-advanced-ai-chip/)  
  <sub>Invezz, 7 hours ago</sub>  
  Alibaba stock jumped by 3% on Tuesday in Hong Kong as investors reacted to news from its Apsara Conference in Hangzhou. BABA jumped to $118.5,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.05</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.05</summary>

```text
Last close 54.15 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 53.94 (+0.4%), 50d 54.50 (-0.6%), 200d 57.18 (-5.3%); 50d below 200d
Momentum: RSI(14) 51.7 | MACD -0.383 vs signal -0.408 (histogram 0.025)
Returns: 1d +0.3% | 5d +2.4% | 1m -2.7% | 3m +4.5%
52-week range: 50.48 - 66.99 (now 22.3% of the way up)
Volatility: ATR(14) 0.61 (1.1% of price) | annualised 20d 14.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 32.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +47.7% above the current prices
Holdings read: 0700.HK, 9988.HK, 00939, 01398, 1810.HK
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 119.03M | fund size: 6.45B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> XBI sits near 52-week highs with a positive longer trend (50d>200d, +17.8% vs 200d) and a strong 5-day pop, but MACD has rolled negative, volume is only 0.45x average and the 1-month return is negative -- no decisive break. Macro is quiet: yields little changed, curve normal, VIX 14.4 and falling, though the 2-year prices hikes rather than cuts, which is a mild headwind for long-duration biotech. News flow is sector-supportive (record $106B biopharma M&A, positive NTLA Phase 3) but headlines about single constituents and a Cathie Wood listicle are not a fund thesis. Analyst roll-up covers only 9% of the fund and shows a negative weighted target with an MRNA downgrade -- a fact about that slice. Flow direction unknown. No macro catalyst, so NEUTRAL.

**Main reasons it gave:**
- MACD below signal (-0.397 histogram) while price sits 89.7% up the 52-week range on 0.45x volume
- Longer-term uptrend intact: 50d above 200d, +17.8% vs 200d SMA
- Biopharma M&A at $106B across 201 deals, strongest pace in years
- 2-year at 4.76% vs 4.00% Fed target prices hikes, a headwind for long-duration biotech
- Analyst roll-up covers only 9% of fund weight and shows -18.3% weighted target plus an MRNA downgrade to Sell

<details><summary><b>News</b> — score +0.20</summary>

- [Cathie Wood Loads Up On Biotech: 5 ETFs Holding Her Latest Bets](https://www.benzinga.com/etfs/sector-etfs/26/09/61923369/cathie-wood-loads-up-on-biotech-5-etfs-holding-her-latest-bets)  
  <sub>Benzinga, 37 minutes ago</sub>  
  Cathie Wood's ARKG bought Ionis, Beam, Veracyte and Scribe Therapeutics. Here are the biotech ETFs that also hold her latest bets.
- [Gilead, Merck, Eli Lilly Lead $106B Biopharma Takeover Wave In 2026](https://stocktwits.com/news-articles/markets/equity/gilead-merck-eli-lilly-lead-106-billion-takeover-wave-in-2026/cZ0FblYRezX)  
  <sub>Stocktwits, 12 hours ago</sub>  
  Biopharma M&A has surged to $106 billion across 201 deals through early June 2026, putting the sector on track for its strongest full-year total since the...
- [Moderna To Present Additional Data From Key Melanoma Trial At ESMO Congress – Retail Says ‘Breakout Is Getting Hard To Ignore’](https://stocktwits.com/news-articles/markets/equity/moderna-to-present-additional-data-from-key-melanoma-trial-at-esmo-congress-mrna-stock-rises/cZMRFFZRBIL)  
  <sub>Stocktwits, 22 hours ago</sub>  
  Moderna will showcase detailed melanoma results for Intismeran at ESMO, alongside data and trial updates exploring the personalized therapy in pancreatic...
- [CRWD, PANW Stocks Extend AI-Fueled Rally As Cybersecurity Bets Outpace Software](https://www.google.com/goto?url=CAESxwEB6zswFdnW_GY7H504XGimXPyO8Nhjh9LstNo6Yccd0X3GdZIJyHov1BNiH006QgR8GR7Aafv6ZF31xoBgTWU9ol4_MB9gA77qb6Ue-CLkZFyk1K5Q979zo-yPJFg2ofnaDqB3jNuoiR0hkuN6tQCXd3pwEoJt60dGTJux4e5TJHdwtSVSAa0a1PAcawRGgV-oMjLGywasf1_mHjdHDKdm5STMysrwTutgoSFp5miGYiiojskdNoFhI7FMB74B4hJtOxEKOdF-)  
  <sub>Stocktwits, 8 hours ago</sub>  
  CRWD and PANW extended gains as investors weighed AI-driven cyber threats against slower frontier-model development. Cybersecurity executives have...
- [NTLA Jumps Premarket On Positive Late-Stage Trial Data For Gene-Editing Therapy — Retail Says Buy Now Before It’s Too Late](https://stocktwits.com/news-articles/markets/equity/ntla-stock-soars-intellia-positive-gene-therapy-trial/cZBNFouRe2C)  
  <sub>Stocktwits, 8 hours ago</sub>  
  Intellia Therapeutics stated that its Phase 3 trial of lonvoguran ziclumeran met the primary and secondary endpoints, with favorable safety and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.10</summary>

```text
Last close 161.96 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 161.14 (+0.5%), 50d 157.68 (+2.7%), 200d 137.51 (+17.8%); 50d above 200d
Momentum: RSI(14) 54.9 | MACD -0.356 vs signal 0.041 (histogram -0.397)
Returns: 1d +2.4% | 5d +5.1% | 1m -2.3% | 3m +10.2%
52-week range: 95.86 - 169.55 (now 89.7% of the way up)
Volatility: ATR(14) 3.98 (2.5% of price) | annualised 20d 25.8%
Volume: 0.45x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.05</summary>

```text
Fund type: Health
What it holds: P/E n/a | P/B 0.20 | P/S 0.12 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +27.6% a year | beta to the market 1.12
Cost and size: expense ratio 0.35% | net assets 11.40B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Moderna Inc 2.8%, Twist Bioscience Corp 1.9%, Apogee Therapeutics Inc 1.5%, Kymera Therapeutics Inc Ordinary Shares 1.4%, Halozyme Therapeutics Inc 1.4%
Sector mix: Healthcare 99.3%, Financial services 0.7%
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

<details><summary><b>What analysts and big funds say</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.20</summary>

```text
Rolled up from the 5 largest holdings, 9.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 52.0% | hold 48.0% | sell 0.0% (mean 2.18 on a 1=strong buy to 5=strong sell scale)
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 72.77M | fund size: 11.79B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro or policy surprise this week: yields broadly flat to slightly lower at the long end, VIX calm at 14.4, curve normally sloped. XLV sits above its 20/50/200d averages with a 3-month gain of 12%, but momentum is fading (MACD below signal, 1-month -2.4%) on light volume, so the technical picture is mixed rather than decisive. Holdings analyst roll-up is uniformly Buy with ~9.5% upside but covers only 44% of the fund and is slow-moving. News is a distribution notice and sector roundups -- noise. Defensive healthcare with beta 0.52 and P/E 30 offers no edge either way this cycle.

**Main reasons it gave:**
- VIX 14.4, -2.8 on the week; no rate or policy surprise (10y -4bp, Fed target 4.00%)
- Price above 20/50/200d SMAs, 50d>200d, +12% 3m
- MACD histogram -0.203 and 1-month return -2.4% on 0.47x volume
- Holdings roll-up 100% buy, +9.5% weighted target, but only 44.3% coverage
- News limited to distribution announcement and sector listicles

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Health Care Select Sector SPDR ETF declares quarterly distribution of $0.6422](https://www.tradingview.com/news/seekingalpha:121fd3c5b094b:0-state-street-health-care-select-sector-spdr-etf-declares-quarterly-distribution-of-0-6422/)  
  <sub>TradingView, 21 hours ago</sub>  
  Content provided by Seeking Alpha is intended for information purposes only, and that Seeking Alpha does not offer any personalist investment advice and is...
- [Leading And Lagging Sectors For September 22, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61919139/leading-and-lagging-sectors-september-22-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLB) State Street Materials Select Sector SPDR ETF 49.9500 0.240 0.48 2.2K (NYSE:XLP) State...
- [The Strange Pair That Led the Market Higher](https://moneyandmarkets.com/the-strange-pair-that-led-the-market-higher/)  
  <sub>Money & Markets, 14 hours ago</sub>  
  Only two sectors finished higher last week, and the unusual pairing tells us plenty about where investors are finding safety...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.10</summary>

```text
Last close 170.39 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 169.80 (+0.3%), 50d 167.10 (+2.0%), 200d 156.07 (+9.2%); 50d above 200d
Momentum: RSI(14) 55.8 | MACD 0.182 vs signal 0.385 (histogram -0.203)
Returns: 1d +0.8% | 5d +1.6% | 1m -2.4% | 3m +12.0%
52-week range: 134.13 - 175.68 (now 87.3% of the way up)
Volatility: ATR(14) 2.34 (1.4% of price) | annualised 20d 13.9%
Volume: 0.47x the 20-day average
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
Three-year record: +10.3% a year | beta to the market 0.52
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.5% above the current prices
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 260.63M | fund size: 44.41B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Staples ETF Widens Gap Over Discretionary in 2026](https://www.etftrends.com/sector-investing-content-hub/staples-etf-widens-gap-over-discretionary-in-2026/)  
  <sub>ETF Trends, 3 hours ago</sub>  
  State Street's staples ETF is outpacing its discretionary counterpart by more than 13 percentage points as household budgets tighten.
- [State Street Consumer Disc Sel Sect SPDR ETF declares quarterly distribution of $0.2441](https://www.google.com/goto?url=CAESzgEB6zswFbbq6iW76TROV3RzzwxXoj33MEadlnOT6rONLHfPQeD_lidClrtXWivjSqJyixZtEuj8icNhNfQ3rC2PrKoQmv9qY2XkBEL-_pwwcHeI5lq00YB3Qt88QeiluBXOrBXzw82MX_TPTV0BWTyZbq38atiQ64dEjRtybvCHbAY6BZpsWUgGzYynGn61cRgt4xGljU4N-4HKoeFHGq8mrfc3urjSH7bcNLXOylsrVVQWZjIK_FujDWbaMfD1j5D392miL_bUOoI65kpArQ)  
  <sub>TradingView, 21 hours ago</sub>  
  Content provided by Seeking Alpha is intended for information purposes only, and that Seeking Alpha does not offer any personalist investment advice and is...
- [Darden Restaurants Stock: Is DRI Outperforming the Consumer Discretionary Sector?](https://www.google.com/goto?url=CAESowEB6zswFbGHiUtxviq7zJhYlNW4Pz9MygTQBE2cZL7mIptcQhHH2URMIfiV5EWcq2s_65KmiVbtyyb-9D8mVUE43gX0XDkZK5Zg8Udxq4OM9JKHuLp_3QvK6yjBPudN1-hzdNUucD07uiTzczF-xzZxxAFKR6_s4EOZEYucXnfgzTY1Xa0_1XjRG06-ajf-qMk6fil2_jIcw29foqbjBSRXcGWs)  
  <sub>Yahoo Finance, 13 hours ago</sub>  
  Darden Restaurants, Inc. (DRI), headquartered in Orlando, Florida, is one of the largest full-service restaurant operators in the United States.
- [On Holding Surges 13% as Investor Day Sets Ambitious Sales Target and $1B Buyback; Nike Ticks Up 2%](https://247wallst.com/investing/2026/09/22/on-holding-surges-13-as-investor-day-sets-ambitious-sales-target-and-1b-buyback-nike-ticks-up-2/)  
  <sub>24/7 Wall St., 1 hour ago</sub>  
  On Holding just did something it has never done before, and the stock is repricing fast. Whether today's surge marks a turning point or a trap depends on...
- [Leading And Lagging Sectors For September 22, 2026](https://www.google.com/goto?url=CAESngEB6zswFX-UO7GmFih5RXGg8-I0wOunQPZ1MBi9HIdhFejgPclo4i0JscxRV6ouODGODeNQ9WN_vb_W2NnGaf6JmJBZI0z9rBVaxpclrvE17jaAoRDEE8MKU9ejFO0fMyw_Of_jHOGXxg89USKaMb23uM3nCIcYwAOKGNT6cQ2y6u-7CqROeKLQDUFGB_2y7d8QSBF5rdNWm20oGkaZbQ)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLB) State Street Materials Select Sector SPDR ETF 49.9500 0.240 0.48 2.2K (NYSE:XLP) State...
- [Two new option listings and eight option delistings on September 21st](https://www.tipranks.com/news/the-fly/two-new-option-listings-and-eight-option-delistings-on-september-21st-thefly-news?mod=mw_quote_news)  
  <sub>TipRanks, 22 hours ago</sub>  
  New option listings for September 21st include Surrozen Inc (SRZN) and Standard Nuclear Inc (STDN). Option delistings effective September 21st include...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 112.16 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 113.88 (-1.5%), 50d 115.19 (-2.6%), 200d 116.78 (-4.0%); 50d below 200d
Momentum: RSI(14) 42.9 | MACD -1.358 vs signal -1.186 (histogram -0.173)
Returns: 1d -0.1% | 5d +1.2% | 1m -5.0% | 3m -1.4%
52-week range: 105.66 - 124.52 (now 34.5% of the way up)
Volatility: ATR(14) 1.59 (1.4% of price) | annualised 20d 15.5%
Volume: 0.48x the 20-day average
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
Three-year record: +10.2% a year | beta to the market 1.16
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
Weighted price target: +22.1% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, BKNG
Recent rating changes among them:
  - AMZN: 2026-09-03 Wells Fargo: main, Overweight -> Overweight
  - TSLA: 2026-09-16 Goldman Sachs: reit, Neutral -> Neutral
  - HD: 2026-09-09 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-09-21 UBS: main, Buy -> Buy
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

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 204.84M | fund size: 22.97B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Oil (USO) · Commodity — BEARISH, confidence 0.40

**Result:** ERROR · BrokerError: submit_order failed for USO: {"code":42210000,"message":"only day orders are allowed for hard-to-borrow asset \"USO\""}

**In the model's own words:**

> Geopolitical risk premium is deflating: crude has fallen five straight sessions (-9.3% on the week) on reports Iran may reopen the Strait of Hormuz, and speculative positioning sits at the 98th percentile of the past year -- a crowded long unwinding into good news is the classic setup for further downside. EIA's official outlook sees WTI falling ~10% over six months toward $79, far below spot, and product inventories built last week even as crude drew marginally. Technicals are still in an uptrend (50d>200d, +31% over 3 months) which caps conviction, but MACD has crossed below signal, RSI has cooled to 54, and volatility is high (44% annualised). Macro is not a driver here: curve normal, VIX calm, though a firmer dollar (+0.93) is a mild headwind for crude. News items promoting specific microcaps or leveraged ETFs are noise and were disregarded.

**Main reasons it gave:**
- Fifth consecutive down session on reported Iranian offer to reopen Strait of Hormuz within 7 days
- CFTC spec net long at 98th percentile of 52 weeks, slightly reduced on the week -- crowded long
- EIA STEO forecasts WTI $88 now to $79 in six months, $70 average 2027, well below spot
- MACD below signal (histogram -0.671) and RSI 54 despite price 84% up the 52-week range
- Petrol +0.8mb and diesel +1.6mb builds against only a 0.6mb crude draw

<details><summary><b>News</b> — score -0.40</summary>

- [Oil Slid, Sending Energy ETFs Lower Before The Open](https://finimize.com/content/oil-slid-sending-energy-etfs-lower-before-the-open)  
  <sub>Finimize, 2 hours ago</sub>  
  WTI fell to $93.51 a barrel and Brent to $98.50, while TotalEnergies signed an MOU with Venezuela's PDVSA and Solaris lined up $1 billion of notes due 2032.
- [U.S. retail diesel prices hit record above $6.50 as momentum grows for export ban (USO:NYSEARCA)](https://seekingalpha.com/news/4645215-us-retail-diesel-prices-hit-record-above-650-as-momentum-grows-for-export-ban)  
  <sub>Seeking Alpha, 15 hours ago</sub>  
  Calls for a US ban diesel exports are gaining momentum as the national average retail price of diesel hit $6.51/gal, the highest on record.
- [Oil ETFs Surge: What's Next for Commodity Investors?](https://www.zacks.com/stock/news/2993265/oil-etfs-surge-whats-next-for-commodity-investors)  
  <sub>Zacks Investment Research, 18 hours ago</sub>  
  What's next for oil, gold and copper as geopolitical risks reshape commodity markets?
- [Capital Flows in US Equities and Insights into the Derivatives Market Amid Accumulating Macro Risks: The Interplay Between Hedge Fund De-leveraging and Long-Term Capital Inflows](https://news.futunn.com/en/post/79600148/capital-flows-in-us-equities-and-insights-into-the-derivatives)  
  <sub>富途牛牛, 12 hours ago</sub>  
  MainpointsAccumulating macro risks have prompted hedge funds to reduce their equity holdings, but robust long-term inflows have provided support.
- [Crude Slips After Iran Reportedly Offers To Reopen Strait Of Hormuz Within 7 Days — USO, SCO In Spotlight](https://stocktwits.com/news-articles/markets/equity/crude-slips-after-iran-reportedly-offers-to-reopen-strait-of-hormuz-within-7-days-uso-sco-in-spotlight/cZMPZ6TRBeN)  
  <sub>Stocktwits, 11 hours ago</sub>  
  Crude oil prices slipped Tuesday after Iran reportedly offered to reopen the Strait of Hormuz within seven days if the U.S. takes initial steps toward...
- [Stocks Jump On Iran, China, and Bitcoin Hopium—But The Big Conflicts Have Not Gone Away](https://www.benzinga.com/Opinion/26/09/61906130/stocks-jump-on-iran-china-and-bitcoin-hopium-but-the-big-conflicts-have-not-gone-away)  
  <sub>Benzinga, 21 hours ago</sub>  
  Buying On Hopium Please click here for an enlarged chart of Direxion Daily Semiconductor Bull 3X ETF (NYSE:SOXL). Note the following: Semiconductors reflect...
- [Oil prices extend slide as Iran reportedly offers to open Strait of Hormuz in seven days](https://seekingalpha.com/news/4645441-oil-prices-extend-slide-as-iran-reportedly-offers-to-open-strait-of-hormuz-in-seven-days)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Crude oil futures fell for a fifth consecutive session following reports of a conditional Iranian offer to reopen the Strait of Hormuz within seven days if...
- [Wall Street's Biggest Bull Turns Cautious Even As S&P 500 Tops 7,600: Yardeni Warns Oil, Fed And Mega IPOs Could Shake Up Record Rally](https://stocktwits.com/news-articles/markets/equity/ed-yardeni-warns-oil-fed-mega-ipos-share-up-record-sp-500-rally/cZ0j4xDRexs)  
  <sub>Stocktwits, 6 hours ago</sub>  
  Ed Yardeni, president of Yardeni Research and one of Wall Street's most bullish strategists, is growing more cautious about the stock market's near-term...
- [Dow Soars Over 750 Points, Hits Record High As Investors Look Beyond Tech Stocks — PCE Inflation Comes In Hottest Since October 2023](https://stocktwits.com/news-articles/markets/equity/dow-soars-hits-record-high-pce-report-may-2026/cZ1GmZ6R7Xa)  
  <sub>Stocktwits, 15 hours ago</sub>  
  U.S. equities were mixed in Thursday morning's trade as investors looked beyond the tech trade, with healthcare and industrial goods stocks helping lift the...
- [BATL, TPET, SKYQ, INDO Stocks Surge Premarket: Oil Prices Spike On Renewed US-Iran Hostilities](https://stocktwits.com/news-articles/markets/equity/batl-tpet-skyq-indo-stocks-surge-premarket-as-oil-prices-spike/cZgi9rgResX)  
  <sub>Stocktwits, 12 hours ago</sub>  
  Oil prices climbed higher after reports emerged that the U.S. and Iran had exchanged fire, stoking concerns over the prolonged closure of the Strait of...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.40</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 146.73 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 145.05 (+1.2%), 50d 133.89 (+9.6%), 200d 112.05 (+30.9%); 50d above 200d
Momentum: RSI(14) 54.0 | MACD 6.167 vs signal 6.837 (histogram -0.671)
Returns: 1d -1.0% | 5d -9.3% | 1m +9.0% | 3m +31.9%
52-week range: 66.17 - 161.86 (now 84.2% of the way up)
Volatility: ATR(14) 4.92 (3.4% of price) | annualised 20d 44.9%
Volume: 0.63x the 20-day average
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

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.40</summary>

```text
US inventories, week ending 2026-09-11 (published the following Wednesday)
  Crude oil: 423.4 million barrels, -0.6 on the week (a draw), 38% percentile over 52 weeks
  Petrol: 207.7 million barrels, +0.8 on the week (a build), 13% percentile over 52 weeks -- low for the time of year
  Diesel: 107.9 million barrels, +1.6 on the week (a build), 33% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

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

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

```text
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 5.4% of open interest (1,955,764 contracts)
Change on the week: -0.3% of open interest
Crowding: 98% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 12.28M | fund size: 1.80B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.35

**In the model's own words:**

> Corn has rallied 20% in three months and sits 95% of the way to its 52-week high, driven by WASDE yield downgrades and trade optimism around Trump-Xi talks. Technicals show strength across the trend (6.8% above 50d SMA, 11.3% above 200d), but momentum is deteriorating: RSI at 62 is elevated, MACD histogram has turned negative, and the latest daily close fell 0.8%. Volume is below average at 0.9x 20-day, signalling weakening conviction behind the move. Most critically, positioning is at the 97th percentile of the past year—a crowded long by construction of the CFTC data—which historically marks exhaustion as often as continuation. Crop condition at 57% good-or-excellent is 9 percentage points worse than the same week last year, which is bearish for price, but this is published information already priced in. The cost of holding the fund is -13.9% annualized due to contango roll drag; this makes the long less attractive and favors patience. Macro is calm (VIX 14.4), the dollar has strengthened (+0.93 on the week), and diesel at record highs lifts input costs—bullish for demand destruction. The setup contains multiple conflicting signals: supply tightness and trade optimism offset by extreme speculative crowding, weakening momentum, and punitive carry costs. This is not a clear catalyst, and macro timing on a single commodity is inherently difficult. The technical deterioration argues caution; the fundamental story is mixed rather than directional.

**Main reasons it gave:**
- CFTC positioning at 97th percentile of past year; crowding statistically predicts exhaustion not continuation
- MACD momentum negative despite price near 52-week high; volume below average
- Crop condition 9 points worse year-on-year but already known; published schedule removes surprise value
- Contango roll cost -13.9% annualized headwind to long position; highest entry point in a year demands larger move to justify
- Dollar +0.93 on week and diesel record high support demand destruction risk

<details><summary><b>News</b> — score +0.30</summary>

- [What's Behind The Latest Surge In Grain And Oilseed Prices?](https://seekingalpha.com/article/4948386-what-behind-latest-surge-grain-oilseed-prices)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  September 1 marked the start of the new marketing year for corn and soybeans, with yield estimates down as of the most recent WASDE report.
- [U.S. grains rally ahead of 'positive' Trump-Xi summit, continued Russia-Ukraine fighting](https://seekingalpha.com/news/4645187-us-grains-rally-ahead-of-positive-trump-xi-summit-continued-russia-ukraine-fighting)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  US grain futures rose after initial US-China trade talks were called positive by both sides, raising hopes the Trump-Xi meeting will include Chinese...
- [US diesel hits record $6.51 as supply deficit deepens despite WTI drop](https://scanx.trade/stock-market-news/commodities/newsom-signs-e15-gas-bill-california-fuel-prices-top-6-iran-tensions/51532724)  
  <sub>scanx.trade, 19 hours ago</sub>  
  US diesel prices hit a record high of $6.51/gal on Sep 21, 2026, driven by geopolitical tensions and infrastructure damage. Farm fuel costs rose by $11/acre...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.30</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 20.11 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 19.99 (+0.6%), 50d 18.83 (+6.8%), 200d 18.08 (+11.3%); 50d above 200d
Momentum: RSI(14) 61.9 | MACD 0.347 vs signal 0.417 (histogram -0.070)
Returns: 1d -0.8% | 5d +0.4% | 1m +5.8% | 3m +20.2%
52-week range: 16.47 - 20.29 (now 95.4% of the way up)
Volatility: ATR(14) 0.31 (1.6% of price) | annualised 20d 17.7%
Volume: 0.90x the 20-day average
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
Cost of holding this fund instead of corn itself: -13.9% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +20.2%, commodity +31.7%, gap -11.6% | 6 months: fund +8.7%, commodity +17.5%, gap -8.8% | 12 months: fund +13.4%, commodity +27.3%, gap -13.9%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.10</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.25</summary>

```text
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 22.5% of open interest (1,843,824 contracts)
Change on the week: -0.5% of open interest
Crowding: 97% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.25</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 8.38M | fund size: 168.47M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.25

**In the model's own words:**

> CANE is a sugar futures fund trading at the top of its range with a heavily crowded long positioning (98th percentile of the past year) and facing a structural headwind from rolling costs of -11.5% annually. The technical picture is mixed: price is up 13% from the 200-day moving average and has rallied 21.2% in three months, but momentum is stalling (RSI 51.4, MACD histogram negative, price now 1.5% below the 20-day SMA). The 3-month cost gap of -16.4% is particularly steep, indicating the fund has lost material value to the roll while the commodity itself gained 37.6%. Macro conditions are stable with low volatility and no recent data surprise; the rate path priced in mild Fed cuts over two years, which is neither supportive nor hostile to commodities. No news catalyst in the past 24 hours. The combination of extreme crowding at cycle highs, mounting evidence of roll decay, and momentum divergence argues for caution, but the fund remains above the 50-day SMA and has not broken the uptrend structurally. This is a hold rather than a trade signal in either direction.

**Main reasons it gave:**
- Large speculator positioning at 98th percentile crowding after 3-month 21.2% rally
- Roll cost of -11.5% annually, with 3-month fund gain of 21.2% vs commodity gain of 37.6%
- Momentum divergence: RSI neutral, MACD histogram negative despite price near 52-week highs
- Price 77.9% of the way into the 52-week range with price below 20-day SMA

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 11.20 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 11.38 (-1.5%), 50d 10.69 (+4.8%), 200d 9.91 (+13.0%); 50d above 200d
Momentum: RSI(14) 51.4 | MACD 0.115 vs signal 0.212 (histogram -0.097)
Returns: 1d +0.6% | 5d -1.6% | 1m -0.1% | 3m +21.2%
52-week range: 9.02 - 11.82 (now 77.9% of the way up)
Volatility: ATR(14) 0.20 (1.8% of price) | annualised 20d 24.3%
Volume: 1.97x the 20-day average
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
Cost of holding this fund instead of sugar itself: -11.5% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +21.2%, commodity +37.6%, gap -16.4% | 6 months: fund +7.2%, commodity +19.0%, gap -11.8% | 12 months: fund +8.0%, commodity +19.5%, gap -11.5%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

```text
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 18.5% of open interest (1,219,523 contracts)
Change on the week: -0.2% of open interest
Crowding: 98% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 5.26M | fund size: 58.94M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.25

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Copper is at the top of its 52-week range with a clean uptrend (50d>200d, MACD positive, RSI 59.6) on a physical-tightening story in China, but nothing here is a macro surprise: yields barely moved, VIX is calm at 14.4, and the dollar firmed +0.93 on the week, a mild headwind for metals. Speculative net long actually fell 5.1% of open interest to a middling 40th percentile, so the recent push is not being confirmed by fresh positioning, and volume is below average at 0.86x. The fund's -6.2%/yr roll drag is heavy and argues for demanding a larger move before paying up for a long near the highs. Vertical-extension risk plus an unremarkable macro backdrop keeps this at NEUTRAL with only a mild upward tilt.

**Main reasons it gave:**
- Close 40.99, 99.5% of the way up the 52-week range, 50d above 200d
- CFTC spec net long fell 5.1% of OI on the week, only 40th percentile crowding
- Roll cost -6.2%/yr vs spot copper, heavy drag on a long
- Dollar index +0.93 on the week, VIX calm at 14.4, no rate surprise (10y -4bp)
- Volume 0.86x 20-day average on the breakout attempt

<details><summary><b>News</b> — score +0.30</summary>

- [Copper rises for sixth straight day on signs of tightening supplies in China (CPER:NYSEARCA)](https://seekingalpha.com/news/4645346-copper-rises-for-sixth-straight-day-on-signs-of-tightening-supplies-in-china)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Copper futures rose toward a record in early trading as falling inventories and pre-holiday buying signaled tightening supplies in China's physical market.
- [Oil ETFs Surge: What's Next for Commodity Investors?](https://www.zacks.com/stock/news/2993265/oil-etfs-surge-whats-next-for-commodity-investors)  
  <sub>Zacks Investment Research, 18 hours ago</sub>  
  What's next for oil, gold and copper as geopolitical risks reshape commodity markets?
- [[ETF 특징주] 중국 공급 압박에 구리값 오르자 CPER·COPP 강세](https://www.newspim.com/news/view/20260922001085)  
  <sub>뉴스핌, 8 hours ago</sub>  
  이 기사는 인공지능(AI) 모델의 번역을 기반으로 전문 기자의 분석과 아이템 발굴을 통해 생성한 콘텐츠입니다. [서울=뉴스핌] 황숙혜 기자 = 중국의 현물 공급이 위축...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.30</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.45</summary>

```text
Last close 40.99 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 39.79 (+3.0%), 50d 39.54 (+3.7%), 200d 37.17 (+10.3%); 50d above 200d
Momentum: RSI(14) 59.6 | MACD 0.149 vs signal 0.033 (histogram 0.116)
Returns: 1d +0.8% | 5d +6.0% | 1m +2.5% | 3m +9.8%
52-week range: 28.62 - 41.05 (now 99.5% of the way up)
Volatility: ATR(14) 0.72 (1.8% of price) | annualised 20d 28.4%
Volume: 0.86x the 20-day average
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
Cost of holding this fund instead of copper itself: -6.2% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +9.8%, commodity +11.4%, gap -1.5% | 6 months: fund +22.2%, commodity +25.7%, gap -3.5% | 12 months: fund +43.4%, commodity +49.7%, gap -6.2%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.15</summary>

```text
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 22.5% of open interest (289,463 contracts)
Change on the week: -5.1% of open interest
Crowding: 40% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 18.71M | fund size: 766.80M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.25

**In the model's own words:**

> Silver faces competing macro headwinds and tailwinds with no clear catalyst for directional conviction. The dollar strengthened +0.93% this week and treasury yields remain elevated at 4.96%, both headwinds for precious metals. Meanwhile news points to fiscal dominance concerns and supply deficits supporting silver, but these are structural themes not recent surprises. Technicals show the 50-day MA below the 200-day (a bearish pattern), RSI neutral at 52.8, and MACD histogram negative. Price is down 9.5% from 200d MA and sits near the lower end of the 52-week range, which could appeal to value buyers but offers no momentum confirmation. The carry cost of -3.8% annualized is a persistent drag that requires conviction of a material move to justify. Positioning at 65th percentile is normal, not crowded. Volume is subthreshold at 0.37x average. The five-day gain of +3.6% is modest and three-month return of +6.9% offers no trend confirmation given the longer-term weakness. No policy surprise, no data surprise, and no technical break support a directional call.

**Main reasons it gave:**
- Dollar index up 0.93% this week, headwind for precious metals
- Price 9.5% below 200-day MA in bearish downtrend structure
- Carry cost -3.8% annually reduces long conviction without catalytic move
- Supply deficit and fiscal dominance themes are structural, not recent catalysts
- RSI 52.8 and MACD histogram negative show no momentum support

<details><summary><b>News</b> — score +0.15</summary>

- [Current price of silver as of Tuesday, Sept. 22, 2026](https://fortune.com/article/current-price-of-silver-9-22-2026/)  
  <sub>Fortune, 4 hours ago</sub>  
  If you're worried about increased inflation, adding precious metals like silver to your portfolio can be a smart choice.
- [Ondo Stocks Goes Live on near.com and NEAR Intents](https://ondo.finance/blog/ondo-stocks-go-live-on-near)  
  <sub>Ondo Finance, 2 hours ago</sub>  
  Ondo Stocks, the largest tokenized securities platform globally with $1B+ in TVL and tens of thousands of asset holders driving $26B+ in trading volume,...
- [‘The Sell Button Won’t Work’: Why Rate Hikes No Longer Save Debt Markets](https://www.benzinga.com/markets/bonds/26/09/61916030/the-sell-button-wont-work-why-rate-hikes-no-longer-save-debt-markets)  
  <sub>Benzinga, 3 hours ago</sub>  
  Forget Fed rate hikes: Macro analysts reveal why fiscal dominance and massive deficits make gold and real assets the ultimate hedges.
- [Quant Silver ETF Share Price NSE/BSE - Live Price Charts & Performance](https://hdfcsky.com/etf/quant-silver-etf)  
  <sub>HDFC Sky, 19 hours ago</sub>  
  Quant Silver ETF price ₹23.55 with -0.97% change at 21-09-2026 15:24. Check ETF price, returns, performance, charts and invest in ETF in India.
- [Gold And Silver Defy A Hawkish Fed](https://seekingalpha.com/article/4948382-gold-silver-defy-hawkish-fed)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Gold and silver managed to regain some ground last week despite facing what might sometimes be a difficult environment for precious metals.
- [Silver Price Forecast: Can the Fed Delay the Next Silver Rally?](https://www.equiti.com/uae-en/news/trade-reviews/silver-price-forecast-fed-supply-deficit-2026/)  
  <sub>www.equiti.com, 21 hours ago</sub>  
  Silver prices face pressure from Fed rate expectations, but a sixth consecutive supply deficit and constrained mine output continue supporting the long-term...
- [Current price of silver as of Monday, September 21, 2026](https://fortune.com/article/current-price-of-silver-9-21-2026/)  
  <sub>Fortune, 23 hours ago</sub>  
  If you're worried about increased inflation, adding precious metals like silver to your portfolio can be a smart choice.
- [Bandhan Silver ETF Share Price NSE/BSE - Live Price Charts & Performance](https://www.google.com/goto?url=CAESYgHrOzAVznFbvfwL_athk4eZDtbc9jZFuS1ZxILPjpOqaS_M9XTy8mzhRJTiGgHpm6MTackxE5-nFqcVk05sY2434OJJGFNB0HIU_c6BTZITap_r_u1VrkiP5KXBNHZboTG8)  
  <sub>HDFC Sky, 21 hours ago</sub>  
  Bandhan Silver ETF price ₹232.30 with -1.35% change at 21-09-2026 15:29. Check ETF price, returns, performance, charts and invest in ETF in India.
- [Gold snaps three-session win streak as dollar rises, oil prices fall (GLD:NYSEARCA)](https://seekingalpha.com/news/4645199-gold-snaps-three-session-win-streak-as-dollar-rises-oil-prices-fall)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Gold futures turned lower, snapping a three-session winning streak, as the market returned its focus to US yields and the Federal Reserve's interest rate...
- [Groww Silver ETF FOF(G)-Direct Plan](https://univest.in/mutual-funds/groww-silver-etf-fof-g-direct-plan)  
  <sub>Univest, 19 hours ago</sub>  
  Groww Silver ETF FOF(G)-Direct Plan details: NAV ₹22.5587, AUM 89 Cr, Expense Ratio 0.18%. Check returns, holdings, sector allocation, and fund manager...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 59.58 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 59.47 (+0.2%), 50d 57.08 (+4.4%), 200d 65.87 (-9.5%); 50d below 200d
Momentum: RSI(14) 52.8 | MACD 0.192 vs signal 0.277 (histogram -0.085)
Returns: 1d -0.1% | 5d +3.6% | 1m -5.0% | 3m +6.9%
52-week range: 39.82 - 105.60 (now 30.0% of the way up)
Volatility: ATR(14) 1.71 (2.9% of price) | annualised 20d 37.3%
Volume: 0.37x the 20-day average
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
Cost of holding this fund instead of silver itself: -3.8% a year -- a steady drag
Measured: 3 months: fund +6.9%, commodity +7.3%, gap -0.4% | 6 months: fund -4.6%, commodity -3.6%, gap -1.0% | 12 months: fund +52.6%, commodity +56.5%, gap -3.8%
A commodity fund holds futures, not silver, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.05</summary>

```text
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 12.7% of open interest (103,745 contracts)
Change on the week: -1.3% of open interest
Crowding: 65% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.05</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 572.79M | fund size: 34.13B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.25

**In the model's own words:**

> SOYB has rallied 15.9% in three months and now sits at the 99.9th percentile of its 52-week range, with technical momentum showing RSI at 65.8 and price 15.1% above the 200-day moving average. The recent Trump-Xi trade optimism provides near-term sentiment support, but the fundamental picture is mixed. Crop conditions at 58% good/excellent are steady week-over-week and only 3 points below last year, showing no deterioration signal. CFTC positioning shows large speculators net long at the 88th percentile of crowding with a -2.2% weekly reduction, suggesting some distribution into strength rather than accumulation. The cost of holding structure shows a -1.4% annual drag from futures rolling. Macro remains benign with the yield curve normal, VIX calm at 14.4, and the dollar strengthening. The technicals reflect a mature advance rather than a breakout: volume is only 0.11x the 20-day average, momentum is rolling over (MACD histogram negative), and the instrument is at historical extremes. A bullish China trade narrative exists but is already priced into the 7.2% one-month move. The combination of extended valuation, light volume, negative momentum divergence, and modest crop deterioration year-over-year argues against chasing the rally, but no clear reversal signal has emerged. A data surprise or policy shock would be needed to break the current equilibrium.

**Main reasons it gave:**
- Price at 99.9th percentile of 52-week range with light volume suggests extended rally
- RSI 65.8 with negative MACD histogram indicates momentum rolling over despite higher price
- Large speculator positioning at 88th percentile crowding with -2.2% weekly reduction signals distribution
- Crop conditions 58% G/E steady with only -3 point year-over-year decline, no supply deterioration
- Cost of carry at -1.4% annually creates structural headwind against further appreciation

<details><summary><b>News</b> — score +0.30</summary>

- [U.S. grains rally ahead of 'positive' Trump-Xi summit, continued Russia-Ukraine fighting](https://seekingalpha.com/news/4645187-us-grains-rally-ahead-of-positive-trump-xi-summit-continued-russia-ukraine-fighting)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  US grain futures rose after initial US-China trade talks were called positive by both sides, raising hopes the Trump-Xi meeting will include Chinese...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.30</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.25</summary>

```text
Last close 28.14 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 27.59 (+2.0%), 50d 26.36 (+6.8%), 200d 24.44 (+15.1%); 50d above 200d
Momentum: RSI(14) 65.8 | MACD 0.523 vs signal 0.553 (histogram -0.030)
Returns: 1d +0.1% | 5d +0.7% | 1m +7.2% | 3m +15.9%
52-week range: 21.46 - 28.14 (now 99.9% of the way up)
Volatility: ATR(14) 0.35 (1.2% of price) | annualised 20d 17.5%
Volume: 0.11x the 20-day average
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
Cost of holding this fund instead of soybeans itself: -1.4% a year -- a steady drag
Measured: 3 months: fund +15.9%, commodity +18.9%, gap -3.0% | 6 months: fund +16.3%, commodity +14.2%, gap +2.1% | 12 months: fund +28.1%, commodity +29.5%, gap -1.4%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.15</summary>

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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 1.68M | fund size: 47.14M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.25

**In the model's own words:**

> UNG faces headwinds from a structural cost of holding that has eroded returns at -22.4% annualized, with the fund down 15.7% versus the commodity up 6.7% over the past 12 months. Near-term technicals show modest strength—price up 3.3% on the day and above both 20d and 50d moving averages with RSI 56.4 and positive MACD histogram—but this sits within a longer downtrend: the asset is 7.8% below its 200d MA in a bear market (52-week range placing it just 13.3% up from lows). Energy inventories posted a build at the 71st percentile, a neutral-to-bearish signal, while the EIA price forecast sees Henry Hub rising only 7% over six months from here—modest upside. CFTC positioning shows large speculators net short at the 33rd percentile of crowding, neither extreme nor capitulation. Macro backdrop is stable: the yield curve is upward-sloping at +95bp, VIX is calm at 14.4, and the dollar just moved +0.93% higher this week, which typically pressures commodities. No material surprise in recent data or policy. The technicals offer a weak bounce, but the structural drag from rolling costs, inventory backdrop, and modest price guidance do not support conviction above NEUTRAL.

**Main reasons it gave:**
- Cost of holding at -22.4% annualized eroded 12-month gap of -22.4% relative to the commodity
- Natural gas inventories at 71st percentile with +44 bcf build this week reads bearish
- EIA price forecast sees only 7% upside over six months to March 2027
- Price 7.8% below 200-day MA in longer downtrend despite near-term +3.3% daily move
- Dollar index up +0.93% this week, headwind for commodity fund

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.35</summary>

```text
Last close 10.60 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 10.40 (+1.9%), 50d 10.24 (+3.6%), 200d 11.49 (-7.8%); 50d below 200d
Momentum: RSI(14) 56.4 | MACD 0.034 vs signal 0.022 (histogram 0.012)
Returns: 1d +3.3% | 5d +0.6% | 1m +6.1% | 3m -7.8%
52-week range: 9.63 - 16.90 (now 13.3% of the way up)
Volatility: ATR(14) 0.28 (2.6% of price) | annualised 20d 26.9%
Volume: 1.07x the 20-day average
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
Cost of holding this fund instead of natural gas itself: -22.4% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -7.8%, commodity -2.1%, gap -5.8% | 6 months: fund -9.6%, commodity +6.6%, gap -16.2% | 12 months: fund -15.7%, commodity +6.7%, gap -22.4%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.20</summary>

```text
US inventories, week ending 2026-09-11 (published the following Wednesday)
  Natural gas: 3,298.0 billion cubic feet, +44.0 on the week (a build), 71% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

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
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 5.5% of open interest (1,820,003 contracts)
Change on the week: -0.2% of open interest
Crowding: 33% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 55.41M | fund size: 587.34M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.25

**In the model's own words:**

> Wheat closed slightly down yesterday (-0.8%) after a brief pop on trade optimism. The technical picture is mixed: the fund sits 76.6% of the way up its 52-week range with a 13.5% gain over a year, but momentum is fading (RSI 49.9, MACD histogram negative). The 20-day moving average is rolling over while the longer-term trend remains positive. CFTC positioning shows large speculators crowded long at the 90th percentile—a level as often marking the end of a move as the middle. More critically, the cost of holding this fund versus wheat itself is brutal: -13.5% annualized due to contango in the futures curve. The 12-month data shows the fund returned 24% while the commodity itself rose 37.5%—the fund captured only 64% of the underlying move. US crop conditions are 51% good/excellent, up only 2 points year-over-year, offering no new bullish signal. While near-term Trump-Xi trade sentiment provided a bounce, macro is calm (VIX 14.4, curve normal, dollar up 0.93 on the week). There is no clear catalyst emerging: the initial trade optimism is priced in, positioning is already crowded, and structural headwinds in the fund itself are substantial. A cautious neutral stance is warranted.

**Main reasons it gave:**
- Large speculators crowded long at 90th percentile of 52-week positioning
- Cost of holding fund -13.5% annualized due to contango roll losses
- Momentum fading with RSI at 50 and negative MACD histogram
- Crop condition up only 2 points year-over-year, no new supply risk
- Trade optimism brief and already reflected in initial move

<details><summary><b>News</b> — score +0.15</summary>

- [U.S. grains rally ahead of 'positive' Trump-Xi summit, continued Russia-Ukraine fighting](https://seekingalpha.com/news/4645187-us-grains-rally-ahead-of-positive-trump-xi-summit-continued-russia-ukraine-fighting)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  US grain futures rose after initial US-China trade talks were called positive by both sides, raising hopes the Trump-Xi meeting will include Chinese...
- [Why is Teucrium Wheat Fund stock climbing today? By Investing.com](https://in.investing.com/news/stock-market-news/why-is-teucrium-wheat-fund-stock-climbing-today-93CH-5600047)  
  <sub>Investing.com India, 23 hours ago</sub>  
  Investing.com -- Teucrium Wheat Fund stock climbed 1.9% in mid-day trading to reach $26.355, as wheat futures advanced on the session against a backdrop of...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 26.10 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 26.74 (-2.4%), 50d 25.51 (+2.3%), 200d 23.00 (+13.5%); 50d above 200d
Momentum: RSI(14) 49.9 | MACD 0.200 vs signal 0.378 (histogram -0.177)
Returns: 1d -0.8% | 5d -0.8% | 1m +2.7% | 3m +16.4%
52-week range: 19.88 - 28.00 (now 76.6% of the way up)
Volatility: ATR(14) 0.59 (2.2% of price) | annualised 20d 31.4%
Volume: 0.12x the 20-day average
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
Cost of holding this fund instead of wheat itself: -13.5% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +16.4%, commodity +22.5%, gap -6.0% | 6 months: fund +15.1%, commodity +22.2%, gap -7.2% | 12 months: fund +24.0%, commodity +37.5%, gap -13.5%
A commodity fund holds futures, not wheat, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.35</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 0.8% of open interest (485,138 contracts)
Change on the week: -1.8% of open interest
Crowding: 90% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 14.00M | fund size: 365.51M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [China's gold imports surpass 1,000-ton mark on strong domestic demand](https://seekingalpha.com/news/4645254-china-gold-imports-surpass-1000-ton-mark-on-strong-domestic-demand)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Chinese gold imports reached record highs this year, bolstered by a retreat in international bullion prices and a strengthening yuan.
- [Best Gold ETFs to Buy Now for September 2026](https://www.zacks.com/featured-articles/882/best-gold-etfs)  
  <sub>Zacks Investment Research, 20 hours ago</sub>  
  Gold ETFs are a great way to buy the commodity without the worry of buying and storing physical bullion. Gold prices have remained elevated in 2026 amid...
- [How do I convert SPDR Gold Shares Tokenized ETF (Derivatives) (GLD) to Japanese Yen (JPY)?](https://cryptorank.io/price/spdr-gold-shares-tokenized-etf-derivatives/jpy)  
  <sub>CryptoRank, 23 hours ago</sub>  
  Current SPDR Gold Shares Tokenized ETF (Derivatives) (GLD) token data: Price to Japanese Yen (JPY) - ¥ 62798, Trading Volume 14.68M, Market Cap N/A.
- [SPDR Gold ETF Options Spot-On: On September 21st, 487.84K Contracts Were Traded, With 6.69 Million Open Interest](https://news.futunn.com/en/post/79574258/spdr-gold-etf-options-spot-on-on-september-21st-487)  
  <sub>富途牛牛, 18 hours ago</sub>  
  OnSeptember 21st ET, $SPDR Gold ETF(GLD.US)$ had active options trading, with a total trading volume of 487.84K options for the day, of which put options...
- [‘The Sell Button Won’t Work’: Why Rate Hikes No Longer Save Debt Markets](https://www.benzinga.com/markets/bonds/26/09/61916030/the-sell-button-wont-work-why-rate-hikes-no-longer-save-debt-markets)  
  <sub>Benzinga, 3 hours ago</sub>  
  Forget Fed rate hikes: Macro analysts reveal why fiscal dominance and massive deficits make gold and real assets the ultimate hedges.
- [Gold snaps three-session win streak as dollar rises, oil prices fall (GLD:NYSEARCA)](https://seekingalpha.com/news/4645199-gold-snaps-three-session-win-streak-as-dollar-rises-oil-prices-fall)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Gold futures turned lower, snapping a three-session winning streak, as the market returned its focus to US yields and the Federal Reserve's interest rate...
- [How do I convert SPDR Gold Shares Tokenized ETF (Derivatives) (GLD) to Chinese Yuan (CNY)?](https://cryptorank.io/price/spdr-gold-shares-tokenized-etf-derivatives/cny)  
  <sub>CryptoRank, 24 hours ago</sub>  
  Current SPDR Gold Shares Tokenized ETF (Derivatives) (GLD) token data: Price to Chinese Yuan (CNY) - CN¥ 2671, Trading Volume 629.66K, Market Cap N/A.
- [How do I convert SPDR Gold Shares Tokenized ETF (Derivatives) (GLD) to Vietnamese Dong (VND)?](https://cryptorank.io/price/spdr-gold-shares-tokenized-etf-derivatives/vnd)  
  <sub>CryptoRank, 23 hours ago</sub>  
  Current SPDR Gold Shares Tokenized ETF (Derivatives) (GLD) token data: Price to Vietnamese Dong (VND) - ₫ 10379182, Trading Volume 2.43B, Market Cap N/A.
- [How do I convert SPDR Gold Shares Tokenized ETF (Derivatives) (GLD) to South Korean Won (KRW)?](https://cryptorank.io/price/spdr-gold-shares-tokenized-etf-derivatives/krw)  
  <sub>CryptoRank, 24 hours ago</sub>  
  Current SPDR Gold Shares Tokenized ETF (Derivatives) (GLD) token data: Price to South Korean Won (KRW) - ₩ 547929, Trading Volume 129.19M, Market Cap N/A.
- [Daily ETF Flows: COWZ Gobbles Up Assets](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-cowz-gobbles-210028745.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Top 10 Creations (All ETFs). Ticker. Name. Net Flows ($, mm). AUM ($, mm). AUM % Change. IVV · iShares Core S&P 500 ETF. 8,519.50. 845,149.30. 1.01%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.01% (+0.05 on the week) | 5-year 4.83% (+0.00 on the week) | 10-year 4.96% (-0.04 on the week) | 30-year 5.30% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 100.58 (+0.93 on the week)
Volatility (VIX): 14.42 (-2.8 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 397.53 (bar of 2026-09-22), from 501 daily bars
Trend: vs 20d SMA 403.91 (-1.6%), 50d 394.01 (+0.9%), 200d 416.33 (-4.5%); 50d below 200d
Momentum: RSI(14) 47.8 | MACD -0.862 vs signal 0.427 (histogram -1.289)
Returns: 1d -0.2% | 5d +0.9% | 1m -6.1% | 3m +5.4%
52-week range: 343.32 - 495.90 (now 35.5% of the way up)
Volatility: ATR(14) 7.20 (1.8% of price) | annualised 20d 22.8%
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
Cost of holding this fund instead of gold itself: -0.9% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +5.4%, commodity +5.5%, gap -0.1% | 6 months: fund -1.6%, commodity -0.7%, gap -0.9% | 12 months: fund +17.2%, commodity +18.1%, gap -0.9%
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 260.30M | fund size: 103.48B
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

