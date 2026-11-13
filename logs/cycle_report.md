# Daily report

**13 Nov 2026, 18:00 Israel time (16:00 UTC)** · 80 names checked · 6 traded · 1 with a problem

**Answers with no explanation:** 10 of 62 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 7 | 9 | 0 |
| Whole-market funds | 14 | 0 | 14 | 0 |
| Sector and country funds | 41 | 2 | 38 | 1 |
| Commodities | 9 | 0 | 9 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| Poland (EPOL) · Sector or country | **Stop raised.** At +0.52R, following the price. Stop-loss raised 42.32 → 42.77. |
| US regional banks (KRE) · Sector or country | **Stop raised.** At +0.04R, following the price. Stop-loss raised 69.67 → 69.92. |
| MercadoLibre (MELI) · Company | **Stop raised.** At +0.03R, following the price. Stop-loss raised 1615.69 → 1612.69. |
| Novo Nordisk (NVO) · Company | **Stop raised.** At +0.08R, following the price. Stop-loss raised 38.63 → 38.64. |
| Teva Pharmaceutical (TEVA) · Company | **Stop raised.** At +1.29R, following the price. Stop-loss raised 41.01 → 41.52. |
| US media and communication (XLC) · Sector or country | **Stop raised.** At +2.38R, following the price. Stop-loss raised 104.47 → 104.93. |
| Elbit Systems (ESLT) · Company | **Holding.** +0.75R, holding 5 shares. Stop-loss 682.06. |
| Canada (EWC) · Sector or country | **Holding.** -0.19R, holding 116 shares. Stop-loss 58.92. |
| South Korea (EWY) · Sector or country | **Holding.** -0.37R, holding 51 shares. Stop-loss 152.20. |
| Brazil (EWZ) · Sector or country | **Holding.** +0.39R, holding 207 shares. Stop-loss 34.10. |
| HDFC Bank (HDB) · Company | **Holding.** +2.35R, holding 102 shares. Stop-loss 24.78. |
| Defence and aerospace (ITA) · Sector or country | **Holding.** +0.11R, holding 98 shares. Stop-loss 69.44. |
| Microsoft (MSFT) · Company | **Holding.** -0.64R, holding 9 shares. Stop-loss 512.86. |
| Nvidia (NVDA) · Company | **Holding.** +4.46R, holding 9 shares. Stop-loss 179.59. |
| Procter & Gamble (PG) · Company | **Holding.** +1.08R, holding 2 shares. Stop-loss 162.86. |
| US house builders (XHB) · Sector or country | **Holding.** -0.09R, holding 68 shares. Stop-loss 97.50. |
| US health care (XLV) · Sector or country | **Holding.** -0.24R, holding 37 shares. Stop-loss 182.28. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Eli Lilly (LLY) · Company — BULLISH, confidence 0.75

**Result:** REJECTED · no room for equity LLY under its 5% cap or the sleeve budget limit: equity 100589.13, price 1439.11, existing exposure 0.00, headroom 1396.00

**In the model's own words:**

> Strong ticker‑specific catalyst (China approval of Orforglipron) and guidance raise from Mounjaro/Zepbound demand, reinforced by four straight earnings beats and solid technical uptrend despite thin volume; fundamentals are robust but valuation is high, and insider sales are routine.

**Main reasons it gave:**
- China regulator approved Orforglipron weight‑loss pill (news)
- Guidance raise driven by strong Mounjaro and Zepbound demand (news)
- Four consecutive earnings beats (earnings record)
- Price above 20‑, 50‑ and 200‑day SMAs with positive momentum (technical)

<details><summary><b>News</b> — score +0.80</summary>

- [Here’s How Much You Would Have Made Owning Eli Lilly Stock In The Last 5 Years](https://www.benzinga.com/news/26/11/63237747/here-s-how-much-you-would-have-made-owning-eli-lilly-stock-last-5-years)  
  <sub>Benzinga, 27 minutes ago</sub>  
  Eli Lilly (NYSE:LLY) has outperformed the market over the past 5 years by 30.78% on an annualized basis producing an average annual return of 40.82%.
- [ETFs Are Buying Eli Lilly (LLY) on Nov. 11](https://finance.yahoo.com/markets/stocks/articles/etfs-buying-eli-lilly-lly-110112211.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. ETFs bought a net $154.5 million of Eli Lilly (LLY) on Wednesday, Nov. 11, as 49 funds added shares and 11 trimmed...
- [Eli Lilly Stocks Rise as China Approves Orforglipron Weight-Loss Pill](https://www.google.com/goto?url=CAESvwEBxCJF13CBhTVe7MzKsJ3j5WlBphgHrSKr0tiaiQPEw_36Q9fub9Bi3sxsJluDJnsZI7EKZDgvc-0kYBlKGjNrnSJmhXzhI-s69yfuNNenhOE5VbE-P9paVkwn01CupbQ0OLHoQoJ3pX0gh8ujDQ8NQ8OTTwEdA0xKCzhVK1YBTM2gxEvlz1avcv6wUCqs9JRoxsBlru0ES7uHVsMoDH7QnL5CRTvwt4wKEspPf-BhQe9f47KDJxfUFG0FHrFQ-A&gsessionid=jRrPlrFMV5IjB29DPt-1L6GhNIEDRXsh6trtHkDkEHzeOgcka_bkqA)  
  <sub>TradingView, 3 hours ago</sub>  
  Eli Lilly and Co NYSE:LLY shares rose 0.35% to $1442.39 at 9:40 a.m. ET in early regular-session trading on November 12 after China's medicines regulator...
- [LLY 261113 1530.00C (LLY261113C1530000) Stock Community & Discussion](https://www.google.com/goto?url=CAESegHEIkXXTt_JN02rv5O2Jxv5RMNwg8_JrQEt-Gkj4GCFeae8mM2y8drmhoGx6fPxDSuIrf_-cXl8OtPlQiZUNqtakL3pTHIV1FVePeAAgF-OwPOuLDmj0LQsMyrHUDKHgvuR8mWEvMUvuUs-ln6-SqjbBJChTK69RX04&gsessionid=jRrPlrFMV5IjB29DPt-1L6GhNIEDRXsh6trtHkDkEHzeOgcka_bkqA)  
  <sub>Moomoo, 13 hours ago</sub>  
  Find the latest LLY 261113 1530.00C (LLY261113C1530000)stock discussion in moomoo's forum, a popular stock community. Get stock reviews, comments and...
- [Is Eli Lilly Stock Ready If Factory Bills Outrun Its Cash?](https://www.google.com/goto?url=CAESsgEBxCJF12vYrftWYi2Nbo-3a75BR1u0sMPobYq93Y4IaMk5Ac_ng7KiVwX_Ww1KkYJa92_4OnixfrrvO8rb7uxP2YX6kUZbygmfTPDn5QQ3NzWVrQ8bF6HUBC-XYiKDT4RZHCVSziyYlQ7ApvCxDlGxFc_dd11GKEkaQ8W4aGMzIuOQqvayoHvjQHazCqL4SE1OVkRBrpQbPpQXLUWpQZy5DxbhNpJkI4CqsJggXl6d0qqy&gsessionid=jRrPlrFMV5IjB29DPt-1L6GhNIEDRXsh6trtHkDkEHzeOgcka_bkqA)  
  <sub>Trefis, 23 hours ago</sub>  
  For questions about this article or underlying research, email help@trefis.com.Eli Lilly (LLY) is in the middle of a U.S. factory build that the company...
- [Jefferies Raised Its Eli Lilly (LLY) Target to $1,700. Here’s What the Firm Is Counting On](https://www.google.com/goto?url=CAESnAEBxCJF17jTDbKvTVOoAXXkWsCpJqAJow9kqIE6PcRvjzMBgr1_E3XdjGiePEpmdkDWtKLQkKmOXUbBWZLvr1E-q8uOWjoAdky7sOuw_PelC8ljT7gJNB5AMoa1UJLFf2R1ZkSquzUA4O1l1-DKtkNplaze1x-pFM3Jyc5rDOJBuqcx7YqnJO3HwZRSA-ag0HM8liThRvFOiQEE_YY&gsessionid=jRrPlrFMV5IjB29DPt-1L6GhNIEDRXsh6trtHkDkEHzeOgcka_bkqA)  
  <sub>Yahoo Finance, 16 hours ago</sub>  
  We just published a list of the 10 Unrivaled Stocks to Buy for the Next Decade and Eli Lilly (NYSE:LLY) ranked 9th on this list. Wall Street had its worst...
- [Lilly's new Pennsylvania plant is expected to create 850 high-wage jobs and about 2,000 construction jobs.](https://www.google.com/goto?url=CAEStwEBxCJF1_zDTe4qDglhwJw5XMj5sMTPpiIA9Rfh_ir7BZnwn7FIv__5kmWRlHUiGJqO-QmhfQ60tBM820ZFPBSLrQC0GqS1upWdMcMwV31aYzLO0u0SV-8A7XPhKWa1PW16vMIXpJp75WxL5CuVvlOpdadY9ntoDKXc9pATKCdtcZVmieaBOehm3JFKnNhjC7_3Fgfa3ujgJ2FgpF8lahrCK-JU11-KuwP0yRSJjPtXQhhJuaM5mzk&gsessionid=jRrPlrFMV5IjB29DPt-1L6GhNIEDRXsh6trtHkDkEHzeOgcka_bkqA)  
  <sub>Stock Titan, 18 hours ago</sub>  
  Eli Lilly and Company (NYSE: LLY) broke ground on a $3.5 billion manufacturing facility in Pennsylvania's Lehigh Valley for injectable medicines.
- [Eli Lilly (LLY) Starts Building $3.5 Billion Pennsylvania Obesity Drug Plant](https://www.google.com/goto?url=CAESygEBxCJF15OZYpZ0ZgA_qveCQ_itAHhVBjlJHeugdr-Fg7OhnJ2p9HhrH6KgU8T5snYZvYc6xUwA_FtuNSgAEVaesYF60rCDELE_meDd8078fDHrflLs3Ob4isy96wawyZ0ygtPLWQjtsYdLZDeESiipm3CVsl4iBEfSY9e01q03Eyrce260QK9e1FzdSASsWmN9SCG7VUgz83Zeqp-p3ohPGKiiEyoUJA-1msHlsLWlIIJDjFLie9gRXI1MgHCBw3KTYbdEK62I-UAT&gsessionid=jRrPlrFMV5IjB29DPt-1L6GhNIEDRXsh6trtHkDkEHzeOgcka_bkqA)  
  <sub>Simply Wall St, 12 hours ago</sub>  
  Eli Lilly (NYSE:LLY) has started building a US$3.5b advanced manufacturing facility in Pennsylvania for next generation injectable obesity medicines.
- [How Are Mounjaro and Zepbound Driving Another Big Outlook Raise at LLY (NYSE:LLY)?](https://www.google.com/goto?url=CAESuQEBxCJF14AoyMEQRTUulV1xK65DXRJtJNqEHn2Qu7_0BBgAN1JRUzdsWZ6pwfv-RXUzq4kuzV_v3iQ8xpkit_dvrWleEN2u3LWUAweZI_kwoR-vteeHIh3jooZt9m-rOYOkTHYv9EAkV0BXw0p0p6pbLnYtZOpxov165LSSsZweQZxUD2-TDHWBPUctkbE8HmGvOXqQZKY43SmAHeMbs-SSFhj7uVKFa-mvSJCfOnbaUtGVrpzTHqhQvQ&gsessionid=jRrPlrFMV5IjB29DPt-1L6GhNIEDRXsh6trtHkDkEHzeOgcka_bkqA)  
  <sub>Kalkine Media, 1 hour ago</sub>  
  Eli Lilly (NYSE:LLY) grows revenue sharply on Mounjaro and Zepbound demand, raises full-year guidance and advances its obesity pipeline with new launches.
- [More Good News for Eli Lilly Sends the Stock Even Higher](https://www.google.com/goto?url=CAESlgEBxCJF19Zg5_DGUfPDWGlyQ7LafGniau4L_fAtyIdYhnPBM5T7fZ_dBFE3hJ5WiViZuh9xYlT3IlJwgDk1Sj-KycMnDkqAvh4EIzv9l6bhfgZTYrKtdR8HEYm9iH5A0Z62tVhmd0zhJUK3XXGBHrKC7d-HH7T_weUxwcjucucAwxiqri95jrISna7K5CylsnwDrGkrzQM&gsessionid=jRrPlrFMV5IjB29DPt-1L6GhNIEDRXsh6trtHkDkEHzeOgcka_bkqA)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  The good news keeps rolling in for Eli Lilly (NYSE:LLY), sending its shares higher at the start of the trading week. Last week, Lilly announced that phase 3...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.40</summary>

```text
Last close 1,421.24 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 1,355.13 (+4.9%), 50d 1,240.63 (+14.6%), 200d 1,109.21 (+28.1%); 50d above 200d
Momentum: RSI(14) 66.5 | MACD 55.387 vs signal 53.356 (histogram 2.030)
Returns: 1d -0.4% | 5d +5.0% | 1m +13.6% | 3m +20.1%
52-week range: 851.21 - 1,437.29 (now 97.3% of the way up)
Volatility: ATR(14) 43.22 (3.0% of price) | annualised 20d 38.6%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.27T
Valuation: trailing P/E 46.13 | forward P/E 28.07 | P/B 31.45 | PEG 1.33
Profitability: profit margin 31.9% | operating margin 51.3% | ROE 86.0%
Growth (YoY): revenue +38.6% | earnings +16.3%
Balance sheet: debt/equity 122.9% | free cash flow 9.34B
Risk: beta 0.39 | short interest 0.8% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-09-30 beat by 18% | 2026-06-30 beat by 38% | 2026-03-31 beat by 27% | 2025-12-31 beat by 12%
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

<details><summary><b>What analysts and big funds say</b> — score +0.10</summary>

```text
Consensus: buy (mean 1.65 on a 1=strong buy to 5=strong sell scale, 29 analysts)
Ratings: 5 strong buy, 20 buy, 4 hold, 1 sell, 1 strong sell
Price target: mean 1,460.30 (+2.7% vs last close), range 940.00 - 1,690.00
Recent rating changes:
  - 2026-11-09 Jefferies: main, Buy -> Buy
  - 2026-11-02 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-10-31 UBS: main, Buy -> Buy
  - 2026-10-30 JP Morgan: main, Overweight -> Overweight
  - 2026-10-30 Citigroup: main, Buy -> Buy
  - 2026-10-30 Scotiabank: main, Sector Outperform -> Sector Outperform
Institutional ownership: 85.6%
Largest holders: Lilly Endowment, Inc (9.6%), Blackrock Inc. (7.2%), Vanguard Capital Management LLC (5.7%), PNC Financial Services Group, Inc. (5.5%), State Street Corporation (3.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 38,018 shares in 36 transaction(s) | sold 313,215 shares in 9
Net: -275,197 shares (-16.1% of insider holdings) | insiders hold 1,434,099 shares
Distinct insiders: 0 buying, 4 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-11-02 HAKIM ANAT (General Counsel): 5,000 shares, 7.01M
  - 2026-08-17 JONSSON PATRIK (Officer): 6,500 shares, 7.64M
  - 2026-08-10 ZAKROWSKI DONALD A (Officer): 2,000 shares, 2.37M
  - 2026-08-07 HAKIM ANAT (General Counsel): 5,000 shares, 5.95M
(36 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Caterpillar (CAT) · Company — BULLISH, confidence 0.70

**Result:** REJECTED · no room for equity CAT under its 5% cap or the sleeve budget limit: equity 100588.06, price 593.87, existing exposure 0.00, headroom 218.11

**In the model's own words:**

> The news includes a strong positive catalyst – record backlog and highest sales quarter driven by data center demand – and a promising gas compression system trial, outweighing the negative investigation news. Fundamentals are solid with high profitability, strong growth, and reasonable valuation despite high leverage. Earnings have consistently beaten expectations. Analysts are bullish with a 36% upside target. Insider activity shows net buying (+2% of holdings). Technicals are bearish (price well below moving averages and low volume), tempering conviction but not overturning the overall bullish view.

**Main reasons it gave:**
- Record backlog and highest sales quarter driven by data center demand (Kalkine Media)
- Gas compression system trial reduces methane emissions by up to 73% (Simply Wall St)
- Net insider buying of 19,507 shares (+2% of holdings) over the last 180 days
- Strong profitability: ROE 56.1%, profit margin 15.2%, earnings growth +46.1% YoY
- Technical weakness: price below 20‑day, 50‑day, 200‑day SMAs and volume 0.03× 20‑day average

<details><summary><b>News</b> — score +0.40</summary>

- [How Much Downside Is Left In Caterpillar Stock?](https://www.trefis.com/stock/cat/articles/624527/how-much-downside-is-left-in-caterpillar-stock/2026-11-12)  
  <sub>Trefis, 17 hours ago</sub>  
  For questions about this article or underlying research, email help@trefis.com. Caterpillar (CAT) stock lost 22% in the month to November 11, while the S&P...
- [Red Cat Holdings, Inc. (RCAT) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/RCAT/latest-news/)  
  <sub>Yahoo Finance UK, 16 hours ago</sub>  
  Red Cat Holdings, Inc. (RCAT) · 3 Drone Defense Stocks With Up To 40% Revenue Growth · 20 Hedge Funds Back This Defeated Robotics Stock: Time to Buy the Dip?
- [Caterpillar Has Fallen 44% From Its June High, but $1,000 Invested Ten Years Ago Is Still Worth $7,785](https://www.google.com/goto?url=CAESygEBxCJF19yQBIWgRLhic5HIi_6ous5UgVUItfIBP6dgDI7wvQ-gbEJmI2VCl3xCQ7oAuMe1RVxW0yqjZeOYiYf_sC52GYrccdxHwRVRQHXIw-L9HUziEvsEfppsPKhAXMir4H_OCHMqbIE9-aYxQK6UyabSQAaGjXIKL8MNryOLTFVHsb3M03z5SX7uIbQazZJM_WeTGwMyHcZLHuKygiOB6g-KeHK96fJRCP0tPS5N9mYVGBTyGnrDgOxHOJZcAm8zVy1FIgJ_-Np9&gsessionid=n_PqHWy48bb_mRYtoio88EAaddeQSS8APHERwX_M_c4Exi1I81MfmQ)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Caterpillar (NYSE:CAT | CAT Price Prediction) has slipped far from its summer high, but long-term shareholders still have collected plenty along the way,...
- [CAT Nov 2026 1150.000 call (CAT261113C01150000) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXIOBpyPrQBznzFCDBIB62Lk7cDkqCUxey1MwdLQcPrfuWxJNWOTkD2qtgIaJBeG_IOxjAcJXmcnyntSj3KD3uZx6Yz4-Uv4NQexgA5Yh_r9_4VvoY3XWCwu8LKEnahV1QlDNUJyrTlBpP4H31ABVtSKPn8jo&gsessionid=n_PqHWy48bb_mRYtoio88EAaddeQSS8APHERwX_M_c4Exi1I81MfmQ)  
  <sub>Yahoo Finance UK, 11 hours ago</sub>  
  Interactive chart for CAT Nov 2026 1150.000 call (CAT261113C01150000) – analyse all of the data with a huge range of indicators.
- [Gas Generator Deal Could Be A Game Changer For Caterpillar (CAT)](https://www.google.com/goto?url=CAESwgEBxCJF13lrfFHnuhl-Mtyzbwe15ofPOK9hZvVxP2Ob689asmYYLwcLUo1OQ0QfDFerlG3mNtj5uo3v03oilbEVc01tkoeqfn1aHes90cmml_21Dtk9YHw-ZLYHGA6h1NC-2EQjPypv64OJxHCajOAbsqpt0E4A9VcPVjqdJRzC4fGR8Oc3bflnM02Bforzg0uHVdTTB37vGre8LchWGwurScHLNkdqZvPd0aeBkNJv-QPry32px54iswczFlv4AHsJOA&gsessionid=n_PqHWy48bb_mRYtoio88EAaddeQSS8APHERwX_M_c4Exi1I81MfmQ)  
  <sub>Simply Wall St, 18 hours ago</sub>  
  Caterpillar and Phoenix Service Partners reported field trial results for a large gas compression system that reduced methane emissions by up to 73% and...
- [How Is Data Center Power Demand Driving a Record Backlog at CAT (NYSE:CAT)?](https://www.google.com/goto?url=CAESsgEBxCJF16nRPIjicAfG1eAvfglpAZHBj4TKhSMusA-_p8QdwsZoEQFWLWEtpHrXaUM0NsHzmmfRwQ0xtx5Cz6su8PSq79rV_4vuQiGYEZaup8sgZgMeLeTdiB1OePZv-2G6rwNO4X3xaCw8zUYy8Yr5-c7qSHdcV2EV_kl6cVylOjh6mXPwltZiEV0Ff5cydvUqFJhsDTqq2iPGmjXAeHOPhChwEWFIHy5vv7mwY4101X8h&gsessionid=n_PqHWy48bb_mRYtoio88EAaddeQSS8APHERwX_M_c4Exi1I81MfmQ)  
  <sub>Kalkine Media, 2 hours ago</sub>  
  Caterpillar (NYSE:CAT) posts its highest sales quarter ever as data center power demand surges, nearly doubling its backlog to a record level.
- [Investigation launched into Caterpillar for pos...](https://www.google.com/goto?url=CAESqwEBxCJF1xNowfZkB7BvDZZJXyX-lOFN8hLqEx_QWGLH5YzihkVuDm6VTKdCQ7ttQ3T6Os5t-byaIO26NurrPnZasjxxl543xn9a1ytmbj0GqtRRy-erseWu2kGRYAt0F_QsEdNET0cD0J_5D9d_gKGaau_9NrXQ7CSQF6Cjh6kw7Jq_JDhXKuZ6qC7IPsaDxnDT3jzcM9I9XNpYWwWDzAGgJbAZZ3hrH7Lm7hM&gsessionid=n_PqHWy48bb_mRYtoio88EAaddeQSS8APHERwX_M_c4Exi1I81MfmQ)  
  <sub>Pluang, 12 hours ago</sub>  
  Pomerantz LLP is investigating Caterpillar Inc. for potential securities fraud following the company's Q3 2026 financial report. Caterpillar disclosed a 22%...
- [Ondas Retreats 5% Despite Record Revenue and Raised Outlook; Red Cat Drops 4%, AeroVironment Holds Steady](https://www.google.com/goto?url=CAESzwEBxCJF13bQ_q8id4vkTFXf9PjYochP9cONQy904LxrUvEMjtSMmwpdP_se-CRkFzV5BngZa-JKYk9ymQjs2C3khfz1NNkIzBDPebiBoHPKME9VbSXZXw53d9iMVjnX9Dwf1t83S6uIzDoByt5XjAKhP13gRNOG-ib87MLNU3YP5QiTiqb29ItAcKk_mc-gzrWGE-NHQqnsCPlp30J2w63ep9dHjOSTV9muSmjumbjwj5khfVq4q1_NVy1KQ0EiQHEBJq7jdszwhu6hOcD2Ph8&gsessionid=n_PqHWy48bb_mRYtoio88EAaddeQSS8APHERwX_M_c4Exi1I81MfmQ)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  Ondas (ONDS) fell 3% despite $167 million in record revenue, as a wider loss and 22% gross margin overshadowed the beat, while Red Cat (RCAT) slid 4%.
- [3 Legacy Industrial Dividend Stocks That Never Go Out of Style](https://www.google.com/goto?url=CAESpwEBxCJF189DUpW8Qh-ZoC1Ui6w-2CqS2jAFYjsa86t1KVFj13_xrW5X9qfxTPTDpDX0zLvKB-p8IinwzuL_vtpPe2J9DAsUQDLXuUv0SLQNfMxJDIcJs8HzlJZPBKy_83AybbfKxgYDeDLhWi7Z1V3Og2VJn1nCfBgXjN2e2vQhwwNOrsG0jFeIK6NrstJFl6uVQMZFayc7TVSOLlHEY4PU8aUmzPYTfA&gsessionid=n_PqHWy48bb_mRYtoio88EAaddeQSS8APHERwX_M_c4Exi1I81MfmQ)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  Emerson, Union Pacific and Caterpillar raised dividends through the 2009 and 2020 downturns, giving retirees growing income from industrial leaders founded...
- [TGT Stock Quote Price and Forecast](https://www.google.com/goto?url=CAESYwHEIkXXAiWx2_AyZ0xNMfEmUabRdJdvQTnmfsyc_BkwQCyeRkzCybfNlsX86GhluSP7ZZzjl9x2QogYWWnSrYQ720pyXxXbR3TOzhCxlYph3RraLH9jNtzv6N4nugpNFuxmxA&gsessionid=n_PqHWy48bb_mRYtoio88EAaddeQSS8APHERwX_M_c4Exi1I81MfmQ)  
  <sub>CNN, 3 hours ago</sub>  
  View Target Corporation TGT stock quote prices, financial information, real-time forecasts, and company news from CNN.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 605.61 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 645.42 (-6.2%), 50d 740.88 (-18.3%), 200d 807.46 (-25.0%); 50d below 200d
Momentum: RSI(14) 36.4 | MACD -46.999 vs signal -48.739 (histogram 1.740)
Returns: 1d +0.1% | 5d +8.4% | 1m -17.7% | 3m -31.3%
52-week range: 546.13 - 1,064.90 (now 11.5% of the way up)
Volatility: ATR(14) 28.02 (4.6% of price) | annualised 20d 59.8%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 277.12B
Valuation: trailing P/E 23.77 | forward P/E 18.78 | P/B 12.90 | PEG 1.05
Profitability: profit margin 15.2% | operating margin 18.8% | ROE 56.1%
Growth (YoY): revenue +17.3% | earnings +46.1%
Balance sheet: debt/equity 210.4% | free cash flow 3.97B
Risk: beta 1.64 | short interest 2.0% of float
Next earnings: 2027-01-28
```

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.50</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 in line
  2026-09-30 in line | 2026-06-30 beat by 31% | 2026-03-31 beat by 19% | 2025-12-31 beat by 9%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: buy (mean 1.97 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 2 strong buy, 15 buy, 11 hold, 1 sell, 0 strong sell
Price target: mean 823.41 (+36.0% vs last close), range 575.00 - 1,044.68
Recent rating changes:
  - 2026-11-10 Evercore ISI Group: main, Outperform -> Outperform
  - 2026-11-02 Freedom Broker: main, Buy -> Buy
  - 2026-11-02 DA Davidson: main, Neutral -> Neutral
  - 2026-10-30 JP Morgan: main, Overweight -> Overweight
  - 2026-10-30 Citigroup: main, Buy -> Buy
  - 2026-10-30 Wells Fargo: main, Overweight -> Overweight
Institutional ownership: 73.8%
Largest holders: Blackrock Inc. (8.3%), State Street Corporation (7.5%), Vanguard Capital Management LLC (6.6%), State Farm Mutual Automobile Insurance Co (3.1%), Vanguard Portfolio Management LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

```text
Last 180 days: bought 71,069 shares in 12 transaction(s) | sold 51,562 shares in 4
Net: +19,507 shares (+2.0% of insider holdings) | insiders hold 1,011,283 shares
Distinct insiders: 1 buying, 1 selling
Open-market purchases — insiders spending their own money:
  - 2026-11-02 FISH JAMES C JR (Director): 1,000 shares, 620.39K
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-08-28 CREED JOSEPH E (Chief Executive Officer): 32,401 shares, 26.21M
(9 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

_Not available today._

</details>

### JPMorgan Chase (JPM) · Company — BULLISH, confidence 0.65

**Result:** ACCEPTED · 4 shares · submitted buy 4 JPM @ ~344.77, stop 330.54

**In the model's own words:**

> ETF purchases of $117.8M in JPM, price above 20‑, 50‑ and 200‑day SMAs, solid fundamentals (trailing P/E 14.5, ROE 18%), earnings record of 3 beats/1 miss, insider net buying of 98,776 shares (+1% of holdings).

**Main reasons it gave:**
- ETF purchases of $117.8M in JPM
- Price above 20‑, 50‑, and 200‑day SMAs
- Solid fundamentals: trailing P/E 14.5, ROE 18%
- Earnings record: 3 beats, 1 miss
- Insider net buying of 98,776 shares (+1% of holdings)

<details><summary><b>News</b> — score +0.70</summary>

- [ETFs Bought $117.8 Million of JPMorgan (JPM) on Wednesday](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af721a7015046d0917b46919faf5ca1&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2fetfs-bought-117-8-million-110135948.html&c=12707475023693630709&mkt=en-us)  
  <sub>Yahoo Finance, 12h ago</sub>  
  JPMorgan Chase, a financial holding company incorporated in 1968 and headquartered in New York, is a leading global financial services firm with $4.4 trillion in ...
- [JPMorgan Chase & Co. (JPM) up 2.4% since last earnings report: Can it continue?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af721a7015046d0917b46919faf5ca1&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2fother%2fjpmorgan-chase-co-jpm-up-2-4-since-last-earnings-report-can-it-continue%2far-AA2hjiQ4&c=1268714928883719701&mkt=en-us)  
  <sub>Zacks Investment Research on MSN, 31h ago</sub>  
  It has been about a month since the last earnings report for JPMorgan Chase & Co. (JPM). Shares have added about 2.4% in that time frame, outperforming the S&P 500. Will the recent positive trend ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.10</summary>

```text
Last close 345.34 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 339.00 (+1.9%), 50d 340.41 (+1.4%), 200d 324.86 (+6.3%); 50d above 200d
Momentum: RSI(14) 55.4 | MACD 1.302 vs signal 0.437 (histogram 0.865)
Returns: 1d +0.7% | 5d +3.2% | 1m +2.9% | 3m -4.3%
52-week range: 282.84 - 365.18 (now 75.9% of the way up)
Volatility: ATR(14) 7.11 (2.1% of price) | annualised 20d 27.3%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 917.09B
Valuation: trailing P/E 14.49 | forward P/E 13.50 | P/B 2.61 | PEG 1.46
Profitability: profit margin 34.6% | operating margin 44.8% | ROE 18.0%
Growth (YoY): revenue +10.2% | earnings +9.9%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 1.02 | short interest 0.9% of float
Next earnings: 2027-01-14
```

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.50</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-09-30 missed by 7% | 2026-06-30 beat by 4% | 2026-03-31 beat by 8% | 2025-12-31 beat by 3%
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
Consensus: buy (mean 2.04 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 5 strong buy, 10 buy, 11 hold, 0 sell, 0 strong sell
Price target: mean 373.48 (+8.1% vs last close), range 312.00 - 425.00
Recent rating changes:
  - 2026-11-02 UBS: main, Buy -> Buy
  - 2026-10-15 Citigroup: main, Neutral -> Neutral
  - 2026-10-14 Truist Securities: main, Hold -> Hold
  - 2026-10-14 Barclays: main, Overweight -> Overweight
  - 2026-10-14 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-14 Morgan Stanley: main, Equal-Weight -> Equal-Weight
Institutional ownership: 75.4%
Largest holders: Blackrock Inc. (7.8%), Vanguard Capital Management LLC (6.1%), State Street Corporation (4.7%), Bank of America Corporation (2.6%), Morgan Stanley (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

```text
Last 180 days: bought 136,610 shares in 7 transaction(s) | sold 37,834 shares in 8
Net: +98,776 shares (+1.0% of insider holdings) | insiders hold 10,489,659 shares
Distinct insiders: 0 buying, 2 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-10 LEOPOLD ROBIN (Officer): 2,500 shares, 882.03K
  - 2026-08-11 LEOPOLD ROBIN (Officer): 2,500 shares, 903.52K
  - 2026-06-22 FRIEDMAN STACEY R. (General Counsel): 5,467 shares, 1.81M
  - 2026-05-20 FRIEDMAN STACEY R. (General Counsel): 5,468 shares, 1.64M
(6 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

_Not available today._

</details>

### ASML (ASML) · Company — BULLISH, confidence 0.60

**Result:** REJECTED · no room for equity ASML under its 5% cap or the sleeve budget limit: equity 100590.16, price 1472.56, existing exposure 0.00, headroom 1393.49

**In the model's own words:**

> Fundamentals are strong and earnings beat is a material catalyst, reinforced by a very bullish analyst consensus. Technicals are weak (price below key moving averages, low volume) and recent news shows some selling pressure, tempering the view. Overall the bullish factors outweigh the bearish technicals, leading to a moderate‑conviction BUY signal.

**Main reasons it gave:**
- Record Q3 earnings beat by 17% (Intellectia AI)
- Strong analyst consensus: 7 strong buys, price target +40.8% (Analyst view)
- Technical weakness: price below 200‑day SMA and low volume (Technical data)
- ETF net sellers $17.9 M on Nov 11 (News)

<details><summary><b>News</b> — score +0.40</summary>

- [ASML Stock Quote Price and Forecast](https://www.cnn.com/markets/stocks/ASML)  
  <sub>CNN, 5 hours ago</sub>  
  ASML Holding NV Sponsored ADR ... ASML is trading in the middle of its 52-week range and below its 200-day simple moving average. Price change. The price of ASML...
- [XNDU Stock Fell From $42 to $2.80. GlobalFoundries and ASML May Explain the Bounce Case](https://finance.yahoo.com/markets/stocks/articles/xndu-stock-fell-42-2-133920573.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  We just published a list of the 10 Quantum Computing Stocks Investors Accidentally Dumped and Xanadu Quantum Technologies ranked 1st on the list.
- [ASML Stocks Fall as NVIDIA Shake-Up Spills Into Chip Equipment](https://www.google.com/goto?url=CAEStwEBxCJF10Iri9MvJbtf5Z1CuIw4cEjw5Y9e_B-lg-4TwjQCHL6yUTRnvRiK8VABFr2wdhnDt24QNDM2TSm3MQ_jsW_m7nkIKQRHtBmmkVG0gqnxlUzFh_O5Gn8J3wAziZlPEVeiVr-qCMm5UgLGtMMOlIMDTL8OzGnuxGnTEW3-7xOXpOeFJjIl4kySrCIheSAYZlGvg4DNQ-z6jftSv5Z6aedlaauMPqxf5gyapQj0yn_DYbUmgYA&gsessionid=lo7FOpRQmw1JFgg2kw2BWvMI83uITfETOuHXFfky-gQ7SK64mgTq1g)  
  <sub>TradingView, 3 hours ago</sub>  
  ASML Holding NV NASDAQ:ASML shares fell 1.56% to $1510.46 at 9:35 a.m. ET in early regular-session trading on November 12 as NVIDIA's CEO resignation pulled...
- [ETFs Are Net Sellers of ASML (ASML) on Nov. 11](https://www.google.com/goto?url=CAESmAEBxCJF1z1z_09VsSQIdLpST-of20n2Y4PPWG9EDanTCl3bqabf-3j3EiepTiFgYMuNOnU67--K9R-McrEWHVyqFMvxh_W5ZVjTH2W2HgNBlzOrFlZUyx4a0D3-UKKEMLPpalgMKX1SiqiYIinsZP_ex4BRyCM-lh5fimhmSWqIsIIpXDw_14TFKiGJgO3NpqoCofQy1_I-_g&gsessionid=lo7FOpRQmw1JFgg2kw2BWvMI83uITfETOuHXFfky-gQ7SK64mgTq1g)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  ASML drew $17.9 million in net ETF selling on Nov. 11 despite 8 buyers versus 4 sellers.
- [ASML (NasdaqGS:ASML) Stock May Be Above Fair Value Following Its 124% Run](https://www.google.com/goto?url=CAESywEBxCJF14-oM7ZBi5yTV2EruyXyCqlREw0H6IA-KKIqOJYx6KQZiYVvkXyHGogMvcpveqbjMli7dduCeHt-wpziYfs0raGcjwwjnXu8IDTwVQ3F-FfDxvGr1JOVwDHDcavfcwTWuaoFzaIjJqBoEQOpqPj1llShMJuy7v2L0RhRCw7Wa-1JNes79lQgSzUKUjCp50iOkb0SoPNxG_e4pjoLgXeCyZ30ynZlrUEQtxNkGqIv-LF7kZKN_XzSnhJ8EgtBffIJwCt0yRltAQ&gsessionid=lo7FOpRQmw1JFgg2kw2BWvMI83uITfETOuHXFfky-gQ7SK64mgTq1g)  
  <sub>Simply Wall St, 6 hours ago</sub>  
  ASML Holding has had a powerful share price run over the past few years. With the stock recently closing at US$1497.12, the live question for investors is...
- [ASML Dec 2026 1360.000 put (ASML261204P01360000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESdAHEIkXX2w46i-ncTMMKY7VbRtvMDr8RBl3t-92FrbMUg90lvZ6zYlb0b9R8fHNGRDSCGDS4Shyo15pmxgK5fw1hzzpEeTlaNivYgQyEa2ixeMFxR79IthFOb74TMIm360wh8mLQ9gAAQnXi_fZL2Hfey-2R&gsessionid=lo7FOpRQmw1JFgg2kw2BWvMI83uITfETOuHXFfky-gQ7SK64mgTq1g)  
  <sub>Yahoo! Finance Canada, 8 hours ago</sub>  
  Find the latest ASML Dec 2026 1360.000 put (ASML261204P01360000) stock quote, history, news and other vital information to help you with your stock trading...
- [ASML Capitalizes on AI Boom with Record Earnings](https://www.google.com/goto?url=CAESjwEBxCJF15X41p2iuRaS6aN_63lSwsj2fOLk4LY9mh-aIUdjv8t-BcogHglniW__bOMlpbvqul0pkMIJB2xvHcPWnZ3e90EH0CeHPDLRXEKk7eRSop434ywQmLK1EbJxPDL2eugYFUgn-AWvSA8bl-_cKo_UQdIc7u06GQW57mcSZj8H3i_C1O1DpvFLty-mww&gsessionid=lo7FOpRQmw1JFgg2kw2BWvMI83uITfETOuHXFfky-gQ7SK64mgTq1g)  
  <sub>Intellectia AI, 23 hours ago</sub>  
  Significant Earnings Growth**: ASML reported record quarterly sales in its Q3 earnings announcement, driven by sustained strength in AI investment...
- [ASML Nov 2026 1465.000 call (ASML261113C01465000) Interactive Stock Chart](https://www.google.com/goto?url=CAESdwHEIkXX5aMoFX1mI3DDS3bgPf0oiaZ5E22FtDj92D_lWv_uYxISgpYBi6Ob9BWibBqVrXxtiZFqLsm3vk_7FSoSEXIoD5BBlCtcwIpldW3mTZzUJwshy80aYfRovaBHqQ8ktRjSVYyFLZopOiDoxztForiTf3JC&gsessionid=lo7FOpRQmw1JFgg2kw2BWvMI83uITfETOuHXFfky-gQ7SK64mgTq1g)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Interactive Chart for ASML Nov 2026 1465.000 call (ASML261113C01465000), analyze all the data with a huge range of indicators.
- [Taiwan Semiconductor Just Became Even More of an AI Anchor On Nvidia’s -25% Plummet](https://www.google.com/goto?url=CAESuQEBxCJF1yAZXitBh9Z7rYGBrVsLfhcQQ5nVgOry7WFyO0eJGJorn5uwYC2eBt_WkxN_UT7atlT_v6n0sRMArGa73uYWpjKiVNrRkdhDjsSnoVVIGw8n-_Mq4DNZWz0ss0iZMf9mUK9h2sgtd1t5pwIVMhz2pXmdIngy8O1tQ2epjh3lO3K16ng02MDMCu-5H5wDgVN8e_y-0ocZWaYNyM-dEUe8obok8ySQN2Khezu9gxLE-T9IPYmncg&gsessionid=lo7FOpRQmw1JFgg2kw2BWvMI83uITfETOuHXFfky-gQ7SK64mgTq1g)  
  <sub>24/7 Wall St., 56 minutes ago</sub>  
  I added to my Taiwan Semiconductor (NYSE:TSM | TSM Price Prediction) position again this week, and every new data point reinforces my conviction to keep...
- [Help wanted: AI firms court ex-spies as Nvidia crisis spotlights security risks](https://www.google.com/goto?url=CAESvAEBxCJF16rMlcIsGsLeUC1xzNvIDz5uiRMBZ_jafPHAg5UQf6YIe68VTA0t8a4sWd_xgxLD2UpiIebfdOC-EvCpGBm8RuVqz1luTMCSp07GfY9YRu7ZCncjKfApghqDKXxKwYZR_3BYuxujGlzUsi5y2IMTrOe7fbLBriU1s3-L8sEHCHPzK-pc8iSd10wJhUtjW3-PjNmeFjUyicK3_4oLFKg94eqpdI62TmoJe6kM_giy3aoHIQ-L2w3vKg&gsessionid=lo7FOpRQmw1JFgg2kw2BWvMI83uITfETOuHXFfky-gQ7SK64mgTq1g)  
  <sub>Reuters, 18 hours ago</sub>  
  AI firms are hiring former intelligence operatives to help shield them from espionage, a ​risk thrust into the spotlight as Nvidia axed its CEO Jensen Huang...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 1,505.26 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 1,556.59 (-3.3%), 50d 1,660.70 (-9.4%), 200d 1,602.26 (-6.1%); 50d above 200d
Momentum: RSI(14) 43.1 | MACD -54.684 vs signal -55.483 (histogram 0.799)
Returns: 1d +0.5% | 5d +5.7% | 1m -9.2% | 3m -20.1%
52-week range: 966.57 - 1,989.44 (now 52.7% of the way up)
Volatility: ATR(14) 63.68 (4.2% of price) | annualised 20d 62.4%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 580.15B
Valuation: trailing P/E 37.04 | forward P/E 23.74 | P/B 1,292.49 | PEG 0.80
Profitability: profit margin 34.1% | operating margin 38.6% | ROE 65.6%
Growth (YoY): revenue +55.2% | earnings +135.9%
Balance sheet: debt/equity 8.9% | free cash flow 10.37B
Risk: beta 1.33 | short interest 0.3% of float
Next earnings: 2027-01-27
```

</details>

<details><summary><b>What this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.60</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-09-30 beat by 17% | 2026-06-30 beat by 9% | 2026-03-31 beat by 7% | 2025-12-31 missed by 5%
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

```text
Consensus: strong_buy (mean 1.37 on a 1=strong buy to 5=strong sell scale, 17 analysts)
Ratings: 7 strong buy, 31 buy, 2 hold, 1 sell, 0 strong sell
Price target: mean 2,119.54 (+40.8% vs last close), range 854.95 - 2,808.45
Recent rating changes:
  - 2026-10-15 JP Morgan: main, Overweight -> Overweight
  - 2026-07-16 JP Morgan: main, Overweight -> Overweight
  - 2026-07-16 Wells Fargo: main, Overweight -> Overweight
  - 2026-07-16 RBC Capital: main, Outperform -> Outperform
  - 2026-07-14 RBC Capital: main, Outperform -> Outperform
  - 2026-07-06 Bernstein: main, Outperform -> Outperform
Institutional ownership: 20.0%
Largest holders: FMR, LLC (1.5%), Fisher Asset Management, LLC (1.2%), Capital World Investors (0.9%), Invesco Ltd. (0.7%), State Farm Mutual Automobile Insurance Co (0.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

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

### Alphabet (Google) (GOOGL) · Company — BULLISH, confidence 0.55

**Result:** ACCEPTED · 4 shares · submitted buy 4 GOOGL @ ~294.74, stop 274.24

**In the model's own words:** no explanation. It wrote only “news_score”, so the main reasons below are all it gave.

**Main reasons it gave:**
- AI chips for customer data centers announced (Motley Fool, 13h ago)
- AI smart glasses launch and $4B Asian bond issuance (Benzinga, 20h ago)
- ETF net buying of $130.4M (Yahoo Finance, 4h ago)
- Technical downtrend: price below 50d/200d SMAs, low volume (daily bars)
- Earnings record: 3 misses, 1 beat in last 4 quarters (Earnings record)

<details><summary><b>News</b> — score +0.50</summary>

- [Alphabet Inc. (GOOGL) is Attracting Investor Attention: Here is What You Should Know](https://finance.yahoo.com/markets/stocks/articles/alphabet-inc-googl-attracting-investor-130006251.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Alphabet (GOOGL) has recently been on Zacks.com's list of the most searched stocks. Therefore, you might want to consider some of the key factors that could...
- [Should You Buy Alphabet Stock Now That Google Will Let Customers Run Its AI Chips in Their Own Data Centers?](https://www.fool.com/investing/2026/11/12/should-you-buy-alphabet-stock-now-that-google-will-let-customers-run-its-ai-chips-in-their-own-data-centers/)  
  <sub>The Motley Fool, 13 hours ago</sub>  
  The search giant's turning its AI chips into hardware it sells. Is the stock a buy around 28% below its peak?
- [Alphabet (GOOGL) Stock Quotes, Company News And Chart Analysis](https://www.google.com/goto?url=CAESrAEBxCJF12l_-kJKVuA1WTKIu8ZKZGNiIu_M-_vY4_JuYt8Bi7wuxy1bFHb86RSA0kkvxSYlrNjDRg6PHXip-dMEflO9vUIcLlV74tgp07GE-oXRiBBG1MMJ5DcAY0KI7XKKA3jdwRMpoyYlqaAsHnxYJ10s9pvFhsP6IlWCljvmaI7ldKaxd2Y8J3nAuhRFHI94bXNYW__pV1ianjDoOLczxm3eRyVxeG5w6gI8&gsessionid=HsOuoflDa6A3FvFtomodCdSKXNPPAMpXRG9bj-tTwZ-AcRLujnwnyw)  
  <sub>Investor's Business Daily, 21 hours ago</sub>  
  Alphabet (GOOGL) Stock Quotes, Company News And Chart Analysis · Google Stock: Alphabet News & Analysis · Related news · Apple Stock Called 'Safe Haven,' Hits...
- [What's Going On With Alphabet Stock Thursday?](https://www.google.com/goto?url=CAESnwEBxCJF10jAWheqttDH6c96_4kAJusW4UmTIKeYQIZyZyZsy33b3QLQiAgqpDd28dN2GAeaoz66ylkhVXlaYOPLR89eKmGoshgq_8fbaQySFKf6g2xFcx4zg0cql141wfyb7Z7z1VLfT8JCZbOFYgWhmNKAVQVbmDoiBngHp-JEztzSVwKeAYZnP-Hu5lrKUy1R9gO8CQ-Er70plo85EQk&gsessionid=HsOuoflDa6A3FvFtomodCdSKXNPPAMpXRG9bj-tTwZ-AcRLujnwnyw)  
  <sub>Benzinga, 20 hours ago</sub>  
  Alphabet stock rises 3% as Google raises nearly $4B in Asian bonds and launches AI smart glasses to rival Meta.
- [Interesting News for Alphabet Stock Investors](https://www.google.com/goto?url=CAESwwEBxCJF1xZvSSfdmVj6LmrdVlO47fH3NdTLHJClIAYdm-FkyD6HTqTqzsjNKEbBGnC6XKz04tkkqAknnDSJncsqXynJOzS_YlmmwapOKicHEiOHhzATS_dFsSBjWCo9Z5MWthbE1P-knwmMbkMkmskvy-7OHM5BKYClu_ud9dzfaYxuR0uJh3Y2y4Ox1vIokdQeP00SD3_thQc2btAu9kMCdyPifYMWluKtwfQMoL808ezH_l0X-ZYR14VSfVj3VlgtGhg&gsessionid=HsOuoflDa6A3FvFtomodCdSKXNPPAMpXRG9bj-tTwZ-AcRLujnwnyw)  
  <sub>The Globe and Mail, 1 hour ago</sub>  
  Detailed price information for Alphabet Cl A (GOOGL-Q) from The Globe and Mail including charting and trades.
- [Google Stock (GOOGL) Rises 1.8% as Nvidia CEO Resigns (Nov 12)](https://www.google.com/goto?url=CAESiQEBxCJF13Yv_Yn5wb81sZPZytlShDr700JnPJYgZ5MbaLEsIOwbtxZRPoqCa1Zvx-m47TkkdNWtq_rJI2Tsww0QZhGFq4PYXt60qznySj0lRp-Yd_psAqr8TYngXDrlMZ75-_VxnFIx8rpHm9uXX2tCwZQWNDIFHKSuF_r_11qwd50qWHz1tr9FDQ&gsessionid=HsOuoflDa6A3FvFtomodCdSKXNPPAMpXRG9bj-tTwZ-AcRLujnwnyw)  
  <sub>Gotrade, 11 hours ago</sub>  
  Share this article. Google Stock (GOOGL) Rises 1.8% as Nvidia CEO Resigns (Nov 12). Summary. Alphabet (GOOGL) closed at $298.70 on November 12, 2026,...
- [ETFs Are Buying Alphabet (GOOGL) on Nov. 11](https://www.google.com/goto?url=CAESnAEBxCJF13AzahNezV_7JHxz4qD2_kRbPgFJyMg_JiBWF9wEB-2qwgLSz2z12jqaRmqJsDM0B3vMa7-8mTp2e7PCzhx0WSJqow3DYY-dCjaEuujGZPmaBAO7p4VVFy-P7DbHx4ZD835ra-pSF85a5vJyvdzMmTklKPdFTuA4PHHOouJtM8sNFCvyQr9RZNnq3RW2UTxBlsrNQPkTm38&gsessionid=HsOuoflDa6A3FvFtomodCdSKXNPPAMpXRG9bj-tTwZ-AcRLujnwnyw)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. ETFs bought a net $130.4 million of Alphabet (GOOGL) shares on Wednesday, with 51 funds adding the stock and 10...
- [How Low Can Alphabet Stock Go?](https://www.google.com/goto?url=CAESmAEBxCJF1xHJLAWEw9x6OQdZ5sN1h8xxoXYiL7PpTKceM1dEx_xj24AKClcBXzpxcHwdz1WVLhs9yBmdPgnshOqmjo8gX_mVGaX7s_mcRRNI5gGIRCSXy7iu_0-QiL6EOGSrP6oqbEA-oc3TboHlN__q-3DcbDp--X3JLENKlt9vv_Pd8y3VwKj9Yh9X5Y_aqtTeeY0Xggv8TQ&gsessionid=HsOuoflDa6A3FvFtomodCdSKXNPPAMpXRG9bj-tTwZ-AcRLujnwnyw)  
  <sub>Trefis, 23 hours ago</sub>  
  For questions about this article or underlying research, email help@trefis.com. A month like this one makes any Alphabet (GOOGL) holder wonder how much...
- [GOOGL Stock Recovers but Faces $300 as Google Commits $10 Billion to Anthropic](https://www.google.com/goto?url=CAEStAEBxCJF15evcgZx4THSDdyRLCnWWoHnWu7d7lad3PLnBfLolWwarDFOlu9r4y3dB614CX3wXes--C6ZzAvOr8dsyCdIj9SDG2FHuH3T-Qu_3m7hNa-0Ju37Sbq7n2tdV8suVsCUFZ5nbEQCS8ntR9QE8G1IKVOEQHaLlS8NzzDAVT_RAVuP8Y9AZCI4IpZSuHhOA6PrHuQMVVCwBdVw6V_iElwftFpMxoYWuUKkHl10Ci5nTcY&gsessionid=HsOuoflDa6A3FvFtomodCdSKXNPPAMpXRG9bj-tTwZ-AcRLujnwnyw)  
  <sub>FXLeaders, 21 hours ago</sub>  
  Alphabet shares are recovering toward $300 following October's earnings-driven sell-off, as Google's $10 billion Anthropic investment highlights its...
- [Nvidia succession uncertainty opens door for Google TPU and Broadcom, analyst says](https://www.google.com/goto?url=CAESyAEBxCJF1_a6PUYuOvG9WuTLwlcyivkmZY9DkmH9-JDAub2VauFabDKfVzSDyEAcILgtiZny2yEmNm4YSK6RO7wMT15acn4QBn-qdsCTD5Oy3wvkYP8RmJK7JdGVeUg-jlfYQcXcV_xido70MQeshp1rs4qWGKpNgS1hsbnQHNXcAUfNM_EElJLGiarqRomoDhfJadZdi-vdqclW889RkkJbugbA1c3_OJmwXzOVjVhkJV0IFujeMMRXmrXfmTSSQH5NTVsKS4-cZQ&gsessionid=HsOuoflDa6A3FvFtomodCdSKXNPPAMpXRG9bj-tTwZ-AcRLujnwnyw)  
  <sub>Investing.com, 21 hours ago</sub>  
  Investing.com -- Alphabet's tensor processing units, alongside key development partners Broadcom and MediaTek, stand to emerge as the primary beneficiaries...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 303.61 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 303.81 (-0.1%), 50d 328.34 (-7.5%), 200d 338.52 (-10.3%); 50d below 200d
Momentum: RSI(14) 46.1 | MACD -11.636 vs signal -13.444 (histogram 1.808)
Returns: 1d +1.6% | 5d +6.6% | 1m -13.1% | 3m -11.7%
52-week range: 273.50 - 402.62 (now 23.3% of the way up)
Volatility: ATR(14) 9.92 (3.3% of price) | annualised 20d 52.1%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 3.73T
Valuation: trailing P/E 15.85 | forward P/E 19.67 | P/B 5.66 | PEG 1.04
Profitability: profit margin 50.0% | operating margin 33.3% | ROE 44.3%
Growth (YoY): revenue +24.7% | earnings -25.3%
Balance sheet: debt/equity 22.2% | free cash flow -1.16B
Risk: beta 1.23 | short interest 1.5% of float
Next earnings: 2026-10-28
```

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

```text
Earnings record, last 4 quarters: 1 beat, 3 missed
  2026-09-30 missed by 14% | 2026-06-30 missed by 4% | 2026-03-31 missed by 3% | 2025-12-31 beat by 4%
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
Consensus: strong_buy (mean 1.34 on a 1=strong buy to 5=strong sell scale, 53 analysts)
Ratings: 10 strong buy, 43 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 400.37 (+31.9% vs last close), range 300.00 - 500.00
Recent rating changes:
  - 2026-11-02 Wells Fargo: main, Overweight -> Overweight
  - 2026-10-30 Citigroup: main, Buy -> Buy
  - 2026-10-30 Wells Fargo: main, Overweight -> Overweight
  - 2026-10-29 Bernstein: main, Market Perform -> Market Perform
  - 2026-10-29 RBC Capital: main, Outperform -> Outperform
  - 2026-10-29 UBS: main, Neutral -> Neutral
Institutional ownership: 80.6%
Largest holders: Blackrock Inc. (7.8%), Vanguard Capital Management LLC (6.5%), FMR, LLC (4.2%), State Street Corporation (4.1%), Geode Capital Management, LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 196,826,928 shares
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

### Royal Bank of Canada (RY) · Company — BULLISH, confidence 0.55

**Result:** ACCEPTED · 6 shares · submitted buy 6 RY @ ~202.19, stop 195.58

**In the model's own words:**

> The overall picture is modestly bullish: solid fundamentals and analyst buy consensus outweigh mixed institutional news and slightly bearish technical signals.

**Main reasons it gave:**
- Fisher Asset Management added 4.3% stake (institutional buy)
- Letko Brosseau trimmed holdings by 19.6% (institutional sell)
- Price above 50‑day and 200‑day SMA, up 6.2% vs 200‑day average
- Analyst consensus buy, price target +3.2% above last close
- Strong profitability: ROE 16.2%, profit margin 33.9%

<details><summary><b>News</b> — score -0.20</summary>

- [Royal Bank Of Canada $RY Stock: Letko Brosseau & Associates Inc. Trims Holdings](https://www.marketbeat.com/instant-alerts/filing-royal-bank-of-canada-ry-stock-letko-brosseau-associates-inc-trims-holdings-2026-11-13/)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Letko Brosseau & Associates Inc. lowered its stake in shares of Royal Bank Of Canada (NYSE:RY - Free Report) (TSE:RY) by 19.6% during the third quarter,...
- [Royal Bank of Canada eliminates senior ESG roles: RY consolidates as buyers maintain support](https://tradersunion.com/news/stocks/show/4232251-royal-bank-of-canada-slips/)  
  <sub>Traders Union, 40 minutes ago</sub>  
  Royal Bank of Canada trades at C$289.39 today, down 0.21%. Get the latest on RY stock moves, news, and technical levels.
- [The Midterms Are Over. History Says This Is What the Stock Market Does Next.](https://www.google.com/goto?url=CAES2wEBxCJF1wZPsrNN-_ZNKLoPyV1GTzxJzFDYhMshjx1hrCKp7UgBfrt-mdzn0rNBCYqzxNAuPygshC3pPAxiw97Myj3FMj-VoqjlONEfJeW3I9Df02lDI9KryveLLF2UUbOvwvt4SwRtkuFeIai6qARc59B0mvjXsS0ZIe9WB5gqsk3EAsXTmBGC6BmiAxx45mgAZoUPmnXS9avBD1xVTtkKVCTJc6Wrxb1duwAvMTRCmZIWF-BaXF0lvrTtoP2WvQeKiDkWRd8hPn_Hrwrg0yp42EVLX6cZ3MuPyg0&gsessionid=4ZQSGhhCPLpYTOSaQgwSwum6oJXU8B_DwAUHTY19cx9GvMbDRaaYUw)  
  <sub>The Globe and Mail, 2 hours ago</sub>  
  Detailed price information for Royal Bank of Canada (RY-N) from The Globe and Mail including charting and trades.
- [RY: SEC Form FWP filed by Royal Bank Of Canada](https://www.google.com/goto?url=CAESkgEBxCJF15_HlVmnLqz8JPrRLo0aCS1qzavYW-KAn98t5he8llcW-wNBSohHQvcaJuJen5fZDU7z9RuKdPjN5SROcN6ANS4Y7eKF7psNJvv5u140m2QsAgLU8cozbkJ2QN7eMWXTSzhQSu17iz04WO_-C0pX-qEca-6qx_tE0PIbo1p2DJOzyZFFF4-yN_Bew-wyXA&gsessionid=4ZQSGhhCPLpYTOSaQgwSwum6oJXU8B_DwAUHTY19cx9GvMbDRaaYUw)  
  <sub>Quantisnow, 18 hours ago</sub>  
  Royal Bank of Canada is offering Buffered PLUS notes linked to the S&P 500 Index, priced November 30, 2026, with a maturity date of March 3, 2028.
- [Canadian Bank Stocks: Buy, Sell, or Hold for 2027?](https://www.google.com/goto?url=CAESiwEBxCJF1xr1meqhxt-cfIcQqk0XnEZPhsBjsi8XC3_513iQ2kYP36AhyMU14or_aykFpEMB8rmvdGGTorg7CzxOyYoywQEuldNdZu4SsTYJ053x2Nuvy66owU3nPJ1bOcakO3C5xD3YSO_lu_oC9NVQSd_mY7Se3skeT2OImO7oDJu_2Hhvpvc-3flV&gsessionid=4ZQSGhhCPLpYTOSaQgwSwum6oJXU8B_DwAUHTY19cx9GvMbDRaaYUw)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Explore the Big Six, their latest earnings and dividend yields, with income and defensive picks. The post Canadian Bank Stocks: Buy, Sell, or Hold for 2027?
- [Trend Tracker for (RY) (RY:CA)](https://www.google.com/goto?url=CAESjAEBxCJF18yg3sC67TSv_TIWyO2m-yjXoCnWmzdC1nEu7iRv0WmGfE-JcLSLZKnsGCjto5IC7RlpNJHtoJFok4dAWTse0ezlNgpAnGDZW_QsU8pj8ILggGt4sMnqCHtga2yvL4qpRXtBw9BggYIIHg-aXqDm38XBuuFKwXoBc9v4qkL47Og0Sy5TaWIzrw&gsessionid=4ZQSGhhCPLpYTOSaQgwSwum6oJXU8B_DwAUHTY19cx9GvMbDRaaYUw)  
  <sub>Stock Traders Daily, 13 hours ago</sub>  
  Stimulus Matters to the Stock Market and to Royal Bank of Canada RY.
- [Royal Bank of Canada eliminates climate, ESG roles amid reorganization, sources say](https://www.google.com/goto?url=CAESxAEBxCJF1_NX-ZWNjcGA9DDQN2uJd47r188fMxad3g-74m4IhKLVY-i-rfbLbgSO67rozp0eOIwS6RIs4aJOiebKnJKnn6cSB_w2bu3CIHRwkC-NkrD4nW4sy7_kaE1xZLOCDYYQe3IBnADW_n0uMnaxKzFLLgtkPQ5M9k05YagTcRRe7aP_XE8vK4RXPj4z8_3MiUKyUZsaHz286uYUdIk8BSej--Bdl9bz3Q8C5m7x_saQiYqj4WMnoJicyDbauZXf4Xtn&gsessionid=4ZQSGhhCPLpYTOSaQgwSwum6oJXU8B_DwAUHTY19cx9GvMbDRaaYUw)  
  <sub>marketscreener.com, 14 hours ago</sub>  
  TORONTO, Nov 12 - Royal Bank of Canada has eliminated at least three senior climate, sustainability and environmental, social, and governance roles,...
- [305,484 Royal Bank Of Canada $RY Shares Purchased by Fisher Asset Management LLC](https://www.google.com/goto?url=CAESyQEBxCJF19e5TWwl_QIcUGsFcS8PtPu8ZJI6d7E0QOQ1mgWl05g-zoJrcto1L0a72ApYUzofMGrouyt0R5r0IzCMMi0yasGMrF7XFFS74ucWwKg3yeHpl6RQS48W0mZvcewfXtIUPL9ZOW05-8Vv2n1sIXAFXU6xJu29E8-TgwkpS2ZsgiO61A50D-j53MB0KWq8eEKeD_AKp5_alrvX_TNGyoiYPsCNgHZZs5ETTlq1haG9HDebDgVrZw3w4_iufwn7kwPN-YOVPNA&gsessionid=4ZQSGhhCPLpYTOSaQgwSwum6oJXU8B_DwAUHTY19cx9GvMbDRaaYUw)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Fisher Asset Management LLC boosted its position in shares of Royal Bank Of Canada (NYSE:RY - Free Report) (TSE:RY) by 4.3% during the 3rd quarter,...
- [Purpose RBC RY Yield Shares ETF CAD Income (RBCY.NE) Seasonal Returns Chart - Yahoo Finance](https://www.google.com/goto?url=CAESdAHEIkXXIXJt4cCPQfftQqlkSHkI-mzSU5pS0ws5dRke_f2abPhmGJNvjKA4PpwIc2ebszHd7lvL0vrKQJaovw6peRPI1Nq90S45SAfW3z4SrrgoVbzUlKw8-XmdpM6WE1hN778NlWE1BVRU-VdIrrM_73xy&gsessionid=4ZQSGhhCPLpYTOSaQgwSwum6oJXU8B_DwAUHTY19cx9GvMbDRaaYUw)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Purpose RBC RY Yield Shares ETF CAD Income (RBCY.NE). 14.13 -0.16 (-1.12%). As of November 10 at 3:50:45 p.m. EST. Market Open.
- [N.F.U. Mutual Unit Managers Ltd - Portfolio Stock Holdings](https://www.google.com/goto?url=CAESjQEBxCJF19_dUU7UcX7aGuhdBmWUKY6WfT_I-WrmL4IcTnbsTxwE9DW0bSVChXIUNuVFRRXZ6OpUsHyguPi4YcyAlYIduJyKUogNyPx6952n8F88o0wXXA-0JBahiSQ63rrzRN69_rHikFvmTCNSQnpQdj-PP0QGyIVrYIiMLxiuVw9yq8lbewpvjhZI6og&gsessionid=4ZQSGhhCPLpYTOSaQgwSwum6oJXU8B_DwAUHTY19cx9GvMbDRaaYUw)  
  <sub>Quiver Quantitative, 17 hours ago</sub>  
  Track which stocks N.F.U. Mutual Unit Managers Ltd is buying and selling. See stock portfolio updates, holdings by sector, and more.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 202.82 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 202.92 (-0.0%), 50d 201.10 (+0.9%), 200d 190.99 (+6.2%); 50d above 200d
Momentum: RSI(14) 51.3 | MACD 0.901 vs signal 1.035 (histogram -0.133)
Returns: 1d +0.1% | 5d +0.8% | 1m +3.1% | 3m -6.2%
52-week range: 146.56 - 217.87 (now 78.9% of the way up)
Volatility: ATR(14) 3.20 (1.6% of price) | annualised 20d 20.5%
Volume: 0.01x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 280.79B
Valuation: trailing P/E 17.73 | forward P/E 15.92 | P/B 2.94 | PEG 1.92
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: buy (mean 2.21 on a 1=strong buy to 5=strong sell scale, 3 analysts)
Ratings: 4 strong buy, 4 buy, 5 hold, 0 sell, 1 strong sell
Price target: mean 209.34 (+3.2% vs last close), range 182.71 - 230.24
Recent rating changes:
  - 2025-08-29 Argus Research: main, Buy -> Buy
  - 2024-12-05 BMO Capital: main, Outperform -> Outperform
  - 2024-08-29 BMO Capital: main, Outperform -> Outperform
  - 2024-06-06 Argus Research: main, Buy -> Buy
  - 2024-04-05 BMO Capital: up, Market Perform -> Outperform
  - 2023-12-18 B of A Securities: up, Neutral -> Buy
Institutional ownership: 50.8%
Largest holders: Royal Bank of Canada (5.1%), Bank of Montreal /CAN/ (4.2%), Vanguard Capital Management LLC (3.1%), TD Asset Management, Inc (1.7%), NORGES BANK (1.4%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 415,328 shares
Distinct insiders: 1 buying, 0 selling
Open-market purchases — insiders spending their own money:
  - 2026-10-30 Royal Bank of Canada (Issuer): 308 shares, 62.87K
  - 2026-10-30 Royal Bank of Canada (Issuer): 177 shares, 36.30K
  - 2026-10-30 Royal Bank of Canada (Issuer): 118 shares, 24.13K
  - 2026-10-30 Royal Bank of Canada (Issuer): 142 shares, 29.14K
(93 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Toyota (TM) · Company — BULLISH, confidence 0.45

**Result:** ACCEPTED · 1 shares · submitted buy 1 TM @ ~213.53, stop 204.30

**In the model's own words:**

> Buy signal driven by strong earnings record, analyst consensus buy with a sizable price target upside, technicals showing price above key moving averages and positive momentum, and a cheap trailing P/E suggesting undervaluation despite high leverage.

**Main reasons it gave:**
- 3 out of 4 recent earnings beats (Earnings Record)
- Analyst consensus buy with mean price target +11.5% above current price
- Technical: price above 20/50/200‑day SMA, RSI 64, MACD positive
- Trailing P/E 9.73 suggests cheap valuation

<details><summary><b>News</b> — score +0.00</summary>

- [TM Redwheel Glbl Eq Inc R Acc (0P0001KUY8.L) Stock Forum & Discussion - Yahoo Finance](https://ca.finance.yahoo.com/quote/0P0001KUY8.L/community/)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  Find the latest TM Redwheel Glbl Eq Inc R Acc (0P0001KUY8.L) stock discussion in Yahoo Finance's forum. Share your opinion and gain insight from other stock...
- [Greenwich LifeSciences Interview to Air Nationally on the RedChip Small Stocks, Big Money(TM) Show on CNBC and Bloomberg TV](https://www.guardonline.com/news/national/greenwich-lifesciences-interview-to-air-nationally-on-the-redchip-small-stocks-big-money-tm-show/article_dd2be4f8-d566-5a3c-ba45-221435d199aa.html)  
  <sub>The Batesville Daily Guard, 41 minutes ago</sub>  
  ORLANDO, FL / ACCESS Newswire / November 13, 2026 / RedChip Companies will air an interview with Greenwich LifeSciences, Inc. (NASDAQ:GLSI) on the RedChip...
- [South Hadley TM rejects school bus stop-arm cameras over surveillance, data concerns](https://www.google.com/goto?url=CAESsgEBxCJF13l_8dBQxMkQI6az86vTr4wyZCiP9SOrDnm0FB0iYOE_B-_YiSCaGtE37EMfzNOlb8uPIO1jfMFKWebFp8tDjuvFfhKOAWZpfE5GVelcIvHBD2aw2YZ1hOl_BOrIgFohlTHqFYVdwhbCE3k7pO5N3ZmBMyf_LMcTDxmVe82wIatdfd5LjRBXzW2Vw_O8AknFc7ouuJ7mmdvenLm2nVGwqxumBhLn7dvua0T_C45_&gsessionid=LbtDuohYvs81h7x4S1dBhtvmR_TNfsjTrr6hZ_xl_BRdsXUbIXMZpA)  
  <sub>Daily Hampshire Gazette, 18 hours ago</sub>  
  SOUTH HADLEY — Town Meeting voters this week rejected a proposal to install cameras on school bus stop arms to catch drivers who illegally pass stopped...
- [(HBND) Technical Pivots with Risk Controls (HBND:CA)](https://www.google.com/goto?url=CAESngEBxCJF1zoHCsXY7T-yZ13N5Kc4AvnLfCQrXJ2A8CgCel38dpOznxTsaeNuN452GF78x_xlHihsCNFEvFNycsSIqqzivUH-keQGlkZLSz6QrzlwiXPEyoaLiODhzTabYnePiF0oAm-LONgOCfblIuTUiDsVMww2jAaFE7zrlZLuVh4qJGDvYq2qNlbMPAenhQONsQ4UGDXY87uAR01b1Q&gsessionid=LbtDuohYvs81h7x4S1dBhtvmR_TNfsjTrr6hZ_xl_BRdsXUbIXMZpA)  
  <sub>Stock Traders Daily, 1 hour ago</sub>  
  Technical analysis for Hamilton U.S. Bond YIELD MAXIMIZER TM ETF HBND including support levels resistance levels and stop losses for HBND.
- [TM UBS (UK) - Global Growth I Inc (0P0001H150.L) Latest Stock News & Headlines - Yahoo Finance](https://www.google.com/goto?url=CAEScQHEIkXXmJS9x-4d7xCYjqJwB_k2I_3JUBMZZyu697IwX7vSq5IZ1_pfgZiTJm18FWuuGvaqu4WMk7CXHu6L71UZM5HHam4vAl2IC4FpNpW9HEiwqiDwRInfdUY5z4EcmVKZvrf1mgvIy9SIqkJhvadU&gsessionid=LbtDuohYvs81h7x4S1dBhtvmR_TNfsjTrr6hZ_xl_BRdsXUbIXMZpA)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  Get the latest TM UBS (UK) - Global Growth I Inc (0P0001H150.L) stock news and headlines to help you in your trading and investing decisions.
- [When the Price of (EMAX) Talks, People Listen (EMAX:CA)](https://www.google.com/goto?url=CAESoQEBxCJF1yGl50Rv2wCzi5EpCCls2acVOyGZP6SKyqpjQPa_8yE4xdfWlidpWd8lr4oMFUoWSIuNEEq60LeR_TXodJAQFMCw9J4HxDF-aTBjKbFt_ouHySzAFTvm5DQd1iHrIqEu76B6XgKg3fbB1YBS40Q-FopYUvJNMUoP9ZDywTXF3gkfbo6d35zzoJw9zZDWxCL0rHWNZhOP0-0dAV5vrw&gsessionid=LbtDuohYvs81h7x4S1dBhtvmR_TNfsjTrr6hZ_xl_BRdsXUbIXMZpA)  
  <sub>Stock Traders Daily, 17 hours ago</sub>  
  When the Price of Hamilton Energy YIELD MAXIMIZER TM ETF EMAX Talks, People Listen.
- [With $14.5 million in cash, Aetherion says its projected funds won't cover 12 months of operations.](https://www.google.com/goto?url=CAESpAEBxCJF10hfsukQZJzOAYMfbHSXgqSRFkfWn4rYCpUlH_uDt0rR-W9rBGUwialbpgHdb8Q_yXcDwpnnW_dfVk9R4r6xlXWBx3pQumtyYHGAJluj-cqE_ayS12uVD54Xpy_DG78TGCzKhTE52Em1aNajNiBflbtxod_0K2CvLz9KoM6CVg55c3dgnXVMuNUXTY_sLuNklH4ZpJRfDIVmozn54G69Ag&gsessionid=LbtDuohYvs81h7x4S1dBhtvmR_TNfsjTrr6hZ_xl_BRdsXUbIXMZpA)  
  <sub>Stock Titan, 17 hours ago</sub>  
  Cespira product revenue rose 85%, while Aetherion's continuing-operations loss narrowed to $3.0 million. The company's results call is set for Nov. 13.
- [HEG Advanced Material Signs Major EV MoU | Sical Q2 FY27 Results | Top Buzzing Stocks Today](https://www.google.com/goto?url=CAES0wEBxCJF16TMtOlRSdDUO1JJwOuBnq6Q67ra0_8jnu8IQ3QXRM2RxSFhvkLiBnSg3EsFHrshbtVLg_J7elg_QSG8Lup5c-Yd7paqRVplBs0O8-CXIUCA10fYZjE1YInw-ti8u5dBhxSBrVU6hfcDixA6Tn7zqQKPXu9qjpyFoo_H5YY_7fRths1dnvYA9rJnk1WukQOPRg-yuIV47PU_bstxKyVDHYBXd7geMor5rOpaCL57dGkpm2Q6ndrk2ylIrPNLhTvKgmM73ZRu-BLduzlUAUG4&gsessionid=LbtDuohYvs81h7x4S1dBhtvmR_TNfsjTrr6hZ_xl_BRdsXUbIXMZpA)  
  <sub>Equitymaster, 14 hours ago</sub>  
  Top cues to track in today's stock market session.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 213.43 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 202.69 (+5.3%), 50d 194.84 (+9.5%), 200d 197.90 (+7.8%); 50d below 200d
Momentum: RSI(14) 64.1 | MACD 6.065 vs signal 4.932 (histogram 1.133)
Returns: 1d +1.8% | 5d -1.3% | 1m +11.2% | 3m +12.8%
52-week range: 166.50 - 248.29 (now 57.4% of the way up)
Volatility: ATR(14) 4.62 (2.2% of price) | annualised 20d 39.1%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 251.38B
Valuation: trailing P/E 9.73 | forward P/E 13.53 | P/B 16.99 | PEG n/a
Profitability: profit margin 8.1% | operating margin 7.5% | ROE 11.6%
Growth (YoY): revenue +8.6% | earnings -10.1%
Balance sheet: debt/equity 112.8% | free cash flow -3.04T
Risk: beta 0.38 | short interest 0.1% of float
Next earnings: 2027-02-04
```

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.20</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 in line
  2026-09-30 in line | 2026-06-30 beat by 44% | 2026-03-31 beat by 12% | 2025-12-31 beat by 27%
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
Consensus: buy (mean 2.25 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 1 strong buy, 1 buy, 2 hold, 0 sell, 0 strong sell
Price target: mean 238.08 (+11.5% vs last close), range 230.00 - 253.00
Recent rating changes:
  - 2026-11-12 Freedom Broker: down, Buy -> Hold
  - 2025-11-07 Freedom Broker: down, Buy -> Hold
  - 2025-02-04 Macquarie: up, Neutral -> Outperform
  - 2024-06-14 Erste Group: down, Buy -> Hold
  - 2023-07-11 Morgan Stanley: down, Overweight -> Equal-Weight
  - 2022-10-06 UBS: down, Buy -> Neutral
Institutional ownership: 2.3%
Largest holders: Fisher Asset Management, LLC (0.5%), Morgan Stanley (0.2%), FMR, LLC (0.1%), Goldman Sachs Group Inc (0.1%), Northern Trust Corporation (0.1%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 942,259 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Exxon Mobil (XOM) · Company — NEUTRAL, confidence 0.38

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> mixed signals: positive news (lithium project, large fund purchase) vs bearish technicals (RSI 46.5, MACD negative, low volume); fundamentals strong but not immediate; analyst view slightly bullish; insider activity neutral; earnings record neutral

**Main reasons it gave:**
- Lithium extraction project announced in Arkansas Smackover Formation (Yahoo Finance, 20h ago)
- Technical indicators (RSI 46.5, MACD negative) suggest short-term weakness (daily bars)
- Strong fundamentals: revenue +32.6% YoY, forward P/E 13.5, debt/equity 12.6% (Fundamentals)
- Jones Financial Companies LLLP opened $475.3M XOM position (13F filing, 35m ago)

<details><summary><b>News</b> — score +0.30</summary>

- [Fund Update: New $475.3M $XOM stock position opened by JONES FINANCIAL COMPANIES LLLP](https://www.quiverquant.com/news/Fund+Update%3A+New+%24475.3M+%24XOM+stock+position+opened+by+JONES+FINANCIAL+COMPANIES+LLLP)  
  <sub>Quiver Quantitative, 35 minutes ago</sub>  
  JONES FINANCIAL COMPANIES LLLP has opened a new $475.3M position in $XOM, per a new SEC 13F filing.
- [Bernstein Keeps Their Buy Rating on Exxon Mobil (XOM)](https://www.theglobeandmail.com/investing/markets/stocks/XOM/pressreleases/8816970/bernstein-keeps-their-buy-rating-on-exxon-mobil-xom/)  
  <sub>The Globe and Mail, 5 hours ago</sub>  
  Bernstein analyst Bob Brackett maintained a Buy rating on Exxon Mobil yesterday and set a price target of $186.00. The company's shares closed yesterday at...
- [ExxonMobil Holdings (XOM) Moves Into Arkansas Lithium With A New Smackover Bet](https://www.google.com/goto?url=CAESnAEBxCJF1z1rrzd2Mzn2zJ1CXOkUCXzhzjfXjorXbfJ1e-MNQj2iTPB5pJ2ORaP9PTxxqkKNW_6oO6O-DXfCzluopM-ct6-FfLEwUd03hqvU6t94vc2zuslJbwer87WO-QLi44jw04QgV-YW1gF444RY3e2Omr7drMApEXrugnp_LQ0sFEXFbW-5L8NX_e2O2cnbquklWfmBdZ56ZNI&gsessionid=MkMX-0cFqRq0alhFgu__VsWj1YD45fidXRLh3OeKQikte0AsheCRKw)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  ExxonMobil Holdings (NYSE:XOM) is moving into lithium extraction in Arkansas' Smackover Formation as part of a new U.S. project. The Arkansas lithium effort...
- [XOM, CVX, COP: This Analyst Trims Price Targets, Warns Oil Stocks May 'Struggle To Appreciate'](https://www.google.com/goto?url=CAES5gEBxCJF12g4xtwz39WOpbcAhWIjRR0CPDaLEaJ6uiOXgfL-DxYSh4mJXPQ_DFPkQotNlpum-aRgYkWtQ7jpcymlt_GdqlfXasr2AQVCI8XIpBBYXMJZJixyBMNEGHUiXb9PwpwU6lzWqURHKuwX2YPIbM7zonsDXwXtEInZEmQDk4olDQcvEbC7t4p5a-3X3_IWxl0w5jtxtOP6JbOceajJziH89EtynOwYGtzZxRs98LidYqoOluGsuPLIlRfBsWMMOAuWaEBMiRVhELcwnDnxCG-RuQOCsSLmxv-2wCoakCoQl-tKAQ&gsessionid=MkMX-0cFqRq0alhFgu__VsWj1YD45fidXRLh3OeKQikte0AsheCRKw)  
  <sub>TradingView, 13 hours ago</sub>  
  The analyst lowered the target on ExxonMobil to $186 from $193 and kept an 'Outperform' rating on the shares. On Chevron, Bernstein cut the price target to...
- [Exxon approves $12.5B Longtail project offshore Guyana (XOM:NYSE)](https://www.google.com/goto?url=CAESmAEBxCJF17ucREK9pRuWdry8sGn43DQtrWn_3YIMpMtX4nWgI559onOYxBE4GbiagJch-YH3YH01vHwzKFmCI-_th-9OSiL8_vktmZCc7ia7UgRmQhvtkjSaMQXJ_N-_t7U_hN2OeMXOiqnLiZ0sO5Iq4oLv7Goi6afuoy4eQFjB47Q2PNmaytPmlkEbhN_IYec3HkzvQll4Ow&gsessionid=MkMX-0cFqRq0alhFgu__VsWj1YD45fidXRLh3OeKQikte0AsheCRKw)  
  <sub>Seeking Alpha, 15 hours ago</sub>  
  ExxonMobil said it made a final investment decision for the $12.5B Longtail development offshore Guyana, the eighth development located in the southeastern...
- [443,020 ExxonMobil Corporation $XOM Shares Sold by Russell Investments Group Ltd.](https://www.google.com/goto?url=CAESyQEBxCJF18y0fKjJQ72KMrXGvk4GCewuf7pVIJuF7vhAHDr1_W3lhOHeEE4qetd1NK1GPsMRlfNK77EIA-_WWYs2kBL8T2NZpo8q_e3HMsqpjdDCya4z-Iwj7a_4C6F3VblKbuoPnn_jaWra5Rp8S6WevfeK15d_jsfSx4Cimq1KqS9sO-tlZ_BFkp4YqWqh18ycQ665RcQp5nfkaaQUQeaM4uXHZFyE7-X7ODY-LlOELzALKTvRrLqf5CYZ93K0DdpNcxZfBi3Zve4&gsessionid=MkMX-0cFqRq0alhFgu__VsWj1YD45fidXRLh3OeKQikte0AsheCRKw)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Russell Investments Group Ltd. decreased its holdings in shares of ExxonMobil Corporation (NYSE:XOM - Free Report) by 13.7% during the 3rd quarter,...
- [XOM: SEC Form DEFA14A filed by ExxonMobil Holdings Corporation](https://www.google.com/goto?url=CAESoQEBxCJF11PZqkzM4XitaM73vfF82Wl9kx3c0-vhpFFrEUpGXWdiSq_FalEGsyxsktpWDhF8YjioqAqK0jSi1rwpmta3S4uKxJOTdD0-2jkDGbhJjFrSmuKbtb_pq0De30qF00UUeiVVu2js_PpRDg2uqGLmQ92O-ERv2lE9oc39QRNIjeZy5yfPu-2eAErbref4gDoiFP_00c0fDVgU0GrceQ&gsessionid=MkMX-0cFqRq0alhFgu__VsWj1YD45fidXRLh3OeKQikte0AsheCRKw)  
  <sub>Quantisnow, 23 hours ago</sub>  
  ExxonMobil Holdings Corporation filed a soliciting material form, DEFA14A, that contains screenshots of updated retail shareholder and voting webpages.
- [ExxonMobil Holdings Corporation (XOM) Stock Forecasts](https://www.google.com/goto?url=CAESjwEBxCJF15gIKrv-4mTalMiFaFeOaQ6X_5ZZx8P_W8op2mXK_fwRm4sJoykWI1VaWjsJc0ci-5Rhm1d8VjXeSlCMtIwAaFjYd8uUUdrxzKluT7fCfqF7ALup5_lRcJKGMIvsDkqBpPZU515qxvRCerXwUeoAvZs7p8XbqcON4OET6JAzF_7ZESjfoVzHjXL_yQ&gsessionid=MkMX-0cFqRq0alhFgu__VsWj1YD45fidXRLh3OeKQikte0AsheCRKw)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [How Lithium Expansion Will Impact ExxonMobil Stock Investors](https://www.google.com/goto?url=CAESwwEBxCJF1y4iGZjyIq_tShTBK3MAJJ1dg1kJs0MTi2TqTQQtxsJxmYo6bHPXLNYgvIveC7GsgkInLY7e9Fvt8-Kv1JLAQK5mugf8_01q7RmmV1kQi2f2SaGRcCE64TwW_KfIx4ekaJKxneZP9_cKAifCwg01233YS6D48C_QtKaqY43GgCFWqExyVHCnioVKf9TrZzA7dM_IRQm8gGaakxkQ0kWxyofIrSsS7j7A5ot7vJzxwwXC_ozDm2D6N_m4aze2tVU&gsessionid=MkMX-0cFqRq0alhFgu__VsWj1YD45fidXRLh3OeKQikte0AsheCRKw)  
  <sub>Simply Wall St, 14 hours ago</sub>  
  ExxonMobil Holdings reported Q3 2026 revenue of US$113.164b and net income of US$15.413b, raised its quarterly dividend to US$1.07 per share, and advanced...
- [ExxonMobil's Guyana project could produce up to 250,000 barrels of light oil daily, with start-up expected in 2030.](https://www.google.com/goto?url=CAESrQEBxCJF14aGh3dDmtV36txYy75NMhp3nlKaQuxosaVQalxZCovaeEZhJYuFIQrYclQKwG68CsMeWWLFbKPZtqVbRy6xo_7qvbfabt5u3wRrqD_xJGNV-7a8K9G3b8WEUozlLk5kl_Fgex40cUe6Y1C5Z3-djq1hinScLpIXkbLVlIJ_z9z5m2LESkvZ6NzPXorcB0ECAa6kbrDpvf4e1nCEnvO_IVPQClIrFtZihA&gsessionid=MkMX-0cFqRq0alhFgu__VsWj1YD45fidXRLh3OeKQikte0AsheCRKw)  
  <sub>Stock Titan, 17 hours ago</sub>  
  Its floating vessel is designed to process 1.2 billion standard cubic feet of gas daily; Longtail is expected to include about 45 subsea wells.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 169.44 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 175.27 (-3.3%), 50d 169.36 (+0.0%), 200d 156.36 (+8.4%); 50d above 200d
Momentum: RSI(14) 46.5 | MACD -1.072 vs signal 0.476 (histogram -1.548)
Returns: 1d -0.2% | 5d +2.2% | 1m -3.0% | 3m +4.9%
52-week range: 114.51 - 187.25 (now 75.5% of the way up)
Volatility: ATR(14) 4.30 (2.5% of price) | annualised 20d 30.6%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 691.18B
Valuation: trailing P/E 17.43 | forward P/E 13.50 | P/B 2.60 | PEG 1.31
Profitability: profit margin 10.5% | operating margin 12.9% | ROE 15.5%
Growth (YoY): revenue +32.6% | earnings +111.4%
Balance sheet: debt/equity 12.6% | free cash flow 28.32B
Risk: beta 0.14 | short interest 1.2% of float
Next earnings: 2027-01-29
```

</details>

<details><summary><b>What this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.60</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-09-30 beat by 3% | 2026-06-30 in line | 2026-03-31 beat by 14% | 2025-12-31 in line
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: buy (mean 2.42 on a 1=strong buy to 5=strong sell scale, 22 analysts)
Ratings: 3 strong buy, 6 buy, 17 hold, 0 sell, 0 strong sell
Price target: mean 184.32 (+8.8% vs last close), range 160.00 - 213.00
Recent rating changes:
  - 2026-11-12 Bernstein: main, Outperform -> Outperform
  - 2026-11-07 Freedom Broker: main, Hold -> Hold
  - 2026-11-04 Citigroup: main, Neutral -> Neutral
  - 2026-11-04 TD Cowen: main, Buy -> Buy
  - 2026-11-02 UBS: main, Buy -> Buy
  - 2026-11-02 Morgan Stanley: main, Overweight -> Overweight
Institutional ownership: 69.0%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.6%), State Street Corporation (5.2%), FMR, LLC (3.6%), Vanguard Portfolio Management LLC (2.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 10,818,651 shares in 251 transaction(s) | sold 3,904,152 shares in 49
Net: +6,914,499 shares (-190.1% of insider holdings) | insiders hold 3,263,378 shares
Distinct insiders: 0 buying, 0 selling
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

- [How Does a $260 Million PULS Contract Change Elbit Systems’ (NASDAQ:ESLT) European Outlook?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af721fd63064f87b875f569fb8d0e5e&url=https%3a%2f%2fkalkine.com.au%2fnews%2findustrials%2fhow-does-a-260-million-puls-contract-change-elbit-systems-nasdaqeslt-european-outlook&c=7929743924413528280&mkt=en-us)  
  <sub>kalkine, 30h ago</sub>  
  Elbit Systems Ltd. (NASDAQ:ESLT) announced on November 12, 2026, that it has been awarded a contract valued at approximately $260 million to supply Precise & Universal Launching System rocket ...
- [Elbit Systems Awarded $260 Million Contract to Supply PULS Rocket Artillery Systems to a European NATO Country](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af721fd63064f87b875f569fb8d0e5e&url=https%3a%2f%2fwww.marketscreener.com%2fnews%2felbit-systems-awarded-260-million-contract-to-supply-puls-rocket-artillery-systems-to-a-european-na-ce785ed8d881f621&c=14714910117891135382&mkt=en-us)  
  <sub>MarketScreener, 32h ago</sub>  
  The PULS system provides a comprehensive and cost-effective solution capable of launching unguided rockets, precision-guided munitions, and missiles with various ranges. The launcher is fully ...
- [埃尔比特系统收跌0.34%，成交额8158.2万美元](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af721fd63064f87b875f569fb8d0e5e&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fusstock%2fnotice%2f2026-11-13%2fdoc-iniypqyq8165420.shtml&c=17864551189437613515&mkt=en-us)  
  <sub>新浪财经, 23h ago</sub>  
  11月13日，埃尔比特系统（ESLT）收跌0.34%，报723美元，成交额8158.2万美元，市值338.94亿美元。 公司最新财报显示，季度营收22.87亿美元，同比增长15.94%；净利润1.74亿美元，同比增长38.13%。 公司简介 该公司开发并提供一系列用于国防、国土安全和商业航空应用的空中、陆地和海军系统及产品。该公司的系统和产品安装在新平台上，同时也执行平台现代化项目。此外，该公司还 ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 701.22 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 740.38 (-5.3%), 50d 723.54 (-3.1%), 200d 785.29 (-10.7%); 50d below 200d
Momentum: RSI(14) 45.3 | MACD -4.156 vs signal 0.292 (histogram -4.449)
Returns: 1d -3.0% | 5d +2.7% | 1m -5.4% | 3m -10.4%
52-week range: 454.95 - 1,014.33 (now 44.0% of the way up)
Volatility: ATR(14) 27.58 (3.9% of price) | annualised 20d 60.2%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 32.87B
Valuation: trailing P/E 52.76 | forward P/E 37.68 | P/B 7.44 | PEG n/a
Profitability: profit margin 7.4% | operating margin 9.4% | ROE 15.2%
Growth (YoY): revenue +15.9% | earnings +34.2%
Balance sheet: debt/equity 19.3% | free cash flow -38.48M
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
Consensus: hold (mean 2.67 on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 838.92 (+19.6% vs last close), range 738.50 - 960.00
Recent rating changes:
  - 2026-10-05 Jefferies: main, Hold -> Hold
  - 2026-08-19 JP Morgan: main, Neutral -> Neutral
  - 2026-06-24 Jefferies: main, Hold -> Hold
  - 2026-05-27 Jefferies: main, Hold -> Hold
  - 2026-05-27 JP Morgan: main, Neutral -> Neutral
  - 2026-04-13 JP Morgan: main, Neutral -> Neutral
Institutional ownership: 27.0%
Largest holders: Clal Insurance Enterprises Holdings Ltd (3.5%), Vanguard Capital Management LLC (1.6%), Van Eck Associates Corporation (1.2%), Y.D. More Investments Ltd (1.1%), Altshuler Shaham Ltd (1.1%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 19,271,332 shares
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

- [HDFC Bank stock gains 3.98% since Bagchi vote report](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af721bb2a7a44658f3eb01a01f94b4b&url=https%3a%2f%2fwww.ad-hoc-news.de%2fboerse%2fnews%2fcorporate-news%2fhdfc-bank-stock-gains-3-98-prozent-since-bagchi-vote-report%2f70498839&c=10688384696038676386&mkt=en-us)  
  <sub>Ad Hoc News, 31h ago</sub>  
  HDFC Bank stock gained 3.98 percent from the latest AD HOC NEWS report to the latest Lang & Schwarz indication. The move comes after shareholders approved Anup Bagchi's appointment as managing ...
- [HDB: Announcement of the change of listing](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af721bb2a7a44658f3eb01a01f94b4b&url=http%3a%2f%2fen.stockbiz.vn%2fNews%2f2026%2f11%2f12%2f1924155%2fhdb-announcement-of-the-change-of-listing.aspx&c=7287211723086045205&mkt=en-us)  
  <sub>Stockbiz, 13h ago</sub>  
  Your most recently viewed tickers will automatically show up here if you type a ticker in the Get Quotes box on the top of the page.
- [HDFC Bank shares stage a comeback, rally over 12% in 1 month; has India's largest private lender finally escaped its valuation trap?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af721bb2a7a44658f3eb01a01f94b4b&url=https%3a%2f%2fwww.msn.com%2fen-in%2fnews%2fother%2fhdfc-bank-shares-stage-a-comeback-rally-over-12-in-1-month-has-indias-largest-private-lender-finally-escaped-its-valuation-trap%2far-AA2hlniP&c=2012463450797539490&mkt=en-us)  
  <sub>ET Now on MSN, 15h ago</sub>  
  HDFC Bank shares have rebounded over 12 per cent in a month, but concerns around valuations are still looming. Citi sees 16 per cent upside as an analyst assesses its growth prospects.
- [Stellar comeback! HDFC Bank shares rally 20% in 12 sessions, add Rs 2 lakh crore in market cap: What's next?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af721bb2a7a44658f3eb01a01f94b4b&url=https%3a%2f%2fwww.zeebiz.com%2fmarket-news%2fnews-stellar-comeback-hdfc-bank-shares-rally-20-in-12-sessions-add-rs-2-lakh-crore-in-market-cap-whats-next-405519&c=2702100558410622940&mkt=en-us)  
  <sub>Zee Business, 13h ago</sub>  
  Zee Business provides the latest business news such as Indian stock market news and Updates, sensex live news & nifty news. Check out the personal finance news from the world of business including BSE ...
- [INDIA BONDS-India bonds under pressure before debt supply; hot inflation prints pinch further](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af721bb2a7a44658f3eb01a01f94b4b&url=https%3a%2f%2fwww.marketscreener.com%2fnews%2findia-bonds-india-bonds-under-pressure-before-debt-supply-hot-inflation-prints-pinch-further-ce785ed9db8cf220&c=4670729595731036854&mkt=en-us)  
  <sub>MarketScreener, 18h ago</sub>  
  India new issue-summary of primary bond market deals reported on November 12 RE Nov. 12 India new issue-HDB Financial Services accepts bids for 3-year bonds, bankers say RE Nov. 12 India new ...
- [BNP Paribas prefers private banks; sees valuation upside in HDFC Bank](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af721bb2a7a44658f3eb01a01f94b4b&url=https%3a%2f%2fwww.cnbctv18.com%2feconomy%2fbnp-paribas-santanu-chakrabarti-hdfc-bank-private-lenders-nbfcs-icici-bank-axis-bank-rbi-reserve-bank-of-india-alpha-article-20033267.htm&c=5872320130441278985&mkt=en-us)  
  <sub>CNBCTV18, 16h ago</sub>  
  Santanu Chakrabarti, India Analyst, BFSI, BNP Paribas, said HDFC Bank remains the firm's top pick, with returns expected to improve over the next two years. He also believes concerns around gold-loan ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 25.84 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 23.56 (+9.7%), 50d 23.05 (+12.1%), 200d 25.44 (+1.6%); 50d below 200d
Momentum: RSI(14) 71.0 | MACD 0.872 vs signal 0.529 (histogram 0.344)
Returns: 1d +0.5% | 5d +2.8% | 1m +9.8% | 3m +11.6%
52-week range: 21.36 - 37.13 (now 28.4% of the way up)
Volatility: ATR(14) 0.59 (2.3% of price) | annualised 20d 32.0%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 132.92B
Valuation: trailing P/E 16.67 | forward P/E 18.71 | P/B 10.29 | PEG n/a
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
Consensus: none (mean n/a on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 1 strong buy, 2 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 30.30 (+17.3% vs last close), range 26.20 - 33.00
Recent rating changes:
  - 2024-07-22 JP Morgan: down, Overweight -> Neutral
  - 2019-09-09 Bernstein: down, Outperform -> Market Perform
  - 2019-06-11 Nomura: down, Buy -> Neutral
  - 2017-03-21 Morgan Stanley: down, Overweight -> Equal-Weight
  - 2016-09-14 Goldman Sachs: main, ? -> Buy
  - 2015-03-11 Societe Generale: init, ? -> Buy
Institutional ownership: 14.3%
Largest holders: Morgan Stanley (1.0%), Royal Bank of Canada (0.8%), JPMORGAN CHASE & CO (0.7%), Schroder Investment Management Group (0.4%), Temasek Holdings (Private) Ltd (0.4%)
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

### MercadoLibre (MELI) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [MercadoLibre (MELI) Stock Price Prediction: Analyst cuts meet a soft technical bid near $1,500](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af722221b0a4b5a9162f8ff1a4d8b0c&url=https%3a%2f%2fblockchain.news%2fnews%2f20261112-price-prediction-meli-analyst-cuts-meet-a-soft-technical&c=15445711251721509119&mkt=en-us)  
  <sub>Blockchain News, 24h ago</sub>  
  MercadoLibre (MELI) is trading at $1,513.52, just above its pivot point of $1,500.47, after a day that was essentially flat at -0.07%. The setup is ...
- [Online marketplace stocks Q3 teardown: MercadoLibre vs the rest](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af722221b0a4b5a9162f8ff1a4d8b0c&url=https%3a%2f%2fstockstory.org%2fus%2fstocks%2fnasdaq%2fmeli%2fnews%2fearnings%2fonline-marketplace-stocks-q3-teardown-mercadolibre-vs-the-rest&c=13887084842125186782&mkt=en-us)  
  <sub>stockstory, 19h ago</sub>  
  As the craze of earnings season draws to a close, here’s a look back at some of the most exciting (and some less so) results from Q3. Today, we are looking ...
- [MercadoLibre stock faces a sharper test of profitable growth](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af722221b0a4b5a9162f8ff1a4d8b0c&url=https%3a%2f%2fwww.ad-hoc-news.de%2fboerse%2fnews%2fcorporate-news%2fmercadolibre-stock-faces-a-sharper-test-of-profitable-growth%2f70499150&c=14344674641643269290&mkt=en-us)  
  <sub>Ad Hoc News, 31h ago</sub>  
  MercadoLibre stock faces a sharper profit test after strong third-quarter growth. Logistics, shipping and Brazilian marketing investments are weighing on margins. MercadoLibre's third-quarter revenue ...
- [“大空头”更新持仓：加仓京东、PayPal等股票，称京东被严重低估](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af722221b0a4b5a9162f8ff1a4d8b0c&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fbxjj%2f2026-11-13%2fdoc-iniyqfvz1019638.shtml&c=14209955127216617873&mkt=en-us)  
  <sub>新浪财经, 19h ago</sub>  
  格隆汇11月13日｜“大空头”原型人物Michael Burry通过其Substack账号披露个人最新持仓调整表示，近期进一步增持PayPal(PYPL)、MercadoLibre(MELI)、Sprouts Farmers Market(SFM)、Adobe(ADBE)、京东(JD)和Ero Copper(ERO)，同时重新买入Lululemon(LULU)，显示其正在继续调整股票投资组合。 B ...
- [MercadoLibre收跌2.44%，成交额7.64亿美元](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af722221b0a4b5a9162f8ff1a4d8b0c&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fusstock%2fnotice%2f2026-11-13%2fdoc-iniypqyr3738405.shtml&c=8206572591226236079&mkt=en-us)  
  <sub>新浪财经, 23h ago</sub>  
  11月13日，MercadoLibre（MELI）收跌2.44%，报1475.09美元，成交额7.64亿美元，市值747.82亿美元。 公司最新财报显示，季度营收107.5亿美元，同比增长45.09%；净利润4.48亿美元，同比增长6.41%。 公司简介 该公司的电子商务产品通过互联网平台实现零售和批发，旨在为用户提供一系列服务以促进商业交易。该公司的地理覆盖范围包括拉丁美洲的约18个国家。该公司 ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,487.11 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 1,656.62 (-10.2%), 50d 1,760.71 (-15.5%), 200d 1,783.65 (-16.6%); 50d below 200d
Momentum: RSI(14) 33.1 | MACD -86.068 vs signal -68.831 (histogram -17.236)
Returns: 1d +0.8% | 5d -1.5% | 1m -19.9% | 3m -16.8%
52-week range: 1,475.09 - 2,295.00 (now 1.5% of the way up)
Volatility: ATR(14) 66.06 (4.4% of price) | annualised 20d 58.3%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 75.39B
Valuation: trailing P/E 39.89 | forward P/E 27.74 | P/B 9.19 | PEG 0.83
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
Consensus: strong_buy (mean 1.50 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 5 strong buy, 17 buy, 4 hold, 0 sell, 0 strong sell
Price target: mean 2,210.32 (+48.6% vs last close), range 1,600.00 - 2,800.00
Recent rating changes:
  - 2026-11-11 UBS: main, Neutral -> Neutral
  - 2026-11-09 JP Morgan: main, Neutral -> Neutral
  - 2026-11-05 Scotiabank: main, Sector Outperform -> Sector Outperform
  - 2026-11-05 StoneX: main, Buy -> Buy
  - 2026-11-05 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-11-05 BTIG: main, Buy -> Buy
Institutional ownership: 80.7%
Largest holders: Capital Research Global Investors (6.0%), BAILLIE GIFFORD & CO (5.8%), Capital International Investors (3.9%), Capital World Investors (3.7%), Morgan Stanley (2.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 3,528,497 shares
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

### Microsoft (MSFT) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Microsoft stock slumps on outage that includes the Copilot tool it has been heavily promoting](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af72171d61d40b7a3a1689f3e591823&url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fmicrosoft-stock-slumps-on-outage-that-includes-the-copilot-tool-it-has-been-heavily-promoting%2far-AA2hmRK5&c=4034141822553627423&mkt=en-us)  
  <sub>MarketWatch on MSN, 10h ago</sub>  
  Microsoft stock fell in premarket trade Friday as the company struggled to address a worldwide outage of its popular products.
- [Microsoft Stock Slips on Widespread Outage](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af72171d61d40b7a3a1689f3e591823&url=https%3a%2f%2fwww.wsj.com%2flivecoverage%2fstock-market-today-dow-sp-500-nasdaq-11-13-2026%2fcard%2fBov00V9K8D7MQ4VxwCYG&c=854867936949735163&mkt=en-us)  
  <sub>The Wall Street Journal, 23h ago</sub>  
  Microsoft said it is working to resolve an hourslong outage that has disrupted services that include Outlook and Teams, with government departments and schools from the U.S. to Australia among those ...
- [Microsoft’s global Office outage is terrible timing for the stock](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af72171d61d40b7a3a1689f3e591823&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2ftop-stocks%2fmicrosoft-s-global-office-outage-is-terrible-timing-for-the-stock%2far-AA2hlY2O&c=218656748274126568&mkt=en-us)  
  <sub>Barron's on MSN, 10h ago</sub>  
  A global outage has hit the company’s Outlook, Teams, and Copilot AI assistant, impacting users across more than 70 countries, according to outage tracker Downdetector ...
- [What Does Microsoft’s Slide Mean for a 67-Year-Old With $700,000 of a $2.4 Million IRA in the Stock?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af72171d61d40b7a3a1689f3e591823&url=https%3a%2f%2f247wallst.com%2finvesting%2f2026%2f11%2f13%2fwhat-does-microsofts-slide-mean-for-a-67-year-old-with-700000-of-a-2-4-million-ira-in-the-stock%2f&c=4846851702917199363&mkt=en-us)  
  <sub>24/7 Wall St., 10h ago</sub>  
  Five trading days were enough to show what a single stock can do to a retirement account. Microsoft shares are trading nearly 6% lower than their one-month high.
- [MSFT Stock Price Faces Pressure as Microsoft Outage and $170 Billion AI Spending Raise Concerns](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af72171d61d40b7a3a1689f3e591823&url=https%3a%2f%2fcoinpedia.org%2fstock-market-news%2fmicrosoft-stock-has-more-than-an-outage-to-worry-about-heres-why%2f&c=13518510109905468637&mkt=en-us)  
  <sub>Coinpedia, 10h ago</sub>  
  Microsoft stock has another problem beyond its latest global outage. While the disruption to Outlook, Teams and Copilot has put cloud reliability under ...
- [Cerebras Stock Surges After Microsoft Deal. Can The AI Chipmaker Sustain Its Growth?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af72171d61d40b7a3a1689f3e591823&url=https%3a%2f%2ffinance.yahoo.com%2ftechnology%2fai%2farticles%2fcerebras-stock-surges-microsoft-deal-135658584.html&c=7600303233072826541&mkt=en-us)  
  <sub>Yahoo Finance, 9h ago</sub>  
  With $26.1 billion in future revenue commitments, Cerebras faces mounting pressure to expand computing capacity, overcome data center shortages and turn soaring demand into profits.
- [Not Apple. Not Microsoft. This "Magnificent Seven" Stock Is My Top Tech Buy for 2027.](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af72171d61d40b7a3a1689f3e591823&url=https%3a%2f%2fwww.fool.com%2finvesting%2f2026%2f11%2f13%2fnot-apple-microsoft-magnificent-7-stock-buy-goog%2f&c=11083641797064510178&mkt=en-us)  
  <sub>The Motley Fool, 9h ago</sub>  
  Alphabet is spending up to $205 billion this year to expand its AI infrastructure. The spending is already paying off, with Google Cloud revenue surging 103% in the third quarter and operating income ...
- [CrowdStrike and Palo Alto Networks Climb 3% as Microsoft Outage Disrupts Outlook and Teams](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af72171d61d40b7a3a1689f3e591823&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2fcrowdstrike-palo-alto-networks-climb-141240301.html&c=5753541108573508902&mkt=en-us)  
  <sub>Yahoo Finance, 8h ago</sub>  
  An outage at Microsoft (NASDAQ:MSFT) is pushing buyers toward the biggest independent names in cybersecurity. CrowdStrike Holdings (NASDAQ:CRWD) stock is at $237.30 in morning trading, up 3%. That ...
- [What you need to know about Microsoft’s tech crash](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af72171d61d40b7a3a1689f3e591823&url=https%3a%2f%2fwww.yahoo.com%2fnews%2fworld%2farticles%2fknow-microsoft-tech-crash-081700126.html&c=5772931838676127588&mkt=en-us)  
  <sub>Yahoo, 14h ago</sub>  
  Microsoft is grappling with a major global blackout, leaving millions of users unable to access their emails and other programs, including Microsoft 365, Outlook and Teams.
- [Wall Street Breakfast Podcast: Microsoft Still On Hold With IT](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af72171d61d40b7a3a1689f3e591823&url=https%3a%2f%2fseekingalpha.com%2farticle%2f4967750-wall-street-breakfast-podcast-microsoft-still-on-hold-with-it&c=2378818216766213711&mkt=en-us)  
  <sub>Seeking Alpha, 10h ago</sub>  
  Microsoft struggles to restore services as its global outage continues. Anthropic's IPO 6x oversubscribed. Applied Materials beats forecasts.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 520.00 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 529.19 (-1.7%), 50d 518.92 (+0.2%), 200d 441.40 (+17.8%); 50d above 200d
Momentum: RSI(14) 47.3 | MACD 1.708 vs signal 3.782 (histogram -2.074)
Returns: 1d -0.6% | 5d -2.0% | 1m -3.6% | 3m +8.3%
52-week range: 352.83 - 555.80 (now 82.4% of the way up)
Volatility: ATR(14) 14.97 (2.9% of price) | annualised 20d 36.9%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.86T
Valuation: trailing P/E 27.14 | forward P/E 21.49 | P/B 8.21 | PEG 1.54
Profitability: profit margin 41.2% | operating margin 47.1% | ROE 34.2%
Growth (YoY): revenue +18.8% | earnings +32.3%
Balance sheet: debt/equity 28.5% | free cash flow 2.99B
Risk: beta 1.04 | short interest 0.8% of float
Next earnings: 2027-01-27
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 in line
  2026-09-30 in line | 2026-06-30 beat by 10% | 2026-03-31 beat by 3% | 2025-12-31 beat by 3%
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
Ratings: 12 strong buy, 41 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 636.12 (+22.3% vs last close), range 440.00 - 870.00
Recent rating changes:
  - 2026-10-29 Bernstein: main, Outperform -> Outperform
  - 2026-10-29 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-29 Citigroup: main, Buy -> Buy
  - 2026-10-29 DA Davidson: main, Buy -> Buy
  - 2026-10-29 TD Cowen: main, Buy -> Buy
  - 2026-10-29 Scotiabank: main, Sector Outperform -> Sector Outperform
Institutional ownership: 76.5%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.5%), State Street Corporation (4.3%), FMR, LLC (2.7%), Geode Capital Management, LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 518,348 shares in 17 transaction(s) | sold 261,954 shares in 12
Net: +256,394 shares (+4.4% of insider holdings) | insiders hold 6,015,217 shares
Distinct insiders: 0 buying, 4 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-11-10 NUMOTO TAKESHI (Officer): 5,000 shares, 2.65M
  - 2026-11-09 HOOD AMY E (Chief Financial Officer): 7,305 shares, 3.98M
  - 2026-10-13 HOOD AMY E (Chief Financial Officer): 7,305 shares, 3.98M
  - 2026-09-14 HOOD AMY E (Chief Financial Officer): 41,674 shares, 20.76M
(16 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

- [Nvidia stock inches higher as investors continue to weigh Jensen Huang’s departure](https://www.cnbc.com/2026/11/13/nvidia-nvda-stock-jensen-huang-transition.html)  
  <sub>CNBC, 6 hours ago</sub>  
  Jensen Huang resigned as CEO of Nvidia on Thursday after coming under scrutiny for two extramarital affairs. Nvidia shares hovered near the flatline in...
- [Michael Burry Sees A ‘Mechanical Bid’ Under NVDA Stock – Even As He Questions Nvidia’s Succession Plan And Asia Sales](https://finance.yahoo.com/markets/stocks/articles/michael-burry-sees-mechanical-bid-041314501.html)  
  <sub>Yahoo Finance, 10 hours ago</sub>  
  Retail investors bought about $111 million of Nvidia shares in the first 30 minutes, a record opening inflow. Burry backed interim CEO Colette Kress's...
- [How Much Is Nvidia Stock Worth Without Jensen Huang?](https://www.google.com/goto?url=CAESmwEBxCJF13CuCm4Bzgw7sIINIil0Oz1tu8O_nHoVQ6ipyzojljdyKt_FzoILzABCfP0eizIgYmwOvCYJzMChDqLMhBSvSHEX13ieFcFPYKQryNqJIMVjRwxb94bw9eOWaRxHx5l6c3vfVO9YI1JwNTud_LseN6Z-5_py6PXaGKJ9BOQzTH106aOiR8J670psai13K4k2ItvGpxyKiA&gsessionid=5uIFopALbu7DbgDaTOJ0TJE3UZzGT75tOp3h98_guat_L5fsSkQiBQ)  
  <sub>The Motley Fool, 2 hours ago</sub>  
  Nvidia (NVDA -4.34%) has been a surefire winner for investors in recent years. The artificial intelligence (AI) stock soared more than 1,300% from the start...
- [Nvidia Stock Is Still a Buy After CEO Jensen Huang’s Departure](https://www.google.com/goto?url=CAEShAEBxCJF1_Q8LI_MbTn99FHPAVYv_KxJkx2VbWe_9rPpBJ38hTn2t3DeBvG22oC9Vs8NdoCHTv1pfD5c9ScdaEgqAkwf6pfwWjTEFSJmo27zIIFOYXPQRAZt_w4VpcOCx85QPNYLP8z3VXUJjTGyb-pJ8lXAReO5pKKFLNdNrwIjoZ-Rd58&gsessionid=5uIFopALbu7DbgDaTOJ0TJE3UZzGT75tOp3h98_guat_L5fsSkQiBQ)  
  <sub>Barron's, 1 hour ago</sub>  
  When the bad news is all out, when the investigations are all done, and when an inevitable new leader is named, Nvidia · NVDA.
- [Nvidia spurs selloff in technology stocks, but experts warn 'don't panic' with your 401K](https://www.google.com/goto?url=CAESvAEBxCJF12QIFejPb7bB0AflfwXruNGEvoyIqwebqdos3sbX9KjgCIFl0IJxX5Rhi1OAi_KckP0yrDfly6FlysZbY54xl8SAdnXnNYN3tCVXID4Q18UYUXg5WIA6_5dFSj0sY8S9Ulk-NJo52MDWVVy3hFvE2pcEsRWPrb4INmwuCfTft_fpeQNnxtWEUsaccscHCzHCO7RCRUFu_DF-nrFg8hcs_lyRbIY9e71H09kMPi0_RI78o2mrhqh_6A&gsessionid=5uIFopALbu7DbgDaTOJ0TJE3UZzGT75tOp3h98_guat_L5fsSkQiBQ)  
  <sub>WGBH, 17 hours ago</sub>  
  Nvidia's stock value tumbled on Wall Street Thursday after CEO Jensen Huang resigned following news of his affairs with an alleged Chinese spy and a company...
- [Why was NVDA stock up? Nvidia slid 4.3% on Thursday · CapitalSnitch](https://www.google.com/goto?url=CAESVAHEIkXX-d9F3LWY05JLED0FAJ4461wxQ3wf6_ZigZSlKMzqk1dggc40Xd-4BcJtWMSzx0s9MmIpWjTReR9wwpvUdUluk36S4OezWYf-_aSJEFIBZQ&gsessionid=5uIFopALbu7DbgDaTOJ0TJE3UZzGT75tOp3h98_guat_L5fsSkQiBQ)  
  <sub>Howl.Link, 12 hours ago</sub>  
  NVDA is down 13.2% over five trading days, closing at $173.73 on Nov. 11, 2026. Its closest peers averaged a 3.1% gain over the same days. That makes the…
- [What Jensen Huang’s Exit Means For Nvidia And Investors](https://www.google.com/goto?url=CAESqAEBxCJF1zVMiZ9Z238TEI0MhnnpzV8FPfp4d1vBPT2Url5V7bWnt0VXydL0Xr7pdlQTFJofoSGg70cRc0Tn2dm4xyrpKy2xsDN7BdaUNfe3DCic3X0jz-UJ5s7zwYcXQMc8MdJEcVf_uUAnnGW6IUR2v9bvRbkWG7o-8V3sopznd5LmrRkoo2kGdoIencueyNIbObB1Oec52DqL79btC7Suzx5BlYWlIWY&gsessionid=5uIFopALbu7DbgDaTOJ0TJE3UZzGT75tOp3h98_guat_L5fsSkQiBQ)  
  <sub>Forbes, 19 hours ago</sub>  
  Jensen Huang's exit as Nvidia CEO raises questions about succession, Nvidia stock and the AI boom. Here's what investors should watch next.
- [NVIDIA Corporation (NVDA) stock price, news, quote and history](https://www.google.com/goto?url=CAESZQHEIkXXRHZbvpqGpmLMkrOhoyBV8BTnNRXTrQjsGgCDDd30_AizNFFTdNaxVUhzslC0AT9eElmfY2S0MvNY6qxuiGcaWL46qxSYfD8hKcs9CFxT6UpdFZ9aXRgTNz5wnN2qGTq0&gsessionid=5uIFopALbu7DbgDaTOJ0TJE3UZzGT75tOp3h98_guat_L5fsSkQiBQ)  
  <sub>Yahoo Finance UK, 17 hours ago</sub>  
  379,762.87% · Previous close 173.73 · Open 150.99 · Bid 165.32 x 100 · Ask 169.98 x 300 · Day's range 148.80 - 167.14 · 52-week range 148.80 - 243.37 · Volume...
- [Is Nvidia Stock a Buy Right Now?](https://www.google.com/goto?url=CAEShwEBxCJF18fjvigvNVkhaTv1miP2AueL9rGrtJAOOlad9HVVoJRHrXmtJyAziiDoQbDn73ewmms_eRJ6lhzqd7YyFEtP-gyxyD9cm4H8hmuBOSAEdmdPCuAy3o6cYCOxyQCoGk1ZZ4GoMmNAzD4VTGSTZG6DzDR5a0tjqBufEQKruvN_BJ68MMM&gsessionid=5uIFopALbu7DbgDaTOJ0TJE3UZzGT75tOp3h98_guat_L5fsSkQiBQ)  
  <sub>The Motley Fool, 57 minutes ago</sub>  
  Shares of Nvidia (NVDA -4.34%) were battered this week by news that the company's CEO, Jensen Huang, resigned. He departed the business he co-founded after...
- [NVDA Stock Price Forecast — Top Analysts Give Multiple Downgrades Ahead of November 17 Earnings amid CEO Jensen Huang Fiasco](https://www.google.com/goto?url=CAESmwEBxCJF12skBAuaAXvDWftmhc_B3flptqjmdCtrpTYhSI8Z8TyMxAA75KTAynuNgfMl8hgCJhNvl3Q4VeCXnFOkYNVnUQixVIvrLmCcWsRfLZWrBXb99_T1SRgK2Mo7I-yElUMPipOxhR0FTq0zfB98ktJJRLtRNMoR1YmBIDiXQ0MRYUGfNS9wlG8xkfQtpXzUj62zzR7ZQbNGMw&gsessionid=5uIFopALbu7DbgDaTOJ0TJE3UZzGT75tOp3h98_guat_L5fsSkQiBQ)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Nvidia (NVDA) stock fell over 7% in Thursday's pre-market session. The decline came after a 2.87% gain during regular hours, as reports about CEO Jensen...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 163.32 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 198.71 (-17.8%), 50d 214.66 (-23.9%), 200d 204.19 (-20.0%); 50d above 200d
Momentum: RSI(14) 25.0 | MACD -14.194 vs signal -10.102 (histogram -4.091)
Returns: 1d -1.7% | 5d -12.5% | 1m -24.8% | 3m -27.4%
52-week range: 163.32 - 239.24 (now 0.0% of the way up)
Volatility: ATR(14) 9.67 (5.9% of price) | annualised 20d 52.7%
Volume: 0.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 3.94T
Valuation: trailing P/E 20.65 | forward P/E 10.30 | P/B 17.22 | PEG 0.21
Profitability: profit margin 63.7% | operating margin 65.2% | ROE 117.2%
Growth (YoY): revenue +105.9% | earnings +127.8%
Balance sheet: debt/equity 17.0% | free cash flow 41.81B
Risk: beta 2.25 | short interest 1.2% of float
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
Consensus: buy (mean 1.59 on a 1=strong buy to 5=strong sell scale, 53 analysts)
Ratings: 10 strong buy, 38 buy, 13 hold, 0 sell, 0 strong sell
Price target: mean 285.35 (+74.7% vs last close), range 174.00 - 515.00
Recent rating changes:
  - 2026-11-12 Melius Research: down, Buy -> Hold
  - 2026-11-12 DA Davidson: main, Buy -> Buy
  - 2026-11-12 Craig-Hallum: down, Buy -> Hold
  - 2026-11-12 B of A Securities: main, Buy -> Buy
  - 2026-11-12 BMO Capital: main, Outperform -> Outperform
  - 2026-11-12 Baird: reit, Neutral -> Neutral
Institutional ownership: 71.3%
Largest holders: Blackrock Inc. (8.1%), Vanguard Capital Management LLC (6.4%), State Street Corporation (4.2%), FMR, LLC (3.9%), Geode Capital Management, LLC (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 2,613,243 shares in 18 transaction(s) | sold 6,198,325 shares in 9
Net: -3,585,082 shares (-0.4% of insider holdings) | insiders hold 965,445,952 shares
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

<details><summary><b>News</b> — score n/a</summary>

- [NVO Nov 2026 39.500 call (NVO261113C00039500) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/NVO261113C00039500/chart/)  
  <sub>Yahoo! Finance Canada, 13 hours ago</sub>  
  Interactive Chart for NVO Nov 2026 39.500 call (NVO261113C00039500), analyze all the data with a huge range of indicators.
- [Novo Nordisk faces new weight-loss drug competitor in China: Can NVO avoid deeper losses?](https://tradersunion.com/news/stocks/show/4226251-novo-nordisk-slides-1-06percent-to/)  
  <sub>Traders Union, 7 hours ago</sub>  
  Novo Nordisk trades at $40.65 after dropping 1.06% today, as competition intensifies in China's weight-loss market.
- [Prediction: $10,000 Invested in Viking Therapeutics Before Its Oral Phase 3 Readouts Could Be Worth This Much by 2028](https://www.google.com/goto?url=CAEShwIBxCJF10FxMiuxfaA0KgXEDILcJmy9WwccpbRiCR7qRMCnQEBIvwvR9FKV7SeNkzZGqnN4860CSolT7F9wMDep4f8L_P-2Y-kaHU7Ykbh1d8y7R6PIf3-1LJ9BPaYPZ3QyzU6NAQBLwnpbnsuUBPubCFlL8xNN-S9lalGUKKA4KVi4rEivThdBGlI63Um7powTtzZBQ70gk0AfDF00ppQkOlYhQpl3UOxwuvPF0GoRF3RZzlijGymJyGiA395DKsQzqTbOUVgqs08BbWYC-qMaIXM4Fvd5QSJpD0vfe-1x8_U2l0h7IKiU94Ekd_k4okUbFKPDlXaFCfpNbNJO7Je8AKW44i_5Cg&gsessionid=ZhUt23DwfeoNquGNKCNNIuBLn_A1JBZFLqLXgqqKnlKNn2h3CRO2zw)  
  <sub>The Globe and Mail, 5 hours ago</sub>  
  Detailed price information for Novo Nordisk A/S ADR (NVO-N) from The Globe and Mail including charting and trades.
- [Novo Nordisk (NYSE:NVO) Share Price | RNS News, Quotes, & Charts | NVO |](https://www.google.com/goto?url=CAESfAHEIkXX2OHnSVSPxb79fYHBAh6xzzR_ovTCk8pu1FWd1fXrE493kYnNChZpMMIFT6HTThUCq9acah4JUTJUgSrb9Vx1zIUslY2WqpezgDY8pZe16Qtqp-Unun98qWzXjb9tXbWk7q8-xiHRMDQMC90st_DQFk3MruhinHM&gsessionid=ZhUt23DwfeoNquGNKCNNIuBLn_A1JBZFLqLXgqqKnlKNn2h3CRO2zw)  
  <sub>Proactive financial news, 22 hours ago</sub>  
  Novo Nordisk (NYSE:NVO) Share Price and News. Novo Nordisk is a global healthcare company with 90 years of innovation and leadership in diabetes care....
- [Novo Nordisk's (NYSE: NVO) 70% Stock Decline Creates Value Case As Wegovy Pill Crosses 8 Million Prescriptions](https://www.google.com/goto?url=CAES2AEBxCJF1-4oTcnPFkd3pugoPQC50AdJHUXJVlrrVE1FebLGPpZUbqYzXk9jglkoYzxCdtp5rzTF8f3uaGEG5DLBMAYJrZBk_A5z8q0Os2tIyUDuSA9huU_VYTjLK60wIeoxQCda5DStmDCL3a3yOlcC5ratJ4KRfvzAwyM4AYhP_1sTzLnwetqAQ6Ev7JR6MdBat6staMf5nSKv2eoRNK9_I88STMwiNWJl7f5vaG1Ow7pNfqWbUmEWoKgOiMkej_rpcvYhy8msU-RDRvqm2aUV_CAvT2SKPSo&gsessionid=ZhUt23DwfeoNquGNKCNNIuBLn_A1JBZFLqLXgqqKnlKNn2h3CRO2zw)  
  <sub>Foreign Policy Journal, 23 hours ago</sub>  
  Shares of Novo Nordisk (NYSE: NVO) have shed roughly 70% of their value since a 2024 peak, drawing fresh attention from income and value-oriented investors.
- [(NVO) Risk Channels and Responsive Allocation](https://www.google.com/goto?url=CAEStwEBxCJF14rvLtyq_GS8EbHot9IZKQasp5s8mKS5r8MA-eHr2wYAjuCdRmcq85O4OQYYeZ5vSvroC7gFzejswWbWCOLnOWwS3Uwuqf9STh4OSMcOOTVknguNSZ54tl6PfnYxgWDHREp6BMNty_sC28gCU_AIn3cGL9ruS8CEUoEedOD4gt702bvoGzGMz4nFKK_f_iXCZfZDCYAqfGjCBYVnwsLRbzmHohk5XpwsKsDrLQ1OE4kzlv0&gsessionid=ZhUt23DwfeoNquGNKCNNIuBLn_A1JBZFLqLXgqqKnlKNn2h3CRO2zw)  
  <sub>Stock Traders Daily, 19 hours ago</sub>  
  Key findings for Novo Nordisk A/s (NYSE: NVO). Mixed Sentiment Alignment Points to Choppiness Across Horizons; Resistance is being tested.
- [NVO 6-K & SEC Filings - Yahoo Finance](https://www.google.com/goto?url=CAEShAEBxCJF1xc2G8j5LDO0pD42P_Y20wHf7-EDBEgBlE6a4027fbgIdPqHigFg4GHUpw0GGIB-eUbjBgQ9z05cxd4kcJhtNmNTCh5m2u9M_gEPa9DVi8ZFyTaoOThTzRWJkAVV7BLHBMs7actqVN20MsILXn2CkAo3HCALooFpnUFCfs4aqfs&gsessionid=ZhUt23DwfeoNquGNKCNNIuBLn_A1JBZFLqLXgqqKnlKNn2h3CRO2zw)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  NVO 6-K and SEC filings offer investors the in-depth insights and information you've come to expect from Yahoo Finance.
- [NVO Nov 2026 47.000 put (NVO261113P00047000) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXew09qqhnLg3Zcr0pdxCc5-Gz5uGkWHyEc_gHX2LeTsNcS-v2nIhmyS05PNFsKWNeHvh2U5PlnMJ5-9Mc96CwFfkMacYJlrx_PvVD4xOL0EG3MRJHV-gOntn5buW8K-g0u7nWk6mtMU3roZBZtD7XrkhVrhM&gsessionid=ZhUt23DwfeoNquGNKCNNIuBLn_A1JBZFLqLXgqqKnlKNn2h3CRO2zw)  
  <sub>Yahoo Finance UK, 22 hours ago</sub>  
  Interactive chart for NVO Nov 2026 47.000 put (NVO261113P00047000) – analyse all of the data with a huge range of indicators.
- [NVO Dec 2026 37.000 put (NVO261204P00037000) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXXL2EvL0rPDnfGkqf33fWkvr0PBtj-2ijQ1LYv5hM4qIF0g2odijgN_Imw2enSqJW37knlwgUSQ1uwo5UfTWy9dDfn7Y6Eun4_LdvBDM9SvIu0OWTJwMadFuJDdGsbdQ9bd8cQStGVAjxL1D6xAVe2HW3VOw&gsessionid=ZhUt23DwfeoNquGNKCNNIuBLn_A1JBZFLqLXgqqKnlKNn2h3CRO2zw)  
  <sub>Yahoo Finance UK, 23 hours ago</sub>  
  Interactive chart for NVO Dec 2026 37.000 put (NVO261204P00037000) – analyse all of the data with a huge range of indicators.
- [Novo Nordisk (NVO) Stock Price Prediction: BMO’s higher target meets a mixed technical tape](https://www.google.com/goto?url=CAESogEBxCJF10iBhw3_aR5WGnWRdXwarKUG2ou_fTNHJTcZ_zycFRX93e4AJNHWMasRhswViKBq8JVzQKeYfHZJFG__umGau6-7XQXG-P1jdnu1y19y25E_5_lX4ityDOMBa8-opWZ8OB4L3hjNEAaWhexmJXzQs4F_PzZdHoxjs0WqoYCM1iZXOB08yl3N9TinUZP3DUcdEdKY6TVlCOLCfySDi94&gsessionid=ZhUt23DwfeoNquGNKCNNIuBLn_A1JBZFLqLXgqqKnlKNn2h3CRO2zw)  
  <sub>Blockchain News, 15 hours ago</sub>  
  Novo Nordisk (NVO) is trading at $41.30, above its short- and medium-term moving averages, while BMO Capital Markets lifted its target to $44 and kept a...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 40.81 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 39.93 (+2.2%), 50d 40.07 (+1.8%), 200d 43.18 (-5.5%); 50d below 200d
Momentum: RSI(14) 54.0 | MACD 0.320 vs signal 0.135 (histogram 0.185)
Returns: 1d +0.4% | 5d +1.2% | 1m +4.1% | 3m -9.1%
52-week range: 35.29 - 63.98 (now 19.2% of the way up)
Volatility: ATR(14) 1.02 (2.5% of price) | annualised 20d 32.2%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 179.90B
Valuation: trailing P/E 10.31 | forward P/E 11.95 | P/B 5.50 | PEG 4.21
Profitability: profit margin 33.9% | operating margin 50.8% | ROE 58.4%
Growth (YoY): revenue +5.6% | earnings -15.8%
Balance sheet: debt/equity 61.7% | free cash flow 32.75B
Risk: beta 0.37 | short interest 1.2% of float
Next earnings: 2027-02-03
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 1 beat, 1 in line, 2 missed
  2026-09-30 missed by 22% | 2026-06-30 missed by 6% | 2026-03-31 beat by 23% | 2025-12-31 in line
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
Price target: mean 45.60 (+11.7% vs last close), range 39.65 - 64.44
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
Net: +0 shares | insiders hold 132,277 shares
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

- [Procter & Gamble vs. Starbucks: Which Stock Is a Better Buy for 2027?](https://finance.yahoo.com/markets/stocks/articles/procter-gamble-vs-starbucks-stock-232139800.html)  
  <sub>Yahoo Finance, 15 hours ago</sub>  
  Choosing between Procter & Gamble (NYSE:PG) and Starbucks (NASDAQ:SBUX) requires balancing the steady reliability of essential household goods against the...
- [Procter & Gamble Has Raised Its Dividend for 70 Straight Years. Where's the Price Target Now?](https://247wallst.com/investing/2026/11/13/procter-gamble-has-raised-its-dividend-for-70-straight-years-wheres-the-price-target-now/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Procter & Gamble (PG) earns a BUY and a $184 price target, about 10% upside, after an earnings beat lifted shares near their 52-week high.
- [Procter & Gamble Company (The) $PG Stock Sold by Russell Investments Group Ltd.](https://www.google.com/goto?url=CAESxAEBxCJF1xc96ZlAtdfLA1vPm3YCdVYIKbMoH-O_S9nvss9E97jd5foUZz4kOvyF1L88XlK0MfJHXjWsekCyYUto6QdJjGHf-TYAK4Sbkz9z9BYzFdNlwo_bqxZQiz7avBeIJDKTWHrdHfebaRGsjD3tudA7uh0DQBtPqq-wWn1KGAxs72A7sDXw6WT8NgtZDy8Jz1c7Oo8X7eoq6A60c0pmX8Ootc2I3duK1WROJEJ7r9_f6b-CLeK3_aHwUWmbv4-TII4V&gsessionid=WeP1I1iJAgaa8oZJ_wG-5bMrDoXPHTzGfwEU-y_rBtiVm4B0UlVCAw)  
  <sub>MarketBeat, 4 hours ago</sub>  
  Russell Investments Group Ltd. cut its holdings in shares of Procter & Gamble Company (The) (NYSE:PG - Free Report) by 20.2% during the third quarter,...
- [PG Nov 2026 133.000 put (PG261113P00133000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScgHEIkXXQG9Y8arf-1ngiXXore_kBOGSIiyuqOZxn83ltZwG9Gd47yPzthA6Jlh_5G8Jad2YEJ8rDfXt5ikEkCtMLvA5pWWmyGRinxK-aBA72Snb_GO9TnumrDhxsv8npswMPeQ8AgOAc7fBJLNeUoeWEg&gsessionid=WeP1I1iJAgaa8oZJ_wG-5bMrDoXPHTzGfwEU-y_rBtiVm4B0UlVCAw)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  Find the latest PG Nov 2026 133.000 put (PG261113P00133000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Procter & Gamble Company (The) $PG Stock Bought by Fisher Asset Management LLC](https://www.google.com/goto?url=CAESxAEBxCJF17UPg61VdykyswzSLybRr-AD_aQjBmwyB8RpnDmwP0xSQeIKmmecIgkQbCnEz-E1zK8cCiYgawBvYRDlp8qnmCgReh930QFkym7m4rIXYVUt1uMfe5-U-gZdNVO3IKIVcqOqd1spoO_FGo63OFc_EsBC49dcN69Tz07J6G74dSOKJL3ZuZ6GGK_cSdxLj-J2N-UMbw5L4zJj75rKl9hELMPqxGCxRCpXR0AJubpDFb9u8dkEp4nwkQdJcuL8mOEA&gsessionid=WeP1I1iJAgaa8oZJ_wG-5bMrDoXPHTzGfwEU-y_rBtiVm4B0UlVCAw)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Fisher Asset Management LLC lifted its stake in shares of Procter & Gamble Company (The) (NYSE:PG - Free Report) by 7.5% in the 3rd quarter, according to...
- [PG Nov 2026 170.000 call (PG261113C00170000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScgHEIkXXs1T08bjWDV-85U9jDoFquKx6jzRwJknOPVrqPmojR0hjCfzeygmnjjv1iEIAk2_BBScmpqAE6ApBzaiElxZ10RKvlV32QDjRFehjj3-fpSC9-XtpJr1549pqsV_eFWUEH1sLhSsImVjXsrOrTQ&gsessionid=WeP1I1iJAgaa8oZJ_wG-5bMrDoXPHTzGfwEU-y_rBtiVm4B0UlVCAw)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  Find the latest PG Nov 2026 170.000 call (PG261113C00170000) stock quote, history, news and other vital information to help you with your stock trading and...
- [PG Nov 2026 139.000 put (PG261113P00139000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScgHEIkXXAp7xo09hmfB5knk2Dqd0RMpk3rKKxpdf0ojKAaBhSgmBbdcclz6c27Jd9qI85HRRJcWKax2HdM7ml2yKaVZevS4CTRr54M7op7rOz7UaMMHArkZ7w3PNCecHZyNexr_u6m9fJhIFNJTrT_hPHQ&gsessionid=WeP1I1iJAgaa8oZJ_wG-5bMrDoXPHTzGfwEU-y_rBtiVm4B0UlVCAw)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Find the latest PG Nov 2026 139.000 put (PG261113P00139000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Insider Selling: Procter & Gamble (NYSE:PG) CEO Sells $379,057.50 in Stock](https://www.google.com/goto?url=CAESvgEBxCJF1zSBZ_8J7sWpzzPNbUH80kqtxDcTFWrU0Ccoq3m8x0DqidHGbGfiCZW7fI84VobOhvPo-ALMYZnZTWxU0rZhMk7LzXPDmewa8Je3xx-eZT4kqK6nvBfI1AO8abnbRR0DPMSc2OxWQ0DWqDTBHUkuGsOrHPl8BimcqSLktlr7sgi3PX9NYe5GO87JIUPGansu2Mx3uV6HWQ0D7l0XPwGeZ-Fn9vg2PkG_vi3GCN-nHAm1SYsLmhD5u9Hu&gsessionid=WeP1I1iJAgaa8oZJ_wG-5bMrDoXPHTzGfwEU-y_rBtiVm4B0UlVCAw)  
  <sub>MarketBeat, 14 hours ago</sub>  
  Procter & Gamble Company (The) (NYSE:PG - Get Free Report) CEO El Hak Hesham Abd sold 2250 shares of the firm's stock in a transaction on Thursday,...
- [Procter & Gamble (PG) executive sells at $168.47, retaining 8,968 shares directly.](https://www.google.com/goto?url=CAESqgEBxCJF12fGuFbLokFGJOHmlphuV2fYyy4FN3Cq4W6eOSD-uDo1YEBXYPEh-ccII-iTHNt0TgsaCUeWwndbZfOg8FA8mxf3_mhCqiIcg3DY8MPR7GgKJsirIffRCDnkJqGA3KZpDBw284Qz3m287Lmut0_fXaNtA6e9Gl0jj8RhYMhs6_736XDme4KCKDrx1k40W1C0Bfx40UCMQuMz__6pI4JdkTdCSJXSwg&gsessionid=WeP1I1iJAgaa8oZJ_wG-5bMrDoXPHTzGfwEU-y_rBtiVm4B0UlVCAw)  
  <sub>Stock Titan, 17 hours ago</sub>  
  Baby and Feminine Care CEO El Hak Hesham Abd sold on November 12, 2026. No trading plan was reported; he held 1542 shares through a retirement trustee.
- [Fifty families can win $1,500 toward baby essentials by adding Pampers to a registry.](https://www.google.com/goto?url=CAESrQEBxCJF1-gqL-dHAoLMif3HjkX0f-yPTTk56OGxytC56d1ZQwTUeFXgmTF8isaiAPpElv_227JUhwCB0UfseJfAJ-myMEotT_kzVlQRey2OQYOghPd3u8-Hmfb_CNB6xLvfXqEMI8jJdGLah8cSCbfwoFYzQktfzvaojvTSm_47_Bg0m10pSGce5oRkMPVMtzIlzEO4NLOcYtDLjvUMP3rZGgVnaFJCeU_FQCRsWw&gsessionid=WeP1I1iJAgaa8oZJ_wG-5bMrDoXPHTzGfwEU-y_rBtiVm4B0UlVCAw)  
  <sub>Stock Titan, 22 hours ago</sub>  
  Dancer and expectant mother Witney Carson joins Pampers; eligible U.S. adults with a Pampers registry item can enter on Instagram, TikTok or by email...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 169.19 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 163.37 (+3.6%), 50d 154.25 (+9.7%), 200d 149.87 (+12.9%); 50d above 200d
Momentum: RSI(14) 67.4 | MACD 4.180 vs signal 4.021 (histogram 0.159)
Returns: 1d +0.7% | 5d +2.3% | 1m +7.7% | 3m +18.2%
52-week range: 138.04 - 169.19 (now 100.0% of the way up)
Volatility: ATR(14) 3.11 (1.8% of price) | annualised 20d 28.9%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 392.15B
Valuation: trailing P/E 25.48 | forward P/E 22.87 | P/B 7.22 | PEG 4.31
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
Price target: mean 174.04 (+2.9% vs last close), range 151.00 - 190.00
Recent rating changes:
  - 2026-10-26 Barclays: main, Equal-Weight -> Equal-Weight
  - 2026-10-26 Piper Sandler: main, Neutral -> Neutral
  - 2026-10-23 Freedom Broker: up, Hold -> Buy
  - 2026-10-23 UBS: main, Buy -> Buy
  - 2026-10-23 Citigroup: main, Buy -> Buy
  - 2026-10-23 BNP Paribas: main, Outperform -> Outperform
Institutional ownership: 71.7%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.4%), Geode Capital Management, LLC (2.9%), Vanguard Portfolio Management LLC (2.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 322,138 shares in 48 transaction(s) | sold 233,622 shares in 27
Net: +88,516 shares (+4.1% of insider holdings) | insiders hold 2,271,427 shares
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

### Teva Pharmaceutical (TEVA) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [H.C. Wainwright reiterates Teva Pharma stock rating on pipeline outlook By Investing.com](https://ng.investing.com/news/stock-market-news/hc-wainwright-reiterates-teva-pharma-stock-rating-on-pipeline-outlook-93CH-2802279)  
  <sub>Investing.com Nigeria, 20 hours ago</sub>  
  Investing.com - H.C. Wainwright reiterated a Buy rating and $54.00 price target on Teva Pharmaceutical Industries (NYSE:TEVA). The stock currently trades at...
- [Teva Pharmaceutical Industries(TEVA.US) Officer Sells US$10.56 Million in Common Stock](https://www.moomoo.com/news/post/1004492565/teva-pharmaceutical-industries-tevaus-officer-sells-us-10-56-million)  
  <sub>Moomoo, 12 hours ago</sub>  
  TevaPharmaceutical Industries(TEVA.US)$ Officer Francis Richard D sold 250K shares of common stock on Nov 10, 2026 at an average price of $42.2367 for a...
- [Teva Pharmaceutical Industries (NYSE:TEVA) Stock: Insider Richard Daniell Sells 20,003 Shares](https://www.google.com/goto?url=CAES1QEBxCJF1wscdD0gO9aWSwj7sgKQNa40BIOtntXoOnkFgtm7lttkPwD5FdDRfP3rCXhYzZ6TnE1eVlrqorZlnjngVhhvLPL5ae4rFl6JZzulde4eMm8ev-6WWIo4ov5B3anGHieQvW2wDCAeXE9KPLUDyl4e3dkUyJjaVo7N7q8oKCjXXGgpkgVXSahzmhmwFvoF6sM7X6lBJkq7kD74NPpzoXLBTDpimayqkY7ZUZ55aAuFkDj13BrrQVboe6bygsuGil1ET2v11uzkUxDUt8nkE_HMRz8&gsessionid=p4E-Bel-zd2q5sgBndzvf9awA1rXNYXOmBfO0a4tKq-CdCswevwQQA)  
  <sub>MarketBeat, 16 hours ago</sub>  
  Teva Pharmaceutical Industries Ltd. (NYSE:TEVA - Get Free Report) EVP Richard Daniell sold 20003 shares of the business's stock in a transaction on...
- [Does First R And D Day Change The Bull Case For Teva (TEVA)?](https://www.google.com/goto?url=CAES3QEBxCJF19jB35BVhKa7YjfT7JJ-xyyXDDBzjqOiv1fMAl7b9gPW_l2ryFEdmaITRlWDCaPRPpSA_g0F0CANyzITUgtGPMCzGtl2-aU6DrjGcD9YHw7iRN2YrhH9F9P40I7f2MWRGOc_rpydabRvr_avTIQpc5PMCwcG2S8GANWx-VUQPD8wWb_7Pgb1z-PPCD1hJft6bsWBDgzyzMk1FzQFyHoPgRzxU0s5zMyDEpZiTmGcegQtz4cnhJywtU954zA1mIfVAW6eT9CIZ1jJNQJMloBajBv6ygzwjma6iw&gsessionid=p4E-Bel-zd2q5sgBndzvf9awA1rXNYXOmBfO0a4tKq-CdCswevwQQA)  
  <sub>Simply Wall St, 9 hours ago</sub>  
  Teva Pharmaceutical Industries used its first R&D Day to outline a shift toward higher value medicines, highlight progress across late stage and early stage...
- [A director’s 3,326-unit stock grant at Teva (TEVA) vests November 10, 2027.](https://www.google.com/goto?url=CAESvgEBxCJF12byEhfN2h-kbDvM8p08cyCjHh40ZZSL3T7flDSM7QQZJPIUHCxnZf3PTna5lMPQILgKHP8qUaGLF_PHBN2PULo2OsLmzHUC0WFGbjX0lC6Q9saTDuMA4SnbhuqFOxrEKXtJqQcS6qriNRM1_t5vy6rCvXm-njPbVO_nNLwaTO-lJ4Ex0Z6XMOEIonW6OSbFr51RwYj7AchsegW9sZNGR96LOiQfq3Re3v16GQJdTzsrLkvF_e5lySmi&gsessionid=p4E-Bel-zd2q5sgBndzvf9awA1rXNYXOmBfO0a4tKq-CdCswevwQQA)  
  <sub>Stock Titan, 18 hours ago</sub>  
  Granted November 10, 2026, the units can settle in ordinary shares or, at the Human Resources and Compensation Committee's option, their cash value.
- [Teva CEO: We have evolved into a biopharma company](https://www.google.com/goto?url=CAESdgHEIkXXWXsDx4mqnxtKe-qT5DHBdZiIURP44PxNNjLVYFI2kWNHaCBeNrA8kszk4LK1vuy-W8rpufE8WJcHr5qMLQQvQeTfJhxLvA7vRqobCIZo_5mxP3Jw8uLgwmzquvA2GbCoYzdkK0MZKE5fWYWLft200YA&gsessionid=p4E-Bel-zd2q5sgBndzvf9awA1rXNYXOmBfO0a4tKq-CdCswevwQQA)  
  <sub>גלובס, 4 hours ago</sub>  
  Richard Francis sees branded drugs accounting for 25% of revenue in 2030 compared with 9% in 2022.
- [Piper Sandler raises Teva stock price target on pipeline strength](https://www.google.com/goto?url=CAESugEBxCJF13cm05qxoRYXDF4p1mxA-jpLfRd9SdPld7Fhd90OOJXtZXHOSU01TQ1gp0JPg-iMCEX--HddqoJoBs-7WhtDX1dFpqZXmhjqsVgOjZ7r1zmzlLKT6f_1gh3d8NQAPLLrsmqxEQ8MaiI5pAkMUikXMzowH7FcQ10Eh5hQ7kXx5Nk1-lzDGjpcdG7bsOfI_jtNNIv85Jvvsx1ooJl8so2TNF7Qh2nQmVes2Pb4oBMnT2tEGytRrq0&gsessionid=p4E-Bel-zd2q5sgBndzvf9awA1rXNYXOmBfO0a4tKq-CdCswevwQQA)  
  <sub>Investing.com, 24 hours ago</sub>  
  Investing.com - Piper Sandler raised its price target on Teva Pharmaceutical Industries shares to $56 from $44 while maintaining an Overweight rating on the...
- [Insider Selling: Teva Pharmaceutical Industries (NYSE:TEVA) CEO Sells $10,560,000.00 in Stock](https://www.google.com/goto?url=CAES0gEBxCJF1x01GOgB4_JIb9xTLa7vhJldO6b8YpF__L9CErOhxTeZYPRp2SpcpHqk21Y1BsiiFguIQfJUm4btJN9EWKsAj6RJBSm9HTx_J--fUwSbZAdTmPlC0En2MQdkk2DE-gYqrlTaY9QkvlUm2xwU4w5sArHayGK1Vp5otcITLRYy6FUj9X-hY5YIkWh-qhTH0aMafUQ0m2Zflc1bYYeSCrSWQxCwWT0sJa_WupPr_Fs4Y0--TpCOjVF_gcD6XQRTxjtc0VrQMUgl9BD3GiUG7SQ&gsessionid=p4E-Bel-zd2q5sgBndzvf9awA1rXNYXOmBfO0a4tKq-CdCswevwQQA)  
  <sub>MarketBeat, 16 hours ago</sub>  
  Teva Pharmaceutical Industries Ltd. (NYSE:TEVA - Get Free Report) CEO Richard Francis sold 250000 shares of the stock in a transaction on Tuesday,...
- [How Could Teva Pharmaceutical (NYSE:TEVA) Transform Its Growth Story?](https://www.google.com/goto?url=CAESrAEBxCJF1wbBOqx1Dl77Aays5I0SCcC0V6f6UdWNQVLJakkRs4YHJa78OW_vSA7q1h3ft-Po4-Wk5kuabSMsWM2nNlgHUIudtC-kNirPyv2ByhRtv8K5_vNxRtfIhm2NI5BkmHkDmP_VSyYW6sYDrhYHVUVsIswTf8wsWly3qMA904lP55OG1GKOBc_QX9x7GYDrsL1nJDQDf-7kG_GvQw6Pr_TGOEO5f7FzK67z&gsessionid=p4E-Bel-zd2q5sgBndzvf9awA1rXNYXOmBfO0a4tKq-CdCswevwQQA)  
  <sub>Kalkine Media, 21 hours ago</sub>  
  Teva (NYSE:TEVA) reaches a yearly high after a raised price objective, with its innovative medicines pipeline and quarterly beat in focus.
- [Jefferies reiterates Teva Pharma stock rating citing pipeline progress By Investing.com](https://www.google.com/goto?url=CAESwQEBxCJF1wLT8ryBziITBEJ8vU1CGIM_IcGcLImjK0MeZobDYeIRe8aq2btKM8lFRxC71UlmzHJMk9-By87SXCcrEMfKpQkmnm5JGyYHNapER2sNvOAVszMxqfXOwl_WNWXWx9aX6JzV8ACOZZ1Vgp9pokpp5pCzbre7EaLfRkZwD8-coHTzIAb9ffF90D4C7UaCt6OBvJu4MLGCJIiZhDI0_rnDuLXd-Api8bje0W2DWfE79m_9yzVNm8Aslw0jeOUK&gsessionid=p4E-Bel-zd2q5sgBndzvf9awA1rXNYXOmBfO0a4tKq-CdCswevwQQA)  
  <sub>Investing.com Nigeria, 21 hours ago</sub>  
  Investing.com - Jefferies reiterated a Buy rating and $48.00 price target on Teva Pharmaceutical Industries (NYSE:TEVA) following the company's research and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 43.65 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 41.55 (+5.0%), 50d 40.17 (+8.7%), 200d 35.10 (+24.4%); 50d above 200d
Momentum: RSI(14) 65.7 | MACD 0.947 vs signal 0.774 (histogram 0.172)
Returns: 1d -0.0% | 5d +2.4% | 1m +6.2% | 3m +19.7%
52-week range: 24.21 - 43.65 (now 100.0% of the way up)
Volatility: ATR(14) 1.16 (2.7% of price) | annualised 20d 27.5%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 50.93B
Valuation: trailing P/E 101.50 | forward P/E 13.96 | P/B 6.38 | PEG 1.05
Profitability: profit margin 2.9% | operating margin 19.8% | ROE 6.7%
Growth (YoY): revenue -1.9% | earnings -46.0%
Balance sheet: debt/equity 212.9% | free cash flow 1.49B
Risk: beta 0.84 | short interest 2.4% of float
Next earnings: 2027-01-27
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-09-30 beat by 15% | 2026-06-30 missed by 92% | 2026-03-31 beat by 9% | 2025-12-31 beat by 39%
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
Consensus: buy (mean 1.53 on a 1=strong buy to 5=strong sell scale, 14 analysts)
Ratings: 4 strong buy, 9 buy, 2 hold, 0 sell, 0 strong sell
Price target: mean 49.44 (+13.3% vs last close), range 42.12 - 57.00
Recent rating changes:
  - 2026-11-12 Piper Sandler: main, Overweight -> Overweight
  - 2026-11-05 Leerink Partners: main, Outperform -> Outperform
  - 2026-11-04 TD Cowen: main, Buy -> Buy
  - 2026-11-04 HC Wainwright & Co.: main, Buy -> Buy
  - 2026-11-02 HC Wainwright & Co.: init, ? -> Buy
  - 2026-10-15 Barclays: main, Overweight -> Overweight
Institutional ownership: 53.3%
Largest holders: Blackrock Inc. (5.5%), Phoenix Financial Ltd. (3.6%), WCM Investment Management, LLC (3.6%), Clal Insurance Enterprises Holdings Ltd (3.6%), Menora Mivtachim Holdings Ltd. (3.4%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 43,476 shares in 3 transaction(s) | sold 29,021 shares in 4
Net: +14,455 shares (+0.3% of insider holdings) | insiders hold 5,635,773 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-11-12 SABAG MARK (Officer): 44,710 shares, 1.97M
  - 2026-11-11 DANIELL RICHARD (Officer): 45,003 shares, 1.93M
  - 2026-11-10 FRANCIS RICHARD D (Chief Executive Officer): 250,000 shares, 10.56M
  - 2026-11-09 WEISS AMIR (Officer): 17,289 shares, 744.05K
(15 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

> No material macro surprise, flat fund flows, no analyst ratings, technicals oversold but low volume, fund fundamentals neutral.

**Main reasons it gave:**
- Flat fund flows: 0.0% change over the past week and month
- No analyst ratings or price targets for the fund's holdings
- RSI 33.4 suggests oversold but volume is only 0.03x the 20‑day average, indicating weak momentum
- Macro yields rose modestly with no surprise; 10‑yr minus 3‑mo spread +1.05 (normal upward slope)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 26.51 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 27.00 (-1.8%), 50d 27.93 (-5.1%), 200d 27.40 (-3.2%); 50d above 200d
Momentum: RSI(14) 33.4 | MACD -0.511 vs signal -0.498 (histogram -0.013)
Returns: 1d +0.8% | 5d +1.6% | 1m -6.2% | 3m -5.8%
52-week range: 25.44 - 29.49 (now 26.5% of the way up)
Volatility: ATR(14) 0.24 (0.9% of price) | annualised 20d 9.0%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Commodities Focused
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 3.4%
Three-year record: +10.5% a year | beta to the market 0.37
Cost and size: expense ratio 0.85% | net assets 1.13B
What it is made of: Other 49.6%, Cash 47.9%, Bonds 2.5%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 40.2%, Invesco Short Term Treasury ETF 5.3%
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
Rolled up from the 2 largest holdings, 45.5% of the fund by weight
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
Shares outstanding: 27.60M | fund size: 731.81M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise or decisive technical break, bullish inflows offset by bearish energy fundamentals.

**Main reasons it gave:**
- Strong inflows (+8.6% share count increase over 1 month) indicating bullish demand
- Energy inventories build (crude +4.7M barrels, natural gas +77 BCF) indicating bearish supply
- EIA price outlook forecasts falling crude and natural gas prices over the next six months
- Technicals show price below 20‑day and 50‑day SMAs, negative MACD, but above 200‑day SMA
- No macro surprise in rates or data; yields modestly up, dollar up, VIX down

<details><summary><b>News</b> — score +0.00</summary>

- [iShares S&P GSCI Commodity-Indexed Trust (GSG) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GSG/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Find the latest iShares S&P GSCI Commodity-Indexed Trust (GSG) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 30.97 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 32.53 (-4.8%), 50d 32.74 (-5.4%), 200d 29.60 (+4.6%); 50d above 200d
Momentum: RSI(14) 32.2 | MACD -0.567 vs signal -0.313 (histogram -0.254)
Returns: 1d +0.2% | 5d -1.8% | 1m -7.0% | 3m +1.3%
52-week range: 22.36 - 34.10 (now 73.3% of the way up)
Volatility: ATR(14) 0.49 (1.6% of price) | annualised 20d 19.7%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Commodities Broad Basket
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +13.6% a year | beta to the market 1.04
Cost and size: expense ratio 0.85% | net assets 1.94B
What it is made of: Other 50.0%, Cash 45.2%, Bonds 2.7%, Stocks 2.1%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 41.8%, Brent Crude Future Jan 27 11.0%, Invesco Short Term Treasury ETF 5.8%, Mini Ibovespa Future Dec 26 2.1%
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
US inventories, week ending 2026-11-06 (published the following Wednesday)
  Crude oil: 414.4 million barrels, +4.7 on the week (a build), 21% percentile over 52 weeks
  Natural gas: 3,801.0 billion cubic feet, +77.0 on the week (a build), 92% percentile over 52 weeks -- high for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.00</summary>

```text
Rolled up from the 4 largest holdings, 60.6% of the fund by weight
Ratings by weight: buy n/a | hold n/a | sell n/a (mean n/a on a 1=strong buy to 5=strong sell scale)
Weighted price target: n/a above the current prices
Holdings read: AGPXX, BRNH27, TBLL, WINZ26
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
Share count change: 1 week: +1.1% (21.84M) over 7d | 1 month: +8.6% (154.28M) over 31d
Shares outstanding: 62.93M | fund size: 1.95B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: rising US Treasury yields and a downtrend in price suggest bearish pressure, while solid fund fundamentals (5.4% yield, 3‑year +9.2% annual return) and positive inflows (+3.8% month‑over‑month) provide bullish support. No clear macro surprise or decisive technical break, so the net view remains neutral.

**Main reasons it gave:**
- US Treasury yields rose across the curve (+0.12 to +0.34) indicating higher rates (bearish)
- EMB price below 20‑day, 50‑day, and 200‑day SMAs (bearish)
- Fund inflows over the past month +3.8% (bullish)
- Fund fundamentals: 5.4% yield, 3‑year annualized return +9.2% (bullish)

<details><summary><b>News</b> — score +0.00</summary>

- [EDF: Time For An Upgrade For This CEF (NYSE:EDF)](https://seekingalpha.com/article/4967568-edf-time-for-an-upgrade-for-this-cef?source=feed_all_articles)  
  <sub>Seeking Alpha, 12 hours ago</sub>  
  Virtus Stone Harbor Emerging Markets (EDF) is up from Sell: roughly 9% distributable income offsets risk after a 15% drop. See more details here.
- [Why Are These ASX Names Hitting Fresh Highs While The Market Slips?](https://kalkinemedia.com/au/stocks/technical-analysis/why-are-these-asx-names-hitting-fresh-highs-while-the-market-slips)  
  <sub>Kalkine Media, 9 hours ago</sub>  
  Big River Industries, Computershare and a wave of global ETFs hit fresh yearly highs as the ASX slipped. Discover what is driving the momentum.
- [Embelton outlines proposed ASX delisting and share buy-back](https://www.google.com/goto?url=CAESrAEBxCJF18WAaeA_sBUwIdnQzJG12mXnSW_MfixOJHCyTLcZnyL98SkeE-MJplQ3Dh3FVUt7Lb5b5g5r7ag2t08LQrIJ9x2C-Xyp6Soo-_UjRalIlkljWe9RHQpN8IyINBl7T6mhnK170PJ93QNXEQ0JbcxZi5Ad6hh_Qt_aMTGxm2lixb2UQR8hAt_jIHWt4ODvCe6M1fvz0NYFEZFTipeqX1cBb_8dBwhbDELm&gsessionid=NZma48XofD5d8F4BD7duhWdOcF07nkJlycoEQpsrjZEeriHd_utwlw)  
  <sub>TipRanks, 10 hours ago</sub>  
  Embelton Limited ( ($AU:EMB) ) has shared an announcement. Embelton Limited has called an extraordinary general meeting for 15 December 2026 at its...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 91.13 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 91.77 (-0.7%), 50d 92.02 (-1.0%), 200d 94.73 (-3.8%); 50d below 200d
Momentum: RSI(14) 42.2 | MACD -0.063 vs signal -0.037 (histogram -0.026)
Returns: 1d -0.2% | 5d -0.9% | 1m -0.8% | 3m -3.8%
52-week range: 90.14 - 97.74 (now 13.0% of the way up)
Volatility: ATR(14) 0.51 (0.6% of price) | annualised 20d 7.3%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Emerging Markets Bond
Yield: 5.4%
Credit quality: BBB 33.5%, BB 25.3%, B 19.5%, A 17.7% | US government debt 87.8%
Three-year record: +9.2% a year | beta to the market 1.06
Cost and size: expense ratio 0.39% | net assets 13.57B
What it is made of: Bonds 99.2%, Cash 0.8%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.0% (4.36M) over 7d | 1 month: +3.8% (494.29M) over 30d
Shares outstanding: 147.70M | fund size: 13.46B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, technicals weak but no decisive break, modest positive fund flows.

**Main reasons it gave:**
- US Treasury yields rose across the curve (3‑month +0.12, 5‑year +0.34, 10‑year +0.31) – no rate surprise
- Price below 20‑day, 50‑day, 200‑day SMAs and RSI 44.4 – bearish technicals but no decisive break
- Share count rose +5.5% over 1 month – positive fund flows

<details><summary><b>News</b> — score +0.00</summary>

- [iShares iBoxx $ High Yield Corporate Bond ETF (HYG) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/HYG/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  iShares iBoxx $ High Yield Corporate Bond ETF (HYG) · -0.39% · -0.40% · -3.62% · -4.62% · -4.60% · -11.33% · -26.23%.
- [What Drove Corporate Bond Funds LQD and HYG Lower When Treasury Yields Surged on November 12?](https://kalkine.ca/by-topic/mutual-funds-etfs/what-drove-corporate-bond-funds-lqd-and-hyg-lower-when-treasury-yields-surged-on-november-12)  
  <sub>kalkine.ca, 3 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [iShares iBoxx $ High Yield Corporate Bond ETF (HYG)](https://www.google.com/goto?url=CAESigEBxCJF19hxSLTuqhxFRpnv_xxv9OdTnLMdsi_4xy8MZ-ntOtIJN447Tc4vin9wMyFR48_iwv19Fz0xvSdWDn6nWPe0FOJRP6_lY30tqFkh3nfmmiw7uGz3bHz-4ZPiB-ipbfqrMFm41NCbIdrFZsmOI7Vyd0KMlDO2hlnMgcmNgsICHjh3JX8VI10&gsessionid=6ODg5WSOXBJvldMHiwwiuscq4PCG7YQUudcARTdc7XPvurvuDH0Q7w)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  View the basic HYG option chain and compare options of iShares iBoxx $ High Yield Corporate Bond ETF on Yahoo Finance.
- [ETF flows surge $54bn as stocks sell off and markets go 24/7](https://www.google.com/goto?url=CAESogEBxCJF10xldWHh8YSN60giGOpbLTT3sifDXPKz0KBw9-6y1n1O9IyyxqUq3vNwBc2Sdv_Tcouo8mF3pPJflBp9zjk1Bycmk_bj0qwh-MskvHWqThNQRYHlD82HFJuPvd-WjyNUO0cH53xIWB5rzQ-iWHmlu6S3ZCx4-ISiF_ewI7euyzofWuMdPy-C86uTY8Aof64RBVC-QdoeCX5CeXU5o2E&gsessionid=6ODg5WSOXBJvldMHiwwiuscq4PCG7YQUudcARTdc7XPvurvuDH0Q7w)  
  <sub>InvestmentNews, 3 hours ago</sub>  
  A turbulent week sent investors toward defensive ETF positions while industry leaders debated the future of round-the-clock trading and tokenization.
- [US ETF flows surge as equity sell-off drives defensive positioning](https://www.google.com/goto?url=CAESuQEBxCJF113ej7YC8_8w8pVB5kEoQFzABPj-v49w_AdvMW0tjWTZb58xRXvb_OU7eJ0luno4PYMcH93UYQN8lfoK4aRL6SH56MCO33aUrtaTq3vl7ZO0X11PEySGQG6Ppfj_S4lkGUsMf2aMwUsbiO5qGQ-z_hOFmsxuIG7WVvoHundNc9uzRyES4OGSiYo7jPKG8QfRHtjANqxnVcMcAvWi86DK3ivzd0axsxQXv50qfNreDCl7Vx1OiQ&gsessionid=6ODg5WSOXBJvldMHiwwiuscq4PCG7YQUudcARTdc7XPvurvuDH0Q7w)  
  <sub>Wealth Professional, 3 hours ago</sub>  
  Global stocks sold off sharply last week, pushing ETF investors into defensive positions as debate builds around 24/7 trading and tokenization in Canada.
- [Top Tokenized ETFs by Market Cap](https://www.google.com/goto?url=CAESXgHEIkXXm0shduncrfOk8HIzum9Sb0RGdnrpBy5I2OnREuXmykPpu2lAmwdimhRBdRX3xVha37sF2E7Rkdc1nMEKXET5ZZ5ZF62y7BR7BFhzNQ74LETlz2Pyv6ewsG8&gsessionid=6ODg5WSOXBJvldMHiwwiuscq4PCG7YQUudcARTdc7XPvurvuDH0Q7w)  
  <sub>CoinGecko, 14 hours ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 77.03 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 77.21 (-0.2%), 50d 77.59 (-0.7%), 200d 79.33 (-2.9%); 50d below 200d
Momentum: RSI(14) 44.4 | MACD -0.102 vs signal -0.118 (histogram 0.016)
Returns: 1d +0.1% | 5d -0.3% | 1m -0.1% | 3m -3.2%
52-week range: 76.81 - 81.18 (now 5.0% of the way up)
Volatility: ATR(14) 0.32 (0.4% of price) | annualised 20d 5.3%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: High Yield Bond
Yield: 6.1%
Credit quality: BB 58.3%, B 32.6%, Below B 7.9%, BBB 0.7%
Three-year record: +7.6% a year | beta to the market 0.65
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.3% (44.33M) over 7d | 1 month: +5.5% (923.03M) over 31d
Shares outstanding: 229.81M | fund size: 17.70B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: macro yields rising, technicals weak but no decisive break, speculators net short, but inflows positive.

**Main reasons it gave:**
- 10-year Treasury yield rose to 5.17% (+0.31% on the week)
- ETF price below 20‑day, 50‑day, and 200‑day SMAs (90.03 vs 91.05, 90.57, 93.63)
- RSI 39.3 indicating weak momentum
- Large speculators net short 38% of open interest (positioning bearish)
- Share count rose 0.8% in the past week (fund flows bullish)

<details><summary><b>News</b> — score -0.20</summary>

- [What Drove the 10-Year Treasury Yield Back Over 5%, Pressuring iShares 7-10 Year Treasury Bond ETF (NASDAQ:IEF)?](https://kalkine.ca/news/economic-news/what-drove-the-10-year-treasury-yield-back-over-5-pressuring-ishares-7-10-year-treasury-bond-etf-nasdaqief)  
  <sub>kalkine.ca, 3 hours ago</sub>  
  What Drove the 10-Year Treasury Yield Back Over 5%, Pressuring iShares 7-10 Year Treasury Bond ETF (NASDAQ:IEF)?
- [Why Has the 10-Year Treasury Yield Returned Over 5%, Hurting iShares 7-10 Year Treasury Bond ETF (NASDAQ:IEF)?](https://kalkine.com.au/news/economic-news/why-has-the-10-year-treasury-yield-returned-over-5-hurting-ishares-7-10-year-treasury-bond-etf-nasdaqief)  
  <sub>Kalkine, 3 hours ago</sub>  
  Why Has the 10-Year Treasury Yield Returned Over 5%, Hurting iShares 7-10 Year Treasury Bond ETF (NASDAQ:IEF)?
- [Which of 5 Top Funds Is Best Positioned for a Fed Hike in December: SPDR S&P 500 ETF Trust (NYSEARCA:SPY), iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT), iShares 7-10 Year Treasury Bond ETF (NASDAQ:IEF), iShares 1-3 Year Treasury Bond](https://www.google.com/goto?url=CAES9wIBxCJF13bBve8kRwzMeGTdvARTHd1nB9fHYgjPHn9sNdevV0VxZnBzP03XeCvqQpu7T7mcdjj4CMP6cA3OoTh0EiEkOQd11lZt-0UZKDTStw63Fx26EOINAfftTJUmOvNpimc3asGkRMELLPBFm0v-oyhGRCslQEqnR-A1yEyCU6x3155J4AGo2q6Qsl-cXwa5Z-kJL2_KnxkMp8K7XHu4mD1fBHWGqNBTPzUaKTxblGDPZBCg1O6ZxN7XXN1bQq3ij2Xli7E1MT8iA8wBDuIU1lFEeayFCqpqs20q2LPO9FHZq2bA0yxEZkBeOdr7G6GjerJN3Lo1iqMdgkb07LtbH-xNkBe4xbDl3J34fPtqTN5KdZuXzu_y0xE9Nc1hCrpVtCyFdfgG-Ewsfvbue2W3vp8S7GkKOPw2gq7b5TiGbF4d4UDzrfvlAyRkp16FHdkuZ8tbLPhCKMLTl9gI5h55HEVjCsXsjPKXS6jfoz4U2UGAo9GjXmg&gsessionid=kCxXelpFJKWtGQlgGZjP1s7QpiKZ_wIX4ybEBvvS2Ux7lzz5iRpeQQ)  
  <sub>kalkine.ca, 21 hours ago</sub>  
  Which of 5 Top Funds Is Best Positioned for a Fed Hike in December: SPDR S&P 500 ETF Trust (NYSEARCA:SPY), iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT),...
- [Why Did the 10-Year Treasury Yield Briefly Cross 5% Again, Pressuring iShares 7-10 Year Treasury Bond ETF (NASDAQ:IEF)?](https://www.google.com/goto?url=CAES1QEBxCJF18UfcirQq-rBNjPQno4YkS8-RvMSmvxHUW8rEEnbWxPO2o1ejmg5GrwfbLjfyrFeCUsjVd8kGhXgD8vzuE4x1FB0ndiSfLWVF4QLjOfSN9JczyzHnXnaEjOoOqr0aU7mDt3N-AgIZh-_wXzO79j1xioLTbuVHuF6SnEwuvDbzQsBA1OWho-CuWc_Waab6s0QM1LpVE0NIK0pKsg-c3BrfUCilptNfgCigMtVOdJb07uYJhoCGzi6MUrnGfB10nTsSLOSRGzqXHfQCOu0I9uh_1k&gsessionid=kCxXelpFJKWtGQlgGZjP1s7QpiKZ_wIX4ybEBvvS2Ux7lzz5iRpeQQ)  
  <sub>kalkine.ca, 22 hours ago</sub>  
  Why Did the 10-Year Treasury Yield Briefly Cross 5% Again, Pressuring iShares 7-10 Year Treasury Bond ETF (NASDAQ:IEF)?
- [The Bond Rally Faces a Reality Check](https://www.google.com/goto?url=CAESjgEBxCJF1_9B6iV9YZF_F9t-1vm9ASl4vpg1oSZdU6-nMAeF_mNchUlrJT-mjE1xLSVB8_2Rs2Qtpr1uV-HeOfNLjBZD14e415SCSyTAKybCYJ0sXhIx_stGiEjkpOnE52xVcU0njVZdbkkiFUVwxD2iK6CrG6DDnPz8GCO3XW1SYndQ47kJuFWPEe6g2VMY&gsessionid=kCxXelpFJKWtGQlgGZjP1s7QpiKZ_wIX4ybEBvvS2Ux7lzz5iRpeQQ)  
  <sub>Investing.com, 22 hours ago</sub>  
  Market Analysis by James Picerno covering: Vanguard Total Bond Market Index Fund ETF Shares, iShares 1-3 Year Treasury Bond ETF, iShares 7-10 Year Treasury...
- [Will October Producer Prices Jolt SPDR S&P 500 ETF Trust (NYSEARCA:SPY) With a 6.6% Annual Forecast?](https://www.google.com/goto?url=CAESwQEBxCJF12BqT5iSkXbxKlxFbltAhfK79TLHQ4-kth6Cr0Kwyr05_9IzqX1I717VcpilEpMsFAKm4T-SXV69rjtXyOXIl8keCu98SdizKGnTqGVl3kYew6U9MQEzjg46SO9H6R3lSyzH2ia7pKQZEaG-RnTkGj0QmY1zE6PEPFSadZXK8qmlA470sr2o4TjgRD21MU2HPP9qmh72Frr3CZfZvMsFzFisi3rAUSk1eSyimuaWsLijpFpXCKn_mmKaqsc0&gsessionid=kCxXelpFJKWtGQlgGZjP1s7QpiKZ_wIX4ybEBvvS2Ux7lzz5iRpeQQ)  
  <sub>kalkine.ca, 3 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports. Become a Kalkine member...
- [How Should Canadian Holders of SPDR S&P 500 ETF Trust (NYSEARCA:SPY) Read a Hot 0.4% October CPI?](https://www.google.com/goto?url=CAESvgEBxCJF140Pac4-ENSHfEoNfJVTmnJ4keRGcibnYjfDhLAYTUC85FugE3-7UBtXT1oIcVd5jApHDi03PrqWnpKqBkmXexz4ZRW8Fm9niiQ1YVylWhPbf5UVL4Ia-hIWoJsTW9ZkbsluhBD0-Je0-JV1TrSXK0ja3SGufUX7pjPhn8nqNQH3hl5CSs8Ff1PBaTfHbkV7xjFYksx8aIY53Ab-1xYxdfWx82JFVf8ErtK2Zd2aldsxL1yA57SaOrPP&gsessionid=kCxXelpFJKWtGQlgGZjP1s7QpiKZ_wIX4ybEBvvS2Ux7lzz5iRpeQQ)  
  <sub>kalkine.ca, 22 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 90.03 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 91.05 (-1.1%), 50d 90.57 (-0.6%), 200d 93.63 (-3.8%); 50d below 200d
Momentum: RSI(14) 39.3 | MACD 0.067 vs signal 0.210 (histogram -0.143)
Returns: 1d -0.2% | 5d -2.0% | 1m -0.4% | 3m -3.0%
52-week range: 88.92 - 97.99 (now 12.3% of the way up)
Volatility: ATR(14) 0.49 (0.5% of price) | annualised 20d 7.3%
Volume: 0.10x the 20-day average
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
Three-year record: +3.7% a year | beta to the market 1.17
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
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 38.0% of open interest (5,947,433 contracts)
Change on the week: -0.2% of open interest
Crowding: 52% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.8% (332.95M) over 7d | 1 month: +2.9% (1.23B) over 31d
Shares outstanding: 478.83M | fund size: 43.11B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, technicals lack decisive break, positioning shows modest reduction in short bias, analyst coverage thin.

**Main reasons it gave:**
- Macro: Treasury yields rose modestly across curve, no policy surprise
- Technical: Price below 20d/50d/200d SMAs, RSI neutral, low volume, no decisive break
- Positioning: Net short 12.3% of OI, short position decreased by 1.8% week-over-week
- Analyst view: Coverage thin (1.9% of fund) despite 100% buy rating, limited impact

<details><summary><b>News</b> — score +0.00</summary>

- [Why Did Small Caps Sink Hardest as Major US Indexes Closed Lower and iShares Russell 2000 ETF (NYSEARCA:IWM) Fell?](https://kalkine.com.au/news/general-news/why-did-small-caps-sink-hardest-as-major-us-indexes-closed-lower-and-ishares-russell-2000-etf-nysearcaiwm-fell)  
  <sub>Kalkine, 3 hours ago</sub>  
  Why Did Small Caps Sink Hardest as Major US Indexes Closed Lower and iShares Russell 2000 ETF (NYSEARCA:IWM) Fell?
- [Why Did the Russell 2000 Drop 1.66%, Leading Losses in Stocks and Hitting iShares Russell 2000 ETF (NYSEARCA:IWM)?](https://www.google.com/goto?url=CAESzgEBxCJF177mUcQpBs6u44Caw4SAmwJAoHdkZPNtKCd2Eee9Ucuhh9pwU_A25unRO81jPvhNxdkxEqpsi4VIbXKvQDQzwGMrvfZY_bkVibnX1oyYI_zn3N319acx_JtO4hJ7JEh1d71yHex2McJjUbNDB56POei6BjGH16VhycyaSQnjM_KAIsAAlgXwF1tE3lP0KZQkSF4zfKF9gidQgMqovO1nKx4Syr4TS1aXGGCGqvjSMFqBiv8x8LXsPYPzUvcowQv3-R7GdSf2DliFxg&gsessionid=tVFh7X-Ed0fyEPdzFLg1aTXzywLvatyb1DyLj64Bh1Yap4NoGer1jw)  
  <sub>kalkine.ca, 3 hours ago</sub>  
  Why Did the Russell 2000 Drop 1.66%, Leading Losses in Stocks and Hitting iShares Russell 2000 ETF (NYSEARCA:IWM)?
- [Which of 5 Top Funds Is Best Positioned for a Fed Hike in December: SPDR S&P 500 ETF Trust (NYSEARCA:SPY), iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT), iShares 7-10 Year Treasury Bond ETF (NASDAQ:IEF), iShares 1-3 Year Treasury Bond](https://www.google.com/goto?url=CAES9wIBxCJF10yRksBYKZuZCPD0lqaMs34hj7-_US6i8jwz3ReBqelxcnXhRVUgWxBxrLjNgKi_6x2SYwVGKLZ0bXh6Z9Wk8UxWVOl_vZ5mCN7XPIeOhfK_BpJYodu3NzHki7ckHUDsEpOYc4ECPD5g4wHUrwuuq2uq_5W7tvAScWJjPc9pBAsqR8tUJgRZUlQwLzBQh2tKWuckckTdU2PZTLoMrMBgEShiFQtczhoewJa60TssfUj3a_sswAKz7ZOqeicB4-4vwmN9ASRfG-PsdUBvznM5YU5b3tTsY57TUNbIjkk6fQo5orWdxT3_oXC47V_Mg04ZNlUcOAwfBJT3vO9n8_UXD_F4OjlqEzrM9XEN6xDOVQeSNYAOHJ-s3W8K-1L3O1S2MLu7KbPAuYDYZJixUExoUQ6Zk_NEHDGwpyZJl5A91MQOuUgZ8ZQZBcn7WMkaHkA7vaGNnNMG8Viy9s2Sw_-CmomAiTf4VRU_mjpFqolSXFUAYbE&gsessionid=tVFh7X-Ed0fyEPdzFLg1aTXzywLvatyb1DyLj64Bh1Yap4NoGer1jw)  
  <sub>kalkine.ca, 20 hours ago</sub>  
  Which of 5 Top Funds Is Best Positioned for a Fed Hike in December: SPDR S&P 500 ETF Trust (NYSEARCA:SPY), iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT),...
- [How Might Expected Fed Hikes in December and March Affect iShares Russell 2000 ETF (NYSEARCA:IWM)?](https://www.google.com/goto?url=CAESwgEBxCJF1-u9R1enBegaF1TsTijDNzn-A05p60DMqxuY-88eq1Zkw6XSMgPidGCeC3H-6mbwNKYeYFKNgioyx9ltgblXhAWmGs-QGpHgHcOihulB4UCrdxSzTjZXeWQyxzQDJBU-0ZsCjj6ZNSq9VbgQVsCZfg9fl2B60PY_Z-ovhOaEZTcPsQ7gyE7cX0KQP0POUI7f40zhX1TKayC_sb7XrEH8KKnYi-OQwFb6lb99muL0fTCM6uIWRVsd5_Dr3mtDzQ&gsessionid=tVFh7X-Ed0fyEPdzFLg1aTXzywLvatyb1DyLj64Bh1Yap4NoGer1jw)  
  <sub>kalkine.ca, 22 hours ago</sub>  
  How Might Expected Fed Hikes in December and March Affect iShares Russell 2000 ETF (NYSEARCA:IWM)?
- [ETF flows surge $54bn as stocks sell off and markets go 24/7](https://www.google.com/goto?url=CAESogEBxCJF18veX1ley5A13aO6VTcDoKXTLBcSjf1S7QS9G5SWTAcoUjBXSzsULGrM6idD1yBGroH-8CB3o_FbgRrMCgKUt8dqQm0oL1xFSOzstl-c_Nzc-UVl3GU1CIVmYoEFWBleNJCDSYnOWHbFAw07M4T2ESqFoPixyg3e-oA-ZsJvXOxk2xAsqMmKp-MuuG9ZwIiiYPR3v-JI3c1p9BcX2C0&gsessionid=tVFh7X-Ed0fyEPdzFLg1aTXzywLvatyb1DyLj64Bh1Yap4NoGer1jw)  
  <sub>InvestmentNews, 3 hours ago</sub>  
  A turbulent week sent investors toward defensive ETF positions while industry leaders debated the future of round-the-clock trading and tokenization.
- [NVIDIA’s Leadership Crisis Is Dragging the S&P 500 Lower. Here’s What Else Is Moving](https://www.google.com/goto?url=CAESuQEBxCJF1_cIaQrzPUrwbNvWwpXUou9kKJSDAMG7CLJnilkJaT5BOOOBiYXjEw-113cUUZkHpquoHdAlCgQjPtrsligiyUytFRE2YEyP7Lk-NOxHNz7LCoFS1n9jsaAOEFydLhQcFvkt4KOsYJQGP0pTgHXqwd4xI16h00Zwd4ha_Lzcsmw0FWyz099F2MrlfPCKmeEgFVXnCbmz2VB3DGENhZHhSHOppFb3vN7tfTNv2gQfURFtTYmmnw&gsessionid=tVFh7X-Ed0fyEPdzFLg1aTXzywLvatyb1DyLj64Bh1Yap4NoGer1jw)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  NVIDIA plunged 7% to about $161 after Jensen Huang resigned as CEO, leaving the chipmaker without a permanent leader. Small caps fell hardest, with IWM down...
- [iShares Russell 2000 ETF (IWM) Price Prediction: Small-cap rebound meets mixed intraday signals near key resistance](https://www.google.com/goto?url=CAESngEBxCJF1-JKxDMSQBYvRfuMM92G8cdGsbtEePr8sIC3_1BmlY5o8ar32-JhsVtZm6XARm4XsEredMZx5WBbSGoqrPsU5lt6to6_usoyVJe_XvKSzk58mzp5auR36pQjrfsiih4Yimx4k8kmVRX4EKAHW9o-fROmwfP8uw8XyuzQH5e3w_XOvFoDwdlN9St2igMd7kNSzH_x-G1wS_GlAA&gsessionid=tVFh7X-Ed0fyEPdzFLg1aTXzywLvatyb1DyLj64Bh1Yap4NoGer1jw)  
  <sub>Blockchain News, 21 hours ago</sub>  
  iShares Russell 2000 ETF (IWM) is trading at $283.28 after a modest 0.35% 24-hour gain, holding above its short-term moving averages but still facing...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 277.74 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 278.39 (-0.2%), 50d 280.77 (-1.1%), 200d 279.41 (-0.6%); 50d above 200d
Momentum: RSI(14) 48.0 | MACD -0.272 vs signal -0.617 (histogram 0.345)
Returns: 1d -0.3% | 5d +1.5% | 1m +1.0% | 3m -8.7%
52-week range: 229.11 - 305.09 (now 64.0% of the way up)
Volatility: ATR(14) 4.66 (1.7% of price) | annualised 20d 24.9%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Small Blend
What it holds: P/E 16.28 | P/B 1.99 | P/S 1.23 | 3y earnings growth n/a
Yield: 1.0%
Three-year record: +20.1% a year | beta to the market 1.26
Cost and size: expense ratio 0.19% | net assets 75.49B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Glaukos Corp 0.5%, BrightSpring Health Services Inc 0.4%, JFrog Ltd Ordinary Shares 0.3%, Twist Bioscience Corp 0.3%, Moog Inc Class A 0.3%
Sector mix: Healthcare 21.0%, Financial services 18.2%, Technology 14.0%, Industrials 12.7%
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
Rolled up from the 5 largest holdings, 1.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.45 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.2% above the current prices
Holdings read: GKOS, BTSG, FROG, TWST, MOG-A
Recent rating changes among them:
  - GKOS: 2026-10-29 HC Wainwright & Co.: main, Buy -> Buy
  - BTSG: 2026-11-03 Guggenheim: main, Buy -> Buy
  - FROG: 2026-11-12 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MOG-A: 2026-10-13 JP Morgan: main, Overweight -> Overweight
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 12.3% of open interest (449,399 contracts)
Change on the week: -1.8% of open interest
Crowding: 67% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 281.05M | fund size: 78.06B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as rising Treasury yields and bearish technicals are offset by solid fund fundamentals and net inflows.

**Main reasons it gave:**
- 10-year Treasury yield up 0.31% on the week
- LQD price below 20‑day SMA (103.89) and RSI 39.5 indicating bearish momentum
- Share count up 0.7% week and 11.6% month showing net inflows

<details><summary><b>News</b> — score +0.00</summary>

- [VCLT vs IGLB: Which Long-Term Corporate Bond ETF Offers Investors Better Long-Term Prospects?](https://finance.yahoo.com/markets/options/articles/vclt-vs-iglb-long-term-232001499.html)  
  <sub>Yahoo Finance, 15 hours ago</sub>  
  Vanguard's fund offers a lower expense ratio and higher yield, but both ETFs share similar risk profiles and diversification.
- [What Drove Corporate Bond Funds LQD and HYG Lower When Treasury Yields Surged on November 12?](https://kalkine.ca/by-topic/mutual-funds-etfs/what-drove-corporate-bond-funds-lqd-and-hyg-lower-when-treasury-yields-surged-on-november-12)  
  <sub>kalkine.ca, 3 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 102.86 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 103.89 (-1.0%), 50d 103.65 (-0.8%), 200d 107.35 (-4.2%); 50d below 200d
Momentum: RSI(14) 39.5 | MACD 0.004 vs signal 0.119 (histogram -0.115)
Returns: 1d -0.2% | 5d -1.6% | 1m -0.6% | 3m -2.7%
52-week range: 101.83 - 112.05 (now 10.1% of the way up)
Volatility: ATR(14) 0.60 (0.6% of price) | annualised 20d 7.3%
Volume: 0.02x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Corporate Bond
Yield: 4.8%
Credit quality: A 46.7%, BBB 40.5%, AA 11.9%, AAA 0.9%
Three-year record: +5.2% a year | beta to the market 1.32
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.7% (212.02M) over 7d | 1 month: +11.6% (3.31B) over 31d
Shares outstanding: 308.45M | fund size: 31.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst view of top holdings covers only 1.4% of fund and shows a modest bearish price target of -7.4% relative to current price
- CFTC positioning shows net short 18.7% of open interest, increasing by 1.7% week over week
- Technicals show price above 20‑, 50‑ and 200‑day SMAs with modest momentum, but volume is only 4% of 20‑day average
- Macro data shows no surprise: yields rose modestly, VIX fell but remains elevated, and Fed policy unchanged

<details><summary><b>News</b> — score +0.00</summary>

- [Warren Buffett doesn't follow his own S&P 500 advice. Should you?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af7224974ce435c852aeacf18fd36e4&url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fwarren-buffett-doesnt-follow-his-own-s-p-500-advice-should-you%2far-AA2hiREJ&c=8083562074322096884&mkt=en-us)  
  <sub>The Motley Fool on MSN, 29h ago</sub>  
  Berkshire's concentrated stock portfolio seems to contradict his advice to buy the S&P 500.
- [November 2026 US Market Outlook: Fiscal Mechanics Vs. Market Pricing](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af7224974ce435c852aeacf18fd36e4&url=https%3a%2f%2fseekingalpha.com%2farticle%2f4967661-november-2026-us-market-outlook-fiscal-mechanics-vs-market-pricing&c=8016853734941427584&mkt=en-us)  
  <sub>Seeking Alpha, 14h ago</sub>  
  November 2026 US Market Outlook: Fiscal Mechanics Vs. Market Pricing Nov 13, 2026, 3:24 AM ET State Street SPDR S&P 500 ETF Trust (SPY), DIA, QQQ, IVV, VOO, IWM, SPX, SP500, NDX, DJI, RTY Alan Longbon ...
- [The Scandal at Nvidia is Exactly What's Wrong with the S&P 500](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af7224974ce435c852aeacf18fd36e4&url=https%3a%2f%2fwww.itiger.com%2fnews%2f2683167655&c=11202052779691535902&mkt=en-us)  
  <sub>itiger, 29h ago</sub>  
  The Scandal at Nvidia is Exactly What's Wrong with the S&P 500. On Tiger Brokers' website to stay informed on market trends, price movements, and investment strategies, helping you make smarter ...
- [Thursday’s Charts – Small Caps Slide as 2-Year Has Biggest Two-Day Jump Since March 2023](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af7224974ce435c852aeacf18fd36e4&url=https%3a%2f%2fpro.thestreet.com%2fmarket-commentary%2fthursdays-charts-small-caps-slide-as-2-year-has-biggest-two-day-jump-since-march-2023&c=13932522041560188591&mkt=en-us)  
  <sub>TheStreet Pro, 23h ago</sub>  
  The 2-year yield had its biggest two-day jump since March 2023 and the dollar hit another 19-month high, while gold fell to its lowest in more than a year and the S&P 500’s run of higher lows ended.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 221.44 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 218.67 (+1.3%), 50d 214.99 (+3.0%), 200d 208.86 (+6.0%); 50d above 200d
Momentum: RSI(14) 57.8 | MACD 1.795 vs signal 1.602 (histogram 0.193)
Returns: 1d +0.3% | 5d +2.5% | 1m +3.0% | 3m +0.3%
52-week range: 182.18 - 223.33 (now 95.4% of the way up)
Volatility: ATR(14) 2.61 (1.2% of price) | annualised 20d 17.7%
Volume: 0.04x the 20-day average
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
Three-year record: +18.4% a year | beta to the market 0.80
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

<details><summary><b>What analysts and big funds say</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.10</summary>

```text
Rolled up from the 5 largest holdings, 1.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 38.4% | hold 61.6% | sell 0.0% (mean 2.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -7.4% above the current prices
Holdings read: MRNA, PTC, ACN, IT, HAS
Recent rating changes among them:
  - MRNA: 2026-11-09 Goldman Sachs: main, Neutral -> Neutral
  - PTC: 2026-11-12 Wolfe Research: down, Outperform -> Peer Perform
  - ACN: 2026-10-26 Wells Fargo: main, Equal-Weight -> Equal-Weight
  - IT: 2026-11-06 Barclays: down, Equal-Weight -> Underweight
  - HAS: 2026-10-28 UBS: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.25</summary>

```text
Contract: E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 18.7% of open interest (1,986,532 contracts)
Change on the week: +1.7% of open interest
Crowding: 68% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.25</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.3% (304.83M) over 7d | 1 month: +0.3% (266.17M) over 31d
Shares outstanding: 452.10M | fund size: 100.11B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No policy surprise, data release, or decisive technical break; modest bullish tilt from reduced net short offset by neutral fundamentals and stable flows.

**Main reasons it gave:**
- Short-term Treasury yields rose 0.12% on the week (3‑month at 4.12%)
- Large speculators net short fell 2.5% of open interest, modest bullish tilt
- Fund inflows positive (+4.3% share count over 1 month) indicating demand
- Technical indicators near moving averages, RSI 41, no decisive break

<details><summary><b>News</b> — score +0.00</summary>

- [债券指数ETF-iShares Barclays 1-3年国收跌0.21%，成交额19.45亿美元](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af722a816aa43f0864758cde27cc5d1&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fusstock%2fnotice%2f2026-11-13%2fdoc-iniypqyp1390120.shtml&c=17301799222670950545&mkt=en-us)  
  <sub>新浪财经, 23h ago</sub>  
  11月13日，债券指数ETF-iShares Barclays 1-3年国（SHY）收跌0.21%，报81.14美元，成交额19.45亿美元，市值277.42亿美元。 声明：市场有风险，投资需谨慎。本文基于第三方数据库发布，不代表新浪财经观点，任何在本文出现的信息均只作为参考，不构成个人投资建议。如有出入请以实际公告为准。如有疑问，请联系biz@staff.sina.com.cn。

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.19 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 81.44 (-0.3%), 50d 81.33 (-0.2%), 200d 82.04 (-1.0%); 50d below 200d
Momentum: RSI(14) 41.0 | MACD -0.014 vs signal 0.028 (histogram -0.042)
Returns: 1d +0.1% | 5d -0.5% | 1m -0.1% | 3m -1.0%
52-week range: 81.05 - 83.18 (now 6.6% of the way up)
Volatility: ATR(14) 0.13 (0.2% of price) | annualised 20d 2.4%
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
Three-year record: +4.0% a year | beta to the market 0.25
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.15</summary>

```text
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 32.5% of open interest (4,464,182 contracts)
Change on the week: -2.5% of open interest
Crowding: 78% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.15</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.3% (72.16M) over 7d | 1 month: +4.3% (1.12B) over 31d
Shares outstanding: 337.65M | fund size: 27.41B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, technicals weak but no decisive break, modest insider short positioning, and supportive fund inflows.

**Main reasons it gave:**
- 10-year Treasury yield up 0.31% on the week, raising real yields for TIPS
- Large speculators net short 38% of open interest, with only a -0.2% weekly change
- Fund inflows of +2.1% over the past month indicate demand for TIP exposure
- Price below 20d, 50d, and 200d SMAs; RSI 34.5; volume 0.04x average

<details><summary><b>News</b> — score +0.00</summary>

- [Jensen Huang's biographer calls him abusive, says 'He gave ₹94,000 tip to waiter as an act' | 'Contradicting Huang was like lighting a fuse' | Inshorts](https://inshorts.com/en/amp_news/jensen-huang-s-biographer-calls-him-abusive--says--he-gave--94-000-tip-to-waiter-as-an-act--1794574156679)  
  <sub>Inshorts, 2 hours ago</sub>  
  NVIDIA Founder Jensen Huang's biographer Stephen Witt said the billionaire's 'humble' image is an act he performs not for the observer but to 'flatter...
- [Today’s Wholesale Price Report Could Tip the Fed Toward a Half-Point Hike](https://www.tipranks.com/news/todays-wholesale-price-report-could-tip-the-fed-toward-a-half-point-hike)  
  <sub>TipRanks, 3 hours ago</sub>  
  Friday's October wholesale price report could tip the Federal Reserve toward a half-point interest rate hike in December. Wall Street is bracing for the...
- [South Korean Startup DeepX Investing Over $100M in New Robotics AI Chip](https://www.google.com/goto?url=CAESnAEBxCJF1-WgCbJBguBX6F8rCbIy8CsS5wAuhaeJwqp4zhVxeZkLPUJzbNgbKbq-X8HG3JL082Sq0I_7z2Pg5dk1uuzHCLkxexnX2dubDCeLAw0Npek-iefI0G9_y5yJMF_AB9hVdsZURhv8AI3p9U5fTj1EJ-G9U-bWFQUh1LvnmVB_ZNR81k_WfsechUHpHYI08MxwUJ7ZNLXvhzQ&gsessionid=-y2GkeFeZx3S2f3VM8j-Ir8VFopHXcTMGRy1LtgNA3jMipGt5NUP2A)  
  <sub>TipRanks, 3 hours ago</sub>  
  South Korean AI startup DeepX is set to spend over $100 million developing a next-generation AI chip using technology from Samsung Electronics ($SSNLF).
- [Nvidia Sees Record $111M Retail Buying as Investors Bet on Earnings Recovery](https://www.google.com/goto?url=CAESpgEBxCJF1ywXCtN3TbjA7IGBMB4KZ4SP6VQgdJdRsSuZ-JIZA6m9W4YH4i_7OgOxRKWSTyWy_Z8CN1VTONuh5dxtM6XBbl1SxaKV7uEF75DYRRLvoNvVhHG9JSHe__MSz4MdRFLTpKlc3WiTVFBPixz6mfsjJKEa2WLAuqBWdmfL-87kcHaDEuIHk-NDF7IbaMhxmyLKIsDBq_4kD7upFIaAlv5anuib&gsessionid=-y2GkeFeZx3S2f3VM8j-Ir8VFopHXcTMGRy1LtgNA3jMipGt5NUP2A)  
  <sub>TipRanks, 3 hours ago</sub>  
  Nvidia ($NVDA) stock saw record retail buying on Thursday, as investors bet on its upcoming earnings despite CEO Jensen Huang's exit.
- [Buy Nvidia Stock ‘With Both Hands,’ Says Analyst as Valuation Drops to ‘Stupid’ Levels](https://www.google.com/goto?url=CAESrAEBxCJF10BJpGReLnx8803H8vgsrYJOIxKeHJ2SdGOD_Vl_M9NDGpfngevkG66gjWuTcrEhmh1N52_s3allJBl5cvFvG6xyojly-VNCTCqhhU913WYQom3DEShB226wWynFA_4UAY4FbBaeTxUeNjYop-V0iuxMfCR5rCmRBUSgRl9LxGgCmpp_2OAq2SnSFvpOwkdfNKwtPlry1fvLHk3o7ECIRbS0r6q-RjX1&gsessionid=-y2GkeFeZx3S2f3VM8j-Ir8VFopHXcTMGRy1LtgNA3jMipGt5NUP2A)  
  <sub>TipRanks, 3 hours ago</sub>  
  Nvidia ($NVDA) stock fell 4.3% on Thursday, closing at $166.19, following CEO Jensen Huang's resignation. However, Freedom Capital's analyst Paul Meeks...
- [Braskem’s November 2026 Filing Notes Going-Concern Uncertainty](https://www.google.com/goto?url=CAESrgEBxCJF1_67iPxr4ILswuT7VgAGe0aDvCubTqutf0ZoT1xyzJd6MdQ-KX0E8Kk_hg6qlMrFEZVc8KWfulORG_hd--KOiCiKIgXjlDpKZN-F9kZseBOYEBCSp9-qHk-OV6aoz2Mo1AHA9PWQvLTQAslwRFzm7AzGYOwOJIJTGXI9G4rWXTLoM8rTA0YiuWarfOWqtbhUNf28C4BCTVltzz9wzwPQOVR6GnFRAOCT9g4&gsessionid=-y2GkeFeZx3S2f3VM8j-Ir8VFopHXcTMGRy1LtgNA3jMipGt5NUP2A)  
  <sub>TipRanks, 3 hours ago</sub>  
  The latest announcement is out from Braskem SA ( ($BAK) ). For the quarter ended September 30, 2026, Deloitte reviewed Braskem S.A.'s individual and...
- [UOBAM ETF to Gradually Reduce ChiNext Constituent Weight Cap](https://www.google.com/goto?url=CAESrQEBxCJF15qiYDtR_KGbcwBansVJ0wdgwhiUk3LawytgmdJm16ewN7ICKlEWCpVMCvQ1xDO0tVMnJejmIMnMQ0wDdmUMo-PkusKxkgWXI4csWdSabKT9NRa80btYZDd4W-yQhnEd3fZCV6loCRJFi40gCA8Nf4nv8FXqZOSESHtFGcB5-M4oL01Pj2aDBGw1uPaVrNeJRCwAAJmxX7ZeWOyC0TiTM9UwRuT8NbzWIw&gsessionid=-y2GkeFeZx3S2f3VM8j-Ir8VFopHXcTMGRy1LtgNA3jMipGt5NUP2A)  
  <sub>TipRanks, 12 hours ago</sub>  
  UOBAM Ping An ChiNext ETF Units ( ($SG:CXS) ) just unveiled an update. UOB Asset Management Ltd, an asset-management company, manages UOBAM Ping An ChiNext...
- [These 3 ETFs Could See 18%+ Gains, According to the AI Analyst](https://www.google.com/goto?url=CAESlgEBxCJF1z_gjAO-FrivDW28sCFl9HL6_HyPLhRwInIheUhq9qWcyU1W-du5xoPceOqiZBa7PhWe_YpM3LN5qciyxc_61mQwJS7d2pPxFwAj-HHWPZ2EdwUqlcbfO_YnLTu528n1jWoRkaK-s5xPUcwjunflsIGYkvwMgF9qYjR_GMGZO5U0Pv9g3mXy4-qNd11ESP4w2jA&gsessionid=-y2GkeFeZx3S2f3VM8j-Ir8VFopHXcTMGRy1LtgNA3jMipGt5NUP2A)  
  <sub>TipRanks, 18 hours ago</sub>  
  TipRanks' ETF AI Analyst sees more than 18% upside potential in the Vanguard Russell 1000 Growth ETF ($VONG), VanEck Semiconductor ETF ($SMH),...
- [Invesco QQQ Trust ETF Resists Pressure as Nvidia CEO Resigns — Here’s Why](https://www.google.com/goto?url=CAESowEBxCJF15fb72mQitEFbyDvpwzmxAKLGuqIoZKKZlebZY8xCp3WQ72hIR0jxV-y-fb9Zavmi3lCtF-1Od0Phl8EStt8HSCvb8eXdOdq2m6ilsYSta_2XfrOrNQ5PGyOqdX-LF7SbnkLE4rJo9agUYMTgxCM1gv8BcNY8zrjg1jxzxLaLAaWPIw6QjclkeHqv3Obk7Q9wDIrpUCecGygpQ3lvOUe&gsessionid=-y2GkeFeZx3S2f3VM8j-Ir8VFopHXcTMGRy1LtgNA3jMipGt5NUP2A)  
  <sub>TipRanks, 18 hours ago</sub>  
  Invesco QQQ Trust ETF ($QQQ), which tracks the Nasdaq-100 index (NDX), was little changed on Thursday afternoon. This came even as Jensen Huang's...
- [Vanguard Just Launched a New ETF — Why Investors Should Take Notice](https://www.google.com/goto?url=CAESnAEBxCJF13sxXoTSqR06R_5R9NyuKfoAxWL7TU3es00lf2n7FT6RvLzaxLge7B7cEeoqTgeGpMgYhKl6kZ9Bui7ep-2tr0aDSQag2fau4xwFnFNMkCRqObf76vnzbzlt0_VTPyxfzkNUPwwTdzW2xN0BdwRap92ud8LAPGPx6JmOV2Q7gFgiPHU4lq9_yjCTv-aAxU2UGNkiNyauph8&gsessionid=-y2GkeFeZx3S2f3VM8j-Ir8VFopHXcTMGRy1LtgNA3jMipGt5NUP2A)  
  <sub>TipRanks, 22 hours ago</sub>  
  Vanguard has expanded its lineup of exchange-traded funds with the launch of the Vanguard Emerging Markets Bond Active ETF (VEMB), giving investors a new...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 104.73 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 105.90 (-1.1%), 50d 105.41 (-0.6%), 200d 108.63 (-3.6%); 50d below 200d
Momentum: RSI(14) 34.5 | MACD -0.069 vs signal 0.122 (histogram -0.191)
Returns: 1d -0.0% | 5d -1.5% | 1m -0.5% | 3m -1.9%
52-week range: 103.98 - 111.88 (now 9.4% of the way up)
Volatility: ATR(14) 0.38 (0.4% of price) | annualised 20d 4.7%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Inflation-Protected Bond
Yield: 4.4%
Credit quality: AA 100.0% | US government debt 99.8%
Three-year record: +3.8% a year | beta to the market 0.73
Cost and size: expense ratio 0.18% | net assets 14.65B
What it is made of: Bonds 99.8%, Cash 0.2%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 38.0% of open interest (5,947,433 contracts)
Change on the week: -0.2% of open interest
Crowding: 52% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.8% (112.75M) over 7d | 1 month: +2.1% (295.45M) over 31d
Shares outstanding: 139.23M | fund size: 14.58B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; macro yields rising, bearish speculator positioning, but solid fund fundamentals and no decisive technical break.

**Main reasons it gave:**
- 10-year Treasury yield rose 0.31% on the week to 5.17%
- CFTC data shows large speculators net short 33.3% of open interest, up 1.1% week-over-week
- Fund basics: AA credit quality, 4.8% yield, expense ratio 0.15%
- Technicals: RSI 38.2, MACD negative, price below 20d/50d/200d SMAs

<details><summary><b>News</b> — score +0.00</summary>

- [[US 10-Year Treasury Yield at 5.10%] Why do US Treasury ETFs fall when interest rates rise? Decoding from the 30-year bond auction](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af722cd58ee440ab640a89111cea988&url=https%3a%2f%2fnote.com%2ficicle9%2fn%2fn0e61931ab558%3fhl%3den&c=15593173284199491824&mkt=en-us)  
  <sub>note, 15h ago</sub>  
  The day after seeing the news that "US Treasury yields have exceeded 5%," you notice the valuation of the US Treasury ETF you hold has dropped. If you have just started investing in bonds, you might ...
- [Amplify TLT U.S. Treasury 12% Option Income ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af722cd58ee440ab640a89111cea988&url=https%3a%2f%2fmarkets.businessinsider.com%2fetfs%2famplify-tlt-us-treasury-12percent-option-income-etf-us0321085161&c=11207425800768926254&mkt=en-us)  
  <sub>Business Insider, 21h ago</sub>  
  Historical Prices for Amplify TLT U.S. Treasury 12% Option Income ETF Loading.. Sustainability Rating Investment Policy Copyright © 2026 Insider Inc and finanzen.net ...
- [The Treasury Secretary Is Now Living on a Military Base After Iranian Threats](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af722cd58ee440ab640a89111cea988&url=https%3a%2f%2f247wallst.com%2finvesting%2f2026%2f11%2f12%2fthe-treasury-secretary-is-now-living-on-a-military-base-after-iranian-threats%2f&c=11866179984473508006&mkt=en-us)  
  <sub>24/7 Wall St., 29h ago</sub>  
  Markets barely flinched when news broke that a cabinet secretary had moved onto a military base. Yet the quiet in oil and long bonds may hide a bigger risk for anyone holding USO or TLT, and a few ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 79.25 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 81.09 (-2.3%), 50d 80.21 (-1.2%), 200d 84.29 (-6.0%); 50d below 200d
Momentum: RSI(14) 38.2 | MACD 0.103 vs signal 0.354 (histogram -0.251)
Returns: 1d -0.6% | 5d -3.3% | 1m -0.9% | 3m -2.6%
52-week range: 77.11 - 90.82 (now 15.6% of the way up)
Volatility: ATR(14) 0.79 (1.0% of price) | annualised 20d 12.6%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Long Government
Yield: 4.8%
Credit quality: AA 100.0% | US government debt 99.5%
Three-year record: +1.5% a year | beta to the market 2.30
Cost and size: expense ratio 0.15% | net assets 47.52B
What it is made of: Bonds 99.5%, Cash 0.5%
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
Contract: ULTRA UST BOND - CHICAGO BOARD OF TRADE (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 33.3% of open interest (2,394,358 contracts)
Change on the week: +1.1% of open interest
Crowding: 55% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 109.70M | fund size: 8.69B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US dollar index rose 0.95% on the week, hitting an 18‑month peak, supporting a bullish outlook for a dollar index fund
- Technical indicators show price above 20‑day, 50‑day and 200‑day SMAs with RSI 67.9 and positive MACD, indicating continued uptrend but no decisive break on volume
- Large speculators net long 6.7% of open interest with only a +0.2% change week‑over‑week, indicating modest bullish positioning
- Analyst view provides no rating or price target, offering no directional guidance

<details><summary><b>News</b> — score +0.00</summary>

- [What Lifted Invesco DB US Dollar Index Bullish Fund (NYSEARCA:UUP) as the Dollar Hit an 18-Month Peak and the Yen Passed 160?](https://kalkine.com.au/news/economic-news/what-lifted-invesco-db-us-dollar-index-bullish-fund-nysearcauup-as-the-dollar-hit-an-18-month-peak-and-the-yen-passed-160)  
  <sub>Kalkine, 3 hours ago</sub>  
  What Lifted Invesco DB US Dollar Index Bullish Fund (NYSEARCA:UUP) as the Dollar Hit an 18-Month Peak and the Yen Passed 160?
- [Why Did the Dollar Reach an 18-Month Peak as the Yen Passed 160, Lifting Invesco DB US Dollar Index Bullish Fund (NYSEARCA:UUP)?](https://kalkine.ca/news/economic-news/why-did-the-dollar-reach-an-18-month-peak-as-the-yen-passed-160-lifting-invesco-db-us-dollar-index-bullish-fund-nysearcauup)  
  <sub>kalkine.ca, 3 hours ago</sub>  
  Why Did the Dollar Reach an 18-Month Peak as the Yen Passed 160, Lifting Invesco DB US Dollar Index Bullish Fund (NYSEARCA:UUP)?

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.45 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 29.06 (+1.3%), 50d 28.80 (+2.3%), 200d 28.03 (+5.1%); 50d above 200d
Momentum: RSI(14) 67.9 | MACD 0.134 vs signal 0.102 (histogram 0.032)
Returns: 1d +0.1% | 5d +1.1% | 1m +1.5% | 3m +4.8%
52-week range: 26.47 - 29.45 (now 100.0% of the way up)
Volatility: ATR(14) 0.13 (0.4% of price) | annualised 20d 5.5%
Volume: 0.04x the 20-day average
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
Three-year record: +4.2% a year | beta to the market -7.93
Cost and size: expense ratio 0.75% | net assets 481.36M
What it is made of: Cash 100.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 49.5%
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
Rolled up from the 1 largest holdings, 49.5% of the fund by weight
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
Contract: USD INDEX - ICE FUTURES U.S. (positions as of 2026-11-03, published the following Friday)
Large speculators: net long 6.7% of open interest (49,091 contracts)
Change on the week: +0.2% of open interest
Crowding: 87% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -1.4% (-7.02M) over 7d | 1 month: +10.5% (45.79M) over 30d
Shares outstanding: 16.41M | fund size: 483.14M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals lack decisive break on volume, positioning modest and mixed, flows negative, analyst coverage thin.

**Main reasons it gave:**
- US inflation 3.7% and unemployment 4.1% were in line with expectations, no macro surprise
- Technicals: price above 20‑day, 50‑day, 200‑day SMAs (+1.3%) but volume 0.04× 20‑day average, indicating weak conviction
- CFTC positioning: net short 2.6% of open interest, down 2.8% points week‑over‑week, still a small short bias
- Fund flows: share count down 4.2% over the past month, indicating net outflows
- Analyst coverage thin (12% of fund) despite 85.7% buy rating and +23.6% price target

<details><summary><b>News</b> — score +0.00</summary>

- [vanguard ftse europe etf - usd dis - VGK](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af7227984fb4527817618fc2bd0668c&url=https%3a%2f%2fwww.foxbusiness.com%2fquote%3fstockTicker%3dVGK&c=9021893360824891178&mkt=en-us)  
  <sub>Fox Business, 31h ago</sub>  
  Usd Dis (VGK) stock quote and chart. View real-time stock prices & the company’s financial overview to help with your trading & investment.
- [欧洲ETF-Vanguard MSCI收跌0.61%，成交额2.02亿美元](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af7227984fb4527817618fc2bd0668c&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fusstock%2fnotice%2f2026-11-13%2fdoc-iniypqyq8165788.shtml&c=10695651672828518478&mkt=en-us)  
  <sub>新浪财经, 23h ago</sub>  
  11月13日，欧洲ETF-Vanguard MSCI（VGK）收跌0.61%，报88.91美元，成交额2.02亿美元，市值301.34亿美元。 声明：市场有风险，投资需谨慎。本文基于第三方数据库发布，不代表新浪财经观点，任何在本文出现的信息均只作为参考，不构成个人投资建议。如有出入请以实际公告为准。如有疑问，请联系biz@staff.sina.com.cn。

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 89.10 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 87.97 (+1.3%), 50d 87.95 (+1.3%), 200d 87.96 (+1.3%); 50d below 200d
Momentum: RSI(14) 54.5 | MACD 0.471 vs signal 0.269 (histogram 0.202)
Returns: 1d +0.2% | 5d +2.1% | 1m +2.2% | 3m -3.3%
52-week range: 77.90 - 93.19 (now 73.3% of the way up)
Volatility: ATR(14) 1.09 (1.2% of price) | annualised 20d 20.2%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Europe Stock
What it holds: P/E 17.26 | P/B 2.24 | P/S 1.59 | 3y earnings growth n/a
Yield: 2.9%
Three-year record: +19.0% a year | beta to the market 0.88
Cost and size: expense ratio 0.06% | net assets 37.08B
What it is made of: Stocks 99.0%, Cash 0.7%, Other 0.3%
Largest holdings: ASML Holding NV 4.5%, HSBC Holdings PLC 2.2%, Roche Holding AG Ordinary Shares new 1.9%, Shell PLC 1.8%, Novartis AG Registered Shares 1.7%
Sector mix: Financial services 25.4%, Industrials 19.5%, Healthcare 12.1%, Technology 9.4%
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
Rolled up from the 5 largest holdings, 12.1% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 85.7% | hold 14.3% | sell 0.0% (mean 2.04 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.6% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, SHEL.L, NOVN.SW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.45</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 2.6% of open interest (505,889 contracts)
Change on the week: -2.8% of open interest
Crowding: 22% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.45</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +0.5% (195.06M) over 7d | 1 month: -4.2% (-1.60B) over 31d
Shares outstanding: 414.98M | fund size: 36.97B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US Treasury yields rose across the curve (+0.12% 3‑month, +0.31% 10‑year) indicating tightening
- VWO price below 20‑day, 50‑day and 200‑day SMAs, with volume at 0.03× 20‑day average
- Analyst coverage thin (23.5% of fund) despite 100% buy rating and +53% price target
- CFTC large speculators net long 1.1% of open interest, up 0.6% week‑over‑week

<details><summary><b>News</b> — score +0.00</summary>

- [VWO vs IXUS: Does Emerging Markets Focus or Broad International Exposure Make for a Better ETF Now?](https://www.fool.com/coverage/etfs/2026/11/12/vwo-vs-ixus-emerging-markets-focus-or-broad-international-exposure/)  
  <sub>The Motley Fool, 19 hours ago</sub>  
  Comparing the Vanguard FTSE Emerging Markets ETF (VWO -1.38%) against the iShares Core MSCI Total International Stock ETF (IXUS -0.91%) highlights a choice...
- [Does Vanguard or iShares Have the Better Emerging Markets ETF?](https://www.fool.com/coverage/etfs/2026/11/12/does-vanguard-or-ishares-have-the-better-emerging-markets-etf/)  
  <sub>The Motley Fool, 16 hours ago</sub>  
  The Vanguard FTSE Emerging Markets ETF (VWO -1.38%) offers a significantly lower expense ratio and broader diversification, while the iShares MSCI Emerging...
- [ETFs Investing in Sany Heavy Industry Co., Ltd. Class H Stocks](https://www.google.com/goto?url=CAESbwHEIkXXHqodgUUoUACN_cPhMRS9vvLyxEyKGM3c_muZuI11VqmCAu8jox7f5fEAD9JSe0nY92a1N8lsnpkOc7X4aBXUDR1NiKdJGAfOTxBAg2SJ5vkBJvry9s15x-VlzA8UPvWLFfdItp67MhcHug&gsessionid=5F-mHxkAQiNvXUo9XTxhIgX360PMfCHYNx58OU9tIP2-3-qCq9IQww)  
  <sub>TradingView, 23 hours ago</sub>  
  Explore funds investing in 1741 in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [SPDW vs IXUS: Which International ETF Is the Better Buy for 2027?](https://www.google.com/goto?url=CAESqwEBxCJF18cCuI5dSjzk54bhSPBrkKXckSYRZkNXKhJe6L9PPNWAI_h5Bfq4_0FSzkFvPZ-MT5sQ7bsz0heGTUQllWDul-cZIPfmBI64rx6_gcjC52VnSd0I71o0wlizIIHJdojFLyFwOXm2dq-tvLy1tcGPCb5azCxXhM_89wkJp1_xx2p8FmKsJdQsBbkQG1q9VriTYXxDhFHtdbj1EVZG9pLEDw2ZI1x2WfY&gsessionid=5F-mHxkAQiNvXUo9XTxhIgX360PMfCHYNx58OU9tIP2-3-qCq9IQww)  
  <sub>The Motley Fool, 17 hours ago</sub>  
  The State Street SPDR Portfolio Developed World ex-US ETF (SPDW -0.68%) offers lower costs and a focus on developed markets, while the iShares Core MSCI...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 56.34 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 56.53 (-0.3%), 50d 58.54 (-3.8%), 200d 58.30 (-3.4%); 50d above 200d
Momentum: RSI(14) 45.1 | MACD -0.661 vs signal -0.836 (histogram 0.175)
Returns: 1d -0.2% | 5d +1.9% | 1m -4.2% | 3m -6.7%
52-week range: 52.42 - 61.44 (now 43.5% of the way up)
Volatility: ATR(14) 0.85 (1.5% of price) | annualised 20d 23.0%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Diversified Emerging Mkts
What it holds: P/E 16.13 | P/B 2.13 | P/S 1.85 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +16.5% a year | beta to the market 0.78
Cost and size: expense ratio 0.06% | net assets 153.78B
What it is made of: Stocks 95.8%, Cash 4.0%, Other 0.1%, Preferred 0.0%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 15.7%, Tencent Holdings Ltd 2.8%, Alibaba Group Holding Ltd Ordinary Shares 2.1%, MediaTek Inc 1.9%, Delta Electronics Inc 0.9%
Sector mix: Technology 33.8%, Financial services 19.5%, Consumer cyclical 9.3%, Industrials 7.5%
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
Rolled up from the 5 largest holdings, 23.5% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +53.3% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 2308.TW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-11-03, published the following Friday)
Large speculators: net long 1.1% of open interest (1,048,229 contracts)
Change on the week: +0.6% of open interest
Crowding: 22% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 1.42B | fund size: 79.90B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Sweden (EWD) · Sector or country — BULLISH, confidence 0.40

**Result:** ACCEPTED · 134 shares · submitted buy 134 EWD @ ~52.51, stop 50.94

**In the model's own words:**

> Positive inflows, strong analyst consensus, bullish technical trend, solid fundamentals

**Main reasons it gave:**
- Strong inflows: share count +10.6% month
- Analyst consensus 100% buy with +8.3% price target
- Price above 20d, 50d, 200d SMAs indicating bullish trend
- Fund fundamentals: P/E 14.5, 3.5% yield, 21.3% annualized 3-year return

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI Netherlands ETF (EWN) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/EWN/)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Find the latest iShares MSCI Netherlands ETF (EWN) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 52.67 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 52.00 (+1.3%), 50d 51.46 (+2.3%), 200d 51.55 (+2.2%); 50d below 200d
Momentum: RSI(14) 54.7 | MACD 0.504 vs signal 0.429 (histogram 0.074)
Returns: 1d +0.1% | 5d +1.7% | 1m +3.0% | 3m +0.4%
52-week range: 45.38 - 54.72 (now 78.1% of the way up)
Volatility: ATR(14) 0.78 (1.5% of price) | annualised 20d 22.1%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.53 | P/B 2.82 | P/S 2.81 | 3y earnings growth n/a
Yield: 3.5%
Three-year record: +21.3% a year | beta to the market 1.18
Cost and size: expense ratio 0.51% | net assets 1.10B
What it is made of: Stocks 99.2%, Cash 0.8%
Largest holdings: Spotify Technology SA 11.4%, Volvo AB Class B 6.4%, Atlas Copco AB Class A 6.2%, Sandvik AB 4.9%, Assa Abloy AB Class B 4.9%
Sector mix: Industrials 44.1%, Financial services 25.0%, Communication services 15.2%, Technology 6.9%
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
Rolled up from the 5 largest holdings, 33.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.97 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +8.3% above the current prices
Holdings read: SPOT, VOLV-B.ST, ATCO-A.ST, SAND.ST, ASSA-B.ST
Recent rating changes among them:
  - SPOT: 2026-10-23 Morgan Stanley: main, Overweight -> Overweight
  - ASSA-B.ST: 2015-12-09 Barclays: main, ? -> Equal-Weight
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
Share count change: 1 week: +1.1% (11.48M) over 7d | 1 month: +10.6% (105.01M) over 31d
Shares outstanding: 20.73M | fund size: 1.09B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — BULLISH, confidence 0.30

**Result:** ACCEPTED · 120 shares · submitted buy 120 XLF @ ~58.53, stop 56.75

**In the model's own words:**

> Overall bullish tilt based on strong analyst coverage, positive technicals, recent net buying, and a macro backdrop that supports financials, while fund flows are flat indicating neutral demand.

**Main reasons it gave:**
- Analyst view: 100% buy rating on top holdings with +5% price target
- Technicals: price above 20‑, 50‑, 200‑day SMAs, RSI 61, MACD positive
- Recent net buying of $369.2M in XLF
- Fund flows flat (0% change week/month), indicating neutral demand
- Macro: yields rising across curve, normal upward slope, supportive for financials

<details><summary><b>News</b> — score +0.20</summary>

- [State Street Fin Sel Sector SPDR (XLF) Buys $49.1 Million More BRK.B on Wednesday](https://finance.yahoo.com/markets/stocks/articles/state-street-fin-sel-sector-110345040.html)  
  <sub>4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Financial Select Sector SPDR ETF (XLF) recorded net buying of $369.2 million on Wednesday, Nov.
- [Lazard, Piper Sandler lead financial stocks with longest Sell streaks (XLF:NYSEARCA)](https://seekingalpha.com/news/4672284-lazard-piper-sandler-lead-financial-stocks-with-longest-sell-streaks)  
  <sub>2 hours ago</sub>  
  Ten financial stocks carry Sell or Strong Sell Quant ratings; Lazard leads with a 298-day Sell streak, while UWM Holdings has a 94-day Strong Sell.
- [Better U.S. Bank ETF: State Street's KBE vs. First Trust's FTXO](https://www.google.com/goto?url=CAESlQEBxCJF1wu8OGbwbMARlwRfViuh9PivURKqBumDb2F3ohE6lRshxer0h_Kr9GYbV1ziLKEbt4c7csfe4u_cvhVlMO-WIY3sGZOzxj282NFWD3oGRviqTDT6_ZbIvLwG68_7KxMfYZuxDHplMycYBpIb8w7FhSb2qU86Yo7v0OPIxYPU30BD4L4pbtOKYdqQ3W4Xo_N3Fw&gsessionid=fPNN_uZOtgiaF7DCad9RZI9VFq-7uVBwcBZdykJwAY8F1rPmwrO9wQ)  
  <sub>10 hours ago</sub>  
  The State Street SPDR S&P Bank ETF (NYSEMKT:KBE) offers a more diversified, lower-cost entry into the banking sector compared to the concentrated and...
- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Friday as Producer Inflation Trails Forecasts](https://www.google.com/goto?url=CAESpwEBxCJF1_VjDa8v9O-DJX-8cWm-8IIBUGeokCBRk0UVFhQpxleIQW7_vp3m2lFOhDcyTxixhs3_HycLfJTOiP18QHTfrEUOiu9QZsXZhhfNt4tV8trVYV3TnK11sJxN9Kw8fumsSK5tUxuKXn9W6gia3Y9-iCJciiZp7z7tuy_webQB7Qi6hlCQscyMkbkURppM5ZMNREJhE-Ki_mEyohBHo17laNhvCw&gsessionid=fPNN_uZOtgiaF7DCad9RZI9VFq-7uVBwcBZdykJwAY8F1rPmwrO9wQ)  
  <sub>34 minutes ago</sub>  
  Thebroad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.4% and the actively traded Invesco QQQ Trust (QQQ) was 0.2% higher in Friday's...
- [Dow Futures Rise After Resilient Session; AMD, Arista Are Buys](https://www.google.com/goto?url=CAESyAEBxCJF1y3yI0hNcHDu0TjA6w0evU62ouerYrgtA4aJviJVqjqnJZ3oqqxHnzQgzBx0c50mUdpohYF4ZM9hZhgTmp9vgLZ7rAGUXEs04Eg8RungynXKywy732-vBl8d3skcdVC08_uUbN7HEbAJYj3roUU2pDffQnRDHqTLRca6s9dNRctbIsQT29rIzbdXw6JrFg3_yDiLU-rUKbfPUVCn4FagUyxmpMczcGps0gmePdZrpc6OvlaX3wISlmiyd1tYu_KatqBrAg&gsessionid=fPNN_uZOtgiaF7DCad9RZI9VFq-7uVBwcBZdykJwAY8F1rPmwrO9wQ)  
  <sub>2 hours ago</sub>  
  Dow Jones futures: The stock market held up well given Nvidia CEO Huang's exit, surging yields and more. A SpaceX-Tesla deal may be close.
- [XLF Sep 2027 50.000 put (XLF270917P00050000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScwHEIkXXE2qUBD0QmMhi3uDsMCM33J8760uGhkvN4OeWnWIsLDilzt2omIOKiYU_s9HZPmWFQLgnFpnO3Gm8q82LkQf07aHEDdF87Rasttvb_qoh0A5G2LL_QLgr_rc6d5cqvGtncJDebhVvCNIzNZYJYPE&gsessionid=fPNN_uZOtgiaF7DCad9RZI9VFq-7uVBwcBZdykJwAY8F1rPmwrO9wQ)  
  <sub>21 hours ago</sub>  
  Find the latest XLF Sep 2027 50.000 put (XLF270917P00050000) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.50</summary>

```text
Last close 58.55 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 57.06 (+2.6%), 50d 55.96 (+4.6%), 200d 53.95 (+8.5%); 50d above 200d
Momentum: RSI(14) 61.2 | MACD 0.786 vs signal 0.645 (histogram 0.141)
Returns: 1d +0.6% | 5d +2.4% | 1m +5.9% | 3m +1.7%
52-week range: 47.81 - 59.20 (now 94.3% of the way up)
Volatility: ATR(14) 0.89 (1.5% of price) | annualised 20d 21.6%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Financial
What it holds: P/E 15.26 | P/B 2.28 | P/S 3.26 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +21.9% a year | beta to the market 0.68
Cost and size: expense ratio 0.08% | net assets 53.58B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Berkshire Hathaway Inc Class B 12.7%, JPMorgan Chase & Co 11.2%, Visa Inc Class A 8.8%, Mastercard Inc Class A 6.5%, Bank of America Corp 4.1%
Sector mix: Financial services 98.2%, Technology 1.6%, Industrials 0.3%
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
Rolled up from the 5 largest holdings, 43.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.86 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +5.0% above the current prices
Holdings read: BRK-B, JPM, V, MA, BAC
Recent rating changes among them:
  - BRK-B: 2026-10-22 UBS: main, Buy -> Buy
  - JPM: 2026-11-02 UBS: main, Buy -> Buy
  - V: 2026-11-11 Bernstein: main, Outperform -> Outperform
  - MA: 2026-11-11 Bernstein: main, Outperform -> Outperform
  - BAC: 2026-11-02 UBS: main, Buy -> Buy
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
Shares outstanding: 883.44M | fund size: 51.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise or decisive technical break is present; bullish analyst view and strong inflows are offset by a steep downtrend, low volume, and a macro backdrop of rising yields and a stronger dollar.

**Main reasons it gave:**
- Analyst coverage of top 5 holdings (51% of fund) is 100% buy with +64% price target
- Fund flows show weekly share count increase of +6.5% (37.81M shares) over 7 days
- Technicals: price 19.5% below 200‑day SMA, RSI 25.8 (oversold), volume 0.09× 20‑day average
- Macro: US Treasury yields rose across the curve, dollar index up +0.95% on the week, inflation 3.7% above Fed target

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 73.21 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 79.72 (-8.2%), 50d 86.23 (-15.1%), 200d 90.91 (-19.5%); 50d below 200d
Momentum: RSI(14) 25.8 | MACD -3.974 vs signal -3.517 (histogram -0.457)
Returns: 1d +0.8% | 5d -0.6% | 1m -16.7% | 3m -19.8%
52-week range: 72.62 - 102.94 (now 1.9% of the way up)
Volatility: ATR(14) 2.04 (2.8% of price) | annualised 20d 31.0%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.90 | P/B 1.59 | P/S 1.22 | 3y earnings growth n/a
Yield: 1.3%
Three-year record: +24.0% a year | beta to the market 0.44
Cost and size: expense ratio 0.59% | net assets 620.12M
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: MercadoLibre Inc 22.2%, YPF SA ADR 10.6%, Vista Energy SAB de CV ADR 8.2%, Grupo Financiero Galicia SA ADR 5.4%, Pampa Energia SA ADR 4.8%
Sector mix: Consumer cyclical 28.3%, Energy 22.6%, Financial services 13.7%, Basic materials 10.3%
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 51.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.60 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +64.2% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, PAM
Recent rating changes among them:
  - MELI: 2026-11-11 UBS: main, Neutral -> Neutral
  - YPF: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-10-13 UBS: main, Neutral -> Neutral
  - PAM: 2026-11-02 JP Morgan: main, Neutral -> Neutral
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.70</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +6.5% (37.81M) over 7d | 1 month: +3.5% (20.60M) over 30d
Shares outstanding: 8.41M | fund size: 616.00M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error response body was rejected) (Bing's feed, direct: 0 headline(s), none naming ARGT)

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, technicals weak, flat flows, modest analyst bullishness limited to 39.6% coverage.

**Main reasons it gave:**
- Flat fund flows (share count unchanged over week and month)
- Price below 20‑day, 50‑day, and 200‑day SMAs; low volume
- US Treasury yields rose across curve; no surprise macro data
- Analyst consensus 100% buy covering 39.6% of fund

<details><summary><b>News</b> — score +0.00</summary>

- [Lang & Schwarz: Der irre Sparplan-Effekt beim Trade-Republic-Verlierer](https://www.wiwo.de/finanzen/boerse/lang-schwarz-der-irre-sparplan-effekt-beim-trade-republic-verlierer/100264550.html)  
  <sub>WirtschaftsWoche, 6 hours ago</sub>  
  Nach dem Ende der Exklusivstellung bei Trade Republic ist das Geschäft des Börsenbetreibers Lang & Schwarz kollabiert. Ausgerechnet die neue ETF-Rente...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 113.02 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 116.52 (-3.0%), 50d 119.88 (-5.7%), 200d 122.90 (-8.0%); 50d below 200d
Momentum: RSI(14) 42.4 | MACD -1.993 vs signal -1.963 (histogram -0.030)
Returns: 1d -0.9% | 5d +1.4% | 1m -5.9% | 3m -7.7%
52-week range: 99.40 - 137.69 (now 35.6% of the way up)
Volatility: ATR(14) 2.34 (2.1% of price) | annualised 20d 36.1%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.09 | P/B 2.45 | P/S 2.45 | 3y earnings growth n/a
Yield: 1.6%
Three-year record: +33.4% a year | beta to the market 0.98
Cost and size: expense ratio 0.59% | net assets 838.23M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Teva Pharmaceutical Industries Ltd 12.6%, Bank Leumi Le-Israel BM 8.6%, Bank Hapoalim BM 7.8%, Elbit Systems Ltd 5.6%, Tower Semiconductor Ltd 5.1%
Sector mix: Financial services 34.6%, Technology 18.0%, Healthcare 13.1%, Industrials 10.8%
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.00 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.5% above the current prices
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
Shares outstanding: 2.55M | fund size: 288.20M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Overall neutral; analyst view slightly bearish, modest inflows slightly bullish, fundamentals neutral, no macro surprise or decisive technical break.

**Main reasons it gave:**
- Analyst view: 57.4% hold, 42.6% sell, weighted price target -9.5% vs current price
- Fund flows: slight net inflow of +0.8% week and +0.4% month
- Technicals: price above 50‑day and 200‑day SMA, but below 20‑day SMA; RSI 48.5 (neutral), MACD slightly bearish
- Macro: no surprise data or policy shift; yields up modestly, dollar stronger, VIX down but still elevated

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.11 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 29.32 (-0.7%), 50d 28.98 (+0.5%), 200d 29.00 (+0.4%); 50d below 200d
Momentum: RSI(14) 48.5 | MACD 0.100 vs signal 0.135 (histogram -0.035)
Returns: 1d -0.3% | 5d -0.2% | 1m +1.1% | 3m -1.5%
52-week range: 24.95 - 30.43 (now 76.0% of the way up)
Volatility: ATR(14) 0.33 (1.1% of price) | annualised 20d 16.7%
Volume: 0.05x the 20-day average
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
Three-year record: +15.1% a year | beta to the market 0.94
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
Weighted price target: -9.5% above the current prices
Holdings read: BHP.AX, CBA.AX, NAB.AX, WBC.AX, ANZ.AX
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
Direction: flat (1 month)
Share count change: 1 week: +0.8% (9.91M) over 7d | 1 month: +0.4% (4.34M) over 31d
Shares outstanding: 42.46M | fund size: 1.24B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, mixed technicals, and moderate fundamentals. Analyst view is bullish but not decisive enough to shift the call.

**Main reasons it gave:**
- Flat fund flows (no net creation/redemption)
- No macro surprise (yields up modestly, inflation within expectations)
- Mixed technicals: price above SMAs but 50‑day SMA below 200‑day SMA and low volume
- Analyst view bullish (78% buy, +15% price target) but not decisive

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI United Kingdom ETF (EWU) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/EWU/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Find the latest iShares MSCI United Kingdom ETF (EWU) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 42.94 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 42.10 (+2.0%), 50d 42.02 (+2.2%), 200d 42.20 (+1.8%); 50d below 200d
Momentum: RSI(14) 56.3 | MACD 0.317 vs signal 0.196 (histogram 0.121)
Returns: 1d +0.3% | 5d +3.3% | 1m +3.4% | 3m -2.3%
52-week range: 38.08 - 44.59 (now 74.7% of the way up)
Volatility: ATR(14) 0.62 (1.4% of price) | annualised 20d 24.1%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.50 | P/B 1.87 | P/S 1.23 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +20.2% a year | beta to the market 0.95
Cost and size: expense ratio 0.49% | net assets 1.57B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: SAP SE 12.7%, Siemens AG 11.4%, Allianz SE 9.9%, Siemens Energy AG Ordinary Shares 5.8%, Deutsche Telekom AG 5.3%
Sector mix: Industrials 27.2%, Financial services 23.5%, Technology 16.9%, Healthcare 7.6%
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

```text
Rolled up from the 5 largest holdings, 45.1% of the fund by weight
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.93 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.2% above the current prices
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
Shares outstanding: 79.50M | fund size: 3.41B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst ratings: 90.8% buy, weighted price target +11.9% above current price
- Fund outflows: -0.4% week, -2.7% month indicating net redemption pressure
- Technicals: price near 200‑day SMA, RSI 54.3, MACD positive but low volume, no decisive break
- Macro: US Treasury yields up across curve, VIX down but still elevated, no surprise data releases

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI Italy ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af72515653b4f83a03d06a4b8489037&url=https%3a%2f%2fwww.barrons.com%2fmarket-data%2ffunds%2fewi&c=10563642463261866545&mkt=en-us)  
  <sub>Barron's, 84h ago</sub>  
  Stocks: Real-time U.S. stock quotes reflect trades reported through Nasdaq only; comprehensive quotes and volume reflect trading in all markets and are delayed at least 15 minutes. International stock ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 58.29 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 56.82 (+2.6%), 50d 58.17 (+0.2%), 200d 58.29 (+0.0%); 50d below 200d
Momentum: RSI(14) 54.3 | MACD 0.244 vs signal -0.121 (histogram 0.365)
Returns: 1d +0.0% | 5d +3.1% | 1m +3.2% | 3m -7.6%
52-week range: 50.70 - 63.35 (now 60.0% of the way up)
Volatility: ATR(14) 0.93 (1.6% of price) | annualised 20d 28.9%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.58 | P/B 1.75 | P/S 1.42 | 3y earnings growth n/a
Yield: 3.4%
Three-year record: +27.7% a year | beta to the market 0.92
Cost and size: expense ratio 0.50% | net assets 1.19B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: UniCredit SpA 16.4%, Intesa Sanpaolo 13.8%, Enel SpA 11.7%, Eni SpA 5.5%, Generali 4.8%
Sector mix: Financial services 50.9%, Utilities 18.2%, Industrials 11.9%, Consumer cyclical 8.4%
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
Rolled up from the 5 largest holdings, 52.1% of the fund by weight
Ratings by weight: buy 90.8% | hold 9.2% | sell 0.0% (mean 2.15 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.9% above the current prices
Holdings read: UCG.MI, ISP.MI, ENEL.MI, ENI.MI, G.MI
Recent rating changes among them: none reported
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
Share count change: 1 week: -0.4% (-4.52M) over 7d | 1 month: -2.7% (-32.61M) over 31d
Shares outstanding: 20.35M | fund size: 1.19B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, modest net‑long positioning, thin analyst coverage, and technicals lacking a decisive break all point to a neutral stance.

**Main reasons it gave:**
- Analyst coverage thin (17.2% of fund) despite 100% buy rating
- Positioning net long 8% of open interest, up 4.7% week
- Fund flows +5.5% share count over month indicating inflows
- Technical indicators: price below 20‑day SMA, RSI 43.6, no decisive break
- Macro: yields up modestly, VIX down 7.5% week, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Options Whale Alert: $255K Bullish Short Put Opened on $EWJ](https://www.moomoo.com/news/post/1004554359/options-whale-alert-255k-bullish-short-put-opened-on-ewj)  
  <sub>Moomoo, 7 hours ago</sub>  
  iSharesMSCI Japan ETF(EWJ.US)$ closed down 0.71% at $91.47. A trader sold 1000 Nov 27, 2026 $93.50 puts to open a Short Put. The position carries a net...
- [If Japan's Stock Market Rally Returns, These 3 ETFs Could Benefit](https://www.marketbeat.com/articles/if-japans-stock-market-rally-returns-these-3-etfs-could-benefit/)  
  <sub>MarketBeat, 22 hours ago</sub>  
  The Nikkei 225 is up 17% YTD despite a recent pullback tied to AI volatility and Bank of Japan rate hikes. DXJ, EWJ, and DFJ each offer a distinct approach...
- [EWJ Nov 2026 89.000 put (EWJ261127P00089000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScwHEIkXXepFZW-LvMzYlhFkuuDywDhLdqQqvpsraFptfDOq_Zv7cTchhTOhoLKQAHnA337DSYZ8H7GcaxNDNMvONdcqVwU40hmuIxiPjr05zhlmhl1qQVgWnJNiVkxPshUmHqsHxrXnm2WRo6OGEq-G4Kns&gsessionid=ycV10g2csw2sWQy_s4PmmUp5tH5iyxqdCeXEgTdEyJWdyMuC1aFX9Q)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Find the latest EWJ Nov 2026 89.000 put (EWJ261127P00089000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Asian equities retreat amid Nvidia turmoil and rising yields ahead of Anthropic IPO; Bitcoin drops below $70K](https://www.google.com/goto?url=CAESzwEBxCJF13hYW4-mRAQfhGVn78GB9qdqimiSpbJnK9VmIgeaRq423TVtNL6WWTrEjAh8lxiu-a2k9DxIR5BtpX_Nuj8j04Etow88NmT7ih2ADjv8NJrTBXI-GKoz2UZ5nOo-Dnyhq-R_uq1wikZSRWmWRk2xtiNWsh6usbw00GOXr5d3CHk5kFWneB4TUhwgHksnSMC71wJPpQ7f-BUu0gk1MFZ63L2E2C3a7mM4huCuCyt6he3p6iH5p9C9tbQ67S-PNDkt3_KyTKkRoNJ6UkA&gsessionid=ycV10g2csw2sWQy_s4PmmUp5tH5iyxqdCeXEgTdEyJWdyMuC1aFX9Q)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  Asian equity markets traded mostly lower following a weak Wall Street lead triggered by sudden leadership turmoil at Nvidia, though Japan bucked the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 91.63 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 93.01 (-1.5%), 50d 95.65 (-4.2%), 200d 92.10 (-0.5%); 50d above 200d
Momentum: RSI(14) 43.6 | MACD -1.388 vs signal -1.348 (histogram -0.040)
Returns: 1d +0.2% | 5d +3.8% | 1m -4.0% | 3m -6.7%
52-week range: 79.49 - 99.32 (now 61.2% of the way up)
Volatility: ATR(14) 1.55 (1.7% of price) | annualised 20d 29.1%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Japan Stock
What it holds: P/E 15.14 | P/B 1.95 | P/S 1.31 | 3y earnings growth n/a
Yield: 3.8%
Three-year record: +18.5% a year | beta to the market 0.86
Cost and size: expense ratio 0.49% | net assets 23.40B
What it is made of: Stocks 99.2%, Cash 0.8%
Largest holdings: Mitsubishi UFJ Financial Group Inc 4.5%, Toyota Motor Corp 3.6%, Advantest Corp 3.1%, Recruit Holdings Co Ltd 3.1%, Sumitomo Mitsui Financial Group Inc 2.9%
Sector mix: Industrials 22.4%, Technology 20.6%, Financial services 19.1%, Consumer cyclical 12.0%
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
Rolled up from the 5 largest holdings, 17.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.0% above the current prices
Holdings read: 8306.T, 7203.T, 6857.T, 6098.T, 8316.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.25</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-03, published the following Friday)
Large speculators: net long 8.0% of open interest (26,231 contracts)
Change on the week: +4.7% of open interest
Crowding: 55% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.25</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +1.0% (238.40M) over 7d | 1 month: +5.5% (1.21B) over 31d
Shares outstanding: 254.42M | fund size: 23.31B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral call based on lack of macro surprise, modest analyst tilt, flat fund flows, and no decisive technical break.

**Main reasons it gave:**
- No macro surprise; yields rose modestly across the curve
- Technicals show price above 20‑day, 50‑day and 200‑day SMAs but low volume and no decisive MACD break
- Analyst view shows 64.8% buy rating but price target essentially flat (-0.1% above current)
- Fund flows flat with no net share creation or redemption

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 64.78 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 64.24 (+0.8%), 50d 61.88 (+4.7%), 200d 61.99 (+4.5%); 50d below 200d
Momentum: RSI(14) 57.4 | MACD 0.976 vs signal 1.025 (histogram -0.048)
Returns: 1d -0.2% | 5d +0.2% | 1m +4.5% | 3m +3.0%
52-week range: 55.69 - 66.56 (now 83.6% of the way up)
Volatility: ATR(14) 0.83 (1.3% of price) | annualised 20d 19.9%
Volume: 0.05x the 20-day average
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
Three-year record: +16.8% a year | beta to the market 0.82
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

<details><summary><b>What analysts and big funds say</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.00</summary>

```text
Rolled up from the 5 largest holdings, 49.6% of the fund by weight
Ratings by weight: buy 64.8% | hold 35.2% | sell 0.0% (mean 2.45 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -0.1% above the current prices
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
Shares outstanding: 28.62M | fund size: 1.85B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise, mixed technicals, flat fund flows, and moderate fundamentals.

**Main reasons it gave:**
- US Treasury yields rose 0.12-0.34% across the curve this week
- RSI(14) at 48.0 and MACD histogram positive but MACD below signal indicate neutral momentum
- Analyst ratings for top holdings are 100% buy covering 42.3% of fund weight with +56.2% price target
- Fund flows flat over past month (share count unchanged), indicating no net demand

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI Netherlands ETF (EWN) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/EWN/)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  iShares MSCI Netherlands ETF (EWN) · 2.82% · -1.65% · 1.47% · 13.92% · 10.06% · 22.56% · 296.76%. Key Events. Baseline. Advanced Chart. Loading chart for...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 64.93 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 64.78 (+0.2%), 50d 66.23 (-2.0%), 200d 65.17 (-0.4%); 50d above 200d
Momentum: RSI(14) 48.0 | MACD -0.297 vs signal -0.484 (histogram 0.186)
Returns: 1d +0.0% | 5d +2.4% | 1m -0.3% | 3m -9.2%
52-week range: 55.33 - 71.61 (now 59.0% of the way up)
Volatility: ATR(14) 1.09 (1.7% of price) | annualised 20d 25.5%
Volume: 0.00x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.38 | P/B 2.46 | P/S 1.73 | 3y earnings growth n/a
Yield: 4.4%
Three-year record: +21.7% a year | beta to the market 1.13
Cost and size: expense ratio 0.50% | net assets 597.52M
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ASML Holding NV 21.9%, ING Groep NV 8.6%, Prosus NV Ordinary Shares - Class N 4.7%, ASM International NV 3.8%, Nebius Group NV Shs Class-A- 3.4%
Sector mix: Technology 30.4%, Financial services 21.1%, Consumer defensive 11.8%, Industrials 11.0%
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
Rolled up from the 5 largest holdings, 42.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.58 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +56.2% above the current prices
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
Shares outstanding: 5.55M | fund size: 360.36M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no material macro surprise, flat fund flows, modest bullish technicals with very low volume, and analyst coverage showing modest optimism but limited to just over half of the fund.

**Main reasons it gave:**
- Flat fund flows (0% change in share count over week and month) indicate no net demand
- No macro surprise: US Treasury yields rose modestly, inflation 3.7% above target, no policy shift
- Technicals show price above 20‑day, 50‑day, 200‑day SMAs with RSI 57 and MACD positive, but volume is only 0.01× 20‑day average
- Analyst view: 76.3% buy rating and +6% price target for 53% of fund weight, indicating modest bullishness

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI United Kingdom ETF (EWU) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/EWU/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Find the latest iShares MSCI United Kingdom ETF (EWU) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 59.88 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 58.17 (+2.9%), 50d 59.24 (+1.1%), 200d 58.14 (+3.0%); 50d above 200d
Momentum: RSI(14) 57.1 | MACD 0.261 vs signal -0.119 (histogram 0.380)
Returns: 1d +0.4% | 5d +3.5% | 1m +2.6% | 3m -4.0%
52-week range: 49.37 - 63.23 (now 75.8% of the way up)
Volatility: ATR(14) 0.93 (1.5% of price) | annualised 20d 25.1%
Volume: 0.01x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 16.25 | P/B 2.19 | P/S 1.75 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +32.9% a year | beta to the market 0.91
Cost and size: expense ratio 0.50% | net assets 1.94B
What it is made of: Stocks 99.4%, Cash 0.6%
Largest holdings: Banco Santander SA 16.4%, Iberdrola SA 14.3%, Banco Bilbao Vizcaya Argentaria SA 12.6%, Repsol SA 5.3%, Industria De Diseno Textil SA Share From Split 4.6%
Sector mix: Financial services 40.5%, Utilities 22.9%, Industrials 14.9%, Technology 6.3%
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
Ratings by weight: buy 76.3% | hold 23.7% | sell 0.0% (mean 2.29 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.0% above the current prices
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
Shares outstanding: 37.35M | fund size: 2.24B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst rating: 100% buy, weighted price target +47.8% above current price
- Weekly outflow: -2.6% (-284.21M) over 7 days, recent net negative flow
- Macro: yields up across curve, dollar up, no policy surprise
- Technical: price below 20d and 50d SMA, RSI 43, no decisive break on volume

<details><summary><b>News</b> — score +0.00</summary>

- [First Trust Indxx Aerospace & Defense ETF (MISL) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/MISL/)  
  <sub>Yahoo! Finance Canada, 24 hours ago</sub>  
  Find the latest First Trust Indxx Aerospace & Defense ETF (MISL) stock quote, history, news and other vital information to help you with your stock trading...
- [Daily ETF Flows: CNEQ Tops Outflows List](https://www.etf.com/sections/daily-etf-flows/daily-etf-flows-cneq-tops-outflows-list)  
  <sub>ETF.com, 20 hours ago</sub>  
  Here are the daily ETF fund flows for November 11, 2026.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 97.02 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 100.86 (-3.8%), 50d 107.84 (-10.0%), 200d 94.67 (+2.5%); 50d above 200d
Momentum: RSI(14) 43.0 | MACD -3.767 vs signal -3.747 (histogram -0.020)
Returns: 1d -0.2% | 5d +8.7% | 1m -11.1% | 3m -10.0%
52-week range: 60.03 - 118.00 (now 63.8% of the way up)
Volatility: ATR(14) 3.76 (3.9% of price) | annualised 20d 63.8%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Greater China Region
What it holds: P/E 27.29 | P/B 4.22 | P/S 2.50 | 3y earnings growth n/a
Yield: 1.0%
Three-year record: +38.2% a year | beta to the market 1.35
Cost and size: expense ratio 0.59% | net assets 11.05B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 22.3%, MediaTek Inc 6.1%, Hon Hai Precision Industry Co Ltd 3.4%, ASE Technology Holding Co Ltd 3.0%, Delta Electronics Inc 2.9%
Sector mix: Technology 71.4%, Financial services 16.3%, Basic materials 4.4%, Industrials 2.6%
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

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

```text
Rolled up from the 5 largest holdings, 37.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.35 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +47.8% above the current prices
Holdings read: 2330.TW, 2454.TW, 2317.TW, 3711.TW, 2308.TW
Recent rating changes among them: none reported
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
Direction: money coming in (1 month)
Share count change: 1 week: -2.6% (-284.21M) over 7d | 1 month: +1.9% (198.13M) over 31d
Shares outstanding: 109.72M | fund size: 10.65B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: strong analyst buy rating (+14% price target) and solid fundamentals suggest bullishness, but recent net outflows and modest technical momentum temper the view. No material macro surprise or decisive technical break justifies a directional tilt.

**Main reasons it gave:**
- Analyst view: 100% buy rating covering 36.9% of fund, weighted price target +14% above current
- Fund flows: 1‑month net outflow of -1.6% (61.11M shares) indicating bearish demand
- Technicals: price above 20‑, 50‑ and 200‑day SMAs, RSI 53.3, modest upward momentum
- Macro: US Treasury yields rose modestly, VIX down, no major policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI United Kingdom ETF (EWU) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/EWU/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  iShares MSCI United Kingdom ETF (EWU) · -0.25% · 2.29% · 2.51% · 8.62% · 9.79% · 42.55% · 93.01%. Key Events. Baseline. Advanced Chart. Loading chart...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 48.02 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 47.75 (+0.6%), 50d 47.41 (+1.3%), 200d 47.09 (+2.0%); 50d above 200d
Momentum: RSI(14) 53.3 | MACD 0.170 vs signal 0.162 (histogram 0.008)
Returns: 1d +0.5% | 5d +1.7% | 1m +0.5% | 3m -0.3%
52-week range: 41.34 - 49.39 (now 83.0% of the way up)
Volatility: ATR(14) 0.62 (1.3% of price) | annualised 20d 20.7%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 16.62 | P/B 2.25 | P/S 1.41 | 3y earnings growth n/a
Yield: 3.1%
Three-year record: +20.1% a year | beta to the market 0.66
Cost and size: expense ratio 0.50% | net assets 3.73B
What it is made of: Stocks 98.5%, Other 1.0%, Cash 0.5%
Largest holdings: Shell PLC 9.9%, HSBC Holdings PLC 9.3%, AstraZeneca PLC 8.9%, Unilever PLC 4.4%, Rolls-Royce Holdings PLC 4.4%
Sector mix: Financial services 23.2%, Consumer defensive 15.3%, Energy 14.3%, Healthcare 13.9%
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
Rolled up from the 5 largest holdings, 36.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.08 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.0% above the current prices
Holdings read: SHEL.L, HSBA.L, AZN.L, ULVR.L, RR.L
Recent rating changes among them:
  - AZN.L: 2026-08-24 CICC: init, ? -> Outperform
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
Share count change: 1 week: +1.4% (51.96M) over 7d | 1 month: -1.6% (-61.11M) over 31d
Shares outstanding: 77.83M | fund size: 3.74B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no material macro surprise, flat fund flows, modest bullish technicals with low volume, and analyst coverage bullish but limited to <50% of the fund.

**Main reasons it gave:**
- Flat fund flows: 0.0% share count change over 1 week and 1 month
- US Treasury yields rose modestly, Fed target unchanged at 4.00% – no policy surprise
- Price above 20‑day, 50‑day, and 200‑day SMAs; RSI 64.8, MACD positive, but volume only 0.12× 20‑day average
- Analyst coverage 100% buy with +9% price target for 47.5% of fund weight

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 77.63 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 75.91 (+2.3%), 50d 74.40 (+4.3%), 200d 76.19 (+1.9%); 50d below 200d
Momentum: RSI(14) 64.8 | MACD 0.971 vs signal 0.748 (histogram 0.222)
Returns: 1d +0.0% | 5d +1.2% | 1m +5.1% | 3m +3.6%
52-week range: 65.87 - 81.23 (now 76.6% of the way up)
Volatility: ATR(14) 1.26 (1.6% of price) | annualised 20d 13.5%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 12.23 | P/B 1.88 | P/S 1.40 | 3y earnings growth n/a
Yield: 3.3%
Three-year record: +13.6% a year | beta to the market 0.99
Cost and size: expense ratio 0.50% | net assets 1.56B
What it is made of: Stocks 99.3%, Cash 0.7%
Largest holdings: Grupo Mexico SAB de CV Class B 14.9%, Grupo Financiero Banorte SAB de CV Class O 11.2%, Fomento Economico Mexicano SAB de CV Units Cons. Of 1 Shs-B- And 4 Shs-D- 8.9%, America Movil SAB de CV Ordinary Shares - Class B 7.9%, Cemex SAB de CV Cert Part Ord Repr 2 Shs-A- & 1 Shs-B- 4.6%
Sector mix: Consumer defensive 25.1%, Basic materials 24.7%, Financial services 18.1%, Industrials 12.7%
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
Rolled up from the 5 largest holdings, 47.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.0% above the current prices
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
Shares outstanding: 18.90M | fund size: 1.47B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, mixed technicals without decisive break, limited analyst coverage weight, modestly positive fundamentals.

**Main reasons it gave:**
- Fund flows flat: 0% net change in share count over 1 week and 1 month
- No macro surprise: Treasury yields rose modestly, Fed target unchanged, inflation 3.7% near expectations
- Technical indicators mixed: price below 20‑, 50‑ and 200‑day SMAs, RSI 46.8, MACD positive, but volume only 0.02× 20‑day average
- Analyst coverage bullish for only 41.8% of fund (100% buy, +29.7% price target) – limited weight
- Fund fundamentals modestly positive: P/E 10.65, yield 8.2%, three‑year return +26.8% per year

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 64.49 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 64.96 (-0.7%), 50d 65.76 (-1.9%), 200d 68.03 (-5.2%); 50d below 200d
Momentum: RSI(14) 46.8 | MACD 0.315 vs signal 0.125 (histogram 0.190)
Returns: 1d -1.3% | 5d -3.8% | 1m -0.8% | 3m -5.4%
52-week range: 60.43 - 81.60 (now 19.2% of the way up)
Volatility: ATR(14) 1.50 (2.3% of price) | annualised 20d 30.6%
Volume: 0.02x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.65 | P/B 1.96 | P/S 1.68 | 3y earnings growth n/a
Yield: 8.2%
Three-year record: +26.8% a year | beta to the market 1.12
Cost and size: expense ratio 0.59% | net assets 438.81M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Anglogold Ashanti PLC 11.3%, Naspers Ltd Class N 8.4%, Gold Fields Ltd 8.2%, Firstrand Ltd 7.5%, Standard Bank Group Ltd 6.4%
Sector mix: Financial services 36.0%, Basic materials 35.9%, Consumer cyclical 13.0%, Communication services 7.2%
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
Rolled up from the 5 largest holdings, 41.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.99 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +29.7% above the current prices
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
Shares outstanding: 7.90M | fund size: 509.46M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst view is offset by net outflows and a weak macro backdrop for gold, while technicals show no decisive break.

**Main reasons it gave:**
- Gold price fell ~3% to a one-year low as Treasury yields and dollar rose
- Fund flows show net outflows: -5.5% share count over past month
- Analyst coverage: 100% buy, weighted price target +19.4% (42% of fund)
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 46.4, no decisive break

<details><summary><b>News</b> — score +0.00</summary>

- [VanEck Gold Miners ETF (GDX) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GDX/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  VanEck Gold Miners ETF (GDX) · -4.56% · -7.56% · -15.75% · -5.76% · 6.69% · 135.85% · 124.10%. Key Events. Baseline. Advanced Chart.
- [Gold sinks to more than one-year low as Fed rate hike bets boost dollar, Treasury yields](https://seekingalpha.com/news/4671853-gold-sinks-to-more-than-one-year-low-as-fed-rate-hike-bets-boost-dollar-treasury-yields?utm_source=feed_news_all&utm_medium=referral&feed_item_type=news)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  Gold fell nearly 3% to their lowest in more than a year as Treasury yields, the dollar, and oil prices all gained after President Trump said the US does not...
- [Top Tokenized ETFs by Market Cap](https://www.google.com/goto?url=CAESXgHEIkXXQFQ-vd04djdz58cVwrQPp3tEnoJrOsA6Bu96ocmeZ17PcQ9pQnVmN3qYPyvpPTbB_pN2UNenmSwvdwuz2MUPzh91ztEgAVxOY0Sc0kHrU2UymYXLX4E9tFc&gsessionid=GbquHpE-ZA_NtGk3qPDhbsqLfww1ootRaNsZcs14ejmNhC-rJQAPFw)  
  <sub>CoinGecko, 14 hours ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap,...
- [Global X MSCI SuperDividend Emerging Markets ETF (SDEM) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZQHEIkXXo9iU_JDa_rpb3aK15mR_F-xlCy6QKAOYxEt5s6KiVUA7E9LbrygnKwbv8ZmkVjIquJ0R_NKUhiQ3XgZSr_YmUT_xarUv81jtOEWd_QG1WHHIRtvDL5KNMz9sBVyMX1hR&gsessionid=GbquHpE-ZA_NtGk3qPDhbsqLfww1ootRaNsZcs14ejmNhC-rJQAPFw)  
  <sub>Yahoo! Finance Canada, 2 hours ago</sub>  
  Find the latest Global X MSCI SuperDividend Emerging Markets ETF (SDEM) stock quote, history, news and other vital information to help you with your stock...
- [Nasdaq 100 Turns Green Despite Nvidia's 5% Drop on Huang Exit: Stock Market Today](https://www.google.com/goto?url=CAESyAEBxCJF1004X9xfOnUriAt9RpOsUE64MbAdqHrZynh9UD8AZqZ6x6RnUZ5LydiO4s9ZFbXzxLRe_oyF4_EPP6W4RXzi4mKrR84PeHlN1A5fJHXH1_IGLXE-XDqmgrXlSTHJoRiik5sG48XmociZMkZf-93UqR85OmnZmtNMc6Fz87dGh38y0SxCo8vhkb8omcz-k_cQpSgs_1n_rEjMqdLKRYVZ5UCh6ULovSHprz377P78h29tfGY1xRiZ8ivPqdyUPTBX4HqnyA&gsessionid=GbquHpE-ZA_NtGk3qPDhbsqLfww1ootRaNsZcs14ejmNhC-rJQAPFw)  
  <sub>TradingView, 21 hours ago</sub>  
  The Nasdaq 100 turned green Thursday even as Nvidia Corp. NASDAQ:NVDA plunged as much as 14.3% at the open, its steepest intraday drop since the DeepSeek...
- [𝗙𝗲𝗱 𝗛𝗮𝘄𝗸𝘀 𝗦𝗶𝗻𝗸 𝗠𝗲𝘁𝗮𝗹𝘀, 𝗖𝗿𝘂𝗱𝗲 𝗣𝗶𝘃𝗼](https://www.google.com/goto?url=CAESfQHEIkXXsteTZ12Iea49SVirrOaqjsbRv3a_WJJBI957rialJH6-RS3q61gFaklRacY74WoYjO7Jh2NIgpCSrerUwQMb1nCMixMZG_rrezqHjf9bFRwuqh6TkR6DzAUDRZvTWWUpG-1ExHZsKEfbt41Q_DXLXqlMlu2NZdcm&gsessionid=GbquHpE-ZA_NtGk3qPDhbsqLfww1ootRaNsZcs14ejmNhC-rJQAPFw)  
  <sub>KuCoin, 14 hours ago</sub>  
  Fed Hawks Sink Metals, Crude Pivots I closed my $PALL position for a small profit today, and I'm still holding my long in crude...
- [VanEck UCITS ETFs Plc - Net Asset Value(s)](https://www.google.com/goto?url=CAEShwEBxCJF17Y_YMnSpDviMr7fROO1kQNreW8UIMeYB6xtO0f4-Wk8D3akIuHpQ7qGRwQ0E8Xkl9M7BKRhs88ovyBy1U2Oe-e22_5YPNv50KjMIBHm1dkPWCHdV-2AI2M2FWnozg88sBxK9TyAA5ZrDrgmaKpXJWsbCLB01CchIiuPhjY4rVUBwAI&gsessionid=GbquHpE-ZA_NtGk3qPDhbsqLfww1ootRaNsZcs14ejmNhC-rJQAPFw)  
  <sub>Yahoo Finance UK, 3 hours ago</sub>  
  Fund Name. NAV Date. ISIN. Shares in Issue. Net Asset Value. NAV per Share. VanEck Emerging Markets High Yield Bond UCITS ETF. 2026-11-12. IE00BF541080.
- [Gold Price Forecast — XAU/USD ($3,871) $4,150 Upside Target on Fed Hike Bets & 103.08 Dollar High](https://www.google.com/goto?url=CAESpQEBxCJF11DmHpI4yegU5pzV9toHqg_JoByk95XhIoTQAvXSfMcH19qLjX67eHMHXiuRvziRpQ2JE5RNFolOBtxeIRPWfWrDxl533hp99miYCPY0PeR5lntkcPCZpSX8FIbztDvr8Hh5dOe1hAqP38oB1WO09CzWuWM5xJNXM6Vo5DUq5tkRCTmS2bXdARMz5J1FSueIGUIgCZ2cCARpLUE674mezpI&gsessionid=GbquHpE-ZA_NtGk3qPDhbsqLfww1ootRaNsZcs14ejmNhC-rJQAPFw)  
  <sub>TradingNEWS, 21 hours ago</sub>  
  Trading News Gold fell 2.90% to $3871.59 as the dollar index hit a 19-month high of 103.08 and December Fed hike odds reached 89% | That's TradingNEWS.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 82.83 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 83.51 (-0.8%), 50d 88.29 (-6.2%), 200d 89.59 (-7.5%); 50d below 200d
Momentum: RSI(14) 46.4 | MACD -0.784 vs signal -1.193 (histogram 0.409)
Returns: 1d +1.2% | 5d -5.4% | 1m -4.8% | 3m -9.9%
52-week range: 70.74 - 115.84 (now 26.8% of the way up)
Volatility: ATR(14) 3.38 (4.1% of price) | annualised 20d 57.8%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Equity Precious Metals
What it holds: P/E 12.25 | P/B 2.71 | P/S 3.99 | 3y earnings growth n/a
Yield: 0.8%
Three-year record: +47.9% a year | beta to the market 0.98
Cost and size: expense ratio 0.51% | net assets 23.82B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Newmont Corp 11.6%, Agnico Eagle Mines Ltd 11.3%, Barrick Mining Corp 8.2%, Wheaton Precious Metals Corp 5.5%, Franco-Nevada Corp 5.5%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 42.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.71 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.4% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, FNV.TO
Recent rating changes among them:
  - NEM: 2026-10-27 Scotiabank: main, Sector Outperform -> Sector Outperform
  - AEM.TO: 2026-11-02 Freedom Broker: up, Hold -> Buy
  - ABX.TO: 2026-11-10 JP Morgan: main, Overweight -> Overweight
  - WPM.TO: 2026-10-08 UBS: main, Buy -> Buy
  - FNV.TO: 2026-11-12 HC Wainwright & Co.: reit, Buy -> Buy
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
Share count change: 1 week: -1.4% (-317.61M) over 7d | 1 month: -5.5% (-1.35B) over 30d
Shares outstanding: 278.70M | fund size: 23.08B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no clear macro surprise, technicals mixed, flat fund flows, and analyst view bullish but limited coverage.

**Main reasons it gave:**
- Analyst view: 100% buy rating on top 5 holdings (42.2% weight) with +32.6% price target
- Fund flows flat over past month, indicating no net demand
- Macro: rising Treasury yields and higher-for-longer rates pressure technology sector
- Technicals: price below 20‑day and 50‑day SMAs, RSI 42, MACD negative, low volume
- Fundamentals: high valuation multiples (P/E 30.79) in a sector facing higher rates

<details><summary><b>News</b> — score +0.00</summary>

- [NET fell 21% before earnings, then rose 10%: why? (Part 3) for NYSE:NET by EdoLab-Markets](https://www.tradingview.com/chart/NET/olZAP5Ow-NET-fell-21-before-earnings-then-rose-10-why-Part-3/)  
  <sub>TradingView, 1 hour ago</sub>  
  Across five sessions NYSE:NET went from 310.30 to 244.51, 21.2% less, and published its numbers that evening, November 5. Friday closed at 268.75,...
- [iShares ESG Aware MSCI EM ETF (ESGE) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/ESGE/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Find the latest iShares ESG Aware MSCI EM ETF (ESGE) stock quote, history, news and other vital information to help you with your stock trading and...
- [XSW: An Equally-Weighted Basket Of Mainly Mid-Cap Software Stocks (NYSEARCA:XSW)](https://www.google.com/goto?url=CAESowEBxCJF13TZDEW8L2b6Wsy4ZdyJgcXthf_XuMJlzMv6y_5UzvsNHDFoxRjc6tgY0RUGYuByKd3vcMmgOHarGfUZtrU07JUlI05zdqjTzqyceYEAdclQ-lwxtYt7WYp2BpGlTI0OSwbkH_39SbL99XaZLJwus_TSO41eX6vWYSnQAnmfs4u_OiEIPdVgOxe2bnBkTEYpmswJWl4C-OvTeToLuEwg&gsessionid=-d1NqoUOkRyY_qo1Q9WtAA3qYGjziF6hY7KlKV72zjZ6d1eoCrPSPg)  
  <sub>Seeking Alpha, 13 hours ago</sub>  
  The State Street SPDR S&P Software & Services ETF offers diversified, mid-cap-heavy exposure to the high-growth, high-margin U.S. software sector.
- [Higher rates hit software harder; Apollo spotlights](https://www.google.com/goto?url=CAESlQEBxCJF147---W3aAfU8vC-8_iv2jUmDIF7o3jgb3Xl6n2FUzFJy_8gIbf4csKcvwJvHCQZUFLbdzY7JyIHv0sKvIMuvcDSu0geAiHV8ZfX95kt52Lpv-hlipKuOB7hojoi4Irj94Lu2_GTc5Tym3rYqGJzW1LbzSsrVaiwZpbYFDGa-UpBJt7Ts9AO61xseW1ZCrcVLg&gsessionid=-d1NqoUOkRyY_qo1Q9WtAA3qYGjziF6hY7KlKV72zjZ6d1eoCrPSPg)  
  <sub>Seeking Alpha, 41 minutes ago</sub>  
  Software companies face mounting refinancing pressure as the higher-for-longer interest-rate regime persists, according to Apollo Global Management's chief...
- [Protests, Inflation, And Unrealistic Expectations: Skip Europe, Buy American (DIA)](https://www.google.com/goto?url=CAESrgEBxCJF13uatmYsufVftX3uzfH0ZV3YDTvXPrwVCw8mpYHQgv2R1dJFs_c342CKgWUhkEMv-3rg21fP25hLcx1IwoNfAo_RN8vhQmJkpiYwE-ylRnFYzyNA3-PTIaufgpCKMJ7Ax4ZMbkcqvHpKG2hVI6k4aDXBWh47-HixMuq0pA0xOEw24SC3q5159eWMD_JgdYOzN60j1MFggbkjHR6zpM3tYlUSd-hj5U4OFXE&gsessionid=-d1NqoUOkRyY_qo1Q9WtAA3qYGjziF6hY7KlKV72zjZ6d1eoCrPSPg)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Europe faces mounting unrest, high debt, and stagnant economies, making broad investment in European markets unattractive; favor U.S. equities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 101.30 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 105.06 (-3.6%), 50d 106.12 (-4.5%), 200d 94.17 (+7.6%); 50d above 200d
Momentum: RSI(14) 42.0 | MACD -1.846 vs signal -1.372 (histogram -0.474)
Returns: 1d -0.1% | 5d +2.4% | 1m -7.6% | 3m -0.7%
52-week range: 74.67 - 112.67 (now 70.1% of the way up)
Volatility: ATR(14) 2.88 (2.8% of price) | annualised 20d 30.9%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Technology
What it holds: P/E 30.79 | P/B 7.22 | P/S 8.03 | 3y earnings growth n/a
Yield: 0.0%
Three-year record: +12.0% a year | beta to the market 1.25
Cost and size: expense ratio 0.38% | net assets 13.46B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Palo Alto Networks Inc 9.1%, Palantir Technologies Inc Ordinary Shares - Class A 9.0%, Microsoft Corp 8.8%, CrowdStrike Holdings Inc Class A 8.6%, Oracle Corp 6.7%
Sector mix: Technology 94.4%, Communication services 3.6%, Financial services 1.7%, Consumer cyclical 0.2%
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
Rolled up from the 5 largest holdings, 42.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.62 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +32.6% above the current prices
Holdings read: PANW, PLTR, MSFT, CRWD, ORCL
Recent rating changes among them:
  - PANW: 2026-11-12 Jefferies: main, Buy -> Buy
  - PLTR: 2026-11-04 Barclays: main, Overweight -> Overweight
  - MSFT: 2026-10-29 Bernstein: main, Outperform -> Outperform
  - CRWD: 2026-11-09 Bernstein: main, Market Perform -> Market Perform
  - ORCL: 2026-11-02 Stephens & Co.: up, Equal-Weight -> Overweight
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
Shares outstanding: 12.50M | fund size: 1.27B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst view on a thin slice of the fund (+0.2), strong outflows indicating bearish sentiment (-0.5), and neutral fundamentals (0.0). Technicals show price above key SMAs but overbought RSI and low volume; macro shows no surprise. Net effect is near‑neutral, so the directional call is neutral.

**Main reasons it gave:**
- Analyst view: 100% buy rating on top holdings with +15% price target (covers 24.8% of fund)
- Fund flows: share count down 10.6% over past month, indicating net outflows
- Technicals: price above 20‑day, 50‑day, 200‑day SMAs, RSI 71.5 (overbought), volume at 0.11× 20‑day average
- Macro: no surprise in rates or data; yields rose modestly, dollar up, VIX down but still elevated

<details><summary><b>News</b> — score +0.00</summary>

- [I.M.I IVZ MS US Ene Infra ETF R (SMLP.HA) interactive stock chart](https://uk.finance.yahoo.com/quote/SMLP.HA/chart/)  
  <sub>Yahoo Finance UK, 13 hours ago</sub>  
  Interactive chart for I.M.I IVZ MS US Ene Infra ETF R (SMLP.HA) – analyse all of the data with a huge range of indicators.
- [iShares MSCI India Small-Cap ETF (SMIN) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/SMIN/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Find the latest iShares MSCI India Small-Cap ETF (SMIN) stock quote, history, news and other vital information to help you with your stock trading and...
- [Allianz Global Investors Fund - Allianz Pet And Animal Wellbeing (ALW7.F) stock price, news, quote and history](https://www.google.com/goto?url=CAESZwHEIkXXsKxCeKeCgySceBjj3tgFGWhjQpuPRXq-oRqw6dgi96-Bq8zhi9gR_Fx2ttLF9H1LSEB-s1eNnehP9M9JNMoohs3cFe2x2RCCKsgj4XqXrtoDwaMqA_eYzIx71Kfe3tJPLIM&gsessionid=YzHjIR85Be38OX-nJ90KBmuA96R3QtFegsEC9H_IpZj8UNp_RJ1Dcg)  
  <sub>Yahoo Finance UK, 9 hours ago</sub>  
  Find the latest Allianz Global Investors Fund - Allianz Pet And Animal Wellbeing (ALW7.F) stock quote, history, news and other vital information to help you...
- [LCUJ (LCUJ.BD) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESbgHEIkXXqr63PSQpK6BI1rnbFCbKOrZ_iLEq_dLT0nIPANr88jCTjWnP62a7EjxAHETg0ecFVvZaLI6ozolOQhu5JAnf7wq3uQMlSNSvTsMSN_7z21-U4WsVPVPkWnth747z-UyceHfOEoK-W9Mw&gsessionid=YzHjIR85Be38OX-nJ90KBmuA96R3QtFegsEC9H_IpZj8UNp_RJ1Dcg)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Interactive Chart for LCUJ (LCUJ.BD), analyze all the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 51.27 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 48.86 (+4.9%), 50d 48.04 (+6.7%), 200d 49.11 (+4.4%); 50d below 200d
Momentum: RSI(14) 71.5 | MACD 1.116 vs signal 0.749 (histogram 0.368)
Returns: 1d -0.5% | 5d +0.7% | 1m +6.9% | 3m +3.4%
52-week range: 45.42 - 54.83 (now 62.2% of the way up)
Volatility: ATR(14) 0.55 (1.1% of price) | annualised 20d 16.4%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: India Equity
What it holds: P/E 21.32 | P/B 2.99 | P/S 2.59 | 3y earnings growth n/a
Yield: n/a
Three-year record: +5.3% a year | beta to the market 0.61
Cost and size: expense ratio 0.61% | net assets 5.84B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: HDFC Bank Ltd 6.3%, ICICI Bank Ltd 5.9%, Reliance Industries Ltd 5.3%, Bharti Airtel Ltd 4.4%, Infosys Ltd 2.9%
Sector mix: Financial services 29.6%, Consumer cyclical 12.2%, Industrials 9.9%, Technology 8.7%
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
Rolled up from the 5 largest holdings, 24.8% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.37 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.0% above the current prices
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
Share count change: 1 week: -3.6% (-217.92M) over 7d | 1 month: -10.6% (-687.85M) over 30d
Shares outstanding: 112.94M | fund size: 5.79B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, technicals bullish but on very low volume, and modest fund inflows.

**Main reasons it gave:**
- Fund flows positive: +0.9% share count increase over the month
- Analyst view strongly bullish: 90.9% buy rating and +15.4% price target above current price
- Technical indicators bullish: price above 20‑day, 50‑day and 200‑day SMAs, MACD positive, RSI 57, but volume extremely low (0.01× 20‑day average)
- Macro environment unchanged: yields modestly higher, no surprise data releases, VIX down but still elevated

<details><summary><b>News</b> — score +0.00</summary>

- [Can the iShares U.S. Transportation ETF (CBOE:IYT) Offer Broad Exposure to Freight and Travel?](https://kalkine.com.au/news/mutual-funds-etfs/can-the-ishares-us-transportation-etf-cboeiyt-offer-broad-exposure-to-freight-and-travel)  
  <sub>Kalkine, 3 hours ago</sub>  
  Can the iShares U.S. Transportation ETF (CBOE:IYT) Offer Broad Exposure to Freight and Travel?
- [Can the iShares Short-Term National Muni Bond ETF (NYSEARCA:SUB) Offer Tax-Exempt Income Without Long Maturities?](https://kalkine.com.au/news/mutual-funds-etfs/can-the-ishares-short-term-national-muni-bond-etf-nysearcasub-offer-tax-exempt-income-without-long-maturities)  
  <sub>Kalkine, 3 hours ago</sub>  
  Can the iShares Short-Term National Muni Bond ETF (NYSEARCA:SUB) Offer Tax-Exempt Income Without Long Maturities?
- [Where Do Small Companies Fit in the iShares MSCI EAFE Small-Cap ETF (NASDAQ:SCZ)?](https://www.google.com/goto?url=CAESuAEBxCJF15pHyUdvenLFdEDiZcFaaIhiKaGSFP_5H1_fnBzXfM1_8_ZvCSC4v1C_RUDcjTKb7rbqzTO_U0I4NOVw3EJrqBELA9Yh5rLp4gu2d_b7Ht3SGvhT8kzZrA1kJThdkvHBM3YGxCVhls-0HPDB099GoWbF-HMj5apK-0dAffXf_EH8VoRSbe91c56xOikdtoHz1yYD9QtRLK2fxJubI2Y7Lt2QoHMfmBWWu8kTt7D_b5iwErsC&gsessionid=UWwGkPD3Izey4uy0FRnvxl4RoqlJ7c0IsxPzbW-6AyRSaKdqEomf_Q)  
  <sub>Kalkine, 3 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [How Does the iShares U.S. Equity Factor ETF (NYSEARCA:LRGF) Use Factor Investing?](https://www.google.com/goto?url=CAEStgEBxCJF1-UyoYzib4NevHdetm2LxzCIuhKYvUmKOLMj1598oyw45b9AGrFqE3-yEwBVUp9hxmE6fPXeblZpWESU9Ylw_hx9BnAaaW2uR6lcB2XYbKtZ2ve2YGD6t92P837j_XziJJwh7tnByd4neP9Mz3-mXYiaUt5nLlhk4Q0_5sBJxB-mWek-4LgTIJmjCrJioQOYp5QicVEpNTAxOfCTXN4ZyroCRBdJprgwikRrzkv6BjnR5w&gsessionid=UWwGkPD3Izey4uy0FRnvxl4RoqlJ7c0IsxPzbW-6AyRSaKdqEomf_Q)  
  <sub>Kalkine, 3 hours ago</sub>  
  Key Highlights. The index selects U.S. stocks using five factors: value, quality, momentum, low Volatility and size. Net Assets total about $3.7 billion...
- [What Is the iShares U.S. Thematic Rotation Active ETF (NYSEARCA:THRO) Rotating Into?](https://www.google.com/goto?url=CAESuQEBxCJF1-nascFPxnZ624OUALK3bg4eOYHmO4CVF5QqP9_bRAakyVu01UFk-8o_6eaq3sx2k21e0IgZbph6FqWMlISpJVEcaWjesVsNHp9M4jNOXnVa1ntq2C4x9Bg4GLiJS1u-oUJBVzP-vW0JVDaoEyTefvamK6sXGURK1Qv3vJGdoBGzjY05OhQPRb_W_-yLIGcvqEAZUlTS_hqQW7zScgpQi6w6p7RDmvIsTH0zYb0GOSiV4z44Wg&gsessionid=UWwGkPD3Izey4uy0FRnvxl4RoqlJ7c0IsxPzbW-6AyRSaKdqEomf_Q)  
  <sub>Kalkine, 3 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Which Companies Drive the iShares U.S. Financial Services ETF (NYSEARCA:IYG)?](https://www.google.com/goto?url=CAESsgEBxCJF11H4h3V8_yz3n2jF-t3HorAnSsFs9LDk6DzINDvM4h-VwmY5fvj845Z1vxz8rAkUL2AwB-Y8hlTnbJaoi9Qow7Bb243jKky9SbsdZAtmht8q6A_SZeta_UmOU7-90wobDqXfQ4NoyggeQ7milEaXwcV-SJRt-DZjHD0G_pDnfiuCZ7eoRp0IaWbaj2exvZnkDFYalIerTUlWIGlvgHQ61WcWZMmUj-epNfJJumH8&gsessionid=UWwGkPD3Izey4uy0FRnvxl4RoqlJ7c0IsxPzbW-6AyRSaKdqEomf_Q)  
  <sub>Kalkine, 3 hours ago</sub>  
  Key Highlights. Berkshire Hathaway, JPMorgan Chase, Visa and Mastercard are the largest holdings. The fund includes Investment banks, asset managers and...
- [What Does the iShares Global Energy ETF (NYSEARCA:IXC) Hold Across Oil and Gas?](https://www.google.com/goto?url=CAEStgEBxCJF18UXOAjjg7NZ_TjIqep9v2GIM8DflFpoE6ZF06Eb-aXB2nvSJ9ReNrr1NqObqkd5A-JiDPVzpOWBT6E2wfHJlQWGS9VE84QwqxbHmmLRC1yqNrdrejwxd8yVNfvBGVRwZQoh9w7QErrv5oslx62mxEa8lNm82noabbYWq8Nh0ZbXWA8aTlyi6sbgirlmY3PvJyV-hh-aqAeHpZlIGG5I3zgFYc5a6NRmE_xbDrHho8MdeQ&gsessionid=UWwGkPD3Izey4uy0FRnvxl4RoqlJ7c0IsxPzbW-6AyRSaKdqEomf_Q)  
  <sub>Kalkine, 3 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports. Become a Kalkine member...
- [Which Sectors Shape the iShares Global Tech ETF (NYSEARCA:IXN)?](https://www.google.com/goto?url=CAESpgEBxCJF11bWAe-IJJnFC20YcNggLVVzmCdFFrLtcYkMo66f4PdLCxYCOmTkSVdAxPUoBjIwwk7ga9RkVYVJ0t0iN-yLkNo44DkMFfBuSpmt_Yf6HvEyj_PACjMhbepCD4S2T6rWGcFfKHcZbj6_oYAt6oBPIKcHTQxt6YPAYf4rNP4KCbh5pUkMlpBBsUumur0d81-VBu6tjnQXi9w8KJi9HA0c1apA&gsessionid=UWwGkPD3Izey4uy0FRnvxl4RoqlJ7c0IsxPzbW-6AyRSaKdqEomf_Q)  
  <sub>Kalkine, 3 hours ago</sub>  
  Key Highlights. The fund covers software, semiconductors and hardware companies worldwide. Apple, NVIDIA and Microsoft make up about 36% of the portfolio.
- [Which Household Brands Anchor the iShares Global Consumer Staples ETF (NYSEARCA:KXI)?](https://www.google.com/goto?url=CAESvAEBxCJF174phEq2IAtf4Q3mdlqgGLPVPEkDvSJd6PTLFjybEX265UYBo-9o2VeHRYLf4znpJ02pAjLNSI-rJJOBFATTdLmVBrBdFgVMBrEr_D1YQk3igp1pgAWLPWZZC6rF0brgxz2Ga7wg7GfWcDiCHnm23E-d2ovVAVja_cAm8MnIow6z-4RAMI7F5eQnGJWlPOOP1SXsh3Xgr4zMLvsthrsEuKSQnwBQx0dlDTa1FDlued6_aq7T3ta5cw&gsessionid=UWwGkPD3Izey4uy0FRnvxl4RoqlJ7c0IsxPzbW-6AyRSaKdqEomf_Q)  
  <sub>Kalkine, 3 hours ago</sub>  
  Key Highlights. The fund holds food, beverage, household goods and tobacco producers worldwide. Walmart, Costco and Procter & Gamble are the largest...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 84.13 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 82.08 (+2.5%), 50d 81.07 (+3.8%), 200d 82.01 (+2.6%); 50d below 200d
Momentum: RSI(14) 57.3 | MACD 0.828 vs signal 0.585 (histogram 0.243)
Returns: 1d +0.7% | 5d +3.9% | 1m +4.0% | 3m -3.7%
52-week range: 68.14 - 90.01 (now 73.1% of the way up)
Volatility: ATR(14) 1.52 (1.8% of price) | annualised 20d 27.6%
Volume: 0.01x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Industrials
What it holds: P/E 19.04 | P/B 4.01 | P/S 1.38 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +15.2% a year | beta to the market 1.24
Cost and size: expense ratio 0.37% | net assets 2.00B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Union Pacific Corp 18.7%, Uber Technologies Inc 13.8%, CSX Corp 10.0%, United Parcel Service Inc Class B 4.9%, Norfolk Southern Corp 4.8%
Sector mix: Industrials 85.3%, Technology 14.7%
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
Rolled up from the 5 largest holdings, 52.2% of the fund by weight
Ratings by weight: buy 90.9% | hold 9.1% | sell 0.0% (mean 1.87 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.4% above the current prices
Holdings read: UNP, UBER, CSX, UPS, NSC
Recent rating changes among them:
  - UNP: 2026-11-05 Baird: down, Outperform -> Neutral
  - UBER: 2026-11-06 UBS: main, Buy -> Buy
  - CSX: 2026-10-27 Susquehanna: main, Positive -> Positive
  - UPS: 2026-10-28 UBS: main, Buy -> Buy
  - NSC: 2026-10-23 Citigroup: main, Neutral -> Neutral
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
Share count change: 1 week: +0.6% (12.25M) over 7d | 1 month: +0.9% (18.62M) over 31d
Shares outstanding: 23.73M | fund size: 2.00B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst view (90.6% buy, +15.8% price target) is offset by net outflows (-5.1% month) and mixed technicals (price below 200‑day SMA, low volume). Macro backdrop shows rising yields, a stronger dollar and lower VIX, but no surprise data or decisive technical break.

**Main reasons it gave:**
- Analyst view: 90.6% buy rating, price target +15.8% for 45.3% of fund
- Fund flows: net outflows of -5.1% over the past month
- Technical: price below 200‑day SMA, RSI 59.8, low volume (0.04× 20‑day avg)
- Macro: US Treasury yields up (10‑yr +0.31% week), dollar up (+0.95% week), VIX down (-7.5% week)

<details><summary><b>News</b> — score +0.00</summary>

- [Saudi Arabia's The Helicopter Company orders 12 Bombardier jets in fixed-wing aviation push](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af72598ee4f4d70bd73fec1965836a9&url=https%3a%2f%2fwww.marketscreener.com%2fnews%2fsaudi-arabia-s-the-helicopter-company-orders-12-bombardier-jets-in-fixed-wing-aviation-push-ce785ed9de8ffe25&c=4962282620886543618&mkt=en-us)  
  <sub>MarketScreener, 9h ago</sub>  
  Bombardier Inc. is a Canada-based company, which designs, builds, modifies and maintains aircraft for the people and businesses, governments, and militaries. In addition to the Co ...
- [Saudi Arabia's The Helicopter Company signs firm order for 12 Bombardier jets](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af72598ee4f4d70bd73fec1965836a9&url=https%3a%2f%2fwww.marketscreener.com%2fnews%2fsaudi-arabia-s-the-helicopter-company-signs-firm-order-for-12-bombardier-jets-ce785ed9de8bf722&c=3713030676786102303&mkt=en-us)  
  <sub>MarketScreener, 10h ago</sub>  
  Bombardier Inc. is a Canada-based company, which designs, builds, modifies and maintains aircraft for the people and businesses, governments, and militaries. In addition to the Co ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 36.03 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 34.84 (+3.4%), 50d 36.05 (-0.1%), 200d 37.78 (-4.6%); 50d below 200d
Momentum: RSI(14) 59.8 | MACD 0.004 vs signal -0.280 (histogram 0.284)
Returns: 1d -0.3% | 5d +2.9% | 1m +2.5% | 3m -5.2%
52-week range: 33.69 - 40.63 (now 33.8% of the way up)
Volatility: ATR(14) 0.35 (1.0% of price) | annualised 20d 16.9%
Volume: 0.04x the 20-day average
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
Three-year record: +0.6% a year | beta to the market 0.20
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 45.3% of the fund by weight
Ratings by weight: buy 90.6% | hold 9.4% | sell 0.0% (mean 2.07 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.8% above the current prices
Holdings read: 1120.SR, 2222.SR, 1180.SR, 7010.SR, 1211.SR
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
Share count change: 1 week: -3.0% (-17.27M) over 7d | 1 month: -5.1% (-30.14M) over 30d
Shares outstanding: 15.46M | fund size: 557.05M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows mixed signals: bearish fund flows (net outflows of -5% over the past month) and a downtrend in price (below 20‑, 50‑ and 200‑day moving averages with low volume) suggest negative sentiment. Macro conditions (rising US Treasury yields and a stronger dollar) also pressure Chinese equities. However, the fund fundamentals are relatively solid (low valuation, modest dividend yield) and analyst coverage, though limited to 32.6% of the fund, is strongly bullish with a +71.5% price target. Given the lack of a clear macro catalyst or decisive technical breakout, the overall stance remains neutral.

**Main reasons it gave:**
- 1‑month net outflows of -5% (fund flows) indicating bearish sentiment
- Price below 20‑, 50‑, and 200‑day moving averages with low volume (technical downtrend)
- Rising US Treasury yields and stronger dollar (macro) pressuring Chinese equities
- Analyst coverage limited to 32.6% of fund but shows 100% buy rating and +71.5% price target
- Fund fundamentals show low valuation (P/E 11.09) and modest dividend yield (2.2%) but no clear catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [White House discusses Lutnick's future as Commerce Secretary - report (MCHI:NASDAQ)](https://seekingalpha.com/news/4671714-white-house-discusses-lutnicks-future-as-commerce-secretary-report)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Senior White House officials are discussing whether Commerce Secretary Howard Lutnick should keep his role after a spy scandal surrounding Nvidia's (NVDA)...
- [Invesco China Technology ETF (CQQQ) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/CQQQ/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Find the latest Invesco China Technology ETF (CQQQ) stock quote, history, news and other vital information to help you with your stock trading and...
- [US EQUITY OPEN: Tech lags with NVDA after Huang's departure](https://www.google.com/goto?url=CAESmgEBxCJF1xbfaNJTUdPFaP10riR5KB6nxPlsqFXLRpd9zDN236K6NF0fn9bMtfDaEY2d7IpOS7410SVHyFFr6GUD523ZzQXhgcjUrOJJcHVXvitfdQU-mt6SZ25zbSAVB68ToNkhVAu2TgTG3-IoVYBhmTbCYDTJWL1fN8JB7vBaMWHosCIQN-DRm9XwK8t5LTI6WRM2ZddVfIbn&gsessionid=fCr_YLB1VENwe-jLni2kL8DsJIhw64WcdE1cZN938UW-jscPtcmODw)  
  <sub>Newsquawk, 24 hours ago</sub>  
  OPEN: US indices opened in the red, with notable pressure in Nvidia (NVDA) after CEO Huang resigned, while neocloud name Nebius (NBIS) plunged after its FY…

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 49.38 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 50.10 (-1.4%), 50d 51.60 (-4.3%), 200d 55.11 (-10.4%); 50d below 200d
Momentum: RSI(14) 38.7 | MACD -0.316 vs signal -0.394 (histogram 0.078)
Returns: 1d -0.7% | 5d -4.8% | 1m -4.5% | 3m -10.3%
52-week range: 48.96 - 64.46 (now 2.7% of the way up)
Volatility: ATR(14) 0.70 (1.4% of price) | annualised 20d 21.4%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Greater China Region
What it holds: P/E 11.09 | P/B 1.27 | P/S 1.27 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +8.8% a year | beta to the market 0.47
Cost and size: expense ratio 0.59% | net assets 5.49B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Tencent Holdings Ltd 13.2%, Alibaba Group Holding Ltd Ordinary Shares 9.1%, China Construction Bank Corp Class H 4.8%, Industrial And Commercial Bank Of China Ltd Class H 2.9%, Xiaomi Corp Class B 2.5%
Sector mix: Consumer cyclical 23.1%, Financial services 22.5%, Communication services 17.5%, Technology 9.9%
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
Rolled up from the 5 largest holdings, 32.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.42 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +71.5% above the current prices
Holdings read: 0700.HK, 9988.HK, 00939, 01398, 1810.HK
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
Share count change: 1 week: +1.3% (67.86M) over 7d | 1 month: -5.0% (-277.88M) over 30d
Shares outstanding: 108.03M | fund size: 5.33B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Analyst consensus 100% buy covering 46.4% of fund with weighted price target +52.8% above current price; Fund flows: +5.6% net inflow over the past month (3.38B) but a recent weekly outflow of -0.5% (335M); Technical indicators: price below 20‑day, 50‑day and 200‑day SMAs; RSI 40.5 and MACD slightly negative; Macro backdrop: rising Treasury yields, inflation 3.7% above target, and elevated VIX (18.1) indicating risk aversion

**Main reasons it gave:**
- Analyst consensus 100% buy covering 46.4% of fund with weighted price target +52.8% above current price
- Fund flows: +5.6% net inflow over the past month (3.38B) but a recent weekly outflow of -0.5% (335M)
- Technical indicators: price below 20‑day, 50‑day and 200‑day SMAs; RSI 40.5 and MACD slightly negative
- Macro backdrop: rising Treasury yields, inflation 3.7% above target, and elevated VIX (18.1) indicating risk aversion

<details><summary><b>News</b> — score +0.00</summary>

- [Michael Burry Doubles Down on Nasdaq-100 and Semiconductor ETF Shorts, Betting Nvidia's Influence Will Wane](https://finance.biggo.com/news/3744e289-232e-4117-8999-60e7a45a0df9)  
  <sub>BigGo Finance, 1 hour ago</sub>  
  Michael Burry, who rose to fame for predicting the 2008 subprime crisis, said in a November 12 post that he doubled his put position on the Nasdaq-100…
- [Michael Burry Doubles Down On Nasdaq 100 Puts, Adds To Semiconductor Shorts As Nvidia Faces Scrutiny](https://finance.yahoo.com/markets/stocks/articles/michael-burry-doubles-down-nasdaq-235318261.html)  
  <sub>Yahoo Finance, 15 hours ago</sub>  
  He also bought back 25% of a previously reduced put position in the VanEck Semiconductor ETF (SMH) expiring in June. On the SMH, where Nvidia is the largest...
- [VanEck Semiconductor ETF Options Spot-On: On November 12th, 265.69K Contracts Were Traded, With 2.47 Million Open Interest](https://www.google.com/goto?url=CAESpQEBxCJF1xvgg53J_vwejfoORRcL_1dkIuyVQOO6OZiROz65dK7KhmT5-jkLW0I0yW0np8O4_5XA1_PcWLNn_aGeum9OYSzJJ0ekFym7sokTr60TXlbZk4Wdj0dIdIzaQ5NU8GqDejGroaU7HxIOGAyG86-mn6xvE2NKmt2l8OkiYp4xqrxfyp1DKCF5SCc4IQoNv5wQZ34qh79bcIu1OMcdS49pRZw&gsessionid=d2lK6JvqbrycvrWR5htNEnvePGHYOVpl-PBZw8yZ1VIAT4t8s8oDjA)  
  <sub>富途牛牛, 7 hours ago</sub>  
  OnNovember 12th ET, $VanEck Semiconductor ETF(SMH.US)$ had active options trading, with a total trading volume of 265.69K options for the day,...
- [Michael Burry Sends Stark Warning on Chip Stocks After Huang's exit](https://www.google.com/goto?url=CAESvAEBxCJF1ypyv-T1n5UuapqFZvORq1l2IJA4mQkPsYkAZtmLNcSaSnVIC_MWvkeEEMKJbydI7G1fMeNwLRgZt7iRszQf07NVABcC-A2-cb6wbgv_BlwhwDCU3zXS_2ZelV3M-kJCT0La3XICHquvSF-btFfj_Z9-TJeJXUwyXrBI1_XrulGEyiftgRZlQBwTaBWRO2RifKh0K1ynbZedxqKvMjTo1QF_3t3WfYJ3uflKk2frkncz4T3kZoCanA&gsessionid=d2lK6JvqbrycvrWR5htNEnvePGHYOVpl-PBZw8yZ1VIAT4t8s8oDjA)  
  <sub>TradingView, 3 hours ago</sub>  
  Michael Burry (Trades, Portfolio) said the grip Nvidia NASDAQ:NVDA has on the AI supply chain may be loosening following Jensen Huang's exit as CEO,...
- [What Message Do USD 750 Million Leaving SMH and USD 2.06 Billion Entering SPY Send About Positioning?](https://www.google.com/goto?url=CAESzwEBxCJF14iQjs5MJ-h7jfciReRPbn1xOxk63KuM2XPmNjFWY43ndqRhneoULPY0vpjM67Bl4HTHTVHNSs47YkBZGqLsNfZRrvB2HhmNYd4e0FtGnShH1ysyXTYjjZYTgG8-iKd_v440OpbLbBMNHgb38DTVUzI8JRie70V1nlaNW4Tt7tBTLS3mZV65vT6BxLCQS_NVM4amBxyK-2r2cWYsTP3jyeC23Vtlz7k8znB3OUUchd7uikjrnQto036ZCNKze90EhZClUvVlgI54phg&gsessionid=d2lK6JvqbrycvrWR5htNEnvePGHYOVpl-PBZw8yZ1VIAT4t8s8oDjA)  
  <sub>kalkine.ca, 3 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Options Whale Alert: $8.21M Move-Away Short Call Diagonal Spread Opened on $SMH](https://www.google.com/goto?url=CAESoAEBxCJF163fogL2mU3eGfYHu4JwiBCfy2HoKgzwWFOT6G_pkGuOoOZpnP8QWw_QjvFrZYUFgSuVYU4_s4H8Ckfew2X-reazL3m3zXfGrHyo3lCaQWFOPIQKwQeRkgb-Nlpb7Xk0Jp4VvOvY4caaxMgpgZdQVD2XgchY6_ZO1081HaVR8__cm_GnWMT--cwfPlU8btLkyTsxRXqYmTKMhneR&gsessionid=d2lK6JvqbrycvrWR5htNEnvePGHYOVpl-PBZw8yZ1VIAT4t8s8oDjA)  
  <sub>Moomoo, 16 hours ago</sub>  
  VanEckSemiconductor ETF(SMH.US)$ closed down 1.03% at $501.73. A trader bought 1000 Mar 19, 2027 $615.00 calls and sold 1000 Sep 17, 2027 $470.00 calls to.
- [Nvidia ETFs Have a New Problem: Life After Jensen Huang](https://www.google.com/goto?url=CAESoQEBxCJF17pzVHLvfP5IxjsbmgdHRHk7LfhfVgGFmCf7XfbN4P7ONtXd3Dk3hJkuzLNahFCmvg0K8j5243U1qlH_aszdKmsRSPAXauvoq-VL_Z4v5EBDUeXkVm1CGYT4yy7k4ZGN608UDzVSmQbNC95oMrwY6daqVYBBxCzmn3RkJ9J5B_3yCzOcDTwc-LllxsCll6o43XIhqpCIA2iUByMHTw&gsessionid=d2lK6JvqbrycvrWR5htNEnvePGHYOVpl-PBZw8yZ1VIAT4t8s8oDjA)  
  <sub>Benzinga, 21 hours ago</sub>  
  Nvidia ETF holdings are under scrutiny now that Jensen Huang is out of the company. Here's what it means for SMH, QQQ and VGT.
- [Jensen Huang Is Out. Here’s How Much Nvidia’s Selloff Cost a $10,000 QQQ Position](https://www.google.com/goto?url=CAESuQEBxCJF1653mvE5mOdSu5eGYvnNNd5sKOAZBDeyBP6mNdfkhDbMowvOTueWspG6VIvJjnVKOQyjiB6vLiiVgyiovYGJnBLIAlNjx6YU0WTyt4RrGVBRTsqJQ70Mky4xozdoREE78n7Z4F6hD-B7152rUJZnqQz9uea6AnYpIHnHTS8wJuwv2N-mv18J5tI-O8aOhkbJ9QXHsJKdF8aVCf1lvxdFBGm57rzsZaDth0rv5LU_no4UpR2Z_Q&gsessionid=d2lK6JvqbrycvrWR5htNEnvePGHYOVpl-PBZw8yZ1VIAT4t8s8oDjA)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  Nvidia's stock dropped after its CEO walked away, yet millions of investors own it without ever buying a share directly. Why did the fund holders barely...
- [Burry doubles down on Nasdaq 100 puts, increases bearish SMH position amid Nvidia leadership turmoil](https://www.google.com/goto?url=CAES4AEBxCJF1xEroEZ5JZN3Jp3OYNTYtI2tgIb-N6gIWpfxxlc0znSkGJhWkvrMG-V2fsTDRfPpTIXg5KMl-s2-nin7pia-spU1pe-9shMddc73OqN2gnqSanPefwz1sYch_NEYf_lhx4IX7fwvDAyJQ5yMkL_pt0FRiKoe-z3Up9Ig9usR6iLSRHVIbvsOAOG0Wg2Qy3LUqNH1cd9G-VF-OVdTdwsX8TdVIrPuVWZZgcf3mjjDen3XbVHeoc-WKXhv_XHSO1ebAZLtSRmFn_xBpOwlRcrYJsy7u2WXZicVSpgadw&gsessionid=d2lK6JvqbrycvrWR5htNEnvePGHYOVpl-PBZw8yZ1VIAT4t8s8oDjA)  
  <sub>TradingView, 11 hours ago</sub>  
  Michael Burry has increased his bearish bets on the Nasdaq 100 NASDAQ:NDX and semiconductor stocks, citing concerns about Nvidia's NASDAQ:NVDA influence on...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 489.17 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 518.26 (-5.6%), 50d 559.85 (-12.6%), 200d 523.90 (-6.6%); 50d above 200d
Momentum: RSI(14) 40.5 | MACD -22.543 vs signal -21.858 (histogram -0.685)
Returns: 1d -2.5% | 5d +5.4% | 1m -12.5% | 3m -17.7%
52-week range: 325.10 - 668.91 (now 47.7% of the way up)
Volatility: ATR(14) 23.23 (4.7% of price) | annualised 20d 65.5%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Technology
What it holds: P/E 28.22 | P/B 9.76 | P/S 11.19 | 3y earnings growth n/a
Yield: 0.2%
Three-year record: +48.4% a year | beta to the market 2.12
Cost and size: expense ratio 0.35% | net assets 66.44B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: NVIDIA Corp 20.2%, Taiwan Semiconductor Manufacturing Co Ltd ADR 9.6%, Texas Instruments Inc 5.7%, Broadcom Inc 5.6%, Advanced Micro Devices Inc 5.3%
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 46.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.53 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +52.8% above the current prices
Holdings read: NVDA, TSM, TXN, AVGO, AMD
Recent rating changes among them:
  - NVDA: 2026-11-12 Melius Research: down, Buy -> Hold
  - TSM: 2026-11-04 Bernstein: main, Outperform -> Outperform
  - TXN: 2026-10-22 Jefferies: main, Hold -> Hold
  - AVGO: 2026-10-27 Rosenblatt: main, Buy -> Buy
  - AMD: 2026-11-12 B of A Securities: main, Buy -> Buy
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
Share count change: 1 week: -0.5% (-335.41M) over 7d | 1 month: +5.6% (3.38B) over 31d
Shares outstanding: 131.02M | fund size: 64.09B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, flat fund flows, mixed technicals, cheap valuation but negative recent performance, strong analyst rating limited to <50% of fund.

**Main reasons it gave:**
- Analyst coverage of 44.9% of fund shows 100% buy rating and +27.5% price target
- Fund flows flat over past month, indicating no net demand
- Technical indicators mixed: price above 20‑day SMA but below 50‑day and 200‑day SMAs, low volume
- Macro backdrop unchanged: modest yield rises, stronger dollar, no policy surprise
- Fund basics show cheap valuation (P/E 11.6) but negative three‑year performance (-0.6% per year)

<details><summary><b>News</b> — score +0.00</summary>

- [Samsung Stocks Rise as Foreign Buyers Step In Despite NVIDIA Turmoil](https://www.gurufocus.com/news/9194967/samsung-stocks-rise-as-foreign-buyers-step-in-despite-nvidia-turmoil)  
  <sub>GuruFocus, 19 hours ago</sub>  
  Samsung Electronics Co Ltd (SSNLF) shares rose 0.97% to 208000 won at the November 12 regular-session close in Seoul, after reports on NVIDIA's leadership...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 32.19 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 31.24 (+3.1%), 50d 34.25 (-6.0%), 200d 38.60 (-16.6%); 50d below 200d
Momentum: RSI(14) 49.4 | MACD -0.591 vs signal -0.980 (histogram 0.389)
Returns: 1d +0.4% | 5d +3.0% | 1m -4.1% | 3m -18.4%
52-week range: 29.53 - 43.74 (now 18.7% of the way up)
Volatility: ATR(14) 0.65 (2.0% of price) | annualised 20d 35.3%
Volume: 0.06x the 20-day average
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
Three-year record: -0.6% a year | beta to the market 0.60
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.5% above the current prices
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
Shares outstanding: 15.65M | fund size: 503.77M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, analyst view bullish but limited to 40.5% weight, fund flows show net outflow over the month, fundamentals mixed with high valuation metrics versus rising yields.

**Main reasons it gave:**
- Analyst coverage of top holdings (40.5% weight) is 100% buy with a +13% price target
- Fund flows show a 1‑month net outflow of -2.3% (~$1.62B), indicating weakening demand
- Macro: Treasury yields rose (10‑yr +0.31% week) and inflation 3.7% above Fed target, pressuring REIT valuations
- Technical: Price above 20‑d, 50‑d, 200‑d SMAs, RSI 60.7, but volume only 0.09× 20‑day average

<details><summary><b>News</b> — score +0.00</summary>

- [AI capital buildout raising housing funding costs - Fed's Schmid (XLRE:NYSEARCA)](https://seekingalpha.com/news/4671655-ai-capital-buildout-raising-housing-funding-costs---feds-schmid)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Jeff Schmid says housing affordability needs construction productivity, not Fed rate cuts; buying a median-priced metro home took 33% of income in 2024.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 96.71 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 94.48 (+2.4%), 50d 92.97 (+4.0%), 200d 94.89 (+1.9%); 50d below 200d
Momentum: RSI(14) 60.7 | MACD 1.286 vs signal 1.029 (histogram 0.256)
Returns: 1d +0.3% | 5d +1.0% | 1m +5.8% | 3m -1.3%
52-week range: 87.00 - 100.95 (now 69.6% of the way up)
Volatility: ATR(14) 1.36 (1.4% of price) | annualised 20d 20.0%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Real Estate
What it holds: P/E 28.38 | P/B 2.42 | P/S 4.62 | 3y earnings growth n/a
Yield: 3.6%
Three-year record: +13.0% a year | beta to the market 0.92
Cost and size: expense ratio 0.13% | net assets 69.46B
What it is made of: Stocks 98.9%, Cash 0.8%, Other 0.3%
Largest holdings: Vanguard Real Estate II Index 14.5%, Welltower Inc 9.1%, Prologis Inc 6.9%, Equinix Inc 5.7%, American Tower Corp 4.3%
Sector mix: Real estate 99.5%, Communication services 0.3%, Energy 0.1%, Industrials 0.0%
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
Rolled up from the 5 largest holdings, 40.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.56 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.0% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2026-11-11 UBS: main, Buy -> Buy
  - PLD: 2026-11-02 Wells Fargo: main, Overweight -> Overweight
  - EQIX: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - AMT: 2026-11-05 Argus Research: reit, Buy -> Buy
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
Share count change: 1 week: +3.0% (2.04B) over 7d | 1 month: -2.3% (-1.62B) over 31d
Shares outstanding: 715.85M | fund size: 69.23B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: modest bullish signals from fund inflows and analyst consensus are offset by a short‑term technical downtrend and a macro backdrop lacking any surprise catalyst.

**Main reasons it gave:**
- Positive fund inflows (+1.8% week, +3.7% month) indicating demand for XBI exposure
- Analyst consensus on top holdings: 75% buy, weighted price target +13.8% (thin coverage 9.5%)
- Technical short‑term downtrend: price below 20‑day and 50‑day SMA, RSI 44.2, low volume
- Macro environment: rising yields, normal yield curve, no surprise data; VIX down but still elevated

<details><summary><b>News</b> — score +0.00</summary>

- [Bank of America Sees Up to 95% Upside in 2 Stocks](https://www.tradingview.com/news/gurufocus:92dd72d0c094b:0-bank-of-america-sees-up-to-95-upside-in-2-stocks/)  
  <sub>TradingView, 16 hours ago</sub>  
  Bank of America is betting that the biotech rally has further room to run, identifying Iambic Therapeutics NASDAQ:IAM and Supernus Pharmaceuticals (SUPN) as...
- [XBI Jan 2028 156.000 call (XBI280121C00156000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/XBI280121C00156000/chart/)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Interactive Chart for XBI Jan 2028 156.000 call (XBI280121C00156000), analyze all the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 148.65 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 153.32 (-3.0%), 50d 154.23 (-3.6%), 200d 142.96 (+4.0%); 50d above 200d
Momentum: RSI(14) 44.2 | MACD -0.282 vs signal -0.033 (histogram -0.250)
Returns: 1d -1.7% | 5d -2.3% | 1m -0.8% | 3m -6.8%
52-week range: 111.91 - 169.55 (now 63.7% of the way up)
Volatility: ATR(14) 4.92 (3.3% of price) | annualised 20d 41.3%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Health
What it holds: P/E n/a | P/B 0.21 | P/S 0.13 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +32.9% a year | beta to the market 1.01
Cost and size: expense ratio 0.35% | net assets 10.92B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Moderna Inc 2.4%, Natera Inc 1.8%, Halozyme Therapeutics Inc 1.8%, Twist Bioscience Corp 1.8%, Biogen Inc 1.7%
Sector mix: Healthcare 99.4%, Financial services 0.6%
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
Rolled up from the 5 largest holdings, 9.5% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 75.0% | hold 25.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.8% above the current prices
Holdings read: MRNA, NTRA, HALO, TWST, BIIB
Recent rating changes among them:
  - MRNA: 2026-11-09 Goldman Sachs: main, Neutral -> Neutral
  - NTRA: 2026-11-09 Baird: main, Outperform -> Outperform
  - HALO: 2026-11-11 Morgan Stanley: down, Overweight -> Equal-Weight
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - BIIB: 2026-11-09 Piper Sandler: reit, Overweight -> Overweight
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
Share count change: 1 week: +1.8% (188.35M) over 7d | 1 month: +3.7% (370.72M) over 30d
Shares outstanding: 69.87M | fund size: 10.39B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, flat fund flows, technicals are mixed but not decisive, and analyst bullishness is limited to 34% of the fund.

**Main reasons it gave:**
- Flat fund flows (0% change week/month)
- No macro surprise: yields modestly higher, VIX down, inflation 3.7% in line
- Technical indicators neutral: price near 52‑week high, RSI 53.6, MACD histogram negative
- Analyst consensus 100% buy on 34% of holdings with +9.5% price target, limited coverage

<details><summary><b>News</b> — score +0.00</summary>

- [Nucor leads as just two materials stocks sustain Strong Buy ratings](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af7247567cd418386f4bea9cf1b6281&url=https%3a%2f%2fseekingalpha.com%2fnews%2f4671667-nucor-leads-as-just-two-materials-stocks-sustain-strong-buy-ratings&c=18376402876963923624&mkt=en-us)  
  <sub>Seeking Alpha, 29h ago</sub>  
  Steel stocks Nucor and Cleveland-Cliffs hold Strong Buy Quant Ratings, with scores of 4.64 and 4.79 after 101 and 16 days, respectively.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 52.36 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 52.24 (+0.2%), 50d 50.93 (+2.8%), 200d 51.24 (+2.2%); 50d below 200d
Momentum: RSI(14) 53.6 | MACD 0.531 vs signal 0.582 (histogram -0.051)
Returns: 1d +0.0% | 5d +0.8% | 1m +3.6% | 3m +0.2%
52-week range: 42.23 - 53.90 (now 86.8% of the way up)
Volatility: ATR(14) 0.88 (1.7% of price) | annualised 20d 20.4%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Natural Resources
What it holds: P/E 21.94 | P/B 2.74 | P/S 1.71 | 3y earnings growth n/a
Yield: 1.6%
Three-year record: +13.2% a year | beta to the market 0.76
Cost and size: expense ratio 0.08% | net assets 8.45B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Linde PLC 12.8%, Newmont Corp 6.1%, Vulcan Materials Co 5.1%, Ecolab Inc 5.1%, Air Products and Chemicals Inc 4.9%
Sector mix: Basic materials 82.3%, Consumer cyclical 17.7%
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
Rolled up from the 5 largest holdings, 34.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.5% above the current prices
Holdings read: LIN, NEM, VMC, ECL, APD
Recent rating changes among them:
  - LIN: 2026-10-31 UBS: main, Buy -> Buy
  - NEM: 2026-10-27 Scotiabank: main, Sector Outperform -> Sector Outperform
  - VMC: 2026-11-09 Stifel: main, Buy -> Buy
  - ECL: 2026-10-29 Wells Fargo: main, Equal-Weight -> Equal-Weight
  - APD: 2026-11-09 Citigroup: main, Neutral -> Neutral
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
Shares outstanding: 71.92M | fund size: 3.77B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, mixed technicals, thin analyst coverage.

**Main reasons it gave:**
- Flat fund flows: share count unchanged over the past week
- No macro surprise: Treasury yields rose modestly, no rate or policy shock
- Technical indicators mixed: price above 20‑day SMA but below 200‑day SMA, RSI near 50
- Analyst coverage thin (24% of fund) despite bullish price targets

<details><summary><b>News</b> — score +0.00</summary>

- [What State Street Industrial Select SPDR (XLI) Bought: GE Leads on Nov. 11](https://ca.finance.yahoo.com/news/state-street-industrial-select-spdr-110440498.html)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Industrial Select Sector SPDR ETF (XLI) was the only ETF buying on Wednesday, Nov.
- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Friday as Producer Inflation Trails Forecasts](https://www.moomoo.com/news/post/1004601462/exchange-traded-funds-equity-futures-higher-pre-bell-friday-as)  
  <sub>Moomoo, 36 minutes ago</sub>  
  Thebroad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.4% and the actively traded Invesco QQQ Trust (QQQ) was 0.2% higher in Friday's...
- [Only three industrial stocks carry longer period Sell or Strong Sell Quant ratings (XLI:NYSEARCA)](https://www.google.com/goto?url=CAEStQEBxCJF138hAxwEc8nB_Ei5bYVxZEUQ8v0UdVjJoDAVJVaY152XWDbDE-cZ21IPFez68uAOUxo52pUVZ5SwwhaV4X_bXV-DoxBUnrHdcpBr6TnuEU5wdktc1uIl4MbTk7Fm2Fy6yvSB0nhu-qBsbPhjRRz5085kdRoaoSBBFdKReciU3ViffKFU8mo2lgwvJwtkGTvHgEdWDKU8zWPhadyzz8rTrmPCrJD47Bbsvy_1lZ16UH4b&gsessionid=KF9fqBJgx1YRqOpli1Ql9bu9ooe-KotEGzuUjO-_TT4JRun8X-v3wQ)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Three industrial stocks have persistent Sell or Strong Sell Quant Ratings: Lennox International leads at 29 days, ESCO at 17 and Modine at 15.
- [What Are Wall Street Analysts' Target Price for C.H. Robinson Stock?](https://www.google.com/goto?url=CAESqgEBxCJF1zgV5EwLfBaszOzO0Zm9UuHmRTM-eSi9BSZX_pac1DtjKgKxMKsy97LOvGRU4_UwHe064oVFLjm0yGf9mCHIhbn4yQEQN1cbfok0DThaX0kJP-mxvKgktfLbeMDtsS5Blf5E30CPxk99yHCBOt9RaRomCPiKmxYfKhRcduucNuF8H-nqV1eLw1jSM9kQ_UwPeN_wzDxJqC-WsB3TBIhJ0IGbd2fThQ&gsessionid=KF9fqBJgx1YRqOpli1Ql9bu9ooe-KotEGzuUjO-_TT4JRun8X-v3wQ)  
  <sub>Barchart.com, 2 hours ago</sub>  
  Despite C.H. Robinson's underperformance relative to the broader market over the past year, Wall Street analysts maintain a bullish outlook on the stock's...
- [Nvidia CEO Huang Resigns as AI Chip Selloff Deepens](https://www.google.com/goto?url=CAESnQEBxCJF17JADAmvprb-xAxOkxcCADHYI6WeGFTY8TYVyLEGtjRu_-bSVEvwOJUgDEMBgjDP2s2gt0zfOcwDUOGTMAvRxIba8b9nizaQ6YftHqHdV6DDn1Q_zQp6R7WysdT4O_pt0Z4S6s3Try8GZgeUxP_MzOsA1ezlgizpLHcXJkx72OA9y4_txRvn8sApYfRJ7uBrkVyjgKB0cjFv&gsessionid=KF9fqBJgx1YRqOpli1Ql9bu9ooe-KotEGzuUjO-_TT4JRun8X-v3wQ)  
  <sub>ETF Database, 22 hours ago</sub>  
  Jensen Huang resigned as Nvidia CEO and shares fell 10%, adding to a chip selloff State Street says began before the midterms.
- [State Street Tech Select SPDR (XLK) Buys $119.9 Million More Apple on Nov. 11](https://www.google.com/goto?url=CAESmwEBxCJF11f6mLNwIR6mY6Z5HKBLbkBCEUsD0Pq-9X2BBjwv82sfRmM5PM0OVE7HnLJu8xHNJI6DTce4QUDTmo7HodyO99QnbLpc2g6izNvP2kOCFK15qUY3ilFozi6SfjtvYq_WxWtpvX4gbAy0YHOpehCLEyJTRa5an7WTTRxN60c3uInQGYAfPHqrizHeJfcb3-KKQgTOt20-xA&gsessionid=KF9fqBJgx1YRqOpli1Ql9bu9ooe-KotEGzuUjO-_TT4JRun8X-v3wQ)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Technology Select Sector SPDR ETF (XLK) was the sole mover in Wednesday's session, adding $739.0...
- [Energy Leads Sectors In Thursday Trading As Materials Trail](https://www.google.com/goto?url=CAESsQEBxCJF168ONtHu-AKcrp3wG2BUv9jyoQ_VJE8Ddf6mBY5wPv6cnv_s3gxrR5CMsImShOM7kFJHYzjqxkoTKKqboJgr-y32g5RYqy6kW5Qnto8EC83NUXhXz25R_ZsxThTruufm_c4pNBo0DRmiv6LBbtM-TtPPiIc5o4D7g5QrphL_4N_NhUmMOVBMwUBUqcLXOYag5_y6n30DPT7-pHP0aBuFNpL8GYBgFxSCK_XqyYM&gsessionid=KF9fqBJgx1YRqOpli1Ql9bu9ooe-KotEGzuUjO-_TT4JRun8X-v3wQ)  
  <sub>Benzinga, 23 hours ago</sub>  
  Five sectors are higher and six are lower in Thursday's regular session, with cyclical, defensive and growth sectors split across the top three positions.
- [Jensen Huang Is Out. Here’s How Much Nvidia’s Selloff Cost a $10,000 QQQ Position](https://www.google.com/goto?url=CAESuQEBxCJF1_X0fTb_2RqbfAxR4YiD8UlrnkKvYxePsJrv23LAVjOaoirrAtcRzSKtT-FFBsxqFH1qA8obw1LX2oekUjJVnLfweb9hzl7nm_QXPWgQq4tOmbIuD8gWoiPeNySrW8iHhZSaiFMzAQRCy7g3CxR1fe3ywEWPxJIKKuzziA2Aipr_ACIlsq5hFGUNzbyXvv7wlYSjgmpo2YY47Kyy6j9pm7gZrA60zNQk6kaNV7e3cph7zjZ-Jw&gsessionid=KF9fqBJgx1YRqOpli1Ql9bu9ooe-KotEGzuUjO-_TT4JRun8X-v3wQ)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  Nvidia's stock dropped after its CEO walked away, yet millions of investors own it without ever buying a share directly. Why did the fund holders barely...
- [PTF: Strong Tech Momentum Comes At The Considerable Expense Of Quality (NASDAQ:PTF)](https://www.google.com/goto?url=CAESpwEBxCJF1wL5UjU25wPoZ0BAXqCyq2T1dh2dSZYNpgySsJTzJZ7PQh3V7NQktdIF4NTxePDWC_MsMmjDZJxmmOWco2scm-2f9YtUYIxFj_extWD-yrl2AnNOcGXWSCOVVFq-y_NMk16egggD5pD5g1C90m77N9ASo8y72hxeqG5v1P1fLd5kEsErfFWnkCpv5fVu80r0qmF07gkKY9kmbN2l9sGrsgjV_Q&gsessionid=KF9fqBJgx1YRqOpli1Ql9bu9ooe-KotEGzuUjO-_TT4JRun8X-v3wQ)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  The Invesco Dorsey Wright Technology Momentum ETF remains rated 'sell' due to a high probability of substantial drawdowns. Discover more about PTF here.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 169.13 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 167.84 (+0.8%), 50d 168.96 (+0.1%), 200d 173.46 (-2.5%); 50d below 200d
Momentum: RSI(14) 51.2 | MACD -0.123 vs signal -0.511 (histogram 0.389)
Returns: 1d -0.2% | 5d +4.0% | 1m +0.7% | 3m -9.2%
52-week range: 147.83 - 186.51 (now 55.1% of the way up)
Volatility: ATR(14) 3.05 (1.8% of price) | annualised 20d 25.2%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Industrials
What it holds: P/E 26.85 | P/B 6.33 | P/S 2.84 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +20.2% a year | beta to the market 1.00
Cost and size: expense ratio 0.08% | net assets 31.20B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: GE Aerospace 5.9%, Caterpillar Inc 5.4%, RTX Corp 5.1%, GE Vernova Inc 4.3%, Union Pacific Corp 3.4%
Sector mix: Industrials 93.0%, Technology 6.5%, Basic materials 0.4%, Consumer cyclical 0.2%
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
Rolled up from the 5 largest holdings, 24.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.5% above the current prices
Holdings read: GE, CAT, RTX, GEV, UNP
Recent rating changes among them:
  - GE: 2026-10-21 UBS: main, Buy -> Buy
  - CAT: 2026-11-10 Evercore ISI Group: main, Outperform -> Outperform
  - RTX: 2026-10-21 UBS: main, Neutral -> Neutral
  - GEV: 2026-11-11 JP Morgan: main, Overweight -> Overweight
  - UNP: 2026-11-05 Baird: down, Outperform -> Neutral
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
Shares outstanding: 136.63M | fund size: 23.11B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: macro tightening and lack of decisive technical break offset modest inflows and strong analyst bullishness.

**Main reasons it gave:**
- 10‑year Treasury yield rose 0.31% this week, curve remains upward sloping
- XLK share count increased 1.2% over the past week, indicating modest inflows
- Price below 20‑day SMA (178.68) and 50‑day SMA (187.11), RSI 39.9, volume 0.10× 20‑day average
- Analyst consensus 100% buy with +32.8% price target, covering 51.5% of fund

<details><summary><b>News</b> — score +0.00</summary>

- [Jensen Huang Is Out. Here’s How Much Nvidia’s Selloff Cost a $10,000 QQQ Position](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af723efd8584669bd2e5cf8cfec5256&url=https%3a%2f%2f247wallst.com%2finvesting%2fetf%2f2026%2f11%2f12%2fjensen-huang-is-out-heres-how-much-nvidias-selloff-cost-a-10000-qqq-position%2f&c=9758400826307325580&mkt=en-us)  
  <sub>24/7 Wall St., 30h ago</sub>  
  Nvidia's stock dropped after its CEO walked away, yet millions of investors own it without ever buying a share directly. Why did the fund holders barely flinch, and which popular ETFs could leave them ...
- [Nvidia CEO Jensen Huang’s exit raises AI financing risks, says Ed Yardeni — sees selloff as buying opportunity](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af723efd8584669bd2e5cf8cfec5256&url=https%3a%2f%2fwww.msn.com%2fen-in%2fnews%2fother%2fnvidia-ceo-jensen-huang-s-exit-raises-ai-financing-risks-says-ed-yardeni-sees-selloff-as-buying-opportunity%2far-AA2hneFd&c=13439050646930210105&mkt=en-us)  
  <sub>Asianet Newsable on MSN, 10h ago</sub>  
  The Yardeni Research President said Washington could tighten chip export controls and close loopholes that let Chinese companies remotely access Nvidia-powered computing capacity.
- [Tom Lee says Jensen Huang exit doesn’t change his bullish tech outlook: AVGO, AMD stocks lead chip rally](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af723efd8584669bd2e5cf8cfec5256&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2fgeneral%2ftom-lee-says-jensen-huang-exit-doesn-t-change-his-bullish-tech-outlook-avgo-amd-stocks-lead-chip-rally%2far-AA2hiUdG&c=4389009209029808546&mkt=en-us)  
  <sub>Stocktwits on MSN, 29h ago</sub>  
  AMD and AVGO stocks rallied in midday trade, with AMD on track for its strongest weekly performance in a decade and AVGO poised to post its strongest weekly gain on record. ・Nvidia shares remained ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 170.77 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 178.68 (-4.4%), 50d 187.11 (-8.7%), 200d 170.82 (-0.0%); 50d above 200d
Momentum: RSI(14) 39.9 | MACD -5.309 vs signal -4.863 (histogram -0.446)
Returns: 1d -1.7% | 5d +3.7% | 1m -9.7% | 3m -10.3%
52-week range: 127.50 - 202.00 (now 58.1% of the way up)
Volatility: ATR(14) 5.32 (3.1% of price) | annualised 20d 44.7%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Technology
What it holds: P/E 31.66 | P/B 11.55 | P/S 8.87 | 3y earnings growth n/a
Yield: 0.5%
Three-year record: +25.6% a year | beta to the market 1.56
Cost and size: expense ratio 0.08% | net assets 118.67B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Apple Inc 15.3%, NVIDIA Corp 15.1%, Microsoft Corp 11.8%, Broadcom Inc 4.7%, Advanced Micro Devices Inc 4.5%
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
Rolled up from the 5 largest holdings, 51.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +32.8% above the current prices
Holdings read: AAPL, NVDA, MSFT, AVGO, AMD
Recent rating changes among them:
  - AAPL: 2026-11-11 China Renaissance: up, Hold -> Buy
  - NVDA: 2026-11-12 Melius Research: down, Buy -> Hold
  - MSFT: 2026-10-29 Bernstein: main, Outperform -> Outperform
  - AVGO: 2026-10-27 Rosenblatt: main, Buy -> Buy
  - AMD: 2026-11-12 B of A Securities: main, Buy -> Buy
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
Share count change: 1 week: +1.2% (1.38B) over 7d | 1 month: +6.3% (6.90B) over 31d
Shares outstanding: 680.72M | fund size: 116.25B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst view: 100% buy on 41.8% of fund, price target +1.4% above current
- Fund flows flat: share count unchanged over week and month
- Technicals: price near 52‑week high (99.5% of range) with RSI 63.7, no decisive breakout
- Macro: no rate or data surprise; yields up modestly, VIX down but still elevated

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Health Care SPDR (XLV) Buys $66.8 Million More Eli Lilly on Nov. 11](https://finance.yahoo.com/healthcare/articles/state-street-health-care-spdr-110327637.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Health Care Select Sector SPDR ETF (XLV) recorded net buying of $396.8 million in Wednesday's session...
- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Friday as Producer Inflation Trails Forecasts](https://www.moomoo.com/news/post/1004601462/exchange-traded-funds-equity-futures-higher-pre-bell-friday-as)  
  <sub>Moomoo, 36 minutes ago</sub>  
  Thebroad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.4% and the actively traded Invesco QQQ Trust (QQQ) was 0.2% higher in Friday's...
- [Energy Leads Sectors In Thursday Trading As Materials Trail](https://www.google.com/goto?url=CAESsQEBxCJF13CXaBMoSpaXLB_oYyF2SenZTRdMW8f8oLEGXLLBLpGoeTWY9ndBVM-g3i9ysF2CATwjNWDbprsIyvN2Zwj2V5LGyqO0EW_q4NzXc3ib5S9SIpfo-LGeWq9PQwPZqZGHi9qFZOVx-G1WKbL2L-7oHg3CtAoU74wj8gvJ3iw0o_HA5iDONK3rOR8OZSHbLBRAMJfbhBMKnK8oeW1kGqVxcdRDa66KTwbUDGQe37s&gsessionid=a5HFDyO-7mVs91EOyGyELGArvLfa2Zo5dLhIdxoGDuDro3fMS4KdWA)  
  <sub>Benzinga, 23 hours ago</sub>  
  Five sectors are higher and six are lower in Thursday's regular session, with cyclical, defensive and growth sectors split across the top three positions.
- [This ETF Has Gained 23% This Year. Is It Still Worth Buying in 2026?](https://www.google.com/goto?url=CAESlwEBxCJF17yq6RbUkEoEJ1qQQtBDJ1kehNsp7PGanjLjQA4gL6uoJDKeg-RUrHFtR0Wfmn9WDqCHiEXsSTT2r8vTzQbO7aRar2GT3X23QIUr7AoizjOXEnMgVmqSe5wh4liPe3E7vRZvZnCfb52oEZ3r-zmw9D99dMlxKCNQJFVF22AawQhD9OlkdteT1SxZy_9ZFLwUwDIy&gsessionid=a5HFDyO-7mVs91EOyGyELGArvLfa2Zo5dLhIdxoGDuDro3fMS4KdWA)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  For the past few years, it seems all that investors care about is tech, artificial intelligence (AI), and growth stocks. The S&P 500 (SNPINDEX: ^GSPC) has...
- [Do Wall Street Analysts Like Sysco Stock?](https://www.google.com/goto?url=CAESngEBxCJF1-XLh5UC_B5hKCnwmA9kO7uDPIDAUxBJDLI_CAOXO41RU9Id6o3lUzNukXAjEExCwFVlO2ETJUoj_ulKvMJgZDAqVxcb2STRt7hj0EdeU0GcpyU0K4hMAbNaYvd9WEMnuPgKQGPcaoKw_ShSFJ3zo8xd5JmM07Rf90Z6iSQqhdg1d8ruxLpp5N8r48ufTw4NAJZEv3aifK42Tw&gsessionid=a5HFDyO-7mVs91EOyGyELGArvLfa2Zo5dLhIdxoGDuDro3fMS4KdWA)  
  <sub>Yahoo Finance, 7 hours ago</sub>  
  With a market cap of $37.9 billion, Sysco Corporation (SYY) is a global leader in selling, marketing, and distributing food and related products to...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 91.87 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 89.46 (+2.7%), 50d 85.64 (+7.3%), 200d 84.88 (+8.2%); 50d above 200d
Momentum: RSI(14) 63.7 | MACD 1.704 vs signal 1.644 (histogram 0.059)
Returns: 1d +0.9% | 5d +2.0% | 1m +6.0% | 3m +8.5%
52-week range: 76.51 - 91.94 (now 99.5% of the way up)
Volatility: ATR(14) 1.47 (1.6% of price) | annualised 20d 23.7%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Consumer Defensive
What it holds: P/E 24.06 | P/B 4.52 | P/S 1.32 | 3y earnings growth n/a
Yield: 2.5%
Three-year record: +12.9% a year | beta to the market 0.39
Cost and size: expense ratio 0.08% | net assets 15.03B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Walmart Inc 11.1%, Costco Wholesale Corp 9.1%, Procter & Gamble Co 7.6%, Coca-Cola Co 7.4%, Philip Morris International Inc 6.6%
Sector mix: Consumer defensive 97.0%, Financial services 1.5%, Consumer cyclical 1.5%
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
Rolled up from the 5 largest holdings, 41.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +1.4% above the current prices
Holdings read: WMT, COST, PG, KO, PM
Recent rating changes among them:
  - WMT: 2026-11-12 BTIG: reit, Buy -> Buy
  - COST: 2026-11-11 Bernstein: main, Outperform -> Outperform
  - PG: 2026-10-26 Barclays: main, Equal-Weight -> Equal-Weight
  - KO: 2026-10-28 Freedom Broker: main, Hold -> Hold
  - PM: 2026-11-03 Stifel: main, Buy -> Buy
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
Shares outstanding: 210.17M | fund size: 19.31B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst view is offset by flat fund flows, mixed technicals, and unchanged macro backdrop.

**Main reasons it gave:**
- Analyst consensus 80% buy, weighted price target +9.3% above current price
- Fund flows flat: 0% change over 1 week and 1 month
- Technical: price above 20‑day and 50‑day SMA but below 200‑day SMA, low volume
- Macro: yields up modestly, no policy surprise; VIX down but still elevated

<details><summary><b>News</b> — score +0.00</summary>

- [Why Is IREN Stock Falling on Thursday?](https://www.benzinga.com/trading-ideas/movers/26/11/63201719/why-is-iren-stock-falling-on-thursday-4)  
  <sub>Benzinga, 23 hours ago</sub>  
  IREN stock falls Thursday after Jensen Huang's immediate resignation as Nvidia CEO, adding to pressure on AI infrastructure stocks from midterm ballot...
- [Do Wall Street Analysts Like PPL Corporation Stock?](https://www.barchart.com/story/news/8821267/do-wall-street-analysts-like-ppl-corporation-stock)  
  <sub>Barchart.com, 1 hour ago</sub>  
  PPL Corporation (PPL) is an American energy utility holding company headquartered in Allentown, Pennsylvania. The company has a market cap of $26.6 billion...
- [IREN Shares Slide as Nvidia Leadership Shock Hits AI and Data Center Names](https://www.google.com/goto?url=CAESgAEBxCJF12-iLlJxg4C602FhcAnQeJihYSsq9mWNPTcn_ANZiTTUGBGqkmOabGzSNOa7Lhk01I10RxD7zWneu8oGQ4jLfAeVT8ASbs-Mux5_q4vTEX60ZEtBoW5cTpVNgXTZ_ivh2lE6yU-pMwaBJ2T55xwC7MNFG0cZHLO-4KIvzg&gsessionid=evyMkVaDzTspsWBlsSYwfUjiJMdoTCv_92-gSsRvQGLc85dqUrGNCQ)  
  <sub>BigGo Finance, 22 hours ago</sub>  
  IREN Limited shares fell Thursday as a leadership shakeup at NVIDIA, where co-founder Jensen Huang resigned as president, CEO and director and CFO…
- [Ameren Stock: Is Wall Street Bullish or Bearish?](https://www.google.com/goto?url=CAESlwEBxCJF14P43DtEoi9OAW5D3l8N1REwnm3ppE_Vhj6spM7Yrir9DfEWRn-ckK9lqk1G33HxSVSZ__J9M3bfwbDpbv_Wp012UDH0ee4lC-W9NEUEOGnTbayo84u4IUbV6_3tuKaHqCy31FfkkNEES4xlMoWJdO3FvJ-wGYkEI1BzOtPs4nukMGshvYIjSS1NfT7TCg1IpO5h&gsessionid=evyMkVaDzTspsWBlsSYwfUjiJMdoTCv_92-gSsRvQGLc85dqUrGNCQ)  
  <sub>Barchart.com, 1 hour ago</sub>  
  Ameren Corporation (AEE) is an American utility holding company headquartered in St. Louis, Missouri. Ameren operates through three primary businesses:...
- [Energy Leads Sectors In Thursday Trading As Materials Trail](https://www.google.com/goto?url=CAESsQEBxCJF1wagcOxNvH9rzB1CspPDNp7o97JeLNbFBwyxv0DmUXx7ZkK6VKHabPTl2qAQjqtSghC-mKDPPiQyC5MQlgyaA0JnICTcDn9Q37ulAIedVxjHJw1z5mjRLUwajXelyNjeEjgk-ym2NQi-O07AkxxYgYIVAqB7aVCrdE8q470xmoQ4NkvlnpWiloqK-b3N4t4BV43O4XCQodcCo-4XbDJ1x8OSRZ1I0dxW7SjohQ8&gsessionid=evyMkVaDzTspsWBlsSYwfUjiJMdoTCv_92-gSsRvQGLc85dqUrGNCQ)  
  <sub>Benzinga, 23 hours ago</sub>  
  Five sectors are higher and six are lower in Thursday's regular session, with cyclical, defensive and growth sectors split across the top three positions.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 43.94 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 43.07 (+2.0%), 50d 41.89 (+4.9%), 200d 44.33 (-0.9%); 50d below 200d
Momentum: RSI(14) 65.0 | MACD 0.570 vs signal 0.528 (histogram 0.042)
Returns: 1d +0.3% | 5d +1.9% | 1m +5.5% | 3m -0.5%
52-week range: 39.25 - 47.73 (now 55.4% of the way up)
Volatility: ATR(14) 0.59 (1.3% of price) | annualised 20d 15.3%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Utilities
What it holds: P/E 17.87 | P/B 2.03 | P/S 2.51 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +16.7% a year | beta to the market 0.34
Cost and size: expense ratio 0.08% | net assets 24.25B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: NextEra Energy Inc 12.8%, Southern Co 7.9%, Duke Energy Corp 7.3%, Constellation Energy Corp 6.3%, American Electric Power Co Inc 5.2%
Sector mix: Utilities 100.0%
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
Rolled up from the 5 largest holdings, 39.4% of the fund by weight
Ratings by weight: buy 80.0% | hold 20.0% | sell 0.0% (mean 2.02 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.3% above the current prices
Holdings read: NEE, SO, DUK, CEG, AEP
Recent rating changes among them:
  - NEE: 2026-10-23 Barclays: main, Equal-Weight -> Equal-Weight
  - SO: 2026-10-22 HSBC: init, ? -> Buy
  - DUK: 2026-10-22 HSBC: init, ? -> Hold
  - CEG: 2026-10-30 Morgan Stanley: main, Overweight -> Overweight
  - AEP: 2026-11-02 Barclays: main, Equal-Weight -> Equal-Weight
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
Shares outstanding: 163.27M | fund size: 7.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals across analyst view, fund flows and fundamentals keep the overall stance neutral.

**Main reasons it gave:**
- Mixed fund flows: +1.1% weekly inflow but -1.8% monthly outflow
- High valuations: P/E 24.15, P/B 5.62
- Macro tightening: 10‑year yield up 31 bps, Fed target 4.0% with expected hikes
- Technicals: price above SMAs but 50‑day SMA below 200‑day SMA, low volume

<details><summary><b>News</b> — score +0.00</summary>

- [Quick spark: Tesla stock has best 5-day rally in over a year as Elon Musk pushes for SpaceX merger by December](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af72452295f42d0acfc7285aa170b1c&url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fquick-spark-tesla-stock-has-best-5-day-rally-in-over-a-year-as-elon-musk-pushes-for-spacex-merger-by-december%2far-AA2hjzzK&c=17180068808703077449&mkt=en-us)  
  <sub>Benzinga on MSN, 26h ago</sub>  
  Elon Musk wants his two largest companies under one roof, and he wants it fast. Space Exploration Technologies Corp. SPCX and Tesla Inc. TSLA are moving toward what would be the largest corporate ...
- [Only these two consumer discretionary stocks carry long-standing sell quant ratings](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af72452295f42d0acfc7285aa170b1c&url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fonly-these-two-consumer-discretionary-stocks-carry-long-standing-sell-quant-ratings%2far-AA2hmPgx&c=11176531641343551283&mkt=en-us)  
  <sub>Seeking Alpha on MSN, 10h ago</sub>  
  Only two consumer discretionary stocks currently carry long standing Sell Quant Ratings, spanning sub-industries such as specialty retail and distributors. DICK'S Sporting Goods, Inc. (DKS) leads the ...
- [Tesla (TSLA) Sees $76.2 Million in Net ETF Buying on Wednesday](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af72452295f42d0acfc7285aa170b1c&url=https%3a%2f%2fuk.finance.yahoo.com%2fnews%2ftesla-tsla-sees-76-2-110209047.html&c=748088829240265763&mkt=en-us)  
  <sub>Yahoo Finance UK, 20h ago</sub>  
  Tesla designs, develops, manufactures, sells, and leases fully electric vehicles and energy generation and storage systems, with a strategic focus on bringing artificial intelligence into the real ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 120.53 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 117.37 (+2.7%), 50d 113.84 (+5.9%), 200d 115.44 (+4.4%); 50d below 200d
Momentum: RSI(14) 61.5 | MACD 2.037 vs signal 1.733 (histogram 0.304)
Returns: 1d +0.1% | 5d +2.5% | 1m +6.3% | 3m +3.2%
52-week range: 105.66 - 124.52 (now 78.8% of the way up)
Volatility: ATR(14) 2.16 (1.8% of price) | annualised 20d 27.1%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 24.15 | P/B 5.62 | P/S 2.30 | 3y earnings growth n/a
Yield: 0.8%
Three-year record: +15.4% a year | beta to the market 1.10
Cost and size: expense ratio 0.08% | net assets 22.40B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Amazon.com Inc 21.3%, Tesla Inc 18.8%, The Home Depot Inc 5.5%, McDonald's Corp 4.5%, TJX Companies Inc 4.1%
Sector mix: Consumer cyclical 98.8%, Technology 1.2%
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
Rolled up from the 5 largest holdings, 54.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.7% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, TJX
Recent rating changes among them:
  - AMZN: 2026-11-03 Freedom Broker: main, Buy -> Buy
  - TSLA: 2026-11-05 GLJ Research: reit, Sell -> Sell
  - HD: 2026-11-10 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-11-06 Argus Research: main, Buy -> Buy
  - TJX: 2026-11-10 UBS: main, Buy -> Buy
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
Share count change: 1 week: +1.1% (240.40M) over 7d | 1 month: -1.8% (-403.19M) over 31d
Shares outstanding: 185.16M | fund size: 22.32B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 44.14 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 43.80 (+0.8%), 50d 44.23 (-0.2%), 200d 40.69 (+8.5%); 50d above 200d
Momentum: RSI(14) 52.4 | MACD -0.095 vs signal -0.159 (histogram 0.064)
Returns: 1d +0.5% | 5d +3.2% | 1m -0.7% | 3m +0.4%
52-week range: 32.56 - 45.76 (now 87.7% of the way up)
Volatility: ATR(14) 0.70 (1.6% of price) | annualised 20d 24.9%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.39 | P/B 2.08 | P/S 1.40 | 3y earnings growth n/a
Yield: 3.4%
Three-year record: +35.6% a year | beta to the market 0.85
Cost and size: expense ratio 0.59% | net assets 1.03B
What it is made of: Stocks 99.4%, Cash 0.6%
Largest holdings: PKO Bank Polski SA 15.0%, Orlen SA 12.8%, Bank Polska Kasa Opieki SA 7.0%, Powszechny Zaklad Ubezpieczen SA 6.1%, Allegro.EU SA Ordinary Shares 5.7%
Sector mix: Financial services 45.2%, Consumer cyclical 14.9%, Energy 13.2%, Basic materials 5.6%
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
Rolled up from the 5 largest holdings, 46.6% of the fund by weight
Ratings by weight: buy 68.5% | hold 31.5% | sell 0.0% (mean 2.28 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.0% above the current prices
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
Direction: money coming in (1 month)
Share count change: 1 week: +1.0% (10.35M) over 7d | 1 month: +24.3% (203.71M) over 30d
Shares outstanding: 23.63M | fund size: 1.04B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error response body was rejected) (Bing's feed, direct: 1 headline(s), none naming EPOL)

### Canada (EWC) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 60.33 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 60.74 (-0.7%), 50d 60.15 (+0.3%), 200d 58.55 (+3.0%); 50d above 200d
Momentum: RSI(14) 49.3 | MACD 0.059 vs signal 0.155 (histogram -0.096)
Returns: 1d +0.3% | 5d +0.7% | 1m +0.0% | 3m -3.0%
52-week range: 49.91 - 62.64 (now 81.9% of the way up)
Volatility: ATR(14) 0.80 (1.3% of price) | annualised 20d 18.6%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.92 | P/B 2.74 | P/S 2.65 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +24.3% a year | beta to the market 0.73
Cost and size: expense ratio 0.50% | net assets 7.58B
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Royal Bank of Canada 9.1%, The Toronto-Dominion Bank 6.7%, Shopify Inc Registered Shs -A- Subord Vtg 6.2%, Bank of Montreal 3.8%, Canadian Natural Resources Ltd 3.8%
Sector mix: Financial services 40.4%, Energy 18.5%, Basic materials 13.1%, Technology 9.3%
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
Rolled up from the 5 largest holdings, 29.5% of the fund by weight
Ratings by weight: buy 87.2% | hold 12.8% | sell 0.0% (mean 2.21 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +5.6% above the current prices
Holdings read: RY, TD, SHOP, BMO.TO, CNQ.TO
Recent rating changes among them:
  - RY: 2025-08-29 Argus Research: main, Buy -> Buy
  - TD: 2026-06-01 RBC Capital: main, Outperform -> Outperform
  - SHOP: 2026-11-05 Argus Research: reit, Buy -> Buy
  - BMO.TO: 2026-05-28 RBC Capital: main, Sector Perform -> Sector Perform
  - CNQ.TO: 2026-03-12 Goldman Sachs: main, Buy -> Buy
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
Share count change: 1 week: +2.1% (155.48M) over 7d | 1 month: +5.4% (388.86M) over 31d
Shares outstanding: 125.29M | fund size: 7.56B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [EWY - iShares MSCI South Korea ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af725630d71476688c8e3dc7d3187fd&url=https%3a%2f%2fseekingalpha.com%2fsymbol%2fEWY%2fbalance-sheet&c=3435854256959578603&mkt=en-us)  
  <sub>Seeking Alpha, 31h ago</sub>  
  Get the detailed balance sheet for iShares MSCI South Korea ETF (EWY). Up to 10 years of financial statements. Quarterly or annual. View as % YoY growth or as % of revenue.
- [[국장방향예측] 코스피 0.52%↑ SK하이닉스 0.21%↓](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af725630d71476688c8e3dc7d3187fd&url=https%3a%2f%2fwww.digitalasset.works%2fnews%2farticleView.html%3fidxno%3d44265&c=9983479230173964584&mkt=en-us)  
  <sub>디지털애셋, 16h ago</sub>  
  *EWY는 미 증시에 상장된 상장지수펀드 (ETF)로, 삼성전자·SK하이닉스 등 국내 대형주를 담은 MSCI 한국 지수를 추종한다. 밤사이 원/달러 환율 변동이 등락률에 함께 반영된다.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 141.74 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 150.11 (-5.6%), 50d 168.44 (-15.9%), 200d 164.01 (-13.6%); 50d above 200d
Momentum: RSI(14) 40.8 | MACD -7.345 vs signal -7.480 (histogram 0.135)
Returns: 1d -2.5% | 5d +3.4% | 1m -9.3% | 3m -23.4%
52-week range: 88.53 - 219.20 (now 40.7% of the way up)
Volatility: ATR(14) 7.20 (5.1% of price) | annualised 20d 72.6%
Volume: 0.09x the 20-day average
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
Three-year record: +38.1% a year | beta to the market 2.62
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
Share count change: 1 week: +4.1% (832.26M) over 7d | 1 month: +1.4% (287.35M) over 31d
Shares outstanding: 149.97M | fund size: 21.26B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Brazil Stock Exchange Profit Up 9.9% in Third Quarter](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af7257e3d2a408eae217f59843d2707&url=https%3a%2f%2fwww.riotimesonline.com%2fbrazil-stock-exchange-b3-third-quarter-profit-2026%2f&c=13927173354892120651&mkt=en-us)  
  <sub>The Rio Times, 24h ago</sub>  
  Brazil's stock exchange B3 earned US$244 million in recurring profit in the third quarter, up 9.9%, as trading and credit fees grew.
- [Ibovespa tem balanços, inflação nos EUA e varejo no radar; Nubank sobe 4% no pré-mercado](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af7257e3d2a408eae217f59843d2707&url=https%3a%2f%2fwww.msn.com%2fpt-br%2fdinheiro%2fprincipais-a%25C3%25A7%25C3%25B5es%2fibovespa-tem-balan%25C3%25A7os-infla%25C3%25A7%25C3%25A3o-nos-eua-e-varejo-no-radar-nubank-sobe-4-no-pr%25C3%25A9-mercado%2far-AA2hm3Ag&c=3423254124090040729&mkt=en-us)  
  <sub>Estadão on MSN, 10h ago</sub>  
  Após recuo de 0,43% na sessão anterior, índice acompanha resultados corporativos e indicadores econômicos que podem influenciar as expectativas para os juros no Brasil e nos EUA ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 32.21 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 35.03 (-8.0%), 50d 37.59 (-14.3%), 200d 37.01 (-13.0%); 50d above 200d
Momentum: RSI(14) 34.2 | MACD -1.982 vs signal -1.830 (histogram -0.152)
Returns: 1d +1.4% | 5d +0.7% | 1m -22.5% | 3m -5.2%
52-week range: 30.97 - 43.54 (now 9.9% of the way up)
Volatility: ATR(14) 1.07 (3.3% of price) | annualised 20d 73.6%
Volume: 0.07x the 20-day average
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
Three-year record: +6.1% a year | beta to the market 0.92
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
Weighted price target: +32.9% above the current prices
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
Shares outstanding: 200.55M | fund size: 6.46B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [ITA vs ARKX: Can an Earthbound Aerospace ETF Outpace a Space Fund?](https://www.fool.com/coverage/etfs/2026/11/12/ita-vs-arkx-can-an-earthbound-aerospace-etf-outpace-a-space-fund/)  
  <sub>The Motley Fool, 17 hours ago</sub>  
  The iShares U.S. Aerospace & Defense ETF (ITA -2.06%) provides a low-cost, index-based approach to domestic defense, while the ARK Space & Defense...
- [BAC: SEC Form FWP filed by Bank of America Corporation](https://www.google.com/goto?url=CAESmQEBxCJF1zzVxnVgcDYoz-DVYDeAyQ7Tqx9xXNABAPT8FRAWPQowBepHyWTEPtFTrO56QB7xYJ90doYBk-9sgWx25D79UCK8rIp9-0QjKb7Jv1YW_OjzoAKQskR6srnUSMeJ6EUSTvTWEQ0BL4KvGz-RKjfSA17AtFA-KjUpOiKky54s0bin3oSqbcOs6zV8ZN5ugty1FbUTLUg&gsessionid=dMLF_gNxEaZ3LJg3AUlTz30NL42-A70KrVqokfdOzOq54RuKsOuxgA)  
  <sub>Quantisnow, 22 hours ago</sub>  
  BofA Finance LLC, guaranteed by Bank of America, is offering 14-month notes tied to the iShares U.S. Aerospace & Defense ETF (ITA).
- [5 Best Invesco ETFs to Buy Now | Investing](https://www.google.com/goto?url=CAEShwEBxCJF1-fId_bq3r8ArFrQ99oU9HcvpSpzuZbJYahpTD_eoSoWZVBOWIZPL5nvz-Npi0Y9-virovCzY9xKFyOUjP2uoeEik-zhSZl2BLOZnrpajvDeqmsXIloZZ9cAwpMtDKhaHDqryQZpLMZGuUz4MpvGClcjZjlyJVRObYdnAHg7khR6NgI&gsessionid=dMLF_gNxEaZ3LJg3AUlTz30NL42-A70KrVqokfdOzOq54RuKsOuxgA)  
  <sub>US News Money, 18 hours ago</sub>  
  These five top Invesco ETFs offer investors a range of strategies, from Nasdaq-100 growth and equal-weight equities to bonds, commodities, and aerospace and...
- [Anduril eyes IPO within 2 years as it challenges defense giants (PPA:NYSEARCA)](https://www.google.com/goto?url=CAESogEBxCJF1_JDF273fVDhGrRjxdANgpkLheI-D0iE3ZKs3Ny2Vzn7xJL3fC8691xWFgNmYTufkWR-beo0a9KeGVdDB8y7io_RwomgXIqIJ8ip1G46S8lV1RCUa5f5pIgZ_Rn7ImyDoSjOrQDx1E96D_y_zRv5QVDWeIIGWPSVRKK2jln-ZFHHWZyBVW72tBqn4fWtkkkZKy2fZXeWAbNbUmAxuPQ&gsessionid=dMLF_gNxEaZ3LJg3AUlTz30NL42-A70KrVqokfdOzOq54RuKsOuxgA)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Anduril hopes to go public within two years as it urges the Pentagon to split defense orders among suppliers, following a $1.8 billion Army project.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 71.36 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 70.13 (+1.8%), 50d 70.40 (+1.4%), 200d 75.92 (-6.0%); 50d below 200d
Momentum: RSI(14) 52.8 | MACD 0.412 vs signal 0.072 (histogram 0.340)
Returns: 1d -0.5% | 5d +3.5% | 1m +3.5% | 3m -14.8%
52-week range: 66.08 - 84.41 (now 28.8% of the way up)
Volatility: ATR(14) 1.76 (2.5% of price) | annualised 20d 30.8%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Industrials
What it holds: P/E 30.89 | P/B 5.67 | P/S 2.83 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +25.3% a year | beta to the market 1.03
Cost and size: expense ratio 0.37% | net assets 12.22B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: GE Aerospace 20.0%, RTX Corp 17.2%, Boeing Co 6.8%, Lockheed Martin Corp 5.7%, Northrop Grumman Corp 5.1%
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
Rolled up from the 5 largest holdings, 54.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.74 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.1% above the current prices
Holdings read: GE, RTX, BA, LMT, NOC
Recent rating changes among them:
  - GE: 2026-10-21 UBS: main, Buy -> Buy
  - RTX: 2026-10-21 UBS: main, Neutral -> Neutral
  - BA: 2026-10-29 Bernstein: main, Outperform -> Outperform
  - LMT: 2026-11-04 Guggenheim: init, ? -> Buy
  - NOC: 2026-10-27 Bernstein: main, Market Perform -> Market Perform
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
Share count change: 1 week: +190.3% (7.80B) over 7d | 1 month: +184.1% (7.71B) over 30d
Shares outstanding: 166.80M | fund size: 11.90B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Better U.S. Bank ETF: State Street's KBE vs. First Trust's FTXO](https://finance.yahoo.com/markets/stocks/articles/better-u-bank-etf-state-050341569.html)  
  <sub>Yahoo Finance, 10 hours ago</sub>  
  The State Street SPDR S&P Bank ETF (NYSEMKT:KBE) offers a more diversified, lower-cost entry into the banking sector compared to the concentrated and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 72.48 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 72.37 (+0.2%), 50d 71.72 (+1.1%), 200d 71.22 (+1.8%); 50d above 200d
Momentum: RSI(14) 51.7 | MACD 0.416 vs signal 0.414 (histogram 0.002)
Returns: 1d -0.1% | 5d +0.4% | 1m +3.9% | 3m -6.3%
52-week range: 58.63 - 77.93 (now 71.8% of the way up)
Volatility: ATR(14) 1.37 (1.9% of price) | annualised 20d 20.9%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Financial
What it holds: P/E 12.00 | P/B 1.21 | P/S 3.59 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +24.1% a year | beta to the market 0.97
Cost and size: expense ratio 0.35% | net assets 4.01B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Glacier Bancorp Inc 1.2%, United Community Banks Inc 1.2%, Texas Capital Bancshares Inc 1.2%, Bank OZK 1.2%, Eastern Bankshares Inc Ordinary Shares 1.2%
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
Rolled up from the 5 largest holdings, 5.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 50.1% | hold 49.9% | sell 0.0% (mean 2.27 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.6% above the current prices
Holdings read: GBCI, UCB, TCBI, OZK, EBC
Recent rating changes among them:
  - GBCI: 2026-10-26 Piper Sandler: main, Overweight -> Overweight
  - UCB: 2026-10-21 Stephens & Co.: main, Overweight -> Overweight
  - TCBI: 2026-11-03 Barclays: main, Equal-Weight -> Equal-Weight
  - OZK: 2026-10-30 Keefe, Bruyette & Woods: main, Market Perform -> Market Perform
  - EBC: 2026-11-03 Barclays: main, Equal-Weight -> Equal-Weight
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
Share count change: 1 week: +1.7% (65.47M) over 7d | 1 month: +1.8% (69.93M) over 30d
Shares outstanding: 54.95M | fund size: 3.98B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Is State Street SPDR S&P Homebuilders ETF (XHB) a Strong ETF Right Now?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af7249a4c4747989165a6a2e7ce0234&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2fstate-street-spdr-p-homebuilders-102002249.html&c=16037635198801674616&mkt=en-us)  
  <sub>Yahoo Finance, 13h ago</sub>  
  The State Street SPDR S&P Homebuilders ETF (XHB) made its debut on 01/31/2006, and is a smart beta exchange traded fund that provides broad exposure to the Industrials ETFs catego ...
- [Peter Schiff’s chilling warning: Get ready for the mother of all housing crashes](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af7249a4c4747989165a6a2e7ce0234&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2feconomy%2fpeter-schiff-s-chilling-warning-get-ready-for-the-mother-of-all-housing-crashes%2far-AA2hj98k&c=4656069185557627159&mkt=en-us)  
  <sub>Benzinga on MSN, 30h ago</sub>  
  U.S. existing-home sales just hit a level not seen since 2010. But Peter Schiff believes the most dangerous part may still be ahead. Unlike 2010, when home prices had already collapsed, he argues ...
- [AI capital buildout raising housing funding costs - Fed's Schmid](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af7249a4c4747989165a6a2e7ce0234&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2feconomy%2fai-capital-buildout-raising-housing-funding-costs-fed-s-schmid%2far-AA2hjr0p&c=4804865872563135242&mkt=en-us)  
  <sub>Seeking Alpha on MSN, 28h ago</sub>  
  Making housing (XLRE) more affordable requires boosting construction productivity rather than relying on central bank interest rate cuts, according to Federal Reserve Bank of Kansas City President ...
- [Mortgage rates hit lowest level in seven weeks](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af7249a4c4747989165a6a2e7ce0234&url=https%3a%2f%2fseekingalpha.com%2fnews%2f4671634-mortgage-rates-hit-lowest-level-in-seven-weeks&c=4831809819537682691&mkt=en-us)  
  <sub>Seeking Alpha, 30h ago</sub>  
  Mortgage rates hit their lowest level in seven weeks, according to the Freddie Mac Weekly Mortgage Applications Survey.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 101.81 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 100.82 (+1.0%), 50d 98.50 (+3.4%), 200d 104.69 (-2.8%); 50d below 200d
Momentum: RSI(14) 52.3 | MACD 1.424 vs signal 1.417 (histogram 0.007)
Returns: 1d +0.5% | 5d -0.5% | 1m +6.3% | 3m -5.9%
52-week range: 92.84 - 121.36 (now 31.5% of the way up)
Volatility: ATR(14) 2.83 (2.8% of price) | annualised 20d 39.6%
Volume: 0.05x the 20-day average
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
Three-year record: +10.9% a year | beta to the market 1.40
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.9% above the current prices
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
Share count change: 1 week: +4.3% (66.76M) over 7d | 1 month: +4.8% (74.27M) over 30d
Shares outstanding: 15.82M | fund size: 1.61B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [State Street Comm Services SPDR (XLC) Adds Meta and Alphabet on Nov. 11](https://ca.finance.yahoo.com/news/state-street-comm-services-spdr-110501441.html)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Communication Services Select Sector SPDR ETF (XLC) was the single fund in this report, and its ETF...
- [These four communication services stocks have stayed Strong Buys for weeks (XLC:NYSEARCA)](https://seekingalpha.com/news/4671656-these-four-communication-services-stocks-have-stayed-strong-buys-for-weeks)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Cinemark and Stagwell lead Seeking Alpha's Communication Services Strong Buy ranking at 102 days each; NIQ has 88 days and AMC 49.
- [ETFs Are Buying Alphabet (GOOGL) on Nov. 11](https://www.google.com/goto?url=CAESnAEBxCJF10gkNUtjL6z9GJM0BF9pwKldSYUfMmhNO-m8eSJQFWbnJzXqK3C-FZ6aGvSW4d-Bh0QTFU49HagOgv_dL3hyS7PUdPaDSIp04A0W7kZgMgvzruxq5LUPEbizLYkOU6tsozWrevPKDMA4l9Zma2FL1a_x22aN7frXEIwrfQGzZ9ea-vRIwyWKGwSis1EYADH7h4mT_NGfljo&gsessionid=iKARqCRXe0HauG1IWwaNcQfMOYF6GUFkCmYJ_5xHFP8VfKdKC4vKIg)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  ETFs bought $130.4 million of Alphabet (GOOGL) shares on Wednesday.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 108.97 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 105.50 (+3.3%), 50d 109.39 (-0.4%), 200d 112.37 (-3.0%); 50d below 200d
Momentum: RSI(14) 56.3 | MACD -0.491 vs signal -1.355 (histogram 0.864)
Returns: 1d +1.3% | 5d +4.0% | 1m -3.1% | 3m -1.7%
52-week range: 99.90 - 120.08 (now 44.9% of the way up)
Volatility: ATR(14) 2.00 (1.8% of price) | annualised 20d 22.4%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Communications
What it holds: P/E 15.87 | P/B 3.10 | P/S 2.22 | 3y earnings growth n/a
Yield: 1.4%
Three-year record: +18.0% a year | beta to the market 0.93
Cost and size: expense ratio 0.08% | net assets 21.45B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Meta Platforms Inc Class A 22.0%, Alphabet Inc Class A 11.1%, Alphabet Inc Class C 8.9%, The Walt Disney Co 5.6%, Comcast Corp Class A 4.9%
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.40 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +28.5% above the current prices
Holdings read: META, GOOGL, GOOG, DIS, CMCSA
Recent rating changes among them:
  - META: 2026-10-22 UBS: main, Buy -> Buy
  - GOOGL: 2026-11-02 Wells Fargo: main, Overweight -> Overweight
  - GOOG: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - DIS: 2026-10-16 Citigroup: main, Buy -> Buy
  - CMCSA: 2026-10-26 Freedom Broker: main, Hold -> Hold
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
Share count change: 1 week: -3.3% (-744.46M) over 7d | 1 month: -3.3% (-723.20M) over 30d
Shares outstanding: 197.47M | fund size: 21.52B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions answered with an empty message

<details><summary><b>News</b> — score n/a</summary>

- [Trending ETFs today](https://uk.finance.yahoo.com/markets/etfs/trending/)  
  <sub>Yahoo Finance UK, 10 hours ago</sub>  
  Vanguard FTSE All-World UCITS ETF USD Accumulation. 170.40. -1.02 (-0.60%). -1.02, -0.60%, 11,205, --, --, --, --, +18.84%. 139.20 173.96.
- [These five energy stocks remain under pressure with persistent Sell ratings (XLE:NYSEARCA)](https://seekingalpha.com/news/4672261-these-five-energy-stocks-remain-under-pressure-with-persistent-sell-ratings)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Five energy stocks carry Sell or Strong Sell Quant Ratings for 23 to 123 days; Peabody Energy leads at 123 days, while Uranium Energy scores 1.22.
- [Energy Leads Sectors In Thursday Trading As Materials Trail](https://www.google.com/goto?url=CAESsQEBxCJF18KQvaTzyqH3_G0_3G2eNtHwYOakaF-BhbP1PACfZoGOTFXJOheCd25KutiSb6UjUcdgXBd3-jk6H6GSXquBU9KcJdWnX3NPSrWvxxNtGY0mJboaZIe5vpxwQE6ANZsFbfkQPOrpi29S0CIBcRIagtUR8v6ARHhihW6KdTUNLbaWRILa5DlyrcSi-u6pwrjap-tvu4lXSuZwcTeW615CJmqxPZwc3xzFrTft7Wc&gsessionid=GnLX-k8lfa2Cs7pVkJmL3xQNIhm-YyRDbqC3K-1Zg7cXg4nQUtYsEw)  
  <sub>Benzinga, 23 hours ago</sub>  
  Five sectors are higher and six are lower in Thursday's regular session, with cyclical, defensive and growth sectors split across the top three positions.
- [XOP vs AMLP. Is a Midstream or Upstream Energy ETF the Better Buy as Oil Prices Stay High?](https://www.google.com/goto?url=CAESlAEBxCJF1ydWXhH7AJmo6WJd5Xii9d6Y6AfTx2tZvRt2_ENIC4kyM7sZVbtC2FeaGHyJI8J8elt9o9b9X2AyUNJ0CrRYMOmWaY3pwTxTedU1hKNQ0iyRvLgH8rhxWT5U8ayNVxLj_tgUoLqrisqAxDSA2g8rIPiPEE39xH9xo1voBlc_ikQPsXywyP_qYbTcF_kUL_IJ&gsessionid=GnLX-k8lfa2Cs7pVkJmL3xQNIhm-YyRDbqC3K-1Zg7cXg4nQUtYsEw)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  The Alerian MLP ETF (NYSEMKT:AMLP) provides high-yield exposure to midstream energy infrastructure, while the State Street SPDR S&P Oil & Gas Exploration...
- [Bill Baruch: NVDA dip, AVGO & AMD gains, XLE rally after Trump comment](https://www.google.com/goto?url=CAESqgEBxCJF19beAB94VDbpBzwdh7ViTZJ0FWAml8FDSSjh-ufiku-Rah5zOsLR2nt-iKMekdJwLkv8UljLV5deIehK1X_EcCpuRI_w_WsPcNrA-AMwLvGC_BRKSK9FXdPi5fvkRIhHPFvVE53i0k0GfAFNGSPD2ok39w8XCMG1Da2NwmJQVIAfIJV1_UyucfSlyZddltH6-w_eEMLT_GIubgEp8GG3qlHMQp4YFg&gsessionid=GnLX-k8lfa2Cs7pVkJmL3xQNIhm-YyRDbqC3K-1Zg7cXg4nQUtYsEw)  
  <sub>Barchart.com, 16 hours ago</sub>  
  Quite the week. $NVDA Jensen news keeps piling on but stock finished off its worst levels. $AVGO $AMD $GOOG beneficiaries. $XLE best sector after Trump...
- [Why Is IREN Stock Falling on Thursday?](https://www.google.com/goto?url=CAESoQEBxCJF1wOIvKcPG9rIKWRt1i8RKklHKVULmVXVu1pgn1fwQ5dQcoOyOVkJZuqaD1axetFON-CCHKCKAO16uckugNT0gt9Z-jbKSyek3dUkMb3GuUwK-fBMhbXVjg4rzCla6YtwcFPORqPSGf51_8WnJf42vLIe3QTFq7V2pk-yITtgtE6MlVHoceVtC-aYro8uCUjFAvg69aIkZtR5uypinA&gsessionid=GnLX-k8lfa2Cs7pVkJmL3xQNIhm-YyRDbqC3K-1Zg7cXg4nQUtYsEw)  
  <sub>Benzinga, 22 hours ago</sub>  
  IREN stock falls Thursday after Jensen Huang's immediate resignation as Nvidia CEO, adding to pressure on AI infrastructure stocks from midterm ballot...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 64.40 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 66.14 (-2.6%), 50d 64.97 (-0.9%), 200d 59.47 (+8.3%); 50d above 200d
Momentum: RSI(14) 47.1 | MACD -0.642 vs signal -0.209 (histogram -0.433)
Returns: 1d +0.1% | 5d +4.5% | 1m -3.2% | 3m +2.9%
52-week range: 43.81 - 70.02 (now 78.6% of the way up)
Volatility: ATR(14) 1.58 (2.5% of price) | annualised 20d 30.2%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Equity Energy
What it holds: P/E 17.48 | P/B 2.46 | P/S 1.71 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +18.6% a year | beta to the market -0.22
Cost and size: expense ratio 0.08% | net assets 46.37B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ExxonMobil Holdings Corp 24.3%, Chevron Corp 18.3%, ConocoPhillips 7.3%, Marathon Petroleum Corp 4.6%, Phillips 66 4.5%
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
US inventories, week ending 2026-11-06 (published the following Wednesday)
  Crude oil: 414.4 million barrels, +4.7 on the week (a build), 21% percentile over 52 weeks
  Diesel: 99.3 million barrels, -3.6 on the week (a draw), 2% percentile over 52 weeks -- low for the time of year
  Natural gas: 3,801.0 billion cubic feet, +77.0 on the week (a build), 92% percentile over 52 weeks -- high for the time of year
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
Rolled up from the 5 largest holdings, 59.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.10 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.1% above the current prices
Holdings read: XOM, CVX, COP, MPC, PSX
Recent rating changes among them:
  - XOM: 2026-11-12 Bernstein: main, Outperform -> Outperform
  - CVX: 2026-11-12 Bernstein: main, Market Perform -> Market Perform
  - COP: 2026-11-12 Bernstein: down, Outperform -> Market Perform
  - MPC: 2026-11-05 Piper Sandler: main, Overweight -> Overweight
  - PSX: 2026-11-04 Citigroup: main, Neutral -> Neutral
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
Shares outstanding: 186.42M | fund size: 12.01B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [This ETF Has Gained 23% This Year. Is It Still Worth Buying in 2026?](https://finance.yahoo.com/markets/stocks/articles/etf-gained-23-still-worth-115700654.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  For the past few years, it seems all that investors care about is tech, artificial intelligence (AI), and growth stocks. The S&P 500 (SNPINDEX: ^GSPC) has...
- [State Street Health Care SPDR (XLV) Buys $66.8 Million More Eli Lilly on Nov. 11](https://finance.yahoo.com/healthcare/articles/state-street-health-care-spdr-110327637.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Health Care Select Sector SPDR ETF (XLV) recorded net buying of $396.8 million in Wednesday's session...
- [ETFs Are Buying Eli Lilly (LLY) on Nov. 11](https://www.google.com/goto?url=CAESlwEBxCJF1036GLCNask8Cjy3gDsvvdOEMqU_5dg_RBBwzM6juylr_4mrMVOsPApjqWlseNjGcXzHMvp9QCjBqX_k9B6dEETIS1Gn4n9b0bZG1cxlTgct9hToRRpLXUUlP5nxy64fBjm6xPq7Zstkogsdoizc5xLXN7ZsgAz6dUHqzdMgc2liWPXaE0CpuIEKXc2F2DcoaxsT&gsessionid=ex7MjpQrX57GBLmq_7k7doJs9tb4s3JW-OAb5E1zQMRhPu1STpZeRA)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. ETFs bought a net $154.5 million of Eli Lilly (LLY) on Wednesday, Nov. 11, as 49 funds added shares and 11 trimmed...
- [5 AI Chip Stocks to Buy as Nvidia’s Turmoil Reshapes the Sector](https://www.google.com/goto?url=CAESpwEBxCJF16avj2lNkJATxS16NoHvij1MgX-unAUr9ilWeUdZ8sLwsFjI4HAA0hAH1BMlFn0C8XZQb1tHl4YDlOIgxj7U9JeQfE7IFJ61GmElHeXH9Zvmbh-ZOl26hO4OkKYb5_ITw8nLtIzntgPtJ71rVg-_NsRVmqhz8IHffn5LsvR5IVVN9SR2T_pbGzw_oNVFAGVCrghiXkbjQ0UPl7vOFVUvmzE4fA&gsessionid=ex7MjpQrX57GBLmq_7k7doJs9tb4s3JW-OAb5E1zQMRhPu1STpZeRA)  
  <sub>Investing.com Canada, 5 hours ago</sub>  
  Market Analysis by Jesse Cohen covering: Nasdaq 100, S&P 500, Dow Jones Industrial Average, State Street® SPDR® Dow Jones Industrial Average® ETF Trust.
- [While AI hogged the headlines, 1 overlooked sector beat the S&P 500 — and its top stock is up 700%+ this year](https://www.google.com/goto?url=CAESlQEBxCJF15V66_507BJ6SNLyU90M1O4yCvkwe51Z2Yg-AsYUUfk1t7vof1aygGH57FyANegPgxyMQ9-5Vuz2RmEW9Wf-QgfjirKhdTTWNHlI-Kd7hIVLwuFRiptv05yI-smbEW0q20ZJmbVrfMKffFhBhUDDjdWaVZmT6LV4OBXLO-AVrbmtgF27w5ar5356a-t9XfVTlA&gsessionid=ex7MjpQrX57GBLmq_7k7doJs9tb4s3JW-OAb5E1zQMRhPu1STpZeRA)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Moneywise and Yahoo Finance LLC may earn commission or revenue through links in the content below. The stock market has been on a nauseating seesaw at the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 187.87 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 183.60 (+2.3%), 50d 175.03 (+7.3%), 200d 160.20 (+17.3%); 50d above 200d
Momentum: RSI(14) 65.3 | MACD 3.980 vs signal 3.910 (histogram 0.071)
Returns: 1d +0.0% | 5d +1.7% | 1m +6.0% | 3m +12.5%
52-week range: 142.84 - 189.66 (now 96.2% of the way up)
Volatility: ATR(14) 3.29 (1.8% of price) | annualised 20d 21.0%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Health
What it holds: P/E 30.14 | P/B 4.82 | P/S 1.66 | 3y earnings growth n/a
Yield: 1.4%
Three-year record: +16.3% a year | beta to the market 0.41
Cost and size: expense ratio 0.08% | net assets 49.10B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Eli Lilly and Co 16.9%, Johnson & Johnson 9.8%, AbbVie Inc 7.8%, Merck & Co Inc 5.5%, UnitedHealth Group Inc 5.4%
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
Rolled up from the 5 largest holdings, 45.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.7% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-11-09 Jefferies: main, Buy -> Buy
  - JNJ: 2026-10-16 Wells Fargo: main, Overweight -> Overweight
  - ABBV: 2026-11-02 UBS: main, Neutral -> Neutral
  - MRK: 2026-11-02 Freedom Broker: main, Hold -> Hold
  - UNH: 2026-10-27 Wells Fargo: main, Overweight -> Overweight
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
Share count change: 1 week: +0.4% (174.94M) over 7d | 1 month: +2.3% (1.09B) over 31d
Shares outstanding: 259.85M | fund size: 48.82B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals show slight short‑term weakness but no decisive break, positioning is a crowded long with a small net‑long reduction, and the fund bears a heavy roll cost.

**Main reasons it gave:**
- Treasury yields up modestly across the curve, no macro surprise
- RSI 41 and MACD -0.207 vs signal -0.150, slight short‑term weakness
- Large speculators net long 18.8% of OI, down 0.9% week, crowded long (90th percentile)
- Cost of holding -8.1% annual, heavy roll cost for long positions

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 11.12 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 11.50 (-3.3%), 50d 11.60 (-4.2%), 200d 10.30 (+8.0%); 50d above 200d
Momentum: RSI(14) 41.0 | MACD -0.207 vs signal -0.150 (histogram -0.057)
Returns: 1d +1.0% | 5d +0.9% | 1m -10.8% | 3m +1.7%
52-week range: 9.02 - 12.47 (now 60.9% of the way up)
Volatility: ATR(14) 0.20 (1.8% of price) | annualised 20d 27.0%
Volume: 0.05x the 20-day average
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
Cost of holding this fund instead of sugar itself: -8.1% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +1.7%, commodity +9.4%, gap -7.6% | 6 months: fund +11.4%, commodity +24.7%, gap -13.2% | 12 months: fund +18.9%, commodity +27.1%, gap -8.1%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-11-03, published the following Friday)
Large speculators: net long 18.8% of open interest (1,191,088 contracts)
Change on the week: -0.9% of open interest
Crowding: 90% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -0.3% (-186.21K) over 7d | 1 month: +19.4% (9.54M) over 30d
Shares outstanding: 5.28M | fund size: 58.67M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected) (Bing's feed, direct: 3 headline(s), none naming CANE)

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise; bearish positioning change and fund outflows; heavy roll cost; price below short‑term SMA with low volume.

**Main reasons it gave:**
- No macro surprise in rates or inflation data
- Positioning: net long fell 3.9% of open interest this week
- Fund flows: share count down 12.4% over the past month
- Cost of holding: -7.0% annual roll cost
- Technical: price below 20‑day SMA, volume 0.11× 20‑day average

<details><summary><b>News</b> — score +0.00</summary>

- [Corn Futures Jump After USDA Forecast Cuts](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af726a84cfb4a3c8b590824143f34dd&url=https%3a%2f%2fijr.com%2fdiscover%2ffinance-2026-11-09-grains-mostly-lower-livestock-mixed-d884a3fb&c=13146946502681003164&mkt=en-us)  
  <sub>Independent Journal Review, 32h ago</sub>  
  Grain futures were mostly lower in early Tuesday trading, while livestock prices were mixed or little changed. Monday’s grain losses came amid pressure ahead of the November USDA outlook and concerns ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 17.33 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 17.46 (-0.7%), 50d 18.61 (-6.9%), 200d 18.18 (-4.7%); 50d above 200d
Momentum: RSI(14) 38.9 | MACD -0.364 vs signal -0.415 (histogram 0.051)
Returns: 1d +1.4% | 5d +0.8% | 1m -5.6% | 3m -6.1%
52-week range: 16.47 - 20.29 (now 22.5% of the way up)
Volatility: ATR(14) 0.24 (1.4% of price) | annualised 20d 13.9%
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
Cost of holding this fund instead of corn itself: -7.0% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -6.1%, commodity -3.5%, gap -2.6% | 6 months: fund -4.5%, commodity -1.5%, gap -2.9% | 12 months: fund -3.9%, commodity +3.1%, gap -7.0%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.20</summary>

```text
Corn rated good or excellent: 56% of the US crop (week 43 of 2026)
Direction over 3 weeks: steady, 0 points
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
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-11-03, published the following Friday)
Large speculators: net long 0.5% of open interest (1,918,622 contracts)
Change on the week: -3.9% of open interest
Crowding: 45% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -0.3% (-353.81K) over 7d | 1 month: -12.4% (-15.16M) over 30d
Shares outstanding: 6.19M | fund size: 107.19M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance due to mixed signals: bearish copper price trend and technicals, net outflows and cost drag, but ambiguous positioning crowding.

**Main reasons it gave:**
- Copper price fell to a five‑week losing streak, worst in nearly two years
- Technical indicators: price below 20‑day, 50‑day and 200‑day SMAs; RSI 36.3; MACD negative
- Fund flows: net outflows over the past month, share count down 1.3%
- Cost of holding: -2.9% annual drag versus copper
- Positioning: net long decreased 1.4% and short crowding at 2% percentile (ambiguous)

<details><summary><b>News</b> — score -0.20</summary>

- [Copper slides to fifth straight weekly loss, worst stretch in nearly two years (CPER:NYSEARCA)](https://seekingalpha.com/news/4672308-copper-slides-to-fifth-straight-weekly-loss-worst-stretch-in-nearly-two-years)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  LME copper futures fell below $13.5K/ton, headed for a fifth straight weekly loss - the metal's longest stretch of declines in nearly two years - on track...
- [Thursday’s Charts – Small Caps Slide as 2-Year Has Biggest Two-Day Jump Since March 2023](https://pro.thestreet.com/market-commentary/thursdays-charts-small-caps-slide-as-2-year-has-biggest-two-day-jump-since-march-2023)  
  <sub>RealMoney Pro, 16 hours ago</sub>  
  The 2-year yield had its biggest two-day jump since March 2023 and the dollar hit another 19-month high, while gold fell to its lowest in more than a year...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 37.08 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 38.73 (-4.2%), 50d 39.43 (-5.9%), 200d 37.98 (-2.3%); 50d above 200d
Momentum: RSI(14) 36.3 | MACD -0.622 vs signal -0.441 (histogram -0.181)
Returns: 1d -0.4% | 5d -1.6% | 1m -6.0% | 3m -7.6%
52-week range: 30.77 - 41.43 (now 59.2% of the way up)
Volatility: ATR(14) 0.66 (1.8% of price) | annualised 20d 24.1%
Volume: 0.07x the 20-day average
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
Cost of holding this fund instead of copper itself: -2.9% a year -- a steady drag
Measured: 3 months: fund -7.6%, commodity -7.0%, gap -0.6% | 6 months: fund -2.8%, commodity -1.8%, gap -1.0% | 12 months: fund +17.7%, commodity +20.7%, gap -2.9%
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
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-11-03, published the following Friday)
Large speculators: net long 10.6% of open interest (327,850 contracts)
Change on the week: -1.4% of open interest
Crowding: 2% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +2.1% (13.56M) over 7d | 1 month: -1.3% (-8.83M) over 30d
Shares outstanding: 17.51M | fund size: 649.20M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Treasury yields rose modestly (3‑month +0.12%, 5‑year +0.34%, 10‑year +0.31%) and the dollar index increased +0.95 points, with no macro surprise
- Inflation 3.7%, unemployment 4.1%, and jobless claims 200k were in line with expectations, indicating no data surprise
- Technical indicators show GLD below 20‑day, 50‑day and 200‑day SMAs, RSI 39.1 and MACD -5.137, but no decisive break on volume
- CFTC positioning shows large speculators net long 26% of open interest, down 0.6% week‑over‑week, indicating a slight bearish shift
- Cost of holding is near zero (-0.1% annual), implying no structural drag

<details><summary><b>News</b> — score +0.00</summary>

- [VanEck Gold Miners ETF (GDX) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GDX/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Find the latest VanEck Gold Miners ETF (GDX) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [GLD 261112 347.00C (GLD261112C347000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/GLD261112C347000-US)  
  <sub>Moomoo, 8 hours ago</sub>  
  $SPDR Gold ETF (GLD.US)$ : The biggest single trade: $75.9M on 11,106 put contracts expiring Jan 15 vs 4,728 open interest. $GLD options: $858.5M in premium...
- [Gold sinks to more than one-year low as Fed rate hike bets boost dollar, Treasury yields](https://www.google.com/goto?url=CAES-wEBxCJF11Ej4iETFPK82Z7zt6SsA8htX9urgTEO0lPjKbGCkLB-oALuHIOXWPaAB9Rh1_Y0P0eqN5C0KjLHwsuSqeeLGKhPvWUSVubtcj7IuI9pdtpNM904jBrPIP5aBCbghpWlgqQcd9YMSicmFTobVr08wCcoHAQZ6ZaFhZh60pbD3OvvjKGx5MABP3Ril-DQ-4Kf_LG0a7FWzmiVK3_hirLR4BKMdFPj4LvnlJsEXNczhdK7zWvybmRZ6msJ7UYOhxGEBAYbgOqNud63lmCeDpo7H1VhpgN5UZNxjqKkakiXmpyuLPjnA-z1ae_d10IgfSNukoH85T6G8Q&gsessionid=k3-L-Y7yCLNwCoYcgWGBLxVs-wqffofIAQeJeCdgAnUuzXtekoMieA)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  Gold fell nearly 3% to their lowest in more than a year as Treasury yields, the dollar, and oil prices all gained after President Trump said the US does not...
- [What Is Driving Gold Toward USD 3,970 and Weighing on SPDR Gold Shares (NYSEARCA:GLD) as the Dollar Climbs?](https://www.google.com/goto?url=CAES0QEBxCJF14kk-ShkH8gpsaCNhly3nF0HoFZFr_-ciDTc7PkbsNgey-Z1mLB9BDCj_RZkuxL2ngPEuA8wYtt21BbBQAvk3I_zngK5IkZPFXxlYC2OQHr9jtnXu-py-YDd9tWYtchl7iOuwzoD1fKV2XNiVQnBiUVNSMuLvOJyHfNSMKP1Gs_wnbOSKzNe412N6CWo0QsrwgfP3GHU--qfi9siHIg-9XyyjY4JXzpbQ9VmGyLy7szpSRbDgE5bNAwvLF5ZWjpZzmA4Isl0Zn3ocxl0Ow&gsessionid=k3-L-Y7yCLNwCoYcgWGBLxVs-wqffofIAQeJeCdgAnUuzXtekoMieA)  
  <sub>kalkine.ca, 22 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [SPDR Gold ETF (GLD) Stock Price | Quotes & News](https://www.google.com/goto?url=CAES8QEBxCJF118THlFbXLIVsjXkDGDwHEmbkPdkPUCZW7FrK251_X9t29kI5zqSv-lrrZuUstbE-CTQyZxoanm8PFJvQ3rQSWSI3BdjxLYh7sYmz-cqN_z3l24o8_28V4FvuoejPxd4C6jFBq6u9snxNRlMuXB_8QPFiTQ8cBwNQWRVRgn_pKHdkD6yRjAqjQaF8mzhl05FxD22DtcfvEoHU-c7ihPjc3W-oW_jhcBheiua5iwFss3MYiUq31VLxaiDa7gDhFEcTQif0GYBGWk-aU7Tq7U5HAiSZjRoMgwKRNhQnTFkMsLy17Qrujl99zEeY4AK&gsessionid=k3-L-Y7yCLNwCoYcgWGBLxVs-wqffofIAQeJeCdgAnUuzXtekoMieA)  
  <sub>Moomoo, 19 hours ago</sub>  
  Track the latest SPDR Gold ETF (GLD) price, quotes, financial information, news, and analyst ratings on moomoo App for your ETF trading and investing needs.
- [Which of the Top 3 Gold and Silver Plays Is Best Positioned Following the Inflation Selloff: SPDR Gold Shares (NYSEARCA:GLD), Hecla Mining (NYSE:HL) or Barrick (NYSE:B)?](https://www.google.com/goto?url=CAES-QEBxCJF1zMZwBS4o6ymRy-sCfjpNyPgwflUBkST7ADYmG_23r1hj0cF4DsmAFioKR64TjXPmcxN6PZ0eHPnFmHXMgm6Sx7ogRtx_Ahlc0KfozomVqLOg6kG6aQfMDQ5I0MlzP3YNxvnFuCTlo39KKSR-g6JaTor1jwjgylAJ7m0gfENckSAhed0nSA_38s7vymyvU2axWacbBjCKPxgCUOm1uVlm7MXlYRPl2pAdrvKbUKq9Q3_st4c0TqoMJrCDeccEhsOyY9lYg40I_xWwPYTR1vZEXH0HD5tXsJgM2Z4L-y3Dqj_QOnpi19pLCB0Oorr7Lz8jniNVS8&gsessionid=k3-L-Y7yCLNwCoYcgWGBLxVs-wqffofIAQeJeCdgAnUuzXtekoMieA)  
  <sub>kalkine.ca, 21 hours ago</sub>  
  Which of the Top 3 Gold and Silver Plays Is Best Positioned Following the Inflation Selloff: SPDR Gold Shares (NYSEARCA:GLD), Hecla Mining (NYSE:HL) or...
- [$SPDR Gold ETF (GLD.US)$$iShares Semiconductor ETF (SOXX.US)$$SK hynix (SKHY.US)$$CoreWeave (CRWV.US)$$NVIDIA (NVDA.US)$](https://www.google.com/goto?url=CAESqAEBxCJF16DRwxrZCwVqzdoA9IScIWMRiSs6jFAh5OB7D4GDjMP-UUVvHlIW6IROHhn1WNE29Hq5j8u-ESGtDF3N0LhJDIOScqugWP4UA8HB1JJ_oQmUz9XyT_Ge9qSJ-RqlWe4mNqPBDunNupF4LQWBQpU_G-K8Fh1V75Dvdz4ISDWqr8tc86QF1V2qURlPbSC6xnSs7yvOOFACqETp4439L0O4xCQKp-Q&gsessionid=k3-L-Y7yCLNwCoYcgWGBLxVs-wqffofIAQeJeCdgAnUuzXtekoMieA)  
  <sub>Moomoo, 23 hours ago</sub>  
  SPDR Gold ETF (GLD.US)$$iShares Semiconductor ETF (SOXX.US)$$SK hynix (SKHY.US)$$CoreWeave (CRWV.US)$$NVIDIA (NVDA.US)$
- [Silver ETF vs. Silver Miners ETF: Which Has Held Up Better This Year?](https://www.google.com/goto?url=CAESmAEBxCJF11cse8IdHjwEpgecbJWD1BhJCo69c6I-BlLU-2uYBk2I0nS4t7RulYJiT4oL-pu_4dBAmsn510PscO7h8GuilK7fcg2_pn2AmrwpqHvGeG_Z_1W5W4EE1zEZn1kRtkVxzEeJSLpS6rSFlLXCyafKUmelRoG01qjmlyusQA6LAe-gcbGfO-Hib-55-GGBHVXY32BnsA&gsessionid=k3-L-Y7yCLNwCoYcgWGBLxVs-wqffofIAQeJeCdgAnUuzXtekoMieA)  
  <sub>The Motley Fool, 20 hours ago</sub>  
  The Global X Silver Miners ETF is thumping the iShares Silver Trust, and that condition could persist even if the commodity's price rebounds.
- [GLD 261112 357.00C (GLD261112C357000) Stock Options Chain | Quotes & News](https://www.google.com/goto?url=CAESbgHEIkXX9LXWxsTiUDMlWof5Lb5NFx-8paiHAsvS78DG-Hh6HRRteMuAtLpHBT1Q2QNQRALtXjuLmNb_PNNFyy4Evbw7CUWrciSMW8PX8qWAgBDpnPWhwyMAROQ_inB60-_kxfAdCTV5i6RGsLpK&gsessionid=k3-L-Y7yCLNwCoYcgWGBLxVs-wqffofIAQeJeCdgAnUuzXtekoMieA)  
  <sub>Moomoo, 18 hours ago</sub>  
  $SPDR Gold ETF (GLD.US)$ : Biggest unusual trade: 25,082 put contracts expiring Mar 19, $10.7M in premium vs 15,644 open interest. $GLD drew $158.7M in...
- [What If You Had Invested $10,000 in Bitcoin 5 Years Ago?](https://www.google.com/goto?url=CAESrAEBxCJF1yo4GuZXVI-Oa4NZkCtHA82g0LQImMjHOc4pZKM-sl-xg0GV-eMQNUBb4QKYEL7um7NVlIeuK7zwnnhbhMDHEYdij77Mv2nllwq_x9NAhLj_Xag8exgBjbChqAVIlgB3KPLwvozK-IeURnNoEMFjTea3gekZIwzDNFb6YT66STHuNAXr4TP67BZPI7JiP3lXxR4VxVX1k2384YrzRXqKj5A7F0WPLp_a&gsessionid=k3-L-Y7yCLNwCoYcgWGBLxVs-wqffofIAQeJeCdgAnUuzXtekoMieA)  
  <sub>24/7 Wall St., 16 hours ago</sub>  
  in Bitcoin invested five years ago is now worth about $11069. See how Bitcoin performed against gold and the S&P 500.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 356.88 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 368.86 (-3.2%), 50d 380.93 (-6.3%), 200d 408.42 (-12.6%); 50d below 200d
Momentum: RSI(14) 39.1 | MACD -5.137 vs signal -4.672 (histogram -0.465)
Returns: 1d +0.6% | 5d -4.2% | 1m -6.7% | 3m -12.0%
52-week range: 354.89 - 495.90 (now 1.4% of the way up)
Volatility: ATR(14) 6.90 (1.9% of price) | annualised 20d 28.1%
Volume: 0.14x the 20-day average
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
Cost of holding this fund instead of gold itself: -0.1% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund -12.0%, commodity -12.8%, gap +0.8% | 6 months: fund -14.5%, commodity -14.5%, gap +0.0% | 12 months: fund -7.5%, commodity -7.4%, gap -0.1%
A commodity fund holds futures, not gold, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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
Contract: GOLD - COMMODITY EXCHANGE INC. (positions as of 2026-11-03, published the following Friday)
Large speculators: net long 26.0% of open interest (399,169 contracts)
Change on the week: -0.6% of open interest
Crowding: 43% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 260.30M | fund size: 92.90B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technical downtrend without decisive break, modest bullish positioning offset by outflows, cost of holding neutral.

**Main reasons it gave:**
- US Treasury yields rose across the curve (3‑month +0.12%, 10‑year +0.31%) – bearish macro backdrop
- SLV price 44.97 is 27% below its 200‑day SMA (61.92) – downtrend
- Large speculators net long 3.5% of OI, weekly increase +0.6% – modest bullish positioning
- Fund outflows: share count down 1.4% in 1 week and 4% in 1 month – bearish flow pressure
- Cost of holding -0.4% per year, essentially neutral – no significant drag

<details><summary><b>News</b> — score +0.00</summary>

- [Silver ETF vs. Silver Miners ETF: Which Has Held Up Better This Year?](https://www.fool.com/investing/2026/11/12/silver-etf-vs-silver-miners-etf-which-has-held-up/)  
  <sub>The Motley Fool, 20 hours ago</sub>  
  The Global X Silver Miners ETF is thumping the iShares Silver Trust, and that condition could persist even if the commodity's price rebounds.
- [Demand for Silver Expected to Fall 5% This Year Amid Declining Jewelry Purchases](https://www.google.com/goto?url=CAESeQHEIkXXGXVRue41om902rUTdXNu28zBUaCpAFd0C7cp5taGrpTAP3QtzNDGUh7eTFb_oA5nNzWJ-Ha4lsBvvQ17nFFW-syCYmBdMIRrWvKiKajgbFDgoW1nMEnDvdeGhMga8ZZ5zcR77HB4uE0sjgAd5ByJT8UC074&gsessionid=sBU9gY1hDzmMh5WrQ379djSYXx04VDOkrMyBB5DUikhrCnYsZp_Bng)  
  <sub>صحيفة مال, 1 hour ago</sub>  
  A study published on Friday indicates that demand for silver is expected to decline by 5% in 2026, driven by a drop in jewelry demand and reduced…
- [Quant Silver ETF FOF - Direct (G)](https://www.google.com/goto?url=CAESigEBxCJF1wtd3T7BbPc6qJ3W3Fo1ZV5eG94sWaoleoOx54ph5Yu3C-AjeTOCJGJwkLYFbApAYQVv2AW3VQt-fQzVqgdXC99vZvrhIJBE94zjlk0hLkScftrk5diMcIIR3FFRM1CVdv7zvUtPaJOuH9T3oeeIvjoS9FAbpR3Bzl79KBpm6K29pk694QM&gsessionid=sBU9gY1hDzmMh5WrQ379djSYXx04VDOkrMyBB5DUikhrCnYsZp_Bng)  
  <sub>Multibagg AI, 4 hours ago</sub>  
  Quant Silver ETF FOF - Direct (G) latest NAV, returns, AUM, expense ratio, holdings, asset allocation, peer comparison and risk metrics. NAV ₹10.01.
- [Sprott Physical Gold and Silver Trust (CEF.TO) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZwHEIkXXPTF2vxscjOfVh4HZIkwxmWh19hF0da9_WKLWV7eyw2RgkiP7CNUHAWEGFG3JoktE6a9UbUC5SrT9cR3vGsaF84x_BRWUpVzRj8rC_xVQg5fohEdHZinQNmfm_hNdBm_QMbc&gsessionid=sBU9gY1hDzmMh5WrQ379djSYXx04VDOkrMyBB5DUikhrCnYsZp_Bng)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Find the latest Sprott Physical Gold and Silver Trust (CEF.TO) stock quote, history, news and other vital information to help you with your stock trading...
- [‘We believe gold and silver are not simply defensive assets’ – BlackRock’s Akullian](https://www.google.com/goto?url=CAESsAEBxCJF1-MlsX6DeOAHulWdS6bJ64FgnqsPCX3sp1MyRdNlSVXf0J8Ld1OV88Kapbv3B2qVqzsA5SIP9OCmGEP3G_q_fCmNMojgQLBXp2tfMqSUYSlAU6F91FZH5d53QlpSMFAP1maOmjxEIO25jlvMK5DB31jyFyGfi30D79bB8u3G1tbUG4vkRgC9-gRn4FxXFsDSoEjU5mxoVxltWVHAg7i8neJCWZJ6udGwbsFHBw&gsessionid=sBU9gY1hDzmMh5WrQ379djSYXx04VDOkrMyBB5DUikhrCnYsZp_Bng)  
  <sub>Kitco, 19 hours ago</sub>  
  (Kitco News) – Even though gold and silver prices continue to show near-term weakness, both precious metals still enjoy strong support from key areas of...
- [Gold and Silver Price Forecast: Gold Hits 13-Month Low Before US PPI](https://www.google.com/goto?url=CAESswEBxCJF12QlKwlqKmi8dku8T2H2jRx2v1NIlfISXI_-FQo6yk6tykIJUgr5uhk-fSfbVKm6a3PoJU8lUlCDLydCVKhxdvOGrrwsDIZD3x9oeQ_7IYqOxMJogvCpK423BteAlK9QpQZE5R0fcdBb27wxs2H_Pr3NXNfLbwcIkhcptWg-FXyueFXffGvTPWmC3S8RF28z8Ggu0CmLZap1ABclRk6Cmuv_2NPzZ3hrIIgOtE3VmA&gsessionid=sBU9gY1hDzmMh5WrQ379djSYXx04VDOkrMyBB5DUikhrCnYsZp_Bng)  
  <sub>FXEmpire, 7 hours ago</sub>  
  A hotter-than-expected US producer price report on Friday could lift Treasury yields, push gold towards $3780 and put silver's $50 support at risk.
- [What $10,000 in Silver on Jan. 1 Is Worth Today](https://www.google.com/goto?url=CAESlAEBxCJF1-yxCM7leFNWjaVUTY3Dgwp_B5MvVZuaIPEF2Mct0kaZo1VO5Sl1zSQlWAn-9X-_0WCRz96d8V9Hvdy_k8yjR63UlypyPRpW_OjC7Qk7wm-HnAOjgN5_Hx5VnbULmwwzIIHcG6oVV4evR8tqpqDizn8aQ_3ZLRHeTbUjt5f3g-yYhqYCUuPWcXCi_wVlFZLX&gsessionid=sBU9gY1hDzmMh5WrQ379djSYXx04VDOkrMyBB5DUikhrCnYsZp_Bng)  
  <sub>The Motley Fool, 23 hours ago</sub>  
  It has been a tough year for most popular precious metals. The SPDR Gold Trust (GLD -2.81%), for example, is down roughly 8% year to date. Silver's year has...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 44.97 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 47.77 (-5.9%), 50d 52.89 (-15.0%), 200d 61.92 (-27.4%); 50d below 200d
Momentum: RSI(14) 34.4 | MACD -2.054 vs signal -2.147 (histogram 0.094)
Returns: 1d -0.3% | 5d -4.0% | 1m -13.4% | 3m -24.5%
52-week range: 44.60 - 105.60 (now 0.6% of the way up)
Volatility: ATR(14) 1.47 (3.3% of price) | annualised 20d 42.6%
Volume: 0.21x the 20-day average
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
Cost of holding this fund instead of silver itself: -0.4% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund -24.5%, commodity -24.6%, gap +0.1% | 6 months: fund -34.9%, commodity -35.4%, gap +0.5% | 12 months: fund -6.9%, commodity -6.5%, gap -0.4%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-11-03, published the following Friday)
Large speculators: net long 3.5% of open interest (115,583 contracts)
Change on the week: +0.6% of open interest
Crowding: 8% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -1.4% (-336.56M) over 7d | 1 month: -4.0% (-983.78M) over 31d
Shares outstanding: 529.30M | fund size: 23.81B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals mixed but no decisive break, positioning change modest, fund outflows moderate, cost of holding near zero, crop condition neutral.

**Main reasons it gave:**
- Large speculators net long 14.9% of open interest, down 4.9% week-over-week
- Fund outflows: -8.3% share count over past month
- Cost of holding near zero (-0.7% annual), indicating minimal roll cost
- No macro surprise: yields up modestly, no policy shift
- Technicals: price below 20‑day SMA, RSI 38.8, MACD histogram +0.020

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 25.72 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 26.04 (-1.2%), 50d 26.98 (-4.7%), 200d 25.28 (+1.7%); 50d above 200d
Momentum: RSI(14) 38.8 | MACD -0.371 vs signal -0.391 (histogram 0.020)
Returns: 1d +0.0% | 5d +1.6% | 1m -4.5% | 3m -0.3%
52-week range: 21.71 - 28.14 (now 62.4% of the way up)
Volatility: ATR(14) 0.29 (1.1% of price) | annualised 20d 13.8%
Volume: 0.02x the 20-day average
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
Cost of holding this fund instead of soybeans itself: -0.7% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund -0.3%, commodity +3.0%, gap -3.3% | 6 months: fund +4.1%, commodity +5.1%, gap -0.9% | 12 months: fund +9.7%, commodity +10.4%, gap -0.7%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

```text
Soybeans rated good or excellent: 57% of the US crop (week 41 of 2026)
Direction over 1 weeks: not enough readings to say
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
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-11-03, published the following Friday)
Large speculators: net long 14.9% of open interest (959,576 contracts)
Change on the week: -4.9% of open interest
Crowding: 43% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -1.5% (-608.31K) over 7d | 1 month: -8.3% (-3.50M) over 30d
Shares outstanding: 1.51M | fund size: 38.88M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No clear macro surprise, technicals lack decisive break, and fundamentals are mixed; overall call remains neutral.

**Main reasons it gave:**
- Natural gas inventories at 3,801 Bcf (+77 Bcf week, 92% percentile) – bearish
- Cost of holding -2.1% per year – drag on long positions
- Large speculators net short 13.4% of OI, down 1.2% week – slight bullish shift
- Fund share count +20.3% over month – net inflows

<details><summary><b>News</b> — score +0.00</summary>

- [Condor Announces 2026 Third Quarter Results and Record Production of 18,631 boe/d](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af7266791024880ad8702ddf2a17553&url=https%3a%2f%2fmarkets.businessinsider.com%2fnews%2fstocks%2fcondor-announces-2026-third-quarter-results-and-record-production-of-18-631-boe-d-1036758661&c=10629221850018692689&mkt=en-us)  
  <sub>Markets Insider, 22h ago</sub>  
  Production in Uzbekistan for the third quarter of 2026 averaged 16,693 boe/d comprised of 16,240 boe/d (97.4 MMscf/d) of natural gas and 453 bopd of condensate which is a total production increase of ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 10.23 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 9.74 (+5.0%), 50d 10.29 (-0.6%), 200d 11.02 (-7.1%); 50d below 200d
Momentum: RSI(14) 54.0 | MACD -0.055 vs signal -0.198 (histogram 0.143)
Returns: 1d -2.2% | 5d +9.4% | 1m -7.7% | 3m +4.1%
52-week range: 9.00 - 16.90 (now 15.6% of the way up)
Volatility: ATR(14) 0.38 (3.7% of price) | annualised 20d 44.1%
Volume: 0.07x the 20-day average
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
Cost of holding this fund instead of natural gas itself: -2.1% a year -- a steady drag
Measured: 3 months: fund +4.1%, commodity +21.2%, gap -17.1% | 6 months: fund -9.7%, commodity +10.1%, gap -19.8% | 12 months: fund -30.2%, commodity -28.1%, gap -2.1%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.50</summary>

```text
US inventories, week ending 2026-10-30 (published the following Wednesday)
  Natural gas: 3,801.0 billion cubic feet, +77.0 on the week (a build), 92% percentile over 52 weeks -- high for the time of year
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 13.4% of open interest (1,678,554 contracts)
Change on the week: -1.2% of open interest
Crowding: 2% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -8.0% (-44.32M) over 7d | 1 month: +20.3% (85.85M) over 31d
Shares outstanding: 49.76M | fund size: 509.07M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fund flows: +20.6% share count increase over past month
- Positioning: net long down 0.5% of open interest, crowding at 25th percentile
- Energy inventories: petrol build +1.8M barrels, diesel build +4.1M barrels
- EIA price outlook: WTI forecast $84 in 6 months, down from current $97

<details><summary><b>News</b> — score +0.00</summary>

- [Oil gains as Trump dampens hopes for U.S.-Iran deal; market ignores bearish U.S. inventory data](https://seekingalpha.com/news/4671993-oil-gains-as-trump-dampens-hopes-for-us-iran-deal-market-ignores-bearish-us-inventory-data)  
  <sub>Seeking Alpha, 14 hours ago</sub>  
  Crude oil closed higher after President Trump said the US does not a peace deal with Iran, blunting the market's recent enthusiasm about the chances for a...
- [Gavin Newsom Calls Trump ‘Wholly Owned Subsidiary of Big Oil’ - Chevron (NYSE:CVX)](https://www.benzinga.com/news/politics/26/11/63230067/gavin-newsom-blasts-trump-big-oil-iran-war)  
  <sub>Benzinga, 8 hours ago</sub>  
  Newsom attacks Trump's Big Oil ties and fossil-fuel policies; GasBuddy analyst warns Iran tensions may lift oil markets as gas prices fall.
- [Jeep Brand, FOX Factory Vehicles and USO Partner to Auction Customized Jeep Wrangler Commando 392](https://www.google.com/goto?url=CAESuwEBxCJF10X-Y-fQ46V7CkmvSkroEnRcXPawVyW2wvrzJvJa21xZhA4q-N0naHuqcjW5rDSkBZNPyguKYvcraU1oWo_Mzsa6UpGAgg-PgU_t66ekm_gzBWDhTNKqdn7bkgYqkx2FRmqn-NDz7rDbHUcVjHFHkRjdPY3j22cKAEhro5nqBPsSeaj6tHlU4B8b4poTrpEOMBoyBcg1lk019NPSur_PXioMfGAvh4b2sR63jy6f5YoZXzWrnXSh&gsessionid=jBv349znRzsmfHiYVB_ki1fZTwA-E3HhpejSJn_mhFmKeDNx1LOiSg)  
  <sub>Finviz, 23 hours ago</sub>  
  AUBURN HILLS, Mich., Nov. 12, 2026 /PRNewswire/ --. The one-of-a-kind Jeep® Wrangler Commando 392, created in. Custom Jeep® Wrangler Commando 392 to be...
- [The Treasury Secretary Is Now Living on a Military Base After Iranian Threats](https://www.google.com/goto?url=CAEStQEBxCJF10TEp2XVFSp_hHVszs6ivwddQIA3gAnzBqzoAR7by3Vj-DBVsw5UmaC4qO_shSWISD6C9-GdA7KyZNqzUAx61mZh5xmAr3JUERCrFEnWf--fK4xH7u51KsyLF0vm8h7gNbjk0vZfBXcgzDzJvBWt4o3CArDZmgOJV5gzM8YBgFS7Q6uXbkdRQT2Lt-ZvY4ZOVyKFzO-yFnS7-M5aCRa3GIunZSHEVIskN4DjSxUG0mq5&gsessionid=jBv349znRzsmfHiYVB_ki1fZTwA-E3HhpejSJn_mhFmKeDNx1LOiSg)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  Treasury Secretary Scott Bessent has moved out of his Washington-area home and onto a U.S. military base because of Iranian threats against his life.
- [[Robinhood onchain] USO token supply shrinks by $0.30 million as USAR trading doubles](https://www.google.com/goto?url=CAESagHEIkXX7wJqZL_0tlDTZqlr08jOUSMOgwxFThuLP4AvZ-gqMWKtta3YwhygfG3xn_kitoNzLQmFYXkxb1h9_BCuiRurtJ3mKexMxWJV9dcBS1TijDDnBbIbShWPtTSNprfBAA-yF0xmKiQ&gsessionid=jBv349znRzsmfHiYVB_ki1fZTwA-E3HhpejSJn_mhFmKeDNx1LOiSg)  
  <sub>www.tokenpost.com, 2 hours ago</sub>  
  USO token supply fell by about $0.30 million in value, while USAR trading volume rose 108.3%. Nvidia added 386 holder wallets.
- [Oil price today: Brent holds near $96 as IEA sees first surplus since Iran war](https://www.google.com/goto?url=CAESrAEBxCJF19ylXFClSOx3SeIKTKxa-O4rOqsbwlgYfiqgeO-iGUMoovN89B3mDWV6V7HTSmc3QDtlLCYmveyaXjBuoD7QZspu0TPMX1YSLAXPEf1PAdbyRg4rUSOK3_4DdHd2V3RnkAHeHgu1-MpzG2BASE5Djz1MJgzIgyedJYIlI3yUKbTsb60eTt8tAtBgq2-cuY8YSMiPxPjsdECUF3EF0_0pjAsx5euu81Pa&gsessionid=jBv349znRzsmfHiYVB_ki1fZTwA-E3HhpejSJn_mhFmKeDNx1LOiSg)  
  <sub>Invezz, 5 hours ago</sub>  
  Oil prices fell slightly, with Brent crude just below $96 a barrel on Friday, November 13, close to Thursday's settlement.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 146.55 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 156.11 (-6.1%), 50d 152.83 (-4.1%), 200d 127.66 (+14.8%); 50d above 200d
Momentum: RSI(14) 43.5 | MACD -2.533 vs signal -0.398 (histogram -2.135)
Returns: 1d +0.3% | 5d -1.2% | 1m -6.8% | 3m +12.5%
52-week range: 66.17 - 169.53 (now 77.8% of the way up)
Volatility: ATR(14) 5.22 (3.6% of price) | annualised 20d 48.0%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.55</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.55</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.55</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.55</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.55</summary>

```text
US inventories, week ending 2026-11-06 (published the following Wednesday)
  Petrol: 210.8 million barrels, +1.8 on the week (a build), 35% percentile over 52 weeks
  Diesel: 103.3 million barrels, +4.1 on the week (a build), 21% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.55</summary>

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
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-11-03, published the following Friday)
Large speculators: net long 1.1% of open interest (1,908,732 contracts)
Change on the week: -0.5% of open interest
Crowding: 25% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +1.8% (35.53M) over 7d | 1 month: +20.6% (343.49M) over 31d
Shares outstanding: 13.71M | fund size: 2.01B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- CFTC: large speculators net short 16.3% of OI, down 2.1% week‑over‑week.
- Fund flows: shares down 8.9% over past month, indicating outflows.
- Cost of holding: -8.2% annual, heavy roll cost.
- Macro: Treasury yields up across curve, no Fed policy surprise.
- Technicals: price below 20‑day, 50‑day, 200‑day SMA; RSI 37.9; volume 0.09× 20‑day avg.

<details><summary><b>News</b> — score +0.00</summary>

- [Wheat Taking Back Some of Thursday’s Losses on Friday Morning](https://www.barchart.com/story/news/8820860/wheat-taking-back-some-of-thursdays-losses-on-friday-morning)  
  <sub>Barchart.com, 2 hours ago</sub>  
  Wheat is showing 5 to 7 cent higher trade on Friday morning. The wheat complex fell across the three markets into the Thursday close, falling double digits.
- [Wheat Falls to New Lows on Thursday](https://www.barchart.com/story/news/8811534/wheat-falls-to-new-lows-on-thursday)  
  <sub>Barchart.com, 16 hours ago</sub>  
  The wheat complex fell across the three markets into the Thursday close, falling double digits. Chicago SRW futures were down 10 ¾ to 15 ½ cents at the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.12% (+0.12 on the week) | 5-year 4.99% (+0.34 on the week) | 10-year 5.17% (+0.31 on the week) | 30-year 5.49% (+0.23 on the week)
Yield curve, 10-year minus 3-month: +1.05 points -- upward sloping (normal)
US dollar index: 103.25 (+0.95 on the week)
Volatility (VIX): 18.10 (-7.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.73% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 22.02 (bar of 2026-11-13), from 502 daily bars
Trend: vs 20d SMA 22.33 (-1.4%), 50d 24.19 (-9.0%), 200d 23.61 (-6.7%); 50d above 200d
Momentum: RSI(14) 37.9 | MACD -0.678 vs signal -0.751 (histogram 0.072)
Returns: 1d +2.1% | 5d +1.3% | 1m -9.3% | 3m -11.9%
52-week range: 19.88 - 28.00 (now 26.4% of the way up)
Volatility: ATR(14) 0.39 (1.8% of price) | annualised 20d 18.9%
Volume: 0.09x the 20-day average
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
Cost of holding this fund instead of wheat itself: -8.2% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -11.9%, commodity -11.9%, gap +0.0% | 6 months: fund -8.7%, commodity -6.5%, gap -2.1% | 12 months: fund +2.7%, commodity +10.9%, gap -8.2%
A commodity fund holds futures, not wheat, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.25</summary>

```text
Wheat rated good or excellent: 45% of the US crop (week 46 of 2026)
Direction over 1 weeks: not enough readings to say
Same week last year: 49% (-4 points)
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
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 16.3% of open interest (534,858 contracts)
Change on the week: -2.1% of open interest
Crowding: 28% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -0.8% (-1.94M) over 7d | 1 month: -8.9% (-22.83M) over 30d
Shares outstanding: 10.60M | fund size: 233.46M
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

