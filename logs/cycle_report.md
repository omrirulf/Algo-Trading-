# Daily report

**21 Sep 2026, 18:34 Israel time (15:34 UTC)** · 80 names checked · 2 traded · 0 with a problem

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 2 | 14 | 0 |
| Whole-market funds | 14 | 0 | 14 | 0 |
| Sector and country funds | 41 | 3 | 38 | 0 |
| Commodities | 9 | 0 | 9 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| Alphabet (Google) (GOOGL) · Company | **Stop raised.** At +0.50R, following the price. Stop-loss raised 330.44 → 338.00. |
| Eli Lilly (LLY) · Company | **Stop raised.** At +0.28R, following the price. Stop-loss raised 1085.29 → 1105.32. |
| Nvidia (NVDA) · Company | **Stop raised.** At +0.79R, following the price. Stop-loss raised 206.79 → 212.84. |
| US dollar (UUP) · Index fund | **Stop raised.** At +0.23R, following the price. Stop-loss raised 28.21 → 28.23. |
| US government bonds, 7-10 years (IEF) · Index fund | **Problem.** Could not be managed: BrokerError: close_position failed for IEF: {"available":"0","code":40310000,"existing_qty":"131","held_for_orders":"131","message":"insufficient qty available for order (requested: 14, available: 0)","symbol":"IEF"} |
| Teva Pharmaceutical (TEVA) · Company | **Problem.** Could not be managed: BrokerError: replace_order failed for aae42775-8f36-4d39-8228-5fe42162cef5: {"code":42210000,"message":"qty cannot be changed for advanced orders"} |
| US inflation-linked bonds (TIP) · Index fund | **Problem.** Could not be managed: BrokerError: close_position failed for TIP: {"available":"0","code":40310000,"existing_qty":"10","held_for_orders":"10","message":"insufficient qty available for order (requested: 1, available: 0)","symbol":"TIP"} |
| US government bonds, 20+ years (TLT) · Index fund | **Problem.** Could not be managed: BrokerError: close_position failed for TLT: {"available":"0","code":40310000,"existing_qty":"147","held_for_orders":"147","message":"insufficient qty available for order (requested: 16, available: 0)","symbol":"TLT"} |
| Developing country bonds (EMB) · Index fund | **Holding.** -0.40R, holding 128 shares. Stop-loss 94.05. |
| Gold (GLD) · Commodity | **Holding.** -0.60R, holding 10 shares. Stop-loss 404.87. |
| US government bonds, 7-10 years (IEF) · Index fund | **Holding.** +0.05R, holding 131 shares. Stop-loss 91.61. |
| S&P 500, equal weight (RSP) · Index fund | **Holding.** -0.07R, holding 14 shares. Stop-loss 215.78. |
| US inflation-linked bonds (TIP) · Index fund | **Holding.** +0.63R, holding 10 shares. Stop-loss 106.08. |
| US government bonds, 20+ years (TLT) · Index fund | **Holding.** -0.41R, holding 147 shares. Stop-loss 82.41. |
| Biotech (XBI) · Sector or country | **Holding.** -0.65R, holding 45 shares. Stop-loss 161.15. |
| US shopping and leisure (XLY) · Sector or country | **Holding.** -0.43R, holding 63 shares. Stop-loss 113.36. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Microsoft (MSFT) · Company — BULLISH, confidence 0.55

**Result:** ACCEPTED · 10 shares · submitted buy 10 MSFT @ ~491.78, stop 471.19

**In the model's own words:**

> Fundamentals are strong and improving: 17.7% revenue and 31.7% earnings growth, 45% operating margins, forward P/E ~21, and four straight beats including +10% last quarter. Analyst consensus is strong buy with ~16% upside to target and a fresh Redburn target raise to $440 (still below spot, so modest). Technicals are the offset: price is 5.7% above the 50d and 14% above the 200d but has pulled back below the 20d with a negative MACD histogram and very thin volume, suggesting near-term consolidation after a +34% three-month run. News flow is mostly recycled valuation/dividend commentary rather than a fresh catalyst. Insider transactions are routine scheduled sales by Hood/Nadella with no open-market buys, which I read as close to neutral. Net: constructive but not a high-conviction few-day setup.

**Main reasons it gave:**
- Four consecutive earnings beats, last quarter +10% vs consensus
- Revenue +17.7%, earnings +31.7% YoY with 45.1% operating margin, forward P/E 20.9
- Strong buy consensus (1.36, 52 analysts), mean target 572.92 = +16.1% upside
- MACD below signal and price -0.9% vs 20d SMA after +34% 3-month run; volume 0.28x average
- Insider net share count positive but 0 distinct open-market buyers; only scheduled sales by CFO/CEO

<details><summary><b>News</b> — score +0.25</summary>

