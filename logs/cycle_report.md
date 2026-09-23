# Daily report

**23 Sep 2026, 19:20 Israel time (16:20 UTC)** · 80 names checked · 7 traded · 3 with a problem

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 7 | 9 | 0 |
| Whole-market funds | 14 | 0 | 14 | 0 |
| Sector and country funds | 41 | 2 | 37 | 2 |
| Commodities | 9 | 0 | 8 | 1 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| Developing country bonds (EMB) · Index fund | **Stop raised.** At +0.43R, following the price. Stop-loss raised 94.05 → 93.91. |
| US government bonds, 7-10 years (IEF) · Index fund | **Stop raised.** At +0.93R, following the price. Stop-loss raised 91.61 → 91.28. |
| US regional banks (KRE) · Sector or country | **Stop raised.** At +0.07R, following the price. Stop-loss raised 73.81 → 73.60. |
| Microsoft (MSFT) · Company | **Stop raised.** At +0.37R, following the price. Stop-loss raised 474.94 → 477.77. |
| Novo Nordisk (NVO) · Company | **Stop raised.** At +0.46R, following the price. Stop-loss raised 42.26 → 41.27. |
| S&P 500, equal weight (RSP) · Index fund | **Stop raised.** At -0.02R, following the price. Stop-loss raised 215.78 → 215.68. |
| Teva Pharmaceutical (TEVA) · Company | **Stop raised.** At +0.05R, following the price. Stop-loss raised 37.03 → 37.12. |
| US government bonds, 7-10 years (IEF) · Index fund | **Stop resized.** Its stop-loss order was for 119 shares but only 131 are held, so an order that size could never have filled. Resized to 131. Stop-loss 91.61. |
| Teva Pharmaceutical (TEVA) · Company | **Stop resized.** Its stop-loss order was for 127 shares but only 128 are held, so an order that size could never have filled. Resized to 128. Stop-loss 37.03. |
| US government bonds, 20+ years (TLT) · Index fund | **Stop resized.** Its stop-loss order was for 133 shares but only 147 are held, so an order that size could never have filled. Resized to 147. Stop-loss 82.41. |
| US government bonds, 7-10 years (IEF) · Index fund | **Problem.** Could not be managed: BrokerError: close_position failed for IEF: {"available":"0","code":40310000,"existing_qty":"131","held_for_orders":"131","message":"insufficient qty available for order (requested: 12, available: 0)","symbol":"IEF"} |
| US inflation-linked bonds (TIP) · Index fund | **Problem.** Could not be managed: BrokerError: close_position failed for TIP: {"available":"0","code":40310000,"existing_qty":"10","held_for_orders":"10","message":"insufficient qty available for order (requested: 3, available: 0)","symbol":"TIP"} |
| US government bonds, 20+ years (TLT) · Index fund | **Problem.** Could not be managed: BrokerError: close_position failed for TLT: {"available":"0","code":40310000,"existing_qty":"147","held_for_orders":"147","message":"insufficient qty available for order (requested: 14, available: 0)","symbol":"TLT"} |
| US government bonds, 20+ years (TLT) · Index fund | **Problem.** Could not be managed: BrokerError: replace_order failed for c5ab9682-7d83-463d-94a1-0eef016f6cc1: {"code":42210000,"message":"order chain not fully replaced"} |
| US dollar (UUP) · Index fund | **Problem.** Could not be managed: BrokerError: close_position failed for UUP: {"available":"0","code":40310000,"existing_qty":"422","held_for_orders":"422","message":"insufficient qty available for order (requested: 140, available: 0)","symbol":"UUP"} |
| Taiwan (EWT) · Sector or country | **Holding.** -0.39R, holding 33 shares. Stop-loss 110.28. |
| Gold (GLD) · Commodity | **Holding.** -0.27R, holding 10 shares. Stop-loss 404.87. |
| Eli Lilly (LLY) · Company | **Holding.** +0.19R, holding 4 shares. Stop-loss 1113.34. |
| Nvidia (NVDA) · Company | **Holding.** +0.84R, holding 16 shares. Stop-loss 216.23. |
| US shopping and leisure (XLY) · Sector or country | **Holding.** -0.24R, holding 63 shares. Stop-loss 113.36. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Exxon Mobil (XOM) · Company — BULLISH, confidence 0.68

**Result:** ACCEPTED · 13 shares · submitted buy 13 XOM @ ~161.18, stop 153.51

**In the model's own words:**

> BUY

**Main reasons it gave:**
- Record oil output and revenue with lower capital spending (Yahoo Finance, 10h ago)
- Insider net purchase of ~6.9M shares in last 180 days
- Forward P/E 14.86 and YoY revenue +44% and earnings +113% indicate cheap, high‑growth fundamentals
- MACD below signal and volume 0.21× 20‑day average suggest weak technical momentum
- Exxon raised LNG sales target to 50M tons by 2030 (Motley Fool, 22h ago)

<details><summary><b>News</b> — score +0.60</summary>

