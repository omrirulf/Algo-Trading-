# Daily report

**19 Nov 2026, 18:30 Israel time (16:30 UTC)** · 80 names checked · 0 traded · 1 with a problem

**Answers with no explanation:** 18 of 64 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 6 | 10 | 0 |
| Whole-market funds | 14 | 0 | 13 | 1 |
| Sector and country funds | 41 | 0 | 41 | 0 |
| Commodities | 9 | 0 | 9 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| HDFC Bank (HDB) · Company | **Sold part.** Sold 51 of 102 shares at +3.02R, 51 still held. Stop-loss raised 25.27 → 25.40. |
| Brazil (EWZ) · Sector or country | **Stop raised.** At +0.97R, following the price. Stop-loss raised 32.88 → 32.01. |
| MercadoLibre (MELI) · Company | **Stop raised.** At +0.41R, following the price. Stop-loss raised 1561.59 → 1538.52. |
| Elbit Systems (ESLT) · Company | **Holding.** -0.11R, holding 7 shares. Stop-loss 640.17. |
| South Korea (EWY) · Sector or country | **Holding.** -0.24R, holding 51 shares. Stop-loss 148.87. |
| Alphabet (Google) (GOOGL) · Company | **Holding.** -0.20R, holding 4 shares. Stop-loss 274.24. |
| JPMorgan Chase (JPM) · Company | **Holding.** -0.04R, holding 15 shares. Stop-loss 340.79. |
| US regional banks (KRE) · Sector or country | **Holding.** -0.74R, holding 97 shares. Stop-loss 70.08. |
| Eli Lilly (LLY) · Company | **Holding.** -0.26R, holding 3 shares. Stop-loss 1304.66. |
| Nvidia (NVDA) · Company | **Holding.** +5.00R, holding 9 shares. Stop-loss 174.60. |
| Procter & Gamble (PG) · Company | **Holding.** +0.85R, holding 2 shares. Stop-loss 165.90. |
| Toyota (TM) · Company | **Holding.** -0.39R, holding 1 shares. Stop-loss 205.44. |
| US house builders (XHB) · Sector or country | **Holding.** -0.51R, holding 68 shares. Stop-loss 97.50. |
| US media and communication (XLC) · Sector or country | **Holding.** +1.56R, holding 47 shares. Stop-loss 104.93. |
| Exxon Mobil (XOM) · Company | **Holding.** -0.16R, holding 30 shares. Stop-loss 153.50. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Caterpillar (CAT) · Company — BEARISH, confidence 0.58

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Technicals show a strong downtrend (price far below 20‑, 50‑ and 200‑day SMAs, very low volume) and recent news highlight macro demand concerns and cooling power‑generation gear demand, outweighing bullish fundamentals and analyst optimism in the short‑term horizon.

**Main reasons it gave:**
- Price 2.9% above 52‑week low, 8.5%‑30.3% below 20‑, 50‑ and 200‑day SMAs
- Volume at 0.08× 20‑day average indicating weak buying pressure
- Macro demand concerns and dealer destocking highlighted in recent news
- Operating margin 18.8% and profit margin 15.2% indicate strong fundamentals
- Consensus buy with mean price target $807 (+44% upside) but no recent rating upgrades

<details><summary><b>News</b> — score -0.30</summary>

- [Is Caterpillar Stock Priced Right Against Its Rivals?](https://finance.yahoo.com/markets/stocks/articles/caterpillar-stock-priced-against-rivals-140505151.html)  
  <sub>Yahoo Finance, 40 minutes ago</sub>  
  Today's big story: Could Anthropic Stock Fall 25%? · Caterpillar (CAT) earns the widest operating margin among six machinery makers, a group that also...
- [Caterpillar’s AI Boom Went Bust. Why Smaller Equipment Could Spark a Comeback.](https://www.barrons.com/articles/caterpillar-stock-ai-compact-construction-equipment-79500887)  
  <sub>Barron's, 22 hours ago</sub>  
  Caterpillar had demand for its power-generation gear. Now, that's cooled. Here's the next catalyst for the beaten-down stock.
- [Caterpillar Is 48% Below Its High With Analysts Still Expecting $32.18 of 2027 Earnings Per Share](https://www.google.com/goto?url=CAESugEBxCJF1_nhFZTqZ6_CY1gqOnX7WFJNvdl1Jq7p5ev1ktw-OatwF1VoaQ6mV0VhOkkW5i14d80Fairai_3yvqsNDBsnn2majC3b7YxLFuoCewqWk1QYb4OYFTb6pYKhIsLGhri7kBgXYef_cskTRCd1A80rTv0-eEXwOQ37ta31r4Lm0FRqpXeX9WvJqfA7zFgUiQ_cY8-awV6AUcL8GuniZhCbNNyLxWJeoZ-koQSgx3xiz2dDZiSyUDo&gsessionid=dk_VgDtnschWtOFc3po1u8KOhhLYHr_eGgYlsLW1QNJw3KiGSy9wMA)  
  <sub>TIKR.com, 2 hours ago</sub>  
  Caterpillar is 48% below its June 30 high, yet analysts expect $32.18 of 2027 normalized EPS, up from $30.15 at the peak. Its forward P/E has fallen from...
- [Is Red Cat Stock a Buy After Its Nov. 16 Earnings Report?](https://www.google.com/goto?url=CAESygEBxCJF1-wa3EXLRmQ97INMI9MuE09BwIWQoamnC0CW3XI-kG6se-9q9ZVi41szKlVahpl2X5FzT2wN_XqbZJqqT2L9wRXkAu4fOHPLxrd1w7jHhS87Ev3nPwP9bUojRmfPbSFzphxmEsdd9M0b34QYUcUjFDkfCEh93h4ul77F_DzKoMpb1yY3h4TZ5-YW56Jl-uQgkavMjzFVF_BI4scNsmZ0TAJLoraDFQgyqttj-HKtT1FezJxhmTz-QYY1EF1q_qXmofbTD924&gsessionid=dk_VgDtnschWtOFc3po1u8KOhhLYHr_eGgYlsLW1QNJw3KiGSy9wMA)  
  <sub>The Globe and Mail, 24 hours ago</sub>  
  Red Cat(NASDAQ: RCAT) reported its third-quarter results after the market closed on Nov. 16, and results were far worse than anticipated.
- [Red Cat Falls 6% as Post-Earnings Selloff Extends; Unusual Machines Slides 3%, AeroVironment Drops 2%](https://www.google.com/goto?url=CAESygEBxCJF1zBIO6A2Ec7rJNPvncBrngBNnQHNfy2slzLM5ZgOeCa89ttgM3odjj8WwHYeTwuBuJEfiYxP4-JoSQWSADvmRxHHUZD_TuKbXJrAZZPY7erj3ou5dOz9JZC6Ydz669chg2DimGe4cBgzKLiSRWC_MvVWRL496ohx8gwdQdORXH4hdbNSyIFN2c3cgkkq3DlL202JqC_WHEMUoFypxoJdavGPnogLhnQD43AtXQ27Yo2WO1OfHCkjWGUopM-CEl2H9PL4eKH9&gsessionid=dk_VgDtnschWtOFc3po1u8KOhhLYHr_eGgYlsLW1QNJw3KiGSy9wMA)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  Red Cat (RCAT) sank 6% to $2.28 after Q3 revenue of $12 million missed estimates by nearly $29 million and management scrapped full-year guidance.
- [Caterpillar's 'Best-In-Class' Construction Business Is Getting Overlooked, Analyst Says](https://www.google.com/goto?url=CAES3QEBxCJF17U8giPSYlQpZJC9Xxvo-oQPSsGYQawhDcOpijLBKf2bgQFaURUjvS-c_WCr19NUSX2bLXZnW9CHyAgO54grK_eP185bRNlYVKTWJGitVMmlQ4eeEgli5YN-ST1vr2-Ld0uvN1q3TXvZrLsr0IwYHyReALrSExqrayfMHiBnZKUZPheP9PVtEpF4KNzmNEY_5zGsKlTT4aqWTi9dw-CsDIHkuYnF9uI8DOE386ohFf2dAYInRjLd6q5DNsVatiPvdxFI21CyNxRjF55_Taux_YpLNd1ULjGnuw&gsessionid=dk_VgDtnschWtOFc3po1u8KOhhLYHr_eGgYlsLW1QNJw3KiGSy9wMA)  
  <sub>Benzinga, 20 hours ago</sub>  
  BofA reiterates a Buy rating on Caterpillar (CAT) with a $746 price target, citing undervalued construction growth.
- [Caterpillar Inc Stock (CAT) Moved Down by 3.10% on Nov 18: What Signal Does It Send?](https://www.google.com/goto?url=CAESjwEBxCJF191aLX3yxa3c2V0rq_003yBSZnw5UjjowfH3eyiDXhqujO_AQZNFeg-3s8WVAQUWBTFxwF3Tk-QZYE-CN-6BAD2Ro1AR-ZqW3U6kDkHqplp_vwHAc5fm4MIw0JgGnLu44OSdNS89Sciq10AIf3JKePz_tti5HnbHsyB4UedGy98ME4bKgIqfAM1izw&gsessionid=dk_VgDtnschWtOFc3po1u8KOhhLYHr_eGgYlsLW1QNJw3KiGSy9wMA)  
  <sub>TradingKey, 22 hours ago</sub>  
  Caterpillar faced downward pressure due to macroeconomic friction and cyclical demand concerns.High borrowing costs and dealer destocking tempered demand...
- [New Analyst Forecast: $CAT Given $685 Price Target](https://www.google.com/goto?url=CAESlgEBxCJF12t6JfScfFbAAI5jS1NqF7RvKiFXxdKhviOysnv4pCXoGhB00PgZtSxGiYof-FlJSGwyl1O292-QMSrx4yeleAkfb5QmHF2a4YejWcteUdlECNR15QxQm3dc2TZht_W0XOMWuOhvCJyrsfBB3vty8AZFexODIWYbJ5JmvjN7XvsaIeo--9kdK6CNIr8b6Z11jrU&gsessionid=dk_VgDtnschWtOFc3po1u8KOhhLYHr_eGgYlsLW1QNJw3KiGSy9wMA)  
  <sub>Quiver Quantitative, 16 hours ago</sub>  
  We just received data on a new analyst forecast for $CAT. Michael Shlisky from DA Davidson set a pri.
- [Caterpillar (CAT) Adds Safety Tech As Investors Ask If The Story Is Already Priced In](https://www.google.com/goto?url=CAESwgEBxCJF1_3EKvEJFXiGI1QXfqKg5SEGmpzWptOnuyEcV_ap9GvSU8l-RwlLKd9q2BMkLRLrf4PvBkEKizXgaoqe7dXDHK80Lc_2HJIjb7Cd2yZ5u3M2MQOWifbaVRn20sWZ4ELtFeZqRgOUT3ZiI7MuG1dUNZR9BePZWWmHYCootG-EBoVZFRb9A2DyTk7qFrz2IKvt2QCxXCn-GvdFxG8fvEj958fZt0Wu20WTpP6_5hmMxB_v08JU0CfLpZwhiR09QA&gsessionid=dk_VgDtnschWtOFc3po1u8KOhhLYHr_eGgYlsLW1QNJw3KiGSy9wMA)  
  <sub>Simply Wall St, 16 hours ago</sub>  
  Caterpillar stock: safety tech shift catches investor attention Caterpillar (CAT) is rolling out collision warning and mitigation systems as standard...
- [Avoiding Lag: Real-Time Signals in (CAT) Movement](https://www.google.com/goto?url=CAESvAEBxCJF14R-8Y01QYsaySW_7TfljtH9w3svBwPToEbuH9wBbjTmWjOhHwBp8YWZv2fcMTnpk1PJyTPjroVIhiIaqPKUup6xjrzdwX_hEMkOVArcgq6ZRDc1DASOrNkqu2BV01NZhthQGNfvOWuA9t14_tqgjAHsmzhcywmEik2fe9AURFj6n74gXW-HIBMmbf_hMrfrEB2ioQE10kDYLAHbgXtHfyGdBf2CP9-U_aHJlcouLtTI09jQrI-e5g&gsessionid=dk_VgDtnschWtOFc3po1u8KOhhLYHr_eGgYlsLW1QNJw3KiGSy9wMA)  
  <sub>Stock Traders Daily, 22 hours ago</sub>  
  Key findings for Caterpillar Inc. (NYSE: CAT). Weak Near and Mid-Term Sentiment Could Challenge Long-Term Positive Outlook; No clear price positioning...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 561.33 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 613.45 (-8.5%), 50d 720.86 (-22.1%), 200d 805.02 (-30.3%); 50d below 200d
Momentum: RSI(14) 30.6 | MACD -46.015 vs signal -47.533 (histogram 1.518)
Returns: 1d +0.5% | 5d -7.3% | 1m -24.2% | 3m -32.2%
52-week range: 546.13 - 1,064.90 (now 2.9% of the way up)
Volatility: ATR(14) 27.10 (4.8% of price) | annualised 20d 59.1%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 256.86B
Valuation: trailing P/E 22.03 | forward P/E 17.44 | P/B 11.96 | PEG 0.98
Profitability: profit margin 15.2% | operating margin 18.8% | ROE 56.1%
Growth (YoY): revenue +17.3% | earnings +46.1%
Balance sheet: debt/equity 210.4% | free cash flow 3.97B
Risk: beta 1.64 | short interest 2.0% of float
Next earnings: 2027-01-28
```

</details>

<details><summary><b>What this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.60</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 in line
  2026-09-30 in line | 2026-06-30 beat by 31% | 2026-03-31 beat by 19% | 2025-12-31 beat by 9%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

```text
Consensus: buy (mean 1.97 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 2 strong buy, 15 buy, 11 hold, 1 sell, 0 strong sell
Price target: mean 807.26 (+43.8% vs last close), range 575.00 - 1,027.00
Recent rating changes:
  - 2026-11-10 Evercore ISI Group: main, Outperform -> Outperform
  - 2026-11-02 Freedom Broker: main, Buy -> Buy
  - 2026-11-02 DA Davidson: main, Neutral -> Neutral
  - 2026-10-30 JP Morgan: main, Overweight -> Overweight
  - 2026-10-30 Citigroup: main, Buy -> Buy
  - 2026-10-30 Wells Fargo: main, Overweight -> Overweight
Institutional ownership: 74.3%
Largest holders: Blackrock Inc. (8.2%), State Street Corporation (7.5%), Vanguard Capital Management LLC (6.6%), State Farm Mutual Automobile Insurance Co (3.1%), Vanguard Portfolio Management LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

```text
Last 180 days: bought 47,091 shares in 10 transaction(s) | sold 32,401 shares in 1
Net: +14,690 shares (+1.3% of insider holdings) | insiders hold 1,130,257 shares
Distinct insiders: 1 buying, 1 selling
Open-market purchases — insiders spending their own money:
  - 2026-11-02 FISH JAMES C JR (Director): 1,000 shares, 620.39K
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-08-28 CREED JOSEPH E (Chief Executive Officer): 32,401 shares, 26.21M
(9 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

_Not available today._

</details>

### Microsoft (MSFT) · Company — BULLISH, confidence 0.58

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- J.P. Morgan maintains Buy rating with $625 price target (+22% upside)
- Strong fundamentals: ROE 34.2%, profit margin 41.2%, low debt/equity 28.5%
- Earnings record: 3 beats, 1 in line over last 4 quarters
- Technical: low volume (0.10x 20‑day avg) and RSI 48.7 (neutral)
- Insider net buy of 257,656 shares (+3.1% of holdings)

<details><summary><b>News</b> — score +0.40</summary>

- [Microsoft (MSFT) Stock May Look Reasonable As AI Commitments Draw Scrutiny](https://finance.yahoo.com/markets/stocks/articles/microsoft-msft-stock-may-look-121347165.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Microsoft has pulled back from recent highs but still trades near the top of its range after a multi year climb, which puts a spotlight on a simple question...
- [Microsoft (NASDAQ:MSFT): A High-ROIC Quality Stock for Long-Term Investors](https://www.chartmill.com/news/MSFT/Chartmill-58913-Microsoft-NASDAQMSFT-A-High-ROIC-Quality-Stock-for-Long-Term-Investors)  
  <sub>ChartMill, 5 hours ago</sub>  
  Microsoft passes key quality tests with 30.6% ROIC and low debt/FCF, but EBIT leverage, cash conversion and valuation need monitoring.
- [Microsoft: Remains My Pick Amongst Hyperscalers](https://www.google.com/goto?url=CAESlAEBxCJF16-qW-I0TF4viyAJOKPN8V-DtHK1E-QSVOD-5Yvv-yXNScPbDRwc5k0lowxG0i1bQl4Z5wVaISkbd0UjYfzozfTsezu211Fo1D1JcxQo6ddEAiE5UoTwpxZb8P7FprJpawbHf2UcdPco2cQFBiuTZ1hI9qXvw6u6KWaLC1IUBImK02brauwptJI7ZUFe7MQt&gsessionid=L7LjbR5e-ka7OSP7D2moFLMZeOY57lex9-ENkj8u8KpBhvkOm7Ynow)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Microsoft (MSFT) stock remains a buy, as resilient software, AI exposure, and improving margins support further upside.
- [Microsoft’s CEO Says He’s “Extremely Sorry” for the Outlook Outage](https://www.google.com/goto?url=CAESpwEBxCJF13C-OwPzHPWEWvo4yklNNINVtHwVQ7ahpBcV5l2tMUHpVz7vplm9_YkYAYvprAoLPx5A7esavypRuNSYFtTm-4nO359dm4tBiN1pQOqYaKpNDovSESbNBPj0R1rlgVLF5rK4ihsssci_9EikxL-JhUQRxwG8OKpKZP0pIIle71Iae2Ycx2uvNYYXcPO7CHioPOpUUMKX2b07tNb9790KcIN9Zg&gsessionid=L7LjbR5e-ka7OSP7D2moFLMZeOY57lex9-ENkj8u8KpBhvkOm7Ynow)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Microsoft (MSFT) shrugged off Satya Nadella's "extremely sorry" apology for the day-long Outlook, Teams and Copilot outage, with shares closing up 0.4% at...
- [New Buy Rating for Microsoft (MSFT), the Technology Giant](https://www.google.com/goto?url=CAESywEBxCJF1753Fi8F_2wn3f4ekZ_xUVSKI2jlP0_bd6mo7hJPrUDmnpuN0iMeloS-NulG5alWI-AJPBwSQ2i_iDnLDmffact9-sGUzEoFjjPn1OTnKVO7D8s0y1ilxPspScQDUPrzZY8Pzdhww-71qk8BsEb18BbMpZScKktC4In1iUv6TgDaNqdAIpDP43NvnYLShzFPkLfJa3x2ZjuOCBzs7DxRTvfsKya6NmT4TaoMOaeWGpX-h5HZivABXwzfDVgroCld0gfizdJBWQ&gsessionid=L7LjbR5e-ka7OSP7D2moFLMZeOY57lex9-ENkj8u8KpBhvkOm7Ynow)  
  <sub>The Globe and Mail, 7 hours ago</sub>  
  In a report released today, Samik Chatterjee from J.P. Morgan maintained a Buy rating on Microsoft, with a price target of $625.00.
- [Microsoft stock consolidates near $512.23 resistance as mixed momentum signals persist](https://www.google.com/goto?url=CAESlQEBxCJF10ylzRjWJ577c7yUN93CQ8waT3cSN0OCXJTOvrueLM3vGpNxZ_ZAtLDgU3DBuGhGLY5ZoWarbWi6zGufvRPIubc9E9g1iiWcjJKP4kocp-XKnS8AwrMfkXE2EyoUhQ8POhHJ7otoA5MArnNjhuLKQhfh7z6O0qTMWApYuOlv7SdLMmge1icPHj6koptEolCTlA&gsessionid=L7LjbR5e-ka7OSP7D2moFLMZeOY57lex9-ENkj8u8KpBhvkOm7Ynow)  
  <sub>Traders Union, 28 minutes ago</sub>  
  Microsoft trades at $508.33 today, up 0.41%. Get the latest on price action, news, and technical insights for MSFT.
- [Microsoft Stock (MSFT) Rises 0.4% to $508.29 (Nov 18)](https://www.google.com/goto?url=CAESiwEBxCJF19zCRdI7qCXW7Rs_gagmIwrqoIbhHdnGR7CmCo6c--JHmHyhRoQmO-izNKDB_6dJ9GBI-Lw-LaHMicpJ-4kc66wZ1azMQcqjFiGCFw9pIqdLdnl8VAFlZeYvx1wv_hOt0f_7OOYxsYTWAz3IVqn7aFDbh5DwlhwjmNAagZLIW-39Ej0ceZzl&gsessionid=L7LjbR5e-ka7OSP7D2moFLMZeOY57lex9-ENkj8u8KpBhvkOm7Ynow)  
  <sub>Gotrade, 10 hours ago</sub>  
  Microsoft (MSFT) closed at $508.29 on Nov 18, up 0.40% in line with the Nasdaq, as Satya Nadella spoke at DealBook and Microsoft explained its outage.
- [Microsoft Stock (MSFT) Forecast – Mizuho Stays Bullish on Strong Revenue Growth Prospects](https://www.google.com/goto?url=CAESogEBxCJF13-HMfoAyq8atmABpDNqDks8TgHofsppwqjw0oDyF1Uzw-oxE3J5xCf-nks_VMuSfqnDXSW9kxWYfhwF9yrKPf2AFemBjqCqfu5_ZOpGNBDlbVRzE4HDs1_vNN5nft_f9pySTc5dDdVoTiRP-ijjfceNjGI8gLnGlu32dWbTtzWAWQValqujAXUAi02e_uFLpCfveb9sPGWYCA93Efc&gsessionid=L7LjbR5e-ka7OSP7D2moFLMZeOY57lex9-ENkj8u8KpBhvkOm7Ynow)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Tech giant Microsoft (MSFT) unveiled new AI models at its Ignite conference amid intense competition from AI players OpenAI and Anthropic (ANT).
- [Anthropic shatters record books with $81 billion blockbuster IPO](https://www.google.com/goto?url=CAESsQEBxCJF1wKITJmxfV0wnqeCPrE1kazaDuaBRelRz5Ruk16M3SbXOwC-pKUALb2g4aXql7mS4eRrLKveeL6lGgHs9npdlIh9__TcgJmlcHYtdQgeO5oRrdLoUQfoVh_id1Ghlzi89-PWMWwr5V2jLnpca4U_NHYkVqpsOL32AxcS_zKWIpn1xel6vNux_Z578sTw-8oZQ0ywgHFe-fd7zxAY2YjKwaE1fxDHnK2qsYmCqPA&gsessionid=L7LjbR5e-ka7OSP7D2moFLMZeOY57lex9-ENkj8u8KpBhvkOm7Ynow)  
  <sub>marketscreener.com, 32 minutes ago</sub>  
  Nov 19 - Anthropic raised $81 billion in its blockbuster initial public offering, smashing records and eclipsing SpaceX's June listing to become the largest...
- [Microsoft: The Last Hyperscaler With Positive Free Cash Flow (NASDAQ:MSFT)](https://www.google.com/goto?url=CAESoQEBxCJF1yHkTwOwV5taA6oc3tEDLkEnyYLYNLdB2yZakpOThFtGixmf1TkIxe39BLqqZf1CILWkiJQR8296J7d-6BZK3hvqQR-6Pu7Q0zxH6PR_N8jYE5ul9vNX0E7KBz2VgKJNuWltvMJ-MqEAd8xdRHzS-zT3iqm0iTD2T6aQ8ocvpVudI-wz9__vdlp5FpaegUkkBPBbzRNcJwyMKrypZQ&gsessionid=L7LjbR5e-ka7OSP7D2moFLMZeOY57lex9-ENkj8u8KpBhvkOm7Ynow)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  Microsoft Corporation is the only one of the five major hyperscalers that is still delivering positive free cash flow.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 520.25 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 526.05 (-1.1%), 50d 520.50 (-0.0%), 200d 443.29 (+17.4%); 50d above 200d
Momentum: RSI(14) 48.7 | MACD -1.896 vs signal 0.893 (histogram -2.789)
Returns: 1d +2.4% | 5d -0.5% | 1m -2.4% | 3m +7.7%
52-week range: 352.83 - 555.80 (now 82.5% of the way up)
Volatility: ATR(14) 14.91 (2.9% of price) | annualised 20d 38.0%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.80</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.86T
Valuation: trailing P/E 27.15 | forward P/E 21.49 | P/B 8.21 | PEG 1.50
Profitability: profit margin 41.2% | operating margin 47.1% | ROE 34.2%
Growth (YoY): revenue +18.8% | earnings +32.3%
Balance sheet: debt/equity 28.5% | free cash flow 2.99B
Risk: beta 1.04 | short interest 0.8% of float
Next earnings: 2027-01-27
```

</details>

<details><summary><b>What this fund holds</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.80</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 in line
  2026-09-30 in line | 2026-06-30 beat by 10% | 2026-03-31 beat by 3% | 2025-12-31 beat by 3%
```

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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: strong_buy (mean 1.37 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 12 strong buy, 41 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 636.12 (+22.3% vs last close), range 440.00 - 870.00
Recent rating changes:
  - 2026-10-29 Bernstein: main, Outperform -> Outperform
  - 2026-10-29 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-29 Citigroup: main, Buy -> Buy
  - 2026-10-29 DA Davidson: main, Buy -> Buy
  - 2026-10-29 TD Cowen: main, Buy -> Buy
  - 2026-10-29 Scotiabank: main, Sector Outperform -> Sector Outperform
Institutional ownership: 76.9%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.3%), FMR, LLC (2.7%), Geode Capital Management, LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 518,348 shares in 17 transaction(s) | sold 260,692 shares in 11
Net: +257,656 shares (+3.1% of insider holdings) | insiders hold 8,688,647 shares
Distinct insiders: 0 buying, 4 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-11-10 NUMOTO TAKESHI (Officer): 5,000 shares, 2.65M
  - 2026-11-09 HOOD AMY E (Chief Financial Officer): 7,305 shares, 3.98M
  - 2026-10-13 HOOD AMY E (Chief Financial Officer): 7,305 shares, 3.98M
  - 2026-09-14 HOOD AMY E (Chief Financial Officer): 41,674 shares, 20.76M
(16 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### ASML (ASML) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> The news flow is strongly positive, highlighting AI demand and ASML's near‑monopoly in EUV lithography, while fundamentals are exceptionally strong. Technicals are bearish, showing price below key moving averages and low volume, which tempers conviction. Overall the bullish catalysts outweigh the technical weakness, leading to a moderate‑conviction bullish signal.

**Main reasons it gave:**
- ASML stock surged 4.9% in the last session, driven by AI demand and EUV monopoly (NEWS)
- Strong profitability: profit margin 34.1%, operating margin 38.6%, ROE 65.6% (FUNDAMENTALS)
- Technical indicators bearish: price below 20‑day, 50‑day, 200‑day SMAs; RSI 40.6; volume 0.13× 20‑day average (TECHNICALS)
- Earnings record: 3 beats and 1 miss in last 4 quarters, recent miss of 5% (EARNINGS RECORD)
- Analyst consensus strong buy with mean price target +47% vs last close (ANALYST & INSTITUTIONAL VIEW)

<details><summary><b>News</b> — score +0.70</summary>

- [Why is ASML stock surging today?](https://www.investing.com/news/stock-market-news/why-is-asml-stock-surging-today-93CH-5038522)  
  <sub>Investing.com, 3 hours ago</sub>  
  Investing.com -- ASML stock surged 4.9% to reach €1,322 during today's session, bouncing back forcefully after the prior session's steep decline driven by...
- [Why ASML Holding (ASML)’s Monopoly in EUV Technology Gives It a Powerful Competitive Advantage](https://finance.yahoo.com/technology/articles/why-asml-holding-asml-monopoly-110444090.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  We just published our list, Ken Fisher Portfolio Review: 10 Highest-Conviction Technology Stocks for Long-Term Growth, and Cisco Systems, Inc. ranked 6th on...
- [Thinking About Buying Anthropic’s IPO on Nov. 19? Here’s an AI Stock I’d Consider First (Hint: It’s Not Nvidia or Broadcom).](https://www.google.com/goto?url=CAES3wEBxCJF10Kc0S8H1kJNK6stl87SNHdhJHddZpeki-KCDNOmR00C5bvB9yhEzo6sQmf-VzLRo5vHezRoNjo5aMYyEo1AiVxmZc5a-TT8CVG6geVCa4o0naE0qKwVBrfPOsve_g3iDn3UoAmMyxItp57TC-rBgOPjT1nfIJn6cA4-9yDXkSAdq0w-LBZ_SKFEEJK3gr-6pyyhkaizL6TvNtykrYuOUIWpawgpD8WjLkAk3myXWcLZDkIs47gwCkbNDj38Gtm9CJUpULeHwqHbMTfw4FVEPsltvzGQ4sIiDwqD&gsessionid=NFm2BMTDcC6hEIniHYobwU1OxPxpcUQLMqsm7SuBfAtRX5GRMLNcYg)  
  <sub>The Motley Fool, 15 hours ago</sub>  
  ASML's impeccable fundamentals allow investors to rest easy amid AI stock volatility.
- [ASML emerges as a top AI stock pick as volatility hits ahead of the Anthropic IPO](https://www.google.com/goto?url=CAESeAHEIkXXwdem9mNre3Kp0p_AX5UNWHnx0lNWwjgyyCq8-ud2qtnH4VWUtpc30mFLxt35nKzGylF00tc6OqIdM4cIsL5rm8r1uy8WNExDgw2sdWncCgPwxClvFMOpp3fQbBplFtMJ2G4NWjDUYJvYK7gJ2Omiq7TsfQ&gsessionid=NFm2BMTDcC6hEIniHYobwU1OxPxpcUQLMqsm7SuBfAtRX5GRMLNcYg)  
  <sub>Crypto Briefing, 15 hours ago</sub>  
  ASML slips into a correction as AI stocks wobble, while Anthropic targets a $1.4 trillion valuation ahead of its November 19, 2026 IPO.
- [ASML Holding shares rebound 4.5% but are down 14.5% over the quarter](https://www.google.com/goto?url=CAESugEBxCJF12N6rChMB69pJQ3mptsFjb5z9T0-YZ_4u5iHWTs-ZNCum9S7ntuhnE2W39Sg4xDYxxue-IQTwNzslmhp34wUPF6YGe1JbgIXIH3FYDkX9JC3Nm8iO8mA6ZHWYf3h8smUCQYKCV9ZL-SavXm4AwAytmArD7gs72BjV-w2AUlw9y3DEn0ZMSc3K6EtevPDqETcZEUh_4eR38CM9KOfqnJV8Kunj82WC1ws0VMcC-EaOloVJNRN5-c&gsessionid=NFm2BMTDcC6hEIniHYobwU1OxPxpcUQLMqsm7SuBfAtRX5GRMLNcYg)  
  <sub>Idéal Investisseur, 3 hours ago</sub>  
  The ASML stock gains 4.33% to €1,315.40, versus €1,260.80 at the previous close. It nevertheless fell 6.3% over the week and 14.68% over three months,...
- [NVIDIA's Leadership Woes: Buy TSMC & ASML Despite Supply-Chain Risks?](https://www.google.com/goto?url=CAESpgEBxCJF17JL0HRonnUOpvSy3-VrdYnBZX84Q0PUTxj5FyxKlr5sAakUMAaMPAL0Y7CAg2sZMaslj6WFOaowweDkItEcgWo0u5LVI7BKfgC0pJ1Iw9YakoLhsIOwJ4kk5i-D8Q2UE7YS_GA6ioVIEHvkAcrLAUX3ASm-a2dfmaWLcEZWQGsOdHSx1t1w2-Q5F4P8zuwP3jyjNPVTTWGNxA4m0If6W7k_&gsessionid=NFm2BMTDcC6hEIniHYobwU1OxPxpcUQLMqsm7SuBfAtRX5GRMLNcYg)  
  <sub>Zacks Investment Research, 19 hours ago</sub>  
  TSMC and ASML shares fell 9.5% and 10.8%, respectively, amid NVIDIA's leadership uncertainty. TSMC benefits from robust AI demand, advanced-node leadership...
- [Nvidia AI Boost Could Matter For ASML Stock (ENXTAM:ASML)](https://www.google.com/goto?url=CAESxQEBxCJF11km85lotZbjFIDj4Ww9T_9h_zqiuobBlSPl6paKZhoPHppbqFgFdbzPUB-kso79IgHtsliqtuj6HDMBDvSwnfUCw5XFNI7fdtYBvu7KmdLoSMk6MqDk_1YrFcimY4Y2DalJx564eKMrHwH2clpuO-zBYGzXkn6FCibk4t0kkF1bUgUHJaUjRMUly1IYMBYcSIhAWnUoFWh9uiP3HU2Bb0gec4YHBmdKLNkrxS9OaHERTmFpPGIdTnB1LIccvmi26A&gsessionid=NFm2BMTDcC6hEIniHYobwU1OxPxpcUQLMqsm7SuBfAtRX5GRMLNcYg)  
  <sub>Simply Wall St, 10 hours ago</sub>  
  Nvidia's recent earnings beat and upbeat AI guidance lifted confidence in chip demand. ASML Holding is benefiting as a key supplier of advanced lithography...
- [ASML stock gains appeal as a safer AI investmen...](https://www.google.com/goto?url=CAESlgEBxCJF1zsUXSg2MdmBy9LqbeNbS_ovO1Up4WCrnpCvKqax4edLniIbKAsTOdxGi8Aa1971SJHNO9K2u4CObLxX8I7iYMbhtwvla-BAcX45nUyjUcfrLgIrszDpjTntZQnQ3F0CG_mwgPpRABH3Y5dduKOCetDreJEFDTVgpsT7XMCICJG47NnVNMKb3wr2YlVP7sIcPiM&gsessionid=NFm2BMTDcC6hEIniHYobwU1OxPxpcUQLMqsm7SuBfAtRX5GRMLNcYg)  
  <sub>Pluang, 14 hours ago</sub>  
  ASML is emerging as a strong AI stock pick due to its near-monopoly on advanced lithography machines essential for manufacturing next-gen AI chips.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 1,434.68 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 1,511.32 (-5.1%), 50d 1,634.96 (-12.2%), 200d 1,602.32 (-10.5%); 50d above 200d
Momentum: RSI(14) 40.6 | MACD -65.663 vs signal -61.351 (histogram -4.311)
Returns: 1d +2.8% | 5d -4.2% | 1m -14.4% | 3m -18.7%
52-week range: 966.57 - 1,989.44 (now 45.8% of the way up)
Volatility: ATR(14) 63.31 (4.4% of price) | annualised 20d 61.2%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.80</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 552.95B
Valuation: trailing P/E 35.30 | forward P/E 22.63 | P/B 1,231.89 | PEG 0.73
Profitability: profit margin 34.1% | operating margin 38.6% | ROE 65.6%
Growth (YoY): revenue +55.2% | earnings +135.9%
Balance sheet: debt/equity 8.9% | free cash flow 10.37B
Risk: beta 1.33 | short interest 0.3% of float
Next earnings: 2027-01-27
```

</details>

<details><summary><b>What this fund holds</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.80</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-09-30 beat by 17% | 2026-06-30 beat by 9% | 2026-03-31 beat by 7% | 2025-12-31 missed by 5%
```

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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

```text
Consensus: strong_buy (mean 1.37 on a 1=strong buy to 5=strong sell scale, 17 analysts)
Ratings: 7 strong buy, 31 buy, 2 hold, 1 sell, 0 strong sell
Price target: mean 2,112.61 (+47.3% vs last close), range 851.09 - 2,795.78
Recent rating changes:
  - 2026-10-15 JP Morgan: main, Overweight -> Overweight
  - 2026-07-16 JP Morgan: main, Overweight -> Overweight
  - 2026-07-16 Wells Fargo: main, Overweight -> Overweight
  - 2026-07-16 RBC Capital: main, Outperform -> Outperform
  - 2026-07-14 RBC Capital: main, Outperform -> Outperform
  - 2026-07-06 Bernstein: main, Outperform -> Outperform
Institutional ownership: 19.9%
Largest holders: FMR, LLC (1.5%), Fisher Asset Management, LLC (1.2%), Capital World Investors (0.9%), Invesco Ltd. (0.7%), State Farm Mutual Automobile Insurance Co (0.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 1,915,500 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Novo Nordisk (NVO) · Company — BEARISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “SELL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Technical: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 44.8; low volume (0.30x avg)
- Earnings: 2 consecutive misses (22% and 6% miss) indicating earnings weakness
- News: reports of intense obesity‑drug competition and pricing scrutiny driving a 2.7% pullback
- Analyst consensus: hold with recent downgrades (Morgan Stanley, Goldman Sachs) and modest price target (+16%)
- Fundamentals: strong profitability (ROE 58.4%) but earnings growth down 15.8% YoY

<details><summary><b>News</b> — score -0.20</summary>

- [NVO Nov 2026 40.500 call (NVO261120C00040500) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/NVO261120C00040500/)  
  <sub>Yahoo Finance UK, 15 hours ago</sub>  
  Find the latest NVO Nov 2026 40.500 call (NVO261120C00040500) stock quote, history, news and other vital information to help you with your stock trading and...
- [Novo Nordisk: The Worst May Be Behind (NYSE:NVO)](https://seekingalpha.com/article/4969689-novo-nordisk-the-worst-may-be-behind)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Novo Nordisk is rated a long-term Buy, as falling capital spending supports higher free cash flow, with a DKK 393.21 intrinsic value.
- [Novo Nordisk A/S Stock (NVO) Moved Down by 3.12% on Nov 18: What Investors Need To Know](https://www.google.com/goto?url=CAESjwEBxCJF1-bGOfdPACeHF1C-cMHrMRL3jABP4m_RW_15_uHRszdZ7z7DD_KMm71DhvRV8KLrsYpx7Mr38_iDwSxd6zZkeTSzO4pj7VIvWt0oGKIK66NfcdjGqqCPXLRIO_ZhEqg4wrOucbQ1a8tdRggb8AVX1ybBnxYxrePzpoPNVTc1e1v8J1dk3S5Xh8JE8g&gsessionid=pm8wVpp93keRMnwqlqnTTJ-qeRmqVQEUkSfNBG01HmqnwrHlD_G95g)  
  <sub>TradingKey, 18 hours ago</sub>  
  Novo Nordisk faced downward trading pressure from intense obesity drug competition.Drug pricing scrutiny and manufacturing risks impacted institutional...
- [What's behind Novo Nordisk's latest 2.8% stock pullback?](https://www.google.com/goto?url=CAESlAEBxCJF1567pijMoX6EXYN0vDtCz_bkXnO3xDdYqjVbPSjyb3MHL_0po1K4ahkYYcJQPjimcS47OneqIZIjTd9I-HTihSJcGAL7L8R-idgKQoGaS0JI29_ixzPNtwehc-efrO1nVJUsp_9nWGA-JeSHZBx4uNHGrttSDdLovVyAfjwzvbZ3-ZUMOe1BAPLC4OUdtDF0&gsessionid=pm8wVpp93keRMnwqlqnTTJ-qeRmqVQEUkSfNBG01HmqnwrHlD_G95g)  
  <sub>Traders Union, 23 hours ago</sub>  
  Novo Nordisk A/S (NVO) dropped 2.75% after sellers pressured the stock lower at the open, even as the company continued its large-scale share buyback...
- [NVO Jun 2028 42.500 put (NVO280616P00042500) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXnqwXVfK9mrJKRhRm9_POo22OPIxFlx65CN2pyw5pp-Fu1HOvWj3fFD14wvJG7LIZOtLFeBwunc0eMrR_JuVR57wW1MA4D4RQIpqcrtYlLhlMHobE0qZxOLZdIgoVXMjKEJFJZV7lKjMsFldwNyk&gsessionid=pm8wVpp93keRMnwqlqnTTJ-qeRmqVQEUkSfNBG01HmqnwrHlD_G95g)  
  <sub>Yahoo Finance UK, 16 hours ago</sub>  
  Find the latest NVO Jun 2028 42.500 put (NVO280616P00042500) stock quote, history, news and other vital information to help you with your stock trading and...
- [Novo Nordisk (NVO) Stock Price Prediction: Bulls still have work to do after a shallow pullback](https://www.google.com/goto?url=CAESkwEBxCJF16TbdfZM_5cUYgCTnW0qORZ3SJ1qFr0jGOhJlkMjzX9bwKdVZnFVhO0R7FIgihWXIIkGAJb1z3QBnBbKGt0wIWiGkQnJAEsnQwiQQNkIPIKmlbXvatR4FSO6y80jJmF7ncKVAnStvF849izXGdBIFd4rtGhRSH7aArt1XM3fqkpuiPT5rqoV1WOHqOEKDlA&gsessionid=pm8wVpp93keRMnwqlqnTTJ-qeRmqVQEUkSfNBG01HmqnwrHlD_G95g)  
  <sub>Blockchain News, 15 hours ago</sub>  
  Novo Nordisk (NVO) is trading at $40.28 after a 2.21% daily decline, with the session range contained between $41.20 and $39.94. That puts the stock...
- [Novo Nordisk AS (NVO) Stock Down 3.1% -- Now Undervalued? GF Sco](https://www.google.com/goto?url=CAESpAEBxCJF17rQM9EKSv6NGfRxUgCElxhZxu1tToS3BIVfdlyvTmGLuBQX-48Ea5-Q2-sHOyd12j11DZGu5hAPidXYUEHiridanyOPoK2ROedXccR33uY9O9uGFuEKCJsst-mrwac5n6zManL8bqK46i2xtL9H5g2dZa-TUbdDrTS2RYHT2Bd_lA4fEKpiY75MqpZexmnyNxpJhEgSweQ5fRQ5RD3F8Q&gsessionid=pm8wVpp93keRMnwqlqnTTJ-qeRmqVQEUkSfNBG01HmqnwrHlD_G95g)  
  <sub>GuruFocus, 16 hours ago</sub>  
  On November 18, 2026, Novo Nordisk AS (NVO) shares fell 3.1% to a current price of $39.43. This price is significantly down from its 52-week high of $64.16...
- [UnitedHealth Group (UNH) Stock Price Prediction: Pullback tests support as trading momentum cools](https://www.google.com/goto?url=CAESogEBxCJF13TZo6bMzb8Tpjgr49J8Y74xYOToBhiGEGYrw0CpHhUxHLeq7JHB21Nt8sSAId4KktKMAryTx4IbZtMlTPd-tD5iRFDuXGhn0gUj5KVRVnDGn4jTt1Ap483RJxM31pdFgusNutGdFeznlGIFaonxEZUWFW-TBX_nGAbBBdY57xKk5eT20o3LEnvjkluNjunB0qS9V1MLoq8hA0KIZIo&gsessionid=pm8wVpp93keRMnwqlqnTTJ-qeRmqVQEUkSfNBG01HmqnwrHlD_G95g)  
  <sub>Blockchain News, 15 hours ago</sub>  
  UnitedHealth Group (UNH) is trading at $388.56, down 3.31% over the last 24 hours, with price sitting just above the lower Bollinger Band at $387.34. The...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 39.36 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 40.21 (-2.1%), 50d 39.70 (-0.9%), 200d 42.91 (-8.3%); 50d below 200d
Momentum: RSI(14) 44.8 | MACD 0.149 vs signal 0.229 (histogram -0.079)
Returns: 1d -0.2% | 5d -3.2% | 1m +0.8% | 3m -15.8%
52-week range: 35.29 - 63.98 (now 14.2% of the way up)
Volatility: ATR(14) 1.06 (2.7% of price) | annualised 20d 34.8%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 173.47B
Valuation: trailing P/E 9.94 | forward P/E 11.21 | P/B 5.30 | PEG 4.12
Profitability: profit margin 33.9% | operating margin 50.8% | ROE 58.4%
Growth (YoY): revenue +5.6% | earnings -15.8%
Balance sheet: debt/equity 61.7% | free cash flow 32.75B
Risk: beta 0.37 | short interest 1.2% of float
Next earnings: 2027-02-03
```

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

```text
Earnings record, last 4 quarters: 1 beat, 1 in line, 2 missed
  2026-09-30 missed by 22% | 2026-06-30 missed by 6% | 2026-03-31 beat by 23% | 2025-12-31 in line
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

<details><summary><b>What analysts and big funds say</b> — score -0.20</summary>

```text
Consensus: hold (mean 2.85 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 0 strong buy, 2 buy, 10 hold, 1 sell, 0 strong sell
Price target: mean 45.77 (+16.3% vs last close), range 39.47 - 64.13
Recent rating changes:
  - 2026-10-12 BMO Capital: main, Market Perform -> Market Perform
  - 2026-09-11 Morgan Stanley: down, Equal-Weight -> Underweight
  - 2026-03-02 Goldman Sachs: down, Buy -> Neutral
  - 2026-02-24 JP Morgan: down, Overweight -> Neutral
  - 2026-01-09 CICC: init, ? -> Outperform
  - 2025-12-08 Argus Research: down, Buy -> Hold
Institutional ownership: 10.2%
Largest holders: Dodge & Cox Inc. (0.6%), LOOMIS SAYLES & CO L P (0.5%), Arrowstreet Capital, Limited Partnership (0.5%), Two Sigma Investments, LP (0.4%), Franklin Templeton, Inc. (0.4%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 132,277 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Royal Bank of Canada (RY) · Company — BEARISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Short‑term outlook leans down as price has fallen ~3% on the day and sits below key short‑ and medium‑term moving averages, while technical indicators (RSI 33.5, negative MACD, low volume) signal bearish momentum. Analyst consensus remains bullish with a +9.5% price‑target uplift, and fundamentals are solid but not cheap, providing a counterweight. Recent insider purchases are modest but suggest a slight positive tilt. Overall, the negative news and technicals dominate the near‑term view.

**Main reasons it gave:**
- Price down 3% on the day, trading below short‑ and medium‑term moving averages (NEWS)
- RSI 33.5 and MACD negative, indicating bearish momentum (TECHNICALS)
- Analysts have a mean rating of Buy with price target +9.5% upside (ANALYST VIEW)
- Insider purchases of 745 shares on 2026‑10‑30 suggest modest confidence (INSIDER ACTIVITY)
- Solid profitability with 33.9% profit margin and ROE 16.2% (FUNDAMENTALS)

<details><summary><b>News</b> — score -0.50</summary>

- [Royal Bank of Canada stock forecast: Further losses possible as weak momentum persists](https://tradersunion.com/news/stocks/show/4320680-royal-bank-of-canada-drops/)  
  <sub>Traders Union, 41 minutes ago</sub>  
  Royal Bank of Canada (RY) stock is trading at C$272.26, down 3.09% on the day. The price sits below its key short- and medium-term moving averages but...
- [RY: Royal Bank of Canada notes linked to Valero stock, due November 2029](https://quantisnow.com/insight/sec-form-fwp-filed-by-royal-bank-of-canada-6798588)  
  <sub>Quantisnow, 18 hours ago</sub>  
  Royal Bank of Canada is offering structured notes tied to the common stock of Valero Energy, with payments depending on Valero's share price rather than a.
- [Honeywell's data center orders doubled year over year. It cited nearly $19 billion in backlog.](https://www.google.com/goto?url=CAEStQEBxCJF1-H5A2z6JkTTZTYtGCHmgcT6OoKSLOzkl_5c8Ac-gpDhanQY8JamCJ2BausevWYU1muMusPKpIqWryb_ZE8z9GX9j8LAEXmH9ixJuD8E6LhiKYXPOOe4WSXwhXIa8Ph1C3AcRtJU0HoLxSKTGebx5Q6xSywOBB70brBQkLirciA7hguxY4h-sP2MlkhdcvWgGYD5Thtcw89P4rZgrxvno1D-NGprHN-cC95ncRjV2bGn&gsessionid=7nyz9vpXZz6fggctuX466FTAjStEpnbmC8B0ORfHOY4-dct8C1DTQA)  
  <sub>Stock Titan, 11 minutes ago</sub>  
  RBC Capital Markets (RY) concluded its Global Industrials Conference in New York, bringing together executives from more than 90 companies and institutional...
- [Royal Bank of Canada stock falls over 2% as selling momentum dominates after earnings report](https://www.google.com/goto?url=CAESiwEBxCJF1x-NpoxPeJBaPT3XRxMMfwG197W6e1_mo3z_TWGDs1Meq3KNwUUGu1AL3Kf_GgbVlD4E3HjJ9BfUufeLk8jfr4EW0cLJlrdz4hREiypvnUVw5xj7-FraWXkf1ukIT3jCN1gAzzdehDpjYy0NphYOCUKa3zPlbAB2_eBwuKR1Os22cEJTlaTf&gsessionid=7nyz9vpXZz6fggctuX466FTAjStEpnbmC8B0ORfHOY4-dct8C1DTQA)  
  <sub>Traders Union, 22 hours ago</sub>  
  Royal Bank of Canada (RY) slid 2.24% today after reporting quarterly earnings and a recently declared dividend, as selling momentum dominated intraday trade...
- [Why Did Royal Bank of Canada (TSX:RY) Fall 3.107% on November 18, 2026?](https://www.google.com/goto?url=CAESnwEBxCJF136F7DzXG6SHRfiJiDLF1FtBrsrduzlhe8z76_xHm0Wy_ELXZKjiGKvNcUTE3ugqCR_tCo3NbLroNxkH8y_3VDYJ7F_Wvys0mvrFlDE7V8LgWrTdBPkb9tFTx_5BL-TgjHhU-uUuzBSndDbYg9OE0XjfwQMmZuUMwfK_N1AqqFVZWvwZ6MHa9OkoJUGQ0BS3_tRnfjwk-YsipuY&gsessionid=7nyz9vpXZz6fggctuX466FTAjStEpnbmC8B0ORfHOY4-dct8C1DTQA)  
  <sub>kalkine.ca, 4 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Royal Bank of Canada Issues Auto-Callable Contingent Coupon Notes Linked to Bristol-Myers Squibb Stock Maturing in 2029](https://www.google.com/goto?url=CAES5AEBxCJF1z_uSn09Pra9wrHvyx458DE2YQ4YQhPXshL2f56Ez1eGeeI69QQLzEm0Todjkv3eOwLNWYqhRdQTOkLZyATmU4ObKuoCBfC_kzsTATeC_8vYhc-fpNWAse6aHQxeZm1ycXLM9E-WciC1LBcHtYVNGkieu38j9rILZN3kD8H6pXgX7gg3iOKPYMjNUrwvEOnckISLt2FKhUMEn2K0ZxxADH4P-8PHejqvO1s53PwrSQOcitezs6cgQ1tP43fw4CQ8cDwUK-TIayTJZtUzUDkCubgeiJu_jE-gkDYZ2GDLOAI&gsessionid=7nyz9vpXZz6fggctuX466FTAjStEpnbmC8B0ORfHOY4-dct8C1DTQA)  
  <sub>Kalkine Media, 19 hours ago</sub>  
  On November 18, 2026, Royal Bank of Canada filed a free writing prospectus detailing the terms for Auto-Callable Contingent Coupon Barrier Notes tied to...
- [Why TSX:RY and TSX:TD fell on the S&P/TSX Composite: hawkish Fed signals stoked fears of more rate hikes](https://www.google.com/goto?url=CAESwwEBxCJF17PyTWvTDzzHT7KmoNTvbGxtlhqDrVgmTUwyvr0ZPM8DdbZY25b1a0m1vBhOQ2Gw7z-2Va2rR6folZH9gK5EEmr70J98_vz4tMQ9RrTPNmo4bH81Utg65gYNId71y9FOZ6i4aNX5cko8vw7aB1HTt0Xt0YODg1nWkok0fq1FK0aezfcag9XWLshZ5JikN72ETFiyk5aD6YGJHsu14mpGvLfnWvbxzVsWU3WzCH9T3qTk2ngnH0gFEkTGT3xamN4&gsessionid=7nyz9vpXZz6fggctuX466FTAjStEpnbmC8B0ORfHOY4-dct8C1DTQA)  
  <sub>kalkine.ca, 5 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Where Does Royal Bank of Canada (TSX:RY) Sit Among Canadian Financial Stocks?](https://www.google.com/goto?url=CAESswEBxCJF1_S0HgvnwRPB7ILQ2NmY0pDw5osHdN4JAxgQ7KwkEYE61lPZvY6VsTD9W7KWP63Y_TUsPRQLg8DyY8-ms_G0X53SDM8516HS-JZ6bbe-vWXfLJfj3knOTod3RXB6v451n8E0bzunWHe3oDU1U5iuxya1Jn142EL0Y4K4JPAsQ5UOZTU3pbotIh5Zvjjz8yBGS5VNYscWgVW36b34UYWK8x6cgNLtl1PWQk2qUzQGPQ&gsessionid=7nyz9vpXZz6fggctuX466FTAjStEpnbmC8B0ORfHOY4-dct8C1DTQA)  
  <sub>Kalkine Media, 15 hours ago</sub>  
  Royal Bank of Canada (TSX:RY) offers banking, wealth, insurance and capital markets services. See its markets and official sources.
- [Why Is Royal Bank (TSX:RY) Shutting Out AI Agents?](https://www.google.com/goto?url=CAESmAEBxCJF16VEt9Y574O7YDkyF5ECDfJsq6pMjmIGXYgoDZRMFm8K7Ze84ZFzibaiPc9UblSnwt64eLnNQ1dDYRacqzv0EQMiurmZqcsqZLbkjopLrraEmsjAyP6_NZr1OgAM3o3DHEZVjb1XAi1F-Mjs99nBjys1RCNgyy7BDsSubslehPNwn0F6t-YSzURi4Y_bCKVsVvc52w&gsessionid=7nyz9vpXZz6fggctuX466FTAjStEpnbmC8B0ORfHOY4-dct8C1DTQA)  
  <sub>Kalkine Media, 14 hours ago</sub>  
  RBC, TD and CIBC are blocking external AI agents. Here's why it matters for bank stocks and fintech competition.
- [RY: SEC Form FWP filed by Royal Bank Of Canada](https://www.google.com/goto?url=CAESjgEBxCJF11-gY20REiQgObuqR5ZMU_WenZkmWQY6moYC68c1MnGFaNuyxRuqJ5hp8LX0pBHmispuxJfXcQcOGoK6O5ZdnX3T_Hc6-PFS6vUVy1tjBhairxdz_53TWXj6OhR-BVt2NperWfojYiWu7gmQhBgcgRyLOgLlQ-v4-L9B07pVKzEfLUMlrByKORlj&gsessionid=7nyz9vpXZz6fggctuX466FTAjStEpnbmC8B0ORfHOY4-dct8C1DTQA)  
  <sub>Quantisnow, 18 hours ago</sub>  
  Royal Bank of Canada filed a pricing term sheet for a structured note linked to Alphabet Class A common stock (GOOGL), due November 30, 2029.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 190.38 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 201.75 (-5.6%), 50d 199.97 (-4.8%), 200d 191.49 (-0.6%); 50d above 200d
Momentum: RSI(14) 33.5 | MACD -1.586 vs signal 0.014 (histogram -1.600)
Returns: 1d +0.1% | 5d -6.0% | 1m -5.8% | 3m -7.2%
52-week range: 147.35 - 217.87 (now 61.0% of the way up)
Volatility: ATR(14) 3.47 (1.8% of price) | annualised 20d 23.2%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 263.57B
Valuation: trailing P/E 16.64 | forward P/E 14.94 | P/B 2.76 | PEG 1.82
Profitability: profit margin 33.9% | operating margin 45.7% | ROE 16.2%
Growth (YoY): revenue +8.9% | earnings +12.8%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.92 | short interest n/a of float
Next earnings: 2026-12-03
```

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-09-30 in line | 2026-06-30 in line | 2026-03-31 beat by 3% | 2026-03-31 beat by 3%
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
Consensus: buy (mean 2.21 on a 1=strong buy to 5=strong sell scale, 3 analysts)
Ratings: 4 strong buy, 4 buy, 5 hold, 0 sell, 1 strong sell
Price target: mean 208.47 (+9.5% vs last close), range 181.95 - 229.29
Recent rating changes:
  - 2025-08-29 Argus Research: main, Buy -> Buy
  - 2024-12-05 BMO Capital: main, Outperform -> Outperform
  - 2024-08-29 BMO Capital: main, Outperform -> Outperform
  - 2024-06-06 Argus Research: main, Buy -> Buy
  - 2024-04-05 BMO Capital: up, Market Perform -> Outperform
  - 2023-12-18 B of A Securities: up, Neutral -> Buy
Institutional ownership: 49.6%
Largest holders: Royal Bank of Canada (4.8%), Bank of Montreal /CAN/ (4.2%), Vanguard Capital Management LLC (3.1%), TD Asset Management, Inc (1.6%), NORGES BANK (1.4%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 539,927 shares
Distinct insiders: 1 buying, 0 selling
Open-market purchases — insiders spending their own money:
  - 2026-10-30 Royal Bank of Canada (Issuer): 308 shares, 62.87K
  - 2026-10-30 Royal Bank of Canada (Issuer): 177 shares, 36.30K
  - 2026-10-30 Royal Bank of Canada (Issuer): 118 shares, 24.13K
  - 2026-10-30 Royal Bank of Canada (Issuer): 142 shares, 29.14K
(93 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

_Not available today._

</details>

### Teva Pharmaceutical (TEVA) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Barclays raised TEVA price target to $50 (Overweight) – bullish analyst signal
- Consensus rating is strong buy (mean 1.53) with 13 buy/strong buy analysts
- Earnings record: 3 beats, 1 miss in last 4 quarters – positive earnings momentum
- Technicals: price below 20‑day SMA, low volume (0.08× 20‑day avg) – short‑term weakness

<details><summary><b>News</b> — score +0.20</summary>

- [Teva Pharmaceutical Industries Ltd. Announces Departure of R&D Chief Medical Officer Dr. Eric Hughes](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0b30f49147af8687f7b5bbd9973a&url=https%3a%2f%2fwww.quiverquant.com%2fnews%2fTeva%2bPharmaceutical%2bIndustries%2bLtd.%2bAnnounces%2bDeparture%2bof%2bR%2526D%2bChief%2bMedical%2bOfficer%2bDr.%2bEric%2bHughes&c=15308230525987055960&mkt=en-us)  
  <sub>quiverquant, 25h ago</sub>  
  Effective immediately, David Gardiner, MD, Head of Innovative Medicines & Clinical Development, will serve as transition lead for R&D, reporting directly to Teva's President and Chief Executive ...
- [Teva Announces R&D Leadership Transition As Chief Medical Officer Departs](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0b30f49147af8687f7b5bbd9973a&url=https%3a%2f%2fwww.rttnews.com%2f3716114%2fteva-announces-r-d-leadership-transition-as-chief-medical-officer-departs.aspx&c=498800485894460632&mkt=en-us)  
  <sub>RTTNews, 18h ago</sub>  
  Effective immediately, Dr. David Gardiner, Head of Innovative Medicines & Clinical Development, will serve as interim R&D transition lead and report directly to CEO Richard Francis.
- [Teva Pharma (TEVA) PT Raised to $50 at Barclays](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0b30f49147af8687f7b5bbd9973a&url=https%3a%2f%2fwww.streetinsider.com%2fAnalyst%2bPT%2bChange%2fTeva%2bPharma%2b%2528TEVA%2529%2bPT%2bRaised%2bto%2b%252450%2bat%2bBarclays%2f27371936.html&c=14042360528168413989&mkt=en-us)  
  <sub>StreetInsider.com, 15h ago</sub>  
  Barclays analyst Glen Santangelo raised the price target on Teva Pharma (NYSE: TEVA) to $50.00 (from $47.00) while maintaining a Overweight rating.
- [Teva Announces R&D Leadership Transition; Eric Hughes to Depart the Company](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0b30f49147af8687f7b5bbd9973a&url=https%3a%2f%2ffinance.yahoo.com%2fhealthcare%2farticles%2fteva-announces-r-d-leadership-220000635.html&c=5705152886124369890&mkt=en-us)  
  <sub>Yahoo Finance, 25h ago</sub>  
  Teva's Pivot to Growth Strategy, R&D priorities, and expectations remain unchanged; Company initiates search for successorTEL AVIV, Israel and PARSIPPANY, N.J., Nov. 18, 2026 (GLOBE NEWSWIRE) -- .
- [Teva Pharmaceutical Industries Limited (TEVA)](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0b30f49147af8687f7b5bbd9973a&url=https%3a%2f%2ffinance.yahoo.com%2fquote%2fTEVA%2fearnings-calls%2f&c=2646209257417279590&mkt=en-us)  
  <sub>Yahoo Finance, 26h ago</sub>  
  This price reflects trading activity during the overnight session on the Blue Ocean ATS, available 8 PM to 4 AM ET, Sunday through Thursday, when regular markets are closed. The above button links to ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 40.84 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 41.86 (-2.4%), 50d 40.62 (+0.5%), 200d 35.24 (+15.9%); 50d above 200d
Momentum: RSI(14) 45.5 | MACD 0.587 vs signal 0.773 (histogram -0.186)
Returns: 1d -3.3% | 5d -6.4% | 1m +0.5% | 3m +9.4%
52-week range: 24.21 - 44.50 (now 82.0% of the way up)
Volatility: ATR(14) 1.27 (3.1% of price) | annualised 20d 34.5%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.40</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 47.65B
Valuation: trailing P/E 94.98 | forward P/E 13.04 | P/B 5.97 | PEG 0.71
Profitability: profit margin 2.9% | operating margin 19.8% | ROE 6.7%
Growth (YoY): revenue -1.9% | earnings -46.0%
Balance sheet: debt/equity 212.9% | free cash flow 1.49B
Risk: beta 0.84 | short interest 2.4% of float
Next earnings: 2027-01-27
```

</details>

<details><summary><b>What this fund holds</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.40</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-09-30 beat by 15% | 2026-06-30 missed by 92% | 2026-03-31 beat by 9% | 2025-12-31 beat by 39%
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

```text
Consensus: buy (mean 1.53 on a 1=strong buy to 5=strong sell scale, 14 analysts)
Ratings: 4 strong buy, 9 buy, 2 hold, 0 sell, 0 strong sell
Price target: mean 50.51 (+23.7% vs last close), range 42.12 - 57.00
Recent rating changes:
  - 2026-11-12 Piper Sandler: main, Overweight -> Overweight
  - 2026-11-05 Leerink Partners: main, Outperform -> Outperform
  - 2026-11-04 TD Cowen: main, Buy -> Buy
  - 2026-11-04 HC Wainwright & Co.: main, Buy -> Buy
  - 2026-11-02 HC Wainwright & Co.: init, ? -> Buy
  - 2026-10-15 Barclays: main, Overweight -> Overweight
Institutional ownership: 69.4%
Largest holders: Blackrock Inc. (5.4%), Phoenix Financial Ltd. (3.6%), WCM Investment Management, LLC (3.6%), Clal Insurance Enterprises Holdings Ltd (3.6%), Migdal Insurance & Financial Holdings Ltd. (3.4%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 43,476 shares in 3 transaction(s) | sold 29,021 shares in 4
Net: +14,455 shares (+0.3% of insider holdings) | insiders hold 5,647,441 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-11-12 SABAG MARK (Officer): 44,710 shares, 1.97M
  - 2026-11-11 DANIELL RICHARD (Officer): 45,003 shares, 1.93M
  - 2026-11-10 FRANCIS RICHARD D (Chief Executive Officer): 250,000 shares, 10.56M
  - 2026-11-09 WEISS AMIR (Officer): 17,289 shares, 744.05K
(16 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Elbit Systems (ESLT) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Elbit sees domestic growth opportunity as U.S. aid to Israel faces doubts](https://seekingalpha.com/news/4674330-elbit-sees-domestic-growth-opportunity-as-u-s-aid-to-israel-faces-doubts)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Elbit Systems (ESLT) Chief Executive Bezalel Machlis expects reduced U.S. military aid to Israel to encourage local weapons production and create export...
- [New Analyst Forecast: $ESLT Given $900 Price Target](https://www.quiverquant.com/news/New+Analyst+Forecast%3A+%24ESLT+Given+%24900+Price+Target)  
  <sub>Quiver Quantitative, 22 hours ago</sub>  
  We just received data on a new analyst forecast for $ESLT. Seth Seifman from JP Morgan set a price t.
- [Implied Volatility Surging for ESCO Technologies Stock Options](https://www.google.com/goto?url=CAESqgEBxCJF19wymh8RHOaV7mo2NDDtzhpuOhuKc3eHJFpXgE9a4-dk-6-Zvq_HiyKyoDmjYLqBDtfgRyZk7a26pFKoG8a93oJgtUXogV94u4W-IBE3rmfyqk8RApwfNX9AWWDTGVfxd4VSQUODejjI2lRs6e0gIGGt88BexZvBZew8EuS7Ftl6moPh0Tg75RxknuLul1tEhBAPfH9vq0pL3XW68neS1i_IgR_r-A&gsessionid=GquE2SHKgMJUi3mi9x64dfeFJtnIcXQohV6d5aq1ig_zCuqpnTft4g)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Investors need to pay close attention to ESE stock based on the movements in the options market lately.
- [Company News for Nov 18, 2026](https://www.google.com/goto?url=CAESgQEBxCJF191UmcD7rr1R0RDkSIWwbMQl9IVUkLD3VHhVpRJkXOdCeH4ARUGEN7G1Y2rI9XzQA7SpuXlhyjoaJocmZqcvrpR_cCxz55kvEfjIZpNorEuLvQHloK_ZGHskZElzTKsA5fwOcGjjptEstaxM3yVP5zE3eNttoyW_1ftS8yw&gsessionid=GquE2SHKgMJUi3mi9x64dfeFJtnIcXQohV6d5aq1ig_zCuqpnTft4g)  
  <sub>Zacks Investment Research, 23 hours ago</sub>  
  ESLT - Free Report) ) jumped 5.9% after the company reported third-quarter 2026 earnings of $4.36 per share, beating the Zacks Consensus Estimate of $3.97...
- [Elbit Systems (NASDAQ:ESLT) Given New $900.00 Price Target at JPMorgan Chase & Co.](https://www.google.com/goto?url=CAESxgEBxCJF1wE3QvPB2m4O7afkEF6B9NSajGphL18gaOdQzbn1rb_9rt7d1-r0c6IQ5Ovhh7jUxIyiallSkZ6DXu-rNA42kb5zEyQIpKY4FAv4DeydoJUzQ4ggSnXyMRU5YPf0mVBTfZ6qznsUSlFyjnpEoZ15MNuYdS4XjRaW1ea9nkcmfWUv2WfIhr3Y4FT2kAq71dfkx71NCl1S_SZBO4uiGoRTs-8LiJl4o5FVcOph4PIrHaJn_cPqT6_g8vgTbHPIeFqv7BU&gsessionid=GquE2SHKgMJUi3mi9x64dfeFJtnIcXQohV6d5aq1ig_zCuqpnTft4g)  
  <sub>MarketBeat, 22 hours ago</sub>  
  JPMorgan Chase & Co. upped their price target on Elbit Systems from $885.00 to $900.00 and gave the stock a "neutral" rating in a report on Wednesday.
- [ESLT Maintained by JP Morgan -- Price Target Raised to $900](https://www.google.com/goto?url=CAESmgEBxCJF10DnO6WScNnZE3GOJ42_FVCT68brgL-gwVvwbVsI8ULTtgkGyqJsHc4iJsl0UvlafsNc-FV0ODDnluSfEADewU6dDDWhxZNtsxc7VuxzZ9-K5BCkjtRIoVtVfhN9o1W5V9BQnUPxk2pRN0b3z8iJVJNXb0aHvp7vqi3OO9uStIW-wfzStuTCyIRAeRv2-Atd7mhN4v9m&gsessionid=GquE2SHKgMJUi3mi9x64dfeFJtnIcXQohV6d5aq1ig_zCuqpnTft4g)  
  <sub>GuruFocus, 22 hours ago</sub>  
  On October 03, 2023, JP Morgan maintained a 'Neutral' rating on Elbit Systems (ESLT) while raising the price target from $885.00 to $900.00, a rise of 1.69%...
- [Elbit Systems stock: Record backlog anchors 2027 outlook](https://www.google.com/goto?url=CAESsgEBxCJF1zCHJdwVSkI5nK1bDaelMONnE-IDw8GoWiRPLtw5BNYgA30pr_6Vx_tF_j1Ge7rEJ9dIIFPswnp3M8it9Ih5sNuU61ZczY0lVwujFN9U3a3P309oXmgvqJLuvKG-FoILUXM5RDMHm_9bwhWsvOTRWhY7xgYKNfbMLzfYBzfexx_wzqTM_JuGYBdkJxJDxSLU_yhtJOLZty8q1ju2Hxjw3a_KP-VMQoQip4S6ZsIk&gsessionid=GquE2SHKgMJUi3mi9x64dfeFJtnIcXQohV6d5aq1ig_zCuqpnTft4g)  
  <sub>ad-hoc-news.de, 22 hours ago</sub>  
  Elbit Systems stock follows record third-quarter growth with a stronger outlook for 2027. Management is expanding capacity to support backlog execution.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 696.59 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 730.98 (-4.7%), 50d 722.57 (-3.6%), 200d 785.30 (-11.3%); 50d below 200d
Momentum: RSI(14) 45.6 | MACD -8.095 vs signal -4.098 (histogram -3.996)
Returns: 1d -0.3% | 5d -3.7% | 1m -6.2% | 3m -6.0%
52-week range: 454.95 - 1,014.33 (now 43.2% of the way up)
Volatility: ATR(14) 28.34 (4.1% of price) | annualised 20d 65.4%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 32.66B
Valuation: trailing P/E 49.09 | forward P/E 34.90 | P/B 7.14 | PEG n/a
Profitability: profit margin 7.7% | operating margin 9.7% | ROE 15.8%
Growth (YoY): revenue +17.2% | earnings +32.1%
Balance sheet: debt/equity 22.6% | free cash flow 362.77M
Risk: beta -0.40 | short interest 0.8% of float
Next earnings: 2026-11-17
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-09-30 beat by 9% | 2026-06-30 beat by 10% | 2026-03-31 beat by 16% | 2025-12-31 beat by 16%
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
Consensus: hold (mean 2.67 on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 841.50 (+20.8% vs last close), range 739.00 - 960.00
Recent rating changes:
  - 2026-10-05 Jefferies: main, Hold -> Hold
  - 2026-08-19 JP Morgan: main, Neutral -> Neutral
  - 2026-06-24 Jefferies: main, Hold -> Hold
  - 2026-05-27 Jefferies: main, Hold -> Hold
  - 2026-05-27 JP Morgan: main, Neutral -> Neutral
  - 2026-04-13 JP Morgan: main, Neutral -> Neutral
Institutional ownership: 26.6%
Largest holders: Clal Insurance Enterprises Holdings Ltd (3.5%), Vanguard Capital Management LLC (1.6%), Van Eck Associates Corporation (1.2%), Y.D. More Investments Ltd (1.1%), Altshuler Shaham Ltd (1.1%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 19,309,244 shares
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

- [Alphabet stock is falling. Here’s why investors should be buying the dip.](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0ab8b67d48efa5c0d07fe8e7dd53&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2fgeneral%2falphabet-stock-is-falling-here-s-why-investors-should-be-buying-the-dip%2far-AA2hII7p&c=5690830646371254519&mkt=en-us)  
  <sub>Barchart on MSN, 27h ago</sub>  
  Alphabet (GOOG) (GOOGL) stock has taken a hit, falling nearly 17% over the past month and trading more than 30% below the 52-week high. The decline followed the tech giant’s third-quarter results, ...
- [Alphabet stock rises 4% as Anthropic IPO boosts investor optimism](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0ab8b67d48efa5c0d07fe8e7dd53&url=https%3a%2f%2finvezz.com%2fnews%2f2026%2f11%2f19%2falphabet-stock-rises-4-as-anthropic-ipo-boosts-investor-optimism%2f&c=17362430521384504884&mkt=en-us)  
  <sub>Invezz, 14h ago</sub>  
  Alphabet shares climbed nearly 4% in premarket trading as Anthropic's IPO boosted the value of its stake and renewed interest in its AI business.
- [Google Urged By Top Investor to Give Away AI Models as Anthropic Prepares for IPO](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0ab8b67d48efa5c0d07fe8e7dd53&url=https%3a%2f%2fwww.tipranks.com%2fnews%2fgoogle-urged-by-top-investor-to-give-away-ai-models-as-anthropic-prepares-for-ipo&c=6233590080981054211&mkt=en-us)  
  <sub>TipRanks, 31h ago</sub>  
  Tech giant Google ($GOOGL) should make more of its artificial intelligence models available for free to prevent Anthropic ($ANT) and OpenAI from gaining too much ...
- [Is Alphabet Stock a Buy Right Now?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0ab8b67d48efa5c0d07fe8e7dd53&url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fis-alphabet-stock-a-buy-right-now%2far-AA2hK17w&c=14003939811772309236&mkt=en-us)  
  <sub>The Motley Fool on MSN, 22h ago</sub>  
  The stock's upside far outweighs its potential downside.
- [Alphabet (GOOGL) Stock Rises 4% as Anthropic IPO Values Google’s Stake at $149B](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0ab8b67d48efa5c0d07fe8e7dd53&url=https%3a%2f%2fblockonomi.com%2falphabet-googl-stock-rises-4-as-anthropic-ipo-values-googles-stake-at-149b%2f&c=15225306025282815967&mkt=en-us)  
  <sub>Blockonomi, 9h ago</sub>  
  Alphabet (GOOGL) stock rose 4% premarket as Anthropic’s IPO valued Google’s stake at $149B. See the key numbers, analyst targets and what’s next.
- [The 5 Best Stocks in Berkshire Hathaway’s Portfolio](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0ab8b67d48efa5c0d07fe8e7dd53&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2f5-best-stocks-berkshire-hathaway-153437382.html&c=3285366110906576736&mkt=en-us)  
  <sub>Yahoo Finance, 31h ago</sub>  
  Key TakeawaysBerkshire Hathaway’s latest 13F shows that, among its positions of 2% or more, analysts see the most upside in Alphabet, Bank of America, Occidental Petroleum and American Express.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 291.22 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 293.12 (-0.6%), 50d 324.14 (-10.2%), 200d 337.40 (-13.7%); 50d below 200d
Momentum: RSI(14) 42.3 | MACD -11.283 vs signal -12.632 (histogram 1.349)
Returns: 1d +3.1% | 5d -2.5% | 1m -13.0% | 3m -15.5%
52-week range: 273.50 - 402.62 (now 13.7% of the way up)
Volatility: ATR(14) 10.01 (3.4% of price) | annualised 20d 53.7%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 3.58T
Valuation: trailing P/E 15.21 | forward P/E 19.04 | P/B 5.43 | PEG 1.00
Profitability: profit margin 50.0% | operating margin 33.3% | ROE 44.3%
Growth (YoY): revenue +24.7% | earnings -25.3%
Balance sheet: debt/equity 22.2% | free cash flow -1.16B
Risk: beta 1.23 | short interest 1.5% of float
Next earnings: 2026-10-28
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 1 beat, 3 missed
  2026-09-30 missed by 14% | 2026-06-30 missed by 4% | 2026-03-31 missed by 3% | 2025-12-31 beat by 4%
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
Ratings: 10 strong buy, 43 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 400.15 (+37.4% vs last close), range 300.00 - 500.00
Recent rating changes:
  - 2026-11-02 Wells Fargo: main, Overweight -> Overweight
  - 2026-10-30 Citigroup: main, Buy -> Buy
  - 2026-10-30 Wells Fargo: main, Overweight -> Overweight
  - 2026-10-29 Bernstein: main, Market Perform -> Market Perform
  - 2026-10-29 RBC Capital: main, Outperform -> Outperform
  - 2026-10-29 UBS: main, Neutral -> Neutral
Institutional ownership: 80.8%
Largest holders: Blackrock Inc. (7.8%), Vanguard Capital Management LLC (6.5%), FMR, LLC (4.2%), State Street Corporation (4.1%), Geode Capital Management, LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 202,850,992 shares
Distinct insiders: 0 buying, 0 selling
(3 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

- [Earnings Calendar for:](https://finance.yahoo.com/calendar/earnings?from=2026-12-29&to=2027-01-27&day=2027-01-16)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Find earnings, economic, stock splits and IPO calendars to track upcoming financial events from Yahoo Finance.
- [Fairfax exits IIFL Finance, sells stake for Rs 3,454 crore](https://m.economictimes.com/markets/stocks/news/fairfax-exits-iifl-finance-sells-stake-for-rs-3454-crore/articleshow/135975290.cms)  
  <sub>The Economic Times, 13 hours ago</sub>  
  Fairfax Financial Holdings divested its 13.25% stake in IIFL Finance for ₹3454 crore through a block deal. This significant transaction involved the sale...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 26.47 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 24.26 (+9.1%), 50d 23.36 (+13.3%), 200d 25.30 (+4.6%); 50d below 200d
Momentum: RSI(14) 73.9 | MACD 0.990 vs signal 0.788 (histogram 0.202)
Returns: 1d +1.0% | 5d +3.0% | 1m +16.8% | 3m +12.2%
52-week range: 21.36 - 36.88 (now 32.9% of the way up)
Volatility: ATR(14) 0.57 (2.1% of price) | annualised 20d 27.4%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 136.18B
Valuation: trailing P/E 17.08 | forward P/E 19.11 | P/B 10.54 | PEG n/a
Profitability: profit margin 26.5% | operating margin 36.6% | ROE 11.0%
Growth (YoY): revenue +80.8% | earnings +21.3%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.39 | short interest 0.8% of float
Next earnings: 2027-01-16
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 1 beat, 2 in line, 1 missed
  2026-09-30 missed by 2% | 2026-06-30 in line | 2026-03-31 in line | 2025-12-31 beat by 61%
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
Price target: mean 30.30 (+14.5% vs last close), range 26.20 - 33.00
Recent rating changes:
  - 2024-07-22 JP Morgan: down, Overweight -> Neutral
  - 2019-09-09 Bernstein: down, Outperform -> Market Perform
  - 2019-06-11 Nomura: down, Buy -> Neutral
  - 2017-03-21 Morgan Stanley: down, Overweight -> Equal-Weight
  - 2016-09-14 Goldman Sachs: main, ? -> Buy
  - 2015-03-11 Societe Generale: init, ? -> Buy
Institutional ownership: 14.2%
Largest holders: Morgan Stanley (1.1%), Royal Bank of Canada (0.8%), JPMORGAN CHASE & CO (0.7%), Temasek Holdings (Private) Ltd (0.4%), Invesco Ltd. (0.4%)
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

- [A property insurer puts $250 million into J.P. Morgan's new global stock fund](https://www.stocktitan.net/news/JPM/j-p-morgan-asset-management-launches-jp-morgan-all-country-research-fvvbyk5nhoxo.html)  
  <sub>Stock Titan, 12 minutes ago</sub>  
  J.P. Morgan Asset Management (JPM) launched the JPMorgan All Country Research Enhanced Equity ETF on NYSE Arca. The fund trades under the symbol JALL and...
- [JPM Nov 2026 347.500 call (JPM261120C00347500) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/JPM261120C00347500/)  
  <sub>Yahoo Finance UK, 9 hours ago</sub>  
  Find the latest JPM Nov 2026 347.500 call (JPM261120C00347500) stock quote, history, news and other vital information to help you with your stock trading...
- [JPMorgan Chase & Co. $JPM Stock: Danske Bank A S Cuts Holdings](https://www.google.com/goto?url=CAESswEBxCJF1899BiUU3WaE1q1aBekg-9PYYPG2zyFRShnGVHASQ8YtqYIJrS4RmTTWozwVTaSXHcPzdg_pPmVvYrySa4djGdeTiJrkO4vlm-e75t5MGfvv9vdTkLoxmbYdZZ9KcU3DwLzVtbZUhcJSCLzgeFcJ1iAOERGoVkG48-kBhQuNNUueROYN2iUdUKL7RUlE-9kgZyEONiICt6PSv2MiGbaUf6yH87y9ZJWZzqFR92TZ-A&gsessionid=OxRVum9W3q_EffmM089HmFbrhrkxdYLTMjSn8SmYPqzIAbmIsvs5bQ)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Danske Bank A S lessened its stake in shares of JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 3.2% during the 3rd quarter, according to the company in...
- [Why Is JPMorgan Chase (JPM) Naming Bregje De Best As Its Next CFO?](https://www.google.com/goto?url=CAESuwEBxCJF17f8UbO3HwwjK_jqmqGnDXgbzvTwc_x4gKgwlMY41gh9ysg66HLJwDRhsPjWBldvZNfUhtduFZ5OEIjnbYAHqrMy-jtchqdzjN9Fx4KzKfmDCQqIGzFFcXWZ1Kyq4yIiURYHRu2bBaGadMoQ34R8lFXSNW5xNQKUZHWMnY176vREvcaIeSUU6W5M9LtKRl_lnxmwyWAikq03muEt69M4e4t6P8oyZxoI_Zua6Pv5UdMHM7LX3QUm&gsessionid=OxRVum9W3q_EffmM089HmFbrhrkxdYLTMjSn8SmYPqzIAbmIsvs5bQ)  
  <sub>Simply Wall St, 8 hours ago</sub>  
  JPMorgan Chase (NYSE:JPM) said Bregje de Best will succeed Jeremy Barnum as Chief Financial Officer after the first quarter of 2027.
- [JPMorgan Stocks Fall 2.44% on Day It Names Bregje de Best Next CFO](https://www.google.com/goto?url=CAESugEBxCJF1xfh0-aiMPOCQoUk1D0F0kKZki6aDQxG79Dz4jlk0MfW0Dfm-r54hYH9EWtd3VHP_j_qG_jDmBVfyGFXXrvM5XI6I1spEQgGCmDHCGHGGXhATjY1bHRdRNjKu0ezafOmH_QHb7ELGn-O-Sako_JbqV1kM3MxG_KG7pdZElzicaQ7qWgdb_yi5zA6nZ5jWLrIlv2uTZhV0N-X9M-ZhsU12hEnF9gM0VLJZUpbuZL9t9B5dne8vnQ&gsessionid=OxRVum9W3q_EffmM089HmFbrhrkxdYLTMjSn8SmYPqzIAbmIsvs5bQ)  
  <sub>TradingView, 19 hours ago</sub>  
  JPMorgan Chase NYSE:JPM named Bregje de Best as its next chief financial officer on November 17, and shares fell 2.44% to $329.96 at the 4:00 p.m. ET close...
- [JPMorgan Chase & Co. (JPM) Sees a More Significant Dip Than Broader Market: Some Facts to Know](https://www.google.com/goto?url=CAESiAEBxCJF14X_3s4aSTf3FNV6_S8So_pLMdZNhfqbKaNDAbwqQbGaEPUGf1F6vYEBUhp1NikdwSSImyx0DUG2dkal5KQtm-tLJ2gofNkfUL0YAKUqr1JmFE7-N4prjxLAiGVi1VUj8TIRYCCW8p5iz2uSsM5MAvBLDLcteJuMcRgyJjBpFvOJAql_&gsessionid=OxRVum9W3q_EffmM089HmFbrhrkxdYLTMjSn8SmYPqzIAbmIsvs5bQ)  
  <sub>Yahoo Finance UK, 17 hours ago</sub>  
  In the latest trading session, JPMorgan Chase & Co. (JPM) closed at $324.11, marking a -1.77% move from the previous day.
- [Trading the Move, Not the Narrative: (JPM) Edition](https://www.google.com/goto?url=CAESvgEBxCJF13KiYsB1Ixqzoynd6YGV3hQs6dy1OJhd7Vs9ycuY9goN5rh_kg5RALIl_gFQCmO8zpImogAZmfJuuNYryQsCKkPUgCsD4klcSHzET3SC6xoCS-lUBGMVX2gy5LSAyCVJ0VLSUntau9HxTfw6Rk55wRrksClTBFw0HBsVtNjKEVjOHNGTnm4fh08cPrVF_O5gYP2ITTHaujijl_Z_w_Xegrxs1sY6TpS9q0wAOQj0bpxalb4mnRk8W_pW&gsessionid=OxRVum9W3q_EffmM089HmFbrhrkxdYLTMjSn8SmYPqzIAbmIsvs5bQ)  
  <sub>Stock Traders Daily, 21 hours ago</sub>  
  Price-action only: Jpmorgan Chase & Co. (JPM) movements set the tone for institutional models. Trading the Move, Not the Narrative: (JPM) Edition.
- [JPMorgan Chase & Co. $JPM Stock Purchased by Bessemer Group Inc.](https://www.google.com/goto?url=CAEStQEBxCJF12c27IbyaOwTFqMJjoFJjEDTICOOWsW290F7QkUxMyl42Lv9pqqRWcfspEh3wOxv5svH_1Cp-zNqXu-MujtZhvPOYLpSXLloPEgI1iZygbf_0uCgd-XFUzHvq56FXxa_mZk4dPJd36MyFR4VVZkEVIxxJmLXmmVTY7veAOOYptJ-Ry4_610719TLV3g3n56Zv2KNHGaSnG4bb-9zoylLbsH7iDgfuenguzrSOTKrO5C1&gsessionid=OxRVum9W3q_EffmM089HmFbrhrkxdYLTMjSn8SmYPqzIAbmIsvs5bQ)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Bessemer Group Inc. increased its position in JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 4.9% in the 3rd quarter, according to the company in its most...
- [JPM Nov 2026 365.000 call (JPM261120C00365000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXei5PnbC7rfu5f7Iy9v_LH30h0pwmTqnyPAanUCocvCnxKoD8cFnEAC0xTQUclVgmkfitFrSTjr2HQp7_sI3pr9UIotoQ8jMDN9Q0doeawVqql-l2KPi80FClIrzerkSDnrA44SlFVyhboEiCNdA&gsessionid=OxRVum9W3q_EffmM089HmFbrhrkxdYLTMjSn8SmYPqzIAbmIsvs5bQ)  
  <sub>Yahoo Finance Australia, 9 hours ago</sub>  
  Find the latest JPM Nov 2026 365.000 call (JPM261120C00365000) stock quote, history, news and other vital information to help you with your stock trading...
- [REG - JPMorganUS Small Cos - Dividend Declaration](https://www.google.com/goto?url=CAEStgEBxCJF1wh6ipaNiRT1qG6_XEMpFlVTSex-po0KcYJEHloEJCeGrbiRsmpgDGHeOw6UeWLiN79CRacTIHz7GF9xQbT1LA2jy8QbM_5WM_jR2oZBfdMiR8cipruB5-0OC3qAynnidHNnuKbKTwoyNWlKYWcfFYeKxQTU-7Lt2BEBiJERvIsPQsiZApHd5H9xPxql-qSyjAYPvPRNAbZJniG3lrwI9vGLI9MXKrbGxoRUaI2OUNQaCA&gsessionid=OxRVum9W3q_EffmM089HmFbrhrkxdYLTMjSn8SmYPqzIAbmIsvs5bQ)  
  <sub>TradingView, 23 hours ago</sub>  
  RNS Number : 7365D JPMorgan US Smaller Co. IT 18 November 2026 LONDON STOCK EXCHANGE ANNOUNCEMENTJPMORGAN US SMALLER COMPANIES INVESTMENT TRUST PLC DIVIDEND...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 326.50 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 337.96 (-3.4%), 50d 338.39 (-3.5%), 200d 325.22 (+0.4%); 50d above 200d
Momentum: RSI(14) 40.5 | MACD -1.900 vs signal -0.269 (histogram -1.631)
Returns: 1d +0.7% | 5d -4.8% | 1m -2.6% | 3m -7.1%
52-week range: 282.84 - 365.18 (now 53.0% of the way up)
Volatility: ATR(14) 7.09 (2.2% of price) | annualised 20d 30.0%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 867.06B
Valuation: trailing P/E 13.70 | forward P/E 12.77 | P/B 2.47 | PEG 1.38
Profitability: profit margin 34.6% | operating margin 44.8% | ROE 18.0%
Growth (YoY): revenue +10.2% | earnings +9.9%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 1.02 | short interest 0.9% of float
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
Price target: mean 373.48 (+14.4% vs last close), range 312.00 - 425.00
Recent rating changes:
  - 2026-11-02 UBS: main, Buy -> Buy
  - 2026-10-15 Citigroup: main, Neutral -> Neutral
  - 2026-10-14 Truist Securities: main, Hold -> Hold
  - 2026-10-14 Barclays: main, Overweight -> Overweight
  - 2026-10-14 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-14 Morgan Stanley: main, Equal-Weight -> Equal-Weight
Institutional ownership: 75.5%
Largest holders: Blackrock Inc. (7.7%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.7%), Vanguard Portfolio Management LLC (2.7%), Morgan Stanley (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 1,583 shares in 6 transaction(s) | sold 15,935 shares in 4
Net: -14,352 shares (-0.1% of insider holdings) | insiders hold 11,180,116 shares
Distinct insiders: 0 buying, 2 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-10 LEOPOLD ROBIN (Officer): 2,500 shares, 882.03K
  - 2026-08-11 LEOPOLD ROBIN (Officer): 2,500 shares, 903.52K
  - 2026-06-22 FRIEDMAN STACEY R. (General Counsel): 5,467 shares, 1.81M
(6 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

- [Eli Lilly Stopped Touting Dose Counts. Should You Worry?](https://www.trefis.com/stock/lly/articles/626833/eli-lilly-stopped-touting-dose-counts-should-you-worry/2026-11-19)  
  <sub>Trefis, 4 hours ago</sub>  
  Today's big story: Could Anthropic Stock Fall 25%?Eli Lilly (LLY) stock trades at 44.7 times earnings, against 21.5 for the S&P 500.
- [Eli Lilly: Everyone Losing Weight, But Lilly Keeps Gaining (Initiating With A Buy) (LLY)](https://seekingalpha.com/article/4969989-eli-lilly-everyone-losing-weight-but-lilly-keeps-gaining-initiating-with-a-buy)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  Eli Lilly and Company (LLY) stock earns a buy rating at a $1600 target as volume growth outweighs pricing pressure and the pipeline advances.
- [LLY Dec 2027 2000.000 call (LLY271217C02000000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXo_1y7VLFGeSnniRACsObZjhcFpMjb6eH-WFSIyrD0Pf1WaUjr1J_VPv9bOrEZ97_YkGW_5oWQy8q5mTn77oGsAJjoWcRST3zG73yeJEFkKBcDuSQzFoUO7Fk7S72Gw_GFCS6_3W6JBxMCwUxXnI&gsessionid=OomQiHY1UBZ2pxROnvXJLGDXkqTwaINUFhZy2-eI99plpGwezQmyNg)  
  <sub>Yahoo Finance UK, 11 hours ago</sub>  
  Find the latest LLY Dec 2027 2000.000 call (LLY271217C02000000) stock quote, history, news and other vital information to help you with your stock trading...
- [What Eli Lilly Buyers Were Betting On](https://www.google.com/goto?url=CAESsgEBxCJF14EkXtmcGF3BbjWS4g3kr9Mtke94VRwjX59rpEQmz_zDeM4adGxStUfMiz3DY2Ge9-XHzquU_NwSUddLgV_W_b1SeWuyN8pFZkuK57seEheSjSsHwNJn0RaJ2t-5-8KDGutLBjayw_zjkKxFbFssNFmQjolTRS_FJaowsKT7N7_MjHqEF-kcm9sbVE9IfdKcpB5BXYge7_c1X51NddkdTKwBnkHdBtq-Y0TQnN2A&gsessionid=OomQiHY1UBZ2pxROnvXJLGDXkqTwaINUFhZy2-eI99plpGwezQmyNg)  
  <sub>Simply Wall St, 15 hours ago</sub>  
  If you only glanced at Eli Lilly's headlines this year, the focus was on soaring GLP-1 revenues, fresh acquisitions across vaccines, oncology,...
- [Liquidity Mapping Around (LLY) Price Events](https://www.google.com/goto?url=CAEStgEBxCJF13UxT4wyruZ5AR4aSPK1C_2tJ_96xAPvIswxrW5fw6iEfpajmleop3AK-cIkIVOqwD3nZrW-yg0olneUamTmwJDXivDRlODnyK9YPFC3jaJ3asuUBAjZ4hZl1EYwCndtdLQt9Lwz-EekhzURdwt3LrR8OyuVKk2NYeqhx-NQRlXkA_aoUP_iH8PXv6txJXp0UKlXdF3vNOfdHTAM03ck51xQXdqhN5ztolqzu9AvfY2onQ&gsessionid=OomQiHY1UBZ2pxROnvXJLGDXkqTwaINUFhZy2-eI99plpGwezQmyNg)  
  <sub>Stock Traders Daily, 21 hours ago</sub>  
  Key findings for Eli Lilly And Company (NYSE: LLY). Weak Near-Term Sentiment Could Precede Shifts in Mid and Long-Term Outlook; Resistance is being tested.
- [LLY (NYSE:LLY) Mounjaro and Zepbound Momentum Powers Another Raise to Revenue Goals](https://www.google.com/goto?url=CAESuwEBxCJF10CbM4f-ORxUJ-leO_cSLdEt8TGPZXAt89aYeUPv5SoAN6tAHPsSpuD_RObnZwUFg9MEP0-TE7473JXymEa4S09XkV1MK_BW1nq8AesgeVlk6dCwl-Y5J3GWAoUXCvidLM1SQyLT5pVP50KpNPOOIDZkDMRF1ASURT0x-dSxza4n86rLJ3zNdXga5fhi70t-Vc_X3CjLCK5VVE8DrwY1-BVmpk8T-3YujTPvj_XsCAv_of9VZssL&gsessionid=OomQiHY1UBZ2pxROnvXJLGDXkqTwaINUFhZy2-eI99plpGwezQmyNg)  
  <sub>Kalkine Media, 4 hours ago</sub>  
  Eli Lilly (NYSE:LLY) grows revenue sharply on Mounjaro and Zepbound demand, expands its oral obesity pill launch and raises its full-year revenue outlook...
- [LLY Nov 2026 1385.000 call (LLY261120C01385000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXX7l-FnIfNGdnunuq1a3FrceBZLVVYPzpBFFigA0EpNWG40JfH1a0LNPhw4fMJ-s8Ouqtxs3YMYGF7404MKYpsCteXgsMVLDddxpZfSPWXkScHjItlHhw9abBMM7KKt7ZdnXNvwLTMeBfYhixGuJI&gsessionid=OomQiHY1UBZ2pxROnvXJLGDXkqTwaINUFhZy2-eI99plpGwezQmyNg)  
  <sub>Yahoo Finance UK, 15 hours ago</sub>  
  Find the latest LLY Nov 2026 1385.000 call (LLY261120C01385000) stock quote, history, news and other vital information to help you with your stock trading...
- [What Keeps Eli Lilly (NYSE:LLY) Close to Its 52-Week High Following a USD 91 Billion to USD 92 Billion Revenue Outlook?](https://www.google.com/goto?url=CAES1AEBxCJF13pN5LUqBCUKGubNeaoNLvpqxg4c39RYhHHTDP0LdjnGtMxA2cnN2ZNp_ltnUJjAUpNqcatgqh3pRON27s6V-Vv6Jt4WdZQKi7H-n5E7SVuzWibupQPpE5sAveYlQd00rwiP4ej03d-0L5OAywNFD1yyW3Svawss-zh_I91ZojNCU0_DLIKCHP02zmykO96V7Bmv2q4RkIOL0_-sDZghraw4LW9QXyKixW-VtRBiQKhNZCC-3DGGTz4mchiHp9i5btk32Iw4tfg6DQD2jD2i4w&gsessionid=OomQiHY1UBZ2pxROnvXJLGDXkqTwaINUFhZy2-eI99plpGwezQmyNg)  
  <sub>kalkine.ca, 24 hours ago</sub>  
  What Keeps Eli Lilly (NYSE:LLY) Close to Its 52-Week High Following a USD 91 Billion to USD 92 Billion Revenue Outlook?
- [How Does ObesityWeek Data Showcase the Eli Lilly (NYSE:LLY) Push?](https://www.google.com/goto?url=CAESqAEBxCJF16ek8ravVQ4pnMygF5oWUNiC1qskfTfcEZ9csJxWdE0ElM4_j6l6We0IQ1uRof5kFV8vRNLzWhab7KFAp4NxjZLJ9riXuveILO9A92mOCteZkFzYooHJ8ZuU6kpOlf3vl6BLsx_QqiTjyC_lXKIz3Kf81smqpyMJFFs-o4t9weMzvsNm-OzcbUUIErRm0_MuCEI3HQxfM1vnUVhVkETCDbbbZMc&gsessionid=OomQiHY1UBZ2pxROnvXJLGDXkqTwaINUFhZy2-eI99plpGwezQmyNg)  
  <sub>Kalkine Media, 9 hours ago</sub>  
  Eli Lilly (NYSE:LLY) drew fresh attention this week as its ObesityWeek data slate spotlighted a widening metabolic-medicine franchise.
- [LLY Dec 2026 1230.000 put (LLY261224P01230000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXeuyI7e5izaSfKlv3GXkVRaPeLKADN988ZV3ZsY78ydXStI-8HQl6LpFp5a4EK1mF944UBRq2r3C4UZaAYgerB2DxoVTCSUpxfLi7LruU35WxS4Zyqc8b7Ma5tJhezaKetzYLuRKRI002KNqQnuw&gsessionid=OomQiHY1UBZ2pxROnvXJLGDXkqTwaINUFhZy2-eI99plpGwezQmyNg)  
  <sub>Yahoo Finance UK, 18 hours ago</sub>  
  Find the latest LLY Dec 2026 1230.000 put (LLY261224P01230000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,367.02 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 1,381.02 (-1.0%), 50d 1,262.61 (+8.3%), 200d 1,116.35 (+22.5%); 50d above 200d
Momentum: RSI(14) 53.0 | MACD 41.092 vs signal 50.250 (histogram -9.158)
Returns: 1d -1.1% | 5d -4.2% | 1m +7.6% | 3m +8.9%
52-week range: 851.21 - 1,443.50 (now 87.1% of the way up)
Volatility: ATR(14) 41.80 (3.1% of price) | annualised 20d 37.5%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.22T
Valuation: trailing P/E 44.37 | forward P/E 26.87 | P/B 30.25 | PEG 1.31
Profitability: profit margin 31.9% | operating margin 51.3% | ROE 86.0%
Growth (YoY): revenue +38.6% | earnings +16.3%
Balance sheet: debt/equity 122.9% | free cash flow 9.34B
Risk: beta 0.39 | short interest 0.8% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-09-30 beat by 18% | 2026-06-30 beat by 38% | 2026-03-31 beat by 27% | 2025-12-31 beat by 12%
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
Consensus: buy (mean 1.65 on a 1=strong buy to 5=strong sell scale, 29 analysts)
Ratings: 5 strong buy, 20 buy, 4 hold, 1 sell, 1 strong sell
Price target: mean 1,468.57 (+7.4% vs last close), range 940.00 - 1,700.00
Recent rating changes:
  - 2026-11-09 Jefferies: main, Buy -> Buy
  - 2026-11-02 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-10-31 UBS: main, Buy -> Buy
  - 2026-10-30 JP Morgan: main, Overweight -> Overweight
  - 2026-10-30 Citigroup: main, Buy -> Buy
  - 2026-10-30 Scotiabank: main, Sector Outperform -> Sector Outperform
Institutional ownership: 85.7%
Largest holders: Lilly Endowment, Inc (9.6%), Blackrock Inc. (7.2%), Vanguard Capital Management LLC (5.7%), PNC Financial Services Group, Inc. (5.5%), State Street Corporation (3.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 39,897 shares in 46 transaction(s) | sold 313,215 shares in 9
Net: -273,318 shares (-13.6% of insider holdings) | insiders hold 1,728,045 shares
Distinct insiders: 0 buying, 4 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-11-02 HAKIM ANAT (General Counsel): 5,000 shares, 7.01M
  - 2026-08-17 JONSSON PATRIK (Officer): 6,500 shares, 7.64M
  - 2026-08-10 ZAKROWSKI DONALD A (Officer): 2,000 shares, 2.37M
  - 2026-08-07 HAKIM ANAT (General Counsel): 5,000 shares, 5.95M
(43 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### MercadoLibre (MELI) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [MercadoLibre: Margin Pressure And Brazil Fears Open A Buying Opportunity (NASDAQ:MELI)](https://seekingalpha.com/article/4970030-mercadolibre-margin-pressure-and-brazil-fears-open-a-buying-opportunity)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  MercadoLibre offers a compelling opportunity at the current price, with the stock having dropped further due to temporary margin contraction. MELI trades at...
- [MELI Nov 2026 2140.000 put (MELI261120P02140000) Interactive Stock Chart](https://finance.yahoo.com/quote/MELI261120P02140000/chart/)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  Interactive Chart for MELI Nov 2026 2140.000 put (MELI261120P02140000), analyze all the data with a huge range of indicators.
- [MercadoLibre, Inc. (MELI) - What Are Brokerages Saying About This Stock?](https://www.google.com/goto?url=CAESvwEBxCJF140Zk-70aFB-HtsjbwlEqkfTYZIqQ9jEUfZBbJUURMedqsp6uJ1rbnz7i7B_tlu3yqyCniCdBI-VrE4YLqKt6ImO3A6YzT143ZM8vsXCc-hENG-vQfC0x9_pVVPe6xC0R8GB8jx7M8OwaVjZ8QVZJeXgbpZiaEtCxVKdLWeZEFzmgpOBrVVR4iDBH4fqALSoEtcqh3ivFXAxuhGrIZTuIf4v2nyLWCs30qzasYqK-yS25gbqF999WNSocQ&gsessionid=clxZeVFlId8kr-NRzoYuSVTD713ky2ai1D3o0U0ePpW6spfG24oeFQ)  
  <sub>MarketBeat, 7 hours ago</sub>  
  MercadoLibre, Inc. (NASDAQ:MELI - Get Free Report) has earned a consensus rating of "Moderate Buy" from the nineteen brokerages that are covering the firm,...
- [MELI Mar 2027 1040.000 call (MELI270319C01040000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESdAHEIkXX_vFE3c1IblYVH6kIWU0iqXEkmZECX3MMg6KED6p-LjfgZzlcBJNQNRjQYj3mhx4Jyln25rPjeNCeOWQ3b-BffEEvdDMPwWqCOFm6XxHP5-XOIpwJAjO9jyd6DCHA1261H6IXfdQbnhpJUEWNHVl6&gsessionid=clxZeVFlId8kr-NRzoYuSVTD713ky2ai1D3o0U0ePpW6spfG24oeFQ)  
  <sub>Yahoo! Finance Canada, 12 hours ago</sub>  
  Find the latest MELI Mar 2027 1040.000 call (MELI270319C01040000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI Mar 2027 2240.000 put (MELI270319P02240000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESdAHEIkXXhZlaD1hcxxTL4GJQMOfPzocwKgDmrs-o81xJ-_staNVqDTCQzGRHcS4oY800E1CFYD0vDpUYlmvMVM27sn1PYnan4WbnXb8hrqR_vL1oelLxGwvQBZWR1eWArCFvm_Cvj7yoOaWcv7P6OzBG5nJ3&gsessionid=clxZeVFlId8kr-NRzoYuSVTD713ky2ai1D3o0U0ePpW6spfG24oeFQ)  
  <sub>Yahoo! Finance Canada, 13 hours ago</sub>  
  Find the latest MELI Mar 2027 2240.000 put (MELI270319P02240000) stock quote, history, news and other vital information to help you with your stock trading...
- [2 Monster Stocks to Hold for the Next 10 Years](https://www.google.com/goto?url=CAESmAEBxCJF1007mO6ijZycTrwyzvnJtQttEOPTF8cx0GID_MqIvoNgbOCRXpP-we8WEYeYe4S9rwYqFUkMW22yxXvor96bbBRSFexWK_lVC6jt3uqi6e2UyYo25uJYpPazeiUGsFb9RyrTT6K5brWTW98ZZklphIk5Spgk2YLikaFWAyaHFZHQD7d_6vsTLT-hdsjIoIuztJwexw&gsessionid=clxZeVFlId8kr-NRzoYuSVTD713ky2ai1D3o0U0ePpW6spfG24oeFQ)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  The best stocks don't just beat the market for a year or two. They compound wealth for a decade or more, and that kind of return almost always traces back...
- [MELI Nov 2026 1470.000 put (MELI261120P01470000) stock price, news, quote and history](https://www.google.com/goto?url=CAESdAHEIkXXxa2xaRHjU-f1srrjleTBXR588EznjFq82tno7ubSxPNAb-GZ77b1GveQRXqhIGwsoCUa2vRP0VgcjDXZbK_8BtfR4msqGeceO5KP4IuuHwV-E0XU6mSWCUXGTx5LWfDU9cIS_hhAYm3KhzGuR-sr&gsessionid=clxZeVFlId8kr-NRzoYuSVTD713ky2ai1D3o0U0ePpW6spfG24oeFQ)  
  <sub>Yahoo Finance UK, 17 hours ago</sub>  
  Find the latest MELI Nov 2026 1470.000 put (MELI261120P01470000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI Dec 2026 1320.000 call (MELI261204C01320000) interactive stock chart](https://www.google.com/goto?url=CAESegHEIkXXWXurvh_KmkOqseIKez1TiInR_Zugdts-bjT7qVBumX521wYLMjLIGFUcvN16_4TmVsgMlmikj2XBmW08rC1xEMTUZLyStsPCsGLbfuhM_tL-7hCwOwVE4VzrsP4BxwxJ4lxdtFg1nnIS94VMNGdbbOeqRRoW&gsessionid=clxZeVFlId8kr-NRzoYuSVTD713ky2ai1D3o0U0ePpW6spfG24oeFQ)  
  <sub>Yahoo Finance UK, 19 hours ago</sub>  
  Interactive chart for MELI Dec 2026 1320.000 call (MELI261204C01320000) – analyse all of the data with a huge range of indicators.
- [MELI Nov 2026 1950.000 call (MELI261120C01950000) interactive stock chart](https://www.google.com/goto?url=CAESegHEIkXX3xrhYGdfp0wEaZlcJJ5gL9lnor4lYeLeM1DJV8QaRSifv4uhpnJdhbozZg4-7s0kt1h_DsBERIGZ_JXjmEMhxS4R0VuY999hU1SUPkPn1YW4yGAPgmJC9_w1SLqJuM6-O4e5RrxFt8Q8DUusX0xLJaa9M1eB&gsessionid=clxZeVFlId8kr-NRzoYuSVTD713ky2ai1D3o0U0ePpW6spfG24oeFQ)  
  <sub>Yahoo Finance UK, 19 hours ago</sub>  
  Interactive chart for MELI Nov 2026 1950.000 call (MELI261120C01950000) – analyse all of the data with a huge range of indicators.
- [MELI Dec 2026 1080.000 put (MELI261211P01080000) stock price, news, quote and history](https://www.google.com/goto?url=CAESdAHEIkXXAxIUjWXuhzikPrUv29opyLuDgS5xLySDZYlpnUX8Er_euuc8WZMz2UR6BBb33dISSmqmM3ZwVsOep0DGCXlVAC2FTkcPp_kk3wa9yOZXAOk73gUXZ3zE5C-c1H1OF-2YtVH92HroEh3DzVJt3d4T&gsessionid=clxZeVFlId8kr-NRzoYuSVTD713ky2ai1D3o0U0ePpW6spfG24oeFQ)  
  <sub>Yahoo Finance UK, 20 hours ago</sub>  
  Find the latest MELI Dec 2026 1080.000 put (MELI261211P01080000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,429.53 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 1,574.47 (-9.2%), 50d 1,722.09 (-17.0%), 200d 1,770.19 (-19.2%); 50d below 200d
Momentum: RSI(14) 30.4 | MACD -93.030 vs signal -82.237 (histogram -10.792)
Returns: 1d +0.5% | 5d -3.1% | 1m -22.9% | 3m -25.7%
52-week range: 1,423.11 - 2,295.00 (now 0.7% of the way up)
Volatility: ATR(14) 57.80 (4.0% of price) | annualised 20d 57.4%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 72.47B
Valuation: trailing P/E 38.35 | forward P/E 26.99 | P/B 8.84 | PEG 0.78
Profitability: profit margin 4.9% | operating margin 7.4% | ROE 26.2%
Growth (YoY): revenue +45.1% | earnings +6.3%
Balance sheet: debt/equity 197.4% | free cash flow -2.57B
Risk: beta 1.39 | short interest 2.0% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 1 beat, 3 missed
  2026-09-30 missed by 8% | 2026-06-30 beat by 4% | 2026-03-31 missed by 7% | 2025-12-31 missed by 6%
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
Consensus: buy (mean 1.52 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 5 strong buy, 16 buy, 4 hold, 0 sell, 0 strong sell
Price target: mean 2,168.14 (+51.7% vs last close), range 1,600.00 - 2,700.00
Recent rating changes:
  - 2026-11-11 UBS: main, Neutral -> Neutral
  - 2026-11-09 JP Morgan: main, Neutral -> Neutral
  - 2026-11-05 Scotiabank: main, Sector Outperform -> Sector Outperform
  - 2026-11-05 StoneX: main, Buy -> Buy
  - 2026-11-05 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-11-05 BTIG: main, Buy -> Buy
Institutional ownership: 81.4%
Largest holders: Capital Research Global Investors (6.0%), BAILLIE GIFFORD & CO (5.8%), Capital International Investors (3.9%), Capital World Investors (3.7%), Morgan Stanley (3.1%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 3,535,594 shares
Distinct insiders: 1 buying, 0 selling
Open-market purchases — insiders spending their own money:
  - 2026-06-11 MELAMUD MARCELO (Officer): 124 shares, 200.00K
(4 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

- [Nvidia Reports Faster Growth, Says Jensen Huang Won’t Return as CEO](https://www.wsj.com/tech/ai/nvidia-nvda-3q-2027-earnings-report-stock-6e642303)  
  <sub>WSJ, 43 minutes ago</sub>  
  In her first earnings call as interim CEO, Colette Kress faced questions over the chipmaker's future without its longtime leader.
- [Nvidia Slides After Blowout Earnings As Investigations Line Up; Is Nvidia Stock A Sell Now?](https://www.investors.com/research/nvidia-nvda-stock-earnings-buy-now-november-2026/)  
  <sub>Investor's Business Daily, 1 hour ago</sub>  
  Nvidia (NVDA) shares dropped Wednesday as investigations into export controls at the artificial intelligence chipmaker and into ex-Chief Executive Jensen...
- [Nvidia (NVDA) Stock Drops Despite Q3 Results Showing Huge AI Earnings](https://www.google.com/goto?url=CAESnQEBxCJF11iYTjVI9jnIvOcET-6M4EpOa7aMxUbdomABqG4SzOYMNpEE54SrROzYNeJZ5g1l9a_DoWA6u7Puk0twuVwYJ71XvI_arwRfBKcE--Ap8bonXXTQl8nsS6vgOkBiNP6qcoI_YRVWJhlskqWk8esj_iQkwt8xvdnbip91-d8-tvK_lRDo_oJRvvF9g5ClTQRYb3S8IBO6Sn83&gsessionid=ritn7dQBJR4Z39qp8HjKa552qCH8qWUYZHaGEydUvygYUD0gqr_W0A)  
  <sub>Yahoo Finance, 15 hours ago</sub>  
  NVIDIA just posted Q3 2027 results that read like an artificial intelligence supercycle, yet the stock closed down 2.9% today and sits well below its recent...
- [Why Nvidia Stock Isn’t Getting the Full-Throttle Anthropic Boost](https://www.google.com/goto?url=CAESiwEBxCJF12TYrOh_vSEems1CSquQhz93Bz9TPEVeGRWE-2KAeXsXV1hdmJ0ciexdj2wRtktdiRMAZe_sB4DDee7TgHIrolJpMu8YhLkTVXZIyZ0Dv_SzdSqm3ZrCrBqnjGmG2AVoRhexWfmYciXCkXzov1OGcEK_5WtOvI4iW9UvkKucgPKuTyp1-qxW&gsessionid=ritn7dQBJR4Z39qp8HjKa552qCH8qWUYZHaGEydUvygYUD0gqr_W0A)  
  <sub>Barron's, 2 hours ago</sub>  
  Nvidia stock is down in the dumps. The AI trade had been faltering for months amid concerns around rising debt and the sustainability of spending.
- [Why Is NVIDIA Stock Gaining Thursday? - NVIDIA (NASDAQ:NVDA)](https://www.google.com/goto?url=CAESugEBxCJF11iUHoaO7EKZ68h7h27xbRnmtfDqsxTdWtaK8dmxqbay5LTZtdLlTUL04Gon9JpJsHk3kzBh3ovTK2FpOJFtdDSVubTK5fnL14d2Jlq3tRsWcOTLweEVKnZym8xkbLAqfBEGJFWcIsYnvT0RZ_-VHdMdS8e_h5FTrTYRjGeFtS85L-OXiMZL17LwUCQDyvA1Vl-ecCIre8r1euAEKXq2FcU02fnugHewx0vTr8i2iEy5Xjm6tRg&gsessionid=ritn7dQBJR4Z39qp8HjKa552qCH8qWUYZHaGEydUvygYUD0gqr_W0A)  
  <sub>Benzinga, 4 hours ago</sub>  
  NVIDIA reported third-quarter fiscal 2027 revenue of $115.84 billion, up 103% year over year and above analyst estimates of $109.08 billion.
- [A tech fund manager sold Nvidia before the drama. Here’s why it won’t buy the dip.](https://www.google.com/goto?url=CAESpwEBxCJF1xuqloeZTMuC7jYldrTd7lvM0YXS5vlLvt7wzXDNkbHMQGQ4eUmvbHQWDr-W755pWDESjQQa4xg3ZGFBKmLsY25oA0KaX2zNJdrcBuKzhzMbz9IKm8K3yUC4k6xHCvazWMUMj1LCMg9ruyegp2HyN61l3kPof_Yc1f2i9OehbgeTNiWe2nVh3a2VAZrhIj8wBByc87XNsjfxaBycBitsJQzlzg&gsessionid=ritn7dQBJR4Z39qp8HjKa552qCH8qWUYZHaGEydUvygYUD0gqr_W0A)  
  <sub>Business Insider, 6 hours ago</sub>  
  Asset manager BIT Capital sold Nvidia amid an AI-stock rout triggered by a Texas election upset, before the chip giant's leadership crisis.
- [GTA VI publisher racks up nearly 3x Nvidia’s tokenized stock volume](https://www.google.com/goto?url=CAESwQEBxCJF17vBc48vF3HsAG4DOg0BijsRxuTB_gTIyyUVKF6SjA9Cph-Rcc4x-AqBSZkxPbUMEEHtJlyxsjNZv7XCZDO-fcLmgwH-nc0c0uIo2EEb-7hKX6QfS_vCRyRoy_KTlnsY3tOLO1-QrXGJYZtJuH-e4M2zJwB22KZeUTCtpzHAtVQuq4ksxxkW9cS-dznRYzSCodmPQds3lela5AJTymquG-HKWk0S_TeChQMY6JZ3c0aeIO99kuSLWYLLGAa6&gsessionid=ritn7dQBJR4Z39qp8HjKa552qCH8qWUYZHaGEydUvygYUD0gqr_W0A)  
  <sub>TradingView, 2 hours ago</sub>  
  Tokenized shares of Grand Theft Auto VI publisher Take-Two Interactive recorded nearly three times the trading volume of tokenized Nvidia shares on...
- [Wedbush raises Nvidia stock price target to $293 on demand outlook](https://www.google.com/goto?url=CAESugEBxCJF1268Semfme5dS2g-dv2KchLVeSV0qE0_MCxQOYQlgsUzMgVv3IAUg_7DhJKtEPwl5lYhRolwMtbBN2DLBv-KHSIn-S2XJ_lQUSNzpM3PhkTA2U89ztJYoIBCRqWbIRr9jqsl3yHTuA6T2ogDj1a3iQjJuk_AG7u-7aU4svjh5gJGfM616oaTZLSfk6mfHIPW1kmVcvRsvLOWUQ2wdHOGN2hYOPj9dD8hVn6chK6j-AeWygcKHRs&gsessionid=ritn7dQBJR4Z39qp8HjKa552qCH8qWUYZHaGEydUvygYUD0gqr_W0A)  
  <sub>Investing.com, 40 minutes ago</sub>  
  Investing.com - Wedbush raised its price target on Nvidia Corp. (NASDAQ:NVDA) to $293 from $275 while maintaining an Outperform rating on the stock.
- [NVIDIA Corporation (NVDA) stock price, news, quote and history](https://www.google.com/goto?url=CAESZQHEIkXX7R35EVDHi9uYib5y0rRahXknGluiRYj1Op8pRnpXQKuhLoEackpGjnD5BQetRYvak3yFmYOb14hJZbs0k1WnI8iAF1Yav5pX93mlCAoRHTOI_JAiMk2nDSA_0ieblQta&gsessionid=ritn7dQBJR4Z39qp8HjKa552qCH8qWUYZHaGEydUvygYUD0gqr_W0A)  
  <sub>Yahoo Finance UK, 16 hours ago</sub>  
  NVIDIA Corporation (NVDA) · -13.11% · -29.50% · -32.10% · -19.06% · -16.76% · 376.59% · 344,951.46%. Key events. Baseline. Advanced chart. Loading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 156.95 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 186.28 (-15.7%), 50d 209.08 (-24.9%), 200d 203.63 (-22.9%); 50d above 200d
Momentum: RSI(14) 27.6 | MACD -16.887 vs signal -13.872 (histogram -3.015)
Returns: 1d +4.0% | 5d -5.6% | 1m -29.3% | 3m -26.9%
52-week range: 150.96 - 239.24 (now 6.8% of the way up)
Volatility: ATR(14) 9.45 (6.0% of price) | annualised 20d 53.5%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 3.79T
Valuation: trailing P/E 16.86 | forward P/E 9.45 | P/B 14.19 | PEG 0.18
Profitability: profit margin 62.5% | operating margin 66.1% | ROE 117.4%
Growth (YoY): revenue +103.2% | earnings +107.7%
Balance sheet: debt/equity 14.3% | free cash flow 99.24B
Risk: beta 2.25 | short interest 1.2% of float
Next earnings: 2026-11-17
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-12-31 beat by 6% | 2026-09-30 beat by 4% | 2026-06-30 beat by 4% | 2026-03-31 beat by 4%
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
Consensus: buy (mean 1.79 on a 1=strong buy to 5=strong sell scale, 55 analysts)
Ratings: 11 strong buy, 34 buy, 15 hold, 2 sell, 0 strong sell
Price target: mean 246.67 (+57.2% vs last close), range 130.00 - 425.00
Recent rating changes:
  - 2026-11-12 Melius Research: down, Buy -> Hold
  - 2026-11-12 DA Davidson: main, Buy -> Buy
  - 2026-11-12 Craig-Hallum: down, Buy -> Hold
  - 2026-11-12 B of A Securities: main, Buy -> Buy
  - 2026-11-12 BMO Capital: main, Outperform -> Outperform
  - 2026-11-12 Baird: reit, Neutral -> Neutral
Institutional ownership: 71.6%
Largest holders: Blackrock Inc. (8.1%), Vanguard Capital Management LLC (6.4%), State Street Corporation (4.2%), FMR, LLC (3.9%), Geode Capital Management, LLC (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 2,613,243 shares in 18 transaction(s) | sold 6,198,325 shares in 9
Net: -3,585,082 shares (-0.4% of insider holdings) | insiders hold 973,159,296 shares
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

### Procter & Gamble (PG) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Is P&G Stock A Bad Buy Near Its High?](https://www.trefis.com/stock/pg/articles/626866/is-pg-stock-a-bad-buy-near-its-high/2026-11-19)  
  <sub>Trefis, 4 hours ago</sub>  
  Today's big story: Could Anthropic Stock Fall 25%?Most investors know the rule: buy low, never at the top. Procter & Gamble (PG) stock closed at a 52-week...
- [PG Dec 2026 170.000 call (PG261211C00170000) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/PG261211C00170000/)  
  <sub>Yahoo Finance Singapore, 2 hours ago</sub>  
  Find the latest PG Dec 2026 170.000 call (PG261211C00170000) stock quote, history, news and other vital information to help you with your stock trading and...
- [156,170 Procter & Gamble Company (The) $PG Shares Bought by Private Advisor Group LLC](https://www.google.com/goto?url=CAESygEBxCJF16UHR9J41WFeaBXa5ZJoPc8EZgko-cAaM1Di4HAG1oV54qyj6QvJkbmVvslei9ZBuGY-p10T3DBu8rj9GOMENx8l5zCe1trY44vnO4coAq7IHOIMpIBKYAyb0UJFy-zCp5GI1iapzwAPX_eJmSKPXut0I0H0xkvbdHQHFGIEwTE8EWapKT0Vq5gNULA9KI0pnbgscDfmRcWGpgKJhEyHe4sknywukjvDBDTpSk2Cd1-SZv1NNgfUEP-10EhxF9XHf6W_wbr1&gsessionid=HLLB8xCoWfcCPMTYQNTIF5bbISww_t-teqp4WRY-eC9zwGOHBqn7sw)  
  <sub>MarketBeat, 10 minutes ago</sub>  
  Private Advisor Group LLC lifted its position in shares of Procter & Gamble Company (The) (NYSE:PG - Free Report) by 68.4% during the 3rd quarter,...
- [Copper price hits 7-month low: Voltas, PG Electroplast, Blue Star shares rally up to 7% on input cost relief hopes](https://www.google.com/goto?url=CAES6wEBxCJF17MkXgw7SnGlt4f42VvrdBmCClLANfL16qghS_RET0hoQhs8QmX8O1Q93oYYyTtsDXNlmnKMXF_XhbHuiRxcwbvTohhO55LX1j7k4vAse7ePmCIRuf8Wcpwmkp7NLMhdA17abM20_kyc-zLMZer8A8cmKpOXpISbzlFvO8ExH5W7sbSTMfXX6qVkIRSLbyH_zbiFeKszGnhp1cX7KGyaW2apg2HBz2YBxhNAbm7aFdsoEoEDM9RMsRp8Y7tfjDh0GpHraVuxAk6di7_N7I1rf8a-CHE8p-Vw5ec6-cOOCE_1QgVL-Sxp&gsessionid=HLLB8xCoWfcCPMTYQNTIF5bbISww_t-teqp4WRY-eC9zwGOHBqn7sw)  
  <sub>TradingView, 9 hours ago</sub>  
  Shares of air-conditioning and cooling products manufacturers witnessed significant rally in today's trading session, November 19, as copper prices tumbled...
- [Why (PG) Price Action Is Critical for Tactical Trading](https://www.google.com/goto?url=CAESwgEBxCJF12DMkvA17Npxto1qMBvbHda1hg2cOnW-fjZumZa6qFNFgPKZubb51lciQpjpn3nXWklfRyiT-mDrlALlsFy8_j_uNfhjgYrlDpob6O7JeUpHp-mVdR_yLueqbKO-RDzzXzv8cG8Egz6WK2AKKtzBpyGv73AR5pY8aPMesRdjTIBPafx3NacQ-4S9XFl9thRXWxAHQst27Vv8aowHllFNu85_M9KDXLFGGdRndj2rZckPSaWwi74dEr4eRh6obA&gsessionid=HLLB8xCoWfcCPMTYQNTIF5bbISww_t-teqp4WRY-eC9zwGOHBqn7sw)  
  <sub>Stock Traders Daily, 20 hours ago</sub>  
  Key findings for Procter & Gamble Company (the) (NYSE: PG). If Near and Mid-Term Strong Sentiment Holds, It Could Extend to Long Term...
- [153,538 Procter & Gamble Company (The) $PG Shares Bought by Ieq Capital LLC](https://www.google.com/goto?url=CAESwAEBxCJF1wVP6yVKf0nzughAUJ8a1G5DOhTn2tyKzkbgDcW8HnobTH54RPNlmS3P0PJ2coMYIcu6aeXFbAYE3-GFfSNnbMLmFTzbY6PlYva4C3eNdMF7oAXLsvBydXCB88Z-GiV0Qs-ZiD5CWssuguxpvwA-XJBC42IC1jcMcej5ZByWXVwIktLuYedr__98LCnxq5c56ETZlyubHjk6VEluBcmYO8sSoAGUXNqgdc9xmcUpRa854OeFuL9Kbcwgh5Y&gsessionid=HLLB8xCoWfcCPMTYQNTIF5bbISww_t-teqp4WRY-eC9zwGOHBqn7sw)  
  <sub>MarketBeat, 54 minutes ago</sub>  
  Ieq Capital LLC raised its holdings in shares of Procter & Gamble Company (The) (NYSE:PG - Free Report) by 91.7% in the 3rd quarter, according to its most...
- [Copper price hits 7-month low: Voltas, PG Electroplast, Blue Star shares rally up to 7% on input cost...](https://www.google.com/goto?url=CAES7QEBxCJF134ud1pNCiUCvOjNrnJdvwP5wL94Ei3VJHDDU-goPgkwpfuRI-2VPHZNvFdU5dJ6d6Rx8a31SMvGTw331WpdHDnXkZgG2UUnJTclo7uKMbTV0MsT-6NUj94GcyWJW3vWlXzAsQiJb8ULL5Db3R7S3j4Re8cHSAxiwZSeAX4MTLIbrcb88y5CQvyQJ-7l9_4U6UWX79HqrXeLlyaXfUsjeDfad_fXp9ABiAuvbQPy94f7vtTV29SPCXENhxB7Xe_8G59OCIoKOT5zoI0XnUb8bNG8TQdi54o9VcfS6FCPskQ5MvU8_sfHE-o&gsessionid=HLLB8xCoWfcCPMTYQNTIF5bbISww_t-teqp4WRY-eC9zwGOHBqn7sw)  
  <sub>Moneycontrol.com, 9 hours ago</sub>  
  Shares of air-conditioning and cooling products manufacturers, including Voltas, PG Electroplast and Blue Star, witnessed significant rally in today's...
- [Is P&G (NYSE:PG) Raising Its Guidance?](https://www.google.com/goto?url=CAESigEBxCJF14_aC7Y7JV603gbH_HY0AWVNxxO23vymsnlIdRML6c_BKsrYe18-JWX8UzFWEO6WikiE9DFcMV_elexzjqj3XSD0uwE__J1cyn3LPuGRA6-LHHLYPzB-R7auEwMxNzMeFnE1mUfNkvQjDKXFSoLqo3PSAU9S2nDgyPe6FdGFEE5xUXmdiUw&gsessionid=HLLB8xCoWfcCPMTYQNTIF5bbISww_t-teqp4WRY-eC9zwGOHBqn7sw)  
  <sub>Kalkine Media, 10 hours ago</sub>  
  Procter & Gamble (NYSE:PG) draws attention as the consumer-goods group lifts its guidance and widens its cash-return plans on volume-led organic revenue...
- [PG261120P00146000 Interactive Stock Chart | PG Nov 2026 146.000 put Stock - Yahoo Finance](https://www.google.com/goto?url=CAEScQHEIkXXJDJ5-Igi4RTrIZL1TiSbbBZn2jO75LH9YF7l_UKVkA5Sc7PFyly00zbvLiZRTq2zU2v4ImWbPRgt_mSMa6YrYI_FkaXnNtT_0F20c3lzpCtutaO78mdIOGS_JhEQTVDIf0qtA8RjD7kPTZ0P&gsessionid=HLLB8xCoWfcCPMTYQNTIF5bbISww_t-teqp4WRY-eC9zwGOHBqn7sw)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [AC makers shine as copper extends fall; Voltas, Blue Star rally up to 8%](https://www.google.com/goto?url=CAESxgEBxCJF14lIIKGfcGswjXQNb6qySZ0lmT7octo4klMxaMzBsoqLC0S3frsNPb-spfzTbFof_ZhhmTfwAQmN80yLnY3xI-pEFYfgjs8dkV357cbsaP4m6PZxm9Y-eEn7Wd_cxuDD4KGgw6LuioeMqYtRK6UQ0GKJ1Umq0jJMC1GiOQKCnTpY6nAsefvbsv6YaQgdaO9urT52VbItWnN9-Yjxfk19MYccOKBgvhAP6dyCsH3j0LJrYMYnD26jNrl2RHJ_P8W_8ig&gsessionid=HLLB8xCoWfcCPMTYQNTIF5bbISww_t-teqp4WRY-eC9zwGOHBqn7sw)  
  <sub>Business Standard, 8 hours ago</sub>  
  Analysts said consumer durables stocks are seeing buying interest as the Street anticipates some relief on input costs, aided by declines in copper and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 167.11 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 165.53 (+1.0%), 50d 156.35 (+6.9%), 200d 150.20 (+11.3%); 50d above 200d
Momentum: RSI(14) 56.8 | MACD 3.980 vs signal 4.186 (histogram -0.206)
Returns: 1d -1.9% | 5d -0.5% | 1m +6.5% | 3m +15.5%
52-week range: 138.04 - 173.02 (now 83.1% of the way up)
Volatility: ATR(14) 3.18 (1.9% of price) | annualised 20d 22.5%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 387.32B
Valuation: trailing P/E 25.17 | forward P/E 22.53 | P/B 7.13 | PEG 4.38
Profitability: profit margin 18.2% | operating margin 24.9% | ROE 29.6%
Growth (YoY): revenue +4.0% | earnings +0.8%
Balance sheet: debt/equity 70.3% | free cash flow 12.65B
Risk: beta 0.36 | short interest 1.0% of float
Next earnings: 2027-01-21
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 1 beat, 3 in line
  2026-09-30 beat by 3% | 2026-06-30 in line | 2026-03-31 in line | 2025-12-31 in line
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
Consensus: buy (mean 2.12 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 5 strong buy, 9 buy, 10 hold, 0 sell, 1 strong sell
Price target: mean 174.78 (+4.6% vs last close), range 151.00 - 190.00
Recent rating changes:
  - 2026-10-26 Barclays: main, Equal-Weight -> Equal-Weight
  - 2026-10-26 Piper Sandler: main, Neutral -> Neutral
  - 2026-10-23 Freedom Broker: up, Hold -> Buy
  - 2026-10-23 UBS: main, Buy -> Buy
  - 2026-10-23 Citigroup: main, Buy -> Buy
  - 2026-10-23 BNP Paribas: main, Outperform -> Outperform
Institutional ownership: 72.2%
Largest holders: Blackrock Inc. (8.4%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.4%), Geode Capital Management, LLC (2.9%), Vanguard Portfolio Management LLC (2.8%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 322,138 shares in 48 transaction(s) | sold 233,622 shares in 27
Net: +88,516 shares (+3.2% of insider holdings) | insiders hold 2,804,517 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-11-12 ABD EL HAK HESHAM (Officer): 2,250 shares, 379.06K
  - 2026-11-05 SCHULTEN ANDRE (Chief Financial Officer): 30,677 shares, 5.18M
  - 2026-11-04 SCHULTEN ANDRE (Chief Financial Officer): 33,624 shares, 5.55M
  - 2026-11-03 JANZARUK MATTHEW W. (Officer and Director): 9,479 shares, 1.55M
(46 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Toyota (TM) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [LASE to Premiere Quantum Bullet(TM) at Counter UAS Technology Conference in Washington, D.C.](https://finance.yahoo.com/technology/articles/lase-premiere-quantum-bullet-tm-103000413.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  Executive Chairman Dmitri Nikitin to Address Senior Military, Government and Industry Leaders as Featured SpeakerORLANDO, FL / ACCESS Newswire / November 19...
- [When the Price of (HBND) Talks, People Listen (HBND:CA)](https://news.stocktradersdaily.com/canada/when-the-price-of-hbnd-talks,-people-listen_20261119_0fd12e)  
  <sub>Stock Traders Daily, 3 hours ago</sub>  
  When the Price of Hamilton U.S. Bond YIELD MAXIMIZER TM ETF HBND Talks, People Listen.
- [Ford Yields 5.27%, but These 3 Auto Dividends Come With Different Risks](https://www.google.com/goto?url=CAESrgEBxCJF181e3Wn67SO-2W9ouD9ANqcagbVqwrQCS_O3-wmfFwJvpTfCnIRHaXutE8zGh0zR6a5rq-Iu80h6Eviw1E5NmKlMDIHyJXZTUz6L-dHlHWb9qnxwSGiJE9_QSnLKZ8QGKwEM61MnYzB0jF5hFxdsTnYXOYH2CRRrV_uKHOAO4G1ZQl94EGCs62RCM5RHREH63w8ysg4KkAKVkqlb-10HicMLhInakVAH76o&gsessionid=e2eQ49QKAwbBXOV7OCcBFJmkhOoOyxyuJu6EEQEAXq7jvLP89I8Jdw)  
  <sub>24/7 Wall St., 18 hours ago</sub>  
  Ford (F) yields 5% and covers its dividend with cash flow: $4 billion of free cash flow through nine months versus $2 billion paid out. Toyota (TM) pays out...
- [Safe Pro Group (NASDAQ: SPAI) Wins Scalable Innovation Award for SpotlightAI(TM) Demining Technology](https://www.google.com/goto?url=CAESxAEBxCJF1zRaq6GodWijIrtIPPHaFEANEs4BDCgcsULZUiAQHr88iACvM1hs0pg8NLuq4MvCY03OwNUdduzIo2U6E8BJ_mdczBEx6z1UwxVvjMHUJ-iRSqDHU8YTJlzWyk1PEtwZDHZJnojpXsviV7UOUnAP-LDHQa5L3veA_2YJPcVCxcF7dmYravE6w8d1kGtUX1xVf69jTwj_e0ZhoZ4djyeYbnyWtC3eJfglliW2rc08ymohMWfniBRkvLsPffF1p7Bx&gsessionid=e2eQ49QKAwbBXOV7OCcBFJmkhOoOyxyuJu6EEQEAXq7jvLP89I8Jdw)  
  <sub>Benzinga, 21 hours ago</sub>  
  Austin, Texas, United States, November 18th, 2026, FinanceWireSafe Pro Group (NASDAQ:SPAI) announced that its cloud-based artificial intelligence (“AI”)...
- [Toyota invests beyond cars into robotics, AI, e...](https://www.google.com/goto?url=CAESnwEBxCJF1znIf8t1vIk5EZDiCW0Q1PdMG4r815UZMM2x479xdcgvYhppPYaGP1ZHd7dfSILdX-Mi8MabiKOtjRj-q7Oo-wzsNBIFzyYCon5oll_FjZYP1OjOnRRY6Ng6ZePANZ-cn3T-MA2bbvNdf6Cj2uhHmIZaLOdplY_yIjqqkV6aqpGhWfI5_tH_AekMzlPIuv-loFuQTuveqNlf-SM&gsessionid=e2eQ49QKAwbBXOV7OCcBFJmkhOoOyxyuJu6EEQEAXq7jvLP89I8Jdw)  
  <sub>Pluang, 10 hours ago</sub>  
  Toyota is expanding its focus beyond traditional automotive manufacturing by investing in robotics, physical AI, energy, aerospace, and other emerging...
- [Sensex Today Rallies 990 Points | Nifty Above 25,500 | 3 Reasons Why Indian Share Markets Are Rising](https://www.google.com/goto?url=CAES3AEBxCJF1yRM7HEvdiVaKz55jM7D3izV-R0IEb8677nOSTKhYcc8CCJmeN_Ssg6PfMWr6hZPEwDFKPNNRgLAYH-JAEjMFfsfz7yqIiyHwtvMOnGjHCX0brYDcw6f38cUgd6CTPwR-sotxEFsZQNSlu7NhYEktr4LsrIlN_9zFbOm0II0DqOiQh5jS0X33YxDrH1lmcko-KT-rNmEVhwNxIskphTgbES5nvwyRaFWwIPH0ElxcuLSYCcoXktOXIshaJpF64GaBgimmbWwxeoUllXs7dXFJRta_Tbam2hK&gsessionid=e2eQ49QKAwbBXOV7OCcBFJmkhOoOyxyuJu6EEQEAXq7jvLP89I8Jdw)  
  <sub>Equitymaster, 3 hours ago</sub>  
  The BSE Sensex ends 990 points higher, while Nifty ended 286 points higher, up at 25514.
- [A recyclable car seal can weigh up to 44% less than conventional seals. It just won an award.](https://www.google.com/goto?url=CAESrQEBxCJF15fsXch5RVnaN86gIKyR7AjxEO6QukuWpjfdQ6QLLYWzonYpW0ljfn-mD0bUrVTG0pehJgt5yiW-75HZ25golCK18Rn3I8ck3_1PuXBeomlczfKKF4tzsgguWYkuf5AO3PyzIdnCv0TFRQxIyGzZs8i0S55CI2pWmvtOSV2OGGLLt2MMO81FlG_JqxRvahYtoxhOdnLg-KB8UphyflMkvv_87cm1syjrrA&gsessionid=e2eQ49QKAwbBXOV7OCcBFJmkhOoOyxyuJu6EEQEAXq7jvLP89I8Jdw)  
  <sub>Stock Titan, 1 hour ago</sub>  
  FlexiCore is expanding across more vehicle programs; its 100% thermoplastic design makes installation up to 20% faster than conventional solutions.
- [Vera Clinic Shares First Clinical Results for the Vector-10 (TM) CVD Diamond Blade](https://www.google.com/goto?url=CAESrwEBxCJF1yqVheSAYMHE1-Mfp7d6I1gRn4XarCAqfxfg3ngifZEbCJyTFtHD5DGsedseGHmaXnRWyFERwX6ump9VsDz1xmjoTOFV3l1VecDI_9PXW89nG2lsbv8-wvs-Lm8sFxJOjms52msroM6hLN1F1I3KfRQuVIOAKAzxSNtDVd7FFJlmqqjqj8NQeWH59RFk9tei8ZEP4xgr70zdYs7kY0sDsAfAaA0JgVJkNjkX&gsessionid=e2eQ49QKAwbBXOV7OCcBFJmkhOoOyxyuJu6EEQEAXq7jvLP89I8Jdw)  
  <sub>Benzinga, 23 hours ago</sub>  
  Istanbul, Turkey, November 18th, 2026, FinanceWireEarly results from 30 patients followed by Vera Clinic Academy show 94.4% graft retention at six months...
- [(EMAX) Trading Report (EMAX:CA)](https://www.google.com/goto?url=CAESigEBxCJF1wfxfNLCeignc7P4kBpb-IuyO5XTUf7-2m5OhjgJmWhhjVToeG_s4KBDZptW3wCldyEdMwDr9RyV9DtppKSXaRp0FJWnC2enEvxmUbTbdTZP9adDqxceVLgEZx4vqRtn18B_H2ikEp5zqMuBA-0hqm-fyEszNe8gFiVfGYEbgVvSge5wfrA&gsessionid=e2eQ49QKAwbBXOV7OCcBFJmkhOoOyxyuJu6EEQEAXq7jvLP89I8Jdw)  
  <sub>Stock Traders Daily, 19 hours ago</sub>  
  Trading Report for Hamilton Energy YIELD MAXIMIZER TM ETF EMAX With Buy and Sell Signals.
- [A planned five-truck test will put natural-gas trucks into Canadian fleets for up to a year](https://www.google.com/goto?url=CAESsgEBxCJF14mhGf4ZsARx211woKSD6qtQqewDLewJvtZ-DNXoqFUL_Bd5YgJuj3VCMEvbgDJK5juwy_8mZXz_vFbsWEe8mPTZfgb0stDW4eAREVLTuKuLJ5CMOIzGstyxyDVg89x169R8F34iKx_KrwL_Ee-7QKblQAdmcwi7_1nkt4g7dqT5_GF2AlFBJ5oS4p9t6a26krkD9Qpr7liaLGRqg6aK8Gvy6fj2izfL_6kxUBJO&gsessionid=e2eQ49QKAwbBXOV7OCcBFJmkhOoOyxyuJu6EEQEAXq7jvLP89I8Jdw)  
  <sub>Stock Titan, 3 hours ago</sub>  
  Aetherion Technologies (AETR) was awarded C$2.0 million in Fuel Innovation Fund support to demonstrate compressed natural gas (CNG) trucks in Canadian...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 210.55 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 205.84 (+2.3%), 50d 196.34 (+7.2%), 200d 197.48 (+6.6%); 50d below 200d
Momentum: RSI(14) 59.0 | MACD 5.151 vs signal 5.290 (histogram -0.139)
Returns: 1d +0.2% | 5d +0.4% | 1m +8.1% | 3m +6.7%
52-week range: 166.50 - 248.29 (now 53.9% of the way up)
Volatility: ATR(14) 4.06 (1.9% of price) | annualised 20d 38.8%
Volume: 0.67x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 247.10B
Valuation: trailing P/E 9.60 | forward P/E 13.34 | P/B 16.76 | PEG 19.65
Profitability: profit margin 8.1% | operating margin 7.5% | ROE 11.6%
Growth (YoY): revenue +8.6% | earnings -10.1%
Balance sheet: debt/equity 112.8% | free cash flow -3.04T
Risk: beta 0.38 | short interest 0.1% of float
Next earnings: 2027-02-04
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 in line
  2026-09-30 in line | 2026-06-30 beat by 44% | 2026-03-31 beat by 12% | 2025-12-31 beat by 27%
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
Consensus: buy (mean 2.25 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 1 strong buy, 1 buy, 2 hold, 0 sell, 0 strong sell
Price target: mean 238.08 (+13.1% vs last close), range 230.00 - 253.00
Recent rating changes:
  - 2026-11-12 Freedom Broker: down, Buy -> Hold
  - 2025-11-07 Freedom Broker: down, Buy -> Hold
  - 2025-02-04 Macquarie: up, Neutral -> Outperform
  - 2024-06-14 Erste Group: down, Buy -> Hold
  - 2023-07-11 Morgan Stanley: down, Overweight -> Equal-Weight
  - 2022-10-06 UBS: down, Buy -> Neutral
Institutional ownership: 2.3%
Largest holders: Fisher Asset Management, LLC (0.5%), Morgan Stanley (0.2%), FMR, LLC (0.1%), Goldman Sachs Group Inc (0.1%), Bank of America Corporation (0.1%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 1,130,711 shares
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

- [How XOM's Strong Balance Sheet Helps Manage Oil Market Volatility](https://finance.yahoo.com/energy/articles/xoms-strong-balance-sheet-helps-131400951.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  ExxonMobil Holdings Corporation XOM, an integrated energy giant, generates the bulk of its earnings from its upstream operations. With a strong presence in...
- [What's behind Exxon Mobil's latest stock pullback?](https://tradersunion.com/news/stocks/show/4313146-exxon-mobil-slides-3-66percent-today/)  
  <sub>Traders Union, 10 hours ago</sub>  
  Exxon Mobil Corporation (XOM) dropped 3.66% today as continued selling pressure dominated trading, even as the company launched a $3 billion debt repurchase...
- [ExxonMobil (XOM) Just Achieved Something 95% of S&P 500 (GSPC) Members Haven't Done](https://www.google.com/goto?url=CAESmgEBxCJF181_kEesJoGZGLSUSlsYAWEp2xbxj2loNqbGOkQQeXFrfrLa8mcCKmVAJ5andSBmQkr8PvoCHIEqJtflCB71UrSQqzuamz_WcWh90__5P2mRZDjAKfJS82A1bHAPCJxhLt758BCvfi8FB09kDWdxcb6ZNN8APALaRxW7uErzDjtmNruOPdFKHcxL6EimYJnBvq-Pjjkt&gsessionid=uNDeQNVg9TdhF3dBU8A9LvA8zCkV0KwAJVZBRxpnLBdXAyPgiekqCQ)  
  <sub>The Motley Fool, 18 hours ago</sub>  
  In late October, the energy giant ExxonMobil (XOM -3.96%) declared a fourth-quarter dividend of $1.07 per share, payable on Dec. 10, 2026, to shareholders...
- [183,059 ExxonMobil Corporation $XOM Shares Bought by Private Advisor Group LLC](https://www.google.com/goto?url=CAESxwEBxCJF1yNWL5qbcMoQgoJliBHSSVMdgckRA5lz1PVTmVnrb__xqgxt_TvbgxfPX30hyi_lWRZV5jKe3J4Od1njdVPtf4LlqZsTogJBj1SGSWs88o5eZ7fr3a6sne0n5RXX6W_DfbWK7neSyaF1lK0Nj5tHhppxe0vJj3KMIyqIUYvQ1Xqn0Kj97EfB19fyK6mGhCys2eT5LoGikmCeId4AANbwfIU7-f8z6KWTIMSQDDoR_W-FLrPZQHUOzQ40rtrTh0zjKLde&gsessionid=uNDeQNVg9TdhF3dBU8A9LvA8zCkV0KwAJVZBRxpnLBdXAyPgiekqCQ)  
  <sub>MarketBeat, 10 minutes ago</sub>  
  Private Advisor Group LLC increased its position in ExxonMobil Corporation (NYSE:XOM - Free Report) by 32.5% during the third quarter, according to the...
- [Exxon Mobil Corp Stock (XOM) Moved Down by 3.28% on Nov 18: A Full Analysis](https://www.google.com/goto?url=CAESjwEBxCJF1-m8kv0QCTD23dV-Nt4KJgd0U1tXRXcgE8nB0sBQQmD5bsCbzaK_VfGT-bXK1INPZSvVIJ-YBhsGVODbxBncCct-oYH1bdBQWi4Jsz2pJqLq6Bx76kb3EGKVobmU76c25GXNe_89mbwOiJXxHDqQAVfdssQixan2PnJCPkN6eB2BoBo7_EYJpFccFw&gsessionid=uNDeQNVg9TdhF3dBU8A9LvA8zCkV0KwAJVZBRxpnLBdXAyPgiekqCQ)  
  <sub>TradingKey, 22 hours ago</sub>  
  Falling global crude oil benchmarks and inventory builds pressured Exxon Mobil shares.Refining margin normalization and petrochemical headwinds diluted the...
- [(XOM) Price Dynamics and Execution-Aware Positioning](https://www.google.com/goto?url=CAESwQEBxCJF1wocmcfYYQpFi0Sh15kQ8ZwKmKuY-dNawtK4tlnF9k4b8dqx1jlHZST81tpFwj4wcpjpMAgQEcvVpnaNc-l5TqmrEskCGmULn2Ynrz0hHuLHmxmGnMHLlxVRgntgOK41WKn_MPAur2kUkC6Lp18nvHVCz7Z7qoHvuGWAj_horlYEB6URZpI3zH2MSacmjJR8QwVYJ8w0r5zXJ7AHbe3BV5_cuzbun6xavvib-azoJUAr-U1a2TgOdK8z5Vh-&gsessionid=uNDeQNVg9TdhF3dBU8A9LvA8zCkV0KwAJVZBRxpnLBdXAyPgiekqCQ)  
  <sub>Stock Traders Daily, 19 hours ago</sub>  
  Price-action only: Exxon Mobil Corporation (XOM) movements set the tone for institutional models. (XOM) Price Dynamics and Execution-Aware Positioning.
- [Exxon Mobil Stock: Business, News and Key Risks](https://www.google.com/goto?url=CAESgwEBxCJF17huUuvvwpjap6A6864dsk5AZshx3dbXpiB8b0IY7-kxglGAmeb2LR8THXIMLWCoog719n-INXu0rbzXhno-K11iOeMaND1WJ90w9EUJOU_9B6S2nC64kR2kfi1nwK6B1bnTzDesbyMEM9Y524dlxIFg3Ls3OVawSUAv6iJlIQ&gsessionid=uNDeQNVg9TdhF3dBU8A9LvA8zCkV0KwAJVZBRxpnLBdXAyPgiekqCQ)  
  <sub>Admirals, 10 hours ago</sub>  
  Exxon Mobil (XOM) explained: oil and gas production and refining, where the stock trades, recent news and the risks to know.
- [ExxonMobil Holdings (XOM) Approves Longtail Project, Is It Still 11% Below Fair Value?](https://www.google.com/goto?url=CAESwwEBxCJF1xk53awwM1ehTycJBY7OohKHk-FghPU6hZdLQVYg0wgQ48YuwyeLZO-Gg5DeEzSd-TXSh7Mz6kos2VAj46YezxThEtP6qW9-Un6qAO20GTi0lYon2QM9XgBbP78L0mz1d-XOsl06hf7LWMxHQg2SvJdSVnkdmf6rMRFHZ27EhY_QcdhHfNgKIDidPWBvEmd_zYGM1KvuLCUoVUCYojcOxmil4fchoC_SQ3oM_0Rug3g0BvFsUm7eVUT-oMQlYm0&gsessionid=uNDeQNVg9TdhF3dBU8A9LvA8zCkV0KwAJVZBRxpnLBdXAyPgiekqCQ)  
  <sub>Simply Wall St, 14 hours ago</sub>  
  ExxonMobil Holdings (XOM) has approved a final US$12.5b investment for its Longtail gas and condensate project offshore Guyana, setting up a large new phase...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 160.89 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 172.48 (-6.7%), 50d 169.50 (-5.1%), 200d 156.78 (+2.6%); 50d above 200d
Momentum: RSI(14) 36.4 | MACD -2.435 vs signal -0.902 (histogram -1.533)
Returns: 1d +0.2% | 5d -5.2% | 1m -9.7% | 3m -2.6%
52-week range: 114.51 - 187.25 (now 63.8% of the way up)
Volatility: ATR(14) 4.19 (2.6% of price) | annualised 20d 34.1%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 656.30B
Valuation: trailing P/E 16.55 | forward P/E 12.89 | P/B 2.47 | PEG 1.26
Profitability: profit margin 10.5% | operating margin 12.9% | ROE 15.5%
Growth (YoY): revenue +32.6% | earnings +111.4%
Balance sheet: debt/equity 12.6% | free cash flow 28.32B
Risk: beta 0.14 | short interest 1.2% of float
Next earnings: 2027-01-29
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-09-30 beat by 3% | 2026-06-30 in line | 2026-03-31 beat by 14% | 2025-12-31 in line
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
Consensus: buy (mean 2.42 on a 1=strong buy to 5=strong sell scale, 22 analysts)
Ratings: 3 strong buy, 6 buy, 17 hold, 0 sell, 0 strong sell
Price target: mean 184.18 (+14.5% vs last close), range 160.00 - 213.00
Recent rating changes:
  - 2026-11-12 Bernstein: main, Outperform -> Outperform
  - 2026-11-07 Freedom Broker: main, Hold -> Hold
  - 2026-11-04 Citigroup: main, Neutral -> Neutral
  - 2026-11-04 TD Cowen: main, Buy -> Buy
  - 2026-11-02 UBS: main, Buy -> Buy
  - 2026-11-02 Morgan Stanley: main, Overweight -> Overweight
Institutional ownership: 67.1%
Largest holders: Blackrock Inc. (8.1%), Vanguard Capital Management LLC (6.6%), State Street Corporation (5.2%), FMR, LLC (3.6%), Vanguard Portfolio Management LLC (2.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 10,818,651 shares in 251 transaction(s) | sold 3,904,152 shares in 49
Net: +6,914,499 shares (-265.7% of insider holdings) | insiders hold 4,323,976 shares
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

> Flat fund flows over the past week and month (0% change); no significant macro surprise (yields stable, VIX up modestly, inflation and unemployment near expectations); technical indicators show modest bearish bias but no decisive break (price below SMAs, RSI 34.9, low volume); wheat price decline noted in news but limited impact on overall fund exposure

**Main reasons it gave:**
- Flat fund flows over the past week and month (0% change)
- No significant macro surprise: yields stable, VIX up modestly, inflation and unemployment near expectations
- Technical indicators show modest bearish bias but no decisive break (price below SMAs, RSI 34.9, low volume)
- Wheat price decline noted in news but limited impact on overall fund exposure

<details><summary><b>News</b> — score +0.00</summary>

- [Wheat leads losses in U.S. grain futures, falling to lowest since January (WEAT:NYSEARCA)](https://seekingalpha.com/news/4674488-wheat-leads-u-s-grain-futures-lower-falling-to-lowest-since-january)  
  <sub>Seeking Alpha, 15 hours ago</sub>  
  CBOT December wheat futures fell $0.25 to $5.70 per bushel, the contract's lowest level since January, leading the market lower as part of a broad selloff...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 26.28 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 26.64 (-1.3%), 50d 27.70 (-5.1%), 200d 27.41 (-4.1%); 50d above 200d
Momentum: RSI(14) 34.9 | MACD -0.449 vs signal -0.478 (histogram 0.029)
Returns: 1d +1.0% | 5d -0.1% | 1m -6.5% | 3m -7.2%
52-week range: 25.44 - 29.49 (now 20.7% of the way up)
Volatility: ATR(14) 0.25 (1.0% of price) | annualised 20d 11.0%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: n/a
What it holds: P/E n/a | P/B n/a | P/S n/a | 3y earnings growth n/a
Yield: n/a
Three-year record: n/a a year | beta to the market n/a
Cost and size: expense ratio n/a | net assets n/a
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 27.60M | fund size: 725.33M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- fund equity_holdings unavailable: HTTP Error 401:
- fund bond_holdings unavailable: HTTP Error 401:
- fund bond_ratings unavailable: HTTP Error 401:
- fund fund_operations unavailable: HTTP Error 401:
- fund fund_overview unavailable: HTTP Error 401:
- fund top_holdings unavailable: HTTP Error 401:
- fund sector_weightings unavailable: HTTP Error 401:
- fund asset_classes unavailable: HTTP Error 401:

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: strong inflows (+11.9% share count in 1 month) suggest bullish sentiment, but bearish fundamentals (inventory builds and falling price outlook) offset it. Technicals show price below short‑term averages with low volume, no decisive break.

**Main reasons it gave:**
- Fund flows: +11.9% share count increase over 1 month (money coming in)
- Energy inventories: crude oil +3.4M barrels (build) and natural gas +61 BCF (build) indicating bearish supply
- EIA price outlook: WTI crude forecast down from $97 to $84 in 6 months (13% decline)
- Technicals: price below 20‑day and 50‑day SMA, RSI 27.6 (oversold), low volume (0.07× 20‑day avg)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 29.84 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 31.79 (-6.1%), 50d 32.51 (-8.2%), 200d 29.71 (+0.4%); 50d above 200d
Momentum: RSI(14) 27.6 | MACD -0.805 vs signal -0.569 (histogram -0.236)
Returns: 1d +1.1% | 5d -3.5% | 1m -10.9% | 3m -4.5%
52-week range: 22.36 - 34.10 (now 63.7% of the way up)
Volatility: ATR(14) 0.50 (1.7% of price) | annualised 20d 21.7%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.45</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.45</summary>

```text
Fund type: n/a
What it holds: P/E n/a | P/B n/a | P/S n/a | 3y earnings growth n/a
Yield: n/a
Three-year record: n/a a year | beta to the market n/a
Cost and size: expense ratio n/a | net assets n/a
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.45</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.45</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.45</summary>

```text
US inventories, week ending 2026-11-13 (published the following Wednesday)
  Crude oil: 417.8 million barrels, +3.4 on the week (a build), 25% percentile over 52 weeks
  Natural gas: 3,862.0 billion cubic feet, +61.0 on the week (a build), 94% percentile over 52 weeks -- high for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

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
Share count change: 1 week: +1.4% (25.62M) over 7d | 1 month: +11.9% (203.69M) over 34d
Shares outstanding: 64.22M | fund size: 1.92B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- fund equity_holdings unavailable: HTTP Error 401:
- fund bond_holdings unavailable: HTTP Error 401:
- fund bond_ratings unavailable: HTTP Error 401:
- fund fund_operations unavailable: HTTP Error 401:
- fund fund_overview unavailable: HTTP Error 401:
- fund top_holdings unavailable: HTTP Error 401:
- fund sector_weightings unavailable: HTTP Error 401:
- fund asset_classes unavailable: HTTP Error 401:

### Developing country bonds (EMB) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bearish technicals are offset by strong recent inflows and no macro surprise.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs, RSI 38.7 and MACD negative indicating bearish technicals
- Net inflows of +6% in the past month and +1.4% in the past week suggest demand for the ETF
- Macro data unchanged with no surprise in inflation, unemployment or Fed policy

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 90.69 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 91.64 (-1.0%), 50d 91.75 (-1.2%), 200d 94.62 (-4.1%); 50d below 200d
Momentum: RSI(14) 38.7 | MACD -0.277 vs signal -0.149 (histogram -0.127)
Returns: 1d -0.1% | 5d -0.7% | 1m -0.8% | 3m -4.2%
52-week range: 90.14 - 97.74 (now 7.3% of the way up)
Volatility: ATR(14) 0.44 (0.5% of price) | annualised 20d 7.0%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: n/a
Yield: n/a
Credit quality: n/a
Three-year record: n/a a year | beta to the market n/a
Cost and size: expense ratio n/a | net assets n/a
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.40</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +1.4% (192.01M) over 7d | 1 month: +6.0% (765.67M) over 30d
Shares outstanding: 149.72M | fund size: 13.58B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- fund equity_holdings unavailable: HTTP Error 401:
- fund bond_holdings unavailable: HTTP Error 401:
- fund bond_ratings unavailable: HTTP Error 401:
- fund fund_operations unavailable: HTTP Error 401:
- fund fund_overview unavailable: HTTP Error 401:
- fund top_holdings unavailable: HTTP Error 401:
- fund sector_weightings unavailable: HTTP Error 401:
- fund asset_classes unavailable: HTTP Error 401:

### US company bonds, riskier (HYG) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Most dimensions are neutral: macro data show no surprise, technicals are slightly bearish but not decisive, and fundamentals are unchanged. The only positive driver is modest inflow in fund shares, which is not enough to tilt the overall view.

**Main reasons it gave:**
- Fund flows: +6.0% share count over 34 days indicating modest inflow
- Technical: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 41.2; MACD below signal
- Macro: no surprise in rates or data; Treasury yields stable; VIX modestly higher

<details><summary><b>News</b> — score +0.00</summary>

- [Deutsche Bank raises 2027 dollar outlook on AI support](https://seekingalpha.com/news/4674721-deutsche-bank-raises-2027-dollar-outlook-on-ai-support?source=generic_rss)  
  <sub>Seeking Alpha, 44 minutes ago</sub>  
  Deutsche Bank raises its 2027 dollar forecasts, expecting first-half gains and only modest second-half easing, with AI spending keeping the dollar elevated.
- [Top Tokenized ETFs by Market Cap](https://www.coingecko.com/en/etfs)  
  <sub>CoinGecko, 1 hour ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...
- [(JNK) and the Role of Price-Sensitive Allocations](https://www.google.com/goto?url=CAESvgEBxCJF17MwwcFOJE9Ty1SF9GGxkrBAuspanz-nqB87cW3dC5aCgn1vxrN7XzZGBqr0ZLiLSQJdVaxTfVg3UiFNPB2VuR1r8XX-px9r3v3GNnAvq7UiCG2zGgM3stoFMLcgilTt5NsGI1qn9jMkbIfyTquHHNEOxA97zuxAoPZ50imB-HcAj6T8Dm5gcMN9nSSAAJGSF91h9gSciB9fSYYje3JdTQ1RwzpFX7H72bHadKhLQmR6Ljvi0mZdL1-x&gsessionid=Hs2vCV5Rn73YO1uIKoHE1nTqp0biiGYrijyjnJ2-vToS9AJuFXe1Ug)  
  <sub>Stock Traders Daily, 10 hours ago</sub>  
  Key findings for Spdr Bloomberg High Yield Bond Etf (NYSE: JNK). Full Alignment in Neutral Sentiment Favors Wait-and-See Approach...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 76.75 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 77.15 (-0.5%), 50d 77.40 (-0.8%), 200d 79.25 (-3.1%); 50d below 200d
Momentum: RSI(14) 41.2 | MACD -0.191 vs signal -0.152 (histogram -0.038)
Returns: 1d +0.1% | 5d -0.3% | 1m -0.3% | 3m -3.6%
52-week range: 76.63 - 81.18 (now 2.7% of the way up)
Volatility: ATR(14) 0.29 (0.4% of price) | annualised 20d 5.3%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: High Yield Bond
Yield: 6.1%
Credit quality: BB 59.6%, B 32.1%, Below B 7.2%, BBB 0.8%
Three-year record: +7.0% a year | beta to the market 0.65
Cost and size: expense ratio 0.49% | net assets 17.71B
What it is made of: Bonds 99.3%, Cash 0.5%, Preferred 0.2%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 1.1%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.6% (98.88M) over 7d | 1 month: +6.0% (1.01B) over 34d
Shares outstanding: 231.16M | fund size: 17.74B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, positioning slightly bearish but within normal range, fund inflows bullish, technicals neutral.

**Main reasons it gave:**
- Positioning: large speculators net short 37.8% of 10‑year note, slight increase (+0.3% OI) – bearish but within normal range
- Fund flows: net inflows +3.7% over past month (share count +0.7% weekly) – bullish demand
- Technical: RSI 46.4, MACD negative, price just below 20‑day SMA – neutral momentum
- Macro: 10‑year yield stable at 5.09% (down 0.01% week) and no Fed policy surprise – neutral backdrop

<details><summary><b>News</b> — score +0.00</summary>

- [Could a December Fed Increase Look Close to Certain, and What Would It Mean for iShares 7-10 Year Treasury Bond ETF (NASDAQ:IEF) Investors?](https://kalkine.com.au/news/economic-news/could-a-december-fed-increase-look-close-to-certain-and-what-would-it-mean-for-ishares-7-10-year-treasury-bond-etf-nasdaqief-investors)  
  <sub>Kalkine, 2 hours ago</sub>  
  Could a December Fed Increase Look Close to Certain, and What Would It Mean for iShares 7-10 Year Treasury Bond ETF (NASDAQ:IEF) Investors?
- [Which Pick Among the Top 4 Rate and Dollar Funds Holds the Edge for a December Fed Hike: iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT), iShares 7-10 Year Treasury Bond ETF (NASDAQ:IEF), Invesco DB US Dollar Index Bullish Fund (NYSEARC](https://kalkine.ca/news/economic-news/which-pick-among-the-top-4-rate-and-dollar-funds-holds-the-edge-for-a-december-fed-hike-ishares-20-year-treasury-bond-etf-nasdaqtlt-ishares-7-10-year-treasury-bond-etf-nasdaqief-invesco-db-us-dollar-index-bullish-fund-nysearcauup-or-ishares-1-3-year-treasury-bond-etf-nasdaqshy)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  Which Pick Among the Top 4 Rate and Dollar Funds Holds the Edge for a December Fed Hike: iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT), iShares 7-10 Year...
- [For SPDR S&P Homebuilders ETF (NYSEARCA:XHB), What Do October's Figures Show, With Starts Up 9.9% and Permits Down 7.4%?](https://www.google.com/goto?url=CAES1AEBxCJF1-96V4_jzVOAbs5GHsSTAjAiVSAxBpyQSXbldnN8qt4UwAFuTXi3W1yDZLwqYOSNFp-sOTbxSqA0x7e9u6MWsJLkHgHAlSOfzpCFG32V93mMr4ftmHCy-pAtFquKxQLTGA_eghpRWM81Ku2rhI5QPl2xCNQ5fPzbS8LlU7TUi8oHs7F4eLciXUXetzG89SlFvVYNdmrjdUQBdky3rVWf9-QCPod3LcZMPlYuRfBwR3e5GfnaP4LtqPyipxgSxdLk8XyG0e_LRqHjmqhFqsGDrg&gsessionid=t_9hqReJ32G5SNVN5jnWrYkdSz_jwcdnoy9xgnAM16NpToeLI8p5DA)  
  <sub>Kalkine, 2 hours ago</sub>  
  For SPDR S&P Homebuilders ETF (NYSEARCA:XHB), What Do October's Figures Show, With Starts Up 9.9% and Permits Down 7.4%?
- [How Could Governor Waller Half-Point Hike Call Affect iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY)?](https://www.google.com/goto?url=CAESxgEBxCJF18EyCT7wP3kY-IBDQP4H1ZCskuJEaGhR86hMqmkXNtVqDNeojjQ5M-ge6WULUKesI05BaFxV3IJ8hvib-59vSwQr68ejag5gdlHDJxXnKRvS0D6q4ju91j-g2MlXgVPZdy1-sXdrAIhQl9hX0chIBJhIaDRqWr3zfI0jhNV-nYsXM0CMapNzO2igKJz6rRa6JLcUEh0pvHeKF8kyqp3icyal9r4nAM1z02GLOXyKVrNJevbMhzI_AqqGvsfF4WMi_5c&gsessionid=t_9hqReJ32G5SNVN5jnWrYkdSz_jwcdnoy9xgnAM16NpToeLI8p5DA)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Which Signals From Jobless Claims and the Philly Fed Survey on November 19 Matter Most for iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY) Holders?](https://www.google.com/goto?url=CAES8wEBxCJF1wPikpVnIhFkROXwfeEXHDI_beZ8D2uSDm2bKPC06pUI_YHXI2GPEvWA6amvSDmnclJGy4EBbX_065Fo5umJbSVq_LKucvxT5h4-00eIEFfr9t4YHbI_1vX5d0XZ5Rfy82PBE1Ux3rEzbeZbq5gmkem0wdcw4XXuIGUASy74oJRsKuhw7wPM2T9AttOX7pdciE3qkLhpjMTCQ_HzKMcOkM16-0gvc7LVwRd9k7UB8_7nEpsQ6g4ZhJiQ5XQv5sdj9BP04MyVeqBPC8TDOJSse8jazaqhr_dQOsbdrsh9sXRKw_hHMwHnw0fEeEO6u8U&gsessionid=t_9hqReJ32G5SNVN5jnWrYkdSz_jwcdnoy9xgnAM16NpToeLI8p5DA)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  Which Signals From Jobless Claims and the Philly Fed Survey on November 19 Matter Most for iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY) Holders?
- [Should Investors Rethink iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) After Fed Minutes Leaned Toward Hikes?](https://www.google.com/goto?url=CAESzgEBxCJF1xPJz68YGrVyUtQpkbUUP4uQXVwCLvOhsXPqnY1E0cuboEtewz7bAwN29PdohQYEisA6ESExQK3j8M4VAJkKfbpVfCmLbWt9Rdu_ryCk63opGOYDbOr5x1QcIRduBoPm0OI-Rru8DVxnJApI2wo7Ketw1LKpeLexx5fEAKVYzUXMJFLo_TfeCwxQHRQyQFQLGjK4S0DzrGSLTHUWDvGn73vplzBP5gfJq6p_M-3RMCIt5ol7oWWQNp7U6plElsR_iMIPMszVL1MJIg&gsessionid=t_9hqReJ32G5SNVN5jnWrYkdSz_jwcdnoy9xgnAM16NpToeLI8p5DA)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [SPDR S&P Homebuilders ETF (NYSEARCA:XHB): What Does a 9.9% Jump in Housing Starts Alongside a 7.4% Fall in Permits Imply?](https://www.google.com/goto?url=CAES0wEBxCJF1zqepmIzMuZOx5rbdrtZkT92JEMRPefufSLuD-3P661-dQQwF4MAbxTKLeuOlr4j_f8B4sby1g4JNqpo6WHPg2Hp8nuaItpEbPCDIP7L5OD21PmMM-L_e4v-8YHCBzzFtPOi639oHZuxky_mF6e3ES1OOOz1fHIDpN8r0WilkTI2_-l5aIv-HTLeG8eR0Uo6xRpaVQP7-iDGPdfxWMOdojPb8_6fo3ZDsv4pFzsOtRsFYXqWiUyL6o7adK2U3y2K6zJz2rFG11Fm0epLf3fP&gsessionid=t_9hqReJ32G5SNVN5jnWrYkdSz_jwcdnoy9xgnAM16NpToeLI8p5DA)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  SPDR S&P Homebuilders ETF (NYSEARCA:XHB): What Does a 9.9% Jump in Housing Starts Alongside a 7.4% Fall in Permits Imply?
- [What Could a 5.07% 10-Year Yield Paired With a 5.41% 30-Year Yield Signal for iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT)?](https://www.google.com/goto?url=CAES2QEBxCJF1zgASnDG9cujnsP7vF_WgjMilB0Fc_vUu7CcnvoFcsRMRpGigxxL9ct2_U4YWRgFMcY-CP1jreoc7BM8QfW--FhqTmEoPW2bwZJyhdpxyPYuOdt33lqd02wqPPa37yIw9bCWKJWOCfdkvhBLGSpF6zrhd58TleNolEhKe_gOtDLV5ONeWjeX5ZTtfzrBQxXdD9l8a-J2RFFv6R6__ercapPDx5V1SKDQddATp29LcovhkuYA-qR4PPIbkqmdpOfdbQGtM0DzXqvXwk6IS8XscB0IIXXX&gsessionid=t_9hqReJ32G5SNVN5jnWrYkdSz_jwcdnoy9xgnAM16NpToeLI8p5DA)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  What Could a 5.07% 10-Year Yield Paired With a 5.41% 30-Year Yield Signal for iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT)?
- [Which of the Top 3 Overseas Funds Faces the Stiffest Test From Inflation and Rate Hikes: iShares MSCI Indonesia ETF (NASDAQ:EIDO), iShares MSCI Eurozone ETF (CBOE:EZU) or iShares MSCI United Kingdom ETF (NYSEARCA:EWU)?](https://www.google.com/goto?url=CAESsgIBxCJF15aaLrt4yMFhPcU1h3QtNVTNka5pxn6sUahyUcuV85H81SRwjwdHgoMyF57UZstJ12vNVow8FtsGBdCCXZrv_M8GTFOkoyfiLM1LXy-HXpv_kmR9q6wvnZ_O1FZdi4LAVz-nfvebfFm3Caug2ckNhivYzclRio8I0PDOzyS5HehY2YaG02tJJhyJxhwmYjQHDC8UP8Ktqlsw1DC3xUV4tE0K5-6QnP-R0IOVdmainzh2rqx3Jtm3QVmIrI3f68r6RT2NSRLJGz9ZGMfjl6J0IEDmRM469eCZ3qwLRVyFrq8HrBiCWomoSQE9ppOfoJwpE2r_tXdkqLBEMSvEEy2OZ33F9tj2D9w69XTtsiuV4CtLQS33PSAxVVAbUGG7OOu29aQi1tqk5WAYsu4pAFg&gsessionid=t_9hqReJ32G5SNVN5jnWrYkdSz_jwcdnoy9xgnAM16NpToeLI8p5DA)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  Which of the Top 3 Overseas Funds Faces the Stiffest Test From Inflation and Rate Hikes: iShares MSCI Indonesia ETF (NASDAQ:EIDO), iShares MSCI Eurozone ETF...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 90.51 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 91.06 (-0.6%), 50d 90.45 (+0.1%), 200d 93.52 (-3.2%); 50d below 200d
Momentum: RSI(14) 46.4 | MACD -0.051 vs signal 0.068 (histogram -0.118)
Returns: 1d -0.2% | 5d +0.3% | 1m +0.3% | 3m -2.5%
52-week range: 88.92 - 97.99 (now 17.6% of the way up)
Volatility: ATR(14) 0.45 (0.5% of price) | annualised 20d 6.2%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Long Government
Yield: 4.0%
Credit quality: AA 100.0% | US government debt 99.6%
Three-year record: +3.0% a year | beta to the market 1.17
Cost and size: expense ratio 0.15% | net assets 43.53B
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 37.8% of open interest (6,095,194 contracts)
Change on the week: +0.3% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.7% (288.18M) over 7d | 1 month: +3.7% (1.56B) over 34d
Shares outstanding: 481.48M | fund size: 43.58B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Technical: price below 20‑day, 50‑day and 200‑day SMAs
- Insider: large speculators net short 10.1% and short position rose 2.2% week over week
- Analyst: 100% buy rating on top holdings covering only 1.9% of fund weight
- Macro: VIX up 3.8 points and yields slightly higher, no surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Which of Five Index Funds Held Its Footing Best as the S&P 500 Slid for a Fifth Session: SPDR Dow Jones Industrial Average ETF Trust (NYSEARCA:DIA), Invesco QQQ Trust (NASDAQ:QQQ), iShares Russell 2000 ETF (NYSEARCA:IWM), Invesco S&P 500 E](https://kalkine.ca/by-topic/mutual-funds-etfs/which-of-five-index-funds-held-its-footing-best-as-the-sp-500-slid-for-a-fifth-session-spdr-dow-jones-industrial-average-etf-trust-nysearcadia-invesco-qqq-trust-nasdaqqqq-ishares-russell-2000-etf-nysearcaiwm-invesco-sp-500-equal-weight-etf-nysearcarsp-and-spdr-sp-500-etf-trust-nysearcaspy)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  Which of Five Index Funds Held Its Footing Best as the S&P 500 Slid for a Fifth Session: SPDR Dow Jones Industrial Average ETF Trust (NYSEARCA:DIA),...
- [What Lifted Smaller Companies Even as the Dow Dropped 561 Points, and What Does It Mean for iShares Russell 2000 ETF (NYSEARCA:IWM)?](https://kalkine.ca/by-topic/mutual-funds-etfs/what-lifted-smaller-companies-even-as-the-dow-dropped-561-points-and-what-does-it-mean-for-ishares-russell-2000-etf-nysearcaiwm)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  What Lifted Smaller Companies Even as the Dow Dropped 561 Points, and What Does It Mean for iShares Russell 2000 ETF (NYSEARCA:IWM)?
- [iShares Russell 2000 ETF (IWM) Price Prediction: Small-cap ETF trades below key moving averages as momentum stays soft](https://www.google.com/goto?url=CAESlgEBxCJF12YQJU71Yr9SvtbKV7RIPUQD60OJuhWqen4qhtEK-CAcIc9sfCsuZwKTfNun4abaespMva7nlyEIpYrFPQ8M6-HCpqypKPoVy04KbId3aODLDJbEPI9wYf6c5pJJti2Y9G96QkSMXRGuH2zgwwH9NQD_w6vIWY7pYFUIbliY6DYaifPkpkvJ1xR2pnwfG1M9-Bk&gsessionid=8kHzZNSsguuVAnEilqvSVdWaFQC32_wct-H-FFjbLFFyq3ZC5IUKkQ)  
  <sub>Blockchain News, 21 hours ago</sub>  
  iShares Russell 2000 ETF (IWM) is trading at $269.55, down 0.78% on the latest reading, with price sitting below the 7-day, 20-day and 50-day moving...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 269.43 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 277.44 (-2.9%), 50d 279.01 (-3.4%), 200d 279.59 (-3.6%); 50d below 200d
Momentum: RSI(14) 40.0 | MACD -2.188 vs signal -1.241 (histogram -0.947)
Returns: 1d -0.3% | 5d -3.2% | 1m -2.5% | 3m -10.2%
52-week range: 229.11 - 305.09 (now 53.1% of the way up)
Volatility: ATR(14) 4.73 (1.8% of price) | annualised 20d 25.5%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Small Blend
What it holds: P/E 16.28 | P/B 1.99 | P/S 1.23 | 3y earnings growth n/a
Yield: 1.0%
Three-year record: +16.0% a year | beta to the market 1.26
Cost and size: expense ratio 0.19% | net assets 75.49B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Glaukos Corp 0.5%, BrightSpring Health Services Inc 0.4%, JFrog Ltd Ordinary Shares 0.3%, Twist Bioscience Corp 0.3%, Moog Inc Class A 0.3%
Sector mix: Healthcare 21.0%, Financial services 18.2%, Technology 14.0%, Industrials 12.7%
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

<details><summary><b>What analysts and big funds say</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.10</summary>

```text
Rolled up from the 5 largest holdings, 1.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.45 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.0% above the current prices
Holdings read: GKOS, BTSG, FROG, TWST, MOG-A
Recent rating changes among them:
  - GKOS: 2026-10-29 HC Wainwright & Co.: main, Buy -> Buy
  - BTSG: 2026-11-03 Guggenheim: main, Buy -> Buy
  - FROG: 2026-11-12 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MOG-A: 2026-10-13 JP Morgan: main, Overweight -> Overweight
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 10.1% of open interest (440,576 contracts)
Change on the week: +2.2% of open interest
Crowding: 77% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 281.05M | fund size: 75.72B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as technicals are bearish while fund flows are strongly positive and fundamentals are solid, with no macro surprise or decisive technical break on heavy volume.

**Main reasons it gave:**
- Monthly inflows +12.9% (304M shares) indicating strong demand
- Price below 20d, 50d, and 200d SMAs; negative MACD and RSI 43.9 showing bearish technicals
- Yield curve normal but market pricing ~4 quarter-point Fed hikes over next 2 years
- No macro surprise: Fed target unchanged, data in line with expectations

<details><summary><b>News</b> — score +0.00</summary>

- [Behavioral Patterns of LQD and Institutional Flows](https://news.stocktradersdaily.com/news_release/43/Behavioral_Patterns_of_LQD_and_Institutional_Flows_111926060402_1795086242.html)  
  <sub>Stock Traders Daily, 9 hours ago</sub>  
  Price-action only: Ishares Iboxx Usd Investment Grade Corporate Bond Etf (LQD) movements set the tone for institutional models. Behavioral Patterns of LQD...
- [Deutsche Bank raises 2027 dollar outlook on AI support](https://seekingalpha.com/news/4674721-deutsche-bank-raises-2027-dollar-outlook-on-ai-support?source=generic_rss)  
  <sub>Seeking Alpha, 43 minutes ago</sub>  
  Deutsche Bank raises its 2027 dollar forecasts, expecting first-half gains and only modest second-half easing, with AI spending keeping the dollar elevated.
- [Treasuries rally for a third day as stocks slip and oil falls](https://www.google.com/goto?url=CAESuAEBxCJF10PsG0ihz-cw32aEhyD1-rpb-rduv5xY6boIOJOlqqEZWrfm0n0FqQXDep4hgyYdhdsibOksfH3gmiSyjYzkDmNXDggzZ1ICKm5zTW0y9kG3VTsnDF7mzCQxcjuynbas27yYgGtrPeODlX0hmfR5NCbFv3mUyz7OJOuCwTJ2LcfPVquQNG1VcBehgFYxAbupLC14-yi-dc6VorON7lDoDpVcEqI6Z3l92wx7_PYlSAEv1GOV&gsessionid=Wy1N1MU78fiYfCzTyiOncAWfe8FINGGZNax3f5GtkozLvpbrGibH9A)  
  <sub>Investing.com, 22 hours ago</sub>  
  Investing.com -- Treasuries rose for a third day as stocks slipped and oil fell. Bloomberg says traders also see much of the Fed's expected tightening as...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 103.11 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 103.80 (-0.7%), 50d 103.48 (-0.4%), 200d 107.20 (-3.8%); 50d below 200d
Momentum: RSI(14) 43.9 | MACD -0.172 vs signal -0.037 (histogram -0.135)
Returns: 1d -0.0% | 5d +0.1% | 1m -0.1% | 3m -2.7%
52-week range: 101.83 - 112.05 (now 12.5% of the way up)
Volatility: ATR(14) 0.53 (0.5% of price) | annualised 20d 6.0%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Corporate Bond
Yield: 4.8%
Credit quality: A 46.4%, BBB 40.8%, AA 11.7%, AAA 1.2%
Three-year record: +4.1% a year | beta to the market 1.32
Cost and size: expense ratio 0.14% | net assets 32.00B
What it is made of: Bonds 99.2%, Cash 0.8%, Convertible 0.0%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 0.5%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.40</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +1.0% (304.17M) over 7d | 1 month: +12.9% (3.66B) over 34d
Shares outstanding: 311.32M | fund size: 32.10B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: Fed policy unchanged, yields stable, VIX modestly higher
- Technical mix: price below 20‑day SMA, MACD negative, but above 200‑day SMA
- Insider positioning: net short 15% of open interest, increased 3.7% week‑over‑week
- Analyst coverage thin (1.4% weight) with modest buy bias (+1.5% price target)

<details><summary><b>News</b> — score +0.00</summary>

- [Which of Five Index Funds Held Its Footing Best as the S&P 500 Slid for a Fifth Session: SPDR Dow Jones Industrial Average ETF Trust (NYSEARCA:DIA), Invesco QQQ Trust (NASDAQ:QQQ), iShares Russell 2000 ETF (NYSEARCA:IWM), Invesco S&P 500 E](https://kalkine.ca/by-topic/mutual-funds-etfs/which-of-five-index-funds-held-its-footing-best-as-the-sp-500-slid-for-a-fifth-session-spdr-dow-jones-industrial-average-etf-trust-nysearcadia-invesco-qqq-trust-nasdaqqqq-ishares-russell-2000-etf-nysearcaiwm-invesco-sp-500-equal-weight-etf-nysearcarsp-and-spdr-sp-500-etf-trust-nysearcaspy)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  Which of Five Index Funds Held Its Footing Best as the S&P 500 Slid for a Fifth Session: SPDR Dow Jones Industrial Average ETF Trust (NYSEARCA:DIA),...
- [GSEW: A Lower-Cost Alternative To RSP That's Worth Considering](https://seekingalpha.com/article/4969770-gsew-lower-cost-alternative-to-rsp-thats-worth-considering)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  The Goldman Sachs Equal Weight US Large Cap Equity ETF holds 500 of the largest U.S. securities in equal weight. It's about 80-85% similar to RSP.
- [Why Did the Equal-Weight S&P 500 (NYSEARCA:RSP) Outperform the Standard Benchmark during the November 18 Session?](https://www.google.com/goto?url=CAES2AEBxCJF14fG1kGSr41RqmXJel2e7IjIMgEtHjFTlWw9NDPoIMoMZjGywTrc_CcmDdagRLVxbjv3VcMBr5DBN-BpUjizWEc20zOPrOlAzPLstP6gjgWA_P0tWb9Ztzyr1GWHUasKJgLXdNJG6G6Ngp37xWMqSkwty0ouJEVwaSFXOpMlM3k9RS4xb9V_l-mtit99_Fa9KqeJMEsMmgxiXXooWxfc_A-8jEYAfWv75hhw8lzJqqG2hnotQW5jDj7hjYAPSQdXGsvNxQjmkkp4mpAgug-s9Z7LC1U&gsessionid=whX0mW7rQ5kRmu5EBvuPZSiKsYDl2Bpw3bXGmEjvZX8jeaAUYz545g)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  Why Did the Equal-Weight S&P 500 (NYSEARCA:RSP) Outperform the Standard Benchmark during the November 18 Session?
- [NVR, Inc. (NVR) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXX9rURLlXXEcC6Av_oszuCWlaGjeRidaJY-pUcDQZHtOe9b8BfWgwPe444pjdSE4rLzLouxT80vWsOjtrOa4WydcKNzp8FWh_bUkd_xC4a8EdDWRpXLZbyo9emWzHX1AA&gsessionid=whX0mW7rQ5kRmu5EBvuPZSiKsYDl2Bpw3bXGmEjvZX8jeaAUYz545g)  
  <sub>Yahoo Finance Australia, 5 hours ago</sub>  
  Find the latest NVR, Inc. (NVR) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Fund Managers Dump Tech Stocks at Fastest Pace Since 2006 - State Street Technology Select Sector SPDR ET](https://www.google.com/goto?url=CAESoAEBxCJF15BgpfMXNAG_eRLMTHHkatb5BOnf8ILMkcDACRW5yUYn5-_ZuN7-UhPEpKtOcnqEgB9pT6xjtkkDC_fgc8h_9snl8P_PGktoDom_nzc2fGn3poDLZtPNjfWjtZ6ijpo89O6zuK9IP3VT7t2ZFLB8VJ7ollOv7MxFOq52zZ1uH43ZOEJy1-LkwZUwSjQEMYk0tlnQ8mVpNJJ7UApU&gsessionid=whX0mW7rQ5kRmu5EBvuPZSiKsYDl2Bpw3bXGmEjvZX8jeaAUYz545g)  
  <sub>Benzinga, 23 hours ago</sub>  
  Fund managers cut tech by the most since 2006 on AI capex fears, Bank of America says, as XLK nears a bear market. The buy signal hasn't come.
- [How Is SPDR S&P 500 ETF Trust (NYSEARCA:SPY) Holding Up as the S&P 500 Logs Its Five-Day Slide?](https://www.google.com/goto?url=CAESxQEBxCJF1znYCavUJtKuKJyQGtau-s1x7xJ2EjY4ILTDLgEsxqo2hvy-0ApwGRAv3p4BshhOtlw9rEtDEcPX2UkrPXqZFpnC3X3dE8_fHPk-O1r2xyWH9dGDf4UZFL-2cKRGZyk6lBn8RIu2CE8cTpNBCxTpHC9nWfIXl6X1YwOJ3tirPuLyWSKAFkGz-fBXbQJDtS406lDq-3tivpzkzCJf2OO7kNW9xRGXg9VPWEIDZbj2xp1VtkIYCi0tyTO8hLM5FRjXzA&gsessionid=whX0mW7rQ5kRmu5EBvuPZSiKsYDl2Bpw3bXGmEjvZX8jeaAUYz545g)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 215.23 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 218.72 (-1.6%), 50d 215.02 (+0.1%), 200d 209.20 (+2.9%); 50d above 200d
Momentum: RSI(14) 44.6 | MACD 0.451 vs signal 1.175 (histogram -0.724)
Returns: 1d -0.1% | 5d -2.5% | 1m -0.7% | 3m -2.9%
52-week range: 182.18 - 223.33 (now 80.3% of the way up)
Volatility: ATR(14) 2.65 (1.2% of price) | annualised 20d 18.2%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Large Blend
What it holds: P/E 19.93 | P/B 2.93 | P/S 1.83 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +15.9% a year | beta to the market 0.80
Cost and size: expense ratio 0.20% | net assets 100.66B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Moderna Inc 0.3%, PTC Inc 0.3%, Accenture PLC Class A 0.3%, Gartner Inc 0.3%, Hasbro Inc 0.3%
Sector mix: Technology 16.9%, Industrials 15.1%, Financial services 13.9%, Healthcare 12.9%
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

<details><summary><b>What analysts and big funds say</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.10</summary>

```text
Rolled up from the 5 largest holdings, 1.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 38.4% | hold 61.6% | sell 0.0% (mean 2.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +1.5% above the current prices
Holdings read: MRNA, PTC, ACN, IT, HAS
Recent rating changes among them:
  - MRNA: 2026-11-09 Goldman Sachs: main, Neutral -> Neutral
  - PTC: 2026-11-12 Wolfe Research: down, Outperform -> Peer Perform
  - ACN: 2026-10-26 Wells Fargo: main, Equal-Weight -> Equal-Weight
  - IT: 2026-11-06 Barclays: down, Equal-Weight -> Underweight
  - HAS: 2026-10-28 UBS: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 15.0% of open interest (2,017,687 contracts)
Change on the week: +3.7% of open interest
Crowding: 88% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +2.4% (2.32B) over 7d | 1 month: +3.6% (3.49B) over 34d
Shares outstanding: 466.56M | fund size: 100.42B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Net short 33.5% of open interest with minimal weekly change (-1% of OI) indicating no strong positioning shift
- Yield curve unchanged and no policy surprise; yields stable with slight weekly moves
- Technical indicators near neutral (RSI 46.2, MACD near zero, price slightly below 20‑day SMA)
- Fund flows flat week‑over‑week (+0.0% share count) indicating no significant demand shift

<details><summary><b>News</b> — score +0.00</summary>

- [Ahead of November 19, what should holders of iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY) focus on in jobless claims and the Philly Fed survey?](https://kalkine.com.au/news/economic-news/ahead-of-november-19-what-should-holders-of-ishares-1-3-year-treasury-bond-etf-nasdaqshy-focus-on-in-jobless-claims-and-the-philly-fed-survey)  
  <sub>Kalkine, 2 hours ago</sub>  
  Ahead of November 19, what should holders of iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY) focus on in jobless claims and the Philly Fed survey?
- [How Could Governor Waller Half-Point Hike Call Affect iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY)?](https://kalkine.ca/news/economic-news/how-could-governor-waller-half-point-hike-call-affect-ishares-1-3-year-treasury-bond-etf-nasdaqshy)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  How Could Governor Waller Half-Point Hike Call Affect iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY)?
- [What Would Governor Waller Half-Point Call Bearing on iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY)?](https://www.google.com/goto?url=CAESygEBxCJF1wyq0Iyo-NTwCG1vKt49qoaNw0mB4etnLSbRB8-TlvEFH7pnro2fPxRFdbHR9SwKYBmyYXjvZ-a8nAZMvVckSkuCEp45PblCtQk7-OHxRz0EKb3RWxUhZO-WHaFEYRwN9ZOP9OGLVSLYrsbAH_LiYvdm2mtOGGmTGVqMAGSSv8O9jZQ9p9c1bweTlq3jdvKw2MUWFdc9Ncl68_TXTZb_jgGA6rQPPgGpaeJWQ3qxgkf80cMnJTRgWupdDM-ZlCWZgs0I7WjC&gsessionid=nXEpv1a7THQL1thb3co3s1gDFhwLFl1Y7x-6VzKfE9DyhHfxrZDYyg)  
  <sub>Kalkine, 2 hours ago</sub>  
  What Would Governor Waller Half-Point Call Bearing on iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY)?
- [Which Signals From Jobless Claims and the Philly Fed Survey on November 19 Matter Most for iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY) Holders?](https://www.google.com/goto?url=CAES8wEBxCJF16kBp9ZcFolrp7vHPczJsvnqpZSZCq7-737mNLNUim2e9Cdv7fR1mGXn1Yv5mQh3us7wQWwDKFf5V3cA07v317XU1MreH5Ze43dEe1fFiIpuo4v9jEfJnStlIfcXqihSQ7Njjq7xq9Z1hu5YeUTGfbvqXsgtPDo-CuJd6IDswR9nNtj7Ur5Af5miUWstZN_bwHegGfNG8B07wm6AdLUKmf0sXZjN-hmUEKBs6UoZKEh95cYo85CMhEdNPySLJu3yxL_-YP9kWHXlLT3genS2WHxeSWlWBbbPK5gqhJVxkEzcrIKhLEnWcNZ664YrWNc&gsessionid=nXEpv1a7THQL1thb3co3s1gDFhwLFl1Y7x-6VzKfE9DyhHfxrZDYyg)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  Which Signals From Jobless Claims and the Philly Fed Survey on November 19 Matter Most for iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY) Holders?
- [iShares 20+ Year Treasury Bond ETF (TLT) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZAHEIkXXAhmrg4OsNugAUqExhsiNsrB13OMfIs1fO1EijIg-uM1ol_rH-SGf9c5iL8RcY-zNt8BzH_evGrXZI-DF7qeflQG_4Rg1PsTwh9q6tvhCbjtIHMAP0m4SVYz0Qop7TaE&gsessionid=nXEpv1a7THQL1thb3co3s1gDFhwLFl1Y7x-6VzKfE9DyhHfxrZDYyg)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Find the latest iShares 20+ Year Treasury Bond ETF (TLT) stock quote, history, news and other vital information to help you with your stock trading and...
- [Which Pick Among the Top 4 Rate and Dollar Funds Holds the Edge for a December Fed Hike: iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT), iShares 7-10 Year Treasury Bond ETF (NASDAQ:IEF), Invesco DB US Dollar Index Bullish Fund (NYSEARC](https://www.google.com/goto?url=CAES-QIBxCJF1xGCq-pGNulB2Wdp5zdwtUhyPH6ZV3Zqbq1q-6YOZsnt-GYgyK_2vTN8nbNDzd4mx4e5dxlU461nmVB49D_TMwt7jqhPdh768o9N9EvZW6ksPujci0xhw_gc1IALXVrY7J_WQFmbu1hkGlBCnxNUJ8EjCzaPz3fmlRLi-37jlrEQpy7o-qwPF9exPJbRynAbbKrnl0c50IMqnQcXO-GiFGbQTRrhqpDYFx9psa2MYy0kVdqpg8P6AhHVBYp9iWVK66H082xc1p4zDSQWyhEqVSVnimm6mwoiU3GUnHLyljPon6upHvu7FBWQJIuUqdGM5wHxwa2ER_OSRSN1wwHQPxhmF-zddjtRft61psEuYUdInkrhYA7zrGpJtkyAK1s3qU8DK2DgI0gHXJVLPXhE21W7kmkDE5EWVho-0ZxyJqmx_quzgnTJk6p9oaXlt5Tjj8ELIev4scTPWXxLQo2UCmRMqyQG4LXenost8T7g7Q5QucDi-w&gsessionid=nXEpv1a7THQL1thb3co3s1gDFhwLFl1Y7x-6VzKfE9DyhHfxrZDYyg)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  Which Pick Among the Top 4 Rate and Dollar Funds Holds the Edge for a December Fed Hike: iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT), iShares 7-10 Year...
- [Should Holders of iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) Be Concerned by a 5.07% Ten Year and 5.41% Thirty Year Yield?](https://www.google.com/goto?url=CAES3gEBxCJF15xxkwDp_47G5C4vTp5vaUskBPyxfjj6CxnKmQvXuDyAdVpu-OLfcfYWGsWqwLGu69hVZDooHk656d0XoOpIvBxprTl8NbWQTWAls6sxLl3lwCpX9k07mT1UrUMypIcYINiZuZaoxbmMZ49Atn8u219VeMBKqWMgUDiMSH_W3SHNwXK5TO0-4ogWa0y1RnG56SBGnP5Go0jvMDDfeJCGb6MRzY0NBcwMzDd5RFV563T38MXfBybbM8tf12gf_vXncn0iesTfaR3Y-Ma5YlKCFbNsX0EedTf4DkY&gsessionid=nXEpv1a7THQL1thb3co3s1gDFhwLFl1Y7x-6VzKfE9DyhHfxrZDYyg)  
  <sub>Kalkine, 2 hours ago</sub>  
  Should Holders of iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) Be Concerned by a 5.07% Ten Year and 5.41% Thirty Year Yield?
- [For SPDR S&P Homebuilders ETF (NYSEARCA:XHB), What Do October's Figures Show, With Starts Up 9.9% and Permits Down 7.4%?](https://www.google.com/goto?url=CAES1AEBxCJF10Chg_5yP9YT86HIvSKrVGQ4zCi2u-fPyWCMpQHx9tdEDzHRwJwls7utl9gDBTtjimmaWZo3AMNUo0ab9cyvHN20l9XkmVJ_5FubLrX_LjF5QpLztD1C5sGBJA0qnkLjS00c_i29U7PWb37cGwVKf5ETJULDURmzdhD5ddAc7zc5Ncs980ZqsUVkivnzFiBH_Xitglf4FXkpCxuj0B6XlMXeRPsv30vrFjNiJembnHOj7SYS996j3fSmH6i1Zizv-RSEpgTY6XhuO20fbR9alw&gsessionid=nXEpv1a7THQL1thb3co3s1gDFhwLFl1Y7x-6VzKfE9DyhHfxrZDYyg)  
  <sub>Kalkine, 2 hours ago</sub>  
  For SPDR S&P Homebuilders ETF (NYSEARCA:XHB), What Do October's Figures Show, With Starts Up 9.9% and Permits Down 7.4%?
- [Should Investors Rethink iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) After Fed Minutes Leaned Toward Hikes?](https://www.google.com/goto?url=CAESzgEBxCJF12yIXRXPsbiHHSlqu0nXen0ov9D_0O7XsMYkn2vaWE4R3Wl-9qRzQ-pE3m1XavZhkOtz0bGvIQafo-jn7_88SkySaMe3mrWLLn1_mMgGTf_GW-zDjFVkk7JVDuJ4HSd5TvPLoQs07zLFbIyt96bIU4_WN_EEgUQSurHORVThxfCxNE8n5mqPYar96W8IoXwRMxH6uXq84XnQBEEm8lXg513oBa8NN_lvfw-1S2lJvWQRL2NtG2-w5NqEOSfhfjFKHzlg9ux5JGEIgQ&gsessionid=nXEpv1a7THQL1thb3co3s1gDFhwLFl1Y7x-6VzKfE9DyhHfxrZDYyg)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [How Could a 91% Chance of a December Fed Hike Reshape Returns on iShares 7-10 Year Treasury Bond ETF (NASDAQ:IEF)?](https://www.google.com/goto?url=CAES0QEBxCJF1_x7CbXTDKCuHPWSZAYTo7ytSQoE_N80JFZQ_BsFoRqNu1IwUG9ULTCi75o6cY1n7DFzuqh9ScozPWK5SkqbQ2QMsLA-MdBgxmeQN-vLfuryMGs0sW4y1c8fKx1B3P9FFL6ql8SPSOzrhy4yYz7n596JZyvZ0ZsqVuN7gM00-si-70VgHZCi1TMP6DjSBah2hbGnLcjbAduS3BYTILDChk7-Cp8Vyh5991lTs6W29ksYqekrBqKSeCwo8tm8wjq3AjWkJWXuPzkQHhZOXg&gsessionid=nXEpv1a7THQL1thb3co3s1gDFhwLFl1Y7x-6VzKfE9DyhHfxrZDYyg)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  How Could a 91% Chance of a December Fed Hike Reshape Returns on iShares 7-10 Year Treasury Bond ETF (NASDAQ:IEF)?

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.29 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 81.43 (-0.2%), 50d 81.31 (-0.0%), 200d 82.01 (-0.9%); 50d below 200d
Momentum: RSI(14) 46.2 | MACD -0.028 vs signal -0.005 (histogram -0.024)
Returns: 1d -0.1% | 5d +0.2% | 1m +0.0% | 3m -0.9%
52-week range: 81.05 - 83.18 (now 11.3% of the way up)
Volatility: ATR(14) 0.12 (0.2% of price) | annualised 20d 2.2%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Short Government
Yield: 3.6%
Credit quality: AA 100.0% | US government debt 99.8%
Three-year record: +3.9% a year | beta to the market 0.25
Cost and size: expense ratio 0.15% | net assets 27.44B
What it is made of: Bonds 99.8%, Cash 0.2%
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
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 33.5% of open interest (4,489,282 contracts)
Change on the week: -1.0% of open interest
Crowding: 77% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.0% (3.60M) over 7d | 1 month: +4.2% (1.12B) over 34d
Shares outstanding: 337.45M | fund size: 27.43B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals weak but no decisive break, positioning neutral, fundamentals unchanged.

**Main reasons it gave:**
- Fed's Waller warned of inflation shock and potential 50bp rate hike
- Technicals: price below 20d, 50d, 200d SMAs; RSI 40.7; MACD negative; volume 0.06x 20‑day average
- Large speculators net short 37.8% of open interest, change +0.3% OI (week)
- Fund flows: net inflows +0.4% weekly, +2.7% monthly

<details><summary><b>News</b> — score +0.00</summary>

- [iShares TIPS Bond ETF (TIP) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TIP/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  iShares TIPS Bond ETF (TIP) · -0.34% · -0.61% · -5.05% · -4.56% · -5.37% · -19.67% · 3.35%. Key Events. Baseline.
- [Fed’s Waller Warns of an Inflation Shock. 3 TIPS ETFs Investors Should Watch - iShares TIPS Bond ETF (ARC](https://www.benzinga.com/etfs/specialty-etfs/26/11/63409365/wallers-rate-hike-warning-puts-3-tips-etfs-inflation-protection-to-the-test)  
  <sub>Benzinga, 19 hours ago</sub>  
  Waller's 50-basis-point rate hike warning puts TIPS ETFs in focus as investors weigh inflation protection against rising real yields.
- [Anthropic Leveraged ETF Race Heats Up Even Before Stock’s Debut](https://www.google.com/goto?url=CAESwQEBxCJF13_EPhAi6Z5KxX_4-eeoxYC062rrbio3pdV-Ypp94un3Tnuk54Qp5g5q3XXOA6V3_fNtFczBa7XvC97CzeuKLWuwIMcnRJpsYyT0JDQ0E67qPYIL4hn7ZMxAUTeKKvgJcZ9fl7qYslHSGMl3QeyHWSK5zMtMce7IKup-f_L_14rc9qQKuKY3LXMfGZyH1npAnro-2dc9IAq7O-AiIxwIMSV95r5KkN0zb61Mp5hd0McIr3kWjHoT4WxX1T6y&gsessionid=AADE34lkfm4Qrize66EF_N8q6CKGZDJUwikFMxaENeTPC93O7Y6HKQ)  
  <sub>Bloomberg.com, 19 hours ago</sub>  
  A slew of leveraged ETFs tied to SpaceX launched soon after its public debut, but only one managed to attract meaningful assets. That experience has raised...
- [PIMCO 1-5 Year US TIPS ETF (STPZ) Seasonal returns chart](https://www.google.com/goto?url=CAEScQHEIkXXuHf_Ojh2qPQcdZ7eZk_iFR5j2Ytzr6awEFDjGG_Tn8GRqUEooC4ZdUB4u5yzcuXn2RcOqMZABHhPeynazzTvg3R-jLUS3Bis8A1pIq4-rUysz0ewflOCAvoZLyo1SDXTiFsHOSDzikYBeSkB&gsessionid=AADE34lkfm4Qrize66EF_N8q6CKGZDJUwikFMxaENeTPC93O7Y6HKQ)  
  <sub>Yahoo Finance UK, 18 hours ago</sub>  
  PIMCO 1-5 Year US TIPS ETF (STPZ) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [iShares USD TIPS UCITS ETF (TPSAA.XD) company profile and facts](https://www.google.com/goto?url=CAEScQHEIkXX1Fve8B7vaF9rl_pLrqqjN4MHi5lfHFqIumXM5jl-zTJCIASItTMaRxTwKg5jOnXJ7QmEgviuBketdFP6VaMTYOqqd_GsVeW4V8F6nT30b8uabCnEJ26-QwbLGH3aaZo4hTIPM3vY5tJGmC1V&gsessionid=AADE34lkfm4Qrize66EF_N8q6CKGZDJUwikFMxaENeTPC93O7Y6HKQ)  
  <sub>Yahoo Finance UK, 19 hours ago</sub>  
  See the company profile for iShares USD TIPS UCITS ETF (TPSAA.XD), including business summary, industry/sector information, number of employees,...
- [iShares USD TIPS UCITS ETF (TPSAA.XD) performance history](https://www.google.com/goto?url=CAESdQHEIkXXcJWFN_BYKS1a0xufx_Yf7E-eNS2YLkOy-5MDhJu0sPtbzf_yvsokWLSguGR9q2J3SyXtkVQf94NddSMaGyEvdO0gZ4SP7L_DgckerQErDySVGonurwZm8Mj8e_Y_LChnXp6LgFXfcU7JPz2PGjF8Xg&gsessionid=AADE34lkfm4Qrize66EF_N8q6CKGZDJUwikFMxaENeTPC93O7Y6HKQ)  
  <sub>Yahoo Finance UK, 24 hours ago</sub>  
  iShares USD TIPS UCITS ETF (TPSAA.XD). 223.86 0.00 (0.00%). As of 12 October at 17:10:39 CEST. Market open. Trailing returns (%) vs. Benchmarks.
- [Solana ETF Draws Fresh $1.3 Million as Token Momentum Stays Muted](https://www.google.com/goto?url=CAESrAEBxCJF17Wbv_Nv_rbfvHf2lcv6GFT_qywlJHYNtRhuGjdexDovsJcmtPDJ3MQcbuSxv_rlxDTY73xDenPjsOQiKip8oBwkUvr_zbGxBMicKKAEFGmpwkmptuml5Tr4jIK_mxsDcBUqth_Sci274tQQA1XKECR38eZby0XJY9UBTvr4YwKT_NbRescXCKes0bcgEMATHTogX81W-HDCM75GQLkxWeMgfpDHOyRf&gsessionid=AADE34lkfm4Qrize66EF_N8q6CKGZDJUwikFMxaENeTPC93O7Y6HKQ)  
  <sub>TipRanks, 1 hour ago</sub>  
  The 2x Solana ETF, SOLT, recorded a $1.30 million net inflow on November 17, 2026. The move represented 1.53% of the fund's $85.12 million in assets under...
- [Investors Chase Yield in NEOS Ethereum High Income ETF Despite Ether Slump](https://www.google.com/goto?url=CAEStgEBxCJF11E2eglus18dx5FXpVDXX828zNCDphJZKECFKZFPqkcu4be06cteKyvest3xXMwVEGWbuahJzwNPbxCUNBtX9x7Ky5nBWB5H5HQBsVvXIlQHGSWd2qdIDzPVff0jP8HeSPy0Ziu50p3eIoFRRas9DyoFfB8swwn5mW3KzbDy2mi6wOlM67PwtTDrWxLen2jaM0XDt1Q0gsHOjACSMdm6Qezrzz7eKwUjEVRdeKl6CYjngQ&gsessionid=AADE34lkfm4Qrize66EF_N8q6CKGZDJUwikFMxaENeTPC93O7Y6HKQ)  
  <sub>TipRanks, 1 hour ago</sub>  
  NEOS Ethereum High Income ETF saw a sizable fresh bid for yield this week, as the NEOS Ethereum High Income ETF's NEHI absorbed $1.66 million of net inflows...
- [XRP ETF Draws Fresh Demand as Short-Term Signals Flash Caution](https://www.google.com/goto?url=CAESqgEBxCJF1yxX5OhnJv1wlXYp4dD_A99k4-xICew_sYA_6Hr3IRiCzJsoE-1YjNbZMOBfxJYqaoKwREHrujTmx-D0zOiGPf3-M0O5Oq9lNJ61ckjv9N1yOlkRBjB6S932mrDYlQ1F5q59yNCjwXUqj6VrTu-C1vy11erOHuDBKtv2IVoa8qx819unFBXimvSCn9DYBEXnWkRgRVjin82bdBpcCBDLxQFV7T2FHA&gsessionid=AADE34lkfm4Qrize66EF_N8q6CKGZDJUwikFMxaENeTPC93O7Y6HKQ)  
  <sub>TipRanks, 5 hours ago</sub>  
  Canary XRP ETF recorded a $952000 inflow on October 30, 2026, lifting its assets under management to $313.208 million. The latest intake represented 0.30%...
- [3 ETFs with At Least 18% Upside Potential, According to the AI Analyst](https://www.google.com/goto?url=CAESpwEBxCJF10xqlfUpzWXw0ifHgw09-8GGLUYpk-77W3N8gzCExcdcKxuVW5UpwiznmAu0KjjXDvApT2URYFX9NMiu88zaQZDacDqIuLl0GJmYJagkW4_qkzjJeX1tdr2RDW99t_MbHLPF1Q_zpVcix_w230QL5JVhsBIgPPQn_ntHcieoBay3GbM-a2TufwIf9ag1Y_vrxVlIiA-3wQaZyfm5E1R-wHjbXQ&gsessionid=AADE34lkfm4Qrize66EF_N8q6CKGZDJUwikFMxaENeTPC93O7Y6HKQ)  
  <sub>TipRanks, 19 hours ago</sub>  
  As global stock markets remain volatile, several investors prefer exchange-traded funds (ETFs) as they help mitigate individual company-specific risk...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 104.93 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 105.73 (-0.8%), 50d 105.25 (-0.3%), 200d 108.52 (-3.3%); 50d below 200d
Momentum: RSI(14) 40.7 | MACD -0.210 vs signal -0.064 (histogram -0.146)
Returns: 1d +0.0% | 5d +0.2% | 1m -0.6% | 3m -2.0%
52-week range: 103.98 - 111.88 (now 12.1% of the way up)
Volatility: ATR(14) 0.35 (0.3% of price) | annualised 20d 3.7%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Inflation-Protected Bond
Yield: 4.4%
Credit quality: AA 100.0% | US government debt 99.8%
Three-year record: +3.4% a year | beta to the market 0.73
Cost and size: expense ratio 0.18% | net assets 14.65B
What it is made of: Bonds 99.8%, Cash 0.2%
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
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 37.8% of open interest (6,095,194 contracts)
Change on the week: +0.3% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.4% (62.23M) over 7d | 1 month: +2.7% (380.64M) over 34d
Shares outstanding: 139.81M | fund size: 14.67B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, technicals lack a decisive break, positioning shows modest bearish bias but recent short reduction, fundamentals unchanged.

**Main reasons it gave:**
- Large speculators net short 33.9% of open interest (bearish bias)
- 10‑year Treasury yield stable at 5.09% (down 0.01% week) – no rate surprise
- TLT price below 20‑day SMA (80.97) and 50‑day SMA (80.05) – no decisive technical break
- Fund basics unchanged: AA credit quality, 4.8% yield, expense ratio 0.15%

<details><summary><b>News</b> — score +0.00</summary>

- [iShares 20+ Year Treasury Bond ETF (TLT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TLT/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  iShares 20+ Year Treasury Bond ETF (TLT) · -0.87% · 0.21% · -4.00% · -8.70% · -9.96% · -45.15% · -1.87%.
- [Should Holders of iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) Be Concerned by a 5.07% Ten Year and 5.41% Thirty Year Yield?](https://kalkine.com.au/news/economic-news/should-holders-of-ishares-20-year-treasury-bond-etf-nasdaqtlt-be-concerned-by-a-507-ten-year-and-541-thirty-year-yield)  
  <sub>Kalkine, 2 hours ago</sub>  
  Should Holders of iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) Be Concerned by a 5.07% Ten Year and 5.41% Thirty Year Yield?
- [Should Investors Rethink iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) After Fed Minutes Leaned Toward Hikes?](https://www.google.com/goto?url=CAESzgEBxCJF11ifnNidHrdmdO-MnSuTNIFO5Zl-W170liQJoYgqBIC5j6U5gI1nW_5M8plnxCJ8dUwTxrcCteJcx-6FZdamNiPI8yOMSEVgJDeetXlVEL2k-HyjJhIbq1iyLrp7-Bsn5nwvxkDYww6GAoBp0TvEODdhGvXpuLuF42qz-HJzAu3dzGTvCpONRHJco8z6JQ4xFI-C0jSYtvH5cmUAL7_BtWRSvZVAUcX6luBMbfGuJOJOWZ8qynqun0QxiMSZGo7pcKd452NIOxjB-g&gsessionid=1R6dsH7P6ex07vf-u-e3LTRJkSmwHvji6atp7cgtA6ItwrbMLVTHug)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  Should Investors Rethink iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) After Fed Minutes Leaned Toward Hikes?
- [iShares 20+ Year Treasury Bond ETF (TLT) Latest Stock News & Headlines - Yahoo Finance](https://www.google.com/goto?url=CAESaQHEIkXXxLeSfTwGCrVhU-0I2WBG_RKeZXXGHAQxwUW4C5r3mu6MZW2_ygz4Hq3O4BN-l-rduAc73cW1NxLUfBTGg0cwD-7jaxSKylPhQkjRCb96luZPKqdy5yElspsdTM1n-mRWfbNfUw&gsessionid=1R6dsH7P6ex07vf-u-e3LTRJkSmwHvji6atp7cgtA6ItwrbMLVTHug)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  iShares 20+ Year Treasury Bond ETF (TLT).
- [Fed Minutes: Almost All Officials See More Rate Hikes - iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT)](https://www.google.com/goto?url=CAESrgEBxCJF171G1z6J3nOMwOeYQyFPRVjUoArKgmr_jlv-7oO_ueTDONQO6MHw6EWkXkjWPUn1Y3bvBkwA4hUdqF05llHSa22Tl1xEdvMhqGcHlSXHvwpVedHiGSEjzM4SK_avcuXjWIeAPmcLTPJySmWXi5Z5TkLM2X4BDGZZ3rk_Ij4RFyuSiCg3i8T4jptwBlTVOEO96Hj9YXkljFOvS3E7hxl28kKbWquzpzWA2F8&gsessionid=1R6dsH7P6ex07vf-u-e3LTRJkSmwHvji6atp7cgtA6ItwrbMLVTHug)  
  <sub>Benzinga, 19 hours ago</sub>  
  Fed minutes show almost all officials expect more rate hikes and flag AI debt as a growing risk, while TLT rose and Treasury yields eased Wednesday.
- [Which of the Top 3 Portfolio Hedges Came Through Best as the S&P 500 Dropped for a Fifth Day: SPDR Gold Shares (NYSEARCA:GLD), iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) or iPath Series B S&P 500 VIX Short-Term Futures ETN (CBOE:VX](https://www.google.com/goto?url=CAESzAIBxCJF1z2O4_mA4r3voxVQGIN_8y4naHmIu7mawL21ab6xaQsS4kjkVzY6VI9ZgXMqSKNcs81PmzYoZOZ3IiB_w70KXsECdJk8z6FHkoaMKqpywGW_GqMKIvVBvFu1N_baDXZ5wxeEWNv7BNnmfG4F4XRvN17p5Z3N4rOmXiGyf8R1dxpYIKpPgaiOhFki856hBH8Htn_av-dDAwXngAKZefV7lBxma45zJ99lw30HgmkQmpB8c6Kr1oXga4uuFlNzFKL6UwXMwYjOv0niuzMOx18K-SJCHqrQCMVj6n_T5Ah3Y71ymUlyfCktHDgUBZg9fQxltjVPI183vwpGSlRuVNe4QKlt2rgAPgScIoOqPIx_nAa5C1QhWQ8FY92LE8Sa-Qpo7NqMuia6_M7R3UWpoo6SED4GNW7nfmfyxsSBNX3fusVfgeXqqutwGw&gsessionid=1R6dsH7P6ex07vf-u-e3LTRJkSmwHvji6atp7cgtA6ItwrbMLVTHug)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  Which of the Top 3 Portfolio Hedges Came Through Best as the S&P 500 Dropped for a Fifth Day: SPDR Gold Shares (NYSEARCA:GLD), iShares 20+ Year Treasury...
- [Amplify TLT U.S. Treasury 12% Option Income ETF (TLTP) Seasonal Returns Chart - Yahoo Finance](https://www.google.com/goto?url=CAEScQHEIkXXNoCrJw-BvmsNIWgGZ1Q2Y88-GFNGnMGM6dnoxm6J4qlg1ZHziZm0MbPpi31FzFpvR1UnRMsg0I7HZV0ZWnb0QqEurbWONEKI5ft2-6b3wYrsU-omG_XFi3UEcnoLhEEFb0LgODQdI6vuFVt4&gsessionid=1R6dsH7P6ex07vf-u-e3LTRJkSmwHvji6atp7cgtA6ItwrbMLVTHug)  
  <sub>Yahoo! Finance Canada, 9 hours ago</sub>  
  Amplify TLT U.S. Treasury 12% Option Income ETF (TLTP) seasonal returns chart provides the mean and median returns by month to inform your investment...
- [Which Pick Among the Top 4 Rate and Dollar Funds Holds the Edge for a December Fed Hike: iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT), iShares 7-10 Year Treasury Bond ETF (NASDAQ:IEF), Invesco DB US Dollar Index Bullish Fund (NYSEARC](https://www.google.com/goto?url=CAES-QIBxCJF18wgamVIONnhFB6IMtbjwbvDk545hAzgN4d_2L9eq5fHZE2b4qOYaXktHxQgiWj0_MKyHoj-uo-_LjoMh_JbNKGrdj-DThX-612yQCLzCm2XlczQDchks7dNex2oS8oX2mBzELayNU480uUpVRl_EI5BDhTSNfZSPtYFwp2Dw-cfH3jEm31cUoyqCjGi2x9rUSr34VV2jHSHjZflydpAiN9xD0A4xFqkKhZYNS-FXl8iHNY3TORlwvt2g_K3w-2QsfYQTDIQcI7mp3w8kZngI11Dfu_dmG43UWCSMnDj6VmdPq9O2Lj546EaNK_dLPZY_QrBc2OFVufZW9SQXjxu2Lu1r4Lk9OwOfjIhW2RrZmYgZ6_UaTbHsFUf0usc-oea7kVnJ50URGW8FMbdlK29wXxPVImMRAuRjjQnKR0kzRclN22LDj_TGlwkmMQ7aV5Kd0X9X615mPzewoE6geWiLWMVYmRb5FTDISj5-UmXvGvhO4CnoQ&gsessionid=1R6dsH7P6ex07vf-u-e3LTRJkSmwHvji6atp7cgtA6ItwrbMLVTHug)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  Which Pick Among the Top 4 Rate and Dollar Funds Holds the Edge for a December Fed Hike: iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT), iShares 7-10 Year...
- [What Could a 5.07% 10-Year Yield Paired With a 5.41% 30-Year Yield Signal for iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT)?](https://www.google.com/goto?url=CAES2QEBxCJF10gL80qe-h2qLYfhGFRGRvlEb-24eKPdcrtOcY_JQOuIuXjnUeLNMr9OCpSQXInEB0HjQd90Z9aqBB_0gsKiCrJ3HDI8WYMdzYshV8Eo6HJGZH4L0-cRWKfqj1oC34U94SdXJOrzKxVAiqDgIwl79HQ1xWtQ2SdojlXry8kfsvbwcTgaB09bBr7AugLlAswHTwggjmwkqOywFwEJR_T8Z8equfgfQfJFP-IRotyquUoFsEbAOkl6_7qNGbx4K7T6_Yj57S8wO5SYsFjCeQhzcMBlUZWi&gsessionid=1R6dsH7P6ex07vf-u-e3LTRJkSmwHvji6atp7cgtA6ItwrbMLVTHug)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  What Could a 5.07% 10-Year Yield Paired With a 5.41% 30-Year Yield Signal for iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT)?
- [Two More Days Above 5% and Treasury Yields Tie 2007’s Run](https://www.google.com/goto?url=CAESoAEBxCJF14OZol6L6yyAcKbcWjvzgKPFM_sX0ZuNq5muEY9ihPRzSO-yA45Cnzp7cuXgkEQETjOfgF1Z3Tml_MLZz0N53XLGVC0AsWtDJdovPmRCIpw73DeRrsDdipCWQmtCFFrbUyQm9oQ2yGLPfMnsdPL0LN6bbzCaEMBd-aiMva5yd7ikQWsKEPxHuc9mDbpskQHb3YzwDNiEi8UojdqB&gsessionid=1R6dsH7P6ex07vf-u-e3LTRJkSmwHvji6atp7cgtA6ItwrbMLVTHug)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  TLT slid 5% this year and 35% over five years as the 10-year Treasury closed above 5% for a fourth straight session. Traders price a better-than-95% chance...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 79.96 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 80.97 (-1.2%), 50d 80.05 (-0.1%), 200d 84.15 (-5.0%); 50d below 200d
Momentum: RSI(14) 45.5 | MACD -0.124 vs signal 0.093 (histogram -0.217)
Returns: 1d -0.3% | 5d +0.3% | 1m -0.3% | 3m -2.5%
52-week range: 77.11 - 90.82 (now 20.8% of the way up)
Volatility: ATR(14) 0.72 (0.9% of price) | annualised 20d 10.1%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Long Government
Yield: 4.8%
Credit quality: AA 100.0% | US government debt 99.5%
Three-year record: +0.2% a year | beta to the market 2.30
Cost and size: expense ratio 0.15% | net assets 47.52B
What it is made of: Bonds 99.5%, Cash 0.5%
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
Contract: ULTRA UST BOND - CHICAGO BOARD OF TRADE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 33.9% of open interest (2,403,991 contracts)
Change on the week: -0.7% of open interest
Crowding: 48% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 109.70M | fund size: 8.77B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals show an uptrend but overbought RSI and low volume, positioning is modestly bearish, and fund flows are mixed.

**Main reasons it gave:**
- Dollar index rose 0.49% on the week to 103.66, near a 19‑month high
- UUP price above 20‑, 50‑ and 200‑day SMAs with RSI 70.6 indicating overbought conditions
- CFTC large speculators net long 5.5% of open interest, down 1.2% week‑over‑week
- Fund flows show a 9.5% share increase over the month but a 1.3% decline over the past week

<details><summary><b>News</b> — score +0.00</summary>

- [Which Pick Among the Top 4 Rate and Dollar Funds Holds the Edge for a December Fed Hike: iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT), iShares 7-10 Year Treasury Bond ETF (NASDAQ:IEF), Invesco DB US Dollar Index Bullish Fund (NYSEARC](https://kalkine.ca/news/economic-news/which-pick-among-the-top-4-rate-and-dollar-funds-holds-the-edge-for-a-december-fed-hike-ishares-20-year-treasury-bond-etf-nasdaqtlt-ishares-7-10-year-treasury-bond-etf-nasdaqief-invesco-db-us-dollar-index-bullish-fund-nysearcauup-or-ishares-1-3-year-treasury-bond-etf-nasdaqshy)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  Which Pick Among the Top 4 Rate and Dollar Funds Holds the Edge for a December Fed Hike: iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT), iShares 7-10 Year...
- [Does Invesco DB US Dollar Index Bullish Fund (NYSEARCA:UUP) Gain From a 19-Month High at 103.80?](https://kalkine.com.au/news/economic-news/does-invesco-db-us-dollar-index-bullish-fund-nysearcauup-gain-from-a-19-month-high-at-10380)  
  <sub>Kalkine, 2 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Deutsche Bank raises 2027 dollar outlook on AI support](https://www.google.com/goto?url=CAESrAEBxCJF190ahJpqnKIp-u_7wbFChwqdwhR6KooOQViUQ9hoqPaPsP0crC_-jMe3sxKZxAwr8AqHns0uMduYdhaFyMQGv7XgCxOfhSWcHGZlXFtnbcPsmKPqBIQz5s5X-VaO7QLAzehkq94jRxb7wH_Cwtdinz5pRKOG6_kLdU1e2jyZRAqvR-n_l6NDaQiIrDvTqh5ns-UqzXd2zKOq0jTl7fkssdfqvSIxf0zK&gsessionid=o7hW2Zm6Fe3jGmBz1zAI_4kTSJnUWtn9NU7Xt5fPgeO8TLsvJiCjqw)  
  <sub>Seeking Alpha, 44 minutes ago</sub>  
  Deutsche Bank raises its 2027 dollar forecasts, expecting first-half gains and only modest second-half easing, with AI spending keeping the dollar elevated.
- [Beyond Nvidia: Are Your AI ETFs Resilient Enough to Survive the Fallout?](https://www.google.com/goto?url=CAESrAEBxCJF13XnrPJaptDPTiDVCsce8qISt-70lThCr5CSlv7Xfwd5AHy_iD9G_t0VbUjZYorOuQElzwPH7kihl2cv56kYEHp7mTPHcSfZfmi72ZrNLzKBzUT_nB03AJZemrrAaDVvO_Ca79JiBJOxFFphcOmiKAebD5hJkcK42j_yMHUPWl6TLvWOHxmsxsWYiAISqxkBemVL5nxkkMci4PVJow-SP15P8Y007RKh&gsessionid=o7hW2Zm6Fe3jGmBz1zAI_4kTSJnUWtn9NU7Xt5fPgeO8TLsvJiCjqw)  
  <sub>Zacks Investment Research, 19 hours ago</sub>  
  Nvidia's leadership uncertainty and $118 billion in guarantees raise AI investment risks. Discover four AI ETFs offering diversified exposure beyond NVDA.
- [Invesco DB US Dollar Index Bullish Fund (NYSEARCA:UUP): What Could a Dollar Index Reading of 103.80, a 19-Month High, Mean for Its Holders?](https://www.google.com/goto?url=CAES5wEBxCJF18jiVvtrgQKh5U9TasGueNhPPfns54mKY6B0r_qByWyPuFiQ_6iTGrlgOBQ_TV3QaBoO4eSSajYk_lEQSciUwjGWNepuMVyyR8NBjV2RwTibG7knw25NfQmgcFfV-yt8SFxayE7QD7fdeh6d6imYbwU8oJy-YdCvwwVTtblVIRv4nWULMOZGUArVdrjHw_zzBMCSKHAnG3dcZ4wFRFdAVe57NyJpEjyqaUp-NffPP5zxCa4ojDw_gvQXmvI3HR5_E2lYIaWWFxsN2Cuyp8YwHZKXZK-nFGJ6PyDR0sUk9_64YY0&gsessionid=o7hW2Zm6Fe3jGmBz1zAI_4kTSJnUWtn9NU7Xt5fPgeO8TLsvJiCjqw)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  Invesco DB US Dollar Index Bullish Fund (NYSEARCA:UUP): What Could a Dollar Index Reading of 103.80, a 19-Month High, Mean for Its Holders?
- [USDU: US Dollar ETF With Adaptive Currency Weights](https://www.google.com/goto?url=CAESlwEBxCJF18_bPp9fXs_yJsmdIA6Mkqv3u-SPEK1R8GSiLUaOSJSpEiEkm5aZldXpydFk4Pfqd3ikZZ6y2ROvku5aMb93oLIOoG2VBWAu4zofkxl7cOwpVdoS-q67gnPOJtfarJTiXumyQAkdexkfVvtaq_ZKBmBDH0D9b_kkO1AvbgOo6HC7lwa945wsOwh3STE8mj2P4EZt&gsessionid=o7hW2Zm6Fe3jGmBz1zAI_4kTSJnUWtn9NU7Xt5fPgeO8TLsvJiCjqw)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  The WisdomTree Bloomberg US Dollar Bullish Fund ETF (USDU) offers dollar exposure through Treasury bills and currency forwards against a dynamic currency...
- [Should Investors Rethink iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) After Fed Minutes Leaned Toward Hikes?](https://www.google.com/goto?url=CAESzgEBxCJF17S47TR1t0YsG-d4_n3sf-hGnOzNrGmN3mRrj1B9vRmp0wBZsiHVdLbUEliQN0kajH91jbWrbzfQIAfTg3Qmz0HyT0x7z4jJXJREij02Y78m_OyYzyH19IcsfgRm1_pfTG91clKO5UG-ViRUAwdurnURI4i5b79y2M3Jf0fCnhcG_1g2ayjG4TPoBdNF6RIEmVqzdzB4NaPmx2zLdu1iUIlMB-C2tZZdYvrxtc4-bCTzVPeYbPbDtEmMnh1KqjyvTyWR7ExrCenHLw&gsessionid=o7hW2Zm6Fe3jGmBz1zAI_4kTSJnUWtn9NU7Xt5fPgeO8TLsvJiCjqw)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.60 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 29.19 (+1.4%), 50d 28.93 (+2.3%), 200d 28.09 (+5.4%); 50d above 200d
Momentum: RSI(14) 70.6 | MACD 0.193 vs signal 0.148 (histogram 0.044)
Returns: 1d -0.1% | 5d +0.6% | 1m +2.4% | 3m +6.1%
52-week range: 26.47 - 29.62 (now 99.5% of the way up)
Volatility: ATR(14) 0.12 (0.4% of price) | annualised 20d 5.3%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: n/a
What it holds: P/E n/a | P/B n/a | P/S n/a | 3y earnings growth n/a
Yield: n/a
Three-year record: n/a a year | beta to the market n/a
Cost and size: expense ratio n/a | net assets n/a
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
Contract: USD INDEX - ICE FUTURES U.S. (positions as of 2026-11-10, published the following Friday)
Large speculators: net long 5.5% of open interest (51,440 contracts)
Change on the week: -1.2% of open interest
Crowding: 82% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -1.3% (-6.30M) over 7d | 1 month: +9.5% (41.71M) over 30d
Shares outstanding: 16.31M | fund size: 482.75M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- fund equity_holdings unavailable: HTTP Error 401:
- fund bond_holdings unavailable: HTTP Error 401:
- fund bond_ratings unavailable: HTTP Error 401:
- fund fund_operations unavailable: HTTP Error 401:
- fund fund_overview unavailable: HTTP Error 401:
- fund top_holdings unavailable: HTTP Error 401:
- fund sector_weightings unavailable: HTTP Error 401:
- fund asset_classes unavailable: HTTP Error 401:

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 40.3; MACD negative; volume 0.04× 20‑day average
- Macro: no policy or data surprise; yields stable, inflation 3.7% near target, VIX up modestly but unchanged
- Analyst view: thin coverage (12% of fund) with bullish rating and +25.4% price target, limiting impact
- Positioning: net long 2.8% with +5.4% weekly increase, but fund flows show 0.8% outflow over the month

<details><summary><b>News</b> — score +0.00</summary>

- [What European Companies Does Vanguard FTSE Europe Shares ETF (ASX:VEQ) Track?](https://kalkine.com.au/news/mutual-funds-etfs/what-european-companies-does-vanguard-ftse-europe-shares-etf-asxveq-track)  
  <sub>Kalkine, 13 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 85.80 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 87.91 (-2.4%), 50d 87.63 (-2.1%), 200d 87.94 (-2.4%); 50d below 200d
Momentum: RSI(14) 40.3 | MACD -0.157 vs signal 0.149 (histogram -0.306)
Returns: 1d -0.1% | 5d -3.5% | 1m -2.0% | 3m -7.5%
52-week range: 77.90 - 93.19 (now 51.7% of the way up)
Volatility: ATR(14) 1.07 (1.3% of price) | annualised 20d 20.8%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Europe Stock
What it holds: P/E 16.72 | P/B 2.27 | P/S 1.51 | 3y earnings growth n/a
Yield: 2.9%
Three-year record: +16.2% a year | beta to the market 0.88
Cost and size: expense ratio 0.06% | net assets 37.08B
What it is made of: Stocks 99.3%, Cash 0.5%, Other 0.2%
Largest holdings: ASML Holding NV 3.9%, Roche Holding AG Ordinary Shares new 2.2%, Shell PLC 2.0%, Novartis AG Registered Shares 1.9%, HSBC Holdings PLC 1.9%
Sector mix: Financial services 23.8%, Industrials 18.9%, Healthcare 13.5%, Technology 8.9%
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
Rolled up from the 5 largest holdings, 12.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 83.8% | hold 16.2% | sell 0.0% (mean 2.08 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.4% above the current prices
Holdings read: ASML.AS, ROP.SW, SHEL.L, NOVN.SW, HSBA.L
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.05</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-11-10, published the following Friday)
Large speculators: net long 2.8% of open interest (506,737 contracts)
Change on the week: +5.4% of open interest
Crowding: 87% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.05</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +3.0% (1.07B) over 7d | 1 month: -0.8% (-293.94M) over 34d
Shares outstanding: 427.27M | fund size: 36.66B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: the streamed answer ran past the 480s ceiling (gave up after 2 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 53.67 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 55.79 (-3.8%), 50d 58.00 (-7.5%), 200d 58.25 (-7.9%); 50d below 200d
Momentum: RSI(14) 33.0 | MACD -1.015 vs signal -0.876 (histogram -0.140)
Returns: 1d -0.2% | 5d -4.9% | 1m -7.8% | 3m -11.2%
52-week range: 52.42 - 61.44 (now 13.9% of the way up)
Volatility: ATR(14) 0.87 (1.6% of price) | annualised 20d 23.7%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Diversified Emerging Mkts
What it holds: P/E 13.83 | P/B 2.03 | P/S 1.69 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +13.5% a year | beta to the market 0.78
Cost and size: expense ratio 0.06% | net assets 153.78B
What it is made of: Stocks 95.4%, Cash 4.2%, Other 0.4%, Preferred 0.0%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 15.3%, Tencent Holdings Ltd 2.7%, Alibaba Group Holding Ltd Ordinary Shares 2.1%, MediaTek Inc 1.5%, China Construction Bank Corp Class H 1.0%
Sector mix: Technology 32.4%, Financial services 20.5%, Consumer cyclical 9.5%, Industrials 7.4%
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
Rolled up from the 5 largest holdings, 22.6% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.32 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +69.5% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 00939
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-11-10, published the following Friday)
Large speculators: net long 2.1% of open interest (1,072,382 contracts)
Change on the week: +1.0% of open interest
Crowding: 30% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 1.42B | fund size: 76.11B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, but positive analyst view and modest inflows; overall call remains neutral.

**Main reasons it gave:**
- Fund flows: +3.7% share count week, +7.3% month (net inflows)
- Analyst view: 100% buy rating, weighted price target +70.7% above current price
- Technical indicators: price below 20d/50d/200d SMAs, RSI 23.2 (oversold), low volume, no decisive break
- Macro data: stable yields, VIX 22.48, no policy surprise
- Fund basics: moderate valuation (P/E 13.9), low beta (0.44), yield 1.3%

<details><summary><b>News</b> — score +0.00</summary>

- [Vaca Muerta atrae a tres magnates de Wall Street y estas son sus apuestas en Argentina](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0efafe144bf493bad06fc07636d4&url=https%3a%2f%2fwww.minutoneuquen.com%2fenergia%2f2026%2f11%2f19%2fvaca-muerta-atrae-a-tres-magnates-de-wall-street-414220.html&c=4533372410907346809&mkt=en-us)  
  <sub>Minuto Neuquen, 14h ago</sub>  
  Durante el tercer trimestre, tres multimillonarios estadounidenses ampliaron sus posiciones en acciones de empresas argentinas.
- [Koers Global X MSCI Argentina ETF - USD](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0efafe144bf493bad06fc07636d4&url=https%3a%2f%2fnl.marketscreener.com%2fkoers%2fetf%2fGLOBAL-X-MSCI-ARGENTINA-E-29426247%2f&c=15985892101984053517&mkt=en-us)  
  <sub>MarketScreener, 25h ago</sub>  
  Global X MSCI Argentina ETF - USD: beurskoers, grafieken, koersen, beursadviezen, financiële gegevens, analyses en real time nieuws ETF Global X MSCI Argentina ETF - USD | ARGT | US37950E2596 | NYSE ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 69.40 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 76.38 (-9.1%), 50d 84.13 (-17.5%), 200d 90.37 (-23.2%); 50d below 200d
Momentum: RSI(14) 23.2 | MACD -4.322 vs signal -3.939 (histogram -0.383)
Returns: 1d +0.3% | 5d -4.4% | 1m -20.6% | 3m -25.2%
52-week range: 69.17 - 102.94 (now 0.7% of the way up)
Volatility: ATR(14) 2.01 (2.9% of price) | annualised 20d 34.2%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.90 | P/B 1.59 | P/S 1.22 | 3y earnings growth n/a
Yield: 1.3%
Three-year record: +20.4% a year | beta to the market 0.44
Cost and size: expense ratio 0.59% | net assets 620.12M
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: MercadoLibre Inc 22.2%, YPF SA ADR 10.6%, Vista Energy SAB de CV ADR 8.2%, Grupo Financiero Galicia SA ADR 5.4%, Pampa Energia SA ADR 4.8%
Sector mix: Consumer cyclical 28.3%, Energy 22.6%, Financial services 13.7%, Basic materials 10.3%
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

<details><summary><b>What analysts and big funds say</b> — score +0.85</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.85</summary>

```text
Rolled up from the 5 largest holdings, 51.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.61 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +70.7% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, PAM
Recent rating changes among them:
  - MELI: 2026-11-11 UBS: main, Neutral -> Neutral
  - YPF: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-10-13 UBS: main, Neutral -> Neutral
  - PAM: 2026-11-02 JP Morgan: main, Neutral -> Neutral
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
Direction: money coming in (1 month)
Share count change: 1 week: +3.7% (21.70M) over 7d | 1 month: +7.3% (41.35M) over 30d
Shares outstanding: 8.75M | fund size: 606.91M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall due to mixed signals: strong analyst bullishness offset by flat fund flows, modest fundamentals, and no macro catalyst.

**Main reasons it gave:**
- Analyst view: 100% buy rating with +31.2% price target
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs and RSI 33.1 (oversold)
- Fund flows: flat share count, no net inflows/outflows
- Macro: no surprise data, yields unchanged, VIX up

<details><summary><b>News</b> — score +0.00</summary>

- [Which Of These 3 ETFs Gives You Elbit Systems With Less Company Risk?](https://simplywall.st/etfs/us/nysearca-iteq/news/which-of-these-3-etfs-gives-you-elbit-systems-with-less-comp)  
  <sub>Simply Wall St, 41 minutes ago</sub>  
  If you like Elbit Systems for its defense technology but hold it directly, you carry its company specific risks on your own. Simply Wall St flags that its...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 106.94 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 114.06 (-6.2%), 50d 118.58 (-9.8%), 200d 122.66 (-12.8%); 50d below 200d
Momentum: RSI(14) 33.1 | MACD -2.859 vs signal -2.345 (histogram -0.514)
Returns: 1d -1.2% | 5d -6.2% | 1m -12.4% | 3m -12.9%
52-week range: 99.40 - 137.69 (now 19.7% of the way up)
Volatility: ATR(14) 2.30 (2.2% of price) | annualised 20d 36.4%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.09 | P/B 2.45 | P/S 2.45 | 3y earnings growth n/a
Yield: 1.6%
Three-year record: +29.4% a year | beta to the market 0.98
Cost and size: expense ratio 0.59% | net assets 838.23M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Teva Pharmaceutical Industries Ltd 12.6%, Bank Leumi Le-Israel BM 8.6%, Bank Hapoalim BM 7.8%, Elbit Systems Ltd 5.6%, Tower Semiconductor Ltd 5.1%
Sector mix: Financial services 34.6%, Technology 18.0%, Healthcare 13.1%, Industrials 10.8%
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
Rolled up from the 5 largest holdings, 39.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.00 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +31.2% above the current prices
Holdings read: TEVA.TA, LUMI.TA, POLI.TA, ESLT.TA, TSEM.TA
Recent rating changes among them:
  - TEVA.TA: 2026-11-12 Piper Sandler: main, Overweight -> Overweight
  - ESLT.TA: 2026-10-05 Jefferies: main, Hold -> Hold
  - TSEM.TA: 2026-11-03 Wedbush: main, Neutral -> Neutral
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
Shares outstanding: 2.55M | fund size: 272.70M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals show weak short‑term momentum, while analyst view and fund inflows are modestly positive but not decisive.

**Main reasons it gave:**
- Price below 20‑day SMA (‑1.9%) and 50‑day SMA (‑3.0%)
- RSI 42 and MACD negative indicating weak momentum
- Fund flows show +27.2% share increase over past month (strong inflow)
- Analyst price target +9.1% above current price (modest bullish view)
- Macro yields stable; no surprise, VIX elevated at 22.5

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 42.71 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 43.54 (-1.9%), 50d 44.05 (-3.0%), 200d 40.80 (+4.7%); 50d above 200d
Momentum: RSI(14) 42.0 | MACD -0.241 vs signal -0.169 (histogram -0.072)
Returns: 1d -0.0% | 5d -2.8% | 1m -5.3% | 3m -3.9%
52-week range: 32.56 - 45.76 (now 76.9% of the way up)
Volatility: ATR(14) 0.64 (1.5% of price) | annualised 20d 23.1%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.39 | P/B 2.08 | P/S 1.40 | 3y earnings growth n/a
Yield: 3.4%
Three-year record: +32.2% a year | beta to the market 0.85
Cost and size: expense ratio 0.59% | net assets 1.03B
What it is made of: Stocks 99.4%, Cash 0.6%
Largest holdings: PKO Bank Polski SA 15.0%, Orlen SA 12.8%, Bank Polska Kasa Opieki SA 7.0%, Powszechny Zaklad Ubezpieczen SA 6.1%, Allegro.EU SA Ordinary Shares 5.7%
Sector mix: Financial services 45.2%, Consumer cyclical 14.9%, Energy 13.2%, Basic materials 5.6%
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
Rolled up from the 5 largest holdings, 46.6% of the fund by weight
Ratings by weight: buy 51.3% | hold 48.7% | sell 0.0% (mean 2.22 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.1% above the current prices
Holdings read: PKO.WA, PKN.WA, PEO.WA, PZU.WA, ALE.WA
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
Direction: money coming in (1 month)
Share count change: 1 week: +1.1% (10.85M) over 7d | 1 month: +27.2% (217.20M) over 30d
Shares outstanding: 23.77M | fund size: 1.02B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected) (Bing's feed, direct: 2 headline(s), none naming EPOL)

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows mixed signals: positive inflows (+4.5% week, +5.3% month) suggest demand, but analysts are bearish (42.6% sell, price target -4.3% below current) and technicals are weak (price below 20‑, 50‑, 200‑day SMAs, RSI 30.5, MACD negative). Macro conditions are stable with no surprise data. Overall the evidence balances out, leading to a neutral stance.

**Main reasons it gave:**
- Positive fund flows: share count +4.5% week, +5.3% month
- Analyst view bearish: 42.6% sell rating, weighted price target -4.3% below current
- Technical downside: price below 20d/50d/200d SMAs, RSI 30.5, MACD negative
- Macro stable: Treasury yields unchanged, VIX up modestly, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

- [澳大利亚ETF-iShares MSCI收跌1.42%，成交额9464.65万美元](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0ec38b0d4c9c898d94ab25e074a2&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fusstock%2fnotice%2f2026-11-19%2fdoc-inizfiwp1121572.shtml&c=2804516004333623587&mkt=en-us)  
  <sub>新浪财经, 16h ago</sub>  
  11月19日，澳大利亚ETF-iShares MSCI（EWA）收跌1.42%，报27.76美元，成交额9464.65万美元，市值12.38亿美元。 声明：市场有风险，投资需谨慎。本文基于第三方数据库发布，不代表新浪财经观点，任何在本文出现的信息均只作为参考，不构成个人投资建议。如有出入请以实际公告为准。如有疑问，请联系biz@staff.sina.com.cn。

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 27.52 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 29.11 (-5.4%), 50d 28.84 (-4.6%), 200d 28.99 (-5.1%); 50d below 200d
Momentum: RSI(14) 30.5 | MACD -0.244 vs signal -0.021 (histogram -0.223)
Returns: 1d -0.9% | 5d -5.8% | 1m -5.9% | 3m -8.7%
52-week range: 24.95 - 30.43 (now 46.9% of the way up)
Volatility: ATR(14) 0.36 (1.3% of price) | annualised 20d 18.5%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 20.37 | P/B 2.63 | P/S 3.35 | 3y earnings growth n/a
Yield: 2.9%
Three-year record: +12.0% a year | beta to the market 0.94
Cost and size: expense ratio 0.50% | net assets 1.25B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: BHP Group Ltd 14.3%, Commonwealth Bank of Australia 13.7%, National Australia Bank Ltd 6.3%, Westpac Banking Corp 6.2%, ANZ Group Holdings Ltd 6.0%
Sector mix: Financial services 43.9%, Basic materials 22.9%, Consumer cyclical 6.6%, Healthcare 6.0%
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

<details><summary><b>What analysts and big funds say</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.40</summary>

```text
Rolled up from the 5 largest holdings, 46.5% of the fund by weight
Ratings by weight: buy 0.0% | hold 57.4% | sell 42.6% (mean 3.45 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -4.3% above the current prices
Holdings read: BHP.AX, CBA.AX, NAB.AX, WBC.AX, ANZ.AX
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
Direction: money coming in (1 month)
Share count change: 1 week: +4.5% (52.53M) over 7d | 1 month: +5.3% (61.75M) over 34d
Shares outstanding: 44.36M | fund size: 1.22B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals bearish but low volume, modest fund inflows, analyst coverage bullish but limited.

**Main reasons it gave:**
- Macro data unchanged: inflation 3.7% and Fed target 4.0% (no surprise)
- Technical trend bearish: price 57.19 below 20d SMA 60.18, 50d SMA 59.90, 200d SMA 58.62
- Fund flows positive: share count +10.3% over past month (689.94M)
- Analyst coverage bullish: 87.2% buy rating covering 29.5% of fund, price target +12.1%

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 57.19 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 60.18 (-5.0%), 50d 59.90 (-4.5%), 200d 58.62 (-2.4%); 50d above 200d
Momentum: RSI(14) 32.5 | MACD -0.553 vs signal -0.140 (histogram -0.413)
Returns: 1d -0.1% | 5d -4.9% | 1m -6.7% | 3m -8.3%
52-week range: 49.91 - 62.64 (now 57.2% of the way up)
Volatility: ATR(14) 0.83 (1.5% of price) | annualised 20d 20.2%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.92 | P/B 2.74 | P/S 2.65 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +21.7% a year | beta to the market 0.73
Cost and size: expense ratio 0.50% | net assets 7.58B
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Royal Bank of Canada 9.1%, The Toronto-Dominion Bank 6.7%, Shopify Inc Registered Shs -A- Subord Vtg 6.2%, Bank of Montreal 3.8%, Canadian Natural Resources Ltd 3.8%
Sector mix: Financial services 40.4%, Energy 18.5%, Basic materials 13.1%, Technology 9.3%
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
Rolled up from the 5 largest holdings, 29.5% of the fund by weight
Ratings by weight: buy 87.2% | hold 12.8% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.1% above the current prices
Holdings read: RY, TD, SHOP, BMO.TO, CNQ.TO
Recent rating changes among them:
  - RY: 2025-08-29 Argus Research: main, Buy -> Buy
  - TD: 2026-06-01 RBC Capital: main, Outperform -> Outperform
  - SHOP: 2026-11-05 Argus Research: reit, Buy -> Buy
  - BMO.TO: 2026-05-28 RBC Capital: main, Sector Perform -> Sector Perform
  - CNQ.TO: 2026-03-12 Goldman Sachs: main, Buy -> Buy
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
Direction: money coming in (1 month)
Share count change: 1 week: +2.7% (197.41M) over 7d | 1 month: +10.3% (689.94M) over 34d
Shares outstanding: 129.17M | fund size: 7.39B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error captcha or protection page found) (Bing's feed, direct: 1 headline(s), none naming EWC)

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral – no macro surprise, technicals are bearish but not decisive, strong inflows and bullish analyst view are offset by modest fundamentals.

**Main reasons it gave:**
- Technicals: price below 20‑day, 50‑day and 200‑day SMAs, negative MACD, low volume
- Macro: no policy or data surprise; yields unchanged, VIX modestly higher
- Fund flows: +15.9% share count increase over the past month, indicating net inflows
- Analyst view: 100% buy rating on 33.9% of the fund, weighted price target +10.7% above current

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 50.89 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 52.08 (-2.3%), 50d 51.36 (-0.9%), 200d 51.52 (-1.2%); 50d below 200d
Momentum: RSI(14) 42.8 | MACD 0.047 vs signal 0.290 (histogram -0.243)
Returns: 1d +0.1% | 5d -3.3% | 1m -0.3% | 3m -5.1%
52-week range: 45.38 - 54.72 (now 59.0% of the way up)
Volatility: ATR(14) 0.74 (1.5% of price) | annualised 20d 22.8%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.53 | P/B 2.82 | P/S 2.81 | 3y earnings growth n/a
Yield: 3.5%
Three-year record: +16.9% a year | beta to the market 1.18
Cost and size: expense ratio 0.51% | net assets 1.10B
What it is made of: Stocks 99.2%, Cash 0.8%
Largest holdings: Spotify Technology SA 11.4%, Volvo AB Class B 6.4%, Atlas Copco AB Class A 6.2%, Sandvik AB 4.9%, Assa Abloy AB Class B 4.9%
Sector mix: Industrials 44.1%, Financial services 25.0%, Communication services 15.2%, Technology 6.9%
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
Rolled up from the 5 largest holdings, 33.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.97 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.7% above the current prices
Holdings read: SPOT, VOLV-B.ST, ATCO-A.ST, SAND.ST, ASSA-B.ST
Recent rating changes among them:
  - SPOT: 2026-10-23 Morgan Stanley: main, Overweight -> Overweight
  - ASSA-B.ST: 2015-12-09 Barclays: main, ? -> Equal-Weight
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
Direction: money coming in (1 month)
Share count change: 1 week: +3.7% (39.38M) over 7d | 1 month: +15.9% (150.16M) over 34d
Shares outstanding: 21.49M | fund size: 1.09B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall due to flat fund flows, bearish technicals, and no macro surprise despite bullish analyst coverage of major holdings.

**Main reasons it gave:**
- Flat fund flows: share count unchanged over week and month
- Price below 20‑day, 50‑day and 200‑day SMAs; RSI 40.8, MACD negative
- Macro: Treasury yields stable, VIX up 3.8 points, no surprise data releases
- Analyst view bullish (78% buy, +22% price target) but covers only 45% of fund

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 40.96 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 42.12 (-2.8%), 50d 41.87 (-2.2%), 200d 42.17 (-2.9%); 50d below 200d
Momentum: RSI(14) 40.8 | MACD -0.037 vs signal 0.135 (histogram -0.172)
Returns: 1d -0.2% | 5d -4.3% | 1m -1.8% | 3m -7.3%
52-week range: 38.08 - 44.59 (now 44.2% of the way up)
Volatility: ATR(14) 0.65 (1.6% of price) | annualised 20d 25.0%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.50 | P/B 1.87 | P/S 1.23 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +16.5% a year | beta to the market 0.95
Cost and size: expense ratio 0.49% | net assets 1.57B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: SAP SE 12.7%, Siemens AG 11.4%, Allianz SE 9.9%, Siemens Energy AG Ordinary Shares 5.8%, Deutsche Telekom AG 5.3%
Sector mix: Industrials 27.2%, Financial services 23.5%, Technology 16.9%, Healthcare 7.6%
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
Rolled up from the 5 largest holdings, 45.1% of the fund by weight
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.99 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.3% above the current prices
Holdings read: SAP.DE, SIE.DE, ALV.DE, ENR.DE, DTE.DE
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
Shares outstanding: 79.50M | fund size: 3.26B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – bullish analyst coverage and inflows are offset by bearish technicals and no macro surprise.

**Main reasons it gave:**
- Analyst coverage shows 90.8% buy rating and +15.4% price target for top holdings
- Fund flows indicate a 3.8% weekly share increase, suggesting inflows
- Technicals show price below 20‑day, 50‑day and 200‑day SMAs, negative MACD and low volume
- Macro data shows no surprise; yields stable, dollar up, VIX elevated but no policy shift

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI Italy ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0eaef913460a9e24f7385b816d2f&url=https%3a%2f%2fwww.barrons.com%2fmarket-data%2ffunds%2fewi&c=10563642463261866545&mkt=en-us)  
  <sub>Barron's, 26h ago</sub>  
  Stocks: Real-time U.S. stock quotes reflect trades reported through Nasdaq only; comprehensive quotes and volume reflect trading in all markets and are delayed at least 15 minutes. International stock ...
- [iShares MSCI Italy ETF (EWI)](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0eaef913460a9e24f7385b816d2f&url=https%3a%2f%2ffinance.yahoo.com%2fquote%2fEWI%2flatest-news%2f&c=5663603106828630729&mkt=en-us)  
  <sub>Yahoo Finance, 14h ago</sub>  
  The above button links to Coinbase. Yahoo Finance is not a broker-dealer or investment adviser and does not offer securities or cryptocurrencies for sale or facilitate trading. Coinbase pays us for ...
- [意大利ETF-iShares MSCI收跌1.86%，成交额2076.86万美元](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0eaef913460a9e24f7385b816d2f&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fusstock%2fnotice%2f2026-11-19%2fdoc-inizfiwi0541328.shtml&c=15435692388222620924&mkt=en-us)  
  <sub>新浪财经, 16h ago</sub>  
  11月19日，意大利ETF-iShares MSCI（EWI）收跌1.86%，报55.93美元，成交额2076.86万美元，市值10.7亿美元。 声明：市场有风险，投资需谨慎。本文基于第三方数据库发布，不代表新浪财经观点，任何在本文出现的信息均只作为参考，不构成个人投资建议。如有出入请以实际公告为准。如有疑问，请联系biz@staff.sina.com.cn。

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 56.41 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 57.02 (-1.1%), 50d 57.80 (-2.4%), 200d 58.29 (-3.2%); 50d below 200d
Momentum: RSI(14) 44.8 | MACD -0.089 vs signal -0.032 (histogram -0.057)
Returns: 1d +0.9% | 5d -3.2% | 1m +0.2% | 3m -10.3%
52-week range: 50.70 - 63.35 (now 45.1% of the way up)
Volatility: ATR(14) 0.89 (1.6% of price) | annualised 20d 28.2%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.58 | P/B 1.75 | P/S 1.42 | 3y earnings growth n/a
Yield: 3.4%
Three-year record: +24.7% a year | beta to the market 0.92
Cost and size: expense ratio 0.50% | net assets 1.19B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: UniCredit SpA 16.4%, Intesa Sanpaolo 13.8%, Enel SpA 11.7%, Eni SpA 5.5%, Generali 4.8%
Sector mix: Financial services 50.9%, Utilities 18.2%, Industrials 11.9%, Consumer cyclical 8.4%
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
Rolled up from the 5 largest holdings, 52.1% of the fund by weight
Ratings by weight: buy 90.8% | hold 9.2% | sell 0.0% (mean 2.16 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.4% above the current prices
Holdings read: UCG.MI, ISP.MI, ENEL.MI, ENI.MI, G.MI
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
Direction: money coming in (1 month)
Share count change: 1 week: +3.8% (43.11M) over 7d | 1 month: +1.1% (12.96M) over 34d
Shares outstanding: 20.95M | fund size: 1.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise; mixed signals from analyst view (strong buy on thin slice), positioning (small net long decreasing), positive fund inflows, and technicals showing price below SMAs with low RSI but no decisive break.

**Main reasons it gave:**
- Analyst view: 100% buy rating on 17.2% of fund, price target +28.7% above current
- CFTC positioning: net long 2.2% of open interest, down 5.8% week over week
- Fund flows: share count up 2.0% week, 9.1% month indicating inflows
- Technicals: price below 20d, 50d, 200d SMAs, RSI 37.2, no decisive break

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI Japan ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0e526f934e63aae1b812f5cf3014&url=https%3a%2f%2fmarkets.ft.com%2fdata%2fetfs%2ftearsheet%2fsummary%3fs%3dEWJ%3aPCQ%3aUSD&c=10615376893919317408&mkt=en-us)  
  <sub>Financial Times, 26h ago</sub>  
  The investment seeks to track the investment results of the MSCI Japan Index. The fund generally will invest at least 80% of its assets in the component securities of its underlying index and in ...
- [Asian stocks diverge on soft Australian employment and Anthropic IPO focus](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0e526f934e63aae1b812f5cf3014&url=https%3a%2f%2fseekingalpha.com%2fnews%2f4674511-asian-stocks-diverge-on-soft-australian-employment-and-anthropic-ipo-focus&c=18000818790270324293&mkt=en-us)  
  <sub>Seeking Alpha, 17h ago</sub>  
  Asian equity markets traded mixed on Thursday as investors weighed fresh economic data across Japan and Australia, monetary policy commentary from the Bank of Japan, and the upcoming Wall Street debut ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 88.69 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 91.74 (-3.3%), 50d 94.96 (-6.6%), 200d 92.15 (-3.7%); 50d above 200d
Momentum: RSI(14) 37.2 | MACD -1.738 vs signal -1.520 (histogram -0.217)
Returns: 1d +0.7% | 5d -3.0% | 1m -7.3% | 3m -6.8%
52-week range: 79.49 - 99.32 (now 46.4% of the way up)
Volatility: ATR(14) 1.55 (1.8% of price) | annualised 20d 30.0%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Japan Stock
What it holds: P/E 15.14 | P/B 1.95 | P/S 1.31 | 3y earnings growth n/a
Yield: 3.8%
Three-year record: +15.8% a year | beta to the market 0.86
Cost and size: expense ratio 0.49% | net assets 23.40B
What it is made of: Stocks 99.2%, Cash 0.8%
Largest holdings: Mitsubishi UFJ Financial Group Inc 4.5%, Toyota Motor Corp 3.6%, Advantest Corp 3.1%, Recruit Holdings Co Ltd 3.1%, Sumitomo Mitsui Financial Group Inc 2.9%
Sector mix: Industrials 22.4%, Technology 20.6%, Financial services 19.1%, Consumer cyclical 12.0%
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
Rolled up from the 5 largest holdings, 17.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +28.7% above the current prices
Holdings read: 8306.T, 7203.T, 6857.T, 6098.T, 8316.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-10, published the following Friday)
Large speculators: net long 2.2% of open interest (27,258 contracts)
Change on the week: -5.8% of open interest
Crowding: 27% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +2.0% (450.81M) over 7d | 1 month: +9.1% (1.96B) over 34d
Shares outstanding: 264.22M | fund size: 23.43B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Analyst consensus is modestly bullish (64.8% buy, +3.2% price target) but technicals are weak (price below 20‑day SMA, MACD below signal, very low volume) and fund flows are flat, with no macro surprise.

**Main reasons it gave:**
- Analyst ratings: 64.8% buy, weighted price target +3.2% above price
- Technicals: price below 20‑day SMA, MACD below signal, volume 0.04× 20‑day average
- Fund flows: flat, share count unchanged over week and month
- Macro: Treasury yields stable, VIX up 3.8 points, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 62.98 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 64.40 (-2.2%), 50d 62.07 (+1.5%), 200d 62.02 (+1.5%); 50d above 200d
Momentum: RSI(14) 44.9 | MACD 0.460 vs signal 0.803 (histogram -0.343)
Returns: 1d -0.6% | 5d -3.0% | 1m -0.3% | 3m -2.1%
52-week range: 55.69 - 66.56 (now 67.1% of the way up)
Volatility: ATR(14) 0.78 (1.2% of price) | annualised 20d 19.8%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 23.89 | P/B 4.18 | P/S 2.64 | 3y earnings growth n/a
Yield: 1.7%
Three-year record: +15.0% a year | beta to the market 0.82
Cost and size: expense ratio 0.50% | net assets 3.02B
What it is made of: Stocks 99.0%, Cash 1.0%
Largest holdings: Roche Holding AG Ordinary Shares new 15.0%, Novartis AG Registered Shares 12.9%, Nestle SA 11.4%, UBS Group AG Registered Shares 5.8%, Zurich Insurance Group AG 4.6%
Sector mix: Healthcare 40.1%, Financial services 19.2%, Consumer defensive 13.5%, Industrials 11.2%
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
Rolled up from the 5 largest holdings, 49.6% of the fund by weight
Ratings by weight: buy 64.8% | hold 35.2% | sell 0.0% (mean 2.46 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +3.2% above the current prices
Holdings read: ROP.SW, NOVN.SW, NESN.SW, UBSG.SW, ZURN.SW
Recent rating changes among them:
  - UBSG.SW: 2026-04-20 Barclays: up, Underweight -> Equal-Weight
  - ZURN.SW: 2016-09-20 Bankhaus Lampe: down, Hold -> Sell
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
Shares outstanding: 28.62M | fund size: 1.80B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected) (Bing's feed, direct: 0 headline(s), none naming EWL)

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals show weak momentum but no decisive break, analyst view is bullish but limited to 42% coverage, fund flows flat.

**Main reasons it gave:**
- Analyst coverage of top 5 holdings (42.3% weight) shows 100% buy rating and +59.9% price target
- Fund flows flat: share count unchanged over past week and month
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 36.7 and negative MACD indicate weak momentum
- Macro: Treasury yields stable, VIX up modestly, no surprise data releases

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 62.08 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 64.28 (-3.4%), 50d 65.73 (-5.5%), 200d 65.17 (-4.7%); 50d above 200d
Momentum: RSI(14) 36.7 | MACD -0.827 vs signal -0.602 (histogram -0.225)
Returns: 1d +0.0% | 5d -4.4% | 1m -5.4% | 3m -10.6%
52-week range: 55.33 - 71.61 (now 41.5% of the way up)
Volatility: ATR(14) 1.04 (1.7% of price) | annualised 20d 26.0%
Volume: 0.01x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.38 | P/B 2.46 | P/S 1.73 | 3y earnings growth n/a
Yield: 4.4%
Three-year record: +17.3% a year | beta to the market 1.13
Cost and size: expense ratio 0.50% | net assets 597.52M
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ASML Holding NV 21.9%, ING Groep NV 8.6%, Prosus NV Ordinary Shares - Class N 4.7%, ASM International NV 3.8%, Nebius Group NV Shs Class-A- 3.4%
Sector mix: Technology 30.4%, Financial services 21.1%, Consumer defensive 11.8%, Industrials 11.0%
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
Rolled up from the 5 largest holdings, 42.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +59.9% above the current prices
Holdings read: ASML.AS, INGA.AS, PRX.AS, ASM.AS, NBIS
Recent rating changes among them:
  - NBIS: 2026-11-04 Citigroup: main, Buy -> Buy
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
Shares outstanding: 5.55M | fund size: 344.54M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected) (Bing's feed, direct: 0 headline(s), none naming EWN)

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: analyst view moderately bullish (76% buy, +9.9% price target), fundamentals modestly positive (3% yield, strong 3‑year record), but technicals slightly bearish (price below SMAs, RSI 43.2, MACD negative) and flows flat, with no macro surprise.

**Main reasons it gave:**
- Analyst coverage 53% of fund, 76% buy, weighted price target +9.9% above current prices
- Price below 20‑day, 50‑day, 200‑day SMAs; RSI 43.2; MACD negative
- Fund flows flat: 0% share count change over 1 week and 1 month
- VIX up 3.8 points to 22.48, dollar index up 0.49, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [西班牙ETF-iShares MSCI收跌1.56%，成交额1472.94万美元](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0eb3ac84485ca648d4854d46a8d9&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fusstock%2fnotice%2f2026-11-19%2fdoc-inizfiwm4339774.shtml&c=10056245007867294694&mkt=en-us)  
  <sub>新浪财经, 17h ago</sub>  
  11月19日，西班牙ETF-iShares MSCI（EWP）收跌1.56%，报57.53美元，成交额1472.94万美元，市值20.58亿美元。 声明：市场有风险，投资需谨慎。本文基于第三方数据库发布，不代表新浪财经观点，任何在本文出现的信息均只作为参考，不构成个人投资建议。如有出入请以实际公告为准。如有疑问，请联系biz@staff.sina.com.cn。

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 57.52 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 58.24 (-1.2%), 50d 58.93 (-2.4%), 200d 58.18 (-1.1%); 50d above 200d
Momentum: RSI(14) 43.2 | MACD -0.039 vs signal 0.002 (histogram -0.041)
Returns: 1d -0.0% | 5d -3.5% | 1m -1.5% | 3m -8.6%
52-week range: 49.37 - 63.23 (now 58.8% of the way up)
Volatility: ATR(14) 0.87 (1.5% of price) | annualised 20d 24.7%
Volume: 0.01x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 16.25 | P/B 2.19 | P/S 1.75 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +29.4% a year | beta to the market 0.91
Cost and size: expense ratio 0.50% | net assets 1.94B
What it is made of: Stocks 99.4%, Cash 0.6%
Largest holdings: Banco Santander SA 16.4%, Iberdrola SA 14.3%, Banco Bilbao Vizcaya Argentaria SA 12.6%, Repsol SA 5.3%, Industria De Diseno Textil SA Share From Split 4.6%
Sector mix: Financial services 40.5%, Utilities 22.9%, Industrials 14.9%, Technology 6.3%
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
Rolled up from the 5 largest holdings, 53.1% of the fund by weight
Ratings by weight: buy 76.3% | hold 23.7% | sell 0.0% (mean 2.29 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.9% above the current prices
Holdings read: SAN.MC, IBE.MC, BBVA.MC, REP.MC, ITX.MC
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

**In the model's own words:**

> Neutral overall; no macro surprise, technicals bearish, but strong inflows and bullish analyst view offset each other.

**Main reasons it gave:**
- US Treasury yields stable; no rate surprise
- Price below 20d, 50d, 200d SMAs; RSI 33.4 (oversold)
- Share count up 7.3% in one week (strong inflows)
- Analyst rating 100% buy, price target +67% above current

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 87.30 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 97.28 (-10.3%), 50d 106.07 (-17.7%), 200d 95.08 (-8.2%); 50d above 200d
Momentum: RSI(14) 33.4 | MACD -4.855 vs signal -4.218 (histogram -0.638)
Returns: 1d -1.6% | 5d -10.2% | 1m -19.9% | 3m -16.3%
52-week range: 60.03 - 118.00 (now 47.0% of the way up)
Volatility: ATR(14) 3.80 (4.4% of price) | annualised 20d 65.8%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Greater China Region
What it holds: P/E 27.29 | P/B 4.22 | P/S 2.50 | 3y earnings growth n/a
Yield: 1.0%
Three-year record: +31.2% a year | beta to the market 1.35
Cost and size: expense ratio 0.59% | net assets 11.05B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 22.3%, MediaTek Inc 6.1%, Hon Hai Precision Industry Co Ltd 3.4%, ASE Technology Holding Co Ltd 3.0%, Delta Electronics Inc 2.9%
Sector mix: Technology 71.4%, Financial services 16.3%, Basic materials 4.4%, Industrials 2.6%
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

<details><summary><b>What analysts and big funds say</b> — score +1.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +1.00</summary>

```text
Rolled up from the 5 largest holdings, 37.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +67.4% above the current prices
Holdings read: 2330.TW, 2454.TW, 2317.TW, 3711.TW, 2308.TW
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
Share count change: 1 week: +7.3% (742.63M) over 7d | 1 month: +14.0% (1.34B) over 34d
Shares outstanding: 124.39M | fund size: 10.86B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall due to mixed signals: bullish analyst view and fund inflows versus bearish technicals and modest macro headwinds.

**Main reasons it gave:**
- Technical: price below 20‑day, 50‑day, 200‑day SMAs; RSI 37.9, low volume
- Macro: US dollar index up to 103.66, inflation 3.7% above target, no policy surprise
- Analyst view: 100% buy rating, weighted price target +18.5% above current price
- Fund flows: share count up 1.9% week‑over‑week, indicating net inflows

<details><summary><b>News</b> — score +0.00</summary>

- [Which of the Top 3 Overseas Funds Faces the Stiffest Test From Inflation and Rate Hikes: iShares MSCI Indonesia ETF (NASDAQ:EIDO), iShares MSCI Eurozone ETF (CBOE:EZU) or iShares MSCI United Kingdom ETF (NYSEARCA:EWU)?](https://kalkine.ca/news/economic-news/which-of-the-top-3-overseas-funds-faces-the-stiffest-test-from-inflation-and-rate-hikes-ishares-msci-indonesia-etf-nasdaqeido-ishares-msci-eurozone-etf-cboeezu-or-ishares-msci-united-kingdom-etf-nysearcaewu)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  Which of the Top 3 Overseas Funds Faces the Stiffest Test From Inflation and Rate Hikes: iShares MSCI Indonesia ETF (NASDAQ:EIDO), iShares MSCI Eurozone ETF...
- [How Could Governor Waller Half-Point Hike Call Affect iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY)?](https://kalkine.ca/news/economic-news/how-could-governor-waller-half-point-hike-call-affect-ishares-1-3-year-treasury-bond-etf-nasdaqshy)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Which Signals From Jobless Claims and the Philly Fed Survey on November 19 Matter Most for iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY) Holders?](https://www.google.com/goto?url=CAES8wEBxCJF124zoLpnBR3xaLY_LztIZppNZwjTNIvwZ7i8uK49qfjJmpuBWxWy8oGD1y-b1IJbljJ3jdWXVU7QVbjqf2KlB1PRVUd4uF7QinrXQZ2cksDaox1lw6I9yyt2gqByJKJ9zSnnVaWtrYNWwl4ZoUQRRzdaWDIH4gofntFTgV0RxHQycpATjqzFvdrPg57BulAE_gbtlrA1uQlO8xeEuW3vnU76INkePJ45DdZBBxmvaNGRa85obeuuSADPi1qoz_dPg8nBF44ZJLmjZQOn8Lxvyl5IN1wM9TUmSgd8IzYWOu1rWkJrQYWKyu2Oi8HGV6I&gsessionid=3ZpkaQGt_tMFk7qyIIqtdPUeTLktHEEgNYupi6UU27mC_h7SVIUMAg)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  Which Signals From Jobless Claims and the Philly Fed Survey on November 19 Matter Most for iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY) Holders?
- [SPDR S&P Homebuilders ETF (NYSEARCA:XHB): What Does a 9.9% Jump in Housing Starts Alongside a 7.4% Fall in Permits Imply?](https://www.google.com/goto?url=CAES0wEBxCJF154lF9UPck7HmaFU0ku69IwUsWIlgpGgLlFDzxhvnJv9EsM7y-O6dm8aoLIHG-Ij1_8PwZ0dKwaB6XQF4QIuxXwrjMtgyGhqxLgwrIw9zgwiOdoPh5y1URjZLhImv-adaHTdJhdvHc6JWa6NRAc5Sl9t-hLvciE42h7stj5kkJ6WX7GX9yT5P_wbV5bA9UykdfiRSDZiMfqcUB4mc1n9ZChjLMhldxUOjGY5G_Iyy81U-jy2kh-TdEq57vej8Mw0peBOG5WE7HzPEoyDy01o&gsessionid=3ZpkaQGt_tMFk7qyIIqtdPUeTLktHEEgNYupi6UU27mC_h7SVIUMAg)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  SPDR S&P Homebuilders ETF (NYSEARCA:XHB): What Does a 9.9% Jump in Housing Starts Alongside a 7.4% Fall in Permits Imply?
- [Should Investors Rethink iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) After Fed Minutes Leaned Toward Hikes?](https://www.google.com/goto?url=CAESzgEBxCJF1yyHJmo4ULq4P-DuIWA1S1AwYeegfflfyzrkK7OBspFU-8MxxSKh3yAaLR6ftDVR-KiaieHEvUmOJy7TTnlGirS4-TBSTPK9PaKEEhR5h8nnaPyjTRk-HqM58HYu_d6NMZ7ixv59aObTNPIz1bkUZZZ1DroGreia4X0lFJ7UIV3NcHevD-POpoWhyWex4O4VEyCya_sdHVzio1c136XYuW9HxtqywzoHXcuPQhjJLIM2-FitLF352Nk95vEkKL6BObaOhu4ttgprew&gsessionid=3ZpkaQGt_tMFk7qyIIqtdPUeTLktHEEgNYupi6UU27mC_h7SVIUMAg)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [How Could a 91% Chance of a December Fed Hike Reshape Returns on iShares 7-10 Year Treasury Bond ETF (NASDAQ:IEF)?](https://www.google.com/goto?url=CAES0QEBxCJF108XKjkeq0vrShUnrxsF8Ow413uQBpaFz2dEcSBV2g1Eq9mkVkbRbhRjCLs-yKVRm7QJ_Pwpsa2WLQ7_9qOvaXd24IwflHxRc6i-Ns6hirJ1NlTE0RQF_bO2SEL5LKYKeEHaAeT_ctY94aVJhqoehD6IS1Z22hqW2upd_RA81JHPCRneHfYVfNgxqcIC4sOMnp-nCq06W8Xtad8prQDqZOR8cfAFnr9_PmW2GMd27EhWKrTnVp90EEVSqjw8LpPIJPkR29kliweiF8DuHw&gsessionid=3ZpkaQGt_tMFk7qyIIqtdPUeTLktHEEgNYupi6UU27mC_h7SVIUMAg)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  How Could a 91% Chance of a December Fed Hike Reshape Returns on iShares 7-10 Year Treasury Bond ETF (NASDAQ:IEF)?
- [Which Pick Among the Top 4 Rate and Dollar Funds Holds the Edge for a December Fed Hike: iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT), iShares 7-10 Year Treasury Bond ETF (NASDAQ:IEF), Invesco DB US Dollar Index Bullish Fund (NYSEARC](https://www.google.com/goto?url=CAES-QIBxCJF1znjQKjlRCNdmtqimMdmECXe-1DREeU50STABJYSj_o3wXR5pBWBQb9UKaE0U6r2H_s58xmWp3PdI4BCDbXAdYrh79VaAOAAsFCdQaaMUz2HPPnfU-2fAwxEjpDJuBxbnwS0U7MhkENFT9rqtUZHR_nVFpWPf8DE8uE7GlW_9oCWZ9H-Db3CZucOzi6kvM41rKGKRvCO8r1lOppuQ_yGyZnNIxHHXoMu5_51JBCDVCNGP-hPGc1hqjhyANEjmvHV0JbUxFNfrSIGREr1DKyvhf0RmuN_LR0ZKHisI8LIDTr5eQlhhPBucWYLUQNBvJWSV8nEgrUOhx3273G-Rw8iPN_qgsCU-MfAtCzzEmqPOMaeWT6N3Y08ukHDxjNb5MKhFjAnXouQei-B0_Z6VeyPOYOH2bkTFiwVuMlJD_VjEn_pU25VjOCw0diF8M32iuSzXEwJ2yDVZ6VWKja335bFkq0LNvYXK0qEytmNnjm_xNnPHNgYNQ&gsessionid=3ZpkaQGt_tMFk7qyIIqtdPUeTLktHEEgNYupi6UU27mC_h7SVIUMAg)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  Which Pick Among the Top 4 Rate and Dollar Funds Holds the Edge for a December Fed Hike: iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT), iShares 7-10 Year...
- [What Could a 5.07% 10-Year Yield Paired With a 5.41% 30-Year Yield Signal for iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT)?](https://www.google.com/goto?url=CAES2QEBxCJF1-peakwb8JussQjeAf3y32BhfSiLaDIgDcQysbqvm9WS8n0txIGi3oisuJxGi4XX2NY_1ZIRfIx7SmBx8ZaAwvAo19iTWq62_o7q24cmbuQWqVnxvMd3fZWh26Aq8gC69SoKQS9dgTPoP7fgveWWatqewWpmNBDP9BIVOi4HbzN3j54D9wHtNv3-6bzTLJ855n-qv01-JfNVGoZr4xE5eykwMJUMVhGFH4-R_Z62rcJWVQD0n8Z83rK8SynFvMxSEX68F0LtKi52VvuhvBzrIAR5xnGM&gsessionid=3ZpkaQGt_tMFk7qyIIqtdPUeTLktHEEgNYupi6UU27mC_h7SVIUMAg)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  What Could a 5.07% 10-Year Yield Paired With a 5.41% 30-Year Yield Signal for iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT)?
- [Is the High-Yield Credit Spread Widening, Currently at 3.43% After a 20 Basis Point Rise?](https://www.google.com/goto?url=CAESuAEBxCJF1-8QJdy3sBr9_zUogQJuCvvnQUQWtVUFmBk85qYyUjIicYtAcLYeaFGrEw0Y0Glwuz_q9EdvmVYd060gji4FC3F5r1K4W1MUQ5nFgb7abDMcPpjuCXmY1D88C_XsYmnQmIY-sHOG39AYHkz3hPnXUXS3XKMRKBgto9Nwt4QyZDAagR31NeZi57Rkb3Z7ENHR4PHCm2U55W7ZGDfcR0rneU_PF4YjBPEC3z8hxgGZrmrHChtR&gsessionid=3ZpkaQGt_tMFk7qyIIqtdPUeTLktHEEgNYupi6UU27mC_h7SVIUMAg)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Invesco DB US Dollar Index Bullish Fund (NYSEARCA:UUP): What Could a Dollar Index Reading of 103.80, a 19-Month High, Mean for Its Holders?](https://www.google.com/goto?url=CAES5wEBxCJF121lL_hL28qIxuzCHhwoHdCZRmRDkpHHp_QOzkOAEhMF_g3moALkHwxW8lNdc4txlYBYgcAg_h74Lexbq_gnchDMa8YvkvkmFzXXwfxrJysqSRMdU4ylt0iyjpx8r-WcdeivTVwzp6wbGZFpL90VndXxCP0KbKr4Mss-3cqMVjTnayxpDsyjDD_YNPSw_P-mggkUVu76uE1I3l-ErtYBAx6m9ONzbyYZRGdbA-D4bzNPxSttt51OTriAiJCt4gbMGABmheIAEmxs3N5rS0GPT_1dAYiOdbkrIsjeMDJGMcSCxmI&gsessionid=3ZpkaQGt_tMFk7qyIIqtdPUeTLktHEEgNYupi6UU27mC_h7SVIUMAg)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  Invesco DB US Dollar Index Bullish Fund (NYSEARCA:UUP): What Could a Dollar Index Reading of 103.80, a 19-Month High, Mean for Its Holders?

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 46.00 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 47.55 (-3.3%), 50d 47.30 (-2.7%), 200d 47.09 (-2.3%); 50d above 200d
Momentum: RSI(14) 37.9 | MACD -0.180 vs signal 0.040 (histogram -0.220)
Returns: 1d -0.2% | 5d -3.7% | 1m -3.5% | 3m -6.0%
52-week range: 41.34 - 49.39 (now 57.9% of the way up)
Volatility: ATR(14) 0.62 (1.3% of price) | annualised 20d 21.3%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 16.62 | P/B 2.25 | P/S 1.41 | 3y earnings growth n/a
Yield: 3.1%
Three-year record: +18.0% a year | beta to the market 0.66
Cost and size: expense ratio 0.50% | net assets 3.73B
What it is made of: Stocks 98.5%, Other 1.0%, Cash 0.5%
Largest holdings: Shell PLC 9.9%, HSBC Holdings PLC 9.3%, AstraZeneca PLC 8.9%, Unilever PLC 4.4%, Rolls-Royce Holdings PLC 4.4%
Sector mix: Financial services 23.2%, Consumer defensive 15.3%, Energy 14.3%, Healthcare 13.9%
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
Rolled up from the 5 largest holdings, 36.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.07 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.5% above the current prices
Holdings read: SHEL.L, HSBA.L, AZN.L, ULVR.L, RR.L
Recent rating changes among them:
  - AZN.L: 2026-08-24 CICC: init, ? -> Outperform
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
Share count change: 1 week: +1.9% (68.27M) over 7d | 1 month: +1.6% (58.43M) over 34d
Shares outstanding: 79.59M | fund size: 3.66B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs; RSI 38.1 indicating bearish momentum
- Analyst coverage: 100% buy on 47.5% of fund, weighted price target +16.5% above current price
- Fund flows flat: share count unchanged (+0.0% week, +0.0% month)
- Macro: yields stable, VIX up 3.8 points, no surprise inflation or unemployment data

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI Mexico ETF (EWW)](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0ee2f19e40ff9d29c402a9667640&url=https%3a%2f%2ffinance.yahoo.com%2fquote%2fEWW%2flatest-news%2f&c=11875460064645588513&mkt=en-us)  
  <sub>Yahoo Finance, 14h ago</sub>  
  The above button links to Coinbase. Yahoo Finance is not a broker-dealer or investment adviser and does not offer securities or cryptocurrencies for sale or facilitate trading. Coinbase pays us for ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 73.18 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 75.82 (-3.5%), 50d 74.29 (-1.5%), 200d 76.16 (-3.9%); 50d below 200d
Momentum: RSI(14) 38.1 | MACD 0.241 vs signal 0.625 (histogram -0.384)
Returns: 1d -0.6% | 5d -5.7% | 1m -3.1% | 3m -5.4%
52-week range: 66.02 - 81.23 (now 47.1% of the way up)
Volatility: ATR(14) 1.41 (1.9% of price) | annualised 20d 20.8%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 12.23 | P/B 1.88 | P/S 1.40 | 3y earnings growth n/a
Yield: 3.3%
Three-year record: +11.3% a year | beta to the market 0.99
Cost and size: expense ratio 0.50% | net assets 1.56B
What it is made of: Stocks 99.3%, Cash 0.7%
Largest holdings: Grupo Mexico SAB de CV Class B 14.9%, Grupo Financiero Banorte SAB de CV Class O 11.2%, Fomento Economico Mexicano SAB de CV Units Cons. Of 1 Shs-B- And 4 Shs-D- 8.9%, America Movil SAB de CV Ordinary Shares - Class B 7.9%, Cemex SAB de CV Cert Part Ord Repr 2 Shs-A- & 1 Shs-B- 4.6%
Sector mix: Consumer defensive 25.1%, Basic materials 24.7%, Financial services 18.1%, Industrials 12.7%
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
Rolled up from the 5 largest holdings, 47.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.5% above the current prices
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 18.90M | fund size: 1.38B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; analyst view bullish but limited coverage, fundamentals solid yet price at 52‑week low, technicals bearish but no decisive break, and flows flat with no macro surprise.

**Main reasons it gave:**
- Analyst view: 100% buy rating and +40.4% price target for top holdings (41.8% weight)
- Fund flows: flat share count (0% change) indicating no net inflows/outflows
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 32.6 (oversold) and low volume
- Fundamentals: low P/E 10.65, high yield 8.2%, three‑year return +22.6% per year
- Macro: yields unchanged, inflation 3.7% in line with expectations, no rate surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 59.37 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 64.25 (-7.6%), 50d 64.99 (-8.6%), 200d 67.78 (-12.4%); 50d below 200d
Momentum: RSI(14) 32.6 | MACD -0.860 vs signal -0.207 (histogram -0.653)
Returns: 1d -0.3% | 5d -9.2% | 1m -9.1% | 3m -18.1%
52-week range: 59.37 - 81.60 (now 0.0% of the way up)
Volatility: ATR(14) 1.56 (2.6% of price) | annualised 20d 35.8%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.65 | P/B 1.96 | P/S 1.68 | 3y earnings growth n/a
Yield: 8.2%
Three-year record: +22.6% a year | beta to the market 1.12
Cost and size: expense ratio 0.59% | net assets 438.81M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Anglogold Ashanti PLC 11.3%, Naspers Ltd Class N 8.4%, Gold Fields Ltd 8.2%, Firstrand Ltd 7.5%, Standard Bank Group Ltd 6.4%
Sector mix: Financial services 36.0%, Basic materials 35.9%, Consumer cyclical 13.0%, Communication services 7.2%
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
Rolled up from the 5 largest holdings, 41.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.99 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +40.4% above the current prices
Holdings read: AU, NPN.JO, GFI.JO, FSR.JO, SBK.JO
Recent rating changes among them:
  - AU: 2026-10-30 JP Morgan: main, Overweight -> Overweight
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
Shares outstanding: 7.90M | fund size: 468.98M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error captcha or protection page found) (Bing's feed, direct: 0 headline(s), none naming EZA)

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst coverage and strong weekly inflows are offset by bearish technical indicators and no macro catalyst.

**Main reasons it gave:**
- Weekly fund flows up 9.5% (1.93B) indicating inflow
- Technical: price below 20‑day, 50‑day, 200‑day SMAs; RSI 35.6; MACD negative
- Analyst view: 100% buy rating, price target +31.2% above current price
- Macro: yields stable, no policy surprise; VIX up to 22.48 (elevated volatility)

<details><summary><b>News</b> — score +0.00</summary>

- [Gold Miners ETF (GDX) Elliott Wave outlook remains bearish, downside target at $62 [Video]](https://www.fxstreet.com/analysis/gold-miners-etf-gdx-elliott-wave-outlook-remains-bearish-downside-target-at-62-video-202611190503)  
  <sub>FXStreet, 10 hours ago</sub>  
  The Gold Miners ETF (GDX) continues to display a bearish sequence from the August 25, 2026 high, suggesting that the broader decline remains incomplete and...
- [Why (GDX) Price Action Is Critical for Tactical Trading](https://news.stocktradersdaily.com/news_release/15/Why_GDX_Price_Action_Is_Critical_for_Tactical_Trading_111926031402_1795076042.html)  
  <sub>Stock Traders Daily, 12 hours ago</sub>  
  Key findings for Vaneck Gold Miners Etf (NYSE: GDX). Weak Near-Term Sentiment Could Catalyze Bearish Positioning; A mid-channel oscillation pattern is in...
- [GDXJ Stock Price, Quote & News](https://www.google.com/goto?url=CAESYAHEIkXX4loZgL-knAKnnhxgW1UnU49gt1wn9p3NJRp0ECoztKKaSOWzPq6zrIBLMI29jSK2Tj48LX37T1Ihnmg9f9I8uGYq1GILXfuaHANij7x-hDhsz-KhZbkZYtbltg&gsessionid=U5btWf7orygaeb8hBUHQg42WfMwZn61TLIqmXMWmL7V5femVlE5nHg)  
  <sub>Syfe, 24 hours ago</sub>  
  Overview. VanEck Junior Gold Miners ETF (GDXJ) is trading at US$90.59, down 5.47% today as of Nov 18, 09:57 EST. Over the past 52 weeks, GDXJ has traded between...
- [How (GDXJ) Movements Inform Risk Allocation Models](https://www.google.com/goto?url=CAESvgEBxCJF16Alm8h8upYNZNvD5XVpXKHFCthZ-PzibDPAh0B8LK-vH7z9rjQk9B6RiGRcfD0gpx4kVH_9QsQLwoOgW078g5k9KbhmfHL0S8wEqQIXQEI1hicHvcWeWp3_Ay_iem_kMBDQT1uvS5XPGJBQO8YRBJYNajMYFcKgcCjf2TzEyfUuk05iubjf30f3Fq34vrul-wdgW4WURK5eMBn440VeRJdOGY_RpIBfAsbW1NhocKzs1l-GE46sUIuv&gsessionid=U5btWf7orygaeb8hBUHQg42WfMwZn61TLIqmXMWmL7V5femVlE5nHg)  
  <sub>Stock Traders Daily, 12 hours ago</sub>  
  Key findings for Vaneck Junior Gold Miners Etf (NASDAQ: GDXJ). Weak Near and Mid-Term Sentiment Could Pressure Neutral Long-Term Outlook...
- [RY: SEC Form FWP filed by Royal Bank Of Canada](https://www.google.com/goto?url=CAESkgEBxCJF18Wq0hVLxz9U9QJPLsdEF8gXKTbyLok1-cutRquGEVq9NiWPm3QrDTLyTdSHMW4zAHB4k71uqcdTF5a4ILww44EnJ_EWli3l4CitB1FwaNXKOX8prYIHfCueCDRAZymPPnCT6BF61mkZWF4Agae2H5WyRsGt_EAa7ix-d93OXaYammCJSLVgh7VOWdDrvQ&gsessionid=U5btWf7orygaeb8hBUHQg42WfMwZn61TLIqmXMWmL7V5femVlE5nHg)  
  <sub>Quantisnow, 19 hours ago</sub>  
  RBC files $1,000 auto-callable notes on VanEck Gold Miners ETF (GDX), due Nov 30, 2029, min 11.50% p.a. contingent coupon, priced below par.
- [Options Whale Alert: $379K Bullish Short Put Opened on $GDXJ](https://www.google.com/goto?url=CAESogEBxCJF17lxhY8iFywB1z6wiK8k_U1Yw64pitq0rD0mREYCyy1KyL7OCFMI09RT4g62L4oUwWV_t45K6CBVY1N_Zlj1SnZJbnm48Zu7_lIAFJjemJolhYz6AXzdsoyWPOYUdpOiDfgzbs0AfF2qH8URq36sRL2DWnwXkThm6Wo62U7_05OvkpXeTU2VTBL4LYt1khEQmiqmnw7wiRTK8TTOY-I&gsessionid=U5btWf7orygaeb8hBUHQg42WfMwZn61TLIqmXMWmL7V5femVlE5nHg)  
  <sub>Moomoo, 13 hours ago</sub>  
  VanEckJunior Gold Miners ETF(GDXJ.US)$ closed down 6.02% at $90.07. A trader sold 1628 Nov 20, 2026 $90.00 puts to open a Short Put. The position carries a.
- [3 Mining Giants Pay Big Dividends, but Their Yields Come With a Catch](https://www.google.com/goto?url=CAESrQEBxCJF17NkVDyV0qrE8D3TsUbW8bK0Win37s9tuzOcl-UN4aDcXEDdMEG-sVchO5JA5HBV8FblMtFr0P48u_HxiX4ZoxFjzDMnaxmGCjpaw61W71bAR5GIYfSur-N89Fr3VQq3BfeP4Qrsl2I2MuQTSRHTpQCNaxTq37YODRvebWDWm54rzRpget4aQ7lk2f3g-XdfxPMh3KrFJPxYK9dlodMxmWj078p6EMLeWA&gsessionid=U5btWf7orygaeb8hBUHQg42WfMwZn61TLIqmXMWmL7V5femVlE5nHg)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  Rio Tinto and BHP share profits with investors, so dividends rise and fall with commodity prices, and Rio now yields about 6% after a selloff.
- [Toronto Dominion Bank (TD): Prices TD autocallable notes tied to gold miners and silver ETFs](https://www.google.com/goto?url=CAESlQEBxCJF1x04qfDb_oaoSBQbGS0fDOMFAmwWWnAC5uEBKo6w7BKviFicfEocYLnUwhcUb1BmOr7EENltpQFrfBPCLLN-gNQZIFCgfGH0ZN1aVn8F-jgt3c23H5jMCpgAnodMtnoeJbrj0PuKA-gZi0mhht8eC2PRTQafMHmfbCLP5Lq89Vp3aK4oWcKGg0upwg2lNQk9uQ&gsessionid=U5btWf7orygaeb8hBUHQg42WfMwZn61TLIqmXMWmL7V5femVlE5nHg)  
  <sub>Quantisnow, 20 hours ago</sub>  
  Toronto-Dominion Bank filed a preliminary pricing supplement for Autocallable Contingent Interest Barrier Notes due on or about November 23, 2029.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 74.40 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 81.79 (-9.0%), 50d 86.55 (-14.0%), 200d 89.19 (-16.6%); 50d below 200d
Momentum: RSI(14) 35.6 | MACD -2.367 vs signal -1.589 (histogram -0.779)
Returns: 1d -0.6% | 5d -9.1% | 1m -14.2% | 3m -27.6%
52-week range: 70.74 - 115.84 (now 8.1% of the way up)
Volatility: ATR(14) 3.42 (4.6% of price) | annualised 20d 58.6%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Equity Precious Metals
What it holds: P/E 12.25 | P/B 2.71 | P/S 3.99 | 3y earnings growth n/a
Yield: 0.8%
Three-year record: +42.6% a year | beta to the market 0.98
Cost and size: expense ratio 0.51% | net assets 23.82B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Newmont Corp 11.6%, Agnico Eagle Mines Ltd 11.3%, Barrick Mining Corp 8.2%, Wheaton Precious Metals Corp 5.5%, Franco-Nevada Corp 5.5%
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
Rolled up from the 5 largest holdings, 42.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.71 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +31.2% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, FNV.TO
Recent rating changes among them:
  - NEM: 2026-10-27 Scotiabank: main, Sector Outperform -> Sector Outperform
  - AEM.TO: 2026-11-02 Freedom Broker: up, Hold -> Buy
  - ABX.TO: 2026-11-10 JP Morgan: main, Overweight -> Overweight
  - WPM.TO: 2026-10-08 UBS: main, Buy -> Buy
  - FNV.TO: 2026-11-12 HC Wainwright & Co.: reit, Buy -> Buy
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
Direction: flat (1 month)
Share count change: 1 week: +9.5% (1.93B) over 7d | 1 month: +0.2% (48.58M) over 30d
Shares outstanding: 300.23M | fund size: 22.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Flat fund flows (0% change over 1 week and 1 month) indicate no net demand; technicals show mixed signals – price above 200‑day SMA (+6.1 %) but below 20‑day and 50‑day SMAs, RSI 44.2, MACD negative – providing no clear bullish break; macro environment unchanged with stable Treasury yields, no policy surprise, and inflation at 3.7 % near target.

**Main reasons it gave:**
- Fund flows flat: 0% change in share count over 1 week and 1 month
- Technicals mixed: price above 200‑day SMA (+6.1%) but below 20‑day (103.12) and 50‑day (105.75) SMAs, RSI 44.2, MACD negative
- Macro unchanged: Treasury yields stable, no policy surprise, inflation 3.7% near target

<details><summary><b>News</b> — score +0.00</summary>

- [iShares Expanded Tech-Software ETF (Derivatives) Price Today](https://cryptorank.io/price/ishares-expanded-tech-software-etf-derivatives)  
  <sub>CryptoRank, 20 hours ago</sub>  
  Current iShares Expanded Tech-Software ETF (Derivatives) (IGV) token data: Price $ 96.79, Trading Volume $ 136.69K, Market Cap $ 0.00, Circ.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 100.14 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 103.12 (-2.9%), 50d 105.75 (-5.3%), 200d 94.39 (+6.1%); 50d above 200d
Momentum: RSI(14) 44.2 | MACD -2.355 vs signal -1.944 (histogram -0.411)
Returns: 1d +3.3% | 5d -1.3% | 1m -8.0% | 3m -3.1%
52-week range: 74.67 - 112.67 (now 67.0% of the way up)
Volatility: ATR(14) 3.04 (3.0% of price) | annualised 20d 34.7%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: n/a
What it holds: P/E n/a | P/B n/a | P/S n/a | 3y earnings growth n/a
Yield: n/a
Three-year record: n/a a year | beta to the market n/a
Cost and size: expense ratio n/a | net assets n/a
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 12.50M | fund size: 1.25B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- fund equity_holdings unavailable: HTTP Error 401:
- fund bond_holdings unavailable: HTTP Error 401:
- fund bond_ratings unavailable: HTTP Error 401:
- fund fund_operations unavailable: HTTP Error 401:
- fund fund_overview unavailable: HTTP Error 401:
- fund top_holdings unavailable: HTTP Error 401:
- fund sector_weightings unavailable: HTTP Error 401:
- fund asset_classes unavailable: HTTP Error 401:

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, technicals lack a decisive break, and mixed fund‑flow and analyst signals.

**Main reasons it gave:**
- US inflation 3.7% and unemployment 4.1% in line with expectations, no policy surprise
- Technicals: price above 20‑day, 50‑day, 200‑day SMAs, RSI 73 (overbought), but volume only 0.12× 20‑day average
- Fund flows: 1‑month outflows of -7.5% (-$475M), indicating bearish demand
- Analyst coverage thin (24.8% of fund) despite 100% buy rating and +13.4% price target

<details><summary><b>News</b> — score +0.00</summary>

- [India: Is It Oversold And Under-Held?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0ecd43e24a63ada8b9138773d6e2&url=https%3a%2f%2fseekingalpha.com%2farticle%2f4970031-india-is-it-oversold-under-held&c=14179819831100773716&mkt=en-us)  
  <sub>Seeking Alpha, 12h ago</sub>  
  Foreigners have pulled a record $27 billion out of Indian stocks this year, and their ownership is at a fifteen-year low. India is about 8.5% of world output at purchasing-power parity but only 1.3% ...
- [Motilal Oswal Launches Nifty Commodities and Chemicals ETFs: Reliance, Tata Steel, Pidilite and More Stocks to Watch](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0ecd43e24a63ada8b9138773d6e2&url=https%3a%2f%2ftradebrains.in%2fmoney%2fmotilal-oswal-launches-nifty-commodities-and-chemicals-etfs-reliance-tata-steel-pidilite-and-more-stocks-to-watch-12822369&c=12676796862182431447&mkt=en-us)  
  <sub>Trade Brains, 10h ago</sub>  
  Two new exchange-traded funds (ETFs) targeted at India's chemicals and commodities industries have been suggested by Motilal Oswal Mutual Fund, offering investors the chance to participate in ...
- [Motilal Oswal Nifty India Defence ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0ecd43e24a63ada8b9138773d6e2&url=https%3a%2f%2feconomictimes.indiatimes.com%2fmotilal-oswal-nifty-india-defence-etf%2fmffactsheet%2fschemeid-44517.cms&c=10069716070539868426&mkt=en-us)  
  <sub>Indiatimes, 18h ago</sub>  
  1. Current NAV: The Current Net Asset Value of the Motilal Oswal Nifty India Defence ETF as of Nov 18, 2026 is Rs 97.10 for Growth option of its Regular plan. 2. Returns: Its trailing returns over ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 52.04 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 49.72 (+4.7%), 50d 48.27 (+7.8%), 200d 49.09 (+6.0%); 50d below 200d
Momentum: RSI(14) 73.0 | MACD 1.162 vs signal 0.992 (histogram 0.170)
Returns: 1d +1.1% | 5d +1.0% | 1m +10.1% | 3m +4.8%
52-week range: 45.42 - 54.83 (now 70.4% of the way up)
Volatility: ATR(14) 0.53 (1.0% of price) | annualised 20d 15.7%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: India Equity
What it holds: P/E 21.32 | P/B 2.99 | P/S 2.59 | 3y earnings growth n/a
Yield: n/a
Three-year record: +5.1% a year | beta to the market 0.61
Cost and size: expense ratio 0.61% | net assets 5.84B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: HDFC Bank Ltd 6.3%, ICICI Bank Ltd 5.9%, Reliance Industries Ltd 5.3%, Bharti Airtel Ltd 4.4%, Infosys Ltd 2.9%
Sector mix: Financial services 29.6%, Consumer cyclical 12.2%, Industrials 9.9%, Technology 8.7%
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
Rolled up from the 5 largest holdings, 24.8% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.37 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.4% above the current prices
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
Share count change: 1 week: -0.5% (-27.66M) over 7d | 1 month: -7.5% (-475.42M) over 30d
Shares outstanding: 112.89M | fund size: 5.87B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Share count up 3.9% in one week (464M) – strong inflows
- Price below 20‑day (70.32) and 50‑day (70.06) SMAs, 8% below 200‑day SMA
- RSI 47.1 and MACD negative, indicating weak momentum
- US Treasury yields unchanged, VIX up to 22.48 – no macro surprise

<details><summary><b>News</b> — score +0.00</summary>

- [How to Invest in iShares US Aerospace & Defense ETF (ITA)](https://www.fool.com/investing/how-to-invest/etfs/how-to-invest-in-ita-etf/)  
  <sub>The Motley Fool, 19 hours ago</sub>  
  What is iShares U.S. Aerospace & Defense ETF's expense ratio? The expense ratio for the ITA ETF is 0.37%, which amounts to $37 annually per $10,000 invested.
- [3 ETFs To Own General Dynamics Without The Same Defense Mix](https://simplywall.st/stocks/us/capital-goods/nyse-gd/general-dynamics/news/3-etfs-to-own-general-dynamics-without-the-same-defense-mix)  
  <sub>Simply Wall St, 24 hours ago</sub>  
  Owning General Dynamics directly means you carry its specific issues on your own. Simply Wall St flags heavy insider selling in recent months and points to...
- [3 Aerospace And Defense ETFs For The 45 Day China Free Magnet Scramble](https://www.google.com/goto?url=CAESmQEBxCJF1yw6TAemDtBof0hDyqgO5VGefHXDY-X8qej5ppmuAhHXs9e32m0YTsYvTUmNOXLfxr3ITLzXnS6reoE5o_aC3DUUcAbQqWyvOG5256HG6xqkwkMFNcrHgiob39Kvzd87kU9milXeADvC8EOcJ0dZor1Cj_81PFxlTldqu0rzaCw6GBFFzx3n6-78nONWeJEVoxdRMw4&gsessionid=iO4gRJ7WJ1dqK5XBCrpD3HZP-Fo0X2D4qb9jBNbMT7TdQKMq1qe4mA)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  You can line up three aerospace and defense ETFs side by side and they still look almost identical from the tickers. Pick one without checking the holdings...
- [Which ETFs Give You General Dynamics Without Going All In?](https://www.google.com/goto?url=CAESoQEBxCJF11Y5MSV6cH791d5DBmHn8Ay_LmC2bjV8-FU8SGEyfGLq3sCeD4X9YwI8czU0-WOz3ZSJexfmPBddaYdVVtFoin4b34kE9kK83L5x-a8OzuuiVDINKNHNKUSr7LgZ1REgxMiqLnkzPrq63KRtt5PUsbRiXDHiT1HpyMgaLULZTwmv-eAN4AJ-KpzB2cUEehay0s5Xcn_uQPAvjn3bdQ&gsessionid=iO4gRJ7WJ1dqK5XBCrpD3HZP-Fo0X2D4qb9jBNbMT7TdQKMq1qe4mA)  
  <sub>Yahoo Finance, 24 hours ago</sub>  
  You might like General Dynamics for its mix of jets, submarines and defense technology, but owning the stock outright means living with its specific issues...
- [Trump-Vance ties strained by midterm blame game over Iran war - report (ITA:BATS)](https://www.google.com/goto?url=CAESqQEBxCJF17-2Ci51Qt8UZUWN2GvsWYpiD-uh2PMCi87gANdRXtXJq7_njYyAqtyG2iYs7nR-194XOr3T3fPIl71-Nxk5gRM8GEAV0JWTZQCSeL-BGixlCHWNbjuqPxmWPeHztiL6w3Bernj_MJLWJ-1pM_kMtudNjQO6xoufR_3Mxp4kt9-nklhs7aEm0OOjF4XmWfih0S6ODnEMGiuVetnBPUW4Fd6_jEmm&gsessionid=iO4gRJ7WJ1dqK5XBCrpD3HZP-Fo0X2D4qb9jBNbMT7TdQKMq1qe4mA)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Trump's frustration with JD Vance over Iran-war comments strains their relationship and lifts Rubio's 2028 standing; Vance's Kalshi 2028 odds are 13%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 69.68 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 70.32 (-0.9%), 50d 70.06 (-0.5%), 200d 75.77 (-8.0%); 50d below 200d
Momentum: RSI(14) 47.1 | MACD -0.010 vs signal 0.089 (histogram -0.099)
Returns: 1d +0.4% | 5d -2.9% | 1m +1.6% | 3m -11.9%
52-week range: 66.08 - 84.41 (now 19.7% of the way up)
Volatility: ATR(14) 1.65 (2.4% of price) | annualised 20d 31.8%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: n/a
What it holds: P/E n/a | P/B n/a | P/S n/a | 3y earnings growth n/a
Yield: n/a
Three-year record: n/a a year | beta to the market n/a
Cost and size: expense ratio n/a | net assets n/a
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.50</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +3.9% (464.01M) over 7d | 1 month: +202.4% (8.19B) over 30d
Shares outstanding: 175.51M | fund size: 12.23B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- fund equity_holdings unavailable: HTTP Error 401:
- fund bond_holdings unavailable: HTTP Error 401:
- fund bond_ratings unavailable: HTTP Error 401:
- fund fund_operations unavailable: HTTP Error 401:
- fund fund_overview unavailable: HTTP Error 401:
- fund top_holdings unavailable: HTTP Error 401:
- fund sector_weightings unavailable: HTTP Error 401:
- fund asset_classes unavailable: HTTP Error 401:

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals are mixed with no decisive break, modest inflows but no fundamental data.

**Main reasons it gave:**
- Share count rose 1.8% in the past week (34.70M) indicating modest inflows
- RSI at 49.3 and MACD below signal (histogram -0.097) showing neutral to bearish momentum
- Recent macro data (inflation 3.7%, unemployment 4.1%) in line with expectations, no surprise
- Fundamental data unavailable (FUND BASICS fields N/A)

<details><summary><b>News</b> — score +0.00</summary>

- [iShares US Home Construction ETF (ITB) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/ITB/)  
  <sub>Yahoo Finance UK, 4 hours ago</sub>  
  Find the latest iShares US Home Construction ETF (ITB) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 82.14 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 82.57 (-0.5%), 50d 81.07 (+1.3%), 200d 82.08 (+0.1%); 50d below 200d
Momentum: RSI(14) 49.3 | MACD 0.517 vs signal 0.613 (histogram -0.097)
Returns: 1d -0.9% | 5d -1.7% | 1m +2.7% | 3m -5.6%
52-week range: 68.14 - 90.01 (now 64.0% of the way up)
Volatility: ATR(14) 1.49 (1.8% of price) | annualised 20d 27.3%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: n/a
What it holds: P/E n/a | P/B n/a | P/S n/a | 3y earnings growth n/a
Yield: n/a
Three-year record: n/a a year | beta to the market n/a
Cost and size: expense ratio n/a | net assets n/a
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
Direction: money coming in (1 month)
Share count change: 1 week: +1.8% (34.70M) over 7d | 1 month: +3.2% (61.36M) over 34d
Shares outstanding: 24.34M | fund size: 2.00B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- fund equity_holdings unavailable: HTTP Error 401:
- fund bond_holdings unavailable: HTTP Error 401:
- fund bond_ratings unavailable: HTTP Error 401:
- fund fund_operations unavailable: HTTP Error 401:
- fund fund_overview unavailable: HTTP Error 401:
- fund top_holdings unavailable: HTTP Error 401:
- fund sector_weightings unavailable: HTTP Error 401:
- fund asset_classes unavailable: HTTP Error 401:

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst view is offset by outflows and technical downtrend, with no macro catalyst.

**Main reasons it gave:**
- Fund flows show outflows: -0.9% week, -6.9% month
- Technical trend: price below 50‑day and 200‑day SMA, indicating downtrend
- Analyst view bullish for 45% of fund: 90.6% buy, +17.4% price target
- Macro environment unchanged: no policy surprise, yields stable, VIX modestly higher

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 35.39 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 35.07 (+0.9%), 50d 35.84 (-1.2%), 200d 37.70 (-6.1%); 50d below 200d
Momentum: RSI(14) 48.6 | MACD 0.054 vs signal -0.080 (histogram 0.134)
Returns: 1d -0.6% | 5d -2.0% | 1m +2.4% | 3m -7.6%
52-week range: 33.69 - 40.63 (now 24.5% of the way up)
Volatility: ATR(14) 0.33 (0.9% of price) | annualised 20d 14.0%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.14 | P/B 1.71 | P/S 2.83 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: -0.3% a year | beta to the market 0.20
Cost and size: expense ratio 0.75% | net assets 556.97M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Al Rajhi Bank 14.1%, Saudi Arabian Oil Co 12.5%, Saudi National Bank 8.2%, Saudi Telecom Co 6.2%, Saudi Arabian Mining Co 4.3%
Sector mix: Financial services 41.3%, Energy 13.5%, Basic materials 12.7%, Communication services 8.9%
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
Rolled up from the 5 largest holdings, 45.3% of the fund by weight
Ratings by weight: buy 90.6% | hold 9.4% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.4% above the current prices
Holdings read: 1120.SR, 2222.SR, 1180.SR, 7010.SR, 1211.SR
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
Direction: money going out (1 month)
Share count change: 1 week: -0.9% (-5.00M) over 7d | 1 month: -6.9% (-40.84M) over 30d
Shares outstanding: 15.54M | fund size: 549.95M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technicals are bearish (RSI 29.1, price below SMAs), macro is hawkish (VIX up, yields high, dollar stronger), analyst view is strongly bullish (100% buy, +86% price target), but fund flows show net outflows over the month.

**Main reasons it gave:**
- Technicals show bearish momentum (RSI 29.1, price below 20‑day, 50‑day, 200‑day SMAs)
- Macro environment hawkish (VIX up 3.8, yields high, dollar index up 0.49)
- Analyst coverage strongly bullish (100% buy, price target +86% above current price)
- Fund flows net outflows over month (-2.9% share count, money going out)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 47.57 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 49.71 (-4.3%), 50d 51.16 (-7.0%), 200d 54.85 (-13.3%); 50d below 200d
Momentum: RSI(14) 29.1 | MACD -0.755 vs signal -0.518 (histogram -0.237)
Returns: 1d -0.5% | 5d -4.4% | 1m -5.0% | 3m -14.5%
52-week range: 47.57 - 64.26 (now 0.0% of the way up)
Volatility: ATR(14) 0.67 (1.4% of price) | annualised 20d 20.3%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Greater China Region
What it holds: P/E 11.09 | P/B 1.27 | P/S 1.27 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +6.5% a year | beta to the market 0.47
Cost and size: expense ratio 0.59% | net assets 5.49B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Tencent Holdings Ltd 13.2%, Alibaba Group Holding Ltd Ordinary Shares 9.1%, China Construction Bank Corp Class H 4.8%, Industrial And Commercial Bank Of China Ltd Class H 2.9%, Xiaomi Corp Class B 2.5%
Sector mix: Consumer cyclical 23.1%, Financial services 22.5%, Communication services 17.5%, Technology 9.9%
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
Rolled up from the 5 largest holdings, 32.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.40 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +86.1% above the current prices
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
Share count change: 1 week: +5.9% (298.84M) over 7d | 1 month: -2.9% (-159.36M) over 30d
Shares outstanding: 113.56M | fund size: 5.40B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error captcha or protection page found) (Bing's feed, direct: 4 headline(s), none naming MCHI)

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals remain weak, but fund inflows show modest bullish sentiment.

**Main reasons it gave:**
- Fund flows: share count +5.1% week‑over‑week (3.36B) and +13.4% month‑over‑month (8.17B) indicate net inflows
- Technical trend: price below 20‑day SMA (-4.6%), 50‑day SMA (-13.1%), 200‑day SMA (-8.8%); RSI 41.6, MACD negative
- Macro: yields stable (10‑yr 5.09% unchanged), VIX up modestly to 22.48, no policy surprise
- No analyst view of holdings or fundamental metrics available

<details><summary><b>News</b> — score +0.00</summary>

- [2026 Semiconductor Stock Selloff: The Long-Term Outlook](https://www.vaneck.com/us/en/blogs/thematic-investing/2026-semiconductor-stock-selloff-the-long-term-outlook/)  
  <sub>VanEck, 48 minutes ago</sub>  
  Semiconductor volatility is reshaping the timing of the AI buildout. Our analyst assesses data center politics, memory risk and long-term compute demand.
- [3 ETFs For AMD After Its OpenAI News গল্প](https://simplywall.st/stocks/us/semiconductors/nasdaq-amd/advanced-micro-devices/news/3-etfs-for-amd-after-its-openai-news)  
  <sub>Simply Wall St, 3 hours ago</sub>  
  You might like Advanced Micro Devices for its chips and artificial intelligence work, but holding the stock on its own means living with its specific risks.
- [Wall Street Says the AI Trade Is Over — ETF Investors Aren’t Acting Like It](https://www.google.com/goto?url=CAESvwEBxCJF14eZALgNYnqipadLcmQLxLPI60aFQMSrcBFUWLWlxwD0rfyFOMlzwpZfCns9vJwbezXZEgHxr9lDXtOKNlk6p-ICDDLaMHyVzr_jLyA-7Ho_lzm8qAf_8ImQXqRDbB7wRNrGIwO1ngpVgHiz-Sbjow-4YpzxopoB0ALn37m3zmFyTbUZa9ZPjhuqRfZ4SEDrmu7XnA-tAjG1WITxxMOK9nT0wPXydKFJYowJ7kDG9Opn61mas_O8TCsfsg&gsessionid=Lz4QijQlEeunTGlV42KnC4E0LhaBiKk7cCvdtIW5dUfbzAa2kmHsMg)  
  <sub>Benzinga, 20 hours ago</sub>  
  Investors pour $14 billion into four battered ETFs despite AI bubble pop fears. Here's where conviction is holding — and where it's fading.
- [Which Funds With Semiconductor Exposure Best Capture The China AI Chip Curbs?](https://www.google.com/goto?url=CAESlwEBxCJF1yw2PRHFQndy6eC9TMBUOZLkzMoz3FeJ-DLYk1qtPWTjSNW5Tp4Kn7a2p7d66RmuGwubWZWFbr8InIyj8x-TxCGaNVSx5gmsKSY0srehSA2czDXRYD3Ch3mZ5Pu0w3JHiQz_YnupEGchUyqj2NLAclGpK-QnAG5PE7nU18UwRmoX3yKu9Org5lyl7tmhdJceTWxm&gsessionid=Lz4QijQlEeunTGlV42KnC4E0LhaBiKk7cCvdtIW5dUfbzAa2kmHsMg)  
  <sub>Yahoo Finance Singapore, 19 hours ago</sub>  
  How different are three funds that all pitch semiconductor exposure when the news hits AI chips this directly? The latest US move to curb China's access to...
- [How (SMH) Movements Inform Risk Allocation Models](https://www.google.com/goto?url=CAESuwEBxCJF1_c_SQ7mLjjQmaIw0n_xf5E3BqBV_9fn-RIy0B-UMdDF9GIXpoFTKlW41GXYVWS6t2y6abG_R8aDPJunF_hNwMOLNwaM6-ZuYiGL69RCVkVyrTuXF3Oc49_CPRmXN59Ph5KUNpwII86tL_Kt1VcBDNuxlyxdP6-cedGUCReflKs_qhCsy2sTOAh1DGxpTGXzwAa0um_goI9VURDYBRlNYhjfX_4Gk9Ajk-JFGqnFKMwXITgigAOi&gsessionid=Lz4QijQlEeunTGlV42KnC4E0LhaBiKk7cCvdtIW5dUfbzAa2kmHsMg)  
  <sub>Stock Traders Daily, 24 hours ago</sub>  
  Key findings for Vaneck Vectors Semiconductor Etf (NYSE: SMH). Weak Near and Mid-Term Sentiment Could Challenge Long-Term Positive Outlook...
- [Nvidia’s $500B AI Machine Is Getting Bigger. Semiconductor ETFs May Need a Rethink](https://www.google.com/goto?url=CAESuwEBxCJF1x7udB0rxp8cRQk3plaopkNd3WWjyz2og_p-1qezL7MXLNqD1qoedZQQ2q7cc8RmiN29ZskJVYuqGnYwrvwY7tVYb6d7j5T-F3yWl0NI8NQLAhJobpARPse5Kqn0iBw3tMWlF8Fb0jGvQIpR4peMUeRBb_5tsHAiZws5rPtDXQqP8fUfVdXlECfoVtGvsuysf2dXyz0-RlbzugvhdABUhmxP7cNUtOHrVS2Jy0GrKklvsG6a2RA8&gsessionid=Lz4QijQlEeunTGlV42KnC4E0LhaBiKk7cCvdtIW5dUfbzAa2kmHsMg)  
  <sub>Benzinga, 21 hours ago</sub>  
  Nvidia's $500B AI expansion raises a bigger question for investors. These ETFs capture the next wave of semiconductor and AI supply-chain winners?
- [Anthropic IPO Puts AI ETF Exposure in Focus as Valuation Bets Cool](https://www.google.com/goto?url=CAESugEBxCJF15XcIIWQelGOZFCJOCgjk7G8W2uSZjmO7jXxUka1IoQM684rnlNjc2JTMzHZ05RQvBX2JUxesthktHfjGGY-0yujXfDI5A8yV42Vw6yMFv-M1ID6wpec_QThqT61j0SXKQd5jhNuDWbg1pjzJ08ETsNlWPT_57j78XmutVYhvW1zHz74IuHkplpNBK3d-5tmmiMnejNs94CWk1S9IqTUpX_PnDkSFXgPIoTUFc1a8KjpM8xXiqs&gsessionid=Lz4QijQlEeunTGlV42KnC4E0LhaBiKk7cCvdtIW5dUfbzAa2kmHsMg)  
  <sub>TradingView, 2 hours ago</sub>  
  Anthropic's Nasdaq debut on Thursday is giving investors another test of the artificial intelligence trade, as a sharp correction in its private-market...
- [Can NVIDIA's Q3 Beat and Solid View Offset China Curbs & Huang's Exit?](https://www.google.com/goto?url=CAESpwEBxCJF15mcQVC6CyVEBVoDcO0ReN52zmrZVV7JNFdWEFnZRvjoHU8edscHu0vR-qF-t-ylXeauHy44BjGDsjjwbgMFaWCA7sDrYA3Hd6Cu67-6qnmD7ldnDC9AM8HknfraJKrxu7XmDK5DA-_ygzyUbZAzONrH_b9G8iOb-pnlo0_nb0HG96AlKiTDj2BBadC5H58zYjFuohMVt6uBfrN5QzMe-OFmYg&gsessionid=Lz4QijQlEeunTGlV42KnC4E0LhaBiKk7cCvdtIW5dUfbzAa2kmHsMg)  
  <sub>Zacks Investment Research, 24 hours ago</sub>  
  NVIDIA beats Q3 estimates and raises its growth outlook, while China curbs and leadership uncertainty remain watchpoints for investors.
- [Nasdaq Eyes Key Support: Hold Cash Ready for These 7 ETFs](https://www.google.com/goto?url=CAESoQEBxCJF10LBXbYS_xcWiCRmLgubOAFT-H746Mt9pcurTcQE7Z1repymYLTqczqWyr496mt-UgnZDtU2RAwbY3DodpneXdMltM2KKN3DXFvevcVjt37LJN2FS7j0AQR9r_0FlQ8Q9Tu9UNHl6PZemL4Wpl5sFmxQ6agWWTKz0MqQVcbmY8qfh0c52BCQ5hx5-nFscehEQuMaJWxjGdeOSrSRPQ&gsessionid=Lz4QijQlEeunTGlV42KnC4E0LhaBiKk7cCvdtIW5dUfbzAa2kmHsMg)  
  <sub>Investing.com India, 22 hours ago</sub>  
  Market Analysis by Tunç Şatıroğlu covering: Nasdaq 100, S&P 500, Invesco QQQ Trust, iShares Biotechnology ETF. Read Tunç Şatıroğlu's Market Analysis on...
- [Fund Managers Are Dumping Tech Stocks at the Fastest Pace Since 2006](https://www.google.com/goto?url=CAESvAEBxCJF10ZW63hHLgznJ7GZ-yOiiOSWToKyTYDxUqdYcOa5ByhZ2uHDZBzajcLMqAR4O2izH0hw_G2BYrNan-LUBgXgPO9gu7mK5tY3ZVEMVQmfY10E6PT-L76_SjphApskH3m_Y7iHIWz5kNwJWNs1XcS3NyfY37WnQ5Y_mMtanmZvKSit_8rwA2qQ0dZUG0CHS2HI7snwFrzPNcTr_Ab2P_cJOPruJGb00p98_jRaRvvEKGi5cUkBORL2Xg&gsessionid=Lz4QijQlEeunTGlV42KnC4E0LhaBiKk7cCvdtIW5dUfbzAa2kmHsMg)  
  <sub>TradingView, 24 hours ago</sub>  
  Fund managers have rarely felt this good about the economy. They have also rarely been in such a hurry to sell technology stocks.Just 3% of investors expect...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 479.22 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 502.43 (-4.6%), 50d 551.51 (-13.1%), 200d 525.23 (-8.8%); 50d above 200d
Momentum: RSI(14) 41.6 | MACD -24.536 vs signal -23.755 (histogram -0.781)
Returns: 1d +4.3% | 5d -4.5% | 1m -13.9% | 3m -14.5%
52-week range: 325.10 - 668.91 (now 44.8% of the way up)
Volatility: ATR(14) 23.36 (4.9% of price) | annualised 20d 66.1%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: n/a
What it holds: P/E n/a | P/B n/a | P/S n/a | 3y earnings growth n/a
Yield: n/a
Three-year record: n/a a year | beta to the market n/a
Cost and size: expense ratio n/a | net assets n/a
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +5.1% (3.36B) over 7d | 1 month: +13.4% (8.17B) over 34d
Shares outstanding: 144.32M | fund size: 69.16B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- fund equity_holdings unavailable: HTTP Error 401:
- fund bond_holdings unavailable: HTTP Error 401:
- fund bond_ratings unavailable: HTTP Error 401:
- fund fund_operations unavailable: HTTP Error 401:
- fund fund_overview unavailable: HTTP Error 401:
- fund top_holdings unavailable: HTTP Error 401:
- fund sector_weightings unavailable: HTTP Error 401:
- fund asset_classes unavailable: HTTP Error 401:

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise or decisive technical break; bullish analyst view offset by bearish technicals and flat flows.

**Main reasons it gave:**
- Analyst ratings: 100% buy with weighted price target +32.2% above current price
- Technical trend: price below 20‑day, 50‑day and 200‑day SMAs; RSI 39.8 indicating bearish momentum
- Macro: no policy or data surprise; yields stable and VIX modestly higher, neutral backdrop
- Fund flows: share count flat over the past week and month, indicating no net demand shift

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI Turkey ETF (TUR)](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0eebc245416b91b7b9e0a99a0b5e&url=https%3a%2f%2ffinance.yahoo.com%2fquote%2fTUR%2fpress-releases%2f&c=1706393195087887909&mkt=en-us)  
  <sub>Yahoo Finance, 74h ago</sub>  
  The above button links to Coinbase. Yahoo Finance is not a broker-dealer or investment adviser and does not offer securities or cryptocurrencies for sale or facilitate trading. Coinbase pays us for ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 30.82 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 31.14 (-1.0%), 50d 33.55 (-8.1%), 200d 38.41 (-19.8%); 50d below 200d
Momentum: RSI(14) 39.8 | MACD -0.507 vs signal -0.692 (histogram 0.185)
Returns: 1d -1.1% | 5d -3.9% | 1m -4.2% | 3m -24.4%
52-week range: 29.53 - 43.74 (now 9.0% of the way up)
Volatility: ATR(14) 0.60 (1.9% of price) | annualised 20d 31.8%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 11.63 | P/B 1.01 | P/S 0.62 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: -1.4% a year | beta to the market 0.60
Cost and size: expense ratio 0.59% | net assets 146.42M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Aselsan Elektronik Sanayi Ve Ticaret AS 13.3%, Tupras-Turkiye Petrol Rafineleri AS 10.9%, Bim Birlesik Magazalar AS 9.8%, Akbank TAS 6.2%, Turk Hava Yollari AO 4.6%
Sector mix: Industrials 30.8%, Financial services 16.9%, Consumer defensive 12.9%, Energy 10.9%
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
Rolled up from the 5 largest holdings, 44.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +32.2% above the current prices
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
Shares outstanding: 15.65M | fund size: 482.26M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall due to mixed signals: strong analyst buy consensus offset by modest fund inflows, neutral‑to‑bearish technicals, high valuation and yield pressure, and no macro surprise.

**Main reasons it gave:**
- Analyst consensus: 100% buy, price target +15.6% above current
- Fund flows: weekly share count +2.3% (1.58B) indicating modest inflows
- Technical: RSI 49.3, MACD below signal, price below 20‑day SMA
- Fundamentals: P/E 29.56, yield 3.6% vs 10‑yr Treasury 5.09% (valuation pressure)
- Macro: yields stable, VIX up to 22.48, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

- [Vanguard Real Estate Index Fund ETF Shares (VNQ) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/VNQ/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Vanguard Real Estate Index Fund ETF Shares (VNQ) · -1.90% · 3.73% · 0.18% · 6.68% · 7.12% · -13.51% · 90.93%. Key Events. Baseline. Advanced...
- [Where’s the floor for U.S. housing as builder sentiment hits 2012 lows? (VNQ:NYSEARCA)](https://seekingalpha.com/news/4674249-where-s-the-floor-for-u-s-housing-as-builder-sentiment-hits-2012-lows?source=feed_tag_real_estate)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  The U.S. residential construction outlook darkened further this week after single-family building permits fell to a three-year low and homebuilder sentiment...
- [A 71-Year-Old Moved $885,000 Out of CDs and Into Dividend ETFs. Here's What Happened to His $4,126 Monthly Paycheck](https://www.google.com/goto?url=CAES3gEBxCJF16tY029gi-Jr18ZmRVenH9I0lPDgK92zfTVtK8gdHSR08AT2Kdr71XJn7NkcuPeKYgPKuu_JUjWsYYdKz3HeUYdb3TYBqTngJO-RJx52GtLIO-qUtucbxCCFoOrosmGxBGB5D9xtYlgVCTPHHCUWkC_GF5fzTVhxvIE_iENfhA_CrpKCtFNQOCUK-R-WSv8bpfBsGTF_1DWaCQBXUq3mm2z3TTxTg15GG6vrj0o1qmMdmV9zKv8dkpNXO-AOkoyh6dXBaV0eUIPk57j6AB5lE8kkP1QkOLD05jI&gsessionid=QPOvUIhIsn5VWr7dsx4QPtWX0eV9y8YZ8SJsGYduXfH8mm41ygEBhA)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  A 71-year-old retiree moved $885,000 from CDs paying 2% into six dividend ETFs yielding about 6%, lifting his income to roughly $4,200 a month.
- [Buried Treasures: 6 Strong, Undervalued High-Yield REITs](https://www.google.com/goto?url=CAESrwEBxCJF1yJvaYCLxLY9mUy0OS-in9Ltpi-l5HZTs9YktJOKZJySCDiGbSLEnd7La7wHgraAcpxoFsBRVU7CRAd1OtvlbUL9OCNSR89hHRpIfdkC3otLAV4Lx8S4zRbF1JqGFitz4fzSI8-rHU6l_NwWWOK0Jp36RDsyVbLUWvJcwiElXsUQyzVnGXXdNmcGxmmU1g2-4zlsG8VzPUIGl2Lj-zv7g8XEd7M7Ao0P1duQ&gsessionid=QPOvUIhIsn5VWr7dsx4QPtWX0eV9y8YZ8SJsGYduXfH8mm41ygEBhA)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  The bull case for REITs: six candidates are at least 20% undervalued, yield 75 bps above the risk-free rate and pass dividend-safety tests.
- [Retiree Moves $885,000 From CDs Into Dividend ETFs for $4,126 a Month, Taking on More Risk in Retirement](https://www.google.com/goto?url=CAESuwEBxCJF17FocP3Kml0-ixY0bprP4x8AwINFWrtiPoGgO0KB_H9fXma3dvmeD3aDqLsZFRfMRmrH_e8pqpcXJJ9cB8Tc12Ib9G93rI1x8thxlzDYAJMrT6eeI8yJYeFuZ3lBR9lHJN0SYrcSlF6ADHs8P5PySbguEiLszgDgZI5_pkgiItctA0vMRvMqCRkFisEEFNliDDudX-hYNcwaj8NITnePqXeLDw4FHthwipqB3DFO1-fvVmaAzUGQ&gsessionid=QPOvUIhIsn5VWr7dsx4QPtWX0eV9y8YZ8SJsGYduXfH8mm41ygEBhA)  
  <sub>SSBCrack, 21 hours ago</sub>  
  A 71-year-old retiree with $885000 in certificates of deposit (CDs) shifted the money into a mix of six dividend-focused exchange-traded funds, seeking to.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 94.53 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 95.15 (-0.7%), 50d 92.96 (+1.7%), 200d 94.98 (-0.5%); 50d below 200d
Momentum: RSI(14) 49.3 | MACD 0.764 vs signal 0.977 (histogram -0.213)
Returns: 1d -0.7% | 5d -2.0% | 1m +3.3% | 3m -4.0%
52-week range: 87.00 - 100.95 (now 54.0% of the way up)
Volatility: ATR(14) 1.34 (1.4% of price) | annualised 20d 19.0%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Real Estate
What it holds: P/E 29.56 | P/B 2.43 | P/S 4.77 | 3y earnings growth n/a
Yield: 3.6%
Three-year record: +10.5% a year | beta to the market 0.92
Cost and size: expense ratio 0.13% | net assets 69.46B
What it is made of: Stocks 99.4%, Cash 0.3%, Other 0.3%
Largest holdings: Vanguard Real Estate II Index 14.6%, Welltower Inc 8.9%, Prologis Inc 6.5%, Equinix Inc 5.4%, American Tower Corp 4.8%
Sector mix: Real estate 99.5%, Communication services 0.4%, Energy 0.1%, Industrials 0.0%
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
Rolled up from the 5 largest holdings, 40.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.56 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.6% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2026-11-11 UBS: main, Buy -> Buy
  - PLD: 2026-11-02 Wells Fargo: main, Overweight -> Overweight
  - EQIX: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - AMT: 2026-11-05 Argus Research: reit, Buy -> Buy
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
Direction: flat (1 month)
Share count change: 1 week: +2.3% (1.58B) over 7d | 1 month: +0.5% (328.97M) over 34d
Shares outstanding: 732.15M | fund size: 69.21B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break on heavy volume, but strong net inflows

**Main reasons it gave:**
- Share count rose 6.7% in the past week (688.44M) indicating net inflows
- Price 145.40 is below 20‑day SMA (152.22) and 50‑day SMA (153.06) showing short‑term downtrend
- RSI 41 and MACD -1.883 vs signal -0.866 indicate bearish momentum with low volume (0.09× 20‑day average)
- Treasury yields stable; VIX up 3.8 points but no policy surprise, macro unchanged

<details><summary><b>News</b> — score +0.00</summary>

- [Why (XBI) Price Action Is Critical for Tactical Trading](https://news.stocktradersdaily.com/news_release/132/Why_XBI_Price_Action_Is_Critical_for_Tactical_Trading_111826073401_1795048441.html)  
  <sub>Stock Traders Daily, 19 hours ago</sub>  
  Key findings for Spdr Biotech Etf (NYSE: XBI). Weak Near and Mid-Term Sentiment Could Challenge Long-Term Positive Outlook; No clear price positioning...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 145.40 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 152.22 (-4.5%), 50d 153.06 (-5.0%), 200d 143.35 (+1.4%); 50d above 200d
Momentum: RSI(14) 41.0 | MACD -1.883 vs signal -0.866 (histogram -1.016)
Returns: 1d +0.2% | 5d -3.8% | 1m -4.8% | 3m -12.3%
52-week range: 113.83 - 169.55 (now 56.7% of the way up)
Volatility: ATR(14) 4.67 (3.2% of price) | annualised 20d 39.2%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: n/a
What it holds: P/E n/a | P/B n/a | P/S n/a | 3y earnings growth n/a
Yield: n/a
Three-year record: n/a a year | beta to the market n/a
Cost and size: expense ratio n/a | net assets n/a
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.40</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +6.7% (688.44M) over 7d | 1 month: +4.7% (491.50M) over 30d
Shares outstanding: 75.18M | fund size: 10.93B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- fund equity_holdings unavailable: HTTP Error 401:
- fund bond_holdings unavailable: HTTP Error 401:
- fund bond_ratings unavailable: HTTP Error 401:
- fund fund_operations unavailable: HTTP Error 401:
- fund fund_overview unavailable: HTTP Error 401:
- fund top_holdings unavailable: HTTP Error 401:
- fund sector_weightings unavailable: HTTP Error 401:
- fund asset_classes unavailable: HTTP Error 401:

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- XLB price below 20‑day SMA (52.12) and 50‑day SMA (50.85), also below 200‑day SMA (51.25)
- RSI 38.9 and MACD negative indicate weak momentum
- Volume 0.18× 20‑day average, showing low participation
- Fund flows flat (0% change) over the past week and month, indicating no net demand
- Macro backdrop unchanged: Treasury yields stable, inflation 3.7% in line with expectations, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://au.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance Australia, 4 hours ago</sub>  
  Find the latest State Street Health Care Select Sector SPDR ETF (XLV) stock quote, history, news and other vital information to help you with your stock...
- [LyondellBasell Stock Outlook: Is Wall Street Bullish or Bearish?](https://www.barchart.com/story/news/8914191/lyondellbasell-stock-outlook-is-wall-street-bullish-or-bearish)  
  <sub>Barchart.com, 2 hours ago</sub>  
  LyondellBasell has outperformed the broader market over the past year, and analysts are moderately optimistic about the stock's prospects.
- [VCR: Consumer Discretionary Sector Dashboard For November (NYSEARCA:VCR)](https://www.google.com/goto?url=CAEStwEBxCJF18Bk5pO8SoZB2UcyyZSbG3HHKuAMnh_ZUTXTS73KzMzMh6b5mKgOytCCx_0kSQWXGfkDWjzoyMR4gGyR9JVb_9jH2eFM5gUXMngvhdokFHPg1PY2Ncsz8jFJ0cu4PngZdtcDgAQXbxZpWiriCyXBikmrpBpFPDsrmTS3VeIszfOvZiZs3RF3flYr8eAQrm92rV7LHegZMGITCHO8P8Zc_Jet-IMpzQDWdrNylck38FXMhqs&gsessionid=xrSMT02lqMWmY-OIz-qYpUafEau-rgyIGeC_hi-G5CoaH2BCU2FrJA)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Vanguard Consumer Discretionary ETF offers a broader portfolio, slightly better value, and returns than XLY, with equivalent long-term risk-adjusted...
- [(XLB) Trading Strategy and Analysis (XLB:CA)](https://www.google.com/goto?url=CAESmAEBxCJF15mKK4RLHKBLRMNiXbsWxh0rknvuJw3Furnln4CryEyXyH3-VMbP4pDi-LR4SIuT722_Dxq5dM-egpt22lyvyXJpr2PXOUozaAiWd-_YDEm2sLGBZ_fSszTQXZtBLjtiz-cgcOQj6PtKFuoWYy3NQuS2P5EVFY0VtEL6ADKoXnmezCriSNLbkqkfltGIwF_QJUBHjQ&gsessionid=xrSMT02lqMWmY-OIz-qYpUafEau-rgyIGeC_hi-G5CoaH2BCU2FrJA)  
  <sub>Stock Traders Daily, 11 hours ago</sub>  
  Trading Strategy and Analysis for iShares Core Canadian Long Term Bond Index ETF (XLB) with Buy/Sell Signals.
- [Do Wall Street Analysts Like International Flavors & Fragrances Stock?](https://www.google.com/goto?url=CAESrAEBxCJF1yayfxDSYb-OnxykWdJqdDKrYupWGjlu3x1a-7_FpMCoyKrIbYELA3Np6k9HUtbRvOAEdvPvBtGgCIbWe_6IWNjP68eEf8VYfxlBMu_5BwtngYZyxSVQewRwHbjOXEqpHpg2JUE1GMz0DWlms1fPH7CvSZphokJpBbJFmf1IW3FTT5l0-ZWLVmU2JH_nI4fLRUygK3M0h28IylhUQ4-Vz-OsPq3Sf6zI&gsessionid=xrSMT02lqMWmY-OIz-qYpUafEau-rgyIGeC_hi-G5CoaH2BCU2FrJA)  
  <sub>Barchart.com, 1 hour ago</sub>  
  International Flavors & Fragrances Inc. (IFF), headquartered in New York, produces and markets cosmetic active and natural health ingredients for use in...
- [State Street Utilities Select Sector SPDR ETF (XLU) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZAHEIkXXgQHdQ33jqjNprqEOlg6KRwBQQZLsUjsQEm2-ObsLmMU6DtHAIwamVC-6Pcuhf-wXHjPeENfyFphxeNKGAuGH--R04E_myH-4U2h2HB5tr5pDrq9RvYVi3-UVUnkM_24&gsessionid=xrSMT02lqMWmY-OIz-qYpUafEau-rgyIGeC_hi-G5CoaH2BCU2FrJA)  
  <sub>Yahoo! Finance Canada, 13 hours ago</sub>  
  Find the latest State Street Utilities Select Sector SPDR ETF (XLU) stock quote, history, news and other vital information to help you with your stock...
- [Growth Leads Sectors In Wednesday Trading As Cyclicals Trail](https://www.google.com/goto?url=CAESzAEBxCJF1_2S0c_sqJJozw6bf6nsZxYC4FuZsU8RBi7KK05G84y9rvmB1Rmt5M13IDVAbDCJARQLJvwKu86FUeqVLAQMHGzlbpWQ0R7PuFr7SF__SxGZacGBmurkHDSopXbaKLMhVWOEJfUIjD23T_iHEXukG4JQMVW0YfWhDgauC2szeUiDhP_j7peX_nOShwjvj7ias2gggzP8oYNaz9bPVdGCsLz0uCe7E9MtjvmXg2182rTuLLcmaLWNFdyRFG4AN1GBgsTxxy6eDlk&gsessionid=xrSMT02lqMWmY-OIz-qYpUafEau-rgyIGeC_hi-G5CoaH2BCU2FrJA)  
  <sub>Benzinga, 23 hours ago</sub>  
  Five sectors are trading higher and six are lower in Wednesday's regular session, with growth sectors holding the top three positions.
- [iShares 20+ Year U.S. Treasury Bond Index ETF (CAD-Hedged) (XTLH.TO) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESaAHEIkXXSNxvlbw2_jUPgj7_4HLpRYb-eF8ffJ4P0O1q6kB-zjcus1jihRSyrWJriY5YqMIs3Znv44NXGDsOhn90SEU0o3psSC7OUXETXOh99nV15dTijPX6ExBnLeCdYB4EP4BVEHvb&gsessionid=xrSMT02lqMWmY-OIz-qYpUafEau-rgyIGeC_hi-G5CoaH2BCU2FrJA)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Find the latest iShares 20+ Year U.S. Treasury Bond Index ETF (CAD-Hedged) (XTLH.TO) stock quote, history, news and other vital information to help you with...
- [Retailers Led A Split Day For Consumer Stocks](https://www.google.com/goto?url=CAEShwEBxCJF10MvSoWgjQ1dzChFA6n9a5UzaDrlm8XNHxz9iGGkTKq9QvtZi3TmBq-KujEWJJNEcN-Tka7h_0tfppevlqJ1zApSWVB9nTLuP01eAQqNFMSlsx-aCvnhp8IVwLarXXOR_gDIjZ4V9ixjez6zbnCP__b56sSaP6p3FpeaiugyN2FSYuY&gsessionid=xrSMT02lqMWmY-OIz-qYpUafEau-rgyIGeC_hi-G5CoaH2BCU2FrJA)  
  <sub>Finimize, 17 hours ago</sub>  
  Target and TJX lifted forecasts after strong Q3 sales, while Lowe's margins slipped and XLP lagged XLY.
- [5 Consumer Discretionary Plays Showing Strength During the Tech Sell-Off](https://www.google.com/goto?url=CAESnwEBxCJF1-WMYrZQclK9nKo_4SKrgi8PJwSfGdhfzr3mJ4ifNhi9FW8dCCbwZZKK6bGnOi28NmgWyJ1DX-vjSQ8-MpIwRhlhshnEoIZJfHwLa5j_4GzJN_g9ZdNVJwfEKLvESP6baW_u2LH9tUm1LRjpQGE81DUpuN7z3tb9JsM4JQd4SPgAQFyIKwhLtsN4uhwqFsQt0cx4-SxA6--2QHo&gsessionid=xrSMT02lqMWmY-OIz-qYpUafEau-rgyIGeC_hi-G5CoaH2BCU2FrJA)  
  <sub>inkl, 23 hours ago</sub>  
  As semiconductors sell off and NVIDIA sees a leadership shake-up, the XLY consumer discretionary ETF has gained ground, with Amazon, Starbucks, Royal…

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 50.15 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 52.12 (-3.8%), 50d 50.85 (-1.4%), 200d 51.25 (-2.1%); 50d below 200d
Momentum: RSI(14) 38.9 | MACD -0.031 vs signal 0.323 (histogram -0.354)
Returns: 1d -0.6% | 5d -4.2% | 1m -2.3% | 3m -6.3%
52-week range: 42.23 - 53.90 (now 67.9% of the way up)
Volatility: ATR(14) 0.90 (1.8% of price) | annualised 20d 21.5%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: n/a
What it holds: P/E n/a | P/B n/a | P/S n/a | 3y earnings growth n/a
Yield: n/a
Three-year record: n/a a year | beta to the market n/a
Cost and size: expense ratio n/a | net assets n/a
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 71.92M | fund size: 3.61B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- fund equity_holdings unavailable: HTTP Error 401:
- fund bond_holdings unavailable: HTTP Error 401:
- fund bond_ratings unavailable: HTTP Error 401:
- fund fund_operations unavailable: HTTP Error 401:
- fund fund_overview unavailable: HTTP Error 401:
- fund top_holdings unavailable: HTTP Error 401:
- fund sector_weightings unavailable: HTTP Error 401:
- fund asset_classes unavailable: HTTP Error 401:

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Energy inventories all showed builds (crude +3.4M barrels, natural gas +61 Bcf) indicating bearish supply pressure
- EIA price outlook forecasts WTI to fall ~13% over six months, supporting a bearish view
- Technical indicators show price below 20‑day and 50‑day SMAs, low RSI (37.7) and negative MACD, indicating weak momentum

<details><summary><b>News</b> — score +0.00</summary>

- [1. Consumer Discretionary Select Sector SPDR Fund (NYSEARCA:XLY)](https://kalkine.ca/by-topic/mutual-funds-etfs/which-of-the-five-sector-funds-shows-the-best-setup-after-november-18-energy-select-sector-spdr-fund-nysearcaxle-health-care-select-sector-spdr-fund-nysearcaxlv-financial-select-sector-spdr-fund-nysearcaxlf-technology-select-sector-spdr-fund-nysearcaxlk-or-consumer-discretionary-select-sector-spdr-fund-nysearcaxly)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  Which of the Five Sector Funds Shows the Best Setup After November 18: Energy Select Sector SPDR Fund (NYSEARCA:XLE), Health Care Select Sector SPDR Fund...
- [Europe’s clean-energy push deepens dependence on Chinese technology (XLE:NYSEARCA)](https://seekingalpha.com/news/4674359-europe-s-clean-energy-push-deepens-dependence-on-chinese-technology)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  The EU proposes favoring local clean-energy equipment in public contracts, as China makes at least 80% of solar products and batteries.
- [3 Funds With Oil And Gas Exposure as Brent Holds Near $93](https://www.google.com/goto?url=CAESpAEBxCJF14IIhD7xmBoE6kAmjn4NQEC82YPaiK191bR9F2LDCVCh-49146ZZswCLb-7xXAECYnfPwAN8k5IeDfnt08DWznamg8sB9Sfddr7Y2q1zCVbwMHjIg46Tzzon21VSbRjMC1Jcu0Ar_JCESdNsFe3hahsAsTeITKpGs6vdvxUNfaWlTvZc1eZCT6mxG5FBiFyoFRTZnLqtBHROSQyFBazoyg&gsessionid=3fXoosPsQE5FMCiDN4uVIAhVHxF0nHeEH9dsa2hJbUjjCPlzPI6h3w)  
  <sub>Simply Wall St, 23 hours ago</sub>  
  How different can three funds tied to the same oil and gas theme really be, and why does that difference matter when Brent is stuck near US$93?
- [SPDR Gold Shares (GLD) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESYwHEIkXXTqtjpIudeajnVWarfdo5ik8ojFIavf5Q3dYBm6cIjQH2ZDbU-x-_OlCgQJre-wnWS8lgm36GEkzZ8iJdTOCEmBUCpYTaBZ5odshoTckafFgjYvCB3PGXuhYvJmVi3w&gsessionid=3fXoosPsQE5FMCiDN4uVIAhVHxF0nHeEH9dsa2hJbUjjCPlzPI6h3w)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Find the latest SPDR Gold Shares (GLD) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [U.S. shale producers speed up payouts as oil windfall fuels buybacks (XLE:NYSEARCA)](https://www.google.com/goto?url=CAESpQEBxCJF18rqMdPaEfQZb-d123S0TkUVAsz6EwBix--EeTRJ3T0M3KH2TKTSaTaZqtHMgCk13My14Nr--3Yaa22puSBao6YTgS0n6GWpfWl1W1kv4rI4sK5q9NoxwiIP8qoIKrps1vF7HUV695WO6cQ3HnWuunt7HRlk9iKoVHAjpN3UmzkPQmjFmXRKPn_fpISurbtLVchgNWq-4S2BgTxtJHDiaDI&gsessionid=3fXoosPsQE5FMCiDN4uVIAhVHxF0nHeEH9dsa2hJbUjjCPlzPI6h3w)  
  <sub>Seeking Alpha, 55 minutes ago</sub>  
  Six U.S. shale producers return $7.25 billion through dividends and buybacks in Q3, up 41% year over year, while keeping 2027 output growth modest.
- [What share and ETF investors are doing with their money as economic blows rain down on the Australian economy with inflation surging, corporates cutting jobs and rates up](https://www.google.com/goto?url=CAES-QEBxCJF19ISsBdqVM0JyEL5DTI-Vw4QuTiZ0fuVDCwWCiJ5zfPicBlkVOX-gMLLpYYQj8WFgZUHWVe-VzbWwnWilIsOVVaWxBEoDdU9HPpvEsrd_ewd16G_NlUQ2PlMOXF63xQUIeEu6bRPzmjfvkE7rTLZCm-XFU5dycyEULhOS9hxS38j36Oc1hX3ES0cSNXXUl7vsDzjdnikB-j5_-9lJXD-oQQ-ogUrKdPqgziEY0qQSkji0OX8jXz1I_YQnLYUPE6FA16NTdgSQ8pAxXQ5dbsmT_nXLMww7DniWwjdMdvHKOI5DuJEXbdYBCqDyGhbIeSIqaNZw9g&gsessionid=3fXoosPsQE5FMCiDN4uVIAhVHxF0nHeEH9dsa2hJbUjjCPlzPI6h3w)  
  <sub>Daily Mail, 11 hours ago</sub>  
  It feels like the hits won't stop coming for the Australian economy. House prices are plunging, inflation is surging, the cash rate has risen five times...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 61.46 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 65.08 (-5.6%), 50d 64.80 (-5.2%), 200d 59.70 (+2.9%); 50d above 200d
Momentum: RSI(14) 37.7 | MACD -0.959 vs signal -0.554 (histogram -0.405)
Returns: 1d +0.3% | 5d -4.5% | 1m -9.8% | 3m -3.4%
52-week range: 43.81 - 70.02 (now 67.3% of the way up)
Volatility: ATR(14) 1.54 (2.5% of price) | annualised 20d 32.7%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.40</summary>

```text
Fund type: n/a
What it holds: P/E n/a | P/B n/a | P/S n/a | 3y earnings growth n/a
Yield: n/a
Three-year record: n/a a year | beta to the market n/a
Cost and size: expense ratio n/a | net assets n/a
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
US inventories, week ending 2026-11-13 (published the following Wednesday)
  Crude oil: 417.8 million barrels, +3.4 on the week (a build), 25% percentile over 52 weeks
  Petrol: 215.9 million barrels, +5.2 on the week (a build), 56% percentile over 52 weeks
  Diesel: 104.9 million barrels, +1.6 on the week (a build), 33% percentile over 52 weeks
  Natural gas: 3,862.0 billion cubic feet, +61.0 on the week (a build), 94% percentile over 52 weeks -- high for the time of year
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
Shares outstanding: 186.42M | fund size: 11.46B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- fund equity_holdings unavailable: HTTP Error 401:
- fund bond_holdings unavailable: HTTP Error 401:
- fund bond_ratings unavailable: HTTP Error 401:
- fund fund_operations unavailable: HTTP Error 401:
- fund fund_overview unavailable: HTTP Error 401:
- fund top_holdings unavailable: HTTP Error 401:
- fund sector_weightings unavailable: HTTP Error 401:
- fund asset_classes unavailable: HTTP Error 401:

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fed minutes hinted at more rate hikes but no policy surprise this week
- Technical indicators: price below 20‑day SMA, RSI 47.1, MACD histogram negative, low volume
- Fund flows flat over the past week and month, indicating no net demand
- Macro: yields stable, VIX elevated but no surprise data releases
- Motley Fool article recommends XLF as rate beneficiary (ignored as direct recommendation)

<details><summary><b>News</b> — score +0.00</summary>

- [Financial Select Sector SPDR ETF (XLF) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/XLF/)  
  <sub>Yahoo Finance UK, 14 hours ago</sub>  
  Financial Select Sector SPDR ETF (XLF) · -3.77% · 1.62% · 9.05% · 3.01% · 9.83% · 43.02% · 196.14%. Key events. Baseline. Advanced chart. Loading chart...
- [State Street Financial Select Sector SPDR ETF Futures Price | XLF Perpetual Price, OI & Funding](https://www.coinglass.com/currencies/XLF)  
  <sub>CoinGlass, 11 hours ago</sub>  
  State Street Financial Select Sector SPDR ETF is $56.568 today, −1.43% in 24h. Plus a live XLF chart, candlesticks and a currency converter.
- [State Street Financial Sel Sec SPDR ETF (Derivatives) price today, XLF to USD live price, marketcap and chart](https://www.google.com/goto?url=CAESlgEBxCJF193j1O8QiGCG3Og-0QTKsIxRqjfMNVvr7Qy1dHTnb6IfGEk3Ji3OaFK007rvMOffDzFf5IUPSZJBZGXmOel5ZteJfd5VO4i2pKRPfABsyZX5tUQp1TgDLO9CPFsl6AI1-LU_DlSvpSgq80DX-Ol4hSq33g2f2_e9_X3KUA1odfxTvkFrzQr5ptn-AABWTTHALDs&gsessionid=7i1BYEIKxJ04cC0j8CgAfBfphOR4YSR_aRB9EPhgW1JWoxALKaFbnw)  
  <sub>CoinMarketCap, 11 hours ago</sub>  
  The live State Street Financial Sel Sec SPDR ETF (Derivatives) price today is $56.30 USD with a 24-hour trading volume of $0 USD. We update our XLF to USD...
- [1. Consumer Discretionary Select Sector SPDR Fund (NYSEARCA:XLY)](https://www.google.com/goto?url=CAESpwMBxCJF19xzHjxm2mexb8ACMK6AOu4-gMxy8oyJdIqkHd0u9GwIWgdY0731LXP2YigPalK5F6SuAWP44NiVLa6PyEubOh6WlAXJKJfohLqTWJtmWY-20VTfrobxkM1cubHtjcqvDAHFWQ7sRMr2zhLhw_7Bw_ua9MpfnwVkr-BTakiLmhfyHUNu9U1aC8RIJ3t0r3RsPmkslG9CSQ4yarn2mT-vGaf7isWSD5lZjQfHetCd3e1Ejwg8aOvsw6evdEAF45eZLdCY5P0VzByjulyYD7sbrNP88vMnG18Njv77Lt_YfcPdjcJfG9zUxEGetn1ZsDieUEvrXzyNukSUtoPORqNlMFiqsamuReLmYtqvjQqPNMGL9Ot1O6m7ECm7D2UXYL7MPmGV-oHvKX2fl5HVURoLpokjXwxX4UFD2QJdB8iap-hdlyU2tuWlaom0xD6EgfQjdaxcPQxaV1gk_AllanGgMaYxM0Ii41xR4Ck59rYyFFPncOxsO6LXNsO9oT4m8tWysrvlmdjxGm1XwRSzXAiCILi2IT-nGZA15pQeyZYJ30Orz_o&gsessionid=7i1BYEIKxJ04cC0j8CgAfBfphOR4YSR_aRB9EPhgW1JWoxALKaFbnw)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  The sector's 1.79% advance came from two sources, which gives the Consumer Discretionary Select Sector SPDR Fund (NYSEARCA:XLY) the best setup.
- [Financial sector ETF XLF underperforms despite rising rates; history suggests potential for gains ahead.](https://www.google.com/goto?url=CAESrAEBxCJF13RxwKVqXCd-k_0c45MHDQNBjsDJl2Ba1cH-7AQONtclVOQ2KsW0oB8ZuY4D9GxmoVi4ezoRJIIDN_4EIKYEwHo43R7D40rjPY1nT3Z_vWumhEpylp_V9e1xAg0TcVn03CJx973rkhv9hY2D3AUhmre7W4cjKNinWit52-Ii8WNkWNPHCxiLlXeAZcCgtL10CDUuxdy-QU81Lj-M2GenkkBpTNBhs-lo&gsessionid=7i1BYEIKxJ04cC0j8CgAfBfphOR4YSR_aRB9EPhgW1JWoxALKaFbnw)  
  <sub>Pluang, 23 minutes ago</sub>  
  The State Street Financial Select Sector SPDR ETF (XLF), a major financial sector fund, has underperformed this year despite a rising interest rate...
- [If the Fed Raises Rates Again in December, Here's the 1 ETF I'm Buying Without Any Hesitation](https://www.google.com/goto?url=CAESwwEBxCJF13ECyq_j7sSM-lHg1KilYI_xBJ4kz8Wd5kmGEqYYVXG4RWUmy-q55cO8SIZMiYNfDN9vGtrROHlAyDfNQQQGu1ZCR0eLu7YNpomuAKlTV2nmyOSKJSoBFq1peupxphWJSfEM336yPLeweZZUVm4GGOoctnBD30qGIpkiDPFEILuL1RbGazsjf1U4fopirKLiUnCwEmsat2ioyK-azkxtN-sEFZcRg5wzil6Y4_9Z8N0LiISdZuB_77H-G25Q5MY&gsessionid=7i1BYEIKxJ04cC0j8CgAfBfphOR4YSR_aRB9EPhgW1JWoxALKaFbnw)  
  <sub>The Motley Fool, 1 hour ago</sub>  
  The State Street Financial Select Sector SPDR ETF makes for a logical beneficiary of rising interest rates.
- [Fed Minutes Kept Bank Stocks On Edge](https://www.google.com/goto?url=CAESfgHEIkXX_Gt-VGifp7h-OkY9CA73ulrW7W-KBGdNJHFxw3CAbWeTOH7aN2AKCj9Puy52xizOxoj8h2dJ_ZviEaT8msOTdK7E-tAuvhD1-EaTssB0x-BlLRq81_G-8wMvpuOAWHjYsYJwtTkH-umm1WAEx4togy-_J3pfVnQOOQ&gsessionid=7i1BYEIKxJ04cC0j8CgAfBfphOR4YSR_aRB9EPhgW1JWoxALKaFbnw)  
  <sub>Finimize, 18 hours ago</sub>  
  Traders digested hints of more rate hikes, while pending home sales fell 4.7% in October.
- [56.75 [XLFUSDT] Futures, USDT-Margined Perpetual Contract | MEXC](https://www.google.com/goto?url=CAESYQHEIkXXDTRix3XkEdzaCST7JmB7HP6rzee8UqjXvEQq4hNGKwywO96AhT3N1vJwWIIbBHI6OX7UhG80A0uoMT17ajWXFY_Ypk-qKXASXgKhJZUaxSlM8naERi1E5E7XFvA&gsessionid=7i1BYEIKxJ04cC0j8CgAfBfphOR4YSR_aRB9EPhgW1JWoxALKaFbnw)  
  <sub>mexc.co, 5 hours ago</sub>  
  Trade XLFUSDT Futures on MEXC with ultra-low fees, deep liquidity, and up to 20x leverage. Experience lightning-fast order execution and top-tier security...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 56.52 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 57.30 (-1.4%), 50d 55.94 (+1.0%), 200d 54.01 (+4.6%); 50d above 200d
Momentum: RSI(14) 47.1 | MACD 0.384 vs signal 0.584 (histogram -0.200)
Returns: 1d +0.2% | 5d -2.9% | 1m +0.9% | 3m -1.7%
52-week range: 47.81 - 59.20 (now 76.5% of the way up)
Volatility: ATR(14) 0.86 (1.5% of price) | annualised 20d 22.8%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: n/a
What it holds: P/E n/a | P/B n/a | P/S n/a | 3y earnings growth n/a
Yield: n/a
Three-year record: n/a a year | beta to the market n/a
Cost and size: expense ratio n/a | net assets n/a
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 883.44M | fund size: 49.93B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- fund equity_holdings unavailable: HTTP Error 401:
- fund bond_holdings unavailable: HTTP Error 401:
- fund bond_ratings unavailable: HTTP Error 401:
- fund fund_operations unavailable: HTTP Error 401:
- fund fund_overview unavailable: HTTP Error 401:
- fund top_holdings unavailable: HTTP Error 401:
- fund sector_weightings unavailable: HTTP Error 401:
- fund asset_classes unavailable: HTTP Error 401:

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Flat fund flows (0.0% change) over the past week and month; Technical trend below 20‑day, 50‑day, and 200‑day SMAs indicating downtrend but no decisive break on heavy volume; Macro data unchanged: Treasury yields stable, inflation 3.7% and unemployment 4.1% within expectations

**Main reasons it gave:**
- Flat fund flows (0.0% change) over the past week and month
- Technical trend below 20‑day, 50‑day, and 200‑day SMAs indicating downtrend but no decisive break on heavy volume
- Macro data unchanged: Treasury yields stable, inflation 3.7% and unemployment 4.1% within expectations

<details><summary><b>News</b> — score +0.00</summary>

- [Build, Run, Harvest: The Just-In-Case Cycle Is Moving On (NYSEARCA:XLI)](https://seekingalpha.com/article/4969780-build-run-harvest-the-just-in-case-cycle-is-moving-on)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  After the pandemic, companies swore they would never again be caught with empty shelves. Six years into the just-in-case era, the data show how the cycle is...
- [Financial Select Sector SPDR ETF (XLF) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/XLF/)  
  <sub>Yahoo Finance UK, 14 hours ago</sub>  
  Find the latest Financial Select Sector SPDR ETF (XLF) stock quote, history, news and other vital information to help you with your stock trading and...
- [3 ETFs For AMD After Its OpenAI News গল্প](https://www.google.com/goto?url=CAEStwEBxCJF10hD1nrSum9rvriVrt-Ydv-vSprvzSwOJC2hk9yKBDP1Yp67waZGTTIqyO8vgWQFMWy0qa_rTGVgIQPdsSIJO-OHe_SUFV5hoxGVSw3XZWlBj5Tz5h1nNyzL8O8G72BmR7vqTP9A8OnMowXAPrQEksv1xN5NyC573OC8KqJrMyjVcarSyF2oaepdFqatETNddZD3XhyUiduBgrQuBZYO1z-Crw12ibZHjxCbLoDIHi1CUW8&gsessionid=QBHD2gokSlxqYh9lMy25W8SrcCGj6v6--lRHx37Kcot6zqq9urFexw)  
  <sub>Simply Wall St, 3 hours ago</sub>  
  You might like Advanced Micro Devices for its chips and artificial intelligence work, but holding the stock on its own means living with its specific risks.
- [State Street Utilities Select Sector SPDR ETF (XLU) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZAHEIkXX8ytRtQxMJN9EdD3FengibYxgPwLz7ouuEeJYTLQ5lA1bWmzFtDETlBznfQJQP9QfKOJ6Wah6nbR7ZHrBmxy2r78VBZqk-wjyTsOKnBFh8peqxjl50YAvp62AxytAHRQ&gsessionid=QBHD2gokSlxqYh9lMy25W8SrcCGj6v6--lRHx37Kcot6zqq9urFexw)  
  <sub>Yahoo! Finance Canada, 13 hours ago</sub>  
  Find the latest State Street Utilities Select Sector SPDR ETF (XLU) stock quote, history, news and other vital information to help you with your stock...
- [Why Morgan Stanley Says the S&P 500 Is Poised to Jump 18%](https://www.google.com/goto?url=CAESnwEBxCJF1-Arp9y_BwA3KAa65PB4Xnx7FSiqHZ6ZPJ22e6ZnzBM6haFB1uOURuTQVrKF7Ngx0GxQKSz-A0f_VLE-vjrbIp21lG9pmRWHObFWnOXSMK4OD__YXWdHhGacoUe_pr7keIq3732Z8hwTOzvHEW8gNCQ3gg4qOMkP2-zENQpWRJ2XfCGgoU-aOFjBM-RL0HUii-qIqz2sfNl5uI4&gsessionid=QBHD2gokSlxqYh9lMy25W8SrcCGj6v6--lRHx37Kcot6zqq9urFexw)  
  <sub>Business Insider, 5 hours ago</sub>  
  The stock market is serving up a meatball for investors to hit out of the park, Morgan Stanley's Mike Wilson says.
- [Automatic Data Processing Stock: Analyst Estimates & Ratings](https://www.google.com/goto?url=CAESogEBxCJF16pxxgDpD_vI7JqoP2KLT0kujUTuWZRSGcvRdBZHqz88H_Dm6HDehQq609L6YZenpQrODCHnwa4ZsxE2eWAGDFLeufOlNGqsvQoAgSG-mo-T5UEslshNqWKycrSojUI4ePI8cOwtLetvKto3S6dxmKiXXjRgX7udXNn9VHytTz-rh8tmZup6uITvrqQXi72ywcU0hdNR9txsA6Kn1bc&gsessionid=QBHD2gokSlxqYh9lMy25W8SrcCGj6v6--lRHx37Kcot6zqq9urFexw)  
  <sub>Barchart.com, 16 minutes ago</sub>  
  Automatic Data Processing has outperformed the broader market over the past year, but analysts are cautious about the stock's prospects.
- [Defensive ETFs Beat Nasdaq, But Wall Street Isn't Rotating Yet - State Street Health Care Select Sector S](https://www.google.com/goto?url=CAESyAEBxCJF13lZGs2E9WomTN6dJRuj6EVSJesXitE-MpH8pfmocTuEJ47H9UyUNxtXo1kSbydIXXm8HJhDeg_Iw9t67NUsUzb0CNa34natN-U2r58Vl_7ARoh6LELrWGd59VCbv1V5oPINk2TDWGV-sbvZIE-tKJtT9VRpbfkh5jbXumI8ozgyw40xG8yYWZYkgi4PSTCPjPAmBYhHTe-SazSTbuWjlqBC3V7Bf0hBj6SKXpS_H_PJWFpn9807uKMYXmAcxNXhAKTnbA&gsessionid=QBHD2gokSlxqYh9lMy25W8SrcCGj6v6--lRHx37Kcot6zqq9urFexw)  
  <sub>Benzinga, 2 hours ago</sub>  
  XLV was trading slightly lower in premarket trading Thursday as defensive stocks outpaced technology shares over a longer period. But ETF investors aren't...
- [Fund Managers Are Dumping Tech Stocks at the Fastest Pace Since 2006](https://www.google.com/goto?url=CAESvAEBxCJF17hq9QOMMW6edsBV5laEYiSKEpZDVcIIL2K8GQ6pbFe1JDwEXvN9AhuJnPHBRzYKqDtBBAh2nzz6HoxSdNieqx00-lJbG5LOzlGcYdX_JekbhTxTce4PUIdchu2pgVIqME4rnRYZOeHZZ9SnaTp0V9I9OBtcGtcXvJ1SSiTXyGRt_w3j1yp5NIYDtYeTDDHNUgVnTGvg6kzV61GneWTgly165cvt3l_mLHshRwoWPcPvf4fuaF7Dzg&gsessionid=QBHD2gokSlxqYh9lMy25W8SrcCGj6v6--lRHx37Kcot6zqq9urFexw)  
  <sub>TradingView, 24 hours ago</sub>  
  Fund managers have rarely felt this good about the economy. They have also rarely been in such a hurry to sell technology stocks.Just 3% of investors expect...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 164.83 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 167.39 (-1.5%), 50d 168.32 (-2.1%), 200d 173.40 (-4.9%); 50d below 200d
Momentum: RSI(14) 43.3 | MACD -0.879 vs signal -0.620 (histogram -0.259)
Returns: 1d +0.1% | 5d -2.7% | 1m -2.1% | 3m -8.6%
52-week range: 147.83 - 186.51 (now 44.0% of the way up)
Volatility: ATR(14) 2.99 (1.8% of price) | annualised 20d 25.7%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: n/a
What it holds: P/E n/a | P/B n/a | P/S n/a | 3y earnings growth n/a
Yield: n/a
Three-year record: n/a a year | beta to the market n/a
Cost and size: expense ratio n/a | net assets n/a
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 136.63M | fund size: 22.52B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- fund equity_holdings unavailable: HTTP Error 401:
- fund bond_holdings unavailable: HTTP Error 401:
- fund bond_ratings unavailable: HTTP Error 401:
- fund fund_operations unavailable: HTTP Error 401:
- fund fund_overview unavailable: HTTP Error 401:
- fund top_holdings unavailable: HTTP Error 401:
- fund sector_weightings unavailable: HTTP Error 401:
- fund asset_classes unavailable: HTTP Error 401:

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fund flows: +12.1% share count increase over past month (13.21B) indicating net inflows
- Technical indicators: price below 20‑day, 50‑day, and 200‑day SMAs; MACD below signal; RSI 42; low volume
- News: fund managers dumping tech stocks at fastest pace since 2006; defensive ETFs outperforming
- Macro: no policy or data surprise; yields stable, VIX elevated but no clear catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [Defensive ETFs Beat Nasdaq, But Wall Street Isn't Rotating Yet - State Street Health Care Select Sector S](https://www.benzinga.com/etfs/sector-etfs/26/11/63423089/defensive-sectors-beat-nasdaq-100-by-22-8-points-but-etf-flows-tell-a-mixed-story)  
  <sub>Benzinga, 2 hours ago</sub>  
  XLV was trading slightly lower in premarket trading Thursday as defensive stocks outpaced technology shares over a longer period. But ETF investors aren't...
- [3 ETFs For AMD After Its OpenAI News গল্প](https://simplywall.st/stocks/us/semiconductors/nasdaq-amd/advanced-micro-devices/news/3-etfs-for-amd-after-its-openai-news)  
  <sub>Simply Wall St, 3 hours ago</sub>  
  You might like Advanced Micro Devices for its chips and artificial intelligence work, but holding the stock on its own means living with its specific risks.
- [1. Consumer Discretionary Select Sector SPDR Fund (NYSEARCA:XLY)](https://www.google.com/goto?url=CAESpwMBxCJF19zcxhiSrglCBrwL91uu56l_SWVT3yNRJsuFqir9gbG-iCmh22JUFPWt-ZZEmq-BDCSyK91m03qftVemK2aeZWqbkVUKRjjjMKlAdxS7NvL99J8LD14nn1sFeoNMNu-2RIBKBCRAZIhDTkH8ReFtbsX59ME5w4bxOwK8r7QmBuixb3YUTmx2I3qmO4RwQ-IK9_wExIvCc0rXJkkHR-7tM-VBLXhnK3U8PDRE4JXEzoGvLC_DGikYx3pSoYgw8EwPgNl-355mbWkroyN7WlgxgyZvjyeOyeD-4HLfcMCc5v5mGqIZaPRHYT63sV0aKIHGh6l8auPwqs4hRoomq4LPjJ2vvH51KEW3tBfPYtFH7wRnuDC2sefF2El2bWZjX3T1hNfdrxSJAIk6LVHj7uzfc6DQpqRoz5EzLBUl-Ak4s6Z3mRda_cvw_BjvrFxy2OIYTnbugCBSNPkp2dj_ez7PbsnVgcbHUX_qUadKCsMWFejdRpzvCx5w91fK1MRm0h7U5hxjysaHYo1ZsFzU2289G9dcPOi1XRw029IVLkmqmKW0RlE&gsessionid=KSPBRzIehC6M4rjg-hIOMjsLgfxXvWkXiW1ENKuWqLBIfr_MYyGI6Q)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  The sector's 1.79% advance came from two sources, which gives the Consumer Discretionary Select Sector SPDR Fund (NYSEARCA:XLY) the best setup.
- [Fund Managers Are Dumping Tech Stocks at the Fastest Pace Since 2006](https://www.google.com/goto?url=CAESvAEBxCJF14sria0qd75i5SPKUArNyYIXMg5PMfvnKIjGb-FniLkJ1Z2Zqf8erTPQwfCFcJ_b9c3CV094RIC7jrNn_c7eSk-6Z_3ZpVpz6_g11-5hJmZyoHgPKo9VVLifas1QfhFn8k5arGY66FVdqVfJ97EfM_1l8Iz0nKNgZcqim0o04_5T-9FekqOqek84K3JcR80nzGBkdZWH3lX3ZnEKUrgBvEE9MQc3V-0VeqT8gVbeuqUDlnYCFTqMow&gsessionid=KSPBRzIehC6M4rjg-hIOMjsLgfxXvWkXiW1ENKuWqLBIfr_MYyGI6Q)  
  <sub>TradingView, 24 hours ago</sub>  
  Fund managers have rarely felt this good about the economy. They have also rarely been in such a hurry to sell technology stocks.Just 3% of investors expect...
- [Pain in TQQQ, SOXL may offer silver lining for tech stocks - SocGen](https://www.google.com/goto?url=CAESowEBxCJF15ZJR6M-HmoWunSyqFJxqjZn0ehI_nELuIc0aOq3dHPtv3INHt6UnOmpmmpj25Oc-N6KTomGxkIO8dDENKYxFrDtIRIeVQb1AG1zU9fh_ku55keQTPgW-_-WixDXnmGMLp3kSWlt1Qnxeh_PgUBfiQbOvEz1HTz6aFwSlESl6EroT_BU_eqR9MUhRUz9G-xtyOcWKBPu975hbdWIRmFP&gsessionid=KSPBRzIehC6M4rjg-hIOMjsLgfxXvWkXiW1ENKuWqLBIfr_MYyGI6Q)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  Investors in the largest U.S. triple-leveraged technology exchange-traded funds have nearly erased tens of billions of dollars in 2026 paper profits,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 169.00 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 174.58 (-3.2%), 50d 185.35 (-8.8%), 200d 171.27 (-1.3%); 50d above 200d
Momentum: RSI(14) 42.0 | MACD -5.817 vs signal -5.505 (histogram -0.312)
Returns: 1d +3.2% | 5d -2.7% | 1m -10.4% | 3m -7.8%
52-week range: 127.50 - 202.00 (now 55.7% of the way up)
Volatility: ATR(14) 5.47 (3.2% of price) | annualised 20d 45.7%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: n/a
What it holds: P/E n/a | P/B n/a | P/S n/a | 3y earnings growth n/a
Yield: n/a
Three-year record: n/a a year | beta to the market n/a
Cost and size: expense ratio n/a | net assets n/a
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.40</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +3.5% (4.13B) over 7d | 1 month: +12.1% (13.21B) over 34d
Shares outstanding: 726.91M | fund size: 122.85B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- fund equity_holdings unavailable: HTTP Error 401:
- fund bond_holdings unavailable: HTTP Error 401:
- fund bond_ratings unavailable: HTTP Error 401:
- fund fund_operations unavailable: HTTP Error 401:
- fund fund_overview unavailable: HTTP Error 401:
- fund top_holdings unavailable: HTTP Error 401:
- fund sector_weightings unavailable: HTTP Error 401:
- fund asset_classes unavailable: HTTP Error 401:

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fund flows flat over past week and month (0% change)
- Technical indicators mixed: RSI 51.2, MACD below signal, price slightly below 20‑day SMA
- Macro environment stable: yields unchanged, VIX modestly higher, inflation 3.7% and unemployment 4.1% in line with expectations
- No significant positioning changes or insider activity observed

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://au.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance Australia, 4 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) · -4.12% · 2.52% · 24.33% · 17.03% · 18.73% · 35.42% · 630.16%. Key events. Baseline. Advanced...
- [Defensive ETFs Beat Nasdaq, But Wall Street Isn't Rotating Yet - State Street Health Care Select Sector S](https://www.benzinga.com/etfs/sector-etfs/26/11/63423089/defensive-sectors-beat-nasdaq-100-by-22-8-points-but-etf-flows-tell-a-mixed-story)  
  <sub>Benzinga, 2 hours ago</sub>  
  XLV was trading slightly lower in premarket trading Thursday as defensive stocks outpaced technology shares over a longer period. But ETF investors aren't...
- [The Case for Increasing Portfolio Exposure to Consumer Staples ETFs](https://www.google.com/goto?url=CAEStwEBxCJF1yxKeeAf_UHUGFcsqWh1Yje1iwUtC6tN9SvoXmgznJyLKxjprHBUHp7du4ft2DcvmKoKyYQTpy_Duz4RrQWgsCipAvw8sC_F6RExrUKs_gP3F3R1ZObJ1aUqr5T-jb-LM87jUsgbKCVciCBnu2YKb4jesAYh--pKPG6tCE2z9Gcu7md9vdFud-DSf97J8bvAnNZVYYFBLDjDfZi5_MtIAD2kJkOQF_8br40IS8G4xkAQGzA&gsessionid=im3fvcS0-Gj_1JWDeIE07qCfD3u-K1F24Afz1Cp5_tnf3X4_QT7aQw)  
  <sub>TradingView, 14 hours ago</sub>  
  The year 2026 has been marked by persistent economic headwinds that have weighed on investor confidence. Ongoing macroeconomic and geopolitical risks have...
- [Fund Managers Dump Tech Stocks at Fastest Pace Since 2006 - State Street Technology Select Sector SPDR ET](https://www.google.com/goto?url=CAESoAEBxCJF1ybksOzF5hbyNun80MbCSWULTnOjzlBFnEaCKMX9-dksp59vTlxVC7Tb8Mg39pDVHgAubxb0uWiTIYKPPevl62X6Ys3B4oI0GApVESAlCDa03UECRSpBTOILaGcSuF15OesJUJRFR-fdyC154xm0PzWoj_nUXYDeX1MkNjvngYcpOWe3bBOrPkJcn8ek9fId5Wt6LmIH62T3Q9kb&gsessionid=im3fvcS0-Gj_1JWDeIE07qCfD3u-K1F24Afz1Cp5_tnf3X4_QT7aQw)  
  <sub>Benzinga, 24 hours ago</sub>  
  Fund managers cut tech by the most since 2006 on AI capex fears, Bank of America says, as XLK nears a bear market. The buy signal hasn't come.
- [Growth Leads Sectors In Wednesday Trading As Cyclicals Trail](https://www.google.com/goto?url=CAESsgEBxCJF17__hpeMcMAIbSRutyeIIitRHvoBvSTtyXeZLo0Pwgf6dnuh3CyP-Zr13IaAqRpKmS8FVMnwfQXKEnikArzbRfKWWuiEXv73DfO7kYx1gH7qeca7nyW17rjoQy0kX35PO-dEgbsptbJ34GsSQnZHbFg16S1Ufg0koUM_kENpDzTrZ37xu256Ln-ptqhrr9bNMwCyBH5Q01jporUoTicuWrRz_fA5kR5QUL-NdC3T&gsessionid=im3fvcS0-Gj_1JWDeIE07qCfD3u-K1F24Afz1Cp5_tnf3X4_QT7aQw)  
  <sub>Benzinga, 23 hours ago</sub>  
  Five sectors are trading higher and six are lower in Wednesday's regular session, with growth sectors holding the top three positions.
- [Retailers Led A Split Day For Consumer Stocks](https://www.google.com/goto?url=CAEShwEBxCJF11Prv_7bhoQpAadVrYCDfgIP5CvJ4kkG0h0-O9h422TpFRAg5QpqdtEfUVVR69s-GgpxlpSVzf4F9l45wEbzQf8SLIGGOFFhkg8A_79iyf5-5pjL0jBNvGKme80mwLQdmYuPRoUAI0HCaEawAm6Jd1Ckb9f_zs8PrNmsQq9174a_2NY&gsessionid=im3fvcS0-Gj_1JWDeIE07qCfD3u-K1F24Afz1Cp5_tnf3X4_QT7aQw)  
  <sub>Finimize, 17 hours ago</sub>  
  Target and TJX lifted forecasts after strong Q3 sales, while Lowe's margins slipped and XLP lagged XLY.
- [ETFs Are Net Sellers of Costco (COST) on Tuesday](https://www.google.com/goto?url=CAESkgEBxCJF12LeWcfkmBhj8DkNja36aBMRoMfw8ioiX4ngisecyB2FoWdZ6tocGTu7kXFurKUTCtaVSoUGUiJ2_3YVXXkMVjYbb4bc_-iL215iwZQQpCURoYxzewtp9ncDSM5b0i34nUi_wFYWbwxoR07Sl6TfWUL7K9FOjBcwiypU986VkDKTlRz328U3_Gspx90EKg&gsessionid=im3fvcS0-Gj_1JWDeIE07qCfD3u-K1F24Afz1Cp5_tnf3X4_QT7aQw)  
  <sub>GuruFocus, 3 hours ago</sub>  
  XLP led the move, cutting its Costco (COST) stake by $42.2 million in Tuesday's session as ETF activity turned net negative at $45.7 million.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 89.58 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 90.12 (-0.6%), 50d 86.25 (+3.9%), 200d 85.01 (+5.4%); 50d above 200d
Momentum: RSI(14) 51.2 | MACD 1.368 vs signal 1.606 (histogram -0.238)
Returns: 1d -1.8% | 5d -1.6% | 1m +2.8% | 3m +4.2%
52-week range: 76.51 - 92.60 (now 81.2% of the way up)
Volatility: ATR(14) 1.46 (1.6% of price) | annualised 20d 22.3%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: n/a
What it holds: P/E n/a | P/B n/a | P/S n/a | 3y earnings growth n/a
Yield: n/a
Three-year record: n/a a year | beta to the market n/a
Cost and size: expense ratio n/a | net assets n/a
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 210.17M | fund size: 18.83B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- fund equity_holdings unavailable: HTTP Error 401:
- fund bond_holdings unavailable: HTTP Error 401:
- fund bond_ratings unavailable: HTTP Error 401:
- fund fund_operations unavailable: HTTP Error 401:
- fund fund_overview unavailable: HTTP Error 401:
- fund top_holdings unavailable: HTTP Error 401:
- fund sector_weightings unavailable: HTTP Error 401:
- fund asset_classes unavailable: HTTP Error 401:

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Flat fund flows (0% change) indicate no net demand
- Technical indicators mixed: price below 20‑day SMA, RSI 52.1, MACD histogram negative, volume 0.15× 20‑day average
- Macro data (inflation 3.7%, unemployment 4.1%, jobless claims 203k) within expectations, no surprise
- Yield curve remains upward sloping (+0.94) and Treasury yields unchanged, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [VPU: Utilities Dashboard For November](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0dd80a2a4c4084d897d5256f3c6f&url=https%3a%2f%2fseekingalpha.com%2farticle%2f4969869-vpu-utilities-dashboard-for-november&c=10832690878381226030&mkt=en-us)  
  <sub>Seeking Alpha, 12h ago</sub>  
  The Vanguard Utilities ETF has a broader portfolio than XLU but similar returns and valuation. XLU is better suited to traders given much higher liquidity.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 43.21 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 43.38 (-0.4%), 50d 41.94 (+3.0%), 200d 44.34 (-2.5%); 50d below 200d
Momentum: RSI(14) 52.1 | MACD 0.426 vs signal 0.508 (histogram -0.082)
Returns: 1d -0.8% | 5d -1.4% | 1m +2.9% | 3m +1.0%
52-week range: 39.25 - 47.73 (now 46.7% of the way up)
Volatility: ATR(14) 0.58 (1.3% of price) | annualised 20d 12.6%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: n/a
What it holds: P/E n/a | P/B n/a | P/S n/a | 3y earnings growth n/a
Yield: n/a
Three-year record: n/a a year | beta to the market n/a
Cost and size: expense ratio n/a | net assets n/a
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 163.27M | fund size: 7.06B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- fund equity_holdings unavailable: HTTP Error 401:
- fund bond_holdings unavailable: HTTP Error 401:
- fund bond_ratings unavailable: HTTP Error 401:
- fund fund_operations unavailable: HTTP Error 401:
- fund fund_overview unavailable: HTTP Error 401:
- fund top_holdings unavailable: HTTP Error 401:
- fund sector_weightings unavailable: HTTP Error 401:
- fund asset_classes unavailable: HTTP Error 401:

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Most dimensions point to a neutral stance: positive fund flows suggest demand, but technicals show mixed/weak momentum and there is no macro surprise.

**Main reasons it gave:**
- Fund flows positive: +2.0% share count increase over 1 week
- Technical momentum bearish: RSI 43.9, MACD below signal
- No macro surprise: Treasury yields stable, inflation 3.7% in line with expectations

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://au.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance Australia, 4 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) · -4.12% · 2.52% · 24.33% · 17.03% · 18.73% · 35.42% · 630.16%. Key events. Baseline. Advanced...
- [Defensive ETFs Beat Nasdaq, But Wall Street Isn't Rotating Yet - State Street Health Care Select Sector S](https://www.benzinga.com/etfs/sector-etfs/26/11/63423089/defensive-sectors-beat-nasdaq-100-by-22-8-points-but-etf-flows-tell-a-mixed-story)  
  <sub>Benzinga, 2 hours ago</sub>  
  XLV was trading slightly lower in premarket trading Thursday as defensive stocks outpaced technology shares over a longer period. But ETF investors aren't...
- [1. Consumer Discretionary Select Sector SPDR Fund (NYSEARCA:XLY)](https://www.google.com/goto?url=CAESpwMBxCJF19puO4C-IjNlMoWnqw-0Gu_VJQpz3dRJFVR5qQ3I2OxUH4bRUZaf-arybU3r_jg9jy8VoP7qCh6DEl32tahVUj9Ucj5B2xgwu7KU2amJk7vwc-Pyh3psh07nWYvvmD1LuzlAG0TQ172WOqYWPf_NbpqddUd1rM3clvAp_o9Yj1P32NMG1-MqzDtkJkxdWAESx2vnbcXRlHvL_P1GnB1COEBs9rTfDU1XjoXNCzIP5hr33rv14Z-1_NYpo8ZrOSRmkNKszZJOGOqxriOxmwpCRUGdaF9cyjHRatpETkw1NXgshIoOL64aenXPHDtstZMX2MXh0cA9LIeipCFHwi0aQcgjt-Xs9xDsgN_VxOnJtMJkE5_f29Qi9mrac0zllKjSigd__fJI-PmTNS91Rp1SrVf71E2f4ve5XAd9YwDfvy3NCtArSu-fZvYqQoAMEwQOP2jjB-ZI3O87cDNodcRmjJroDCCZicaGTqigf3VyNue4oLeebqKZ7absC_Ts6wEc5bFMgxK1o-CgOqwkomRYAMpthbTM0h9FQv61coiLSPXym88&gsessionid=eXQ6mwDbOomGxk_N-S3uZRdKqqS7CPE77GThJztmFn9rc45YUKmcuA)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  The sector's 1.79% advance came from two sources, which gives the Consumer Discretionary Select Sector SPDR Fund (NYSEARCA:XLY) the best setup.
- [Fund Managers Dump Tech Stocks at Fastest Pace Since 2006 - State Street Technology Select Sector SPDR ET](https://www.google.com/goto?url=CAESuQEBxCJF1w4nqjVbNvqC6CDulXRNhMXwQRsRHf5xEfMxL1jxIWT6xNgL2Fb5shZaXFGexuli0PaUbdGssUvzysO5mS-UrvjZEfW_EYXTX5haGH3luIFF6zK26Yy0X6Ug57HuhKt3UT3uexOx8GKRlEuiL8omBVA6BCHCdlBDCixaYCMiae-lieTEkpvE9D9LJbGF-YR5icwCiFOAaWJYpSWTydOnS5cjfP3VYae8XMeG9ietj8IMj6cJzg&gsessionid=eXQ6mwDbOomGxk_N-S3uZRdKqqS7CPE77GThJztmFn9rc45YUKmcuA)  
  <sub>Benzinga, 24 hours ago</sub>  
  Fund managers cut tech by the most since 2006 on AI capex fears, Bank of America says, as XLK nears a bear market. The buy signal hasn't come.
- [Financial Select Sector SPDR ETF (XLF) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXXvGbWXXVEhQMm7b8hEN0se2siZRaA5nKu0BHnEAwg6cFBOusgMYhiMuxfc2GkRzyEN_KvgTbYx_W24I3YPpiDYN_6p15ovb8nL10ZPjP17rBe5Vfi4cgHPWKtitvLJ6s&gsessionid=eXQ6mwDbOomGxk_N-S3uZRdKqqS7CPE77GThJztmFn9rc45YUKmcuA)  
  <sub>Yahoo Finance UK, 14 hours ago</sub>  
  Find the latest Financial Select Sector SPDR ETF (XLF) stock quote, history, news and other vital information to help you with your stock trading and...
- [Invesco Aerospace & Defense ETF (PPA) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXXoQp7Wbq5cwtYeUnbgOa1Xa1bjE2zFB0UnpYP7WwxANsrnADT_95vOMbXMTU_3Eru4fo24y8D9fD0UQa43URAPB9bl7KN3jVepQpOaar0Sf72XC9paF5GtE6F3x_R9nI&gsessionid=eXQ6mwDbOomGxk_N-S3uZRdKqqS7CPE77GThJztmFn9rc45YUKmcuA)  
  <sub>Yahoo Finance Singapore, 21 hours ago</sub>  
  Find the latest Invesco Aerospace & Defense ETF (PPA) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 179.26 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 184.54 (-2.9%), 50d 176.30 (+1.7%), 200d 160.77 (+11.5%); 50d above 200d
Momentum: RSI(14) 43.9 | MACD 2.151 vs signal 3.344 (histogram -1.194)
Returns: 1d -1.1% | 5d -4.6% | 1m +0.2% | 3m +2.7%
52-week range: 142.84 - 189.66 (now 77.8% of the way up)
Volatility: ATR(14) 3.37 (1.9% of price) | annualised 20d 21.7%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: n/a
What it holds: P/E n/a | P/B n/a | P/S n/a | 3y earnings growth n/a
Yield: n/a
Three-year record: n/a a year | beta to the market n/a
Cost and size: expense ratio n/a | net assets n/a
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +2.0% (913.80M) over 7d | 1 month: +3.7% (1.68B) over 34d
Shares outstanding: 265.09M | fund size: 47.52B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- fund equity_holdings unavailable: HTTP Error 401:
- fund bond_holdings unavailable: HTTP Error 401:
- fund bond_ratings unavailable: HTTP Error 401:
- fund fund_operations unavailable: HTTP Error 401:
- fund fund_overview unavailable: HTTP Error 401:
- fund top_holdings unavailable: HTTP Error 401:
- fund sector_weightings unavailable: HTTP Error 401:
- fund asset_classes unavailable: HTTP Error 401:

### US shopping and leisure (XLY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro or fundamental catalyst; modest inflows and mixed technicals keep outlook neutral.

**Main reasons it gave:**
- Fund flows show modest inflows: +3.4% share count week-over-week
- Technical indicators mixed: price above SMAs but MACD below signal
- Macro environment unchanged: yields down slightly, VIX up modestly, no policy surprise
- No analyst view or fundamental data indicating a shift
- Disregarded promotional news suggesting XLY will benefit from holiday spending as unreliable

<details><summary><b>News</b> — score +0.00</summary>

- [VCR: Consumer Discretionary Sector Dashboard For November (NYSEARCA:VCR)](https://seekingalpha.com/article/4969796-vcr-consumer-discretionary-sector-dashboard-for-november?source=feed_all_articles)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Vanguard Consumer Discretionary ETF offers a broader portfolio, slightly better value, and returns than XLY, with equivalent long-term risk-adjusted...
- [XLY seen benefiting from stronger U.S. holiday consumer spending](https://tradersunion.com/news/stocks/show/4318486-xly-benefits-us-holiday-consumer-spending/)  
  <sub>Traders Union, 3 hours ago</sub>  
  XLY ETF expected to benefit from robust U.S. holiday consumer spending, with forecasts projecting record online sales this year-end season.
- [Retailers Led A Split Day For Consumer Stocks](https://www.google.com/goto?url=CAEShwEBxCJF12MLlqVgxPDE1mkKE3rYmVOK-nUawCFr-Ma2Vzm89BXBZkYb_gze19RZEyQSNK1OdkewRNEPdcpAL62R-A-FtENMlIwg1fVu-ujSCarK02L9PzOfQHc65OoFU0ih7W3IUM2_oYdkPxkdcd3fAjf2EKfwgci0dWnKimmB0QPU1oYW-z0&gsessionid=nU2ykPPVx72lQMk9vpIwlbpmGymeo1meKyQdBkz2Yg2vxKCWETIQVA)  
  <sub>Finimize, 17 hours ago</sub>  
  Target and TJX lifted forecasts after strong Q3 sales, while Lowe's margins slipped and XLP lagged XLY.
- [1. Consumer Discretionary Select Sector SPDR Fund (NYSEARCA:XLY)](https://www.google.com/goto?url=CAESpwMBxCJF11ZitcJjZx2p1iJTPg6U2aHw9EUmPv5ye985j1gMOSw7GJhtdzaybcy2Jypl3rOpEUngihZrU9jvC33G7T_i6m0VMwHV92oQK3m3dP_2fszqKUo4Wrs8Qj8iCgGJov4qDtjqTmlX97gKdcLSy_UDJofHm2d3vtF99YG2D-0IxdsFrwmu2EnlDAE6az8boE7gG6sNyTfwMKk451q83dC6MGg_A8GUOSiwKE9b0_VOlb2Noi-L2v2MrM-_suporhQJaiHgVsHeCCzo2A2vmEumZvkGqu0XzfmPNr4YhNmFn-McjL8G7uKW7fSmdYPvvI7xI0zr5Kvp-jNjmZDX-cN-ltU2ZfBNU1XHALYlhWtKxasSMrWPML4PpoxrTDr2W83wqB49fOBLcxwbTMaYQkJmdU2fj4ZbMMs3PgoHkzLCMeu-zSHxzNODWPiHOxaRk76GxKq2H8WPrNNX19siZSrM9YPiVXZ7mH_8fhHQ0XwlcVfHZIoYY1KJj07sPG9WNI59G8e8VzOLWGwjLMjKoZ39tJaMnjGhWNJXz5B-iyeCxiFyc5w&gsessionid=nU2ykPPVx72lQMk9vpIwlbpmGymeo1meKyQdBkz2Yg2vxKCWETIQVA)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  The sector's 1.79% advance came from two sources, which gives the Consumer Discretionary Select Sector SPDR Fund (NYSEARCA:XLY) the best setup.
- [Growth Leads Sectors In Wednesday Trading As Cyclicals Trail](https://www.google.com/goto?url=CAESsgEBxCJF15Xw6iADnfWWGuq9VjlWkGobZ2wdt4zZG0ExSi85DWkFgoUC9vCZYdWRibuPZ7cYnvy7fXEAqKNx4pvZ8ZII4oVYB2IlAReGmQ0N2a0iqLgttzZ2FfKvzaenWBmZsYL9dK9nT8kBs1rQW3HMakUQ_9Wxx7RWEnV_jNs-4tBucjVg1xFS0yxVBZKMQvDhmXOICA7mjMgCmypRxynSTPqAIjTLPOr_V6bI-Ort5tSL&gsessionid=nU2ykPPVx72lQMk9vpIwlbpmGymeo1meKyQdBkz2Yg2vxKCWETIQVA)  
  <sub>Benzinga, 23 hours ago</sub>  
  Five sectors are trading higher and six are lower in Wednesday's regular session, with growth sectors holding the top three positions.
- [Six Flags Entertainment climbs 9% as recent rebound continues (FUN:NYSE)](https://www.google.com/goto?url=CAESnwEBxCJF11ExgYk1Yw6kvxDTbD597_8dSi7DHqfH7zO0PWo3ERSKbYMp38JiNxsCbzP1qJswoTyBNR97E9MCJDUPsHU_LWG02Fhzb_qWgn6FPK7MGGzL13TUvu_A8lTvzPtilxpMKGrff8pUEO2wzcB2VcFajwhWi6rGB2zb8Wi3B0GZ7NNrqAu-LZirq36TtRYIH8FYhnSjrvd9eFVTvT8&gsessionid=nU2ykPPVx72lQMk9vpIwlbpmGymeo1meKyQdBkz2Yg2vxKCWETIQVA)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Six Flags shares rise just over 9% to $11.97 as consumer discretionary stocks and peers gain; shares are up just over 35% in a month.
- [Burlington Stores climbs 6% as off-price retailers move higher (BURL:NYSE)](https://www.google.com/goto?url=CAESoAEBxCJF16bj5ekPSKCJA8oin1kdPi6a51hzN2lsf4H43UGyZdlz-HNPa-Z_pRAvuxCqsiXSbqPiEHBhp07ErmX2cQ53BdrBpRTrRiWYobsy8gvXjXR2uF5U9fNsfsanQcq1pE3GM-Bnt2R0bes_rdao9sdw3_3FTIWfOQxLfewH3SBF7VyqM-ipRlmvqNn7fhY2i-UOdD9EPsk9xPQ6NBC4&gsessionid=nU2ykPPVx72lQMk9vpIwlbpmGymeo1meKyQdBkz2Yg2vxKCWETIQVA)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Burlington Stores shares gain 6.4% to $250.21, while TJX rises just over 10%, ROST gains just over 3% and XLY adds almost 2%.
- [5 Consumer Discretionary Plays Showing Strength During the Tech Sell-Off](https://www.google.com/goto?url=CAESnwEBxCJF1_XC4Vjd_kr-SRoHFLntXuGhX_L4DL6UuW8WdINxs1xlCpIm_lW6fulzv-SWBXTGFVnusc5TB4JEsrDkccCen5SxQGDsAEdZfpofuwizhs3r7KEMEKbRnXUjZxJ9BrBP5NoRq-3OIJYwR4zGjBFAwEUqqHthBpsx_gd4fGs245Ggj8ExxfOkE67Nz5TbhzJzG5iEo7HUTjPZneU&gsessionid=nU2ykPPVx72lQMk9vpIwlbpmGymeo1meKyQdBkz2Yg2vxKCWETIQVA)  
  <sub>inkl, 23 hours ago</sub>  
  As semiconductors sell off and NVIDIA sees a leadership shake-up, the XLY consumer discretionary ETF has gained ground, with Amazon, Starbucks, Royal…

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 119.11 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 117.99 (+0.9%), 50d 114.23 (+4.3%), 200d 115.39 (+3.2%); 50d below 200d
Momentum: RSI(14) 55.7 | MACD 1.376 vs signal 1.589 (histogram -0.212)
Returns: 1d -0.1% | 5d -1.1% | 1m +3.1% | 3m +0.9%
52-week range: 105.66 - 124.52 (now 71.3% of the way up)
Volatility: ATR(14) 2.18 (1.8% of price) | annualised 20d 28.1%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: n/a
What it holds: P/E n/a | P/B n/a | P/S n/a | 3y earnings growth n/a
Yield: n/a
Three-year record: n/a a year | beta to the market n/a
Cost and size: expense ratio n/a | net assets n/a
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
Direction: money coming in (1 month)
Share count change: 1 week: +3.4% (739.59M) over 7d | 1 month: +1.0% (222.05M) over 34d
Shares outstanding: 191.22M | fund size: 22.78B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- fund equity_holdings unavailable: HTTP Error 401:
- fund bond_holdings unavailable: HTTP Error 401:
- fund bond_ratings unavailable: HTTP Error 401:
- fund fund_operations unavailable: HTTP Error 401:
- fund fund_overview unavailable: HTTP Error 401:
- fund top_holdings unavailable: HTTP Error 401:
- fund sector_weightings unavailable: HTTP Error 401:
- fund asset_classes unavailable: HTTP Error 401:

### South Korea (EWY) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [iShares MSCI South Korea ETF (EWY) Price Prediction: Momentum Is Repairing, But Trend Damage Is Still Visible](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0ed4b1d14e1bb56f2237d5150a28&url=https%3a%2f%2fblockchain.news%2fnews%2f20261119-price-prediction-ewy-momentum-is-repairing-but-trend-damage&c=2562716480103072330&mkt=en-us)  
  <sub>Blockchain News, 11h ago</sub>  
  Shares MSCI South Korea ETF (EWY) is trading at $140.59, above its 7-day average but still below its 20-, 50-, and 200-day moving averages. Binance ...
- [iShares MSCI South Korea ETF (EWY)](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0ed4b1d14e1bb56f2237d5150a28&url=https%3a%2f%2ffinance.yahoo.com%2fquote%2fEWY%2flatest-news%2f&c=9665331078479750015&mkt=en-us)  
  <sub>Yahoo Finance, 14h ago</sub>  
  The above button links to Coinbase. Yahoo Finance is not a broker-dealer or investment adviser and does not offer securities or cryptocurrencies for sale or facilitate trading. Coinbase pays us for ...
- [韩国ETF-iShares MSCI收涨1.04%，成交额15.93亿美元](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0ed4b1d14e1bb56f2237d5150a28&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fusstock%2fnotice%2f2026-11-19%2fdoc-inizfcqp4453251.shtml&c=9758950423059974833&mkt=en-us)  
  <sub>新浪财经, 23h ago</sub>  
  11月19日，韩国ETF-iShares MSCI（EWY）收涨1.04%，报136.73美元，成交额15.93亿美元，市值198.05亿美元。 声明：市场有风险，投资需谨慎。本文基于第三方数据库发布，不代表新浪财经观点，任何在本文出现的信息均只作为参考，不构成个人投资建议。如有出入请以实际公告为准。如有疑问，请联系biz@staff.sina.com.cn。

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 140.33 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 146.79 (-4.4%), 50d 164.39 (-14.6%), 200d 164.32 (-14.6%); 50d above 200d
Momentum: RSI(14) 41.9 | MACD -7.314 vs signal -7.515 (histogram 0.201)
Returns: 1d +2.6% | 5d -3.5% | 1m -10.5% | 3m -21.3%
52-week range: 88.53 - 219.20 (now 39.6% of the way up)
Volatility: ATR(14) 6.69 (4.8% of price) | annualised 20d 70.5%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.36 | P/B 1.72 | P/S 1.66 | 3y earnings growth n/a
Yield: 1.3%
Three-year record: +32.7% a year | beta to the market 2.62
Cost and size: expense ratio 0.59% | net assets 22.30B
What it is made of: Stocks 98.7%, Cash 1.3%
Largest holdings: SK hynix Inc 23.8%, Samsung Electronics Co Ltd 23.0%, SK Square 3.0%, Samsung Electro-Mechanics Co Ltd 2.6%, KB Financial Group Inc 2.1%
Sector mix: Technology 52.7%, Industrials 15.4%, Financial services 14.9%, Consumer cyclical 4.6%
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
Direction: money coming in (1 month)
Share count change: 1 week: +4.2% (937.04M) over 7d | 1 month: +5.3% (1.17B) over 34d
Shares outstanding: 166.39M | fund size: 23.35B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Brazil’s Real Falls to 18-Month Low](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0edf99c74e8da317a3ea36e7631d&url=https%3a%2f%2fwww.riotimesonline.com%2fbrazil-real-18-month-low-fiscal-package-senate-2026-11-18%2f&c=9311712858386333817&mkt=en-us)  
  <sub>The Rio Times, 28h ago</sub>  
  Brazil’s real fell 1% to about R$5.84 per US dollar, its weakest since April 2025, as a stalled Senate fiscal vote rattles investors.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 29.91 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 32.66 (-8.4%), 50d 36.97 (-19.1%), 200d 36.87 (-18.9%); 50d above 200d
Momentum: RSI(14) 27.4 | MACD -2.063 vs signal -1.949 (histogram -0.114)
Returns: 1d -0.5% | 5d -5.9% | 1m -29.6% | 3m -14.7%
52-week range: 29.91 - 43.54 (now 0.0% of the way up)
Volatility: ATR(14) 1.00 (3.3% of price) | annualised 20d 73.3%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.38 | P/B 1.84 | P/S 1.40 | 3y earnings growth n/a
Yield: 4.5%
Three-year record: +3.3% a year | beta to the market 0.92
Cost and size: expense ratio 0.59% | net assets 9.62B
What it is made of: Stocks 98.0%, Cash 1.6%, Preferred 0.4%
Largest holdings: Vale SA 8.7%, Petroleo Brasileiro SA Petrobras 8.5%, Nu Holdings Ltd Ordinary Shares Class A 8.5%, Weg SA 3.4%, Axia Energia 3.0%
Sector mix: Financial services 31.8%, Energy 21.4%, Basic materials 13.1%, Utilities 12.1%
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
Rolled up from the 5 largest holdings, 32.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.71 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +40.5% above the current prices
Holdings read: VALE3.SA, PETR3.SA, NU, WEGE3.SA, AXIA3.SA
Recent rating changes among them:
  - NU: 2026-10-20 UBS: main, Buy -> Buy
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
Shares outstanding: 200.55M | fund size: 6.00B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Understanding Momentum Shifts in (KRE)](https://news.stocktradersdaily.com/news_release/16/Understanding_Momentum_Shifts_in_KRE_111926054001_1795084801.html)  
  <sub>Stock Traders Daily, 9 hours ago</sub>  
  Price-action only: Spdr S&p Regional Banking Etf (KRE) movements set the tone for institutional models. Understanding Momentum Shifts in (KRE)
- [iShares US Home Construction ETF (ITB) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/ITB/)  
  <sub>Yahoo Finance UK, 4 hours ago</sub>  
  Find the latest iShares US Home Construction ETF (ITB) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 70.52 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 72.44 (-2.7%), 50d 71.47 (-1.3%), 200d 71.23 (-1.0%); 50d above 200d
Momentum: RSI(14) 41.6 | MACD -0.083 vs signal 0.224 (histogram -0.307)
Returns: 1d +0.0% | 5d -2.8% | 1m -0.1% | 3m -5.8%
52-week range: 59.59 - 77.93 (now 59.6% of the way up)
Volatility: ATR(14) 1.32 (1.9% of price) | annualised 20d 18.8%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: n/a
What it holds: P/E n/a | P/B n/a | P/S n/a | 3y earnings growth n/a
Yield: n/a
Three-year record: n/a a year | beta to the market n/a
Cost and size: expense ratio n/a | net assets n/a
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
Direction: money coming in (1 month)
Share count change: 1 week: +3.1% (121.21M) over 7d | 1 month: +5.9% (223.02M) over 30d
Shares outstanding: 56.52M | fund size: 3.99B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- fund equity_holdings unavailable: HTTP Error 401:
- fund bond_holdings unavailable: HTTP Error 401:
- fund bond_ratings unavailable: HTTP Error 401:
- fund fund_operations unavailable: HTTP Error 401:
- fund fund_overview unavailable: HTTP Error 401:
- fund top_holdings unavailable: HTTP Error 401:
- fund sector_weightings unavailable: HTTP Error 401:
- fund asset_classes unavailable: HTTP Error 401:

### US house builders (XHB) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [For SPDR S&P Homebuilders ETF (NYSEARCA:XHB), What Do October's Figures Show, With Starts Up 9.9% and Permits Down 7.4%?](https://kalkine.com.au/news/economic-news/for-spdr-sp-homebuilders-etf-nysearcaxhb-what-do-octobers-figures-show-with-starts-up-99-and-permits-down-74)  
  <sub>Kalkine, 2 hours ago</sub>  
  For SPDR S&P Homebuilders ETF (NYSEARCA:XHB), What Do October's Figures Show, With Starts Up 9.9% and Permits Down 7.4%?
- [SPDR S&P Homebuilders ETF (NYSEARCA:XHB): What Does a 9.9% Jump in Housing Starts Alongside a 7.4% Fall in Permits Imply?](https://kalkine.ca/news/economic-news/spdr-sp-homebuilders-etf-nysearcaxhb-what-does-a-99-jump-in-housing-starts-alongside-a-74-fall-in-permits-imply)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  SPDR S&P Homebuilders ETF (NYSEARCA:XHB): What Does a 9.9% Jump in Housing Starts Alongside a 7.4% Fall in Permits Imply?
- [Which Housing Investment Ranks Highest Among Lowe's (NYSE:LOW), SPDR S&P Homebuilders ETF (NYSEARCA:XHB) and Zillow Group (NASDAQ:Z) as Pending Sales Hit a Record Low?](https://www.google.com/goto?url=CAESgAIBxCJF17buTuvcVhAsmT4vyfsODAT332unZnPcTSe5-I9EWq2z_gy6KwbaepkffYMBVH7UuWITuchgatNihRXHsq8hESJqMT7g4gnThuJH43A-M0IMGWbhuGd_3V7vQXfUbdUKxF_Ja0U5-6iqfwt_m-7tDckPRV7fT4CummIfSTF8ODwcEulM6RRMclI9epYYneDrmUuGallGKrcGV7R884I1P5SJwp6mZvV3Lv_KOZTA9q3G41fiOqDuhCeX63_sVzdMxmVtnMg7B17_6Dqp_3fmEnjkDcTYpUZK_hfx1oSLzEwe7DjVTngEYmGvOa0hbOpH_QEaNmFxXSDoEGXO&gsessionid=PXvWktNL-LtnkbHeft_AvVhYG_RrSwJ0LisSTuFV_efI348GY4VQvQ)  
  <sub>Kalkine, 2 hours ago</sub>  
  Which Housing Investment Ranks Highest Among Lowe's (NYSE:LOW), SPDR S&P Homebuilders ETF (NYSEARCA:XHB) and Zillow Group (NASDAQ:Z) as Pending Sales Hit a...
- [iShares US Home Construction ETF (ITB) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXXBU7uXKQuQW9DB_UXZWTM08klB_EdlklHWb-jwZoGKP7kal-Xyt6DIWm1j8t4TZK2hWmf1t5m9qh4TxbIeU5RvIebFdcYkjIIb5ZDAxJslA79Vw4J0O6xgEIOE8UPDgE&gsessionid=PXvWktNL-LtnkbHeft_AvVhYG_RrSwJ0LisSTuFV_efI348GY4VQvQ)  
  <sub>Yahoo Finance UK, 4 hours ago</sub>  
  Find the latest iShares US Home Construction ETF (ITB) stock quote, history, news and other vital information to help you with your stock trading and...
- [Where’s the floor for U.S. housing as builder sentiment hits 2012 lows?](https://www.google.com/goto?url=CAESwgEBxCJF14see968VU_wBhTOfcJ0lvQ6X4z8nNl_ysg-KliGtKwBAB9bssEb1_kMRLhNt8OC5vc-Ap5XqQkHl8nZ0DFjNgyK0xoZyGjSrMEVaQr-s7gz-JlKu6_0zadt9_KPtgTxvR90AFoZqof2h_CmiRFfBvQJPZwIf8yIPqfVCoPT_V2p-jC3z5b9lDT7-oH_k7d-h0Llz-p_gU0WGCn7EmjJsDT9Kqo0vJrVkjdezV9km1iuq8eqA1mQuJWbJK2ERQ&gsessionid=PXvWktNL-LtnkbHeft_AvVhYG_RrSwJ0LisSTuFV_efI348GY4VQvQ)  
  <sub>TradingView, 23 hours ago</sub>  
  The U.S. residential construction outlook darkened further this week after single-family building permits fell to a three-year low and homebuilder sentiment...
- [Could a December Fed Increase Look Close to Certain, and What Would It Mean for iShares 7-10 Year Treasury Bond ETF (NASDAQ:IEF) Investors?](https://www.google.com/goto?url=CAES7gEBxCJF16GAR1Gq03qm65F9GHJujaNSMcW03QV5QyLA-Q7KlCmevGQMpXQp28PXqrVXRQBwbgfVA3dEMNhTvZwjwr7v5r1WdAmWIoY8zzD-BBeslNHy2Bg0ZfJFtZ5yYHcKxjcBvgwA3CJZqlcX_y2Y-cuBB-ORW9B36IVIP-bErUfuu2JCPkM6EkyCnLxBTJ57TDAes0Hp-VxP46ASe231FxHovBw1j0S4dsjpBNo7uWwfoSPhUdGbEa_KLOWo0AplujRl8Q7OrJVbY1ic3SJcYZdvSy_XeHqxsTRB3GrF1bX9tDsXO9HUoijwF9yv&gsessionid=PXvWktNL-LtnkbHeft_AvVhYG_RrSwJ0LisSTuFV_efI348GY4VQvQ)  
  <sub>Kalkine, 2 hours ago</sub>  
  Could a December Fed Increase Look Close to Certain, and What Would It Mean for iShares 7-10 Year Treasury Bond ETF (NASDAQ:IEF) Investors?
- [Ahead of November 19, what should holders of iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY) focus on in jobless claims and the Philly Fed survey?](https://www.google.com/goto?url=CAES9QEBxCJF1wxmShKRjNiPCGznEUoYbzsXm8EZBM0jGrpgOzk4MrHCH5FNDrR0yZOcEdFW53AKZRxbKfpPTEohI8jYPfYml8hc_T7QNZ2NZfjJ3B50BO_GnICjJj1F2RWUZACCzUzIJjwO8whW14bnOx7sNBv9zQoDyzydZ3AHRrRU5el78o74jghiFMuYrXZyp2Sap8H1GMfTHut54KfX1ldyz1gtAtvMXR0LXP6S9icgMjmC8Zz0YHrJ1nXXRCAFDmMv7vCJdALpqvQmm-7vET6O5TtEWk56p-BmmGgHGYW8KCkdDRz8BF-3GKtw6URUXLMIeRL_Cg&gsessionid=PXvWktNL-LtnkbHeft_AvVhYG_RrSwJ0LisSTuFV_efI348GY4VQvQ)  
  <sub>Kalkine, 2 hours ago</sub>  
  Ahead of November 19, what should holders of iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY) focus on in jobless claims and the Philly Fed survey?
- [Should Holders of iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) Be Concerned by a 5.07% Ten Year and 5.41% Thirty Year Yield?](https://www.google.com/goto?url=CAES3gEBxCJF13KMQT7c_Wc3dNCH5TV8wJU5-RP5BKbuqgjmwmX52ob2WeZh_6ZmqJSTQck8kyPkDKe49ni9SRtGzcNyH_816WK5Jj2xEYR7jnbG18CFfaaFVHubWjJcgCWUxPK9HAQ68cswsgy7rC2By4wq-x8DQ-kI9E7x41C3HUigY9n8Z0jzsMJC-oaNn-NF7AtcKd18vn1BoVgREsam1Hr9piP9t2SiaqMJ9nHyvJzJk_LoBUdaDaDKSoF-BOcvDbjPnodJjhpu9yJTsLF8fyj2AXi-aB3DFYJWpa5AcMs&gsessionid=PXvWktNL-LtnkbHeft_AvVhYG_RrSwJ0LisSTuFV_efI348GY4VQvQ)  
  <sub>Kalkine, 2 hours ago</sub>  
  Should Holders of iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) Be Concerned by a 5.07% Ten Year and 5.41% Thirty Year Yield?
- [Does Invesco DB US Dollar Index Bullish Fund (NYSEARCA:UUP) Gain From a 19-Month High at 103.80?](https://www.google.com/goto?url=CAESwwEBxCJF15KB8j3-MqNcPBHovl2QlCXFP9EF8XX5Zd1L-BeyIla58Tab8dBiEOyHsUQGOlqBtbXG0ID4vuvx-g6ehuffcN_1kyBkwLr45qNF0Hbw_dqhP9WabCmAnU109euJEP6Y2W98-PEGeg4HhjwxlVBnIeShrG0-9C_9-xWwqOD8A41cfun520ne4TIpCKSk-EfSxRdrMF7KaWMc_YBCaMhIs42RoJqDNpTqww_6XkW76-U2IZIJKiHqz0lqrR5rE28&gsessionid=PXvWktNL-LtnkbHeft_AvVhYG_RrSwJ0LisSTuFV_efI348GY4VQvQ)  
  <sub>Kalkine, 2 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [What Led Bank Indonesia to Catch Markets Off Guard With a Hike Taking Its Rate to 6.00%?](https://www.google.com/goto?url=CAESvAEBxCJF1_7H5IoNfnWenQh5xP1fK10dFs0pubvrS2LQka6gkqf_qGxj7FnluxpjeB6M_QJixud1AGTHpywExQ6fE08l3f28E8v08m6yoMzGvVxzS2mreSZke5ngUS2w1DYAXy2B6Vt2awsjXZlLlAs5fTwuDPZe9ddQgO0D1GY_X3XGJ0zZURDc7TU04ZVFdLGYlFJu3nwqJgg-3NebUHPINjbLyb7OouZf9bSiRD3pcCMv-Cht8daRQhYUsA&gsessionid=PXvWktNL-LtnkbHeft_AvVhYG_RrSwJ0LisSTuFV_efI348GY4VQvQ)  
  <sub>Kalkine, 2 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 99.85 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 101.61 (-1.7%), 50d 98.51 (+1.4%), 200d 104.48 (-4.4%); 50d below 200d
Momentum: RSI(14) 48.4 | MACD 0.591 vs signal 1.068 (histogram -0.478)
Returns: 1d -0.9% | 5d -1.5% | 1m +4.4% | 3m -6.2%
52-week range: 92.84 - 121.36 (now 24.6% of the way up)
Volatility: ATR(14) 2.79 (2.8% of price) | annualised 20d 38.1%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 18.48 | P/B 2.18 | P/S 1.27 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +7.2% a year | beta to the market 1.40
Cost and size: expense ratio 0.35% | net assets 1.63B
What it is made of: Stocks 100.9%, Cash -0.9%
Largest holdings: Allegion PLC 3.9%, SharkNinja Inc 3.9%, Masco Corp 3.7%, Wayfair Inc Class A 3.7%, Cavco Industries Inc 3.7%
Sector mix: Consumer cyclical 62.4%, Industrials 32.7%, Basic materials 3.5%, Real estate 1.5%
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
Rolled up from the 5 largest holdings, 18.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.86 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.8% above the current prices
Holdings read: ALLE, SN, MAS, W, CVCO
Recent rating changes among them:
  - ALLE: 2026-11-03 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - SN: 2026-11-09 Guggenheim: main, Buy -> Buy
  - MAS: 2026-11-05 Argus Research: main, Buy -> Buy
  - W: 2026-11-12 Argus Research: main, Buy -> Buy
  - CVCO: 2026-11-02 Oppenheimer: reit, Outperform -> Outperform
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
Share count change: 1 week: +4.2% (65.83M) over 7d | 1 month: +9.3% (139.57M) over 30d
Shares outstanding: 16.47M | fund size: 1.64B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Rising Token Usage to Favor AI Investing? ETFs in Focus](https://www.zacks.com/stock/news/3032284/rising-token-usage-to-favor-ai-investing-etfs-in-focus)  
  <sub>Zacks Investment Research, 1 hour ago</sub>  
  AI token usage is surging as costs fall, but rising consumption alone may not guarantee profitability in the short term. Explore ETFs positioned for AI...
- [Take-Two Is Surging on GTA VI's Launch, and Your Index Fund Might Be Along for the Ride Without You Knowing It](https://247wallst.com/investing/etf/2026/11/18/take-two-is-surging-on-gta-vis-launch-and-your-index-fund-might-be-along-for-the-ride-without-you-knowing-it/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  GTA VI just lit up Take-Two's stock, but the bigger story sits inside your retirement account. Three kinds of funds hold the stock, and they feel this...
- [Yes, You Can Invest in Grand Theft Auto VI (GTA 6). Here's How.](https://www.google.com/goto?url=CAESogEBxCJF11b9aJPg2Y_mDstSliX5Toj7LDc6isqPG8aRFiMZkxn31aWpQWgFwERAmXJWMP9Pwyirr7COe0sbLe6ES3SzygKp1JUpCHqwd5MLXzx9etxaqeWNhEzXReoUu_a73wjHELJitMJkg0NyzejBB9HXZtWblAIpRntjqdNK8AdOxVU9EfZY1I0U8XkEXgun-SalF5TDEF42FrfHdgbWlOQ&gsessionid=syRFxnRxLP3SxcQqOAgAATLEdtFgepUk4jEXQhkUj-9rv1WIxXmRkg)  
  <sub>The Motley Fool, 15 hours ago</sub>  
  Investors have several options for buying GTA 6-related investments.
- [Disney's Better-Than-Expected Q4 Results Put These ETFs in Focus](https://www.google.com/goto?url=CAES0QEBxCJF18p0CN5PcPRlwGrniMfL1eqOS7Vl4xVz7JkSAyox-sRO9RB2VVamQUi0wt8IcGR9mhufmVUrdYvQxrrB_uh07-yQiRHaG93bPZveWy8CV_rK0_KoVq1LjE8gfkA2OLdXrQm0zqvNGEu7AsvWDTvHPNuzhGtK6Hk8mHbRTBQYwEUc4wMT52ytSJtMYjndHB26HHgoskBg0OwgwFDGPflVwsThyo2MCDDDlC204DzL10P6rMCfcnJYlqOVK1KZa1GPq-KM9qh8yRoqBrkXiA&gsessionid=syRFxnRxLP3SxcQqOAgAATLEdtFgepUk4jEXQhkUj-9rv1WIxXmRkg)  
  <sub>The Globe and Mail, 22 hours ago</sub>  
  On Nov. 17, before market open, Walt Disney CompanyDIS reported fourth-quarter fiscal 2026 adjusted earnings of $1.77 per share, significantly up 59.5% year...
- [Here’s how to invest in Grand Theft Auto VI (GTA 6)](https://www.google.com/goto?url=CAESggEBxCJF126MyzwKezMY-ljOl-rs3Aw61I6d-U84pZTMNrsxJcWgrb7sKI7WP_gnN3YQx-Zo7nbEXrRaHjeFM13fkR2YTviwnh3f4a-0nEde5t6OZdqsOUyKL6iqAc9ch1wPpDrbUB1mB38Rwdd7wpg-oHCVZGqtkd9gataKSE6UxRNl&gsessionid=syRFxnRxLP3SxcQqOAgAATLEdtFgepUk4jEXQhkUj-9rv1WIxXmRkg)  
  <sub>Finbold, 4 hours ago</sub>  
  Yes, you can invest in GTA 6. Here are a couple of options after the game's highly anticipated launch in November 2026.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 106.35 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 104.85 (+1.4%), 50d 108.95 (-2.4%), 200d 112.11 (-5.1%); 50d below 200d
Momentum: RSI(14) 48.7 | MACD -0.477 vs signal -0.848 (histogram 0.371)
Returns: 1d +0.7% | 5d -1.1% | 1m -2.4% | 3m -4.5%
52-week range: 99.90 - 120.08 (now 32.0% of the way up)
Volatility: ATR(14) 1.96 (1.8% of price) | annualised 20d 22.9%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: n/a
What it holds: P/E n/a | P/B n/a | P/S n/a | 3y earnings growth n/a
Yield: n/a
Three-year record: n/a a year | beta to the market n/a
Cost and size: expense ratio n/a | net assets n/a
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
Share count change: 1 week: +2.3% (497.49M) over 7d | 1 month: -0.2% (-50.14M) over 30d
Shares outstanding: 203.75M | fund size: 21.67B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- fund equity_holdings unavailable: HTTP Error 401:
- fund bond_holdings unavailable: HTTP Error 401:
- fund bond_ratings unavailable: HTTP Error 401:
- fund fund_operations unavailable: HTTP Error 401:
- fund fund_overview unavailable: HTTP Error 401:
- fund top_holdings unavailable: HTTP Error 401:
- fund sector_weightings unavailable: HTTP Error 401:
- fund asset_classes unavailable: HTTP Error 401:

## Commodities

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: Treasury yields stable, inflation and unemployment in line with expectations
- Technicals show short‑term downtrend but no decisive break on volume; RSI near oversold, MACD still negative
- Positioning shows moderate net long (17.1% OI) with a small weekly decrease (-1.7%); crowding at 83th percentile, not extreme
- Cost of holding is heavy (-8.3% annual), dragging long performance but not a directional signal

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 10.58 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 11.23 (-5.8%), 50d 11.54 (-8.3%), 200d 10.33 (+2.4%); 50d above 200d
Momentum: RSI(14) 30.8 | MACD -0.249 vs signal -0.197 (histogram -0.052)
Returns: 1d -2.6% | 5d -3.9% | 1m -13.6% | 3m -5.6%
52-week range: 9.02 - 12.47 (now 45.2% of the way up)
Volatility: ATR(14) 0.20 (1.9% of price) | annualised 20d 28.3%
Volume: 0.05x the 20-day average
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
Cost of holding this fund instead of sugar itself: -8.3% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -5.6%, commodity +0.1%, gap -5.7% | 6 months: fund +5.3%, commodity +18.3%, gap -13.0% | 12 months: fund +11.6%, commodity +19.9%, gap -8.3%
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
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-11-10, published the following Friday)
Large speculators: net long 17.1% of open interest (1,145,979 contracts)
Change on the week: -1.7% of open interest
Crowding: 83% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -0.1% (-44.24K) over 7d | 1 month: +25.0% (11.37M) over 30d
Shares outstanding: 5.38M | fund size: 56.91M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, mixed positioning and flow signals, heavy roll cost, and down‑trend technicals balance each other.

**Main reasons it gave:**
- Positioning: net short fell 1.6% of open interest (bullish pressure)
- Fund flows: 1-month outflows of 13.3% (bearish pressure)
- Cost of holding: -9.1% annual roll cost (heavy cost for long)
- Technicals: price below 20-day SMA, RSI 36.8 (downtrend)

<details><summary><b>News</b> — score +0.00</summary>

- [Wheat leads losses in US grain futures, falling to lowest since January](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0f7f7c0b4daaae250d1c471365a8&url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fwheat-leads-losses-in-us-grain-futures-falling-to-lowest-since-january%2far-AA2hJDSQ&c=303495965112692920&mkt=en-us)  
  <sub>Seeking Alpha on MSN, 24h ago</sub>  
  CBOT December wheat futures fell $0.25 to $5.70 per bushel on Wednesday, the contract's lowest level since January, leading the market lower as part of a broad selloff in commodities. The dollar ...
- [CBOT corn may fall into $4.19-1/4 to $4.27-1/2 range](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0f7f7c0b4daaae250d1c471365a8&url=https%3a%2f%2fwww.tradingview.com%2fnews%2freuters.com%2c2026%3anewsml_L2N4700BL%3a0-cbot-corn-may-fall-into-4-19-1-4-to-4-27-1-2-range%2f&c=7596372133655743888&mkt=en-us)  
  <sub>TradingView, 15h ago</sub>  
  ZC1! may fall into a range of $4.19-1/4 to $4.27-1/2 per bushel, as suggested by its wave pattern and a projection analysis.The market has broken a support at $4.35-1/2, the 214.6% projection level of ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 17.08 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 17.29 (-1.2%), 50d 18.38 (-7.0%), 200d 18.17 (-6.0%); 50d above 200d
Momentum: RSI(14) 36.8 | MACD -0.332 vs signal -0.373 (histogram 0.040)
Returns: 1d +1.2% | 5d -0.0% | 1m -5.0% | 3m -10.1%
52-week range: 16.47 - 20.29 (now 16.1% of the way up)
Volatility: ATR(14) 0.24 (1.4% of price) | annualised 20d 14.6%
Volume: 0.83x the 20-day average
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
Cost of holding this fund instead of corn itself: -9.1% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -10.1%, commodity -6.1%, gap -4.0% | 6 months: fund -6.7%, commodity -1.8%, gap -4.9% | 12 months: fund -5.2%, commodity +3.9%, gap -9.1%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.20</summary>

```text
Corn rated good or excellent: 56% of the US crop (week 43 of 2026)
Direction over 2 weeks: not enough readings to say
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
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 1.1% of open interest (1,979,758 contracts)
Change on the week: -1.6% of open interest
Crowding: 33% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +0.9% (909.81K) over 7d | 1 month: -13.3% (-16.24M) over 30d
Shares outstanding: 6.21M | fund size: 106.05M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance given lack of material macro surprise, mixed technicals, modest positioning, and cost drag.

**Main reasons it gave:**
- No macro surprise: yields and inflation unchanged, no policy shift
- Technicals: price below 20d, 50d, 200d SMAs, RSI 23.4 (oversold) but no decisive break on volume
- Positioning: net long 11.2% OI, small weekly increase (+0.5%), crowding indicates historically short bias
- Fund flows: net inflows (+4.2% week) but cost of holding -3.4% annual drag

<details><summary><b>News</b> — score +0.00</summary>

- [Commodities Fall With A Thud](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0f1158f8418889a7827a2c48d7e3&url=https%3a%2f%2fseekingalpha.com%2farticle%2f4969867-commodities-fall-with-thud&c=13167228631723951333&mkt=en-us)  
  <sub>Seeking Alpha, 22h ago</sub>  
  After months of bucking the downtrends in gold, platinum, and silver, copper prices have played catch-up in the last few weeks.
- [Wednesday’s Charts – The S&P 500 Clings to Its Uptrend Line as Commodities Slip Further](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0f1158f8418889a7827a2c48d7e3&url=https%3a%2f%2fpro.thestreet.com%2fmarket-commentary%2fwednesdays-charts-the-sp-500-clings-to-its-uptrend-line-as-commodities-slip-further&c=15615491045096217385&mkt=en-us)  
  <sub>TheStreet Pro, 24h ago</sub>  
  DMA for a second day but held its uptrend line, while copper had its worst day since July 2025, gold its lowest close since September 2025 and bitcoin its lowest since mid-July. This is the companion ...
- [United States Copper Index Fund](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0f1158f8418889a7827a2c48d7e3&url=https%3a%2f%2fwww.wsj.com%2fmarket-data%2fquotes%2fmutualfund%2fCPER&c=15684457593770213374&mkt=en-us)  
  <sub>Wall Street Journal, 23h ago</sub>  
  The Fund seeks to reflect the daily changes in percentage terms of the SummerHaven Copper Index Total Return. This Index is designed as a benchmark for investors seeking attractive risk-adjusted ...
- [Kurv Copper & Mining Enhanced Income ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0f1158f8418889a7827a2c48d7e3&url=https%3a%2f%2fmarkets.businessinsider.com%2fetfs%2fkurv-copper-mining-enhanced-income-etf-us5009488314&c=12239846957817661186&mkt=en-us)  
  <sub>Business Insider, 21h ago</sub>  
  Copyright © 2026 Insider Inc and finanzen.net GmbH (Imprint). All rights reserved. Registration on or use of this site constitutes acceptance of our Terms of Service ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 34.07 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 37.85 (-10.0%), 50d 39.01 (-12.7%), 200d 37.94 (-10.2%); 50d above 200d
Momentum: RSI(14) 23.4 | MACD -1.202 vs signal -0.782 (histogram -0.421)
Returns: 1d -0.1% | 5d -8.5% | 1m -13.8% | 3m -14.8%
52-week range: 30.77 - 41.43 (now 31.0% of the way up)
Volatility: ATR(14) 0.72 (2.1% of price) | annualised 20d 29.1%
Volume: 0.33x the 20-day average
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
Cost of holding this fund instead of copper itself: -3.4% a year -- a steady drag
Measured: 3 months: fund -14.8%, commodity -14.0%, gap -0.8% | 6 months: fund -11.7%, commodity -9.6%, gap -2.1% | 12 months: fund +10.6%, commodity +14.0%, gap -3.4%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-11-10, published the following Friday)
Large speculators: net long 11.2% of open interest (314,115 contracts)
Change on the week: +0.5% of open interest
Crowding: 3% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +4.2% (25.34M) over 7d | 1 month: +2.0% (12.08M) over 30d
Shares outstanding: 18.40M | fund size: 627.01M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise; technicals bearish but no decisive break; positioning modestly bullish; cost of holding near zero; flat fund flows.

**Main reasons it gave:**
- Fed target unchanged at 4.00% and yields only marginally changed, no policy surprise
- Technical downtrend (price below 20d, 50d, 200d SMAs, RSI 29.9) with low volume, no decisive break
- Large speculators net long 27.8% with modest weekly increase of +1.8%, indicating moderate bullish sentiment
- Cost of holding near zero (-0.6% annual), not a strong tailwind for short

<details><summary><b>News</b> — score +0.00</summary>

- [Gold price falls as Fed hike odds jump and GLD, IAU ETF outflows surge](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0efff6304f5c95a86c7fcc401c31&url=https%3a%2f%2finvezz.com%2fnews%2f2026%2f11%2f19%2fgold-price-falls-as-fed-hike-odds-jump-and-gld-iau-etf-outflows-surge%2f&c=8391119509951579352&mkt=en-us)  
  <sub>Invezz, 22h ago</sub>  
  Gold has been in a strong sell-off in the past few months as demand among investors waned. ETF Database data shows that the SPDR Gold ETF GLD has had over $1.37 billion in outflows in the last 30 days ...
- [Nasdaq, Dow, S&P 500 Futures Climb Ahead Of Anthropic’s Record Debut: SLS, GLD, TTWO, UNH In Focus](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0efff6304f5c95a86c7fcc401c31&url=https%3a%2f%2fstocktwits.com%2fnews-articles%2fmarkets%2fequity%2fnasdaq-dow-s-and-p-500-futures-climb-ahead-of-anthropic-s-record-debut-sls-gld-ttwo-unh-in-focus%2fcNbLDbCR9iW&c=16693970838677579485&mkt=en-us)  
  <sub>Stocktwits, 18h ago</sub>  
  On Wednesday, the three U.S. benchmark indexes closed mixed. The Dow Jones Industrial Average shed more than 650 points to end the session 1.11% lower, while the S&P 500 fell 0.23%. The Nasdaq ...
- [Gold, silver divide widens: Why SLV looks riskier than GLD as Fed rate fears mount](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0efff6304f5c95a86c7fcc401c31&url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fgold-silver-divide-widens-why-slv-looks-riskier-than-gld-as-fed-rate-fears-mount%2far-AA2hHX6Q&c=5555130753426001832&mkt=en-us)  
  <sub>Benzinga on MSN, 31h ago</sub>  
  The widening gap between gold and silver prices is raising fresh questions about the relative risks of investing in precious metals ETFs, with silver emerging as the more vulnerable trade amid ...
- [Gold's bad year is getting worse. Why its price keeps falling](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0efff6304f5c95a86c7fcc401c31&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2fother%2fgold-s-bad-year-is-getting-worse-why-its-price-keeps-falling%2far-AA2hLWtr&c=14648582880766008525&mkt=en-us)  
  <sub>CNBC on MSN, 9h ago</sub>  
  Gold has fallen sharply from its January record as higher interest rates and a stronger dollar change the investment case for the precious metal.
- [Gold and silver stocks drop: What's going on?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0efff6304f5c95a86c7fcc401c31&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2ftop-stocks%2fgold-and-silver-stocks-drop-what-s-going-on%2far-AA2hIzO7&c=2527724186285312074&mkt=en-us)  
  <sub>Benzinga on MSN, 28h ago</sub>  
  SPDR Gold Shares ETF (NYSE:GLD) and iShares Silver Trust (NYSE:SLV) are falling Wednesday as both funds trade at their lowest levels since September 2025. SPDR Gold Shares stock is at significant ...
- [Bitcoin Bounces From $62K: Is Gold and Silver’s 14% Crash Sending Money Into Crypto?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0efff6304f5c95a86c7fcc401c31&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fcrypto%2farticles%2fbitcoin-bounces-62k-gold-silver-093005595.html&c=14619913712059101684&mkt=en-us)  
  <sub>Yahoo Finance, 14h ago</sub>  
  In today’s Bitcoin news, on November 19, silver and gold are extending their sell-off, but Bitcoin is holding its ground near $63,800. BTC has bounced off the $62,000 level for the second time in four ...
- [Gold Plunges 30% From Record High to 14-Month Low on Fed Hawkishness, Strong Dollar](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0efff6304f5c95a86c7fcc401c31&url=https%3a%2f%2ffinance.biggo.com%2fnews%2f7ba1c92d-5d28-4538-b1b3-d4693b736170&c=13208950157670464347&mkt=en-us)  
  <sub>finance.biggo, 9h ago</sub>  
  International gold prices tumbled to a 14-month low, pressured by fears of further Federal Reserve rate hikes and a stronger dollar. December ...
- [Nvidia Reversal and Metals Slide Draw Options Focus](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0efff6304f5c95a86c7fcc401c31&url=https%3a%2f%2fozarab.media%2fnvidia-reversal-and-metals-slide-draw-options-focus%2f&c=1116351868773332095&mkt=en-us)  
  <sub>ozarab.media, 23h ago</sub>  
  Nvidia reversed despite strong earnings as copper and gold fell, while options activity drew attention ahead of Anthropic’s expected IPO. #Nvidia #Gold #Options ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 339.64 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 362.83 (-6.4%), 50d 376.51 (-9.8%), 200d 406.45 (-16.4%); 50d below 200d
Momentum: RSI(14) 29.9 | MACD -8.581 vs signal -6.278 (histogram -2.302)
Returns: 1d -0.5% | 5d -4.3% | 1m -10.4% | 3m -19.8%
52-week range: 339.64 - 495.90 (now 0.0% of the way up)
Volatility: ATR(14) 6.60 (1.9% of price) | annualised 20d 28.6%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.05</summary>

```text
Cost of holding this fund instead of gold itself: -0.6% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund -19.8%, commodity -20.7%, gap +0.9% | 6 months: fund -18.5%, commodity -18.3%, gap -0.3% | 12 months: fund -9.3%, commodity -8.7%, gap -0.6%
A commodity fund holds futures, not gold, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

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

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: GOLD - COMMODITY EXCHANGE INC. (positions as of 2026-11-10, published the following Friday)
Large speculators: net long 27.8% of open interest (404,725 contracts)
Change on the week: +1.8% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 260.30M | fund size: 88.41B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fed rate expectations: market pricing ~4 hikes over 2 years – bearish for silver
- Fund inflows: share count +9.6% week, +6.2% month – bullish demand
- Technical: RSI 27.6 (oversold) but price 33% below 200d SMA – mixed
- Cost of holding: -1% per year drag – slight negative for long

<details><summary><b>News</b> — score +0.00</summary>

- [Gold-Silver Ratio Hits One-Year High as Fed Rate Fears Hit SLV Harder Than GLD](https://finance.biggo.com/news/6bfcd3c6-78d1-4fea-bb2c-296da62919f9)  
  <sub>BigGo Finance, 22 hours ago</sub>  
  The gold-to-silver ratio rose to a one-year high of 82.6 on Wednesday as both metals extended losses, with silver falling harder. December gold…
- [Gold, Silver Divide Widens: Why SLV Looks Riskier Than GLD As Fed Rate Fears Mount](https://www.benzinga.com/etfs/sector-etfs/26/11/63394802/gold-silver-divide-widens-why-slv-looks-riskier-than-gld-as-fed-rate-fears-mount)  
  <sub>Benzinga, 23 hours ago</sub>  
  The widening gap between gold and silver prices is raising fresh questions about the relative risks of investing in precious metals ETFs, with silver...
- [Gold hits 14-month low: Why are silver and copper prices falling too? Experts explain what investors should do now](https://www.google.com/goto?url=CAES8gEBxCJF1wKaGA9Q3VCn0cCKMRvwacpAvHEaTTfz53FY-y2dc4FPvhnTFNnrkE0SwLyE0MXaRjRm49fSg3nC6oE8EXmDu1EgfSTuFgEJvxAUa8LhRuc-sXBtzbFf2v9zTVQimgcxsYtTfhiIED9eUjK6sEKYHN3RytgsRg13lh0MjwVHLENWjLye0cebOBJcwgH9KUR0ojeG_OII3fzF0SavC79nksY5vnIjOW1ARHDJBtjAroPc2BQDuAL3K2hNmOXpFa8QvniMuthTRYzCyfvHzHwxxvZOWx8uYo0G2I7puz2l4MWgQXliEPmXcyHBtGW1LA&gsessionid=bU3CjAEjrPvz3TI0fpJ-AB6uB-T9iNZhD1lw31kIkRh-e0KW2SYt3g)  
  <sub>Livemint, 8 hours ago</sub>  
  Gold, silver, and copper prices have witnessed a sharp selloff amid a stronger US dollar, rising Treasury yields, and concerns over global demand.
- [Silver mining ETF sees biggest ever outflows and steep drop, Otavio (Tavi) Costa notes](https://www.google.com/goto?url=CAESlgEBxCJF1xkhFlO5-8IN1VuG_D7czBJBc5QesY2c4YW0IIxeosaDhf_Rb5SQdkm-3Lwr4epiZtHoQquywAv_ZpoKDSKkuSC2XCMTfTML0O6fDuB2yULGyogG69ETK1T8KqsWpfciqWEhftTZSjQAlt1Z0WuLNQ0HTNuiUH3HQIkn78c2AaumMP9_rA17IEFrolMA9T7uwtQ&gsessionid=bU3CjAEjrPvz3TI0fpJ-AB6uB-T9iNZhD1lw31kIkRh-e0KW2SYt3g)  
  <sub>Traders Union, 15 hours ago</sub>  
  Silver miners' biggest ETF saw record outflows and more than a 50% decline in six months, Otavio (Tavi) Costa reports.
- [Silver ETFs decline up to 2%, Hindustan Zinc shares down as precious metal crashes up to 5%](https://www.google.com/goto?url=CAES1wEBxCJF10Arqh47ihCm3ROx7ghg4_ks8eZrClYToo9ZAakszFY2CsHDPyj5uce0vlCpLt8Vdvzm_rhPvJ1nI9D9CJaGVpM0GLbyRNDVy_jKoqCP83tMV3afMrt39IKItq4VmJIY7diICpD40m2tD0qco2KI3Msr_apexrDUrnSToqm6ug1gd7_Rq9TkiV4vaaYWOhGRxm8duMrX78_4RH4eAd_Tn-8g1z-Q_OxKajQM2H-jJdnd0QDB3zzr14qQ6uwd-JJTVxMRCVniFc1N_ELSNaI88G_S2Q&gsessionid=bU3CjAEjrPvz3TI0fpJ-AB6uB-T9iNZhD1lw31kIkRh-e0KW2SYt3g)  
  <sub>Moneycontrol.com, 8 hours ago</sub>  
  Silver exchange-traded funds (ETFs) declined by up to 2 per cent on Thursday, tracking a sharp fall in international silver prices, which dropped by as much...
- [Silver ETF, Suzlon, TFCI among top traded mid-, small-caps under MTF in Nov](https://www.google.com/goto?url=CAESmAIBxCJF12_SEuJNP8do4hjgGyTZR3dQWrZtzeF_gs9_fKRt3W7gU8ETThs9OqdOyQsnWolsRTGiaMyqQpp3DUCbW6ssmGatMS5pyO5R9Hj-R0l5ROdtPW7GPG8qHSvkBA0uN-SWWZwV3HwtG2GxzGrElW4WsZdvtNzfkHBcxl1eXZwtn0Bzh7lKGcm9N-rgAJZlwb8h1AKIcBrXCGiPdvYcvZpuQrTpqYUOB0GH6Q0UAzv42Vp_MJrrfnLgUn5E6MoK4UlvwnN8URQ_IBbPla1S26PhUfHTZOe3ZV2ai7O09y9v0H7lq9Rup-mD-UdIwk3RvdFeiPgvW9_FkclIGuPsODH1FLiI79XWZ1VAPNeC5yJU568VPL7b&gsessionid=bU3CjAEjrPvz3TI0fpJ-AB6uB-T9iNZhD1lw31kIkRh-e0KW2SYt3g)  
  <sub>Business Standard, 11 hours ago</sub>  
  MTF Stocks: The 15 most actively traded mid- and small-caps via MTF on an average gained 3.8% so far in November, while the average gain of Midcap 150 and...
- [Invesco India Silver ETF Fund of Fund - Dir (G)](https://www.google.com/goto?url=CAESmAEBxCJF13OxR1LHpwaEvCl1EV50JAsPr7ZCfVJ2fNLuhLX9m9TU_o6DP5WLnmr1KIK7F3tKcvGFrB2iWox0x_zxU0LDWgiebBgwy-AdZmVmEtxhUOa78XZGJqeWQR-4MAZcSDLTEx6NOFNFS27f91BydsxDa19b0s0Bp9EJK6iTRfsHVfGx0wkHkYOPI1vz1HpqPz5o9fkQtw&gsessionid=bU3CjAEjrPvz3TI0fpJ-AB6uB-T9iNZhD1lw31kIkRh-e0KW2SYt3g)  
  <sub>Multibagg AI, 12 hours ago</sub>  
  Invesco India Silver ETF Fund of Fund - Dir (G) latest NAV, returns, AUM, expense ratio, holdings, asset allocation, peer comparison and risk metrics.
- [Gold-silver price ratio crosses 82: What does this indicate? Where should investors start ETF SIPs for 2027? Experts say](https://www.google.com/goto?url=CAES9gEBxCJF19CRaaEX_F_Biex3XajY0wAqKlsqEQE1Hxj28ZjYDsQr1_UqYNJUVJ_a_V8K5bznlNtemDGsQNWFK7FJT1tmAR8xcupVv9HyJhJVfTn7TygJ6hRgZcE9YyiFEXqBqQQL2HNWMxQcVN_SUhML-vbpi9DVSBrdNcjxqpnRjK2KIYyT05c2dQ3zr-a_PJ7ki0iwbkRKrPlr8mXN2B0CIgaGWmYVcK14t7UKdGCjgwmQn1ChGalIGnpxrJ07BFB5-Zuc5eJwAyDQ-bM-71nKUmYVCOB3TQZkjD4FnZYD2IzwGjEW7oxAXahMjP91ARCdKCykA5c&gsessionid=bU3CjAEjrPvz3TI0fpJ-AB6uB-T9iNZhD1lw31kIkRh-e0KW2SYt3g)  
  <sub>Livemint, 12 hours ago</sub>  
  Gold-silver ratio crosses 82 as both metals correct sharply, with silver falling more than gold. Experts explain what the elevated ratio signals and...
- [Gold and silver weather a perfect storm as demand holds firm](https://www.google.com/goto?url=CAESnQEBxCJF1zBz7kYLiQnOZxqcM0fygKeg_etkF86cqzlxBKJ6woi3A6VeL9sdZmjfh8T03vrm6co6pz-fW5jcpTK1BjObs_5-1miXnu8Cuqv56Mq4qUjd0ZfyubfiDfSRsZw5lt4XI5zTkOAiiY3eAi-oi6no2tiLLjqSdl9PV4YWV1HZiD4DWVhfA0FxFIiXP7wHa2-9Jn3uMXttq003&gsessionid=bU3CjAEjrPvz3TI0fpJ-AB6uB-T9iNZhD1lw31kIkRh-e0KW2SYt3g)  
  <sub>Kitco, 21 hours ago</sub>  
  (Kitco Commentary) - Key Takeaways. Positioning, Not Demand, Drove the Selloff: **Gold fell 6.80% to a 52-week low, but ETF holdings rose to 100.97 million...
- [Gold and silver sink to 14-month lows as hawkish Fed commentary boosts dollar (GLD:NYSEARCA)](https://www.google.com/goto?url=CAESsAEBxCJF1zNm0HM6awzM-VEVLuSLmw87TC6Zu-C48gIHKuxb5Q48Y4Iv4z9n6BS4kc_iMDwA2QBWTLJD-VJUZK8mUgrmF7eaB0D1J3WVPv-V7yHsjsZJWNVEr5eBCwVdIoAKSz0AsQrrHWeoqQMK3DcVV3PFasc1csOO7J8xKw3xrViD-XLSywA2tzSeFMz519rjeC2x8RLHf2xws3erXjATN__JFf9P-0leJJD_nvruaQ&gsessionid=bU3CjAEjrPvz3TI0fpJ-AB6uB-T9iNZhD1lw31kIkRh-e0KW2SYt3g)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  Gold and silver futures fell to their lowest levels since September 2025, pressured by a stronger dollar and expectations of further interest rate hikes by...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 40.99 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 45.80 (-10.5%), 50d 51.46 (-20.3%), 200d 61.23 (-33.1%); 50d below 200d
Momentum: RSI(14) 27.6 | MACD -2.702 vs signal -2.383 (histogram -0.319)
Returns: 1d +0.7% | 5d -9.2% | 1m -21.6% | 3m -34.6%
52-week range: 40.70 - 105.60 (now 0.4% of the way up)
Volatility: ATR(14) 1.49 (3.6% of price) | annualised 20d 42.9%
Volume: 0.25x the 20-day average
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
Cost of holding this fund instead of silver itself: -1.0% a year -- a steady drag
Measured: 3 months: fund -34.6%, commodity -34.7%, gap +0.0% | 6 months: fund -41.0%, commodity -40.6%, gap -0.3% | 12 months: fund -11.1%, commodity -10.1%, gap -1.0%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-11-10, published the following Friday)
Large speculators: net long 3.1% of open interest (115,652 contracts)
Change on the week: -0.4% of open interest
Crowding: 5% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +9.6% (2.11B) over 7d | 1 month: +6.2% (1.40B) over 34d
Shares outstanding: 585.18M | fund size: 23.99B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No clear macro surprise or decisive technical break; mixed technicals, moderate bearish positioning and fund outflows, and a 2.5% annual roll cost suggest slight downside but not enough for a directional call.

**Main reasons it gave:**
- Inflation 3.7% reported, no clear surprise
- Technical indicators mixed: RSI 42.7, price just below 20‑day SMA
- Fund outflows of -10% over the past month
- CFTC speculators reduced net long by -2.8% week‑over‑week
- Cost of holding 2.5% annual roll cost

<details><summary><b>News</b> — score +0.00</summary>

- [Wheat leads losses in US grain futures, falling to lowest since January](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0f9780254d2293692afb902641cb&url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fwheat-leads-losses-in-us-grain-futures-falling-to-lowest-since-january%2far-AA2hJDSQ&c=303495965112692920&mkt=en-us)  
  <sub>Seeking Alpha on MSN, 24h ago</sub>  
  CBOT December wheat futures fell $0.25 to $5.70 per bushel on Wednesday, the contract's lowest level since January, leading the market lower as part of a broad selloff in commodities. The dollar ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 25.75 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 25.87 (-0.5%), 50d 26.82 (-4.0%), 200d 25.35 (+1.6%); 50d above 200d
Momentum: RSI(14) 42.7 | MACD -0.287 vs signal -0.338 (histogram 0.051)
Returns: 1d +0.6% | 5d +0.1% | 1m -3.2% | 3m -1.9%
52-week range: 21.71 - 28.14 (now 62.8% of the way up)
Volatility: ATR(14) 0.28 (1.1% of price) | annualised 20d 15.3%
Volume: 0.05x the 20-day average
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
Cost of holding this fund instead of soybeans itself: 2.5% a year -- the roll has been paying this fund
Measured: 3 months: fund -1.9%, commodity -0.2%, gap -1.7% | 6 months: fund +2.9%, commodity +2.4%, gap +0.5% | 12 months: fund +8.5%, commodity +6.0%, gap +2.5%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-11-10, published the following Friday)
Large speculators: net long 12.1% of open interest (973,693 contracts)
Change on the week: -2.8% of open interest
Crowding: 32% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +0.3% (120.08K) over 7d | 1 month: -10.0% (-4.36M) over 30d
Shares outstanding: 1.52M | fund size: 39.04M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Technical indicators modestly bullish (MACD 0.047 > signal -0.084, RSI 57.3) but no decisive break
- Fundamental bearish: cost of holding -3.1% a year, inventory build +61 BCF (94% percentile), EIA forecast price drop ~11% over six months
- Positioning shows crowded short (net short 13.7% OI, 2% percentile) with slight reduction (-0.2% change)
- Macro environment stable: yields unchanged, inflation 3.7% in line with expectations, VIX elevated but no surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 10.53 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 9.74 (+8.1%), 50d 10.28 (+2.4%), 200d 10.94 (-3.8%); 50d below 200d
Momentum: RSI(14) 57.3 | MACD 0.047 vs signal -0.084 (histogram 0.131)
Returns: 1d -0.8% | 5d +0.7% | 1m +5.6% | 3m +5.4%
52-week range: 9.00 - 16.90 (now 19.4% of the way up)
Volatility: ATR(14) 0.38 (3.7% of price) | annualised 20d 47.1%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.60</summary>

```text
Cost of holding this fund instead of natural gas itself: -3.1% a year -- a steady drag
Measured: 3 months: fund +5.4%, commodity +21.6%, gap -16.2% | 6 months: fund -7.1%, commodity +11.7%, gap -18.8% | 12 months: fund -26.0%, commodity -22.9%, gap -3.1%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.60</summary>

```text
US inventories, week ending 2026-11-06 (published the following Wednesday)
  Natural gas: 3,862.0 billion cubic feet, +61.0 on the week (a build), 94% percentile over 52 weeks -- high for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.60</summary>

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
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 13.7% of open interest (1,642,671 contracts)
Change on the week: -0.2% of open interest
Crowding: 2% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +2.7% (13.67M) over 7d | 1 month: +22.9% (97.67M) over 34d
Shares outstanding: 49.84M | fund size: 524.78M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error captcha or protection page found) (Bing's feed, direct: 10 headline(s), none naming UNG)

### Oil (USO) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bearish fundamentals are offset by bullish fund flows and modest long positioning.

**Main reasons it gave:**
- EIA forecast expects WTI price to fall to $84 in 6 months (bearish)
- Crude oil inventories increased by 3.4M barrels (build) (bearish)
- Fund flows show strong inflows (+24.6% share count over 1 month) (bullish)
- CFTC positioning net long 1.3% of OI, up 0.2% week over week (bullish)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 138.91 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 151.64 (-8.4%), 50d 151.99 (-8.6%), 200d 128.88 (+7.8%); 50d above 200d
Momentum: RSI(14) 38.3 | MACD -4.268 vs signal -2.448 (histogram -1.819)
Returns: 1d +2.1% | 5d -4.9% | 1m -13.1% | 3m +3.2%
52-week range: 66.17 - 169.53 (now 70.4% of the way up)
Volatility: ATR(14) 5.15 (3.7% of price) | annualised 20d 50.3%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.80</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.80</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.80</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.80</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.80</summary>

```text
US inventories, week ending 2026-11-13 (published the following Wednesday)
  Crude oil: 417.8 million barrels, +3.4 on the week (a build), 25% percentile over 52 weeks
  Petrol: 215.9 million barrels, +5.2 on the week (a build), 56% percentile over 52 weeks
  Diesel: 104.9 million barrels, +1.6 on the week (a build), 33% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.80</summary>

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
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-11-10, published the following Friday)
Large speculators: net long 1.3% of open interest (1,917,473 contracts)
Change on the week: +0.2% of open interest
Crowding: 28% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.2% (3.72M) over 7d | 1 month: +24.6% (379.38M) over 34d
Shares outstanding: 13.83M | fund size: 1.92B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error captcha or protection page found) (Bing's feed, direct: 10 headline(s), none naming USO)

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro policy or data surprise; moderate net short position; heavy cost of holding; fund outflows; price below key moving averages.

**Main reasons it gave:**
- Large speculators net short 14.6% of open interest
- Fund share count down -9.7% over 1 month
- Cost of holding fund vs wheat -10.2% annualized
- Price below 20‑day, 50‑day and 200‑day moving averages
- US Treasury yields stable; no macro policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Wheat leads losses in US grain futures, falling to lowest since January](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0f89780645fabfefe7d19ba67258&url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fwheat-leads-losses-in-us-grain-futures-falling-to-lowest-since-january%2far-AA2hJDSQ&c=303495965112692920&mkt=en-us)  
  <sub>Seeking Alpha on MSN, 24h ago</sub>  
  CBOT December wheat futures fell $0.25 to $5.70 per bushel on Wednesday, the contract's lowest level since January, leading the market lower as part of a broad selloff in commodities. The dollar ...
- [Teucrium 2x Daily Wheat ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0f89780645fabfefe7d19ba67258&url=https%3a%2f%2fmarkets.ft.com%2fdata%2fetfs%2ftearsheet%2fsummary%3fs%3dWXET%3aPCQ%3aUSD&c=16397338446331531027&mkt=en-us)  
  <sub>FT Markets, 32h ago</sub>  
  Pricing for ETFs is the latest price and not "real time". Share price information may be rounded up/down and therefore not entirely accurate. FT is not responsible for any use of content by you ...
- [Australian Wheat Hits Two-Year High as Buyers Flee Black Sea](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6aff0f89780645fabfefe7d19ba67258&url=https%3a%2f%2fwww.livemint.com%2fmarket%2faustralian-wheat-hits-two-year-high-as-buyers-flee-black-sea-11795035834767.html&c=14378819238113639201&mkt=en-us)  
  <sub>Mint, 26h ago</sub>  
  Australian wheat prices climbed to a two-year high as strong export demand overshadows the start of the harvest, with buyers racing to replace stalled Black Sea supplies.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.02 on the week) | 5-year 4.91% (-0.03 on the week) | 10-year 5.09% (-0.01 on the week) | 30-year 5.43% (-0.01 on the week)
Yield curve, 10-year minus 3-month: +0.94 points -- upward sloping (normal)
US dollar index: 103.66 (+0.49 on the week)
Volatility (VIX): 22.48 (+3.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 21.53 (bar of 2026-11-19), from 502 daily bars
Trend: vs 20d SMA 21.97 (-2.0%), 50d 23.79 (-9.5%), 200d 23.62 (-8.9%); 50d above 200d
Momentum: RSI(14) 37.5 | MACD -0.620 vs signal -0.684 (histogram 0.064)
Returns: 1d +1.7% | 5d -0.2% | 1m -6.8% | 3m -15.3%
52-week range: 19.88 - 28.00 (now 20.3% of the way up)
Volatility: ATR(14) 0.43 (2.0% of price) | annualised 20d 22.8%
Volume: 0.19x the 20-day average
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
Cost of holding this fund instead of wheat itself: -10.2% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -15.3%, commodity -12.1%, gap -3.2% | 6 months: fund -12.1%, commodity -7.5%, gap -4.6% | 12 months: fund -0.6%, commodity +9.6%, gap -10.2%
A commodity fund holds futures, not wheat, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.10</summary>

```text
Wheat rated good or excellent: 48% of the US crop (week 47 of 2026)
Direction over 2 weeks: not enough readings to say
Same week last year: 55% (-7 points)
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
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 14.6% of open interest (553,579 contracts)
Change on the week: +1.6% of open interest
Crowding: 37% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.25</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -0.8% (-1.78M) over 7d | 1 month: -9.7% (-24.59M) over 30d
Shares outstanding: 10.68M | fund size: 229.98M
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