- [Microsoft (NASDAQ:MSFT) Dividend Quality Backs Income Investors](https://www.chartmill.com/news/MSFT/Chartmill-55097-Microsoft-NASDAQMSFT-Dividend-Quality-Backs-Income-Investors)  
  <sub>ChartMill, 3 hours ago</sub>  
  MSFT dividend: Microsoft's low yield is backed by strong profitability, health, and growth, making it a quality income pick for long-term investors.
- [MSFT Stock Jumps 3% After-Hours — Lower-Than-Expected Q4 Capex, Strong Azure Sales Boost Sentiment](https://stocktwits.com/news-articles/markets/equity/msft-stock-jumps-3-after-hours-lower-than-expected-q4-capex-strong-azure-sales-boost-sentiment/cZNT9ukRJTF)  
  <sub>Stocktwits, 15 hours ago</sub>  
  The social media giant generated $60.80 billion in revenue for the quarter ended June 30, up slightly from analyst estimates of around $60.28 billion. However,...
- [MSFT Looks 15.7% Undervalued on GF Value™](https://www.gurufocus.com/news/9089987/msft-looks-157-undervalued-on-gf-value)  
  <sub>GuruFocus, 1 hour ago</sub>  
  On September 21, 2026, Microsoft Corp (NASDAQ: MSFT) CEO Satya Nadella joined a state dinner hosted by President Trump, alongside other leading tech...
- [Microsoft To Rally Over 23%? Here Are 10 Top Analyst Forecasts For Monday](https://www.benzinga.com/news/26/09/61893682/microsoft-to-rally-over-23-here-are-10-top-analyst-forecasts-for-monday)  
  <sub>Benzinga, 2 hours ago</sub>  
  Analysts raised targets for INSP, SECZ, CLF and WAT, while cutting targets for CRDO, CL and TTMI; ratings remained unchanged.
- [This Artificial Intelligence (AI) Stock Has Raised Its Dividend by Over 150% in 10 Years](https://www.theglobeandmail.com/investing/markets/stocks/MSFT-Q/pressreleases/4708489/this-artificial-intelligence-ai-stock-has-raised-its-dividend-by-over-150-in-10-years/)  
  <sub>The Globe and Mail, 3 hours ago</sub>  
  Detailed price information for Microsoft Corp (MSFT-Q) from The Globe and Mail including charting and trades.
- [The Week That Proved AI Is Real: MSFT +16%, AMZN +10%, META -10%, AAPL -4% - Winners, Losers and Key Takeaways](https://www.tradingkey.com/analysis/stocks/us-stocks/262067343-week-review-july-28-31-2026-microsoft-amazon-apple-meta-earnings-ai-tradingkey)  
  <sub>TradingKey, 14 hours ago</sub>  
  Microsoft surged 16% adding $450B in a single day. Amazon jumped 10%. Meta crashed 10%. Apple fell 4%. The KOSPI gained 17.9% — the largest one-day gain in...
- [Microsoft's price target raised to $440 amid st...](https://pluang.com/en/news-feed/analisis-saham-msft-naikkan-target-harga-dan-laporan-keuangan-kuat)  
  <sub>Pluang, 1 hour ago</sub>  
  Rothschild & Co Redburn raised Microsoft's price target from $400 to $440 following strong fiscal 2026 results, with revenue up 18% to $331.8 billion and...
- [Microsoft AI chief urges guardrails as White House resists broad regulation (MSFT:NASDAQ)](https://seekingalpha.com/news/4644588-microsoft-ai-chief-urges-guardrails-as-white-house-resists-broad-regulation)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Microsoft (MSFT) AI chief Mustafa Suleyman said competition with China should not prevent the United States from establishing safeguards for artificial...
- [MSFT Looks 15.5% Undervalued on GF Value™](https://www.gurufocus.com/news/9090065/msft-looks-155-undervalued-on-gf-value)  
  <sub>GuruFocus, 25 minutes ago</sub>  
  On September 21, 2026, reports surfaced that Microsoft Corp (NASDAQ: MSFT) is exploring a strategic partnership with OpenAI and Anthropic to collaboratively...
- [SBUX Stock Set For Best Day In Two Months — Starbucks Steps Up AI Push To Cut Reliance On MSFT, IBM](https://stocktwits.com/news-articles/markets/equity/sbux-stock-set-for-best-day-in-two-months-steps-up-ai-push/cZmY55FR7nN)  
  <sub>Stocktwits, 8 hours ago</sub>  
  Starbucks (SBUX) shares gained about 3% on Thursday as the coffee chain is turning to AI to build its own business applications, aiming to reduce its reliance...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.05</summary>

```text
Last close 493.35 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 498.02 (-0.9%), 50d 466.85 (+5.7%), 200d 431.62 (+14.3%); 50d above 200d
Momentum: RSI(14) 52.9 | MACD 6.122 vs signal 9.236 (histogram -3.114)
Returns: 1d -0.1% | 5d -2.4% | 1m +2.5% | 3m +34.3%
52-week range: 352.83 - 542.07 (now 74.3% of the way up)
Volatility: ATR(14) 10.28 (2.1% of price) | annualised 20d 22.0%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.70</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.66T
Valuation: trailing P/E 27.45 | forward P/E 20.91 | P/B 8.28 | PEG 1.60
Profitability: profit margin 40.3% | operating margin 45.1% | ROE 34.0%
Growth (YoY): revenue +17.7% | earnings +31.7%
Balance sheet: debt/equity 29.1% | free cash flow 16.55B
Risk: beta 1.11 | short interest 1.0% of float
Next earnings: 2026-10-28
```

</details>

<details><summary><b>What this fund holds</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.70</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 10% | 2026-03-31 beat by 3% | 2025-12-31 beat by 3% | 2025-09-30 beat by 10%
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
Consensus: strong_buy (mean 1.36 on a 1=strong buy to 5=strong sell scale, 52 analysts)
Ratings: 14 strong buy, 38 buy, 3 hold, 0 sell, 0 strong sell
Price target: mean 572.92 (+16.1% vs last close), range 400.00 - 870.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

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

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

_Not available today._

</details>

### Novo Nordisk (NVO) · Company — BEARISH, confidence 0.55

**Result:** ACCEPTED · 123 shares · submitted sell 123 NVO @ ~39.77, stop 42.61

**In the model's own words:**

> Capital Markets Day guidance disappointed and the stock broke down 8% on 2.3x volume to near 52-week lows, with price well below all major moving averages and MACD deteriorating. Sentiment is negative and the analyst prior has been ratcheting lower (Morgan Stanley to Underweight on 9/11). Valuation is genuinely cheap (9.9x trailing, 35% margins, huge FCF) and RSI ~31 with a wide price-target gap argues against chasing, so conviction is moderate; post-event drift after a disappointing strategy day plus competitive fears from Lilly favours continued weakness near term.

**Main reasons it gave:**
- Capital Markets Day 2030 targets underwhelmed; stock -8.2% on 2.33x average volume
- Price 15% below 50d and 14% below 200d SMA, near 52-week low of 35.29
- Morgan Stanley downgrade to Underweight on 2026-09-11; consensus hold (2.71)
- Earnings -20.6% YoY, 2 misses in last 4 quarters despite 9.9x trailing P/E
- RSI 30.9 and mean target +17.7% above price limit downside conviction

<details><summary><b>News</b> — score -0.60</summary>

- [Novo shares slide as drugmaker lays out post-Wegovy growth strategy](https://www.cnbc.com/2026/09/21/novo-nordisk-stock-sales-target-obesity-drugs.html)  
  <sub>CNBC, 7 hours ago</sub>  
  Novo stock fell after the company laid out plans to revive growth in the anti-obesity market. CEO Mike Doustdar laid out plans to diversify the company at...
- [Novo Nordisk stock falls after 2030 strategy disappoints investors](https://finance.yahoo.com/markets/stocks/articles/novo-nordisk-stock-falls-2030-111924503.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  The Danish drugmaker pledged to launch 5 multi-blockbuster drugs by 2030 and grow revenue in line with peers, but investors wanted more.
- [A healthcare company holds 48 million of its own shares. Novo Nordisk expects to buy back more.](https://www.stocktitan.net/news/NVO/novo-nordisk-a-s-share-repurchase-dagaubj8r4f6.html)  
  <sub>Stock Titan, 3 hours ago</sub>  
  Novo Nordisk (NVO) reports continued execution of its 2026 share repurchase programme, detailing B share buybacks completed through 18 September 2026.
- [Novo Nordisk Slides as Strategy Targets Underwhelm Investors](https://www.quiverquant.com/news/Novo+Nordisk+Slides+as+Strategy+Targets+Underwhelm+Investors)  
  <sub>Quiver Quantitative, 20 minutes ago</sub>  
  Novo Nordisk A/S (NVO) is down 8.1% today. Here is some analysis on what might have caused this pric.
- [Novo Shares Slip as Growth Plan Disappoints Investors](https://www.schaeffersresearch.com/content/news/2026/09/21/novo-shares-slip-as-growth-plan-disappoints-investors)  
  <sub>Schaeffer's Investment Research, 23 minutes ago</sub>  
  Novo Nordisk (NVO) shares are lower as investors worry about the drugmaker pipeline.
- [Novo Nordisk Falls 7% as Post-Wegovy Growth Plan Fails to Ease Competition Fears; Eli Lilly Slips, Viking Therapeutics Edges Higher](https://247wallst.com/investing/2026/09/21/novo-nordisk-falls-7-as-post-wegovy-growth-plan-fails-to-ease-competition-fears-eli-lilly-slips-viking-therapeutics-edges-higher/)  
  <sub>24/7 Wall St., 1 hour ago</sub>  
  Novo Nordisk took the stage at its own capital markets day and said something that sent its stock tumbling 7%, yet its closest rivals barely flinched.
- [Novo Nordisk (NVO) Faces Stock Drop Amid New Growth Targets Anno](https://www.gurufocus.com/news/9089443/novo-nordisk-nvo-faces-stock-drop-amid-new-growth-targets-announcement)  
  <sub>GuruFocus, 5 hours ago</sub>  
  On September 21, 2026, Novo Nordisk AS (NVO) faced a notable pre-market stock decline of up to 7% following the announcement of its ambitious growth targets...
- [Novo Nordisk says CagriSema bests Eli Lilly's Zepbound (NVO:NYSE)](https://seekingalpha.com/news/4644774-novo-nordisk-says-cagrisema-bests-eli-lilly-zepbound)  
  <sub>Seeking Alpha, 39 minutes ago</sub>  
  Novo Nordisk (NVO) said that results from a phase 3 trial found that its experimental, once-weekly obesity treatment CagriSema (cagrilintide and...
- [Novo Nordisk Targets Over Five New Blockbusters By 2030, But NVO Stock Slides On Growth Concerns](https://finance.yahoo.com/healthcare/articles/novo-nordisk-targets-over-five-113108107.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  Novo Nordisk's long-term growth targets failed to ease investor concerns over Eli Lilly's obesity-drug lead, CagriSema's comparative performance and...
- [Novo Nordisk A/S Stock (NVO) Moved Down by 7.86% on Sep 21: A Full Analysis](https://www.tradingkey.com/news/market-movers/262178564-market-movers-nvo-20260921)  
  <sub>TradingKey, 54 minutes ago</sub>  
  Novo Nordisk faced downward pressure after its Capital Markets Day strategic update.Eli Lilly competition and patent expirations raised concerns over market...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.70</summary>

```text
Last close 39.71 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 44.83 (-11.4%), 50d 46.71 (-15.0%), 200d 46.11 (-13.9%); 50d above 200d
Momentum: RSI(14) 30.9 | MACD -1.375 vs signal -0.981 (histogram -0.394)
Returns: 1d -8.2% | 5d -8.6% | 1m -13.9% | 3m -13.5%
52-week range: 35.29 - 63.98 (now 15.4% of the way up)
Volatility: ATR(14) 1.42 (3.6% of price) | annualised 20d 43.5%
Volume: 2.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 175.41B
Valuation: trailing P/E 9.85 | forward P/E 11.91 | P/B 5.14 | PEG 3.10
Profitability: profit margin 35.3% | operating margin 42.5% | ROE 59.8%
Growth (YoY): revenue +2.1% | earnings -20.6%
Balance sheet: debt/equity 63.3% | free cash flow 37.67B
Risk: beta 0.34 | short interest 1.0% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.10</summary>

```text
Earnings record, last 4 quarters: 1 beat, 1 in line, 2 missed
  2026-06-30 missed by 6% | 2026-03-31 beat by 23% | 2025-12-31 in line | 2025-09-30 missed by 7%
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

<details><summary><b>What analysts and big funds say</b> — score -0.40</summary>

```text
Consensus: hold (mean 2.71 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 0 strong buy, 3 buy, 10 hold, 1 sell, 0 strong sell
Price target: mean 46.74 (+17.7% vs last close), range 39.54 - 63.32
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

<details><summary><b>What analysts say about what this fund holds</b> — score -0.40</summary>

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

### ASML (ASML) · Company — NEUTRAL, confidence 0.40

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> News is mostly routine buyback disclosures and comparison listicles; the one ticker-specific negative (CXMT mass-producing DRAM without EUV) is modest. Technicals are neutral-to-soft: RSI 50, MACD below signal, below 50d SMA, -12% over 3 months but +7.5% over 5 days on thin volume (0.42x). Fundamentals are strong (21% revenue growth, 54% ROE, low leverage) but richly valued, and earnings on Oct 14 is the real catalyst. Strong-buy consensus with +26% target gap is already priced and rating changes are stale reiterations. No insider transactions. Mild upward tilt insufficient for a directional call.

**Main reasons it gave:**
- Buyback disclosure (€124M/day) is routine MAR reporting, not a new catalyst
- CXMT mass-producing G5 DRAM without EUV tools — mild structural negative
- MACD below signal and price -1.5% vs 50d SMA, RSI 50, volume 0.42x average
- Consensus strong_buy with mean target +26.1%, but rating changes are July reiterations
- Revenue +21.3%, earnings +28.5% YoY, D/E 9.1%; earnings 2026-10-14 likely dominates

<details><summary><b>News</b> — score +0.05</summary>

- [A company that helps make computer chips spent €124M buying back shares in one day](https://www.stocktitan.net/news/ASML/asml-reports-transactions-under-its-current-share-buyback-jfoqn09hbqc3.html)  
  <sub>Stock Titan, 3 hours ago</sub>  
  Another 65000 shares cost €90.3M on Sept. 15, one of five transactions ASML disclosed under the Market Abuse Regulation.
- [Better Artificial Intelligence Stock: Arm Holdings vs. ASML](https://finance.yahoo.com/markets/stocks/articles/better-artificial-intelligence-stock-arm-015219848.html)  
  <sub>Yahoo Finance, 13 hours ago</sub>  
  Arm trades at a 125x forward P/E versus ASML's 27.9x, yet both command premium valuations for their monopolistic positions in mobile and chip manufacturing,...
- [ASML Holding N.V. - New York Registry Shares Price Today | xASML Live Price, Chart & Market Cap](https://www.okx.com/en-eu/price/asml-holding-n-v----new-york-registry-shares-xasml)  
  <sub>OKX, 5 hours ago</sub>  
  ASML Holding N.V. - New York Registry Shares price today. ASML Holding N.V. - New York Registry Shares price today is €1,493.15, marking a -- over the past 24...
- [ASML (NasdaqGS:ASML) Stock May Trade At A Premium Despite High NA EUV News](https://simplywall.st/stocks/us/semiconductors/nasdaq-asml/asml-holding/news/asml-nasdaqgsasml-stock-may-trade-at-a-premium-despite-high)  
  <sub>Simply Wall Street, 19 hours ago</sub>  
  ASML Holding has delivered a powerful share price run in recent years, and that kind of move naturally puts the focus on whether the current valuation is...
- [European Semiconductor Stocks Surge Amid AI Investment Interest](https://www.gurufocus.com/news/9089519/european-semiconductor-stocks-surge-amid-ai-investment-interest)  
  <sub>GuruFocus, 4 hours ago</sub>  
  On September 21, 2026, European semiconductor stocks opened higher, buoyed by ongoing investor enthusiasm for artificial intelligence-related stocks.
- [What company Is ASML? Between ASML and AMD, Which Is a Better Investment?](https://www.tradingkey.com/analysis/stocks/us-stocks/261749862-asml-amd-investment-tradingkey)  
  <sub>TradingKey, 14 hours ago</sub>  
  TradingKey - ASML Holding N.V. (NASDAQ: ASML) is not a chip designer; instead, it's best understood as a supplier of equipment for producing semiconductors...
- [ASML reports transactions under its current share buyback program](https://www.marketscreener.com/news/asml-reports-transactions-under-its-current-share-buyback-program-ce785adbdd80f221)  
  <sub>www.marketscreener.com, 3 hours ago</sub>  
  ASML reports transactions under its current share buyback program VELDHOVEN, the Netherlands – ASML Holding N.V. reports the following transactions,...
- [ASML stock heads into the open after a 3.08 percent rise](https://www.ad-hoc-news.de/boerse/news/corporate-news/asml-stock-heads-into-the-open-after-a-3-08-percent-rise/70142390)  
  <sub>AD HOC NEWS, 9 hours ago</sub>  
  At the close on September 19, 2026, ASML stock finished at USD 1679.92 on Nasdaq, up 3.08 percent. The move came as investors focused on stronger guidance,...
- [China's CXMT Starts Mass-Producing Advanced DRAM Chips Without ASML's Tools](https://startupfortune.com/chinas-cxmt-starts-mass-producing-advanced-dram-chips-without-asmls-tools/)  
  <sub>Startup Fortune, 10 hours ago</sub>  
  CXMT's G5 DRAM chips enter mass production without ASML's banned EUV lithography tools, pushing China's chipmaker to roughly 10% of global DRAM share.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.05</summary>

```text
Last close 1,693.44 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 1,685.88 (+0.4%), 50d 1,720.07 (-1.5%), 200d 1,512.39 (+12.0%); 50d above 200d
Momentum: RSI(14) 50.0 | MACD -24.459 vs signal -23.745 (histogram -0.714)
Returns: 1d +0.8% | 5d +7.5% | 1m -3.2% | 3m -12.2%
52-week range: 932.15 - 1,989.44 (now 72.0% of the way up)
Volatility: ATR(14) 53.44 (3.2% of price) | annualised 20d 39.7%
Volume: 0.42x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 650.45B
Valuation: trailing P/E 58.27 | forward P/E 28.52 | P/B 1,442.82 | PEG 1.52
Profitability: profit margin 30.1% | operating margin 37.1% | ROE 53.9%
Growth (YoY): revenue +21.3% | earnings +28.5%
Balance sheet: debt/equity 9.1% | free cash flow 8.44B
Risk: beta 1.36 | short interest 0.4% of float
Next earnings: 2026-10-14
```

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.35</summary>

```text
Earnings record, last 4 quarters: 2 beats, 1 in line, 1 missed
  2026-06-30 beat by 9% | 2026-03-31 beat by 7% | 2025-12-31 missed by 5% | 2025-09-30 in line
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: strong_buy (mean 1.40 on a 1=strong buy to 5=strong sell scale, 16 analysts)
Ratings: 7 strong buy, 31 buy, 3 hold, 1 sell, 0 strong sell
Price target: mean 2,134.93 (+26.1% vs last close), range 887.81 - 2,842.92
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

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

### Caterpillar (CAT) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> News flow is almost entirely noise — 'cat' keyword contamination, a DCF opinion piece and a rate-sensitivity roundup — with no ticker-specific catalyst. Technicals are mixed: above 20d and 200d but below 50d, RSI ~51, MACD histogram turning up, yet 3-month return is -19.8% and volume is a quarter of average, so the +4.6% 5-day bounce is unconfirmed. Fundamentals are strong operationally (24% revenue growth, 68% earnings growth, 57% ROE, four straight beats) but valuation is rich at 35x trailing/19x book with 233% debt/equity and beta 1.59. Consensus buy is already priced, with a large hold contingent and stale rating changes; insider net buying is a single 250-share director purchase against executive sales. No dimension corroborates another strongly enough for a directional call ahead of the 10/29 print.

**Main reasons it gave:**
- News set dominated by irrelevant 'cat' keyword matches; no ticker-specific catalyst
- Price below 50d SMA (-2.1%) but above 200d (+4.4%); RSI 51, MACD histogram +3.65
- 3-month return -19.8% while 5-day +4.6% on 0.25x average volume
- Four consecutive earnings beats (31%, 19%, 9%, 8%) with +24% revenue and +68% earnings growth
- Rich valuation: 35x trailing P/E, 19.4x book, debt/equity 233%
- Mean target 975.61 (+19%) but 12 of 26 analysts at hold and no rating changes since 2024

<details><summary><b>News</b> — score +0.00</summary>

- [What Higher Interest Rates Mean for Caterpillar, GE Vernova, and Vertiv](https://finance.yahoo.com/markets/stocks/articles/higher-interest-rates-mean-caterpillar-085500295.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  It's important not to panic over the impact of rising rates on industrial stocks, not least because they are likely to affect different stocks in varied...
- [Is CAT Overvalued? DCF Says Worth $621](https://www.gurufocus.com/news/9089603/is-cat-overvalued-dcf-says-worth-621)  
  <sub>GuruFocus, 3 hours ago</sub>  
  On September 21, 2026, we conducted a DCF analysis for Caterpillar Inc (CAT), a company that has shown impressive price performance over the past year,...
- [Tracking bacterial growth in response to nutrients and antibiotics](https://www.news-medical.net/whitepaper/20260921/Tracking-bacterial-growth-in-response-to-nutrients-and-antibiotics.aspx)  
  <sub>News-Medical, 6 hours ago</sub>  
  Measuring the wavelength-specific absorbance of light by cultures over time can provide insights about microbial growth. Bacterial growth curves performed...
- [Skater Makes A Strong Super Stock Statement](https://www.powerboatnation.com/skater-makes-a-strong-super-stock-statement/)  
  <sub>Powerboat Nation, 1 hour ago</sub>  
  Though the Skater 388 catamaran model remains dominant in offshore racing's Super Cat class, the brand had all but vanished from the Super Stock ranks...
- [Jason Calacanis Calls Bitcoin a 'Dead Cat' Which Continues to Bounce—Cathie Wood Argues BTC Has 'Many Liv](https://www.benzinga.com/crypto/cryptocurrency/26/09/61887673/jason-calacanis-bitcoin-dead-cat-cathie-wood-many-lives-ahead)  
  <sub>Benzinga, 8 hours ago</sub>  
  Ark Invest CEO Cathie Wood on Saturday, September 19, rebutted the argument that Bitcoin is an outdated and "boring" store of value.
- [Caterpillar stock gains as valuation eases after recent correction](https://www.ad-hoc-news.de/boerse/news/corporate-news/caterpillar-stock-gains-as-valuation-eases-after-recent-correction/70144654)  
  <sub>AD HOC NEWS, 2 hours ago</sub>  
  Caterpillar stock closed at USD 808.99 on September 20, 2026, about 1.30% higher on the day and near its recent trading range. Recent analysis highlights a...
- [Why Caterpillar Inc. (NYSE:CAT) Is In Focus Now?](https://kalkinemedia.com/us/stocks/bluechip/why-caterpillar-inc-nysecat-is-in-focus-now)  
  <sub>Kalkine Media, 6 hours ago</sub>  
  Caterpillar Inc. (CAT) draws attention after a current business development reshapes the market discussion around operations, customers, competition,...
- [Michael Saylor Hints at More MicroStrategy Bitcoin Buys After “Dead Cat Bounce” Debate](https://www.mitrade.com/au/insights/stock-analysis/us-stocks/beincrypto-BTCUSD-202609210933)  
  <sub>Mitrade, 13 hours ago</sub>  
  MicroStrategy has not bought Bitcoin (BTC) in two weeks, its most recent regulatory filing shows. In his latest post, however, Executive Chairman Michael...
- [Drone Stocks Are Back In Play: Why RCAT, AVAV, KTOS, UMAC Stocks Are Climbing](https://stocktwits.com/news-articles/markets/equity/drone-stocks-are-back-in-play-why-rcat-avav-ktos-umac-stocks-are-climbing/cZZbZqyR7pc)  
  <sub>Stocktwits, 12 hours ago</sub>  
  Red Cat Holdings (RCAT), AeroVironment (AVAV), Kratos Defense & Security Solutions (KTOS) and Unusual Machines (UMAC) stocks gained overnight as investors...
- [Portage Girl Scouts build pet pantry for dogs, cats](https://www.chicagotribune.com/2026/09/20/portage-girl-scouts-build-pet-pantry/)  
  <sub>Chicago Tribune, 18 hours ago</sub>  
  Girl Scout Troop 35579 used the Little Free Library concept to build a pet pantry for dogs and cats. It now stands outside Portage's Woodland Park dog park.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.10</summary>

```text
Last close 819.80 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 804.19 (+1.9%), 50d 837.49 (-2.1%), 200d 785.30 (+4.4%); 50d above 200d
Momentum: RSI(14) 51.1 | MACD -10.597 vs signal -14.249 (histogram 3.652)
Returns: 1d +1.3% | 5d +4.6% | 1m +0.5% | 3m -19.8%
52-week range: 463.72 - 1,064.90 (now 59.2% of the way up)
Volatility: ATR(14) 24.56 (3.0% of price) | annualised 20d 26.9%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 376.84B
Valuation: trailing P/E 35.31 | forward P/E 25.32 | P/B 19.43 | PEG 1.42
Profitability: profit margin 14.5% | operating margin 22.2% | ROE 57.0%
Growth (YoY): revenue +24.0% | earnings +68.2%
Balance sheet: debt/equity 232.8% | free cash flow 5.05B
Risk: beta 1.59 | short interest 1.8% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.35</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 31% | 2026-03-31 beat by 19% | 2025-12-31 beat by 9% | 2025-09-30 beat by 8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: buy (mean 2.14 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 1 strong buy, 13 buy, 12 hold, 1 sell, 1 strong sell
Price target: mean 975.61 (+19.0% vs last close), range 575.00 - 1,225.00
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

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

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

_Not available today._

</details>

### Elbit Systems (ESLT) · Company — NEUTRAL, confidence 0.35

**In the model's own words:**

> Elbit Systems shows mixed signals that don't cohere into a directional conviction. The rebranding of its U.S. segment as Twenty-Six Defense is corporate repositioning that may improve market access, but it is a structural change not a catalyst with near-term margin impact. Fundamentals are strong: four consecutive earnings beats, 34% YoY earnings growth, and healthy 15.2% ROE. However, the valuation is stretched—a 56x trailing P/E and 41x forward P/E on a defense industrials name trades at a significant premium. Technicals show modest momentum with RSI at 54.7 and MACD histogram positive, but the stock is 1.5-1.7% below its 50d and 200d moving averages, with volume at 0.14x the 20-day average, suggesting positioning is thin and conviction among participants is low. The analyst consensus is 'hold' with a mean target of 816 (+8.7%), implying limited upside. Insider selling in April—including the CEO's substantial 25k share sale—was clustered and substantial, though without buys to counter it, the signal remains ambiguous and may reflect scheduled diversification rather than conviction. The rebranding announcement is news-cycle fodder, not a material catalyst. Near-term earnings are not until late November, leaving a long period of data vacuum. The absence of independent corroboration across dimensions—bullish earnings history undercut by expensive valuation and analyst skepticism, weak volume, and lack of insider buying conviction—does not support a high-conviction directional call.

**Main reasons it gave:**
- Four consecutive quarterly earnings beats; 34% YoY earnings growth
- Valuation stretched at 56x trailing P/E; analyst consensus 'hold' with modest +8.7% upside
- Rebranding announcement is structural repositioning, not near-term catalyst
- Volume at 0.14x 20d average and price below both 50d and 200d SMAs suggest weak positioning
- CEO and officer sales in April aggregating ~45k shares with no offsetting insider buys

<details><summary><b>News</b> — score +0.20</summary>

- [Elbit Systems (TASE:ESLT) Just Gave Investors Something To Think About](https://simplywall.st/stocks/il/capital-goods/tase-eslt/elbit-systems-shares/news/elbit-systems-taseeslt-just-gave-investors-something-to-thin/amp)  
  <sub>Simply Wall Street, 9 hours ago</sub>  
  Elbit Systems (TASE:ESLT) just reshaped its U.S. presence by rebranding its American operating segment as Twenty-Six Defense. This move puts domestic design...
- [Why Is Elbit Systems (TASE:ESLT) Rebranding Its U.S. Business As Twenty Six Defense?](https://finance.yahoo.com/markets/stocks/articles/why-elbit-systems-tase-eslt-171034248.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Elbit Systems (TASE:ESLT) has rebranded its U.S. operating segment as Twenty-Six Defense, targeting the domestic American defense market.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.15</summary>

```text
Last close 750.72 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 721.88 (+4.0%), 50d 762.15 (-1.5%), 200d 763.87 (-1.7%); 50d below 200d
Momentum: RSI(14) 54.7 | MACD -5.690 vs signal -12.652 (histogram 6.962)
Returns: 1d +1.0% | 5d +3.6% | 1m +0.9% | 3m -3.1%
52-week range: 454.95 - 1,014.33 (now 52.9% of the way up)
Volatility: ATR(14) 16.19 (2.2% of price) | annualised 20d 15.5%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 35.18B
Valuation: trailing P/E 56.49 | forward P/E 40.88 | P/B 7.96 | PEG n/a
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

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 10% | 2026-03-31 beat by 16% | 2025-12-31 beat by 16% | 2025-09-30 beat by 21%
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

<details><summary><b>What analysts and big funds say</b> — score -0.15</summary>

```text
Consensus: hold (mean 2.67 on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 816.33 (+8.7% vs last close), range 518.00 - 960.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

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

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

_Not available today._

</details>

### HDFC Bank (HDB) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> News is mostly noise (HDB Financial Services items are a different entity, plus generic roundups); the only ticker-specific piece is a balanced Seeking Alpha note on margin pressure. Technically the stock is below its 200d with a bearish 50/200 cross and sits near the bottom of its 52-week range, though short-term momentum has improved on very thin volume (0.23x). Fundamentals are solid (16-18% growth, 27% margins) but P/B 9.5 is rich and ROE 13.8% is subdued. Analyst targets imply +30% upside, but the coverage set is small and stale. No insider transactions. Nothing here justifies a directional bet ahead of Oct 17 earnings.

**Main reasons it gave:**
- Price -14.4% vs 200d SMA with 50d below 200d, only 11.9% up the 52-week range
- Volume 0.23x 20-day average limits signal value of the +2.2% day
- Most headlines refer to HDB Financial Services or are generic market roundups, not HDB itself
- Revenue +16.6%/earnings +18.1% but P/B 9.46 and ROE 13.8% with margin pressure flagged
- Consensus buy with mean target 30.77 (+30%), but only 4 analysts and no recent rating changes

<details><summary><b>News</b> — score +0.05</summary>

- [HDFC Bank: Growth Is Back, But The Margin Recovery Matters More (NYSE:HDB)](https://seekingalpha.com/article/4948335-hdfc-bank-growth-is-back-but-the-margin-recovery-matters-more)  
  <sub>Seeking Alpha, 38 minutes ago</sub>  
  HDFC Bank (HDB) shows strong loan growth and asset quality, but margins/ROE lag.
- [HDB: HDFC Bank Limited - Stock Price, Quote and News | NYSE](https://techgraph.co/stock-market/quote/hdb/)  
  <sub>TechGraph, 4 hours ago</sub>  
  HDB: HDFC Bank Limited stock price, quote and news on NYSE. Live HDB chart, volume, 52-week range and coverage on TechGraph.
- [MCAT - Price, Charts & Blockchain Insights](https://intellectia.ai/crypto/MCAT)  
  <sub>Intellectia AI, 6 hours ago</sub>  
  PAGE NOT FOUND. Oops! It seems the page you are looking for does not exist... Back to Homepage. Blog. Get What You Are Looking For Here. oil prices,stock...
- [Benchmarks trade near the day's high; metal shares tumble on profit booking](https://www.business-standard.com/markets/capital-market-news/benchmarks-trade-near-the-day-s-high-metal-shares-tumble-on-profit-booking-126092100577_1.html)  
  <sub>Business Standard, 6 hours ago</sub>  
  The domestic equity barometers traded with strong gains and hit fresh intraday high in afternoon trade, supported by easing crude oil prices and positive...
- [HDB Financial Services - Positive Breakout: These 12 midcap stocks cross above their 200 DMAs](https://m.economictimes.com/markets/stocks/news/positive-breakout-these-12-midcap-stocks-cross-above-their-200-dmas/hdb-financial-services/slideshow/134378054.cms)  
  <sub>The Economic Times, 13 hours ago</sub>  
  200 DMA: Rs 696.53| LTP: Rs 698.4 HDB Financial Services.
- [688187.SH Technical Analysis & Stock Price Forecast](https://intellectia.ai/en/stock/688187.SH/technical)  
  <sub>Intellectia AI, 15 hours ago</sub>  
  Get realtime 688187.SH technical analysis, moving averages, RSI, and MACD indicators. View professional stock forecasts and buy/sell signals.
- [HDB Financial Services ESOP Allotment: 29,480 Shares Issued](https://www.kalkine.co.in/article/announcements/hdb-financial-services-nsehdbfs-what-triggered-the-allotment-of-29480-equity-shares-under-esop)  
  <sub>Kalkine India, 8 hours ago</sub>  
  HDB Financial Services (NSE:HDBFS) allotted 29480 equity shares under its ESOP on 21 Sep 2026, raising paid-up capital. Here is what investors should know.
- [HDB Financial Services allots 29,480 equity shares under ESOS](https://www.business-standard.com/markets/capital-market-news/hdb-financial-services-allots-29-480-equity-shares-under-esos-126092100526_1.html)  
  <sub>Business Standard, 6 hours ago</sub>  
  HDB Financial Services has allotted 29480 equity shares to the employees of the company pursuant to exercise of options under its Employees Stock Option...
- [Which NBFCs will gain the most from rate hike cycle? JM Financial lists top picks](https://m.economictimes.com/markets/stocks/news/which-nbfcs-will-gain-the-most-from-rate-hike-cycle-jm-financial-lists-top-picks/amp_articleshow/134386955.cms)  
  <sub>The Economic Times, 5 hours ago</sub>  
  Soaring bond yields and rate hike worries have led to a downturn in Indian NBFC stocks, with JM Financial noting that investors must juxtapose the NIM...
- [688187.SH Earning Date, Earning Analysis and Earning Prediction](https://intellectia.ai/en/stock/688187.SH/earnings)  
  <sub>Intellectia AI, 15 hours ago</sub>  
  Explore 688187.SH earnings with our in-depth analysis, covering revenue trends, EPS, earnings surprises, and market reactions. Get detailed insights into...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 23.67 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 22.91 (+3.3%), 50d 23.55 (+0.5%), 200d 27.65 (-14.4%); 50d below 200d
Momentum: RSI(14) 55.8 | MACD -0.151 vs signal -0.270 (histogram 0.119)
Returns: 1d +2.2% | 5d +3.4% | 1m +1.4% | 3m -5.7%
52-week range: 21.84 - 37.18 (now 11.9% of the way up)
Volatility: ATR(14) 0.56 (2.4% of price) | annualised 20d 37.3%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 121.61B
Valuation: trailing P/E 16.55 | forward P/E 17.01 | P/B 9.46 | PEG n/a
Profitability: profit margin 26.8% | operating margin 33.3% | ROE 13.8%
Growth (YoY): revenue +16.6% | earnings +18.1%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.40 | short interest 0.7% of float
Next earnings: 2026-10-17
```

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.25</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-06-30 in line | 2026-03-31 in line | 2025-12-31 beat by 61% | 2025-09-30 beat by 10%
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

```text
Consensus: buy (mean 1.75 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 1 strong buy, 2 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 30.77 (+30.0% vs last close), range 26.10 - 35.00
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

### JPMorgan Chase (JPM) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The $20B QIA asset-management partnership is real but immaterial to near-term earnings for a $935B bank, and much of the remaining flow is Zacks/listicle noise. Technicals are flat-to-soft: price below 20d and 50d, MACD negative, RSI 47, volume 0.19x average, though the 50d>200d uptrend and +9.6% vs 200d remain intact. Fundamentals are sound (15x forward, 17.8% ROE, four straight beats) but earnings are three weeks out on 10/13. Consensus is a lukewarm buy with only 6.8% upside and no fresh rating changes; insider net share count is positive only via grants, with 10 distinct sellers and zero open-market buyers. No corroborated catalyst for the next few days.

**Main reasons it gave:**
- $20B QIA partnership is fee-business scale, not near-term EPS mover
- Price below 20d/50d SMAs, MACD histogram -0.96, RSI 47.5
- Volume 0.19x 20-day average — thin, low-information tape
- 4 consecutive earnings beats; earnings 2026-10-13, outside window
- Consensus buy but only +6.8% to mean target; no recent rating changes
- 10 distinct insider sellers, zero open-market buyers

<details><summary><b>News</b> — score +0.15</summary>

- [Investors Heavily Search JPMorgan Chase & Co. (JPM): Here is What You Need to Know](https://finance.yahoo.com/markets/stocks/articles/investors-heavily-search-jpmorgan-chase-130003199.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  JPMorgan Chase & Co. (JPM) is one of the stocks most watched by Zacks.com visitors lately. So, it might be a good idea to review some of the factors that...
- [J.P. Morgan and Qatar’s investment authority plan $20B for stocks and U.S. businesses](https://www.stocktitan.net/news/JPM/qia-and-j-p-morgan-asset-management-announce-20-billion-strategic-lvu4iu9e7ix1.html)  
  <sub>Stock Titan, 3 hours ago</sub>  
  J.P. Morgan Asset Management (JPM) and Qatar Investment Authority have signed a Memorandum of Understanding for a USD 20 billion strategic investment...
- [J.P. Morgan and Qatar Investment Authority ink $20B partnership (JPM:NYSE)](https://seekingalpha.com/news/4644742-j-p-morgan-and-qatar-investment-authority-ink-20b-partnership)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  JPMorgan Asset Management and Qatar Investment Authority launch a $20B partnership spanning public equities and private credit.
- [Zacks Market Edge Highlights: ExxonMobil, JPMorgan Chase and NVIDIA](https://www.tradingview.com/news/zacks:84adcc7ce094b:0-zacks-market-edge-highlights-exxonmobil-jpmorgan-chase-and-nvidia/)  
  <sub>TradingView, 2 hours ago</sub>  
  For Immediate ReleaseChicago, IL – September 21, 2026 – Zacks Market Edge is a podcast hosted weekly by Zacks Stock Strategist Tracey Ryniec.
- [JPM Looks 15.1% Overvalued on GF Value™ as Dividend Sustainabili](https://www.gurufocus.com/news/9090048/jpm-looks-151-overvalued-on-gf-value-as-dividend-sustainability-takes-center-stage)  
  <sub>GuruFocus, 25 minutes ago</sub>  
  On September 21, 2026, JPMorgan Chase & Co (NYSE: JPM) announced a $20 billion strategic partnership with the Qatar Investment Authority (QIA),...
- [Fed Rate Hike Fails to Lift Bank Stocks as Market Reprices the Rally](https://www.aol.com/articles/fed-rate-hike-fails-lift-132042000.html)  
  <sub>AOL.com, 2 hours ago</sub>  
  The Fed raised rates for the first time in three years, and bank stocks promptly sold off. What looks like a contradiction might be a warning about where...
- [Apple: JPM says iPhone 18 lead times increase in second week](https://www.investing.com/news/stock-market-news/apple-jpm-says-iphone-18-lead-times-increase-in-second-week-4908259)  
  <sub>Investing.com, 9 hours ago</sub>  
  Investing.com-- Apple Inc's (NASDAQ:AAPL) new iPhone 18 Pro lineup saw increased lead times in its second week of orders and now broadly matches those seen...
- [JPMorgan Chase & Co. $JPM Shares Sold by Palisade Capital Management LP](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-shares-sold-by-palisade-capital-management-lp-2026-09-21/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Palisade Capital Management LP reduced its position in JPMorgan Chase & Co. (NYSE:JPM) by 8.2% during the 2nd quarter, according to its most recent filing...
- [Will JPMorgan's Selective M&A Strategy Expand Growth Runway?](https://www.tradingview.com/news/zacks:ce228a5e2094b:0-will-jpmorgan-s-selective-m-a-strategy-expand-growth-runway/)  
  <sub>TradingView, 2 hours ago</sub>  
  JPMorgan Chase JPM does not need acquisitions to fuel growth, but that may be exactly what gives it an edge when the right opportunity emerges.
- [JPM, Jamie Dimon to Boost Investment in India's Thriving Market](https://www.gurufocus.com/news/9089744/jpm-jamie-dimon-to-boost-investment-in-indias-thriving-market)  
  <sub>GuruFocus, 2 hours ago</sub>  
  On September 21, 2026, JPMorgan Chase CEO Jamie Dimon is set to visit India as the firm intensifies its focus on the local market. The stock ticker for...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 351.62 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 354.47 (-0.8%), 50d 353.50 (-0.5%), 200d 320.75 (+9.6%); 50d above 200d
Momentum: RSI(14) 47.5 | MACD -0.892 vs signal 0.071 (histogram -0.963)
Returns: 1d +0.6% | 5d +0.4% | 1m +0.0% | 3m +6.1%
52-week range: 282.84 - 365.18 (now 83.5% of the way up)
Volatility: ATR(14) 6.62 (1.9% of price) | annualised 20d 14.0%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.45</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 934.68B
Valuation: trailing P/E 15.08 | forward P/E 14.07 | P/B 2.64 | PEG 1.63
Profitability: profit margin 34.9% | operating margin 50.4% | ROE 17.8%
Growth (YoY): revenue +30.4% | earnings +46.9%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.97 | short interest 1.0% of float
Next earnings: 2026-10-13
```

</details>

<details><summary><b>What this fund holds</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.45</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 4% | 2026-03-31 beat by 8% | 2025-12-31 beat by 3% | 2025-09-30 beat by 4%
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

<details><summary><b>What analysts and big funds say</b> — score +0.15</summary>

```text
Consensus: buy (mean 2.12 on a 1=strong buy to 5=strong sell scale, 21 analysts)
Ratings: 4 strong buy, 9 buy, 10 hold, 0 sell, 1 strong sell
Price target: mean 375.38 (+6.8% vs last close), range 305.00 - 436.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

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

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

_Not available today._

</details>

### MercadoLibre (MELI) · Company — NEUTRAL, confidence 0.35

**In the model's own words:**

> MELI presents conflicting signals that warrant caution. The technical picture is genuinely weak: price is 4.8% below the 20-day SMA, RSI at 42.9 is approaching oversold, MACD has turned negative, and volume is 28% of average—all suggesting near-term downward pressure. The stock has declined 5.2% over one month despite broader strength. News flow is mixed, with recent commentary citing 'earnings outlook' concerns, which aligns with the earnings record showing 3 misses in the last 4 quarters (most recently 13% miss in Sept 2025). Fundamentals are expensive: forward P/E of 32.3 and trailing P/E of 49.5 sit well above tech peers, on a company with high leverage (debt/equity 168.6%) and declining earnings growth (-10.9% YoY) despite strong revenue growth. Analyst consensus (buy, 24 analysts, target +24.3%) is decidedly bullish and fully reflected in the current price, reducing its informational value. Insider activity shows two isolated buying transactions in May-June 2026—meaningful but not recent. The next catalyst (earnings Nov 4) is 44 days away, well beyond our short-term horizon. The company's profitability metrics (27.5% ROE, 6.7% operating margin) are solid, but a richly valued, high-beta name in a correction with deteriorating technicals and a history of missing guidance does not justify conviction above neutral. Short-term technicals argue for a bounce risk, but current setup is tentative.

**Main reasons it gave:**
- 3 misses vs 1 beat in earnings record; most recent miss 13%
- Price 4.8% below 20-day SMA with RSI 42.9 and negative MACD
- Forward P/E 32.3 and trailing P/E 49.5 with leverage at 168% debt/equity
- Analyst consensus already priced in at +24% target, limiting upside surprise
- Volume 28% of average indicates weak conviction in bounce

<details><summary><b>News</b> — score -0.30</summary>

- [MELI stock heads into the open after a 2.07 percent drop](https://www.ad-hoc-news.de/boerse/news/corporate-news/meli-stock-heads-into-the-open-after-a-2-07-percent-drop/70142535)  
  <sub>AD HOC NEWS, 8 hours ago</sub>  
  At the close on September 18, 2026, MELI stock finished at USD 1787.39 on Nasdaq after falling 2.07 percent; the shares traded within a recent range and sat...
- [MercadoLibre stock slips on earnings outlook and BTIG](https://www.ad-hoc-news.de/boerse/news/corporate-news/mercadolibre-stock-slips-on-earnings-outlook-and-btig/70143613)  
  <sub>AD HOC NEWS, 5 hours ago</sub>  
  MELI, US58733R1023. MercadoLibre stock slips on earnings outlook and BTIG. Published on 09/21/2026 at 12:22 | Editorial responsibility: Rafael Müller,...
- [Melisron (TASE:MLSR) Stock Still Looks Like A Bargain After An 81% Run](https://finance.yahoo.com/markets/stocks/articles/melisron-tase-mlsr-stock-still-011230128.html)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  Melisron has delivered a strong 3 year share price run, and that kind of gain naturally raises the question of whether the current price is still aligned...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 1,822.24 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 1,913.90 (-4.8%), 50d 1,876.87 (-2.9%), 200d 1,851.53 (-1.6%); 50d above 200d
Momentum: RSI(14) 42.9 | MACD -16.066 vs signal 3.121 (histogram -19.187)
Returns: 1d +1.9% | 5d -4.1% | 1m -5.2% | 3m +14.6%
52-week range: 1,546.81 - 2,510.97 (now 28.6% of the way up)
Volatility: ATR(14) 60.31 (3.3% of price) | annualised 20d 29.7%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.25</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 92.38B
Valuation: trailing P/E 49.49 | forward P/E 32.28 | P/B 11.79 | PEG 0.98
Profitability: profit margin 5.3% | operating margin 6.7% | ROE 27.5%
Growth (YoY): revenue +49.8% | earnings -10.9%
Balance sheet: debt/equity 168.6% | free cash flow 353.38M
Risk: beta 1.31 | short interest 1.6% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.25</summary>

```text
Earnings record, last 4 quarters: 1 beat, 3 missed
  2026-06-30 beat by 4% | 2026-03-31 missed by 7% | 2025-12-31 missed by 6% | 2025-09-30 missed by 13%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: buy (mean 1.58 on a 1=strong buy to 5=strong sell scale, 24 analysts)
Ratings: 4 strong buy, 15 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 2,264.88 (+24.3% vs last close), range 1,750.00 - 2,800.00
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

### Procter & Gamble (PG) · Company — NEUTRAL, confidence 0.35

**In the model's own words:**

> PG presents conflicting signals that resist a directional conviction. On the positive side: recent fiscal Q4 results were solid, the company delivered 4 consecutive earnings in line with expectations, a strong analyst consensus (6 strong buys, 7 buys vs zero sells), mean price target of $160.61 (+10.1%) suggests upside, solid fundamentals including 30.3% ROE and 22.1% operating margin, and significant insider net buying (+50,121 shares over 180 days from 25 transactions). On the negative side: the GuruFocus DCF analysis values PG at $90 intrinsic value vs $146 price (37% overvalued), trailing P/E of 22.03 is elevated for single-digit revenue growth (+1.5%), earnings declined 15.5% YoY despite solid absolute profitability, PEG of 3.75 signals expensive valuation relative to growth, and recent technical weakness with the stock down 1.1% from its 200d SMA and trading below its 50d average. The news flow is mixed and largely generic (dividend reviews, DCF commentary) with no material catalyst. Technicals show neutral momentum (RSI 50.4) and a stock holding near recent highs but not breaking out; volume is notably thin at 0.13x average. The recent downgrade pattern (Argus Research and HSBC both moved from Buy to Hold in late July/early August) suggests analyst sentiment may be shifting, though the consensus remains constructive. The insider buying appears routine (officers selling portions of holdings for liquidity/tax purposes) rather than a concentrated signal of conviction. Given the valuation concern, modest growth, recent analyst downgrades amid weak volume, and absence of a near-term catalyst, a NEUTRAL posture at low-to-moderate conviction is appropriate until either the valuation compresses or a clearer fundamental catalyst emerges.

**Main reasons it gave:**
- DCF intrinsic value $90 vs price $146 (37% overvaluation)
- Earnings declined 15.5% YoY despite 4 consecutive quarters in line
- Recent downgrades from Argus Research and HSBC (Buy to Hold)
- Elevated trailing P/E 22.03 on modest 1.5% revenue growth
- Insider net buying of 50,121 shares routine for officers, not concentrated conviction

<details><summary><b>News</b> — score -0.15</summary>

- [3 Unpopular Stocks Walking a Fine Line](https://stockstory.org/us/stocks/nyse/pg/news/buy-or-sell/3-unpopular-stocks-walking-a-fine-line)  
  <sub>StockStory, 7 hours ago</sub>  
  Wall Street has issued downbeat forecasts for the stocks in this article. These predictions are rare - financial institutions typically hesitate to say bad...
- [PG DCF Analysis: Intrinsic Value $90 vs Price $146](https://www.gurufocus.com/news/9089607/pg-dcf-analysis-intrinsic-value-90-vs-price-146)  
  <sub>GuruFocus, 3 hours ago</sub>  
  On September 21, 2026, we delve into the DCF analysis for Procter & Gamble Co (PG), a company that has seen mixed price performance recently,...
- [Best Dividend Stocks for 2026: What 2025’s Winners Tell Investors](https://finchannel.com/best-dividend-stocks-for-2026-what-2025s-winners-tell-investors/135909/american-business-trends/stock-prices/2026/09/)  
  <sub>finchannel, 7 hours ago</sub>  
  A review of the best-performing dividend stocks of 2025, including CVS, Invesco, Hasbro, Ford and others, with dividend trends and 2026 outlook.
- [Procter & Gamble stock holds firm as investors eye recent earnings and dividend strength](https://www.ad-hoc-news.de/boerse/news/corporate-news/procter-and-gamble-stock-holds-firm-as-investors-eye-recent-earnings-and/70143504)  
  <sub>AD HOC NEWS, 5 hours ago</sub>  
  Procter & Gamble stock trades near its recent high after solid fiscal Q4 2026 results reported on August 2, 2026. The consumer goods giant lifted annual...
- [I'm Watching PG&E Closely, but Here's Why I Haven't Bought the Dip](https://www.aol.com/articles/im-watching-pg-e-closely-162500000.html)  
  <sub>AOL.com, 23 hours ago</sub>  
  Utilities are usually seen as low-risk bets, but due to its California footprint, risk abounds with PG&E.
- [PG Electroplast to host investor meet at Nuvama CEO Forum on Sep 28](https://scanx.trade/stock-market-news/companies/pg-electroplast-host-investor-meet-nuvama-ceo-forum-sep-28/51519154)  
  <sub>scanx.trade, 8 hours ago</sub>  
  PG Electroplast will attend the Nuvama Emerging India CEO Forum on September 28, 2026. The physical meeting will take place at Hotel Grand Hyatt, Mumbai,...
- [HDB: HDFC Bank Limited - Stock Price, Quote and News | NYSE](https://techgraph.co/stock-market/quote/hdb/)  
  <sub>TechGraph, 4 hours ago</sub>  
  HDB: HDFC Bank Limited stock price, quote and news on NYSE. Live HDB chart, volume, 52-week range and coverage on TechGraph.
- [Procter & Gamble stock heads into the open after a muted move](https://www.ad-hoc-news.de/boerse/news/corporate-news/procter-and-gamble-stock-heads-into-the-open-after-a-muted-move/70142078)  
  <sub>AD HOC NEWS, 9 hours ago</sub>  
  At the close on September 18, 2026, Procter & Gamble stock finished little changed on the NYSE, holding within its recent trading range while the S&P 500...
- [POWERGRID Infrastructure Inves Share Price - Live PGINVIT Stock Price & Chart](https://upstox.com/stocks/powergrid-infrastructure-inves-share-price/)  
  <sub>Upstox, 8 hours ago</sub>  
  Get POWERGRID Infrastructure Inves share price, market statistics, corporate action, fundamental and technical analysis at Upstox.
- [PG&E Corporation stock falls sharply as wildfire liability fears mount](https://www.ad-hoc-news.de/boerse/news/corporate-news/pg-and-e-corporation-stock-falls-sharply-as-wildfire-liability-fears-mount/70139139)  
  <sub>AD HOC NEWS, 22 hours ago</sub>  
  PG&E Corporation stock has dropped about 26.5 percent over the past 30 days to USD 13.20 as of September 18, 2026 amid renewed wildfire liability concerns.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.05</summary>

```text
Last close 145.87 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 145.62 (+0.2%), 50d 146.10 (-0.2%), 200d 147.46 (-1.1%); 50d below 200d
Momentum: RSI(14) 50.4 | MACD 0.200 vs signal -0.003 (histogram 0.204)
Returns: 1d -0.4% | 5d -0.2% | 1m +2.0% | 3m -1.2%
52-week range: 138.04 - 167.20 (now 26.9% of the way up)
Volatility: ATR(14) 2.25 (1.5% of price) | annualised 20d 14.4%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.35</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 338.81B
Valuation: trailing P/E 22.03 | forward P/E 19.71 | P/B 6.36 | PEG 3.75
Profitability: profit margin 18.4% | operating margin 22.1% | ROE 30.3%
Growth (YoY): revenue +1.5% | earnings -15.5%
Balance sheet: debt/equity 64.5% | free cash flow 13.28B
Risk: beta 0.38 | short interest 1.2% of float
Next earnings: 2026-10-22
```

</details>

<details><summary><b>What this fund holds</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.35</summary>

```text
Earnings record, last 4 quarters: 4 in line
  2026-06-30 in line | 2026-03-31 in line | 2025-12-31 in line | 2025-09-30 in line
```

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

```text
Consensus: buy (mean 2.20 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 6 strong buy, 7 buy, 12 hold, 0 sell, 0 strong sell
Price target: mean 160.61 (+10.1% vs last close), range 143.00 - 186.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.05</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.05</summary>

_Not available today._

</details>

### Royal Bank of Canada (RY) · Company — NEUTRAL, confidence 0.35

**In the model's own words:**

> Royal Bank of Canada presents a mixed picture with no clear directional catalyst. News is generic coverage focused on the 2.47% dividend yield and P/E valuation (15.4x in one headline, 18.1x in fundamentals) without material new developments or earnings-specific catalysts. Technicals show a stock that is neither extended nor deeply oversold: RSI at 46.8 is neutral, price sits 11% above the 200d MA but only 0.3% below the 20d, and volume is thin at 0.13x average. The most recent earnings were in line (last two quarters), with an earlier beat already digested. Valuation at 18.1x forward P/E is cited as a "quality premium" but places RY above peers like CIBC and TD on trailing multiples. Analyst consensus is solidly bullish (mean 2.13, mostly buy/strong buy ratings) with a mean price target of 209.55 (+2.1%), but this consensus appears fully reflected in the 49.6% institutional ownership and the modest rating activity over the past 18 months. Insider activity consists of share buybacks by the issuer (the company itself), which is a weak signal—buybacks are routine capital allocation, not insiders with superior information deploying personal capital. No officers or directors are buying. Growth is solid (revenue +8.9%, earnings +12.8% YoY) and profitability is healthy, but these support a "hold at fair value" thesis rather than a near-term directional move. Earnings are not until December 3, 2026, leaving 2.5 months until the next material catalyst. The stock's intraday action shows a 0.9% bounce but zero return over the past month, suggesting equilibrium. With no fresh catalyst, conflicting valuation narratives, thin volume, and insider disinterest, conviction merits a below-midpoint NEUTRAL call.

**Main reasons it gave:**
- Recent earnings in line with consensus, not beats
- Analyst consensus already reflected in 49.6% institutional ownership and modest 2.1% upside to mean target
- Share buybacks by issuer, not open-market purchases by officers indicating personal conviction
- No material catalyst until December 3 earnings date
- Valuation dispute in headlines (15.4x vs 18.1x) with stock trading above peer multiples on trailing basis

<details><summary><b>News</b> — score +0.00</summary>

- [Royal Bank of Canada stock holds firm as earnings and valuation draw focus](https://www.ad-hoc-news.de/boerse/news/corporate-news/royal-bank-of-canada-stock-holds-firm-as-earnings-and-valuation-draw-focus/70144761)  
  <sub>AD HOC NEWS, 2 hours ago</sub>  
  Royal Bank of Canada stock trades at a P/E of 15.4x as of September 20, 2026, highlighting a quality premium over Canadian peers.
- [Why Is Royal Bank of Canada (TSX:RY) Drawing Fresh Attention?](https://kalkinemedia.com/ca/stocks/bluechip/why-is-royal-bank-of-canada-tsxry-drawing-fresh-attention)  
  <sub>Kalkine Media, 7 hours ago</sub>  
  Royal Bank of Canada coverage examines current market developments, its banking, wealth services and capital markets operations and the S&P/TSX 60 backdrop...
- [Royal Bank of Canada’s 2.47% Yield Looks Well Supported as Earnings Growth and Capital Strength Reinforce Dividend Outlook](https://kalkine.ca/news/dividend-stocks/royal-bank-of-canadas-247-yield-looks-well-supported-as-earnings-growth-and-capital-strength-reinforce-dividend-outlook)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [RY stock heads into the open after a modest decline on the TSX](https://www.ad-hoc-news.de/boerse/news/corporate-news/ry-stock-heads-into-the-open-after-a-modest-decline-on-the-tsx/70142014)  
  <sub>AD HOC NEWS, 9 hours ago</sub>  
  At the close on September 20, 2026, RY stock finished at CAD 284.45 on the Toronto Stock Exchange, slipping 0.17 percent, while the broader Canadian market...
- [Resolute Mining Stock Drops 8.3% as Syama Cut Narrows Gold-Price Buffer](https://ts2.tech/en/resolute-mining-stock-drops-8-3-as-syama-cut-narrows-gold-price-buffer/)  
  <sub>TechStock², 10 hours ago</sub>  
  Sydney, September 21, 2026, 15:24 (AEST). Resolute traded at A$1.242, down 8.3%, at 15:17 AEST. The 2026 group production midpoint fell 18.1% to 215,000...
- [CIBC stands out as the value pick among Canada’s major bank stocks](https://uk.investing.com/news/stock-market-news/cibc-stands-out-as-the-value-pick-among-canadas-major-bank-stocks-93CH-4875332)  
  <sub>Investing.com UK, 24 hours ago</sub>  
  Investing.com -- CIBC and TD Bank currently look like the cheapest Canadian bank stocks by P/E ratio—both trading under 14x trailing earnings, while Royal...
- [Why Is Royal Bank of Canada (TSX:RY) Back in Focus?](https://kalkinemedia.com/ca/stocks/financial/why-is-royal-bank-of-canada-tsxry-back-in-focus-1)  
  <sub>Kalkine Media, 9 hours ago</sub>  
  Royal Bank of Canada coverage examines current market developments, its banking, wealth services and capital markets operations and the S&P/TSX 60 backdrop...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 205.23 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 205.84 (-0.3%), 50d 209.10 (-1.9%), 200d 184.77 (+11.1%); 50d above 200d
Momentum: RSI(14) 46.8 | MACD -1.236 vs signal -0.986 (histogram -0.250)
Returns: 1d +0.9% | 5d +0.0% | 1m +0.0% | 3m +1.2%
52-week range: 143.64 - 217.87 (now 83.0% of the way up)
Volatility: ATR(14) 3.18 (1.6% of price) | annualised 20d 15.5%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 284.12B
Valuation: trailing P/E 18.10 | forward P/E 16.07 | P/B 2.97 | PEG 2.26
Profitability: profit margin 33.9% | operating margin 46.4% | ROE 16.2%
Growth (YoY): revenue +8.9% | earnings +12.8%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.92 | short interest n/a of float
Next earnings: 2026-12-03
```

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.15</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-09-30 in line | 2026-06-30 in line | 2026-03-31 beat by 3% | 2026-03-31 beat by 3%
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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

```text
Consensus: buy (mean 2.13 on a 1=strong buy to 5=strong sell scale, 3 analysts)
Ratings: 4 strong buy, 5 buy, 5 hold, 0 sell, 1 strong sell
Price target: mean 209.55 (+2.1% vs last close), range 181.88 - 228.54
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

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

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

_Not available today._

</details>

### Toyota (TM) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> News flow is generic filler: most items are unrelated to Toyota (Pega, Cosmo, Indian market roundups), and the two TM headlines are auto-generated price recaps with no catalyst. Technicals are mid-range and mildly negative: price below 20d and 200d SMAs, 50d below 200d, MACD rolling under signal, RSI exactly 50, and volume at 0.11x average implies little information. Fundamentals are the most supportive leg — trailing P/E 8.6, +10.4% revenue and +86.9% earnings growth, four straight beats, low beta 0.34 — and analysts are strong_buy with a 21% target gap, but that prior is long-standing and already in the price. No insider transactions. Nothing ticker-specific to trade over a few days.

**Main reasons it gave:**
- TM-specific headlines are auto-generated price recaps; other news items concern unrelated companies
- 50d SMA below 200d, price -4.6% vs 200d, MACD histogram -0.788, RSI 50
- Trailing P/E 8.56 with revenue +10.4% and earnings +86.9% YoY
- Four consecutive earnings beats (44%, 12%, 27%, 24%)
- Strong_buy consensus with mean target 234 (+21.5%) but only 4 analysts and no fresh rating change
- No insider open-market transactions in 180 days

<details><summary><b>News</b> — score +0.00</summary>

- [Gartner gave Pega top scores in two business automation categories](https://www.stocktitan.net/news/PEGA/pega-named-a-leader-in-gartner-magic-quadrant-tm-and-recognized-in-moqn69n6omnn.html)  
  <sub>Stock Titan, 2 hours ago</sub>  
  Gartner assessed 20 vendors across seven criteria, while Pega's AI suite was recognized for a second consecutive year in a companion report.
- [Toyota Motor stock steadies as automation and demand plans shape outlook](https://www.ad-hoc-news.de/boerse/news/corporate-news/toyota-motor-stock-steadies-as-automation-and-demand-plans-shape-outlook/70144193)  
  <sub>AD HOC NEWS, 3 hours ago</sub>  
  TM, US8923313071. Toyota Motor stock steadies as automation and demand plans shape outlook. Published on 09/21/2026 at 13:48 | Editorial responsibility:...
- [More than 334,000 colonoscopies tested AI. Odds of detecting colon growths were 22% higher.](https://www.stocktitan.net/news/CMOPF/largest-real-world-study-of-the-gi-genius-tm-intelligent-endoscopy-5tkhp8ivrwz1.html)  
  <sub>Stock Titan, 10 hours ago</sub>  
  Cosmo (CMOPF) reported results from the CADeNCE study, the largest real‑world evaluation of its GI Genius(TM) intelligent endoscopy system, covering more...
- [Toyota Motor stock heads into the open after a 1.23 percent drop.](https://www.ad-hoc-news.de/boerse/news/corporate-news/toyota-motor-stock-heads-into-the-open-after-a-1-23-percent-drop/70141600)  
  <sub>AD HOC NEWS, 10 hours ago</sub>  
  TM, US8923313071. Toyota Motor stock heads into the open after a 1.23 percent drop. Published on 09/21/2026 at 07:03 | Editorial responsibility: Rafael...
- [Indian Stock Market News, Equity Market and Sensex Today in India](https://www.equitymaster.com/tm/tm.asp?date=9/21/2026&title=GPT-Infra-Bags-Major-Railway-Infrastructure-Order--Oil-India-Plans-Major-Deepwater-Exploration-Push--Top-Buzzing-Stocks-Today)  
  <sub>Equitymaster, 15 hours ago</sub>  
  Top cues to track in today's stock market session.
- [Sensex Today Trades Higher | Nifty Above 23,350 | Sun Pharma & HCL Tech Top Gainers](https://www.equitymaster.com/indian-share-markets/09/21/2026/Sensex-Today-Trades-Higher--Nifty-Above-23350--Sun-Pharma--HCL-Tech-Top-Gainers?utm_source=todays-market-plug&utm_medium=website&utm_campaign=content&utm_content=TM)  
  <sub>Equitymaster, 11 hours ago</sub>  
  Asian equities edged higher on Monday, helped by gains in semiconductor stocks as demand related to artificial intelligence continued to support the...
- [GCash IPO expanding MSME reach](https://tribune.net.ph/2026/09/20/gcash-ipo-expanding-msme-reach)  
  <sub>Daily Tribune, 24 hours ago</sub>  
  The DTI says wider digital payment adoption can help MSMEs expand into e-commerce and reach customers beyond local markets, as GCash parent Mynt prepares...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 192.73 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 194.57 (-0.9%), 50d 189.05 (+1.9%), 200d 202.02 (-4.6%); 50d below 200d
Momentum: RSI(14) 50.0 | MACD 1.043 vs signal 1.831 (histogram -0.788)
Returns: 1d +0.6% | 5d -2.4% | 1m +0.3% | 3m +13.6%
52-week range: 166.50 - 248.29 (now 32.1% of the way up)
Volatility: ATR(14) 3.35 (1.7% of price) | annualised 20d 21.2%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.45</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 228.23B
Valuation: trailing P/E 8.56 | forward P/E 12.21 | P/B 15.67 | PEG n/a
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

```text
Consensus: strong_buy (mean 1.50 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 2 strong buy, 2 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 234.08 (+21.5% vs last close), range 230.00 - 239.31
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 757,877 shares
Distinct insiders: 0 buying, 0 selling
(1 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Exxon Mobil (XOM) · Company — NEUTRAL, confidence 0.35

**In the model's own words:**

> XOM is caught between conflicting signals that prevent a directional conviction. The recent price action shows weakness (-2.7% in 1d, -3.6% in 5d) despite a strong 3-month gain (+14.9%), and technicals display early deterioration: RSI at 45.8 is neutral, MACD histogram turned negative, and volume is only 21% of the 20-day average, suggesting weak conviction behind the sell-off. The stock trades 24-27% above intrinsic value per multiple valuation frameworks and carries a trailing P/E of 20.47, which is elevated relative to a forward P/E of 14.74 and PEG of 1.40. Fundamentally, earnings have been mixed (2 beats, 2 in-line over last 4 quarters), and the next earnings date is 39 days away, leaving limited near-term catalyst clarity. The analyst consensus is constructive (buy rating, +7.4% target), but recent rating changes show mixed sentiment: two neutral/downgrade moves (Piper Sandler, Bank of America) offset by maintains of Overweight/Buy from MS, Barclays, and TD Cowen. The Venezuela re-entry story is speculative and multi-year. Insider buying was net positive over 180 days (+6.9M shares) but lacked attribution to specific named executives. The news is largely sector-neutral roundups and valuation commentary rather than ticker-specific catalysts. With technicals showing signs of momentum fade, valuation stretched, earnings record uneven, and no material near-term trigger, the risk-reward does not favor a directional bet at this moment.

**Main reasons it gave:**
- Recent 1d and 5d price weakness with below-average volume suggests fading momentum
- Valuation 24-27% above fair value on GuruFocus and 20.5x trailing P/E relative to forward 14.7x
- Earnings record mixed (2 beats, 2 in-line) with next catalyst 39 days away
- Analyst consensus constructive but recent downgrades (BofA, Piper Sandler) offset maintains
- No material ticker-specific catalyst in past 24 hours; Venezuela story is long-dated and preliminary

<details><summary><b>News</b> — score +0.00</summary>

- [Monday's session: gap up and gap down stock in the S&P500 index](https://www.chartmill.com/news/DOW/Chartmill-55111-Mondays-session-gap-up-and-gap-down-stock-in-the-SP500-index)  
  <sub>ChartMill, 35 minutes ago</sub>  
  Wondering which stocks are making significant price gaps? Explore the S&P500 index on Monday to find the gap up and gap down stocks in today's session.
- [XOM Looks 24.0% Overvalued on GF Value™ as Dividend Sustainabili](https://www.gurufocus.com/news/9090097/xom-looks-240-overvalued-on-gf-value-as-dividend-sustainability-faces-mixed-signals)  
  <sub>GuruFocus, 5 minutes ago</sub>  
  On September 21, 2026, ExxonMobil Holdings Corp (NYSE: XOM) experienced a notable decline in its stock price, slipping by $3.94 to around $159.59.
- [Zacks Market Edge Highlights: ExxonMobil, JPMorgan Chase and NVIDIA](https://www.tradingview.com/news/zacks:84adcc7ce094b:0-zacks-market-edge-highlights-exxonmobil-jpmorgan-chase-and-nvidia/)  
  <sub>TradingView, 2 hours ago</sub>  
  For Immediate ReleaseChicago, IL – September 21, 2026 – Zacks Market Edge is a podcast hosted weekly by Zacks Stock Strategist Tracey Ryniec.
- [XOM: Volume Growth Still Matters, Free Cash Flow Discipline Now Carries The Case](https://simplywall.st/community/narratives/us/energy/nyse-xom/exxonmobil-holdings/6q89hkau-xom-future-dividend-strength-and-global-projects-will-balance-sector-risks/updates/28-the-thesis-on-exxonmobil-has-been-reviewed-and-reaffirmed-t)  
  <sub>Simply Wall Street, 2 hours ago</sub>  
  The thesis on ExxonMobil has been reviewed and reaffirmed. The updated view places more weight on recent evidence of capital discipline, cost savings and...
- [Why Are BATL, TPET, XOM, CVX, USO, UCO Stocks Rising Overnight?](https://stocktwits.com/news-articles/markets/equity/why-are-batl-tpet-xom-cvx-uso-uco-stocks-rising-overnight/cZZLqW1R7Mp)  
  <sub>Stocktwits, 18 hours ago</sub>  
  BATL, TPET, USO, UCO Stocks: Retail Sentiment. On Stocktwits, retail sentiment around BATL stock slipped from 'extremely bullish' to 'bullish' over 24 hours...
- [Exxon (XOM) Eyes a Return to Venezuela After Nearly Two Decades Away](https://finance.yahoo.com/energy/articles/exxon-xom-eyes-return-venezuela-164059135.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  A Wall Street Journal report on September 16 revealed that ExxonMobil Holdings Corporation (NYSE:XOM) is nearing a preliminary agreement with Venezuela's...
- [3 Inflated Stocks We Think Twice About](https://www.theglobeandmail.com/investing/markets/stocks/XOM/pressreleases/4706590/3-inflated-stocks-we-think-twice-about/)  
  <sub>The Globe and Mail, 11 hours ago</sub>  
  Detailed price information for Exxonmobil Holdings Corp (XOM-N) from The Globe and Mail including charting and trades.
- [Xometry stock rating reiterated at Citizens on durable growth outlook By Investing.com](https://uk.investing.com/news/stock-market-news/xometry-stock-rating-reiterated-at-citizens-on-durable-growth-outlook-93CH-4875988)  
  <sub>Investing.com, 3 hours ago</sub>  
  Investing.com - Citizens reiterated a Market Outperform rating and $120 price target on Xometry Inc (NASDAQ:XMTR) stock following investor meetings in...
- [XOM Looks 27.3% Overvalued on GF Value™ Amid Dividend Sustainabi](https://www.gurufocus.com/news/9089749/xom-looks-273-overvalued-on-gf-value-amid-dividend-sustainability-focus)  
  <sub>GuruFocus, 2 hours ago</sub>  
  On September 21, 2026, RBC Capital analyst Biraj Borkhataria reaffirmed a Sector Perform rating and a $180 price target for ExxonMobil Holdings Corp (NYSE:...
- [HOST News & Events](https://intellectia.ai/stock/HOST/news)  
  <sub>Intellectia AI, 5 hours ago</sub>  
  Latest HOST stock news: earnings reports, major events, and real-time price action alerts. Daily updates on everything moving HOST stock.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 159.12 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 162.36 (-2.0%), 50d 158.19 (+0.6%), 200d 147.12 (+8.2%); 50d above 200d
Momentum: RSI(14) 45.8 | MACD 1.419 vs signal 2.046 (histogram -0.627)
Returns: 1d -2.7% | 5d -3.6% | 1m -4.2% | 3m +14.9%
52-week range: 110.64 - 171.47 (now 79.7% of the way up)
Volatility: ATR(14) 3.76 (2.4% of price) | annualised 20d 27.6%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 654.14B
Valuation: trailing P/E 20.47 | forward P/E 14.74 | P/B 2.52 | PEG 1.40
Profitability: profit margin 9.1% | operating margin 15.9% | ROE 12.6%
Growth (YoY): revenue +44.1% | earnings +112.8%
Balance sheet: debt/equity 15.9% | free cash flow 20.67B
Risk: beta 0.17 | short interest 1.1% of float
Next earnings: 2026-10-30
```

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.15</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-06-30 in line | 2026-03-31 beat by 14% | 2025-12-31 in line | 2025-09-30 beat by 2%
```

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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.15</summary>

```text
Last 180 days: bought 10,818,651 shares in 251 transaction(s) | sold 3,904,152 shares in 49
Net: +6,914,499 shares (-194.8% of insider holdings) | insiders hold 3,371,767 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.15</summary>

_Not available today._

</details>

### Alphabet (Google) (GOOGL) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Alphabet Stock Surges as Google Search Makes a Major Comeback](https://finance.yahoo.com/markets/stocks/articles/alphabet-stock-surges-google-search-122833154.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  This article first appeared on GuruFocus. Alphabet (GOOGL, Financials) shares were higher in Friday's premarket, after Evercore boosted its price target on...
- [What's Going On With Alphabet Stock Today?](https://www.benzinga.com/trading-ideas/movers/26/09/61897638/whats-going-on-with-alphabet-stock-today-2)  
  <sub>Benzinga, 47 minutes ago</sub>  
  Alphabet Inc. (NASDAQ:GOOG) shares are moving higher. The company unveiled Googlebook, a new line of Android-based laptops built for deep integration with...
- [Alphabet (GOOGL) Stock Price Forecast 2026: Cloud Hit $20B But FCF Collapsed — Buy or Short?](https://www.tradingkey.com/analysis/stocks/us-stocks/262008961-alphabet-googl-stock-price-forecast-2026-google-cloud-tradingkey)  
  <sub>TradingKey, 14 hours ago</sub>  
  The main reason the market is selling Alphabet stock down is the increased $190 billion 2026 capex guidance which has dropped Free Cash Flow margin down from 21...
- [This Energy Storage Stock Jumps on Deal to Power Google Data Centers](https://www.barrons.com/articles/eos-energy-stock-google-alphabet-3b0aaf6d)  
  <sub>Barron's, 5 hours ago</sub>  
  This Energy Storage Stock Jumps on Deal to Power Google Data Centers ... Eos Energy Enterprises will supply Alphabet-owned Google with zinc-based data-center...
- [The Tech Selloff Is Only Strengthening My Belief In Alphabet](https://247wallst.com/investing/2026/09/21/the-tech-selloff-is-only-strengthening-my-belief-in-alphabet/)  
  <sub>24/7 Wall St., 4 hours ago</sub>  
  While most investors flee the tech selloff, one mega cap keeps pulling more capital in the opposite direction, and the reasoning has nothing to do with...
- [Google fined €403M by Irish regulatory board for privacy violations (GOOG:NASDAQ)](https://seekingalpha.com/news/4644713-google-fined-403m-by-irish-regulatory-board-for-privacy-violations)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Ireland's DPC fines Google €403M for GDPR location-data violations (2018–2020).
- [GOOG vs GOOGL - which Alphabet share class should you buy?](https://finance.yahoo.com/markets/stocks/articles/goog-vs-googl-alphabet-share-102934940.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  If you're thinking of buying shares in Google's parent company Alphabet, you might be confused as to why there are two symbols to choose from.
- [Garmin Stock Rises Overnight: Can Its $200 Whoop And Google Fitbit Challenger Get Investors’ Hearts Racing Again?](https://stocktwits.com/news-articles/markets/equity/garmin-stock-rises-overnight-can-its-200-whoop-and-google-fitbit-challenger-get-investors-hearts-racing-again/cZZmJxPR7wj)  
  <sub>Stocktwits, 9 hours ago</sub>  
  Benchmark raised its AMC price target to $3 from $2.50 and kept a Buy rating after the company's Q2 results beat expectations. The firm said AMC's revenue and...
- [Is GOOGL Overvalued? DCF Says Worth $316](https://www.gurufocus.com/news/9089580/is-googl-overvalued-dcf-says-worth-316)  
  <sub>GuruFocus, 4 hours ago</sub>  
  On September 21, 2026, we conducted a discounted cash flow (DCF) analysis for Alphabet Inc (GOOGL), a company that has shown strong price performance over...
- [Alphabet's strong AI-driven growth and solid fi...](https://pluang.com/en/news-feed/keyakinan-alphabet-menguat-di-tengah-penjualan-teknologi)  
  <sub>Pluang, 4 hours ago</sub>  
  Despite a broad tech selloff, Alphabet continues to attract investment due to its strong financial performance and leadership in AI technology.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 354.67 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 342.28 (+3.6%), 50d 345.53 (+2.6%), 200d 337.69 (+5.0%); 50d above 200d
Momentum: RSI(14) 58.6 | MACD 0.613 vs signal -1.370 (histogram 1.983)
Returns: 1d +1.5% | 5d +1.5% | 1m +4.1% | 3m +1.4%
52-week range: 236.57 - 402.62 (now 71.1% of the way up)
Volatility: ATR(14) 8.41 (2.4% of price) | annualised 20d 23.4%
Volume: 0.39x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 4.34T
Valuation: trailing P/E 17.80 | forward P/E 23.83 | P/B 6.97 | PEG 1.27
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
Price target: mean 428.16 (+20.7% vs last close), range 340.00 - 515.00
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

- [Novo Nordisk Falls 7% as Post-Wegovy Growth Plan Fails to Ease Competition Fears; Eli Lilly Slips, Viking Therapeutics Edges Higher](https://finance.yahoo.com/healthcare/articles/novo-nordisk-falls-7-post-134522608.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  Novo Nordisk took the stage at its own capital markets day and said something that sent its stock tumbling 7%, yet its closest rivals barely flinched.
- [Nvidia vs. Eli Lilly: I’d Choose This Stock for the Next Decade](https://247wallst.com/investing/2026/09/21/nvidia-vs-eli-lilly-id-choose-this-stock-for-the-next-decade/)  
  <sub>24/7 Wall St., 39 minutes ago</sub>  
  NVDA posted 106% revenue growth to $96B last quarter while LLY grew 48% to $23B, yet NVIDIA trades at just 23x forward earnings against a 60% operating...
- [Eli Lilly Vs. Novo Nordisk Stock: Temporarily Cheap Or Correctly Cheap? (NYSE:LLY)](https://seekingalpha.com/article/4948208-eli-lilly-vs-novo-nordisk-temporarily-cheap-or-correctly-cheap)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  Eli Lilly demonstrates superior operating momentum, while Novo Nordisk offers lower expectations and higher cash returns. Learn why LLY and NVO are rated...
- [5 Stocks In The Spotlight Last Week: Wall Street's Most Accurate Analysts Weigh In](https://www.benzinga.com/analyst-stock-ratings/price-target/26/09/61888771/5-stocks-in-the-spotlight-last-week-wall-streets-most-accurate-analysts-weigh-in-12)  
  <sub>Benzinga, 6 hours ago</sub>  
  U.S. stocks ended mixed; the Dow had its worst week since March. Benzinga highlights top picks from five accurate analysts, including ON, AXSM and LLY.
- [Novo Nordisk Stock Drops 5.6% as 2030 Goals Match Peers](https://www.tradingview.com/news/gurufocus:f13861ee9094b:0-novo-nordisk-stock-drops-5-6-as-2030-goals-match-peers/)  
  <sub>TradingView, 3 hours ago</sub>  
  Novo Nordisk A/S NYSE:NVO shares fell 5.96% in Copenhagen trading, as the Danish drugmaker used its London Capital Markets Day to lay out 2030 strategic...
- [Novo Nordisk A/S Stock (NVO) Moved Down by 7.86% on Sep 21: A Full Analysis](https://www.tradingkey.com/news/market-movers/262178564-market-movers-nvo-20260921)  
  <sub>TradingKey, 53 minutes ago</sub>  
  Novo Nordisk faced downward pressure after its Capital Markets Day strategic update.Eli Lilly competition and patent expirations raised concerns over market...
- [Novo Nordisk says CagriSema bests Eli Lilly's Zepbound (NVO:NYSE)](https://seekingalpha.com/news/4644774-novo-nordisk-says-cagrisema-bests-eli-lilly-zepbound)  
  <sub>Seeking Alpha, 38 minutes ago</sub>  
  Novo Nordisk's CagriSema beats Lilly's Zepbound in phase 3 obesity/diabetes trials, with greater weight loss and similar HbA1c reduction. Read more here.
- [Eli Lilly and Company (LLY) Price: Live Chart & Market Cap](https://cryptorank.io/rwa/stocks/eli-lilly-and)  
  <sub>CryptoRank, 16 hours ago</sub>  
  Track Eli Lilly and Company (LLY), a tokenized asset in the "Stocks" category — compare its token price to the real one, and follow market cap and trading...
- [PLTR Stock Heads for Worst Month Ever: Retail Awaits Dip Below $100, Michael Burry Takes Victory Lap](https://stocktwits.com/news-articles/markets/equity/pltr-stock-heads-for-worst-month-ever-retail-awaits-dip-below-100-michael-burry-takes-victory-lap/cZKUD9QR7O0)  
  <sub>Stocktwits, 18 hours ago</sub>  
  Despite strong financial growth, Palantir's shares have retreated amid an increasingly negative sentiment for software stocks.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,165.36 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 1,158.81 (+0.6%), 50d 1,176.90 (-1.0%), 200d 1,066.94 (+9.2%); 50d above 200d
Momentum: RSI(14) 51.1 | MACD -11.262 vs signal -13.053 (histogram 1.791)
Returns: 1d +1.1% | 5d +2.4% | 1m -6.4% | 3m +5.7%
52-week range: 714.59 - 1,280.34 (now 79.7% of the way up)
Volatility: ATR(14) 29.80 (2.6% of price) | annualised 20d 19.5%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.04T
Valuation: trailing P/E 39.17 | forward P/E 24.61 | P/B 30.67 | PEG 1.14
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
Price target: mean 1,325.39 (+13.7% vs last close), range 930.00 - 1,600.00
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

### Nvidia (NVDA) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Jensen Huang Just Delivered Incredible News for Nvidia Stock Investors](https://www.fool.com/investing/2026/09/21/jensen-huang-incredible-news-nvidia-stock-investor/)  
  <sub>The Motley Fool, 1 hour ago</sub>  
  Nvidia (NVDA +1.34%) supplies the world's best graphics processing units (GPUs) for data centers, which are the primary chips used in artificial...
- [Wall Street Analysts Think Nvidia (NVDA) Is a Good Investment: Is It?](https://finance.yahoo.com/markets/stocks/articles/wall-street-analysts-think-nvidia-133003752.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Investors often turn to recommendations made by Wall Street analysts before making a Buy, Sell, or Hold decision about a stock. While media reports about...
- [Wall Street Analysts See a 46.61% Upside in Nvidia (NVDA): Can the Stock Really Move This High?](https://www.zacks.com/stock/news/2992946/wall-street-analysts-see-a-4661-upside-in-nvidia-nvda-can-the-stock-really-move-this-high)  
  <sub>Zacks Investment Research, 2 hours ago</sub>  
  Shares of Nvidia ( NVDA Quick Quote NVDA - Free Report) have gained 3.5% over the past four weeks to close the last trading session at $222.27,...
- [Nvidia Stock: Are Trump Talks With China's Xi the AI Chips Catalyst It Needs?](https://www.barrons.com/articles/nvidia-stock-price-trump-china-xi-ai-chips-3828556a)  
  <sub>Barron's, 1 hour ago</sub>  
  is looking for something to fuel its latest assault on new share-price highs. This week's summit between President Donald Trump and Chinese leader Xi...
- [NVDA Stock In Focus As Huawei Announces 2 Advanced AI Chips For 2027](https://stocktwits.com/news-articles/markets/equity/nvda-stock-in-focus-as-huawei-announces-2-advanced-ai-chips-for-2027/cZtr0EKRB5h)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Huawei will launch the 960DT in Q1 2027 and Ascend 960PR in Q3 as it expands its AI chip lineup. Its UnifiedBus technology is designed to connect many...
- [NVDA Looks 43.3% Undervalued on GF Value™](https://www.gurufocus.com/news/9089993/nvda-looks-433-undervalued-on-gf-value)  
  <sub>GuruFocus, 1 hour ago</sub>  
  On September 21, 2026, Nvidia's CEO Jensen Huang addressed concerns about artificial intelligence risks, dismissing fears of an AI apocalypse as exaggerated...
- [Einride Taps Nvidia To Power Autonomous Trucking Push - Targets Up To 2,000 Vehicles By 2028](https://www.tradingview.com/news/stocktwits:24108e9aa094b:0-einride-taps-nvidia-to-power-autonomous-trucking-push-targets-up-to-2-000-vehicles-by-2028/)  
  <sub>TradingView, 2 hours ago</sub>  
  Shares of Einride (ENRD) rose around 7% in pre-market trading after the freight operator announced a tie-up with Nvidia (NVDA) to expand its autonomous...
- [I Keep Buying Nvidia Over and Over Despite China Concerns, Despite The Tech Selloff](https://247wallst.com/investing/2026/09/21/i-keep-buying-nvidia-over-and-over-despite-china-concerns-despite-the-tech-selloff/)  
  <sub>24/7 Wall St., 3 hours ago</sub>  
  China headlines, a tech selloff, and a $279 billion supply commitment that could go sideways if AI demand fades: here is why one investor keeps adding to...
- [Nvidia vs. Eli Lilly: I’d Choose This Stock for the Next Decade](https://www.aol.com/articles/nvidia-vs-eli-lilly-d-143010000.html)  
  <sub>AOL.com, 38 minutes ago</sub>  
  NVIDIA (NASDAQ: NVDA) and Eli Lilly (NYSE: LLY) just posted quarters that showcase two of the most powerful growth engines in the market.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 225.32 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 219.41 (+2.7%), 50d 214.56 (+5.0%), 200d 198.60 (+13.5%); 50d above 200d
Momentum: RSI(14) 56.7 | MACD 1.257 vs signal 1.466 (histogram -0.209)
Returns: 1d +1.4% | 5d +6.8% | 1m +3.9% | 3m +8.0%
52-week range: 165.17 - 235.74 (now 85.2% of the way up)
Volatility: ATR(14) 6.25 (2.8% of price) | annualised 20d 46.5%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 5.44T
Valuation: trailing P/E 28.49 | forward P/E 14.37 | P/B 23.76 | PEG 0.47
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
Consensus: strong_buy (mean 1.31 on a 1=strong buy to 5=strong sell scale, 59 analysts)
Ratings: 11 strong buy, 48 buy, 2 hold, 1 sell, 0 strong sell
Price target: mean 327.70 (+45.4% vs last close), range 180.00 - 515.00
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
Net: -2,570,722 shares (-0.3% of insider holdings) | insiders hold 965,928,000 shares
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

### Teva Pharmaceutical (TEVA) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Teva (NYSE: TEVA) legal chief files $273K share-sale notice](https://www.stocktitan.net/sec-filings/TEVA/144-teva-pharmaceutical-industries-ltd-sec-filing-8b18ba7d8013.html)  
  <sub>Stock Titan, 4 hours ago</sub>  
  Rule 144 filing shows CLO Brian Savage may sell up to 7028 Teva shares worth $273062 through Citigroup Global Markets on the NYSE from awards and options.
- [Medincell's Partner Teva Presented New Data on Investigational Olanzapine LAI and UZEDY® at Psych Congress 2026](https://www.biospace.com/press-releases/medincells-partner-teva-presented-new-data-on-investigational-olanzapine-lai-and-uzedy-at-psych-congress-2026)  
  <sub>BioSpace, 5 hours ago</sub>  
  New Phase 3 analyses of Olanzapine LAI, currently under regulatory review, provided further insights into stabilization, long-term efficacy and...
- [Nykredit A S Takes Position in Teva Pharmaceutical Industries Ltd. $TEVA](https://www.marketbeat.com/instant-alerts/filing-nykredit-a-s-takes-position-in-teva-pharmaceutical-industries-ltd-teva-2026-09-21/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Nykredit A S bought a new stake in shares of Teva Pharmaceutical Industries Ltd. (NYSE:TEVA - Free Report) during the second quarter, according to the...
- [Daily US Equity Opening News: Anthropic shifts potential IPO to November; PSKY in talks with California over production concession](https://www.newsquawk.com/headlines/daily-us-equity-opening-news-anthropic-shifts-potential-ipo-to-november-psky-in-talks-with-california-over-production-concession)  
  <sub>Newsquawk, 2 hours ago</sub>  
  DAY AHEAD: US INDEX FUTURES: ES +0.6%, NQ +1.1%, YM +0.9%, RUT +0.8% BROKER MOVES: CIEN upgraded at Evercore; INVH & AMH upgraded at Mizuho.
- [Medincell: Teva unveils new data on its olanzapine, FDA decision expected end of 2026](https://www.ideal-investisseur.fr/en/stock-news/medincell-teva-unveils-new-data-on-its-olanzapine-fda-decision-expected-end-of-2026/25427.html)  
  <sub>Idéal Investisseur, 9 hours ago</sub>  
  Teva, Medincell's partner, presented new clinical and real-world data on two treatments based on the BEPO technology of the Montpellier-based...
- [Teva Pharmaceutical Industries stock gains on NYSE listing milestone](https://www.ad-hoc-news.de/boerse/news/nebenwerte/teva-pharmaceutical-industries-stock-gains-on-nyse-listing-milestone/70139441)  
  <sub>AD HOC NEWS, 21 hours ago</sub>  
  Teva Pharmaceutical Industries stock closed at USD 38.98 on September 18, 2026, marking a 36.25 percent gain since the start of the year.
- [Aurobindo Pharma to host JP Morgan analyst meet in Hyderabad on Sep 24](https://scanx.trade/stock-market-news/companies/aurobindo-pharma-host-jp-morgan-analyst-meet-hyderabad-sep-24/51533363)  
  <sub>scanx.trade, 4 hours ago</sub>  
  Aurobindo Pharma officials to meet investors on September 24, 2026. Session is part of JP Morgan Healthcare Trip - Hyderabad. Group meeting scheduled for...
- [MedinCell’s BEPO Platform Gains Momentum as Teva Unveils Strong Data for Long-Acting Antipsychotics](https://www.tipranks.com/news/company-announcements/medincells-bepo-platform-gains-momentum-as-teva-unveils-strong-data-for-long-acting-antipsychotics)  
  <sub>TipRanks, 8 hours ago</sub>  
  An update from MedinCell SA ( ($FR:MEDCL) ) is now available. New data presented by Teva at Psych Congress 2026 highlight the performance of two long-acting...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 39.24 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 37.53 (+4.5%), 50d 35.48 (+10.6%), 200d 33.21 (+18.2%); 50d above 200d
Momentum: RSI(14) 63.4 | MACD 0.886 vs signal 0.747 (histogram 0.139)
Returns: 1d +0.7% | 5d +1.3% | 1m +6.6% | 3m +21.9%
52-week range: 18.34 - 39.25 (now 100.0% of the way up)
Volatility: ATR(14) 1.13 (2.9% of price) | annualised 20d 31.8%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 45.77B
Valuation: trailing P/E 65.40 | forward P/E 12.68 | P/B 5.90 | PEG 0.72
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
Consensus: strong_buy (mean 1.50 on a 1=strong buy to 5=strong sell scale, 1 analysts)
Ratings: 1 strong buy, 1 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 42.00 (+7.0% vs last close), range 42.00 - 42.00
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

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.35

**In the model's own words:**

> DBC is a broad commodities fund dominated by short-term bonds (41% in short-term Treasuries and government bonds) with meaningful energy exposure (9% Brent crude futures). The technical picture is mixed: the fund is near the top of its 52-week range (90.7%) with a 17.5% gain above the 200-day moving average, suggesting momentum, but momentum indicators are losing steam (RSI 58.8 is overbought territory, MACD histogram negative). Volume is light at 0.2x average, which weakens conviction in the current price level. The macro backdrop offers no clear tailwind: short-end Treasury yields have moved slightly higher this week, and the dollar has strengthened (+0.90), both headwinds for commodity prices. The VIX is calm at 14.62, removing volatility support. Energy inventories show a crude oil draw (bullish signal) but at only the 38th percentile, meaning levels are not tight; natural gas built at a high 71st percentile, a bearish signal. The EIA price outlook calls for WTI to fall ~10% over six months to $79, a clear headwind for this fund's energy holdings, while natural gas is forecast modestly higher. The 3-year record of +13.8% annualized reflects a strong commodity cycle, but near-term catalysts do not support extension. No analyst coverage exists for a commodity fund. Fund flows data is too sparse to read conviction. The case for staying neutral rather than bearish rests on the technical strength visible in the trend structure and the real crude draw, which offer modest support, but these are outweighed by overbought momentum, light volume, near-term EIA price forecasts showing weakness, and the lack of near-term macro catalysts.

**Main reasons it gave:**
- MACD histogram negative and RSI overbought at 58.8 despite proximity to 52-week high
- Light volume of 0.2x average weakens conviction in current price level
- EIA crude forecast down ~10% to $79 over six months versus current ~$88
- Dollar strength and short-end Treasury yield rise headwinds for commodities
- Crude draw bullish but at only 38th percentile of annual range; natural gas build at 71st percentile

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.25</summary>

```text
Last close 32.60 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 32.16 (+1.4%), 50d 30.57 (+6.6%), 200d 27.74 (+17.5%); 50d above 200d
Momentum: RSI(14) 58.8 | MACD 0.784 vs signal 0.837 (histogram -0.053)
Returns: 1d -1.0% | 5d -1.7% | 1m +4.8% | 3m +18.9%
52-week range: 22.07 - 33.68 (now 90.7% of the way up)
Volatility: ATR(14) 0.47 (1.5% of price) | annualised 20d 19.7%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.25</summary>

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

<details><summary><b>Does this company beat its own forecasts</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.25</summary>

```text
US inventories, week ending 2026-09-11 (published the following Wednesday)
  Crude oil: 423.4 million barrels, -0.6 on the week (a draw), 38% percentile over 52 weeks
  Natural gas: 3,298.0 billion cubic feet, +44.0 on the week (a build), 71% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.25</summary>

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
Shares outstanding: 54.03M | fund size: 1.76B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Farm goods basket (DBA) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> DBA is a commodity-focused fund with an unusual composition: 51.8% Other (likely agricultural commodities given the ticker), 46.2% Cash, and only 2% Bonds. The technicals show a fund near the top of its 52-week range (77.5%), trading slightly below its 20-day SMA while holding above both the 50-day and 200-day SMAs. Momentum is neutral (RSI 49.6, MACD histogram negative at -0.125), suggesting no decisive directional push. The macro backdrop is stable: yields are flat to slightly higher across the curve, the dollar strengthened 0.90 on the week, and the VIX remains calm at 14.62. Inflation data at 3.4% is above the market's 2.3% ten-year expectation, which could support commodities over time, but this week's yield moves have been minimal. The one-day return of +1.5% is noise against the fund's low volatility (1.1% ATR). Volume is well below average (0.27x), indicating thin conviction either way. The fund's sector mix and large cash position (46.2%) suggest either hedging or recent inflows that have not yet been deployed, but fund flows data is insufficient to read. The news mention of agribusiness as a long-term theme is thematic rather than a catalyst for this cycle. Without a clear rate surprise, commodity price breakout, or flow reversal, the case for a directional tilt is absent. The fund sits at equilibrium: near range highs but on soft momentum, in a stable macro environment with no fresh catalyst.

**Main reasons it gave:**
- Price near 52-week highs (77.5%) with below-average volume
- RSI at midpoint (49.6) and MACD histogram negative (no momentum confirmation)
- Macro backdrop stable: minimal yield moves, calm VIX, no inflation surprise this week
- Large cash position (46.2%) and thin analyst coverage suggest no imminent reallocation

<details><summary><b>News</b> — score +0.00</summary>

- [Market Musings 200926: Watch Micron for clues on Tech direction](https://www.stockopedia.com/content/market-musings-200926-watch-micron-for-clues-on-tech-direction-1057681/)  
  <sub>Stockopedia, 23 hours ago</sub>  
  Agribusiness is emerging as one of the most compelling long-term investment themes within the real economy. Spanning the entire agricultural value chain,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 28.58 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 28.87 (-1.0%), 50d 28.26 (+1.1%), 200d 27.05 (+5.6%); 50d above 200d
Momentum: RSI(14) 49.6 | MACD 0.103 vs signal 0.228 (histogram -0.125)
Returns: 1d +1.5% | 5d -1.3% | 1m +0.7% | 3m +7.2%
52-week range: 25.44 - 29.49 (now 77.5% of the way up)
Volatility: ATR(14) 0.31 (1.1% of price) | annualised 20d 14.1%
Volume: 0.27x the 20-day average
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
Shares outstanding: 27.60M | fund size: 788.81M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> HYG is trading below all major moving averages (20d, 50d, 200d) with a downward trend of -1.7% versus the 200-day MA. Momentum is weak: RSI at 40.1 sits in weak territory, and MACD remains negative with the histogram still underwater. Returns over 1m (-1.1%) and 3m (-1.6%) are negative. Volume is depressed at 0.37x the 20-day average, suggesting limited conviction in either direction. On the macro side, the backdrop is benign: the yield curve remains normally upsloped at +0.98, the VIX is calm at 14.62 (down 2.5 on the week), and the dollar's recent strength (+0.90) may support credit positioning. Treasury yields moved modestly, with the 3-month rising 5bps but longer rates stable, consistent with a slow-hiking scenario already priced into the 2-year at 4.67%. Fund basics show solid fundamentals for high-yield: 5.9% yield, predominantly BB-rated credit (57.9%), and a three-year track record of +7.9% annually. However, no macro surprise or technical catalyst has emerged to justify a directional move. The technical setup—below all MAs, weak momentum, low volume, positioned in the lower half of the 52-week range—argues for patience rather than entry. Absence of recent news and flow data further limits conviction. This is a hold-steady cycle for the fund.

**Main reasons it gave:**
- Price below all major moving averages with downward trend of -1.7% vs 200d MA
- Weak momentum: RSI 40.1, negative MACD, depressed volume at 0.37x average
- Benign macro backdrop: yield curve normal, VIX calm, no rate surprise
- 5.9% yield on BB-heavy credit quality supports fundamental value but insufficient to overcome technical weakness
- No macro catalyst or flow conviction to trigger directional move

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 78.70 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 79.11 (-0.5%), 50d 79.37 (-0.8%), 200d 80.02 (-1.7%); 50d below 200d
Momentum: RSI(14) 40.1 | MACD -0.277 vs signal -0.236 (histogram -0.041)
Returns: 1d +0.2% | 5d +0.2% | 1m -1.1% | 3m -1.6%
52-week range: 78.38 - 81.32 (now 10.9% of the way up)
Volatility: ATR(14) 0.23 (0.3% of price) | annualised 20d 4.3%
Volume: 0.37x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

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
Shares outstanding: 206.31M | fund size: 16.24B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> IWM sits below its 20-, 50-, and 200-day moving averages with weak momentum (RSI 38.4, MACD deeply negative) despite holding above the 200-day line on a longer view. The macro backdrop is mixed: Treasury yields have stabilized with the curve normalized at +0.98, the Fed's 25bp hike landed softer than feared, and the dollar strengthened +0.90 on the week while the VIX compressed to 14.62. Valuations remain reasonable at P/E 17.30 and P/B 2.13. However, small-cap positioning shows large speculators net short 19.6% with a +6.0% weekly increase in short crowding—a shift toward bearishness, though still only at the 30th percentile historically so not extreme. The analyst view is extremely thin (1.7% coverage), with the five largest holdings all rated buy at +22.1% targets, but this offers little signal on the 98.3% of the fund not represented. Volume is low at 0.25x the 20-day average, suggesting conviction is absent on both sides. The fund's three-year returns of +17.4% annually with beta 1.24 show resilience, but near-term technicals are soft and macro data (unemployment 4.1%, claims 196k, inflation 3.4%) does not yet suggest a catalyst for re-acceleration in small caps. The one positive: rates appear to have found a ceiling, which could eventually support equities, but this has not yet translated to price action or positioning conviction.

**Main reasons it gave:**
- RSI 38.4 with MACD deeply negative; price below 20d, 50d SMA
- Large speculator positioning net short and increasing week-over-week
- Fed hike landed soft, curve normalized, rates appear to have stabilized at ceiling
- Analyst coverage extremely thin at 1.7% of fund; targets of +22% on largest holdings do not represent 98% of basket
- Low volume at 0.25x 20-day average indicates absence of conviction on either side

<details><summary><b>News</b> — score +0.00</summary>

- [Weekly Setup | Rates Find Their Ceiling. Chips Break Out, Washington Waits](https://www.moomoo.com/community/feed/weekly-setup-rates-find-their-ceiling-chips-break-out-washington-117308458991622)  
  <sub>Moomoo, 5 hours ago</sub>  
  The gift and the test arrived in the same week. The Federal Reserve's 25-basis-point hike on September 16 landed softer than feared -- markets priced ...
- [Evolution Metals Just Joined the Indexes Behind $12.2 Trillion in Invested Assets (NASDAQ: EMAT)](https://www.benzinga.com/content/61895255/evolution-metals-just-joined-indexes-behind-12-2-trillion-invested-assets-nasdaq-emat)  
  <sub>Benzinga, 2 hours ago</sub>  
  WSW, NY, September 21st, 2026, FinanceWireToday, Evolution Metals & Technologies Corp. (NASDAQ:EMAT) joined the Russell 3000 and Russell 2000 indexes.
- [The Options Weekly Ahead: Index Skew Resets, Gold Bets Build, SpaceX Vol Craters](https://www.moomoo.com/community/feed/the-options-weekly-ahead-index-skew-resets-gold-bets-build-117308120039430)  
  <sub>Moomoo, 7 hours ago</sub>  
  Last Week's Highlights Index Put Skew Snaps Back to Life. The cheapest hedges of the summer are gone. One-month put/call skew on the $S&P 500 Index (...
- [BlackRock's IBIT bitcoin spot ETF surpasses GLD in daily trading](https://www.digitaltoday.co.kr/en/view/105702/blackrock-ibit-bitcoin-spot-etf-surpasses-gld)  
  <sub>디지털투데이, 16 hours ago</sub>  
  [DigitalToday reporter Yoonseo Lee] BlackRock's bitcoin spot exchange-traded fund (ETF), the iShares Bitcoin Trust ETF 'IBIT', rose more than 5 percent in...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 285.80 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 291.78 (-2.0%), 50d 294.94 (-3.1%), 200d 275.03 (+3.9%); 50d above 200d
Momentum: RSI(14) 38.4 | MACD -3.377 vs signal -2.534 (histogram -0.843)
Returns: 1d +0.6% | 5d -0.7% | 1m -4.0% | 3m -4.2%
52-week range: 229.11 - 305.09 (now 74.6% of the way up)
Volatility: ATR(14) 3.43 (1.2% of price) | annualised 20d 11.6%
Volume: 0.25x the 20-day average
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
Three-year record: +17.4% a year | beta to the market 1.24
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 1.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.1% above the current prices
Holdings read: FROG, MOG-A, XTSLA, UMBF, GKOS
Recent rating changes among them:
  - FROG: 2026-09-04 DA Davidson: main, Buy -> Buy
  - MOG-A: 2026-09-15 Guggenheim: init, ? -> Neutral
  - UMBF: 2026-09-14 UBS: init, ? -> Neutral
  - GKOS: 2026-08-20 BTIG: main, Buy -> Buy
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
Shares outstanding: 281.05M | fund size: 80.32B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> LQD is trading below all major moving averages (20d, 50d, 200d) in a downtrend, with the 50d below the 200d signaling deteriorating momentum. RSI at 43.7 and negative MACD histogram show weakening momentum without oversold conditions that would suggest a reversal. The fund has declined 3.5% over three months and trades only 7.9% above its 52-week low, reflecting the broader headwinds in credit markets. Macro backdrop is mixed: the yield curve is normal at +0.98, the dollar strengthened 0.90 this week, and VIX fell 2.5 to 14.62 suggesting reduced stress. However, the 3-month yield moved up 5bps and the 2-year remains elevated at 4.67% against a 3.75-4.00% Fed target, indicating the bond market is not pricing imminent rate cuts. The fund's yield of 4.7% is attractive and credit quality weighted toward A-rated (46.6%) and BBB (40.2%), but there is no catalyst to reverse the technical deterioration within a single cycle. Volume is depressed at 0.22x average, which reduces confidence in any directional move. The lack of recent news, stable fund flows, and benign risk metrics prevent a bearish escalation, but the downtrend, below-average momentum, and lack of a clear macro catalyst supporting credit weakness recovery argue against conviction in a bullish reversal.

**Main reasons it gave:**
- Price below 20d, 50d, and 200d SMAs with 50d below 200d
- RSI at 43.7 and negative MACD histogram signal fading momentum
- Yield curve normal but 2-year yield at 4.67% reflects limited easing priced by bond market
- Fund yield of 4.7% on A/BBB-weighted credit quality is reasonable but provides no new catalyst
- Trading 7.9% above 52-week low with depressed volume

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 104.96 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 105.40 (-0.4%), 50d 106.07 (-1.0%), 200d 108.76 (-3.5%); 50d below 200d
Momentum: RSI(14) 43.7 | MACD -0.468 vs signal -0.477 (histogram 0.009)
Returns: 1d +0.2% | 5d +0.6% | 1m -1.0% | 3m -3.5%
52-week range: 104.28 - 112.92 (now 7.9% of the way up)
Volatility: ATR(14) 0.51 (0.5% of price) | annualised 20d 6.4%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

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
Shares outstanding: 306.91M | fund size: 32.21B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> SHY is a short-duration US government bond fund holding primarily Treasury debt. The macro backdrop shows a normalization of rate expectations: the 3-month yield rose 5bp while the 10-year was flat, the curve remains upward-sloping at +98bp (normal regime), the dollar strengthened 90bp this week on modest inflation data (3.4%), and the bond market prices roughly 75bp of Fed cuts over two years from a 4.67% two-year yield. This suggests the recent tightening cycle may have peaked, which ordinarily would support bonds. However, SHY technicals are tepid: the fund sits below its 20d, 50d and 200d moving averages, momentum (RSI 33, MACD negative) is weak, and volume is 0.12x the 20-day average—a sign of low conviction among traders. The 52-week range shows SHY near the bottom of its band, which offers optionality but no urgent catalyst. Positioning in the 2Y note is at the 95th percentile long crowding, a contrarian signal: extreme positioning is as often the end of a move as the start. The yield of 3.6% on quality collateral (100% AA US Treasuries) is fair in context, but there is no material data surprise nor a decisive technical break to justify conviction either way. The macro environment supports bonds in the absence of a rate shock, but SHY's technical weakness and crowded long positioning argue for patience. A modest bullish lean reflects improving rate-cut expectations, but low volume and extreme crowding limit the signal strength.

**Main reasons it gave:**
- Crowded long positioning at 95th percentile of 52-week crowding—reversal risk
- RSI 33 and below all major moving averages—technical weakness
- 2-year yield 4.67% vs Fed target 3.75–4.00%—bond market prices ~75bp of cuts, supporting duration
- Volume 0.12x 20-day average—low conviction trader participation

<details><summary><b>News</b> — score +0.00</summary>

- [Grayscale takes Zcash ETF to US$ 914.53 million](https://portalcripto.com.br/en/grayscale-takes-zcash-etf-to-us-914-53-million)  
  <sub>portalcripto.com.br, 17 hours ago</sub>  
  ZCSH fund is about US$ 85 million shy of US$ 1 billion and will have a 3-for-1 stock split.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 81.31 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 81.62 (-0.4%), 50d 81.81 (-0.6%), 200d 82.34 (-1.3%); 50d below 200d
Momentum: RSI(14) 33.3 | MACD -0.174 vs signal -0.140 (histogram -0.034)
Returns: 1d +0.1% | 5d -0.0% | 1m -0.9% | 3m -0.7%
52-week range: 81.24 - 83.18 (now 3.4% of the way up)
Volatility: ATR(14) 0.10 (0.1% of price) | annualised 20d 2.0%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Short Government
Yield: 3.6%
Credit quality: AA 100.0% | US government debt 99.2%
Three-year record: +4.0% a year | beta to the market 0.22
Cost and size: expense ratio 0.15% | net assets 25.91B
What it is made of: Bonds 99.2%, Cash 0.8%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.35</summary>

```text
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 29.2% of open interest (4,433,736 contracts)
Change on the week: +0.5% of open interest
Crowding: 95% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.35</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 318.97M | fund size: 25.93B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> VGK is a broadly diversified European equity fund with reasonable fundamentals (P/E 17.85, 2.8% yield) and solid three-year returns (+17.6% annually). However, multiple headwinds argue against a directional call. Technicals show the fund trading 1.7% below its 20-day moving average with RSI at 42.5 and a negative MACD histogram, suggesting mild weakness. Momentum is mixed: modest 1-day strength (+1.1%) is offset by 1-month underperformance (-3.1%). The US dollar has strengthened notably (+0.90 this week), a headwind for US-based investors in euro-denominated assets. More critically, CFTC positioning in the MSCI EAFE shows large speculators at the 95th percentile crowded long—a positioning extreme that is as often a sign of late-stage moves as early ones. The analyst view is constructive (65.7% buy, +16.6% target) but covers only 11.4% of the fund, too thin to drive conviction. Macro backdrop is stable: the yield curve is normalizing, inflation expectations remain anchored at 2.3%, and volatility is low at 14.62. No policy surprise or data shock has occurred. News flow is generic and immaterial (TradingView sector roundups, not macro or sector catalysts). The absence of recent analyst rating changes among the largest holdings and unknown fund flows provide no additional traction. This reads as a holding pattern: no catalyst sharp enough to overcome the modest technical weakness and positioning crowding.

**Main reasons it gave:**
- CFTC positioning at 95th percentile crowded long in EAFE
- USD strengthened +0.90 on week, headwind for euro exposure
- RSI 42.5 and negative MACD histogram suggest momentum loss
- Analyst view thin at 11.4% coverage of fund weight
- No macro catalyst: stable yields, anchored inflation expectations

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs Investing in Navigator Company SA Stocks](https://www.tradingview.com/symbols/LSX-895885/etfs/)  
  <sub>TradingView, 14 hours ago</sub>  
  Explore funds investing in 895885 in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in BAWAG Group AG Stocks](https://www.tradingview.com/symbols/OTC-BWAGF/etfs/)  
  <sub>TradingView, 15 hours ago</sub>  
  Explore funds investing in BWAGF in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Lakefront Biotherapeutics Stocks](https://www.google.com/goto?url=CAESagHrOzAVpkUYrEB2LRRYp7jtC7-ezeAZEEgRIMSI6AY39MhvoioDm4uFF-QNL1U0pcKdxfLP7vSVbO6bisQI19yTJcRg9jGdypIPW-0lj-ZPuQWacHolo4AsXofOma_Zed9BgHMJwYcheDA)  
  <sub>TradingView, 15 hours ago</sub>  
  Explore funds investing in GXE in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in Endesa S.A. Stocks](https://www.google.com/goto?url=CAESaQHrOzAVwWbJteFq-n-sYTp0OQ-lEZ6k68ThY8NsMV0rCSY2RhigiRHrVPL_dxyQxNab5cWinYZ3bxLbPu_2leyqNgUh9ELmDkrwbGa1bh2m-ZQocdj-HtXiACiSQqISb1_Oi0BvaFXdOQ)  
  <sub>TradingView, 19 hours ago</sub>  
  Explore funds investing in ENA in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 89.18 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 90.70 (-1.7%), 50d 90.56 (-1.5%), 200d 87.39 (+2.0%); 50d above 200d
Momentum: RSI(14) 42.5 | MACD -0.657 vs signal -0.367 (histogram -0.290)
Returns: 1d +1.1% | 5d -0.1% | 1m -3.1% | 3m +1.1%
52-week range: 77.90 - 93.19 (now 73.8% of the way up)
Volatility: ATR(14) 0.89 (1.0% of price) | annualised 20d 11.3%
Volume: 0.34x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 11.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 65.7% | hold 34.3% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.6% above the current prices
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
Shares outstanding: 442.27M | fund size: 39.44B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> VWO trades within a normal technical range with modest positive momentum but insufficient catalysts to justify directional conviction. The fund is up 5.5% above its 200-day moving average and trading at the 93.6th percentile of its 52-week range, leaving limited room to the upside without a fresh catalyst. Macro conditions are stable: Treasury yields are flat to slightly higher, the dollar has strengthened, the Fed is expected to hold or ease modestly, and inflation expectations remain anchored at 2.3%. The analyst coverage of the top 5 holdings (22.2% of the fund) is uniformly bullish with a +35.3% price target, but this slice is thin and does not speak to the broader 78% of the fund not in that sample. The positioning in the EM index futures is within its normal range at the 37th percentile of crowding, with a slight reduction in net long exposure over the week—no signal of accumulation. Fund flows data is incomplete. Technicals show RSI at 56.5 (neutral), MACD histogram negative, and volume well below average at 0.33x the 20-day mean, suggesting tepid conviction in the move. The 1-month return of +1.4% is not commensurate with the 5.5% rally from the 200-day; the index has retraced most of its gains in recent weeks. Without a macro surprise, technical break on volume, or material shift in positioning, the risk-reward is balanced but uninspiring.

**Main reasons it gave:**
- RSI 56.5 and MACD histogram negative despite near-52-week highs suggest momentum is not accelerating
- Volume 0.33x 20-day average implies weak conviction in the upside move
- EM futures positioning at 37th percentile with -0.9% weekly change shows no accumulation or conviction shift
- Analyst coverage of top 5 holdings is bullish but covers only 22% of fund weight
- Treasury curve normal, dollar strengthening, no data surprise to justify a tactical call

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs Investing in ANTA Sports Products Ltd. Stocks](https://www.google.com/goto?url=CAESbwHrOzAV0hI26gn6PF8DyrAa7HOZL3gAG89wUCDbMnsuMT8ui1idCNeG9vB-5JZ0gk5LXeqKwsxrfa4AJyxavMTQpEsbjdwU-VM9rbG4iuF4Ed24BQz2XVZjNk842-d-_slYz_XkSx1F-LIxIfi61w)  
  <sub>TradingView, 15 hours ago</sub>  
  Explore funds investing in AS7 in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 60.86 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 60.43 (+0.7%), 50d 59.71 (+1.9%), 200d 57.70 (+5.5%); 50d above 200d
Momentum: RSI(14) 56.5 | MACD 0.019 vs signal 0.098 (histogram -0.079)
Returns: 1d +1.4% | 5d +2.1% | 1m +1.4% | 3m -0.6%
52-week range: 52.42 - 61.44 (now 93.6% of the way up)
Volatility: ATR(14) 0.63 (1.0% of price) | annualised 20d 12.6%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 22.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.34 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +35.3% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 2308.TW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.05</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 3.3% of open interest (1,310,241 contracts)
Change on the week: -0.9% of open interest
Crowding: 37% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.05</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 1.42B | fund size: 86.31B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 93.70 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 94.14 (-0.5%), 50d 94.68 (-1.0%), 200d 95.66 (-2.1%); 50d below 200d
Momentum: RSI(14) 43.4 | MACD -0.430 vs signal -0.399 (histogram -0.032)
Returns: 1d +0.3% | 5d +0.5% | 1m -1.0% | 3m -2.8%
52-week range: 92.95 - 97.74 (now 15.7% of the way up)
Volatility: ATR(14) 0.40 (0.4% of price) | annualised 20d 5.7%
Volume: 0.41x the 20-day average
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
Shares outstanding: 160.26M | fund size: 15.02B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [FLDR: A Low-Risk Fixed Income Vehicle For Risk-Averse Allocation (BATS:FLDR)](https://seekingalpha.com/article/4948236-fldr-a-low-risk-fixed-income-vehicle-for-risk-averse-allocation)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  Fidelity Low Duration Bond Factor ETF offers ultra-short duration and high-quality investment-grade exposure, minimizing both interest rate and credit risk.
- [Gold to $5,000? Strategist Warns a Drop to $3,000 Comes First](https://www.benzinga.com/markets/commodities/26/09/61889634/gold-to-5000-strategist-warns-a-drop-to-3000-comes-first)  
  <sub>Benzinga, 5 hours ago</sub>  
  Gold targets $5000 on continuous ETF inflows, yet market euphoria and rising bond yields signal potential risk for precious metals.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 91.08 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 91.97 (-1.0%), 50d 92.70 (-1.7%), 200d 94.78 (-3.9%); 50d below 200d
Momentum: RSI(14) 36.7 | MACD -0.583 vs signal -0.508 (histogram -0.074)
Returns: 1d +0.3% | 5d +0.2% | 1m -2.1% | 3m -3.1%
52-week range: 90.73 - 97.99 (now 4.9% of the way up)
Volatility: ATR(14) 0.40 (0.4% of price) | annualised 20d 5.6%
Volume: 0.15x the 20-day average
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
Shares outstanding: 461.15M | fund size: 42.00B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Is Invesco S&P MidCap 400 GARP ETF (GRPM) a Strong ETF Right Now?](https://finance.yahoo.com/markets/stocks/articles/invesco-p-midcap-400-garp-102002232.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Launched on 12/03/2010, the Invesco S&P MidCap 400 GARP ETF (GRPM) is a smart beta exchange traded fund offering broad exposure to the Style Box - Mid Cap...
- [Chip Strength Lifts Nasdaq Futures; Oil Slides](https://www.moomoo.com/community/feed/chip-strength-lifts-nasdaq-futures-oil-slides-117308928557462?chain_id=Name1K9-3FXPhg.1lb2720&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A107%2C%22f%22%3A%22www.moomoo.com%2Fetfs%2FPMGOLD-AU%22%7D)  
  <sub>Moomoo, 3 hours ago</sub>  
  Tap the related stocks on the image above to add them to your Watchlist. Market Overview $E-mini S&P 500 Futures (DEC6) (ESmain.US)$ +0.72%, $E-mini N...
- [Futures Rise: Can Market Take Off? 2026's Top Stocks Are Buys](https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-robinhood-sandisk-amd-moderna-surge-buy-areas/)  
  <sub>Investor's Business Daily, 3 hours ago</sub>  
  Dow Jones futures: The stock market is set for a positive start to the week with Robinhood, Sandisk, AMD and Moderna already in buy areas.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 212.26 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 217.05 (-2.2%), 50d 217.21 (-2.3%), 200d 204.94 (+3.6%); 50d above 200d
Momentum: RSI(14) 36.2 | MACD -1.663 vs signal -0.967 (histogram -0.696)
Returns: 1d -0.0% | 5d -1.3% | 1m -3.6% | 3m +1.3%
52-week range: 182.18 - 222.77 (now 74.1% of the way up)
Volatility: ATR(14) 1.86 (0.9% of price) | annualised 20d 8.7%
Volume: 0.30x the 20-day average
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
Ratings by weight: buy 67.9% | hold 32.1% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +2.3% above the current prices
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
Shares outstanding: 475.30M | fund size: 100.89B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [TIPS: The Only Part Of The Federal Debt That Grows Without An Auction (NYSEARCA:TIP)](https://seekingalpha.com/article/4948238-tips-the-only-part-of-the-federal-debt-that-grows-without-an-auction)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  Summary. I rate iShares TIPS Bond ETF a Hold at $105.27 due to structural inflation accretion dynamics and lack of actionable trade opportunities.
- [Dogecoin Price Prediction Stalls as Bitwise Shuts DOGE ETF and Pepeto Presale Races Past $11 Million](https://techbullion.com/dogecoin-price-prediction-stalls-as-bitwise-shuts-doge-etf-and-pepeto-presale-races-past-11-million/)  
  <sub>TechBullion, 24 hours ago</sub>  
  Explore the latest insights on dogecoin price as ETF developments impact the market. Discover the current trends and predictions.
- [Washington Becomes a Quantum Investor: Inside the Defiance QTUM ETF as CHIPS Awards Move From Letters to Contracts](https://www.tipranks.com/news/washington-becomes-a-quantum-investor-inside-the-defiance-qtum-etf-as-chips-awards-move-from-letters-to-contracts)  
  <sub>TipRanks, 4 hours ago</sub>  
  Between September 8 and September 16, the U.S. Commerce Department converted up to $1.3 billion of proposed CHIPS and Science Act quantum incentives into...
- [Cathie Wood Sells Tech Favorites Palantir and AMD; Buys Archer Aviation Stock for ARK Innovation ETF](https://www.tipranks.com/news/cathie-wood-sells-tech-favorites-palantir-and-amd-buys-archer-aviation-stock-for-ark-innovation-etf)  
  <sub>TipRanks, 2 hours ago</sub>  
  Cathie Wood and her team at ARK Invest made a notable move in their latest portfolio updates. The investment firm sold off shares of tech favorites Palantir...
- [Why Is the Roundhill Memory ETF (DRAM) Rising Today, Sept. 17?](https://www.google.com/goto?url=CAESjwEB6zswFQF4Ufssg1l37hceikdti8XI8v1_ODiL6FUzLjOomTVwRvmqg8yOV-tF4DbJ9a8f08z8lM0WsT9ae1XxBcVkFi7saSWFueEh4qpq_Xs6s7akMBz5sy6rQmPaf2H_1-YfwfJYmCsJ5D3N9SkzBOghtGS3GhgHtvwitWIfyabNqvu9ikxtvjZVGrIn7Q)  
  <sub>TipRanks, 5 hours ago</sub>  
  Roundhill Memory ETF ($DRAM) is up more than 4% as of this writing on Thursday, as memory and semiconductor stocks continue to gain momentum.
- [İş Yatırım Details Market-Making Activity in ISX30 ETF](https://www.tipranks.com/news/company-announcements/is-yatirim-details-market-making-activity-in-isx30-etf-2)  
  <sub>TipRanks, 4 hours ago</sub>  
  Is Yatirim Menkul Degerler AS ( ($TR:ISMEN) ) just unveiled an announcement. İş Yatırım Menkul Değerler A.Ş., a leading brokerage and investment services...
- [From Korean Chipmakers to Leveraged Semiconductor ETFs: STARTRADER Launches 49 New 24/7 Stock and ETF CFDs](https://www.tipranks.com/news/newswire/from-korean-chipmakers-to-leveraged-semiconductor-etfs-startrader-launches-49-new-24-7-stock-and-etf-cfds)  
  <sub>TipRanks, 6 hours ago</sub>  
  Port Louis, Mauritius, September 21st, 2026, FinanceWire Available from September 18, 2026, the expansion adds 30 US stocks, 14 ETFs, and five USD-quoted...
- [Bitcoin ETF IBIT Draws Fresh Wave of Inflows as Price Surge Lures Traditional Investors](https://www.tipranks.com/news/cryptocurrencies/bitcoin-etf-ibit-draws-fresh-wave-of-inflows-as-price-surge-lures-traditional-investors)  
  <sub>TipRanks, 5 hours ago</sub>  
  Bitcoin ETF pulls in fresh cash as investors chase rally IShares Bitcoin Trust Registered's IBIT logged new inflows of $183.7 million on September 18, 2026,...
- [Leveraged XRP Bets Heat Up as ProShares Ultra XRP ETF Draws Fresh Inflows](https://www.tipranks.com/news/cryptocurrencies/leveraged-xrp-bets-heat-up-as-proshares-ultra-xrp-etf-draws-fresh-inflows-2)  
  <sub>TipRanks, 8 hours ago</sub>  
  ProShares Ultra XRP ETF saw another jolt of capital this week, as the leveraged crypto fund logged a fresh inflow of $521151 on September 15, 2026.
- [Leveraged Bitcoin Bulls Tap the Brakes as ProShares’ BITU Registers Outflow](https://www.tipranks.com/news/cryptocurrencies/leveraged-bitcoin-bulls-tap-the-brakes-as-proshares-bitu-registers-outflow)  
  <sub>TipRanks, 3 hours ago</sub>  
  Leveraged Bitcoin Bulls Tap the Brakes as ProShares' BITU Sees Outflow ProShares Ultra Bitcoin ETF, BITU, recorded a single-day outflow of $515284 on...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 105.53 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 106.54 (-0.9%), 50d 107.07 (-1.4%), 200d 109.60 (-3.7%); 50d below 200d
Momentum: RSI(14) 33.5 | MACD -0.503 vs signal -0.391 (histogram -0.111)
Returns: 1d +0.2% | 5d -0.3% | 1m -1.9% | 3m -3.1%
52-week range: 105.27 - 112.20 (now 3.8% of the way up)
Volatility: ATR(14) 0.36 (0.3% of price) | annualised 20d 4.1%
Volume: 0.44x the 20-day average
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
Shares outstanding: 142.47M | fund size: 15.03B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [The Fed shouldn't 'look through' some supply shocks, Chicago Fed's Goolsbee says (TLT:NASDAQ)](https://seekingalpha.com/news/4644700-the-fed-shouldnt-look-through-some-supply-shocks-chicago-feds-goolsbee-says)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Since the 1970s, the Federal Reserve has held the stance of “looking through” supply shocks and only responding if the resulting inflation bleeds into other...
- [Investors pour $625B into bond funds despite po...](https://pluang.com/en/news-feed/harga-obligasi-turun-tetap-ada-pembeli)  
  <sub>Pluang, 3 hours ago</sub>  
  In 2023, bond investors have faced losses, with major bond ETFs like the iShares Core US Aggregate Bond ETF down 4% and the iShares 20+ Year Treasury Bond...
- [Why the White House's Push to Control Bond Markets Is Destined to Disappoint Investors](https://www.theglobeandmail.com/investing/markets/markets-news/motley/4702709/why-the-white-house-s-push-to-control-bond-markets-is-destined-to-disappoint-investors/)  
  <sub>The Globe and Mail, 20 hours ago</sub>  
  With enough gumption, the White House and the Treasury Department can try to nudge the bond market in its preferred direction. In August, the Treasury said...
- [Nasdaq, S&P 500, Dow Futures Shake Off Iran Jitters As Investors Turn To AI Hyperscaler Earnings: INTC, TSLA, TTD, HIMS In Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-s-and-p-500-dow-futures-shake-off-iran-jitters-as-investors-turn-to-ai-hyperscaler-earnings-intc-tsla-ttd-hims-in-focus/cZZYW1bR7UM)  
  <sub>Stocktwits, 10 hours ago</sub>  
  Markets were primarily focused on earnings from major companies, alongside rising oil prices due to the continued tensions between the U.S. and Iran.
- [Nasdaq, S&P 500 Futures Rise As Chip Rally Counters Iran Jitters Ahead Of Big Tech Earnings: Why IREN, ACHR, TSLA, BA Stocks Are Drawing Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-s-and-p-500-futures-rise-as-chip-rally-counters-iran-jitters-ahead-of-big-tech-earnings/cZZ1tCdR7HO)  
  <sub>Stocktwits, 22 hours ago</sub>  
  The VanEck Semiconductor ETF was up 0.41% at close, reversing three consecutive days of declines. However, tensions in the Middle East continued to rise...
- [Higher Rates Push Investors to Short and Intermediate Bond Funds](https://www.thedailyupside.com/etf/thematics-sectors/higher-rates-push-investors-to-short-and-intermediate-bond-funds/)  
  <sub>The Daily Upside, 11 hours ago</sub>  
  More than $9 billion flowed into short-term government funds in August, the second-highest month on record after March 2020.
- [Dow, S&P 500, Nasdaq Futures Climb Ahead Of Key China Summit: CRML, APLD, GME, AMD Stocks In Focus](https://es.tradingview.com/news/stocktwits:09b9f8005094b:0-dow-s-p-500-nasdaq-futures-climb-ahead-of-key-china-summit-crml-apld-gme-amd-stocks-in-focus/)  
  <sub>TradingView, 13 hours ago</sub>  
  U.S. stock futures traded higher in the overnight session late Sunday ahead of a key summit this week between President Donald Trump and Chinese President...
- [S&P 500, Nasdaq, Dow Futures Ease After Another Record Close As AI Momentum Cushions Iran's Expanding Strikes: MRVL, AVGO, MSFT, PANW In Focus](https://stocktwits.com/news-articles/markets/equity/sp500-nasdaq-dow-futures-ease-after-another-record-close-ai-momentum-cushions-iran-strikes/cZ0SoqTReDV)  
  <sub>Stocktwits, 9 hours ago</sub>  
  U.S. President Donald Trump said in a post on Truth Social on Tuesday that the U.S. and Iran deal negotiations are ongoing, dismissing reports of strained...
- [COST Stock Retreats After Hours On Decelerating Comparable Sales After Strong May Performance](https://stocktwits.com/news-articles/markets/equity/cost-stock-retreats-after-hours-on-decelerating-comparable-sales-after-strong-may-performance/cZmoWMAR7VQ)  
  <sub>Stocktwits, 9 hours ago</sub>  
  Costco reported net sales of $29.24 billion for the five weeks ended July 5, 2026, a 10.6% increase from $26.44 billion a year earlier.
- [Nasdaq, S&P 500, Dow Futures Climb As Trump's $2B Quantum Computing Bet Outweighs Iran Jitters: RKLB, IBM, RGTI, NIO In Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-sp500-dow-futures-climb-as-trump-quantum-computing-bet-outweighs-iran-jitters/cZgbH1xRe8r)  
  <sub>Stocktwits, 20 hours ago</sub>  
  The Trump administration said on Friday it would invest $2 billion in quantum computing stocks, with about half earmarked for IBM.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 81.64 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 81.94 (-0.4%), 50d 82.56 (-1.1%), 200d 85.83 (-4.9%); 50d below 200d
Momentum: RSI(14) 47.0 | MACD -0.425 vs signal -0.448 (histogram 0.023)
Returns: 1d +0.5% | 5d +0.9% | 1m -0.8% | 3m -5.2%
52-week range: 80.71 - 92.06 (now 8.2% of the way up)
Volatility: ATR(14) 0.68 (0.8% of price) | annualised 20d 9.2%
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
Shares outstanding: 109.70M | fund size: 8.96B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 28.43 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 28.14 (+1.1%), 50d 28.21 (+0.8%), 200d 27.72 (+2.6%); 50d above 200d
Momentum: RSI(14) 64.9 | MACD 0.062 vs signal 0.012 (histogram 0.049)
Returns: 1d +0.2% | 5d +0.9% | 1m +1.9% | 3m +0.3%
52-week range: 26.47 - 28.60 (now 92.3% of the way up)
Volatility: ATR(14) 0.10 (0.4% of price) | annualised 20d 4.6%
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
Shares outstanding: 10.52M | fund size: 299.18M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Taiwan (EWT) · Sector or country — BULLISH, confidence 0.35

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> EWT is at a 52-week high, 32.9% above its 200d SMA with 50d>200d and positive MACD, and RSI 65.8 is strong without being extreme. Analyst roll-up over 38% of the fund is unanimously buy with ~28% upside, though that is concentrated AI-semis coverage (TSMC alone 22%). Macro is benign for risk: VIX down 2.5 to 14.6, curve normally sloped, 10y unchanged. Offsets: no macro catalyst this cycle, breakout came on 0.25x average volume, dollar up 0.9 and a priced hiking path are mild headwinds for an EM tech proxy, and P/E 27 after +43.5%/yr for three years leaves little cushion. Modest long tilt rather than a conviction call.

**Main reasons it gave:**
- Close 115.04 at top of 52-week range, +32.9% vs 200d SMA, 50d above 200d
- Breakout volume only 0.25x the 20-day average
- Analyst roll-up over 38% of fund: 100% buy, +27.8% weighted target
- VIX 14.62, down 2.5 on week; 10y flat, curve +0.98 normal
- Dollar index +0.90 and 2y at 4.67% pricing hikes — headwind for EM tech
- 73.9% technology, 22.1% single-name TSMC concentration; P/E 27.3

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.55</summary>

```text
Last close 115.04 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 109.19 (+5.3%), 50d 104.29 (+10.3%), 200d 86.54 (+32.9%); 50d above 200d
Momentum: RSI(14) 65.8 | MACD 1.904 vs signal 1.761 (histogram 0.143)
Returns: 1d +3.0% | 5d +7.3% | 1m +10.5% | 3m +3.1%
52-week range: 60.03 - 115.04 (now 100.0% of the way up)
Volatility: ATR(14) 2.30 (2.0% of price) | annualised 20d 25.9%
Volume: 0.25x the 20-day average
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
Weighted price target: +27.8% above the current prices
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

### US house builders (XHB) · Sector or country — BEARISH, confidence 0.35

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Homebuilder/construction basket is in a clear downtrend: price below 20/50/200d SMAs, 50d under 200d, -8.5% in a month, sitting 6.8% off the 52-week low with negative MACD. The macro backdrop is the driver: 10-year at 4.96% and a 2-year at 4.67% implying the market prices tightening rather than easing, which is direct pressure on mortgage rates and housing-sensitive cyclicals, plus a firmer dollar. Offsets are real -- RSI 33.7 is oversold, volume is thin (0.21x), VIX is calm at 14.6, and analyst targets on the top slice sit +22% above spot -- so this is a modest, low-conviction tilt rather than a catalyst trade. The single news item is an unrelated ETF listicle and carries no information.

**Main reasons it gave:**
- Price below 20d (-4.1%), 50d (-8.0%) and 200d (-9.3%) SMAs with 50d under 200d
- 10-year yield 4.96% and 2-year 4.67% vs 4.00% Fed target -- market pricing hikes, adverse for rate-sensitive housing
- -8.5% 1m / -11.4% 3m, only 6.8% above the 52-week low
- RSI 33.7 and 0.21x average volume argue against chasing the break
- Top-5 roll-up (20.9% of fund) shows 73.5% buy weight and +22.4% targets -- thin coverage, mild offset

<details><summary><b>News</b> — score +0.00</summary>

- [Should You Invest in the Invesco Building & Construction ETF (PKB)?](https://finance.yahoo.com/markets/stocks/articles/invest-invesco-building-construction-etf-102002535.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Looking for broad exposure to the Industrials - Engineering and Construction segment of the equity market? You should consider the Invesco Building...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.55</summary>

```text
Last close 96.68 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 100.81 (-4.1%), 50d 105.03 (-8.0%), 200d 106.61 (-9.3%); 50d below 200d
Momentum: RSI(14) 33.7 | MACD -2.664 vs signal -2.380 (histogram -0.285)
Returns: 1d +0.3% | 5d -1.6% | 1m -8.5% | 3m -11.4%
52-week range: 94.86 - 121.36 (now 6.8% of the way up)
Volatility: ATR(14) 2.14 (2.2% of price) | annualised 20d 18.5%
Volume: 0.21x the 20-day average
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
Three-year record: +7.6% a year | beta to the market 1.46
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 20.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 73.5% | hold 26.5% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.4% above the current prices
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
Shares outstanding: 13.76M | fund size: 1.33B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — BULLISH, confidence 0.30

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> EIS is in a clean uptrend (50d>200d, price above all major SMAs, RSI 59, MACD positive) with +4.6% over a month, though volume is light at 0.71x average and there is no macro catalyst. Rates were essentially unchanged on the week, VIX fell to 14.6 (calm), and the dollar firmed slightly -- a benign but unremarkable backdrop. The analyst roll-up over 37.6% of the fund is unanimously buy with a +14.7% weighted target, which supports a mild positive tilt. Flow direction is unknown, so no behavioural read. Nothing here rises to a macro surprise, so conviction stays low.

**Main reasons it gave:**
- Price above 20d/50d/200d SMAs with 50d above 200d and RSI 59
- Advance on light volume (0.71x 20-day average)
- Analyst roll-up over 37.6% of fund: 100% buy, +14.7% weighted target
- VIX 14.62, down 2.5 on the week; 10-year yield unchanged
- P/E 17.89 with concentrated financials weight (36%) and 10% single-name Teva exposure

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.45</summary>

```text
Last close 126.74 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 123.93 (+2.3%), 50d 122.10 (+3.8%), 200d 121.97 (+3.9%); 50d above 200d
Momentum: RSI(14) 59.1 | MACD 0.704 vs signal 0.575 (histogram 0.129)
Returns: 1d +1.6% | 5d +3.0% | 1m +4.6% | 3m +4.7%
52-week range: 94.16 - 137.69 (now 74.8% of the way up)
Volatility: ATR(14) 1.72 (1.4% of price) | annualised 20d 19.8%
Volume: 0.71x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 37.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.19 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.7% above the current prices
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
Shares outstanding: 2.55M | fund size: 323.19M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.28

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> SMH is in a firm uptrend (above 20/50/200d, 50d>200d, +21% vs 200d) with a fresh MACD cross and a +3.1% day, but the move came on 0.53x average volume and is still -11.7% over three months, so this is a bounce inside a wide range rather than a decisive break. Macro is unhelpful for high-beta duration-sensitive tech: the 2-year at 4.67% versus a 4.00% target prices further hikes, the 10-year sits near 5% unchanged, the dollar firmed 0.9 and inflation is 3.4%. No policy or data surprise this week; VIX at 14.6 is calm. Holdings-level analyst view is genuinely supportive (100% buy by weight across 49% coverage, +37% weighted target) but valuation is rich (P/E 37.8, beta 2.06). The Seeking Alpha piece asserting SMH is 'ready to run' is promotional and given no weight; the SK hynix index-inclusion stories are irrelevant to SMH's own basket. Net: no edge in timing a macro-sensitive chip basket here.

**Main reasons it gave:**
- Price above 20/50/200d SMAs, 50d>200d, MACD crossed above signal (hist +3.0)
- Rally on 0.53x 20-day average volume; still -11.7% over 3 months
- 2-year 4.67% vs 4.00% Fed target prices ~3 hikes; 10-year flat at 4.96%, dollar +0.90
- Holdings roll-up: 100% buy by weight over 49.2% of fund, +36.9% weighted target
- Rich basket valuation (P/E 37.8, P/B 11.1) with beta 2.06 and 35.7% 20-day annualised vol

<details><summary><b>News</b> — score +0.05</summary>

- [Stocks Didn't Really Rally Because Of The Rate Hike; SMH & Robinhood Markets Ready To Run](https://seekingalpha.com/article/4948230-stocks-didnt-rally-because-of-rate-hike-smh-robinhood-markets-ready-to-run)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  The most bullish part of the FOMC meeting wasn't the rate hike; it was the clarity it gave investors. SMH, QQQ, and a select cohort of chip stocks all look...
- [SK hynix ADR Joins Major U.S. and Korean ETFs](https://www.businesskorea.co.kr/news/articleView.html?idxno=277460)  
  <sub>Businesskorea, 6 hours ago</sub>  
  As domestic and foreign exchange-traded funds (ETFs) containing SK hynix American Depositary Receipts (ADR) rapidly increase, market attention is focusing...
- [History Says This Chip ETF Keeps Beating the S&P 500. It Has Trailed the Index Only Twice Since 2016.](https://www.theglobeandmail.com/investing/markets/stocks/SMH-Q/pressreleases/4704160/history-says-this-chip-etf-keeps-beating-the-sp-500-it-has-trailed-the-index-only-twice-since-2016/)  
  <sub>The Globe and Mail, 12 hours ago</sub>  
  Detailed price information for Vaneck Semiconductor ETF (SMH-Q) from The Globe and Mail including charting and trades.
- [SK Hynix ADR Joins Benchmark U.S. Semiconductor Index SMH; Samsung Asset Management ETF Adds It Too](https://finance.biggo.com/news/23c8ad76-4117-493c-99e6-a260b0522c56)  
  <sub>BigGo Finance, 14 hours ago</sub>  
  Samsung Asset Management's KODEX US Semiconductor ETF has added SK Hynix ADR at approximately 4.8% weighting following the September regular…
- [KODEX U.S. Semiconductor ETF Adds SK hynix ADR](https://en.sedaily.com/finance/2026/09/21/kodex-us-semiconductor-etf-adds-sk-hynix-adr)  
  <sub>Seoul Economic Daily, 14 hours ago</sub>  
  SK hynix Joins Leading U.S. Chip Index Two Months After Nasdaq Debut Weighting of 4.8% Matches That of SMH, the Largest U.S. Chip ETF. Finance|.
- [Samsung Asset Management Adds SK hynix ADR to 'KODEX US Semiconductor' ETF](https://www.asiae.co.kr/en/article/2026092109164342016)  
  <sub>아시아경제, 15 hours ago</sub>  
  Samsung Asset Management announced on September 21 that the 'KODEX US Semiconductor' Exchange-Traded Fund (ETF) has newly included SK hynix ADR, follo.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.05</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.30</summary>

```text
Last close 590.89 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 559.35 (+5.6%), 50d 564.38 (+4.7%), 200d 488.47 (+21.0%); 50d above 200d
Momentum: RSI(14) 59.8 | MACD 0.209 vs signal -2.796 (histogram 3.005)
Returns: 1d +3.1% | 5d +9.1% | 1m +5.0% | 3m -11.7%
52-week range: 315.71 - 668.91 (now 77.9% of the way up)
Volatility: ATR(14) 16.56 (2.8% of price) | annualised 20d 35.7%
Volume: 0.53x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 49.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.34 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +36.9% above the current prices
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
Shares outstanding: 124.27M | fund size: 73.43B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.28

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> XLK is in a strong uptrend (above 20/50/200d, 50d>200d, +18.9% vs 200d, RSI 63.7, MACD positive) and near 52-week highs, with calm volatility (VIX 14.6, -2.5 on week) and unanimous buy coverage across 45.7% of the fund with +26% weighted targets. But there is no macro catalyst this week: yields essentially flat across the curve, curve normally sloped, dollar firm, and the 2-year still prices a hiking path against 3.4% inflation -- a headwind for a 33x P/E, 1.50-beta sector. Volume on the latest advance was 0.44x average, which undercuts the breakout. News is roundups, single-holding items and trade-talk anticipation, not a policy surprise. Slight upward tilt at most; NEUTRAL is the honest call.

**Main reasons it gave:**
- Price 93.3% of 52-week range, above 20/50/200d SMAs with 50d>200d
- Advance came on 0.44x average volume -- weak confirmation
- Treasury yields flat on the week (10y +0.00), no rate or data surprise
- 2-year 4.67% prices ~3 hikes with inflation at 3.4% -- headwind for 33x P/E tech
- 100% buy ratings and +26.1% weighted target over 45.7% of fund weight

<details><summary><b>News</b> — score +0.10</summary>

- [U.S.-China Talks Seem Successful: ETF Areas in Focus](https://www.google.com/goto?url=CAESogEB6zswFYpwUadWKfhefy7WC9tVgwuY0JtVcj34eErJtZPD8s9Ww-IGnochmCgm9Lj5nm9-Ork6Cn8H3l_KBu8yTsDxAfw_Aw--tpZgph9DfTqR1R21j4ZA-zra2bjD1sVDuCAj47yboLMPx3fy86NU1q5JHnLqcQuN2PY8ZbKLydRgOQ2HWCiggVqRoYxc57gPKA-5SJ8zOl_ao-WsoviVv8A)  
  <sub>TradingView, 2 hours ago</sub>  
  Investors are currently tracking developments ahead of an expected meeting between U.S. President Donald Trump and Chinese President Xi Jinping in...
- [Exchange-Traded Funds Rise, Equity Futures up Pre-Bell Monday as Oil Prices Decline](https://www.moomoo.com/news/post/76538074/exchange-traded-funds-rise-equity-futures-up-pre-bell-monday)  
  <sub>Moomoo, 1 hour ago</sub>  
  Thebroad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.7% and the actively traded Invesco QQQ Trust (QQQ) advanced 1.1% in Monday's...
- [Leading And Lagging Sectors For September 21, 2026](https://www.google.com/goto?url=CAESngEB6zswFWr6XMVsKURncCG_jn_bE4_8cG0PDDcWxeLtuYWHNiC9VDOCQeWTdK1Uc7c50FpxAuRtxGj9ot_rPc0UpmNQF4cdJ6vyPnn63x-ZS6T6brceoeVp8EdFG547-23MvU0DUuNuTD-DVyNdAkF03RNArCVam4KL4xpFS7FVwZE524b-7Ql5q37VFuV5EuFGnmcl478_8_fBFHqJqg)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLK) State Street Technology Select Sector SPDR ETF 191.7700 2.170 1.14 39.0K (NYSE:XLC) State...
- [Meta Spikes 7% as Wells Fargo Lifts Price Target to $796 Ahead of Connect; Alphabet Nudges Higher, Microsoft Holds Flat](https://www.google.com/goto?url=CAES2AEB6zswFU5nPjDnVSqJTCLEoXOyrhChvz-4TqfBselJbhat4m-oxs9XFmnW3PDqGTSNgJ0fQNYixskpCEdH-bM4eLu68zw0BUBmHzGqqdHAv9E7CWuybHtaBWFVT1E14XKRh6FiJ7khjQwzf9HXf_n3oaREXE1VtK7qJpkfE0WelclcLNwR1IFWzH3gR8lV2eZuc5k1fnFy8qf1XD2jdfE4vlZrGQbM6XaDBCuJGwQxaMcjMgXZuHDWiyrtFV0XMu8ui6VIW-7uSKVFcinUHl_fkBWJiXa8YHI)  
  <sub>24/7 Wall St., 50 minutes ago</sub>  
  Wells Fargo raised its META price target from $640 to $796, sending shares up 6% to $704 ahead of the Connect conference. Alphabet climbed 2% with the...
- [The Week That Proved AI Is Real: MSFT +16%, AMZN +10%, META -10%, AAPL -4% - Winners, Losers and Key Takeaways](https://www.tradingkey.com/analysis/stocks/us-stocks/262067343-week-review-july-28-31-2026-microsoft-amazon-apple-meta-earnings-ai-tradingkey)  
  <sub>TradingKey, 14 hours ago</sub>  
  Microsoft surged 16% adding $450B in a single day. Amazon jumped 10%. Meta crashed 10%. Apple fell 4%. The KOSPI gained 17.9% — the largest one-day gain in...
- [Applied Materials (AMAT) Earnings Preview: AI Chip Demand, Capital Expenditure Trends, & Trade Setups - In Progress](https://www.google.com/goto?url=CAES1QEB6zswFfhjo_qB8_fjnDZLxkQBaExogJWJf8spyvZrRVTMIpsu5cKhp4LaRdcbjrH6sBfs6oLOu58S6AZXL1B5Tb1t8VaZ1UAtbTL4cpUzQRys-xPvItyHkGXV0BGNUlxDqBiXkRQL-Y5adkQpP_z1WRcjZJ3eHhtTieJVMFGHFbvKDmZ5fpzVTcWvx27KObrVaQTpMw5PsUa85_t97w1lnG5BytqclKEnIyTxkX_ZqV-cUXh-tehKisQitC5R1neYGflKeanyB_pXjYo2KdZ3kYkaf5c)  
  <sub>TradingKey, 18 hours ago</sub>  
  TradingKey - The May 14 report comes when AMAT has risen by 179.83% over the past year and the whole semiconductor equipment cycle rests on AI demand for...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.45</summary>

```text
Last close 193.49 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 185.88 (+4.1%), 50d 183.27 (+5.6%), 200d 162.69 (+18.9%); 50d above 200d
Momentum: RSI(14) 63.7 | MACD 1.385 vs signal 0.888 (histogram 0.497)
Returns: 1d +2.1% | 5d +5.0% | 1m +5.7% | 3m +0.7%
52-week range: 127.50 - 198.21 (now 93.3% of the way up)
Volatility: ATR(14) 3.46 (1.8% of price) | annualised 20d 22.2%
Volume: 0.44x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

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
Rolled up from the 5 largest holdings, 45.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.56 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.1% above the current prices
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
Shares outstanding: 660.09M | fund size: 127.72B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWA is an Australian equity fund with mixed technical and fundamental signals offering no clear directional catalyst. The technical picture shows deteriorating momentum (RSI 44.5, MACD histogram negative) and price weakness below multiple moving averages (-2.0% vs 20d, -1.6% vs 50d), offset by still-positive trend relative to the 200d SMA. Volume is subdued at 0.20x average, limiting signal reliability. The fund's holdings face headwinds from analyst consensus: the largest 46.4% of holdings (financials and BHP) carry a weighted mean rating of 3.48 on a 1-5 sell scale with a collective -6.7% downside to targets, suggesting limited near-term upside. Valuation is moderate at 21.06x P/E with a 2.8% yield. Macro backdrop is neutral: US yields have moved modestly higher with the curve normalizing, the dollar has appreciated 0.90 on the week, and VIX has declined, reflecting reduced risk-off sentiment. There is no material data surprise, policy shock, or technical break to justify conviction in either direction. A weak quarter-point AUD sensitivity to modest USD strength and elevated yield environment provide light headwinds, but nothing decisive. The fund deserves a hold pending clearer catalyst.

**Main reasons it gave:**
- Momentum deterioration: RSI 44.5, MACD histogram -0.125 and below signal line
- Analyst consensus on top 46% holdings at 3.48/5 (hold-to-sell) with -6.7% target downside
- Price below 20d and 50d SMAs (-2.0% and -1.6% respectively)
- Low trading volume at 0.20x 20d average limits breakout conviction
- No macro catalyst: Treasury yields flat to modestly higher, VIX calm at 14.62

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 29.02 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 29.62 (-2.0%), 50d 29.48 (-1.6%), 200d 28.54 (+1.7%); 50d above 200d
Momentum: RSI(14) 44.5 | MACD -0.218 vs signal -0.093 (histogram -0.125)
Returns: 1d +0.9% | 5d -0.1% | 1m -2.5% | 3m +2.0%
52-week range: 24.95 - 30.43 (now 74.3% of the way up)
Volatility: ATR(14) 0.39 (1.3% of price) | annualised 20d 17.2%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

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

<details><summary><b>What analysts and big funds say</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.25</summary>

```text
Rolled up from the 5 largest holdings, 46.4% of the fund by weight
Ratings by weight: buy 0.0% | hold 59.6% | sell 40.4% (mean 3.48 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -6.7% above the current prices
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

> EWC (iShares Canada ETF) presents a mixed technical and fundamental picture with no catalytic macro shifts to justify a directional lean. The fund has drifted lower over the past month (-2.6%) despite holding above its 200-day moving average, and is trading 1.6% below its 20-day SMA. Momentum indicators are tepid: RSI at 43.3 suggests neither overbought nor oversold conditions, while MACD histogram remains negative, indicating weak or fading upside momentum. The 3-month performance of +3.9% shows the fund still holds a constructive longer-term trend, and the fund's beta of 0.79 with three-year returns of +21.9% annually reflects solid historical performance. On the fundamental side, analyst coverage of the top 28.3% of holdings is constructive (74.3% buy-rated, +7.1% weighted price target), but this represents less than one-third of the fund. The valuation metrics are reasonable (P/E 19.49, yield 1.2%) for a Canadian equity fund with heavy exposure to financials (39.2%) and energy (17.9%), sectors that are neither especially compelling nor concerning at current macro conditions. The macro backdrop offers no fresh impetus: Treasury yields are stable intra-week, the dollar has strengthened modestly (+0.90), volatility has declined (VIX -2.5), and the rate path prices only about three quarter-point hikes over two years. No significant news or data surprises have emerged to shift the calculus. Volume is light at 0.23x average, typical of early autumn trading. The technicals do not show a decisive break either direction; the fund remains in a choppy consolidation phase. Without a material catalyst—whether policy surprise, earnings inflection, or technical breakdown/breakout—the appropriate stance is to await clearer direction.

**Main reasons it gave:**
- RSI 43.3 and negative MACD histogram signal fading momentum
- price 1.6% below 20-day MA, -2.6% over one month despite 4.7% above 200-day MA
- analyst coverage of top holdings shows +7.1% target but covers only 28.3% of fund
- macro backdrop stable with no rate surprise or policy catalyst
- light volume at 0.23x average suggests low conviction in either direction

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 60.17 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 61.18 (-1.6%), 50d 60.67 (-0.8%), 200d 57.46 (+4.7%); 50d above 200d
Momentum: RSI(14) 43.3 | MACD -0.229 vs signal -0.029 (histogram -0.200)
Returns: 1d -0.1% | 5d -0.5% | 1m -2.6% | 3m +3.9%
52-week range: 49.72 - 62.64 (now 80.9% of the way up)
Volatility: ATR(14) 0.67 (1.1% of price) | annualised 20d 13.4%
Volume: 0.23x the 20-day average
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
Three-year record: +21.9% a year | beta to the market 0.79
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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 28.3% of the fund by weight
Ratings by weight: buy 74.3% | hold 25.7% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +7.1% above the current prices
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

> EWD (iShares MSCI Sweden ETF) holds a focused basket of Swedish equities with solid fundamentals: P/E 14.99, dividend yield 3.4%, and three-year annualized returns of +19.6%. The fund is currently trading 1.6% below its 20-day SMA and 0.8% below its 50-day, with RSI at 45.7 and MACD in negative territory—technical indicators suggest mild weakness without conviction. Momentum is softer over the one- and three-month horizon. The analyst roll-up (29.5% coverage) shows 82% buy ratings with a +10.6% upside target, which is constructive but modest and covers less than one-third of the fund. Macro backdrop is benign: the yield curve is positively sloped at +0.98, VIX is calm at 14.62, the dollar has risen 0.90 this week, and US rates are stable. Volume is notably thin at 0.08x the 20-day average, limiting the reliability of the recent +1.3% one-day move. The fund trades 67.7% of the way up its 52-week range, not at an extreme. There is no recent news catalyst, no rate surprise, and no decisive technical break. The combination of adequate valuations, analyst support on major holdings, and calm macro conditions prevents a bearish call, but the technical softness, thin volume, thin analyst coverage roll-up, and absence of a specific near-term catalyst do not support conviction to the upside. A marginal lean to stability is warranted.

**Main reasons it gave:**
- RSI 45.7 and MACD histogram negative; price below both 20d and 50d SMAs
- Analyst roll-up 82% buy with +10.6% target, but covers only 29.5% of fund
- Thin volume 0.08x 20-day average undermines technical signal reliability
- Macro stable with normal yield curve and low volatility; no catalyst
- Valuation reasonable at P/E 14.99, 3.4% yield, but no specific near-term driver

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 51.70 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 52.57 (-1.6%), 50d 52.11 (-0.8%), 200d 51.29 (+0.8%); 50d above 200d
Momentum: RSI(14) 45.7 | MACD -0.339 vs signal -0.142 (histogram -0.197)
Returns: 1d +1.3% | 5d +0.4% | 1m -2.2% | 3m +3.1%
52-week range: 45.38 - 54.72 (now 67.7% of the way up)
Volatility: ATR(14) 0.67 (1.3% of price) | annualised 20d 15.5%
Volume: 0.08x the 20-day average
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
Weighted price target: +10.6% above the current prices
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

> EWG is a focused German equity fund with solid fundamentals and analyst support, but technical positioning and macro conditions do not yet justify a directional call. The fund's 18.4 P/E and 1.9% yield sit in reasonable territory; the three-year +18.2% annualized return reflects solid performance. Analyst coverage of the top 45.5% by weight shows 78% buy ratings and a +15.9% price target, which is constructive. However, technicals are mixed: the fund is 1.9% below its 20-day SMA and RSI(14) at 42.9 is in neutral-to-weak momentum territory. MACD histogram is negative, signalling weakening momentum. The price sits 69% of the way through its 52-week range with only 0.23x average volume, suggesting light conviction in the move. Macro backdrop is calm with VIX at 14.6, Treasury yields stable, and the curve normally upward-sloping, but offers no catalyst. The dollar has strengthened +0.90 this week, which can pressure international equities; rate expectations imply modest Fed ease ahead but nothing dramatic. The one-month return of -3.0% and negligible five-day change (-0.3%) show recent choppiness without directional clarity. German equities lack a fresh macro or policy impulse to trigger re-rating. Support from analyst consensus on the holdings is real, but insufficient alone to overcome neutral technicals and absent catalysts in a macro environment that is stable rather than favorable.

**Main reasons it gave:**
- Analyst buy ratings 78% of top 5 holdings with +15.9% price target
- RSI(14) at 42.9 and negative MACD histogram signal weakening momentum
- Price 1.9% below 20-day SMA; low volume (0.23x 20d avg) shows weak conviction
- No macro catalyst; stable rates and calm volatility do not support a directional move

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 42.58 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 43.41 (-1.9%), 50d 42.99 (-0.9%), 200d 42.37 (+0.5%); 50d above 200d
Momentum: RSI(14) 42.9 | MACD -0.270 vs signal -0.100 (histogram -0.170)
Returns: 1d +1.0% | 5d -0.3% | 1m -3.0% | 3m +2.5%
52-week range: 38.08 - 44.59 (now 69.2% of the way up)
Volatility: ATR(14) 0.45 (1.1% of price) | annualised 20d 12.5%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

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
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.85 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.9% above the current prices
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
Shares outstanding: 79.50M | fund size: 3.39B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWJ is at the top of its 52-week range after a 9% move from the 200-day MA, with momentum indicators showing exhaustion (RSI at 56, MACD histogram negative). Technicals suggest limited upside from current levels. The macro backdrop is mixed: the dollar strengthened 0.90 this week to 100.36, which headwinds the yen and therefore a Japan fund; Treasury yields are stable; volatility is low and benign. Fund fundamentals are reasonable (P/E 19.1, 3.7% yield, strong 3-year returns) but offer no exceptional catalyst. Analyst coverage of the largest holdings (only 17% of fund weight) shows universal buy ratings with a +19.7% price target, but this thin coverage and the target's typical forward-looking bias limit its weight. CFTC positioning in the Nikkei is modest and near historical averages with only a 1.5% increase on the week, showing neither crowding nor conviction. Fund flows data is insufficient. The fund has had a solid run, but the combination of technical saturation, dollar strength headwinds, and lack of new macro or flow catalyst argues for neutrality rather than a bullish extension.

**Main reasons it gave:**
- Price at 96% of 52-week range with RSI exhaustion and negative MACD histogram
- Dollar strength to 100.36 (+0.90 on week) headwinds yen-denominated Japan exposure
- Analyst buy ratings on top 5 holdings but coverage only 17% of fund weight
- CFTC positioning at 38th percentile, only +1.5% change on week, within normal range

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 97.83 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 96.76 (+1.1%), 50d 95.02 (+3.0%), 200d 89.77 (+9.0%); 50d above 200d
Momentum: RSI(14) 56.3 | MACD 0.657 vs signal 0.703 (histogram -0.046)
Returns: 1d +0.9% | 5d +0.3% | 1m +3.8% | 3m +0.9%
52-week range: 78.36 - 98.56 (now 96.4% of the way up)
Volatility: ATR(14) 1.34 (1.4% of price) | annualised 20d 14.5%
Volume: 0.43x the 20-day average
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
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 4.3% of open interest (22,625 contracts)
Change on the week: +1.5% of open interest
Crowding: 38% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 234.82M | fund size: 22.97B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWL is a focused Swiss equity fund holding large-cap names (Roche, Novartis, Nestle, UBS, Richemont). Technicals show a weak picture: the fund trades 1.7–2.9% below its 20d, 50d, and 200d moving averages, RSI at 42 signals mild oversold conditions, and MACD remains negative with a deteriorating histogram. The one-month return of −4.4% reflects downward pressure. However, the broader macro backdrop is stable: the yield curve is normally sloped, the Fed is holding steady with modest rate expectations, and VIX at 14.62 reflects calm markets. No macro surprise or policy catalyst has emerged. On valuation, the fund trades at a P/E of 24.65 and P/B of 4.25, which is elevated but not shocking for quality Swiss equities. Analyst coverage of the top 5 holdings (48.5% of the fund) shows 74.5% buy-rated and a +9.4% consensus price target, which is mildly supportive but insufficient to overcome the technical weakness in isolation. Volume is light at 0.31x the 20-day average, and fund flow conviction cannot be read (insufficient data). The three-year performance at +12.1% annually and 0.91 beta suggest steady exposure to broad market health, but near-term momentum is unfavorable. Without a clear macro catalyst, a decisive technical reversal, or a material shift in fund flows, the case remains equivocal. A small long bias is warranted only by analyst upside and valuation stability, tempered by technical underperformance.

**Main reasons it gave:**
- Price 1.7–2.9% below 20d, 50d, 200d SMAs; RSI 42 and negative MACD suggest recent selling pressure
- Analyst consensus 74.5% buy on top 48.5% of holdings; +9.4% price target provides modest floor
- No macro catalyst; stable curve, calm VIX, and steady Fed backdrop offer neutral environment
- One-month return −4.4% and light volume (0.31x 20d average) indicate weak near-term conviction

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 60.94 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 62.00 (-1.7%), 50d 62.76 (-2.9%), 200d 61.54 (-1.0%); 50d above 200d
Momentum: RSI(14) 42.2 | MACD -0.839 vs signal -0.686 (histogram -0.152)
Returns: 1d +1.5% | 5d +0.7% | 1m -4.4% | 3m -0.5%
52-week range: 53.86 - 65.08 (now 63.1% of the way up)
Volatility: ATR(14) 0.70 (1.1% of price) | annualised 20d 13.9%
Volume: 0.31x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 48.5% of the fund by weight
Ratings by weight: buy 74.5% | hold 25.5% | sell 0.0% (mean 2.40 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.4% above the current prices
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
Shares outstanding: 28.62M | fund size: 1.74B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWN is a focused Netherlands equity ETF held back by mixed momentum and macro headwinds. The technical picture is conflicted: the fund sits 76% of the way up its 52-week range and trades near its 20-day and 50-day SMAs, suggesting consolidation rather than conviction. RSI at 48.8 and negative MACD histogram show momentum has faded despite recent 1.1% daily gain and 1.9% five-day strength; the one-month -1.7% and three-month -4.1% returns reveal underlying weakness. Volume is critically thin at 0.03x the 20-day average, signaling low conviction from buyers. The macro backdrop is neutral to slightly restrictive: the dollar strengthened 0.90 on the week to 100.36, which pressures EM-adjacent holdings; US rates are stable with an upward-sloping curve and VIX calm at 14.62, removing tail-risk hedging demand. Fund fundamentals are reasonable—P/E 18.97, 4.1% yield, three-year +23.3% annually—and analyst coverage of the top 44% shows 100% buy ratings with +33.1% upside, a positive signal. However, a fresh initiation by Rothschild on Nebius (4.3% of fund) with a Sell rating on 2026-09-21 clouds the near-term outlook for a core holding. The fund's 1.14 beta and concentration in Technology (31.5%) and Financials (21.4%) leave it exposed to rate-sensitive sectors at a moment when US yields are stable but the market is pricing only modest Fed cuts ahead. No news in 24 hours and extremely light volume suggest the market is waiting for clarity. The case for conviction either way is absent.

**Main reasons it gave:**
- RSI momentum fade at 48.8 and negative MACD histogram despite recent gains
- Volume critically thin at 0.03x 20-day average
- Dollar strength +0.90 on week pressures non-USD holdings
- Fresh Sell-rated initiation on Nebius (4.3% of fund) by Rothschild on 2026-09-21
- 100% buy ratings from analysts with +33.1% weighted price target on top 44% of holdings, offset by technical consolidation

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 67.78 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 67.99 (-0.3%), 50d 68.15 (-0.6%), 200d 63.91 (+6.0%); 50d above 200d
Momentum: RSI(14) 48.8 | MACD -0.474 vs signal -0.354 (histogram -0.121)
Returns: 1d +1.1% | 5d +1.9% | 1m -1.7% | 3m -4.1%
52-week range: 55.33 - 71.61 (now 76.4% of the way up)
Volatility: ATR(14) 0.89 (1.3% of price) | annualised 20d 14.3%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 44.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.60 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +33.1% above the current prices
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
Shares outstanding: 5.55M | fund size: 376.15M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWP is a focused Spain equity fund holding 99.7% stocks with exposure concentrated in financials (45.4%) and utilities (20.0%). The macro backdrop shows a normal, upward-sloping yield curve with short-end rates up modestly on the week; the dollar has strengthened but volatility remains calm at 14.62 VIX. No material news flow in the past 24 hours. Technicals present a mixed picture: the fund sits 7.2% above its 200-day moving average with a healthy three-year return of 33.6% annualized, but momentum is neutral-to-weak (RSI 47.9, MACD histogram negative), the one-month return is negative at -1.4%, and today's volume is well below average at 0.10x the 20-day. The price sits at 87.6% of the 52-week range, near recent highs. Fund basics show reasonable valuation (P/E 16.28, P/B 2.22) with a 2.7% yield, and analyst coverage of the top 5 holdings (54.5% of assets) shows 52% buy and 48% hold ratings with a modest +1.5% weighted price target. Fund flows are indeterminate due to insufficient data. The lack of any recent catalyst, combined with mixed technicals at an elevated level in the 52-week range, weak momentum, and thin volume, argues against conviction in either direction. The fund appears fairly valued on fundamentals with adequate analyst support, but macro conditions are neutral and there is no specific trigger to shift positioning.

**Main reasons it gave:**
- RSI 47.9 and MACD histogram negative despite price near 200-day high
- One-month return -1.4% and volume 0.10x average on day of +1.3% move
- Analysts show modest +1.5% upside on top 54% of holdings but no recent catalysts
- Spain exposure benefits from normal yield curve but lacks rate or policy surprise to drive flows

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 61.37 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 61.96 (-0.9%), 50d 61.45 (-0.1%), 200d 57.27 (+7.2%); 50d above 200d
Momentum: RSI(14) 47.9 | MACD -0.181 vs signal -0.008 (histogram -0.174)
Returns: 1d +1.3% | 5d +0.6% | 1m -1.4% | 3m +3.2%
52-week range: 48.25 - 63.23 (now 87.6% of the way up)
Volatility: ATR(14) 0.79 (1.3% of price) | annualised 20d 15.2%
Volume: 0.10x the 20-day average
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

> EWU is a focused UK equity fund currently trading near the upper end of its 52-week range with no material macro catalyst or news catalyst present. The technical picture is mixed: the fund sits slightly below its 20-day and 50-day moving averages but remains above its 200-day, with momentum indicators (RSI 45.6, MACD histogram negative) showing neither clear strength nor decisive weakness. The three-month return of +4.3% has pulled price near resistance. Volume is notably light at 0.13x the 20-day average, suggesting low conviction on either side. The macro backdrop is stable: the US curve remains normally upsloped, volatility is calm at 14.62, and the Fed path prices modest further tightening. Sterling is embedded in a stronger dollar environment (+0.90 on the week), a minor headwind for UK equities. Analyst coverage of the top 36% of holdings shows a constructive tilt (buy 57.5%, hold 42.5%) with a +10.9% weighted price target, but this rolls up a thin fraction of the fund and reflects analyst positioning rather than a catalyst. The fund's valuation (P/E 17.08, P/B 2.29) is neither compelling nor alarming. Fund flows data is insufficient to infer conviction. The lack of any directional catalyst—no policy surprise, no earnings surprise, no technical breakout on volume—argues for a neutral stance with minimal conviction. The modest analyst upside and position in the upper half of the range offer marginal support, but not enough to override the absence of a clear trigger.

**Main reasons it gave:**
- No macro or policy catalyst present; stable rate environment with normal curve
- RSI at 45.6 and negative MACD histogram show no clear momentum; light volume (0.13x) reflects low conviction
- Price near 52-week high with resistance; sitting below both 20d and 50d SMAs
- Analyst roll-up on top 36% holdings shows +10.9% weighted target, but thin coverage and no fresh catalyst
- Stronger US dollar (+0.90 on week) a modest headwind for UK equity exposure

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 47.67 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 48.21 (-1.1%), 50d 47.96 (-0.6%), 200d 46.52 (+2.5%); 50d above 200d
Momentum: RSI(14) 45.6 | MACD -0.154 vs signal -0.043 (histogram -0.112)
Returns: 1d +0.9% | 5d -0.5% | 1m -1.8% | 3m +4.3%
52-week range: 41.04 - 49.39 (now 79.5% of the way up)
Volatility: ATR(14) 0.47 (1.0% of price) | annualised 20d 11.3%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

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
Rolled up from the 5 largest holdings, 36.0% of the fund by weight
Ratings by weight: buy 57.5% | hold 42.5% | sell 0.0% (mean 2.18 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.9% above the current prices
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
Shares outstanding: 80.06M | fund size: 3.82B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWW (iShares MSCI Mexico ETF) is a focused regional fund trading 3.0-3.2% below its 20-, 50- and 200-day moving averages in a still-uptrend structure (50d above 200d). Momentum is deteriorating: RSI at 38.4 suggests weakness, MACD histogram is negative, and recent returns are negative across all horizons (1d flat, 5d -1.9%, 1m -2.8%). Volume is well below average at 0.30x the 20-day mean, indicating low conviction in either direction. Macro backdrop is mixed: the US dollar strengthened +0.90 this week to 100.36, which is headwind for emerging-market equities; US yields are stable to slightly higher at the short end; the Fed is expected to cut rates modestly over two years, but the immediate picture is firm. On the positive side, analyst coverage of the fund's 5 largest holdings (48% of weight) shows unanimous buy ratings with an 18% price target upside; the fund's 3-year return of +10.7% annually and 3.2% yield are respectable. However, fund basics show modest valuation (P/E 12.68, P/B 1.98) and the holdings are concentrated in cyclical sectors (basic materials 27%, financials 20%) that are sensitive to both currency moves and global growth. The recent USD strength and lack of positive catalysts in the past 24 hours, combined with deteriorating technicals and low volume, do not justify a directional call. The analyst upside is noted but is forward-looking and does not override the current momentum weakness and flow uncertainty. A neutral stance is appropriate pending either a technical reversal on improved volume or a material shift in macro conditions (Fed policy surprise, notable data beat, or dollar reversal).

**Main reasons it gave:**
- RSI 38.4 and negative MACD histogram signal weakening momentum
- Volume 0.30x 20-day average shows low conviction on any move
- USD +0.90 on week headwind for EM equity fund
- Analyst buy consensus on 48% of fund with 18% price target, but not reflected in current price action
- Price 3.0-3.2% below all key moving averages in still-intact uptrend

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 73.42 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 75.75 (-3.1%), 50d 75.86 (-3.2%), 200d 75.67 (-3.0%); 50d above 200d
Momentum: RSI(14) 38.4 | MACD -0.716 vs signal -0.386 (histogram -0.330)
Returns: 1d +0.1% | 5d -1.9% | 1m -2.8% | 3m -3.3%
52-week range: 64.39 - 81.23 (now 53.6% of the way up)
Volatility: ATR(14) 1.26 (1.7% of price) | annualised 20d 14.8%
Volume: 0.30x the 20-day average
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
Three-year record: +10.7% a year | beta to the market 1.05
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 47.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.06 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.0% above the current prices
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

### Brazil (EWZ) · Sector or country — NEUTRAL, confidence 0.25

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> EWZ has run +11% in a month and sits 71% up its 52-week range, but momentum is flattening (MACD histogram slightly negative, volume 0.4x average) and the 50d remains below the 200d. No macro catalyst this cycle: US yields essentially unchanged, curve normally sloped, VIX calm at 14.6, though a firmer dollar (+0.90) and a bond market pricing hikes rather than cuts is a mild headwind for Brazilian equities. Valuation is cheap (P/E 10.5, 4.1% yield) and analyst coverage of the top 40.9% of the fund is 100% buy with +22.8% targets, which supports the medium term but is not a timing signal after a double-digit run. Flows data insufficient. Staying neutral with a modest constructive tilt.

**Main reasons it gave:**
- +11.2% in one month, 71% of 52-week range, but MACD histogram negative and volume 0.4x average
- 50d SMA still below 200d despite price above both
- Top-5 holdings (40.9% weight) 100% buy-rated, +22.8% weighted price target
- Dollar index +0.90 on the week and 2y at 4.67% pricing hikes — headwind for EM
- No macro or Brazil-specific news in the window; VIX 14.6 and 10y unchanged

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.25</summary>

```text
Last close 37.98 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 37.22 (+2.0%), 50d 36.08 (+5.3%), 200d 36.20 (+4.9%); 50d below 200d
Momentum: RSI(14) 60.5 | MACD 0.636 vs signal 0.669 (histogram -0.033)
Returns: 1d +1.2% | 5d +0.7% | 1m +11.2% | 3m +10.8%
52-week range: 28.79 - 41.73 (now 71.0% of the way up)
Volatility: ATR(14) 0.78 (2.1% of price) | annualised 20d 21.9%
Volume: 0.40x the 20-day average
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
Three-year record: +11.5% a year | beta to the market 0.84
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 40.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.8% above the current prices
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
Shares outstanding: 200.55M | fund size: 7.62B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EZA is a focused South African equity fund heavily weighted to gold miners (23.6% combined: Anglogold, Gold Fields) and financials (33.2%). The technical picture is mixed: the fund sits 1.2% above its 50-day MA but 3.0% below the 20-day, momentum is weak (RSI 45.6, MACD histogram -0.501), and volume is 0.17x average suggesting low conviction. The 50-day MA sits below the 200-day, indicating a downtrend over intermediate timeframes, though the fund is only 36% of the way up its 52-week range. Macro conditions are stable: the dollar strengthened 0.90 on the week to 100.36, which typically pressures gold prices and SA equities; Treasury yields are steady (10-year flat on the week); and VIX declined to 14.62, indicating calm risk appetite. Analyst view is bullish (100% buy-rated holdings with +23.7% upside to targets), but this covers only 45.6% of the fund's holdings and reflects sentiment on the largest names rather than conviction in the fund itself. There is no news catalyst in the past 24 hours, no insider positioning data, and no clear macro surprise to act on. The three-year annual return of +28.3% is backward-looking and does not inform near-term direction. The combination of weak technicals, a stronger dollar headwind, subdued volume, and absence of a fresh catalyst does not support a directional call. The bullish analyst overlay is noted but insufficient to overcome the technical weakness given the fund's regional and sector concentration.

**Main reasons it gave:**
- RSI 45.6 and MACD histogram -0.501 show weak momentum despite 3m gain of +4.6%
- US dollar strengthened 0.90 on week to 100.36, headwind for gold and SA equities
- 50-day MA below 200-day MA signals intermediate downtrend
- Analyst buy-rating and +23.7% upside target covers only 45.6% of fund holdings
- Volume 0.17x average indicates low participation in current price action

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 68.11 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 70.19 (-3.0%), 50d 67.30 (+1.2%), 200d 69.26 (-1.7%); 50d below 200d
Momentum: RSI(14) 45.6 | MACD 0.048 vs signal 0.549 (histogram -0.501)
Returns: 1d -0.6% | 5d -0.6% | 1m -3.3% | 3m +4.6%
52-week range: 60.43 - 81.60 (now 36.3% of the way up)
Volatility: ATR(14) 1.27 (1.9% of price) | annualised 20d 21.7%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

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
Rolled up from the 5 largest holdings, 45.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.82 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.7% above the current prices
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
Shares outstanding: 7.90M | fund size: 538.07M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> INDA faces headwinds from weakening technicals and macro crosscurrents, partially offset by analyst optimism on its largest holdings. The fund is trading below its 20d, 50d, and 200d SMAs with the 50d below the 200d, signaling a bearish trend structure. Momentum is deteriorating: RSI at 43.9 is below 50 and MACD histogram is negative. The 3-month return of -3.1% and position at the 29.9th percentile of the 52-week range indicate downward pressure. Macro conditions are mixed: the US dollar strengthened 0.90% this week to 100.36, which typically pressures emerging markets; Treasury yields are broadly stable at elevated levels, keeping carry costs high. The curve is normally sloped and VIX is calm at 14.62, so panic is not priced in. On the positive side, analyst coverage of the top 5 holdings (24.7% of the fund) shows 100% buy ratings with a weighted price target 30.2% above current levels, suggesting conviction among analysts on the largest positions. However, this view covers less than 25% of the fund and is thin as a read on the whole. Fund basics show a P/E of 22.87 and P/B of 3.14, which are reasonable for India equity but not cheap, and the 3-year 2.3% annualized return trails broad markets. The absence of flow data and very light volume (0.17x average) limit confidence in either direction. The technical deterioration and strong dollar are offset but not overcome by analyst bullishness on a narrow slice. This warrants a small lean to caution while acknowledging the analyst case remains intact.

**Main reasons it gave:**
- 50d SMA below 200d, price below all key moving averages
- US dollar +0.90% on the week pressures emerging market equity
- Analyst roll-up shows +30.2% price target on largest 5 holdings but covers only 24.7% of fund
- RSI 43.9 and negative MACD histogram indicate deteriorating momentum
- 3-month return -3.1% with position at 52-week low quartile

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 48.38 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 48.99 (-1.3%), 50d 49.22 (-1.7%), 200d 50.13 (-3.5%); 50d below 200d
Momentum: RSI(14) 43.9 | MACD -0.427 vs signal -0.309 (histogram -0.118)
Returns: 1d +0.7% | 5d -0.1% | 1m -2.4% | 3m -3.1%
52-week range: 45.42 - 55.29 (now 29.9% of the way up)
Volatility: ATR(14) 0.45 (0.9% of price) | annualised 20d 14.5%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.05</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 24.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.36 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.2% above the current prices
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
Shares outstanding: 141.66M | fund size: 6.85B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> KRE is a regional bank ETF trading below its key moving averages (20d, 50d) with momentum weakening (RSI 35.7, MACD histogram negative), suggesting near-term technical fragility. However, the macro backdrop does not yet support a bearish call: the yield curve is normal and upward sloping at +0.98, treasury yields are stable on the week, the dollar has strengthened modestly (+0.90), and the VIX is calm at 14.62. Inflation at 3.4% and unemployment at 4.1% are not crisis signals. The Fed's priced path implies modest easing ahead (3 quarter-point cuts priced over two years), which could support financials, but the fund's valuation (P/E 12.60, P/B 1.27) is not expensive enough to have priced in a rally. Analyst coverage of the five largest holdings (7.1% of the fund) shows 65.9% buy ratings and a weighted +19.4% price target, with recent upgrades from Morgan Stanley and UBS, but this thin coverage—one-fifteenth of the fund—limits its force. No news, unknown flows, and sub-average volume (0.34x) suggest low conviction in either direction. The technical weakness is real but not yet a breakdown, and the macro regime is neutral. The call is neutral with low conviction, held by near-term downside momentum offset by the lack of a macro catalyst to justify a more aggressive bearish stance and modest analyst support for the largest holdings.

**Main reasons it gave:**
- RSI 35.7 and negative MACD histogram show weakening momentum
- price -2% to -4% below 20d and 50d SMAs signals near-term technical weakness
- yield curve normal and upward-sloping at +0.98, supporting financial sector thesis
- analyst view of top 5 holdings shows 65.9% buy and +19.4% price target but covers only 7.1% of fund
- below-average volume and unknown flows indicate low conviction

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 72.34 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 73.85 (-2.0%), 50d 75.32 (-4.0%), 200d 70.39 (+2.8%); 50d above 200d
Momentum: RSI(14) 35.7 | MACD -0.691 vs signal -0.547 (histogram -0.144)
Returns: 1d -0.6% | 5d -2.4% | 1m -3.2% | 3m +0.5%
52-week range: 58.14 - 77.93 (now 71.8% of the way up)
Volatility: ATR(14) 1.20 (1.7% of price) | annualised 20d 14.3%
Volume: 0.34x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 7.1% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 65.9% | hold 34.1% | sell 0.0% (mean 2.04 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.4% above the current prices
Holdings read: CFR, SSB, BPOP, PNFP, UMBF
Recent rating changes among them:
  - CFR: 2026-09-08 Morgan Stanley: up, Underweight -> Overweight
  - SSB: 2026-07-28 Citigroup: main, Buy -> Buy
  - BPOP: 2026-08-31 Benchmark: main, Buy -> Buy
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
Shares outstanding: 55.11M | fund size: 3.99B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> KSA is a focused Saudi Arabia equity fund holding high-quality blue chips with strong analyst support (90% buy ratings, +15.1% price target on 44% of holdings). Valuation is reasonable at 15x P/E with 2.7% yield. However, technicals are deteriorating: price is below all three moving averages (20d, 50d, 200d), momentum is weak (RSI 31.5, MACD negative with histogram -0.190), and the fund is down 3.1% over one month on below-average volume. The 52-week range shows KSA near the lower quartile. Macro backdrop is calm (VIX 14.6, curve normal at +98 bps), but oil headlines are mixed—Hormuz shipments hit six-month highs yet WTI fell below $100, and Saudi production constraints offer limited tailwind. The custodian appointment to HSBC is a positive structural development but is institutional plumbing, not a price catalyst. Fund flows data is insufficient to read conviction. The combination of solid fundamentals and analyst sentiment is offset by clear technical weakness and lack of a near-term macro or idiosyncratic catalyst to reverse the downtrend. This warrants a modest bearish lean rather than outright NEUTRAL given the technical deterioration, but analyst support and reasonable valuation prevent a stronger conviction.

**Main reasons it gave:**
- RSI 31.5 with price below all three moving averages (20d, 50d, 200d)
- MACD negative with histogram -0.190 and one-month return -3.1%
- Analysts rate 90% buy on 44% of holdings with +15.1% price target
- P/E 15.0 and 2.7% yield provide valuation cushion despite recent weakness
- Oil headlines mixed; Hormuz shipments highest in 6 months but WTI fell below $100

<details><summary><b>News</b> — score +0.10</summary>

- [HSBC Saudi Arabia named custodian to Al Rajhi MSCI Saudi Arabia ETF](https://www.globalcustodian.com/hsbc-saudi-arabia-named-custodian-to-al-rajhi-msci-saudi-arabia-etf/)  
  <sub>Global Custodian, 3 hours ago</sub>  
  Custody. HSBC Saudi Arabia named custodian to Al Rajhi MSCI Saudi Arabia ETF. Mandate adds to HSBC Saudi Arabia's growing ETF and securities services...
- [Hormuz Oil Shipments Hit Six-Month High? ETFs to Win/Lose](https://www.tradingview.com/news/zacks:9ed16a4fe094b:0-hormuz-oil-shipments-hit-six-month-high-etfs-to-win-lose/)  
  <sub>TradingView, 3 hours ago</sub>  
  Oil and liquefied natural gas shipments through the Strait of Hormuz reached their highest level in six months over the past two weeks, indicating that...
- [Oil Near $100, Treasury Yields Near 5%, Bitcoin’s Resilience: 3 Charts To Watch This Week](https://www.tradingview.com/news/stocktwits:c7de3f4f9094b:0-oil-near-100-treasury-yields-near-5-bitcoin-s-resilience-3-charts-to-watch-this-week/)  
  <sub>TradingView, 6 hours ago</sub>  
  WTI crude oil futures fell back below $100 a barrel Monday after Saudi Arabia said its East-West pipeline could restore about half of its capacity within...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.55</summary>

```text
Last close 37.06 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 38.34 (-3.4%), 50d 37.79 (-1.9%), 200d 38.14 (-2.8%); 50d below 200d
Momentum: RSI(14) 31.5 | MACD -0.215 vs signal -0.026 (histogram -0.190)
Returns: 1d -1.0% | 5d -2.0% | 1m -3.1% | 3m -3.3%
52-week range: 35.83 - 41.03 (now 23.6% of the way up)
Volatility: ATR(14) 0.30 (0.8% of price) | annualised 20d 11.4%
Volume: 0.50x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.65</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.65</summary>

```text
Rolled up from the 5 largest holdings, 44.4% of the fund by weight
Ratings by weight: buy 90.0% | hold 10.0% | sell 0.0% (mean 2.06 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.1% above the current prices
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
Shares outstanding: 17.03M | fund size: 631.15M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> MCHI is a concentrated China regional fund facing conflicting signals with no clear catalyst for direction change. On the positive side, analyst coverage of its five largest holdings (32% of the fund) is unanimously bullish with a +52.8% weighted price target, and the fund's valuation metrics (P/E 11.90, P/B 1.39) remain attractive relative to developed markets. The three-year return of +9.1% annually and 2.0% yield provide income support. However, technicals are weak: the price is down 6.2% from its 200-day moving average, momentum is soft (RSI 47.7, MACD histogram negative), and volume is well below average at 0.28x the 20-day mean, suggesting weak conviction. The macro backdrop is mixed: a strengthening dollar (+0.90 on the week) typically headwinds China equities, while the Fed's rate path and Treasury moves show modest policy changes rather than a clear catalyst. Most critically, the news of China's sharp decline in rare earth exports to the US ahead of a Trump-Xi summit introduces geopolitical risk to the China exposure without yet being priced as a decisive break. The fund's low beta of 0.44 to broader markets and its 6.3B in assets suggest it moves with China-specific factors rather than global equity sentiment. With technicals lagging fundamentals, no analyst rating changes among major holdings, and macro signals ambiguous, the risk-reward lacks a clear directional edge. A material catalyst would require either a surprise improvement in China growth data, a geopolitical de-escalation, or a decisive technical break above resistance.

**Main reasons it gave:**
- Analyst consensus on top 5 holdings 100% buy with +52.8% weighted price target
- Price down 6.2% from 200-day SMA with RSI 47.7 and negative MACD histogram
- China rare earth exports to US fell sharply, adding geopolitical uncertainty ahead of Trump-Xi summit
- Fund valuation (P/E 11.90, P/B 1.39) attractive but volume 0.28x average signals weak institutional demand
- Dollar strength (+0.90 on week) typically headwind for China equities with no offsetting domestic catalyst

<details><summary><b>News</b> — score -0.15</summary>

- [ETFs Investing in AAC Technologies Holdings Inc. Stocks](https://www.tradingview.com/symbols/DUS-A2XN/etfs/)  
  <sub>TradingView, 20 hours ago</sub>  
  Explore funds investing in A2XN in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [China's rare earth exports to US drop ahead of Trump-Xi summit](https://invezz.com/uk/news/2026/09/21/chinas-rare-earth-exports-to-us-fall-20percent-ahead-of-trump-xi-summit/)  
  <sub>Invezz, 4 hours ago</sub>  
  China's shipments of rare earth magnets to the US fell sharply last month, according to official Chinese customs data released Sunday.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.15</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 53.67 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 53.96 (-0.5%), 50d 54.47 (-1.5%), 200d 57.22 (-6.2%); 50d below 200d
Momentum: RSI(14) 47.7 | MACD -0.500 vs signal -0.419 (histogram -0.080)
Returns: 1d +1.1% | 5d +0.7% | 1m -3.3% | 3m +1.5%
52-week range: 50.48 - 66.99 (now 19.4% of the way up)
Volatility: ATR(14) 0.60 (1.1% of price) | annualised 20d 13.7%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

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
Rolled up from the 5 largest holdings, 32.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +52.8% above the current prices
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
Shares outstanding: 120.50M | fund size: 6.47B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> TUR is a Turkish equities fund with modest positive technical headwinds balanced by supportive fundamentals and analyst sentiment. The fund trades 4.4–4.9% below its moving averages across the 20d, 50d, and 200d, with RSI(14) at 40.4 indicating neither oversold nor strongly bearish conditions; momentum (MACD histogram -0.358) is negative but not extreme. The 50d SMA below the 200d suggests a primary downtrend, though the 1-month pullback of 6.8% is moderate in the context of the fund's 34.5% annualised volatility. Volume is light at 0.22x average, reducing conviction in the directional move. On the fundamental side, the fund's valuation (P/E 13.81, P/B 1.21, P/S 0.66) is attractive, and the 2.1% yield provides modest income support. Analyst coverage of the top 39.5% of holdings shows 100% buy ratings with a +16.2% weighted price target, a constructive signal. However, the macro backdrop is mixed: the US dollar has strengthened +0.90 this week, which historically pressures emerging markets including Turkish assets; Treasury yields are broadly flat to up slightly, maintaining elevated carry costs; and VIX is calm at 14.62, suggesting low market stress but also reduced risk appetite for EM exposure. Fund flows data are unavailable, and no news was found in the past 24 hours. The combination of technical weakness, a strengthening dollar, and light volume prevents a bullish lean despite the attractive valuation and analyst optimism. A modest neutral-to-slightly-bullish lean is warranted by fundamentals and analyst consensus, but macro headwinds and technical deterioration constrain conviction.

**Main reasons it gave:**
- Price 4.4–4.9% below 20d, 50d, and 200d SMAs with 50d below 200d
- RSI(14) 40.4 and MACD histogram -0.358 show modest negative momentum
- Attractive valuation (P/E 13.81, P/B 1.21, P/S 0.66) and 2.1% yield
- Analyst consensus 100% buy on top 39.5% of holdings with +16.2% price target
- US dollar +0.90 on the week pressures emerging market assets

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 37.55 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 39.49 (-4.9%), 50d 39.23 (-4.3%), 200d 39.26 (-4.4%); 50d below 200d
Momentum: RSI(14) 40.4 | MACD -0.517 vs signal -0.159 (histogram -0.358)
Returns: 1d +0.7% | 5d -5.6% | 1m -6.8% | 3m -7.3%
52-week range: 31.90 - 43.74 (now 47.7% of the way up)
Volatility: ATR(14) 0.77 (2.1% of price) | annualised 20d 34.5%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.45</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 39.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.2% above the current prices
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
Shares outstanding: 15.65M | fund size: 587.66M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> VNQ sits in a weak technical position with price below its 20-, 50- and 200-day SMAs, RSI at 37 suggesting oversold conditions, and negative MACD histogram indicating momentum erosion. The 1-month -4.8% drawdown shows recent underperformance. However, several offsetting factors prevent a bearish call: (1) the 50d SMA remains above 200d, so the uptrend structure is intact despite the pullback; (2) the yield curve is normal and upward-sloping at +98bp, supporting real estate; (3) VIX at 14.62 is calm, reducing near-term stress; (4) analyst consensus on the top 39.9% of holdings is unanimously bullish with a +16.7% weighted price target; (5) recent rating upgrades (Equinix Buy initiation, Barclays upgrade AMT to Overweight) show fresh positive sentiment. The macro backdrop is stable: inflation at 3.4% is not deflationary, unemployment 4.1% is moderate, and the Fed rate path prices only modest tightening. Treasury yields are essentially flat for the week. Fund flows data is too sparse to read. The technical weakness argues against conviction bullish, but the combination of beaten-down price (48.9% of 52-week range), oversold RSI, intact trend structure, and strong analyst backing on core holdings suggests limited downside risk and modest upside potential from here. A small bounce is plausible but not a high-conviction signal.

**Main reasons it gave:**
- Price below all major SMAs with RSI 37, momentum negative but trend structure intact
- Analyst consensus +100% buy on top 39.9% of holdings with +16.7% price target
- Normal yield curve +98bp and calm VIX 14.62 support real estate asset class
- Recent rating upgrades (EQIX Buy initiation, AMT upgrade) show fresh sentiment lift

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 93.82 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 95.76 (-2.0%), 50d 97.59 (-3.9%), 200d 94.31 (-0.5%); 50d above 200d
Momentum: RSI(14) 37.4 | MACD -1.215 vs signal -1.018 (histogram -0.197)
Returns: 1d +1.0% | 5d -0.5% | 1m -4.8% | 3m -2.9%
52-week range: 87.00 - 100.95 (now 48.9% of the way up)
Volatility: ATR(14) 1.12 (1.2% of price) | annualised 20d 10.4%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.74 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.7% above the current prices
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
Shares outstanding: 757.71M | fund size: 71.09B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLB is caught between offsetting technical and fundamental signals with no clear catalyst. Technicals are weak: the fund trades 3.9% below its 20-day moving average with RSI at 34.3, MACD in negative territory, and a one-month decline of -5.0%, but volume is light at 0.35x average, which limits the signal's conviction. The fund is down only -1.2% from its 200-day MA, suggesting the weakness is relatively recent rather than a regime break. Macro backdrop is stable: Treasury yields moved modestly, the yield curve is normally upsloped at +0.98, the dollar firmed but modestly, and the VIX fell to 14.62 in calm conditions. The Fed has priced rate cuts ahead but no shock has occurred. On valuation, the fund's P/E of 24.59 and P/B of 3.00 are elevated for a materials fund, and GuruFocus flags overvaluation, though that is a static call not a change. Analyst coverage of the top 37% of holdings is uniformly bullish—100% buy-rated with a +14.5% weighted price target—which would normally support a mild bullish lean, but this coverage is thin as a fraction of the total fund and there are no recent upgrades of consequence, just maintenance ratings. Fund flows data is insufficient. The one-month drawdown is material but lacks a macro or earnings shock to explain it, and light volume suggests it may not be conviction-driven selling. This is a wait-and-see setup: technicals have turned sour but not decisively, fundamentals are not visibly deteriorating, and the macro calendar offers no imminent catalyst. A break below the 200-day MA with volume, or a clear macro shift, would warrant a bearish reassessment.

**Main reasons it gave:**
- RSI 34.3 and MACD negative histogram, fund 3.9% below 20-day MA
- Light volume on weakness limits conviction of technical breakdown
- Analyst consensus 100% buy-rated with +14.5% price target on largest holdings
- Valuation elevated at P/E 24.59 and P/B 3.00 relative to materials peers
- Macro backdrop stable: yield curve normal, VIX calm, no Fed surprise

<details><summary><b>News</b> — score +0.00</summary>

- [XLB Looks 3.0% Overvalued on GF Value™ as Dividend Sustainabilit](https://www.gurufocus.com/news/9089824/xlb-looks-30-overvalued-on-gf-value-as-dividend-sustainability-remains-key)  
  <sub>GuruFocus, 2 hours ago</sub>  
  On September 21, 2026, the S&P Select Materials SPDR (ticker: XLB) established critical pivot points using the DeMark calculation method, setting a pivot...
- [Leading And Lagging Sectors For September 21, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61894029/leading-and-lagging-sectors-september-21-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLK) State Street Technology Select Sector SPDR ETF 191.7700 2.170 1.14 39.0K (NYSE:XLC) State...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 49.81 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 51.86 (-3.9%), 50d 51.75 (-3.7%), 200d 50.43 (-1.2%); 50d above 200d
Momentum: RSI(14) 34.3 | MACD -0.586 vs signal -0.321 (histogram -0.265)
Returns: 1d -0.4% | 5d -1.3% | 1m -5.0% | 3m -3.5%
52-week range: 42.23 - 53.67 (now 66.3% of the way up)
Volatility: ATR(14) 0.77 (1.5% of price) | annualised 20d 12.4%
Volume: 0.35x the 20-day average
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
Weighted price target: +14.5% above the current prices
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
Shares outstanding: 71.92M | fund size: 3.58B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLE is trading near 52-week highs with positive 3-year returns and 100% analyst buy ratings on its top holdings, supported by a +5.4% weighted price target. However, near-term technicals are showing deterioration: the price is 2.1% below the 20-day moving average, momentum has rolled over (RSI 46.9, MACD histogram negative at -0.354), and volume is well below average at 0.49x. Recent price action shows -2.5% on the day and -2.8% over five days despite broader market strength. The energy backdrop is mixed: crude inventories drew 0.6M barrels (bullish) but remain at only the 38th percentile, while petrol inventories built to a 52-week low (bearish signal for demand). The EIA price outlook calls for WTI to decline ~10% over six months to $79/barrel, a headwind for energy sector valuations. Macro conditions are stable with a normalized yield curve, low volatility (VIX 14.6), and the dollar firmer week-over-week. Strait of Hormuz shipments hitting a six-month high and supertanker supply constraints are modest supply-side supports, but insufficient to overcome the combination of near-term technical weakness, soft inventory demand signals, and a downward price forecast. Fund flows data is incomplete, limiting conviction on positioning. The call reflects cautious positioning ahead of what could be further consolidation, with no clear catalyst to justify a directional lean.

**Main reasons it gave:**
- Momentum rolling over: RSI 46.9 and MACD histogram -0.354 after price break below 20d MA
- EIA six-month crude forecast down ~10% to $79/barrel; three-month forecast down to $84.50
- Petrol inventories at 13th percentile despite seasonal build, signaling weak demand
- 100% buy ratings from analysts with +5.4% weighted price target offset by technical deterioration
- Volume 0.49x average during down move, suggesting lack of conviction in recent weakness

<details><summary><b>News</b> — score -0.15</summary>

- [Exchange-Traded Funds Rise, Equity Futures up Pre-Bell Monday as Oil Prices Decline](https://www.moomoo.com/news/post/76538074/exchange-traded-funds-rise-equity-futures-up-pre-bell-monday)  
  <sub>Moomoo, 1 hour ago</sub>  
  Thebroad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.7% and the actively traded Invesco QQQ Trust (QQQ) advanced 1.1% in Monday's...
- [SCHD: Why I Think This ETF Still Wins In A Rate Hike Cycle (NYSEARCA:SCHD)](https://seekingalpha.com/article/4948157-schd-why-i-think-this-etf-still-wins-in-a-rate-hike-cycle)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Summary. Schwab U.S. Dividend Equity ETF (SCHD) remains a core buy for income-focused portfolios, leveraging disciplined methodology and low-cost structure.
- [Hormuz Oil Shipments Hit Six-Month High? ETFs to Win/Lose](https://www.tradingview.com/news/zacks:9ed16a4fe094b:0-hormuz-oil-shipments-hit-six-month-high-etfs-to-win-lose/)  
  <sub>TradingView, 3 hours ago</sub>  
  Oil and liquefied natural gas shipments through the Strait of Hormuz reached their highest level in six months over the past two weeks, indicating that...
- [Leading And Lagging Sectors For September 21, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61894029/leading-and-lagging-sectors-september-21-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLK) State Street Technology Select Sector SPDR ETF 191.7700 2.170 1.14 39.0K (NYSE:XLC) State...
- [Futures Rise: Can Market Take Off? 2026's Top Stocks Are Buys](https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-robinhood-sandisk-amd-moderna-surge-buy-areas/)  
  <sub>Investor's Business Daily, 3 hours ago</sub>  
  Dow Jones futures: The stock market is set for a positive start to the week with Robinhood, Sandisk, AMD and Moderna already in buy areas.
- [Crude Oil Weekly Outlook: BRICS Summit Calls for Maximum Restraint](https://www.stonex.com/en-gb/news-and-analysis/crude-oil-weekly-outlook-brics-summit-calls-for-maximum-restraint/)  
  <sub>www.stonex.com, 10 hours ago</sub>  
  The BRICS summit called for maximum restraint this weekend as the energy crisis reaches critical economic tipping points. Diplomacy was presented as the...
- [Oil supertanker shortage: Another risk for gas prices](https://seekingalpha.com/news/4644620-oil-supertanker-shortage-another-risk-for-gas-prices)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  There's now a shortage of oil supertankers, adding more pressure on gasoline prices, with shipping rates reaching record levels around the world.
- [Silver Jumps 3% While Copper Surges 2.2% And Gold Breaks Hig](https://www.kucoin.com/news/insight/XLE/6ab02e2662cf3700074382dc)  
  <sub>KuCoin, 20 hours ago</sub>  
  Silver Jumps 3% While Copper Surges 2.2% And Gold Breaks Higher ~ Monday Market Moves Full Episode: https://t.co/ze6UCHwPEN Rick Rule Mining in Mexico...
- [Qatar Energy CEO counters Bessent: Strait of Hormuz ‘will never be obsolete’ (CL1:COM:Commodity)](https://seekingalpha.com/news/4644605-qatar-energy-ceo-counters-bessent-strait-of-hormuz-will-never-be-obsolete)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  Qatari Energy Minister Saad Al-Kaabi on Sunday said Treasury Secretary Scott Bessent was “wrong” when he said that the strategic Strait of Hormuz will be...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.15</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 62.71 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 64.06 (-2.1%), 50d 61.33 (+2.3%), 200d 55.82 (+12.4%); 50d above 200d
Momentum: RSI(14) 46.9 | MACD 0.805 vs signal 1.159 (histogram -0.354)
Returns: 1d -2.5% | 5d -2.8% | 1m -1.6% | 3m +16.0%
52-week range: 42.61 - 65.93 (now 86.2% of the way up)
Volatility: ATR(14) 1.31 (2.1% of price) | annualised 20d 21.4%
Volume: 0.49x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 51.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.04 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +5.4% above the current prices
Holdings read: XOM, CVX, COP, MPC, PSX
Recent rating changes among them:
  - XOM: 2026-09-03 Piper Sandler: main, Neutral -> Neutral
  - CVX: 2026-09-03 BMO Capital: main, Outperform -> Outperform
  - COP: 2026-09-14 UBS: main, Buy -> Buy
  - MPC: 2026-09-21 Goldman Sachs: main, Buy -> Buy
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
Shares outstanding: 186.42M | fund size: 11.69B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLF is trading 2.6% below its 20-day moving average and shows weak momentum with RSI at 36.6 and a negative MACD histogram, indicating downward pressure. However, the fundamental backdrop remains constructive: the fund's largest holdings (JPM, BRK-B, V, MA, BAC) have unanimous buy ratings from analysts with an +11.6% weighted price target above current prices, and the analyst roll-up covers 41.5% of the fund's weight. The macro environment is benign—a normal upward-sloping yield curve, falling volatility (VIX down 2.5 this week), and a strengthening dollar (+0.90 on the week) which can support financial services stocks. The fund's valuation at P/E 16.36 and P/B 2.42 appears reasonable relative to its 18.8% annualized three-year return and defensive 0.71 beta. The headwind is technical: price is 2.4-2.6% below its 50- and 20-day moving averages, volume is light at 0.35x average, and momentum indicators are in weak territory. The news flow is generic and does not contain a material surprise. The recent short-term pullback (-2.1% over 5 days) coincides with higher short-term Treasury yields (3-month +5bp this week) but this is a modest move in a low-volatility environment. Without a decisive technical break, a data surprise, or a policy catalyst, the balanced setup—strong analyst coverage and fundamentals offset by near-term weakness—supports NEUTRAL with modest upside conviction. The call could shift bullish on technical repair or a yield curve steepen, or bearish on a break below the 50-day.

**Main reasons it gave:**
- Price 2.6% below 20-day moving average with RSI 36.6 and negative MACD histogram
- Analyst consensus: 100% buy weighting, +11.6% price target on top 41.5% of holdings
- Normal yield curve, VIX down 2.5 this week, falling long-end yields
- Light volume at 0.35x average; no data surprise or policy catalyst
- Valuation P/E 16.36 reasonable relative to 18.8% three-year annualized return

<details><summary><b>News</b> — score +0.00</summary>

- [XLF Looks 0.0% Fairly Valued on GF Value™](https://www.gurufocus.com/news/9089808/xlf-looks-00-fairly-valued-on-gf-value)  
  <sub>GuruFocus, 2 hours ago</sub>  
  On September 21, 2026, the Financial Select Sector SPDR ETF (ticker: XLF) has established key DeMark pivot points that traders are watching closely to gauge...
- [These financial stocks score highest on dividend growth (XLF:NYSEARCA)](https://seekingalpha.com/news/4644706-these-financial-stocks-score-highest-on-dividend-growth)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Screen top financial stocks with A+ Dividend Growth Grades—CINF, ERIE, EVR, MA, MCO, MSCI, PGR, SEIC, V.
- [Product Due Diligence Session: Building Resilient Portfolios with Real Assets | ETF Trends](https://www.advisorperspectives.com/webinars/2026/10/07/building-resilient-portfolios-with-real-assets?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 1 hour ago</sub>  
  Attendees will gain insights into the role of real assets and a framework for implementing an allocation in client portfolios.
- [Exchange-Traded Funds Rise, Equity Futures up Pre-Bell Monday as Oil Prices Decline](https://www.moomoo.com/news/post/76538074/exchange-traded-funds-rise-equity-futures-up-pre-bell-monday)  
  <sub>Moomoo, 1 hour ago</sub>  
  Thebroad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.7% and the actively traded Invesco QQQ Trust (QQQ) advanced 1.1% in Monday's...
- [Leading And Lagging Sectors For September 21, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61894029/leading-and-lagging-sectors-september-21-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLK) State Street Technology Select Sector SPDR ETF 191.7700 2.170 1.14 39.0K (NYSE:XLC) State...
- [Futures Rise: Can Market Take Off? 2026's Top Stocks Are Buys](https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-robinhood-sandisk-amd-moderna-surge-buy-areas/)  
  <sub>Investor's Business Daily, 3 hours ago</sub>  
  Dow Jones futures: The stock market is set for a positive start to the week with Robinhood, Sandisk, AMD and Moderna already in buy areas.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 55.81 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 57.29 (-2.6%), 50d 57.18 (-2.4%), 200d 53.71 (+3.9%); 50d above 200d
Momentum: RSI(14) 36.6 | MACD -0.350 vs signal -0.098 (histogram -0.253)
Returns: 1d -0.1% | 5d -2.1% | 1m -2.0% | 3m +3.9%
52-week range: 47.81 - 58.56 (now 74.5% of the way up)
Volatility: ATR(14) 0.69 (1.2% of price) | annualised 20d 12.8%
Volume: 0.35x the 20-day average
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
Three-year record: +18.8% a year | beta to the market 0.71
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 41.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
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
Shares outstanding: 883.44M | fund size: 49.31B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLI trades below its 20-day, 50-day and 200-day moving averages, with momentum deteriorating (RSI 35, MACD histogram negative) and volume well below average. The 1-month return is -5.5% and the 3-month is -6.5%, indicating a sustained downturn. Macro backdrop is stable: the yield curve slopes normally, VIX is calm at 14.6 (down 2.5 on the week), the dollar has strengthened 0.9 on the week, and Treasury yields have moved modestly. Inflation at 3.4% and unemployment at 4.1% are not far outside expectations. The fund's fundamentals show elevated valuation (P/E 28.43, P/B 6.75) after the recent rally, and while analyst coverage of the top 25.8% is uniformly bullish with a +23.1% price target, the largest holding UNP just upgraded to Buy on 2026-09-16, suggesting fresh conviction, but this is offset by broad technical weakness and below-average volume suggesting weak conviction from the fund's actual investors. There is no decisive macro catalyst or technical break to justify a directional call. The U.S.-China talks mentioned in headlines are speculative forward guidance, not a settled development, and the sector rotation into technology (XLK +1.14% vs XLI flat) on a down day reflects relative weakness, not absolute strength.

**Main reasons it gave:**
- RSI 35 and negative MACD histogram signal momentum deterioration
- Price 2.0-4.9% below short and intermediate moving averages over one month
- Volume 0.43x 20-day average suggests weak investor conviction despite analyst upside targets
- P/E 28.43 and P/B 6.75 reflect stretched valuation after recent appreciation
- Analyst roll-up 100% buy rated with +23.1% price target offset by technical breakdown

<details><summary><b>News</b> — score +0.00</summary>

- [Product Due Diligence Session: Building Resilient Portfolios with Real Assets | ETF Trends](https://www.advisorperspectives.com/webinars/2026/10/07/building-resilient-portfolios-with-real-assets?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 1 hour ago</sub>  
  Attendees will gain insights into the role of real assets and a framework for implementing an allocation in client portfolios.
- [Exchange-Traded Funds Rise, Equity Futures up Pre-Bell Monday as Oil Prices Decline](https://www.moomoo.com/news/post/76538074/exchange-traded-funds-rise-equity-futures-up-pre-bell-monday)  
  <sub>Moomoo, 1 hour ago</sub>  
  Thebroad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.7% and the actively traded Invesco QQQ Trust (QQQ) advanced 1.1% in Monday's...
- [Leading And Lagging Sectors For September 21, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61894029/leading-and-lagging-sectors-september-21-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLK) State Street Technology Select Sector SPDR ETF 191.7700 2.170 1.14 39.0K (NYSE:XLC) State...
- [U.S.-China Talks Seem Successful: ETF Areas in Focus](https://www.tradingview.com/news/zacks:5293da3f7094b:0-u-s-china-talks-seem-successful-etf-areas-in-focus/)  
  <sub>TradingView, 2 hours ago</sub>  
  Investors are currently tracking developments ahead of an expected meeting between U.S. President Donald Trump and Chinese President Xi Jinping in...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 169.92 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 173.47 (-2.0%), 50d 178.74 (-4.9%), 200d 171.72 (-1.0%); 50d above 200d
Momentum: RSI(14) 35.0 | MACD -3.033 vs signal -2.808 (histogram -0.225)
Returns: 1d +0.1% | 5d -0.0% | 1m -5.5% | 3m -6.5%
52-week range: 147.83 - 186.51 (now 57.1% of the way up)
Volatility: ATR(14) 2.44 (1.4% of price) | annualised 20d 13.1%
Volume: 0.43x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

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
Rolled up from the 5 largest holdings, 25.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.1% above the current prices
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
Shares outstanding: 136.63M | fund size: 23.22B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLP shows conflicting signals on a weak macro backdrop. Technicals are markedly oversold with RSI at 35.7 and negative MACD histogram, offering a potential bounce opportunity; the fund has underperformed over the past month (-3.9%) and trades below its 20, 50, and 200-day moving averages. However, the fundamental picture is constructive: analyst consensus on the largest holdings (39.6% of the fund) is unanimously bullish with a +14% weighted price target, and the fund's defensive positioning (beta 0.49, 2.6% yield) remains appropriate for the current environment. Macro conditions are stable -- the VIX is calm at 14.62, the yield curve is normal at +0.98, and the Fed's rate path suggests near-terminal rates. The recent underperformance appears technical exhaustion rather than a fundamental deterioration. The one minor headwind is low volume on the day (0.38x average), which limits conviction in any bounce. The fund remains attractive for defensive investors given analyst support for its largest holdings, but macro timing risk and the absence of a clear near-term catalyst (no recent positive surprise, no decisive technical reversal) prevent a stronger call.

**Main reasons it gave:**
- RSI 35.7 signals technical oversold condition
- Analyst consensus buy on top 5 holdings with +14% weighted price target
- Fund underperformed 1m and 3m despite stable macro backdrop
- Volume 0.38x average limits conviction in reversal
- Defensive positioning (beta 0.49) remains appropriate for environment

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds Rise, Equity Futures up Pre-Bell Monday as Oil Prices Decline](https://www.moomoo.com/news/post/76538074/exchange-traded-funds-rise-equity-futures-up-pre-bell-monday)  
  <sub>Moomoo, 1 hour ago</sub>  
  Thebroad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.7% and the actively traded Invesco QQQ Trust (QQQ) advanced 1.1% in Monday's...
- [Leading And Lagging Sectors For September 21, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61894029/leading-and-lagging-sectors-september-21-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLK) State Street Technology Select Sector SPDR ETF 191.7700 2.170 1.14 39.0K (NYSE:XLC) State...
- [XLV Looks 1.0% Overvalued on GF Value™ as Dividend Sustainabilit](https://www.gurufocus.com/news/9089817/xlv-looks-10-overvalued-on-gf-value-as-dividend-sustainability-remains-strong)  
  <sub>GuruFocus, 2 hours ago</sub>  
  On September 21, 2026, the Health Care Select Sector SPDR ETF (ticker: XLV) saw new pivot points established using the DeMark method, signaling potential...
- [Should You Invest in the iShares U.S. Consumer Discretionary ETF (IYC)?](https://finance.yahoo.com/markets/stocks/articles/invest-ishares-u-consumer-discretionary-102002712.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Designed to provide broad exposure to the Consumer Discretionary - Broad segment of the equity market, the iShares U.S. Consumer Discretionary ETF (IYC) is...
- [Novo Nordisk Falls 7% as Post-Wegovy Growth Plan Fails to Ease Competition Fears; Eli Lilly Slips, Viking Therapeutics Edges Higher](https://247wallst.com/investing/2026/09/21/novo-nordisk-falls-7-as-post-wegovy-growth-plan-fails-to-ease-competition-fears-eli-lilly-slips-viking-therapeutics-edges-higher/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Novo Nordisk took the stage at its own capital markets day and said something that sent its stock tumbling 7%, yet its closest rivals barely flinched.
- [Healthcare stocks with the strongest dividend growth grades (XLV:NYSEARCA)](https://seekingalpha.com/news/4644665-healthcare-stocks-with-the-strongest-dividend-growth-grades)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Screen the top healthcare dividend growth stocks (A+ to A-) across pharma, devices, services and life sciences—see the full list and ETFs to watch now.
- [Biotech Week Ahead: XLV Beats The Market — Here Are The Stocks, Readouts And Events To Watch Next](https://finance.yahoo.com/healthcare/articles/biotech-week-ahead-xlv-beats-043704054.html)  
  <sub>Yahoo Finance, 11 hours ago</sub>  
  The Health Care Select Sector SPDR Fund (XLV) gained 1.8% last week, outperforming the broader market and biotech ETFs. Sellas Life Sciences (SLS) will...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 82.04 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 84.49 (-2.9%), 50d 84.88 (-3.3%), 200d 83.59 (-1.9%); 50d above 200d
Momentum: RSI(14) 35.7 | MACD -0.666 vs signal -0.432 (histogram -0.234)
Returns: 1d -0.9% | 5d -2.8% | 1m -3.9% | 3m -0.2%
52-week range: 75.60 - 90.01 (now 44.7% of the way up)
Volatility: ATR(14) 0.99 (1.2% of price) | annualised 20d 12.8%
Volume: 0.38x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.45</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 39.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.0% above the current prices
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
Shares outstanding: 210.17M | fund size: 17.24B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLU is technically oversold with RSI at 29.6 and negative momentum (MACD histogram -0.133), trading 8.3% below its 200-day moving average on below-average volume. Macro backdrop is calm: VIX at 14.62, yield curve normal, and the Fed has cut rates as expected. Analyst coverage of the fund's largest holdings shows strong buy weight (80.9%) with a +21.5% price target, providing fundamental support. However, recent news consists of one promotional article and two vendor pieces about competing ETFs, with no material macro catalyst. The fund's valuation at 19.0x P/E is elevated relative to historical norms, and rates have stabilized rather than moving decisively in utilities' favor. The technical picture shows acute oversold conditions that typically precede bounces, but conviction is tempered by: (1) the lack of a concrete catalyst to drive reversal; (2) the absence of fund flow data to confirm accumulation; (3) modest recent momentum. This is a setup where utilities could stabilize, but without a clear macro trigger or behavioral confirmation from flows, the risk-reward is ambiguous. A small bullish tilt reflects oversold technicals and positive analyst sentiment on holdings, but the conviction floor reflects the absence of a material surprise or decisive catalyst.

**Main reasons it gave:**
- RSI 29.6 oversold with negative MACD histogram
- Analyst consensus on top 39.4% of holdings at +21.5% price target
- Trading 8.3% below 200-day SMA on below-average volume
- No material macro catalyst; rates stable, VIX calm
- P/E 19.0x elevated; fund flows data unavailable

<details><summary><b>News</b> — score +0.00</summary>

- [Buy Utilities At 16x While Demand Climbs (NYSEARCA:XLU)](https://seekingalpha.com/article/4948161-buy-utilities-at-16x-while-demand-climbs?source=feed_tag_market_outlook)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  Explore Global X U.S. Electrification ETF (ZAP): utilities + industrials for grid modernization.
- [EMLP ETF offers stability with North American e...](https://www.google.com/goto?url=CAESjQEB6zswFd4H6TTpOjkwstVlFbjqOyWp6MRctt4AL-VNNIXceereOKDq1GVhfT2g5tCW2AtJfhqrGWs0IxYUJvId7E3rc8z89ki5SWGXQUxPHfnhZGda0TNxXtuJ1tSgyn1EQU7bqJq79MAKoZFO_Qx7E5z7kKy80YOsiJp32vIbS4Slrf0oBRgo7WXGW-Y)  
  <sub>Pluang, 14 hours ago</sub>  
  EMLP is an actively managed ETF focused on North American energy infrastructure, especially electric power and transmission, aiming for total return with...
- [Global X U.S. Electrification ETF targets growt...](https://pluang.com/en/news-feed/beli-utilitas-di-16x-saat-permintaan-naik)  
  <sub>Pluang, 17 hours ago</sub>  
  The Global X U.S. Electrification ETF (ZAP) offers focused exposure to utilities and industrials benefiting from U.S. electrification and grid modernization...
- [EMLP: May Be A 'Set It And Forget It' Candidate For Risky Times (NYSEARCA:EMLP)](https://seekingalpha.com/article/4948165-emlp-may-be-a-set-it-and-forget-it-candidate-for-risky-times?source=feed_sector_etf_portfolio_strategy)  
  <sub>Seeking Alpha, 14 hours ago</sub>  
  EMLP is an actively managed ETF focused on North American energy infrastructure. Click here to read why EMLP is a Hold.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.35</summary>

```text
Last close 40.85 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 42.45 (-3.8%), 50d 43.73 (-6.6%), 200d 44.54 (-8.3%); 50d below 200d
Momentum: RSI(14) 29.6 | MACD -0.708 vs signal -0.575 (histogram -0.133)
Returns: 1d -0.6% | 5d -2.3% | 1m -6.7% | 3m -8.7%
52-week range: 40.85 - 47.73 (now 0.0% of the way up)
Volatility: ATR(14) 0.62 (1.5% of price) | annualised 20d 13.8%
Volume: 0.37x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

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
Rolled up from the 5 largest holdings, 39.4% of the fund by weight
Ratings by weight: buy 80.9% | hold 19.1% | sell 0.0% (mean 2.06 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.5% above the current prices
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
Shares outstanding: 163.27M | fund size: 6.67B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLV trades near the top of its 52-week range with elevated valuation (P/E 30.47, 1% overvalued on GF Value), but sentiment remains supported. Technicals show a stalled uptrend: price is 0.7% below the 20-day SMA, momentum has rolled over (RSI 51, MACD histogram negative at -0.406), and volume is 33% of average, all consistent with consolidation or pullback risk. The macro backdrop is stable with yields flat this week, a normal upward-sloping curve, low volatility (VIX 14.6), and a dollar up 0.9% -- none of these are a macro catalyst. The fund's largest five holdings (44% of weight) are uniformly rated Buy by consensus with a +10% upside target, which is constructive but already partially reflected in the 12.5% three-month return and 8.2% gain from the 200-day MA. Novo Nordisk's 7% drop and GLP-1 competitive fears are single-holding news within an 100-holding fund, not a material sector signal. The absence of recent fund flow data prevents a conviction read from insider activity. Technicals do not support a bullish add here, and valuation at P/E 30.47 offers limited margin of safety; upside targets are modest relative to what has already been priced in. This is a hold, not a buy.

**Main reasons it gave:**
- Price 0.7% below 20-day SMA with RSI 51 and negative MACD histogram signal stall
- P/E 30.47 with 1% overvaluation on GF Value limits margin of safety
- Analyst consensus +10% upside already partially reflected in 12.5% three-month gain
- Volume 33% below 20-day average on a near-record-high price
- Novo Nordisk decline is single-holding news in 100-holding fund

<details><summary><b>News</b> — score +0.15</summary>

- [XLV Looks 1.0% Overvalued on GF Value™ as Dividend Sustainabilit](https://www.gurufocus.com/news/9089817/xlv-looks-10-overvalued-on-gf-value-as-dividend-sustainability-remains-strong)  
  <sub>GuruFocus, 2 hours ago</sub>  
  On September 21, 2026, the Health Care Select Sector SPDR ETF (ticker: XLV) saw new pivot points established using the DeMark method, signaling potential...
- [Novo Nordisk Falls 7% as Post-Wegovy Growth Plan Fails to Ease Competition Fears; Eli Lilly Slips, Viking Therapeutics Edges Higher](https://247wallst.com/investing/2026/09/21/novo-nordisk-falls-7-as-post-wegovy-growth-plan-fails-to-ease-competition-fears-eli-lilly-slips-viking-therapeutics-edges-higher/)  
  <sub>24/7 Wall St., 1 hour ago</sub>  
  Novo Nordisk took the stage at its own capital markets day and said something that sent its stock tumbling 7%, yet its closest rivals barely flinched.
- [Healthcare stocks with the strongest dividend growth grades (XLV:NYSEARCA)](https://seekingalpha.com/news/4644665-healthcare-stocks-with-the-strongest-dividend-growth-grades)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Screen the top healthcare dividend growth stocks (A+ to A-) across pharma, devices, services and life sciences—see the full list and ETFs to watch now.
- [Biotech Week Ahead: XLV Beats The Market — Here Are The Stocks, Readouts And Events To Watch Next](https://finance.yahoo.com/healthcare/articles/biotech-week-ahead-xlv-beats-043704054.html)  
  <sub>Yahoo Finance, 11 hours ago</sub>  
  The Health Care Select Sector SPDR Fund (XLV) gained 1.8% last week, outperforming the broader market and biotech ETFs. Sellas Life Sciences (SLS) will...
- [Exchange-Traded Funds Rise, Equity Futures up Pre-Bell Monday as Oil Prices Decline](https://www.moomoo.com/news/post/76538074/exchange-traded-funds-rise-equity-futures-up-pre-bell-monday)  
  <sub>Moomoo, 1 hour ago</sub>  
  Thebroad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.7% and the actively traded Invesco QQQ Trust (QQQ) advanced 1.1% in Monday's...
- [Leading And Lagging Sectors For September 21, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61894029/leading-and-lagging-sectors-september-21-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLK) State Street Technology Select Sector SPDR ETF 191.7700 2.170 1.14 39.0K (NYSE:XLC) State...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 168.80 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 170.00 (-0.7%), 50d 166.91 (+1.1%), 200d 155.99 (+8.2%); 50d above 200d
Momentum: RSI(14) 51.1 | MACD 0.026 vs signal 0.432 (histogram -0.406)
Returns: 1d +0.2% | 5d +0.6% | 1m -2.1% | 3m +12.5%
52-week range: 134.13 - 175.68 (now 83.5% of the way up)
Volatility: ATR(14) 2.28 (1.4% of price) | annualised 20d 13.4%
Volume: 0.33x the 20-day average
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
Three-year record: +10.3% a year | beta to the market 0.52
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
Weighted price target: +10.0% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-09-18 Guggenheim: main, Buy -> Buy
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
Shares outstanding: 261.78M | fund size: 44.19B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro catalyst this cycle: US yields essentially unchanged on the week, curve normally sloped, VIX calm at 14.6. Technicals are mildly soft -- price below 20d/50d, MACD negative, RSI 41, on light volume -- but no decisive break, and 50d remains above 200d. Fund basics are reasonable (P/E 15.5, strong 3y record) and analyst roll-up over 51% of weight is unanimously buy with ~30% upside, a mild positive offset. A stronger dollar (+0.90) is a modest headwind for Argentine equities. Flows direction unknown, so no behavioural read. NEUTRAL.

**Main reasons it gave:**
- 10-year unchanged on the week; curve +0.98, VIX 14.6 calm -- no rate surprise
- Price below 20d (-3.0%) and 50d (-1.9%), MACD histogram -0.47, RSI 40.7
- Volume 0.53x 20-day average -- no conviction behind the pullback
- Analyst roll-up on 51.1% of weight: 100% buy, +30% weighted target
- Dollar index +0.90 on the week, a headwind for EM/Argentina exposure

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 92.17 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 95.00 (-3.0%), 50d 93.92 (-1.9%), 200d 92.74 (-0.6%); 50d above 200d
Momentum: RSI(14) 40.7 | MACD -0.101 vs signal 0.369 (histogram -0.470)
Returns: 1d -0.3% | 5d -3.4% | 1m -0.1% | 3m -2.7%
52-week range: 67.55 - 102.94 (now 69.6% of the way up)
Volatility: ATR(14) 1.84 (2.0% of price) | annualised 20d 18.0%
Volume: 0.53x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

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
Rolled up from the 5 largest holdings, 51.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.54 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.1% above the current prices
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
Shares outstanding: 8.72M | fund size: 804.08M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Poland equities sit at the top of a strong uptrend (+16.6% vs 200d, 98.6% of 52-week range) but momentum is rolling over (MACD below signal) on very thin volume, and the weighted analyst target on the top 47% of the fund is slightly below current prices. Macro backdrop is benign but not a catalyst: VIX 14.6 and calm, 10-year unchanged, though a firmer dollar (+0.90) and a bond market pricing hikes are mild headwinds for an EM regional fund. No macro or policy surprise this cycle, so no directional edge. Cheap valuation (P/E 13.5, 3.3% yield) argues against shorting an extended tape.

**Main reasons it gave:**
- Price at 98.6% of 52-week range, 50d above 200d, +15.8% in 3 months
- MACD 0.424 below signal 0.510 with volume only 0.21x average
- Weighted analyst price target 2.9% below current price across 47.4% of fund
- VIX 14.62 and 10-year unchanged on the week -- no macro surprise
- Dollar index +0.90 on the week, 2-year at 4.67% pricing hikes, mild EM headwind

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.25</summary>

```text
Last close 45.57 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 44.68 (+2.0%), 50d 43.44 (+4.9%), 200d 39.07 (+16.6%); 50d above 200d
Momentum: RSI(14) 59.3 | MACD 0.424 vs signal 0.510 (histogram -0.086)
Returns: 1d +2.6% | 5d +0.9% | 1m +3.2% | 3m +15.8%
52-week range: 31.57 - 45.76 (now 98.6% of the way up)
Volatility: ATR(14) 0.67 (1.5% of price) | annualised 20d 19.6%
Volume: 0.21x the 20-day average
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
Three-year record: +42.9% a year | beta to the market 0.73
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

<details><summary><b>What analysts and big funds say</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.05</summary>

```text
Rolled up from the 5 largest holdings, 47.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.14 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -2.9% above the current prices
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
Shares outstanding: 19.24M | fund size: 876.67M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise this week: yields essentially unchanged, curve normal, VIX calm and falling. EWI sits just below its 20d/50d with slightly negative MACD but a strong uptrend vs the 200d, so the technical picture is mixed consolidation rather than a break. Holdings are cheap (P/E 15, 3% yield) and analyst coverage on half the fund is uniformly buy with ~11% upside, but that is a slow-moving valuation argument, not a catalyst. Flow direction unknown. Dollar strength is a mild headwind for a euro-denominated basket. Default to NEUTRAL.

**Main reasons it gave:**
- Price below 20d (-0.9%) and 50d (-1.1%) SMAs with MACD histogram -0.131, RSI 46.6
- 50d above 200d, +5.8% over 200d, 82.6% of 52-week range - intact longer uptrend
- 10-year yield flat on week, curve +0.98 normal, VIX 14.62 down 2.5 - no macro surprise
- Holdings P/E 15.25, 3.0% yield; 52.6% financial services concentration
- Analyst roll-up on 50.9% of fund: 100% buy, +10.6% weighted target upside
- Dollar index +0.90 on the week, a headwind for unhedged euro exposure

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.05</summary>

```text
Last close 61.08 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 61.60 (-0.9%), 50d 61.73 (-1.1%), 200d 57.73 (+5.8%); 50d above 200d
Momentum: RSI(14) 46.6 | MACD -0.366 vs signal -0.235 (histogram -0.131)
Returns: 1d +1.7% | 5d +0.3% | 1m -2.7% | 3m +1.0%
52-week range: 50.31 - 63.35 (now 82.6% of the way up)
Volatility: ATR(14) 0.72 (1.2% of price) | annualised 20d 15.9%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

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
Rolled up from the 5 largest holdings, 50.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.03 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.6% above the current prices
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
Shares outstanding: 18.74M | fund size: 1.14B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise this cycle: yields essentially flat across the curve, curve normally sloped, VIX calm at 14.6 and falling. Dollar firmed +0.9, a mild headwind for Korean equities. Technicals are constructive (price above all major SMAs, 50d>200d, +6.8% in 5 days) but on 0.33x volume and with MACD rolling over, and the fund is still -14.1% over three months with 46% annualised volatility and beta 2.5 -- a two-way risk profile, not a clean break. Valuation is cheap (P/E 10.4) but the fund is really a levered bet on SK hynix and Samsung at 46% combined weight. Analyst roll-up returned no usable ratings or targets, so that dimension is left unscored. No macro catalyst to justify a side.

**Main reasons it gave:**
- 10-year yield unchanged on the week, curve normally sloped +0.98 -- no rate surprise
- VIX 14.62, down 2.5 on the week (calm regime)
- Price +3.6% over 20d SMA and +23.8% over 200d, 50d above 200d, but volume only 0.33x average
- MACD histogram negative (-0.171) despite RSI 57 -- momentum flattening
- Concentration risk: SK hynix 23.7% + Samsung 22.2%, tech 54.6%, beta 2.50
- Analyst roll-up returned no ratings or price targets despite 53.5% coverage

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 188.22 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 181.63 (+3.6%), 50d 173.49 (+8.5%), 200d 152.08 (+23.8%); 50d above 200d
Momentum: RSI(14) 57.0 | MACD 1.966 vs signal 2.137 (histogram -0.171)
Returns: 1d +3.8% | 5d +6.8% | 1m +5.6% | 3m -14.1%
52-week range: 78.87 - 219.20 (now 77.9% of the way up)
Volatility: ATR(14) 6.65 (3.5% of price) | annualised 20d 46.0%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

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

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Gold miners are consolidating after a big run: price sits below the 20d SMA but well above the 50d and 200d, MACD has rolled over, RSI is neutral at 49.6, and volume is thin at 0.25x average. Macro is mixed for gold -- the dollar firmed +0.90 on the week, the 2-year prices hikes rather than cuts, and long yields are flat-to-slightly-lower; none of that is a fresh surprise in either direction. News is promotional target-chasing ($5,000 gold) with one piece explicitly flagging a $3,000 drawdown risk first -- narrative, not catalyst. Analyst roll-up is uniformly buy with +10.8% upside but only covers 40% of the fund and the recent RBC actions were reiterations. Flows direction is unknown, so no behavioural read. No policy or data surprise, so no directional bet.

**Main reasons it gave:**
- Price -3.9% below 20d SMA with MACD histogram -1.14, momentum rolling over after +15.9% 3m run
- Dollar index +0.90 on the week and 2-year at 4.67% pricing hikes, a headwind for gold
- Analyst roll-up 100% buy, +10.8% weighted target, but only 39.9% fund coverage and recent actions were reiterations
- VIX 14.62 and calm, flat 10-year -- no macro surprise this cycle
- Volume 0.25x the 20-day average, so the pullback lacks conviction

<details><summary><b>News</b> — score +0.05</summary>

- [Hormuz Oil Shipments Hit Six-Month High? ETFs to Win/Lose](https://www.tradingview.com/news/zacks:9ed16a4fe094b:0-hormuz-oil-shipments-hit-six-month-high-etfs-to-win-lose/)  
  <sub>TradingView, 3 hours ago</sub>  
  Oil and liquefied natural gas shipments through the Strait of Hormuz reached their highest level in six months over the past two weeks, indicating that...
- [Gold to $5,000? Strategist Warns a Drop to $3,000 Comes First](https://www.benzinga.com/markets/commodities/26/09/61889634/gold-to-5000-strategist-warns-a-drop-to-3000-comes-first)  
  <sub>Benzinga, 5 hours ago</sub>  
  Gold targets $5000 on continuous ETF inflows, yet market euphoria and rising bond yields signal potential risk for precious metals.
- [Product Due Diligence Session: Building Resilient Portfolios with Real Assets | ETF Trends](https://www.advisorperspectives.com/webinars/2026/10/07/building-resilient-portfolios-with-real-assets?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 1 hour ago</sub>  
  Attendees will gain insights into the role of real assets and a framework for implementing an allocation in client portfolios.
- [Gold rebounds from $4K support as Timmer sees $5K in sight (GLD:NYSEARCA)](https://seekingalpha.com/news/4644631-gold-rebounds-from-4k-support-as-timmer-sees-5k-in-sight)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  Gold price outlook: Fidelity's Jurrien Timmer says global liquidity, M2 growth and ETF flows could drive gold from $4K toward $5K+.
- [Betashares: ETF inflows strengthen bull case for gold](https://www.moneymanagement.com.au/betashares-etf-inflows-strengthen-bull-case-for-gold/)  
  <sub>Money Management, 20 hours ago</sub>  
  Betashares sees upcoming tailwinds for gold, but notes a discrepancy between profitability and current valuations. The ETF provider observed rising return...
- [Inflation Watch Mode: Diversify, Buy Dips, Or Hedge? Yes (NDX)](https://seekingalpha.com/article/4948170-inflation-watch-mode-diversify-buy-dips-or-hedge-yes)  
  <sub>Seeking Alpha, 13 hours ago</sub>  
  I remain bullish on equities, expecting a rally into late September driven by robust earnings and AI-related momentum. Read more on the market here.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.05</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 94.42 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 98.21 (-3.9%), 50d 88.35 (+6.9%), 200d 90.73 (+4.1%); 50d below 200d
Momentum: RSI(14) 49.6 | MACD 1.075 vs signal 2.215 (histogram -1.140)
Returns: 1d -1.1% | 5d +0.3% | 1m -5.4% | 3m +15.9%
52-week range: 68.28 - 115.84 (now 55.0% of the way up)
Volatility: ATR(14) 3.36 (3.6% of price) | annualised 20d 38.6%
Volume: 0.25x the 20-day average
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
Three-year record: +49.2% a year | beta to the market 0.83
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
Weighted price target: +10.8% above the current prices
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
Shares outstanding: 328.81M | fund size: 31.05B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise this week: yields essentially flat, VIX calm at 14.6, curve normally sloped. IGV's trend is constructive (above 20/50/200d, +21.9% 3m) but momentum is fading (MACD below signal, 5d flat, volume 0.33x average) and the fund is well below its 52-week high. Holdings are expensive (P/E 34, beta 1.21) with a hawkish-leaning priced rate path, offsetting a uniformly buy-rated top-5 roll-up (~43% coverage, +8.8% targets). The single news item is a promotional listicle-style piece, not evidence. NEUTRAL.

**Main reasons it gave:**
- 10-year yield unchanged on week, VIX 14.6 and falling -- no macro surprise
- Price above 20/50/200d SMAs with 50d over 200d, +21.9% over 3 months
- MACD histogram negative (-0.190) and volume only 0.33x 20-day average
- Top-5 holdings 100% buy-rated by weight, +8.8% weighted target, but only 43% coverage
- Holdings P/E 34.2, P/S 9.1 with 2-year at 4.67% pricing hikes, not cuts

<details><summary><b>News</b> — score +0.00</summary>

- [Nvidia Has Been the King of AI. This ETF Bets the Next Winners Will Be Somewhere Else.](https://www.fool.com/investing/2026/09/21/nvidia-king-of-ai-this-etf-bets-next-winners-igv/)  
  <sub>The Motley Fool, 5 hours ago</sub>  
  The factors that made software stocks a laggard before could make them leaders today.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.15</summary>

```text
Last close 106.44 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 104.93 (+1.4%), 50d 100.29 (+6.1%), 200d 93.68 (+13.6%); 50d above 200d
Momentum: RSI(14) 56.3 | MACD 1.143 vs signal 1.332 (histogram -0.190)
Returns: 1d +2.0% | 5d -0.2% | 1m +4.4% | 3m +21.9%
52-week range: 74.67 - 117.79 (now 73.7% of the way up)
Volatility: ATR(14) 2.71 (2.5% of price) | annualised 20d 42.2%
Volume: 0.33x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 43.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +8.8% above the current prices
Holdings read: PLTR, PANW, MSFT, CRWD, CRM
Recent rating changes among them:
  - PLTR: 2026-09-15 UBS: main, Buy -> Buy
  - PANW: 2026-09-17 Bernstein: down, Outperform -> Market Perform
  - MSFT: 2026-09-21 Cantor Fitzgerald: main, Overweight -> Overweight
  - CRWD: 2026-09-18 B of A Securities: main, Neutral -> Neutral
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
Shares outstanding: 12.50M | fund size: 1.33B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Aerospace/defense basket in a sharp pullback: -9.2% over a month, below 20/50/200d SMAs with RSI 31 and negative MACD, but volume is only 0.23x average and no macro catalyst has arrived. Rates were essentially flat on the week, VIX fell to 14.6, dollar modestly firmer -- nothing that constitutes a policy or data surprise. Analyst roll-up on 57.5% of the fund is uniformly buy with ~25% upside, which offsets the weak tape but is backward-looking. News items are irrelevant (a Bitcoin volatility story and a Canada-France space MOU). Oversold in an intact longer-term uptrend is not a directional edge; stand aside.

**Main reasons it gave:**
- Price -8.1% vs 50d SMA and -6.3% vs 200d, RSI 31, MACD below signal
- Down volume at 0.23x 20-day average -- weak conviction in the selloff
- 10y yield unchanged on week, VIX -2.5 to 14.6: no macro surprise
- Holdings roll-up 100% buy by weight, +24.9% weighted price target over 57.5% of fund
- P/E 34.7 and 0.5% yield after a +25.8%/yr three-year run leaves valuation rich

<details><summary><b>News</b> — score +0.00</summary>

- [Canada, France plan space partnership as Ottawa deepens European ties](https://www.google.com/goto?url=CAESogEB6zswFafEAvOi2xZFVeqNGq8yhl7tvjtySxC1N2egZ7yjmgNUhyQOr4hfDjGcZgZ0RkgvkGuHbt_AQtC7dVSWNq-MTQvWHVp_34s9A_oLjYhIkNo_hV_qZw788IX5x9IIbmqKpSu1F7QlZjzogBMN2f0uDQiqp04yqFX87c5LIRJvGp8otc3X8kF3nU4hEwFAmje7Gy9lt6IIbEY8ZTIOg9w)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Canada and France plan to cooperate on space-launch systems and ground-based infrastructure as Ottawa seeks closer economic and security ties with Europe.
- [BlackRock says Bitcoin volatility fell to 35–40](https://www.google.com/goto?url=CAESfAHrOzAVQ6Be0cAesVaxD3l4muyjAwJx_hTDGEPlGV10zZy259-_1BZ6Mn_sY713XlEQDWv1XSzuLTQjzUOjGK2i4PGwxiAvKhlZhqWfs2dcLhnJdf6A7G34pAlCGe3u7VBlE5DrA9QBnAiPU11KjJ43UqLETfIhEhUTPpc)  
  <sub>Crypto News, 24 hours ago</sub>  
  BlackRock's Jay Jacobs says Bitcoin volatility has fallen to 35–40 as large holders use ETF wrappers for lending, options and liquidity.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 215.76 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 223.49 (-3.5%), 50d 234.83 (-8.1%), 200d 230.22 (-6.3%); 50d above 200d
Momentum: RSI(14) 31.0 | MACD -6.748 vs signal -6.211 (histogram -0.537)
Returns: 1d +0.9% | 5d -0.5% | 1m -9.2% | 3m -8.4%
52-week range: 198.23 - 253.22 (now 31.9% of the way up)
Volatility: ATR(14) 3.86 (1.8% of price) | annualised 20d 14.9%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

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
Rolled up from the 5 largest holdings, 57.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.75 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.9% above the current prices
Holdings read: GE, RTX, BA, GD, LMT
Recent rating changes among them:
  - GE: 2026-07-23 Bernstein: main, Outperform -> Outperform
  - RTX: 2026-08-03 Bernstein: main, Market Perform -> Market Perform
  - BA: 2026-09-18 B of A Securities: reit, Buy -> Buy
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
Shares outstanding: 63.32M | fund size: 13.66B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Transports are in a clear downtrend (below 20/50d SMAs, MACD negative, RSI 28.8 oversold) but there is no macro catalyst this week: yields flat, VIX calm and falling, curve normal. Oversold on light volume argues against pressing shorts, while the trend argues against buying. Analyst roll-up on 53% of the fund is constructive (91% buy, +26% targets), partially offsetting the weak tape. Rate path pricing hikes and a firmer dollar are mild headwinds for a high-beta cyclical basket. No news flow; no fund flow data. NEUTRAL with a slight negative tilt.

**Main reasons it gave:**
- Price 4.7% below 20d and 7.3% below 50d SMA, MACD histogram -0.331
- RSI(14) 28.8 oversold on volume just 0.32x average
- Analyst roll-up over 53.1% of fund: 90.8% buy weight, +26.5% weighted target
- Macro quiet: 10y unchanged on week, VIX 14.6 and falling, curve +0.98 normal
- 2-year at 4.67% vs 4.00% target prices hikes; dollar +0.90 on week, headwind for cyclicals

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 79.46 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 83.37 (-4.7%), 50d 85.68 (-7.3%), 200d 81.10 (-2.0%); 50d above 200d
Momentum: RSI(14) 28.8 | MACD -1.634 vs signal -1.303 (histogram -0.331)
Returns: 1d -1.0% | 5d -3.8% | 1m -7.9% | 3m -6.1%
52-week range: 68.14 - 90.01 (now 51.8% of the way up)
Volatility: ATR(14) 1.28 (1.6% of price) | annualised 20d 15.8%
Volume: 0.32x the 20-day average
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
Three-year record: +11.5% a year | beta to the market 1.28
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

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
Shares outstanding: 27.46M | fund size: 2.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise this week: 10-year unchanged, curve normally sloped, VIX down to 14.6, no data release far from expectations. Technicals are mixed -- price above 20d/50d but below the 200d with a death-cross configuration, MACD histogram slightly negative, volume 0.6x average on the pop. The 7% WBD move is a small-weight constituent story and does not drive a fund where Meta and Alphabet are 35%. Analyst roll-up is constructive (100% buy by weight, +13% targets) but covers only 45% of the fund and is slow-moving. Rate path pricing hikes and a firmer dollar are mild headwinds for long-duration growth exposure. No side worth taking.

**Main reasons it gave:**
- 10-year 4.96% unchanged on the week; curve +0.98 normal; VIX 14.62 and falling -- no policy or vol shock
- Price 113.47 below 200d SMA 113.99 with 50d under 200d; MACD histogram -0.036
- Rally came on 0.61x average volume -- not a decisive break
- Analyst roll-up 100% buy, +13% weighted target, but only 45.5% of fund covered
- 2-year 4.67% vs 4.00% target prices ~3 hikes; dollar +0.90 -- headwind for duration-sensitive growth names

<details><summary><b>News</b> — score +0.05</summary>

- [Warner Bros. Discovery Jumps 7%, Paramount Skydance Climbs 5% as Antitrust Settlement Talks Advance; Netflix Sits Out the Rally](https://247wallst.com/investing/2026/09/21/warner-bros-discovery-jumps-7-paramount-skydance-climbs-5-as-antitrust-settlement-talks-advance-netflix-sits-out-the-rally/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Shares of Warner Bros. Discovery (NASDAQ:WBD | WBD Price Prediction) are jumping in early Monday trading on fresh reports that antitrust settlement talks...
- [Leading And Lagging Sectors For September 21, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61894029/leading-and-lagging-sectors-september-21-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLK) State Street Technology Select Sector SPDR ETF 191.7700 2.170 1.14 39.0K (NYSE:XLC) State...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.05</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.05</summary>

```text
Last close 113.47 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 112.39 (+1.0%), 50d 111.22 (+2.0%), 200d 113.99 (-0.5%); 50d below 200d
Momentum: RSI(14) 54.4 | MACD 0.412 vs signal 0.448 (histogram -0.036)
Returns: 1d +2.4% | 5d -1.4% | 1m +2.5% | 3m +6.2%
52-week range: 105.38 - 120.08 (now 55.0% of the way up)
Volatility: ATR(14) 1.79 (1.6% of price) | annualised 20d 18.9%
Volume: 0.61x the 20-day average
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.55 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.0% above the current prices
Holdings read: META, GOOGL, GOOG, T, VZ
Recent rating changes among them:
  - META: 2024-09-30 Cantor Fitzgerald: reit, Overweight -> Overweight
  - GOOGL: 2026-09-18 Tigress Financial: main, Strong Buy -> Strong Buy
  - GOOG: 2026-07-23 JP Morgan: main, Overweight -> Overweight
  - T: 2026-07-23 Wolfe Research: up, Peer Perform -> Outperform
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
Shares outstanding: 198.53M | fund size: 22.53B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [SLS, IBRX Eye Green Month As Biotech ETF Gains Steam: Analyst Sees ‘Continued Opportunities’ In Immuno-Oncology](https://stocktwits.com/news-articles/markets/equity/sls-ibrx-xbi-analyst-continued-opportunities-immuno-oncology/cZ1BDwKR7hT)  
  <sub>Stocktwits, 17 hours ago</sub>  
  XBI, which includes both SLS and IBRX, is on track for its strongest monthly performance since December 2023.
- [Biotech Week Ahead: XLV Beats The Market — Here Are The Stocks, Readouts And Events To Watch Next](https://finance.yahoo.com/healthcare/articles/biotech-week-ahead-xlv-beats-043704054.html)  
  <sub>Yahoo Finance, 11 hours ago</sub>  
  The Health Care Select Sector SPDR Fund (XLV) gained 1.8% last week, outperforming the broader market and biotech ETFs. Sellas Life Sciences (SLS) will...
- [The Real Start of Every Biotech Story is not a Lab but the Funding Decision](https://www.moomoo.com/community/feed/the-real-start-of-every-biotech-story-is-not-a-117304363909126)  
  <sub>Moomoo, 23 hours ago</sub>  
  Before a company like the ones I usually write about here can develop a drug, someone has to fund the basic science behind it, and that funding proces...
- [Could IBRX Be A Tokenized Stock? Founder’s Tease Sends ImmunityBio Traders Into Speculation Mode](https://stocktwits.com/news-articles/markets/equity/ibrx-tokenized-stock-founder-tease-immunitybio-traders-speculation-mode/cZMRI94RB4K)  
  <sub>Stocktwits, 5 hours ago</sub>  
  IBRX stock, ImmunityBio, ImmunityBio Patrick Soon-Shiong, tokenized stocks, Nant Global Finance, SEC Innovation Exemption, blockchain stock trading.
- [NOK Stock Rises Overnight: Nokia’s EURO STOXX 50 Index Return On Monday Adds To AI-Fueled Momentum](https://stocktwits.com/news-articles/markets/equity/nok-stock-rises-overnight-nokia-s-euro-stoxx-50-index-return-on-monday-adds-to-ai-fueled-momentum/cZMRdyoRB4Q)  
  <sub>Stocktwits, 10 hours ago</sub>  
  Its inclusion in the EURO STOXX 50 will trigger passive buying from index funds in the Eurozone, likely pushing its prices higher and in turn,...
- [NIO, XPEV, LI Fall In Hong Kong Amid US-China Trade Truce Jitters — Here’s What's Happening Across China’s EV Sector](https://stocktwits.com/news-articles/markets/equity/nio-xpev-li-us-china-trade-truce-jitters-china-ev-sector/cZMR3iQRB4W)  
  <sub>Stocktwits, 10 hours ago</sub>  
  Nio expects ES9 deliveries to reach 30000 this week, less than four months after deliveries began.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 158.51 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 161.27 (-1.7%), 50d 157.56 (+0.6%), 200d 137.31 (+15.4%); 50d above 200d
Momentum: RSI(14) 49.1 | MACD -0.673 vs signal 0.145 (histogram -0.818)
Returns: 1d +1.1% | 5d +0.6% | 1m -3.0% | 3m +8.7%
52-week range: 95.60 - 169.55 (now 85.1% of the way up)
Volatility: ATR(14) 3.99 (2.5% of price) | annualised 20d 24.5%
Volume: 0.35x the 20-day average
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
Three-year record: +27.6% a year | beta to the market 1.12
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
Weighted price target: -15.3% above the current prices
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

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 73.99M | fund size: 11.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Should You Invest in the iShares U.S. Consumer Discretionary ETF (IYC)?](https://finance.yahoo.com/markets/stocks/articles/invest-ishares-u-consumer-discretionary-102002712.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Designed to provide broad exposure to the Consumer Discretionary - Broad segment of the equity market, the iShares U.S. Consumer Discretionary ETF (IYC) is...
- [Exchange-Traded Funds Rise, Equity Futures up Pre-Bell Monday as Oil Prices Decline](https://www.moomoo.com/news/post/76538074/exchange-traded-funds-rise-equity-futures-up-pre-bell-monday)  
  <sub>Moomoo, 1 hour ago</sub>  
  Thebroad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.7% and the actively traded Invesco QQQ Trust (QQQ) advanced 1.1% in Monday's...
- [Leading And Lagging Sectors For September 21, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61894029/leading-and-lagging-sectors-september-21-2026)  
  <sub>Benzinga, 2 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLK) State Street Technology Select Sector SPDR ETF 191.7700 2.170 1.14 39.0K (NYSE:XLC) State...
- [Should You Invest in the Vanguard Consumer Discretionary Index Fund ETF Shares (VCR)?](https://finance.yahoo.com/markets/stocks/articles/invest-vanguard-consumer-discretionary-index-102002432.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  The Vanguard Consumer Discretionary Index Fund ETF Shares (VCR) was launched on January 26, 2004, and is a passively managed exchange traded fund designed...
- [How to Buy McDonald's Stock (MCD) in 2026](https://www.fool.com/investing/how-to-invest/stocks/how-to-invest-in-mcdonalds-stock/)  
  <sub>The Motley Fool, 18 hours ago</sub>  
  Learn about how to invest in McDonald's stock, including how to buy shares, whether it pays a dividend, and its stock split history.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 111.62 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 114.16 (-2.2%), 50d 115.26 (-3.2%), 200d 116.81 (-4.4%); 50d below 200d
Momentum: RSI(14) 40.6 | MACD -1.480 vs signal -1.152 (histogram -0.327)
Returns: 1d +0.5% | 5d -1.1% | 1m -4.3% | 3m -2.9%
52-week range: 105.66 - 124.52 (now 31.6% of the way up)
Volatility: ATR(14) 1.59 (1.4% of price) | annualised 20d 15.0%
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.77 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.0% above the current prices
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
Shares outstanding: 206.55M | fund size: 23.05B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.25

**In the model's own words:**

> CANE is a sugar futures fund trading near the top of its 52-week range with mixed technicals and a severe structural headwind. The 3-month chart shows the fund +21.5% versus the commodity +38.7%, a -17.2% gap driven by contango roll costs averaging -12.5% annually. This is history, not forecasting, but it means the fund has bled value for months while the commodity itself rallied -- a structural tax that will persist if the curve stays in backwardation. Technicals are neutral to slightly negative: price is 1.8% below the 20-day SMA, RSI sits at 50.5 (no momentum), and MACD has turned down with a negative histogram. The 52-week rally (+26% from the 9.02 low) has crowded speculators to the 98th percentile long, a crowding that is as often a top as it is a middle. The only bullish element is the 50-day SMA above the 200-day in a gently upsloping trend, and a 3-month return of +21.5% that, while lagging the commodity sharply, still reflects underlying strength in sugar prices. Macro backdrop is stable: volatility is calm at 14.62, yields are flat to slightly higher, the curve is normal, and inflation expectations remain anchored. There is no fresh catalyst, no positioning surprise, and no unusual flow data (too few readings to read). Without a clear technical break, a macro surprise, or a flow reversal, this trade appears fairly valued at the margin with a significant structural cost working against longs. A NEUTRAL signal reflects this equilibrium.

**Main reasons it gave:**
- 52-week crowding at 98th percentile with net long near record levels
- Negative roll drag: fund -12.5% annualized cost versus commodity, -17.2% over 3 months
- Price 1.8% below 20-day SMA and 76.8% of the way to 52-week high
- MACD histogram negative with RSI neutral at 50.5
- No fresh macro catalyst or policy surprise to justify re-entry

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 11.17 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 11.38 (-1.8%), 50d 10.66 (+4.8%), 200d 9.90 (+12.8%); 50d above 200d
Momentum: RSI(14) 50.5 | MACD 0.136 vs signal 0.237 (histogram -0.101)
Returns: 1d +1.1% | 5d -2.4% | 1m -0.2% | 3m +21.5%
52-week range: 9.02 - 11.82 (now 76.8% of the way up)
Volatility: ATR(14) 0.21 (1.9% of price) | annualised 20d 24.4%
Volume: 0.50x the 20-day average
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
Cost of holding this fund instead of sugar itself: -12.5% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +21.5%, commodity +38.7%, gap -17.2% | 6 months: fund +6.9%, commodity +18.0%, gap -11.1% | 12 months: fund +7.9%, commodity +20.4%, gap -12.5%
A commodity fund holds futures, not sugar, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

```text
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 18.5% of open interest (1,219,523 contracts)
Change on the week: -0.2% of open interest
Crowding: 98% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 5.11M | fund size: 57.13M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.25

**In the model's own words:**

> SLV trades 9.3% below its 200-day moving average with a 50d still below 200d, indicating a downtrend environment despite a recent 5.1% bounce over 5 days. Momentum is mixed: RSI at 53.4 is neither oversold nor overbought, and MACD histogram is negative. The fund faces a structural 2.6% annual drag from futures roll costs, a permanent headwind. Positioning shows large speculators at 65th percentile crowding with a net short of 1.3% on the week, suggesting neither extreme conviction nor major unwind. Macro backdrop is benign: the Fed is expected to cut rates modestly (pricing about 75bp over two years), the curve is normal, and the dollar has strengthened 0.9% this week, which is a modest headwind for dollar-denominated commodities. Volatility at 14.6 is calm. Volume is light at 0.32x average, reducing confidence in the recent bounce. No macro catalyst or technical breakout is present; the trend remains down despite the short-term recovery. This is a holding pattern, not a directional setup.

**Main reasons it gave:**
- price 9.3% below 200d MA, 50d below 200d in downtrend
- MACD histogram negative, momentum not confirming bounce
- 2.6% annual structural drag from futures roll costs
- large speculator positioning at 65th percentile, not extreme
- dollar +0.9% this week, mild headwind for silver

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 59.74 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 59.61 (+0.2%), 50d 56.93 (+4.9%), 200d 65.84 (-9.3%); 50d below 200d
Momentum: RSI(14) 53.4 | MACD 0.158 vs signal 0.299 (histogram -0.141)
Returns: 1d -0.3% | 5d +5.1% | 1m -3.1% | 3m +1.4%
52-week range: 39.04 - 105.60 (now 31.1% of the way up)
Volatility: ATR(14) 1.78 (3.0% of price) | annualised 20d 37.4%
Volume: 0.32x the 20-day average
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
Cost of holding this fund instead of silver itself: -2.6% a year -- a steady drag
Measured: 3 months: fund +1.4%, commodity +1.7%, gap -0.3% | 6 months: fund -2.9%, commodity -3.9%, gap +1.0% | 12 months: fund +57.2%, commodity +59.8%, gap -2.6%
A commodity fund holds futures, not silver, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 12.7% of open interest (103,745 contracts)
Change on the week: -1.3% of open interest
Crowding: 65% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.25

**In the model's own words:**

> SOYB has rallied 15.2% in three months and now sits at the 98.4th percentile of its 52-week range, driven partly by crop concerns (US soybean crop rated 58% good/excellent, down 5 points year-over-year). Technicals show an uptrend across all moving averages and positive returns, but momentum is already elevated: RSI at 64.7 suggests overbought conditions, MACD has rolled over below signal, and volume is only 0.39x average, indicating weakening conviction during the rally. Large speculators hold a net long at the 88th percentile of crowding—within normal range but not extreme—and reduced their long by 2.2% of open interest this week, a small signal of positioning moderation. Macro backdrop is stable: yields are flat to modestly higher, the dollar strengthened, and the 10-year real rate is pricing only modest Fed cuts ahead. Crop condition is steady week-to-week and while it is worse than last year, the market has already traded this fact. The fund's tracking cost is minimal at -1% annualized. The rally appears mature: near all-time highs, RSI elevated, volume flagging, and speculators slightly reducing longs. Without a fresh catalyst (weather shock, policy surprise, or significant data miss), the risk/reward at these levels favors caution rather than conviction in either direction.

**Main reasons it gave:**
- RSI 64.7 with MACD rolling over signals overbought momentum despite strong trend
- Large speculators reduced net long 2.2% this week as fund hits 98.4th percentile of 52-week range
- Crop condition steady week-to-week and down only 5 points YoY, already reflected in price
- Volume 0.39x average suggests weakening conviction during rally to near all-time highs

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.35</summary>

```text
Last close 28.03 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 27.47 (+2.0%), 50d 26.30 (+6.6%), 200d 24.41 (+14.8%); 50d above 200d
Momentum: RSI(14) 64.7 | MACD 0.522 vs signal 0.559 (histogram -0.037)
Returns: 1d +1.3% | 5d +1.2% | 1m +7.1% | 3m +15.2%
52-week range: 21.46 - 28.14 (now 98.4% of the way up)
Volatility: ATR(14) 0.35 (1.3% of price) | annualised 20d 18.0%
Volume: 0.39x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.15</summary>

```text
Cost of holding this fund instead of soybeans itself: -1.0% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +15.2%, commodity +18.5%, gap -3.3% | 6 months: fund +16.4%, commodity +13.8%, gap +2.6% | 12 months: fund +26.4%, commodity +27.4%, gap -1.0%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.15</summary>

```text
Soybeans rated good or excellent: 58% of the US crop (week 37 of 2026)
Direction over 3 weeks: steady, 0 points
Same week last year: 63% (-5 points)
A better crop means more supply, which reads bearish for the price, and a worse one bullish. The trend matters more than the level, and the market has already seen this: it is published on a schedule everyone trades.
```

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
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 21.9% of open interest (1,104,880 contracts)
Change on the week: -2.2% of open interest
Crowding: 88% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 1.66M | fund size: 46.45M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.25

**In the model's own words:**

> UNG faces conflicting signals that cancel to neutral. Technicals show a fund in a downtrend (10.6% below the 200d SMA, 50d below 200d) with momentum neutral (RSI 48.9, MACD histogram near zero) and weak volume at 0.46x average. The 3-month return is -12.5%, consistent with the broader downward trend. However, the macro backdrop is benign: yields are stable with only modest moves, the dollar strengthened (+0.90 on the week) which typically pressures natural gas, and the VIX is low at 14.62 suggesting risk appetite is intact. On the commodity fundamentals, inventory builds at the 71st percentile are mildly bearish but not extreme; the EIA outlook forecasts a 7% rise from current levels over six months, a modest but constructive view. Most critically, the fund's cost of holding is severe at -15.4% annualized due to contango roll losses—this is a structural headwind that demands a meaningfully larger move to justify a long, and a tailwind for shorts. Large speculators hold a net short at the 33rd percentile of crowding, neither extreme nor shifted materially on the week. Taken together: technicals are weak, the commodity outlook is slightly bullish, the carry structure bleeds long positions, and positioning shows no extreme. This is a sideways tape with structural headwinds, not a directional setup.

**Main reasons it gave:**
- Downtrend intact: price 10.6% below 200-day SMA with 50d below 200d
- Heavy roll cost at -15.4% annually suppresses long conviction
- EIA forecast sees 7% rise over 6 months, mildly supportive
- Inventory builds at 71st percentile—mild bearish pressure but not extreme
- Dollar strength (+0.90 on week) headwind for natural gas

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 10.30 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 10.38 (-0.8%), 50d 10.23 (+0.6%), 200d 11.52 (-10.6%); 50d below 200d
Momentum: RSI(14) 48.9 | MACD 0.018 vs signal 0.020 (histogram -0.002)
Returns: 1d -1.1% | 5d -0.3% | 1m +2.8% | 3m -12.5%
52-week range: 9.63 - 16.90 (now 9.1% of the way up)
Volatility: ATR(14) 0.27 (2.6% of price) | annualised 20d 24.6%
Volume: 0.46x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.15</summary>

```text
Cost of holding this fund instead of natural gas itself: -15.4% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -12.5%, commodity -12.7%, gap +0.2% | 6 months: fund -16.9%, commodity -8.2%, gap -8.7% | 12 months: fund -18.7%, commodity -3.4%, gap -15.4%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.15</summary>

```text
US inventories, week ending 2026-09-11 (published the following Wednesday)
  Natural gas: 3,298.0 billion cubic feet, +44.0 on the week (a build), 71% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

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

<details><summary><b>Buying and selling by company insiders</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.05</summary>

```text
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 5.5% of open interest (1,820,003 contracts)
Change on the week: -0.2% of open interest
Crowding: 33% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.05</summary>

_Not available today._

</details>

### Oil (USO) · Commodity — NEUTRAL, confidence 0.25

**In the model's own words:**

> USO tracks WTI crude oil, which is caught between conflicting macro and technical signals. The recent rally from $66 to $148 (86th percentile of 52-week range) is extended technically, with momentum flattening (RSI 56, MACD histogram 0.006). A four-day selloff below $100 reflects de-escalation rhetoric from Trump on Iran and Yemen, reducing near-term geopolitical premium. Positioning is at the 98th percentile of crowding—a crowded long that often marks the end of a move rather than the middle. Energy inventories show crude draws (bullish, 38th percentile) but petrol and diesel builds (bearish), reflecting mixed demand signals and the diesel shortage noted in headlines. The EIA forecast sees WTI falling 10% over six months to $79, creating a headwind even if near-term support holds. Treasury yields rose marginally (3-month +5bp) but the curve normalized; the dollar strengthened +0.90 on the week, a structural headwind for commodities. News flow is mixed: geopolitical risk premiums compressing, but diesel scarcity and Strait of Hormuz concerns persisting. Volume is 0.44x average, suggesting weak conviction in either direction. The technicals show a valid uptrend (50d > 200d, price +33% in three months) but entry momentum is flat and positioning extreme, leaving little room for new buyers. A failure to hold above $95-$100 would accelerate a retest toward $85 in line with EIA forecasts.

**Main reasons it gave:**
- Positioning at 98th percentile crowding, a crowded long historically coincident with move exhaustion
- EIA official forecast sees WTI falling 10% to $79 over six months, well below spot
- Four-day selloff as Trump signals openness to Iran talks and defers Yemen action, reducing geopolitical premium
- Crude inventory draw (bullish) offset by petrol and diesel builds and low gasoline stocks (bearish mixed demand)
- RSI 56 and flat MACD histogram after 32.9% gain show momentum rolling over despite uptrend intact

<details><summary><b>News</b> — score -0.15</summary>

- [Trading Crude Oil With The UCO And SCO ETFs (NYSEARCA:UCO)](https://seekingalpha.com/article/4948162-trading-crude-oil-with-the-uco-and-sco-etfs)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  ProShares Ultra Bloomberg Crude Oil ETF is a Buy, supported by strong momentum and liquidity, but carries high volatility and risk. Read more on UCO & SCO...
- [Oil Near $100, Treasury Yields Near 5%, Bitcoin’s Resilience: 3 Charts To Watch This Week](https://www.tradingview.com/news/stocktwits:c7de3f4f9094b:0-oil-near-100-treasury-yields-near-5-bitcoin-s-resilience-3-charts-to-watch-this-week/)  
  <sub>TradingView, 6 hours ago</sub>  
  WTI crude oil futures fell back below $100 a barrel Monday after Saudi Arabia said its East-West pipeline could restore about half of its capacity within...
- [Gavin Newsom Fires Back at Trump’s 'Disastrous' Iran War With E15 Gas Push as California Fuel Tops $6](https://www.benzinga.com/news/politics/26/09/61889688/gavin-newsom-fires-back-at-trumps-disastrous-iran-war-with-e15-gas-push-as-california-fuel-tops-6)  
  <sub>Benzinga, 5 hours ago</sub>  
  California Gov. Gavin Newsom will release E15 fuel to ease soaring gas prices, blaming Trump's Iran war and Strait of Hormuz disruptions.
- [Crude oil dips below $100 after Trump says he may be open to talking to Iran (CL1:COM:Commodity)](https://seekingalpha.com/news/4644792-crude-oil-dips-below-100-after-trump-says-he-may-be-open-to-talking-to-iran)  
  <sub>Seeking Alpha, 40 minutes ago</sub>  
  Crude oil futures fell for the fourth straight session after President Trump reportedly decided against bombing Yemen for now and indicated he was open to...
- [Diesel Hits Historic $6.51/Gal: Commodity Strategist Warns We Are Facing a Deficit That 'No Handshake' Can Refill](https://www.tradingview.com/news/benzinga:ebba5f08d094b:0-diesel-hits-historic-6-51-gal-commodity-strategist-warns-we-are-facing-a-deficit-that-no-handshake-can-refill/)  
  <sub>TradingView, 4 hours ago</sub>  
  The national average price for diesel reached $6.51 per gallon on Monday. A commodity strategist stated the supply disruption has moved into a diesel market...
- [Stocks Didn't Really Rally Because Of The Rate Hike; SMH & Robinhood Markets Ready To Run](https://seekingalpha.com/article/4948230-stocks-didnt-rally-because-of-rate-hike-smh-robinhood-markets-ready-to-run)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  The most bullish part of the FOMC meeting wasn't the rate hike; it was the clarity it gave investors. SMH, QQQ, and a select cohort of chip stocks all look...
- [Qatar Energy CEO counters Bessent: Strait of Hormuz ‘will never be obsolete’ (CL1:COM:Commodity)](https://seekingalpha.com/news/4644605-qatar-energy-ceo-counters-bessent-strait-of-hormuz-will-never-be-obsolete)  
  <sub>Seeking Alpha, 11 hours ago</sub>  
  Qatari Energy Minister Saad Al-Kaabi on Sunday said Treasury Secretary Scott Bessent was “wrong” when he said that the strategic Strait of Hormuz will be...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.15</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.10</summary>

```text
Last close 148.47 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 144.34 (+2.9%), 50d 133.32 (+11.4%), 200d 111.67 (+32.9%); 50d above 200d
Momentum: RSI(14) 56.2 | MACD 7.016 vs signal 7.010 (histogram 0.006)
Returns: 1d -3.5% | 5d -5.2% | 1m +10.4% | 3m +31.8%
52-week range: 66.17 - 161.86 (now 86.0% of the way up)
Volatility: ATR(14) 5.02 (3.4% of price) | annualised 20d 45.1%
Volume: 0.44x the 20-day average
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

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.20</summary>

```text
US inventories, week ending 2026-09-11 (published the following Wednesday)
  Crude oil: 423.4 million barrels, -0.6 on the week (a draw), 38% percentile over 52 weeks
  Petrol: 207.7 million barrels, +0.8 on the week (a build), 13% percentile over 52 weeks -- low for the time of year
  Diesel: 107.9 million barrels, +1.6 on the week (a build), 33% percentile over 52 weeks
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.25</summary>

```text
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 5.4% of open interest (1,955,764 contracts)
Change on the week: -0.3% of open interest
Crowding: 98% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.25</summary>

_Not available today._

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.25

**In the model's own words:**

> WEAT presents a mixed technical and fundamental picture with no clear directional catalyst. The price has rallied 15.4% over three months and sits at the 78th percentile of its 52-week range, supported by a solid uptrend versus the 200-day moving average (+14.2%). However, momentum is deteriorating: RSI at 51.5 shows no overbought condition, but MACD has turned negative (histogram -0.186) and the price is 1.7% below the 20-day SMA, suggesting momentum is stalling. Volume is well below average at 0.38x the 20-day level, indicating weak conviction in the rally. On the macro side, the Treasury curve has normalized with short rates rising modestly, the dollar has strengthened (+0.90%), and the VIX remains calm at 14.62. CFTC positioning is crowded long at the 90th percentile, historically a contrarian signal; large speculators have reduced their net short position by 1.8% of open interest on the week, but a crowded long often marks the end of a move rather than the middle. Crop conditions are slightly better than last year (51% vs 49% good/excellent), providing mild supply pressure. Most concerning is the fund's carry cost: at -14.1% annualized, the rolling structure has been a significant headwind. The rally has outpaced this drag only because the underlying commodity moved substantially; without continued strong wheat price action, the fund faces structural decay. No macro surprise or policy catalyst has emerged to justify a directional tilt. The weak volume, negative momentum divergence, crowded positioning, and heavy carry cost argue for caution on a long, while the uptrend and modest supply news are insufficient to justify a short. The lack of fresh news or data surprise leaves no clear edge.

**Main reasons it gave:**
- MACD histogram turned negative despite price near highs
- CFTC positioning crowded long at 90th percentile, a contrarian signal
- Fund carry cost of -14.1% annualized, structural headwind that has been masked by commodity rally
- Volume 0.38x average suggests weak conviction in price advance
- No macro catalyst or news catalyst present to sustain rally

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.10</summary>

```text
Last close 26.25 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 26.71 (-1.7%), 50d 25.46 (+3.1%), 200d 22.98 (+14.2%); 50d above 200d
Momentum: RSI(14) 51.5 | MACD 0.235 vs signal 0.421 (histogram -0.186)
Returns: 1d +1.5% | 5d +0.3% | 1m +3.4% | 3m +15.4%
52-week range: 19.88 - 28.00 (now 78.4% of the way up)
Volatility: ATR(14) 0.61 (2.3% of price) | annualised 20d 31.0%
Volume: 0.38x the 20-day average
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
Cost of holding this fund instead of wheat itself: -14.1% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +15.4%, commodity +21.5%, gap -6.1% | 6 months: fund +14.9%, commodity +22.0%, gap -7.1% | 12 months: fund +24.4%, commodity +38.5%, gap -14.1%
A commodity fund holds futures, not wheat, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.20</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.35</summary>

```text
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 0.8% of open interest (485,138 contracts)
Change on the week: -1.8% of open interest
Crowding: 90% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.35</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 13.72M | fund size: 360.19M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Uptrend is intact (price 95% of 52-week range, 50d above 200d, +19.9% in 3 months) and crop condition at 57% good/excellent vs 67% a year ago is supportive of prices, but the offsetting evidence is heavy: speculative net long at the 97th percentile of the past year and slightly rolling over, MACD histogram turning negative, volume only 0.67x average, and a measured -14.1% annual roll cost that has cost this fund 11-14 points versus the commodity itself. A crowded long into a contango-bleeding vehicle near range highs is not a place to add directional risk. Macro is quiet: 10-year unchanged on the week, VIX 14.6, though a firmer dollar (+0.90) is a mild headwind for commodities. The lone news item concerns diesel and is not a corn signal.

**Main reasons it gave:**
- Spec net long at 97th percentile of 52 weeks, down 0.5% on the week -- crowded and no longer building
- Roll cost -14.1%/yr; fund +13.4% vs corn +27.5% over 12 months
- Crop 57% good/excellent vs 67% year-ago, steady 3 weeks -- supply-supportive but already known
- Price 95.4% up 52-week range with MACD histogram -0.086 and volume 0.67x average
- Dollar index +0.90 on the week; rates and VIX essentially unchanged, no macro surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Diesel Hits Historic $6.51/Gal: Commodity Strategist Warns We Are Facing a Deficit That 'No Handshake' Can Refill](https://www.tradingview.com/news/benzinga:ebba5f08d094b:0-diesel-hits-historic-6-51-gal-commodity-strategist-warns-we-are-facing-a-deficit-that-no-handshake-can-refill/)  
  <sub>TradingView, 4 hours ago</sub>  
  The national average price for diesel reached $6.51 per gallon on Monday. A commodity strategist stated the supply disruption has moved into a diesel market...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.30</summary>

```text
Last close 20.12 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 19.94 (+0.9%), 50d 18.77 (+7.1%), 200d 18.06 (+11.4%); 50d above 200d
Momentum: RSI(14) 63.8 | MACD 0.346 vs signal 0.431 (histogram -0.086)
Returns: 1d +2.1% | 5d +0.5% | 1m +6.8% | 3m +19.9%
52-week range: 16.47 - 20.29 (now 95.4% of the way up)
Volatility: ATR(14) 0.31 (1.5% of price) | annualised 20d 16.2%
Volume: 0.67x the 20-day average
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
Cost of holding this fund instead of corn itself: -14.1% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +19.9%, commodity +31.3%, gap -11.3% | 6 months: fund +7.0%, commodity +16.1%, gap -9.1% | 12 months: fund +13.4%, commodity +27.5%, gap -14.1%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.20</summary>

```text
Corn rated good or excellent: 57% of the US crop (week 37 of 2026)
Direction over 3 weeks: steady, 0 points
Same week last year: 67% (-10 points)
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
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 22.5% of open interest (1,843,824 contracts)
Change on the week: -0.5% of open interest
Crowding: 97% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 8.26M | fund size: 166.21M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Uptrend is intact -- price near 52-week highs, above all major moving averages, 50d over 200d, RSI 57 -- but the breakout is on 0.38x average volume, which is not a decisive break. No macro catalyst: yields flat on the week, curve normally sloped, VIX calm at 14.6, and a firming dollar (+0.90) is a mild headwind for copper. Positioning is mid-range and specs trimmed 5.1% of open interest last week, so no crowding extreme either way. The -6.1% annual roll cost is a real drag that argues for wanting a larger move before taking a long. No news flow to weigh. Default to NEUTRAL with a slight positive tilt from trend.

**Main reasons it gave:**
- price at 96.5% of 52-week range, above 20d/50d/200d with 50d over 200d
- breakout volume only 0.38x the 20-day average
- roll cost of -6.1% a year versus spot copper
- CFTC specs net long 22.5% of OI but down 5.1% on the week, 40th percentile crowding
- macro quiet: 10-year unchanged, VIX 14.6, dollar +0.90 on the week

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.35</summary>

```text
Last close 40.62 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 39.74 (+2.2%), 50d 39.47 (+2.9%), 200d 37.13 (+9.4%); 50d above 200d
Momentum: RSI(14) 57.4 | MACD 0.043 vs signal 0.003 (histogram 0.040)
Returns: 1d +1.0% | 5d +6.2% | 1m +3.2% | 3m +4.7%
52-week range: 28.58 - 41.05 (now 96.5% of the way up)
Volatility: ATR(14) 0.73 (1.8% of price) | annualised 20d 28.2%
Volume: 0.38x the 20-day average
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
Cost of holding this fund instead of copper itself: -6.1% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +4.7%, commodity +6.7%, gap -2.1% | 6 months: fund +25.5%, commodity +27.0%, gap -1.4% | 12 months: fund +43.3%, commodity +49.4%, gap -6.1%
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
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 22.5% of open interest (289,463 contracts)
Change on the week: -5.1% of open interest
Crowding: 40% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: unknown
Share count change: n/a (too few readings)
Shares outstanding: 19.24M | fund size: 781.27M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [SPDR Gold Shares Tokenized ETF (Derivatives) Price Today](https://cryptorank.io/price/spdr-gold-shares-tokenized-etf-derivatives)  
  <sub>CryptoRank, 46 minutes ago</sub>  
  Current SPDR Gold Shares Tokenized ETF (Derivatives) (GLD) token data: Price $ 397.84, Trading Volume $ 91.25K, Market Cap $ 0.00, Circ.
- [Gold: The Rate Hikes Do Not Change The Bullish Thesis (NYSEARCA:GLD)](https://seekingalpha.com/article/4948345-gold-rate-hikes-do-not-change-bullish-thesis)  
  <sub>Seeking Alpha, 13 minutes ago</sub>  
  Gold has lagged stocks YTD, but inflation, deficits, and China's buying keep the long-term hedge case strong. Here's what investors need to consider.
- [Silver Crashes To Over 6-Month Lows – But This Analyst Sees ‘Very Limited Downside’](https://stocktwits.com/news-articles/markets/equity/gold-silver-falls-six-month-lows-analysts-remain-bullish/cZKyafnR7fW)  
  <sub>Stocktwits, 10 hours ago</sub>  
  Rashad Hajiyev, founder of RM Capital Consulting, said silver may consolidate for a while before gradually moving higher. Peter Schiff said that while gold...
- [Gold rebounds from $4K support as Timmer sees $5K in sight (GLD:NYSEARCA)](https://seekingalpha.com/news/4644631-gold-rebounds-from-4k-support-as-timmer-sees-5k-in-sight)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  Gold price outlook: Fidelity's Jurrien Timmer says global liquidity, M2 growth and ETF flows could drive gold from $4K toward $5K+.
- [BlackRock's IBIT bitcoin spot ETF surpasses GLD in daily trading](https://www.digitaltoday.co.kr/en/view/105702/blackrock-ibit-bitcoin-spot-etf-surpasses-gld)  
  <sub>디지털투데이, 16 hours ago</sub>  
  BlackRock's iShares Bitcoin Trust ETF, IBIT, rose more than 5 percent in daily trading and outpaced the SPDR Gold Shares ETF, GLD, in both trading volume...
- [The Options Weekly Ahead: Index Skew Resets, Gold Bets Build, SpaceX Vol Craters](https://www.moomoo.com/community/feed/the-options-weekly-ahead-index-skew-resets-gold-bets-build-117308120039430)  
  <sub>Moomoo, 7 hours ago</sub>  
  Last Week's Highlights Index Put Skew Snaps Back to Life. The cheapest hedges of the summer are gone. One-month put/call skew on the $S&P 500 Index (...
- [Fed Enters Tightening Cycle](https://www.streetwisereports.com/article/2026/09/21/fed-enters-tightening-cycle.html)  
  <sub>Streetwise Reports, 41 minutes ago</sub>  
  Michael Ballanger of GGM Advisory Inc. looks at the current state of the market after the Fed's recent hike.
- [Claude AI Predicts Bitcoin Could Outpace Gold if ETF Hedging Fades](https://www.coinspeaker.com/claude-ai-predicts-bitcoin-could-outpace-gold-if-etf-hedging-fades/)  
  <sub>Coinspeaker, 21 hours ago</sub>  
  Bitcoin has spent most of 2026 in gold's shadow. While the precious metal kept setting the pace as investors looked for protection against inflation and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 3.99% (+0.05 on the week) | 5-year 4.82% (+0.03 on the week) | 10-year 4.96% (+0.00 on the week) | 30-year 5.30% (-0.03 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 100.36 (+0.90 on the week)
Volatility (VIX): 14.62 (-2.5 on the week) -- calm
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 196k (2026-09-12)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.67% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 399.00 (bar of 2026-09-21), from 500 daily bars
Trend: vs 20d SMA 405.40 (-1.6%), 50d 393.41 (+1.4%), 200d 416.28 (-4.2%); 50d below 200d
Momentum: RSI(14) 49.0 | MACD -0.708 vs signal 0.759 (histogram -1.467)
Returns: 1d -0.5% | 5d +1.6% | 1m -3.9% | 3m +3.7%
52-week range: 339.18 - 495.90 (now 38.2% of the way up)
Volatility: ATR(14) 7.54 (1.9% of price) | annualised 20d 23.1%
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
Cost of holding this fund instead of gold itself: -0.4% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +3.7%, commodity +4.4%, gap -0.7% | 6 months: fund -3.5%, commodity -4.1%, gap +0.6% | 12 months: fund +18.9%, commodity +19.3%, gap -0.4%
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
Shares outstanding: 260.30M | fund size: 103.86B
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