- [ExxonMobil (XOM) Delivers Record Oil Output And Revenue On Lower Spending](https://finance.yahoo.com/energy/articles/exxonmobil-xom-delivers-record-oil-051644024.html)  
  <sub>Yahoo Finance, 10 hours ago</sub>  
  ExxonMobil Holdings (NYSE:XOM) recently reported record oil output and revenue achieved while keeping capital spending at lower levels.
- [XOM|Exxon Mobil Corp|Price:158.710|Chg%:+0.410](https://www.tradingkey.com/markets/stocks/xom)  
  <sub>TradingKey, 7 hours ago</sub>  
  Exxon Mobil Corp News ... Marathon Petroleum fell due to profit-taking and easing geopolitical risks. • Refining crack spreads compressed following...
- [US-Israel Strikes On Iran Send Nasdaq, S&P 500 Futures Lower As Offensive Continues Across The Middle East — LMT, RTX, XOM, USO, BATL On Traders' Radar Today](https://stocktwits.com/news-articles/markets/equity/nasdaq-sp-500-futures-decline-us-israel-strikes-on-iran-crude-oil-price-soars/cZd35CDRIcM)  
  <sub>Stocktwits, 6 hours ago</sub>  
  Data from Stocktwits showed that retail sentiment on SPY has remained 'bullish', while it hovered in the 'bearish' territory on QQQ.
- [Could Palantir Be the Next Stock Added to the Dow Jones?](https://www.google.com/goto?url=CAESxAEB6zswFY2kzmIFmLnZ0fNmGiTGfnpRa-DtC872M93oiHGxk0Gy8sd9CgLaZIICcqMS7KoykUkj0tLmKcUlzP5Q9MGB2DFQZuHzqK5Td11Q5Fmgch2uw4DsWMcxE_HhgbUl7ZlZ0wK3_Znt-hVr6oFCyeC-SiS8M5urlbIupRsy7YbgfoytB04_4JWqcLoQYzxoSzAcUvmubi8W7ZFIlfWSwE_B8wa7P4loAMkq1yvk0CHOO1pWrPihTAaPZbfir4ab1gpa)  
  <sub>The Globe and Mail, 5 hours ago</sub>  
  Detailed price information for Exxonmobil Holdings Corp (XOM-N) from The Globe and Mail including charting and trades.
- [Exxon sees Brazil’s offshore Foz do Amazonas as next South American energy prize (XOM:NYSE)](https://seekingalpha.com/news/4645788-exxon-sees-brazils-offshore-foz-do-amazonas-as-next-south-american-energy-prize)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  ExxonMobil said it sees the next wave of large oil and natural gas discoveries in South America's northern equatorial margin occurring in Brazil,...
- [XOM Looks 23.4% Overvalued on GF Value™ Amid Solid Dividend Fund](https://www.gurufocus.com/news/9092560/xom-looks-234-overvalued-on-gf-value-amid-solid-dividend-fundamentals)  
  <sub>GuruFocus, 14 hours ago</sub>  
  On September 22, 2026, ExxonMobil (NYSE: XOM) announced promising exploration prospects in Brazil's northern equatorial margin, following its recent...
- [Is Exxon Mobil (NYSE:XOM) Worth Watching as Tech Strength Meets Broader Market Caution?](https://kalkinemedia.com/us/stocks/oil-gas/is-exxon-mobil-nysexom-worth-watching-as-tech-strength-meets-broader-market-caution)  
  <sub>Kalkine Media, 3 hours ago</sub>  
  Highlights. Exxon Mobil's Permian and Guyana assets drive production growth. Oil and Gas Stocks are responding to changing sector and macro signals.
- [XOM Oct 2026 185.000 call (XOM261030C00185000) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XOM261030C00185000/)  
  <sub>Yahoo Finance Singapore, 3 hours ago</sub>  
  Find the latest XOM Oct 2026 185.000 call (XOM261030C00185000) stock quote, history, news and other vital information to help you with your stock trading...
- [Exxon Just Set a Bold 2030 Target for LNG Sales. Here's What 50 Million Tons Actually Means.](https://www.fool.com/investing/2026/09/22/exxon-just-set-a-bold-2030-target-for-lng-sales-here-s-what-50-million-tons-actually-means/)  
  <sub>The Motley Fool, 22 hours ago</sub>  
  ExxonMobil (XOM +0.26%) recently raised its annual sales target for liquefied natural gas (LNG) to 50 million tons by 2030. That's double the company's...
- [DE: Deere & Company - Stock Price, Quote and News | NYSE](https://techgraph.co/stock-market/quote/de/)  
  <sub>TechGraph, 6 hours ago</sub>  
  ... AM 12:45 PM 2:25 PM 4:00 PM 704.92 684.01 684.73 703.12. HDB $23.41 -1.01% JPM $340.00 -3.42% JNJ $269.19 -0.10% XOM $158.71 +0.26% BRK.B $503.49 +0.29%

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 160.98 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 162.16 (-0.7%), 50d 158.50 (+1.6%), 200d 147.33 (+9.3%); 50d above 200d
Momentum: RSI(14) 49.3 | MACD 1.098 vs signal 1.846 (histogram -0.748)
Returns: 1d +1.7% | 5d -4.9% | 1m -2.5% | 3m +15.2%
52-week range: 110.64 - 171.47 (now 82.8% of the way up)
Volatility: ATR(14) 3.84 (2.4% of price) | annualised 20d 28.9%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.70</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 661.94B
Valuation: trailing P/E 20.66 | forward P/E 14.86 | P/B 2.55 | PEG 1.36
Profitability: profit margin 9.1% | operating margin 15.9% | ROE 12.6%
Growth (YoY): revenue +44.1% | earnings +112.8%
Balance sheet: debt/equity 15.9% | free cash flow 20.67B
Risk: beta 0.17 | short interest 1.1% of float
Next earnings: 2026-10-30
```

</details>

<details><summary><b>What this fund holds</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.70</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-06-30 in line | 2026-03-31 beat by 14% | 2025-12-31 in line | 2025-09-30 beat by 2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: buy (mean 2.32 on a 1=strong buy to 5=strong sell scale, 22 analysts)
Ratings: 3 strong buy, 7 buy, 15 hold, 0 sell, 0 strong sell
Price target: mean 171.91 (+6.8% vs last close), range 142.00 - 200.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.50</summary>

```text
Last 180 days: bought 10,818,651 shares in 251 transaction(s) | sold 3,904,152 shares in 49
Net: +6,914,499 shares (-194.8% of insider holdings) | insiders hold 3,371,767 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.50</summary>

_Not available today._

</details>

### ASML (ASML) · Company — BULLISH, confidence 0.60

**Result:** ACCEPTED · 1 shares · submitted buy 1 ASML @ ~1726.51, stop 1619.35

**In the model's own words:**

> The news includes a material sales outlook upgrade to EUR 45 bn, which is a bullish catalyst, while also noting zero European sales – a mixed signal. Fundamentals are strong (high margins, low debt, solid growth) and earnings have been positive (2 beats in the last 4 quarters). Technicals show the price above key moving averages but with thin volume, tempering confidence. Analyst consensus is already strongly bullish, adding little new information. No insider activity provides a neutral contribution. Overall, the positive catalyst and strong fundamentals outweigh the mixed news and thin volume, leading to a bullish view with moderate conviction.

**Main reasons it gave:**
- Q2 sales outlook raised to EUR 45 bn (AD HOC NEWS, 3 h ago)
- Strong fundamentals: 30% profit margin, 37% operating margin, low debt (DE 9.1%)
- Technical: price above 20‑day, 50‑day, and 200‑day SMAs; volume only 0.35× 20‑day average
- Earnings record: 2 beats in last 4 quarters, recent beats of 9% and 7%
- Negative news: zero lithography sales in Europe Q2 (Briefs Finance, 15 h ago)

<details><summary><b>News</b> — score +0.20</summary>

- [ASML vs. Intel: Which AI Chip Stock Is a Better Buy in 2026?](https://www.fool.com/coverage/better-buy/2026/09/22/asml-vs-intel-ai-chip-stock-better-buy-2026/)  
  <sub>The Motley Fool, 15 hours ago</sub>  
  ASML commands a near-monopoly on essential chipmaking equipment with a 29% net margin and strong cash flow, while Intel navigates a turnaround with negative...
- [ASML Holding (NasdaqGS:ASML) Jumped, So What Is Driving Attention Now?](https://simplywall.st/stocks/us/semiconductors/nasdaq-asml/asml-holding/news/asml-holding-nasdaqgsasml-jumped-so-what-is-driving-attentio)  
  <sub>Simply Wall Street, 9 hours ago</sub>  
  ASML Holding (NasdaqGS:ASML) continues to attract attention after its recent share move. The stock closed at US$1747.90 and delivered a year-to-date return...
- [ASML: Europe Gets No Chip Tools in Q2](https://www.briefs.co/news/asml-warns-europe-is-missing-out-as-it-sells-zero-chipmaking/)  
  <sub>Briefs Finance, 15 hours ago</sub>  
  ASML sold zero lithography systems in Europe in Q2 as fab investment shifts to South Korea, Taiwan, China and the US; EU revises chip policy to boost local...
- [ASML Holding stock gains as sales outlook reaches EUR 45 billion](https://www.ad-hoc-news.de/boerse/news/corporate-news/asml-holding-stock-gains-as-sales-outlook-reaches-eur-45-billion/70166783)  
  <sub>AD HOC NEWS, 3 hours ago</sub>  
  ASML Holding stock traded at EUR 1510.60 on September 23, 2026, up 64.01 percent year to date. Second quarter sales reached EUR 9.3 billion at a 54 percent...
- [Why Is Bitcoin Price Going Up Today? Rally Defies Every Bearish Catalyst](https://cryptorank.io/news/feed/a1e2b-why-is-bitcoin-price-going-up-today-rally-defies-every-bearish-catalyst)  
  <sub>CryptoRank, 9 hours ago</sub>  
  Bitcoin is trading at $86767.30, up 1.1% over 24 hours and 14.6% over the past week, following a rally that pushed it to $87000, its highest level in eight.
- [ASML Apr 2027 1020.000 put (ASML270416P01020000) interactive stock chart](https://uk.finance.yahoo.com/quote/ASML270416P01020000/chart/)  
  <sub>Yahoo Finance UK, 13 hours ago</sub>  
  Interactive chart for ASML Apr 2027 1020.000 put (ASML270416P01020000) – analyse all of the data with a huge range of indicators.
- [German and Dutch strategic innovation agencies to collaborate on AI chip design](https://www.marketscreener.com/news/german-and-dutch-strategic-innovation-agencies-to-collaborate-on-ai-chip-design-ce785ad9db88fe22)  
  <sub>marketscreener.com, 10 hours ago</sub>  
  A Dutch government agency set up to foster strategic innovation will work with its German counterpart to pursue breakthroughs in AI computer chip design,...
- [3 Undervalued International Stocks for US Investors](https://www.realclearmarkets.com/2026/09/23/3_undervalued_international_stocks_for_us_investors_1207716.html)  
  <sub>RealClearMarkets, 7 hours ago</sub>  
  The ADRs of these wide-moat companies are attractive buys today. Read Full Article ». Related Topics: Taiwan Semiconductor Manufacturing Co Ltd, ASML...
- [South Korea's Kospi Closes Up Nearly 1%, Samsung Electronics Rises Over 3%; Japanese Markets Remain Closed](https://www.tradingkey.com/analysis/stocks/more/262182063-japan-south-korea-stocks-kospi-sk-hynix-samsung-tradingkey)  
  <sub>TradingKey, 8 hours ago</sub>  
  TradingKey - South Korean stocks extended their upward trend today, with the Korea Composite Stock Price Index (KOSPI) closing up 0.90% at 7080.92 points.
- [ASTS Stock Drops 13% After-Hours As Dilution Fears Hit On New Debt Raise](https://stocktwits.com/news-articles/markets/equity/asts-stock-drops-13-after-hours-as-dilution-fears-hit-on-new-debt-raise/cZZPSwVR7rS)  
  <sub>Stocktwits, 22 hours ago</sub>  
  The company said that it intends to raise $1 billion through a private offering of convertible senior notes due February 1, 2034.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.10</summary>

```text
Last close 1,727.73 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 1,686.15 (+2.5%), 50d 1,720.46 (+0.4%), 200d 1,515.42 (+14.0%); 50d above 200d
Momentum: RSI(14) 53.5 | MACD -16.730 vs signal -22.114 (histogram 5.384)
Returns: 1d +1.0% | 5d +8.6% | 1m -2.0% | 3m -2.9%
52-week range: 936.19 - 1,989.44 (now 75.2% of the way up)
Volatility: ATR(14) 53.55 (3.1% of price) | annualised 20d 40.2%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 663.62B
Valuation: trailing P/E 59.19 | forward P/E 29.14 | P/B 1,473.49 | PEG 1.58
Profitability: profit margin 30.1% | operating margin 37.1% | ROE 53.9%
Growth (YoY): revenue +21.3% | earnings +28.5%
Balance sheet: debt/equity 9.1% | free cash flow 8.44B
Risk: beta 1.36 | short interest 0.4% of float
Next earnings: 2026-10-14
```

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.50</summary>

```text
Earnings record, last 4 quarters: 2 beats, 1 in line, 1 missed
  2026-06-30 beat by 9% | 2026-03-31 beat by 7% | 2025-12-31 missed by 5% | 2025-09-30 in line
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
Consensus: strong_buy (mean 1.40 on a 1=strong buy to 5=strong sell scale, 16 analysts)
Ratings: 7 strong buy, 31 buy, 3 hold, 1 sell, 0 strong sell
Price target: mean 2,120.82 (+22.8% vs last close), range 881.94 - 2,824.13
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

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

### Caterpillar (CAT) · Company — BULLISH, confidence 0.55

**Result:** ACCEPTED · 2 shares · submitted buy 2 CAT @ ~805.79, stop 757.24

**In the model's own words:**

> BUY

**Main reasons it gave:**
- Four consecutive earnings beats (31%, 19%, 9%, 8%)
- YoY revenue growth +24% and earnings growth +68% indicating strong growth
- Technical weakness: price below 50‑day SMA and volume at 0.26× 20‑day average
- Analyst consensus buy with mean rating 2.14 and price target +20.9% vs last close

<details><summary><b>News</b> — score +0.00</summary>

- [Caterpillar Inc. (CAT) stock price, news, quote and history - Yahoo Finance](https://sg.finance.yahoo.com/quote/CAT/latest-news/)  
  <sub>Yahoo Finance Singapore, 12 hours ago</sub>  
  Caterpillar (CAT) Down 9.1% Since Last Earnings Report: Can It...
- [Caterpillar vs. Komatsu: Which Heavy Equipment Stock is the Better Buy?](https://www.zacks.com/stock/news/2994628/caterpillar-vs-komatsu-which-heavy-equipment-stock-is-the-better-buy)  
  <sub>Zacks Investment Research, 7 minutes ago</sub>  
  CAT's record backlog, earnings growth and stronger 2026 outlook contrast with KMTUY's tariff costs and profit pressures.
- [Tuesday's session: top gainers and losers in the dow jones index](https://www.chartmill.com/news/CSCO/Chartmill-55185-Tuesdays-session-top-gainers-and-losers-in-the-dow-jones-index)  
  <sub>ChartMill, 20 hours ago</sub>  
  Uncover the latest developments among dow jones stocks in today's session. Stay tuned to the dow jones index's top gainers and losers on Tuesday.
- [IonQ Stock Jumps 12% on Quantum Error-Correction Milestone](https://www.tradingview.com/news/gurufocus:da4482e24094b:0-ionq-stock-jumps-12-on-quantum-error-correction-milestone/)  
  <sub>TradingView, 3 hours ago</sub>  
  IonQ NYSE:IONQ, a full-stack quantum computing company, rose 12.05% in premarket, after it said it had built and tested the first end-to-end real-time...
- [XRX Stock Rises 11.5% in 3 Months: Here's What You Should Know](https://finance.yahoo.com/markets/stocks/articles/xrx-stock-rises-11-5-144000905.html)  
  <sub>Yahoo Finance, 30 minutes ago</sub>  
  Xerox Holdings Corporation XRX stock has gained 11.5% over the past three months, outperforming the industry's 2.8% growth and the Zacks S&P 500 Composite's...
- [12 Communication Services Stocks Moving In Tuesday's After-Market Session](https://www.benzinga.com/trading-ideas/movers/26/09/61935374/12-communication-services-stocks-moving-tuesday-s-after-market-session)  
  <sub>Benzinga, 18 hours ago</sub>  
  Gainers Haoxi Health Technology (NASDAQ:HAO) stock rose 8.8% to $3.09 during Tuesday's after-market session. The market value of their outstanding shares is...
- [Bitcoin Just Broke Its Correlation With Gold, Stocks, and the Dollar: What Changed?](https://cryptorank.io/news/feed/d9411-bitcoin-just-broke-its-correlation-with-gold-stocks-and-the-dollar-what-changed)  
  <sub>CryptoRank, 7 hours ago</sub>  
  Santiment data shows Bitcoin's correlations with stocks, the greenback and gold have weakened sharply over the past few weeks, with BTC now trading far more...
- [Crypto Weekly: Tokenized stock trading exemption, Hormuz exchange sanctioned](https://www.reuters.com/video/watch/idRW451722092026RP1/)  
  <sub>Reuters, 4 hours ago</sub>  
  From a major exemption for tokenized stock trading to sanctions for a crypto exchange linked to Hormuz payments. Sean Hogan rounds up the crypto stories of...
- [Caterpillar stock holds its ground as investors await fresh figures](https://www.ad-hoc-news.de/boerse/news/corporate-news/caterpillar-stock-holds-its-ground-as-investors-await-fresh-figures/70167417)  
  <sub>AD HOC NEWS, 2 hours ago</sub>  
  Caterpillar stock was priced at USD 242.93 on September 21, 2026. September call options at USD 575.00 show a wide valuation gap.
- [Amazon Is Rolling Out Tons of Deals on Pet Supplies Ahead of Its Prime Big Deal Days Event](https://www.islandpacket.com/deals-offers/bargain-hunter/article317341572.html)  
  <sub>Hilton Head Island Packet, 20 hours ago</sub>  
  Bargain Hunter has affiliate partnerships. We receive compensation when you click on a link and make a purchase. Learn more!

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 807.28 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 803.83 (+0.4%), 50d 834.94 (-3.3%), 200d 786.36 (+2.7%); 50d above 200d
Momentum: RSI(14) 47.4 | MACD -9.803 vs signal -13.402 (histogram 3.599)
Returns: 1d -1.1% | 5d +3.0% | 1m -2.5% | 3m -18.0%
52-week range: 463.72 - 1,064.90 (now 57.1% of the way up)
Volatility: ATR(14) 24.28 (3.0% of price) | annualised 20d 25.9%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 371.09B
Valuation: trailing P/E 34.81 | forward P/E 24.93 | P/B 19.13 | PEG 1.43
Profitability: profit margin 14.5% | operating margin 22.2% | ROE 57.0%
Growth (YoY): revenue +24.0% | earnings +68.2%
Balance sheet: debt/equity 232.8% | free cash flow 5.05B
Risk: beta 1.59 | short interest 1.8% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 31% | 2026-03-31 beat by 19% | 2025-12-31 beat by 9% | 2025-09-30 beat by 8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: buy (mean 2.14 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 1 strong buy, 13 buy, 12 hold, 1 sell, 1 strong sell
Price target: mean 975.61 (+20.9% vs last close), range 575.00 - 1,225.00
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

### HDFC Bank (HDB) · Company — BULLISH, confidence 0.55

**Result:** ACCEPTED · 90 shares · submitted buy 90 HDB @ ~23.33, stop 22.23

**In the model's own words:**

> BUY

**Main reasons it gave:**
- Class action lawsuit filing creates legal risk (NEWS)
- Analyst consensus buy with 31.5% upside price target (ANALYST)
- Price below 200d SMA and thin volume indicate bearish technicals (TECHNICALS)
- Strong profit margins and YoY revenue growth (FUNDAMENTALS)
- Earnings record: 2 beats, 2 in line (FUNDAMENTALS)

<details><summary><b>News</b> — score -0.40</summary>

- [HDB Shareholder Alert: HDFC Bank Limited Securities Class Action Lawsuit - Investors With Losses May Contact Levi & Korsinsky](https://www.prnewswire.com/news-releases/hdb-shareholder-alert-hdfc-bank-limited-securities-class-action-lawsuit---investors-with-losses-may-contact-levi--korsinsky-302887147.html)  
  <sub>PR Newswire, 1 hour ago</sub>  
  PRNewswire/ -- Levi & Korsinsky, LLP encourages investors who suffered losses in HDFC Bank Limited (NYSE: HDB) to contact the firm. Those who purchased HDFC...
- [HDFC Bank Limited (HDB) stock price, news, quote and history](https://au.finance.yahoo.com/quote/HDB/)  
  <sub>Yahoo Finance Australia, 16 hours ago</sub>  
  HDFC Bank Limited (HDB) · 4.60% · -0.81% · -7.80% · -35.76% · -33.23% · -35.62% · 3,128.97%. Key events. Baseline. Advanced chart.
- [Kaplan Fox Deadline Alert: HDFC Bank Limited (NYSE: HDB) Investors Have Until October 13, 2026 to Seek a Lead Plaintiff Role](https://www.theglobeandmail.com/investing/markets/stocks/HDB/pressreleases/4755451/kaplan-fox-deadline-alert-hdfc-bank-limited-nyse-hdb-investors-have-until-october-13-2026-to-seek-a-lead-plaintiff-role/)  
  <sub>The Globe and Mail, 3 hours ago</sub>  
  Detailed price information for Hdfc Bank Ltd ADR (HDB-N) from The Globe and Mail including charting and trades.
- [HDB EQUITY ACTION REMINDER: Faruqi & Faruqi, LLP Reminds HDFC Bank Limited Investors of Securities Class Action Lawsuit Deadline on October 12, 2026](https://www.newsfilecorp.com/release/315261/HDB-EQUITY-ACTION-REMINDER-Faruqi-Faruqi-LLP-Reminds-HDFC-Bank-Limited-Investors-of-Securities-Class-Action-Lawsuit-Deadline-on-October-12-2026?lang=fr)  
  <sub>TMX Newsfile, 19 hours ago</sub>  
  Faruqi & Faruqi, LLP Securities Litigation Partner James (Josh) Wilson Encourages Investors Who Suffered Losses In HDFC Bank Limited To...
- [HDFC Bank (NYSE: HDB) to review Sept. 2026 results Oct. 17](https://www.stocktitan.net/sec-filings/HDB/6-k-hdfc-bank-ltd-current-report-foreign-issuer-3d5e07a6ea77.html)  
  <sub>Stock Titan, 24 hours ago</sub>  
  HDFC BANK LTD (HDB) reports that its Board of Directors plans to meet on October 17, 2026 to consider and approve the unaudited standalone and consolidated...
- [HDFC Bank Limited Securities Fraud Class Action Result of](https://www.globenewswire.com/news-release/2026/09/22/3367000/6713/en/hdfc-bank-limited-securities-fraud-class-action-result-of-deceptive-interest-payments-and-approximately-4-stock-decline-investors-may-contact-lewis-kahn-esq-at-kahn-swick-foti-llc.html)  
  <sub>GlobeNewswire, 16 hours ago</sub>  
  HDFC Bank (HDB) Investors Have Opportunity to Lead HDFC Bank Limited Securities Fraud Lawsuit...
- [Pokémon TCG 30th Celebration at Cheers: Elite Trainer Box $89.90 and Ex Tins $49.90 From 1pm Thu 24 Sep, but the ETB Is at Only 4 Stores](https://www.misslobang.com/article/cheers-pokemon-tcg-30th-celebration-sep-2026)  
  <sub>https://www.misslobang.com/, 9 hours ago</sub>  
  Pokémon TCG 30th Celebration at Cheers Singapore, 24 Sep 2026 from 1pm: Poster Collection $34.90, Ex Tin $49.90, Elite Trainer Box $89.90 at 4 stores only.
- [DE: Deere & Company - Stock Price, Quote and News | NYSE](https://techgraph.co/stock-market/quote/de/)  
  <sub>TechGraph, 6 hours ago</sub>  
  685.00 690.00 695.00 700.00 9:30 AM 11:10 AM 12:45 PM 2:25 PM 4:00 PM 704.92 684.01 684.73 703.12. HDB $23.41 -1.01% JPM $340.00 -3.42% JNJ $269.19 -0.10%...
- [Is HDB Undervalued? DCF Says Worth $31](https://www.gurufocus.com/news/9091386/is-hdb-undervalued-dcf-says-worth-31)  
  <sub>GuruFocus, 23 hours ago</sub>  
  On September 22, 2026, we conducted a DCF analysis for HDFC Bank Ltd (HDB), which has seen a challenging price performance recently. The stock is currently...
- [News by CNBC TV18 on TradingView, 2026-09-23 — cnbctv:39a5cd712094b:0](https://www.tradingview.com/news/cnbctv:39a5cd712094b:0/)  
  <sub>TradingView, 7 hours ago</sub>  
  Shares of Bajaj Finance Ltd. gained 2.5% on Wednesday, September 23, as brokerage firm UBS upgraded its recommendation and raised its target price on the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 23.40 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 22.91 (+2.2%), 50d 23.49 (-0.4%), 200d 27.58 (-15.2%); 50d below 200d
Momentum: RSI(14) 53.0 | MACD -0.103 vs signal -0.237 (histogram 0.134)
Returns: 1d -1.1% | 5d +3.6% | 1m -0.8% | 3m -6.5%
52-week range: 21.84 - 37.18 (now 10.2% of the way up)
Volatility: ATR(14) 0.55 (2.3% of price) | annualised 20d 37.4%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 120.30B
Valuation: trailing P/E 16.37 | forward P/E 16.82 | P/B 9.36 | PEG n/a
Profitability: profit margin 26.8% | operating margin 33.3% | ROE 13.8%
Growth (YoY): revenue +16.6% | earnings +18.1%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.40 | short interest 0.7% of float
Next earnings: 2026-10-17
```

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-06-30 in line | 2026-03-31 in line | 2025-12-31 beat by 61% | 2025-09-30 beat by 10%
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

```text
Consensus: buy (mean 1.75 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 1 strong buy, 2 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 30.77 (+31.5% vs last close), range 26.10 - 35.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

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

### JPMorgan Chase (JPM) · Company — BULLISH, confidence 0.55

**Result:** ACCEPTED · 6 shares · submitted buy 6 JPM @ ~337.93, stop 323.48

**In the model's own words:**

> Fundamentals are strong and insider net buying signals confidence, while analyst consensus remains bullish. Technicals are bearish and recent news is mixed (price down despite a $20B partnership), tempering conviction to a moderate level.

**Main reasons it gave:**
- Strong fundamentals: 30% YoY revenue growth, 46.9% earnings growth (Fundamentals)
- Insider net buying of 7.7% of holdings (22 purchases, 969k shares) (Insider Activity)
- Technical downtrend: price 4.2% below 20d/50d SMA, RSI 34.4, volume 0.29x avg (Technicals)
- Analyst consensus buy, mean price target +10.8% vs last close (Analyst View)
- Stock fell 3% on sector rotation despite $20B QIA partnership (News)

<details><summary><b>News</b> — score -0.20</summary>

- [JPMorgan Chase & Co. (JPM) Stock Moves -3.34%: What You Should Know](https://finance.yahoo.com/markets/stocks/articles/jpmorgan-chase-co-jpm-stock-214503311.html)  
  <sub>Yahoo Finance, 17 hours ago</sub>  
  JPMorgan Chase & Co. (JPM) reached $340.29 at the closing of the latest trading day, reflecting a -3.34% change compared to its last close.
- [Why Did IMAX, JPM, CSX Stocks Surge To 52-Week Highs Last Week?](https://stocktwits.com/news-articles/markets/equity/imax-jpm-csx-stocks-52-week-highs-last-week/cZZxcQ3R7C3)  
  <sub>Stocktwits, 7 hours ago</sub>  
  Citi raised the price target on CSX to $54 from $53 and maintained a Neutral rating on the shares, implying an upside of about 1.5% from its last close.
- [Scott Bessent’s Husband Held Up to $250,000 in JPMorgan Stock Misreported as Cash, Ethics Review Found No](https://www.benzinga.com/news/politics/26/09/61938115/scott-bessents-husband-held-up-to-250000-in-jpmorgan-stock-misreported-as-cash-ethics-review-found-no-knowing-violation-report)  
  <sub>Benzinga, 9 hours ago</sub>  
  Treasury Secretary Scott Bessent's husband held between $100,000 and $250,000 of JPMorgan Chase & Co. (NYSE:JPM) stock that was mistakenly listed as cash in...
- [JPMorgan Chase & Co. $JPM Shares Sold by Public Employees Retirement System of Ohio](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-shares-sold-by-public-employees-retirement-system-of-ohio-2026-09-23/)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Public Employees Retirement System of Ohio lessened its stake in shares of JPMorgan Chase & Co. (NYSE:JPM) by 36.0% during the 2nd quarter, according to the...
- [JPMorgan Stock Slips as Traders Shift to Tech Sector](https://www.tradingview.com/news/benzinga:b87e5d573094b:0-jpmorgan-stock-slips-as-traders-shift-to-tech-sector/)  
  <sub>TradingView, 21 hours ago</sub>  
  JPMorgan Chase & Co. (NYSE:JPM) shares are sliding Tuesday as financial stocks broadly sell off, with traders rotating into technology names amid growing...
- [Tuesday's session: top gainers and losers in the dow jones index](https://www.chartmill.com/news/CSCO/Chartmill-55185-Tuesdays-session-top-gainers-and-losers-in-the-dow-jones-index)  
  <sub>ChartMill, 20 hours ago</sub>  
  Uncover the latest developments among dow jones stocks in today's session. Stay tuned to the dow jones index's top gainers and losers on Tuesday.
- [JP Morgan Chase & Co. (JPM) Stock Forecasts](https://ca.finance.yahoo.com/research/reports/MS_0P0000031C_AnalystReport_1790119985000)  
  <sub>Yahoo! Finance Canada, 10 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [JPMorgan Chase & Co. $JPM Shares Sold by Liontrust Investment Partners LLP](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-shares-sold-by-liontrust-investment-partners-llp-2026-09-23/)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Liontrust Investment Partners LLP cut its stake in JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 17.8% in the second quarter, according to its most...
- [JPMorgan Chase Falls 3% Despite New $20B QIA Partnership; Goldman Sachs Eases, Bank of America Slips](https://finance.yahoo.com/markets/stocks/articles/jpmorgan-chase-falls-3-despite-165238714.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  JPMorgan Chase just landed a $20 billion sovereign wealth partnership, yet its stock is leading the big banks lower today. Something bigger than a press...
- [JPMorgan Chase & Co. $JPM Shares Acquired by Empowered Funds LLC](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-shares-acquired-by-empowered-funds-llc-2026-09-23/)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Empowered Funds LLC lifted its holdings in shares of JPMorgan Chase & Co. (NYSE:JPM) by 2.4% during the second quarter, according to the company in its most...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 338.68 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 353.61 (-4.2%), 50d 353.59 (-4.2%), 200d 320.89 (+5.5%); 50d above 200d
Momentum: RSI(14) 34.4 | MACD -1.900 vs signal -0.318 (histogram -1.582)
Returns: 1d -3.8% | 5d -3.9% | 1m -3.7% | 3m +1.4%
52-week range: 282.84 - 365.18 (now 67.8% of the way up)
Volatility: ATR(14) 7.22 (2.1% of price) | annualised 20d 18.7%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.70</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 900.34B
Valuation: trailing P/E 14.52 | forward P/E 13.55 | P/B 2.55 | PEG 1.64
Profitability: profit margin 34.9% | operating margin 50.4% | ROE 17.8%
Growth (YoY): revenue +30.4% | earnings +46.9%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.97 | short interest 1.0% of float
Next earnings: 2026-10-13
```

</details>

<details><summary><b>What this fund holds</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.70</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 4% | 2026-03-31 beat by 8% | 2025-12-31 beat by 3% | 2025-09-30 beat by 4%
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

```text
Consensus: buy (mean 2.08 on a 1=strong buy to 5=strong sell scale, 21 analysts)
Ratings: 4 strong buy, 9 buy, 11 hold, 0 sell, 0 strong sell
Price target: mean 375.14 (+10.8% vs last close), range 305.00 - 436.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.50</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.50</summary>

_Not available today._

</details>

### Procter & Gamble (PG) · Company — BULLISH, confidence 0.55

**Result:** ACCEPTED · 14 shares · submitted buy 14 PG @ ~147.40, stop 142.78

**In the model's own words:**

> Buy

**Main reasons it gave:**
- New Head & Shoulders formulas and expanded Oral‑B iO line launched (product news)
- Price above 20‑, 50‑ and 200‑day SMAs with positive MACD indicating bullish momentum (technical)
- Strong profitability (ROE 30.3%, profit margin 18.4%) and solid free cash flow (fundamentals)
- Analyst consensus remains buy with mean rating 2.20 and price target +8.6% (analyst view)

<details><summary><b>News</b> — score +0.30</summary>

- [Procter & Gamble (PG) Stock Moves 1.45%: What You Should Know](https://finance.yahoo.com/markets/stocks/articles/procter-gamble-pg-stock-moves-215004182.html)  
  <sub>Yahoo Finance, 17 hours ago</sub>  
  Procter & Gamble (PG) closed the most recent trading day at $148.20, moving +1.45% from the previous trading session. At the same time, the Dow lost 0.36%,...
- [New Head And Shoulders Push Could Reframe The Case For P&G Stock](https://simplywall.st/stocks/us/household/nyse-pg/procter-gamble/news/new-head-and-shoulders-push-could-reframe-the-case-for-pg-st)  
  <sub>Simply Wall Street, 1 hour ago</sub>  
  Procter & Gamble recently rolled out Head & Shoulders formulas featuring HydraZinc Complex and broadened its Oral-B iO line, aiming to pair clinically...
- [Procter & Gamble price readies to tackle important resistance - Forecast today - 23-09-2026](https://www.economies.com/stocks/united-states-analysis/procter---gamble-price-readies-to-tackle-important-resistance---forecast-today---23-09-2026-130529)  
  <sub>Economies.com, 3 hours ago</sub>  
  Procter & Gamble (PG) advanced in recent intraday trading as the stock prepares to challenge the $148.50 resistance level. The stock benefited from finding...
- [Will P&G’s (PG) New Science-Led Head & Shoulders and Oral-B iO Push Change Its Narrative?](https://finance.yahoo.com/markets/stocks/articles/p-g-pg-science-led-081758791.html)  
  <sub>Yahoo Finance, 7 hours ago</sub>  
  In recent months, Procter & Gamble has rolled out new Head & Shoulders formulations featuring the HydraZinc Complex and expanded its Oral-B iO line,...
- [Why is Procter & Gamble (NYSE:PG) in focus amid today’s bluechip stocks discussion?](https://kalkinemedia.com/us/stocks/bluechip/why-is-procter-gamble-nysepg-in-focus-amid-todays-bluechip-stocks-discussion)  
  <sub>Kalkine Media, 7 hours ago</sub>  
  Procter & Gamble (NYSE:PG) enters today's market discussion as sector themes, operations, and broader conditions draw attention.
- [Procter & Gamble Company (The) $PG Shares Purchased by State Street Corp](https://www.marketbeat.com/instant-alerts/filing-procter-gamble-company-the-pg-shares-purchased-by-state-street-corp-2026-09-22/)  
  <sub>MarketBeat, 22 hours ago</sub>  
  State Street Corp raised its stake in Procter & Gamble Company (The) (NYSE:PG - Free Report) by 1.0% during the 2nd quarter, according to its most recent...
- [Uncover the latest developments among dow jones stocks in today's session.](https://www.chartmill.com/news/MSFT/Chartmill-55172-Uncover-the-latest-developments-among-dow-jones-stocks-in-todays-session)  
  <sub>ChartMill, 23 hours ago</sub>  
  Stay updated with the movements of the dow jones index in the middle of the day on Tuesday. Discover which stocks are leading as top gainers and losers in...
- [GM's California EV bundle includes a home charger at no extra cost](https://www.stocktitan.net/news/GM/new-pg-e-and-gm-energy-bundle-makes-home-ev-charging-easier-and-more-tjx22uyliu7h.html)  
  <sub>Stock Titan, 2 hours ago</sub>  
  New GM EV buyers at participating Northern and Central California dealers can get a charger worth up to $1999; managed charging may save up to $50 monthly.
- [Procter & Gamble Tokenized Stock price today, PGX to USD chart, marketcap and volume](https://cryptoslate.com/coins/procter-gamble-tokenized-stock/)  
  <sub>CryptoSlate, 7 hours ago</sub>  
  Procter & Gamble Tokenized Stock price is $150.57 on Sep 23, 2026. Market cap $453.52K; 24h volume $36.43K.
- [PG vs. CL: Which Consumer Staples Giant Has Stronger Market Position?](https://www.theglobeandmail.com/investing/markets/stocks/PG/pressreleases/4736657/pg-vs-cl-which-consumer-staples-giant-has-stronger-market-position/)  
  <sub>The Globe and Mail, 23 hours ago</sub>  
  Detailed price information for Procter & Gamble (PG-N) from The Globe and Mail including charting and trades.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 147.87 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 145.69 (+1.5%), 50d 146.09 (+1.2%), 200d 147.47 (+0.3%); 50d below 200d
Momentum: RSI(14) 56.9 | MACD 0.350 vs signal 0.070 (histogram 0.280)
Returns: 1d +1.2% | 5d +0.8% | 1m +2.2% | 3m -2.0%
52-week range: 138.04 - 167.20 (now 33.7% of the way up)
Volatility: ATR(14) 2.31 (1.6% of price) | annualised 20d 14.2%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 343.45B
Valuation: trailing P/E 22.30 | forward P/E 19.98 | P/B 6.44 | PEG 3.74
Profitability: profit margin 18.4% | operating margin 22.1% | ROE 30.3%
Growth (YoY): revenue +1.5% | earnings -15.5%
Balance sheet: debt/equity 64.5% | free cash flow 13.28B
Risk: beta 0.38 | short interest 1.2% of float
Next earnings: 2026-10-22
```

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.10</summary>

```text
Earnings record, last 4 quarters: 4 in line
  2026-06-30 in line | 2026-03-31 in line | 2025-12-31 in line | 2025-09-30 in line
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

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
  - 2026-08-20 PURUSHOTHAMAN BALAJI (Officer): 2,019 shares, 290.31K
(24 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Royal Bank of Canada (RY) · Company — BULLISH, confidence 0.55

**Result:** ACCEPTED · 10 shares · submitted buy 10 RY @ ~201.34, stop 194.59

**In the model's own words:**

> Insider purchases provide a strong bullish signal, while technicals show short‑term weakness that reduces conviction. Analyst consensus is positive, fundamentals are solid but valuation is high, and recent news is mixed but not materially negative.

**Main reasons it gave:**
- Insider purchases: 350k shares on Aug 31 and Aug 28 (total >700k shares)
- Technical bearishness: price below 20‑day/50‑day SMA, RSI 40.9, thin volume (0.18× avg)
- Analyst consensus: buy with price target +3.7% above current price
- Fundamentals: strong profitability (33.9% margin, 16.2% ROE) but high valuation (P/B 2.92, PEG 2.26)

<details><summary><b>News</b> — score -0.10</summary>

- [Royal Bank of Canada (RY) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RY/)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Royal Bank of Canada (RY) · 0.17% · -1.27% · 25.22% · 18.85% · 36.87% · 100.29% · 3,424.00%. Key Events. Baseline. Advanced Chart. Loading chart for...
- [Canadian Bank Stocks Have Soared: Has the Easy Money Already Been Made?](https://www.moomoo.com/news/post/1000045936/canadian-bank-stocks-have-soared-has-the-easy-money-already)  
  <sub>Moomoo, 19 hours ago</sub>  
  Canadianbank stocks have long been an essential portfolio anchor for investors, providing security as well as reliable dividend income and growth.
- [Andra AP fonden Sells 7,700 Shares of Royal Bank Of Canada $RY](https://www.marketbeat.com/instant-alerts/filing-andra-ap-fonden-sells-7700-shares-of-royal-bank-of-canada-ry-2026-09-22/)  
  <sub>MarketBeat, 22 hours ago</sub>  
  Andra AP fonden lessened its position in shares of Royal Bank Of Canada (NYSE:RY - Free Report) (TSE:RY) by 4.9% in the second quarter, according to its...
- [Royal Bank Of Canada (RY) Stock Forecasts](https://finance.yahoo.com/research/reports/MS_0P000004QB_AnalystReport_1790111531000)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [Royal Bank of Canada admits €85m covered bonds to LSE](https://ca.investing.com/news/stock-market-news/royal-bank-of-canada-admits-85m-covered-bonds-to-lse-93CH-4850197)  
  <sub>Investing.com Canada, 25 minutes ago</sub>  
  LONDON - Royal Bank of Canada has admitted €85 million of covered bonds to trading on the London Stock Exchange's main market, according to a press release...
- [Royal Bank of Canada stock slips as capital notes raise $1.1 billion](https://www.ad-hoc-news.de/boerse/news/corporate-news/royal-bank-of-canada-stock-slips-as-capital-notes-raise-1-1-billion/70165917)  
  <sub>AD HOC NEWS, 4 hours ago</sub>  
  Royal Bank of Canada stock closed at CAD 287.17 on September 22, 2026, down 0.85 percent. Fiscal Q3 EPS reached USD 3.07 against USD 2.89 expected.
- [Royal Bank of Canada announces NVCC AT1 Limited Recourse Capital Notes issue](https://www.theglobeandmail.com/investing/markets/stocks/RY/pressreleases/4743200/royal-bank-of-canada-announces-nvcc-at1-limited-recourse-capital-notes-issue/)  
  <sub>The Globe and Mail, 17 hours ago</sub>  
  Detailed price information for Royal Bank of Canada (RY-N) from The Globe and Mail including charting and trades.
- [Rayonier Inc. (RYN) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/RYN/)  
  <sub>Yahoo Finance UK, 4 hours ago</sub>  
  Find the latest Rayonier Inc. (RYN) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Why Is Royal Bank of Canada (TSX:RY) Trending?](https://kalkinemedia.com/ca/stocks/financial/why-is-royal-bank-of-canada-tsxry-trending)  
  <sub>Kalkine Media, 17 hours ago</sub>  
  Explore Financial Stocks trends, competitive factors, and Royal Bank of Canada (TSX:RY) market themes as Canadian investors assess sector growth, valuation,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 202.05 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 205.78 (-1.8%), 50d 208.95 (-3.3%), 200d 185.01 (+9.2%); 50d above 200d
Momentum: RSI(14) 40.9 | MACD -1.337 vs signal -1.044 (histogram -0.294)
Returns: 1d -2.0% | 5d -1.1% | 1m -1.5% | 3m -0.4%
52-week range: 143.64 - 217.87 (now 78.7% of the way up)
Volatility: ATR(14) 3.30 (1.6% of price) | annualised 20d 17.4%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 279.72B
Valuation: trailing P/E 18.02 | forward P/E 15.86 | P/B 2.92 | PEG 2.26
Profitability: profit margin 33.9% | operating margin 46.4% | ROE 16.2%
Growth (YoY): revenue +8.9% | earnings +12.8%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.92 | short interest n/a of float
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

```text
Consensus: buy (mean 2.13 on a 1=strong buy to 5=strong sell scale, 3 analysts)
Ratings: 4 strong buy, 5 buy, 5 hold, 0 sell, 1 strong sell
Price target: mean 209.52 (+3.7% vs last close), range 184.57 - 227.11
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

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
  - 2026-07-31 Royal Bank of Canada (Issuer): 211 shares, 44.11K
  - 2026-07-31 Royal Bank of Canada (Issuer): 140 shares, 29.28K
(105 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.80</summary>

_Not available today._

</details>

### MercadoLibre (MELI) · Company — NEUTRAL, confidence 0.38

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish news and analyst consensus offset by bearish technicals and a weak earnings record; fundamentals are mixed, and insider purchases are modest. Net score is near zero, leading to a neutral stance with low conviction.

**Main reasons it gave:**
- Buy rating from New Street Research with $2450 target (news)
- Price below 20‑day, 50‑day, 200‑day SMAs and RSI 41.3 (technical)
- High valuation (P/E 48.97) but strong revenue growth (+49.8% YoY) (fundamentals)
- Earnings record: 3 misses out of last 4 quarters (earnings)
- Insider purchases: Officer Marcelo bought 124 shares (insider)

<details><summary><b>News</b> — score +0.30</summary>

- [MercadoLibre, Inc. (MELI.VI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/MELI.VI/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Valuation Measures · Market Cap. 80.78B · Enterprise Value. 87.45B · Trailing P/E. 49.51 · Forward P/E. 32.68 · PEG Ratio (5yr expected). 1.00 · Price/Sales (...
- [MercadoLibre (NASDAQ:MELI) Earns Buy Rating from Analysts at New Street Research](https://www.marketbeat.com/instant-alerts/analyst-mercadolibre-nasdaq-meli-earns-buy-rating-from-analysts-at-new-street-research-2026-09-23/)  
  <sub>MarketBeat, 58 minutes ago</sub>  
  New Street Research assumed coverage on shares of MercadoLibre in a research note on Wednesday. They issued a "buy" rating and a $2450.00 target price for...
- [2 Large-Cap Stocks on Our Buy List and 1 We Question](https://stockstory.org/us/stocks/nasdaq/meli/news/buy-or-sell/2-large-cap-stocks-on-our-buy-list-and-1-we-question)  
  <sub>StockStory, 7 hours ago</sub>  
  Large-cap stocks are known for their staying power and ability to weather market storms better than smaller competitors. However, their sheer size makes it...
- [Is MercadoLibre (MELI) Still Worth A Look After Its Ad Engine Gains Share?](https://simplywall.st/stocks/us/retail/nasdaq-meli/mercadolibre/news/is-mercadolibre-meli-still-worth-a-look-after-its-ad-engine)  
  <sub>Simply Wall Street, 8 hours ago</sub>  
  MercadoLibre (MELI) recently highlighted its fast growing ad engine, with updates indicating it now accounts for more than 10% of Latin America's digital...
- [Michael Burry adds fresh shorts in Micron, Nebius, Palantir as chip supply ramps up (MU:NASDAQ)](https://seekingalpha.com/news/4645798-michael-burry-adds-fresh-shorts-in-micron-nebius-palantir-as-chip-supply-ramps-up)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  Michael Burry boosts shorts in Micron, SOXX, Palantir and Nebius, warning the AI/semiconductor boom may fade amid chip glut risks.
- [MercadoLibre, Inc. (MELI) stock price, news, quote and history](https://au.finance.yahoo.com/quote/MELI/latest-news/)  
  <sub>Yahoo Finance Australia, 12 hours ago</sub>  
  1 of Wall Street's Favorite Stocks with Exciting Potential and 2 Facing Headwinds.
- [MELI 260925 2180.00P (MELI260925P2180000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/MELI260925P2180000-US)  
  <sub>Moomoo, 23 hours ago</sub>  
  Track real-time MELI 260925 2180.00P (MELI260925P2180000) stock options chain data and pricing information and news on moomoo App for your options trading...
- [MELI stock heads into the open after a 3.53 percent gain](https://www.ad-hoc-news.de/boerse/news/corporate-news/meli-stock-heads-into-the-open-after-a-3-53-percent-gain/70163899)  
  <sub>AD HOC NEWS, 8 hours ago</sub>  
  At the close on September 22, 2026, MercadoLibre stock reached USD 1824.00 on Nasdaq after trading between USD 1787.28 and USD 1834.53.
- [Oil Prices Surge Nearly 10% — US Forces To Resume Maritime Blockade Against Iran On Tuesday](https://stocktwits.com/news-articles/markets/equity/oil-prices-surge-10-percent-us-forces-to-resume-maritime-blockade-against-iran-on-tuesday/cZmz6rZR7Yo)  
  <sub>Stocktwits, 8 hours ago</sub>  
  The U.S. Central Command said U.S. forces will enforce the blockade on vessels entering or leaving Iranian ports starting July 14 at 4 p.m. ET.
- [Why Is MercadoLibre (NASDAQ:MELI) Standing Out as Traders Parse Sector Signals and Macro Pressure?](https://kalkinemedia.com/us/stocks/growth/why-is-mercadolibre-nasdaqmeli-standing-out-as-traders-parse-sector-signals-and-macro-pressure)  
  <sub>Kalkine Media, 3 hours ago</sub>  
  MercadoLibre (NASDAQ:MELI) stands out as traders parse sector signals and macro pressure. See how e-commerce, logistics and Mercado Pago drive its story.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 1,807.04 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 1,906.77 (-5.2%), 50d 1,875.63 (-3.7%), 200d 1,849.96 (-2.3%); 50d above 200d
Momentum: RSI(14) 41.3 | MACD -19.517 vs signal -1.429 (histogram -18.088)
Returns: 1d -0.7% | 5d -1.2% | 1m -6.0% | 3m +14.1%
52-week range: 1,546.81 - 2,510.97 (now 27.0% of the way up)
Volatility: ATR(14) 58.94 (3.3% of price) | annualised 20d 29.0%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 91.61B
Valuation: trailing P/E 48.97 | forward P/E 32.01 | P/B 11.69 | PEG 1.00
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: buy (mean 1.58 on a 1=strong buy to 5=strong sell scale, 24 analysts)
Ratings: 4 strong buy, 15 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 2,264.88 (+25.3% vs last close), range 1,750.00 - 2,800.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

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

### Elbit Systems (ESLT) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The data set lacks a material, ticker‑specific catalyst. Generic sector news provides no clear direction, technicals show price below key moving averages with low volume, valuation is high relative to modest profitability, and insider activity is neutral. The only positive is a strong earnings record (four consecutive beats), but it does not outweigh the mixed signals, leading to a neutral stance with low conviction.

**Main reasons it gave:**
- No specific ticker‑specific news catalyst; only generic sector headlines
- Price below 50‑day and 200‑day SMA with low volume (0.28x 20‑day avg) indicating weak technical momentum
- High trailing P/E (56.44) and forward P/E (40.79) versus modest profit margins, suggesting limited upside
- Four consecutive earnings beats, indicating strong earnings momentum but not a near‑term catalyst
- Insider activity net small buy but dominated by sales, providing little directional information

<details><summary><b>News</b> — score +0.00</summary>

- [Elbit Systems Ltd. (ESLT) latest stock news and headlines – Yahoo Finance](https://sg.finance.yahoo.com/quote/ESLT/news/)  
  <sub>Yahoo Finance Singapore, 6 hours ago</sub>  
  Elbit Systems Ltd. (ESLT) · 3 Defense Stocks Investors Are Watching As Middle East Risk Puts Aerospace In Focus · 3 Drone Tech Stocks Well-Positioned for Long-...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 748.97 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 722.81 (+3.6%), 50d 762.42 (-1.8%), 200d 765.22 (-2.1%); 50d below 200d
Momentum: RSI(14) 53.8 | MACD -4.097 vs signal -10.941 (histogram 6.844)
Returns: 1d -0.2% | 5d +2.4% | 1m +1.0% | 3m -3.0%
52-week range: 454.95 - 1,014.33 (now 52.6% of the way up)
Volatility: ATR(14) 15.76 (2.1% of price) | annualised 20d 14.5%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 35.10B
Valuation: trailing P/E 56.44 | forward P/E 40.79 | P/B 7.94 | PEG n/a
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

<details><summary><b>What analysts and big funds say</b> — score +0.00</summary>

```text
Consensus: hold (mean 2.67 on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 816.33 (+9.0% vs last close), range 518.00 - 960.00
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

### Alphabet (Google) (GOOGL) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed news: negative AI model delay vs positive fundamentals and analyst outlook; technicals neutral to slightly bearish; no insider activity; earnings record mixed. Overall view is neutral with low conviction.

**Main reasons it gave:**
- AI flagship model Gemini 3.5 Pro delay reported (negative news)
- Strong fundamentals: P/E 17.1, profit margin 54.8% (positive)
- Analyst consensus strong buy with +25.6% price target (positive)
- Technical: price below 20‑day SMA, low volume (neutral/bearish)
- Mixed earnings record: 2 beats, 2 misses, recent miss 4% (neutral/bearish)

<details><summary><b>News</b> — score -0.30</summary>

- [GOOGL Stock Falls 5% As Google’s Flagship AI Model Reportedly Runs Behind Schedule — Why Retail Traders Aren’t Worried](https://stocktwits.com/news-articles/markets/equity/googl-stock-falls-5-percent-googles-flagship-ai-model-runs-behind-schedule-why-retail-traders-arent-worried/cZZEVY5R7sz)  
  <sub>Stocktwits, 5 hours ago</sub>  
  Alphabet Inc. (GOOGL) shares sank nearly 5% on Thursday after a report said Google is months behind schedule in releasing Gemini 3.5 Pro, its flagship...
- [Alphabet (GOOGL) Stock May Be A Bargain After Privacy Fine](https://finance.yahoo.com/markets/stocks/articles/alphabet-googl-stock-may-bargain-011402689.html)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  Alphabet has rewarded long term holders with a very large 3 year return, and with the stock around US$351 at the last close the live question is how well...
- [Nvidia Stock Falls. It Has a Google AI Chip Conundrum.](https://www.barrons.com/articles/nvidia-stock-price-ai-chips-google-2c231d8d)  
  <sub>Barron's, 2 hours ago</sub>  
  A familiar problem is haunting Nvidia. The chip maker's stock has paused in its latest effort to break out to new highs and part of the problem is Google.
- [These 4 Companies Are Monetizing AI Today](https://www.marketbeat.com/articles/these-4-companies-are-monetizing-ai-today/)  
  <sub>MarketBeat, 38 minutes ago</sub>  
  NVIDIA, Microsoft, Alphabet, and Palantir are monetizing AI through distinct moats, from hardware and cloud services to advertising and safety-focused data...
- [Netflix stock is getting shredded — and Google's YouTube may be the reason](https://finance.yahoo.com/markets/stocks/article/netflix-stock-is-getting-shredded--and-googles-youtube-may-be-the-reason-123041480.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  While Netflix (NFLX) execs sit in their ivory tower licking their wounds for not closing the deal for Warner Bros. (WBD) — which will now officially end up...
- [Google (GOOGL) Stock Fails at Resistance as Gemini Growth Meets Spending Concerns](https://www.fxleaders.com/news/2026/09/22/google-googl-stock-fails-at-resistance-as-gemini-growth-meets-spending-concerns/)  
  <sub>FXLeaders, 12 hours ago</sub>  
  Alphabet's latest move above $360 failed to hold as investors weighed Gemini's expansion against rising infrastructure costs, competitive pressure and...
- [Move Over, Alphabet! Warren Buffett's Successor, Greg Abel, Has Nearly $47 Billion Devoted to This Top Investment Idea](https://www.theglobeandmail.com/investing/markets/stocks/GOOGL-Q/pressreleases/4750147/move-over-alphabet-warren-buffett-s-successor-greg-abel-has-nearly-47-billion-devoted-to-this-top-investment-idea/)  
  <sub>The Globe and Mail, 6 hours ago</sub>  
  Detailed price information for Alphabet Cl A (GOOGL-Q) from The Globe and Mail including charting and trades.
- [GOOG stock: why Alphabet’s shares are back in investor focus](https://eciks.org/27913-goog-stock-alphabet-investor-focus)  
  <sub>eciks.org, 18 hours ago</sub>  
  GOOG stock is back in investor focus as renewed attention on Alphabet's AI and a high-profile shareholder shuffle have traders watching into the fall.
- [Bill Ackman ditches a major AI stock after just one quarter](https://www.thestreet.com/investing/stocks/ackman-pershing-square-exit-alphabet-meta-stake)  
  <sub>TheStreet, 23 hours ago</sub>  
  Bill Ackman sold his entire Alphabet position and raised Pershing Square's Meta stake within one quarter, a swap that has paid off through September.
- [GOOGL Stock Inches Up Premarket: Retail Traders Are Buying The Dip After CapEx-Fueled Selloff](https://stocktwits.com/news-articles/markets/equity/googl-stock-inches-up-premarket-retail-traders-are-buying-the-dip-after-cap-ex-fueled-selloff/cZZYAMLR7yW)  
  <sub>Stocktwits, 20 hours ago</sub>  
  The move came as a relief for the stock which has fallen sharply over the last two months.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 341.95 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 341.99 (-0.0%), 50d 345.32 (-1.0%), 200d 337.80 (+1.2%); 50d above 200d
Momentum: RSI(14) 48.3 | MACD 0.342 vs signal -1.024 (histogram 1.365)
Returns: 1d -3.7% | 5d -0.9% | 1m -0.8% | 3m -1.2%
52-week range: 236.57 - 402.62 (now 63.5% of the way up)
Volatility: ATR(14) 8.87 (2.6% of price) | annualised 20d 26.9%
Volume: 0.45x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.90</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 4.18T
Valuation: trailing P/E 17.14 | forward P/E 22.98 | P/B 6.72 | PEG 1.27
Profitability: profit margin 54.8% | operating margin 34.0% | ROE 48.7%
Growth (YoY): revenue +24.2% | earnings +294.0%
Balance sheet: debt/equity 18.9% | free cash flow 22.67B
Risk: beta 1.23 | short interest 1.3% of float
Next earnings: 2026-10-28
```

</details>

<details><summary><b>What this fund holds</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.90</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 missed
  2026-06-30 missed by 4% | 2026-03-31 missed by 3% | 2025-12-31 beat by 4% | 2025-09-30 beat by 29%
```

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

```text
Consensus: strong_buy (mean 1.38 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 13 strong buy, 43 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 429.46 (+25.6% vs last close), range 340.00 - 515.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

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

### Toyota (TM) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> mixed signals – technicals point to short‑term weakness while fundamentals and earnings record are strong; news is ambiguous and no insider activity.

**Main reasons it gave:**
- Price below 20‑day SMA and negative MACD signal bearish short‑term momentum
- Thin trading volume (0.19× 20‑day average) suggests low participation
- Trailing P/E 8.56 and 4‑quarter earnings beat record indicate strong fundamentals
- Mixed news: earnings estimate rise (+2.97% stock) vs Erste Group cuts forecasts
- No insider buying activity in the last 180 days

<details><summary><b>News</b> — score +0.10</summary>

- [A planned knee-pain study will assess weekly shots against a historical 15-injection regimen](https://www.stocktitan.net/news/GCTK/lokahi-therapeutics-tm-and-glucotrack-ceo-erik-emerson-provides-h1it7ndrfbkq.html)  
  <sub>Stock Titan, 2 hours ago</sub>  
  ai² screens over 12000 drug programs and found over 45 assets in year one; LT-100 study start is targeted near term, subject to regulatory feedback.
- [Harvest High Income Shares ETFs Announces September 2026 Distributions](https://www.businesswire.com/news/home/20260923197145/en/Harvest-High-Income-Shares-ETFs-Announces-September-2026-Distributions)  
  <sub>Business Wire, 4 hours ago</sub>  
  Harvest Portfolios Group Inc. (“Harvest”) announces the following distributions for Harvest High Income Shares ETFs TM for the month ending September 30,...
- [Erste Group Bank Reduces Earnings Estimates for Toyota Motor](https://www.marketbeat.com/instant-alerts/estimates-erste-group-bank-reduces-earnings-estimates-for-toyota-motor-2026-09-23/)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Toyota Motor Corporation (NYSE:TM - Free Report) - Equities research analysts at Erste Group Bank reduced their FY2028 earnings per share estimates for...
- [Why does Toyota Motor (NYSE:TM) matter in today's automobile stocks conversation?](https://kalkinemedia.com/us/stocks/automobile/why-does-toyota-motor-nysetm-matter-in-todays-automobile-stocks-conversation)  
  <sub>Kalkine Media, 8 hours ago</sub>  
  A current look at Toyota Motor (NYSE:TM), the market theme driving attention, and the company-specific evidence investors should watch next.
- [Toyota Motor stock gains 2.97 percent as earnings estimates rise](https://www.ad-hoc-news.de/boerse/news/corporate-news/toyota-motor-stock-gains-2-97-percent-as-earnings-estimates-rise/70166192)  
  <sub>AD HOC NEWS, 4 hours ago</sub>  
  TM, US8923313071. Toyota Motor stock gains 2.97 percent as earnings estimates rise. Published on 09/23/2026 at 13:11 | Editorial responsibility: Rafael...
- [Why This Top Automaker's Gamble on V-8 Engines During a Hybrid Boom Actually Makes Sense](https://www.theglobeandmail.com/investing/markets/stocks/TM-N/pressreleases/4745378/why-this-top-automaker-s-gamble-on-v-8-engines-during-a-hybrid-boom-actually-makes-sense/)  
  <sub>The Globe and Mail, 15 hours ago</sub>  
  Detailed price information for Toyota Motor Corp Ord ADR (TM-N) from The Globe and Mail including charting and trades.
- [Onco-Innovations Limited (ONCO.NE) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/ONCO.NE/)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Find the latest Onco-Innovations Limited (ONCO.NE) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Janus Henderson Triton Fund Q2 2026 Commentary (JSMGX)](https://seekingalpha.com/article/4948832-janus-henderson-triton-fund-q2-2026-commentary)  
  <sub>Seeking Alpha, 14 hours ago</sub>  
  Summary. The Fund returned 19.34% and the Russell 2500TM Growth Index returned 24.02%. Stocks delivered strong performance in the second quarter,...
- [In an evaluation, 84% of clinicians said an AI summary could save time. Now 400+ in New Brunswick can use it.](https://www.stocktitan.net/news/HWAIF/healwell-expands-smart-summary-ai-deployment-across-new-d4siygbzsp5b.html)  
  <sub>Stock Titan, 5 hours ago</sub>  
  Every summary claim links to its source record; 79% of evaluated clinicians would recommend the tool. More deployments are planned in Canada and abroad.
- [Decoy Therapeutics, Inc. Issues Correction to Warrant Inducement Transaction Press Release](https://www.tradingview.com/news/prnewswire:64607661b7ece:0-decoy-therapeutics-inc-issues-correction-to-warrant-inducement-transaction-press-release/)  
  <sub>TradingView, 17 hours ago</sub>  
  HOUSTON, Sept. 22, 2026 /PRNewswire/ -- Decoy Therapeutics, Inc. (NASDAQ:DCOY) (the "Company" or "Decoy"), today issued a correction to its press release...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 191.53 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 194.45 (-1.5%), 50d 189.39 (+1.1%), 200d 202.00 (-5.2%); 50d below 200d
Momentum: RSI(14) 48.0 | MACD 0.766 vs signal 1.615 (histogram -0.849)
Returns: 1d -0.5% | 5d -2.0% | 1m -2.9% | 3m +14.5%
52-week range: 166.50 - 248.29 (now 30.6% of the way up)
Volatility: ATR(14) 3.24 (1.7% of price) | annualised 20d 20.3%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 226.81B
Valuation: trailing P/E 8.56 | forward P/E 12.14 | P/B 15.58 | PEG n/a
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

```text
Consensus: strong_buy (mean 1.50 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 2 strong buy, 2 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 234.08 (+22.2% vs last close), range 230.00 - 239.31
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

### Eli Lilly (LLY) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Eli Lilly Keeps Pulling Ahead—Can Novo Nordisk Catch Up?](https://www.marketbeat.com/articles/eli-lilly-keeps-pulling-aheadcan-novo-nordisk-catch-up/)  
  <sub>MarketBeat, 2 hours ago</sub>  
  Eli Lilly leads Novo Nordisk in GLP-1 market share and analyst sentiment, while Novo pins hopes on its CagriSema catalyst and pipeline to offset...
- [VKTX Stock On Track To Beat LLY, NVO This Month After Obesity Drug Data — Can Viking Win Over Wegovy And Zepbound Users?](https://finance.yahoo.com/healthcare/articles/vktx-stock-track-beat-lly-022242899.html)  
  <sub>Yahoo Finance, 13 hours ago</sub>  
  Obesity specialist Lou Aronne said switching from a GLP-1 drug to a dual GLP-1/GIP drug could mean greater weight loss.
- [Eli Lilly Could Be a ‘$2,000 Stock’ in the Next 3 to 4 Years, Says Home Depot Co-Founder Ken Langone](https://www.benzinga.com/markets/equities/26/09/61938783/eli-lilly-could-be-a-2000-stock-in-the-next-3-to-4-years-says-home-depot-co-founder-ken-langone)  
  <sub>Benzinga, 7 hours ago</sub>  
  Home Depot Inc. (NYSE:HD) co-founder Ken Langone stated that Mounjaro maker Eli Lilly and Co. (NYSE:LLY) could reach a $2,000 share price within three to...
- [Why Viking Stock Jumped On Obesity Data. Novo Falls.](https://www.investors.com/news/technology/viking-therapeutics-stock-skyrockets-obesity-drug-data-roche-eli-lilly-novo-fall/)  
  <sub>Investor's Business Daily, 19 hours ago</sub>  
  Viking stock catapulted Tuesday on "stellar" test results for its weight-loss shot, sending shares of rival Novo lower.
- [Why Viking Therapeutics Stock Skyrocketed on Tuesday](https://www.theglobeandmail.com/investing/markets/stocks/LLY-N/pressreleases/4746392/why-viking-therapeutics-stock-skyrocketed-on-tuesday/)  
  <sub>The Globe and Mail, 11 hours ago</sub>  
  Detailed price information for Eli Lilly and Company (LLY-N) from The Globe and Mail including charting and trades.
- [Why is Eli Lilly (NYSE:LLY) in focus amid today’s healthcare stocks discussion?](https://kalkinemedia.com/us/stocks/healthcare/why-is-eli-lilly-nyselly-in-focus-amid-todays-healthcare-stocks-discussion)  
  <sub>Kalkine Media, 4 hours ago</sub>  
  Eli Lilly (NYSE:LLY) enters today's market discussion as sector themes, operations, and broader conditions draw attention.
- [LLY Reiterated by TD Cowen -- Price Target Maintained at $1250](https://www.gurufocus.com/news/9092050/lly-reiterated-by-td-cowen-price-target-maintained-at-1250)  
  <sub>GuruFocus, 20 hours ago</sub>  
  Eli Lilly Analyst Rating Update On October 5, 2023, TD Cowen reiterated its rating for Eli Lilly (LLY) as "Outperform". The firm has maintained its price...
- [Should Eli Lilly (LLY) Investors Watch Its $6.5 Billion Houston GLP 1 Buildout?](https://finance.yahoo.com/healthcare/articles/eli-lilly-lly-investors-watch-211523509.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Eli Lilly (NYSE: LLY) has started construction on a US$6.5b manufacturing facility in Houston to produce its oral GLP-1 drug Foundayo.
- [Nektar Therapeutics drops as jury deliberates in Eli Lilly patent dispute over Rezpeg](https://www.tradingview.com/news/seekingalpha:ab9d876f6094b:0-nektar-therapeutics-drops-as-jury-deliberates-in-eli-lilly-patent-dispute-over-rezpeg/)  
  <sub>TradingView, 20 hours ago</sub>  
  Nektar Therapeutics NASDAQ:NKTR quickly sank 11% as a jury deliberated in its patent dispute with Eli Lilly NYSE:LLY over its Rezpeg drug.
- [TD Cowen reiterates Buy on Eli Lilly stock, $1,250 target on approval](https://ng.investing.com/news/stock-market-news/td-cowen-reiterates-buy-on-eli-lilly-stock-1250-target-on-approval-93CH-2703768)  
  <sub>Investing.com Nigeria, 23 hours ago</sub>  
  Investing.com - TD Cowen reiterated a Buy rating and $1,250 price target on Eli Lilly (NYSE:LLY) stock following the approval of its Inluriyo combination...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,160.35 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 1,154.46 (+0.5%), 50d 1,176.46 (-1.4%), 200d 1,067.57 (+8.7%); 50d above 200d
Momentum: RSI(14) 49.5 | MACD -9.650 vs signal -12.379 (histogram 2.729)
Returns: 1d -0.4% | 5d +2.1% | 1m -7.6% | 3m +4.8%
52-week range: 714.59 - 1,280.34 (now 78.8% of the way up)
Volatility: ATR(14) 30.28 (2.6% of price) | annualised 20d 19.4%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.03T
Valuation: trailing P/E 38.89 | forward P/E 24.51 | P/B 30.53 | PEG 1.15
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
Price target: mean 1,325.39 (+14.2% vs last close), range 930.00 - 1,600.00
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

- [Oppenheimer Boosts Microsoft Price Target to $570 Following Strong Azure and Copilot Growth](https://www.tikr.com/blog/oppenheimer-microsoft-msft-stock-price-target-570-azure-copilot-growth)  
  <sub>TIKR.com, 2 hours ago</sub>  
  Price change for Microsoft stock in last 6 months: 30%; $MSFT Stock Price as of Sep. 22: $498; 52-Week High: $554; $MSFT Stock Price Target: $576.
- [What's Going On With Microsoft Stock Wednesday? - Microsoft (NASDAQ:MSFT)](https://www.benzinga.com/markets/tech/26/09/61940208/microsoft-chases-mass-copilot-adoption-with-deep-discounts-for-large-companies)  
  <sub>Benzinga, 5 hours ago</sub>  
  Microsoft stock rises premarket as MSFT slashes Copilot prices up to 50% for enterprise clients and prepares a new AI "super app."
- [President Trump Sells Millions in Microsoft and Amazon, Buys Nvidia Stock](https://www.tradingview.com/news/gurufocus:3e266d0d0094b:0-president-trump-sells-millions-in-microsoft-and-amazon-buys-nvidia-stock/)  
  <sub>TradingView, 3 hours ago</sub>  
  President Donald Trump's latest financial disclosure shows a series of large technology stock trades in July, with his investment accounts selling sizable...
- [Microsoft Is Cutting 268 Xbox Roles as Activision Takes Over Halo. This Is a Simple Restructuring, Not a Broader Panic Signal for MSFT Stock.](https://www.barchart.com/story/news/4758110/microsoft-is-cutting-268-xbox-roles-as-activision-takes-over-halo-this-is-a-simple-restructuring-not-a-broader-panic-signal-for-msft-stock)  
  <sub>Barchart.com, 18 minutes ago</sub>  
  Microsoft's (MSFT) Xbox business is entering a decisive stage of consolidation even as the company's core financial engine gathers pace. On Sept.
- [4 stocks to watch on Wednesday: NVO, GIS, MSFT, and CBRL (SP500:)](https://seekingalpha.com/news/4645987-4-stocks-to-watch-on-wednesday-nvo-gis-msft-and-cbrl)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Stock index futures were little changed on Tuesday as President Donald Trump raised the prospect of a negotiated end to the U.S. conflict with Iran.
- [MSFT Ticks Up Overnight: Analyst Upgrades To ‘Buy’ And Sees 15% Upside On AI Growth, Cost Discipline](https://finance.yahoo.com/markets/stocks/articles/msft-ticks-overnight-analyst-upgrades-025639017.html)  
  <sub>Yahoo Finance, 12 hours ago</sub>  
  Stifel sees Microsoft sustaining mid-to-high teens revenue growth as Azure supports a broader range of AI models. Improving Azure efficiency, disciplined...
- [Trump Logged 1,156 Trades in One Month and Sold Microsoft. The Reason Is a Tax Strategy You Can Copy.](https://247wallst.com/personal-finance/2026/09/23/trump-logged-1156-trades-in-one-month-and-sold-microsoft-the-reason-is-a-tax-strategy-you-can-copy/)  
  <sub>24/7 Wall St., 1 hour ago</sub>  
  When a president logs over a thousand trades in a single month and unloads shares in some of the world's biggest companies, the real story has nothing to do...
- [What Microsoft’s Trailing Multiple Leaves Out](https://www.trefis.com/stock/msft/articles/616304/what-microsofts-trailing-multiple-leaves-out/2026-09-23)  
  <sub>Trefis, 30 minutes ago</sub>  
  Microsoft (MSFT) has returned about 33% over the past three months, though it is down 3.1% over the past twelve months. Near $500 a share, the stock carries...
- [MSFT Stock Rises Premarket Ahead Of Q4 Results: CapEx, Azure Growth In Focus](https://stocktwits.com/news-articles/markets/equity/msft-stock-rises-premarket-ahead-of-q4-results-cap-ex-azure-growth-in-focus/cZNR8GoRJRW)  
  <sub>Stocktwits, 18 hours ago</sub>  
  Microsoft rose 1% in early premarket trading on Wednesday, ahead of its quarterly report after the markets close. Once one of the key stocks rising in the...
- [3 Tech Stocks Positioned for More Upside if the Sector’s Breakout Holds](https://www.marketbeat.com/articles/3-tech-stocks-positioned-for-more-upside-if-the-sectors-breakout-holds/)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Tech stocks broke out this week as the QQQ neared record highs. Microsoft, Atlassian, and Hewlett Packard Enterprise show supportive fundamentals and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 499.40 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 499.03 (+0.1%), 50d 469.18 (+6.4%), 200d 431.77 (+15.7%); 50d above 200d
Momentum: RSI(14) 55.7 | MACD 6.473 vs signal 8.789 (histogram -2.316)
Returns: 1d -0.4% | 5d +0.5% | 1m +3.3% | 3m +33.6%
52-week range: 352.83 - 542.07 (now 77.5% of the way up)
Volatility: ATR(14) 10.82 (2.2% of price) | annualised 20d 22.6%
Volume: 0.37x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.71T
Valuation: trailing P/E 28.01 | forward P/E 21.09 | P/B 8.38 | PEG 1.63
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
Price target: mean 577.26 (+15.6% vs last close), range 440.00 - 870.00
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

- [2 Undervalued Semiconductor Stocks to Watch While the Market Is Skeptical of AI Growth](https://global.morningstar.com/en-nd/stocks/2-undervalued-semiconductor-stocks-watch-while-market-is-skeptical-ai-growth)  
  <sub>Morningstar, 9 hours ago</sub>  
  Nvidia and Broadcom could still have room to run if their AI-fueled growth lasts longer than investors expect.
- [President Trump Sells Millions in Microsoft and Amazon, Buys Nvidia Stock](https://www.tradingview.com/news/gurufocus:3e266d0d0094b:0-president-trump-sells-millions-in-microsoft-and-amazon-buys-nvidia-stock/)  
  <sub>TradingView, 3 hours ago</sub>  
  President Donald Trump's latest financial disclosure shows a series of large technology stock trades in July, with his investment accounts selling sizable...
- [Nvidia (NVDA) Stock Could Be A Bargain After AI Expansion](https://simplywall.st/stocks/us/semiconductors/nasdaq-nvda/nvidia/news/nvidia-nvda-stock-could-be-a-bargain-after-ai-expansion)  
  <sub>Simply Wall Street, 6 hours ago</sub>  
  NVIDIA has delivered huge returns in recent years, and with the stock most recently closing at US$228.87 the basic question is whether that price is still...
- [Nvidia Stock Set For 40% Surge: 3 Catalysts That Could Drive the Next Big Move](https://finance.yahoo.com/markets/stocks/articles/nvidia-stock-set-40-surge-130024665.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  NVDA earns a BUY with a $310.20 target (~40% upside), driven by the Vera Rubin ramp and $500 billion in mobilized AI infrastructure capital.
- [NVDA Stock Looks 'Remarkably Cheap', Says Wall Street After Beat-And-Raise Q1 — Analyst Sees Nvidia Market Cap Soaring Past $10 Trillion](https://stocktwits.com/news-articles/markets/equity/nvda-stock-remarkably-cheap-after-q1-market-cap-soaring-past-10-trillion/cZXCdOMReFz)  
  <sub>Stocktwits, 5 hours ago</sub>  
  Baird raised its price target for Nvidia to $500 from $300, implying an upside potential of 124% from the stock's closing price on Wednesday. The firm has an '...
- [Not Palantir. Not Micron. The $325 Billion Nvidia Partner That Jim Cramer Just Called a "Must Buy" Stock](https://www.fool.com/investing/2026/09/23/not-palantir-not-micron-the-325-billion-nvidia-par/)  
  <sub>The Motley Fool, 31 minutes ago</sub>  
  Investors have spent the last two years defaulting to the same stocks as proxies for the artificial intelligence (AI) trend. Palantir Technologies (PLTR...
- [NVIDIA Board Member Trades $300.15M In Company Stock](https://www.benzinga.com/news/26/09/61949386/nvidia-board-member-trades-300-15m-company-stock)  
  <sub>Benzinga, 6 minutes ago</sub>  
  It was reported on September 22, that Mark A Stevens, Board Member at NVIDIA (NASDAQ:NVDA) executed a significant insider sell, according to an SEC filing.
- [Nvidia Stock Price Prediction: NVDA Targets and Valuation](https://www.indmoney.com/blog/us-stocks/nvidia-stock-price-prediction)  
  <sub>INDmoney, 3 hours ago</sub>  
  Nvidia stock price prediction: see NVDA analyst targets, valuation, fundamentals, technicals and what our price model implies for the stock.
- [NVDA Stock Eyes the $236 Record High as 2027 NVIDIA Growth Forecasts Rise](https://www.fxleaders.com/news/2026/09/22/nvda-stock-eyes-the-236-record-high-as-2027-nvidia-growth-forecasts-rise/)  
  <sub>FXLeaders, 13 hours ago</sub>  
  NVIDIA stock's recovery toward $236 is supported by Jensen Huang's ambitious 2027 growth outlook, although elevated expectations, heavy infrastructure...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 226.10 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 220.39 (+2.6%), 50d 215.05 (+5.1%), 200d 198.84 (+13.7%); 50d above 200d
Momentum: RSI(14) 56.9 | MACD 1.797 vs signal 1.558 (histogram 0.239)
Returns: 1d -0.6% | 5d +6.6% | 1m +5.3% | 3m +13.0%
52-week range: 165.17 - 235.74 (now 86.3% of the way up)
Volatility: ATR(14) 6.28 (2.8% of price) | annualised 20d 45.5%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 5.46T
Valuation: trailing P/E 28.58 | forward P/E 14.42 | P/B 23.84 | PEG 0.48
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
Price target: mean 327.70 (+44.9% vs last close), range 180.00 - 515.00
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
Last 180 days: bought 2,452,825 shares in 17 transaction(s) | sold 6,389,547 shares in 9
Net: -3,936,722 shares (-0.4% of insider holdings) | insiders hold 965,687,040 shares
Distinct insiders: 0 buying, 4 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-18 STEVENS MARK A (Director): 1,366,000 shares, 300.15M
  - 2026-09-04 STEVENS MARK A (Director): 1,022,239 shares, 235.64M
  - 2026-09-02 STEVENS MARK A (Director): 1,848,501 shares, 410.84M
  - 2026-08-31 TETER TIMOTHY S (General Counsel): 30,000 shares, 6.54M
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

- [Novo Nordisk (NVO) Stock Still Looks Cheap On Earnings Today](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-nvo/novo-nordisk/news/novo-nordisk-nvo-stock-still-looks-cheap-on-earnings-today)  
  <sub>Simply Wall Street, 5 hours ago</sub>  
  Novo Nordisk has seen its share price retreat sharply in recent years, which puts fresh focus on whether today's valuation is still supported by its...
- [Novo Nordisk Stock Slides After Unveiling Long Term Pipeline Growth Targets](https://finance.yahoo.com/markets/stocks/articles/novo-nordisk-stock-slides-unveiling-124126008.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Key Stats for Novo Nordisk StockPrice change for Novo Nordisk stock in last 1 year: -35%$NVO Stock Price as of Sep. 22: $3952-Week High: $64$NVO Stock Price...
- [Novo Nordisk: A Cheap Multiple Can’t Fix Poor Growth (NYSE:NVO)](https://seekingalpha.com/article/4948993-novo-nordisk-a-cheap-multiple-cant-fix-poor-growth)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Novo Nordisk A/S outlook: CMD didn't convince as Street sees 2026 revenue dip. Click for this NVO stock update and see if it is the right stock for you.
- [Eli Lilly Keeps Pulling Ahead—Can Novo Nordisk Catch Up?](https://www.marketbeat.com/articles/eli-lilly-keeps-pulling-aheadcan-novo-nordisk-catch-up/)  
  <sub>MarketBeat, 2 hours ago</sub>  
  To see whether Novo Nordisk NYSE: NVO is closing the gap with competitor Eli Lilly NYSE: LLY in the GLP-1 market, investors need only look at patent-cliff...
- [Video](https://qz.com/video/all?page=108)  
  <sub>qz.com, 2 hours ago</sub>  
  Video. Reporting you can watch: explainers, interviews, and series from the Quartz newsroom. All video · Business News · Leadership · Food...
- [Can Novo's Rare Disease Pipeline Add a New Growth Pillar Beyond GLP-1?](https://www.zacks.com/stock/news/2994481/can-novos-rare-disease-pipeline-add-a-new-growth-pillar-beyond-glp-1)  
  <sub>Zacks Investment Research, 2 hours ago</sub>  
  NVO's rare disease pipeline gains momentum as Frehemgo and Sogroya receive positive CHMP opinions for EU approval, opening new growth opportunities beyond...
- [4 stocks to watch on Wednesday: NVO, GIS, MSFT, and CBRL (SP500:)](https://seekingalpha.com/news/4645987-4-stocks-to-watch-on-wednesday-nvo-gis-msft-and-cbrl)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Stock index futures were little changed on Tuesday as President Donald Trump raised the prospect of a negotiated end to the U.S. conflict with Iran.
- [Trading the Move, Not the Narrative: (NVO) Edition](https://news.stocktradersdaily.com/news_release/23/Trading_the_Move,_Not_the_Narrative:_NVO_Edition_092226085201_1790124721.html)  
  <sub>Stock Traders Daily, 18 hours ago</sub>  
  Key findings for Novo Nordisk A/s (NYSE: NVO). Weak Sentiment Across All Horizons Supports Short Bias; A mid-channel oscillation pattern is in play.
- [Why Viking Stock Jumped On Obesity Data. Novo Falls.](https://www.investors.com/news/technology/viking-therapeutics-stock-skyrockets-obesity-drug-data-roche-eli-lilly-novo-fall/)  
  <sub>Investor's Business Daily, 19 hours ago</sub>  
  Viking stock catapulted Tuesday on "stellar" test results for its weight-loss shot, sending shares of rival Novo (NVO) lower.
- [3 Health Care Stocks With Whale Alerts In Today’s Session](https://www.benzinga.com/markets/options/26/09/61929692/3-health-care-stocks-whale-alerts-today-s-session)  
  <sub>Benzinga, 22 hours ago</sub>  
  This whale alert can help traders discover the next big trading opportunities. Whales are entities with large sums of money and we track their transactions...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 38.50 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 44.41 (-13.3%), 50d 46.49 (-17.2%), 200d 46.06 (-16.4%); 50d above 200d
Momentum: RSI(14) 28.3 | MACD -1.648 vs signal -1.113 (histogram -0.534)
Returns: 1d -3.3% | 5d -9.5% | 1m -17.6% | 3m -18.8%
52-week range: 35.29 - 63.98 (now 11.2% of the way up)
Volatility: ATR(14) 1.41 (3.7% of price) | annualised 20d 43.7%
Volume: 0.64x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 170.04B
Valuation: trailing P/E 9.65 | forward P/E 11.39 | P/B 4.99 | PEG 2.84
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
Price target: mean 46.42 (+20.6% vs last close), range 39.76 - 62.92
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

- [Oppenheimer initiates Teva stock with outperform rating on pipeline](https://www.investing.com/news/analyst-ratings/oppenheimer-initiates-teva-stock-with-outperform-rating-on-pipeline-93CH-4912622)  
  <sub>Investing.com, 4 hours ago</sub>  
  Investing.com - Oppenheimer initiated coverage on Teva Pharmaceutical Industries Ltd. (NYSE:TEVA) with an outperform rating and a price target of $50.00 on...
- [Teva Eyes New Growth Phase After Securing Investment-Grade Ratings](https://finance.yahoo.com/healthcare/articles/teva-eyes-growth-phase-securing-120248772.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Interested in Teva Pharmaceutical Industries Ltd.? Here are five stocks we like better. Teva achieved investment-grade ratings from all three major credit...
- [Oppenheimer Initiates Coverage on Teva Pharmaceutical Industries (NYSE:TEVA)](https://www.marketbeat.com/instant-alerts/analyst-oppenheimer-initiates-coverage-on-teva-pharmaceutical-industries-nyse-teva-2026-09-23/)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Oppenheimer assumed coverage on shares of Teva Pharmaceutical Industries in a research note on Wednesday. They set an "outperform" rating and a $50.00 price...
- [Director’s fund exits Teva Pharmaceutical Industries (TEVA) stake in one-day sale](https://www.stocktitan.net/sec-filings/TEVA/form-4-teva-pharmaceutical-industries-ltd-insider-trading-activity-380c0832b711.html)  
  <sub>Stock Titan, 19 hours ago</sub>  
  TEVA PHARMACEUTICAL INDUSTRIES LTD (TEVA) reported that director Roberto Mignone had an affiliated fund sell 367,600 Ordinary Shares on September 18,...
- [TEVA Oct 2026 42.000 call (TEVA261009C00042000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/TEVA261009C00042000/)  
  <sub>Yahoo Finance UK, 2 hours ago</sub>  
  Find the latest TEVA Oct 2026 42.000 call (TEVA261009C00042000) stock quote, history, news and other vital information to help you with your stock trading...
- [A look at a few stocks](https://www.moomoo.com/community/feed/a-look-at-a-few-stocks-117317971607957)  
  <sub>Moomoo, 13 hours ago</sub>  
  DATE: September 22, 2026 A few stocks iam watching for a breakout or run soon. I own them or in the case of EE iam looking at adding. 1. AURINIA PH...
- [Brian Savage Sells 7,342 Shares of Teva Pharmaceutical Industries (NYSE:TEVA) Stock](https://www.marketbeat.com/instant-alerts/insider-brian-savage-sells-7342-shares-of-teva-pharmaceutical-industries-nyse-teva-stock-2026-09-22/)  
  <sub>MarketBeat, 16 hours ago</sub>  
  Teva Pharmaceutical Industries Ltd. (NYSE:TEVA - Get Free Report) insider Brian Savage sold 7342 shares of the firm's stock in a transaction on Friday,...
- [Teva Pharmaceutical Industries Limited (TEVA) latest press releases and corporate news](https://uk.finance.yahoo.com/quote/TEVA/press-releases/)  
  <sub>Yahoo Finance UK, 6 hours ago</sub>  
  Get the latest Teva Pharmaceutical Industries Limited (TEVA) stock news and headlines to help you in your trading and investment decisions.
- [Teva at Bank of America Global Healthcare Conference: growth takes center stage](https://in.investing.com/news/stock-market-news/teva-at-bank-of-america-global-healthcare-conference-growth-takes-center-stage-93CH-5602613)  
  <sub>Investing.com India, 4 hours ago</sub>  
  Wednesday, 23 September 2026 — Teva Pharmaceutical Industries (TEVA) used the Bank of America Global Healthcare Conference to outline a sharper growth story...
- [Teva Pharmaceutical Industries (NYSE:TEVA) Director Roberto Mignone Sells 367,600 Shares](https://www.marketbeat.com/instant-alerts/insider-teva-pharmaceutical-industries-nyse-teva-director-roberto-mignone-sells-367600-shares-2026-09-22/)  
  <sub>MarketBeat, 18 hours ago</sub>  
  Teva Pharmaceutical Industries Ltd. (NYSE:TEVA - Get Free Report) Director Roberto Mignone sold 367600 shares of the business's stock in a transaction that...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 39.54 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 37.71 (+4.9%), 50d 35.64 (+10.9%), 200d 33.27 (+18.9%); 50d above 200d
Momentum: RSI(14) 62.9 | MACD 0.979 vs signal 0.804 (histogram 0.175)
Returns: 1d -1.3% | 5d +0.8% | 1m +5.9% | 3m +19.1%
52-week range: 18.34 - 40.06 (now 97.6% of the way up)
Volatility: ATR(14) 1.19 (3.0% of price) | annualised 20d 33.1%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 46.12B
Valuation: trailing P/E 67.03 | forward P/E 13.01 | P/B 5.94 | PEG 0.72
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
Consensus: buy (mean 1.67 on a 1=strong buy to 5=strong sell scale, 3 analysts)
Ratings: 2 strong buy, 2 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 43.33 (+9.6% vs last close), range 40.00 - 48.00
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

## Whole-market funds

### Farm goods basket (DBA) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral

**Main reasons it gave:**
- Treasury yields rose modestly across the curve (+0.06 to +0.11) with no policy surprise
- Price above 200‑day SMA (+5.5%) but below 20‑day SMA (‑1.2%); RSI 49.1, MACD negative, volume 0.08× 20‑day average
- Analyst view provides no rating or price target for the fund's holdings
- Fund flows direction unknown; share count change not reported

<details><summary><b>News</b> — score +0.00</summary>

- [DBA: All Agriculture Eyes On Trump-Xi (NYSEARCA:DBA)](https://seekingalpha.com/article/4948661-dba-all-agriculture-eyes-on-trump-xi)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  Invesco DB Agriculture Fund ETF maintains a Hold rating as bullish sentiment and geopolitical catalysts drive recent outperformance.
- [Invesco DB Agriculture Fund ETF holds steady am...](https://pluang.com/en/news-feed/dbainvesco-dba-semua-pertanian-mengamati-trump-xi)  
  <sub>Pluang, 23 hours ago</sub>  
  The Invesco DB Agriculture Fund ETF (DBA) maintains a Hold rating as it has shown strong year-to-date returns of 12.4%, closely tracking the S&P 500.
- [Exchange Traded Concepts and xETFs Launch NECK, an ETF Targeting the Critical Constraints Shaping AI Growth](https://www.tradingview.com/news/prnewswire:0616da2060f34:0-exchange-traded-concepts-and-xetfs-launch-neck-an-etf-targeting-the-critical-constraints-shaping-ai-growth/)  
  <sub>TradingView, 3 hours ago</sub>  
  Actively managed xETFs AI Bottlenecks ETF focuses on memory, networking, power, compute and other areas where demand may be outpacing supplyOKLAHOMA CITY,...
- [AI needs memory, power and data centers. A new fund targets those pressure points.](https://www.stocktitan.net/news/NECK/exchange-traded-concepts-and-x-et-fs-launch-neck-an-etf-targeting-bzqskur87k34.html)  
  <sub>Stock Titan, 3 hours ago</sub>  
  Exchange Traded Concepts and xETFs launched the xETFs AI Bottlenecks ETF (NYSE Arca: NECK), an actively managed fund targeting companies positioned around...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 28.55 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 28.89 (-1.2%), 50d 28.28 (+1.0%), 200d 27.07 (+5.5%); 50d above 200d
Momentum: RSI(14) 49.1 | MACD 0.088 vs signal 0.202 (histogram -0.113)
Returns: 1d -0.5% | 5d -1.1% | 1m +0.8% | 3m +7.3%
52-week range: 25.44 - 29.49 (now 76.8% of the way up)
Volatility: ATR(14) 0.31 (1.1% of price) | annualised 20d 14.8%
Volume: 0.08x the 20-day average
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
Three-year record: +13.9% a year | beta to the market 0.35
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
Shares outstanding: 27.60M | fund size: 787.96M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- No macro surprise: yields up modestly, dollar up, VIX low
- Technicals show price above 20‑day, 50‑day, 200‑day SMAs but MACD histogram negative
- Energy inventories mixed: crude draw (-0.6 mb) bullish, gas build (+44 bcf) bearish
- EIA price outlook mixed: oil forecast down ~10% over 6 months, gas up ~7% over 6 months

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 32.61 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 32.24 (+1.1%), 50d 30.66 (+6.4%), 200d 27.79 (+17.3%); 50d above 200d
Momentum: RSI(14) 58.9 | MACD 0.718 vs signal 0.813 (histogram -0.095)
Returns: 1d +0.1% | 5d -3.2% | 1m +4.3% | 3m +20.2%
52-week range: 22.07 - 33.68 (now 90.8% of the way up)
Volatility: ATR(14) 0.46 (1.4% of price) | annualised 20d 19.2%
Volume: 0.22x the 20-day average
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
Three-year record: +13.8% a year | beta to the market 1.05
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
US inventories, week ending 2026-09-11 (published the following Wednesday)
  Crude oil: 423.4 million barrels, -0.6 on the week (a draw), 38% percentile over 52 weeks
  Natural gas: 3,298.0 billion cubic feet, +44.0 on the week (a build), 71% percentile over 52 weeks
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 54.45M | fund size: 1.78B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, no decisive technical break on volume, fundamentals stable, fund‑flow data unavailable.

**Main reasons it gave:**
- US Treasury yields rose modestly (10‑year +0.06% week) with no policy surprise
- Technical indicators show downtrend (price below 20‑day, 50‑day, 200‑day SMAs) but no decisive break on volume (volume 0.43× 20‑day average)
- Fundamentals stable: yield 5.9%, credit quality BB/B, three‑year record +8.4% per year
- Fund flows data unavailable (direction unknown, share count change n/a)

<details><summary><b>News</b> — score +0.00</summary>

- [HYI: High Yield Exposure At A Deep Discount (NYSE:HYI)](https://seekingalpha.com/article/4948987-hyi-high-yield-exposure-at-a-deep-discount)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Western Asset High Yield Opportunity Fund is a non-leveraged CEF trading at a relatively wider discount. Read more on HYI here.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 78.32 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 79.04 (-0.9%), 50d 79.34 (-1.3%), 200d 80.01 (-2.1%); 50d below 200d
Momentum: RSI(14) 33.1 | MACD -0.294 vs signal -0.248 (histogram -0.046)
Returns: 1d -0.5% | 5d -0.1% | 1m -1.6% | 3m -1.9%
52-week range: 78.32 - 81.32 (now 0.0% of the way up)
Volatility: ATR(14) 0.24 (0.3% of price) | annualised 20d 4.5%
Volume: 0.43x the 20-day average
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
Three-year record: +8.4% a year | beta to the market 0.67
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 206.39M | fund size: 16.17B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- Treasury yields rose modestly across the curve (+0.06% on 10‑yr) with no policy surprise
- Technicals: price below 20‑day (291.06) and 50‑day (294.74) SMAs, RSI 35.5, no decisive breakout
- Analyst coverage thin (1.7% of fund) despite 100% buy rating and +23.3% price target
- CFTC positioning shows net short 19.6% of open interest, up 6% week‑over‑week, indicating modest bearish crowding

<details><summary><b>News</b> — score +0.00</summary>

- [Goldman’s Chris Lucas: Small Caps Are Becoming a Flow Problem](https://thedarksideoftheboom.substack.com/p/goldmans-chris-lucas-small-caps-are)  
  <sub>The Dark Side Of The Boom, 12 hours ago</sub>  
  Goldman Sachs ETF specialist Chris Lucas describes the rotation across the small-cap ETF complex as “striking.” The weakness is no longer simply a relative...
- [Exchange-Traded Funds Rise, US Equities Mixed After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-rise-us-171035923.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV edged higher. Actively traded Invesco QQQ Trust (QQQ) added 0.5%.
- [One of These S&P 500 Funds Has Trailed for 10 Years. Its Fans Say That’s the Point.](https://247wallst.com/investing/etf/2026/09/23/one-of-these-sp-500-funds-has-trailed-for-10-years-its-fans-say-thats-the-point/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  The gap in returns of two nearly identical stocks S&P 500 funds tells a story about what most investors misunderstand about diversification.
- [Nasdaq 100 Flirts with Records, Oil Sinks for Fifth Day: Stock Market Today](https://www.tradingview.com/news/benzinga:de108ba70094b:0-nasdaq-100-flirts-with-records-oil-sinks-for-fifth-day-stock-market-today/)  
  <sub>TradingView, 21 hours ago</sub>  
  The Nasdaq 100 carved out a fresh intraday record by midday Tuesday as the artificial intelligence trade powered ahead.Speaking at the United Nations...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 283.82 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 291.06 (-2.5%), 50d 294.74 (-3.7%), 200d 275.20 (+3.1%); 50d above 200d
Momentum: RSI(14) 35.5 | MACD -3.491 vs signal -2.729 (histogram -0.762)
Returns: 1d -0.6% | 5d -0.5% | 1m -5.4% | 3m -3.9%
52-week range: 229.11 - 305.09 (now 72.0% of the way up)
Volatility: ATR(14) 3.45 (1.2% of price) | annualised 20d 11.5%
Volume: 0.39x the 20-day average
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
Three-year record: +18.8% a year | beta to the market 1.24
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

<details><summary><b>What analysts and big funds say</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.10</summary>

```text
Rolled up from the 5 largest holdings, 1.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.3% above the current prices
Holdings read: FROG, MOG-A, XTSLA, UMBF, GKOS
Recent rating changes among them:
  - FROG: 2026-09-04 DA Davidson: main, Buy -> Buy
  - MOG-A: 2026-09-15 Guggenheim: init, ? -> Neutral
  - UMBF: 2026-09-14 UBS: init, ? -> Neutral
  - GKOS: 2026-09-22 Jefferies: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.15</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 19.6% of open interest (496,762 contracts)
Change on the week: +6.0% of open interest
Crowding: 30% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 281.05M | fund size: 79.77B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, technicals not decisive, flows unknown, fundamentals modestly positive but not compelling enough to outweigh macro risk.

**Main reasons it gave:**
- US Treasury yields rose modestly (10y +0.06% week) with no surprise
- LQD technicals show downtrend below SMAs, RSI 36.9, low volume, no decisive break
- Fund flows direction unknown, share count change n/a
- Fund fundamentals solid (yield 4.7%, credit quality A 46.6% BBB 40.2%, expense ratio 0.14%) but not compelling enough to outweigh macro risk

<details><summary><b>News</b> — score +0.00</summary>

- [CORP: Well-Rounded ETF In Corporate Bonds, But Not Low-Cost (NYSEARCA:CORP)](https://seekingalpha.com/article/4948656-corp-well-rounded-etf-in-corporate-bonds-but-not-low-cost)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  The PIMCO Investment Grade Corporate Bond Index ETF offers broad exposure to USD-denominated investment-grade corporate bonds with a 5.43% SEC yield and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 104.18 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 105.31 (-1.1%), 50d 106.02 (-1.7%), 200d 108.73 (-4.2%); 50d below 200d
Momentum: RSI(14) 36.9 | MACD -0.487 vs signal -0.477 (histogram -0.009)
Returns: 1d -0.9% | 5d -0.1% | 1m -1.6% | 3m -4.3%
52-week range: 104.18 - 112.92 (now 0.0% of the way up)
Volatility: ATR(14) 0.55 (0.5% of price) | annualised 20d 7.0%
Volume: 0.36x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Corporate Bond
Yield: 4.7%
Credit quality: A 46.6%, BBB 40.2%, AA 12.3%, AAA 1.0%
Three-year record: +5.2% a year | beta to the market 1.35
Cost and size: expense ratio 0.14% | net assets 32.04B
What it is made of: Bonds 98.9%, Cash 1.1%, Convertible 0.0%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 1.0%
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
Shares outstanding: 306.32M | fund size: 31.91B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No clear macro surprise, no decisive technical break, and mixed signals from positioning and fundamentals lead to a neutral stance.

**Main reasons it gave:**
- Large speculators net short 29.2% of open interest, up 0.5% week, crowding at 95th percentile
- Fund has AA 100% credit quality, 3.6% yield and low 0.15% expense ratio
- RSI 28.8 (oversold) and price below 20‑day, 50‑day and 200‑day SMAs
- Treasury yields rose modestly (10‑yr +6bps, 5‑yr +11bps) and VIX low at 14.5

<details><summary><b>News</b> — score +0.00</summary>

- [iShares 20+ Year Treasury Bond ETF (TLT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TLT/)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  Find the latest iShares 20+ Year Treasury Bond ETF (TLT) stock quote, history, news and other vital information to help you with your stock trading and...
- [Advanced AI-Powered Crypto Investment Research Platform](https://sosovalue.com/ru/assets/etf/us-btc-spot)  
  <sub>SoSoValue, 16 hours ago</sub>  
  Добро пожаловать в SoSoValue — бесплатную платформу криптовалютной аналитики. Отслеживайте в реальном времени цены, потоки ETF и тренды Web 3.0 с помощью...
- [Vanguard's All-World ETF Hits Fresh Peak Days Before September Payout Lands](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/vanguard-s-all-world-etf-hits-fresh-peak-days-before-september-payout/70167821)  
  <sub>AD HOC NEWS, 1 hour ago</sub>  
  Vanguard's All-World ETF reached a 52-week high of 164.98 euros as its distributing share class prepares a September 30 payout of 0.543371 dollars per unit.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.18 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 81.58 (-0.5%), 50d 81.79 (-0.8%), 200d 82.33 (-1.4%); 50d below 200d
Momentum: RSI(14) 28.8 | MACD -0.182 vs signal -0.149 (histogram -0.033)
Returns: 1d -0.1% | 5d -0.2% | 1m -1.0% | 3m -1.0%
52-week range: 81.18 - 83.18 (now 0.0% of the way up)
Volatility: ATR(14) 0.10 (0.1% of price) | annualised 20d 2.0%
Volume: 0.26x the 20-day average
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
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 29.2% of open interest (4,433,736 contracts)
Change on the week: +0.5% of open interest
Crowding: 95% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 319.03M | fund size: 25.90B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: modest analyst bullishness offset by slight insider bearishness and mixed technicals, with no macro surprise.

**Main reasons it gave:**
- Analyst coverage of top holdings (11.4% of fund) shows 65.7% buy rating and +15.3% price target
- CFTC positioning shows crowded long (95th percentile) with net long 4.7% and slight reduction (-0.4% OI)
- Technical indicators: price below 20‑day and 50‑day SMAs, RSI 38.6, MACD negative
- Europe energy crisis news raises risk for European equities

<details><summary><b>News</b> — score +0.00</summary>

- [Vanguard FTSE Emerging Markets Index Fund ETF Shares (VWO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/VWO/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Find the latest Vanguard FTSE Emerging Markets Index Fund ETF Shares (VWO) stock quote, history, news and other vital information to help you with your...
- [Europe Entering Another Energy Crisis, Markets Might See A Repeat Of 2022 Selloff (SPY)](https://seekingalpha.com/article/4948698-europe-entering-another-energy-crisis-markets-might-see-a-repeat-of-2022-selloff)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  European gas inventories hit 2021 lows, raising 2022-style selloff risk amid a diesel crisis. Click to read what investors need to know.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 88.36 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 90.49 (-2.4%), 50d 90.57 (-2.5%), 200d 87.42 (+1.1%); 50d above 200d
Momentum: RSI(14) 38.6 | MACD -0.709 vs signal -0.435 (histogram -0.274)
Returns: 1d -1.0% | 5d -0.7% | 1m -4.7% | 3m +1.4%
52-week range: 77.90 - 93.19 (now 68.4% of the way up)
Volatility: ATR(14) 0.92 (1.0% of price) | annualised 20d 11.7%
Volume: 0.25x the 20-day average
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
Three-year record: +18.6% a year | beta to the market 0.90
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
Weighted price target: +15.3% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, NOVN.SW, SHEL.L
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.15</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 4.7% of open interest (626,488 contracts)
Change on the week: -0.4% of open interest
Crowding: 95% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 441.87M | fund size: 39.04B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral

**Main reasons it gave:**
- Analyst view: 100% buy rating on top holdings with +34.3% price target (22.2% coverage)
- CFTC positioning: net long fell by -0.9% week over week
- Technicals: RSI 51.4, price just below 20‑day SMA, MACD histogram negative
- Macro data: inflation 3.4% and Fed policy unchanged, no surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Vanguard FTSE Emerging Markets Index Fund ETF Shares (VWO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/VWO/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Vanguard FTSE Emerging Markets Index Fund ETF Shares (VWO) · 3.17% · 1.08% · 16.25% · 13.65% · 13.00% · 20.49% · 142.94%. Key Events. Baseline. Advanced Chart.
- [Better Vanguard International ETF: VEA Targeting Developed Markets vs. VWO's Emerging Markets Focus](https://www.fool.com/coverage/etfs/2026/09/22/better-vanguard-international-etf-vea-targeting-developed-markets-vs-vwo-s-emerging-markets-focus/)  
  <sub>The Motley Fool, 17 hours ago</sub>  
  VEA concentrates on established economies with lower costs and higher income, while VWO pursues growth in developing nations with greater tech exposure and...
- [EPU: Hold But Stay Underweight (NYSEARCA:EPU)](https://seekingalpha.com/article/4948907-epu-hold-but-stay-underweight)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  iShares MSCI Peru and Global Exposure ETF is a top emerging market ETF, but Peru's outlook is uncertain. Click here to read more on EPU here.
- [ETFs Investing in Kingboard Holdings Limited Stocks](https://www.tradingview.com/symbols/FWB-KGZ/etfs/)  
  <sub>TradingView, 16 hours ago</sub>  
  Explore funds investing in KGZ in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 60.35 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 60.47 (-0.2%), 50d 59.75 (+1.0%), 200d 57.73 (+4.5%); 50d above 200d
Momentum: RSI(14) 51.4 | MACD 0.048 vs signal 0.091 (histogram -0.043)
Returns: 1d -1.3% | 5d +1.9% | 1m -0.2% | 3m +1.7%
52-week range: 52.42 - 61.44 (now 88.0% of the way up)
Volatility: ATR(14) 0.67 (1.1% of price) | annualised 20d 13.9%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Diversified Emerging Mkts
What it holds: P/E 15.91 | P/B 2.13 | P/S 1.86 | 3y earnings growth n/a
Yield: 2.3%
Three-year record: +19.3% a year | beta to the market 0.75
Cost and size: expense ratio 0.06% | net assets 168.36B
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 22.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +34.3% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 2308.TW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 3.3% of open interest (1,310,241 contracts)
Change on the week: -0.9% of open interest
Crowding: 37% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 1.42B | fund size: 85.59B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 93.10 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 94.06 (-1.0%), 50d 94.63 (-1.6%), 200d 95.65 (-2.7%); 50d below 200d
Momentum: RSI(14) 37.4 | MACD -0.441 vs signal -0.406 (histogram -0.035)
Returns: 1d -0.7% | 5d +0.1% | 1m -1.7% | 3m -3.3%
52-week range: 92.95 - 97.74 (now 3.1% of the way up)
Volatility: ATR(14) 0.43 (0.5% of price) | annualised 20d 6.2%
Volume: 0.43x the 20-day average
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
Three-year record: +9.5% a year | beta to the market 1.08
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
Shares outstanding: 159.90M | fund size: 14.89B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [iShares 20+ Year Treasury Bond ETF (TLT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TLT/)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  Find the latest iShares 20+ Year Treasury Bond ETF (TLT) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 90.44 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 91.84 (-1.5%), 50d 92.64 (-2.4%), 200d 94.74 (-4.5%); 50d below 200d
Momentum: RSI(14) 31.4 | MACD -0.609 vs signal -0.528 (histogram -0.082)
Returns: 1d -0.8% | 5d -0.4% | 1m -2.6% | 3m -3.9%
52-week range: 90.44 - 97.99 (now 0.0% of the way up)
Volatility: ATR(14) 0.42 (0.5% of price) | annualised 20d 6.0%
Volume: 0.44x the 20-day average
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
Three-year record: +3.4% a year | beta to the market 1.16
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
Shares outstanding: 460.82M | fund size: 41.68B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [One of These S&P 500 Funds Has Trailed for 10 Years. Its Fans Say That’s the Point.](https://247wallst.com/investing/etf/2026/09/23/one-of-these-sp-500-funds-has-trailed-for-10-years-its-fans-say-thats-the-point/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  The gap in returns of two nearly identical stocks S&P 500 funds tells a story about what most investors misunderstand about diversification.
- [Invesco Ltd. (IVZ) latest press releases and corporate news](https://sg.finance.yahoo.com/quote/IVZ/press-releases/)  
  <sub>Yahoo Finance Singapore, 2 hours ago</sub>  
  Get the latest Invesco Ltd. (IVZ) stock news and headlines to help you in your trading and investment decisions.
- [From cash management to core holdings: How pensions use ETFs](https://www.invesco.com/us/en/insights/etf-adoption-for-pensions.html)  
  <sub>Invesco, 21 hours ago</sub>  
  Learn how pension funds are deploying ETFs across their portfolios and how new use cases are influencing investment implementation and allocation decisions.
- [For the first time, Invesco's QQQ innovation suite has an international ETF.](https://www.stocktitan.net/news/IVZ/the-invesco-qqq-innovation-suite-expands-with-the-launch-of-invesco-o76ad69a9f4z.html)  
  <sub>Stock Titan, 2 hours ago</sub>  
  Invesco (IVZ) has expanded its Invesco QQQ Innovation Suite with the launch of the Invesco Nasdaq International Innovators 100 ETF (QQI), the suite's first...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 212.21 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 216.59 (-2.0%), 50d 217.18 (-2.3%), 200d 205.05 (+3.5%); 50d above 200d
Momentum: RSI(14) 36.7 | MACD -1.702 vs signal -1.109 (histogram -0.594)
Returns: 1d -0.2% | 5d -0.8% | 1m -4.3% | 3m +1.6%
52-week range: 182.18 - 222.77 (now 74.0% of the way up)
Volatility: ATR(14) 1.82 (0.9% of price) | annualised 20d 8.7%
Volume: 0.43x the 20-day average
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
Three-year record: +15.9% a year | beta to the market 0.83
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
Weighted price target: -1.6% above the current prices
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
Shares outstanding: 475.10M | fund size: 100.82B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Goldman Sachs wants C++ specialists for a new high-frequency market making team](https://www.efinancialcareers.com/news/goldman-sachs-wants-c-specialists-for-a-new-high-frequency-market-making-team)  
  <sub>eFinancialCareers, 23 hours ago</sub>  
  Goldman wants some of Jane Street's pie.
- [İş Yatırım Details Market-Making Activity in ISMDL ETF](https://www.tipranks.com/news/company-announcements/is-yatirim-details-market-making-activity-in-ismdl-etf)  
  <sub>TipRanks, 38 minutes ago</sub>  
  Is Yatirim Menkul Degerler AS ( ($TR:ISMEN) ) has shared an update. İş Yatırım Menkul Değerler A.Ş., acting as market maker for the ISMDL exchange-traded...
- [3 Best Vanguard ETFs Built for Steady Dividend Income](https://www.tipranks.com/news/3-best-vanguard-etfs-built-for-steady-dividend-income)  
  <sub>TipRanks, 39 minutes ago</sub>  
  Dividend investing is an easy way to earn regular income. Many investors choose steady dividend-paying companies, and Vanguard ETFs offer a low-cost option...
- [VOO vs. VOOG: Which Vanguard ETF Fits Your Portfolio Better?](https://www.tipranks.com/news/voo-vs-voog-which-vanguard-etf-fits-your-portfolio-better)  
  <sub>TipRanks, 6 hours ago</sub>  
  Vanguard's ETFs are popular among U.S. investors for their low fees and broad market exposure. The Vanguard SP 500 ETF ($VOO) and Vanguard SP 500 Growth E..
- [Is Yatirim Details ISX30 ETF Market-Making Activity](https://www.tipranks.com/news/company-announcements/is-yatirim-details-isx30-etf-market-making-activity)  
  <sub>TipRanks, 38 minutes ago</sub>  
  Is Yatirim Menkul Degerler AS ( ($TR:ISMEN) ) has issued an announcement. Is Yatirim Menkul Degerler AS, a key player in Turkey's capital markets,...
- [Is Yatirim Reports No Market-Making Activity in ISGLK ETF on 22 September](https://www.tipranks.com/news/company-announcements/is-yatirim-reports-no-market-making-activity-in-isglk-etf-on-22-september)  
  <sub>TipRanks, 38 minutes ago</sub>  
  Is Yatirim Menkul Degerler AS ( ($TR:ISMEN) ) has shared an announcement. Is Yatirim Menkul Degerler AS reported that it conducted no market-making...
- [Why Is the Roundhill Memory ETF (DRAM) Rising Today, Sept. 17?](https://www.tipranks.com/news/why-is-the-roundhill-memory-etf-dram-rising-today-sept-17)  
  <sub>TipRanks, 14 hours ago</sub>  
  Roundhill Memory ETF ($DRAM) is up more than 4% as of this writing on Thursday, as memory and semiconductor stocks continue to gain momentum.
- [3 Top ETFs with 12% or More Upside, According to AI Analyst](https://www.tipranks.com/news/3-best-buy-etfs-with-12-or-more-upside-according-to-ai-analyst)  
  <sub>TipRanks, 15 hours ago</sub>  
  Exchange-traded funds (ETFs) remain a key way to capture growth opportunities in the market. Investors seeking exposure to industries such as tech,...
- [Associate Global Partners Director Increases ETF Holdings via Dividend Reinvestment](https://www.tipranks.com/news/company-announcements/associate-global-partners-director-increases-etf-holdings-via-dividend-reinvestment)  
  <sub>TipRanks, 14 hours ago</sub>  
  Contango Asset Management Ltd. ( ($AU:APL) ) has shared an update. Associate Global Partners Limited reported a minor change in director Jason Craig...
- [Ethereum Income ETF NEHI Attracts Fresh Cash as ETH Rally Supercharges Yield Play](https://www.tipranks.com/news/cryptocurrencies/ethereum-income-etf-nehi-attracts-fresh-cash-as-eth-rally-supercharges-yield-play)  
  <sub>TipRanks, 13 hours ago</sub>  
  Ethereum Income Fund Pulls Fresh Capital as Crypto Rally Deepens The NEOS Ethereum High Income ETF, NEHI, drew $1241284 in new money on September 18, 2026,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 105.01 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 106.43 (-1.3%), 50d 107.02 (-1.9%), 200d 109.57 (-4.2%); 50d below 200d
Momentum: RSI(14) 30.1 | MACD -0.534 vs signal -0.418 (histogram -0.116)
Returns: 1d -0.6% | 5d -0.7% | 1m -2.0% | 3m -3.6%
52-week range: 105.01 - 112.20 (now 0.0% of the way up)
Volatility: ATR(14) 0.39 (0.4% of price) | annualised 20d 4.6%
Volume: 0.25x the 20-day average
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
Three-year record: +3.9% a year | beta to the market 0.68
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
Shares outstanding: 142.60M | fund size: 14.97B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [iShares 20+ Year Treasury Bond ETF (TLT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TLT/)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  iShares 20+ Year Treasury Bond ETF (TLT) · 1.29% · -0.37% · -4.75% · -6.95% · -7.84% · -46.14% · 0.00%. Key...
- [Is 60/40 Dead? With BNDW's YTM For Me It Has Just Risen Again](https://seekingalpha.com/article/4948918-is-6040-dead-with-bndws-ytm-for-me-it-has-just-risen-again)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  BNDW's global, investment-grade exposure, 51% US, 41% foreign, diversifies risk beyond classic government bonds. Read why BNDW ETF is a hold.
- [This 2X ETF Was Made for Higher Interest Rates. Should You Buy Before the Next Fed Hike?](https://247wallst.com/investing/etf/2026/09/22/this-2x-etf-was-made-for-higher-interest-rates-should-you-buy-before-the-next-fed-hike/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  The Fed raised rates and TBT barely flinched, which raises an uncomfortable question for anyone betting on more hikes: being right about the direction still...
- [2X inverse Treasury ETF TBT struggles despite F...](https://pluang.com/en/news-feed/etf-2x-untuk-bunga-tinggi-beli-sebelum-kenaikan-fed)  
  <sub>Pluang, 21 hours ago</sub>  
  The ProShares UltraShort 20+ Year Treasury ETF (TBT), designed to profit from rising interest rates by delivering twice the inverse daily return of...
- [More rate adjustments are likely needed to lower inflation, Fed Governor Barr says (TLT:NASDAQ)](https://seekingalpha.com/news/4646048-more-rate-adjustments-are-likely-needed-to-lower-inflation-fed-governor-barr-says)  
  <sub>Seeking Alpha, 56 minutes ago</sub>  
  Further rate adjustments will likely be needed to ensure that inflation declines to the Federal Reserve's 2% target in a timely fashion, Fed Governor...
- [After the Hike: Fixed Income ETF Money Trail](https://etfdb.com/fixed-income-content-hub/following-hike-fixed-income-etf-money-trail/)  
  <sub>ETF Database, 52 minutes ago</sub>  
  As the Fed lifted rates for the first time since 2023 and signaled a tighter trajectory ahead, the response across ETFs was swift.
- [Wedbush Goes Old School with Analog Economy ETF](https://www.thedailyupside.com/etf/thematics-sectors/wedbush-goes-old-school-with-analog-economy-etf/)  
  <sub>The Daily Upside, 11 hours ago</sub>  
  The fund will track an index focused on companies whose business models depend on human labor, physical assets and tangible output.
- [Why Has the U.S. Long Bond Futures Broken Out of the Multiyear Consolidation Range in 2026?](https://www.barchart.com/story/news/4740385/why-has-the-u-s-long-bond-futures-broken-out-of-the-multiyear-consolidation-range-in-2026)  
  <sub>Barchart.com, 20 hours ago</sub>  
  I concluded a July 21, 2026, Barchart article on the bond market and interest rates with the following thoughts: I do not see the bonds or TLT breaking...
- [Dow Drops To Record Worst Week In Six Months Amid Elevated Yields, Oil — NVDA, TSLA, SPCX, ONON In Focus](https://stocktwits.com/news-articles/markets/equity/dow-drops-to-record-worst-week-in-six-months-amid-elevated-yields-oil-nvda-tsla-spcx-onon-in-focus/cZtHOYsRBEK)  
  <sub>Stocktwits, 6 hours ago</sub>  
  The S&P 500 ended Friday 0.2% higher, while the Nasdaq 100 added 0.7% and the Dow Jones Industrial Average fell 0.2%. Treasury 10-year yields settled the...
- [Dow, S&P 500, Nasdaq Futures Climb Amid Iran Diplomacy Hopes, AI Rally: IONQ, VKTX, INFQ, BB Stocks In Focus](https://www.tradingview.com/news/stocktwits:6c76a162d094b:0-dow-s-p-500-nasdaq-futures-climb-amid-iran-diplomacy-hopes-ai-rally-ionq-vktx-infq-bb-stocks-in-focus/)  
  <sub>TradingView, 13 hours ago</sub>  
  U.S. stock futures edged higher in the overnight session late Tuesday after President Donald Trump confirmed that U.S. and Iranian officials met on the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 80.74 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 81.85 (-1.4%), 50d 82.49 (-2.1%), 200d 85.79 (-5.9%); 50d below 200d
Momentum: RSI(14) 40.3 | MACD -0.444 vs signal -0.445 (histogram 0.001)
Returns: 1d -1.3% | 5d +0.0% | 1m -1.6% | 3m -6.3%
52-week range: 80.71 - 92.06 (now 0.3% of the way up)
Volatility: ATR(14) 0.72 (0.9% of price) | annualised 20d 10.1%
Volume: 0.41x the 20-day average
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
Three-year record: +0.8% a year | beta to the market 2.39
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
Shares outstanding: 109.70M | fund size: 8.86B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Dollar Strength Grows: ETFs to Gain From Greenback Momentum](https://www.zacks.com/stock/news/2994565/dollar-strength-grows-etfs-to-gain-from-greenback-momentum)  
  <sub>Zacks Investment Research, 39 minutes ago</sub>  
  The dollar is gaining momentum as markets price in further Fed rate hikes. Here are some ETFs to consider for bullish greenback exposure.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 28.62 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 28.17 (+1.6%), 50d 28.21 (+1.5%), 200d 27.73 (+3.2%); 50d above 200d
Momentum: RSI(14) 71.1 | MACD 0.090 vs signal 0.028 (histogram 0.061)
Returns: 1d +0.5% | 5d +1.4% | 1m +2.6% | 3m +0.6%
52-week range: 26.47 - 28.62 (now 100.0% of the way up)
Volatility: ATR(14) 0.11 (0.4% of price) | annualised 20d 4.8%
Volume: 0.25x the 20-day average
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
Shares outstanding: 10.53M | fund size: 301.24M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Argentina (ARGT) · Sector or country — BULLISH, confidence 0.60

**Result:** REJECTED · no room under the gross exposure limit

**In the model's own words:**

> Analyst coverage of top holdings (51.1% weight) shows 100% buy rating and weighted price target +30.6% above current prices; Macro news: MSCI to replace S&P and redesign Merval index methodology, potentially boosting Argentine equity exposure; Fund fundamentals: P/E 15.48, three‑year annualized return +30.3% per year, indicating strong performance; Technical indicators: price below 20‑day SMA, RSI 40.1, low volume, suggesting slight downside pressure

**Main reasons it gave:**
- Analyst coverage of top holdings (51.1% weight) shows 100% buy rating and weighted price target +30.6% above current prices
- Macro news: MSCI to replace S&P and redesign Merval index methodology, potentially boosting Argentine equity exposure
- Fund fundamentals: P/E 15.48, three‑year annualized return +30.3% per year, indicating strong performance
- Technical indicators: price below 20‑day SMA, RSI 40.1, low volume, suggesting slight downside pressure

<details><summary><b>News</b> — score +0.30</summary>

- [Giro histórico en la Bolsa: MSCI reemplazará a S&P y calculará el índice Merval](https://www.google.com/goto?url=CAESrwEB6zswFXRErVjVPKOAVDkwwTZGRDlTY4dJ3whHcYReYKdg4xd666PwR4LMKKKIk4sokcapIu6lEvjNdYsb6chLIiLgcsK1Cp1qBuxJ_0mA06_DrZOTvFCQeKwluTxDAPBFIwwmbK8kQFGOx9sJB6kq_1Lcgf9UtReK8lQ649jSjYtUBT02PPopMGpaB_XQRffWzOkUkZcXz_gD6RhRgukNd2NkNPAB7MVN2zJuwpGZ)  
  <sub>Diario Mendoza, 14 hours ago</sub>  
  BYMA selló una alianza estratégica con el principal proveedor global de índices para rediseñar la metodología bursátil desde el 19 de octubre.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.30</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 92.00 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 94.87 (-3.0%), 50d 93.88 (-2.0%), 200d 92.72 (-0.8%); 50d above 200d
Momentum: RSI(14) 40.1 | MACD -0.251 vs signal 0.248 (histogram -0.499)
Returns: 1d -0.4% | 5d -2.6% | 1m -0.9% | 3m -0.6%
52-week range: 67.55 - 102.94 (now 69.1% of the way up)
Volatility: ATR(14) 1.81 (2.0% of price) | annualised 20d 16.0%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.48 | P/B 1.77 | P/S 1.36 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +30.3% a year | beta to the market 0.50
Cost and size: expense ratio 0.59% | net assets 815.33M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: MercadoLibre Inc 25.4%, YPF SA ADR 9.5%, Vista Energy SAB de CV ADR 6.2%, Grupo Financiero Galicia SA ADR 5.6%, Banco Macro SA ADR 4.3%
Sector mix: Consumer cyclical 30.4%, Energy 19.4%, Financial services 14.4%, Basic materials 12.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 51.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.54 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.6% above the current prices
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
Shares outstanding: 8.81M | fund size: 810.92M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — BULLISH, confidence 0.45

**Result:** REJECTED · no room under the gross exposure limit

**In the model's own words:**

> Analyst consensus: 100% buy on top holdings with +5.9% price target; Technical trend: price above 20‑day, 50‑day and 200‑day SMAs, up 23.5% YTD; Sector news: Frontier AI slowdown shifting focus to software platforms; Macro: stable yields, low VIX, no surprise data

**Main reasons it gave:**
- Analyst consensus: 100% buy on top holdings with +5.9% price target
- Technical trend: price above 20‑day, 50‑day, 200‑day SMAs, up 23.5% YTD
- Sector news: Frontier AI slowdown shifting focus to software platforms
- Macro: stable yields, low VIX, no surprise data

<details><summary><b>News</b> — score +0.45</summary>

- [iShares Expanded Tech-Software Sector ETF (IGV) Stock Price | Live Quotes & Charts | BATS](https://www.timothysykes.com/quote/IGV/)  
  <sub>www.timothysykes.com, 18 hours ago</sub>  
  Get latest iShares Expanded Tech-Software Sector ETF (IGV) stock price, news, and charts. Access real-time quotes and historical data with interactive...
- [Semiconductor ETFs Hit Historic AUM: SMH at $70B, SOXX at $46B](https://www.kucoin.com/news/flash/semiconductor-etfs-hit-historic-aum-smh-at-70b-soxx-at-46b)  
  <sub>KuCoin, 21 hours ago</sub>  
  Semiconductor ETFs are registering historic capital inflows — and the data is not subtle.The VanEck Semiconductor ETF ($SMH) has seen assets under...
- [Frontier AI Slowdown: Stocks and ETFs to Watch](https://www.tradingview.com/news/zacks:bc7e4472b094b:0-frontier-ai-slowdown-stocks-and-etfs-to-watch/)  
  <sub>TradingView, 2 hours ago</sub>  
  The recent debate over slowing frontier AI development could shift investor attention from capital-intensive chipmakers toward software platforms,...
- [What's Going On With Oracle Stock Wednesday?](https://www.benzinga.com/markets/large-cap/26/09/61942244/whats-going-on-with-oracle-stock-wednesday-4)  
  <sub>Benzinga, 3 hours ago</sub>  
  Oracle (ORCL) edges lower in premarket trading amid tech sector weakness. Get the latest price targets, stock technicals, and analysis.
- [Adobe Is Down 32% This Year: Is ADBE Stock Dead Money or Due for a Bounce?](https://247wallst.com/investing/2026/09/22/adobe-is-down-32-this-year-is-adbe-stock-dead-money-or-due-for-a-bounce/)  
  <sub>24/7 Wall St., 20 hours ago</sub>  
  Adobe has fallen harder than its software peers while the broader market climbed, and the selling has not slowed even after quarterly results landed.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.45</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.45</summary>

```text
Last close 107.84 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 105.23 (+2.5%), 50d 100.60 (+7.2%), 200d 93.69 (+15.1%); 50d above 200d
Momentum: RSI(14) 58.7 | MACD 1.341 vs signal 1.343 (histogram -0.002)
Returns: 1d +0.7% | 5d +2.2% | 1m +4.3% | 3m +23.5%
52-week range: 74.67 - 117.79 (now 76.9% of the way up)
Volatility: ATR(14) 2.69 (2.5% of price) | annualised 20d 42.5%
Volume: 0.30x the 20-day average
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
Three-year record: +16.4% a year | beta to the market 1.21
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 43.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +5.9% above the current prices
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 12.50M | fund size: 1.35B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, modest technical uptrend with low volume, analyst view bullish but limited to 37.6% of fund, no flow data.

**Main reasons it gave:**
- Technicals: price above 20d, 50d, 200d SMAs (+0.9% to +2.7%) with low volume
- Analyst consensus: 100% buy rating, price target +16.6% (covers 37.6% of fund weight)
- Macro: no policy or rate surprise; yields stable, VIX low
- Fund flows: direction unknown, share count change n/a (no flow data)

<details><summary><b>News</b> — score +0.00</summary>

- [Animoca legt Fusionsdeal mit Currenc wegen kurz- und mittelfristiger Differenzen auf Eis](https://www.cryptopolitan.com/de/animoca-shelves-currenc-merger-deal/)  
  <sub>Cryptopolitan, 24 hours ago</sub>  
  Animoca Brands und Currenc Group haben die Gespräche über die geplante umgekehrte Fusion einvernehmlich ausgesetzt.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 125.33 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 124.17 (+0.9%), 50d 122.26 (+2.5%), 200d 122.06 (+2.7%); 50d above 200d
Momentum: RSI(14) 54.0 | MACD 0.783 vs signal 0.628 (histogram 0.155)
Returns: 1d -1.8% | 5d +2.2% | 1m +2.1% | 3m +4.9%
52-week range: 94.16 - 137.69 (now 71.6% of the way up)
Volatility: ATR(14) 1.85 (1.5% of price) | annualised 20d 21.3%
Volume: 0.52x the 20-day average
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
Three-year record: +35.0% a year | beta to the market 1.07
Cost and size: expense ratio 0.59% | net assets 897.28M
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.25 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.6% above the current prices
Holdings read: TEVA, LUMI.TA, POLI.TA, TSEM.TA, ESLT.TA
Recent rating changes among them:
  - TEVA: 2026-09-23 Oppenheimer: init, ? -> Outperform
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
Shares outstanding: 2.55M | fund size: 319.59M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral

**Main reasons it gave:**
- Analyst view: 90% buy rating and 1.7% price target upside
- Fund fundamentals: strong 3‑year record (+44% annual) and moderate valuation (P/E 13.5) with 3.3% yield
- No macro surprise: yields up modestly, dollar up, VIX low, no policy shock
- Technicals: price near 52‑week high but RSI neutral, MACD histogram negative, low volume – no decisive breakout
- No positioning data: fund flows unknown, no insider flow signal

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 44.67 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 44.70 (-0.1%), 50d 43.54 (+2.6%), 200d 39.12 (+14.2%); 50d above 200d
Momentum: RSI(14) 51.8 | MACD 0.384 vs signal 0.487 (histogram -0.102)
Returns: 1d -2.2% | 5d -0.4% | 1m +0.6% | 3m +15.3%
52-week range: 31.57 - 45.76 (now 92.3% of the way up)
Volatility: ATR(14) 0.71 (1.6% of price) | annualised 20d 21.7%
Volume: 0.57x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.37</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.37</summary>

```text
Rolled up from the 5 largest holdings, 47.4% of the fund by weight
Ratings by weight: buy 90.3% | hold 9.7% | sell 0.0% (mean 2.26 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -1.7% above the current prices
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
Shares outstanding: 19.09M | fund size: 852.55M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise, no decisive technical break, mixed analyst view, moderate fundamentals, and unreliable direct buy recommendation in news.

**Main reasons it gave:**
- Analyst view: 59.6% hold, 40.4% sell, mean rating 3.48 (slightly bearish)
- Technical indicators: price below 20‑day, 50‑day, 200‑day SMAs; RSI 38.9; MACD below signal; low volume
- Macro: US dollar up, yields rising, VIX low; no major data surprise
- News: Seeking Alpha article's direct buy recommendation ignored as unreliable; Australian manufacturing contraction reported
- Fundamentals: moderate valuation (P/E 21), strong 3‑year performance (+14.7% per year), dividend yield 2.8%

<details><summary><b>News</b> — score +0.00</summary>

- [The Case For Australia And The EWA ETF (NYSEARCA:EWA)](https://seekingalpha.com/article/4948732-the-case-for-australia-and-the-ewa-etf)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Buy iShares MSCI Australia ETF (EWA): commodity-driven upside >20% to new highs above $34.83, ~3% yield, BHP-heavy exposure—read more macroanalysis here.
- [Australia Flash PMI: Manufacturing contracts for first time since March, services growth softens](https://seekingalpha.com/news/4645806-australia-flash-pmi-manufacturing-contracts-for-first-time-since-march-services-growth-softens)  
  <sub>Seeking Alpha, 11 hours ago</sub>  
  Australia's manufacturing sector contracted in September 2026 for the first time in six months, led by a sharp drop in factory output and weakening order...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 28.48 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 29.54 (-3.6%), 50d 29.48 (-3.4%), 200d 28.56 (-0.3%); 50d above 200d
Momentum: RSI(14) 38.9 | MACD -0.260 vs signal -0.126 (histogram -0.133)
Returns: 1d -1.9% | 5d -1.4% | 1m -5.5% | 3m +1.6%
52-week range: 24.95 - 30.43 (now 64.3% of the way up)
Volatility: ATR(14) 0.40 (1.4% of price) | annualised 20d 18.4%
Volume: 0.43x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 21.06 | P/B 2.81 | P/S 3.39 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +14.7% a year | beta to the market 0.96
Cost and size: expense ratio 0.50% | net assets 1.33B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: BHP Group Ltd 16.3%, Commonwealth Bank of Australia 13.0%, National Australia Bank Ltd 5.9%, Westpac Banking Corp 5.7%, ANZ Group Holdings Ltd 5.5%
Sector mix: Financial services 41.1%, Basic materials 26.7%, Consumer cyclical 6.5%, Healthcare 5.2%
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

<details><summary><b>What analysts and big funds say</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.40</summary>

```text
Rolled up from the 5 largest holdings, 46.4% of the fund by weight
Ratings by weight: buy 0.0% | hold 59.6% | sell 40.4% (mean 3.48 on a 1=strong buy to 5=strong sell scale)
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 46.17M | fund size: 1.31B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals lack a decisive breakout, and fund fundamentals are moderate despite a strong 3‑year record. Analyst view is modestly bullish but covers only ~28% of the fund, and flow data is unavailable.

**Main reasons it gave:**
- Analyst coverage of 28.3% of fund shows 74.3% buy rating and +6.4% price target (bullish but limited scope)
- Technical indicators: price below 20‑day and 50‑day SMA, RSI 42.5, MACD negative – no decisive breakout
- Macro backdrop: modest yield rises, low VIX, no policy or data surprise – neutral environment
- Canada's business tax cut to 6.4% and $1T mining capex push could boost basic materials exposure (16% of fund)
- Fund fundamentals: moderate valuation (P/E 19.5) and strong 3‑yr record (+23.4%/yr) but heavy financial sector weight (39%)

<details><summary><b>News</b> — score +0.00</summary>

- [Kevin O'Leary Explains Why His Big AI Bet is Uranium, Not Big Tech: 'The Trade is Now the Energy Trade'](https://www.benzinga.com/markets/market-summary/26/09/61941964/kevin-oleary-explains-why-his-big-ai-bet-is-uranium-not-big-tech-the-trade-is-now-the-energy-trade)  
  <sub>Benzinga, 4 hours ago</sub>  
  Kevin O'Leary explains why his big AI bet is uranium, not big tech. Discover his 'energy trade' strategy and the ETFs to track his picks.
- [Canada Just Triggered a Mining Capex Rush: 2 Stocks Analysts Love Right Now](https://www.benzinga.com/markets/commodities/26/09/61943063/canada-just-triggered-a-mining-capex-rush-2-stocks-analysts-love-right-now)  
  <sub>Benzinga, 3 hours ago</sub>  
  Canada slashes business tax rates to 6.4%, launching a $1T investment push that boosts mining project economics and drives new M&A.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 60.03 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 61.09 (-1.7%), 50d 60.70 (-1.1%), 200d 57.50 (+4.4%); 50d above 200d
Momentum: RSI(14) 42.5 | MACD -0.243 vs signal -0.068 (histogram -0.175)
Returns: 1d -0.7% | 5d -0.4% | 1m -3.7% | 3m +4.1%
52-week range: 49.72 - 62.64 (now 79.8% of the way up)
Volatility: ATR(14) 0.66 (1.1% of price) | annualised 20d 13.6%
Volume: 0.31x the 20-day average
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
Three-year record: +23.4% a year | beta to the market 0.79
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 113.71M | fund size: 6.83B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, technicals are mixed and not decisive, analyst coverage is bullish but limited to a small portion of the fund, and fund flow direction is unknown.

**Main reasons it gave:**
- US macro data (inflation 3.4%, unemployment 4.1%, jobless claims 196k) in line with expectations
- Price below 20‑day SMA (51.42 vs 52.46) and 50‑day SMA (51.42 vs 52.15), negative MACD (-0.345 vs -0.182), low volume (0.27× 20‑day avg)
- Analyst coverage of top holdings (29.5% of fund) shows 82.1% buy rating and weighted price target +10.8% above current prices
- Fund flows direction unknown (share count change n/a), no clear positioning signal

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 51.42 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 52.46 (-2.0%), 50d 52.15 (-1.4%), 200d 51.31 (+0.2%); 50d above 200d
Momentum: RSI(14) 43.6 | MACD -0.345 vs signal -0.182 (histogram -0.163)
Returns: 1d -0.7% | 5d +0.3% | 1m -4.1% | 3m +5.4%
52-week range: 45.38 - 54.72 (now 64.7% of the way up)
Volatility: ATR(14) 0.67 (1.3% of price) | annualised 20d 15.7%
Volume: 0.27x the 20-day average
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
Three-year record: +20.7% a year | beta to the market 1.19
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
Weighted price target: +10.8% above the current prices
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
Shares outstanding: 14.83M | fund size: 762.31M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; positive German business activity surprise is offset by weak technicals and no major macro catalyst.

**Main reasons it gave:**
- German Composite Output Index rose to 53.8, beating expectations of 51.8
- EWG price below 20‑day and 50‑day SMAs, RSI 37.6, MACD negative
- Analyst coverage: 78% buy, weighted price target +17.3% above current price
- US yields up modestly, VIX low, no major policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Germany's business activity accelerates in September as services return to growth (EWG:NYSEARCA)](https://seekingalpha.com/news/4645822-germany-business-activity-accelerates-in-september-as-services-return-to-growth)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  Germany's flash Composite Output Index rises to 53.8 in September from 51.8, marking an 11-month high, and beating market expectations of 51.8.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 42.04 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 43.31 (-2.9%), 50d 43.00 (-2.2%), 200d 42.38 (-0.8%); 50d above 200d
Momentum: RSI(14) 37.6 | MACD -0.314 vs signal -0.142 (histogram -0.172)
Returns: 1d -1.3% | 5d -1.2% | 1m -4.9% | 3m +2.6%
52-week range: 38.08 - 44.59 (now 60.8% of the way up)
Volatility: ATR(14) 0.47 (1.1% of price) | annualised 20d 13.2%
Volume: 0.39x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.78</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.78</summary>

```text
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.85 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.3% above the current prices
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
Shares outstanding: 79.50M | fund size: 3.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, weak technicals, bullish analyst coverage but no flow signal.

**Main reasons it gave:**
- US Treasury yields rose modestly across the curve (+0.06‑0.11) with no surprise
- Technical indicators show price below 20‑day and 50‑day SMAs, RSI 41.1, MACD negative, and low volume
- Analyst coverage is 100% buy with a weighted price target +11% above current price
- Fundamentals show moderate valuation (P/E 15.25) and a 3% yield, with strong three‑year performance
- Fund flows direction unknown and share count unchanged, providing no flow signal

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 60.19 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 61.48 (-2.1%), 50d 61.73 (-2.5%), 200d 57.77 (+4.2%); 50d above 200d
Momentum: RSI(14) 41.1 | MACD -0.404 vs signal -0.267 (histogram -0.138)
Returns: 1d -1.7% | 5d -0.9% | 1m -4.3% | 3m +1.3%
52-week range: 50.31 - 63.35 (now 75.8% of the way up)
Volatility: ATR(14) 0.76 (1.3% of price) | annualised 20d 17.3%
Volume: 0.16x the 20-day average
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
Three-year record: +29.5% a year | beta to the market 0.88
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 50.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.02 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.0% above the current prices
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
Shares outstanding: 18.83M | fund size: 1.13B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst view is thin, positioning modestly long, fundamentals solid but macro unchanged and technicals indecisive.

**Main reasons it gave:**
- Analyst view: 100% buy on 17% of fund, price target +19.7% (thin coverage)
- Positioning: net long 4.3% of open interest, weekly increase +1.5%
- Fund basics: P/E 19.1, 3-year return +20% per year, yield 3.7%
- Macro: dollar index up 1.34% on week, no major policy or data surprise, VIX 14.5 (low volatility)
- Technicals: price above 20‑day SMA (+0.6%), RSI 54, MACD below signal, volume 0.30× 20‑day avg

<details><summary><b>News</b> — score +0.00</summary>

- [Asian stocks trade mixed following Wall St, caution over US-China summ](https://seekingalpha.com/news/4645805-asian-stocks-trade-mixed-following-wall-street-chinese-equities-edge-lower-ahead-of-summit)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  Asian stock markets traded mixed on Wednesday, reflecting a cautious overnight session on Wall Street as investors turned their attention to macroeconomic...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 97.47 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 96.90 (+0.6%), 50d 95.12 (+2.5%), 200d 89.85 (+8.5%); 50d above 200d
Momentum: RSI(14) 54.2 | MACD 0.635 vs signal 0.691 (histogram -0.056)
Returns: 1d -0.5% | 5d +0.6% | 1m +2.4% | 3m +5.1%
52-week range: 78.36 - 98.56 (now 94.6% of the way up)
Volatility: ATR(14) 1.32 (1.4% of price) | annualised 20d 14.7%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Japan Stock
What it holds: P/E 19.11 | P/B 2.01 | P/S 1.68 | 3y earnings growth n/a
Yield: 3.7%
Three-year record: +20.2% a year | beta to the market 0.86
Cost and size: expense ratio 0.49% | net assets 22.69B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Mitsubishi UFJ Financial Group Inc 4.6%, Toyota Motor Corp 3.5%, Sumitomo Mitsui Financial Group Inc 3.0%, Tokyo Electron Ltd 3.0%, Advantest Corp 2.9%
Sector mix: Industrials 22.9%, Technology 21.5%, Financial services 19.1%, Consumer cyclical 11.6%
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.7% above the current prices
Holdings read: 8306.T, 7203.T, 8316.T, 8035.T, 6857.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 4.3% of open interest (22,625 contracts)
Change on the week: +1.5% of open interest
Crowding: 38% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 234.29M | fund size: 22.84B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- Analyst coverage: 74.5% buy rating and +10% price target for top holdings
- Technical indicators: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 39.7; MACD below signal; low volume
- Macro environment: no policy surprise; inflation 3.4% below Fed target; yields up slightly; VIX low
- Fundamentals: solid 3‑year record (+12.9% per year), defensive sector mix (37.5% healthcare), moderate valuation (P/E 24.65)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 60.60 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 61.81 (-2.0%), 50d 62.72 (-3.4%), 200d 61.55 (-1.5%); 50d above 200d
Momentum: RSI(14) 39.7 | MACD -0.815 vs signal -0.714 (histogram -0.102)
Returns: 1d -0.3% | 5d +0.6% | 1m -5.8% | 3m -1.4%
52-week range: 53.86 - 65.08 (now 60.1% of the way up)
Volatility: ATR(14) 0.68 (1.1% of price) | annualised 20d 13.5%
Volume: 0.39x the 20-day average
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
Three-year record: +12.9% a year | beta to the market 0.91
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 48.5% of the fund by weight
Ratings by weight: buy 74.5% | hold 25.5% | sell 0.0% (mean 2.40 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.0% above the current prices
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
Shares outstanding: 28.62M | fund size: 1.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no macro surprise or decisive technical break; analyst view is strongly bullish but not enough to outweigh mixed technicals and neutral macro backdrop.

**Main reasons it gave:**
- Analyst view: 100% buy rating on 44.1% of fund, price target +30.6% above current price
- Technical: price below 20‑day SMA, RSI 47.4, MACD negative, volume 0.17× 20‑day average
- Macro: US Treasury yields up modestly, VIX down 2.7% week, no data surprise
- Fund fundamentals: P/E 18.97, dividend yield 4.1%, 3‑year return +24.5% per year

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 67.55 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 67.91 (-0.5%), 50d 68.17 (-0.9%), 200d 63.96 (+5.6%); 50d above 200d
Momentum: RSI(14) 47.4 | MACD -0.427 vs signal -0.367 (histogram -0.060)
Returns: 1d -0.4% | 5d +1.9% | 1m -2.7% | 3m -0.5%
52-week range: 55.33 - 71.61 (now 75.1% of the way up)
Volatility: ATR(14) 0.89 (1.3% of price) | annualised 20d 14.4%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.60</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.97 | P/B 2.54 | P/S 1.84 | 3y earnings growth n/a
Yield: 4.1%
Three-year record: +24.5% a year | beta to the market 1.14
Cost and size: expense ratio 0.50% | net assets 626.66M
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ASML Holding NV 21.8%, ING Groep NV 9.0%, Prosus NV Ordinary Shares - Class N 5.1%, Nebius Group NV Shs Class-A- 4.3%, ASM International NV 4.0%
Sector mix: Technology 31.5%, Financial services 21.4%, Industrials 10.8%, Consumer defensive 10.7%
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
Rolled up from the 5 largest holdings, 44.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.6% above the current prices
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
Shares outstanding: 5.55M | fund size: 374.90M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; modest bullish analyst and fundamental signals are offset by lack of decisive technical break and stable macro backdrop.

**Main reasons it gave:**
- Analyst view: 52% buy, 48% hold, weighted price target +2.1% (modest bullish)
- Fundamentals: strong 3‑year record (+34.3% per year) and moderate valuation (P/E 16.28)
- Technicals: price below 20‑day and 50‑day SMA, RSI 43.7, MACD negative, low volume (no decisive break)
- Macro: upward‑sloping yield curve, modest rate‑hike expectations, low VIX (no surprise)
- Sector mix: 45% financials may benefit from rising rates, offsetting utilities exposure

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 60.72 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 61.83 (-1.8%), 50d 61.48 (-1.2%), 200d 57.31 (+5.9%); 50d above 200d
Momentum: RSI(14) 43.7 | MACD -0.225 vs signal -0.051 (histogram -0.175)
Returns: 1d -1.1% | 5d -0.6% | 1m -3.5% | 3m +2.9%
52-week range: 48.25 - 63.23 (now 83.2% of the way up)
Volatility: ATR(14) 0.79 (1.3% of price) | annualised 20d 15.5%
Volume: 0.32x the 20-day average
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
Three-year record: +34.3% a year | beta to the market 0.87
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 54.5% of the fund by weight
Ratings by weight: buy 52.0% | hold 48.0% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +2.1% above the current prices
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
Shares outstanding: 37.35M | fund size: 2.27B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no macro surprise, technicals are mixed without a decisive break, and analyst coverage, while positive, only spans a modest portion of the fund.

**Main reasons it gave:**
- No news or macro surprise this week
- Technicals show price below 20‑day and 50‑day SMAs but above 200‑day SMA, no decisive break
- Analyst coverage positive (+11.5% price target) but only covers 36% of fund
- Fund basics show moderate valuation (P/E 17.1) and strong 3‑year performance (+18.7%/yr) but not enough to shift overall view

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 47.37 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 48.13 (-1.6%), 50d 47.98 (-1.3%), 200d 46.53 (+1.8%); 50d above 200d
Momentum: RSI(14) 42.3 | MACD -0.181 vs signal -0.070 (histogram -0.111)
Returns: 1d -0.7% | 5d -0.9% | 1m -3.2% | 3m +3.9%
52-week range: 41.04 - 49.39 (now 75.7% of the way up)
Volatility: ATR(14) 0.47 (1.0% of price) | annualised 20d 11.4%
Volume: 0.34x the 20-day average
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
Three-year record: +18.7% a year | beta to the market 0.68
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 36.0% of the fund by weight
Ratings by weight: buy 57.5% | hold 42.5% | sell 0.0% (mean 1.82 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.5% above the current prices
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
Shares outstanding: 79.92M | fund size: 3.79B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: macro data stable, technicals show slight weakness but no decisive break, analyst view bullish but limited to <50% of holdings, and fund flow data unavailable.

**Main reasons it gave:**
- Macro data stable: yields modestly up, inflation and unemployment in line with expectations
- Technical indicators show price below 20‑, 50‑ and 200‑day SMAs and negative MACD, indicating slight weakness but no decisive break
- Analyst coverage of 47.6% of the fund is 100% buy with a +16.1% price target, bullish but limited to less than half the holdings
- Fund flow data unavailable, providing no directional signal

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 73.55 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 75.58 (-2.7%), 50d 75.85 (-3.0%), 200d 75.69 (-2.8%); 50d above 200d
Momentum: RSI(14) 39.6 | MACD -0.731 vs signal -0.451 (histogram -0.280)
Returns: 1d -0.2% | 5d -0.6% | 1m -4.9% | 3m -1.6%
52-week range: 64.39 - 81.23 (now 54.4% of the way up)
Volatility: ATR(14) 1.23 (1.7% of price) | annualised 20d 15.0%
Volume: 0.45x the 20-day average
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
Three-year record: +11.0% a year | beta to the market 1.05
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 47.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.92 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.1% above the current prices
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

### South Korea (EWY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals not decisive, fundamentals modestly positive but tempered by high beta and low yield; single‑stock news ignored.

**Main reasons it gave:**
- US Treasury yields up modestly (+0.06% on 10‑year) and curve remains upward sloping
- VIX at 14.49, down 2.7% on the week, indicating calm market conditions
- Technicals: price above 20‑day, 50‑day, 200‑day SMAs with RSI 55.3 and MACD positive, but volume only 0.47× 20‑day average
- Fund basics: low P/E 10.41, strong 3‑year record (+49.8% annual) but high beta 2.5 and low yield 1.1%
- News: no macro surprise; single‑stock SK Hynix drop ignored for fund view

<details><summary><b>News</b> — score +0.00</summary>

- [Middle East strike sinks US stocks as markets eye US-China summit - CHOSUNBIZ](https://biz.chosun.com/en/en-international/2026/09/23/C54WQYE7J5B7PK5WUJOMMOQMVU/)  
  <sub>Chosunbiz, 1 hour ago</sub>  
  As geopolitical tensions in the Middle East flared again, the three major U.S. stock indexes in New York opened lower on the 23rd.
- [What Is KORU? The 3x Korea ETF That Delivered 1.55x](https://www.google.com/goto?url=CAESbgHrOzAVbOA2putomKijWOhbPrlADjQ-oxMU_EwoRlCfCKtnvIqn6s8QQH4R_wqcwoiXCLKUeUpcp9f0dvdXp4NgoYxTr2gKlka_f0SQfW6wIIKi-gNLvESa597OSxAGiy6nvfjqAJObUeFkOEPc)  
  <sub>Phemex, 9 hours ago</sub>  
  Discover how KORU, the 3x Korea ETF, achieved only 1.55x index returns over 67 sessions, and learn the risks of leveraged ETF decay. Explore more now.
- [CPU Demand Raises the Odds of DRAM Staying Tight Through 2031](https://www.google.com/goto?url=CAESpgEB6zswFZDFRRE4m4yDJq-iNfjC-PaopxkeL6b0bnrZwaxzVRB55NVwV9R3O0KXUKHbhm-tdwPVwOLPA60lR-uLyrjDt9EflyXHLPlOUhW9hKJmi7oPyF7vYHUH776I41BNJTwhr0P_UHEwhieMUx_n3pu34fMTuxsPGfT7hlnL8OxuaPJARLGPCSQeThC8k6d5xy3KREM_W6KDNxYAC296ItiX1_RX)  
  <sub>Moomoo, 9 hours ago</sub>  
  Memory stocks rallied again on Tuesday. The more important update is that stronger server CPU demand is adding another source of DRAM pressure, making...
- [Asian stocks trade mixed following Wall St, caution over US-China summ](https://seekingalpha.com/news/4645805-asian-stocks-trade-mixed-following-wall-street-chinese-equities-edge-lower-ahead-of-summit)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  Asian stock markets traded mixed on Wednesday, reflecting a cautious overnight session on Wall Street as investors turned their attention to macroeconomic...
- [SK Hynix stock falls 8% on AI development slowdown fears](https://scanx.trade/stock-market-news/equity-markets/sk-hynix-stock-falls-3-5-profit-taking-macro-pressures/50587236)  
  <sub>scanx.trade, 18 hours ago</sub>  
  SK Hynix shares fell 7.53% to $175.76 in premarket trading on Monday. Nasdaq futures dropped 1.59% amid concerns over slowed frontier AI development.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 186.71 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 182.33 (+2.4%), 50d 173.89 (+7.4%), 200d 152.55 (+22.4%); 50d above 200d
Momentum: RSI(14) 55.3 | MACD 2.245 vs signal 2.170 (histogram 0.075)
Returns: 1d -1.3% | 5d +5.8% | 1m +4.7% | 3m -2.9%
52-week range: 78.87 - 219.20 (now 76.8% of the way up)
Volatility: ATR(14) 6.55 (3.5% of price) | annualised 20d 45.6%
Volume: 0.47x the 20-day average
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
Three-year record: +49.8% a year | beta to the market 2.50
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
Shares outstanding: 152.34M | fund size: 28.44B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals bearish but not decisive, analyst view bullish but limited coverage, fund flows unknown.

**Main reasons it gave:**
- US Treasury yields rose modestly (10y +0.06% week) and VIX fell to 14.49, no macro surprise
- Technical indicators show price below 20‑day, 50‑day and 200‑day SMAs, RSI 39.5, but no decisive break on volume
- Analyst coverage of top holdings (45.6% weight) is 100% buy with +26.3% price target, indicating bullish view but limited scope
- Fund flows direction unknown, share count unchanged, providing no clear insider signal

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 66.46 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 69.95 (-5.0%), 50d 67.37 (-1.4%), 200d 69.26 (-4.0%); 50d below 200d
Momentum: RSI(14) 39.5 | MACD -0.163 vs signal 0.408 (histogram -0.571)
Returns: 1d -2.6% | 5d -3.6% | 1m -8.3% | 3m +4.0%
52-week range: 60.43 - 81.60 (now 28.5% of the way up)
Volatility: ATR(14) 1.32 (2.0% of price) | annualised 20d 22.7%
Volume: 0.37x the 20-day average
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
Three-year record: +28.2% a year | beta to the market 1.02
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.82 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.3% above the current prices
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
Shares outstanding: 7.90M | fund size: 525.03M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – analyst coverage is bullish but technicals are mixed and there is no macro surprise; fund flow data is unavailable.

**Main reasons it gave:**
- Analyst ratings: 100% buy, price target +11.5% above current price
- Technicals: price below 20‑day SMA, MACD below signal, RSI 48.9 (neutral)
- Macro: Treasury yields rose modestly, no policy surprise; dollar index up
- Fund flows: direction unknown, share count unchanged

<details><summary><b>News</b> — score +0.00</summary>

- [AAAU vs. GDX: Is It Better to Hold Physical Gold or Invest in Gold Miners?](https://finance.yahoo.com/markets/commodities/articles/aaau-vs-gdx-better-hold-110201144.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  The Goldman Sachs Physical Gold ETF (NYSEMKT:AAAU) offers low-cost exposure to physical bullion, whereas the VanEck Gold Miners ETF (NYSEMKT:GDX) invests in...
- [Canada Just Triggered a Mining Capex Rush: 2 Stocks Analysts Love Right Now](https://www.benzinga.com/markets/commodities/26/09/61943063/canada-just-triggered-a-mining-capex-rush-2-stocks-analysts-love-right-now)  
  <sub>Benzinga, 3 hours ago</sub>  
  Canada slashes business tax rates to 6.4%, launching a $1T investment push that boosts mining project economics and drives new M&A.
- [YieldMax® ETFs Announces Weekly Distributions for Group 2 ETFs](https://www.globenewswire.com/news-release/2026/09/23/3367313/0/en/yieldmax-etfs-announces-weekly-distributions-for-group-2-etfs.html)  
  <sub>GlobeNewswire, 4 hours ago</sub>  
  CHICAGO and MILWAUKEE and NEW YORK, Sept. 23, 2026 (GLOBE NEWSWIRE) -- YieldMax® ETFs today announced distributions for the YieldMax® Group 2 weekly pay...
- [VanEck Gold Miners Equity ETF (GDX) Stock Price | Quotes & News](https://www.moomoo.com/stock/GDX-US?chain_id=Name1K9-3FXPhg.1lb5d0g&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A107%2C%22f%22%3A%22www.moomoo.com%2Fetfs%2FGDXJ-US%22%7D)  
  <sub>Moomoo, 22 hours ago</sub>  
  Track the latest VanEck Gold Miners Equity ETF (GDX) price, quotes, financial information, news, and analyst ratings on moomoo App for your ETF trading and...
- [Gold ends little changed; silver's direction torn between rate-hike risks, industrial demand](https://seekingalpha.com/news/4645779-gold-ends-little-changed-silvers-direction-torn-between-rate-hike-risks-industrial-demand)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Gold futures fell slightly while silver edged higher, as the precious metals remained within "a solid support range" with the US dollar firming and oil...
- [Nasdaq 100 Flirts with Records, Oil Sinks for Fifth Day: Stock Market Today](https://www.tradingview.com/news/benzinga:de108ba70094b:0-nasdaq-100-flirts-with-records-oil-sinks-for-fifth-day-stock-market-today/)  
  <sub>TradingView, 21 hours ago</sub>  
  The Nasdaq 100 carved out a fresh intraday record by midday Tuesday as the artificial intelligence trade powered ahead.Speaking at the United Nations...
- [Gold Miners: Most Of The Discount Is Still In The Price, Here’s Why. - TalkMarkets](https://t.co/c9IjEFWuvc)  
  <sub>Howl.link, 15 hours ago</sub>  
  Source: DepositPhotos. Gold miners just did something they almost never do… They beat gold. The ratio of the big gold miner fund (GDX) to the gold price...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 94.01 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 97.74 (-3.8%), 50d 88.77 (+5.9%), 200d 90.80 (+3.5%); 50d below 200d
Momentum: RSI(14) 48.9 | MACD 0.851 vs signal 1.943 (histogram -1.092)
Returns: 1d -0.4% | 5d -0.1% | 1m -8.6% | 3m +21.1%
52-week range: 68.28 - 115.84 (now 54.1% of the way up)
Volatility: ATR(14) 3.27 (3.5% of price) | annualised 20d 38.4%
Volume: 0.49x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Equity Precious Metals
What it holds: P/E 12.84 | P/B 2.68 | P/S 4.10 | 3y earnings growth n/a
Yield: 0.6%
Three-year record: +50.1% a year | beta to the market 0.83
Cost and size: expense ratio 0.51% | net assets 30.54B
What it is made of: Stocks 100.0%
Largest holdings: Newmont Corp 10.7%, Agnico Eagle Mines Ltd 10.7%, Barrick Mining Corp 7.4%, Wheaton Precious Metals Corp 5.8%, Anglogold Ashanti PLC 5.3%
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
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.5% above the current prices
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
Shares outstanding: 319.25M | fund size: 30.01B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst consensus, bearish technicals, high valuation, and recent defense‑sector sell‑off; no macro surprise.

**Main reasons it gave:**
- Analyst consensus: 100% buy rating, weighted price target +24.4% above current price
- Technical indicators: price below 20‑day SMA (222.64), 50‑day SMA (234.45), 200‑day SMA (230.29); RSI 31.8; MACD negative; volume 0.32× 20‑day average
- Fund fundamentals: high valuation (P/E 34.66, P/B 6.62, P/S 3.21) and low yield (0.5%)
- Sector news: defense stocks fell (Lockheed Martin, RTX, Boeing) impacting the fund's largest holdings

<details><summary><b>News</b> — score +0.00</summary>

- [Should You Invest in the iShares U.S. Transportation ETF (IYT)?](https://finance.yahoo.com/markets/stocks/articles/invest-ishares-u-transportation-etf-102003782.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Looking for broad exposure to the Industrials - Transportation/Shipping segment of the equity market? You should consider the iShares U.S. Transportation...
- [Defense Stocks Fall While Oil Slides on Hormuz Reopening Report: Lockheed Martin and RTX Drop 3%, Boeing Dips](https://247wallst.com/investing/2026/09/22/defense-stocks-fall-while-oil-slides-on-hormuz-reopening-report-lockheed-martin-and-rtx-drop-3-boeing-dips/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  A Reuters report on Iran's Hormuz offer sent defense primes tumbling Tuesday morning, but the selloff in Lockheed Martin and RTX started long before today's...
- [iShares U.S. Medical Devices ETF (IHI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/IHI/)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>  
  Find the latest iShares U.S. Medical Devices ETF (IHI) stock quote, history, news and other vital information to help you with your stock trading and...
- [Defense stocks fall as Trump raises prospect of Iran peace deal at UN (PPA:NYSEARCA)](https://seekingalpha.com/news/4645573-defense-stocks-fall-as-trump-raises-prospect-of-iran-peace-deal-at-un)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Defense stocks slide as Trump hints at Iran and Ukraine peace talks but warns of escalation. See market moves and what replenishing U.S. weapons means.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 216.06 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 222.64 (-3.0%), 50d 234.45 (-7.8%), 200d 230.29 (-6.2%); 50d above 200d
Momentum: RSI(14) 31.8 | MACD -6.449 vs signal -6.254 (histogram -0.195)
Returns: 1d -0.0% | 5d +1.0% | 1m -9.0% | 3m -8.4%
52-week range: 198.23 - 253.22 (now 32.4% of the way up)
Volatility: ATR(14) 3.91 (1.8% of price) | annualised 20d 14.5%
Volume: 0.32x the 20-day average
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
Weighted price target: +24.4% above the current prices
Holdings read: GE, RTX, BA, GD, LMT
Recent rating changes among them:
  - GE: 2026-07-23 Bernstein: main, Outperform -> Outperform
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 63.73M | fund size: 13.77B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, technicals not decisive, analyst view bullish but limited, fundamentals moderate.

**Main reasons it gave:**
- Yield curve remains upward sloping (+1.03) with modest yield rises – no macro surprise
- Price below 20d/50d/200d SMAs, RSI 31.9, MACD negative – bearish technicals but no decisive volume break
- Analyst consensus 90.8% buy with +25.6% price target, covering 53% of fund – bullish but limited scope
- Fund basics: P/E 20.28, yield 0.9% – moderate valuation, no strong catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [Should You Invest in the iShares U.S. Transportation ETF (IYT)?](https://finance.yahoo.com/markets/stocks/articles/invest-ishares-u-transportation-etf-102003782.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Sector ETF report for IYT.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 80.12 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 83.05 (-3.5%), 50d 85.53 (-6.3%), 200d 81.13 (-1.2%); 50d above 200d
Momentum: RSI(14) 31.9 | MACD -1.617 vs signal -1.361 (histogram -0.256)
Returns: 1d +0.3% | 5d -2.1% | 1m -7.9% | 3m -4.6%
52-week range: 68.14 - 90.01 (now 54.8% of the way up)
Volatility: ATR(14) 1.24 (1.6% of price) | annualised 20d 15.9%
Volume: 0.44x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 53.1% of the fund by weight
Ratings by weight: buy 90.8% | hold 9.2% | sell 0.0% (mean 1.84 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.6% above the current prices
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
Shares outstanding: 27.47M | fund size: 2.20B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals weak but low volume, analyst view bullish but limited coverage, fundamentals moderate, flows unknown.

**Main reasons it gave:**
- US Treasury yields rose modestly, no policy surprise
- Price below 20d, 50d, 200d SMAs; RSI 34, low volume
- Analyst coverage 44.4% of fund, 90% buy, +15.9% price target
- Fund fundamentals moderate: P/E 15, yield 2.7%, 3‑yr return +1.7%/yr
- Fund flows direction unknown, share count change n/a

<details><summary><b>News</b> — score +0.00</summary>

- [KSA’s Daughter Damilola Breaks Silence: “I Never Knew Pain Till I Lived With My Father”](https://ng.headtopics.com/news/ksa-s-daughter-damilola-breaks-silence-i-never-knew-pain-88034967)  
  <sub>Head Topics, 11 hours ago</sub>  
  A woman identifying herself as Damilola, who describes herself as a daughter of Juju legend King Sunny Ade, has made a series of allegations against him in...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 37.21 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 38.25 (-2.7%), 50d 37.79 (-1.5%), 200d 38.14 (-2.5%); 50d below 200d
Momentum: RSI(14) 34.0 | MACD -0.237 vs signal -0.067 (histogram -0.170)
Returns: 1d +0.1% | 5d -0.6% | 1m -2.9% | 3m -2.6%
52-week range: 35.83 - 41.03 (now 26.4% of the way up)
Volatility: ATR(14) 0.29 (0.8% of price) | annualised 20d 8.3%
Volume: 0.35x the 20-day average
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
Three-year record: +1.7% a year | beta to the market 0.18
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
Weighted price target: +15.9% above the current prices
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
Shares outstanding: 17.02M | fund size: 633.21M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Overall neutral: no macro surprise, no decisive technical break on heavy volume, and mixed signals from fundamentals and analyst view.

**Main reasons it gave:**
- Analyst consensus 100% buy with +52.3% price target
- Price below 20‑day, 50‑day, and 200‑day SMAs; MACD negative
- Low valuation: P/E 11.9, P/B 1.39, solid 3‑year record (+10.9% annual)
- No macro surprise: yields stable, dollar up, VIX low

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 53.26 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 53.89 (-1.2%), 50d 54.49 (-2.2%), 200d 57.18 (-6.8%); 50d below 200d
Momentum: RSI(14) 44.8 | MACD -0.454 vs signal -0.422 (histogram -0.032)
Returns: 1d -1.4% | 5d +0.7% | 1m -4.3% | 3m +2.8%
52-week range: 50.48 - 66.99 (now 16.9% of the way up)
Volatility: ATR(14) 0.63 (1.2% of price) | annualised 20d 14.7%
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
Three-year record: +10.9% a year | beta to the market 0.44
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +52.3% above the current prices
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
Shares outstanding: 119.03M | fund size: 6.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, technicals bullish but low volume, analyst view strongly positive yet limited to ~49% of fund, and fund‑flow data unavailable.

**Main reasons it gave:**
- Treasury yields rose modestly this week, curve remains upward sloping (normal)
- SMH price above 20‑day, 50‑day, and 200‑day SMAs, RSI 62, MACD positive, but volume at 0.42× 20‑day average
- Analyst coverage of top 5 holdings (49% weight) is 100% buy with +35.9% price target
- Fund flows direction unknown, share count change n/a, no flow signal

<details><summary><b>News</b> — score +0.00</summary>

- [Michael Burry Bets Against the Memory Boom: These ETFs Could Be Exposed if He’s Right](https://www.benzinga.com/etfs/sector-etfs/26/09/61934916/michael-burry-bets-against-the-memory-boom-these-etfs-could-be-exposed-if-hes-right)  
  <sub>Benzinga, 19 hours ago</sub>  
  Michael Burry is betting against the memory boom as Chinese supply rises. Here's why some semiconductor ETFs could face risks if his thesis plays out.
- [Semiconductor ETFs Hit Historic AUM: SMH at $70B, SOXX at $46B](https://www.kucoin.com/news/flash/semiconductor-etfs-hit-historic-aum-smh-at-70b-soxx-at-46b)  
  <sub>KuCoin, 21 hours ago</sub>  
  Semiconductor ETFs are registering historic capital inflows — and the data is not subtle.The VanEck Semiconductor ETF ($SMH) has seen assets under...
- [REX Shares Launches REX AI Chipmaking ETF (CHIP)](https://finance.yahoo.com/technology/ai/articles/rex-shares-launches-rex-ai-120000192.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  MIAMI, September 23, 2026--REX Shares ("REX"), a leading innovator in alternative ETFs, today announced the launch of the REX AI Chipmaking ETF (Ticker:...
- [Semiconductor relative momentum falls below 20-year average (SMH:NASDAQ)](https://seekingalpha.com/news/4645890-semiconductor-relative-momentum-falls-below-20-year-average)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Semiconductor stocks lag the S&P 500 as SMH-SPY 100-day spread drops below its 20-year average.
- [Nasdaq Jumps To Close At Record As Chipmakers Climb, Oil Prices Cool — AAPL, META, SPCX, MSFT, VKTX In Focus](https://www.tradingview.com/news/stocktwits:2ad8240a2094b:0-nasdaq-jumps-to-close-at-record-as-chipmakers-climb-oil-prices-cool-aapl-meta-spcx-msft-vktx-in-focus/)  
  <sub>TradingView, 18 hours ago</sub>  
  The tech-focused Nasdaq 100 soared to its record high on Tuesday amid strong gains in tech and chipmakers, while investors looked ahead at the highly...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.30</summary>

```text
Last close 600.03 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 562.27 (+6.7%), 50d 564.77 (+6.2%), 200d 489.67 (+22.5%); 50d above 200d
Momentum: RSI(14) 62.1 | MACD 3.397 vs signal -1.492 (histogram 4.889)
Returns: 1d +0.7% | 5d +10.7% | 1m +7.1% | 3m -3.5%
52-week range: 321.06 - 668.91 (now 80.2% of the way up)
Volatility: ATR(14) 16.77 (2.8% of price) | annualised 20d 35.3%
Volume: 0.42x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

```text
Rolled up from the 5 largest holdings, 49.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +35.9% above the current prices
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
Shares outstanding: 118.34M | fund size: 71.00B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – analyst coverage is bullish, but technicals are weak, macro conditions are risk‑off for emerging markets, and fundamentals are modest.

**Main reasons it gave:**
- Analyst view: 100% buy rating on 39.5% of fund weight with +15.9% price target
- Technicals: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 40.3; MACD negative; volume 0.32× 20‑day average
- Macro: US dollar index up 1.34% on the week, indicating risk‑off for emerging markets
- Fund basics: low valuation (P/E 13.81, P/B 1.21) but modest three‑year return (+2.3% per year)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 37.51 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 39.35 (-4.7%), 50d 39.22 (-4.4%), 200d 39.28 (-4.5%); 50d below 200d
Momentum: RSI(14) 40.3 | MACD -0.560 vs signal -0.238 (histogram -0.322)
Returns: 1d -0.3% | 5d -3.2% | 1m -7.9% | 3m -6.2%
52-week range: 31.90 - 43.74 (now 47.4% of the way up)
Volatility: ATR(14) 0.76 (2.0% of price) | annualised 20d 34.6%
Volume: 0.32x the 20-day average
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
Three-year record: +2.3% a year | beta to the market 0.44
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 39.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.9% above the current prices
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
Shares outstanding: 15.65M | fund size: 587.03M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst view is offset by weak technicals, high valuation and yield convergence with T‑bills, and no macro surprise.

**Main reasons it gave:**
- Analyst coverage: 39.9% of fund weighted, all buy, price target +17.7% above current price
- Technicals: price below 20‑day SMA (95.40) and RSI 30.1, indicating weak momentum
- Macro: Treasury yields unchanged (+0.06 on 10‑yr) and market expects further rate hikes, no surprise
- Fundamentals: high P/E 30.19 and yield 3.6% similar to T‑bills, limiting upside
- Yield convergence: VNQ yield 3.6% comparable to SGOV 3.7% with near‑zero risk, reducing relative attractiveness

<details><summary><b>News</b> — score +0.00</summary>

- [VNQ vs. SGOV: Why Own a REIT ETF When T-Bills Pay Almost as Much With Zero Rate Risk?](https://finance.yahoo.com/real-estate/articles/vnq-vs-sgov-why-own-154633834.html)  
  <sub>Yahoo Finance, 24 hours ago</sub>  
  VNQ yields ~3.6% with 25% drawdown risk in rate spikes, while SGOV matches it at ~3.7% with near-zero price volatility. VNQ's data center and tower REIT...
- [Vanguard REIT ETF declares quarterly distribution of $0.8046](https://www.tradingview.com/news/seekingalpha:6b7520e93094b:0-vanguard-reit-etf-declares-quarterly-distribution-of-0-8046/)  
  <sub>TradingView, 22 hours ago</sub>  
  Content provided by Seeking Alpha is intended for information purposes only, and that Seeking Alpha does not offer any personalist investment advice and is...
- [REIT ETF and T-bill yields converge, but risk p...](https://pluang.com/en/news-feed/vnq-vs-sgov-mengapa-memiliki-etf-reit-saat-t-bills-memberikan-hasil-hampir-sama)  
  <sub>Pluang, 23 hours ago</sub>  
  Vanguard Real Estate ETF (VNQ) and iShares 0-3 Month Treasury Bond ETF (SGOV) currently offer similar yields, making T-bills attractive due to near-zero...
- [Howard Marks: $40T Debt Isn’t a Reason to Sell Stocks. ETFs Could Help - SPDR Gold Shares (ARCA:GLD)](https://www.benzinga.com/etfs/sector-etfs/26/09/61931952/billionaire-howard-marks-says-americas-40t-debt-problem-isnt-a-reason-to-sell-stocks-heres-where-etfs-come-in)  
  <sub>Benzinga, 20 hours ago</sub>  
  Howard Marks says selling U.S. stocks won't solve U.S. fiscal problems. These ETFs offer gold, international and real estate exposure.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 91.92 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 95.40 (-3.7%), 50d 97.47 (-5.7%), 200d 94.32 (-2.6%); 50d above 200d
Momentum: RSI(14) 30.1 | MACD -1.334 vs signal -1.081 (histogram -0.253)
Returns: 1d -2.0% | 5d -2.3% | 1m -6.7% | 3m -6.1%
52-week range: 87.00 - 100.95 (now 35.2% of the way up)
Volatility: ATR(14) 1.18 (1.3% of price) | annualised 20d 11.6%
Volume: 0.37x the 20-day average
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
Three-year record: +10.6% a year | beta to the market 0.98
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

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
Shares outstanding: 761.95M | fund size: 70.03B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral – no macro surprise, mixed technicals, thin analyst coverage with slight bearish price target, fundamentals modestly positive but no clear catalyst.

**Main reasons it gave:**
- Macro: Treasury yields rose modestly, VIX fell to 14.5, Fed target unchanged – no surprise data
- Technical: price below 20‑day SMA, MACD negative, RSI 45.8 – mixed signals, no decisive break
- Analyst view: thin coverage (9% weight) shows slight bearish price target (-16.5%) and mixed ratings
- Fundamentals: low valuation multiples (P/B 0.20, P/S 0.12) and strong 3‑year performance (+29.3%/yr) but no clear catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [VHT vs. XBI: Is Diversified Healthcare Exposure or Biotech Stocks the Smarter Choice for Investors?](https://www.fool.com/coverage/etfs/2026/09/22/vht-vs-xbi-is-diversified-healthcare-exposure-or-biotech-stocks-the-smarter-choice-for-investors/)  
  <sub>The Motley Fool, 19 hours ago</sub>  
  The Vanguard Health Care ETF (VHT +0.69%) offers broad sector exposure and lower fees, while the State Street SPDR S&P Biotech ETF (XBI +2.30%) provides a...
- [SBIO: Big Pharma Needs What This Fund Owns (NYSEARCA:SBIO)](https://seekingalpha.com/article/4948736-sbio-big-pharma-needs-what-this-fund-owns?source=google_editors_picks)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  The ALPS Medical Breakthroughs ETF is a Buy, as its pullback offers a better entry into late-stage biotech. Click for more on the SBIO ETF.
- [How Is Incyte’s Stock Performance Compared to Other Biotech Stocks?](https://finance.yahoo.com/healthcare/articles/incyte-stock-performance-compared-other-045305372.html)  
  <sub>Yahoo Finance, 10 hours ago</sub>  
  Based in Wilmington, Delaware, Incyte Corporation (INCY) is a global biopharmaceutical company that discovers, develops, and commercializes innovative...
- [VKTX Stock On Track To Beat LLY, NVO This Month After Obesity Drug Data — Can Viking Win Over Wegovy And Zepbound Users?](https://stocktwits.com/news-articles/markets/equity/vktx-stock-beat-lly-nvo-this-month-obesity-drug-data-can-viking-win-over-wegovy-zepbound-users/cZMEh0VRB7V)  
  <sub>Stocktwits, 13 hours ago</sub>  
  Obesity specialist Lou Aronne said switching from a GLP-1 drug to a dual GLP-1/GIP drug could mean greater weight loss.
- [Indices Churn On Mix of Good and Bad Action](https://pro.thestreet.com/market-commentary/indices-churn-on-mix-of-good-and-bad-action)  
  <sub>TheStreet Pro, 19 hours ago</sub>  
  Financials broke down on the flat yield curve while biotech caught the speculative bid.
- [iShares Biotechnology ETF (IBB) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/IBB/)  
  <sub>Yahoo! Finance Canada, 2 hours ago</sub>  
  Find the latest iShares Biotechnology ETF (IBB) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Could IBRX Be A Tokenized Stock? Founder’s Tease Sends ImmunityBio Traders Into Speculation Mode](https://stocktwits.com/news-articles/markets/equity/ibrx-tokenized-stock-founder-tease-immunitybio-traders-speculation-mode/cZMRI94RB4K)  
  <sub>Stocktwits, 5 hours ago</sub>  
  IBRX stock, ImmunityBio, ImmunityBio Patrick Soon-Shiong, tokenized stocks, Nant Global Finance, SEC Innovation Exemption, blockchain stock trading.
- [Rocket Lab CEO Puts Iridium Deal Alongside SpaceX And Amazon’s Spectrum Bets: ‘You Can’t Just Magic Up Spectrum’](https://stocktwits.com/news-articles/markets/equity/rocket-lab-ceo-iridium-deal-spacex-amazon-spectrum-bets/cZMEhNCRB7n)  
  <sub>Stocktwits, 13 hours ago</sub>  
  CEO Peter Beck estimated Rocket Lab could have deployed Iridium's constellation for about $350 million instead of $3 billion.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 156.66 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 160.88 (-2.6%), 50d 157.58 (-0.6%), 200d 137.48 (+13.9%); 50d above 200d
Momentum: RSI(14) 45.8 | MACD -0.778 vs signal -0.043 (histogram -0.735)
Returns: 1d -1.0% | 5d +1.7% | 1m -5.5% | 3m +6.5%
52-week range: 95.86 - 169.55 (now 82.5% of the way up)
Volatility: ATR(14) 4.18 (2.7% of price) | annualised 20d 24.4%
Volume: 0.54x the 20-day average
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
Ratings by weight: buy 52.0% | hold 48.0% | sell 0.0% (mean 2.18 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -16.5% above the current prices
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
Shares outstanding: 72.77M | fund size: 11.40B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals show no decisive break, analyst view positive but thin, fundamentals moderate.

**Main reasons it gave:**
- Analyst coverage thin (20.9% of fund) but shows 78.9% buy rating and +19.2% price target
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 40.4; low volume; no decisive break
- Macro: modest rise in yields (+0.06% on 10‑yr) and no surprise in inflation (3.4%) or unemployment (4.1%)
- Fundamentals: P/E 19.5, consumer‑cyclical sector facing housing headwinds, beta 1.46

<details><summary><b>News</b> — score +0.00</summary>

- [State Street SPDR S&P Homebuilders ETF (XHB) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XHB/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  State Street SPDR S&P Homebuilders ETF (XHB) · 1.32% · -7.91% · -1.33% · -4.74% · -11.89% · 30.44% · 114.10%. Key Events. Baseline.
- [Is "classic value investing" making a comeback? As the U.S. housing market faces headwinds, Berkshire Hathaway is bucking the trend by increasing its stake in homebuilder Lennar Corporation.](https://news.futunn.com/en/post/1000054875/is-classic-value-investing-making-a-comeback-as-the-us)  
  <sub>富途牛牛, 14 hours ago</sub>  
  Accordingto a securities filing, Berkshire Hathaway has made a substantial purchase of shares in the struggling homebuilder Lennar Corporation (LEN.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 98.33 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 100.42 (-2.1%), 50d 104.86 (-6.2%), 200d 106.56 (-7.7%); 50d below 200d
Momentum: RSI(14) 40.4 | MACD -2.472 vs signal -2.394 (histogram -0.078)
Returns: 1d +1.4% | 5d +0.6% | 1m -7.7% | 3m -9.1%
52-week range: 94.86 - 121.36 (now 13.1% of the way up)
Volatility: ATR(14) 2.15 (2.2% of price) | annualised 20d 19.9%
Volume: 0.37x the 20-day average
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
Three-year record: +9.3% a year | beta to the market 1.46
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 20.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 78.9% | hold 21.1% | sell 0.0% (mean 2.15 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.2% above the current prices
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

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technical weakness, limited analyst coverage, and ambiguous flows.

**Main reasons it gave:**
- Analyst coverage of top holdings (37% weight) is 100% buy with +12.1% price target
- Technical indicators show price below 20‑day and 50‑day SMA, RSI 41.7, MACD negative
- Macro data shows no surprise; yields modestly up, VIX low, dollar up
- Fund flows direction unknown, share count unchanged

<details><summary><b>News</b> — score +0.00</summary>

- [Why Is Newmont Stock Falling Wednesday?](https://www.benzinga.com/trading-ideas/movers/26/09/61943335/why-is-newmont-stock-falling-wednesday)  
  <sub>Benzinga, 3 hours ago</sub>  
  Newmont (NEM) stock dips premarket as gold drops. Explore technical levels, key support at $121.50, analyst ratings, and ETF exposure.
- [State Street Consumer Staples Select Sector SPDR ETF (XLP) stock price, news, quote and history](https://au.finance.yahoo.com/quote/XLP/)  
  <sub>Yahoo Finance Australia, 10 hours ago</sub>  
  Find the latest State Street Consumer Staples Select Sector SPDR ETF (XLP) stock quote, history, news and other vital information to help you with your...
- [Staples ETF Widens Gap Over Discretionary in 2026](https://etfdb.com/sector-investing-content-hub/staples-etf-widens-gap/)  
  <sub>ETF Database, 22 hours ago</sub>  
  The State Street Consumer Staples Select Sector SPDR ETF (XLP A) has climbed 6.6% so far in 2026, according to State Street data as of September 21.
- [Leading And Lagging Sectors For September 23, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61944915/leading-and-lagging-sectors-september-23-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLE) State Street Energy Select Sector SPDR ETF 62.26 0.48 0.77 300.1K (NYSE:XLP) State Street...
- [Nasdaq 100 Flirts with Records, Oil Sinks for Fifth Day: Stock Market Today](https://www.tradingview.com/news/benzinga:de108ba70094b:0-nasdaq-100-flirts-with-records-oil-sinks-for-fifth-day-stock-market-today/)  
  <sub>TradingView, 21 hours ago</sub>  
  The Nasdaq 100 carved out a fresh intraday record by midday Tuesday as the artificial intelligence trade powered ahead.Speaking at the United Nations...
- [This Wall Street Veteran Says the Market Has Bottomed: Here’s What He Thinks Comes Next](https://www.aol.com/articles/wall-street-veteran-says-market-124713000.html)  
  <sub>AOL.com, 8 hours ago</sub>  
  While the Dow slides into correction territory and the "fear gauge" flashes red, the loudest voice on Wall Street is also the calmest.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 50.47 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 51.70 (-2.4%), 50d 51.74 (-2.5%), 200d 50.46 (+0.0%); 50d above 200d
Momentum: RSI(14) 41.7 | MACD -0.584 vs signal -0.375 (histogram -0.209)
Returns: 1d +1.5% | 5d -0.5% | 1m -5.7% | 3m -0.8%
52-week range: 42.23 - 53.67 (now 72.0% of the way up)
Volatility: ATR(14) 0.77 (1.5% of price) | annualised 20d 14.1%
Volume: 0.39x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Natural Resources
What it holds: P/E 24.59 | P/B 3.00 | P/S 2.01 | 3y earnings growth n/a
Yield: 1.6%
Three-year record: +10.3% a year | beta to the market 0.82
Cost and size: expense ratio 0.08% | net assets 8.75B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Linde PLC 13.1%, Newmont Corp 7.8%, Freeport-McMoRan Inc 6.3%, Corteva Inc 4.9%, Air Products and Chemicals Inc 4.8%
Sector mix: Basic materials 84.5%, Consumer cyclical 15.5%
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
Rolled up from the 5 largest holdings, 37.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.70 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.1% above the current prices
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
Shares outstanding: 71.92M | fund size: 3.63B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, mixed technicals, bullish analyst view limited to 45.5% of fund, and no clear fund‑flow signal. Overall the evidence points to a neutral stance.

**Main reasons it gave:**
- Analyst coverage 45.5% of fund, 100% buy rating, +13.8% price target
- Technical: price +0.5% above 20‑day SMA, -0.8% below 200‑day SMA; RSI 52.5, volume 0.5× avg
- Macro: modest yield rises, VIX low (14.49), no policy surprise
- Fund flows: direction unknown, share count change n/a (no clear inflow/outflow signal)

<details><summary><b>News</b> — score +0.00</summary>

- [Pinterest Sinks 5% as Month-Long Slide Deepens; Reddit Slips, Snap Stays Put](https://247wallst.com/investing/2026/09/22/pinterest-sinks-5-as-month-long-slide-deepens-reddit-slips-snap-stays-put/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Pinterest keeps sliding lower while its closest peers barely flinch, and no news has surfaced to explain the gap. Something is moving inside Pinterest's...
- [Trump July disclosure: 1,156 trades, Microsoft and Amazon among largest sales](https://www.google.com/goto?url=CAESwwEB6zswFatZlCZqYpQKeaHvsAUoDqgUiZBkbE4rGDHczIR9eIaxoaSWwJn8V2YUKbhBJS7SesB6FEdKfFtJ4Az0zR048Z-Yn3XHl_apkY5YQzjtkNeEbpNEJUBEmLKcdj_s8ChOZxWvzpjyiWggJCIjh-nejsZcTk4AU_xgSpTpTOXQaW6Pxvr_wjBeLmCpD4LqCVmBiWWS3xo08wMDZtNZe7aDIjqY53xfqpcIAnzwxmglKVCOEtocZtxUbf_1Z1IqRxU)  
  <sub>TradingView, 10 hours ago</sub>  
  U.S. President Donald Trump reported 1156 securities transactions in July, with the trades carrying a combined value of roughly $79M to $270M, according to...
- [Weekly ETFs: Eight of 11 sectors record outflows; Gold leads inflows](https://www.tradingview.com/news/seekingalpha:c3689e0ef094b:0-weekly-etfs-eight-of-11-sectors-record-outflows-gold-leads-inflows/)  
  <sub>TradingView, 23 hours ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 ETF Trust AMEX:SPY, saw outflows of $22.64B for the week ended September 18, while its price...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 113.10 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 112.50 (+0.5%), 50d 111.28 (+1.6%), 200d 113.98 (-0.8%); 50d below 200d
Momentum: RSI(14) 52.5 | MACD 0.507 vs signal 0.476 (histogram 0.031)
Returns: 1d -1.4% | 5d -0.8% | 1m +1.5% | 3m +5.4%
52-week range: 105.38 - 120.08 (now 52.5% of the way up)
Volatility: ATR(14) 1.95 (1.7% of price) | annualised 20d 21.7%
Volume: 0.50x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Communications
What it holds: P/E 15.38 | P/B 2.92 | P/S 2.06 | 3y earnings growth n/a
Yield: 1.3%
Three-year record: +21.8% a year | beta to the market 0.85
Cost and size: expense ratio 0.08% | net assets 22.43B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Meta Platforms Inc Class A 16.8%, Alphabet Inc Class A 10.3%, Alphabet Inc Class C 8.2%, AT&T Inc 5.3%, Verizon Communications Inc 5.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.54 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.8% above the current prices
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
Shares outstanding: 202.30M | fund size: 22.88B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, mixed fundamentals and technicals, bullish analyst rating offset by bearish oil outlook and mixed inventory data.

**Main reasons it gave:**
- Analyst coverage: 100% buy rating, weighted price target +6% above current price
- EIA price outlook: WTI crude forecast to decline ~10% over six months
- Energy inventories: crude oil draw of -0.6M bbl (bullish) vs builds in gasoline (+0.8M) and diesel (+1.6M) (bearish) – mixed
- Technical momentum: RSI 46.7, MACD histogram -0.438, 5‑day return -5% (short‑term bearish)
- Macro data: Treasury yields up modestly, inflation 3.4% and unemployment 4.1% in line with expectations

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Energy Select Sector SPDR ETF (XLE) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLE/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  State Street Energy Select Sector SPDR ETF (XLE) · -6.29% · -2.92% · 4.16% · 38.18% · 40.94% · 153.14% · 430.02%. Key Events. Baseline. Advanced...
- [Winning and Losing Sectors for ETF Investors](https://www.baystreet.ca/amp/articles/etfs.aspx?articleid=124070)  
  <sub>Baystreet.ca, 5 hours ago</sub>  
  At the start of the second half of 2026, the technology sector looked like it would give back some of its gains. Instead, software and semiconductor stocks...
- [Leading And Lagging Sectors For September 23, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61944915/leading-and-lagging-sectors-september-23-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLE) State Street Energy Select Sector SPDR ETF 62.26 0.48 0.77 300.1K (NYSE:XLP) State Street...
- [Oil Slid, Sending Energy ETFs Lower Before The Open](https://finimize.com/content/oil-slid-sending-energy-etfs-lower-before-the-open)  
  <sub>Finimize, 24 hours ago</sub>  
  WTI fell to $93.51 a barrel and Brent to $98.50, while TotalEnergies signed an MOU with Venezuela's PDVSA and Solaris lined up $1 billion of notes due 2032.
- [Analyzing The Venezuelan Oil Deal And Possible Opportunities (NYSEARCA:XLE)](https://seekingalpha.com/article/4948973-analyzing-the-venezuelan-oil-deal-and-possible-opportunities?source=google_editors_picks)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Venezuela's political shift and a new US-backed joint venture open significant long-term opportunities for upstream and oilfield services companies.
- [Weekly ETFs: Eight of 11 sectors record outflows; Gold leads inflows](https://www.tradingview.com/news/seekingalpha:c3689e0ef094b:0-weekly-etfs-eight-of-11-sectors-record-outflows-gold-leads-inflows/)  
  <sub>TradingView, 23 hours ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 ETF Trust AMEX:SPY, saw outflows of $22.64B for the week ended September 18, while its price...
- [State Street SPDR S&P Oil & Gas Exploration & Production ETF (XOP) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XOP/)  
  <sub>Yahoo! Finance Canada, 9 hours ago</sub>  
  Find the latest State Street SPDR S&P Oil & Gas Exploration & Production ETF (XOP) stock quote, history, news and other vital information to help you with...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 62.64 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 64.02 (-2.2%), 50d 61.44 (+1.9%), 200d 55.90 (+12.1%); 50d above 200d
Momentum: RSI(14) 46.7 | MACD 0.607 vs signal 1.045 (histogram -0.438)
Returns: 1d +0.3% | 5d -5.0% | 1m -1.6% | 3m +15.0%
52-week range: 42.61 - 65.93 (now 85.9% of the way up)
Volatility: ATR(14) 1.30 (2.1% of price) | annualised 20d 21.9%
Volume: 0.49x the 20-day average
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
Three-year record: +15.5% a year | beta to the market -0.07
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
US inventories, week ending 2026-09-11 (published the following Wednesday)
  Crude oil: 423.4 million barrels, -0.6 on the week (a draw), 38% percentile over 52 weeks
  Petrol: 207.7 million barrels, +0.8 on the week (a build), 13% percentile over 52 weeks -- low for the time of year
  Diesel: 107.9 million barrels, +1.6 on the week (a build), 33% percentile over 52 weeks
  Natural gas: 3,298.0 billion cubic feet, +44.0 on the week (a build), 71% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.55</summary>

```text
Rolled up from the 5 largest holdings, 51.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.0% above the current prices
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
Shares outstanding: 186.42M | fund size: 11.68B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals show mixed signals, analyst view bullish but limited weight, fund flows direction unknown.

**Main reasons it gave:**
- Analyst coverage of top 5 holdings is 100% buy with +13.4% price target
- Technicals show price below 20‑day and 50‑day SMA, RSI at 30, MACD negative
- Macro data shows no surprise: yields up modestly, VIX low, no policy shift
- Fund flows direction unknown, share count change not available

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 54.81 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 57.13 (-4.0%), 50d 57.16 (-4.1%), 200d 53.71 (+2.1%); 50d above 200d
Momentum: RSI(14) 30.0 | MACD -0.464 vs signal -0.170 (histogram -0.294)
Returns: 1d -1.9% | 5d -3.6% | 1m -4.6% | 3m +1.7%
52-week range: 47.81 - 58.56 (now 65.2% of the way up)
Volatility: ATR(14) 0.75 (1.4% of price) | annualised 20d 13.2%
Volume: 0.60x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Financial
What it holds: P/E 16.36 | P/B 2.42 | P/S 3.50 | 3y earnings growth n/a
Yield: 1.4%
Three-year record: +20.0% a year | beta to the market 0.71
Cost and size: expense ratio 0.08% | net assets 54.59B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: JPMorgan Chase & Co 11.7%, Berkshire Hathaway Inc Class B 11.3%, Visa Inc Class A 7.7%, Mastercard Inc Class A 5.8%, Bank of America Corp 5.0%
Sector mix: Financial services 98.1%, Technology 1.6%, Industrials 0.3%
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
Rolled up from the 5 largest holdings, 41.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.78 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.4% above the current prices
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
Shares outstanding: 883.44M | fund size: 48.43B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals not decisive, fundamentals relatively expensive, analyst coverage limited.

**Main reasons it gave:**
- Yield curve unchanged (+1.03) – no macro surprise
- Price below 20‑day SMA (170.95 vs 173.07) – slight bearish technical
- RSI 39.1 – low momentum
- P/E 28.43 – high valuation relative to industrials
- Analyst coverage 25.8% of fund – limited bullish coverage

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Energy Select Sector SPDR ETF (XLE) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLE/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Find the latest State Street Energy Select Sector SPDR ETF (XLE) stock quote, history, news and other vital information to help you with your stock trading...
- [BofA clients resumed buying stocks last week after big de-risking](https://www.tradingview.com/news/seekingalpha:f17340018094b:0-bofa-clients-resumed-buying-stocks-last-week-after-big-de-risking/)  
  <sub>TradingView, 2 hours ago</sub>  
  Overall, clients returned to buying U.S. equities following a week of de-risking, purchasing $1.3B in single stocks and $1.7B in exchange-traded funds,...
- [Leading And Lagging Sectors For September 23, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61944915/leading-and-lagging-sectors-september-23-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLE) State Street Energy Select Sector SPDR ETF 62.26 0.48 0.77 300.1K (NYSE:XLP) State Street...
- [State Street Materials Select Sector SPDR ETF (XLB) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLB/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Find the latest State Street Materials Select Sector SPDR ETF (XLB) stock quote, history, news and other vital information to help you with your stock...
- [State Street Consumer Staples Select Sector SPDR ETF (XLP) stock price, news, quote and history](https://au.finance.yahoo.com/quote/XLP/)  
  <sub>Yahoo Finance Australia, 10 hours ago</sub>  
  Find the latest State Street Consumer Staples Select Sector SPDR ETF (XLP) stock quote, history, news and other vital information to help you with your...
- [Exchange-Traded Funds Rise, US Equities Mixed After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-rise-us-171035923.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV edged higher. Actively traded Invesco QQQ Trust (QQQ) added 0.5%.
- [Micron Earnings Are Set for a 10x Jump: The Stock Is Still the Cheapest in Tech](https://www.benzinga.com/markets/tech/26/09/61930540/micron-third-quarter-earnings-10x-jump-cheapest-tech-stock)  
  <sub>Benzinga, 21 hours ago</sub>  
  Micron earnings are expected to jump 10-fold on Sept. 30, yet the stock trades at 7.3 times forward profits, the cheapest valuation in XLK.
- [Is First Trust Industrials/Producer Durables AlphaDEX ETF (FXR) a Strong ETF Right Now?](https://finance.yahoo.com/markets/stocks/articles/first-trust-industrials-producer-durables-102002820.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Launched on 05/08/2007, the First Trust Industrials/Producer Durables AlphaDEX ETF (FXR) is a smart beta exchange traded fund offering broad exposure to the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 170.95 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 173.07 (-1.2%), 50d 178.55 (-4.3%), 200d 171.81 (-0.5%); 50d above 200d
Momentum: RSI(14) 39.1 | MACD -2.834 vs signal -2.812 (histogram -0.022)
Returns: 1d +0.6% | 5d +1.2% | 1m -5.2% | 3m -4.0%
52-week range: 147.83 - 186.51 (now 59.8% of the way up)
Volatility: ATR(14) 2.39 (1.4% of price) | annualised 20d 13.3%
Volume: 0.46x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 25.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.0% above the current prices
Holdings read: CAT, GE, RTX, GEV, UNP
Recent rating changes among them:
  - CAT: 2024-10-14 JP Morgan: main, Overweight -> Overweight
  - GE: 2026-07-23 Bernstein: main, Outperform -> Outperform
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 136.63M | fund size: 23.36B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: strong analyst bullishness is limited to ~45% of the fund, technicals are positive but volume is weak, macro data show no surprise and valuations are high, offset by strong past performance. No insider flow signal.

**Main reasons it gave:**
- Analyst view: 100% buy rating with +25.7% price target (covers 45.7% of fund)
- Technicals: price above 20‑day, 50‑day, 200‑day SMAs, RSI 65.5, MACD positive, but volume only 0.42× 20‑day average
- Macro: yields modestly higher, VIX low, no surprise data; Fed target unchanged at 4.0%
- Fundamentals: high valuations (P/E 33, P/B 11.4) offset by strong 3‑year performance (+34.3%/yr)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 195.08 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 186.70 (+4.5%), 50d 183.57 (+6.3%), 200d 162.94 (+19.7%); 50d above 200d
Momentum: RSI(14) 65.5 | MACD 1.978 vs signal 1.123 (histogram 0.855)
Returns: 1d +0.1% | 5d +6.2% | 1m +6.4% | 3m +5.9%
52-week range: 127.50 - 198.21 (now 95.6% of the way up)
Volatility: ATR(14) 3.52 (1.8% of price) | annualised 20d 21.7%
Volume: 0.42x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

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
Rolled up from the 5 largest holdings, 45.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.55 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.7% above the current prices
Holdings read: NVDA, AAPL, MSFT, AVGO, MU
Recent rating changes among them:
  - NVDA: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - AAPL: 2026-09-18 Evercore ISI Group: main, Outperform -> Outperform
  - MSFT: 2026-09-23 Stifel: up, Hold -> Buy
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
Shares outstanding: 640.16M | fund size: 124.88B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall call; no macro surprise, technicals bearish but not decisive, analyst view bullish but limited coverage, no flow data.

**Main reasons it gave:**
- Technical: price 82.40 below 20d SMA (84.23), 50d SMA (84.83), 200d SMA (83.61); RSI 38.9, MACD negative
- Macro: yields up modestly (3‑month +0.06%, 5‑yr +0.11%, 10‑yr +0.06%); upward sloping curve (+1.03); VIX low at 14.49; no policy surprise
- Analyst view: 100% buy coverage of top holdings (39.6% weight) with weighted price target +12.6% above current price
- Fund flows: direction unknown, share count change n/a, no insider positioning data

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Consumer Staples Select Sector SPDR ETF (XLP) stock price, news, quote and history](https://au.finance.yahoo.com/quote/XLP/)  
  <sub>Yahoo Finance Australia, 10 hours ago</sub>  
  State Street Consumer Staples Select Sector SPDR ETF (XLP) · -1.19% · -3.79% · 1.77% · 6.50% · 6.12% · 17.63% · 219.73%. Key events. Baseline.
- [Should You Invest in the State Street Consumer Staples Select Sector SPDR ETF (XLP)?](https://finance.yahoo.com/markets/stocks/articles/invest-state-street-consumer-staples-102003398.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Sector ETF report for XLP.
- [Only three consumer staples stocks have held Strong Buy ratings for at least 60 days (XLP:NYSEARCA)](https://seekingalpha.com/news/4645966-only-three-consumer-staples-stocks-have-held-strong-buy-ratings-for-at-least-60-days)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  While consumer staples are generally associated with defensive demand, agricultural products and food distribution companies remain exposed to commodity...
- [Staples ETF Widens Gap Over Discretionary in 2026](https://etfdb.com/sector-investing-content-hub/staples-etf-widens-gap/)  
  <sub>ETF Database, 22 hours ago</sub>  
  The State Street Consumer Staples Select Sector SPDR ETF (XLP A) has climbed 6.6% so far in 2026, according to State Street data as of September 21.
- [Leading And Lagging Sectors For September 23, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61944915/leading-and-lagging-sectors-september-23-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLE) State Street Energy Select Sector SPDR ETF 62.26 0.48 0.77 300.1K (NYSE:XLP) State Street...
- [Should You Invest in the First Trust Consumer Staples AlphaDEX ETF (FXG)?](https://finance.yahoo.com/markets/stocks/articles/invest-first-trust-consumer-staples-102002734.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  If you're interested in broad exposure to the Consumer Staples - Broad segment of the equity market, look no further than the First Trust Consumer Staples...
- [Weekly ETFs: Eight of 11 sectors record outflows; Gold leads inflows](https://www.tradingview.com/news/seekingalpha:c3689e0ef094b:0-weekly-etfs-eight-of-11-sectors-record-outflows-gold-leads-inflows/)  
  <sub>TradingView, 23 hours ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 ETF Trust AMEX:SPY, saw outflows of $22.64B for the week ended September 18, while its price...
- [Nasdaq 100 Flirts with Records, Oil Sinks for Fifth Day: Stock Market Today](https://www.tradingview.com/news/benzinga:de108ba70094b:0-nasdaq-100-flirts-with-records-oil-sinks-for-fifth-day-stock-market-today/)  
  <sub>TradingView, 21 hours ago</sub>  
  The Nasdaq 100 carved out a fresh intraday record by midday Tuesday as the artificial intelligence trade powered ahead.Speaking at the United Nations...
- [State Street Health Care Select Sector SPDR ETF (XLV) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) · 1.17% · -2.79% · 17.25% · 9.65% · 23.95% · 28.09% · 584.09%. Key Events. Baseline. Advanced...
- [Sector Update: Consumer Stocks Advance Tuesday Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-advance-tuesday-173619109.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Consumer stocks advanced Tuesday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) rising 1.1% and the State Street Consumer...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 82.40 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 84.23 (-2.2%), 50d 84.83 (-2.9%), 200d 83.61 (-1.4%); 50d above 200d
Momentum: RSI(14) 38.9 | MACD -0.717 vs signal -0.491 (histogram -0.226)
Returns: 1d +0.6% | 5d -1.6% | 1m -4.2% | 3m -1.6%
52-week range: 75.60 - 90.01 (now 47.2% of the way up)
Volatility: ATR(14) 0.99 (1.2% of price) | annualised 20d 11.1%
Volume: 0.36x the 20-day average
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
Three-year record: +8.0% a year | beta to the market 0.49
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 39.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.6% above the current prices
Holdings read: WMT, COST, KO, PG, PM
Recent rating changes among them:
  - WMT: 2026-09-10 DA Davidson: main, Buy -> Buy
  - COST: 2026-09-23 BTIG: reit, Buy -> Buy
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 210.17M | fund size: 17.32B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals bearish but no decisive break, analyst view bullish but limited coverage, fundamentals moderate, fund flows data unavailable.

**Main reasons it gave:**
- No macro surprise: yields up modestly, inflation 3.4% in line with expectations
- Technical indicators bearish (RSI 24.4, price below 20d/50d/200d SMA) but low volume, no decisive break
- Analyst coverage 80.9% buy with +24% price target, covering 39.4% of fund weight
- Fund fundamentals moderate: P/E 19, yield 2.8% lower than 10-year Treasury, beta 0.43
- Fund flows data unavailable, no clear insider sentiment

<details><summary><b>News</b> — score +0.00</summary>

- [America’s Power Buildout Is Accelerating. These 3 ETFs Invest in the Infrastructure](https://247wallst.com/investing/etf/2026/09/22/americas-power-buildout-is-accelerating-these-3-etfs-invest-in-the-infrastructure/)  
  <sub>24/7 Wall St., 18 hours ago</sub>  
  PAVE, XLU, and GRID each target America's grid buildout differently, focusing respectively on contractors, regulated utilities, and electrical equipment...
- [Leading And Lagging Sectors For September 23, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61944915/leading-and-lagging-sectors-september-23-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLE) State Street Energy Select Sector SPDR ETF 62.26 0.48 0.77 300.1K (NYSE:XLP) State Street...
- [Three ETFs target U.S. power grid rebuild with distinct approaches amid rising electricity demand.](https://pluang.com/en/news-feed/pembangunan-infrastruktur-listrik-amerika-dan-3-etf-investasi)  
  <sub>Pluang, 18 hours ago</sub>  
  The U.S. electricity grid is undergoing a rapid rebuild driven by rising demand from data centers, factory reshoring, and vehicle electrification.
- [Howard Marks Warns $5 Trillion AI Boom Could Keep Rates Higher: 3 Infrastructure ETFs to Watch](https://www.benzinga.com/markets/economic-data/26/09/61941091/howard-marks-warns-5-trillion-ai-boom-could-keep-rates-higher-3-infrastructure-etfs-to-watch)  
  <sub>Benzinga, 4 hours ago</sub>  
  Oaktree's Howard Marks warns a $5T AI boom will keep interest rates high. Discover 3 infrastructure ETFs to watch as capital demand surges.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 39.90 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 42.27 (-5.6%), 50d 43.61 (-8.5%), 200d 44.52 (-10.4%); 50d below 200d
Momentum: RSI(14) 24.4 | MACD -0.825 vs signal -0.628 (histogram -0.197)
Returns: 1d -1.9% | 5d -3.4% | 1m -6.7% | 3m -11.5%
52-week range: 39.90 - 47.73 (now 0.0% of the way up)
Volatility: ATR(14) 0.63 (1.6% of price) | annualised 20d 14.3%
Volume: 0.46x the 20-day average
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
Three-year record: +11.9% a year | beta to the market 0.43
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 39.4% of the fund by weight
Ratings by weight: buy 80.9% | hold 19.1% | sell 0.0% (mean 2.06 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.2% above the current prices
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
Shares outstanding: 163.27M | fund size: 6.51B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, technicals flat, analyst view bullish but limited coverage, fundamentals moderate, no net flow data.

**Main reasons it gave:**
- Analyst view: 100% buy rating, +10.7% price target, covering 44.3% of fund
- Macro: Treasury yields up 0.06% on week, VIX down 2.7% to 14.49, no policy surprise
- Technical: RSI 52.9, MACD histogram -0.266, volume 0.43x 20‑day average
- Fundamentals: P/E 30.47, yield 1.5%, three‑year record +10.8% per year
- Fund flows: direction unknown, share count change n/a

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Health Care Select Sector SPDR ETF (XLV) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) · 1.17% · -2.79% · 17.25% · 9.65% · 23.95% · 28.09% · 584.09%. Key Events. Baseline. Advanced...
- [These four healthcare stocks have held Strong Buy ratings for 60+ days (XLV:NYSEARCA)](https://seekingalpha.com/news/4645995-these-four-healthcare-stocks-have-held-strong-buy-ratings-for-60-days)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Healthcare stock picks: 4 names with 60+ days of Strong Buy Quant Ratings—BTSG, CNC, AVAH & QTTB.
- [4 Elite Dividend Stocks Yielding Up to 6.14% With Diversified Pipelines That Protect Your Payout](https://247wallst.com/investing/2026/09/23/4-elite-dividend-stocks-yielding-up-to-6-14-with-diversified-pipelines-that-protect-your-payout/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Patent cliffs have buried lesser pharma dividends, yet these four Big Pharma giants keep raising payouts despite losing blockbuster exclusivities worth...
- [BofA clients resumed buying stocks last week after big de-risking](https://www.tradingview.com/news/seekingalpha:f17340018094b:0-bofa-clients-resumed-buying-stocks-last-week-after-big-de-risking/)  
  <sub>TradingView, 2 hours ago</sub>  
  Bank of America Securities clients poured record cash into mid-cap equities AMEX:IJH AMEX:VO and healthcare AMEX:XLV stocks last week while dumping...
- [Leading And Lagging Sectors For September 23, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61944915/leading-and-lagging-sectors-september-23-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLE) State Street Energy Select Sector SPDR ETF 62.26 0.48 0.77 300.1K (NYSE:XLP) State Street...
- [Exchange-Traded Funds Lower, Equity Futures Mixed Pre-Bell Wednesday as Traders Await Developments in US-Iran Talks](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-lower-equity-133135107.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.1%, and the actively t.
- [VKTX Stock On Track To Beat LLY, NVO This Month After Obesity Drug Data — Can Viking Win Over Wegovy And Zepbound Users?](https://stocktwits.com/news-articles/markets/equity/vktx-stock-beat-lly-nvo-this-month-obesity-drug-data-can-viking-win-over-wegovy-zepbound-users/cZMEh0VRB7V)  
  <sub>Stocktwits, 13 hours ago</sub>  
  Obesity specialist Lou Aronne said switching from a GLP-1 drug to a dual GLP-1/GIP drug could mean greater weight loss.
- [Personal imports of cheaper prescription drugs will soon get trickier](https://seekingalpha.com/news/4645823-cbp-rule-personal-importation-prescription-medication)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  New rule will require a stricter customs process for prescription medication mailed from abroad. Read more.
- [State Street Energy Select Sector SPDR ETF (XLE) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLE/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Find the latest State Street Energy Select Sector SPDR ETF (XLE) stock quote, history, news and other vital information to help you with your stock trading...
- [Nasdaq 100 Flirts with Records, Oil Sinks for Fifth Day: Stock Market Today](https://www.tradingview.com/news/benzinga:de108ba70094b:0-nasdaq-100-flirts-with-records-oil-sinks-for-fifth-day-stock-market-today/)  
  <sub>TradingView, 21 hours ago</sub>  
  The Nasdaq 100 carved out a fresh intraday record by midday Tuesday as the artificial intelligence trade powered ahead.Speaking at the United Nations...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 169.40 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 169.75 (-0.2%), 50d 167.08 (+1.4%), 200d 156.06 (+8.5%); 50d above 200d
Momentum: RSI(14) 52.9 | MACD 0.103 vs signal 0.369 (histogram -0.266)
Returns: 1d +0.2% | 5d +1.0% | 1m -3.0% | 3m +11.3%
52-week range: 134.13 - 175.68 (now 84.9% of the way up)
Volatility: ATR(14) 2.30 (1.4% of price) | annualised 20d 13.5%
Volume: 0.43x the 20-day average
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
Three-year record: +10.8% a year | beta to the market 0.52
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.7% above the current prices
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
Shares outstanding: 260.63M | fund size: 44.15B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 113.12 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 109.71 (+3.1%), 50d 104.53 (+8.2%), 200d 86.79 (+30.3%); 50d above 200d
Momentum: RSI(14) 59.8 | MACD 2.029 vs signal 1.823 (histogram 0.207)
Returns: 1d -2.2% | 5d +6.0% | 1m +8.5% | 3m +7.5%
52-week range: 60.03 - 115.64 (now 95.5% of the way up)
Volatility: ATR(14) 2.40 (2.1% of price) | annualised 20d 27.9%
Volume: 0.44x the 20-day average
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
Three-year record: +47.0% a year | beta to the market 1.30
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
Weighted price target: +26.2% above the current prices
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 105.25M | fund size: 11.91B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: The read operation timed out

<details><summary><b>News</b> — score n/a</summary>

- [EPU: Hold But Stay Underweight (NYSEARCA:EPU)](https://seekingalpha.com/article/4948907-epu-hold-but-stay-underweight)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  iShares MSCI Peru and Global Exposure ETF is a top emerging market ETF, but Peru's outlook is uncertain. Click here to read more on EPU here.
- [ETF Boom Draws Nearly 1 Million Retail Investors in Brazil](https://finance.yahoo.com/markets/stocks/articles/etf-boom-draws-nearly-1-122554387.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Retail investors in Brazil are piling into exchange-traded funds at a record pace as a wave of new products broadens the market.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 37.81 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 37.36 (+1.2%), 50d 36.13 (+4.6%), 200d 36.22 (+4.4%); 50d below 200d
Momentum: RSI(14) 58.2 | MACD 0.611 vs signal 0.659 (histogram -0.048)
Returns: 1d -0.7% | 5d +0.1% | 1m +7.8% | 3m +10.7%
52-week range: 28.79 - 41.73 (now 69.7% of the way up)
Volatility: ATR(14) 0.78 (2.1% of price) | annualised 20d 22.4%
Volume: 0.61x the 20-day average
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
Three-year record: +13.3% a year | beta to the market 0.84
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
Weighted price target: +23.4% above the current prices
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 200.55M | fund size: 7.58B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: The read operation timed out

<details><summary><b>News</b> — score n/a</summary>

- [LIC, Meesho, Coforge, Swiggy top Centrum’s high-conviction list for MSCI India November review](https://www.moneycontrol.com/news/business/markets/lic-meesho-coforge-swiggy-top-centrum-s-high-conviction-list-for-msci-india-november-review-14036314.html)  
  <sub>Moneycontrol.com, 7 hours ago</sub>  
  LIC stands out as the clearest corporate-action-driven inclusion, while Meesho, Coforge, Swiggy and Glenmark lead the high-conviction size-based candidates.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 48.12 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 48.94 (-1.7%), 50d 49.21 (-2.2%), 200d 50.10 (-4.0%); 50d below 200d
Momentum: RSI(14) 41.6 | MACD -0.414 vs signal -0.329 (histogram -0.085)
Returns: 1d -0.8% | 5d +1.1% | 1m -3.1% | 3m -1.9%
52-week range: 45.42 - 55.29 (now 27.3% of the way up)
Volatility: ATR(14) 0.45 (0.9% of price) | annualised 20d 14.8%
Volume: 0.52x the 20-day average
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
Three-year record: +3.2% a year | beta to the market 0.56
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
Weighted price target: +30.6% above the current prices
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 139.94M | fund size: 6.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [2027: The Year The CRE Debt Maturity Wall Triggers Peak Pain](https://seekingalpha.com/article/4948753-2027-the-year-the-cre-debt-maturity-wall-triggers-peak-pain)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Commercial real estate faces mounting stress as higher rates drive CMBS delinquency rates to 7.85%, 6x higher than pre-pandemic levels. Click for more.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 71.28 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 73.66 (-3.2%), 50d 75.24 (-5.3%), 200d 70.42 (+1.2%); 50d above 200d
Momentum: RSI(14) 30.7 | MACD -0.834 vs signal -0.609 (histogram -0.225)
Returns: 1d -1.0% | 5d -3.7% | 1m -4.8% | 3m -2.5%
52-week range: 58.14 - 77.93 (now 66.4% of the way up)
Volatility: ATR(14) 1.21 (1.7% of price) | annualised 20d 14.8%
Volume: 0.33x the 20-day average
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
Three-year record: +23.5% a year | beta to the market 1.04
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
Weighted price target: +20.5% above the current prices
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 55.14M | fund size: 3.93B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Winning and Losing Sectors for ETF Investors](https://www.baystreet.ca/amp/articles/etfs.aspx?articleid=124070)  
  <sub>Baystreet.ca, 5 hours ago</sub>  
  At the start of the second half of 2026, the technology sector looked like it would give back some of its gains. Instead, software and semiconductor stocks...
- [Seven consumer discretionary stocks with long-running Strong Buy Quant ratings](https://seekingalpha.com/news/4645903-seven-consumer-discretionary-stocks-with-long-running-strong-buy-quant-ratings)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Screen consumer discretionary stocks with Strong Buy Quant Ratings—GM, LTH, F, AMZN & more—plus ETFs.
- [Staples ETF Widens Gap Over Discretionary in 2026](https://etfdb.com/sector-investing-content-hub/staples-etf-widens-gap/)  
  <sub>ETF Database, 22 hours ago</sub>  
  The State Street Consumer Staples Select Sector SPDR ETF (XLP A) has climbed 6.6% so far in 2026, according to State Street data as of September 21.
- [Sector Update: Consumer Stocks Advance Tuesday Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-advance-tuesday-173619109.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Consumer stocks advanced Tuesday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) rising 1.1% and the State Street Consumer...
- [Leading And Lagging Sectors For September 23, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61944915/leading-and-lagging-sectors-september-23-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLE) State Street Energy Select Sector SPDR ETF 62.26 0.48 0.77 300.1K (NYSE:XLP) State Street...
- [Weekly ETFs: Eight of 11 sectors record outflows; Gold leads inflows](https://www.tradingview.com/news/seekingalpha:c3689e0ef094b:0-weekly-etfs-eight-of-11-sectors-record-outflows-gold-leads-inflows/)  
  <sub>TradingView, 23 hours ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 ETF Trust AMEX:SPY, saw outflows of $22.64B for the week ended September 18, while its price...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 110.85 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 113.82 (-2.6%), 50d 115.17 (-3.7%), 200d 116.77 (-5.1%); 50d below 200d
Momentum: RSI(14) 39.1 | MACD -1.463 vs signal -1.207 (histogram -0.256)
Returns: 1d -1.2% | 5d -0.0% | 1m -6.1% | 3m -2.6%
52-week range: 105.66 - 124.52 (now 27.5% of the way up)
Volatility: ATR(14) 1.63 (1.5% of price) | annualised 20d 15.8%
Volume: 0.44x the 20-day average
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
Three-year record: +12.3% a year | beta to the market 1.16
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
Weighted price target: +23.7% above the current prices
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
Shares outstanding: 204.84M | fund size: 22.71B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- No news or macro surprise in the past 24h
- Technicals: price above 50d and 200d SMA but MACD negative and low volume, no decisive break
- Positioning: crowded long (98th percentile) with slight net long reduction (-0.2% change)
- Cost of holding: heavy negative roll cost of -14.1% per year, bearish for long positions

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 11.37 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 11.38 (-0.1%), 50d 10.69 (+6.4%), 200d 9.91 (+14.7%); 50d above 200d
Momentum: RSI(14) 55.7 | MACD 0.129 vs signal 0.214 (histogram -0.086)
Returns: 1d +2.2% | 5d -0.1% | 1m +1.4% | 3m +23.1%
52-week range: 9.02 - 11.82 (now 83.9% of the way up)
Volatility: ATR(14) 0.22 (1.9% of price) | annualised 20d 25.4%
Volume: 0.74x the 20-day average
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
Cost of holding this fund instead of sugar itself: -14.1% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +23.1%, commodity +40.6%, gap -17.6% | 6 months: fund +8.8%, commodity +18.8%, gap -10.0% | 12 months: fund +9.6%, commodity +23.7%, gap -14.1%
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 5.26M | fund size: 59.83M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, positioning shows a modest net long with a slight weekly decrease and high crowding, heavy roll cost drags long returns while a weaker crop relative to last year is bullish on supply, and technicals lack a decisive break.

**Main reasons it gave:**
- Positioning: net long 22.5% of OI, down 0.5% week, 97% crowding
- Cost of holding: -14.1% annual roll cost (heavy drag on longs)
- Crop condition: 57% good/excellent, down 9 points YoY (bullish supply)
- Macro: yields up modestly, no policy surprise, VIX low
- Technicals: price below 20‑day SMA, MACD histogram negative, volume 0.31× 20‑day avg

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 19.77 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 19.98 (-1.0%), 50d 18.82 (+5.0%), 200d 18.07 (+9.4%); 50d above 200d
Momentum: RSI(14) 54.2 | MACD 0.319 vs signal 0.411 (histogram -0.092)
Returns: 1d -2.5% | 5d -1.3% | 1m +4.0% | 3m +18.1%
52-week range: 16.47 - 20.29 (now 86.4% of the way up)
Volatility: ATR(14) 0.33 (1.7% of price) | annualised 20d 19.9%
Volume: 0.31x the 20-day average
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
Cost of holding this fund instead of corn itself: -14.1% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +18.1%, commodity +30.1%, gap -12.0% | 6 months: fund +6.8%, commodity +14.5%, gap -7.7% | 12 months: fund +11.4%, commodity +25.5%, gap -14.1%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 22.5% of open interest (1,843,824 contracts)
Change on the week: -0.5% of open interest
Crowding: 97% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 8.38M | fund size: 165.58M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral call based on mixed signals: bullish technicals but no decisive break, slight bearish shift in positioning, and heavy roll cost tempering long bias; macro unchanged.

**Main reasons it gave:**
- Price 40.61 above 20‑day SMA 39.77, 50‑day SMA 39.53, 200‑day SMA 37.17
- Net long 22.5% of open interest, down 5.1% week‑over‑week
- Cost of holding -6.3% annual (heavy roll cost)
- Treasury yields modestly higher; 10‑yr 5.05% (+0.06), curve +1.03, VIX 14.49 (-2.7), dollar 100.99 (+1.34)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.30</summary>

```text
Last close 40.61 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 39.77 (+2.1%), 50d 39.53 (+2.7%), 200d 37.17 (+9.3%); 50d above 200d
Momentum: RSI(14) 57.2 | MACD 0.119 vs signal 0.027 (histogram 0.092)
Returns: 1d -0.1% | 5d +5.0% | 1m +1.6% | 3m +8.8%
52-week range: 28.62 - 41.05 (now 96.5% of the way up)
Volatility: ATR(14) 0.71 (1.7% of price) | annualised 20d 28.3%
Volume: 1.01x the 20-day average
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
Cost of holding this fund instead of copper itself: -6.3% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +8.8%, commodity +14.2%, gap -5.4% | 6 months: fund +21.1%, commodity +25.2%, gap -4.0% | 12 months: fund +42.1%, commodity +48.4%, gap -6.3%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 22.5% of open interest (289,463 contracts)
Change on the week: -5.1% of open interest
Crowding: 40% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 18.71M | fund size: 759.69M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, mixed technical signals, slight bearish positioning, and low cost of holding provide no clear directional edge.

**Main reasons it gave:**
- Positioning: net long 12.7% of open interest, down 1.3% week‑over‑week
- Technical: price 58.36 below 20‑day SMA 59.41 and MACD histogram -0.163
- Macro: Treasury yields up 0.06‑0.11% on the week and dollar index +1.34%, a modestly bearish backdrop
- Cost of holding: 0.6% a year, near zero, no directional bias

<details><summary><b>News</b> — score +0.00</summary>

- [Silver Made America’s Critical Minerals List. This ETF Is the Easiest Way In](https://finance.yahoo.com/markets/commodities/articles/silver-made-america-critical-minerals-170320821.html)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  Washington just handed silver a designation that lithium and cobalt already carry, and the fallout for stock investors is more complicated than the...
- [Australian ETF Movers for Wednesday | Global X Silver Miners ETF Was the Top Gainer](https://www.moomoo.com/news/post/1000070986/australian-etf-movers-for-wednesday-global-x-silver-miners-etf)  
  <sub>Moomoo, 7 hours ago</sub>  
  TopGainers/Losers with the total trading value of A$579.48 million. Among them: $Global X Silver Miners ETF(SLVM.AU)$ was the top gainer, climbing 4.29% to...
- [High Beta, Short Supply: The Drivers of Silver's New Rally](https://etfdb.com/gold-silver-investing-content-hub/high-beta-short-supply-drive-silver-rally/)  
  <sub>ETF Database, 21 hours ago</sub>  
  Silver and gold both saw their spot prices increase in August, but insights from Sprott note that silver's price rose across the month even higher than gold...
- [Silver joins US Critical Minerals List, boostin...](https://pluang.com/en/news-feed/silver-masuk-daftar-mineral-kritis-amerika-ini-etf-termudah)  
  <sub>Pluang, 22 hours ago</sub>  
  Silver was added to the US Critical Minerals List, highlighting its importance alongside lithium and cobalt for national security and energy transition.
- [Silver ETFs Rise; Gold, IT Funds Slip on Sept 23](https://hdfcsky.com/news/silver-etfs-extend-gains-as-gold-it-ease-bank-defence-firm-liquid-steady-on-wednesday)  
  <sub>HDFC Sky, 5 hours ago</sub>  
  Silver ETFs gained across the board, while gold and IT funds eased. Bank and defence ETFs stayed firm, with liquid ETFs largely unchanged.
- [Silver (XAG) Forecast: Dollar and Yields Drive Silver Lower Despite Cheaper Oil](https://www.fxempire.com/forecasts/article/silver-xag-forecast-dollar-and-yields-drive-silver-lower-despite-cheaper-oil-1631044)  
  <sub>FXEmpire, 5 hours ago</sub>  
  XAGUSD falls despite cheaper oil as the two-year yield reaches 4.788% and silver ETF outflows deepen the bearish outlook.
- [Daily ETF Flows: ARKK Enters Top 10](https://www.etf.com/sections/daily-etf-flows/daily-etf-flows-arkk-enters-top-10)  
  <sub>ETF.com, 19 hours ago</sub>  
  Here are the daily ETF fund flows for September 21, 2026.
- [Direxion Daily Silver Bull 2X ETF declares quarterly distribution of $0.0706](https://www.tradingview.com/news/seekingalpha:141c333b7094b:0-direxion-daily-silver-bull-2x-etf-declares-quarterly-distribution-of-0-0706/)  
  <sub>TradingView, 19 hours ago</sub>  
  Content provided by Seeking Alpha is intended for information purposes only, and that Seeking Alpha does not offer any personalist investment advice and is...
- [Gold ends little changed; silver's direction torn between rate-hike risks, industrial demand](https://seekingalpha.com/news/4645779-gold-ends-little-changed-silvers-direction-torn-between-rate-hike-risks-industrial-demand)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Gold futures fell slightly while silver edged higher, as the precious metals remained within "a solid support range" with the US dollar firming and oil...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 58.36 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 59.41 (-1.8%), 50d 57.05 (+2.3%), 200d 65.86 (-11.4%); 50d below 200d
Momentum: RSI(14) 48.8 | MACD 0.094 vs signal 0.257 (histogram -0.163)
Returns: 1d -2.1% | 5d +1.4% | 1m -7.0% | 3m +4.7%
52-week range: 39.82 - 105.60 (now 28.2% of the way up)
Volatility: ATR(14) 1.77 (3.0% of price) | annualised 20d 38.0%
Volume: 0.52x the 20-day average
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
Cost of holding this fund instead of silver itself: 0.6% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +4.7%, commodity +12.4%, gap -7.6% | 6 months: fund -6.6%, commodity -5.8%, gap -0.7% | 12 months: fund +49.5%, commodity +48.9%, gap +0.6%
A commodity fund holds futures, not silver, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

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
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 12.7% of open interest (103,745 contracts)
Change on the week: -1.3% of open interest
Crowding: 65% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 572.79M | fund size: 33.43B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- Macro: yields rose modestly, inflation 3.4% in line with expectations
- Technical: price near 52‑week high, above SMAs, but MACD below signal and volume low
- Positioning: net long 21.9% of OI, down 2.2% week‑over‑week
- Fundamentals: cost of holding -2.8% annual drag, crop condition steady at 58% good/excellent

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 27.94 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 27.58 (+1.3%), 50d 26.35 (+6.0%), 200d 24.43 (+14.3%); 50d above 200d
Momentum: RSI(14) 62.0 | MACD 0.507 vs signal 0.550 (histogram -0.042)
Returns: 1d -0.6% | 5d -0.0% | 1m +6.5% | 3m +15.1%
52-week range: 21.46 - 28.14 (now 97.0% of the way up)
Volatility: ATR(14) 0.35 (1.3% of price) | annualised 20d 17.8%
Volume: 0.21x the 20-day average
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
Cost of holding this fund instead of soybeans itself: -2.8% a year -- a steady drag
Measured: 3 months: fund +15.1%, commodity +18.6%, gap -3.5% | 6 months: fund +15.5%, commodity +13.8%, gap +1.7% | 12 months: fund +27.2%, commodity +30.0%, gap -2.8%
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 1.68M | fund size: 46.81M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- CFTC positioning shows crowded long (98th percentile) with slight net long reduction (-0.3% OI)
- EIA inventories report a small crude draw (-0.6M barrels) but builds in gasoline (+0.8M) and diesel (+1.6M)
- EIA price outlook forecasts WTI falling to $79 in six months, indicating bearish fundamentals
- Iran blockade and supertanker shortage raise oil transport costs, but impact not yet reflected in price
- No major policy or rate surprise; macro data (inflation, unemployment) in line with expectations

<details><summary><b>News</b> — score +0.00</summary>

- [Supertanker shortage sends costs soaring past $1.2M/day amid Iran war turmoil (USO:NYSEARCA)](https://seekingalpha.com/news/4646049-supertanker-shortage-sends-costs-soaring-past-12mday-amid-iran-war-turmoil)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  The cost of hiring a Very Large Crude Carrier has surpassed $1.2M/day for the first time on routes between the Middle East and Asia, which have more than...
- [Oil Prices Surge Nearly 10% — US Forces To Resume Maritime Blockade Against Iran On Tuesday](https://stocktwits.com/news-articles/markets/equity/oil-prices-surge-10-percent-us-forces-to-resume-maritime-blockade-against-iran-on-tuesday/cZmz6rZR7Yo)  
  <sub>Stocktwits, 8 hours ago</sub>  
  The U.S. Central Command said U.S. forces will enforce the blockade on vessels entering or leaving Iranian ports starting July 14 at 4 p.m. ET.
- [Commodity ETF Delivers Double Nvidia’s YTD Returns; Muse Ignites CPU Fever](https://www.benzinga.com/Opinion/26/09/61928535/commodity-etf-delivers-double-nvidias-ytd-returns-muse-ignites-cpu-fever)  
  <sub>Benzinga, 23 hours ago</sub>  
  CPU Fever Please click here for an enlarged chart comparing NVIDIA Corp (NASDAQ:NVDA) and Invesco Optimum Yield Diversified Commodity Strategy No K-1 ETF...
- [Diesel’s record refining premium is feeding core inflation, Apollo warns](https://seekingalpha.com/news/4645983-diesels-record-refining-premium-is-feeding-core-inflation-apollo-warns)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Diesel crack spread tops $100—an inflation shock hitting core CPI via freight and logistics. Learn more here.
- [Oil Slid, Sending Energy ETFs Lower Before The Open](https://finimize.com/content/oil-slid-sending-energy-etfs-lower-before-the-open)  
  <sub>Finimize, 24 hours ago</sub>  
  WTI fell to $93.51 a barrel and Brent to $98.50, while TotalEnergies signed an MOU with Venezuela's PDVSA and Solaris lined up $1 billion of notes due 2032.
- [Dow Soars 800 Points Driven By Healthcare Stocks — But Chip Stocks Drag S&P 500, Nasdaq](https://stocktwits.com/news-articles/markets/equity/dow-soars-as-investors-flee-chip-stocks-pile-into-healthcare-sector/cZ0ZLU0Reys)  
  <sub>Stocktwits, 23 hours ago</sub>  
  U.S. equities were split in Thursday morning's trade as investors rotated out of chip stocks and piled into healthcare, financials, and communication...
- [How would a ban on U.S. diesel exports impact the economy?](https://seekingalpha.com/news/4645825-deep-dive-ban-us-diesel-export-ban)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Trump-backed proposals to ban U.S. diesel exports may cut prices short term, but could raise fuel and grocery costs by hurting refinery output and...
- [Trump says he supports U.S. diesel export ban; Bessent says studying feasibility (USO:NYSEARCA)](https://seekingalpha.com/news/4645794-trump-says-he-supports-us-diesel-export-ban-bessent-says-studying-feasibility)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  President Trump said he is encouraging his advisors to support a ban on US diesel exports, as the nationwide average of diesel prices continued to rise,...
- [U.S. crude stockpiles rose 1.8M barrels last week, API says (USO:NYSEARCA)](https://seekingalpha.com/news/4645787-u-s-crude-stockpiles-rose-1_8m-barrels-last-week-api-says)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  The American Petroleum Institute reportedly shows a build of 1.78M barrels of oil in US commercial stockpiles for the week ending September 18.
- [Evening digest: Anthropic launches Claude Opus 5.5, oil falls below $100](https://invezz.com/news/2026/09/22/evening-digest-anthropic-launches-claude-opus-5-5-oil-falls-below-100/)  
  <sub>Invezz, 19 hours ago</sub>  
  Anthropic launched Claude Opus 5.5 on Tuesday as the AI industry continues to debate the pace and safety of increasingly capable models.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 149.04 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 145.17 (+2.7%), 50d 133.94 (+11.3%), 200d 112.07 (+33.0%); 50d above 200d
Momentum: RSI(14) 56.7 | MACD 6.351 vs signal 6.874 (histogram -0.523)
Returns: 1d +0.6% | 5d -7.9% | 1m +10.7% | 3m +34.0%
52-week range: 66.17 - 161.86 (now 86.6% of the way up)
Volatility: ATR(14) 4.91 (3.3% of price) | annualised 20d 44.5%
Volume: 0.54x the 20-day average
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
US inventories, week ending 2026-09-11 (published the following Wednesday)
  Crude oil: 423.4 million barrels, -0.6 on the week (a draw), 38% percentile over 52 weeks
  Petrol: 207.7 million barrels, +0.8 on the week (a build), 13% percentile over 52 weeks -- low for the time of year
  Diesel: 107.9 million barrels, +1.6 on the week (a build), 33% percentile over 52 weeks
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 5.4% of open interest (1,955,764 contracts)
Change on the week: -0.3% of open interest
Crowding: 98% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 12.28M | fund size: 1.83B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, mixed technicals, heavy roll cost and slightly better crop condition weigh bearish, while positioning shift to net long is modestly bullish; overall neutral stance.

**Main reasons it gave:**
- Positioning: net short 0.8% of OI, weekly change -1.8% (crowding 90th percentile)
- Cost of holding: -16.7% annual, heavy roll cost dragging long performance
- Crop condition: 51% good/excellent, +2 points YoY (bearish supply)
- Technicals: price above 200‑day SMA (+11.3%) but below 20‑day SMA (-4.2%); RSI 45.3 (neutral)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 25.60 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 26.72 (-4.2%), 50d 25.50 (+0.4%), 200d 23.00 (+11.3%); 50d above 200d
Momentum: RSI(14) 45.3 | MACD 0.160 vs signal 0.370 (histogram -0.209)
Returns: 1d -2.7% | 5d -2.7% | 1m +0.7% | 3m +14.2%
52-week range: 19.88 - 28.00 (now 70.4% of the way up)
Volatility: ATR(14) 0.62 (2.4% of price) | annualised 20d 32.8%
Volume: 0.26x the 20-day average
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
Cost of holding this fund instead of wheat itself: -16.7% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +14.2%, commodity +20.6%, gap -6.4% | 6 months: fund +12.9%, commodity +19.7%, gap -6.8% | 12 months: fund +21.6%, commodity +38.3%, gap -16.7%
A commodity fund holds futures, not wheat, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.30</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 0.8% of open interest (485,138 contracts)
Change on the week: -1.8% of open interest
Crowding: 90% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 14.00M | fund size: 358.50M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Gold ETFs Shrink from Record But Demand 'Defies Rising Real Rates'](https://www.bullionvault.com/gold-news/gold-price-news/gold-etfs-gld-real-rates-092320261)  
  <sub>BullionVault, 46 minutes ago</sub>  
  Gold ETF and bullion prices fell Wednesday as bond yields rose, but analysts pointed to an underlying break with the 'normal' pattern vs real rates >>
- [SPDR Gold Trust (GLD) Stock Price Today: $394.38](https://pluang.com/en/asset/usstock/GLD/10890)  
  <sub>Pluang, 6 hours ago</sub>  
  Buy and sell SPDR Gold Trust stock securely on Pluang with real-time prices, live charts, and detailed market trend information. Track SPDR Gold Trust...
- [AAAU vs. GDX: Is It Better to Hold Physical Gold or Invest in Gold Miners?](https://finance.yahoo.com/markets/commodities/articles/aaau-vs-gdx-better-hold-110201144.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  The Goldman Sachs Physical Gold ETF (NYSEMKT:AAAU) offers low-cost exposure to physical bullion, whereas the VanEck Gold Miners ETF (NYSEMKT:GDX) invests in...
- [Silver Made America’s Critical Minerals List. This ETF Is the Easiest Way In](https://247wallst.com/investing/etf/2026/09/22/silver-made-americas-critical-minerals-list-this-etf-is-the-easiest-way-in/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  Washington just handed silver a designation that lithium and cobalt already carry, and the fallout for stock investors is more complicated than the...
- [Howard Marks: $40T Debt Isn’t a Reason to Sell Stocks. ETFs Could Help - SPDR Gold Shares (ARCA:GLD)](https://www.benzinga.com/etfs/sector-etfs/26/09/61931952/billionaire-howard-marks-says-americas-40t-debt-problem-isnt-a-reason-to-sell-stocks-heres-where-etfs-come-in)  
  <sub>Benzinga, 21 hours ago</sub>  
  Howard Marks says selling U.S. stocks won't solve U.S. fiscal problems. These ETFs offer gold, international and real estate exposure.
- [GLD 260922 394.00C (GLD260922C394000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/GLD260922C394000-US)  
  <sub>Moomoo, 22 hours ago</sub>  
  Track real-time GLD 260922 394.00C (GLD260922C394000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [Gold ends little changed; silver's direction torn between rate-hike risks, industrial demand](https://seekingalpha.com/news/4645779-gold-ends-little-changed-silvers-direction-torn-between-rate-hike-risks-industrial-demand)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Gold futures fell slightly while silver edged higher, as the precious metals remained within "a solid support range" with the US dollar firming and oil...
- [Weekly ETFs: Eight of 11 sectors record outflows; Gold leads inflows](https://www.tradingview.com/news/seekingalpha:c3689e0ef094b:0-weekly-etfs-eight-of-11-sectors-record-outflows-gold-leads-inflows/)  
  <sub>TradingView, 24 hours ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 ETF Trust AMEX:SPY, saw outflows of $22.64B for the week ended September 18, while its price...
- [Bitcoin: ETF Inflows, Fed Hikes, Failed Regulation, And A Rally That Makes No Sense](https://seekingalpha.com/article/4948747-bitcoin-etf-inflows-fed-hikes-failed-regulation-and-a-rally-that-makes-no-sense)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Bitcoin rally analysis: spot ETF inflows and IBIT call hedging may be driving gains despite hawkish Fed and 5% yields.
- [Silver joins US Critical Minerals List, boostin...](https://pluang.com/en/news-feed/silver-masuk-daftar-mineral-kritis-amerika-ini-etf-termudah)  
  <sub>Pluang, 22 hours ago</sub>  
  Silver was added to the US Critical Minerals List, highlighting its importance alongside lithium and cobalt for national security and energy transition.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 392.91 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 403.68 (-2.7%), 50d 393.92 (-0.3%), 200d 416.31 (-5.6%); 50d below 200d
Momentum: RSI(14) 44.6 | MACD -1.231 vs signal 0.353 (histogram -1.584)
Returns: 1d -1.4% | 5d -0.3% | 1m -7.2% | 3m +4.1%
52-week range: 343.32 - 495.90 (now 32.5% of the way up)
Volatility: ATR(14) 7.44 (1.9% of price) | annualised 20d 23.1%
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
Cost of holding this fund instead of gold itself: 1.2% a year -- the roll has been paying this fund
Measured: 3 months: fund +4.1%, commodity +8.0%, gap -3.9% | 6 months: fund -2.8%, commodity -1.7%, gap -1.1% | 12 months: fund +15.8%, commodity +14.7%, gap +1.2%
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
Shares outstanding: 260.30M | fund size: 102.27B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: The read operation timed out

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.02% (+0.06 on the week) | 5-year 4.93% (+0.11 on the week) | 10-year 5.05% (+0.06 on the week) | 30-year 5.36% (+0.00 on the week)
Yield curve, 10-year minus 3-month: +1.03 points -- upward sloping (normal)
US dollar index: 100.99 (+1.34 on the week)
Volatility (VIX): 14.49 (-2.7 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 10.84 (bar of 2026-09-23), from 501 daily bars
Trend: vs 20d SMA 10.41 (+4.1%), 50d 10.24 (+5.9%), 200d 11.50 (-5.7%); 50d below 200d
Momentum: RSI(14) 60.9 | MACD 0.053 vs signal 0.026 (histogram 0.027)
Returns: 1d +5.7% | 5d +2.8% | 1m +8.5% | 3m -5.7%
52-week range: 9.63 - 16.90 (now 16.6% of the way up)
Volatility: ATR(14) 0.29 (2.7% of price) | annualised 20d 31.3%
Volume: 1.44x the 20-day average
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
US inventories, week ending 2026-09-11 (published the following Wednesday)
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
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 55.41M | fund size: 600.63M
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

