# Daily report

**18 Nov 2026, 18:37 Israel time (16:37 UTC)** · 80 names checked · 4 traded · 17 with a problem

**Answers with no explanation:** 11 of 49 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 4 | 12 | 0 |
| Whole-market funds | 14 | 0 | 12 | 2 |
| Sector and country funds | 41 | 0 | 35 | 6 |
| Commodities | 9 | 0 | 0 | 9 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| Brazil (EWZ) · Sector or country | **Stop raised.** At +0.72R, following the price. Stop-loss raised 33.34 → 32.88. |
| MercadoLibre (MELI) · Company | **Stop raised.** At +0.28R, following the price. Stop-loss raised 1580.76 → 1561.59. |
| Poland (EPOL) · Sector or country | **Holding.** -0.25R, holding 96 shares. Stop-loss 42.85. |
| South Korea (EWY) · Sector or country | **Holding.** +0.06R, holding 51 shares. Stop-loss 148.87. |
| Alphabet (Google) (GOOGL) · Company | **Holding.** -0.60R, holding 4 shares. Stop-loss 274.24. |
| HDFC Bank (HDB) · Company | **Holding.** +2.59R, holding 102 shares. Stop-loss 25.27. |
| US regional banks (KRE) · Sector or country | **Holding.** -0.51R, holding 97 shares. Stop-loss 70.08. |
| Nvidia (NVDA) · Company | **Holding.** +5.02R, holding 9 shares. Stop-loss 174.60. |
| Novo Nordisk (NVO) · Company | **Holding.** -0.13R, holding 124 shares. Stop-loss 39.89. |
| Procter & Gamble (PG) · Company | **Holding.** +1.48R, holding 2 shares. Stop-loss 165.90. |
| Toyota (TM) · Company | **Holding.** -0.20R, holding 1 shares. Stop-loss 205.44. |
| US house builders (XHB) · Sector or country | **Holding.** -0.56R, holding 68 shares. Stop-loss 97.50. |
| US media and communication (XLC) · Sector or country | **Holding.** +1.50R, holding 47 shares. Stop-loss 104.93. |
| US health care (XLV) · Sector or country | **Holding.** -0.68R, holding 37 shares. Stop-loss 183.37. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Exxon Mobil (XOM) · Company — BULLISH, confidence 0.75

**Result:** ACCEPTED · 30 shares · submitted buy 30 XOM @ ~162.10, stop 153.50

**In the model's own words:**

> The news includes a material production startup in Guyana and a fresh upgrade from Hold to Buy, both bullish catalysts. Insider activity shows a sizable net purchase, reinforcing a positive outlook. Fundamentals are strong with low leverage and robust cash flow, supporting the bullish view. Technicals are currently bearish (price below short‑term averages, low volume), which tempers conviction but does not outweigh the material catalyst and insider buying. Analyst consensus is already buy, adding modest support.

**Main reasons it gave:**
- Uaru offshore Guyana production startup announced (Simply Wall St, 19h ago)
- Erste Group upgraded XOM from Hold to Buy (Quantisnow, 1h ago)
- Insiders net bought ~6.9M shares in last 180 days (Insider Activity)
- Strong fundamentals: low debt/equity (12.6%) and free cash flow $28.3B (Fundamentals)

<details><summary><b>News</b> — score +0.70</summary>

- [Exxon Mobil upgraded by Erste Group](https://www.quantisnow.com/insight/exxon-mobil-upgraded-by-erste-group-6798158)  
  <sub>Quantisnow, 1 hour ago</sub>  
  Erste Group upgraded Exxon Mobil from Hold to Buy Real-time XOM news, filings and analyst ratings on Quantisnow.
- [ExxonMobil (NYSE:XOM) Upgraded at Erste Group Bank](https://www.marketbeat.com/instant-alerts/analyst-exxonmobil-nyse-xom-upgraded-at-erste-group-bank-2026-11-18/)  
  <sub>MarketBeat, 37 minutes ago</sub>  
  Erste Group Bank raised shares of ExxonMobil from a "hold" rating to a "buy" rating in a research report on Wednesday.
- [Fund Update: New $627.8M $XOM stock position opened by NEW YORK STATE COMMON RETIREMENT FUND](https://www.google.com/goto?url=CAESwQEBxCJF11wYD_tP0iNQxGjYaFFBX5gkhjuP6aKzZ5vsd5gbqIR7UQ6ayO3N3ozmsHP8r4MDzYsMp0IZgwvmFSgJOuDX65JXxVgCZR8Wa5WM3Z4LYPuypt-QzWTHWsUtaiMIvGfMgbdhyytKKCLeMyXEsnmDpfApH_np7weq4zainENMGncuENveCiOQMhzgt-eSPTb6kmpeJoC0-DKKxEMF35FYfv6JMzXmZXgJE8V0G325izoouLQ2RQmWxIEmafpK&gsessionid=9he54pCb_wMMg7LCVrYG6N8ROqGgYizCIdCtlT3zLhFbe4b0cIdmGg)  
  <sub>Quiver Quantitative, 18 hours ago</sub>  
  NEW YORK STATE COMMON RETIREMENT FUND has opened a new $627.8M position in $XOM, per a new SEC 13F filing. This disclosure reflects the funds' holdings for...
- [XOM Nov 2026 200.000 put (XOM261120P00200000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXX5QRYEfs4dyIYQIWwsEzhD8nXInVDCwdIw8Q6Tud-R6Xhi0vc3nY2WeQeUFoHXz6GMB_anhgdmNIgbbPY3J0mAvm1P9eBTEhcq7rUYUgSTL86d6Hk23eErUNEBNb51QtEgxYENV9m8xs990PQEtc&gsessionid=9he54pCb_wMMg7LCVrYG6N8ROqGgYizCIdCtlT3zLhFbe4b0cIdmGg)  
  <sub>Yahoo Finance Australia, 23 hours ago</sub>  
  Find the latest XOM Nov 2026 200.000 put (XOM261120P00200000) stock quote, history, news and other vital information to help you with your stock trading and...
- [SBM Offshore awarded Longtail FPSO contracts, its sixth for Exxon in Guyana (SBFFF:OTCMKTS)](https://www.google.com/goto?url=CAESrQEBxCJF104KLrjHkcaVWP0c4gcecFY7_YEOfa91RemiUK8lLUQNh3NM3OjpwQLa28Tn0o6HLeAbYJtYhOpEUCmM6vVcCGeh8BgkeM0RBTmPrgsH5PdNP_wUK6ibHVTsuYf-4VwTz8Mp_CoZ4GXzZjuA8pVxP5iNtgnLMAT4nOM7iU5_ue_kVwiMBCA3yoK7PfX0oiLEy1clqPsbiYH4NjNYzLKe1n6PmX8LAU8YFw&gsessionid=9he54pCb_wMMg7LCVrYG6N8ROqGgYizCIdCtlT3zLhFbe4b0cIdmGg)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  SBM Offshore awarded contracts by ExxonMobil to build and install a floating production, storage and offloading vessel for the Longtail development project...
- [Energy Stocks And Industry News: Oil, Gas, Solar, Coal And Nuclear Energy](https://www.google.com/goto?url=CAESxgEBxCJF11Ipg4q7GmSGETBxYyTKoh7k1IWQTfPlVagV3fvJZqtoPdcazX0y6kmV8RbfyaQbZgYLmLrcIH3F2mTcRFNNIsTvNSjIv2mbNiSREN-uRUC-5WecLwjSng3fDhfcWwz6p17QJfdldJ7lSIm0TWMGm2pQPg4_8rz8PDeYAgMNLyokWyFjZ6YkKSxsy4sRaM4t87h4s3FmAIsch6xdZJFL6ByPxUJUmVe-E3r6-PlapwI7JSZHyNOC313xJEBOvS7ODOw&gsessionid=9he54pCb_wMMg7LCVrYG6N8ROqGgYizCIdCtlT3zLhFbe4b0cIdmGg)  
  <sub>Investor's Business Daily, 22 hours ago</sub>  
  Track the latest news, trends and analysis on oil stocks and energy industry news.
- [ExxonMobil Corporation $XOM Stock: Cibc World Market Inc. Increases Position](https://www.google.com/goto?url=CAESxAEBxCJF18lIBRRSR9kn4GCJu-cXnFtNLJGMgcMnLzfpKxkaDZYpx4GVRc5hVy4xdfBdo3bf4SxA5j95DI2aJTtwMwK--OlL34Ji1RH_npZAlKa3fTL3Spq18_hRHH-H8Pbd3xHpXApMXFEt1x0TByQMN1XtwO-I6UdIvekyyG1mbOLvySNILIZY6R06c07gc4A1BemJTvmyIy1do8cbbtJoZRf_BggCznmMc_VMcWvZoaBGnUcx_b-sfYIU71GpAMOXoEaN&gsessionid=9he54pCb_wMMg7LCVrYG6N8ROqGgYizCIdCtlT3zLhFbe4b0cIdmGg)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Cibc World Market Inc. lifted its position in shares of ExxonMobil Corporation (NYSE:XOM - Free Report) by 56.5% during the third quarter, according to its...
- [How Is New Guyana Output Strengthening the Production Story at XOM (NYSE:XOM) Ahead?](https://www.google.com/goto?url=CAEStwEBxCJF12PtplMMhicSnONfPaG0oC_fXALGu1HLUOrsty3cN-E9ONGNBCsdzF4vPhhcZO6cnlHd2CJnFknCzlvlpXz9qd1-Wk4Ru_8l61CP-oa8deVKhmE88G6waZOjzbdD14vEb02rb5HsyuBZDhQO5nyTX2aZ9IfO4QSEHXlsFxvcS7CbdLboXz7n9UUBeo4L5HpGA00jQLuLxSD6fZeJsiyLF2_XJjSBEkriBdnE4Wd4y15Ao34&gsessionid=9he54pCb_wMMg7LCVrYG6N8ROqGgYizCIdCtlT3zLhFbe4b0cIdmGg)  
  <sub>Kalkine Media, 1 hour ago</sub>  
  Exxon Mobil (NYSE:XOM) starts first oil at Uaru offshore Guyana as refining profits lead earnings and crude stays volatile on Middle East tensions.
- [ExxonMobil Holdings (XOM) Starts Uaru Oil Production In Guyana With New Stabroek Milestone](https://www.google.com/goto?url=CAESwwEBxCJF11S-d8k2Hjc8zyi_CwhchulB7oRwI1aM6N139gn-4WSU5EpWO4esJh9UBpyEcifbeDMKdyW-R1rvmotJXv98Ya6fXAAXV8UfvkWMm7k7GqjbdBqbn77TsGAnX6kdYW-rhXUcERQYhf6fIPaNe5Twiyjxu7MAmSL8DXbjpgnJuoaztgDXaqUvJNpshDn__ZViwM3oC6nvC265k-KB9t8TFdQVfebd2-a4BZyYZ3J2pDzE1zPrbm8AOMYOXhT5ua4&gsessionid=9he54pCb_wMMg7LCVrYG6N8ROqGgYizCIdCtlT3zLhFbe4b0cIdmGg)  
  <sub>Simply Wall St, 19 hours ago</sub>  
  ExxonMobil Holdings (NYSE:XOM) has started production at the Uaru project in Guyana, expanding operations on the Stabroek block. The Uaru startup increases...
- [Xometry, Inc. (XMTR) stock price, news, quote and history](https://www.google.com/goto?url=CAESZQHEIkXXUXWQ3CgKHwaNr-J0rDIUstr5DIOD3lqyE5iXTQtmJPt79cYEzk5ZgoNzMwGJQiy1a4KGaIuYI3iNwTamZ731JLTrK99e-faLmlN0hifIIJOqD5dtvjg6Q8PqCaV5V14O&gsessionid=9he54pCb_wMMg7LCVrYG6N8ROqGgYizCIdCtlT3zLhFbe4b0cIdmGg)  
  <sub>Yahoo Finance UK, 24 hours ago</sub>  
  Xometry, Inc. operates an artificial intelligence (AI) powered online manufacturing marketplace in the United States and internationally.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 162.94 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 173.47 (-6.1%), 50d 169.63 (-3.9%), 200d 156.73 (+4.0%); 50d above 200d
Momentum: RSI(14) 38.3 | MACD -1.803 vs signal -0.482 (histogram -1.321)
Returns: 1d -2.6% | 5d -2.3% | 1m -8.4% | 3m -1.9%
52-week range: 114.51 - 187.25 (now 66.6% of the way up)
Volatility: ATR(14) 4.25 (2.6% of price) | annualised 20d 32.5%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.70</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 664.67B
Valuation: trailing P/E 16.76 | forward P/E 13.05 | P/B 2.50 | PEG 1.32
Profitability: profit margin 10.5% | operating margin 12.9% | ROE 15.5%
Growth (YoY): revenue +32.6% | earnings +111.4%
Balance sheet: debt/equity 12.6% | free cash flow 28.32B
Risk: beta 0.14 | short interest 1.2% of float
Next earnings: 2027-01-29
```

</details>

<details><summary><b>What this fund holds</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.70</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-09-30 beat by 3% | 2026-06-30 in line | 2026-03-31 beat by 14% | 2025-12-31 in line
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
Consensus: buy (mean 2.42 on a 1=strong buy to 5=strong sell scale, 22 analysts)
Ratings: 3 strong buy, 6 buy, 17 hold, 0 sell, 0 strong sell
Price target: mean 184.18 (+13.0% vs last close), range 160.00 - 213.00
Recent rating changes:
  - 2026-11-12 Bernstein: main, Outperform -> Outperform
  - 2026-11-07 Freedom Broker: main, Hold -> Hold
  - 2026-11-04 Citigroup: main, Neutral -> Neutral
  - 2026-11-04 TD Cowen: main, Buy -> Buy
  - 2026-11-02 UBS: main, Buy -> Buy
  - 2026-11-02 Morgan Stanley: main, Overweight -> Overweight
Institutional ownership: 67.0%
Largest holders: Blackrock Inc. (8.1%), Vanguard Capital Management LLC (6.6%), State Street Corporation (5.2%), FMR, LLC (3.6%), Vanguard Portfolio Management LLC (2.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.70</summary>

```text
Last 180 days: bought 10,818,651 shares in 251 transaction(s) | sold 3,904,152 shares in 49
Net: +6,914,499 shares (-265.7% of insider holdings) | insiders hold 4,323,976 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.70</summary>

_Not available today._

</details>

### Microsoft (MSFT) · Company — NEUTRAL, confidence 0.58

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “SELL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Stock fell below $500 after global outage and AI monetization concerns (NEWS)
- Price below 20‑day and 50‑day SMA, RSI 40.6, low volume indicating weak momentum (TECHNICAL)
- Insider activity shows net selling by CFO and officer, no distinct insider buying (INSIDER)
- Strong fundamentals but valuation high (trailing P/E 26, near 52‑week high) (FUNDAMENTALS)

<details><summary><b>News</b> — score -0.40</summary>

- [Microsoft Corporation (MSFT) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/MSFT/)  
  <sub>Yahoo Finance UK, 7 hours ago</sub>  
  571,651.27% · Previous close 517.99 · Open 514.01 · Bid 508.02 x 400 · Ask 511.70 x 200 · Day's range 496.51 - 515.64 · 52-week range 349.20 - 559.15 · Volume...
- [Microsoft Stock Loses Key Level Amid Global Outage; Is Microsoft A Buy Now?](https://www.investors.com/research/microsoft-outage-msft-stock-november-2026-buy-now/)  
  <sub>Investor's Business Daily, 2 hours ago</sub>  
  Microsoft (MSFT) stock fell further below a key level on Tuesday amid a broader sell-off in tech stocks. The software maker's stock has been under pressure...
- [A Memo To Microsoft’s Shrinking PC Business](https://www.google.com/goto?url=CAESpAEBxCJF11yHt3jMmfsux9FTywKHh0fNv_7gGG7gVZKSI9neOjVLDS_X6toi2IEeg4zf2EF8wPqwnRvPGkRMbau8hCwW9tncE2YJEoTuGmU1tb69Imekl2qxTXHudgHqNbdkfI1i7O_YmxqcSKrxWo0_p8Gxg75oASNwt2mgD1oYfZ_25Pux3BopVywxzOWC2optlciPWMGLpl0SGHguQY-2SMQhTg&gsessionid=ZSojOatnqpGTybLpkvBEi8lHsaYsWeoCjigDKad14fQ7Bfrkz1J0lQ)  
  <sub>Trefis, 4 hours ago</sub>  
  For questions about this article or underlying research, email help@trefis.com.Most of the business at Microsoft (MSFT) is growing fast.
- [Microsoft in talks with ByteDance for additional $500M in cloud usage: report (MSFT:NASDAQ)](https://www.google.com/goto?url=CAESrgEBxCJF183FH08nluTFyJ-UZQguG6XSX6v4mCtahjuwv41JlwfChA6r4EQ3iQUp-XReYc5qPUHq-9ViRLrDvRGCe-vOWTN1uYXzjexyColkXbP2CtsUOiS8aLW5-OTO6I5Jrzd2r6qJz2dbdaiEi7gr3tKUU38i8UbN8PkgFty_bcqcCTu87J0lcrE9DtI6UiqCOT4R5xlkcZdznfkDKnVduwhf4GMxaEwpbJTh6FE&gsessionid=ZSojOatnqpGTybLpkvBEi8lHsaYsWeoCjigDKad14fQ7Bfrkz1J0lQ)  
  <sub>Seeking Alpha, 28 minutes ago</sub>  
  Microsoft (MSFT) is in discussions with ByteDance (BDNCE) that would see the Chinese tech giant spend an additional $500M for cloud services, largely to use...
- [Microsoft Corp Stock (MSFT) Moved Down by 3.35% on Nov 17: A Full Analysis](https://www.google.com/goto?url=CAESkAEBxCJF1yAuX7ypDCZnHQfECIYp4ccLx8fmA0RN7K9Iu2I5hX_kr2Nuk6BVVDaJrKN29eXGwBY0MmEALWTDFII-ebav8BAn-tqkijldQBrSiILvlxYzTz4I7-gNHvMDHM2oWd9QsM_FCnLWUFtnWgxcVAJ3y4aF8tLl6j1qUM8T-Dn1AUBmOgkjsrKpHDWRYak&gsessionid=ZSojOatnqpGTybLpkvBEi8lHsaYsWeoCjigDKad14fQ7Bfrkz1J0lQ)  
  <sub>TradingKey, 22 hours ago</sub>  
  Microsoft shares declined amid tech sector sell-offs and AI monetization scrutiny.Heavy capital expenditures raised concerns over Azure growth and margin...
- [Microsoft Stock Falls Amid Sector Weakness and Outages](https://www.google.com/goto?url=CAESsAEBxCJF10XKmX1vptJje_PbSb0KdCKaOQ8Vmgd91DFnSy_-C9sFMze6Pc7ZiPWNxOox2BI_FipHNQ3b8EdScypxxXxNTz0DB3alsmDkrRuKKbauFfD54__pxK-dxissZAJHv0NdASnMT8Z_TVOLX2qMe03BgdE2IFHnLyvKDbF9T3j38R2MdbeGea54ZhTToZVk2NXdQQt8pEfzusP38crVR0OTaw2rr2M47OYtoTiRvw&gsessionid=ZSojOatnqpGTybLpkvBEi8lHsaYsWeoCjigDKad14fQ7Bfrkz1J0lQ)  
  <sub>Benzinga, 19 hours ago</sub>  
  Microsoft Corp. (NASDAQ:MSFT) shares are sliding Tuesday amid weakness in software stocks, driven by outage concerns, fears of AI-driven disruption and...
- [Microsoft Stock Hits Seven-Week Low: Is a Bigger Drop Coming?](https://www.google.com/goto?url=CAESegHEIkXXLxlcHrfuSmQxKkQXizoxQ3Gv1WaNteJhvCplqdUFPiHgGmMMw-jvFgznL8BlhgQi08gBI6_JqfeH8xh5RnysqyZByCIXPY8QHK_st4VSOskyhqlka6xmBuMslnoU3zioI05gqUcqhQFT8ERZXM7pcZM11PBJ&gsessionid=ZSojOatnqpGTybLpkvBEi8lHsaYsWeoCjigDKad14fQ7Bfrkz1J0lQ)  
  <sub>BeInCrypto, 9 hours ago</sub>  
  Microsoft (MSFT) shares plunged to $496.51 on Tuesday, their lowest since September 24, as Wall Street's growing doubts about the AI boom reached one of its...
- [Microsoft Stock MSFT Drops Below $500 as Cybersecurity Concerns Hit Tech Stocks](https://www.google.com/goto?url=CAEStgEBxCJF1z-k1hU8enaILGaPCJmUseQmECqWEJmDVysgq2g6WcduG92oftHr1U1Q9HPtpePV-i4n7OFgw6VFAmw4b2I-ETXpvdEB88WexFjUW2w-VktJOwMEqIOb966PSKuQB6wZH2k89Wcy74RsAd_bmG7sfIX6U8S9ZpjuXfqlOJcDq31_-9L09WwXK2Xdf5kaagQIS3JZ5lPYM_LgDnEqahwMRb_-faw7ICn1bGzVzXj1fBYT_A&gsessionid=ZSojOatnqpGTybLpkvBEi8lHsaYsWeoCjigDKad14fQ7Bfrkz1J0lQ)  
  <sub>FXLeaders, 22 hours ago</sub>  
  Microsoft (MSFT) shares have fallen below $500 as technology-sector selling intensifies following recent service disruptions, reports of a U.S. National...
- [Microsoft Leads 4 Stocks That Just Announced Bigger Dividend Payments](https://www.google.com/goto?url=CAESrgEBxCJF1wI0qjGYDLvc3O32649RmZH0Hguh7MbM6v_PnHw-F6g_nXYa5N_RW6C_xwC7ix8KRFBFYoDSaw44h2vo5UBzRyRVhrqjBSpXgx2METeURSbV_9UFNFxStKHDnqSuuMhpT2E6hB7AFgxlbdXOvrgvIIE6eVgNaU83_y6ozsy7j6rY-XR-WSkuw3EThg_8lnzbshAXNPwIS1UkRyUoEXe35DSBUEDZgVleh0k&gsessionid=ZSojOatnqpGTybLpkvBEi8lHsaYsWeoCjigDKad14fQ7Bfrkz1J0lQ)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  Microsoft and Quanta raised dividends but yield under 1%, with payouts using 43% and 3% of free cash flow, leaving ample room to grow.
- [Microsoft stock rating maintained at Buy by TD Cowen on AI push](https://www.google.com/goto?url=CAESuAEBxCJF1whwhhzOnAu9aiOJ36n2woWgtlbiB_IlCKtvOOfUwar5XdAut9aizHHl2hXEGgpccIS_CapRM8FhxOUZk_Cc5tJbmJQ7vegnloD62G4bmALoBhexOb3d_HKQ5erRJJ7YFmkhkMxMAqOkRWfiA5Oc9nPwX6TlvA3ZY2sOL6o6OUhwr-ICyl20sw889xkY8YmmKXmED8ko5elXviWmaRxEJH-wMiqGCC_uBVXunO26UtblvVaq&gsessionid=ZSojOatnqpGTybLpkvBEi8lHsaYsWeoCjigDKad14fQ7Bfrkz1J0lQ)  
  <sub>Investing.com, 33 minutes ago</sub>  
  Investing.com - TD Cowen reiterated a Buy stock rating on Microsoft (NASDAQ:MSFT) and maintained its $650.00 price target. The target aligns with broader...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 502.85 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 525.82 (-4.4%), 50d 519.83 (-3.3%), 200d 442.73 (+13.6%); 50d above 200d
Momentum: RSI(14) 40.6 | MACD -2.371 vs signal 1.504 (histogram -3.874)
Returns: 1d -0.7% | 5d -3.5% | 1m -5.5% | 3m +4.5%
52-week range: 352.83 - 555.80 (now 73.9% of the way up)
Volatility: ATR(14) 14.72 (2.9% of price) | annualised 20d 37.7%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.73T
Valuation: trailing P/E 26.24 | forward P/E 20.78 | P/B 7.94 | PEG 1.50
Profitability: profit margin 41.2% | operating margin 47.1% | ROE 34.2%
Growth (YoY): revenue +18.8% | earnings +32.3%
Balance sheet: debt/equity 28.5% | free cash flow 2.99B
Risk: beta 1.04 | short interest 0.8% of float
Next earnings: 2027-01-27
```

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 in line
  2026-09-30 in line | 2026-06-30 beat by 10% | 2026-03-31 beat by 3% | 2025-12-31 beat by 3%
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
Consensus: strong_buy (mean 1.38 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 12 strong buy, 41 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 636.12 (+26.5% vs last close), range 440.00 - 870.00
Recent rating changes:
  - 2026-10-29 Bernstein: main, Outperform -> Outperform
  - 2026-10-29 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-29 Citigroup: main, Buy -> Buy
  - 2026-10-29 DA Davidson: main, Buy -> Buy
  - 2026-10-29 TD Cowen: main, Buy -> Buy
  - 2026-10-29 Scotiabank: main, Sector Outperform -> Sector Outperform
Institutional ownership: 76.8%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.3%), FMR, LLC (2.7%), Geode Capital Management, LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

```text
Last 180 days: bought 518,348 shares in 17 transaction(s) | sold 261,954 shares in 12
Net: +256,394 shares (+3.1% of insider holdings) | insiders hold 8,614,385 shares
Distinct insiders: 0 buying, 4 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-11-10 NUMOTO TAKESHI (Officer): 5,000 shares, 2.65M
  - 2026-11-09 HOOD AMY E (Chief Financial Officer): 7,305 shares, 3.98M
  - 2026-10-13 HOOD AMY E (Chief Financial Officer): 7,305 shares, 3.98M
  - 2026-09-14 HOOD AMY E (Chief Financial Officer): 41,674 shares, 20.76M
(16 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

_Not available today._

</details>

### Elbit Systems (ESLT) · Company — BULLISH, confidence 0.55

**Result:** ACCEPTED · 7 shares · submitted buy 7 ESLT @ ~699.50, stop 640.17

**In the model's own words:**

> Positive earnings beat and record backlog provide a fresh catalyst, while fundamentals remain solid with consistent earnings beats. Technicals are bearish, suggesting caution, but the material news outweighs the downside, leading to a moderate bullish call.

**Main reasons it gave:**
- Q3 earnings beat consensus ($4.36 vs $3.65) and revenue up 17.2%
- Record $33B backlog indicating strong demand
- Price below 20‑day, 50‑day, and 200‑day SMAs with negative MACD and low volume
- Four consecutive earnings beats over the past year

<details><summary><b>News</b> — score +0.90</summary>

- [What Elbit Systems (ESLT) Said on Its Q3 Earnings Call](https://finance.yahoo.com/markets/stocks/articles/elbit-systems-eslt-said-q3-161616276.html)  
  <sub>22 hours ago</sub>  
  Interested in Elbit Systems Ltd.? Here are five stocks we like better. Third-quarter revenue rose 17.2% to $2.25 billion, while diluted EPS increased on...
- [Elbit Systems shares rise on earnings beat as backlog reaches $33B (ESLT:NASDAQ)](https://seekingalpha.com/news/4673889-elbit-systems-shares-rise-on-earnings-beat-as-backlog-reaches-33b)  
  <sub>18 hours ago</sub>  
  Elbit Systems (ESLT) rose 6.2% Tuesday after the defense contractor reported third-quarter earnings and revenue above Wall Street expectations as demand for...
- [Elbit Systems (ESLT) Gets a Buy from Bank of America Securities](https://www.google.com/goto?url=CAES0AEBxCJF19FgG68xS4VwBZsOHm0esQ-zDt7c07L5OSNMIW-biac-U50tQJ976NbD6n4qh1P3EpOnBJGUWqjGpCEbQpKxf-aheAgLMqAsiL9gbOyI54O4vpmvWbgLES_1tksIXuy3gYelwm61EC6eNIpNvItwDw9b4yB8BAnqz3jhWMkXjsHH79KDWv85Dyvt4iS5G9VjMKqRU19kOvY4zBsn1dhHBmtDkPXnTFiC93l3tV0HmqnVLT0oOnbf7MShD8SK6KqJfDKiMYiZhIffAsmm&gsessionid=gdU0Ks-xRvDQZ9n0R_2-FAJQLl0dvUfH3tXpApznHincDKKql8yM1Q)  
  <sub>9 hours ago</sub>  
  Bank of America Securities analyst Ronald Epstein maintained a Buy rating on Elbit Systems today. The company's shares closed today at ILA223,860.00.
- [Elbit Systems Stock Jumps After Q3 Beat, Record $33 Billion Backlog](https://www.google.com/goto?url=CAESuwEBxCJF16aAxzw1O2GUm2nzfjaIfnnLM_YF2qPl9mQqu8cxuXhF5XT4R6MrUwKaF1cs3C6QaRu8s1quOTV2jwdMBsVPYLb22H-PAuxbdwUFFERgT561aJ_-7GG9_mBvrzTn6kzRmDNRth9q9o2uv_s8gjenFfIhNDq46s4wKO0BTD4QF2oWdNLl9gP9QwGkEUWbXyD7R1B1tj-c_p7NRtR1OpxcI4UT2J_yBCiNxW27FNpz6sFCM3glmPjV&gsessionid=gdU0Ks-xRvDQZ9n0R_2-FAJQLl0dvUfH3tXpApznHincDKKql8yM1Q)  
  <sub>24 hours ago</sub>  
  Elbit Systems Ltd. (NASDAQ:ESLT) shares rose Tuesday after the defense company reported third-quarter adjusted earnings of $4.36 per share,...
- [Elbit Systems Stocks Jump 7.8% as Backlog Hits Record $33 Billion](https://www.google.com/goto?url=CAESuAEBxCJF1_Yu8dex9j9g0sgD6rck4IB_oIedx2mFeTrRLc_SZRr3Ea4Hy625wUFJFWMx3CKohwedCOZSfQoyJUCXSBvfy01TFIS6KbcU0FIirSe0zwB6H_apquIAlOa8QoVgsJvcmnI10OQFt9RZ92Vo4ITyPIUBNKMy7eVoIknhuwj6RnkPYJWkE7HoMc6k3Vsj3bICre-TIVF1raIV0Nk4ouv7eZ8IYoWOnA4_ltPVSmfhAExVvKX8&gsessionid=gdU0Ks-xRvDQZ9n0R_2-FAJQLl0dvUfH3tXpApznHincDKKql8yM1Q)  
  <sub>21 hours ago</sub>  
  Elbit Systems NASDAQ:ESLT shares jumped 7.8% to $733.83 at 9:49 a.m. ET in regular trading on November 17, after the Israeli defense electronics maker...
- [ESLT Nov 2026 450.000 put (ESLT261120P00450000) Seasonal Returns Chart](https://www.google.com/goto?url=CAESgAEBxCJF19h_kb5QwGEnrRLl2_ALM1b9GaVoc5s8bQdYxmupHUXjja8UytNsrk5Y6lLWerZZkjTC-fV-ABS-PSU2iDov8sRq3oBOUu7mG87hR-0RMJNVP2FRfJgRHmnlxG70dRGyA4zrVcaYL_KA8W3eVjj_pgAD3w1-DNlU-aNbMg&gsessionid=gdU0Ks-xRvDQZ9n0R_2-FAJQLl0dvUfH3tXpApznHincDKKql8yM1Q)  
  <sub>13 hours ago</sub>  
  ESLT Nov 2026 450.000 put (ESLT261120P00450000) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [Which of This Week's Top 5 Industrial and Transport Stocks Offers the Strongest Outlook: Elbit Systems (NASDAQ:ESLT), AECOM (NYSE:ACM), SiteOne Landscape Supply (NYSE:SITE), United Airlines (NASDAQ:UAL) or Hertz (NASDAQ:HTZ)?](https://www.google.com/goto?url=CAESrgIBxCJF10pxufjZzntB7AbcHGmIsz_9-2oUhFXnMaY1nzk0GRJJvNuXsredr0hacA7EEwUAZx44-kPtnzXafgd-cHXeFo8dvKJtkL8euFpUrTKnGIDUeHr6xRExU7p-k9kxltIwlNTUvz5i-DxdVSpKT0fcODoG6XzQTaKvNpnYKFYbD0zuJqitW4j68FwMMyHrgz-rpiiHn19MzBCqdFsUQBBaTp-XaK_lHpAPwuIujnWpmdNePUBLe4SiPfUMf4KRRzdR6d8DI4HwQlNXY6W3cioMYppni4RFt8kQ-BD8IkNYe7nUaqTC_w6dJWxyPFz4SmA6KhFPS82faE_MMTt-ROvMvxR5SZmwaOulQljMa5NKGll0Jgo6-o4fwyI09gcYquKHcVwFVhGhRGdC3A&gsessionid=gdU0Ks-xRvDQZ9n0R_2-FAJQLl0dvUfH3tXpApznHincDKKql8yM1Q)  
  <sub>20 hours ago</sub>  
  Which of This Week's Top 5 Industrial and Transport Stocks Offers the Strongest Outlook: Elbit Systems (NASDAQ:ESLT), AECOM (NYSE:ACM), SiteOne Landscape...
- [Elbit Systems (NASDAQ:ESLT) Shares Gap Up After Strong Earnings](https://www.google.com/goto?url=CAEStgEBxCJF1-0aBDv6iHQ0mClIqjNI1NFXhKU2VTvmdnW_mbGSgCGKCN-XgYVgE8QV0umSWK60GVsb1g7obQyZDv6jqKWteeaLH5T72TMfG23klQVcw5x2DQq-aAxwNxhaAexh08vktAEtB0UR4MbTBGEXB533yH1Zr2nqsIPn3ne_V_ln9paAQ6GoXxXO-EPCWmwtDY3h_vJ8uokd8TNTUIAWgufBir8PssHBDQRM0yp_7LwiXteFMg&gsessionid=gdU0Ks-xRvDQZ9n0R_2-FAJQLl0dvUfH3tXpApznHincDKKql8yM1Q)  
  <sub>23 hours ago</sub>  
  Elbit Systems Ltd. (NASDAQ:ESLT - Get Free Report)'s stock price gapped up prior to trading on Tuesday after the company announced better than expected...
- [Elbit Systems Ltd. 2026 Q3 - Results - Earnings Call Presentation (NASDAQ:ESLT) 2026-11-17](https://www.google.com/goto?url=CAESuQEBxCJF1weHZNXOpatsBiutWagvRbYOIllVT8Xdmd5xJhQSDDF71Hl5lt4jrnP-gqVxFY1Fr8xk1ydndUeMCDcWiJMFfdwQ6cdp0oJ3VBBct6-NZrabqfU3jJanEQouc1Wb_Bh3a5wGRIHvPUQLsXfmKuJWmyfcoTfeRD6ItU3K_WBvORZPR_o1Syxx5fC7DGlZ2qVmxudKQ3abqsjEyyq76rf39zuqvtMU6B5pg6HdOrKXZ7RMMRS7rg&gsessionid=gdU0Ks-xRvDQZ9n0R_2-FAJQLl0dvUfH3tXpApznHincDKKql8yM1Q)  
  <sub>24 hours ago</sub>  
  2026-11-17. The following slide deck was published by Elbit Systems Ltd.
- [Elbit Systems Q3 2026 Earnings Results and Report](https://www.google.com/goto?url=CAESjAEBxCJF145YVVxfWvQjgkZ5Q0HDhhs4gUi8nyMz_9os4o0D5m1wmQMjPThaOSktnyZYhG52PxouydHuiauCM7ionMrtHHAec-8jWWrdJOQgl_MKkcrpGx5kX3t3BMttE6zCk8lwdBgHQWcjeKtYUrtiHhfAyARanzOFCEe05MV44koMChRs2V9916dfew&gsessionid=gdU0Ks-xRvDQZ9n0R_2-FAJQLl0dvUfH3tXpApznHincDKKql8yM1Q)  
  <sub>21 hours ago</sub>  
  Elbit Systems reported Q3 2026 earnings of $4.36 per share on November 17, 2026, beating the $3.65 consensus estimate, on revenue of $2.25 billion.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 706.62 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 733.72 (-3.7%), 50d 723.28 (-2.3%), 200d 785.26 (-10.0%); 50d below 200d
Momentum: RSI(14) 47.2 | MACD -6.525 vs signal -2.967 (histogram -3.558)
Returns: 1d -1.9% | 5d -2.6% | 1m -5.1% | 3m -5.0%
52-week range: 454.95 - 1,014.33 (now 45.0% of the way up)
Volatility: ATR(14) 29.19 (4.1% of price) | annualised 20d 64.9%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.45</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 33.13B
Valuation: trailing P/E 49.80 | forward P/E 37.07 | P/B 7.24 | PEG n/a
Profitability: profit margin 7.7% | operating margin 9.7% | ROE 15.8%
Growth (YoY): revenue +17.2% | earnings +32.1%
Balance sheet: debt/equity 22.6% | free cash flow 355.98M
Risk: beta n/a | short interest 0.8% of float
Next earnings: 2026-11-17
```

</details>

<details><summary><b>What this fund holds</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.45</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-09-30 beat by 9% | 2026-06-30 beat by 10% | 2026-03-31 beat by 16% | 2025-12-31 beat by 16%
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
Consensus: hold (mean 2.67 on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 838.92 (+18.7% vs last close), range 738.50 - 960.00
Recent rating changes:
  - 2026-10-05 Jefferies: main, Hold -> Hold
  - 2026-08-19 JP Morgan: main, Neutral -> Neutral
  - 2026-06-24 Jefferies: main, Hold -> Hold
  - 2026-05-27 Jefferies: main, Hold -> Hold
  - 2026-05-27 JP Morgan: main, Neutral -> Neutral
  - 2026-04-13 JP Morgan: main, Neutral -> Neutral
Institutional ownership: 26.3%
Largest holders: Clal Insurance Enterprises Holdings Ltd (3.5%), Vanguard Capital Management LLC (1.6%), Van Eck Associates Corporation (1.2%), Y.D. More Investments Ltd (1.1%), Altshuler Shaham Ltd (1.1%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 19,309,244 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### JPMorgan Chase (JPM) · Company — BEARISH, confidence 0.55

**Result:** ACCEPTED · 15 shares · submitted sell 15 JPM @ ~326.30, stop 340.79

**In the model's own words:**

> The recent payments outage and CFO succession news have turned negative sentiment, and the stock is trading below short‑term moving averages on very low volume, indicating short‑term weakness. However, JPM’s fundamentals remain strong (low P/E, high ROE, solid margins) and analysts still have a buy consensus with a 13% upside target, providing some bullish support. The net balance leans slightly bearish, but without a clear catalyst, conviction stays moderate.

**Main reasons it gave:**
- Payments outage on Monday caused stock slide
- CFO succession announced, adding uncertainty
- Price below 20‑day and 50‑day SMA with volume at 0.10× average
- Strong fundamentals: trailing P/E 13.8, ROE 18%, profit margin 34.6%
- Analyst consensus remains buy with mean target +13.3% vs last close

<details><summary><b>News</b> — score -0.60</summary>

- [JPMorgan Announces CFO Succession and Leadership Changes](https://www.theglobeandmail.com/investing/markets/stocks/JPM-N/pressreleases/8896288/jpmorgan-announces-cfo-succession-and-leadership-changes/)  
  <sub>The Globe and Mail, 55 minutes ago</sub>  
  Detailed price information for JP Morgan Chase & Company (JPM-N) from The Globe and Mail including charting and trades.
- [JPM Nov 2026 415.000 call (JPM261120C00415000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/JPM261120C00415000/chart/)  
  <sub>Yahoo! Finance Canada, 8 hours ago</sub>  
  Interactive Chart for JPM Nov 2026 415.000 call (JPM261120C00415000), analyze all the data with a huge range of indicators.
- [JPMorgan Stock Slides: What's Going On?](https://www.google.com/goto?url=CAESngEBxCJF1zxGyOAzvSk_M-78VDHoLQsr4LVJoAcMunNS8kjtQLjCHyJBDxF_7b-UoJxaRn6L2_T3vo4mCpn7qvA8q54rkdDiSwx8nrQxPLa2NQymLtpcQ1zwGInSuguWZ_7_r9W1SVOkU13Hw7O8_wTb7_d1_3mVR0MzEfiYeMua3_bT5Au4GFdDdkFUYfWL96yNgKRmSBpqpJYP9L-laQ&gsessionid=ovS6li7TQBRrUzPs9uq_Yg4SRWDMyjjoj6DtxUGYuBPFfpQTFcDLyw)  
  <sub>Benzinga, 23 hours ago</sub>  
  JPMorgan Chase & Co. (NYSE: JPM) shares are falling Tuesday. A payments outage occurred Monday, and the bank announced a new CFO.
- [JPMorgan Chase & Co. $JPM Stock Holdings Decreased by Mawer Investment Management Ltd.](https://www.google.com/goto?url=CAESzAEBxCJF14tkeS7AFOui7ea0VjiKHk7DEnxBnA7vxGWdIzthpsdvlVDcQ746HggYuGMtSUtGXpBvpnq7W3BKI1-JrBNtJdTUDW397klIs51gGJNflYY3dsH3jlqlIR1BKISxoz0Kij0ZHnEbr4FBqgdpulvGzB3JWor9ttH4FjNNL9no6pcU4saKJVTqojzCsLd4d9FjqxmunuiGUGwcW4NlcYysuLe1qdmkGlFJbXBypGT45x9OyOxoDrSSVCkUhfr7XkchVDbRgjwxVXY&gsessionid=ovS6li7TQBRrUzPs9uq_Yg4SRWDMyjjoj6DtxUGYuBPFfpQTFcDLyw)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Mawer Investment Management Ltd. lowered its stake in shares of JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 13.3% during the third quarter,...
- [Big bank stocks near 'death cross' bearish chart pattern after reports of outages (BKX:)](https://www.google.com/goto?url=CAESsgEBxCJF1-oHdY0JBteM71XGrShnGKJOJPo4kRW4foTWqOuxYiaIVTvjRI9t-Kt6g5WR36HxgN-lEYk1x0XCYRQSBNLtVosC7jnFt9MmHF3PiUQsfnTs179SnfNrOAV0aYStc3LNrD-cusyfX2JAgnzd0NExOn5UgokmPhXophJZK6jIPzTcJChaBeuW6jzHBF2sHP4zNTW0ywn69BornvK3yj_Xk0eCkK-3z2xyXFQ5vmkS&gsessionid=ovS6li7TQBRrUzPs9uq_Yg4SRWDMyjjoj6DtxUGYuBPFfpQTFcDLyw)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Large U.S. bank stock prices neared the rare 'death cross' bearish technical chart pattern, with the KBW Bank Index's (BKX) 50-day moving average almost...
- [JPM GBP Std Mny Mkt VNAV W acc. (0P00019JPN.L) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAEScwHEIkXX6Iy3U0OxslQeMfJk2i8HmT_qNpYTUstKyCFmbBcF6GXjiAZwugtUF3Z9sIwuSZ4DHntY23sR7FgPeTH-QH7DC-wMlbBmrv2nMQnKIrSloS1-UtLoUuO6_gnhgWrwbttI5gt1KANILABrtgu9Sno&gsessionid=ovS6li7TQBRrUzPs9uq_Yg4SRWDMyjjoj6DtxUGYuBPFfpQTFcDLyw)  
  <sub>Yahoo! Finance Canada, 9 hours ago</sub>  
  Interactive Chart for JPM GBP Std Mny Mkt VNAV W acc. (0P00019JPN.L), analyze all the data with a huge range of indicators.
- [After Monday's Banking Outage, JPMorgan Chase (NYSE:JPM) Slips as It Names a New CFO](https://www.google.com/goto?url=CAESrgEBxCJF10taLfzvPtGgSIdLo-gaZCMbYYtOEsIRqTBpdX3viGOw_SeAilRAriZqZC2UsZwdiCH8NVchwuTsMGH38NdvHDDDK6hdYlZpzff3ioAqcY4_uqFmP5Qg4Gg9ruIjBOHNAP3Vze6VRAlfuecMSueh1TWH9SbwJ5cHe5fJ0XaGC3wkUPMGaRmg4xJ_TBPAE8Kb7P6eNfaY7YkONCFBPoRYdJvMMjLp56Er07Y&gsessionid=ovS6li7TQBRrUzPs9uq_Yg4SRWDMyjjoj6DtxUGYuBPFfpQTFcDLyw)  
  <sub>kalkine.ca, 19 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [JPMorgan Chase & Co. $JPM Stock: Aberdeen Group plc Grows Holdings](https://www.google.com/goto?url=CAEStwEBxCJF1yeqjdnOmItIGFbAnQ1d65-DSFYGdCzCvVynhsGmO5V22vS8QlVWkycFIIZdtkQ8AWcBOM8TN8QVG6RQgPVJO_GMyQ_ep4YbrRu93uDmz6PKHCYrEXZSK2C1a1Qui9Z9VubTcgx3mxLzVLjgaToRUcDdXA5DyqxftUn0AdJG2VpKOWBGAnzvDFdPDH4rrikMvcJsw2PIK-5ZiI38DiXbpHmD2lH3KLXyNoHpOdn34f3hGbU&gsessionid=ovS6li7TQBRrUzPs9uq_Yg4SRWDMyjjoj6DtxUGYuBPFfpQTFcDLyw)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Aberdeen Group plc grew its holdings in JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 3.7% in the third quarter, according to the company in its most...
- [JPM Nov 2026 332.500 call (JPM261120C00332500) Interactive Stock Chart](https://www.google.com/goto?url=CAESeQHEIkXXgUD_rt7JEdx7jqVSHzIk-0-ylDbZWLeNPGIhfUSmBttb4zhgCD6R10htH1Kiz4yY_tNUTzqSbwFYK12kQhPN4D2tij2wVIzHfs31iascUmjHbtMDLpFuCYHB9aTMlqOIbhatirOL5kdfbKvfyxdovKAUl9A&gsessionid=ovS6li7TQBRrUzPs9uq_Yg4SRWDMyjjoj6DtxUGYuBPFfpQTFcDLyw)  
  <sub>Yahoo! Finance Canada, 13 hours ago</sub>  
  Interactive Chart for JPM Nov 2026 332.500 call (JPM261120C00332500), analyze all the data with a huge range of indicators.
- [JPMorgan Chase & Co. $JPM Stock: 10Elms LLP Cuts Position](https://www.google.com/goto?url=CAESrgEBxCJF12O34_MysZXvpl0z8rkZQpi4FFL47YyYpY8CmgtNMmplwMHI7-ZKqb78VhzNFyx5rzYiLf5EukSw4wn6sSuIz7gDBFMm1m6WZhLd1QP775_sMwIQvG5ke0-uMLTfbaTgwdMGNlWBaanPA9MkavuxLTMKaFOrKrmp5OKyPQQrDAuIpYJm5HLiq2i3NDBiOxWz8H_vHODfF7gAHy6jWdXyTQ1CPwoNofOR2JI&gsessionid=ovS6li7TQBRrUzPs9uq_Yg4SRWDMyjjoj6DtxUGYuBPFfpQTFcDLyw)  
  <sub>MarketBeat, 7 hours ago</sub>  
  10Elms LLP decreased its stake in JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 97.6% in the 3rd quarter, according to its most recent Form 13F filing...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.70</summary>

```text
Last close 329.53 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 338.73 (-2.7%), 50d 339.04 (-2.8%), 200d 325.21 (+1.3%); 50d above 200d
Momentum: RSI(14) 41.7 | MACD -0.722 vs signal 0.225 (histogram -0.947)
Returns: 1d -0.1% | 5d -4.0% | 1m -1.7% | 3m -6.3%
52-week range: 282.84 - 365.18 (now 56.7% of the way up)
Volatility: ATR(14) 7.16 (2.2% of price) | annualised 20d 29.2%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 875.10B
Valuation: trailing P/E 13.82 | forward P/E 12.89 | P/B 2.49 | PEG 1.40
Profitability: profit margin 34.6% | operating margin 44.8% | ROE 18.0%
Growth (YoY): revenue +10.2% | earnings +9.9%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 1.02 | short interest 0.9% of float
Next earnings: 2027-01-14
```

</details>

<details><summary><b>What this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.60</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-09-30 missed by 7% | 2026-06-30 beat by 4% | 2026-03-31 beat by 8% | 2025-12-31 beat by 3%
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
Consensus: buy (mean 2.04 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 5 strong buy, 10 buy, 11 hold, 0 sell, 0 strong sell
Price target: mean 373.48 (+13.3% vs last close), range 312.00 - 425.00
Recent rating changes:
  - 2026-11-02 UBS: main, Buy -> Buy
  - 2026-10-15 Citigroup: main, Neutral -> Neutral
  - 2026-10-14 Truist Securities: main, Hold -> Hold
  - 2026-10-14 Barclays: main, Overweight -> Overweight
  - 2026-10-14 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-14 Morgan Stanley: main, Equal-Weight -> Equal-Weight
Institutional ownership: 75.3%
Largest holders: Blackrock Inc. (7.7%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.7%), Vanguard Portfolio Management LLC (2.7%), Morgan Stanley (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Royal Bank of Canada (RY) · Company — NEUTRAL, confidence 0.50

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technical indicators are bearish (price below 20‑day and 50‑day SMAs, low RSI, negative MACD, very low volume) suggesting short‑term downside pressure. Fundamentals remain solid and analysts are bullish, while recent institutional buying and short‑interest unwind provide modest positive sentiment. The mixed news and lack of a clear catalyst lead to a cautious stance.

**Main reasons it gave:**
- Price below 20‑day and 50‑day SMA (‑4% and ‑3%) indicating downtrend
- RSI 37.8 and MACD negative, showing weak momentum
- Low volume (0.03× 20‑day average) suggests lack of buying support
- Public Sector Pension Investment Board increased stake by 27.8% in Q3 (institutional buying)
- Short interest fell 39.6% indicating unwind of bearish positions

<details><summary><b>News</b> — score +0.20</summary>

- [REG - Chapel Down Group Royal Bank of Canada - Holding(s) in Company](https://www.tradingview.com/news/reuters.com,2026-11-18:newsml_RSR7268Da:0-reg-chapel-down-group-royal-bank-of-canada-holding-s-in-company/)  
  <sub>TradingView, 1 hour ago</sub>  
  RNS Number : 7268D Chapel Down Group PLC 18 November 2026 TR-1: Standard form for notification of major holdings This information is provided by RNS,...
- [Royal Bank of Canada shares technical analysis: Weak momentum signals prevail below resistance](https://tradersunion.com/news/stocks/show/4303097-royal-bank-of-canada-down/)  
  <sub>Traders Union, 42 minutes ago</sub>  
  Highlights. Short interest in Royal Bank of Canada stock fell 39.6% in the second half of October, indicating a substantial unwind of bearish positions.
- [RY Nov 2026 185.000 call (RY261120C00185000) Seasonal Returns Chart - Yahoo Finance](https://www.google.com/goto?url=CAESfgHEIkXXXX7kL3U_WIcF6H242zjnvlWDgG7U-RwzpfPco1SfFOFh1YBfFWRgyjWbJJs2pSBoOKBKuPsOEwlhIGapTz068KspTnHVFv2dcVTAtfP8cBjYs7QELNF0PdVdvEFgnTa1SgXPUSLz4hPMGleVavHTkLHUt3bkKcYzbw&gsessionid=vjcXWjUBocd0zfwxFQLwG3CikWbDWYcULJyCt2PvmTIiJLArTHc94g)  
  <sub>Yahoo! Finance Canada, 8 hours ago</sub>  
  RY Nov 2026 185.000 call (RY261120C00185000) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [Royal Bank Of Canada $RY Shares Acquired by Public Sector Pension Investment Board](https://www.google.com/goto?url=CAESzAEBxCJF1yo-l7Agd-dbyLY_LbiGYlKQ1tgsjzYW7jnBGOw0kgp_oqiiKHvb4yPLLGnuHhnPZMUnzKjQyLf_5rUuqoxZNd5DbbRIqUvmhVP-UWuRvnHb2SyEKRe9qV2PL4Nflw_7X6LJK-LVlfuursts7fSoiWLbIF1xa6Q9kDi6nsSEKWHODpD-uVhWmvkS-88a9Y-t_oKjIdVitkp9mMeJWby067RyyBUXOfTpL7BZ0idoiIsBk6iZxb5sv6MJsyoq-eslpt8aRXljlnM&gsessionid=vjcXWjUBocd0zfwxFQLwG3CikWbDWYcULJyCt2PvmTIiJLArTHc94g)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Public Sector Pension Investment Board grew its stake in shares of Royal Bank Of Canada (NYSE:RY - Free Report) (TSE:RY) by 27.8% during the 3rd quarter,...
- [Royal Bank Of Canada (RY) - What Are Brokerages Thinking About This Stock?](https://www.google.com/goto?url=CAESwwEBxCJF19Oxrv2xJcfhUb5nqIPkA_WtwDQfflGVCzBFyWWPH-uS9jRZKhnpfJ5Wp8dSinULyfDmN85cvHusZ9dtPaX0cj5VuNRY99rm8G_0Jnz0RntjmWv54EWWnGfnPGvUl6U2jL6IoruobQg2GRR3zLRLexCx-_N6xikDFsquC3AmKniXd71IrltTD3fWflgH006I95IbwU-43fu1efFBFlJOsnh8g_Ghcnj33r9Lcb61B3KXNPmmeGt_2O1wX4m8_Vk&gsessionid=vjcXWjUBocd0zfwxFQLwG3CikWbDWYcULJyCt2PvmTIiJLArTHc94g)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Royal Bank Of Canada (NYSE:RY - Get Free Report) (TSE:RY) has earned an average rating of "Moderate Buy" from the fourteen brokerages that are currently...
- [What's behind Royal Bank of Canada's latest 2.0% stock pullback?](https://www.google.com/goto?url=CAESiwEBxCJF1-nJYP73A1T6PT3tf9_CPI0GFmhj2vb01371CQ1LEbBY2v_DnpUbz3hklC7pT1d8IiWaxBbliAj2Qo25Sr8x6mpi8Lw29GfLNBSV5xE0TZOlOsaAsbeIcaP28jnDaI72JAjfk44M2nDfT5cHBEypxyqdN6LTITJztyWZp4sIzF_XhSfqn1zD&gsessionid=vjcXWjUBocd0zfwxFQLwG3CikWbDWYcULJyCt2PvmTIiJLArTHc94g)  
  <sub>Traders Union, 20 hours ago</sub>  
  Royal Bank of Canada (RY) fell 2.00% today as the session opened with a downside gap and sustained selling pressure, even as the company reported...
- [How rate-hike worries dragged TSX:RY, TSX:TD and TSX:BMO lower on the S&P/TSX Composite](https://www.google.com/goto?url=CAESsAEBxCJF1yIXc4tKV44Fvbrv1EkPE9HJoUAT7AiBjwgXyRxKR56tclRT3KHCjpA8K8PtxsRliIAjyFL_dNA3W1An8RFkDyX2RxouvSQXrqs7XIncBw5PZ0wk_YKZud-y8c--qQc3lpaJW4TGJabGeN9kc9DI3jM6zPi2D2Zw130UwSA_HoXVdVrsycKzY_YgQd5w7dFLi2FtN6ogUhLD35NSArNnSDaOVQqPuHaqk4DnUA&gsessionid=vjcXWjUBocd0zfwxFQLwG3CikWbDWYcULJyCt2PvmTIiJLArTHc94g)  
  <sub>kalkine.ca, 7 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [RY Jan 2028 155.000 put (RY280121P00155000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScgHEIkXXa1DPjhyj6Y-wmdzhM9RDXsTXwviVl1ruMg5zjf02x5MS2wk58yXqRG8M4LYecs6B2QL9WGotMzu7zCknPOKchIicwJ6AeSrIbTN07XnjoLl13lVkNy-KLaJt6QRLTcyNAVJg6vg14Sz7jsmQKw&gsessionid=vjcXWjUBocd0zfwxFQLwG3CikWbDWYcULJyCt2PvmTIiJLArTHc94g)  
  <sub>Yahoo Finance UK, 23 hours ago</sub>  
  Find the latest RY Jan 2028 155.000 put (RY280121P00155000) stock quote, history, news and other vital information to help you with your stock trading and...
- [How I’d Structure a $10,000 TFSA for Steady Income, Stock By Stock](https://www.google.com/goto?url=CAESmwEBxCJF146Q-vivvN0lrn8uANceRiGwmgqoDFxI80CWEwJ2pV49qXG0KE47xN3xEOjLdE3ottjrxNEPsXCR339LVvICf4a-28oQIkGegkZFHWEczFxVYTqimQx-KKMuQvYNe3loHP_6JCY2kwE_84EZ6j7sUL9jSoWRHiN3xrw38D_x--Vs_-2vxO1baFrrX_4DLgpHUqjGPD0ePg&gsessionid=vjcXWjUBocd0zfwxFQLwG3CikWbDWYcULJyCt2PvmTIiJLArTHc94g)  
  <sub>The Motley Fool Canada, 17 hours ago</sub>  
  Wondering how to earn over $325 per year in your TFSA? This simple 4-stock portfolio bulks up in some of Canada's top dividend growth stocks.
- [Purpose Investments Inc. Announces November 2026 Distributions](https://www.google.com/goto?url=CAES0QEBxCJF16ZfsMbgsC9nNWEMvuSZqfS5aJFEf77dMjXKbT3g-KTJ7nwR87xdVh_krwqv8racHVevqQxAM27HbMD8KUKpNbunFz6jRIb8kIXUXl-H866H-0t6y5o9s2vWiVydHFEHwYp8ojXsXhi5CVQ-TnGM6AEBpsFNS8LUdtRlHh1_63SfIPKUe9luX6kuGStlS-xbDmIwCuXEP-VHxWEEP-A_naQVYQqAaTqUUTmJxJRSMgAaH6PeXSIpd9K2sliJL0J4k2UdQspUYQRZOL4g7w&gsessionid=vjcXWjUBocd0zfwxFQLwG3CikWbDWYcULJyCt2PvmTIiJLArTHc94g)  
  <sub>The Globe and Mail, 16 hours ago</sub>  
  TORONTO, Nov. 17, 2026 (GLOBE NEWSWIRE) -- Purpose Investments Inc. (“Purpose”) is pleased to announce distributions for the month of November 2026 for its...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 194.42 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 202.55 (-4.0%), 50d 200.37 (-3.0%), 200d 191.41 (+1.6%); 50d above 200d
Momentum: RSI(14) 37.8 | MACD -0.559 vs signal 0.483 (histogram -1.042)
Returns: 1d -1.1% | 5d -4.5% | 1m -2.3% | 3m -5.3%
52-week range: 147.35 - 217.87 (now 66.7% of the way up)
Volatility: ATR(14) 3.30 (1.7% of price) | annualised 20d 20.6%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 269.16B
Valuation: trailing P/E 16.99 | forward P/E 15.26 | P/B 2.82 | PEG 1.87
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: buy (mean 2.21 on a 1=strong buy to 5=strong sell scale, 3 analysts)
Ratings: 4 strong buy, 4 buy, 5 hold, 0 sell, 1 strong sell
Price target: mean 208.32 (+7.2% vs last close), range 181.82 - 229.13
Recent rating changes:
  - 2025-08-29 Argus Research: main, Buy -> Buy
  - 2024-12-05 BMO Capital: main, Outperform -> Outperform
  - 2024-08-29 BMO Capital: main, Outperform -> Outperform
  - 2024-06-06 Argus Research: main, Buy -> Buy
  - 2024-04-05 BMO Capital: up, Market Perform -> Outperform
  - 2023-12-18 B of A Securities: up, Neutral -> Buy
Institutional ownership: 49.6%
Largest holders: Royal Bank of Canada (5.1%), Bank of Montreal /CAN/ (4.2%), Vanguard Capital Management LLC (3.1%), TD Asset Management, Inc (1.6%), NORGES BANK (1.4%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

_Not available today._

</details>

### Eli Lilly (LLY) · Company — BULLISH, confidence 0.45

**Result:** ACCEPTED · 3 shares · submitted buy 3 LLY @ ~1390.98, stop 1304.66

**In the model's own words:** no explanation. It wrote only “moderately bullish”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Four consecutive earnings beats (12%–38% above consensus)
- Stock trading near 96% of 52‑week high, above 20‑, 50‑, 200‑day SMAs
- High profit margin (31.9%) and ROE (86%) indicating strong business
- Analyst consensus buy with mean price target +3.5% above current price

<details><summary><b>News</b> — score +0.00</summary>

- [LLY Jun 2028 1580.000 put (LLY280616P01580000) interactive stock chart](https://uk.finance.yahoo.com/quote/LLY280616P01580000/chart/)  
  <sub>3 hours ago</sub>  
  Interactive chart for LLY Jun 2028 1580.000 put (LLY280616P01580000) – analyse all of the data with a huge range of indicators.
- [LLY Dec 2026 1430.000 put (LLY261224P01430000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/LLY261224P01430000/)  
  <sub>4 hours ago</sub>  
  Find the latest LLY Dec 2026 1430.000 put (LLY261224P01430000) stock quote, history, news and other vital information to help you with your stock trading...
- [LLY Dec 2026 1475.000 call (LLY261224C01475000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXZcIA3tcbdehA5uBv0OmQwWZL3tQayDPgzJzvN0KBxBqaXBG-5TUOtx9196Keowv-M6Zr9eA3oRWsC5r959WBjV3qjELOo8u6ZcHrMSRqjBjPYDCNUtpbE0q8yCgSgHbyBkEqiJVgWljSxKI6FEY&gsessionid=pa33CVAIqyQ8MWe4laVDZDbX6lQJ5XFwmcJnApk6kbMIuqfu-wwVRA)  
  <sub>4 hours ago</sub>  
  Find the latest LLY Dec 2026 1475.000 call (LLY261224C01475000) stock quote, history, news and other vital information to help you with your stock trading...
- [LLY Dec 2026 1130.000 put (LLY261224P01130000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXtQzfMPjgMvOpVGqizYlI4lGaVsQlp3YShkxTuqb90JNed8A4QE2ZDMUfuBtFVlftp-fgLNZz-8UAz8fE_FD6f7drFoco9Il4uRwI3caoY9ThvLcjvxhhK8crrxSxf1NYYSkHmDLK99MJ9f0h6I4&gsessionid=pa33CVAIqyQ8MWe4laVDZDbX6lQJ5XFwmcJnApk6kbMIuqfu-wwVRA)  
  <sub>4 hours ago</sub>  
  Find the latest LLY Dec 2026 1130.000 put (LLY261224P01130000) stock quote, history, news and other vital information to help you with your stock trading...
- [LLY Dec 2026 1450.000 put (LLY261224P01450000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXX6BuPZkt4FSrKNeIKolWAtM_WfTnRudqYswvB5YcJ3ApO1vIJ6c7T48UWlda-UQHapAa2f45PvNg84Tu0M77GjygGXoPkmMNur1SIMl-rMGMSGWAjB--4Wlk7are-2Bg8JpriXk346DUn-9ihu40&gsessionid=pa33CVAIqyQ8MWe4laVDZDbX6lQJ5XFwmcJnApk6kbMIuqfu-wwVRA)  
  <sub>5 hours ago</sub>  
  Find the latest LLY Dec 2026 1450.000 put (LLY261224P01450000) stock quote, history, news and other vital information to help you with your stock trading...
- [LLY Dec 2026 1560.000 call (LLY261224C01560000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXQoOT1jS5dCTPLUccAMXnafZEvl8VfZFvvWAkRHp6GnIzIvNTimquWSZ9FSky9E41rRfHPf4F9q9RT0uvO8A8ib2Frcxn47TM7ddxQA3ITz4oR4ERG0enAuVtvRBD7Aucm8ueAI2Evgm6tDeN-Hs&gsessionid=pa33CVAIqyQ8MWe4laVDZDbX6lQJ5XFwmcJnApk6kbMIuqfu-wwVRA)  
  <sub>5 hours ago</sub>  
  Find the latest LLY Dec 2026 1560.000 call (LLY261224C01560000) stock quote, history, news and other vital information to help you with your stock trading...
- [LLY Dec 2026 1225.000 put (LLY261224P01225000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXA84ZNsLahlDCx4vgfkDikY7I4KWW3hSCFAITUI41L6HAOAKyrY7uoT0F7RRxE3Vce5RSTAxVKMzlsr1fXuyA04QNoO7A1mJoX7Ir13yoyS-3lOrqq00B0hzpyQJC7vvJJpOC88sSO69Tvn5KmbM&gsessionid=pa33CVAIqyQ8MWe4laVDZDbX6lQJ5XFwmcJnApk6kbMIuqfu-wwVRA)  
  <sub>5 hours ago</sub>  
  Find the latest LLY Dec 2026 1225.000 put (LLY261224P01225000) stock quote, history, news and other vital information to help you with your stock trading...
- [LLY Dec 2026 1110.000 call (LLY261224C01110000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXXqHkW2_7u0Y-AhaxhBk2Jx-ctm6K1IwerGIvH99MSjlOdKrdqcCeinxvlH3htYj_zyenCBFwP8E7DC_PIt5V0H3CYAT6DeaWjTxYpYV5XL4SXAEvX8YvK1_cyKd9zTj9qQkhq4m3PxqZUxxSb18&gsessionid=pa33CVAIqyQ8MWe4laVDZDbX6lQJ5XFwmcJnApk6kbMIuqfu-wwVRA)  
  <sub>5 hours ago</sub>  
  Find the latest LLY Dec 2026 1110.000 call (LLY261224C01110000) stock quote, history, news and other vital information to help you with your stock trading...
- [LLY Dec 2026 790.000 put (LLY261224P00790000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXI16RvEzrbDOp0FGlHfY0sADSmPaKZQx-4I_MvKlQ5qdlNremlymhMKs7ZwFIh6du-tnLXJIIucjZR7CGbm0jp1re27-ZDyWTKAue42FND4W2XG_uU25LR53M4PeYgHGUCdQo3nPIy0IwU0dMFuE&gsessionid=pa33CVAIqyQ8MWe4laVDZDbX6lQJ5XFwmcJnApk6kbMIuqfu-wwVRA)  
  <sub>5 hours ago</sub>  
  Find the latest LLY Dec 2026 790.000 put (LLY261224P00790000) stock quote, history, news and other vital information to help you with your stock trading and...
- [LLY Nov 2026 1325.000 call (LLY261120C01325000) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXfRBIl92yGrer6urtHyPKPbyRNkvVcgei_Xcy9PhxARDmvmtxAbFbelQy79D3Oy1AIDarjTUxC-qGa0vmSzKPXMxsm-MhPZIbumeFwjv7Ch8OQTDNjv2G1i-hAZ1zl1lo4e3tPG3whl0x5OX-YOpCFgyfgIs&gsessionid=pa33CVAIqyQ8MWe4laVDZDbX6lQJ5XFwmcJnApk6kbMIuqfu-wwVRA)  
  <sub>7 hours ago</sub>  
  Interactive chart for LLY Nov 2026 1325.000 call (LLY261120C01325000) – analyse all of the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 1,418.94 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 1,379.82 (+2.8%), 50d 1,258.45 (+12.8%), 200d 1,115.23 (+27.2%); 50d above 200d
Momentum: RSI(14) 63.5 | MACD 50.130 vs signal 53.117 (histogram -2.987)
Returns: 1d +0.2% | 5d -1.3% | 1m +10.5% | 3m +14.0%
52-week range: 851.21 - 1,443.50 (now 95.9% of the way up)
Volatility: ATR(14) 41.85 (2.9% of price) | annualised 20d 36.8%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.26T
Valuation: trailing P/E 46.05 | forward P/E 27.93 | P/B 31.40 | PEG 1.31
Profitability: profit margin 31.9% | operating margin 51.3% | ROE 86.0%
Growth (YoY): revenue +38.6% | earnings +16.3%
Balance sheet: debt/equity 122.9% | free cash flow 9.34B
Risk: beta 0.39 | short interest 0.8% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-09-30 beat by 18% | 2026-06-30 beat by 38% | 2026-03-31 beat by 27% | 2025-12-31 beat by 12%
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
Consensus: buy (mean 1.65 on a 1=strong buy to 5=strong sell scale, 29 analysts)
Ratings: 5 strong buy, 20 buy, 4 hold, 1 sell, 1 strong sell
Price target: mean 1,468.57 (+3.5% vs last close), range 940.00 - 1,700.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 39,034 shares in 42 transaction(s) | sold 313,215 shares in 9
Net: -274,181 shares (-13.7% of insider holdings) | insiders hold 1,728,045 shares
Distinct insiders: 0 buying, 4 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-11-02 HAKIM ANAT (General Counsel): 5,000 shares, 7.01M
  - 2026-08-17 JONSSON PATRIK (Officer): 6,500 shares, 7.64M
  - 2026-08-10 ZAKROWSKI DONALD A (Officer): 2,000 shares, 2.37M
  - 2026-08-07 HAKIM ANAT (General Counsel): 5,000 shares, 5.95M
(38 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

> The news is mildly bearish (soft fourth‑quarter outlook and AI‑related sell‑off causing a 22% drop), while technicals are also slightly bearish (price far below moving averages, low volume) but show oversold momentum. Fundamentals are strong (high ROE, solid growth, reasonable valuation) and earnings record is positive (3 beats, 1 in‑line). Analyst consensus is bullish with a large upside target, and insider net buying is modest. The mixed signals lead to a neutral stance with low conviction.

**Main reasons it gave:**
- Soft fourth‑quarter outlook and AI sell‑off causing 22% drop in past month (negative news)
- Fundamentals: strong profitability (ROE 56.1%) and growth (revenue +17.3%, earnings +46.1%)
- Technical oversold RSI 29.1 and positive MACD histogram suggest potential bounce but price far below moving averages
- Analyst consensus: buy with mean rating 1.97 and price target +45.7% vs last close
- Insider net buying of 14,690 shares (+1.3% of holdings) despite CEO sale

<details><summary><b>News</b> — score -0.40</summary>

- [Is Red Cat Stock a Buy After Its Nov. 16 Earnings Report?](https://finance.yahoo.com/markets/stocks/articles/red-cat-stock-buy-nov-113500616.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Red Cat (NASDAQ: RCAT) reported its third-quarter results after the market closed on Nov. 16, and results were far worse than anticipated.
- [What Is The True Hidden Price Of Caterpillar Stock?](https://www.trefis.com/stock/cat/articles/626242/what-is-the-true-hidden-price-of-caterpillar-stock/2026-11-18)  
  <sub>Trefis, 4 hours ago</sub>  
  For questions about this article or underlying research, email help@trefis.com.Caterpillar (CAT) stock trades at 23.0 times its normalized net income over...
- [Red Cat Holdings, Inc. (RCAT) stock price, news, quote and history](https://www.google.com/goto?url=CAESZQHEIkXXlpI06sUfUyooGLzu9ux03kXyu63aEMAxISeDknzFW_mCKWWFt8bGrNFTYjVggoPywQZafpkM3pdiXouZmAIniWkvfJtWEPG5JdSbJvlw_NxFkS_tVeV29Crv8DIP0io0&gsessionid=r5Jht7io73FAlavSfmWoTP9VJNT3zBDZ7-6Kee6kI1Zq5PLxLEL7zQ)  
  <sub>Yahoo Finance UK, 3 hours ago</sub>  
  -100.00% · Previous close 3.5300 · Open 2.5600 · Bid 1.9300 x 200 · Ask 3.1200 x 200 · Day's range 2.3000 - 2.7200 · 52-week range 2.3000 - 18.7800 · Volume...
- [Red Cat stock plunges a third after revenue miss and pulled 2026 target](https://www.google.com/goto?url=CAESoAEBxCJF16fC6voTp1x6AhxgyrctpqeWp-OS7fJEhXIm6i8QGjLYuENIAert66F-fgNnJBuDDK7FofinDQb5YEIhBiSKRUlwwrFLR65BGAhiUjvd3PGmrBYUkqR5c2CR7Ua9mzUcd2PpUMICy_7ZOrLZpTMqLWev2BjFJhxp680vWtAWs5nrBNbRQD_lS6kr535A-8Ox9BS6beIYOLsMYiwM&gsessionid=r5Jht7io73FAlavSfmWoTP9VJNT3zBDZ7-6Kee6kI1Zq5PLxLEL7zQ)  
  <sub>Startup Fortune, 4 hours ago</sub>  
  Red Cat Holdings missed Q3 revenue by about 70%, withdrew its 2026 target after a weak Gauntlet II showing, and its shares fell roughly a third on Nov 17.
- [Drone Maker Red Cat Stock Plunges 35% on Trouble Getting Sales off the Ground](https://www.google.com/goto?url=CAESgwEBxCJF19_VSpNlwhJ3Qu4LX4da5nlYiv4ybCCjVqgjMJ8vTKXM4xZVVQwyAWQZhLfPBSZY0cLpVuI2XG82FMoUjPsRxeX4-EV-QkiNORKVNHFxynDejhFRNDEoK1jHzNBOwn6igNJJbwrEPJFfpa2r28KC6dzRy7SrJuieh67JCt68SQ&gsessionid=r5Jht7io73FAlavSfmWoTP9VJNT3zBDZ7-6Kee6kI1Zq5PLxLEL7zQ)  
  <sub>Barron's, 24 hours ago</sub>  
  Red Cat reported third-quarter sales of $11.8 million after the market closed Monday. Wall Street was looking for $38 million.
- [Why Did ASTS, NFLX, RCAT Stocks Plunge To 52-Week Lows Today?](https://www.google.com/goto?url=CAEStAEBxCJF113PEOE2_FUlSmZOfIo3PSKUChRlvL7RzYC9jdlgqfaoyEl_SB85YLJOCtFrHaF6LhbOz9d5ZtjO6SpwU25KkbINy9xVeDcST87DtdWIMMVBUMoR8PBuGJJXt2TVmIukBqXwnGknOLy-5Wi-T_tqft9VPNzeIo-6_TpnoiXNTR-eYg1YLtYi6_YjAC5i5erkrOT_5VY7773VDNz7Jp5i7k-UB658Z2t2NEZX1fft6V4&gsessionid=r5Jht7io73FAlavSfmWoTP9VJNT3zBDZ7-6Kee6kI1Zq5PLxLEL7zQ)  
  <sub>TradingView, 10 hours ago</sub>  
  AST SpaceMobile (ASTS), Netflix (NFLX) and Red Cat Holdings (RCAT) stocks hit fresh 52-week lows on Tuesday as concerns over rocket development costs,...
- [$100 Invested In Caterpillar 10 Years Ago Would Be Worth This Much Today](https://www.google.com/goto?url=CAESqQEBxCJF1xwOYV64YKdVMiLHaDP0zKpriWAkYcJLdGsdskFpFh7VDLBBVjMqSCdNSij8qbHlQvFHR_lTtMrcJCQRuhOByaeYA3H1ym9815tKtqKSlBNfJD-TVAbGqDoJ44SD4jl63gU92dbVVR-ubJSClHL2i2kKqS6PQ7V-Y88wqIqDbxmX1VOdEAUQgTo0ZvwUgrc5K1ggEiQG672v6GB4FiQ78XWd94bW&gsessionid=r5Jht7io73FAlavSfmWoTP9VJNT3zBDZ7-6Kee6kI1Zq5PLxLEL7zQ)  
  <sub>Benzinga, 15 hours ago</sub>  
  Caterpillar (NYSE:CAT) has outperformed the market over the past 10 years by 7.06% on an annualized basis producing an average annual return of 19.81%.
- [Red Cat Holdings Investigation Notice: Levi & Korsinsky Notifies Investors of Pending Investigation Into Red Cat Holdings, Inc. (RCAT)](https://www.google.com/goto?url=CAES-gEBxCJF1zhg4xSGxYT98WJ7CRgoN4qjIrZzMQ876lNX-QVV21CPyG4F6z69uAgXCINmIqEgihw0IzVO_S6jmuQPp7BnyDGGGLq71N-OGI0qAX5kzKAsI_E43oDVWX8pEAIiJ9uS1yGLH3q4eHf9ObgScCnzZZYyhIzWM-0BI88ulMPdQ8w7Yrb7Yg7r8y9siujIQDvgRwUAy0eGsnkFmjw07X7vMT3ejh9wMzHDkcha8VTnDmNcfSwLUyf3Svkz_sTDJ683YfSwt-KSSxGeBvLZAbsZCJY-Y6lW4sGxYo-CJPEcIlcQHZrwze5dhF_MeMOIQtwgvnyzXMaP&gsessionid=r5Jht7io73FAlavSfmWoTP9VJNT3zBDZ7-6Kee6kI1Zq5PLxLEL7zQ)  
  <sub>Morningstar, 15 hours ago</sub>  
  Red Cat Holdings Investigation Notice: Levi & Korsinsky Notifies Investors of Pending Investigation Into Red Cat Holdings, Inc. (RCAT)...
- [“Trades Basically Like an AI Stock”: Caterpillar Just Dropped 22% in a Month. Sell, or Load Up?](https://www.google.com/goto?url=CAESrwEBxCJF18AgcNLhSJ1xwYxmml6FZXkSbLNwORTcN73sINUnbERb4eGma3SW_5tbyxAgwEN-nVpotGYfrFMXmHKrlsj_ynXajnGnC0d94RqILorXOqrxMyhPOsu_hSckiFMRU79WFIOkBfSZH2vV243GCoVDUT8WVFNd5ZK4BllXNvOsk0wz-MA5cThySy8ulrKa5RG0YnupvKq3E5HBL8qVIgVW2_xx81UJxhbeJQgf&gsessionid=r5Jht7io73FAlavSfmWoTP9VJNT3zBDZ7-6Kee6kI1Zq5PLxLEL7zQ)  
  <sub>TIKR.com, 6 hours ago</sub>  
  Caterpillar stock is down 22% in the past month. A soft fourth-quarter outlook started the drop, and an AI-power selloff that also hit GE Vernova deepened...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 553.97 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 620.35 (-10.7%), 50d 725.63 (-23.7%), 200d 805.65 (-31.2%); 50d below 200d
Momentum: RSI(14) 29.1 | MACD -47.162 vs signal -47.989 (histogram 0.827)
Returns: 1d -2.9% | 5d -7.9% | 1m -23.6% | 3m -32.1%
52-week range: 546.13 - 1,064.90 (now 1.5% of the way up)
Volatility: ATR(14) 28.19 (5.1% of price) | annualised 20d 60.5%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 253.49B
Valuation: trailing P/E 21.74 | forward P/E 17.22 | P/B 11.80 | PEG 1.00
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: buy (mean 1.97 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 2 strong buy, 15 buy, 11 hold, 1 sell, 0 strong sell
Price target: mean 807.26 (+45.7% vs last close), range 575.00 - 1,027.00
Recent rating changes:
  - 2026-11-10 Evercore ISI Group: main, Outperform -> Outperform
  - 2026-11-02 Freedom Broker: main, Buy -> Buy
  - 2026-11-02 DA Davidson: main, Neutral -> Neutral
  - 2026-10-30 JP Morgan: main, Overweight -> Overweight
  - 2026-10-30 Citigroup: main, Buy -> Buy
  - 2026-10-30 Wells Fargo: main, Overweight -> Overweight
Institutional ownership: 74.1%
Largest holders: Blackrock Inc. (8.2%), State Street Corporation (7.5%), Vanguard Capital Management LLC (6.6%), State Farm Mutual Automobile Insurance Co (3.1%), Vanguard Portfolio Management LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Teva Pharmaceutical (TEVA) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: settlement of a price‑fixing lawsuit (uncertain impact) and Argus Research price‑target raise are bullish, but weak fundamentals (high trailing P/E, high debt), low trading volume, and insider officer sales are bearish. Overall the evidence is contradictory, leading to a neutral stance with low conviction.

**Main reasons it gave:**
- Settlement of generic drug price‑fixing lawsuit (material catalyst, impact uncertain)
- Argus Research raised price target to $50 (positive analyst view)
- Trailing P/E 99.73 and debt/equity 212.9% indicate weak fundamentals
- Trading volume 0.03× 20‑day average suggests low technical participation
- Multiple insider officers sold shares (weak insider signal)

<details><summary><b>News</b> — score -0.10</summary>

- [Teva Pharmaceutical Industries (TEVA) Stock Forecasts](https://finance.yahoo.com/research/reports/ARGUS_3576_AnalystReport_1794917591000)  
  <sub>22 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [Teva Inks Settlement in States’ Generic Drug Price-Fixing Suit](https://news.bloomberglaw.com/antitrust/teva-inks-settlement-in-states-generic-drug-price-fixing-suit)  
  <sub>17 hours ago</sub>  
  Teva Pharmaceutical Industries Ltd. and its Actavis subsidiary reached an agreement in principle to settle claims in a sprawling generic drug price-fixing...
- [Understanding the Setup: (TEVA) and Scalable Risk](https://www.google.com/goto?url=CAESvAEBxCJF12nYMADLny4c72IHmDcAKRvDyXzI3nfC2jdtYxlHLF1usi8b7zUMGFbYmoPLD50NWm4JV0PiczXZ5vyv2vTlzX8v8z_Gl6kmPEMIBkzBWWc8r3Qws2blFFsqg8uc1V6IgsPoMx_WR83TFZFnlEPRH6Bmy306JdaC3KA72MIDDBXZo3VO7znzkbuHcvk9hJNS3VN46JTYYxi_TVd9eZsSAiwCcw3B-860p6IBWZlvOg3yqNwck4NGQA&gsessionid=reyTi5CAZtHRj3656PNKV2EOIclH3JEbFqtpqKRLI5DQuJcFzu4ZDA)  
  <sub>8 hours ago</sub>  
  Price-action only: Teva Pharmaceutical Industries Limited American Depositary Shares (TEVA) movements set the tone for institutional models.
- [TEVA Nov 2026 36.000 call (TEVA261120C00036000) interactive stock chart](https://www.google.com/goto?url=CAESegHEIkXXoQMxqwzOH1TLdIyMrIFG4BC222JnUPxmaxspIJnx1e_3b24WVSldmolHftb1g3kszIICpCZcRgG6zlfrk60sXY25jZE3cl4Y5V-_CWliA9A7JtKYfFZmhlkvIBoutLayiBuWDUARbfBXlBoQaqqxCxc0YgSO&gsessionid=reyTi5CAZtHRj3656PNKV2EOIclH3JEbFqtpqKRLI5DQuJcFzu4ZDA)  
  <sub>15 hours ago</sub>  
  Interactive chart for TEVA Nov 2026 36.000 call (TEVA261120C00036000) – analyse all of the data with a huge range of indicators.
- [David Einhorn Bets on Aluminum in Q3: Here Are His New Stock Picks, Fund Changes](https://www.google.com/goto?url=CAESxwEBxCJF1yaFTZSS4KPUorpuG_upkpTzb2dX8_KvMF9yfhfizcPWVJsSIwwrRk9pyiYx79uMgbfh9IiyY2EuiQAIE-AeOyoWI5fhW4i_zr4Oo5arhGqpRBBLNdU08uCdxNeo9JcYFHIMv1LtSiHeN6fKRw2cLTuksvVNJ3pRQ1i5OifPtoBQdikSQN_kFyc8agDkz9QUaRYKIG2n1re5zcHFqkbWYDzoBjP2uoQhJInHaAw33qaX59WtiwjDziP4Uo0SMaGS-tEG&gsessionid=reyTi5CAZtHRj3656PNKV2EOIclH3JEbFqtpqKRLI5DQuJcFzu4ZDA)  
  <sub>22 hours ago</sub>  
  DME Capital Management LP, founded and led by well-known investor David Einhorn, unveiled its newest third-quarter stock positions and fund changes on...
- [Deckers Outdoor Corporation (DECK) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZQHEIkXXZb4qdB4EEdUvPL_3Idnoh_eruxOftJhUAz_J0nWbfRisFa1v8OkGLlaYcOeLN9pcGSuzltkAngZrr7vCA8dsBCKXPB1C7TGLpJ5-tuyQ60zjsA2mvqf8dpIzcEbS08Q8&gsessionid=reyTi5CAZtHRj3656PNKV2EOIclH3JEbFqtpqKRLI5DQuJcFzu4ZDA)  
  <sub>16 hours ago</sub>  
  Find the latest Deckers Outdoor Corporation (DECK) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Argus Research maintains Teva Pharmaceutical Indus at Buy, raises price target to $50 from $42](https://www.google.com/goto?url=CAES1wEBxCJF13V8y6m_V6TvZ3xg0L4V3494mnmqE5FLnadjpSFRKVphrgif_S8ph6L2HMZkARoyz7BvsxOI1CdmYvYqUhwzgsR_0-dj7QYv1-bfIeo32xYSlOk8CPq_JqUfJFOK5CPeM3gtij2krLW2wWKV48WO6t-VcaQppkb_XpeJXZFevar-p62HOb4QhVHm3i_p1H0pLShTMPsAkla2xTYtoyQ0NOpK_TEk3D5QSgekW51K4LESNMdDv4BPDfDgNQgcg5ZVJazSFFZOD9iuwmita69pa4h7hA&gsessionid=reyTi5CAZtHRj3656PNKV2EOIclH3JEbFqtpqKRLI5DQuJcFzu4ZDA)  
  <sub>22 hours ago</sub>  
  Argus Research maintained Teva Pharmaceutical Indus at Buy and raised its price target to $50 from $42, a 19.0% increase.The price target implies a downside...
- [Teva Pharmaceutical Industries (NYSE:TEVA) Given New $50.00 Price Target at Argus](https://www.google.com/goto?url=CAESyQEBxCJF1zr77kT-qkwSyrURcAnVQjb35x2OJC_wAB2BXaDaGHhXxePb-wBxQfyzooaRUdK6s8WdpYOhOedR1MoJVRXuZ8GoDpgptAuWfRCcOTyS1w1ek5TQ9Q_nM_PhmXfWdo6CZ5z0gSO3jstsxHtfD1SFLTzJky4x6EsWy8azGZtZb3GGOq2_GFmlcjlEJH1XyRjiZnxwQcvIJZg6yr7uTFgCtxW-ffXsPdpGoDXer2AbRStdORIdfaJjAFIEj9NvPLTHWcZnBV4&gsessionid=reyTi5CAZtHRj3656PNKV2EOIclH3JEbFqtpqKRLI5DQuJcFzu4ZDA)  
  <sub>22 hours ago</sub>  
  Argus raised their price objective on Teva Pharmaceutical Industries from $42.00 to $50.00 and gave the company a "buy" rating in a research note on...
- [Israel stocks higher at close of trade; TA 35 up 0.08%](https://www.google.com/goto?url=CAESqQEBxCJF18D_06rm5ffZgeLYfLrBhbkbaxABuqiesKZvqQ-XrnxMn6Be7Y9gAPQyYAzeO5uZl1Ncd5wFXBcP2gaLUP8aYtya7pb9pV2Ogc0GdM09GGzwWhoksOlFVAjnWmP0fW5yxp72ApLIUliqxzTYnOyb90Wc6jP4jHEogN80QPVoqvxuq8erKtSk3guK0Ds12Xk0-umNcaitrNJYng6erth0D3efdKyz&gsessionid=reyTi5CAZtHRj3656PNKV2EOIclH3JEbFqtpqKRLI5DQuJcFzu4ZDA)  
  <sub>23 hours ago</sub>  
  Investing.com – Israel stocks were higher after the close on Tuesday, as gains in the Oil & Gas, Banking and Communication sectors led shares higher.
- [Tue: Elbit stands out on flat TASE](https://www.google.com/goto?url=CAESjAEBxCJF15d-VncwNbethCauvV7klS__i9AAlgOWroJ3dh5JzV7-F82DHU5Y8E3t6Zwx0uqp7sgbUYQ7Qd_ZAZmFLe_dapkKYQ4kmNfwsPDYjD5zLthqgVo8bn-6-tVPHFK2QyCr3NRLgW5-EIdu7QbUQ-MyXneO8RrhYpEE5xamWP8lCe3vCZsd0kzfOQ&gsessionid=reyTi5CAZtHRj3656PNKV2EOIclH3JEbFqtpqKRLI5DQuJcFzu4ZDA)  
  <sub>21 hours ago</sub>  
  Elbit Systems and Navitas led the gains today as Teva lost ground.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 42.88 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 41.86 (+2.5%), 50d 40.55 (+5.8%), 200d 35.21 (+21.8%); 50d above 200d
Momentum: RSI(14) 57.1 | MACD 0.832 vs signal 0.830 (histogram 0.002)
Returns: 1d +0.6% | 5d -0.8% | 1m +5.0% | 3m +16.5%
52-week range: 24.21 - 44.50 (now 92.0% of the way up)
Volatility: ATR(14) 1.21 (2.8% of price) | annualised 20d 32.1%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.50</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 50.04B
Valuation: trailing P/E 99.73 | forward P/E 13.72 | P/B 6.27 | PEG 1.03
Profitability: profit margin 2.9% | operating margin 19.8% | ROE 6.7%
Growth (YoY): revenue -1.9% | earnings -46.0%
Balance sheet: debt/equity 212.9% | free cash flow 1.49B
Risk: beta 0.84 | short interest 2.4% of float
Next earnings: 2027-01-27
```

</details>

<details><summary><b>What this fund holds</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.50</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-09-30 beat by 15% | 2026-06-30 missed by 92% | 2026-03-31 beat by 9% | 2025-12-31 beat by 39%
```

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: buy (mean 1.53 on a 1=strong buy to 5=strong sell scale, 14 analysts)
Ratings: 4 strong buy, 9 buy, 2 hold, 0 sell, 0 strong sell
Price target: mean 50.29 (+17.3% vs last close), range 42.12 - 57.00
Recent rating changes:
  - 2026-11-12 Piper Sandler: main, Overweight -> Overweight
  - 2026-11-05 Leerink Partners: main, Outperform -> Outperform
  - 2026-11-04 TD Cowen: main, Buy -> Buy
  - 2026-11-04 HC Wainwright & Co.: main, Buy -> Buy
  - 2026-11-02 HC Wainwright & Co.: init, ? -> Buy
  - 2026-10-15 Barclays: main, Overweight -> Overweight
Institutional ownership: 69.3%
Largest holders: Blackrock Inc. (5.4%), Phoenix Financial Ltd. (3.6%), WCM Investment Management, LLC (3.6%), Clal Insurance Enterprises Holdings Ltd (3.6%), Migdal Insurance & Financial Holdings Ltd. (3.4%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

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

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

_Not available today._

</details>

### ASML (ASML) · Company — NEUTRAL, confidence 0.30

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The short‑term technicals are bearish (price well below key moving averages and RSI 34.5), while fundamentals, earnings record and analyst consensus are strongly bullish. No insider buying activity and only generic news leave the short‑term outlook ambiguous, leading to a neutral stance with low conviction.

**Main reasons it gave:**
- Price 1,378.03 below 20‑day SMA (1,516.75) and RSI 34.5 (bearish technicals)
- Trailing P/E 33.9, forward P/E 21.7, profit margin 34.1% (strong fundamentals)
- Analyst consensus strong buy, mean price target $2,104.65 (+52.7% vs close) (bullish view)
- No insider purchases in last 180 days (neutral insider activity)

<details><summary><b>News</b> — score +0.00</summary>

- [Is ASML Holding (NasdaqGS:ASML) Getting Too Pricey For Its Cash Flow?](https://finance.yahoo.com/markets/stocks/articles/asml-holding-nasdaqgs-asml-getting-121213477.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  ASML Holding has delivered a powerful long term share price run, yet the recent pullback raises a sharper question for you as an investor: how much of...
- [ASML Holding N.V. (ASML) is Attracting Investor Attention: Here is What You Should Know](https://finance.yahoo.com/markets/stocks/articles/asml-holding-n-v-asml-130005912.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Zacks.com users have recently been watching ASML (ASML) quite a bit. Thus, it is worth knowing the facts that could determine the stock's prospects.
- [ASML261120C01675000 Interactive Stock Chart | ASML Nov 2026 1675.000 call Stock](https://www.google.com/goto?url=CAESbwHEIkXX1nlFeAS5EbbzlcT1adVT_5gsMu0hQikCiaZE_LKmU_xIJnJq-Dix7zt2CIBWIZ3arJxl0HtpA1RtzY_ROdHEFyT99lhUNYJd9C29QF0r5G7V_bb5AhAvBe14rYhQGmvjvt0zDkw04oLPig&gsessionid=tBQVllEPqplVCxFt9RhsHHkhDigtmWQeiZJNCzQ_kFNuxCczfxmqRA)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [ASML Nov 2026 1670.000 put (ASML261120P01670000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScwHEIkXXiEob7EXixRpOAw3e__6G5gtqGG80npOlzF0EJxLA0kPvQCksTSC_Y03NFvoI2Y2vEZQW3cezq7M-i1Sve8rg5cM4VJyYtSLdKZZ1f2YHoMY36mLmIUa2eNw_NPzk91Vs3La3Dwe9pKwd32aYJlw&gsessionid=tBQVllEPqplVCxFt9RhsHHkhDigtmWQeiZJNCzQ_kFNuxCczfxmqRA)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest ASML Nov 2026 1670.000 put (ASML261120P01670000) stock quote, history, news and other vital information to help you with your stock trading...
- [ASML261120P02740000 Interactive Stock Chart | ASML Nov 2026 2740.000 put Stock](https://www.google.com/goto?url=CAESbwHEIkXXtt6YTZSAuAHwFOUWXsyvdE0vyhN7K8ig7DsSPA3jrf9CZcQqBq4UXPaR8eVknaUNWSDmHvifXmQxAxKx9JSvVlx0_4wr9u1yvgpnakOwIgpGnXFLmzYZyQtRFJP8e2VZ7gVT9FBH3J7Nag&gsessionid=tBQVllEPqplVCxFt9RhsHHkhDigtmWQeiZJNCzQ_kFNuxCczfxmqRA)  
  <sub>Yahoo Finance, 10 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [ASML Nov 2026 1665.000 call (ASML261120C01665000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScwHEIkXXGKEPGKk7NTBlRvPkGbk5alinLYLDPH7F12vjTpbbhdST06VXuBBDQULB2Dqtg-EXzxcaW9VDFhcddp81pBhqjHgd831PhXUZSLcHF1Ixo9SGyP4LxNz8ZxC9yRhWfPqH6_ZNQnTYn_ldywPIbRk&gsessionid=tBQVllEPqplVCxFt9RhsHHkhDigtmWQeiZJNCzQ_kFNuxCczfxmqRA)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Find the latest ASML Nov 2026 1665.000 call (ASML261120C01665000) stock quote, history, news and other vital information to help you with your stock trading...
- [ASML Nov 2026 580.000 call (ASML261120C00580000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXxzjJ1_hDy6pwCZ6fO_G8pR-BymNkdZEiBPkweYPPfH5BYdxH3RLLDb59vAWCZjwxC28h-mGLLdCmzb-2eAB1CQQXCvpu7SvKUiDUsQ5Xe5wsgvNvdFjG85_uqd-mfdxxDLTQs-Sg2A5bl5HYwRY&gsessionid=tBQVllEPqplVCxFt9RhsHHkhDigtmWQeiZJNCzQ_kFNuxCczfxmqRA)  
  <sub>Yahoo Finance UK, 6 hours ago</sub>  
  Find the latest ASML Nov 2026 580.000 call (ASML261120C00580000) stock quote, history, news and other vital information to help you with your stock trading...
- [ASML261120C01405000 Interactive Stock Chart | ASML Nov 2026 1405.000 call Stock](https://www.google.com/goto?url=CAESbwHEIkXXxCdI5Atn58FZu5vfC-e--_5CrYDMab1WPWa0VPE9zwKRPxFHXXZd2Xlh73iBjJO0tFetub8oVk-mM8m0CrXj3R17UWSqfBoer4KZcQmhkC-yAP3MHnApJlyBH4w7lsRLI4pTaXrKIrWyvg&gsessionid=tBQVllEPqplVCxFt9RhsHHkhDigtmWQeiZJNCzQ_kFNuxCczfxmqRA)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [ASML Nov 2026 1370.000 put (ASML261120P01370000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXcxwxT1FfVrI0OnP9S1Spf5Ab8wH6PM5aL0-AaT6qpssp93YAFi3_rJuN2HnfT_OkR7G7fVuq452vFcCuy8j-3Z9OdSIBeXy5XasXbK5jm84LMO_zYj9f27oryeGVQ2eOf7vjCYQQnzOoo7fTWfc&gsessionid=tBQVllEPqplVCxFt9RhsHHkhDigtmWQeiZJNCzQ_kFNuxCczfxmqRA)  
  <sub>Yahoo Finance UK, 10 hours ago</sub>  
  Find the latest ASML Nov 2026 1370.000 put (ASML261120P01370000) stock quote, history, news and other vital information to help you with your stock trading...
- [ASML Nov 2026 1655.000 call (ASML261120C01655000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXoDfMk_f5bGIRbELbNuUh8pCJx6UfudTPlNrAx0yCNaPZBac1a-S_SYqiV6pgb0JVQFspZnjpBZ-UOq9qIsAjliwr38k2P7HcmULQJ6m4gVta0P1iWA-lS72FcIiAWmGOcrtnFhkQBkob8keXI5w&gsessionid=tBQVllEPqplVCxFt9RhsHHkhDigtmWQeiZJNCzQ_kFNuxCczfxmqRA)  
  <sub>Yahoo Finance UK, 16 hours ago</sub>  
  Find the latest ASML Nov 2026 1655.000 call (ASML261120C01655000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 1,378.03 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 1,516.75 (-9.1%), 50d 1,639.67 (-16.0%), 200d 1,601.75 (-14.0%); 50d above 200d
Momentum: RSI(14) 34.5 | MACD -69.178 vs signal -60.548 (histogram -8.629)
Returns: 1d -0.4% | 5d -10.2% | 1m -15.5% | 3m -21.3%
52-week range: 966.57 - 1,989.44 (now 40.2% of the way up)
Volatility: ATR(14) 63.96 (4.6% of price) | annualised 20d 63.9%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.70</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 531.29B
Valuation: trailing P/E 33.92 | forward P/E 21.74 | P/B 1,183.62 | PEG 0.75
Profitability: profit margin 34.1% | operating margin 38.6% | ROE 65.6%
Growth (YoY): revenue +55.2% | earnings +135.9%
Balance sheet: debt/equity 8.9% | free cash flow 10.37B
Risk: beta 1.33 | short interest 0.3% of float
Next earnings: 2027-01-27
```

</details>

<details><summary><b>What this fund holds</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.70</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-09-30 beat by 17% | 2026-06-30 beat by 9% | 2026-03-31 beat by 7% | 2025-12-31 missed by 5%
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
Consensus: strong_buy (mean 1.37 on a 1=strong buy to 5=strong sell scale, 17 analysts)
Ratings: 7 strong buy, 31 buy, 2 hold, 1 sell, 0 strong sell
Price target: mean 2,104.65 (+52.7% vs last close), range 848.94 - 2,788.72
Recent rating changes:
  - 2026-10-15 JP Morgan: main, Overweight -> Overweight
  - 2026-07-16 JP Morgan: main, Overweight -> Overweight
  - 2026-07-16 Wells Fargo: main, Overweight -> Overweight
  - 2026-07-16 RBC Capital: main, Outperform -> Outperform
  - 2026-07-14 RBC Capital: main, Outperform -> Outperform
  - 2026-07-06 Bernstein: main, Outperform -> Outperform
Institutional ownership: 19.8%
Largest holders: FMR, LLC (1.5%), Fisher Asset Management, LLC (1.2%), Capital World Investors (0.9%), Invesco Ltd. (0.7%), State Farm Mutual Automobile Insurance Co (0.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

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

### Alphabet (Google) (GOOGL) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [RDDT vs. GOOGL: Which digital advertising stock has an edge right now?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afdb95a77d7460fbc915a11d81bb9f6&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2fgeneral%2frddt-vs-googl-which-digital-advertising-stock-has-an-edge-right-now%2far-AA2hDkJJ&c=11676980740469910075&mkt=en-us)  
  <sub>Zacks Investment Research on MSN, 31h ago</sub>  
  Reddit RDDT and Alphabet GOOGL are major players in the digital advertising space. While Reddit is an emerging social media platform gaining traction with community-driven advertising, Alphabet ...
- [Alphabet stock is down 25% from its high. History suggests a $5,000 investment now will be worth this much by 2028.](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afdb95a77d7460fbc915a11d81bb9f6&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2ftechnology%2falphabet-stock-is-down-25-from-its-high-history-suggests-a-5-000-investment-now-will-be-worth-this-much-by-2028%2far-AA2hGqrb&c=1143329808105257223&mkt=en-us)  
  <sub>The Motley Fool on MSN, 13h ago</sub>  
  Alphabet's stock has sold off due to long-term investments.
- [Stanley Druckenmiller Dumped AMD and Alphabet. His Next 3 AI Bets May Surprise Investors](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afdb95a77d7460fbc915a11d81bb9f6&url=https%3a%2f%2f247wallst.com%2finvesting%2f2026%2f11%2f17%2fstanley-druckenmiller-dumped-amd-and-alphabet-his-next-3-ai-bets-may-surprise-investors%2f&c=9707487326507368970&mkt=en-us)  
  <sub>24/7 Wall St., 30h ago</sub>  
  Stanley Druckenmiller walked away from two fast-growing AI giants, yet he did not walk away from AI. His latest 13F reveals where the money went instead, and the new picks tell a different story about ...
- [Alphabet Inc Class A (GOOGL)](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afdb95a77d7460fbc915a11d81bb9f6&url=https%3a%2f%2fwww.fidelity.co.uk%2ffactsheet-data%2ffactsheet%2fUS02079K3059-alphabet-inc%2fkey-statistics&c=6276737704724218234&mkt=en-us)  
  <sub>Fidelity International, 17h ago</sub>  
  Alphabet is a holding company that wholly owns internet giant Google. The California-based company derives slightly more than three-fourths of its revenue from Google services, the vast majority of ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 282.15 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 294.76 (-4.3%), 50d 324.96 (-13.2%), 200d 337.60 (-16.4%); 50d below 200d
Momentum: RSI(14) 34.7 | MACD -12.295 vs signal -12.974 (histogram 0.679)
Returns: 1d +0.7% | 5d -3.9% | 1m -17.1% | 3m -17.2%
52-week range: 273.50 - 402.62 (now 6.7% of the way up)
Volatility: ATR(14) 9.74 (3.5% of price) | annualised 20d 52.7%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 3.47T
Valuation: trailing P/E 14.73 | forward P/E 18.61 | P/B 5.26 | PEG 0.99
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
Price target: mean 400.37 (+41.9% vs last close), range 300.00 - 500.00
Recent rating changes:
  - 2026-11-02 Wells Fargo: main, Overweight -> Overweight
  - 2026-10-30 Citigroup: main, Buy -> Buy
  - 2026-10-30 Wells Fargo: main, Overweight -> Overweight
  - 2026-10-29 Bernstein: main, Market Perform -> Market Perform
  - 2026-10-29 RBC Capital: main, Outperform -> Outperform
  - 2026-10-29 UBS: main, Neutral -> Neutral
Institutional ownership: 80.7%
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

- [Stock options and units at HDFC Bank (HDB) each vest in four stages.](https://www.stocktitan.net/sec-filings/HDB/6-k-hdfc-bank-ltd-current-report-foreign-issuer-c4bee4255667.html)  
  <sub>Stock Titan, 4 hours ago</sub>  
  HDFC Bank Limited (HDB) reported that its Governance, Nomination and Remuneration Committee granted options under Employees' Stock Option Scheme (ESOS) Plan...
- [HDFC Bank Grants Stock Options and Restricted Stock Units](https://www.tipranks.com/news/company-announcements/hdfc-bank-grants-stock-options-and-restricted-stock-units)  
  <sub>TipRanks, 3 hours ago</sub>  
  The latest announcement is out from Hdfc Bank ( ($HDB) ). On November 17, 2026, HDFC Bank's Governance, Nomination and Remuneration Committee granted 186031...
- [HDB Financial Servic Investor Analysis | StockIQ](https://www.google.com/goto?url=CAESmwEBxCJF143MVs3uFMkPBQubeLik8q-BuYXKdMb_qz6uzGf2t9fBVEis4zPaDsPVVhdXkWoJzWF2fMy6SAENUIM8x00OfDfYbeqQU0P6BJtcatefHjyMMkEQD6VNuzu_LUV-w1_-2vxaMmEIUsQ8Wfbx-kOFGY2bqfBKwR4w3FaMZM_NHli50shtFIML8-qaEstXEXRKlsTcRidGkg&gsessionid=qXf_ejgRqBoyiT0DDYWRykVxla6OM5EnE8GuUJUZmwS7kZ9vbwSGlw)  
  <sub>The Economic Times, 23 hours ago</sub>  
  Explore HDB Financial Servic investor analysis with StockIQ. Get AI scores, financial health insights, investment risks and management commentary.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 26.07 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 24.05 (+8.4%), 50d 23.27 (+12.0%), 200d 25.33 (+2.9%); 50d below 200d
Momentum: RSI(14) 70.1 | MACD 0.960 vs signal 0.735 (histogram 0.225)
Returns: 1d -0.7% | 5d +0.2% | 1m +13.1% | 3m +11.7%
52-week range: 21.36 - 37.13 (now 29.9% of the way up)
Volatility: ATR(14) 0.56 (2.2% of price) | annualised 20d 28.5%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 134.12B
Valuation: trailing P/E 16.82 | forward P/E 18.83 | P/B 10.38 | PEG n/a
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
Price target: mean 30.30 (+16.2% vs last close), range 26.20 - 33.00
Recent rating changes:
  - 2024-07-22 JP Morgan: down, Overweight -> Neutral
  - 2019-09-09 Bernstein: down, Outperform -> Market Perform
  - 2019-06-11 Nomura: down, Buy -> Neutral
  - 2017-03-21 Morgan Stanley: down, Overweight -> Equal-Weight
  - 2016-09-14 Goldman Sachs: main, ? -> Buy
  - 2015-03-11 Societe Generale: init, ? -> Buy
Institutional ownership: 14.1%
Largest holders: Morgan Stanley (1.1%), Royal Bank of Canada (0.8%), JPMORGAN CHASE & CO (0.7%), Schroder Investment Management Group (0.4%), Temasek Holdings (Private) Ltd (0.4%)
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

- [MercadoLibre, Inc. (MELI.VI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/MELI.VI/)  
  <sub>16 hours ago</sub>  
  Valuation Measures · Market Cap. 67.24B · Enterprise Value. 75.16B · Trailing P/E. 41.67 · Forward P/E. 26.81 · PEG Ratio (current). 0.47 · Price/Sales (ttm).
- [MELI Nov 2026 2460.000 put (MELI261120P02460000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/MELI261120P02460000/chart/)  
  <sub>4 hours ago</sub>  
  Interactive Chart for MELI Nov 2026 2460.000 put (MELI261120P02460000), analyze all the data with a huge range of indicators.
- [MELI Dec 2026 1920.000 call (MELI261204C01920000) stock price, news, quote and history](https://www.google.com/goto?url=CAESdAHEIkXX0P4e088KrQpDYHY_0k-wzzj0nsRt1tZrx3C4qy3G_5FZuMOfoWh9HVGtwA46EWqts7C3R9DxcO4iO3jePmivfDn1M-TRdAstR8Al_AyxKdPbDNMc0Nho_SqbPjDI729lMvdv7bX2T_rmjhwY302p&gsessionid=rZH9GtVlKN4o1Xq-kASIAm4qqfDNKx5rEIa2whaKGVV7KphoIWJpjQ)  
  <sub>7 hours ago</sub>  
  Find the latest MELI Dec 2026 1920.000 call (MELI261204C01920000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI Mar 2027 2240.000 call (MELI270319C02240000) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESegHEIkXXFHArKu16se3LYIVAZfwCGPD2kObmZ6nkoOwdlSS4XPM9aKEOMysZI1ipr9yCMeEyWqp5q8RfFMStyRrxGb-L2KoQs6vUva3jlLQUeO2Uyp9jfb36pQ3JxkdsW4TN87rl2kbPkaU-LpmZVwjR_h72NtyEyV6q&gsessionid=rZH9GtVlKN4o1Xq-kASIAm4qqfDNKx5rEIa2whaKGVV7KphoIWJpjQ)  
  <sub>6 hours ago</sub>  
  Interactive Chart for MELI Mar 2027 2240.000 call (MELI270319C02240000), analyze all the data with a huge range of indicators.
- [MELI261127C01890000 Interactive Stock Chart | MELI Nov 2026 1890.000 call Stock](https://www.google.com/goto?url=CAEScAHEIkXXbBI99wb59f95kuDyp2XD1WAXykZsKn2ykvpaxrg8f2j0oQnTt0Yn_m7AUGX_IS_V3ymME1Mv13Gb5vJbAIVT38BSRS89HJDhK_VGkaZV5Tt1PlISxgCt26sWfCn9Z1R9YaHqQLYSuky-q3E&gsessionid=rZH9GtVlKN4o1Xq-kASIAm4qqfDNKx5rEIa2whaKGVV7KphoIWJpjQ)  
  <sub>18 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [MELI Mar 2027 1160.000 put (MELI270319P01160000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESdAHEIkXXRD_sIuJyFkpPZdR6nkObD8KEhuuxrLBf4pdbUO4GhGCh2GCSykgmjolgpizrP-0z_MGK8z6cxzr0xd8MuYw0OwCmoILRyVtuYXx-eBsh85NrCGl3pSipxOJ8vVqYKqdfrvWcB6AREXsMir7gHoU3&gsessionid=rZH9GtVlKN4o1Xq-kASIAm4qqfDNKx5rEIa2whaKGVV7KphoIWJpjQ)  
  <sub>13 hours ago</sub>  
  Find the latest MELI Mar 2027 1160.000 put (MELI270319P01160000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI Dec 2026 1360.000 put (MELI261204P01360000) Interactive Stock Chart](https://www.google.com/goto?url=CAESegHEIkXX4VzU6wyFJuO9FOuNI3QSsRzt8PMSQhaCtphrRcku20eRQLz1isMeKw-9DHFAZjKQGNujqjitwr1GGN-JCLqpYqcwHYpJenvSHCO6ZkhnIBenGr0_AwzznQ88m_soiQUTPkVPC0D0ui__pjEY7Gz6cAobYyzz&gsessionid=rZH9GtVlKN4o1Xq-kASIAm4qqfDNKx5rEIa2whaKGVV7KphoIWJpjQ)  
  <sub>13 hours ago</sub>  
  Interactive Chart for MELI Dec 2026 1360.000 put (MELI261204P01360000), analyze all the data with a huge range of indicators.
- [MELI Nov 2026 1530.000 put (MELI261120P01530000) interactive stock chart](https://www.google.com/goto?url=CAESegHEIkXXWr2joIYg-pj2s5Fb3pomg77RV7hzKMSGaNlpai7Hgs6CkjuJ9rj3m6SDl4gtBT7Flf-9iy5M_MmyWYf6A3eg1RsuDOy8iKrP7j0zynZTYRUfOPlCLoA6XjBCioHR-8Lqvsmb81TF3VykkHircnZrLFRlDTMD&gsessionid=rZH9GtVlKN4o1Xq-kASIAm4qqfDNKx5rEIa2whaKGVV7KphoIWJpjQ)  
  <sub>16 hours ago</sub>  
  Interactive chart for MELI Nov 2026 1530.000 put (MELI261120P01530000) – analyse all of the data with a huge range of indicators.
- [MELI Nov 2026 1505.000 call (MELI261120C01505000) stock price, news, quote and history](https://www.google.com/goto?url=CAESdAHEIkXX4HpwTwvwWvREa8oif75DtVRKEP1dZ7OHiwtPBr4PUghiZCUIpYISjzTj53ilwBFyx-dH7FuGSQNUX76DoV0mfX2YsSEaXRQ9WWbXoaCQmJBZ8gfaVpos0ZKmJw1TTfj2f4wrAXRbzfCMV7p1prfi&gsessionid=rZH9GtVlKN4o1Xq-kASIAm4qqfDNKx5rEIa2whaKGVV7KphoIWJpjQ)  
  <sub>17 hours ago</sub>  
  Find the latest MELI Nov 2026 1505.000 call (MELI261120C01505000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI Dec 2026 1420.000 put (MELI261204P01420000) stock price, news, quote and history](https://www.google.com/goto?url=CAESdAHEIkXXXhS5laVi0LofjWBzFRG4oTZ-uFwv9OaIEGoxC3VLVy9M77ICAe3TxFkziCu7YK90nBZYKe-vIizlwnKAwrDeMYkfGXeX3_Tt7ptF7_yviFGi0_7eBkP43tE5ke-1Ito2SZq0topLywYrHXxhbW-w&gsessionid=rZH9GtVlKN4o1Xq-kASIAm4qqfDNKx5rEIa2whaKGVV7KphoIWJpjQ)  
  <sub>18 hours ago</sub>  
  Find the latest MELI Dec 2026 1420.000 put (MELI261204P01420000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,441.07 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 1,595.14 (-9.7%), 50d 1,731.98 (-16.8%), 200d 1,773.39 (-18.7%); 50d below 200d
Momentum: RSI(14) 30.9 | MACD -91.437 vs signal -79.253 (histogram -12.184)
Returns: 1d +0.3% | 5d -4.7% | 1m -23.3% | 3m -25.0%
52-week range: 1,436.83 - 2,295.00 (now 0.5% of the way up)
Volatility: ATR(14) 59.64 (4.1% of price) | annualised 20d 57.4%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 73.06B
Valuation: trailing P/E 38.66 | forward P/E 27.21 | P/B 8.91 | PEG 0.78
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
Price target: mean 2,194.30 (+52.3% vs last close), range 1,600.00 - 2,800.00
Recent rating changes:
  - 2026-11-11 UBS: main, Neutral -> Neutral
  - 2026-11-09 JP Morgan: main, Neutral -> Neutral
  - 2026-11-05 Scotiabank: main, Sector Outperform -> Sector Outperform
  - 2026-11-05 StoneX: main, Buy -> Buy
  - 2026-11-05 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-11-05 BTIG: main, Buy -> Buy
Institutional ownership: 81.2%
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

### Nvidia (NVDA) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Nvidia Is in Turmoil, But Earnings Are Still Rocketing Higher. Is the Stock a Buy?](https://www.fool.com/investing/2026/11/18/nvidia-is-in-turmoil-but-earnings-are-still-rocketing-higher-is-the-stock-a-buy/)  
  <sub>The Motley Fool, 2 hours ago</sub>  
  Nvidia (NVDA -0.44%) just continued to do something that it's done quarter after quarter in recent years: The tech powerhouse reported earnings that beat...
- [Dear Nvidia Stock Fans, Mark Your Calendars for December 10](https://www.barchart.com/story/news/8894753/dear-nvidia-stock-fans-mark-your-calendars-for-december-10)  
  <sub>Barchart.com, 2 hours ago</sub>  
  Nvidia stock faces earnings on Nov. 17 and Senate hearings on Dec. 3 and Dec. 10. See why Lutnick's testimony could shape what happens next for NVDA stock.
- [NVIDIA Shares Jump 3.13% in Premarket Trading - NVIDIA (NASDAQ:NVDA)](https://www.google.com/goto?url=CAESpAEBxCJF1wgbtmKe4MFmuLRzQFTPRUarn4z4n__G9S1RvwCyvdZZxI97GzE_9vKXYoHyYPIUoi5pUmTUABscBpcbvoQEoC_IdtNwWR-Nf5wW8frPaU63Dva5sDKBND0mcegQWlxBrgVGmCkEca-BoBk3VpVaz40_fKbS5vDFsafRrZVYsVFoDSlHCBEBliqwwdopSeWaoB6dvETkgjulpvDWhVRYCA&gsessionid=V_aUZoxgCcT9PI3G2mMuyyRemxn3jG8im51qIMJ8pHU-fJ3UFMN85w)  
  <sub>Benzinga, 5 hours ago</sub>  
  NVIDIA shares gained 3.13% in premarket trading as strong quarterly results, an earnings beat and upbeat revenue guidance lifted sentiment.
- [Nvidia Chaos Is the Perfect Setup for Anthropic IPO](https://www.google.com/goto?url=CAESiAEBxCJF1_KfwIDnRCvtqof-CeIqW6FQ_x1Y23LE0rcz1ynmI7yBLKSWM6v6NfdtDWMnRiRw4wRxh1t9EQlWzKQiwPBE0t3BkxzHj1HGp-xAHplqMOgfR4FrDGlg9EuFQo0PkwFKIIp8jCqFynLB5KtELwofTIZUQtiVqvHUz1RMuqm145oK3PLv&gsessionid=V_aUZoxgCcT9PI3G2mMuyyRemxn3jG8im51qIMJ8pHU-fJ3UFMN85w)  
  <sub>Barron's, 2 hours ago</sub>  
  Anxiety around Nvidia earnings created the perfect sweet spot for Anthropic's IPO, and more things to know about the stock market today.
- [Nvidia Reports Faster Growth, Says Jensen Huang Won’t Return as CEO](https://www.google.com/goto?url=CAESiwEBxCJF15tgvav_rdRk7Iogw5bXobscN5beTDWvlPFODOsDO5UrkuME4OamVjQDrhRfUzOFVgrgKsvaVGYppSJwtfmzGdnX1UHVBt28YY1AJLDvtubloVdceLihUcVAFvXG3ZDZGEEaWQ5OKoxICHgJxBnKBDqmdFgIA0bb11xXglRSI1OyKlqchXCJ&gsessionid=V_aUZoxgCcT9PI3G2mMuyyRemxn3jG8im51qIMJ8pHU-fJ3UFMN85w)  
  <sub>WSJ, 12 hours ago</sub>  
  In her first earnings call as interim CEO, Colette Kress faced questions over the chipmaker's future without its longtime leader.
- [NVDA Stock Set for a Strong Rebound After Earnings: Can Bulls Take Control?](https://www.google.com/goto?url=CAESswEBxCJF11658_AygE1P_KfvAPxJrAX-9MoxI_T4oEJhteVVspI2vDVi_P_1PtFB8nBg_9JFXXDQ9b6BiKnc90Cku0Z9nKYCBZ2fp2K4BiCydbKvFmxRv6KnQxqGVh8fywKDjreC58_38pYAFFLjV5L63u4J9BmFr816Ag2AUtnhU-POr-Fp0WzhH-iItqlBfX4JPYOHnMoMZ5tvbZgosE5QezH-BmRiK3O311r42xIDeuuodg&gsessionid=V_aUZoxgCcT9PI3G2mMuyyRemxn3jG8im51qIMJ8pHU-fJ3UFMN85w)  
  <sub>Coinpedia, 2 hours ago</sub>  
  NVDA Stock rises 2.5% in premarket after Q3 earnings beat estimates, with revenue up 103% and positive Q4 guidance. Can NVDA extend gains?
- [Nvidia (NVDA) Stock Is Trending In Pre-Market After Q3 Earnings Beat](https://www.google.com/goto?url=CAESugEBxCJF177JpaJZi4JL0V_sERQtDF_pMMKJhFjpGlYBN1CN8DcB5lymivWXEtyj3wtuh7TCQQrF7yD36SIXzZylTysN19wTMmsleBa_r0wiaNeF58OmpKXQX24PDFia-ibanN8XMMfVhKg5wjbBm670Ku-tNkH2VjkWPbWeH6VI-5WNkvbHCkoOE6oZFp41iHLHswMKoxFwRraM3y7Hh-EVfuMNX8r6FuBLtXgNYdSA587c3Kq9U-sVV_g&gsessionid=V_aUZoxgCcT9PI3G2mMuyyRemxn3jG8im51qIMJ8pHU-fJ3UFMN85w)  
  <sub>TradingView, 5 hours ago</sub>  
  Nvidia Corp. NASDAQ:NVDA shares are trending on Wednesday.Shares of the California-based developer of AI and graphics chips gained 3.13% to $160.33 in...
- [The 3 Best AI Stocks to Buy Now (Yes, Nvidia Is One of Them)](https://www.google.com/goto?url=CAESkgEBxCJF1yS7rQL_SyZQ9zi_OwYMRuntRATBk7K-xJ5_XIGco7nYLBO0vGJzeB8G54FPt49_DEiy_evu2F7OkwFv4hxTxgZkaRqnCp6myGJH5kufnBxFIKOPPoHqRBpooEbXsv348-4DZKyQXaG8niiEIRdLIBTaZNQdZzQPxdd5L2U5Wmpd-jZK1JIVU4lKgnViyw&gsessionid=V_aUZoxgCcT9PI3G2mMuyyRemxn3jG8im51qIMJ8pHU-fJ3UFMN85w)  
  <sub>Yahoo Finance, 37 minutes ago</sub>  
  The artificial intelligence sector of the stock market isn't the most popular place to invest right now. There are questions surrounding how the AI...
- [AMD, Broadcom, CoreWeave stocks rise on Nvidia earnings beat](https://www.google.com/goto?url=CAES0QEBxCJF1x4A9QLQNIuZ1_6g7qqfuEGwjApSIMkrp9HLUrAnGfw_zKmKwrNsFv0l4G7foeTVy7Wf_Y4DuwhBRekkifaKx6BR8uB-N0ZLxxtbkaxpg9DalehdwHjXYztwOF5ceJ9N1uuZb_E67VOq83VC0pvNAJKyYyMb6k7N1W63MjFtIdPYL4Q1f_WbGcTjJUYuzlbM_Jc6_havY1ZuXk-qj0xCQZsMGwoMCopXs22iLrKFvzxgvfBOQp2Zd5DkF9rutSi0cKLMN8sNVobkpqrmxA&gsessionid=V_aUZoxgCcT9PI3G2mMuyyRemxn3jG8im51qIMJ8pHU-fJ3UFMN85w)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Semiconductor and neocloud provider stocks rose on Wednesday during premarket trading as AI chip-heavy Nvidia (NVDA) reported Q3 results that beat Wall...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 155.34 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 189.26 (-17.9%), 50d 210.39 (-26.2%), 200d 203.74 (-23.8%); 50d above 200d
Momentum: RSI(14) 22.5 | MACD -16.594 vs signal -13.049 (histogram -3.545)
Returns: 1d -0.1% | 5d -10.6% | 1m -28.2% | 3m -28.4%
52-week range: 155.34 - 239.24 (now 0.0% of the way up)
Volatility: ATR(14) 9.34 (6.0% of price) | annualised 20d 50.7%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 3.75T
Valuation: trailing P/E 19.65 | forward P/E 9.53 | P/B 24.02 | PEG 0.19
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
Consensus: buy (mean 1.69 on a 1=strong buy to 5=strong sell scale, 55 analysts)
Ratings: 11 strong buy, 36 buy, 14 hold, 2 sell, 0 strong sell
Price target: mean 265.23 (+70.7% vs last close), range 130.00 - 515.00
Recent rating changes:
  - 2026-11-12 Melius Research: down, Buy -> Hold
  - 2026-11-12 DA Davidson: main, Buy -> Buy
  - 2026-11-12 Craig-Hallum: down, Buy -> Hold
  - 2026-11-12 B of A Securities: main, Buy -> Buy
  - 2026-11-12 BMO Capital: main, Outperform -> Outperform
  - 2026-11-12 Baird: reit, Neutral -> Neutral
Institutional ownership: 71.4%
Largest holders: Blackrock Inc. (8.1%), Vanguard Capital Management LLC (6.4%), State Street Corporation (4.2%), FMR, LLC (3.9%), Geode Capital Management, LLC (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 2,613,243 shares in 18 transaction(s) | sold 6,198,325 shares in 9
Net: -3,585,082 shares (-0.4% of insider holdings) | insiders hold 972,675,904 shares
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

- [Novo Nordisk (NVO) Could Be 47% Below Fair Value Following Its AI Push](https://finance.yahoo.com/healthcare/articles/novo-nordisk-nvo-could-47-051252677.html)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  Novo Nordisk (NYSE:NVO) is back in focus after its collaboration with Anthropic was highlighted as a driver of AI assisted drug discovery and software...
- [Novo Nordisk (NVO) Stock May Be Undervalued On Raised 2026 Outlook](https://au.finance.yahoo.com/news/novo-nordisk-nvo-stock-may-061727245.html)  
  <sub>Yahoo Finance Australia, 8 hours ago</sub>  
  Novo Nordisk has seen its share price fall 57.9% over the past three years, even as its weight loss franchise remains central to the investment story.
- [NVO280616P00042500 Interactive Stock Chart | NVO Jun 2028 42.500 put Stock](https://www.google.com/goto?url=CAESbwHEIkXXj-zP25JTPCrm_0_ZiQmF9WR4zWjlbK5mBrxa94hDSnjVlT9j6-FV1Huof1ooPUGOSrcFdbpF2veABrOqm6V1KDuEPtSuh8g495iuXIXZLb8nuy07hWYKo_A21zIZQ-SgiunbZ_OH9qkfaA&gsessionid=lG1sc7nYxc9Vo6_tCN-bcGmBkXzPeMAejdKzB-eQiOzRMSiRo3-VPw)  
  <sub>Yahoo Finance, 17 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [NVO Dec 2026 50.000 call (NVO261204C00050000) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXSqRDBVskdbZu32AWprUeNkhOLX-jOAKU-7kEMIwdxQcYVeb15tUmX-r5dsMQm4xuwTojXUpycqT2EsiYL2jAp7-adaMJ_xVAZRlJ73XOSGKiFA_bhzVEVTadrsNR_pKsGev9hAFZOp8bmBKq6cMz8Wksee0&gsessionid=lG1sc7nYxc9Vo6_tCN-bcGmBkXzPeMAejdKzB-eQiOzRMSiRo3-VPw)  
  <sub>Yahoo Finance UK, 10 hours ago</sub>  
  Interactive chart for NVO Dec 2026 50.000 call (NVO261204C00050000) – analyse all of the data with a huge range of indicators.
- [NVO Nov 2026 36.500 call (NVO261120C00036500) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXnvWTKcpNtm1dgHzqEB3Sc_aBWQ0KcPNnOAzKSAMuN2QBQSYH4NQU5V9pFFe7C17PEZZo6LICYoq61t2mWsEaRZTacdSTbdfrZrZ56c_eTzNPwuL-LydlKKX2F8qaBwco399Ht3BDkCqnQWlsOPRHP2OLCtc&gsessionid=lG1sc7nYxc9Vo6_tCN-bcGmBkXzPeMAejdKzB-eQiOzRMSiRo3-VPw)  
  <sub>Yahoo Finance UK, 13 hours ago</sub>  
  Interactive chart for NVO Nov 2026 36.500 call (NVO261120C00036500) – analyse all of the data with a huge range of indicators.
- [Novo Nordisk: The Thesis Is Working, The Stock Just Hasn't Noticed Yet (NYSE:NVO)](https://www.google.com/goto?url=CAESqQEBxCJF1xD8LZD7vCNaAaGQ4xYWzMRQGtD3mdMtLXUsnRkWPY8bVX-Cybl2USHtG_uVcGiOgosiaX6bhb1VfWB5Pz0mcZh6T5T72ED4xVxZK5C6FH9hwh6_f-bnMxTg4lRqMtaLrBADrqUVT2v3JmF5dKKgtsc_lMOaDuhfqw5b7qS14sK2X3Cgq5DVy_0sPpEr7WAu0UNEMmItTsFsnRTt9owlc5EY5Nfc&gsessionid=lG1sc7nYxc9Vo6_tCN-bcGmBkXzPeMAejdKzB-eQiOzRMSiRo3-VPw)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  I retain a Strong Buy on Novo Nordisk: improving cash flow and cost discipline reinforce an inexpensive valuation at 10.89 times non-GAAP earnings. NVO...
- [NVO Dec 2028 42.500 put (NVO281215P00042500) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXo624eDmvFZARYkLy2l2XlFNS5WzesXDD0NA02xITFM6xgsATSEb6-VJda0fana6UOTui9sc5epC7M7qmR2EusFJRpqYRlzN8FNXbf7YhWfTsz4S6krSyEhCnxDgz16J-eLEKKc60UUP4S9fDBlY&gsessionid=lG1sc7nYxc9Vo6_tCN-bcGmBkXzPeMAejdKzB-eQiOzRMSiRo3-VPw)  
  <sub>Yahoo Finance UK, 18 hours ago</sub>  
  Find the latest NVO Dec 2028 42.500 put (NVO281215P00042500) stock quote, history, news and other vital information to help you with your stock trading and...
- [Pfizer: Strong Growth Momentum And Attractive Valuation Support A Strong Buy (NYSE:PFE)](https://www.google.com/goto?url=CAEStwEBxCJF10q8dn9-JDtdLK3-BnboT9UlYpOIB__YgsqRqFTOXezJKkhg6mV01ZsIf-p_hVJ21fu5C4vZdvonJdbzMiJMxF_Iue7LfExmoqypYDaPGOTTM16p9GvZ_axREasj3z_E3G-ioxehJcYBm44CJihmmUmqVnLCsreHqoBObwFhjRwDGoqyvhbO7oaauJezmDQNI0q2_StkemFeg-DeTvfFSeU6NLYMjrRb4B19h2NvQ297Bt4&gsessionid=lG1sc7nYxc9Vo6_tCN-bcGmBkXzPeMAejdKzB-eQiOzRMSiRo3-VPw)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  At 9.6 times guidance-midpoint earnings with a 5.95% dividend yield, Pfizer stock looks inexpensive.
- [Novo Nordisk (NVO) Stock Price Prediction: Pullback Holds Above Key Support as Positioning Stays Constructive](https://www.google.com/goto?url=CAESmwEBxCJF18GPSJ60-eR-u2MAi1NpeiQZFahItWwx4343MkWtU99n_TD8yk_2j_vL315_ODcm9IeSnxmcDZSwTmlHJ6gdcAqPaX4DCNRom4tLku74zDMBxE6DwQS5Y0_lmLDodvyRcPNhmEF39n_dFdQSrUn8GBKt_1PG2r6c07yF1p84f77epjNQ_sEaCh8Z4lp7qvfcbekNxva4Lg&gsessionid=lG1sc7nYxc9Vo6_tCN-bcGmBkXzPeMAejdKzB-eQiOzRMSiRo3-VPw)  
  <sub>Blockchain News, 15 hours ago</sub>  
  Novo Nordisk (NVO) closed the latest session at $41.20, down 2.67% on the day, with the 24-hour range running from $42.35 to $41.16. That puts the stock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 40.37 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 40.26 (+0.3%), 50d 39.81 (+1.4%), 200d 42.95 (-6.0%); 50d below 200d
Momentum: RSI(14) 50.1 | MACD 0.338 vs signal 0.263 (histogram 0.075)
Returns: 1d -0.8% | 5d -1.8% | 1m +2.6% | 3m -12.5%
52-week range: 35.29 - 63.98 (now 17.7% of the way up)
Volatility: ATR(14) 1.05 (2.6% of price) | annualised 20d 33.0%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 177.88B
Valuation: trailing P/E 10.19 | forward P/E 11.49 | P/B 5.44 | PEG 4.24
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
Price target: mean 45.69 (+13.2% vs last close), range 39.40 - 64.02
Recent rating changes:
  - 2026-10-12 BMO Capital: main, Market Perform -> Market Perform
  - 2026-09-11 Morgan Stanley: down, Equal-Weight -> Underweight
  - 2026-03-02 Goldman Sachs: down, Buy -> Neutral
  - 2026-02-24 JP Morgan: down, Overweight -> Neutral
  - 2026-01-09 CICC: init, ? -> Outperform
  - 2025-12-08 Argus Research: down, Buy -> Hold
Institutional ownership: 10.1%
Largest holders: Dodge & Cox Inc. (0.6%), LOOMIS SAYLES & CO L P (0.5%), Arrowstreet Capital, Limited Partnership (0.5%), Two Sigma Investments, LP (0.4%), Franklin Templeton, Inc. (0.4%)
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

- [Own P&G Stock For Safety? Watch Bond Yields](https://www.trefis.com/stock/pg/articles/626185/own-p-g-stock-for-safety-watch-bond-yields/2026-11-18)  
  <sub>Trefis, 5 hours ago</sub>  
  Procter & Gamble stock has worked as a hiding place since mid-August. In the 63 trading days to Tuesday's close, P&G rose 20.0%. Over the same days the S&P...
- [PG Dec 2027 95.000 put (PG271217P00095000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/PG271217P00095000/)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  Find the latest PG Dec 2027 95.000 put (PG271217P00095000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Can PG's Health Care Segment Extend Its Sales Momentum Ahead?](https://www.google.com/goto?url=CAESsAEBxCJF16hDGH3ODIIoka5Ah0CcrAA2lHF9EDUQrq-4-61mnsR3GU6VaZKGUDbVwvlG-0poU4ZB0M7VTepmiEs1-Iuyf2o_Q23yg3FoU1m6KrVlbdPZBjsqcYghy5IAjDicRPDpoxQPt3DpeKJ36lVfn8OqW8_YH1PUDWSxhk9kXI21So1zF2peCsQ-9ezZM8CfTRqJPbOHOq3lu1gdGLE3ayoWWnrn3vifI4d7LYDwtw&gsessionid=G3wJo0w5u5Qg0YyoJ8Dgobjte5za4eb88J0TAFcLvYxTc0lxd903Dg)  
  <sub>TradingView, 10 hours ago</sub>  
  The Procter & Gamble Company PG, also known as P&G, is looking to sustain growth in its Health Care segment, supported by improving demand trends,...
- [Wells Fargo & Company Issues Positive Forecast for Procter & Gamble (NYSE:PG) Stock Price](https://www.google.com/goto?url=CAESzwEBxCJF1wTp-kkB7hAeqKzlvATh8m6KJ1d1nw6xLhuJw9nfjvthOSSLc2izL0KFzARuDSYUkn1fNduKo5TdJZbN9Z5pA44TUDsQLn6TMLR0qIesLjJLjWHHs1L7tIqrUmZW_qHSJTjYuZBcxsTH0i13Phwcx_Xavzp-71c1dcS3F2ogMNxj3oXyjb8vZDESmoRVujw6YXbDxJt0VOHn1DwYRKUtn2_kYVQ9DRP7ffUzxT7Oq-bcMxzn9CsVpuRpWWP2x0oSM8hDxtVd57bkQiA&gsessionid=G3wJo0w5u5Qg0YyoJ8Dgobjte5za4eb88J0TAFcLvYxTc0lxd903Dg)  
  <sub>MarketBeat, 7 minutes ago</sub>  
  Wells Fargo & Company increased their target price on shares of Procter & Gamble from $180.00 to $188.00 and gave the stock an "overweight" rating in a...
- [PG261204P00160000 Interactive Stock Chart | PG Dec 2026 160.000 put Stock - Yahoo Finance](https://www.google.com/goto?url=CAEScQHEIkXXOUIQWxUWGCFHdvtvv9x5cn-EpEbbUO3LTtENp_Z8GSAzJKG02GLgES2SkAy0oXVi0a1c60MDQPpQD06VYmhfD6WR0mcrMpGcJvwY7Vchs2MQXush0_AZrB7yab-HdVwCTZphdE0uEH_hwuML&gsessionid=G3wJo0w5u5Qg0YyoJ8Dgobjte5za4eb88J0TAFcLvYxTc0lxd903Dg)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [Procter & Gamble Company (The) $PG Shares Purchased by Voya Investment Management LLC](https://www.google.com/goto?url=CAESywEBxCJF18tbpIRXjS7bEe6V-fbQCNjqM4Wc2mrfOrl4L4TTBIXoWtKdpMOPV2sR-5d2ITREFIya2nDtgxTfvTUJ4R_NvawvNZzJdavVGIUAaUqz4NswXK96N6Uwe80k183AQ_7qQmHZ9Fmrt5M5kUNVPhVN8wgnsTpj_lALGZfBZiUsBEWmn8-LLDYjDEeJmzZZah-0-QQ8ooyfMFWVX8aebPXkJOLuo_urrFnYVVDtkxsHTKzi0YPArrPTOmN6rBnRwF1qFM02A7tyUg&gsessionid=G3wJo0w5u5Qg0YyoJ8Dgobjte5za4eb88J0TAFcLvYxTc0lxd903Dg)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Voya Investment Management LLC lifted its position in Procter & Gamble Company (The) (NYSE:PG - Free Report) by 10.7% during the 3rd quarter, according to...
- [PG&E reports layoffs across California, including 125 in Bay Area](https://www.google.com/goto?url=CAESmQEBxCJF1xEFiSA5exdi_AjprMOXVwnN_pLSSPK3yFuOb6mKPPyKDiVh-ccpEWoozU3EfXD7D2LlYad7vTE4yNI7of_1CKD--FTJ_6X8sW7dF86POlB3wppNrXII7rg2PMU0YkKtcKiT3ZJiflpmsFYdtFus6u3msUDFdDWDFwmmjV85BxFSDKnra-A2byhIIoqPMV6yVrCGDmo&gsessionid=G3wJo0w5u5Qg0YyoJ8Dgobjte5za4eb88J0TAFcLvYxTc0lxd903Dg)  
  <sub>Yahoo Finance, 17 hours ago</sub>  
  PG&E has reported hundreds of permanent layoffs across California, including 125 in the Bay Area. The cuts are spread across 65 locations in the state,...
- [What Does Procter & Gamble (NYSE:PG) Latest Performance Signal Ahead?](https://www.google.com/goto?url=CAESqAEBxCJF1w6TRGty58kJbxmp2BuJb1yMC1W9QnvrZEjmFNe7TgiALRz1XOJOSWjzIUxiJhULkWWtfsNX2T1A7xYFCUqaUhUOO5ywZOzZAmC1vZvtC1nCtvtTxcGJC_aI1qRR4TtuBCcr8Pj-OQ36palNKXqLDyHXGVcE4TH7C4C_vBfhlY2dL1l4BXll22axVjWnsR5RW_06wtZKnTUeI54g3BLqb_xTfV8&gsessionid=G3wJo0w5u5Qg0YyoJ8Dgobjte5za4eb88J0TAFcLvYxTc0lxd903Dg)  
  <sub>Kalkine Media, 18 hours ago</sub>  
  Procter & Gamble (NYSE:PG) declared its regular quarterly cash distribution, spotlighting one of the steadiest American consumer-staples payers during a...
- [One NYSE-Listed Household Products Company Near Resistance Level: PG](https://www.google.com/goto?url=CAESpwEBxCJF12lASkqQBL4O3BPAYupp9p38P2_K7kuVXsjY8ATvW21SRhYxfrLKVFClBLVy2UpbWKwJm60inrUA0U2U2ralvyPlo3HZnb5ePGApUwYm7CahQpnMc45ko3J28NqwsJ_dps4efOXe6ouwsxbl8pH9f0HmtrI6VvrUVA4xg96AnQxplSX30Ee8iiJpJ55sMAms8i-VTRIo-L7ZnRSiXIvx2dbNEQ&gsessionid=G3wJo0w5u5Qg0YyoJ8Dgobjte5za4eb88J0TAFcLvYxTc0lxd903Dg)  
  <sub>Kalkine, 23 hours ago</sub>  
  Procter & Gamble (NYSE: PG) operates in approximately 70 countries and sells branded consumer products in about 180 countries and territories.
- [PG&E Corporation (PCG) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZAHEIkXX53X42ajbjMjpd56Qfpn4mdXVccEy_cvtgJwGRDtMuO-HQkP6limL8bKAwTTDVs07TTeXq_s_NlCKWwDgO7XERSg9UB_V0b29VrRv-5eBOMRdW3RoA-VrMUvqmXse0VI&gsessionid=G3wJo0w5u5Qg0YyoJ8Dgobjte5za4eb88J0TAFcLvYxTc0lxd903Dg)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Find the latest PG&E Corporation (PCG) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 171.32 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 165.51 (+3.5%), 50d 155.89 (+9.9%), 200d 150.16 (+14.1%); 50d above 200d
Momentum: RSI(14) 67.3 | MACD 4.470 vs signal 4.254 (histogram 0.216)
Returns: 1d -0.2% | 5d +2.2% | 1m +7.5% | 3m +19.8%
52-week range: 138.04 - 173.02 (now 95.1% of the way up)
Volatility: ATR(14) 3.17 (1.8% of price) | annualised 20d 28.4%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 397.07B
Valuation: trailing P/E 25.80 | forward P/E 23.10 | P/B 7.31 | PEG 4.41
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
Price target: mean 174.26 (+1.7% vs last close), range 151.00 - 190.00
Recent rating changes:
  - 2026-10-26 Barclays: main, Equal-Weight -> Equal-Weight
  - 2026-10-26 Piper Sandler: main, Neutral -> Neutral
  - 2026-10-23 Freedom Broker: up, Hold -> Buy
  - 2026-10-23 UBS: main, Buy -> Buy
  - 2026-10-23 Citigroup: main, Buy -> Buy
  - 2026-10-23 BNP Paribas: main, Outperform -> Outperform
Institutional ownership: 72.0%
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

- [Enablix Named a Visionary in 2026 Gartner(R) Magic Quadrant(TM) for Revenue Enablement Platforms](https://finance.yahoo.com/technology/ai/articles/enablix-named-visionary-2026-gartner-130000123.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Enablix Named as a Visionary and Positioned Furthest on Completeness of Vision in 2026 Gartner® Magic Quadrant™ for Revenue Enablement PlatformsASHBURN,...
- [AbTherx Licenses Atlas(TM) Platform to Athenova Therapeutics for Next-Generation Targeted Alpha Radiopharmaceutical Discovery](https://finance.yahoo.com/healthcare/articles/abtherx-licenses-atlas-tm-platform-110000642.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  Partnership combines Atlas Mice with Athenova's novel oncology target and expertise in astatine-211-based therapies to accelerate new cancer treatments to...
- [Toyota Motor Corporation (NYSE:TM) Stock Short Interest Report for October](https://www.google.com/goto?url=CAESwwEBxCJF1zk-b7Z4f_oAUQuFX5ZL91phHPe9hFEUkySzYmPuX9_0auIvZoAZ1hjmBHbIfwJ24h05FArblokoyNL5JU7ScV1aSXg1ZlEMXZvFlWsAhsxjyydATyt8HKqpLTt9XTsY8lqQLNk4TZ0PeFB9R-tKcB7mjAAMtVr3UmMg5i-kOlr2ts_epD6IGuuftmbWIsOfbfO5ReMmr1lS6IBhhwW-9ih00SAuYUs-dsceJfU1bIC1dXkRV3KYtofGw7_neDk&gsessionid=CfowMMJryvmPZFjwNEN8d6NkAs_gqv_HXvm6XJSpWUwDmmQYLwaiJg)  
  <sub>MarketBeat, 18 hours ago</sub>  
  Toyota Motor Corporation (NYSE:TM - Get Free Report) saw a significant increase in short interest during the month of October. As of October 30th,...
- [(HBIL) Trading Advice (HBIL:CA)](https://www.google.com/goto?url=CAESiQEBxCJF1yrkZvGkVeVuxJHBOh10GiP-C9JdkACyauv3s-kQiOk4_armaxXw50K5v47BxlJ02dM9ZeN6Yzk7VYrYtLr4eUypFVBJGYP18bFpATCzSMawHV_N3LOK6Yf1F7XC2rRuaYxHPd0gBIlnJ21fUana9JrEtDPpucxxtONGU9H2rZ_oA3N5kw&gsessionid=CfowMMJryvmPZFjwNEN8d6NkAs_gqv_HXvm6XJSpWUwDmmQYLwaiJg)  
  <sub>Stock Traders Daily, 3 hours ago</sub>  
  Trading Advice for Hamilton U.S. T-Bill YIELD MAXIMIZER TM ETF HBIL including day trading swing trading and long term investing plans for HBIL.
- [Tesla Short Interest Falls As Bears Retreat From August Peak](https://www.google.com/goto?url=CAESugEBxCJF1-B0i0xiXKVzdcy31WzcTTW7WyJmFA7tZMTXhJelM0kZfDqixahpxohSDMzSChkyuK4AsVZK6T5oc8p_P7xyJaMrooHssqrgxJNVkE8m3xjlNeY-Xgdq3PVYGWSVP4H0h2hBll0y2pJVOn4Eql-sI0kfn1H-IrXK1aoDoh6VMBWMpiNWzqQpsoOHjtxWpivHlt2YlX58-qMqWAzcQvkS9fZVHjZ3iZbwffeXPGOhF-U5ghv2RUs&gsessionid=CfowMMJryvmPZFjwNEN8d6NkAs_gqv_HXvm6XJSpWUwDmmQYLwaiJg)  
  <sub>Benzinga, 24 hours ago</sub>  
  Tesla Inc. (NASDAQ:TSLA) short sellers pulled back from their positions.Short interest fell 4.89% to 65.96 million shares as of the Oct. 30 settlement date,...
- [Three companies earned ISG's highest customer-experience honor, selected from 225 providers.](https://www.google.com/goto?url=CAEStQEBxCJF1yCzsA0eEityUnSs5-ZfglfHKYn2p7iNQmU2MG5_T9TkdXCfzlAg6vfUKKz3C7Qu-MJ9ep-1h9QH1mblu2H4EyZ0Bt9_-ESjHrJgTwym078iEwPUgimmbIpLBQp8LEQOAIKOwBQt4COgBjYgmBQnEkqXFqXrJSVZHpBv0vA72Z1it85VrPXfykaXdRUMEJzbpIJcZ5qn5sy4emLy_UVfwXjjPg8w729mf3tUkgvpdX8J&gsessionid=CfowMMJryvmPZFjwNEN8d6NkAs_gqv_HXvm6XJSpWUwDmmQYLwaiJg)  
  <sub>Stock Titan, 6 hours ago</sub>  
  HCLTech collected the most awards overall, with three; Cognizant, Hexaware, Infosys and Persistent Systems each won two at the Nov. 17 ceremony.
- [TM's RM2.7 bil undersea cable project to tap Sarawak's AI data centre growth — Kenanga](https://www.google.com/goto?url=CAESYwHEIkXXdDtSxrfoP0qHFOcdY9bD1Jjz-pKp816RjBCzHtD9hl0lWp5hTrfaD4SxEg-s0OOyjWjlBvIWI1UnBSDJ98UaSIy_wgDV0Gsb0H8YRUIX36Q0OqVAssDqBwBS2OWL0w&gsessionid=CfowMMJryvmPZFjwNEN8d6NkAs_gqv_HXvm6XJSpWUwDmmQYLwaiJg)  
  <sub>The Edge Malaysia, 9 hours ago</sub>  
  Telekom Malaysia Bhd (KL:TM) could unlock additional earnings opportunities beyond 2030 from its RM2.7 billion undersea cable project, as growing artificial...
- [STXE TM Food Producers I (U5B.Z) Seasonal Returns Chart - Yahoo Finance](https://www.google.com/goto?url=CAEScQHEIkXX4fdwNmPy5lyNhhaAXn5qYHWTseHIyVAmkb55xyJfjzHD9lsV0ghCYjJ2faMROBX7Amx_CbdLerzzQicxE5mgv9kADIJ8hONxhJ_8561IrLl4g0c8Fc8mQzbQXkHQScSIt412If4yjbyBuvzc&gsessionid=CfowMMJryvmPZFjwNEN8d6NkAs_gqv_HXvm6XJSpWUwDmmQYLwaiJg)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  STXE TM Food Producers I (U5B.Z) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [Can Toyota Motor (NYSE:TM) Build On Its Latest Momentum?](https://www.google.com/goto?url=CAESngEBxCJF14-yEF2LEub-5SDvG25xoObpJFmjl_1LuOv-11MtR9wFoAuvdg9CMFAX1x-VSz3VMMSNgpUvlrfBdGpyIKdpxWa8uElMK4qGjt8IfpFRNWCSIIN2ZMHp88XdD6z2_wCCjaz9EF5JannFNOkc1ROVhhwl8B9jY66z_PyaX86kizULm89_Cqx8lS4ecNO-No0bjQcYcjyFyl6scw&gsessionid=CfowMMJryvmPZFjwNEN8d6NkAs_gqv_HXvm6XJSpWUwDmmQYLwaiJg)  
  <sub>Kalkine Media, 22 hours ago</sub>  
  Toyota Motor (NYSE:TM) advances its multi-pathway electrification approach as the global automobile sector navigates rapid technological and regulatory...
- [(AMAX) Trading Strategy and Analysis (AMAX:CA)](https://www.google.com/goto?url=CAESmAEBxCJF17QLUySBe12DUMP5jcNmGonkNjTHuNcJ0QPeB32cxGtzTy5uYWHPI0eE9l1VLBjGGeZajpxXWzbbpak_7LLGjldHqfMhT7epccKNq8fW2J9jRhTBjnIMLo4BbqDN6nIYnBUM-7mxKYXht7GcXsd2lGZ5xEwH8d7A_LfGkxkE8QNYUA5ecfdiC0jSsYAXcm4KJe2pxQ&gsessionid=CfowMMJryvmPZFjwNEN8d6NkAs_gqv_HXvm6XJSpWUwDmmQYLwaiJg)  
  <sub>Stock Traders Daily, 19 hours ago</sub>  
  Trading Strategy and Analysis for Hamilton Gold Producer YIELD MAXIMIZER TM ETF (AMAX) with Buy/Sell Signals.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 212.01 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 205.32 (+3.3%), 50d 196.01 (+8.2%), 200d 197.64 (+7.3%); 50d below 200d
Momentum: RSI(14) 61.5 | MACD 5.639 vs signal 5.355 (histogram 0.285)
Returns: 1d -0.5% | 5d -0.5% | 1m +7.9% | 3m +10.3%
52-week range: 166.50 - 248.29 (now 55.6% of the way up)
Volatility: ATR(14) 4.18 (2.0% of price) | annualised 20d 38.7%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 248.86B
Valuation: trailing P/E 9.67 | forward P/E 13.44 | P/B 16.88 | PEG 19.96
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
Price target: mean 238.08 (+12.3% vs last close), range 230.00 - 253.00
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

## Whole-market funds

### Farm goods basket (DBA) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; macro and technicals are bearish but no clear surprise, fundamentals modestly positive, and flows flat.

**Main reasons it gave:**
- Price below 20‑day, 50‑day, and 200‑day SMAs with RSI 28.3, indicating bearish technicals and low volume
- Rising Treasury yields and a stronger dollar (USDX +0.88) pressuring commodity prices
- Flat fund flows (0% change) showing no net demand
- Fund basics show 3.4% yield and 10.4% annualized three‑year return, modestly positive fundamentals

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 26.17 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 26.73 (-2.1%), 50d 27.77 (-5.8%), 200d 27.41 (-4.5%); 50d above 200d
Momentum: RSI(14) 28.3 | MACD -0.458 vs signal -0.482 (histogram 0.025)
Returns: 1d -0.8% | 5d -0.7% | 1m -7.1% | 3m -7.8%
52-week range: 25.44 - 29.49 (now 18.0% of the way up)
Volatility: ATR(14) 0.24 (0.9% of price) | annualised 20d 9.4%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Commodities Focused
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 3.4%
Three-year record: +10.4% a year | beta to the market 0.37
Cost and size: expense ratio 0.85% | net assets 1.13B
What it is made of: Other 49.6%, Cash 47.9%, Bonds 2.5%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 40.2%, Invesco Short Term Treasury ETF 5.3%
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 27.60M | fund size: 722.29M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Energy inventories: crude +4.7M barrels (build), nat gas +61 BCF (build) – bearish but already priced
- EIA price outlook: WTI forecast $84 in 6 months (down ~13%) – bearish but likely priced in
- Technicals: RSI 22.4 (oversold) but volume 0.16x 20‑day avg, price below 20‑day SMA, no decisive break
- Macro: Treasury yields up modestly, inflation 3.7% (no surprise), dollar up 0.88% – no material shock
- Fund flows: share count unchanged (+0.0% week, +0.0% month) – neutral

<details><summary><b>News</b> — score +0.00</summary>

- [商品指数ETF-PowerShares DB收跌0.2%，成交额2267.86万美元](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afdbb18a81948179f0a2eff6bd4af89&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fusstock%2fnotice%2f2026-11-18%2fdoc-inizayrr1790117.shtml&c=10310666215160895535&mkt=en-us)  
  <sub>新浪财经, 16h ago</sub>  
  11月18日，商品指数ETF-PowerShares DB（DBC）收跌0.2%，报30.19美元，成交额2267.86万美元，市值16.91亿美元。 声明：市场有风险，投资需谨慎。本文基于第三方数据库发布，不代表新浪财经观点，任何在本文出现的信息均只作为参考，不构成个人投资建议。如有出入请以实际公告为准。如有疑问，请联系biz@staff.sina.com.cn。

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.67 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 31.99 (-7.2%), 50d 32.59 (-9.0%), 200d 29.69 (-0.0%); 50d above 200d
Momentum: RSI(14) 22.4 | MACD -0.762 vs signal -0.507 (histogram -0.255)
Returns: 1d -1.7% | 5d -3.8% | 1m -11.6% | 3m -4.6%
52-week range: 22.36 - 34.10 (now 62.3% of the way up)
Volatility: ATR(14) 0.49 (1.7% of price) | annualised 20d 20.5%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.40</summary>

```text
Fund type: Commodities Broad Basket
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +13.5% a year | beta to the market 1.04
Cost and size: expense ratio 0.85% | net assets 1.94B
What it is made of: Other 50.0%, Cash 45.2%, Bonds 2.7%, Stocks 2.1%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 41.8%, Brent Crude Future Jan 27 11.0%, Invesco Short Term Treasury ETF 5.8%, Mini Ibovespa Future Dec 26 2.1%
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
US inventories, week ending 2026-11-06 (published the following Wednesday)
  Crude oil: 414.4 million barrels, +4.7 on the week (a build), 21% percentile over 52 weeks
  Natural gas: 3,862.0 billion cubic feet, +61.0 on the week (a build), 94% percentile over 52 weeks -- high for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.40</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 111.40M | fund size: 3.31B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: technicals show a downtrend but no decisive break, fund flows are positive, fundamentals are solid with attractive yield, and macro environment shows modest yield rises and higher volatility but no surprise.

**Main reasons it gave:**
- Price below 20‑day, 50‑day, and 200‑day SMAs; MACD negative indicating downtrend
- Share count up 5.1% over past month, indicating net inflows
- US Treasury yields rose 10 bps this week and VIX rose to 24.33, suggesting higher risk aversion
- Fund yield 5.4% with moderate credit mix (33.9% BBB, 25.6% BB, 19.2% B) and solid three‑year performance

<details><summary><b>News</b> — score +0.00</summary>

- [3 ETFs Were Paying Monthly Before the 2008 Crash. Did the Checks Survive It?](https://247wallst.com/investing/etf/2026/11/17/3-etfs-were-paying-monthly-before-the-2008-crash-did-the-checks-survive-it/)  
  <sub>15 hours ago</sub>  
  When the paycheck stops in retirement, the real test of a monthly income fund is what its check does in a crash. Three iShares bond ETFs were already paying...
- [QUICK SPARK: Vanguard’s New Emerging Markets Bond Fund Challenges iShares’ $14 Billion EMB ETF](https://www.benzinga.com/etfs/new-etfs/26/11/63363408/quick-spark-vanguards-new-emerging-markets-bond-fund-challenges-ishares-14-billion-emb-etf)  
  <sub>20 hours ago</sub>  
  Vanguard recently launched VEMB, an actively managed emerging markets bond ETF with a 0.35% fee, challenging iShares' $14B EMB fund.
- [Monthly payouts from three key bond ETFs survived the 2008 crash, showing resilience in crisis income streams.](https://www.google.com/goto?url=CAESlgEBxCJF14e5EfYa-GPSpHH836Tlr8GYp3yZ02c7qhrtVO7sY0nl4nwkWCiHeGppZpKpNZUW9qBj7cTgLQ4kDk6r_bTSeG-UdZlJL3csQNRQ_qOnFwN0_3Br9xb2pGdsV2csB9fdTiwsXUVFQ8EujXdI0x_S0ZJ-8VrmcObwv0MpObhiX8P-oFKvuVnnWbNZxzczhjXjDqU&gsessionid=uxGsf2E6kGdu424iZo32BHqB_iDgNzYxsahFwbfAninhvwoajcodaw)  
  <sub>15 hours ago</sub>  
  Three iShares bond ETFs—TLT, HYG, and EMB—that paid monthly distributions before the 2008 financial crisis continued to deliver income checks through the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 90.89 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 91.70 (-0.9%), 50d 91.81 (-1.0%), 200d 94.64 (-4.0%); 50d below 200d
Momentum: RSI(14) 41.0 | MACD -0.233 vs signal -0.116 (histogram -0.117)
Returns: 1d +0.2% | 5d -1.3% | 1m -0.4% | 3m -4.0%
52-week range: 90.14 - 97.74 (now 9.9% of the way up)
Volatility: ATR(14) 0.47 (0.5% of price) | annualised 20d 7.2%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Emerging Markets Bond
Yield: 5.4%
Credit quality: BBB 33.9%, BB 25.6%, B 19.2%, A 17.3% | US government debt 87.8%
Three-year record: +8.2% a year | beta to the market 1.06
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
Share count change: 1 week: +1.5% (200.19M) over 7d | 1 month: +5.1% (653.84M) over 32d
Shares outstanding: 149.27M | fund size: 13.57B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, flat fund flows, and technicals show no decisive breakout; fundamentals are modestly positive but not strong enough to tilt the view.

**Main reasons it gave:**
- Flat fund flows: 0% share count change over 1 week and 1 month
- Technical: price below 20‑day, 50‑day, 200‑day SMAs; RSI 38.7; no decisive breakout
- Macro: Treasury yields rose modestly (10‑yr +0.10% weekly) and VIX up 6.8% weekly, no surprise data
- Fund basics: 6.1% yield, BB/B credit mix, 3‑yr return +7.1%/yr, indicating mixed fundamentals

<details><summary><b>News</b> — score +0.00</summary>

- [3 ETFs Were Paying Monthly Before the 2008 Crash. Did the Checks Survive It?](https://247wallst.com/investing/etf/2026/11/17/3-etfs-were-paying-monthly-before-the-2008-crash-did-the-checks-survive-it/)  
  <sub>15 hours ago</sub>  
  Retirees live on the monthly check, and 2008 tested whether it would show up at all. Three bond funds continued paying monthly when credit markets seized.
- [Which of the Top Three Bond ETFs Is Most Exposed to Wednesday's Fed Minutes: iShares 1-3 Year Treasury ETF (NASDAQ:SHY), iShares 20+ Year Treasury ETF (NASDAQ:TLT) or iShares iBoxx High Yield ETF (NYSEARCA:HYG)?](https://kalkine.com.au/news/economic-news/which-of-the-top-three-bond-etfs-is-most-exposed-to-wednesdays-fed-minutes-ishares-1-3-year-treasury-etf-nasdaqshy-ishares-20-year-treasury-etf-nasdaqtlt-or-ishares-iboxx-high-yield-etf-nysearcahyg)  
  <sub>4 hours ago</sub>  
  Which of the Top Three Bond ETFs Is Most Exposed to Wednesday's Fed Minutes: iShares 1-3 Year Treasury ETF (NASDAQ:SHY), iShares 20+ Year Treasury ETF...
- [Which Top 3 Bond ETF Reacts Most to Wednesday's Fed Minutes: iShares 1-3 Year Treasury ETF (NASDAQ:SHY), iShares 20+ Year Treasury ETF (NASDAQ:TLT) or iShares iBoxx High Yield ETF (NYSEARCA:HYG)?](https://www.google.com/goto?url=CAESmAIBxCJF1-iYzm-_1ijRVp1vMThRX2u7LZuHJSItFdhNQX1xPqfIzrzpvlGindH0b39AjdPfHA70lKq4vWhPdZtkgoXDr9JQAywgLfaw7OOPhuDLsurnXcIZAjYm9d6YgKH_NOmMIB65DMtlnhCDV8QF5HAxWaRvGI3KXdRSVxkmPUBCC1mIibhj5la2PAazRSm-Q-KirkYbWm_57mviSwREs7lQICCK2hN_7xy0w2eSRM4T2Mu0CXhyykYd2SWiZ3nIM6l0VLv0Ea5eNTOl24vnVjLEeKxvvcpzXa_stNvmfnrf-6A4Ttz5oDbdTDJyPvVKmdrwrnfiv-pKldnoe1Ot0vJyD4hbDgYvhAOSChr7GroPHS_ytGNd&gsessionid=KhGo9yOC2M07QvNFw16vCCDqUkWU4DgIlqVFGjXAhTxaq0-g12ijDg)  
  <sub>5 hours ago</sub>  
  Which Top 3 Bond ETF Reacts Most to Wednesday's Fed Minutes: iShares 1-3 Year Treasury ETF (NASDAQ:SHY), iShares 20+ Year Treasury ETF (NASDAQ:TLT) or...
- [How Did US High-Yield Credit Spreads (NYSEARCA:HYG) Gain 11 Basis Points Within a Single Session?](https://www.google.com/goto?url=CAESyAEBxCJF11KLfWBYcTbmzdd5qCvi4H5xcUEChsx1qrylV3YdaqRnvYP4bl2RiLNunHTOa2NcgOjSxldyEP0xmhDBpDe-O6HJG8bp_HMZ5xDpzLkVUNWEoSXLFxneK6J4PlhLrKYSFLoarxo6RSjUi-Hq2hNnrhiHaqdNJNFks3nbnlzcFm1o6Fr55-2UPh98hDz90D6Or-pc0x7ScNWtGFF-qnC-HJYD8_gixeifI7-1gIiE8Tm5vmSsgjU7n9EHCDyBW9k2iLv0Ug&gsessionid=KhGo9yOC2M07QvNFw16vCCDqUkWU4DgIlqVFGjXAhTxaq0-g12ijDg)  
  <sub>5 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [1. iShares iBoxx Investment Grade Corporate Bond ETF (NYSEARCA:LQD)](https://www.google.com/goto?url=CAESmAMBxCJF14kWCCCBQ4EIGcNMcoQe1h7Z4S-RwmSBRQAMDjhrht2wYXMBcCb7We1sr1lHR4f4euGelfQOBDlkaWyUMWqtzNaRseEMD-2wwAqN_EWGpeR_SCyRJ71dkPCFrI7MnkH8BPBNA63qOb4zdowgSwq9uJENGIS_58Ifrgk7825itlVT1U5KjZN3vVIoPgU9GNF8vJh9EWibjLoZ-PYoSsHoP-zQVP3Lt_Boc86U8wwycHDhqrBmqc1SHnoQpuzh4y1erJa0ujNnnzRtrvUMyK1andgkKXUyMreEZRPi8LepWM1E3sNr7GKsp-GjpATtTScZyYjqnMzrke4Q5mVHDMrfIbKrpkxFaIG_qwbI6kZejieeWPzVWAmlR9vyjVYuWzoNNHXCmFQ3RoG9DwNkdws_6qJF2vVHmLjGxq4xQvV6ymrPopDez68469HYbZbboOMqyhGiPprl4QMphuO_QmyGUZULq20FDvRfut-d6rOHJEOBwedFB-Y4juzd5bbaMKtYIMUZzILd7_XfTDIGw6bO4yu2Ooo&gsessionid=KhGo9yOC2M07QvNFw16vCCDqUkWU4DgIlqVFGjXAhTxaq0-g12ijDg)  
  <sub>20 hours ago</sub>  
  What Makes the Top 5 Credit and Income Plays in Focus This Week Stand Out, and Which Looks Strongest: iShares iBoxx Investment Grade Corporate Bond ETF...
- [Monthly payouts from three key bond ETFs survived the 2008 crash, showing resilience in crisis income streams.](https://www.google.com/goto?url=CAESlQEBxCJF1_7ZF_w9ejrbJFPU5GVutCo2ZFP794o0M5G4VBugtbRWS3uyjPMdjhFBCDnjL4Ee0Ry3dmTc45_omQJvGaRk1FXOftD1YA0SKA6h1_gBl7APZaqsCxs28WzM4OsMvtkM7ScUKGwx2n9GCb8eLBmyzRc99Nt6ma-6puF5X16G34VbZi_dbXzlg06FVjN0W2_qtA&gsessionid=KhGo9yOC2M07QvNFw16vCCDqUkWU4DgIlqVFGjXAhTxaq0-g12ijDg)  
  <sub>15 hours ago</sub>  
  Three iShares bond ETFs—TLT, HYG, and EMB—that paid monthly distributions before the 2008 financial crisis continued to deliver income checks through the...
- [Is iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) Vulnerable as the 10-Year Yield Holds at 5.10%?](https://www.google.com/goto?url=CAESvgEBxCJF1yMxfrAOCA6C_-x8EZRaCWRaOydBIO4cUbeRD-luuEmrdF_wjzC4P6Tuhq7WNhrQpDRCBXjb06yc7T8_esT5gUPxB1XKDtXEG1bzBKHdpvwTeDbQcTI9krcq5DNeapq2so0XsztahjNzq921oB2WdgW5nn8gdNbANlauwQRi34KuhGCKOrNvTgWQqvVOhMivX7foMqxJSxPboh9WFaVTugXzDeXAprwHRVa6IVzqrekLVqMQdhfUrGc4&gsessionid=KhGo9yOC2M07QvNFw16vCCDqUkWU4DgIlqVFGjXAhTxaq0-g12ijDg)  
  <sub>5 hours ago</sub>  
  Is iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) Vulnerable as the 10-Year Yield Holds at 5.10%?

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 76.65 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 77.17 (-0.7%), 50d 77.44 (-1.0%), 200d 79.27 (-3.3%); 50d below 200d
Momentum: RSI(14) 38.7 | MACD -0.186 vs signal -0.142 (histogram -0.043)
Returns: 1d +0.0% | 5d -0.9% | 1m -0.2% | 3m -3.7%
52-week range: 76.63 - 81.18 (now 0.5% of the way up)
Volatility: ATR(14) 0.29 (0.4% of price) | annualised 20d 5.3%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: High Yield Bond
Yield: 6.1%
Credit quality: BB 59.6%, B 32.1%, Below B 7.2%, BBB 0.8%
Three-year record: +7.1% a year | beta to the market 0.65
Cost and size: expense ratio 0.49% | net assets 17.71B
What it is made of: Bonds 99.3%, Cash 0.5%, Preferred 0.2%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 1.1%
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 195.60M | fund size: 14.99B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund’s fundamentals are solid (AA‑rated bonds, 4% yield, low expense), but positioning data shows large speculators are net short (37.8% of OI) with a slight increase this week, indicating modest bearish pressure on bond prices. No macro surprise or decisive technical breakout is present, leading to a neutral overall view.

**Main reasons it gave:**
- Large speculators net short 37.8% of open interest
- Net short increased by 0.3% of open interest this week
- Fund holds AA‑rated US government bonds with 4.0% yield and 0.15% expense ratio
- 10‑year Treasury yield rose 10 bps to 5.10% this week

<details><summary><b>News</b> — score +0.00</summary>

- [State Street SPDR MSCI All Country World UCITS ETF (SPYY.F) Seasonal returns chart](https://uk.finance.yahoo.com/quote/SPYY.F/seasonality/)  
  <sub>19 hours ago</sub>  
  State Street SPDR MSCI All Country World UCITS ETF (SPYY.F). 171.16 +2.00 (+1.18%). As of 30 June at 14:02:49 CEST. Market open.
- [The Government Spends About $5.5 Billion a Day More Than It Takes In. The Debt Has Doubled in 10 Years. Jaime Dimon This the Situation Could Get Much Worse.](https://247wallst.com/investing/2026/11/17/the-government-spends-about-5-5-billion-a-day-more-than-it-takes-in-the-debt-has-doubled-in-10-years-jaime-dimon-this-the-situation-could-get-much-worse-2/)  
  <sub>18 hours ago</sub>  
  Washington's debt has doubled to roughly $40 trillion in a decade as spending outpaced revenue, and interest costs now feed even more borrowing.
- [Top Tokenized ETFs by Market Cap](https://www.google.com/goto?url=CAESXgHEIkXX2vOk5Vz0ElKi4qzSLa1ghFMJR1wGp1pV6h44yj7xP7Hhge5a2V9XRhlQvVRlewpuiq5t2dkV7UabDzs7opJV1ftu0NQ-hzrkXTg0tG2dfWARK98zxe24kEw&gsessionid=O68iy_rR5Xer-cMQffujM9PBzfGFcE6nNd24hP1bNWXakz3yAXNGJA)  
  <sub>14 hours ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap,...
- [Xtrackers USD Corporate Green Bond UCITS ETF 1C EUR Hedged Acc (XGUE.F) Seasonal returns chart](https://www.google.com/goto?url=CAEScwHEIkXXt5PLOLpgjVFokvurzFLdFopifiyeOy259b8UVa5eDxqaFjwPTiEXKYA8ZEjbSkguQXPC7k50n5wrUkKdcRm5UvfulQeXNtFUELPXZWf67tVTRTKY9gnoM1dNtfPm4cBisDsjm6l5EdU2rpwqydA&gsessionid=O68iy_rR5Xer-cMQffujM9PBzfGFcE6nNd24hP1bNWXakz3yAXNGJA)  
  <sub>19 hours ago</sub>  
  Xtrackers USD Corporate Green Bond UCITS ETF 1C EUR Hedged Acc (XGUE.F) seasonal returns chart provides the mean and median returns by month to inform your...
- [Acatis Qilin Marco Polo Asien Fonds (UF11.MU) Seasonal returns chart](https://www.google.com/goto?url=CAESdAHEIkXXshUkmbGqlwRAhBD9kfHQmkNPyRu_xY97MvYBjB2ELLNvgacLqMXlEUDT3dY7dmn2yxd1daeyOAwrwQlQoLJM3rKDF7Ec6qDVVb_w3sMCAmXV0pceKIx4TrhskkAKQ4nbETQBmjEu4lyX3Wa_FK04&gsessionid=O68iy_rR5Xer-cMQffujM9PBzfGFcE6nNd24hP1bNWXakz3yAXNGJA)  
  <sub>19 hours ago</sub>  
  Acatis Qilin Marco Polo Asien Fonds (UF11.MU) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 90.64 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 91.09 (-0.5%), 50d 90.47 (+0.2%), 200d 93.55 (-3.1%); 50d below 200d
Momentum: RSI(14) 48.0 | MACD -0.036 vs signal 0.097 (histogram -0.133)
Returns: 1d +0.3% | 5d -0.3% | 1m +0.4% | 3m -2.5%
52-week range: 88.92 - 97.99 (now 19.0% of the way up)
Volatility: ATR(14) 0.46 (0.5% of price) | annualised 20d 7.3%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Long Government
Yield: 4.0%
Credit quality: AA 100.0% | US government debt 99.6%
Three-year record: +3.0% a year | beta to the market 1.17
Cost and size: expense ratio 0.15% | net assets 43.53B
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 37.8% of open interest (6,095,194 contracts)
Change on the week: +0.3% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 146.00M | fund size: 13.23B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Technical: price 3% below 20‑day, 50‑day, 200‑day SMAs; RSI 40; MACD negative
- Positioning: large speculators net short 10.1% of open interest, short increased 2.2% week‑over‑week
- Analyst view: 100% buy rating on 1.9% of fund, price target +14.3% above current price
- Fund flows: flat over past month, no net creations or redemptions

<details><summary><b>News</b> — score +0.00</summary>

- [IWM 261120 287.00C (IWM261120C287000) Stock Options Chain | Quotes & News](https://www.moomoo.com/stock/IWM261120C287000-US)  
  <sub>18 hours ago</sub>  
  Track real-time IWM 261120 287.00C (IWM261120C287000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [Vanguard Russell 2000 Index Fund ETF Shares (VTWO) Stock Price, News, Quote & History](https://finance.yahoo.com/quote/VTWO/latest-news/)  
  <sub>18 hours ago</sub>  
  Find the latest Vanguard Russell 2000 Index Fund ETF Shares (VTWO) stock quote, history, news and other vital information to help you with your stock...
- [9 Of 11 Sectors Fall In Tuesday Trading As Cyclicals Lead](https://www.google.com/goto?url=CAESrgEBxCJF1z0jGJV3Z-NGDTo3z0QDAQiz3UOkovGTHtMXwJfFR9OM5YOSu3cAZIiMOuB-kCwEgc7qNSw5y_8B1_Xi1MK7mTYniZGR-DB-YzHB0BVC4MPNryzIqx8xzjhduap1kVMy0wDxcj9jCpkiIChLuNGeAmPTBab2NxBiJXIkdDgD0fQTDPcc20oBwV-6bXeK0wX0IhlIZhvre_nv7nyUpUerKRGBM9GdxqZ38HM&gsessionid=kgoaLuKp7ETj8ay0w_OPaOxOTQnIsa9NbLU-gMxxexvM6lwsptCvMQ)  
  <sub>23 hours ago</sub>  
  Two sectors are higher and nine are lower in Tuesday's regular session, with cyclical sectors holding two of the top three positions.
- [Invesco S&P 500 Equal Weight ETF (RSP) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESYwHEIkXXv1vUtXfgmGJpK4kjH1rfwi4-N19QrIhcb4rtKNaPzjuxG2xqJcLlDpyMOXKmesqNfBQz3hPsPdOLVt5KcfdocvDe8BjkQXWeOoh2bzD-NYeI6k1iMCL3p3Xzv638XA&gsessionid=kgoaLuKp7ETj8ay0w_OPaOxOTQnIsa9NbLU-gMxxexvM6lwsptCvMQ)  
  <sub>14 hours ago</sub>  
  Find the latest Invesco S&P 500 Equal Weight ETF (RSP) stock quote, history, news and other vital information to help you with your stock trading and...
- [IWM NAV Falls 1.69% to $272.81; ETF Closes at $272.94](https://www.google.com/goto?url=CAESagHEIkXXs5dkxmo5OIauOj0eWSxaKm4Ve6iNFEcfx7YmVllIpd4K0TKeciV9o2X4OJ0KkdwFJv5MizZxVZG5ioUI8FMqgKqPYLvpKCOW57scLJiHFWeADXUvE6o5Hk2gCVg4JFdXOTgeTo8&gsessionid=kgoaLuKp7ETj8ay0w_OPaOxOTQnIsa9NbLU-gMxxexvM6lwsptCvMQ)  
  <sub>21 hours ago</sub>  
  The iShares Russell 2000 ETF's net asset value was $272.81 on Nov. 16, down $4.68 for the day. The decline amounted to 1.69%. Its shares closed at $272.94,...
- [iShares Russell 2000 ETF (IWM) Price Prediction: Small caps slip into a technically weak but not broken setup](https://www.google.com/goto?url=CAESmQEBxCJF1wV_aR79A8fvwiv1XL69ePr_DIyq69CG0WL5ZKAfx9BxZEm4YF6Chacd3e-s2ht9pOmMDDJeM_sarb_x6fZ5CKW1H_Wm3Cv67TnErX2jAyAYRdh8zSVf0TX-tPsfqbdc4-KKDxFEFVgVAikqEpUSLcXC3YIBTJteroTusQn4CrGxLaTqEEGvo_91Vx3WD7I6t9dn5m8&gsessionid=kgoaLuKp7ETj8ay0w_OPaOxOTQnIsa9NbLU-gMxxexvM6lwsptCvMQ)  
  <sub>21 hours ago</sub>  
  iShares Russell 2000 ETF (IWM) is trading at $271.75, down 1.67% on the day and below its short- and medium-term moving averages. The tape is soft, but the.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 269.65 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 277.78 (-2.9%), 50d 279.37 (-3.5%), 200d 279.55 (-3.5%); 50d below 200d
Momentum: RSI(14) 40.1 | MACD -1.864 vs signal -1.011 (histogram -0.853)
Returns: 1d +0.2% | 5d -4.7% | 1m -2.2% | 3m -9.4%
52-week range: 229.11 - 305.09 (now 53.4% of the way up)
Volatility: ATR(14) 4.74 (1.8% of price) | annualised 20d 25.5%
Volume: 0.13x the 20-day average
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
Three-year record: +17.1% a year | beta to the market 1.26
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
Weighted price target: +14.3% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 281.05M | fund size: 75.79B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, flat fund flows, modest yield rise, technicals not decisive, and no significant data shock.

**Main reasons it gave:**
- 10-year Treasury yield up 10 bps to 5.10% this week
- Fund share count unchanged (0% change) over past week and month
- Price below 20‑day, 50‑day and 200‑day SMAs (103.08 vs 103.86, 103.50, 107.24)
- No macro data surprise (inflation 3.7% in line with expectations)
- Corporate bond supply expected to increase by $35 B while LQD holdings remain steady

<details><summary><b>News</b> — score +0.00</summary>

- [Why Is USD 35 Billion of Corporate Bond Supply Coming While the iShares iBoxx Investment Grade ETF (NYSEARCA:LQD) Holds Steady?](https://kalkine.ca/by-topic/mutual-funds-etfs/why-is-usd-35-billion-of-corporate-bond-supply-coming-while-the-ishares-iboxx-investment-grade-etf-nysearcalqd-holds-steady)  
  <sub>kalkine.ca, 20 hours ago</sub>  
  Why Is USD 35 Billion of Corporate Bond Supply Coming While the iShares iBoxx Investment Grade ETF (NYSEARCA:LQD) Holds Steady?
- [How to Buy iShares Core S&P 500 ETF (IVV)](https://www.fool.com/investing/how-to-invest/etfs/how-to-invest-in-ivv-etf/)  
  <sub>The Motley Fool, 23 hours ago</sub>  
  The iShares Core S&P 500 ETF (IVV -1.03%) is one of the largest exchange-traded funds (ETFs) in the U.S. It had $879 billion in assets under management...
- [1. iShares iBoxx Investment Grade Corporate Bond ETF (NYSEARCA:LQD)](https://www.google.com/goto?url=CAESmQMBxCJF18xG3jeJwZcOT1UZcI4vaByWmHDzX0ge3d4fMkdillJouEMEYateGs-y8gMKwcz4dAl2YIyRtDf-olFb05nWW6KxVxkxyphNhEISKWiQb7-KtR1u_4CcUJ7PXkoX4XQhRjIWkxtGJufJVEEiU_GwLWm8ixLtn4RUef6QiSgyJLba0RtTIoNqcgTUQP-mDWO1E4bfhojQNoFuHVzZ1341KxsSEMj8dQBAK8rU27YFZDSpy_h36q5_0xfjbdMojuICOln0YRwA8WBd3LaOZ8Ql0oh7UlQU_FpWp6jwbiQLKH2gnyas1xLiraixk8EysvTNYnD78oBw_C6xb_WXffBmOWVEHm-mcLiT2fNO-13x0Ys7qFYc8_5-V2sZankeO4AqAn4kRkBZaLpLqdRP7LxInEzyYuVE-ysWz_POvoyOEuatr9qnVoMK-dkls_MNQG-7Hx7AwX2b2Y1tZvMwdIZfIFFnnRCCUU-_XAJjhnen9TOd2gIAw5Gr7BWwKzZ6ouGSpFEBMJwi0Y3kPUx5n_SPPHIoTkdu&gsessionid=0Jb7Oux9nhYM1fZkTCJoptl1nVm_JgZDWFk-0Eg3S69l658zai1gcQ)  
  <sub>kalkine.ca, 20 hours ago</sub>  
  What Makes the Top 5 Credit and Income Plays in Focus This Week Stand Out, and Which Looks Strongest: iShares iBoxx Investment Grade Corporate Bond ETF...
- [3 ETFs Were Paying Monthly Before the 2008 Crash. Did the Checks Survive It?](https://www.google.com/goto?url=CAEStwEBxCJF172uWBeW7OpVK0YEg7TF1F0XLqzQtEy3R4Azqihf7fqAo5Inns7bV9g3UjTqBgARXykd_dv0swP2qszmdB0Atmuk5fVZbr8eswjO_uxsr6ZrnwKlK34Djj0-2ELE6fpOXoBOlJ6NjCg39wvyc17wHYeSossax-9x6kheypjuiUhCPATZ20ipPpHNps5GSw2CNO-fWmpnDWYBarQIquUtq_7XkYcjQOm3Go3BcXOt4nzWHOo&gsessionid=0Jb7Oux9nhYM1fZkTCJoptl1nVm_JgZDWFk-0Eg3S69l658zai1gcQ)  
  <sub>24/7 Wall St., 15 hours ago</sub>  
  Retirees live on the monthly check, and 2008 tested whether it would show up at all. Three bond funds continued paying monthly when credit markets seized.
- [LQD Oct 2027 89.000 call (LQD271015C00089000) Seasonal returns chart](https://www.google.com/goto?url=CAESfwHEIkXXj53Chmgm9kZ1Zf4JPQl7SHWp-13cGWB_KV8W3DISHtjDExMjSz6lQLbkxO9vwuLyJ82xXxI6Dl6B1WfYnuLOdmKnP7nrvlJtYzTHZFMbmaxM3kCb_hv04vCKEHvGqHj7mTzNJv3aC6ppkNsU6qa4rxYStP0yQkWyqhg&gsessionid=0Jb7Oux9nhYM1fZkTCJoptl1nVm_JgZDWFk-0Eg3S69l658zai1gcQ)  
  <sub>Yahoo Finance Singapore, 22 hours ago</sub>  
  LQD Oct 2027 89.000 call (LQD271015C00089000) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [Which of the Top Three Bond ETFs Is Most Exposed to Wednesday's Fed Minutes: iShares 1-3 Year Treasury ETF (NASDAQ:SHY), iShares 20+ Year Treasury ETF (NASDAQ:TLT) or iShares iBoxx High Yield ETF (NYSEARCA:HYG)?](https://www.google.com/goto?url=CAESrQIBxCJF1xtNhoqaSOB6Kk7udNxkGxK4C7c6OciJT42jTbSFoisDhB6IYb2s2GF2pV089SLyy7B4BCdiiGt9niRic1zxuLMEhi2AzyJOjRSFS5a-PGOVBi7_dcflorFMUl_MdqBd7Pi946NrmZ2cq8gIr1AL9s1z4mQrzk8X7KTpMkDOoaGeZzLR9yA2XdJQdc0A9vQwIed0Wlt6PG4PDHbWVjtSvIMmyAAAk84dkOKr6e90oYGg_LFqrCbcRMHBVwu9jxsPxsYPvI7fXcmL9qgDGq30jV0dq6Q_eeZRE6bKvLWAHd9b6YLElARtR5n0zW8FB_NBpV5D_sHTaglCEMhq7NRsVtW-4SbI8FXg5TaPCnL52z9NYkcx40t45nNLsxnTpXPINQTdKbvkFl3a&gsessionid=0Jb7Oux9nhYM1fZkTCJoptl1nVm_JgZDWFk-0Eg3S69l658zai1gcQ)  
  <sub>Kalkine, 4 hours ago</sub>  
  Which of the Top Three Bond ETFs Is Most Exposed to Wednesday's Fed Minutes: iShares 1-3 Year Treasury ETF (NASDAQ:SHY), iShares 20+ Year Treasury ETF...
- [Which Top 3 Bond ETF Reacts Most to Wednesday's Fed Minutes: iShares 1-3 Year Treasury ETF (NASDAQ:SHY), iShares 20+ Year Treasury ETF (NASDAQ:TLT) or iShares iBoxx High Yield ETF (NYSEARCA:HYG)?](https://www.google.com/goto?url=CAESmQIBxCJF12V5JQVvBwXKyBIe8AtmaohR3tFMHJW1P_WFmBab3v4RuATWdl50CS_VTKmmQb6o0bZU4tj-3DCZ5Cp6Iuvm2-1wicESrmhOcIIi-wtjnyPhBM4g3ubYLSSUiXhiYWuDxZSV62l4QWjYOvsB3O4990YPHn3djklMZS3usoqJHcg1pIEYoHMFTJauexzghAL75JmilBhPKJfe4MsnVPYcMIfabfL6-VDEjoJdBM6D_0MNEV3Yc4kI1Kn4wnHyVASmd4ZeSto5TOYnB61hpZELo1DY_QplsQeje0uKgSJbX3F_DZ9eYSD97vHuufWLMMhhYz9-HRY8IqR1rhxdhlaF7CeDjpjOG1PkL4o-hgdPg0GHoE8P4Q&gsessionid=0Jb7Oux9nhYM1fZkTCJoptl1nVm_JgZDWFk-0Eg3S69l658zai1gcQ)  
  <sub>kalkine.ca, 5 hours ago</sub>  
  Which Top 3 Bond ETF Reacts Most to Wednesday's Fed Minutes: iShares 1-3 Year Treasury ETF (NASDAQ:SHY), iShares 20+ Year Treasury ETF (NASDAQ:TLT) or...
- [What Made Leveraged Solana ETFs Plunge About 21% as Solana Reached Its Weakest Level Since June?](https://www.google.com/goto?url=CAESygEBxCJF12dou5mflmQauHxcxcgSqniJvmbAuoJnexvOMsGrErupE3rIEsBBsX1pifZa9e8hXjjU42RsPRJVUpLmLLiOB4wEqaYw9PNSQmK4KDzA8zMTLeQsGauz3hchPYteccdaqRPoQHb-LM4C2NWbU8Tiu0kr5m5ybUPJmJ199quuhtTPuRlW4HEfI0YHnZAee--tl8BoUs-bAfscsQmC6s2O3HaLwZhShDR2pwPN5E7DkgREzFz3xBrD1sYSf_OXjUgQ4IEk93nQ&gsessionid=0Jb7Oux9nhYM1fZkTCJoptl1nVm_JgZDWFk-0Eg3S69l658zai1gcQ)  
  <sub>kalkine.ca, 20 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Has the Nasdaq Entered a Correction With an 11% Slide From Its Record, and How Does It Affect Invesco QQQ Trust (NASDAQ:QQQ)?](https://www.google.com/goto?url=CAES4wEBxCJF1yVfYJjA8sSS-pMmYCtmP93FXzrHgMK28atSctO-vm8lYaQBazhPMvyBvxAIrGkeXBaz6FS5acaQzO9pSw7AlGSPh9sEsUMI6eD08gJqhsP0CYOV1vJFP5ZI9ZgHNi_DN3K6KD4F2K8stogy46l6ucan6t6ACWwAm_jpqSaS0MFlRspvOb2VcIk3ksw9HslWzrqQP4zJ3lS3qmEdPGWT2rmRzsBnwq5JqGtccwjNrdCHkcwFB1dLJ4o_X3sbqIK9vzhfxkgJx-URrcptqcqu-l39Nw6NdQAdMgO0bO6fCA&gsessionid=0Jb7Oux9nhYM1fZkTCJoptl1nVm_JgZDWFk-0Eg3S69l658zai1gcQ)  
  <sub>kalkine.ca, 20 hours ago</sub>  
  Has the Nasdaq Entered a Correction With an 11% Slide From Its Record, and How Does It Affect Invesco QQQ Trust (NASDAQ:QQQ)?

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 103.08 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 103.86 (-0.7%), 50d 103.50 (-0.4%), 200d 107.24 (-3.9%); 50d below 200d
Momentum: RSI(14) 43.4 | MACD -0.163 vs signal -0.005 (histogram -0.158)
Returns: 1d +0.3% | 5d -0.8% | 1m -0.1% | 3m -2.8%
52-week range: 101.83 - 112.05 (now 12.2% of the way up)
Volatility: ATR(14) 0.55 (0.5% of price) | annualised 20d 7.1%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Corporate Bond
Yield: 4.8%
Credit quality: A 46.4%, BBB 40.8%, AA 11.7%, AAA 1.2%
Three-year record: +4.2% a year | beta to the market 1.32
Cost and size: expense ratio 0.14% | net assets 32.00B
What it is made of: Bonds 99.2%, Cash 0.8%, Convertible 0.0%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 0.5%
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
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 293.50M | fund size: 30.25B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral outlook as macro data shows modest yield rises without surprise, positioning indicates slight bearish bias but unchanged, technicals are near neutral, and fundamentals remain stable.

**Main reasons it gave:**
- 10-year Treasury yield rose 10 bps this week to 5.10%
- CFTC data shows net short 33.5% of open interest, down 1% week-over-week
- Technical indicators near neutral: RSI 49, MACD slightly negative, price just below 20‑day SMA
- Fund basics unchanged: yield 3.6%, AA credit quality, low beta 0.25

<details><summary><b>News</b> — score +0.00</summary>

- [Which of the Top Three Bond ETFs Is Most Exposed to Wednesday's Fed Minutes: iShares 1-3 Year Treasury ETF (NASDAQ:SHY), iShares 20+ Year Treasury ETF (NASDAQ:TLT) or iShares iBoxx High Yield ETF (NYSEARCA:HYG)?](https://kalkine.com.au/news/economic-news/which-of-the-top-three-bond-etfs-is-most-exposed-to-wednesdays-fed-minutes-ishares-1-3-year-treasury-etf-nasdaqshy-ishares-20-year-treasury-etf-nasdaqtlt-or-ishares-iboxx-high-yield-etf-nysearcahyg)  
  <sub>Kalkine, 4 hours ago</sub>  
  Which of the Top Three Bond ETFs Is Most Exposed to Wednesday's Fed Minutes: iShares 1-3 Year Treasury ETF (NASDAQ:SHY), iShares 20+ Year Treasury ETF...
- [Which Top 3 Bond ETF Reacts Most to Wednesday's Fed Minutes: iShares 1-3 Year Treasury ETF (NASDAQ:SHY), iShares 20+ Year Treasury ETF (NASDAQ:TLT) or iShares iBoxx High Yield ETF (NYSEARCA:HYG)?](https://kalkine.ca/news/economic-news/which-top-3-bond-etf-reacts-most-to-wednesdays-fed-minutes-ishares-1-3-year-treasury-etf-nasdaqshy-ishares-20-year-treasury-etf-nasdaqtlt-or-ishares-iboxx-high-yield-etf-nysearcahyg)  
  <sub>kalkine.ca, 5 hours ago</sub>  
  Which Top 3 Bond ETF Reacts Most to Wednesday's Fed Minutes: iShares 1-3 Year Treasury ETF (NASDAQ:SHY), iShares 20+ Year Treasury ETF (NASDAQ:TLT) or...
- [Can Musalem's Case for Up to Four More Hikes Weigh on iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY)?](https://www.google.com/goto?url=CAESyQEBxCJF1zoCuTnkfbxQCUb3u0CHwj75SA7We2CCe7KezcKGj9mh5JG2qWt_AJY0-wKsjZBvURa87phqu7nrtcn6L1j8ReqNk38C0rX-5EwR2JeB8Dv8lOG4f96j20miKGJxPF9l39qeKDzwuO0_mQMBn3TAM68cyHqi9tchJW0A02Luv1VDS4BHeKyTC84CSeHwTVk9j0fBdpBYs9X-hXfR437FbngJFKf0JHnwSIoX63ohoXVydX7D6hpudjm9uWhdRnzQUwwCxN0&gsessionid=AHMxQgcE5cGA1xOtWrVYxY_WpROdVBKNq_WvBP0V5Voy-jgwOwiayg)  
  <sub>Kalkine, 4 hours ago</sub>  
  Can Musalem's Case for Up to Four More Hikes Weigh on iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY)?
- [How Might Musalem's Push for Up to Four More Hikes Affect iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY)?](https://www.google.com/goto?url=CAESyQEBxCJF1_4yhWTzx7VB1NKfHLNKohrs6xz9fWgIF9iFR-MZSebT9_V8HsHT09K8miLUxdRDLdX2iDQOcfHn1drLdJlGfg_w31nKeX7iZ8RTQZOkQxNpC7M1ynZws4daH3Q-k5mUjabv7Un9h30vVzXBzOtvX7dG3_kdh7RXnG6Y9xM3G6NSsVSpdZ1PQkKHw5MbKYWobhcTCdj0Df36cxfc00Jk5vWjMWXYAeymRtr6iOlKenV4ZcK-ZX85vHOJjzR8Oi7xv-GlazI&gsessionid=AHMxQgcE5cGA1xOtWrVYxY_WpROdVBKNq_WvBP0V5Voy-jgwOwiayg)  
  <sub>kalkine.ca, 5 hours ago</sub>  
  How Might Musalem's Push for Up to Four More Hikes Affect iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY)?
- [1. iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT)](https://www.google.com/goto?url=CAESowMBxCJF1zR59lCaSr4xCfF6eJi7f7qN5ylmDjPPROIN7RsLWYaUBTPfSZVewmRYowqXUY8EAeKGhRQpocMWd1R7PI4N0bSbgPXeyV5KBSaACGX7xiGS1FFUxW-nCPPT7KK_cmFDDvP2RAIpPXRl33r6lfINOAYPq79KGOhw-JfwUH3Qn8RdI9l__DzQa_LSAjaVIEMC_fA0Ae-Oa2EoarKP_Jq44oDT3RyBiWYfry3HyYRIncUEl7eTK4uDZXt8UAHj5Eji8aMvKXnbu8-YYhJvExdXOwIdpPHUg_c0kCgvAsceEjceoi9ohK0pA6vDxJNwsptr2IPvhTmyYyHeB6O1rqHbdtQLqKRDAYMY6k9cA2JHm7CJKJEO93_O0qznnEpYkVSIvgA6a8mRkkfTt2145zl-MVEpgnLJADlo_MGSezR0QyU461LCfBkWbfAFMgnweINFFbR0n1qrFmFOqj9A04wZ7g2ZxR6bLMOSSQ2OVyE5BU0DmX5Xt7iIbdHqrzx_6YFTh22o04mHXWGgquS93chtvUqVRmD8jDm2w0gu1dFQ7Q&gsessionid=AHMxQgcE5cGA1xOtWrVYxY_WpROdVBKNq_WvBP0V5Voy-jgwOwiayg)  
  <sub>kalkine.ca, 20 hours ago</sub>  
  Of the five, iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) is the most sensitive to rates. Because it holds Treasuries with maturities of 20 years or more...
- [What Might Waller, Hammack and Williams Signal Today for iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY)?](https://www.google.com/goto?url=CAESyAEBxCJF19zbZICNN4IpMn2AEDOZCkmIk5Di4Ii_vV8S3Rrkb4q5Iuo8vTci-noKsX8HBVUS0u5m8L2cRZagZ_XzhnZDvAqs1m5CHrbshpujLByaefpqBWyvJE7-bnH2-52m919ikRwYWDvD_9Bte-WOgvfO9-eHPTFDxkl3ifcV9tlRGTHuW26ZBhc5kzxIzopwBNrqwtU49wcyb8k4L8--77mHWv0AnR44M7BQvhdmaIH7_ukxwuHzEntvIb2rlnYMmqiz_W-uog&gsessionid=AHMxQgcE5cGA1xOtWrVYxY_WpROdVBKNq_WvBP0V5Voy-jgwOwiayg)  
  <sub>kalkine.ca, 20 hours ago</sub>  
  What Might Waller, Hammack and Williams Signal Today for iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY)?
- [The Government Spends About $5.5 Billion a Day More Than It Takes In. The Debt Has Doubled in 10 Years. Jaime Dimon This the Situation Could Get Much Worse.](https://www.google.com/goto?url=CAEShAIBxCJF1xz6R1R_MiVt8iLkT8tIayvCE30nAZIZvOz-3zuQLvTkqXScnnzNZ5JkVmCUIfPU3_Cn68Hzadt4f6bLP8n5TjWbJaSf0MvqnkKs7WzXARTVLqAV5rbqs2YGigxH5NILw7AjMr7i_5a_bDHE4JpfPfV9XoS2v_MNUcLSDa9FT_PfEdXRej1lgYAvtTamze6g3EwGZDaz6P2RVuAbo10KFvR6XPAdj84aHSMhStPl1rDHNaUAJRn9dZ-j9UTvKGbdG1H-Pha5ElHYIAymtVnaP3HBrEeSMlto1YiQMIldTrxjiMjGEst3CMAqy2mRnuzogOoNtc_n6--ycCFsFFBQTg&gsessionid=AHMxQgcE5cGA1xOtWrVYxY_WpROdVBKNq_WvBP0V5Voy-jgwOwiayg)  
  <sub>24/7 Wall St., 18 hours ago</sub>  
  Washington's debt has doubled to roughly $40 trillion in a decade as spending outpaced revenue, and interest costs now feed even more borrowing.
- [Is iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) Vulnerable as the 10-Year Yield Holds at 5.10%?](https://www.google.com/goto?url=CAESvwEBxCJF1xscJZpY2tI_oJX5hI_k5E7AcCfjQF9adUkyR8JV6YXnsk53Jwd54_x7hPDO_2ylVrf6LG3D49-TJNHLLsEP3ntdMAKcWFgXYKKbu-KtU5-HH1euJdewOKbGyKivkxh-7rtncAKNIvuBSLAP0Ldz4FCaGpAMKtJF0Ow3b9d_SMLqsf4q7nQOoQaFa206D8mb2Cu3D71rbs1j61MJdTRLPk4DY0f3RgM2it5NtM2qJjmvqFeOt4fQRIvf5w&gsessionid=AHMxQgcE5cGA1xOtWrVYxY_WpROdVBKNq_WvBP0V5Voy-jgwOwiayg)  
  <sub>kalkine.ca, 5 hours ago</sub>  
  Is iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) Vulnerable as the 10-Year Yield Holds at 5.10%?
- [Could the Fed Minutes Shift iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) as a December Hike Trades Near 95%?](https://www.google.com/goto?url=CAESzQEBxCJF1-GID5uK3qO0DRjcpHGLGmBC_4XqWQxv-rrsiJSi6Wh5nKAPyDa3Wz6iAmMbZ9Bhtfq6YSFn78TiHviWdCADEoNfgIKJkpiIVlvWUyaSKN5G4hQXAjzocrTh4F2fDSInOQJGhjs7kgsBf-D24Y9GxGse9_cqOiT53JX8F6xiJ-8Q2u3GJbgHNDuNrmREjhkZKWKh-WZ5I5u7kmB6HX1bXtLRtBoA_S_UStTVk8tQGMlo0W8AIFmaCw-1HZ_AQpKZB7lD_dsK7_Vb&gsessionid=AHMxQgcE5cGA1xOtWrVYxY_WpROdVBKNq_WvBP0V5Voy-jgwOwiayg)  
  <sub>kalkine.ca, 5 hours ago</sub>  
  Could the Fed Minutes Shift iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) as a December Hike Trades Near 95%?
- [How Could a Second Straight 1.1% Import Price Gain Shape the Outlook for iShares TIPS Bond ETF (NYSEARCA:TIP)?](https://www.google.com/goto?url=CAESzAEBxCJF14Y2ObUXs9Da-KmlfzjdgzplTQfRzfcbPQ1pNuRO0qzTBpWHzKKHhpNkeFZ7xXHlTj_2rsocGHgi1Gpd-wAMIgnfmErRmVRcJq_eQ6EW2AnM9GtIBgj3bJR14jzjOyD81ZJB1trchJ-9HKg2Q4pLZfXfTZHREVsUa-Hn9zJZqfH50ni643LXtLMkMX8M1KHKGiRiwL--RI67aMmTlrt0jFAzTxvNgXsp8m3d4kb8IMI3mDeO3JahpeXHPoI6po1JDzM_rlBmT3E&gsessionid=AHMxQgcE5cGA1xOtWrVYxY_WpROdVBKNq_WvBP0V5Voy-jgwOwiayg)  
  <sub>kalkine.ca, 5 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports. Become a Kalkine member...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.36 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 81.44 (-0.1%), 50d 81.31 (+0.1%), 200d 82.02 (-0.8%); 50d below 200d
Momentum: RSI(14) 49.0 | MACD -0.024 vs signal 0.001 (histogram -0.026)
Returns: 1d +0.0% | 5d +0.1% | 1m +0.1% | 3m -0.8%
52-week range: 81.05 - 83.18 (now 14.3% of the way up)
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
Three-year record: +3.8% a year | beta to the market 0.25
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.25</summary>

```text
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 33.5% of open interest (4,489,282 contracts)
Change on the week: -1.0% of open interest
Crowding: 77% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.25</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 209.30M | fund size: 17.03B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; modest bearish signals from rates and positioning are offset by lack of any material macro surprise or decisive technical break.

**Main reasons it gave:**
- 10-year Treasury yield rose 10 bps to 5.10% this week (rate increase, bearish for bonds)
- Large speculators net short 33.9% of open interest (bearish positioning)
- TLT price below 200‑day SMA and RSI 46.3, indicating slight downside momentum
- No major macro surprise or data release deviating from expectations this week

<details><summary><b>News</b> — score +0.00</summary>

- [Is iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) Vulnerable as the 10-Year Yield Holds at 5.10%?](https://kalkine.ca/news/economic-news/is-ishares-20-year-treasury-bond-etf-nasdaqtlt-vulnerable-as-the-10-year-yield-holds-at-510)  
  <sub>kalkine.ca, 5 hours ago</sub>  
  Is iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) Vulnerable as the 10-Year Yield Holds at 5.10%?
- [How Exposed Is iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) With the 10-Year Yield Near 5.10%?](https://kalkine.com.au/news/economic-news/how-exposed-is-ishares-20-year-treasury-bond-etf-nasdaqtlt-with-the-10-year-yield-near-510)  
  <sub>Kalkine, 4 hours ago</sub>  
  How Exposed Is iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) With the 10-Year Yield Near 5.10%?
- [3 ETFs Were Paying Monthly Before the 2008 Crash. Did the Checks Survive It?](https://www.google.com/goto?url=CAEStwEBxCJF16B1sXcAW33HgxG8L2T4_6pT7bQ0nePuaB5h581lg40ONCaa6nif5tyQef-R4pr_eCk3sg0cewRjyXXfK-YQG8BuCgiC64ZG-UrmCC3ky5ahwAU5MvxRYlWTK9JDya_1cdE0v890A78i2DQGjLKLOk17D0V4FGFPnDacA01w6jg9YwYvDiL4pQ1Fyu9YdXN5bRRtfay2Kdi_PqOVvp0KW24JUUkisa4G8YW-jPRaDiBh8Zc&gsessionid=U0hB1SB5icpUECspxToiPe4jKzvoTnN_ZiIIaDHYVgQv8ZGqS4-aAg)  
  <sub>24/7 Wall St., 15 hours ago</sub>  
  When the paycheck stops in retirement, the real test of a monthly income fund is what its check does in a crash. Three iShares bond ETFs were already paying...
- [Which of Five Market-Moving Events on November 18 Matters Most: iShares 20+ Year Treasury ETF (NASDAQ:TLT), Anthropic (NASDAQ:ANT), Palo Alto (NASDAQ:PANW), Everpure (NYSE:P) or Target (NYSE:TGT)?](https://www.google.com/goto?url=CAESkgIBxCJF13ow5nXgwZtO43131iH4FNX446sXHxJLmT4rZ523_2I_W-KLnMJGbaCqeLWTPJpXm9LqGJDXiuNfO7YA5SiXLxGh85SPQJPy_Qg5mxd0PAuHenNI0j9nD8LaO2HC_lP7qYquqZahhugLE20ARYZ04diS-QXuOYQ2cVK3n4lXxPRmFHQTsncDzsgWrz0wrbA6Td8ScwmB7XhYzV4pS6f6ax021yuCdG8erxqmmCJFTtYqNc9eKMm4PfenRZR2ZuKLbvsx3MTxDVWQtSeBgrblWybrlsP8Shj0QM_6xlAzPcKxSY_HS33O4fT_J-VfnhzHFBqrS7TLGHEqJ3lg_2LdvOatn-TBNintq7048OtM&gsessionid=U0hB1SB5icpUECspxToiPe4jKzvoTnN_ZiIIaDHYVgQv8ZGqS4-aAg)  
  <sub>kalkine.ca, 5 hours ago</sub>  
  Which of Five Market-Moving Events on November 18 Matters Most: iShares 20+ Year Treasury ETF (NASDAQ:TLT), Anthropic (NASDAQ:ANT), Palo Alto (NASDAQ:PANW),...
- [Which of Five Market Events on 18 November Could Shift Prices Most: the 20+ Year Treasury ETF (NASDAQ:TLT), Anthropic (NASDAQ:ANT), Palo Alto (NASDAQ:PANW), Everpure (NYSE:P) or Target (NYSE:TGT)?](https://www.google.com/goto?url=CAESlgIBxCJF11bMSFFZEM55g2wtCTU2Zxy1AIe4e93w-yQnwWVf8fW4iGi1--Au0c3cIJUZ_6dQfP4XuOgiXK0Rj5NCTs6UwF3UiyHHZL4QPCZ_p-uKGGiyfJoYPINJO8UQxwsd5iGkw4m_0SRlMCC04C0DR6VhjKz_X-k6w7JqYfck83v-aNBoVVm0S5o5bObl_qvveZijzT-jwNADPQfXUCcfaoofdrNeQzFDws4nZJBrsXDzVVdRjF-rNdpoRsiwyZsIW6t5LzTNC4E5dHG7RnPtt03HK0G0_1vYHMBnazPhOV_XEtzquM9Nc7E-LFmDQVnSoBb-RILQtYllpyGNgITQ3Msax62T_95tbReRT1jYQD8HegZctw&gsessionid=U0hB1SB5icpUECspxToiPe4jKzvoTnN_ZiIIaDHYVgQv8ZGqS4-aAg)  
  <sub>Kalkine, 4 hours ago</sub>  
  Which of Five Market Events on 18 November Could Shift Prices Most: the 20+ Year Treasury ETF (NASDAQ:TLT), Anthropic (NASDAQ:ANT), Palo Alto (NASDAQ:PANW),...
- [Monthly payouts from three key bond ETFs survived the 2008 crash, showing resilience in crisis income streams.](https://www.google.com/goto?url=CAESlgEBxCJF17KeoC7WYaoaZJKBzD4uZZJQjVfuvCk-D-dlgSyiehI3kTRvT5E9y_hj9wV5vOdCh3CSpnuBvrmpio_xWr_A_Jf1MyygY5pNmD0yzbfWMCdibOeA4qKH0AKvDE6kZvxCPlue8E05RzzifHNQjfaO2xPJ7wgH6gqccXbTdLwrIA78bdkWkojL0WBcHX5kw2tZV7c&gsessionid=U0hB1SB5icpUECspxToiPe4jKzvoTnN_ZiIIaDHYVgQv8ZGqS4-aAg)  
  <sub>Pluang, 15 hours ago</sub>  
  Three iShares bond ETFs—TLT, HYG, and EMB—that paid monthly distributions before the 2008 financial crisis continued to deliver income checks through the...
- [Can Minutes From the Fed Shift iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) While a December Hike Sits Near 95%?](https://www.google.com/goto?url=CAES1QEBxCJF1wKdwx9UjJmzvXoAZuA02IF916U40J9efUJP2yT7uKPC5N4dx2rXZAXo821eRfTpBmmC_KVF3whw-pR5qQ7EQocqd-dEB2FOwcTyShE_llojPqV4pqHjq6C5dVXKBNOg1-dRwO3nhezCRyKfhNyjsRSxH7bbYQ6W0s0Xzs0UnWa3nSuJGjrf-SieSGcjnKFWno27OynPqzdo_mYwR7EuevaumLZ0AatCudyJR1Tiv2YPCEPc9wcRvlZuxna1tYc1hkgIuqEXtP6V53NdRRCphS0&gsessionid=U0hB1SB5icpUECspxToiPe4jKzvoTnN_ZiIIaDHYVgQv8ZGqS4-aAg)  
  <sub>Kalkine, 4 hours ago</sub>  
  Can Minutes From the Fed Shift iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) While a December Hike Sits Near 95%?
- [Which Top 3 Bond ETF Reacts Most to Wednesday's Fed Minutes: iShares 1-3 Year Treasury ETF (NASDAQ:SHY), iShares 20+ Year Treasury ETF (NASDAQ:TLT) or iShares iBoxx High Yield ETF (NYSEARCA:HYG)?](https://www.google.com/goto?url=CAESmQIBxCJF1zZoS04Q5zKpp-gRc9ikNtHst0MQipduC6ZZXHsezAi2R5Ti-EN_seD-el6clbGno_d9bbfFbuCmyRo4IT-gAmMu3XaWdhwFXtE9UAZ5rYdbbxOOzCgVHPQetGnO60Lb8OkMWpB4JhjDPaKzOxm-gwFQR_ETpH2jKbSNrmkKHtIVlar2io7uB5A2VY0RPcX1erU7GMLV0yBEobR_6TBgJEwO2JL-aAuHIHPngFJj6m4xjTkpoP6gsW81aE_c0aKnzkzBEIsTb5I6UI8G9ChJ1GWr5WFdD3vM2uX52orZpIYFVdOVaBVU_zyp2a2IFqD8WdqTlTCTBtoZNWi43-bMOBK6PDLqJYQZgP3VsojZFIrRib1jsg&gsessionid=U0hB1SB5icpUECspxToiPe4jKzvoTnN_ZiIIaDHYVgQv8ZGqS4-aAg)  
  <sub>kalkine.ca, 5 hours ago</sub>  
  Which Top 3 Bond ETF Reacts Most to Wednesday's Fed Minutes: iShares 1-3 Year Treasury ETF (NASDAQ:SHY), iShares 20+ Year Treasury ETF (NASDAQ:TLT) or...
- [Which of the Top Three Bond ETFs Is Most Exposed to Wednesday's Fed Minutes: iShares 1-3 Year Treasury ETF (NASDAQ:SHY), iShares 20+ Year Treasury ETF (NASDAQ:TLT) or iShares iBoxx High Yield ETF (NYSEARCA:HYG)?](https://www.google.com/goto?url=CAESrQIBxCJF13FRgk7ZyeErh8L68oyLpdPD7GsIxt_bVjvvRsBPzxPG-8t3jynw4P9jSrHn4zTmiTTsagCkmRDNqZ-Yb3hCAPFFzCoEJ3RQFE_kmxZL26o54Xuh-b7Xi6W787cqCu5OWFGd1R0kjiet3SiXOVWYYkkfBwx7jGCbkWf8iR1tb3u1oJK2VyYJHuNfKJbs1Z5QC5F1OTrNwBLiyubGtVwsNzuyjnSqJfo9C-Izb07fxqDS1tHHwc5D5p6dr-cPUjeHKkQty3m8gmSzZTa49AgC5e1tnxFJdBxgu4s71efV5agbUbUBqQBBzOtqhSRwL4uCZtt1YYHSFjn1RlGVLC4wF6IgYicn3miqQ2PcggghX7278Au2-EKn7Lai8dyfdiiPYexU3rcw1ujx&gsessionid=U0hB1SB5icpUECspxToiPe4jKzvoTnN_ZiIIaDHYVgQv8ZGqS4-aAg)  
  <sub>Kalkine, 4 hours ago</sub>  
  Which of the Top Three Bond ETFs Is Most Exposed to Wednesday's Fed Minutes: iShares 1-3 Year Treasury ETF (NASDAQ:SHY), iShares 20+ Year Treasury ETF...
- [1. iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT)](https://www.google.com/goto?url=CAESowMBxCJF15Cu9pW1RHMynBXFzLmtLM4HQneoGMFXI085RHfj7zWJ-x6RMpwAKRt1lkt7YXLL3G1JNFPP-COkK48bXLC6u6Q54zLYz4RHT_CEcyf9uvEvhn1vNcc4otiHyegU8aNTodECpTSS0sQ53cCokj6zTuYKfy7XngMnuov6OE8Uz752O0CLDptXYr0CtWGGU4imDHWuJPJcU_n1ZlzPtn2LZFz1Tbt8eYXfCkE5L0j46YbWYIZMrn1sBQo2F9cNWAh79GvhFW8aqSoFMxNcAVL0BO6-zVGjwxAyUCLOeGWmeGmgB9yj3SYfqwfSUONTqXXMU5Ym1rV7GjOr30eeN1INppJtHvt_U9InPBmTaWDdrVDO5NwRpQfyjLcP5IA56Ohn43IOoxeVHLyMKB4p124t0ykuo3WoVZi8xI5VnvV3B0RsTl-mB6q4ACRHnGtueIrKgbhg-k27r__rsEYvLvf1UvD1yk6GVOH-KzMcVxACoVkK2sixIACPf2eC8pw4q3LlOWhYGQhnUIS-l_HlZAL7xNiUAg76itbKkN29rODDrA&gsessionid=U0hB1SB5icpUECspxToiPe4jKzvoTnN_ZiIIaDHYVgQv8ZGqS4-aAg)  
  <sub>kalkine.ca, 20 hours ago</sub>  
  Of the five, iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) is the most sensitive to rates. Because it holds Treasuries with maturities of 20 years or more...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 80.08 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 81.05 (-1.2%), 50d 80.07 (+0.0%), 200d 84.19 (-4.9%); 50d below 200d
Momentum: RSI(14) 46.3 | MACD -0.108 vs signal 0.145 (histogram -0.254)
Returns: 1d +0.7% | 5d -1.0% | 1m -0.1% | 3m -2.7%
52-week range: 77.11 - 90.82 (now 21.7% of the way up)
Volatility: ATR(14) 0.74 (0.9% of price) | annualised 20d 12.1%
Volume: 0.13x the 20-day average
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

```text
Contract: ULTRA UST BOND - CHICAGO BOARD OF TRADE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 33.9% of open interest (2,403,991 contracts)
Change on the week: -0.7% of open interest
Crowding: 48% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 109.70M | fund size: 8.79B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: dollar index up modestly, UUP at 52‑week high with overbought RSI and low volume, slight unwinding in speculator positioning, mixed fund flows. No macro surprise or decisive technical break.

**Main reasons it gave:**
- US dollar index rose 0.88% on the week
- UUP at 52‑week high; RSI 70.6 (overbought) and volume 0.06× 20‑day average
- CFTC speculators net long 5.5% fell 1.2% week‑over‑week
- Fund flows: week share count down 1.9% but month up 10.1% (mixed demand)

<details><summary><b>News</b> — score +0.00</summary>

- [US Dollar ETF (UUP) Hits New 52-Week High](https://www.zacks.com/stock/news/3031782/us-dollar-etf-uup-hits-new-52-week-high)  
  <sub>Zacks Investment Research, 34 minutes ago</sub>  
  For investors seeking momentum, Invesco DB US Dollar Index Bullish ETF ( UUP Quick Quote UUP - Free Report) is probably on the radar now.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.58 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 29.15 (+1.5%), 50d 28.89 (+2.4%), 200d 28.07 (+5.4%); 50d above 200d
Momentum: RSI(14) 70.6 | MACD 0.182 vs signal 0.137 (histogram 0.045)
Returns: 1d +0.1% | 5d +0.8% | 1m +2.4% | 3m +6.0%
52-week range: 26.47 - 29.58 (now 100.0% of the way up)
Volatility: ATR(14) 0.12 (0.4% of price) | annualised 20d 5.3%
Volume: 0.06x the 20-day average
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
Three-year record: +4.9% a year | beta to the market -7.93
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
Share count change: 1 week: -1.9% (-9.49M) over 7d | 1 month: +10.1% (44.39M) over 32d
Shares outstanding: 16.30M | fund size: 482.22M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Technical trend: price below 20‑day, 50‑day and 200‑day SMAs; RSI 42.3 and MACD negative
- Macro backdrop: rising US Treasury yields, higher VIX and a stronger dollar suggest risk aversion
- Analyst coverage thin (12% of fund) despite 83.8% buy rating and +24.7% price target
- Positioning: modest net long (2.8% of OI) with a +5.4% weekly increase, indicating limited bullish bias

<details><summary><b>News</b> — score +0.00</summary>

- [Vanguard FTSE All-World ex-US Index Fund ETF Shares (VEU) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/VEU/)  
  <sub>10 hours ago</sub>  
  Find the latest Vanguard FTSE All-World ex-US Index Fund ETF Shares (VEU) stock quote, history, news and other vital information to help you with your stock...
- [ETFs Investing in IG Group Holdings plc Stocks](https://www.tradingview.com/symbols/BX-IGG/etfs/)  
  <sub>3 hours ago</sub>  
  Explore funds investing in IGG in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [Morgan Stanley Sees 22% Upside for Japan ETFs in 2027 - iShares MSCI Japan Index Fund (ARCA:EWJ)](https://www.google.com/goto?url=CAES2AEBxCJF1xy7UTXgDHGKO-psrEtozSsxZu1INNSPqBqAFUOcjYcZAEHH9tafIDhqIyg7blRoY6CZlngH-gLy2gXp6yFu1C4BMgL6lE1uAprGgWHOELymAhQra7GWWBw6ouDLdXmEl7_tzjpE5HR4GCVh2yqshAk5PNt7YOKnIKWkif2puhuCVEYl8lSDFvGBl0uQCju_mnBxR2EPLaHBRHd7vQWBZ25-kdnluSeG9XGB8v2c9v4JJc0qE1D4ldxlpX_2PiT4jp-okCuFIA7OXTQ-E8IrSNyhHSc&gsessionid=KBDGpwVUICvd2N4PXp4Twk2V-IMx8zcvYZGxyJvueMc2dXYU8sbt0g)  
  <sub>23 hours ago</sub>  
  Morgan Stanley sees 22% upside for Japan's TOPIX in 2027, putting Japan ETFs in focus as global investors look beyond the S&P 500 for bigger gains.
- [AstraZeneca Announced Two Approvals in One Day. The Stronger Evidence Belongs to the One Getting Less Attention.](https://www.google.com/goto?url=CAEStwEBxCJF16dFVzLceUR6QWMM8lv17i-bL_7Paj5mUFV-pChIwxgOHL959T3kngWhJPAljmHSlngoma-i6YpTbOrlCeQsgxnav2la0b_vyb__W0TZ3nJmM2m76rKVigDd4uKxhh7hvB1zFhfMelF72ew_sjY7UEB-hw3ezz2vLYFT7A3thtsPdIRO8wb-0OxhyrmAsnR3ruwbRTzOyTIEs2N3z_RCbCAlwChwBI31FmDTtWysw35-9oE&gsessionid=KBDGpwVUICvd2N4PXp4Twk2V-IMx8zcvYZGxyJvueMc2dXYU8sbt0g)  
  <sub>22 hours ago</sub>  
  Klygefa beat placebo in myasthenia gravis, yet its gain of 1.6 points on a 24-point daily-function scale is no better than the 1.7 points AstraZeneca'...
- [Morgan Stanley Lifts Japan to Overweight, Sees 22% TOPIX Upside by End-2027](https://www.google.com/goto?url=CAESgAEBxCJF168N20ZvgCkbpmRBmf1vXBSw3T2yUQVDY-VP0GrQ_FwQ8PBfAUZXo2CFmdx3pl5aT1V4yRaaKs3vvAF2a_ZtSIsbk6lXTehJ3QdFlG6jhCJpgojDo4QaI6VPLuoKW4VpJUu4x4ClNv_aoHDt48_4T9HAkzE73DmZC-6AtA&gsessionid=KBDGpwVUICvd2N4PXp4Twk2V-IMx8zcvYZGxyJvueMc2dXYU8sbt0g)  
  <sub>23 hours ago</sub>  
  Morgan Stanley has upgraded Japanese equities to overweight from equal-weight and lifted its December 2027 TOPIX target to 4800, about 22% above the…

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 86.35 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 87.98 (-1.9%), 50d 87.71 (-1.6%), 200d 87.95 (-1.8%); 50d below 200d
Momentum: RSI(14) 42.3 | MACD 0.053 vs signal 0.233 (histogram -0.180)
Returns: 1d -0.7% | 5d -3.5% | 1m -1.0% | 3m -6.2%
52-week range: 77.90 - 93.19 (now 55.2% of the way up)
Volatility: ATR(14) 1.08 (1.3% of price) | annualised 20d 20.6%
Volume: 0.05x the 20-day average
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
Three-year record: +17.2% a year | beta to the market 0.88
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 12.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 83.8% | hold 16.2% | sell 0.0% (mean 2.08 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.7% above the current prices
Holdings read: ASML.AS, ROP.SW, SHEL.L, NOVN.SW, HSBA.L
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-11-10, published the following Friday)
Large speculators: net long 2.8% of open interest (506,737 contracts)
Change on the week: +5.4% of open interest
Crowding: 87% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 282.09M | fund size: 24.36B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US Treasury yields rose modestly (3‑month +0.03, 10‑year +0.10) with no policy surprise
- Price below 20‑day, 50‑day, 200‑day SMAs; RSI 33.7 (oversold) but volume 0.05× 20‑day avg
- Analyst view thin (23.5% of fund) – 100% buy, price target +65% above current
- CFTC positioning: net long 2.1% of OI, weekly increase +1.0% OI, low crowding (30th percentile)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 53.84 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 55.96 (-3.8%), 50d 58.13 (-7.4%), 200d 58.26 (-7.6%); 50d below 200d
Momentum: RSI(14) 33.7 | MACD -0.928 vs signal -0.839 (histogram -0.089)
Returns: 1d -0.8% | 5d -5.9% | 1m -7.6% | 3m -10.3%
52-week range: 52.42 - 61.44 (now 15.7% of the way up)
Volatility: ATR(14) 0.89 (1.7% of price) | annualised 20d 24.7%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Diversified Emerging Mkts
What it holds: P/E 16.13 | P/B 2.13 | P/S 1.85 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +14.0% a year | beta to the market 0.78
Cost and size: expense ratio 0.06% | net assets 153.78B
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 23.5% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.32 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +65.2% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 2308.TW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-11-10, published the following Friday)
Large speculators: net long 2.1% of open interest (1,072,382 contracts)
Change on the week: +1.0% of open interest
Crowding: 30% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 1.42B | fund size: 76.35B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: the streamed answer ran past the 480s ceiling (gave up after 2 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Invesco S&P 500 Equal Weight ETF (RSP) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RSP/)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Invesco S&P 500 Equal Weight ETF (RSP) · -2.32% · 0.78% · 7.05% · 11.67% · 15.17% · 33.07% · 754.50%. Key Events. Baseline. Advanced Chart. Loading...
- [EQWL: An Alternative To Conventional Large-Cap Exposure](https://www.google.com/goto?url=CAESnAEBxCJF18FwcXR3NOXLUrrcYWAH_mLS4O6qLqcXj1YtbruaKziT-MsGbQt20Ba5ZUdyz3iC7KIf5xhxtukMXa9D2pPOc1SAuxmqSb73yS8YJ5BzP4zwyhj6mOjjCr3Js4fdCEueeOOtWuOB0zlfeMPts41zS4RrH5OBRIARSSyjQOzF9SGcqyt4ex845JLObsFpTP9oxNxZAy1ie1c&gsessionid=iBZoF4XAgbLIWhsLJc-ruyIavEVO5W7WJO0GSRRFQtOcXK1GsYxSTg)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  Invesco S&P 100 Equal Weight ETF (EQWL) deserves a look given its attractive valuation, favorable earnings prospects, and diversification away from big...
- [NVR, Inc. (NVR) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXXYh71T01VuKJl1XDGdh9hnL7irRvA7zXuD0H0mkjsov_8cYvGqUISPyJwlLFS6nAYUviOH620vaZqoIPDYplNUT1gtwqpFwkP_h26tTsZ01p6e9iLwxR3yg1c8ofj8yg&gsessionid=iBZoF4XAgbLIWhsLJc-ruyIavEVO5W7WJO0GSRRFQtOcXK1GsYxSTg)  
  <sub>Yahoo Finance UK, 10 hours ago</sub>  
  Find the latest NVR, Inc. (NVR) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 215.57 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 218.87 (-1.5%), 50d 214.98 (+0.3%), 200d 209.13 (+3.1%); 50d above 200d
Momentum: RSI(14) 45.3 | MACD 0.780 vs signal 1.358 (histogram -0.578)
Returns: 1d -0.1% | 5d -3.2% | 1m -0.1% | 3m -2.1%
52-week range: 182.18 - 223.33 (now 81.1% of the way up)
Volatility: ATR(14) 2.65 (1.2% of price) | annualised 20d 18.4%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Large Blend
What it holds: P/E 19.93 | P/B 2.93 | P/S 1.83 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +16.6% a year | beta to the market 0.80
Cost and size: expense ratio 0.20% | net assets 100.66B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Moderna Inc 0.3%, PTC Inc 0.3%, Accenture PLC Class A 0.3%, Gartner Inc 0.3%, Hasbro Inc 0.3%
Sector mix: Technology 16.9%, Industrials 15.1%, Financial services 13.9%, Healthcare 12.9%
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
Rolled up from the 5 largest holdings, 1.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 38.4% | hold 61.6% | sell 0.0% (mean 2.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -1.2% above the current prices
Holdings read: MRNA, PTC, ACN, IT, HAS
Recent rating changes among them:
  - MRNA: 2026-11-09 Goldman Sachs: main, Neutral -> Neutral
  - PTC: 2026-11-12 Wolfe Research: down, Outperform -> Peer Perform
  - ACN: 2026-10-26 Wells Fargo: main, Equal-Weight -> Equal-Weight
  - IT: 2026-11-06 Barclays: down, Equal-Weight -> Underweight
  - HAS: 2026-10-28 UBS: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

```text
Contract: E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 15.0% of open interest (2,017,687 contracts)
Change on the week: +3.7% of open interest
Crowding: 88% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 155.55M | fund size: 33.53B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: the streamed answer ran past the 480s ceiling (gave up after 2 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Why Does a Second 1.1% Jump in US Import Prices Matter for iShares TIPS Bond ETF (NYSEARCA:TIP)?](https://kalkine.com.au/news/economic-news/why-does-a-second-11-jump-in-us-import-prices-matter-for-ishares-tips-bond-etf-nysearcatip)  
  <sub>Kalkine, 4 hours ago</sub>  
  Why Does a Second 1.1% Jump in US Import Prices Matter for iShares TIPS Bond ETF (NYSEARCA:TIP)?
- [How Could a Second Straight 1.1% Import Price Gain Shape the Outlook for iShares TIPS Bond ETF (NYSEARCA:TIP)?](https://kalkine.ca/news/economic-news/how-could-a-second-straight-11-import-price-gain-shape-the-outlook-for-ishares-tips-bond-etf-nysearcatip)  
  <sub>kalkine.ca, 5 hours ago</sub>  
  How Could a Second Straight 1.1% Import Price Gain Shape the Outlook for iShares TIPS Bond ETF (NYSEARCA:TIP)?
- [Is iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) Vulnerable as the 10-Year Yield Holds at 5.10%?](https://www.google.com/goto?url=CAESvwEBxCJF17UVvX-haa7DUXAzGJK_XVNW31qs4W3I2fTKjA9aGC0NsDzAIYFUW2eWXS3WXnAEZ0bxm1uPSPvYjq9pKxp5OFt62_qVqBQLHIiZpQyZ2zxq-CQfXNyxnZIak_MulxiM5aGQlUB1VK09gnJHhvTIBtYNZVy2F2Xxcvj26Fk8xkylw4tuINmXWBODoqWgQOTYnvtwlZFhNPyEsavMTn1JiSJ9J0QDjDxsOhDb9yvHW9au7f06z4lfBB4ELw&gsessionid=AU-OqDCaeyKNN4FIDpm1bDCAVysildVH3nqEWLX4R8jZB--3Ojui6g)  
  <sub>kalkine.ca, 5 hours ago</sub>  
  Is iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) Vulnerable as the 10-Year Yield Holds at 5.10%?
- [How Exposed Is iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) With the 10-Year Yield Near 5.10%?](https://www.google.com/goto?url=CAESwgEBxCJF1_Amipex4PZpvUozgC9A0HTZ20KdGpFq8S303MP7GT0tr135VwXLmeoPOYE5-adqhMaxRaHFVqX96bb12XhFCHxs3tLJLuVbCLZBz5T0Zf2SyqsHp24vZLknoJXnVELElD-kxRgnGQZqNqFJThfMtXviJY8TyZpumo1ZPuul1IH0ToLYG9OSVY6izqBhfVGFq4bQ458kW-xYlSdculGBngVCYTtQLKoxqnNeyDeglUxYGL1vfCFPjVe8tKeESQ&gsessionid=AU-OqDCaeyKNN4FIDpm1bDCAVysildVH3nqEWLX4R8jZB--3Ojui6g)  
  <sub>Kalkine, 4 hours ago</sub>  
  How Exposed Is iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) With the 10-Year Yield Near 5.10%?
- [Can Minutes From the Fed Shift iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) While a December Hike Sits Near 95%?](https://www.google.com/goto?url=CAES1QEBxCJF1_pQQYI1z9GtJg7OqpX-BCIQcNJ9FnVD-7BRile4ayJ8ufGLgNbdPRiqdgnVPdqtleetfAnsh_jxbkQ8HLxHQu02Y-qLocUDgaihbO9jgiuOPO8xC7QtXG2_5OqJ0WCHds_GRyr9L6uxQUxfLRKxXUAqNo6rkjsiMvzUp87f8JdUTu-LrnBK24Tav_Ma4OTrkVWt7RD-oBC1IZ0O0Fk-xY8YTwGHguwBq8MIYkPFEzwQVcZaX_AOvTuAOIkE6UK_mlq8dD8uApYzaCUo_FHw5ow&gsessionid=AU-OqDCaeyKNN4FIDpm1bDCAVysildVH3nqEWLX4R8jZB--3Ojui6g)  
  <sub>Kalkine, 4 hours ago</sub>  
  Can Minutes From the Fed Shift iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) While a December Hike Sits Near 95%?
- [Can Musalem's Case for Up to Four More Hikes Weigh on iShares 1-3 Year Treasury Bond ETF (NASDAQ:SHY)?](https://www.google.com/goto?url=CAESyQEBxCJF15fCCTKla_ItCE67R5gd2dAKqTwgx-KJxuXDirZSGPfEX2SKoVsP79Ad7wjr0E6sq9lwbaRcg9Pq34ujia3_z-yrIYkJbCnKNTdzia_VsMNMkFbfC1NdvX09uLaWaH0VZcbYSSFS-82J-FyP8umCH9iVrjUMf9JSY4Iv_8BQeDSxIvvWkeizvmgS1XwanBX8hcsDfbneVX2iLg0qSUEVbZIh7txgc_oLt7-fpbrG5dgfYjUCl4XAU6AwB_rk2jVwi-jAx70&gsessionid=AU-OqDCaeyKNN4FIDpm1bDCAVysildVH3nqEWLX4R8jZB--3Ojui6g)  
  <sub>Kalkine, 4 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [TIP Issues Investor-Relations Announcement](https://www.google.com/goto?url=CAESmwEBxCJF13PDUPpygsTvGbZrfOHkgTrmct1W6r3bdBy8cYnwVvDMlMzO5d5dMDfvJKOyOtHCJ86zw1RlCv7pqbcwj9TkH3yZcKl6wXDBGxuXPRwr_sJtuowOFzia9Dg8RgBl2lLipejLEUW2Psb4oDH513ys1xPHo5ISeT-Oestr5bTZqmYR5lBhC3ciBKKMVoEuP83ijl2e92ZilQ&gsessionid=AU-OqDCaeyKNN4FIDpm1bDCAVysildVH3nqEWLX4R8jZB--3Ojui6g)  
  <sub>TipRanks, 2 hours ago</sub>  
  Tamburi Investment Partners Spa ( ($IT:TIP) ) just unveiled an announcement. TIP is an independent and diversified industrial group listed on Euronext STAR...
- [XRP Flashes Two-Year Price Warning Below $1 as ETF Investors Pull $19.66 Million](https://www.google.com/goto?url=CAESqQEBxCJF17LXyRSsEwTDi7PiShlkG-sNKarUGcNpHTyr09d7gPJj3uUywoa6vweMcbn7RmY7ET7BY9hsbjbAD7tAzGPfwpxyebLPYameogMSTttb17-udZ19uVmnUSLvAMuqpOIwVpiMSn31wmq327HVWrqnIC1DDrsoCRpSaQahh094VpmWxaANLX3D0Gb-nBOGtjDzeF4ICP--wfg762iPE3_QCKfSPCXy&gsessionid=AU-OqDCaeyKNN4FIDpm1bDCAVysildVH3nqEWLX4R8jZB--3Ojui6g)  
  <sub>TipRanks, 2 hours ago</sub>  
  XRP (XRP-USD) just triggered a warning signal last seen in 2024 after ending the trading week below the $1.00 mark. This has left crypto traders questioning...
- [İş Yatırım Reports ISMDL ETF Market-Maker Transactions](https://www.google.com/goto?url=CAESpwEBxCJF1-HhpGXp-J-s0pFElUd563a5i0ATxvpNl7uxUjaT_c5Gn7RjhqNCFV7QvKlBA4Og0WGq7qSr3yxuPpyNBasBwATxjcXdF43hdRE_HltDcVvhLldeT7_MtKet5afaberV3bnMxk9pqtjVV4KzlYn6dYTwD_D3iFNlkT36VCAEGSf91OCGaAv4y7fpGmfAr7z5mVWUbe1uCL7Acv-0Y4xm8Mv9dQ&gsessionid=AU-OqDCaeyKNN4FIDpm1bDCAVysildVH3nqEWLX4R8jZB--3Ojui6g)  
  <sub>TipRanks, 1 hour ago</sub>  
  An announcement from Is Yatirim Menkul Degerler AS ( ($TR:ISMEN) ) is now available. İş Yatırım Menkul Değerler A.Ş. is identified as the market maker for...
- [Bitcoin ETF IBIT Loses $143.5 Million as Short-Term Signals Turn Cautious](https://www.google.com/goto?url=CAEStAEBxCJF11udsFORCMsi6PZPjWsrMm8O3uldoZI-FvqbsUdJBznSJUkOUdR1wyCPX_Pz875Kmmyj9OIiYTPOCbkCZ5ZYxY3MzfKcNN80ZuDDNd2iMXCHbwbF8UHQcMlpzUDjy3ck085tzipQS0aARoYfnrdc3bCH-N7i53bozDlkYsjuKwTgDUfJQqaukGseEJIy5-McghqR1mNp0aWESOjcw06lkg1tvWRNUNRi8Fl6DYjm7d8&gsessionid=AU-OqDCaeyKNN4FIDpm1bDCAVysildVH3nqEWLX4R8jZB--3Ojui6g)  
  <sub>TipRanks, 12 hours ago</sub>  
  IShares Bitcoin Trust Registered saw $143.5 million in net outflows from IBIT on November 16, 2026. The withdrawal represented approximately 0.27% of the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 105.02 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 105.80 (-0.7%), 50d 105.28 (-0.2%), 200d 108.55 (-3.3%); 50d below 200d
Momentum: RSI(14) 42.3 | MACD -0.191 vs signal -0.025 (histogram -0.166)
Returns: 1d +0.2% | 5d -0.2% | 1m -0.4% | 3m -2.3%
52-week range: 103.98 - 111.88 (now 13.2% of the way up)
Volatility: ATR(14) 0.37 (0.4% of price) | annualised 20d 4.7%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Inflation-Protected Bond
Yield: 4.4%
Credit quality: AA 100.0% | US government debt 99.8%
Three-year record: +3.4% a year | beta to the market 0.73
Cost and size: expense ratio 0.18% | net assets 14.65B
What it is made of: Bonds 99.8%, Cash 0.2%
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
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 37.8% of open interest (6,095,194 contracts)
Change on the week: +0.3% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 177.70M | fund size: 18.66B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fund flows flat: 0.0% share count change over 1 week and 1 month
- Analyst consensus: 100% buy rating on top holdings with +27.2% price target
- Technical downtrend: price below 20‑day, 50‑day, 200‑day SMAs; RSI 35.4 (oversold) and low volume (0.02× 20‑day average)
- Macro environment: yields up across curve, VIX up 6.8% to 24.33, no surprise inflation or policy data

<details><summary><b>News</b> — score +0.00</summary>

- [Why Elbit Systems Investors Could Turn To ETFs Now](https://finance.yahoo.com/markets/stocks/articles/why-elbit-systems-investors-could-141138148.html)  
  <sub>46 minutes ago</sub>  
  Owning Elbit Systems stock directly ties your results to everything that happens to this one business. Simply Wall St flags risks such as future profit...
- [Why ETFs Could Make Sense After Elbit Systems Record Backlog](https://simplywall.st/etfs/us/nysearca-iteq/news/why-etfs-could-make-sense-after-elbit-systems-record-backlog)  
  <sub>13 hours ago</sub>  
  Owning Elbit Systems directly means any bump it hits lands full force in your portfolio. Simply Wall St flags that its Aerospace arm and Elbit Systems of...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 108.54 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 114.73 (-5.4%), 50d 118.89 (-8.7%), 200d 122.73 (-11.6%); 50d below 200d
Momentum: RSI(14) 35.4 | MACD -2.604 vs signal -2.211 (histogram -0.392)
Returns: 1d -0.9% | 5d -5.9% | 1m -10.3% | 3m -10.4%
52-week range: 99.40 - 137.69 (now 23.9% of the way up)
Volatility: ATR(14) 2.34 (2.2% of price) | annualised 20d 36.5%
Volume: 0.02x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.09 | P/B 2.45 | P/S 2.45 | 3y earnings growth n/a
Yield: 1.6%
Three-year record: +29.7% a year | beta to the market 0.98
Cost and size: expense ratio 0.59% | net assets 838.23M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Teva Pharmaceutical Industries Ltd 12.6%, Bank Leumi Le-Israel BM 8.6%, Bank Hapoalim BM 7.8%, Elbit Systems Ltd 5.6%, Tower Semiconductor Ltd 5.1%
Sector mix: Financial services 34.6%, Technology 18.0%, Healthcare 13.1%, Industrials 10.8%
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
Rolled up from the 5 largest holdings, 39.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.00 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.2% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 2.55M | fund size: 276.79M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, flat fund flows, bearish analyst view but no decisive technical break, fundamentals are moderate.

**Main reasons it gave:**
- Analyst view: weighted price target -5.8% and 42.6% sell rating
- Technicals: price below 20d, 50d, 200d SMAs; RSI 33.7; volume 0.08x 20‑day avg
- Macro: no policy or data surprise; VIX up 6.8 points, yields rising
- Fund flows: flat share count, no net inflows/outflows
- Fundamentals: moderate valuation (P/E 20.37) and 3‑yr return +12.9%/yr

<details><summary><b>News</b> — score +0.00</summary>

- [S&P 500 Index(.SPX) Stock Price Today | Quotes & News](https://www.moomoo.com/stock/.SPX-US?chain_id=Name1K9-3FXPhg.1lfqq8g&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A107%2C%22f%22%3A%22www.moomoo.com%2Fetfs%2FEWA-US%22%7D)  
  <sub>Moomoo, 6 hours ago</sub>  
  Track the latest S&P 500 Index(.SPX) stock price, quotes, financial information, news and analyst rating on moomoo App for your stock trading and investing...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 27.89 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 29.18 (-4.4%), 50d 28.88 (-3.4%), 200d 29.00 (-3.8%); 50d below 200d
Momentum: RSI(14) 33.7 | MACD -0.139 vs signal 0.037 (histogram -0.176)
Returns: 1d -1.0% | 5d -5.1% | 1m -4.3% | 3m -6.3%
52-week range: 24.95 - 30.43 (now 53.6% of the way up)
Volatility: ATR(14) 0.36 (1.3% of price) | annualised 20d 18.2%
Volume: 0.08x the 20-day average
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
Three-year record: +12.9% a year | beta to the market 0.94
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

<details><summary><b>What analysts and big funds say</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.35</summary>

```text
Rolled up from the 5 largest holdings, 46.5% of the fund by weight
Ratings by weight: buy 0.0% | hold 57.4% | sell 42.6% (mean 3.45 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -5.8% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 63.60M | fund size: 1.77B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: strong analyst buy coverage (+10.9% price target) but flat fund flows, bearish technicals, and neutral macro backdrop lead to a neutral overall stance.

**Main reasons it gave:**
- Analyst coverage: 87.2% buy rating, weighted price target +10.9% above current price
- Fund flows: share count unchanged over past month (0% net flow)
- Technical indicators: price 57.71 below 20-day SMA 60.39, 50-day SMA 59.97, 200-day SMA 58.61; RSI 34.6; MACD negative
- Macro: US 10-year yield up 10 bps to 5.10%, VIX up 6.8 points to 24.33 (elevated)
- Fundamentals: P/E 18.92, 3-year annualized return +22.5%, expense ratio 0.50%

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI Canada ETF (EWC) Seasonal returns chart](https://uk.finance.yahoo.com/quote/EWC/seasonality/)  
  <sub>Yahoo Finance UK, 22 hours ago</sub>  
  iShares MSCI Canada ETF (EWC) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [Energy World Sets Proxy Deadline Ahead of Annual General Meeting](https://www.tipranks.com/news/company-announcements/energy-world-sets-proxy-deadline-ahead-of-annual-general-meeting)  
  <sub>TipRanks, 7 hours ago</sub>  
  Energy World Corporation Ltd ( ($AU:EWC) ) has shared an announcement. Energy World Corporation Ltd has provided proxy-voting instructions for its annual...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 57.71 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 60.39 (-4.4%), 50d 59.97 (-3.8%), 200d 58.61 (-1.6%); 50d above 200d
Momentum: RSI(14) 34.6 | MACD -0.352 vs signal -0.029 (histogram -0.323)
Returns: 1d -1.7% | 5d -4.6% | 1m -5.2% | 3m -6.6%
52-week range: 49.91 - 62.64 (now 61.2% of the way up)
Volatility: ATR(14) 0.84 (1.5% of price) | annualised 20d 19.3%
Volume: 0.08x the 20-day average
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
Three-year record: +22.5% a year | beta to the market 0.73
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 29.5% of the fund by weight
Ratings by weight: buy 87.2% | hold 12.8% | sell 0.0% (mean 2.21 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.9% above the current prices
Holdings read: RY, TD, SHOP, BMO.TO, CNQ.TO
Recent rating changes among them:
  - RY: 2025-08-29 Argus Research: main, Buy -> Buy
  - TD: 2026-06-01 RBC Capital: main, Outperform -> Outperform
  - SHOP: 2026-11-05 Argus Research: reit, Buy -> Buy
  - BMO.TO: 2026-05-28 RBC Capital: main, Sector Perform -> Sector Perform
  - CNQ.TO: 2026-03-12 Goldman Sachs: main, Buy -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 94.80M | fund size: 5.47B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Overall neutral: bullish analyst view and solid fundamentals are offset by bearish technicals, low volume, and a macro backdrop of rising US yields and higher VIX, with no net fund flows.

**Main reasons it gave:**
- Price below 20-day, 50-day, and 200-day SMAs; RSI 42.1 and MACD below signal (bearish technicals)
- Analyst coverage of top 5 holdings (33.9% of fund) is 100% buy with a +10.6% price target (moderate bullish view)
- Fund flows flat over the past month, share count unchanged (neutral positioning)
- US Treasury yields rising and VIX up 6.8 points this week, indicating higher risk aversion (macro pressure)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 50.80 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 52.05 (-2.4%), 50d 51.37 (-1.1%), 200d 51.53 (-1.4%); 50d below 200d
Momentum: RSI(14) 42.1 | MACD 0.150 vs signal 0.350 (histogram -0.200)
Returns: 1d -0.9% | 5d -4.6% | 1m -0.5% | 3m -3.9%
52-week range: 45.38 - 54.72 (now 58.0% of the way up)
Volatility: ATR(14) 0.77 (1.5% of price) | annualised 20d 23.4%
Volume: 0.02x the 20-day average
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
Three-year record: +18.2% a year | beta to the market 1.18
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 33.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.97 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.6% above the current prices
Holdings read: SPOT, VOLV-B.ST, ATCO-A.ST, SAND.ST, ASSA-B.ST
Recent rating changes among them:
  - SPOT: 2026-10-23 Morgan Stanley: main, Overweight -> Overweight
  - ASSA-B.ST: 2015-12-09 Barclays: main, ? -> Equal-Weight
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
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 7.65M | fund size: 388.62M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US Treasury yields rose modestly across the curve (+0.03 to +0.10 on the week)
- VIX increased 6.8 points on the week, indicating higher volatility
- EWG trading below 20‑day, 50‑day, and 200‑day SMAs with low volume (0.07× 20‑day average)
- Fund flows flat over the past month (0% net change)
- Analyst coverage shows 78% buy rating and +21% price target, but no rating changes

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 41.28 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 42.16 (-2.1%), 50d 41.91 (-1.5%), 200d 42.18 (-2.1%); 50d below 200d
Momentum: RSI(14) 42.9 | MACD 0.084 vs signal 0.181 (histogram -0.097)
Returns: 1d -0.9% | 5d -4.0% | 1m -0.4% | 3m -6.0%
52-week range: 38.08 - 44.59 (now 49.2% of the way up)
Volatility: ATR(14) 0.67 (1.6% of price) | annualised 20d 24.8%
Volume: 0.07x the 20-day average
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
Three-year record: +17.6% a year | beta to the market 0.95
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
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.97 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.1% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 79.50M | fund size: 3.28B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst view and fundamentals are offset by bearish technicals, risk‑off macro backdrop, and flat fund flows.

**Main reasons it gave:**
- Analyst view: 90.8% buy rating and +15% price target
- Technicals: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 44.2
- Macro: US Treasury yields up and VIX up 6.8% to 24.33, indicating risk aversion
- Fund flows flat (0% change) indicating no net demand

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 56.44 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 56.98 (-1.0%), 50d 57.90 (-2.5%), 200d 58.29 (-3.2%); 50d below 200d
Momentum: RSI(14) 44.2 | MACD 0.026 vs signal -0.010 (histogram 0.036)
Returns: 1d -1.0% | 5d -3.7% | 1m +0.8% | 3m -10.1%
52-week range: 50.70 - 63.35 (now 45.3% of the way up)
Volatility: ATR(14) 0.89 (1.6% of price) | annualised 20d 28.7%
Volume: 0.12x the 20-day average
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
Three-year record: +25.6% a year | beta to the market 0.92
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
Ratings by weight: buy 90.8% | hold 9.2% | sell 0.0% (mean 2.17 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.0% above the current prices
Holdings read: UCG.MI, ISP.MI, ENEL.MI, ENI.MI, G.MI
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
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 8.55M | fund size: 482.52M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Price at $88.27 below 20-day SMA $92.05, 50-day SMA $95.12, 200-day SMA $92.14
- CFTC net long 2.2% of open interest fell 5.8% week-over-week
- Analyst coverage only 17.2% of fund weight, rating 100% buy, price target +28% above current
- Macro unchanged: Fed target 4.0%, yields up modestly, no policy surprise
- Fundamentals stable: P/E 15.14, dividend yield 3.8%, expense ratio 0.49%

<details><summary><b>News</b> — score +0.00</summary>

- [Options Whale Alert: $600K Bearish Risk Reversal Opened on $EWJ](https://www.moomoo.com/news/post/1004946409/options-whale-alert-600k-bearish-risk-reversal-opened-on-ewj)  
  <sub>15 hours ago</sub>  
  iSharesMSCI Japan ETF(EWJ.US)$ closed down 1.29% at $88.69. A trader bought 1500 Dec 18, 2026 $88.00 puts and sold 1500 Dec 18, 2026 $91.00 calls to open a.
- [Morgan Stanley Sees 22% Upside for Japan ETFs in 2027 - iShares MSCI Japan Index Fund (ARCA:EWJ)](https://www.benzinga.com/etfs/emerging-market-etfs/26/11/63346582/morgan-stanley-sees-japan-stocks-outrunning-the-sp-500-in-2027-these-etfs-offer-exposure)  
  <sub>23 hours ago</sub>  
  Morgan Stanley sees 22% upside for Japan's TOPIX in 2027, putting Japan ETFs in focus as global investors look beyond the S&P 500 for bigger gains.
- [What Lies Behind Japan's 0.1% Q3 Economic Contraction, and How Does It Affect iShares MSCI Japan ETF (NYSEARCA:EWJ)?](https://www.google.com/goto?url=CAES0AEBxCJF19axbwUzjKdSPO_2FUZgRCuVgL9m7AHw5kWNRbdhnHdyuzcZGp85LXKeOrDbzvPkup_eHq91WAUtsr1LWFjggPXRPFCuZW0JehToCKWlv2AoQ5aXF3pJO4m_2rrCLxvMmcCU6q-VMp-lGZ3YHw2770nljAS-z3GTEhcjt1DyPMUSxJq3DQkK7vW9M19a_vyROtiM5XhKghuh0W0_ohIs2Pw2giQ4FvvOHZVHgfsanyt_NxSk7HW2KjyjAIXFEq0eLTRb-U-sBEMSLFMn&gsessionid=jRbSv0LD_EacFdFyPu9P0SGK1OXCurts1htHaff4GWnZdnE7xq5UfA)  
  <sub>21 hours ago</sub>  
  What Lies Behind Japan's 0.1% Q3 Economic Contraction, and How Does It Affect iShares MSCI Japan ETF (NYSEARCA:EWJ)?
- [FLJP: Reasonable Low-Fee ETF Trading At A Discount To Developed Markets (NYSEARCA:FLJP)](https://www.google.com/goto?url=CAESrAEBxCJF1xkCd6lA-vWR2MeOiHAMvnCDK0GOLT54dp5Nlac_eJq2X0K8cc2hieVy7esrFHJ3aMAjFEweL47cSf7qIPSOtSY4noTh0lb6wCWkgLhgvOuxwi0C2lU-a-bzdMEypLJUJitllCowuU3DEB51U-elFFb_GdLkviveqnRJrxk9BnvXQDz7e2Q0ejReie2Q0ajXn1fiPjaUXEgsTGdjN3w0bWjqBOsR09uh&gsessionid=jRbSv0LD_EacFdFyPu9P0SGK1OXCurts1htHaff4GWnZdnE7xq5UfA)  
  <sub>8 hours ago</sub>  
  The Franklin FTSE Japan ETF offers exposure to Japanese equities through a low-cost, passive index approach.
- [Morgan Stanley Lifts Japan to Overweight, Sees 22% TOPIX Upside by End-2027](https://www.google.com/goto?url=CAESgAEBxCJF106W_Y7SlEWbD99yaa-0IV6JNfgYwo5843_ysDUZxYA6D7n7a-wyJGz50hdUZtrtwwnDhRgb8yShr38Isi2C5RCSvZV9zEek3Vr5oiD3UPBeaBSSpTVKFFmUvVXriFMcaf9i_B2iJ8dVUkeeUQfWoJw9DcfhK2Uq-jpZug&gsessionid=jRbSv0LD_EacFdFyPu9P0SGK1OXCurts1htHaff4GWnZdnE7xq5UfA)  
  <sub>23 hours ago</sub>  
  Morgan Stanley has upgraded Japanese equities to overweight from equal-weight and lifted its December 2027 TOPIX target to 4800, about 22% above the…

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 88.27 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 92.05 (-4.1%), 50d 95.12 (-7.2%), 200d 92.14 (-4.2%); 50d above 200d
Momentum: RSI(14) 34.8 | MACD -1.686 vs signal -1.462 (histogram -0.224)
Returns: 1d -0.5% | 5d -4.2% | 1m -7.5% | 3m -6.4%
52-week range: 79.49 - 99.32 (now 44.3% of the way up)
Volatility: ATR(14) 1.57 (1.8% of price) | annualised 20d 29.8%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Japan Stock
What it holds: P/E 15.14 | P/B 1.95 | P/S 1.31 | 3y earnings growth n/a
Yield: 3.8%
Three-year record: +16.9% a year | beta to the market 0.86
Cost and size: expense ratio 0.49% | net assets 23.40B
What it is made of: Stocks 99.2%, Cash 0.8%
Largest holdings: Mitsubishi UFJ Financial Group Inc 4.5%, Toyota Motor Corp 3.6%, Advantest Corp 3.1%, Recruit Holdings Co Ltd 3.1%, Sumitomo Mitsui Financial Group Inc 2.9%
Sector mix: Industrials 22.4%, Technology 20.6%, Financial services 19.1%, Consumer cyclical 12.0%
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
Rolled up from the 5 largest holdings, 17.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +28.0% above the current prices
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 227.85M | fund size: 20.11B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst ratings: 64.8% buy, weighted price target +1.1% above current price
- Fund flows flat: 0% change in share count over week and month
- Technicals: price above 50‑day SMA (+2.7%) and 200‑day SMA (+2.7%) but below 20‑day SMA (‑1.2%), RSI 49.5, volume 0.06× 20‑day average
- Macro: Treasury yields up across curve, VIX up 6.8 points to 24.33, dollar index +0.88% indicating risk‑off environment

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 63.69 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 64.45 (-1.2%), 50d 62.02 (+2.7%), 200d 62.02 (+2.7%); 50d above 200d
Momentum: RSI(14) 49.5 | MACD 0.647 vs signal 0.894 (histogram -0.247)
Returns: 1d -0.4% | 5d -1.8% | 1m +1.0% | 3m -0.1%
52-week range: 55.69 - 66.56 (now 73.6% of the way up)
Volatility: ATR(14) 0.78 (1.2% of price) | annualised 20d 19.7%
Volume: 0.06x the 20-day average
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
Three-year record: +15.8% a year | beta to the market 0.82
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
Ratings by weight: buy 64.8% | hold 35.2% | sell 0.0% (mean 2.45 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +1.1% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 28.62M | fund size: 1.82B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall due to weak technicals, higher macro risk, and flat fund flows despite bullish analyst coverage and solid fundamentals.

**Main reasons it gave:**
- Technicals: price 61.81 below 20‑day SMA (64.37) and 50‑day SMA (65.83) with low volume (0.02x 20‑day avg)
- Macro: Treasury yields rose (10‑yr +0.10% week) and VIX up 6.8 points to 24.33, indicating higher risk
- Fund flows: share count flat (+0.0% week, +0.0% month) showing no net demand
- Analyst view: 100% buy rating on top holdings (42.3% weight) with +61.9% price target

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 61.81 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 64.37 (-4.0%), 50d 65.83 (-6.1%), 200d 65.17 (-5.2%); 50d above 200d
Momentum: RSI(14) 35.8 | MACD -0.752 vs signal -0.550 (histogram -0.202)
Returns: 1d -0.6% | 5d -6.7% | 1m -5.0% | 3m -10.4%
52-week range: 55.33 - 71.61 (now 39.8% of the way up)
Volatility: ATR(14) 1.08 (1.8% of price) | annualised 20d 27.1%
Volume: 0.02x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.38 | P/B 2.46 | P/S 1.73 | 3y earnings growth n/a
Yield: 4.4%
Three-year record: +18.3% a year | beta to the market 1.13
Cost and size: expense ratio 0.50% | net assets 597.52M
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ASML Holding NV 21.9%, ING Groep NV 8.6%, Prosus NV Ordinary Shares - Class N 4.7%, ASM International NV 3.8%, Nebius Group NV Shs Class-A- 3.4%
Sector mix: Technology 30.4%, Financial services 21.1%, Consumer defensive 11.8%, Industrials 11.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

```text
Rolled up from the 5 largest holdings, 42.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.58 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +61.9% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 5.55M | fund size: 343.05M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no material macro surprise, technicals show weak short‑term momentum, and fund flows are flat. Analyst coverage is bullish but limited to ~53% of the fund, and fundamentals are modestly positive.

**Main reasons it gave:**
- No news in past 24h
- Technicals: price 0.8% below 20‑day SMA, RSI 44.6, volume 0.02× 20‑day average
- Macro: US Treasury yields rose across the curve and VIX up 6.8 points, no policy surprise
- Fund flows: share count unchanged (+0.0% week, +0.0% month)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 57.80 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 58.25 (-0.8%), 50d 59.02 (-2.1%), 200d 58.17 (-0.6%); 50d above 200d
Momentum: RSI(14) 44.6 | MACD 0.082 vs signal 0.017 (histogram 0.066)
Returns: 1d -1.1% | 5d -3.5% | 1m -0.4% | 3m -7.2%
52-week range: 49.37 - 63.23 (now 60.8% of the way up)
Volatility: ATR(14) 0.90 (1.6% of price) | annualised 20d 25.0%
Volume: 0.02x the 20-day average
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
Three-year record: +30.5% a year | beta to the market 0.91
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
Weighted price target: +9.2% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 37.35M | fund size: 2.16B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Analyst view bullish (100% buy, +60.5% price target) covering 37.7% of the fund; Technical indicators bearish (price below 20‑day, 50‑day, 200‑day SMAs; RSI 35.3; MACD negative); Inflation 3.7% higher than market expectation of 2.2% over 10 years; Higher rates and elevated volatility (VIX 24.33, Fed expected hikes, upward‑sloping yield curve); Fund flows flat (no net creations or redemptions over the past month)

**Main reasons it gave:**
- Analyst view bullish (100% buy, +60.5% price target) covering 37.7% of the fund
- Technical indicators bearish (price below 20‑day, 50‑day, 200‑day SMAs; RSI 35.3; MACD negative)
- Inflation 3.7% higher than market expectation of 2.2% over 10 years
- Higher rates and elevated volatility (VIX 24.33, Fed expected hikes, upward‑sloping yield curve)
- Fund flows flat (no net creations or redemptions over the past month)

<details><summary><b>News</b> — score +0.00</summary>

- [TSMC Is Sliding Before Nvidia Reports. Your Chip ETF Is Taking the Hit](https://247wallst.com/investing/etf/2026/11/17/tsmc-is-sliding-before-nvidia-reports-your-chip-etf-is-taking-the-hit/)  
  <sub>24/7 Wall St., 20 hours ago</sub>  
  Chip stocks are flinching hours before Nvidia reports, and TSMC's slide is rippling through funds many retirement savers own. Why does one earnings call put...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 89.07 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 98.13 (-9.2%), 50d 106.51 (-16.4%), 200d 94.98 (-6.2%); 50d above 200d
Momentum: RSI(14) 35.3 | MACD -4.590 vs signal -4.053 (histogram -0.537)
Returns: 1d +0.4% | 5d -11.1% | 1m -17.0% | 3m -14.4%
52-week range: 60.03 - 118.00 (now 50.1% of the way up)
Volatility: ATR(14) 3.94 (4.4% of price) | annualised 20d 67.2%
Volume: 0.22x the 20-day average
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
Three-year record: +32.6% a year | beta to the market 1.35
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 37.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +60.5% above the current prices
Holdings read: 2330.TW, 2454.TW, 2317.TW, 3711.TW, 2308.TW
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
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 85.00M | fund size: 7.57B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, technicals bearish but not decisive, flat fund flows, analyst view bullish but limited to ~37% of holdings.

**Main reasons it gave:**
- Yield curve remains upward sloping (+0.95) – no rate surprise
- RSI 40.6 and price below 20‑day SMA (46.43 vs 47.66) – bearish technicals
- Fund flows flat (share count +0.0% week) – neutral demand
- Analyst ratings 100% buy for top 5 holdings (36.9% weight) – bullish but limited

<details><summary><b>News</b> — score +0.00</summary>

- [AstraZeneca Announced Two Approvals in One Day. The Stronger Evidence Belongs to the One Getting Less Attention.](https://www.moomoo.com/community/feed/astrazeneca-announced-two-approvals-in-one-day-the-stronger-evidence-117632829358486)  
  <sub>Moomoo, 22 hours ago</sub>  
  Klygefa beat placebo in myasthenia gravis, yet its gain of 1.6 points on a 24-point daily-function scale is no better than the 1.7 points AstraZeneca'...
- [阿斯利康公司一日内宣布两项获批。其中，证据更为充分的那项却鲜少受到关注。](http://www.moomoo.com/hans/community/feed/astrazeneca-announced-two-approvals-in-one-day-the-stronger-evidence-117632829358486)  
  <sub>Moomoo, 22 hours ago</sub>  
  克利格法在重症肌无力的治疗中优于安慰剂，然而其在24分制的日常功能量表上仅提高1.6分，效果并无改善高于阿斯利康自家药物Ultomiris在另一项试验中显示出的1.7个...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 46.43 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 47.66 (-2.6%), 50d 47.34 (-1.9%), 200d 47.10 (-1.4%); 50d above 200d
Momentum: RSI(14) 40.6 | MACD -0.045 vs signal 0.100 (histogram -0.145)
Returns: 1d -1.1% | 5d -2.9% | 1m -2.8% | 3m -4.3%
52-week range: 41.34 - 49.39 (now 63.2% of the way up)
Volatility: ATR(14) 0.63 (1.4% of price) | annualised 20d 20.8%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 16.62 | P/B 2.25 | P/S 1.41 | 3y earnings growth n/a
Yield: 3.1%
Three-year record: +19.1% a year | beta to the market 0.66
Cost and size: expense ratio 0.50% | net assets 3.73B
What it is made of: Stocks 98.5%, Other 1.0%, Cash 0.5%
Largest holdings: Shell PLC 9.9%, HSBC Holdings PLC 9.3%, AstraZeneca PLC 8.9%, Unilever PLC 4.4%, Rolls-Royce Holdings PLC 4.4%
Sector mix: Financial services 23.2%, Consumer defensive 15.3%, Energy 14.3%, Healthcare 13.9%
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
Rolled up from the 5 largest holdings, 36.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.08 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.6% above the current prices
Holdings read: SHEL.L, HSBA.L, AZN.L, ULVR.L, RR.L
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 67.80M | fund size: 3.15B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: yields up modestly, dollar stronger, VIX elevated but no policy change
- Technical indicators mixed: price below 20‑day and 200‑day SMA, negative MACD, low volume
- Fund flows flat: share count unchanged over week and month
- Analyst coverage bullish (+15% price target) but only covers 47.5% of fund

<details><summary><b>News</b> — score +0.00</summary>

- [Can Your Trash Can Pass the Holiday 'Eww' Test?](https://www.morningstar.com/news/accesswire/1251102msn/can-your-trash-can-pass-the-holiday-eww-test)  
  <sub>Morningstar, 24 hours ago</sub>  
  GREEN BAY, WI / ACCESS Newswire / November 17, 2026 / Your house is picture-perfect for the holidays. You've cleaned, polished and decorated from top to...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 75.55 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 76.01 (-0.6%), 50d 74.37 (+1.6%), 200d 76.19 (-0.8%); 50d below 200d
Momentum: RSI(14) 48.9 | MACD 0.668 vs signal 0.751 (histogram -0.084)
Returns: 1d -1.7% | 5d -2.8% | 1m +0.1% | 3m +0.1%
52-week range: 66.02 - 81.23 (now 62.7% of the way up)
Volatility: ATR(14) 1.34 (1.8% of price) | annualised 20d 15.6%
Volume: 0.18x the 20-day average
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
Three-year record: +11.3% a year | beta to the market 0.99
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 47.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.1% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 18.90M | fund size: 1.43B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, mixed fund flows, bullish analyst view not enough to outweigh bearish macro/technical backdrop.

**Main reasons it gave:**
- US Treasury yields rose across the curve (+0.03 to +0.10) and the dollar index increased (+0.88), both typically bearish for gold miners
- GDX is below its 20‑day, 50‑day and 200‑day SMAs, RSI 36.4 and MACD negative, indicating bearish technical momentum
- Analyst coverage of the top holdings is 100% buy with a +30.7% price target, but macro and technicals are not supportive
- Fund flows show a recent week inflow (+15.7% share count) but a net outflow over the month (-3.8%), indicating mixed investor sentiment

<details><summary><b>News</b> — score +0.00</summary>

- [3 Funds With Metals And Mining Exposure For The Army Rare Earth Push](https://simplywall.st/etfs/us/nysearca-gdxj/news/3-funds-with-metals-and-mining-exposure-for-the-army-rare-ea)  
  <sub>13 hours ago</sub>  
  Metals and mining ETFs can look interchangeable at first glance. Tick up a ticker like GDX, GDXJ or GNR and the names all sound close enough that it is easy...
- [iShs III-Flex.Inc.Bd Act.ETF R (IFLX.HM) stock price, news, quote and history](https://au.finance.yahoo.com/quote/IFLX.HM/)  
  <sub>2 hours ago</sub>  
  Find the latest iShs III-Flex.Inc.Bd Act.ETF R (IFLX.HM) stock quote, history, news and other vital information to help you with your stock trading and...
- [YieldMax® ETFs Announces Weekly Distributions for Group 2 ETFs](https://www.google.com/goto?url=CAESwwEBxCJF13PEkQgHBmWqFa33GLdqhXzkuTrXLDWZpy2e22v1o4DvK02LtG3i8YurBqK5mhKcEM9k8WuFPSldkALnvQ7DNhX5Xi4MC4h4Gcq6dKNLEtvKe2Mg4qUkWKLkJpe2E0g7A2bWpIxdmonmQi-opK3XJytZiFmU8MFq0A5rmKaW9w0KfsFvlHrclvoY_6qaCSBASpKUUWVEgIKe6SuWhTTX68XAhDqiWdGhwtzEGADrH2r17C3ZojA10tKUxLunB98&gsessionid=9ZX69q9o7ztB6n_iBxzqBKK6Fe8ZWrpWSGrz1GM1rjW7qiZISP98PA)  
  <sub>3 hours ago</sub>  
  CHICAGO and MILWAUKEE and NEW YORK, Nov. 18, 2026 (GLOBE NEWSWIRE) -- YieldMax® ETFs today announced distributions for the YieldMax® Group 2 weekly pay ETFs...
- [Gold seen grinding higher to $4,650/oz by year-end 2027 on central bank buying - Goldman](https://www.google.com/goto?url=CAESuAEBxCJF19il2hAx_RO_5ky_hQa7klOpXpjJ1iiTWFRxlE5WGDMoriRxjQjyo_bg4oQufCh9JTm5h2lgA5Tbvt8Wn_LWtgOnWTNzj1RVdJe942KJkfkIKKEreU6R1rvJF-uWPvMSXTi1hAm77ZBt3786hmkkrsR3xt6X2U8qyU-n-7UWNALDz_72hCSwES1ANTVf1L286YHqcOC8IOoY8aT9Wb2Bz7zOMV7io501wubpf24AwXEp2upL&gsessionid=9ZX69q9o7ztB6n_iBxzqBKK6Fe8ZWrpWSGrz1GM1rjW7qiZISP98PA)  
  <sub>16 hours ago</sub>  
  Gold's near-term performance likely will be slowed by expectations of higher interest rates, but central bank buying should push prices back above $4600 by...
- [United States Oil Fund, LP (USO) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZAHEIkXXQLZXpRlaufRgsQtkG9mXxt2rExOX4T0bTzo9l_ANuzoaQDPlBPex2AqdrsoAMUrqw-vwKt8hkjpZbGLvv5vZp5myKNqQF0RhnVY1lKstJunlBa0LPrzSLls0oC8xru8&gsessionid=9ZX69q9o7ztB6n_iBxzqBKK6Fe8ZWrpWSGrz1GM1rjW7qiZISP98PA)  
  <sub>12 hours ago</sub>  
  Find the latest United States Oil Fund, LP (USO) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 75.09 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 82.17 (-8.6%), 50d 86.99 (-13.7%), 200d 89.32 (-15.9%); 50d below 200d
Momentum: RSI(14) 36.4 | MACD -1.925 vs signal -1.390 (histogram -0.535)
Returns: 1d -5.6% | 5d -11.9% | 1m -12.8% | 3m -24.8%
52-week range: 70.74 - 115.84 (now 9.6% of the way up)
Volatility: ATR(14) 3.53 (4.7% of price) | annualised 20d 61.3%
Volume: 0.36x the 20-day average
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
Three-year record: +41.9% a year | beta to the market 0.98
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

<details><summary><b>What analysts and big funds say</b> — score +0.65</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.65</summary>

```text
Rolled up from the 5 largest holdings, 42.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.71 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.7% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, FNV.TO
Recent rating changes among them:
  - NEM: 2026-10-27 Scotiabank: main, Sector Outperform -> Sector Outperform
  - AEM.TO: 2026-11-02 Freedom Broker: up, Hold -> Buy
  - ABX.TO: 2026-11-10 JP Morgan: main, Overweight -> Overweight
  - WPM.TO: 2026-10-08 UBS: main, Buy -> Buy
  - FNV.TO: 2026-11-12 HC Wainwright & Co.: reit, Buy -> Buy
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
Direction: money going out (1 month)
Share count change: 1 week: +15.7% (3.09B) over 7d | 1 month: -3.8% (-900.66M) over 32d
Shares outstanding: 302.17M | fund size: 22.69B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: technicals are bearish (price below 20‑, 50‑, and 200‑day SMAs, negative MACD, RSI ~48), macro shows higher yields and rising VIX but no surprise, and while fund flows are strongly positive, there is no decisive macro catalyst or technical breakout to justify a directional bias.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs (70.26, 70.13, 75.80) indicating bearish trend
- MACD histogram negative (-0.029) and RSI 47.5, showing weak momentum
- US Treasury yields rose across the curve (+0.03 to +0.10) and VIX up 6.8% to 24.33, indicating higher market stress
- Fund flows show strong inflows (+195% share count over 32 days) but no macro catalyst or decisive technical break

<details><summary><b>News</b> — score +0.00</summary>

- [NSA communications network is said to fail, amid recent technology disruptions (PPA:NYSEARCA)](https://seekingalpha.com/news/4673724-nsa-communications-network-is-said-to-fail-amid-recent-technology-disruptions?source=generic_rss)  
  <sub>23 hours ago</sub>  
  NSA Net, the NSA's classified network, is offline with no evidence so far of a cyberattack; staff arrivals are staggered as officials assess the disruption.
- [NSA says network disruption affected internal systems, critical operations intact (PPA:NYSEARCA)](https://seekingalpha.com/news/4673863-nsa-says-network-disruption-affected-internal-systems-critical-operations-intact)  
  <sub>19 hours ago</sub>  
  The NSA says scheduled maintenance temporarily disrupted some internal systems, while mission-critical capabilities remained fully operational.
- [Bitcoin Today, November 18, 2026: Still Under Pressure, Price at Rp1.18 Billion as Investors Brace for Further Declines](https://www.google.com/goto?url=CAESzwEBxCJF19IpePrzYh7cg1-pjXtJGhuEhuyVikXbkvF90BZPue2cysSFad6zcslyQ9X9Iw2RYQ3UBCIPWapTsh9CGtcgqnOA2CQ_1TaehdbL4WDdCf0DLl51yVUbX-Us-fd7bDkB21-85LZ1srIeYiV0I0lqt-1kQDMZRx9PLXwVnpBq_LH3-xvWV6M4vyXXFu1VNFBGhOrolLVMETmd0Cv6jE6j5RcyboSRAjtD7UzbFT1Vwt7divIE8TQHp80eLjZdUMA1pSgWMViShQiELwU&gsessionid=xOqQL5hUrBncQo04mbG1I6t1_0QJIl_z4cPRBKI3WF9Vb_lsXfT5ug)  
  <sub>12 hours ago</sub>  
  JAKARTA, Aktualita.co - The price of Bitcoin today , Wednesday (11/18/2026), remains under pressure after experiencing a sharp decline throughout last week.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 69.84 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 70.26 (-0.6%), 50d 70.13 (-0.4%), 200d 75.80 (-7.9%); 50d below 200d
Momentum: RSI(14) 47.5 | MACD 0.092 vs signal 0.120 (histogram -0.029)
Returns: 1d +0.3% | 5d -4.6% | 1m +1.6% | 3m -11.8%
52-week range: 66.08 - 84.41 (now 20.5% of the way up)
Volatility: ATR(14) 1.70 (2.4% of price) | annualised 20d 31.9%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Industrials
What it holds: P/E 30.89 | P/B 5.67 | P/S 2.83 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +22.7% a year | beta to the market 1.03
Cost and size: expense ratio 0.37% | net assets 12.22B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: GE Aerospace 20.0%, RTX Corp 17.2%, Boeing Co 6.8%, Lockheed Martin Corp 5.7%, Northrop Grumman Corp 5.1%
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 54.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.74 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.4% above the current prices
Holdings read: GE, RTX, BA, LMT, NOC
Recent rating changes among them:
  - GE: 2026-10-21 UBS: main, Buy -> Buy
  - RTX: 2026-10-21 UBS: main, Neutral -> Neutral
  - BA: 2026-10-29 Bernstein: main, Outperform -> Outperform
  - LMT: 2026-11-04 Guggenheim: init, ? -> Buy
  - NOC: 2026-10-27 Bernstein: main, Market Perform -> Market Perform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.90</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +2.8% (339.47M) over 7d | 1 month: +195.2% (8.10B) over 32d
Shares outstanding: 175.44M | fund size: 12.25B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The analyst view is strongly bullish (89.9% buy rating and a +16.8% price target), but fund flows are flat, indicating no net demand shift. Macro data show modest yield increases, a higher‑than‑usual VIX, and no policy surprise, which together temper the bullish analyst stance. Technicals show the price above short‑ and long‑term moving averages with only modest momentum and no decisive breakout. With no material macro surprise or clear technical signal, the overall call remains neutral.

**Main reasons it gave:**
- Analyst view: 89.9% buy rating and +16.8% price target (bullish)
- Fund flows flat over the past month, indicating neutral demand
- Macro: Treasury yields rose modestly across the curve, VIX up, no policy surprise
- Technicals: price above 20‑day, 50‑day, and 200‑day SMAs, RSI 53, MACD slightly positive but no decisive break

<details><summary><b>News</b> — score +0.00</summary>

- [iShares U.S. Home Construction ETF (ITB) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/ITB/)  
  <sub>22 hours ago</sub>  
  Find the latest iShares U.S. Home Construction ETF (ITB) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 83.11 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 82.57 (+0.7%), 50d 81.07 (+2.5%), 200d 82.08 (+1.3%); 50d below 200d
Momentum: RSI(14) 53.0 | MACD 0.650 vs signal 0.641 (histogram 0.009)
Returns: 1d +0.9% | 5d -1.6% | 1m +4.1% | 3m -3.7%
52-week range: 68.14 - 90.01 (now 68.5% of the way up)
Volatility: ATR(14) 1.48 (1.8% of price) | annualised 20d 28.5%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Industrials
What it holds: P/E 19.04 | P/B 4.01 | P/S 1.38 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +13.4% a year | beta to the market 1.24
Cost and size: expense ratio 0.37% | net assets 2.00B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Union Pacific Corp 18.7%, Uber Technologies Inc 13.8%, CSX Corp 10.0%, United Parcel Service Inc Class B 4.9%, Norfolk Southern Corp 4.8%
Sector mix: Industrials 85.3%, Technology 14.7%
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

<details><summary><b>What analysts and big funds say</b> — score +0.65</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.65</summary>

```text
Rolled up from the 5 largest holdings, 52.2% of the fund by weight
Ratings by weight: buy 89.9% | hold 10.1% | sell 0.0% (mean 1.84 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.8% above the current prices
Holdings read: UNP, UBER, CSX, UPS, NSC
Recent rating changes among them:
  - UNP: 2026-11-05 Baird: down, Outperform -> Neutral
  - UBER: 2026-11-06 UBS: main, Buy -> Buy
  - CSX: 2026-10-27 Susquehanna: main, Positive -> Positive
  - UPS: 2026-10-28 UBS: main, Buy -> Buy
  - NSC: 2026-10-23 Citigroup: main, Neutral -> Neutral
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
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 2.80M | fund size: 232.72M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst view (+16.8% price target) is offset by moderate outflows and mixed technicals, while macro risk aversion (rising yields, elevated VIX) adds bearish pressure.

**Main reasons it gave:**
- Analyst rating: 90.6% buy, weighted price target +16.8% above current
- Fund flows: share count down 1.3% in 1 week, 6.7% in 1 month
- Technical: price below 200‑day SMA, MACD positive but volume 0.4× 20‑day avg
- Macro: US Treasury yields up, VIX at 24.33 (+6.8% week), indicating risk aversion

<details><summary><b>News</b> — score +0.00</summary>

- [The Trillion-Dollar Club in One ETF: Direxion Launches TRLL](https://www.tradingview.com/news/prnewswire:c762cc5d96e79:0-the-trillion-dollar-club-in-one-etf-direxion-launches-trll/)  
  <sub>59 minutes ago</sub>  
  TRLL: Dynamic, Equal-Weight Exposure to Companies Valued at $1 Trillion or MoreNEW YORK, Nov. 18, 2026 /PRNewswire/ -- Direxion, a leading provider of ETFs,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 35.75 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 34.99 (+2.2%), 50d 35.90 (-0.4%), 200d 37.72 (-5.2%); 50d below 200d
Momentum: RSI(14) 54.3 | MACD 0.083 vs signal -0.111 (histogram 0.194)
Returns: 1d -0.5% | 5d -0.8% | 1m +2.8% | 3m -6.5%
52-week range: 33.69 - 40.63 (now 29.7% of the way up)
Volatility: ATR(14) 0.34 (0.9% of price) | annualised 20d 16.5%
Volume: 0.40x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.14 | P/B 1.71 | P/S 2.83 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: -0.2% a year | beta to the market 0.20
Cost and size: expense ratio 0.75% | net assets 556.97M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Al Rajhi Bank 14.1%, Saudi Arabian Oil Co 12.5%, Saudi National Bank 8.2%, Saudi Telecom Co 6.2%, Saudi Arabian Mining Co 4.3%
Sector mix: Financial services 41.3%, Energy 13.5%, Basic materials 12.7%, Communication services 8.9%
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
Rolled up from the 5 largest holdings, 45.3% of the fund by weight
Ratings by weight: buy 90.6% | hold 9.4% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.8% above the current prices
Holdings read: 1120.SR, 2222.SR, 1180.SR, 7010.SR, 1211.SR
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
Share count change: 1 week: -1.3% (-7.15M) over 7d | 1 month: -6.7% (-39.94M) over 32d
Shares outstanding: 15.56M | fund size: 556.32M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, technical downtrend, high valuations offset by strong analyst bullish view.

**Main reasons it gave:**
- Analyst coverage of top holdings 46.4% weight, 100% buy rating, price target +56.5% above current
- Fund flows flat over past week and month, indicating no net demand
- Technical indicators: price below 20‑day, 50‑day, 200‑day SMAs; RSI 34.9; MACD negative
- Macro: yields up, VIX elevated, inflation 3.7% above target, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

- [VanEck Semiconductor ETF (SMH) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/SMH/)  
  <sub>5 hours ago</sub>  
  VanEck Semiconductor ETF (SMH) · -4.87% · -14.76% · -17.30% · 26.64% · 33.37% · 202.10% · 843.79%. Key events. Baseline. Advanced chart. Loading chart...
- [SMH: Another Buy The Dip Moment](https://seekingalpha.com/article/4969507-smh-another-buy-the-dip-moment)  
  <sub>3 hours ago</sub>  
  The VanEck Semiconductor ETF is a strong buy and long-term hold after its 31% decline, offering diversified exposure to semiconductor leaders. SMH's 20%...
- [Should You Invest in the VanEck Semiconductor ETF (SMH)?](https://www.google.com/goto?url=CAESkQEBxCJF14drUuX3b-aIpHJNQCf6zX4h98Cil1oyyFIqNsum7od8_R58IN7rNdxWGOECcUC97rygP0jcCjLhxR8QeA0Z27jESSViAII9nJfzOekny2oyC8I9rEn7MAWOEFaJ-EJQME5Se8Azvqy8yAlaU3nmuUOuo9aRskS5bRjycv0XeuryN-g_zvTzxhWZZYrb&gsessionid=cwDLb-fibu-MUIHea0_Qx1AAJgPh8n1VZjftHzrq458Zsw-wGjNdeg)  
  <sub>5 hours ago</sub>  
  If you're interested in broad exposure to the Technology - Semiconductors segment of the equity market, look no further than the VanEck Semiconductor ETF...
- [Nvidia Is Only 17% of SMH. After Its Beat, the Chip ETF Jumped Almost as Much as Nvidia Did](https://www.google.com/goto?url=CAESwgEBxCJF19aApehAL6zE_rm_S9IS7OLeRAL0uaOhSt5z5zV6oA1qcLDcHJhohLk8XQSjgQZxA2hXd5muiCaI4OhPMsoCg2uwIJfcZrr0q4I-5RM7liao8eU8bGMhFmkQCzNutIlxlFp7fSLbyjeCdD5XbFlCfWuW5Q_zhBxkjAGuJZqFNR2RfkC6Dc23ohGeEHj_KV_fis-wkm-r4nVKPXgVC9820JFR6G760-Q0u_parjrOp-MtbwQxbMOD6n8wMAnTkw&gsessionid=cwDLb-fibu-MUIHea0_Qx1AAJgPh8n1VZjftHzrq458Zsw-wGjNdeg)  
  <sub>16 hours ago</sub>  
  Nvidia (NASDAQ: NVDA) beat estimates on Tuesday with $115.8 billion in third-quarter revenue and forecast $130 billion for the fourth quarter,...
- [Chip ETF SMH jumps 3.3% after Nvidia's strong Q...](https://www.google.com/goto?url=CAESmAEBxCJF12pcQTBB3rjNPgVutqyjiA02lG14dmtbOqXouqjgpG94nk3NqAgZzJoGAFwmIZyOM9Bl_k77pucEHalVfdqxND2Rs9RkXJ6NrAe2NdEWt_-8JidXPpBeK1RsN7SlIqNcnwziD8d9pkyifDDSufBuga9rcxwVST5PbJuCGazV6EI1NklzBtK69mLM5sIKqtWt4aIr9g&gsessionid=cwDLb-fibu-MUIHea0_Qx1AAJgPh8n1VZjftHzrq458Zsw-wGjNdeg)  
  <sub>16 hours ago</sub>  
  Nvidia reported better-than-expected Q3 revenue of $115.8 billion and forecasted $130 billion for Q4, boosting the VanEck Semiconductor ETF (SMH) by 3.3% in...
- [What Led a 28% Cut in the 2028 AI Accelerator Spending Forecast to Weigh on VanEck Semiconductor ETF (NASDAQ:SMH)?](https://www.google.com/goto?url=CAES2wEBxCJF1xx-qLPaH97-AUgSkjS7yIvD0aXRFrxS5WckwkKiF8U0ViFnHoVhM6vkY0rPOwBWQX9N76RIgCFkCG6DWT_Q3SHHI80bx74VkBMUJTFjwPg3MM8ZKFPeuxfRQ4f12gM_8TdJQZtGkegb2PbrtbFs9yR30yqqNP5mhWHecFSRP3r4DXfbPJQssGMk8Tao_m3OJxRLyFXr1UIG_zYBdwMWUOM3_zoPkpjpo6ohJYuuU3dPv7OcBTcuGRhPyvGOq--7YHXraCggUxamr6gbiiQOzDqDEitTt9U&gsessionid=cwDLb-fibu-MUIHea0_Qx1AAJgPh8n1VZjftHzrq458Zsw-wGjNdeg)  
  <sub>21 hours ago</sub>  
  What Led a 28% Cut in the 2028 AI Accelerator Spending Forecast to Weigh on VanEck Semiconductor ETF (NASDAQ:SMH)?
- [Nvidia Has Fallen 18% Since the Jensen Huang Scandal Broke and the Biggest Chip ETF Barely Moved. Here's What Tonight's Report Does to SMH, SOXX, SOXL and NVDL](https://www.google.com/goto?url=CAESgwIBxCJF18osBdoGGMKuuoSm9OKniH0mrnWcTqLQ7uxEfaGW-eztApHVO2lh-HVGayjNKJ17nEeme7JvliVRq-AoeCpYf_Ytq274YbCeZEWPQvz5frvdKMdZHrGignfuIFXewet2hgWK9olUZYvzfEqgGYH1N8wqxzwVl88HJhPcINN2d85jdfFcs5QLuQDPxdIz5RsaDqrq4O1HFKTo20sbZdETvY3vuw-mfadfgaxZZmf_-GoP43VXDFgDz_snyGCWTc0Lk5XKaO_e73x_KKGpfM4HP7jDmRMw3uRTbAh6oxCdd8BF0LGdTyVzPPG117LTjQ-OWrest1LKAlpjBm7oFk7g&gsessionid=cwDLb-fibu-MUIHea0_Qx1AAJgPh8n1VZjftHzrq458Zsw-wGjNdeg)  
  <sub>20 hours ago</sub>  
  Nvidia is 17.44% of SMH (VanEck, Nov 16), 6.71% of SOXX (iShares, Nov 13), about 20% of SOXL's net assets as 3x index exposure (Direxion, Nov 17) and 200%...
- [TSMC Is Sliding Before Nvidia Reports. Your Chip ETF Is Taking the Hit](https://www.google.com/goto?url=CAESsgEBxCJF17R4Z-7nCv3td9rKdkDYf8AyFVrKwPr_JHfT4K88eWsRrzEeINp85blrbAyAEX9Ebf2dcu_EoyL5jY7rPr2Z0W8Q9rqV3QmqKhR8M1-Had_P2k-ChF2GXda8eu2MGjnkGXdlWLcYn0xnsr33OVsT9IkPHGQpRkAURwgoLm1u6jpOM3-3p8SLewA9GQWBeQtib1hc7g6yBhMpkCajlvj9YTkkTuQjLhLTn3LxCClx&gsessionid=cwDLb-fibu-MUIHea0_Qx1AAJgPh8n1VZjftHzrq458Zsw-wGjNdeg)  
  <sub>20 hours ago</sub>  
  Chip stocks are flinching hours before Nvidia reports, and TSMC's slide is rippling through funds many retirement savers own. Why does one earnings call put...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 457.75 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 504.55 (-9.3%), 50d 553.10 (-17.2%), 200d 524.74 (-12.8%); 50d above 200d
Momentum: RSI(14) 34.9 | MACD -26.078 vs signal -23.588 (histogram -2.490)
Returns: 1d -0.5% | 5d -9.7% | 1m -16.2% | 3m -18.6%
52-week range: 325.10 - 668.91 (now 38.6% of the way up)
Volatility: ATR(14) 23.52 (5.1% of price) | annualised 20d 66.5%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Technology
What it holds: P/E 28.22 | P/B 9.76 | P/S 11.19 | 3y earnings growth n/a
Yield: 0.2%
Three-year record: +42.5% a year | beta to the market 2.12
Cost and size: expense ratio 0.35% | net assets 66.44B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: NVIDIA Corp 20.2%, Taiwan Semiconductor Manufacturing Co Ltd ADR 9.6%, Texas Instruments Inc 5.7%, Broadcom Inc 5.6%, Advanced Micro Devices Inc 5.3%
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

```text
Rolled up from the 5 largest holdings, 46.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.58 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +56.5% above the current prices
Holdings read: NVDA, TSM, TXN, AVGO, AMD
Recent rating changes among them:
  - NVDA: 2026-11-12 Melius Research: down, Buy -> Hold
  - TSM: 2026-11-04 Bernstein: main, Outperform -> Outperform
  - TXN: 2026-10-22 Jefferies: main, Hold -> Hold
  - AVGO: 2026-10-27 Rosenblatt: main, Buy -> Buy
  - AMD: 2026-11-12 B of A Securities: main, Buy -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 11.67M | fund size: 5.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals show no decisive break, fund flows are flat, fundamentals are neutral, analyst view is modestly bullish but covers only 40% of the fund.

**Main reasons it gave:**
- Fund flows flat: 0% change in share count over 1 week and 1 month
- Technical momentum neutral: RSI 51.4, MACD below signal
- Macro stable: yields up modestly, no rate surprise
- Fundamentals high valuation: P/E 29.56, yield 3.6%

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 94.92 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 95.05 (-0.1%), 50d 92.94 (+2.1%), 200d 94.96 (-0.0%); 50d below 200d
Momentum: RSI(14) 51.4 | MACD 0.899 vs signal 1.026 (histogram -0.126)
Returns: 1d +0.0% | 5d -2.2% | 1m +2.9% | 3m -3.7%
52-week range: 87.00 - 100.95 (now 56.8% of the way up)
Volatility: ATR(14) 1.35 (1.4% of price) | annualised 20d 19.2%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Real Estate
What it holds: P/E 29.56 | P/B 2.43 | P/S 4.77 | 3y earnings growth n/a
Yield: 3.6%
Three-year record: +11.0% a year | beta to the market 0.92
Cost and size: expense ratio 0.13% | net assets 69.46B
What it is made of: Stocks 99.4%, Cash 0.3%, Other 0.3%
Largest holdings: Vanguard Real Estate II Index 14.6%, Welltower Inc 8.9%, Prologis Inc 6.5%, Equinix Inc 5.4%, American Tower Corp 4.8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 40.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.7% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2026-11-11 UBS: main, Buy -> Buy
  - PLD: 2026-11-02 Wells Fargo: main, Overweight -> Overweight
  - EQIX: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - AMT: 2026-11-05 Argus Research: reit, Buy -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 370.18M | fund size: 35.14B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: macro environment is hawkish (rising yields, higher VIX) and technicals are bearish (price below short‑term SMAs, negative MACD), but fund flows are strongly positive and analyst coverage of top holdings is bullish, leading to a balanced view.

**Main reasons it gave:**
- US Treasury yields rose across the curve (+0.03% to +0.10% weekly)
- VIX increased 6.8 points to 24.33, indicating elevated volatility
- ETF price below 20‑day and 50‑day SMAs (-4.9% and -5.3%) with negative MACD
- Share count rose 7.5% in the past week, showing net inflows
- Analyst coverage of top holdings shows 75% buy rating and +12.5% price target

<details><summary><b>News</b> — score +0.00</summary>

- [SLS Joins MRNA And ANL In Biotech’s Top 3 This Year — Here’s How A Late-2025 Bet Could Grow 10x From Here](https://es.tradingview.com/news/stocktwits:486670cf8094b:0-sls-joins-mrna-and-anl-in-biotech-s-top-3-this-year-here-s-how-a-late-2025-bet-could-grow-10x-from-here/)  
  <sub>12 hours ago</sub>  
  Among biotech stocks worth at least $500 million, only Moderna and Adlai Nortye ranked ahead of Sellas. STAT columnist Adam Feuerstein acknowledged he had...
- [Why is SLS stock soaring over 220% on Tuesday?](https://invezz.com/in/news/2026/11/17/why-is-sls-stock-soaring-over-220percent-on-tuesday/)  
  <sub>22 hours ago</sub>  
  SLS' experimental vaccine GPS reduced the risk of death by 41% in patients with acute myeloid leukemia. Patients receiving the vaccine lived a median of 24...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 145.12 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 152.54 (-4.9%), 50d 153.29 (-5.3%), 200d 143.25 (+1.3%); 50d above 200d
Momentum: RSI(14) 40.5 | MACD -1.612 vs signal -0.611 (histogram -1.001)
Returns: 1d -0.1% | 5d -7.2% | 1m -5.3% | 3m -11.2%
52-week range: 113.83 - 169.55 (now 56.2% of the way up)
Volatility: ATR(14) 4.75 (3.3% of price) | annualised 20d 39.2%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Health
What it holds: P/E n/a | P/B 0.21 | P/S 0.13 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +27.9% a year | beta to the market 1.01
Cost and size: expense ratio 0.35% | net assets 10.92B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Moderna Inc 2.4%, Natera Inc 1.8%, Halozyme Therapeutics Inc 1.8%, Twist Bioscience Corp 1.8%, Biogen Inc 1.7%
Sector mix: Healthcare 99.4%, Financial services 0.6%
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
Rolled up from the 5 largest holdings, 9.5% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 75.0% | hold 25.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.5% above the current prices
Holdings read: MRNA, NTRA, HALO, TWST, BIIB
Recent rating changes among them:
  - MRNA: 2026-11-09 Goldman Sachs: main, Neutral -> Neutral
  - NTRA: 2026-11-09 Baird: main, Outperform -> Outperform
  - HALO: 2026-11-11 Morgan Stanley: down, Overweight -> Equal-Weight
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - BIIB: 2026-11-09 Piper Sandler: reit, Overweight -> Overweight
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
Share count change: 1 week: +7.5% (757.42M) over 7d | 1 month: +6.0% (615.49M) over 32d
Shares outstanding: 74.83M | fund size: 10.86B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: technicals show a downtrend but no decisive break, macro environment is slightly bearish with higher yields and a strong dollar, and fund flows are flat. Analyst coverage is modestly bullish but limited to 34% of the fund, while fundamentals are moderate.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs, RSI 40.7, negative momentum
- US Treasury yields up across the curve, dollar index up, VIX elevated at 24.33
- Fund flows flat over the past week and month, indicating no net demand shift
- Analyst coverage limited to 34% of fund, all buy with +13.6% price target

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Communication Services Select Sector SPDR ETF (XLC) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLC/)  
  <sub>5 hours ago</sub>  
  Find the latest State Street Communication Services Select Sector SPDR ETF (XLC) stock quote, history, news and other vital information to help you with...
- [What Is Going On With Rigetti Computing Stock on Tuesday?](https://www.benzinga.com/trading-ideas/movers/26/11/63362398/what-is-going-on-with-rigetti-computing-stock-on-tuesday)  
  <sub>20 hours ago</sub>  
  Find out why Rigetti Computing, Inc. (NASDAQ: RGTI) stock is falling on Tuesday amid technology sector pressure, index declines, and recent analyst price...
- [3 Tesla ETFs That Hold It Very Differently](https://www.google.com/goto?url=CAESqgEBxCJF156RzWESuN-3Df6qJwMzR2V6M7r5H9E65yB37hKYwcIG6Aa7cnaEKH3YoBUsuIo0A_vwpdz4LYI0bPsrOgONfmvEhy_AJ9LwQPawluwuBHAjMlUOwSPwI1gg3J_kxOtmaCt3cUsLRzymI6pslPl-8xfd4UL3AKGLYVzmdv6YpXp6WdFJ213AEaL5e9OhMEhGHt3VpzlA0iu5-UWjbN9OJeui-lSGnQ&gsessionid=wKHqTkk71KZ5HvbA8YupzYW2m1IQzFgNoiUv31WqM-WywCc2zviRhQ)  
  <sub>13 hours ago</sub>  
  You can own Tesla directly or hold it inside a fund that also owns other companies. Owning a single stock means living with that company's specific issues,...
- [3 ETFs For Tesla As Its Germany Expansion Changes The Mix](https://www.google.com/goto?url=CAESjAEBxCJF1-Mv72AiA_DGiQALVpW3BRPS1NzeV09sAwockoHF-aPR4H4iCok6p70YayQCNc5ylBe80w85qxG5rwIULI-c2AyjJYDieswf-7WWEWUEN5VS3p0Qq4597bqJnW-F2eJ1Q-G-OOiBbl9caNHnUpGm85fLN7LLD4JsEOGy3Frno1QibFMNFWd1-A&gsessionid=wKHqTkk71KZ5HvbA8YupzYW2m1IQzFgNoiUv31WqM-WywCc2zviRhQ)  
  <sub>2 hours ago</sub>  
  You can own Tesla directly and let every twist in its story hit your portfolio on its own, or you can hold it through a fund alongside many other businesses...
- [BlackRock® Canada Announces November Cash Distributions for the iShares® ETFs](https://www.google.com/goto?url=CAESpgEBxCJF1wPo_4SB5lXPQLzrmpXNAaAD7HWJlzvgxrhXtIkZCM1GLWla7vgKGFqP7j889_gqeYmhh2OaQXZUfJQV5gB_T9sW5aNE-N2galSBWY_p60hdFwiqyH7c4hLtCXwTkfHtu2qgDDWZuo2fuT58ny0pJx-xXcQblKThyMj_HUFZQeR3zHVYtNYPKTutUouiOquZy_B132WUFE6ugqvCa1MpPGVX&gsessionid=wKHqTkk71KZ5HvbA8YupzYW2m1IQzFgNoiUv31WqM-WywCc2zviRhQ)  
  <sub>5 hours ago</sub>  
  TORONTO, Nov. 18, 2026 (GLOBE NEWSWIRE) -- BlackRock Asset Management Canada Limited (“BlackRock Canada”), an indirect, wholly-owned subsidiary of BlackRock...
- [ETFs Are Net Sellers of Sherwin-Williams (SHW) on Nov. 16](https://www.google.com/goto?url=CAEShAIBxCJF18ylTci40snv0fqa4c7MtIdkgzXPVXctn_UefVTxGZbe3KoWr_oeGiu5De5BaJ7gkNkjLVUWjR7ihnPjKqAL2eUbYvzgMKMwakzJ16X8w2uiIJx8FecxbUzi0zzIgGqW5u_dtKoJ7yBVdMbf0KtznqkA_H93Ri1XJsUgvRaiIX9mqbah9c0nmX8h8GAECV2gmreIdlUS7PM3tTAkMSgT4qmUBCilfE2c_TW8bALtO_4VYcMgamZBbD5KsXPkLIZhkFTO2HabnZZ_V8xHxs4fYaBxmBgKtn6I1b-0yVZWbIUV_YvcSnD2DcP3gAdasN20RdaYZPTNf5lJVeZM5ww9IQ&gsessionid=wKHqTkk71KZ5HvbA8YupzYW2m1IQzFgNoiUv31WqM-WywCc2zviRhQ)  
  <sub>3 hours ago</sub>  
  The SPDR Dow Jones Industrial Average ETF (DIA) drove the move, accounting for $29.1 million of the selling as ETF activity turned negative on Monday.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 50.44 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 52.19 (-3.3%), 50d 50.86 (-0.8%), 200d 51.26 (-1.6%); 50d below 200d
Momentum: RSI(14) 40.7 | MACD 0.109 vs signal 0.412 (histogram -0.302)
Returns: 1d -0.8% | 5d -4.9% | 1m -1.5% | 3m -3.8%
52-week range: 42.23 - 53.90 (now 70.4% of the way up)
Volatility: ATR(14) 0.93 (1.8% of price) | annualised 20d 21.7%
Volume: 0.14x the 20-day average
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
Three-year record: +10.8% a year | beta to the market 0.76
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 34.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.71 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.6% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 71.92M | fund size: 3.63B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst coverage is offset by bearish fundamentals (inventory builds, falling price outlook) and bearish technicals, with flat fund flows indicating no net demand.

**Main reasons it gave:**
- Analyst view: 100% buy rating and +14.5% price target for top holdings
- Energy inventories: weekly builds in crude, gasoline, diesel and natural gas (bearish)
- EIA price outlook: forecasted ~13% decline in WTI price over six months (bearish)
- Technicals: price below 20‑day and 50‑day SMA, RSI 39, MACD negative (bearish)
- Fund flows: flat share count, indicating no net demand (neutral)

<details><summary><b>News</b> — score +0.00</summary>

- [What Is Going On With Rigetti Computing Stock on Tuesday?](https://www.benzinga.com/trading-ideas/movers/26/11/63362398/what-is-going-on-with-rigetti-computing-stock-on-tuesday)  
  <sub>Benzinga, 20 hours ago</sub>  
  Find out why Rigetti Computing, Inc. (NASDAQ: RGTI) stock is falling on Tuesday amid technology sector pressure, index declines, and recent analyst price...
- [3 ‘Safe’ Stocks Investors Are Rotating Into Amid the Tech Downturn](https://ng.investing.com/analysis/3-safe-stocks-investors-are-rotating-into-amid-the-tech-downturn-220767)  
  <sub>Investing.com Nigeria, 6 hours ago</sub>  
  Market Analysis by Jesse Cohen covering: Nasdaq 100, S&P 500, Dow Jones Industrial Average, State Street® SPDR® Dow Jones Industrial Average® ETF Trust.
- [9 Of 11 Sectors Fall In Tuesday Trading As Cyclicals Lead](https://www.google.com/goto?url=CAESrwEBxCJF1xreoAd1_ZvZDp7QnIO9IZRgjaJZ8M04370fYcJSxQf637Wj79utQJbkUBfcruwRF-fVZxAAEEkFAco15m5KO1rw0-LAWpKM8Y7JDnxv9FaukwLSCw6a0jXN7ShL5QH1Np7maipmWNwE8CZ6CmmQxweI4McuBYXO4MuZZbdxtqQKj_N9LicCjWadZtAZpUjTJj1Kmu5e-EdwHT_7OeEUHveOcb_C7Vw00NMZ&gsessionid=wSEWVfCWSlULwCGbdgwA3cybLEu7weB-jnzCE2CO8RdnGv90pZLhWA)  
  <sub>Benzinga, 23 hours ago</sub>  
  Two sectors are higher and nine are lower in Tuesday's regular session, with cyclical sectors holding two of the top three positions.
- [ExxonMobil (XOM) Sees $70.3 Million in Net ETF Selling on Nov. 1](https://www.google.com/goto?url=CAESiwIBxCJF1zEuGB7CKMTv-VbfO9s0m7bbGzxxsjCDoGVJBBGIz-o1fKU_8_Pm9SY9pmfbHxsymqEp1HbrtPEukdQi8tSEKEunQFDfm5RUKTIYqg2wVr81IlTOUspT7VQIgYtWO5AcbX3Y9tXt4evVjHo7bC_R2aSzU8YTvi-zcBVt0hYwGW1lAJ8uZemOiwaReK3A5wSA3anrqhhCvl7sGxh234CE3Kzklsb7lFuL2rhkJFYScap8QpNVCXhz8pM79oEjeENWvXnim2ZyXTCRKHzUzqzmn0ULrq6MKzfeQk9FmRiDZJJ_9XzVh_AV9rvoUB3GQ8xw9lXDgqCLJjkAW_LDEWwEFupsLAlekOc&gsessionid=wSEWVfCWSlULwCGbdgwA3cybLEu7weB-jnzCE2CO8RdnGv90pZLhWA)  
  <sub>GuruFocus, 3 hours ago</sub>  
  ExxonMobil (XOM) ended a one-day buying streak on Monday, with ETF flows turning to $70.3 million in net selling. More funds traded the other way,...
- [ETFs Are Net Sellers of Chevron (CVX) on Monday](https://www.google.com/goto?url=CAES_AEBxCJF1_7MsQSgBnEkCNy257YitqqI89iQIUdQYXQfFtKzKNa2_mgmLnSpSDXFQO0y41ZizQE2sK-B_n0gjuAHH9fODzkgX_xiayflLpi4wtbpzvtEplFIct77LKasujlJmZwniSAJp9XM4-ou7-6-VwpyU5cPPfdsejhVvA6YIo5QbB90mDSK_1auOe1jvNNv9eWtamYCWthIB8NCzK_UnJgmF867Tjftq3AGpznnqytPWe_Jw2QvedaMQO630nJzo5D7OVqfKggF186qS7zVmp0LqhCISZVaIBKmPG9k28ruVO25INi1hbwDaDNFIGs0GXEQ2n0o0KAuGBw&gsessionid=wSEWVfCWSlULwCGbdgwA3cybLEu7weB-jnzCE2CO8RdnGv90pZLhWA)  
  <sub>GuruFocus, 3 hours ago</sub>  
  On Monday, 37 ETFs were buying Chevron (CVX) shares versus 15 selling, but the sellers moved larger amounts, producing a net $169.5 million in ETF selling.
- [ETFs Are Net Sellers of ConocoPhillips (COP) on Monday](https://www.google.com/goto?url=CAESmAEBxCJF1w1wQSde05EyyK4WQlu4CDSWz-AHaTYmYxtuF7w7MQ-vW82Eu8w3gmpp5PQ1gdFy_WMgH8A7wWlYWqxN9-53Z7mWXCtR6EwYDUscGlE3vEUJx0jfoXP5QG8wjZgddNIDv1_UwZnfHHGBrcBsxMBnQ2qGP1SUM0gPegVMsGUuBWbjlLUmCQR7CA7VKvUt1muvGP71tg&gsessionid=wSEWVfCWSlULwCGbdgwA3cybLEu7weB-jnzCE2CO8RdnGv90pZLhWA)  
  <sub>GuruFocus, 3 hours ago</sub>  
  Thirty-six ETFs were buying ConocoPhillips (COP) shares on Monday versus 8 selling, yet the net dollar value of ETF activity came to -$17.3 million in...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 62.05 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 65.43 (-5.2%), 50d 64.88 (-4.4%), 200d 59.66 (+4.0%); 50d above 200d
Momentum: RSI(14) 39.0 | MACD -0.776 vs signal -0.441 (histogram -0.335)
Returns: 1d -2.1% | 5d -2.1% | 1m -8.7% | 3m -2.7%
52-week range: 43.81 - 70.02 (now 69.6% of the way up)
Volatility: ATR(14) 1.58 (2.5% of price) | annualised 20d 31.5%
Volume: 0.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.40</summary>

```text
Fund type: Equity Energy
What it holds: P/E 17.48 | P/B 2.46 | P/S 1.71 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +19.1% a year | beta to the market -0.22
Cost and size: expense ratio 0.08% | net assets 46.37B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ExxonMobil Holdings Corp 24.3%, Chevron Corp 18.3%, ConocoPhillips 7.3%, Marathon Petroleum Corp 4.6%, Phillips 66 4.5%
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
US inventories, week ending 2026-11-06 (published the following Wednesday)
  Crude oil: 414.4 million barrels, +4.7 on the week (a build), 21% percentile over 52 weeks
  Petrol: 210.8 million barrels, +1.8 on the week (a build), 35% percentile over 52 weeks
  Diesel: 103.3 million barrels, +4.1 on the week (a build), 21% percentile over 52 weeks
  Natural gas: 3,862.0 billion cubic feet, +61.0 on the week (a build), 94% percentile over 52 weeks -- high for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 59.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.10 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.5% above the current prices
Holdings read: XOM, CVX, COP, MPC, PSX
Recent rating changes among them:
  - XOM: 2026-11-12 Bernstein: main, Outperform -> Outperform
  - CVX: 2026-11-12 Bernstein: main, Market Perform -> Market Perform
  - COP: 2026-11-12 Bernstein: down, Outperform -> Market Perform
  - MPC: 2026-11-05 Piper Sandler: main, Overweight -> Overweight
  - PSX: 2026-11-04 Citigroup: main, Neutral -> Neutral
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 186.42M | fund size: 11.57B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no material macro surprise, mixed technicals, flat flows, modest fundamentals, but strong analyst consensus.

**Main reasons it gave:**
- Analyst consensus 100% buy with +8.9% price target
- Fund flows flat over past month (no net inflow/outflow)
- Technicals: price below 20‑day SMA and MACD histogram negative
- Macro: yields up modestly and VIX up 6.8 points (no surprise)

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Financial Select Sector SPDR ETF (XLF.MX) Seasonal Returns Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/XLF.MX/seasonality/)  
  <sub>Yahoo! Finance Canada, 3 hours ago</sub>  
  State Street Financial Select Sector SPDR ETF (XLF.MX) seasonal returns chart provides the mean and median returns by month to inform your investment...
- [What Bank Capital Rules Could Mean For Funds With Bank Exposure](https://simplywall.st/etfs/us/nasdaq-kbwb/news/what-bank-capital-rules-could-mean-for-funds-with-bank-expos)  
  <sub>Simply Wall St, 2 hours ago</sub>  
  How different are three bank themed funds when the rules that shape their balance sheets are about to change? That is the question investors are really...
- [Webcast: After the Run-Up: Positioning Portfolios with Options-Based Strategies for 2027 | ETF Trends](https://www.google.com/goto?url=CAES5AEBxCJF18A6QVlwQ95YbSwNeD7V0debx9b54W6ps57Ff5twfG2OMA3Ba7GcIdI7JUild56p32hsuOAFQndRhrZ1ulfC_9CrL2C_7DH4x_omdXkwMYBo2FkSNDue0GDbK11AMHca62twPKXrumpry8-rvtl_9nC7CkZSAT9hd8el8HqXziDLuf4a2nnO0E3ITedf9kgv9ls2iSArkSQAjZcQu5xuJqtKjgLxZtJNYAolT3TpHN44ef_ggg5HVOmfla-R7wqousNGj4btF72u429B7zclyN-Hh_OV5PlUIMKMs7WH9Qg&gsessionid=3esPBsTt5qccXHjItBVv0ibY4ZCghW5n8e-c0X95cpKtcHFFsdMzqQ)  
  <sub>Advisor Perspectives, 18 hours ago</sub>  
  Join us for a practical look at how advisors can position portfolios using options-based strategies heading into 2027.
- [Futures Mixed; Nvidia Tops, Fed's Waller Warns Of 'Shock' Rate Hike](https://www.google.com/goto?url=CAESrgEBxCJF1w2bx6Kr7APgrQwiw8vcDLQfWZ1RzzxNiuHxVB7sr6aJn5aXAl86BscE0vdrnpR4gW-lj6XfMhtwWDGTJt6s7c8XKxuyizbSm-MbVulOu_AN4WqeIciYZTxTL4syUDAuG8ZPPCd81grcJXue4FBmQkSt5T3WHYB7YkknoDNLaYduPSRmhQNcJkSG9Mr_-rQxGs0Tn7T_JyREvo-VX50R9Le9tAoLpHwC2Rk&gsessionid=3esPBsTt5qccXHjItBVv0ibY4ZCghW5n8e-c0X95cpKtcHFFsdMzqQ)  
  <sub>Investor's Business Daily, 2 hours ago</sub>  
  Dow Jones futures: Nvidia and Target earnings topped views. Fed Gov. Waller said inflation is "spreading out." The Anthropic IPO looms.
- [56.71 [XLFUSDT] Futures, USDT-Margined Perpetual Contract](https://www.google.com/goto?url=CAESYgHEIkXXbKCKpNtJMDiQwlIjovkfH91HI0iTEvnone3wHrQ0k7dwrGG3WoNQ2qu4mpdTkYJC7YIWoD0ViC_lFunkfdM2MNOH5L7pF4YgTC7j3JE16np4budNgky-gy3jtZTV&gsessionid=3esPBsTt5qccXHjItBVv0ibY4ZCghW5n8e-c0X95cpKtcHFFsdMzqQ)  
  <sub>MEXC, 3 hours ago</sub>  
  Trade XLFUSDT Futures on MEXC with ultra-low fees, deep liquidity, and up to 20x leverage. Experience lightning-fast order execution and top-tier security...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 56.67 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 57.32 (-1.1%), 50d 55.96 (+1.3%), 200d 54.00 (+4.9%); 50d above 200d
Momentum: RSI(14) 47.8 | MACD 0.521 vs signal 0.638 (histogram -0.118)
Returns: 1d -0.7% | 5d -3.3% | 1m +1.7% | 3m -0.5%
52-week range: 47.81 - 59.20 (now 77.8% of the way up)
Volatility: ATR(14) 0.89 (1.6% of price) | annualised 20d 22.8%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Financial
What it holds: P/E 15.26 | P/B 2.28 | P/S 3.26 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +20.5% a year | beta to the market 0.68
Cost and size: expense ratio 0.08% | net assets 53.58B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Berkshire Hathaway Inc Class B 12.7%, JPMorgan Chase & Co 11.2%, Visa Inc Class A 8.8%, Mastercard Inc Class A 6.5%, Bank of America Corp 4.1%
Sector mix: Financial services 98.2%, Technology 1.6%, Industrials 0.3%
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
Rolled up from the 5 largest holdings, 43.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.86 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +8.9% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 883.44M | fund size: 50.06B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no material macro surprise, bearish technicals but low volume, flat fund flows, thin analyst coverage with modest bullish bias.

**Main reasons it gave:**
- 10-year Treasury yield rose 10 bps to 5.10% (up 0.10% on the week)
- Industrial output fell 0.4% in October
- XLI price below 20‑day, 50‑day, and 200‑day SMAs; RSI 42.9; MACD negative; volume 0.14× 20‑day average
- Fund share count unchanged (+0.0% week, +0.0% month)
- Analyst ratings for top holdings 100% buy with +27.3% price target, covering 24% of fund weight

<details><summary><b>News</b> — score +0.00</summary>

- [Humyn Labs raises $47M to expand robot training data business (XLI:NYSEARCA)](https://seekingalpha.com/news/4674181-humyn-labs-raises-47m-to-expand-robot-training-data-business)  
  <sub>41 minutes ago</sub>  
  Humyn Labs secures $47 million to expand robotics training data; it cites over $50 million in annualized revenue within six months, not full-year sales.
- [Invesco S&P 500 Equal Weight ETF (RSP) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RSP/)  
  <sub>14 hours ago</sub>  
  Find the latest Invesco S&P 500 Equal Weight ETF (RSP) stock quote, history, news and other vital information to help you with your stock trading and...
- [1. iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT)](https://www.google.com/goto?url=CAESowMBxCJF1xu_1LF-1sXboIKUJfJmJxHXgesfW7OQT_VFD_jdd8mGuGo011aF1zasOhagyW3EwygHLOjZxs5auI0RYqh2M_mPWEA2tC7JlCWQmSYd1wrZfPZSKBBm66kVJeUDaZYg3ZJ-io9vYgJuTRDZiuMt3GBxvRbU7VAg6Fkapb3XAoNwYYQGmRqpBmRH_1qJOL6NSEH0PapJvTFizdJHiG3Llalzu2BW1Fg8uP1dwhKVWKElzxc1CsS7psvDhLPOYpECZHlZ8kNMkJhGyfQyTd-3TzS3wwzRKeOBJE9k6yK0KuBrXz0nMAIGjLB4bubVMe9BzG1l9cH7PGyedakYtHHdYt42szi7og_e1HVIz8pOF71zcV7YHNWM70MYUmBVy91rBKvY15xIf_F_3ut_IJjgfB85HS9atwhXzE2uM_EAqRbfwsLCwebrvI4ohR_Z2zhEgivsj7HcUO781YM_KWktizuAIajfuSEIdnOzimNRfQDuXoF7hwHZbQXPCTNRWW1Bq6lqK2uLuxa9F9HLVGaXxdiJGUgj4Yuhn9WQgl4cAw&gsessionid=tIEVA0BOEjgRpxLJJfwkeX5LxoFV_IwiYX07N-JqlJE-IQ1Culbvjg)  
  <sub>21 hours ago</sub>  
  Of the five, iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) is the most sensitive to rates. Because it holds Treasuries with maturities of 20 years or more...
- [EXI: Industrials Dashboard For November (NYSEARCA:EXI)](https://www.google.com/goto?url=CAESjAEBxCJF16mgWgp0caxSqPQH7ee8ZnZjJFAh8N0w0CDJtH95HIaMqLrJNfbSa6M7fiJl4lUij_S_odaRJKwK7KZFp7rBRaD4gBG-SPNCDG5AKj-uXXPhktqi99THMPuS8Jy_nhzN5_vQoKoitmJ5FcUF3Xoq1yyhITJauqkubdAYKeVhpqc0ZfZozk-JUA&gsessionid=tIEVA0BOEjgRpxLJJfwkeX5LxoFV_IwiYX07N-JqlJE-IQ1Culbvjg)  
  <sub>19 hours ago</sub>  
  The iShares Global Industrials ETF offers ex-U.S. diversification, lower company risk, and better fundamentals than XLI.
- [Does October's 0.4% Decline in Industrial Output Signal Trouble for Industrial Select Sector SPDR Fund (NYSEARCA:XLI)?](https://www.google.com/goto?url=CAES0wEBxCJF134RH8I0xtN4btxQ8hcFa1hkEWnQN3s0Mg8HaClRjbOR6rc0gZ_XJLRi9Ihdv2ZAb0FAp-6XTmOtcxwZucoLDyT-y2Ibc2tBuGzNAXwVjo56FxlNpQjHBPw3VtJKFocYxm6WwZ7UH1wDzfgE29MWBVuPdFkNT4I9aMs2SMV9LGRf5XTAFQNHrdHh_afl-DsA5gyxN7luv06MF8uENPfIPGnWT8EnQ3rdfG0f3HEBu5ygQyc95Epq6KVnCWU4IGGXcKRunNf9HWH0gsacmUMb&gsessionid=tIEVA0BOEjgRpxLJJfwkeX5LxoFV_IwiYX07N-JqlJE-IQ1Culbvjg)  
  <sub>5 hours ago</sub>  
  Does October's 0.4% Decline in Industrial Output Signal Trouble for Industrial Select Sector SPDR Fund (NYSEARCA:XLI)?
- [How Might October Retail Sales With a Forecast 0.2% Gain Affect SPDR S&P Retail ETF (NYSEARCA:XRT)?](https://www.google.com/goto?url=CAESwAEBxCJF11X4GShGxhDfXZEdhizr01qLwOTK4DNS0WDhQwTFoGZ49OC8YYQ_CyQTyZ7ESxtSqSCi6GfKRDFuSW7wP_ankQVbO1oDO3vPeLsHMlXScwI735tESNW6KHcEmhzoCY0mKhcn6YDzYBTfiQobNh9fM5MIIR15_asG9qVfy6zpvlmMAXJ0nIUxjxewyKbcWsooAJvN9FlseV2e6eRa0uCb_WfwqRXLUbSdhPxh7wOh3bdeaD2qMpe1o1G9K3o&gsessionid=tIEVA0BOEjgRpxLJJfwkeX5LxoFV_IwiYX07N-JqlJE-IQ1Culbvjg)  
  <sub>21 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports. Become a Kalkine member...
- [How Do a 10-Year Yield Over 5.1% and the Dollar's Best Level Since April 2025 Affect iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT)?](https://www.google.com/goto?url=CAES4QEBxCJF1ydqKDIwyqwg1CMirNJyLlHk9C5DBb8gf3-A6LeM9zi4VKGGzV6GDKbO3iBGVLCllg8b7vpysnNUNYfnnDbJy-TgHa5rckeThuim1c0ch9hS5qGkbbkjSecC44z7EE0YteYLO5NwbT-0Ubi9gja8u2ls3fcSBxGwZAch9zz2PoR50zWSUrfDghejHkCjmU-YqRPDn4yMikNHQO8KeuuiXfeiEPx7cI83-EKfTlscBsF1xZYbqjMEMLjBrPvE93FrSTcQjVhEso267Q1_w_YIOTi0KD0Rg1n-SJ2YWn4&gsessionid=tIEVA0BOEjgRpxLJJfwkeX5LxoFV_IwiYX07N-JqlJE-IQ1Culbvjg)  
  <sub>21 hours ago</sub>  
  How Do a 10-Year Yield Over 5.1% and the Dollar's Best Level Since April 2025 Affect iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT)?
- [How Might a Near-Certain December Fed Hike Affect iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) Ahead of the FOMC Minutes?](https://www.google.com/goto?url=CAES2wEBxCJF13sFrRemL579rk8Ye0RLmdV1vGuzKVg7H1Wx6zd0QxuE5XWjzciwR9_RroLMR_Hfq9panuj2_msYAzUmqbsjscsjz6tc3ZxpPldGZIe1jTIQ_aBQ4ZkVVlM_qOJ5vOOz4-Zlaw9FZwkqZbh8BXecQRswIZyvjvKqc_2WsfHdiDHrLZB4vXq5RcziE6lUD1ewtZ2GubWy0ihUqL1S3kL5E-7lWWX0qdDFAn9HRs-RdmzhbS3ZgOoPKc-QeNc1KBw4Abnk0RO5cPl6kHkEZ7RlGuYQMp9R3ME&gsessionid=tIEVA0BOEjgRpxLJJfwkeX5LxoFV_IwiYX07N-JqlJE-IQ1Culbvjg)  
  <sub>21 hours ago</sub>  
  How Might a Near-Certain December Fed Hike Affect iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) Ahead of the FOMC Minutes?
- [What Is Behind the Real's 19-Month Low and the Pressure on the iShares MSCI Brazil ETF (NYSEARCA:EWZ)?](https://www.google.com/goto?url=CAESxQEBxCJF1324Ud3jV8gWVQK0qRTOh4HF_qKJ9qd4r7cwd5bi3BGtALW_ow53qzcF5AhmxI7gHI19nKBKR1FwCD1N_u_jmrhxkVd9pjwZ2oqb_D5wljiccfmTjOQBrJ3iHDP2j_elYfbAkxikFguZEJoK8SDS8Y1crRrKfJMmIbh2Vj3qlflUEmFG5TD0jZTmxh-01mYAu1qmhauSYZF1GOkjWqb4uop8siAP1Why0235ATSKmNiFXuglT42aTVSunZ-kVsKtZw&gsessionid=tIEVA0BOEjgRpxLJJfwkeX5LxoFV_IwiYX07N-JqlJE-IQ1Culbvjg)  
  <sub>21 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [What Did Fed Chair Warsh Say on AI and Employment, and Why Might It Matter for SPDR S&P 500 ETF Trust (NYSEARCA:SPY)?](https://www.google.com/goto?url=CAES0wEBxCJF1wh3MVX4WpJgnTnoKOQBQbhip7u_TOyZXJwOVgakV9fYd36SOytAgCTscOEWWo7u1-H-XFypFiXEK-M1JpQj8OFmXUnJHUvKK37NpOrsMv1JsKFhcTdA-m2L6ofDIerJrF_7BHMkU9N8tEbboeXF3yCDAr_ml2D6rMYzEWLSh9-LNghEF5wOYaWgC1x5b7pqOsbFQ8D8gIycq5fn4dRNOCLB9au1tvwuLYyjxzx94elNOSrr_CaPOq5awR9D8EsXL6Cln2PpcKgT3TG1b5f6&gsessionid=tIEVA0BOEjgRpxLJJfwkeX5LxoFV_IwiYX07N-JqlJE-IQ1Culbvjg)  
  <sub>21 hours ago</sub>  
  What Did Fed Chair Warsh Say on AI and Employment, and Why Might It Matter for SPDR S&P 500 ETF Trust (NYSEARCA:SPY)?

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 164.70 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 167.49 (-1.7%), 50d 168.43 (-2.2%), 200d 173.42 (-5.0%); 50d below 200d
Momentum: RSI(14) 42.9 | MACD -0.757 vs signal -0.555 (histogram -0.203)
Returns: 1d -0.0% | 5d -3.7% | 1m -1.3% | 3m -8.4%
52-week range: 147.83 - 186.51 (now 43.6% of the way up)
Volatility: ATR(14) 3.03 (1.8% of price) | annualised 20d 25.8%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Industrials
What it holds: P/E 26.85 | P/B 6.33 | P/S 2.84 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +18.1% a year | beta to the market 1.00
Cost and size: expense ratio 0.08% | net assets 31.20B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: GE Aerospace 5.9%, Caterpillar Inc 5.4%, RTX Corp 5.1%, GE Vernova Inc 4.3%, Union Pacific Corp 3.4%
Sector mix: Industrials 93.0%, Technology 6.5%, Basic materials 0.4%, Consumer cyclical 0.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 24.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.3% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 136.63M | fund size: 22.50B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no material macro surprise, flat fund flows, mixed signals from bullish analyst view versus bearish technicals and sector rotation.

**Main reasons it gave:**
- Fund managers reduced tech overweight from 37% to 12% in the past month, indicating sector rotation away from tech
- US Treasury yields rose across the curve (+0.03 to +0.10% on the week) and the yield curve remains upward sloping
- VIX rose 6.8% on the week to 24.33, reflecting higher market volatility
- Technical indicators show XLK below its 20‑day, 50‑day and 200‑day SMAs, RSI 33.4 (oversold), negative MACD, and volume at 0.25× 20‑day average

<details><summary><b>News</b> — score +0.00</summary>

- [Fund Managers Are Cutting Tech at the Fastest Pace Since 2006](https://247wallst.com/investing/2026/11/18/fund-managers-are-cutting-tech-at-the-fastest-pace-since-2006/)  
  <sub>2 hours ago</sub>  
  Fund managers slashed tech overweight from 37% to 12%, the biggest one-month drop since 2006, leaving XLK and QQQ exposed to AI spending fears.
- [What's Going On With Bloom Energy Stock Tuesday?](https://www.benzinga.com/trading-ideas/movers/26/11/63361008/whats-going-on-with-bloom-energy-stock-tuesday-4)  
  <sub>20 hours ago</sub>  
  Bloom Energy stock falls as investors question AI infrastructure spending and rotate out of technology stocks.
- [Bill Ackman Cut His Microsoft Stake. Your S&P 500 Fund Can’t.](https://www.google.com/goto?url=CAESpgEBxCJF18n-Yf8tBHuzMyKyyv9dZyjneSG8yfJ7uCyWfAgRDwXJZfsJTJe902rdHFItF25hByfsMRrDH4TwNbpNldHXpP_7OjEuk-5lhPqNCr_-BDqytsYgxrDslR2rb1msyq1X7nb7oAeidH_m_QtHrFAHKhaskB_hEs3Qrjydf-F-VpFEQM2XBW3ZegcdnfVbRqXcUHgiZ8PDmKHr5mPM8LOMh_IF&gsessionid=ts1OwyYNxmWFYA9C3jJr-jaq5XgvV3xGZizLNDjzmzAJ5LMBW3_Ckg)  
  <sub>21 hours ago</sub>  
  A hedge fund can trim Microsoft the moment its view shifts. If you own it through a 401(k), an IRA, and a brokerage account, you may hold far more of the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 162.40 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 175.18 (-7.3%), 50d 185.65 (-12.5%), 200d 171.11 (-5.1%); 50d above 200d
Momentum: RSI(14) 33.4 | MACD -6.297 vs signal -5.449 (histogram -0.848)
Returns: 1d -0.5% | 5d -6.9% | 1m -12.4% | 3m -11.3%
52-week range: 127.50 - 202.00 (now 46.8% of the way up)
Volatility: ATR(14) 5.44 (3.4% of price) | annualised 20d 44.7%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Technology
What it holds: P/E 31.66 | P/B 11.55 | P/S 8.87 | 3y earnings growth n/a
Yield: 0.5%
Three-year record: +22.4% a year | beta to the market 1.56
Cost and size: expense ratio 0.08% | net assets 118.67B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Apple Inc 15.3%, NVIDIA Corp 15.1%, Microsoft Corp 11.8%, Broadcom Inc 4.7%, Advanced Micro Devices Inc 4.5%
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
Rolled up from the 5 largest holdings, 51.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.70 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +34.1% above the current prices
Holdings read: AAPL, NVDA, MSFT, AVGO, AMD
Recent rating changes among them:
  - AAPL: 2026-11-11 China Renaissance: up, Hold -> Buy
  - NVDA: 2026-11-12 Melius Research: down, Buy -> Hold
  - MSFT: 2026-10-29 Bernstein: main, Outperform -> Outperform
  - AVGO: 2026-10-27 Rosenblatt: main, Buy -> Buy
  - AMD: 2026-11-12 B of A Securities: main, Buy -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 272.06M | fund size: 44.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, mixed technical picture, and modest analyst bullishness do not provide a clear catalyst for a directional call.

**Main reasons it gave:**
- No macro surprise: yields rose modestly, no policy shock
- Fund flows flat: no net creation/redemption
- Technical picture mixed: price above SMAs but MACD slightly bearish and low volume
- Analyst consensus 100% buy with +2.9% price target

<details><summary><b>News</b> — score +0.00</summary>

- [Own P&G Stock For Safety? Watch Bond Yields](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afdbc7360554cd39bdfb0d9681b475f&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2fown-p-g-stock-safety-134156249.html&c=3045101107090426062&mkt=en-us)  
  <sub>Yahoo Finance, 11h ago</sub>  
  So staples now trade partly like bonds. A P&G holder owns a position that leans against tech and toward falling yields. If AI stocks recover while yields rise, we think both parts of that position ...
- [Lock In the Consumer Staples Sector with This ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afdbc7360554cd39bdfb0d9681b475f&url=https%3a%2f%2fwww.tipranks.com%2fnews%2farticle%2flock-in-the-consumer-staples-sector-with-this-etf&c=3764668531894399783&mkt=en-us)  
  <sub>TipRanks, 27h ago</sub>  
  Monday was another rough day for the major indexes. On the other hand, it was a pretty good day for the consumer staples sector. Consider that the S&P 500 is ...
- [FSTA: Consumer Staples Dashboard For November](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afdbc7360554cd39bdfb0d9681b475f&url=https%3a%2f%2fseekingalpha.com%2farticle%2f4969277-fsta-consumer-staples-dashboard-for-november&c=15097713662868740843&mkt=en-us)  
  <sub>Seeking Alpha, 10h ago</sub>  
  The Fidelity MSCI Consumer Staples Index ETF offers broad sector exposure with slightly better growth and historical returns than XLP.
- [Quick spark: Walmart stock has best 2-month run against S&P 500 since 1975](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afdbc7360554cd39bdfb0d9681b475f&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2ftop-stocks%2fquick-spark-walmart-stock-has-best-2-month-run-against-s-p-500-since-1975%2far-AA2hDi9R&c=9386689500876888072&mkt=en-us)  
  <sub>Benzinga on MSN, 30h ago</sub>  
  Since the end of September, Walmart Inc. (NASDAQ:WMT) has climbed about 23%, while the S&P 500 has slipped roughly 4%. Measured as a ratio, Walmart has outperformed the index by 28% over two months, ...
- [ETFs Are Net Sellers of Coca-Cola (KO) on Nov. 16](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afdbc7360554cd39bdfb0d9681b475f&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2fetfs-net-sellers-coca-cola-110222816.html&c=8800551807698479709&mkt=en-us)  
  <sub>Yahoo Finance, 12h ago</sub>  
  Every ETF and guru trade in KO is tracked on the KO guru trades page. The largest sellers by dollar value were DGRW ($228.8 million), DIA ($8.3 million) and XLP ($4.2 million). In all, 43 ETFs added ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 91.30 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 90.15 (+1.3%), 50d 86.12 (+6.0%), 200d 84.99 (+7.4%); 50d above 200d
Momentum: RSI(14) 59.1 | MACD 1.605 vs signal 1.667 (histogram -0.062)
Returns: 1d -0.2% | 5d -0.2% | 1m +4.0% | 3m +7.0%
52-week range: 76.51 - 92.60 (now 91.9% of the way up)
Volatility: ATR(14) 1.43 (1.6% of price) | annualised 20d 24.2%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Consumer Defensive
What it holds: P/E 24.06 | P/B 4.52 | P/S 1.32 | 3y earnings growth n/a
Yield: 2.5%
Three-year record: +13.0% a year | beta to the market 0.39
Cost and size: expense ratio 0.08% | net assets 15.03B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Walmart Inc 11.1%, Costco Wholesale Corp 9.1%, Procter & Gamble Co 7.6%, Coca-Cola Co 7.4%, Philip Morris International Inc 6.6%
Sector mix: Consumer defensive 97.0%, Financial services 1.5%, Consumer cyclical 1.5%
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +2.9% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 210.17M | fund size: 19.19B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The analyst view is moderately bullish (80% buy rating and +10.8% price target for top holdings covering 39.4% of the fund), but fund flows are flat indicating no net demand, and macro conditions (rising Treasury yields and upward‑sloping curve) pressure utilities while technicals show price below the 200‑day SMA, MACD below signal, and low volume. With no material policy surprise or decisive technical break, the overall stance remains neutral.

**Main reasons it gave:**
- Analyst coverage: 80% buy rating and +10.8% price target for top holdings (39.4% weight)
- Fund flows: flat share count over 1 week and 1 month (no net inflows/outflows)
- Macro: 10‑year Treasury yield up 10 bps to 5.10% and upward‑sloping curve, raising rate pressure on utilities
- Technicals: price below 200‑day SMA, MACD below signal, low volume, indicating weak bullish momentum

<details><summary><b>News</b> — score +0.00</summary>

- [Utilities Select Sector SPDR Fund (XLU) Stock Price | Quotes & News](https://www.moomoo.com/stock/XLU-US?chain_id=Name1K9-3FXPhg.1lfqj7g&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A107%2C%22f%22%3A%22www.moomoo.com%2Fetfs%2FSMN-US%22%7D)  
  <sub>7 hours ago</sub>  
  Track the latest Utilities Select Sector SPDR Fund (XLU) price, quotes, financial information, news, and analyst ratings on moomoo App for your ETF trading...
- [Do Wall Street Analysts Like Entergy Stock?](https://www.barchart.com/story/news/8893996/do-wall-street-analysts-like-entergy-stock)  
  <sub>3 hours ago</sub>  
  Entergy has outperformed the broader market over the past year, and analysts are highly optimistic about the stock's prospects.
- [Morgan Stanley (MS): Structured notes tied to four indexes, due December 2027](https://www.google.com/goto?url=CAESjAEBxCJF169U8BpwazkI-ZcMmaUda_IoPuOBVLzBIW6J7RgUX-rkJRyE3PbxtDfl1k6WowNtH1uPfli6RZHWAw5zqacDe-kjUFnQr1upyhMMQzQcXyJFkJMTo13pUrDBA7I3YYmEwhWGsNdRfA3G4Iiz9BL7Edj2IJXeK9upM1LDJ2iNzWYKOmtQc9oz0w&gsessionid=XjGF9idNpUI-f-VcxdLGRdZDhzDXHzbAAkekHB2GmcjXHGRGQ9HE7g)  
  <sub>17 hours ago</sub>  
  Morgan Stanley Finance LLC plans to sell market linked securities due December 10, 2027, with returns tied to the lowest performing of four underlyings: the...
- [Is Wall Street Bullish or Bearish on WEC Energy’s Stock?](https://www.google.com/goto?url=CAESnQEBxCJF1xcI2Oe-QWUdYODs-EXN3UAOlFZUK1twXgtJKhdlpDhmkD44EnLwKS0738KcQEUhFwgrpGOI9LpZ4pMDV7d5UP0aGtundt37L_OsCfXkATtuSw0T49pUAoCj7eJFBY-YIL23_3BzhnGq_pLZV8D3LCIfUXDooyZMA-wbQjcMgeXA27klQZP1uorykarO2GcgTaVuMBtlKMZd&gsessionid=XjGF9idNpUI-f-VcxdLGRdZDhzDXHzbAAkekHB2GmcjXHGRGQ9HE7g)  
  <sub>21 hours ago</sub>  
  WEC Energy Group, Inc. (WEC), headquartered in Milwaukee, Wisconsin, is a regulated utility holding company serving millions of customers across Wisconsin,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 43.51 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 43.36 (+0.3%), 50d 41.92 (+3.8%), 200d 44.34 (-1.9%); 50d below 200d
Momentum: RSI(14) 56.4 | MACD 0.487 vs signal 0.528 (histogram -0.042)
Returns: 1d +0.2% | 5d -0.7% | 1m +3.9% | 3m -0.6%
52-week range: 39.25 - 47.73 (now 50.2% of the way up)
Volatility: ATR(14) 0.59 (1.3% of price) | annualised 20d 14.1%
Volume: 0.12x the 20-day average
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
Three-year record: +15.8% a year | beta to the market 0.34
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
Ratings by weight: buy 80.0% | hold 20.0% | sell 0.0% (mean 2.03 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.8% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 163.27M | fund size: 7.10B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; macro slowdown and higher rates weigh on consumer discretionary, while analyst consensus remains bullish and flows are flat.

**Main reasons it gave:**
- U.S. consumer spending forecast slowdown to 2%-2.5% (Pantheon)
- Treasury yields up across curve; 10-year at 5.10% (+0.10) indicating higher rates
- VIX up 6.8 points to 24.33, showing elevated market volatility
- Analyst consensus 100% buy with weighted price target +15.5% above current price
- Fund flows flat with no net share creation or redemption

<details><summary><b>News</b> — score +0.00</summary>

- [3 ETFs For Tesla As Its Germany Expansion Changes The Mix](https://uk.finance.yahoo.com/news/3-etfs-tesla-germany-expansion-131023445.html)  
  <sub>Yahoo Finance UK, 2 hours ago</sub>  
  You can own Tesla directly and let every twist in its story hit your portfolio on its own, or you can hold it through a fund alongside many other businesses...
- [3 Tesla ETFs That Hold It Very Differently](https://simplywall.st/stocks/us/automobiles/nasdaq-tsla/tesla/news/3-tesla-etfs-that-hold-it-very-differently)  
  <sub>Simply Wall St, 13 hours ago</sub>  
  You can own Tesla directly or hold it inside a fund that also owns other companies. Owning a single stock means living with that company's specific issues,...
- [U.S. consumer spending set to slow as inflation and higher rates bite (XLY:NYSEARCA)](https://www.google.com/goto?url=CAESuQEBxCJF1-0wH_gCmbPto9o17fpgTVV0i_O9DeD6m4vLtLYeJdCnri35aXMLedWR5MXMMLqup4-B_PUvBYISjg5MTZuuzLmYk5yl9qhpXbWNzx1TFQCgnX5H05PsZbh2NQ5pSUcpJ3tnuteoXN5B8V9n1ciIE-7irlkf1lcx-2JQ_dQQwDSeGwksLXVPlSrKRUG2l3ZeXl01a6S4UK8aSKFcoZ3F5lTjAi3sfOt92ZMEJHnBzLzHT70efA&gsessionid=TKlooBkqXHy_ag_cxPeShz5ha_YYVw-MMU_MV8SXnEXrcjpLZ-MrTQ)  
  <sub>Seeking Alpha, 57 minutes ago</sub>  
  Pantheon forecasts U.S. consumer spending growth to slow to 2%-2.5% in Q4 2026 from 3.8% in Q3; October retail sales control group rose 0.6%.
- [Consumer ETFs Slipped As CEOs And Forecasts Shifted](https://www.google.com/goto?url=CAESjQEBxCJF1xoxiADjasy6EyFOM-9Y4Pn14jnbj-GBQCMG5WE5g9gROMMIEzDfLCqlOA-8zodNdHgUw_eW5xpOQoue20L380M2WY-DgQ_OELngetHRL93AEMcJ7-h-54ul24ULPdUrejbdl2OXHmumsFG5lSfotpekAHaQLmbppDbVa3H_1Y0vJhXn_6KMwSc&gsessionid=TKlooBkqXHy_ag_cxPeShz5ha_YYVw-MMU_MV8SXnEXrcjpLZ-MrTQ)  
  <sub>Finimize, 17 hours ago</sub>  
  Home Depot narrowed its full-year outlook while Redbook data pointed to early holiday promotions keeping US spending active ahead of Black Friday.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 118.43 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 117.75 (+0.6%), 50d 114.07 (+3.8%), 200d 115.39 (+2.6%); 50d below 200d
Momentum: RSI(14) 54.1 | MACD 1.387 vs signal 1.629 (histogram -0.243)
Returns: 1d +1.1% | 5d -2.1% | 1m +2.5% | 3m +1.5%
52-week range: 105.66 - 124.52 (now 67.7% of the way up)
Volatility: ATR(14) 2.18 (1.8% of price) | annualised 20d 27.8%
Volume: 0.17x the 20-day average
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
Three-year record: +13.4% a year | beta to the market 1.10
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 54.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.5% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, TJX
Recent rating changes among them:
  - AMZN: 2026-11-03 Freedom Broker: main, Buy -> Buy
  - TSLA: 2026-11-05 GLJ Research: reit, Sell -> Sell
  - HD: 2026-11-10 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-11-06 Argus Research: main, Buy -> Buy
  - TJX: 2026-11-10 UBS: main, Buy -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 120.25M | fund size: 14.24B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Argentina (ARGT) · Sector or country — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 90 minute budget before ARGT was asked

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 70.00 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 77.23 (-9.4%), 50d 84.70 (-17.4%), 200d 90.50 (-22.7%); 50d below 200d
Momentum: RSI(14) 23.2 | MACD -4.221 vs signal -3.830 (histogram -0.391)
Returns: 1d -1.1% | 5d -5.2% | 1m -19.7% | 3m -24.2%
52-week range: 70.00 - 102.94 (now 0.0% of the way up)
Volatility: ATR(14) 2.03 (2.9% of price) | annualised 20d 33.7%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.90 | P/B 1.59 | P/S 1.22 | 3y earnings growth n/a
Yield: 1.3%
Three-year record: +20.8% a year | beta to the market 0.44
Cost and size: expense ratio 0.59% | net assets 620.12M
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: MercadoLibre Inc 22.2%, YPF SA ADR 10.6%, Vista Energy SAB de CV ADR 8.2%, Grupo Financiero Galicia SA ADR 5.4%, Pampa Energia SA ADR 4.8%
Sector mix: Consumer cyclical 28.3%, Energy 22.6%, Financial services 13.7%, Basic materials 10.3%
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.61 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +69.0% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, PAM
Recent rating changes among them:
  - MELI: 2026-11-11 UBS: main, Neutral -> Neutral
  - YPF: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-10-13 UBS: main, Neutral -> Neutral
  - PAM: 2026-11-02 JP Morgan: main, Neutral -> Neutral
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
Share count change: 1 week: +6.3% (36.40M) over 7d | 1 month: +6.3% (36.26M) over 32d
Shares outstanding: 8.77M | fund size: 613.72M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 43.00 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 43.62 (-1.4%), 50d 44.10 (-2.5%), 200d 40.78 (+5.5%); 50d above 200d
Momentum: RSI(14) 44.0 | MACD -0.169 vs signal -0.147 (histogram -0.022)
Returns: 1d -0.4% | 5d -1.4% | 1m -2.7% | 3m -2.6%
52-week range: 32.56 - 45.76 (now 79.1% of the way up)
Volatility: ATR(14) 0.66 (1.5% of price) | annualised 20d 23.9%
Volume: 0.13x the 20-day average
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
Three-year record: +33.1% a year | beta to the market 0.85
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
Ratings by weight: buy 57.7% | hold 42.3% | sell 0.0% (mean 2.19 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +7.8% above the current prices
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
Share count change: 1 week: -0.2% (-2.34M) over 7d | 1 month: +23.9% (194.73M) over 32d
Shares outstanding: 23.48M | fund size: 1.01B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Top Tokenized ETFs by Market Cap](https://www.coingecko.com/en/etfs)  
  <sub>CoinGecko, 1 hour ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...
- [TSMC Is Sliding Before Nvidia Reports. Your Chip ETF Is Taking the Hit](https://247wallst.com/investing/etf/2026/11/17/tsmc-is-sliding-before-nvidia-reports-your-chip-etf-is-taking-the-hit/)  
  <sub>24/7 Wall St., 20 hours ago</sub>  
  Chip stocks are flinching hours before Nvidia reports, and TSMC's slide is rippling through funds many retirement savers own. Why does one earnings call put...
- [Quant ratings on Bridgewater Associates' top holdings: SPY, IVV, NVDA, AVGO](https://www.google.com/goto?url=CAESwwEBxCJF1xiT0yHD04-x7eUDsqqC9zH_BgIVnGHw_D-__-VAzID5WdgLbd1CjwmiQIwbKZe6e9ptUbeFSvn3H2Iis7rddAXaKnciH9AVnIgD3cZ3jjbjFosWM2bLzSL4fveC0VjRM7VxuKJRngziEPRR3603mALa3GND2s8tpu-_7F3DTm9z2y6h4Q7sjTRlqGClKXvct4GVgkPkrB_DaMen-3yrKb-rJZL7kdWpOKfn6r6sVLytPav9bNTnM8xJsPrjhLs&gsessionid=zeZ2bl07TR4BMSoAmyUPZj1xeYNuaKUUCGkJelolXVi8jiXv068AQg)  
  <sub>TradingView, 20 hours ago</sub>  
  Bridgewater Associates, the fund primarily focused on information technology stocks, with notable holdings in finance, consumer discretionary,...
- [Asian markets trade mixed as Nvidia earnings lift Kospi and Nikkei; Hong Kong slips on US chip curbs](https://www.google.com/goto?url=CAESxwEBxCJF1z8KCRl9olOs7NQ-YfwAIOoBk8Pxk-_-u7b8sRPKIiziRajkY-07huHCi3doIGU6F6z0JdK3oW3VUhOt8i5fg9XHzsSR-QaUqWAjzo8mLRRMiFQ56dIQGWUUH8ly5Dv9YVhim8-DclkgkqGj4035Rd0z5No0NKQHlH215nyjqqKQRj8dVAKpoCIM7whk3wsxEuH731fAkcO0QKmW6ojwbQwRwRy_t3DJ4nP1KwFfnj2bo9UMuORYseC3aEQO3147PWkE&gsessionid=zeZ2bl07TR4BMSoAmyUPZj1xeYNuaKUUCGkJelolXVi8jiXv068AQg)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  Asian stock markets traded mixed on Wednesday as upbeat earnings from Nvidia lifted sentiment across major tech hubs, though escalating US-China...
- [iShares MSCI South Korea ETF (EWY) Price Prediction: South Korea rebound lifts the tape, but EWY still trades below key trend gauges](https://www.google.com/goto?url=CAESmgEBxCJF1zOhlKsf_-DiU7kFCa0VRfCxxqvSx9gfw5hpvg7ydBEfxxCSyvppiBCw8TmqiMpm6mBSm2MePoJo4Zai7JNR8w4dq62Iam38t7M9kB-xuQwbdYuvFlPncdgP_CyB4dRae2rj3GuB83agy3VKD8OV6Qux0G0SJfbttH3tODv_q171d6sao1tusj6n63jx-y-2DlDs4Ogl&gsessionid=zeZ2bl07TR4BMSoAmyUPZj1xeYNuaKUUCGkJelolXVi8jiXv068AQg)  
  <sub>blockchain.news, 4 hours ago</sub>  
  iShares MSCI South Korea ETF (EWY) is trading at $139.07 after a 2.32% 24-hour gain, with volume of $194.7 million and a neutral funding rate on Binance...
- [Direxion South Korea Bull 3X ETF (KORU) Price Prediction: Leveraged South Korea exposure is trading below its short-term trend, but momentum is not yet broken](https://www.google.com/goto?url=CAESogEBxCJF12WZwnEi54AN3lYk5HHglsH2R6ScvCs3GAF0ybdcm9etTq8G-bLoUe7f1G3tWhy0iyOCVWvEaJkrOLu2tpILv6wdLiPazeDrxM2BHeuQM6SUnzGfoYbOY-XXa0RAxeoFhEpQ2_wxUC2TBaW8zJnRgYTEn3zZLjYVrvBM17S5A6ebj652CEP-_AidCbAxHrc3eTjIH8ZqPiZx8IHnzHE&gsessionid=zeZ2bl07TR4BMSoAmyUPZj1xeYNuaKUUCGkJelolXVi8jiXv068AQg)  
  <sub>Blockchain News, 4 hours ago</sub>  
  Direxion South Korea Bull 3X ETF (KORU) is trading at $7.02, up 7.01% on the day, after a sharp recent pullback from higher moving averages.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 137.45 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 147.26 (-6.7%), 50d 165.26 (-16.8%), 200d 164.23 (-16.3%); 50d above 200d
Momentum: RSI(14) 39.2 | MACD -7.655 vs signal -7.554 (histogram -0.101)
Returns: 1d +1.6% | 5d -7.0% | 1m -10.7% | 3m -22.9%
52-week range: 88.53 - 219.20 (now 37.4% of the way up)
Volatility: ATR(14) 6.82 (5.0% of price) | annualised 20d 71.8%
Volume: 0.14x the 20-day average
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 75.60M | fund size: 10.39B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [What Is Behind the Real's 19-Month Low and the Pressure on the iShares MSCI Brazil ETF (NYSEARCA:EWZ)?](https://kalkine.ca/news/economic-news/what-is-behind-the-reals-19-month-low-and-the-pressure-on-the-ishares-msci-brazil-etf-nysearcaewz)  
  <sub>kalkine.ca, 21 hours ago</sub>  
  What Is Behind the Real's 19-Month Low and the Pressure on the iShares MSCI Brazil ETF (NYSEARCA:EWZ)?
- [US Options](https://www.moomoo.com/quote/options-us/total-volume/stock?chain_id=Name1K9-3FXPhg.1lfkhs0&global_content=%7B%22promote_id%22%3A13764,%22sub_promote_id%22%3A9,%22f%22%3A%22www.moomoo.com%2Fsectors%2FNASDAQ%22%7D)  
  <sub>Moomoo, 14 hours ago</sub>  
  Stock Market · Options Market · Futures Market · ETF Market · Forex Market. Technical Tools. Stock Screener · Heat Map · Earnings Calendar...
- [Top Tokenized ETFs by Market Cap](https://www.google.com/goto?url=CAESXgHEIkXXaHkNFGBsg6eaR0UPVgEfJcFVbTPTex3_jtTEeNBJwdyWRDI5IJmqJYXkAXhaW3zN5-aL8LhacXBEIGb3o0xyOeK4AlXKqiHEy5fOexlBBjD5v7Dhxm8r2YA&gsessionid=D-pF1kryatK-t5GWHlsoAr3jf7VYFlhARWmNwM0qzX-xALuRkfeU6g)  
  <sub>CoinGecko, 14 hours ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 30.83 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 33.30 (-7.4%), 50d 37.16 (-17.0%), 200d 36.91 (-16.5%); 50d above 200d
Momentum: RSI(14) 30.1 | MACD -1.978 vs signal -1.908 (histogram -0.069)
Returns: 1d -0.6% | 5d -4.9% | 1m -28.2% | 3m -9.7%
52-week range: 30.83 - 43.54 (now 0.0% of the way up)
Volatility: ATR(14) 1.01 (3.3% of price) | annualised 20d 73.1%
Volume: 0.05x the 20-day average
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
Three-year record: +3.0% a year | beta to the market 0.92
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
Weighted price target: +38.8% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 200.55M | fund size: 6.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 90 minute budget before EZA was asked

<details><summary><b>News</b> — score n/a</summary>

- [iShares Enhanced Emerging Markets Active ETF (ENHE) options chain](https://sg.finance.yahoo.com/quote/ENHE/options/)  
  <sub>22 hours ago</sub>  
  Contract name, Last trade date (GMT-5), Strike, Last price, Bid, Ask, Change, % change, Volume, Open interest, Implied volatility...
- [Arirang 200 ETF (152100.KS) Seasonal returns chart](https://uk.finance.yahoo.com/quote/152100.KS/seasonality/)  
  <sub>24 hours ago</sub>  
  Arirang 200 ETF (152100.KS) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [iShares S&P U.S. Small-Cap Index ETF (CAD-Hedged) (XSMH.TO) Seasonal returns chart](https://www.google.com/goto?url=CAESdAHEIkXX5h95vBoa7jS3tW3GbjofdA0wNWRa7_cFS2gAkb0L-6xmpnQjs70oYRs-MtC1iFiJ4c34w4ddkN-w9A6G1ngz6DCB4R7VIrUVYPt_o57DQG2neYHN8rDTKZM7xquRw1RuXK7gzy6buvLxC8a_yIAw&gsessionid=D1ghcZz4QQDgEMA-xC5Mxz75kO8W4tZWchWVnQbLrFOrgHGtmI8XVw)  
  <sub>21 hours ago</sub>  
  iShares S&P U.S. Small-Cap Index ETF (CAD-Hedged) (XSMH.TO) seasonal returns chart provides the mean and median returns by month to inform your investment...
- [iShares J.P. Morgan EM Local Govt Bond UCITS ETF (IEMLZ.XC) Seasonal returns chart](https://www.google.com/goto?url=CAESdQHEIkXXaJX8b_xKgFhbzeS0YqfJT8-eMe7-Fp1UjBs13cgdMEXeuLyBFdDLKGzbWZ15fMH_V2vTi5ytYEOpMKI4hFNXbwGLJCebAAYQyg3JGj__zcOeYAgY6TFvclnao_f3o4Y6M4UmM6FPwgNbrwNDKwz_sA&gsessionid=D1ghcZz4QQDgEMA-xC5Mxz75kO8W4tZWchWVnQbLrFOrgHGtmI8XVw)  
  <sub>20 hours ago</sub>  
  iShares J.P. Morgan EM Local Govt Bond UCITS ETF (IEMLZ.XC) seasonal returns chart provides the mean and median returns by month to inform your investment...
- [iShares-ESTXX Mid UCITS ETF R (IQQM.DU) Seasonal returns chart](https://www.google.com/goto?url=CAESdAHEIkXXWRztPfQDLRT9cIHjnGS9WyBMhkzFr9a-gXcFy9Cm-8UGfoQCqe4okR53wya82emSL0G7KPhIkdc1U6CTx86o9BH17o1Pa-w4fvOmZdaUUwOmg4tv7MAIZkMfGT9ZU70NGrqqrjW8IIj7-8N0jfuH&gsessionid=D1ghcZz4QQDgEMA-xC5Mxz75kO8W4tZWchWVnQbLrFOrgHGtmI8XVw)  
  <sub>22 hours ago</sub>  
  iShares-ESTXX Mid UCITS ETF R (IQQM.DU) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [BNP Paribas Easy MSCI Europe Small Caps SRI PAB UCITS ETF Capitalisation (EESM.MI) Seasonal returns chart](https://www.google.com/goto?url=CAESdAHEIkXXSqwRdt08bH_-TOrQgZ3eOudm9a7Yd_i4TffD2CwvdeLEW7i_hEUKl_O6MkAPNrCuUXrAi6b3gx4f-DnTnSjk1kfgQWJidtaWGHYLWnduLV-AD28dT2k95LWNmHRxgGzs416amODuQQz-YdqGczQh&gsessionid=D1ghcZz4QQDgEMA-xC5Mxz75kO8W4tZWchWVnQbLrFOrgHGtmI8XVw)  
  <sub>20 hours ago</sub>  
  BNP Paribas Easy MSCI Europe Small Caps SRI PAB UCITS ETF Capitalisation (EESM.MI) seasonal returns chart provides the mean and median returns by month to...
- [Renaissance International IPO ETF (IPOS) Seasonal returns chart](https://www.google.com/goto?url=CAEScQHEIkXXVIr0ZMVE1TDu5zokkEckrZ-dV3l40hnUYSoUgi4iPKIol9BuS275eqGrgjsC3dSUkDCbsdalxwzjeJEEQ1JllBv0BHNmS9P1qvEEKCraGdpyDjr4wVe_Hx8LnFNF5EZElZgkN-lWgXrDBfz4&gsessionid=D1ghcZz4QQDgEMA-xC5Mxz75kO8W4tZWchWVnQbLrFOrgHGtmI8XVw)  
  <sub>24 hours ago</sub>  
  Renaissance International IPO ETF (IPOS) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [Amundi Index Solutions - Amundi Prime Global Government Bond UCITS ETF Dist (PR1G.DE) Seasonal returns chart](https://www.google.com/goto?url=CAESdAHEIkXXaZL4s6Z5DEcU34XedGFm60TL62xbncKQmdMOBr8GKfppca3AT_J05nF3KtPNdBsGBZnjHlBh8WteSFP2fVri-LjhU4IcRf-RDUR51fIbUXyQXpjOfnCMj2TKDpFjMQYmFVxobCX03P71jUZr_3Ui&gsessionid=D1ghcZz4QQDgEMA-xC5Mxz75kO8W4tZWchWVnQbLrFOrgHGtmI8XVw)  
  <sub>22 hours ago</sub>  
  Amundi Index Solutions - Amundi Prime Global Government Bond UCITS ETF Dist (PR1G.DE). 16.59 +0.01 (+0.03%). At close: 17:23:10 CET...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 59.86 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 64.49 (-7.2%), 50d 65.20 (-8.2%), 200d 67.86 (-11.8%); 50d below 200d
Momentum: RSI(14) 33.7 | MACD -0.496 vs signal -0.039 (histogram -0.457)
Returns: 1d -5.0% | 5d -10.5% | 1m -8.5% | 3m -15.1%
52-week range: 59.86 - 81.60 (now 0.0% of the way up)
Volatility: ATR(14) 1.61 (2.7% of price) | annualised 20d 35.5%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.65 | P/B 1.96 | P/S 1.68 | 3y earnings growth n/a
Yield: 8.2%
Three-year record: +22.7% a year | beta to the market 1.12
Cost and size: expense ratio 0.59% | net assets 438.81M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Anglogold Ashanti PLC 11.3%, Naspers Ltd Class N 8.4%, Gold Fields Ltd 8.2%, Firstrand Ltd 7.5%, Standard Bank Group Ltd 6.4%
Sector mix: Financial services 36.0%, Basic materials 35.9%, Consumer cyclical 13.0%, Communication services 7.2%
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
Rolled up from the 5 largest holdings, 41.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.99 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +39.4% above the current prices
Holdings read: AU, NPN.JO, GFI.JO, FSR.JO, SBK.JO
Recent rating changes among them:
  - AU: 2026-10-30 JP Morgan: main, Overweight -> Overweight
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 7.90M | fund size: 472.89M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: the streamed answer ran past the 480s ceiling (gave up after 2 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [iShares Expanded Tech-Software ETF (Derivatives) price today, IGV to USD live price, marketcap and chart](https://coinmarketcap.com/currencies/ishares-expanded-tech-software-etf-derivatives/)  
  <sub>CoinMarketCap, 5 hours ago</sub>  
  The live iShares Expanded Tech-Software ETF (Derivatives) price today is $97.06 USD with a 24-hour trading volume of $0 USD. We update our IGV to USD price...
- [Binance Lists 6 Perpetual Futures on Stocks and ETFs, Offering Up to 20x Leverage](https://finance.biggo.com/news/f0152ad5-f077-4524-9c7a-080fa6eb38e0)  
  <sub>BigGo Finance, 8 hours ago</sub>  
  Binance is listing perpetual futures contracts based on six stocks and ETFs—SOXX, IGV, ARTY, IBIT, CCJ, and ETN—rolling them out at five-minute…

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 96.12 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 103.51 (-7.1%), 50d 105.75 (-9.1%), 200d 94.30 (+1.9%); 50d above 200d
Momentum: RSI(14) 33.8 | MACD -2.582 vs signal -1.854 (histogram -0.728)
Returns: 1d +0.4% | 5d -6.0% | 1m -10.1% | 3m -5.7%
52-week range: 74.67 - 112.67 (now 56.4% of the way up)
Volatility: ATR(14) 2.90 (3.0% of price) | annualised 20d 31.4%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Technology
What it holds: P/E 30.79 | P/B 7.22 | P/S 8.03 | 3y earnings growth n/a
Yield: 0.0%
Three-year record: +9.9% a year | beta to the market 1.25
Cost and size: expense ratio 0.38% | net assets 13.46B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Palo Alto Networks Inc 9.1%, Palantir Technologies Inc Ordinary Shares - Class A 9.0%, Microsoft Corp 8.8%, CrowdStrike Holdings Inc Class A 8.6%, Oracle Corp 6.7%
Sector mix: Technology 94.4%, Communication services 3.6%, Financial services 1.7%, Consumer cyclical 0.2%
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
Rolled up from the 5 largest holdings, 42.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.60 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +39.1% above the current prices
Holdings read: PANW, PLTR, MSFT, CRWD, ORCL
Recent rating changes among them:
  - PANW: 2026-11-12 Jefferies: main, Buy -> Buy
  - PLTR: 2026-11-04 Barclays: main, Overweight -> Overweight
  - MSFT: 2026-10-29 Bernstein: main, Outperform -> Outperform
  - CRWD: 2026-11-09 Bernstein: main, Market Perform -> Market Perform
  - ORCL: 2026-11-02 Stephens & Co.: up, Equal-Weight -> Overweight
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 12.50M | fund size: 1.20B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: the streamed answer ran past the 480s ceiling (gave up after 2 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Principal CLO ETF (UUPP) latest stock news and headlines](https://sg.finance.yahoo.com/quote/UUPP/news/)  
  <sub>Yahoo Finance Singapore, 21 hours ago</sub>  
  Get the latest Principal CLO ETF (UUPP) stock news and headlines to help you in your trading and investment decisions.
- [Xtr.(IE)-MSCI World FinancialsR (XDWF.DU) latest stock news and headlines](https://sg.finance.yahoo.com/quote/XDWF.DU/news/)  
  <sub>Yahoo Finance Singapore, 20 hours ago</sub>  
  Xtr.(IE)-MSCI World FinancialsR (XDWF.DU). 42.84 -0.65 (-1.48%). As of 6:46:03 pm GMT+1. Market open. Related ETF news.
- [UBS Factor MSCI USA Quality Screened UCITS ETF USD dis (UQLTD.MI) Latest Stock News & Headlines](https://www.google.com/goto?url=CAESbgHEIkXXsagN-wVSl2B0zXpysytHZL4daiRcH9DbTfEa1ZJYq2x3oL0g8AZpr7_j9vZmWWudjzrIZM-noSCQoUTca5T9UzdyaQ8OO02r3v6owpW2qo8yPy-_lQXc9H61ZuE1fG-Vyof7Bf1StNXl&gsessionid=cOsNbhT-HNvmxna9NP6wSk9I4tU6FpiIEth0MZRPlSOfCy2rVPM6BQ)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  Get the latest UBS Factor MSCI USA Quality Screened UCITS ETF USD dis (UQLTD.MI) stock news and headlines to help you in your trading and investing...
- [Xtrackers II Singapore Government Bond UCITS ETF 1C (LU0378818560-SGD.LU) latest stock news and headlines](https://www.google.com/goto?url=CAESeQHEIkXXTPZfQbYtoYNnEfBaCvQt-zOIjMK49M6FxjTGAQesrD0zuyIKKyt-guD23Lc6LP0m7D2r_KCjJ7loLR7hWpNm7_zIsN7UfDCQ14t_6I3dZRk8ax0tQzDqJ2ZjlvzUpM-0ApDPFZLW7rsoKHzWyTFOMtKT5DI&gsessionid=cOsNbhT-HNvmxna9NP6wSk9I4tU6FpiIEth0MZRPlSOfCy2rVPM6BQ)  
  <sub>Yahoo Finance Singapore, 19 hours ago</sub>  
  Xtrackers II Singapore Government Bond UCITS ETF 1C (LU0378818560-SGD.LU). 164.58 -0.16 (-0.10%). At close: 12:25:10 pm GMT+1...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 51.56 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 49.50 (+4.2%), 50d 48.19 (+7.0%), 200d 49.09 (+5.0%); 50d below 200d
Momentum: RSI(14) 71.1 | MACD 1.157 vs signal 0.951 (histogram 0.206)
Returns: 1d -0.7% | 5d -0.1% | 1m +7.9% | 3m +4.1%
52-week range: 45.42 - 54.83 (now 65.2% of the way up)
Volatility: ATR(14) 0.52 (1.0% of price) | annualised 20d 15.3%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: India Equity
What it holds: P/E 21.32 | P/B 2.99 | P/S 2.59 | 3y earnings growth n/a
Yield: n/a
Three-year record: +4.9% a year | beta to the market 0.61
Cost and size: expense ratio 0.61% | net assets 5.84B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: HDFC Bank Ltd 6.3%, ICICI Bank Ltd 5.9%, Reliance Industries Ltd 5.3%, Bharti Airtel Ltd 4.4%, Infosys Ltd 2.9%
Sector mix: Financial services 29.6%, Consumer cyclical 12.2%, Industrials 9.9%, Technology 8.7%
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
Rolled up from the 5 largest holdings, 24.8% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.37 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.2% above the current prices
Holdings read: HDFCBANK.NS, ICICIBANK.NS, RELIANCE.NS, BHARTIARTL.NS, INFY.NS
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
Direction: money going out (1 month)
Share count change: 1 week: -0.0% (-1.54M) over 7d | 1 month: -8.3% (-532.07M) over 32d
Shares outstanding: 113.76M | fund size: 5.87B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [What Bank Capital Rules Could Mean For Funds With Bank Exposure](https://simplywall.st/etfs/us/nasdaq-kbwb/news/what-bank-capital-rules-could-mean-for-funds-with-bank-expos)  
  <sub>Simply Wall St, 2 hours ago</sub>  
  How different are three bank themed funds when the rules that shape their balance sheets are about to change? That is the question investors are really...
- [iShares U.S. Home Construction ETF (ITB) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/ITB/)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Find the latest iShares U.S. Home Construction ETF (ITB) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 70.76 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 72.55 (-2.5%), 50d 71.54 (-1.1%), 200d 71.24 (-0.7%); 50d above 200d
Momentum: RSI(14) 42.7 | MACD 0.061 vs signal 0.305 (histogram -0.244)
Returns: 1d -0.1% | 5d -3.0% | 1m +0.2% | 3m -5.3%
52-week range: 59.16 - 77.93 (now 61.8% of the way up)
Volatility: ATR(14) 1.35 (1.9% of price) | annualised 20d 21.0%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Financial
What it holds: P/E 12.17 | P/B 1.26 | P/S 3.63 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +20.7% a year | beta to the market 0.97
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
Ratings by weight: buy 66.6% | hold 33.4% | sell 0.0% (mean 2.22 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.9% above the current prices
Holdings read: GBCI, UCB, TXCP, OZK, EBC
Recent rating changes among them:
  - GBCI: 2026-10-26 Piper Sandler: main, Overweight -> Overweight
  - UCB: 2026-10-21 Stephens & Co.: main, Overweight -> Overweight
  - TXCP: 2026-11-03 Barclays: main, Equal-Weight -> Equal-Weight
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
Share count change: 1 week: +1.6% (62.64M) over 7d | 1 month: +2.1% (80.93M) over 32d
Shares outstanding: 55.48M | fund size: 3.93B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: the streamed answer ran past the 480s ceiling (gave up after 2 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 48.12 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 49.80 (-3.4%), 50d 51.27 (-6.1%), 200d 54.92 (-12.4%); 50d below 200d
Momentum: RSI(14) 31.6 | MACD -0.613 vs signal -0.453 (histogram -0.159)
Returns: 1d -0.6% | 5d -5.1% | 1m -5.6% | 3m -13.3%
52-week range: 48.12 - 64.26 (now 0.0% of the way up)
Volatility: ATR(14) 0.68 (1.4% of price) | annualised 20d 21.1%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Greater China Region
What it holds: P/E 11.09 | P/B 1.27 | P/S 1.27 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +7.0% a year | beta to the market 0.47
Cost and size: expense ratio 0.59% | net assets 5.49B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Tencent Holdings Ltd 13.2%, Alibaba Group Holding Ltd Ordinary Shares 9.1%, China Construction Bank Corp Class H 4.8%, Industrial And Commercial Bank Of China Ltd Class H 2.9%, Xiaomi Corp Class B 2.5%
Sector mix: Consumer cyclical 23.1%, Financial services 22.5%, Communication services 17.5%, Technology 9.9%
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
Rolled up from the 5 largest holdings, 32.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.42 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +79.6% above the current prices
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
Direction: money going out (1 month)
Share count change: 1 week: +5.4% (275.60M) over 7d | 1 month: -3.6% (-202.61M) over 32d
Shares outstanding: 111.98M | fund size: 5.39B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 90 minute budget before TUR was asked

<details><summary><b>News</b> — score n/a</summary>

- [Lider Faktoring Reports Coupon Payment on TRY 150 Million Notes](https://www.tipranks.com/news/company-announcements/lider-faktoring-reports-coupon-payment-on-try-150-million-notes)  
  <sub>8 hours ago</sub>  
  Lider Faktoring Anonim Sirketi ( ($TR:LIDFA) ) just unveiled an announcement. The disclosure identifies Lider Faktoring A.Ş. as the issuer of a...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 31.13 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 31.15 (-0.1%), 50d 33.74 (-7.7%), 200d 38.46 (-19.1%); 50d below 200d
Momentum: RSI(14) 41.9 | MACD -0.481 vs signal -0.738 (histogram 0.257)
Returns: 1d -1.6% | 5d -2.4% | 1m -4.5% | 3m -22.8%
52-week range: 29.53 - 43.74 (now 11.3% of the way up)
Volatility: ATR(14) 0.62 (2.0% of price) | annualised 20d 33.8%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 11.63 | P/B 1.01 | P/S 0.62 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: -0.4% a year | beta to the market 0.60
Cost and size: expense ratio 0.59% | net assets 146.42M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Aselsan Elektronik Sanayi Ve Ticaret AS 13.3%, Tupras-Turkiye Petrol Rafineleri AS 10.9%, Bim Birlesik Magazalar AS 9.8%, Akbank TAS 6.2%, Turk Hava Yollari AO 4.6%
Sector mix: Industrials 30.8%, Financial services 16.9%, Consumer defensive 12.9%, Energy 10.9%
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
Rolled up from the 5 largest holdings, 44.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.63 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.3% above the current prices
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 15.65M | fund size: 487.18M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Is SPDR S&P Homebuilders ETF (NYSEARCA:XHB) Exposed as Builder Sentiment Hits a 14-Year Low?](https://kalkine.ca/news/real-estate/is-spdr-sp-homebuilders-etf-nysearcaxhb-exposed-as-builder-sentiment-hits-a-14-year-low)  
  <sub>kalkine.ca, 5 hours ago</sub>  
  Is SPDR S&P Homebuilders ETF (NYSEARCA:XHB) Exposed as Builder Sentiment Hits a 14-Year Low?
- [Why Could a 14-Year Low in Builder Confidence Put SPDR S&P Homebuilders ETF (NYSEARCA:XHB) at Risk?](https://kalkine.com.au/news/real-estate/why-could-a-14-year-low-in-builder-confidence-put-spdr-sp-homebuilders-etf-nysearcaxhb-at-risk)  
  <sub>Kalkine, 5 hours ago</sub>  
  Why Could a 14-Year Low in Builder Confidence Put SPDR S&P Homebuilders ETF (NYSEARCA:XHB) at Risk?
- [Homebuilder Confidence Just Fell to Its Lowest Since 2012](https://www.google.com/goto?url=CAESoQEBxCJF12RjgoJrJx59NHHj6RgPhReC4F_0iIByznSMAmSxcVm7mY6Mzeyy9uBCEgeHBjdR4MivJKm1cvF1CI6D3SRzxodMKTQfgIrtPNBSpevGaunL348ktJv9qKG6yLQqsxST7VLzBzzSCdfRYU-AUSe_8N9_En4XLzDF-eCNq0ZS_DYEJKXZ8Zq955CgeH74F8Bpjuigm2hjNtudKwE_hA&gsessionid=U_dRIhc0Ut-t5vItk3vAIEvv2Z7-wCzgDOWAnNH6QS2zAobOzXyLBQ)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Nearly half of America's home builders are now cutting prices. That is the clearest finding in the November NAHB/Wells Fargo Housing Market Index,...
- [Futures Mixed; Nvidia Tops, Fed's Waller Warns Of 'Shock' Rate Hike](https://www.google.com/goto?url=CAESrQEBxCJF19VFtvyDzNJRP8aMPfUB90gnzUY3UbKCf3-K9pt5XNvDKta30mSD_O3isAbxfNFDtCo6oXJbdjB-vOY4o4ySDLNrHxZ1SjH5hoHkhtteUv6HI4LbdHlcPWYGZ2Hz-nM5tHYZEBiSvNm1XZmBM63eL60WAuecF7zbIV74equ70V4UQU9Jx25SHMCIctl90NFBsrgLx2asXY3ac02DF-MmdkwF_J8qiQiHwg&gsessionid=U_dRIhc0Ut-t5vItk3vAIEvv2Z7-wCzgDOWAnNH6QS2zAobOzXyLBQ)  
  <sub>Investor's Business Daily, 2 hours ago</sub>  
  Dow Jones futures: Nvidia and Target earnings topped views. Fed Gov. Waller said inflation is "spreading out." The Anthropic IPO looms.
- [(XHB) Market Dynamics and Trading Signals (XHB:CA)](https://www.google.com/goto?url=CAESnQEBxCJF1992WzfELaw6Ro2P4Yx7hwAJp8YRqjaBHpb7SC_VIdi_ze5PMKi-fl03OhLdrDz5JPQ6mSL5u_zirpNlqiHgjOGHf6gOp66vEOLaAzZ2QJCsn8KCqvspPfArBmIvZtTPG08WnhUjSjopjTGKc5uWb9vSMt5fykKFcY7zA7m4X-rcsf7paQXUroz4LaholNxTJg0nY7glsa6u&gsessionid=U_dRIhc0Ut-t5vItk3vAIEvv2Z7-wCzgDOWAnNH6QS2zAobOzXyLBQ)  
  <sub>Stock Traders Daily, 15 hours ago</sub>  
  Market Dynamics Report for iShares Canadian HYBrid Corporate Bond Index ETF (XHB) Featuring Key Trading Signals.
- [BlackRock® Canada Announces November Cash Distributions for the iShares® ETFs](https://www.google.com/goto?url=CAES1gEBxCJF1-p4l4l6ojFp8a1MNGmY6GBxg4PGBD8yn_2xfmXXn7V9sA5FWRIZI6Dk85jRD4-xbya8w3UsxnJZQKwA5CNdBwXD2ABr6uW0zjOMd9a6-O-hZNN1BBbMnMIKEbP2NJEFcjvO5tF2efj3alDZEanBxQI6JadAKG1Gp1lpAdC3kej1eKgRD9Yla9QZbrGG0U0_1VwA5oHkMyDv_-lpT4r2pQnmQDKcFmoSAi7dxsq9e_WiG-E95S4IHsmSOA61novV7wZo7xya8FygpELt-IBYURFw&gsessionid=U_dRIhc0Ut-t5vItk3vAIEvv2Z7-wCzgDOWAnNH6QS2zAobOzXyLBQ)  
  <sub>The Manila Times, 5 hours ago</sub>  
  TORONTO, Nov. 18, 2026 (GLOBE NEWSWIRE) -- BlackRock Asset Management Canada Limited ('BlackRock Canada”), an indirect, wholly-owned subsidiary of BlackRock...
- [PulteGroup Stock Outlook: Is Wall Street Bullish or Bearish?](https://www.google.com/goto?url=CAESoQEBxCJF12dYAie1UEeMS1nrfTqCM0klEHlJCm5fAP6Y5ECFXYtMD003wmjmSDZCqnEul3D1O69Ua3xM3hcV1V5R4VQtt_Uo0gQPEayTHqJdZAd9PJoL_vQcigf6NEkP7caexoWKV0tkiZu5KeaQjd5OG8Uk_3e5qeaNZku8qiLaKaY1nV03xZzfOYqMXRXp_qAkKXhuLX4_EKcmOg5vDMQItA&gsessionid=U_dRIhc0Ut-t5vItk3vAIEvv2Z7-wCzgDOWAnNH6QS2zAobOzXyLBQ)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  Atlanta, Georgia-based PulteGroup, Inc. (PHM) engages in the homebuilding business. Valued at $23.4 billion by market cap, the company sells and constructs...
- [iShares U.S. Home Construction ETF (ITB) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESYwHEIkXXFALhmuODpYdCRa4xSEBVESB-OIH8cl6MFivkEYE1biGFfvMKFXiWJhPqkENgEu4r6j7naZwC-TlRBVRTmt1Pp1clb-ZF2BprKci9QztYLQW0W9KejUT3U9XQUh3MGQ&gsessionid=U_dRIhc0Ut-t5vItk3vAIEvv2Z7-wCzgDOWAnNH6QS2zAobOzXyLBQ)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Find the latest iShares U.S. Home Construction ETF (ITB) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 99.63 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 101.52 (-1.9%), 50d 98.43 (+1.2%), 200d 104.55 (-4.7%); 50d below 200d
Momentum: RSI(14) 47.9 | MACD 0.688 vs signal 1.170 (histogram -0.482)
Returns: 1d +0.5% | 5d -3.4% | 1m +3.5% | 3m -5.7%
52-week range: 92.84 - 121.36 (now 23.8% of the way up)
Volatility: ATR(14) 2.75 (2.8% of price) | annualised 20d 39.7%
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
Three-year record: +8.3% a year | beta to the market 1.40
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
Weighted price target: +11.2% above the current prices
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
Share count change: 1 week: +4.9% (75.23M) over 7d | 1 month: +4.8% (74.09M) over 32d
Shares outstanding: 16.15M | fund size: 1.61B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [State Street Communication Services Select Sector SPDR ETF (XLC) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLC/)  
  <sub>4 hours ago</sub>  
  State Street Communication Services Select Sector SPDR ETF (XLC) · -2.32% · -4.59% · -9.32% · -11.02% · -5.45% · 30.19% · 111.79%.
- [Disney's Better-Than-Expected Q4 Results Put These ETFs in Focus](https://www.zacks.com/stock/news/3031786/disneys-better-than-expected-q4-results-put-these-etfs-in-focus)  
  <sub>36 minutes ago</sub>  
  Disney beats Q4 earnings estimates, driven by strong growth across its key business segments. Explore ETFs with significant exposure to DIS.
- [10 communication services stocks that surpassed Wall Street's Q3 earnings expectations (XLC:NYSEARCA)](https://www.google.com/goto?url=CAESuAEBxCJF1wh_CYny7UsuY1142rEttOhOcTAShiZ8_OsZ4Grc-mQf4GJUy-6jjlQvBOwn13kR7GboI8OfOFXv1hQPnf04rJsIN-R9157-Ed3zm9uv_LYFQ4_h4XMf4CSQr0o1SxiYjdlG2oDqgcffC2wH8b7IHS7QYJz-2aFh6Vy5HmvLkfRRx2NgQ7KouPdAbJij9nTGPe6Ah60wp2MtyaEso_OSApU_hJib6reYziK91XWUS11abYe9&gsessionid=pq07PNtZ7CJxXUDedwiMrle2_qdk-ADNNsWyOrVed1fFWsBcji9Qhg)  
  <sub>1 hour ago</sub>  
  Charter Communications tops communication services with a $11.94 EPS surprise; Liberty Live Holdings and TKO Group Holdings follow at $2.54 and $1.70.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 105.90 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 104.92 (+0.9%), 50d 109.06 (-2.9%), 200d 112.17 (-5.6%); 50d below 200d
Momentum: RSI(14) 47.1 | MACD -0.503 vs signal -0.935 (histogram 0.432)
Returns: 1d +0.6% | 5d -2.5% | 1m -3.9% | 3m -4.3%
52-week range: 99.90 - 120.08 (now 29.7% of the way up)
Volatility: ATR(14) 1.96 (1.8% of price) | annualised 20d 23.3%
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
Three-year record: +16.4% a year | beta to the market 0.93
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
Ratings by weight: buy 90.6% | hold 9.4% | sell 0.0% (mean 1.52 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +32.9% above the current prices
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
Share count change: 1 week: +0.5% (105.78M) over 7d | 1 month: -1.2% (-267.97M) over 32d
Shares outstanding: 200.82M | fund size: 21.27B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [3 ETFs That Hold Johnson & Johnson In Very Different Ways](https://simplywall.st/etfs/us/nysearca-xlv/news/3-etfs-that-hold-johnson-johnson-in-very-different-ways)  
  <sub>3 hours ago</sub>  
  If you like Johnson & Johnson for its mix of medicine and medical devices, owning the stock directly means living with its specific bumps.
- [Your "Safe" Health Care ETF Just Got Hit by UnitedHealth Again](https://247wallst.com/investing/etf/2026/11/17/your-safe-health-care-etf-just-got-hit-by-unitedhealth-again/)  
  <sub>22 hours ago</sub>  
  Shares of UnitedHealth Group (NYSE:UNH | UNH Price Prediction) fell 3.54% to $397.44 as of 11:10 AM ET Tuesday, after trading as low as $389.04 earlier in...
- [3 ‘Safe’ Stocks Investors Are Rotating Into Amid the Tech Downturn](https://www.google.com/goto?url=CAESqQEBxCJF17QvdOdOQL9jkNppsY4G5KaKBWfwFx4AyVqowPHsPg-hPX57yOfAWgy22iXz3fQwg-TbYRcPP-bCCykUkJG0rBORqfSgAuQAYPiqy1Y06pXjQB7pWw7e6StsK5L6GKkZIuMvoQtFCv29H9HapqXvEfe717GpivrB7UBc4hGQD1tQGAI62q9CVuGVzNSleA_xGUvET4bTudDO62R2BTtDkjDuohiX&gsessionid=KvUj8criO85ljOVdo_4TbMKQ2fCRhSsisPAILtH1ilhYpOeKX42yFw)  
  <sub>6 hours ago</sub>  
  Market Analysis by Jesse Cohen covering: Nasdaq 100, S&P 500, Dow Jones Industrial Average, State Street® SPDR® Dow Jones Industrial Average® ETF Trust.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 183.85 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 184.77 (-0.5%), 50d 176.08 (+4.4%), 200d 160.67 (+14.4%); 50d above 200d
Momentum: RSI(14) 53.0 | MACD 3.069 vs signal 3.685 (histogram -0.617)
Returns: 1d -0.8% | 5d -2.7% | 1m +2.2% | 3m +6.6%
52-week range: 142.84 - 189.66 (now 87.6% of the way up)
Volatility: ATR(14) 3.26 (1.8% of price) | annualised 20d 20.5%
Volume: 0.20x the 20-day average
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
Three-year record: +15.4% a year | beta to the market 0.41
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
Weighted price target: +8.2% above the current prices
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 197.42M | fund size: 36.29B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Sugar (CANE) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 90 minute budget before CANE was asked

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 10.92 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 11.30 (-3.4%), 50d 11.57 (-5.6%), 200d 10.32 (+5.8%); 50d above 200d
Momentum: RSI(14) 37.1 | MACD -0.219 vs signal -0.183 (histogram -0.037)
Returns: 1d -0.2% | 5d -2.1% | 1m -10.9% | 3m -2.4%
52-week range: 9.02 - 12.47 (now 55.1% of the way up)
Volatility: ATR(14) 0.19 (1.7% of price) | annualised 20d 27.6%
Volume: 0.06x the 20-day average
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
Cost of holding this fund instead of sugar itself: -7.3% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -2.4%, commodity +3.2%, gap -5.6% | 6 months: fund +9.4%, commodity +22.7%, gap -13.3% | 12 months: fund +14.8%, commodity +22.2%, gap -7.3%
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
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-11-10, published the following Friday)
Large speculators: net long 17.1% of open interest (1,145,979 contracts)
Change on the week: -1.7% of open interest
Crowding: 83% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.4% (222.60K) over 7d | 1 month: +24.6% (11.58M) over 32d
Shares outstanding: 5.37M | fund size: 58.69M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected) (Bing's feed, direct: 3 headline(s), none naming CANE)

### Corn (CORN) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 90 minute budget before CORN was asked

<details><summary><b>News</b> — score n/a</summary>

- [Corn Slipping to Start Midweek Trade](https://www.barchart.com/story/news/8896006/corn-slipping-to-start-midweek-trade)  
  <sub>Barchart.com, 1 hour ago</sub>  
  Corn prices are showing Wednesday morning losses of 1 to 2 1/2 cents. Futures closed the Tuesday session fading of early highs, as December was down 2 cents...
- [Corn Fades Lower into Tuesday’s Close](https://www.barchart.com/story/news/8885556/corn-fades-lower-into-tuesdays-close)  
  <sub>Barchart.com, 17 hours ago</sub>  
  Corn futures closed the Tuesday session fading of early highs, as December was down 2 cents and other contracts fractionally to 2 cents higher.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 17.20 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 17.34 (-0.8%), 50d 18.44 (-6.7%), 200d 18.18 (-5.3%); 50d above 200d
Momentum: RSI(14) 35.6 | MACD -0.320 vs signal -0.378 (histogram 0.058)
Returns: 1d -0.3% | 5d -0.9% | 1m -3.7% | 3m -8.6%
52-week range: 16.47 - 20.29 (now 19.2% of the way up)
Volatility: ATR(14) 0.22 (1.3% of price) | annualised 20d 12.1%
Volume: 0.12x the 20-day average
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
Cost of holding this fund instead of corn itself: -6.5% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -8.6%, commodity -7.4%, gap -1.2% | 6 months: fund -6.6%, commodity -4.8%, gap -1.8% | 12 months: fund -4.5%, commodity +2.0%, gap -6.5%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

```text
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 1.1% of open interest (1,979,758 contracts)
Change on the week: -1.6% of open interest
Crowding: 33% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -0.7% (-772.39K) over 7d | 1 month: -12.0% (-14.53M) over 32d
Shares outstanding: 6.22M | fund size: 107.04M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 90 minute budget before CPER was asked

<details><summary><b>News</b> — score n/a</summary>

- [Copper extends slide to lowest level since April on firm dollar, AI doubts (CPER:NYSEARCA)](https://seekingalpha.com/news/4674129-copper-extends-slide-to-lowest-level-since-april-on-firm-dollar-ai-doubts?source=generic_rss)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Copper futures sank to their lowest since April as a stronger dollar, weaker sentiment around AI-related assets, and concerns over Chinese demand weighed on...
- [Red Hot Metal: China's Role In The Global Copper Supply Chain](https://seekingalpha.com/article/4969432-red-hot-metal-china-role-in-global-copper-supply-chain)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  Global copper demand is projected to surge 50% by 2040, driven by AI, renewable energy and electrification, while supply constraints and declining ore...
- [Commodities: Copper Hits 6-Month Low; Improving Supply Weighs On Oil](https://www.google.com/goto?url=CAESuAEBxCJF17v9xAGZU4sonswijBmMUqG4xkfTTf-3RhaSVTlXOZOW280CdXPwwI1IYQHhpTBi3_RftT5UIYKNJ94lIAcgYVQct2eSg4YH-dvgjBPHy15gNlqsXcUmacVECOHw86KYCgBa2mCpM2zYFxRyXqxvPxjz2rsdNZV--WDeufcy8n4xUoy6MF78O6DFAds7LjXpm_WBM_1pNgJNajpaRHR2w8d4M6L4USqAmC-qqm-yGkq3YdOV&gsessionid=i763H7oWEnOpRblGZ4cRFlFyHEpp8igBzINRZIqtXqgaRp2lx-bjIQ)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  Base metals remained under pressure this morning as a firmer dollar and concerns over Chinese demand weighed on sentiment.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 34.17 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 38.07 (-10.3%), 50d 39.11 (-12.6%), 200d 37.95 (-10.0%); 50d above 200d
Momentum: RSI(14) 23.7 | MACD -1.048 vs signal -0.675 (histogram -0.373)
Returns: 1d -5.1% | 5d -9.4% | 1m -14.1% | 3m -13.2%
52-week range: 30.77 - 41.43 (now 31.8% of the way up)
Volatility: ATR(14) 0.74 (2.2% of price) | annualised 20d 29.6%
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
Cost of holding this fund instead of copper itself: -2.7% a year -- a steady drag
Measured: 3 months: fund -13.2%, commodity -12.3%, gap -0.9% | 6 months: fund -11.4%, commodity -10.0%, gap -1.5% | 12 months: fund +10.5%, commodity +13.3%, gap -2.7%
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
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-11-10, published the following Friday)
Large speculators: net long 11.2% of open interest (314,115 contracts)
Change on the week: +0.5% of open interest
Crowding: 3% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +5.6% (33.40M) over 7d | 1 month: +2.9% (17.50M) over 32d
Shares outstanding: 18.33M | fund size: 626.35M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 90 minute budget before GLD was asked

<details><summary><b>News</b> — score n/a</summary>

- [GLD, SLV Sink To Near 14-Month Lows – But This Commodities Expert Sees A ‘Relative Bright Spot’](https://finance.yahoo.com/markets/commodities/articles/gld-slv-sink-near-14-104632506.html)  
  <sub>4 hours ago</sub>  
  Gold futures for December 2026 deliveries were down to $3773.80 per ounce, while silver futures expiring in December declined to $45.68 per ounce.
- [Institutional Flow in SPDR Gold Shares (GLD): 85% of the Options Money Is in Puts](https://www.moomoo.com/community/feed/institutional-flow-in-spdr-gold-shares-gld-85-of-the-117637278663061)  
  <sub>3 hours ago</sub>  
  SPDR Gold ETF (GLD.US)$ : Biggest unusual trade: 7940 call contracts expiring Nov 20, $992K in premium vs 2173 open interest. $GLD: $280.7M in opti...
- [China Gold Market Update: Robust Demand In October](https://www.google.com/goto?url=CAESlAEBxCJF16NMZVfdn8AF2z1VM96HZZCf3vZYvdo3qaY4XZHwdfSgFqudpydGXnuRcJjZNp1bFGflWdug-b_I4qTo4qpf19_ZT-zm0kpic9pG-sobtMkV7cdY_Pa3DkUJjwITM7WavhYvAW6GOimS-u6wo47evuSw3MzuRXcavEMONH98lHVEs6Sfk1Y191Z7pVli5NRk&gsessionid=NCeltcIG8XmqEwPmKK3yevPMPUeMp9L8pXGT3koUpjbJuBGLg4yYWw)  
  <sub>2 hours ago</sub>  
  Both the LBMA Gold Price PM in USD and the Shanghai Benchmark Gold Price PM in RMB extended their September weakness into October. Chinese gold ETFs saw a...
- [Gold Falls Below $3,900 as Caitong Securities Says Central Bank and ETF Buying Retreat, Real Rates Regain Pricing Power](https://www.google.com/goto?url=CAESgAEBxCJF18Oa5EP9Vk65TBxMALilB8RV3BItmBvJ-oV5AnDYZXvwKQHRtA-8rTIjJemOjEVMUTZgceZj5UhFg4xbtQY7t2f2tNyMYBBjfU78b_VDW_j14lFtQS1yBpMG_0pawyuxWCAOLKYoPI_wupJB87lOE08aWnIv2w-aWa-bGw&gsessionid=NCeltcIG8XmqEwPmKK3yevPMPUeMp9L8pXGT3koUpjbJuBGLg4yYWw)  
  <sub>4 hours ago</sub>  
  International gold prices have recently fallen below $3900 per ounce, hitting a more than one-year low, with the US 10-year Treasury yield climbing…
- [Investors Poured $2 Billion Into This Bitcoin ETF as It Lost a Quarter of Its Value This Year](https://www.google.com/goto?url=CAESygEBxCJF12o41eUT1q61KY76V3op3RlcL81_5dq48XVez5N1o-YEVK__iPSAH5yMK9Dp3sHmLj0oCjlOyT1rHmSR-WeMUGujArso2gRgmvApFIkgOJj4v0j2ZLHfo7CXRIoXnRx507ywqSgBCD5XBcoe1LsnRFyml8ZwxCkN--FB40grMxYovw4u_bIb_YZWCX9pOVa3VZmbd1XElgoUTf9R2-7vLLUterzYnYocRyQKztWDFZvMUc-A6gjuWmhjoJZ4XX2VD8z6b-nq&gsessionid=NCeltcIG8XmqEwPmKK3yevPMPUeMp9L8pXGT3koUpjbJuBGLg4yYWw)  
  <sub>23 hours ago</sub>  
  IBIT has lost 26% this year with bitcoin's slide, yet still pulled in about $2 billion in net new money, which Eric Balchunas called "unreal given the...
- [1. iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT)](https://www.google.com/goto?url=CAESowMBxCJF1zcDDcLu2PmLs_dOocG4KvmRY2pGHNVq24Jc6GKhfdN5o4hTZl7Yrvlx1RlO_zl5U8YubZ4LoaOOfgB9n7Hc6aBDcFhZvtYEy8yjV4BR03rKdIo2PmDKxJMQjHjwmG_NocXqRoarmo1ketna0L0zMeKufjcpO_Ob5Sf8OUx8jQKvxoCCxI0dEGNWr6VausG71gp21PlqXwtQGxqF4uoBK4n1pjniX-cD-WUID5_1VRqyS-dM9unlXdIJHOL_WpQtNGD2dXNEZ9ATPUrofIenqrdIXiSUR3vjqhlO_sWGFCramkhvy-BiGzWz_KyfvHmrmaCCkzAnAndckvbtfKVR-llcKAtfIIWc6-sX2RUpkDnVe5razbvk66A4ogXM2ra6eqYveDBkENuF9Y0D-uP58pN-mYmJHNsxL26ngBlVc3xaX2MrE8U4HlHogwxogfvgQJZ4_POk-T4cYO8e0BxWDU6xzzxqqtZtynWw885xHQXqjZV48JtchqkdLl2J2ZM-i7i3UJZ6AQqwgKr29avavW1GwXuwn1weDIa2xSr_Yw&gsessionid=NCeltcIG8XmqEwPmKK3yevPMPUeMp9L8pXGT3koUpjbJuBGLg4yYWw)  
  <sub>21 hours ago</sub>  
  Of the five, iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) is the most sensitive to rates. Because it holds Treasuries with maturities of 20 years or more...
- [Gold seen grinding higher to $4,650/oz by year-end 2027 on central bank buying - Goldman](https://www.google.com/goto?url=CAESuAEBxCJF12o8gQuzcOzSXwORdE3IXYwnYn54i2awH2mUQsdutEPMJFE2NQFD0eHMlye1R0d_iXtqPsf8-ToRYmDem4pDTiEGVCguq8BeEKxs3szx7Y59zzGiF758ZARM0UIMIJYFcvDCn-6cu6gFx_FtQ6sULZcaplSsn6UKnc_ITEDx0i-lEN3zzW9cBtuto_zJXsYzXV_JBOtCZ6wnrHe7Cd1p5QWrghfOldkj7yh5njx1kN0aOnrG&gsessionid=NCeltcIG8XmqEwPmKK3yevPMPUeMp9L8pXGT3koUpjbJuBGLg4yYWw)  
  <sub>16 hours ago</sub>  
  Gold's near-term performance likely will be slowed by expectations of higher interest rates, but central bank buying should push prices back above $4600 by...
- [What Drove Gold to Its Weakest Level Since October 2025 and Weighed on SPDR Gold Shares (NYSEARCA:GLD)?](https://www.google.com/goto?url=CAESzwEBxCJF1x_-rETIa66l03VoY20ssiJSgRS5H-yWSLyln-d4fVPkvuagbjMlsdxteoto2lLl0VHs-OBtspQgjeBzmC74nCKtdZA7ShaAdSjvIBqqM5O1ufGteJUtNKk5ClbM2XxCklsFEuE5YgFX-AKagV1KVSNwQod971t_p2iVg8KKmQDgaZJ2oZ9OBFWem_ESGRvtb8kzbn4iqbNFYiKijJ0LQcoxoLP-9EuMDFXQnGThqrvp7E_iUkRHbmQPBOwEWISaqfGpW4U-qiMl_fQ&gsessionid=NCeltcIG8XmqEwPmKK3yevPMPUeMp9L8pXGT3koUpjbJuBGLg4yYWw)  
  <sub>21 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Which of This Week's Top 3 Pressured Commodity Funds Is Best Positioned: SPDR Gold Shares (NYSEARCA:GLD), United States Oil Fund (NYSEARCA:USO) or iShares Silver Trust (NYSEARCA:SLV)?](https://www.google.com/goto?url=CAESlgIBxCJF137_dGM_Yf5CukeRBvV0gqU8OyYDoJFcN3CGjuDFj6h_R5nalRJCKhz0RsU9i4gXm-bzpYxbe2Zs0Jyku2KnPzqjZwJip9yKcvMpsS5-ZjZDZq1AciAvotMXsHPXFeYxUIb4Jlkfc0Hb2G518mh9dTc_A__LRwx5-fUgH2X5rBo0tLXsvpadY_I0FbeMzwxS-YBS57DI-fghRQlv2-3eIkCDl6HcI1NqCbtQ8Vk7qn534lCG8a8H_LwkJkMuYYSGBGOUWUrXn06HuincQcG0zcSWne0ukIlke4RvjJ0PclXcJruQ1ucgbEDhEsCPjh368I85tJbGaLxO5NLjvYGoFj-gAVQuqh9T3DV98DsdgjlPDQ&gsessionid=NCeltcIG8XmqEwPmKK3yevPMPUeMp9L8pXGT3koUpjbJuBGLg4yYWw)  
  <sub>21 hours ago</sub>  
  Which of This Week's Top 3 Pressured Commodity Funds Is Best Positioned: SPDR Gold Shares (NYSEARCA:GLD), United States Oil Fund (NYSEARCA:USO) or iShares...
- [Day 526: Rate Hike + Trump 2.0 Day 665](https://www.google.com/goto?url=CAESlgEBxCJF19XzxwBZeFJ_O86FGzmvy7x3bFkUr96xX0Wq1V79SS6JkoFl4L5eM_Gdfgc6JLG5q06QCvQ8zywNa_FDFM9Od8sxOGxFYELINo6tmoJLUS8V6ghP6yy1DL2U8qza_EZ0MF7Ea_lTyBcad2bhRodVEhmzCHK3BrX4bcpiVwZ8g3pJLPwwPTK2XZ1K-ZGQgYxZiUY&gsessionid=NCeltcIG8XmqEwPmKK3yevPMPUeMp9L8pXGT3koUpjbJuBGLg4yYWw)  
  <sub>24 hours ago</sub>  
  Market Recap | Tuesday, November 17, 2026 One Report to Decide the Month Tonight Nvidia reports its first quarter since Jensen Huang's exit. In...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 345.37 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 364.51 (-5.3%), 50d 377.72 (-8.6%), 200d 407.04 (-15.2%); 50d below 200d
Momentum: RSI(14) 32.5 | MACD -7.265 vs signal -5.636 (histogram -1.629)
Returns: 1d -2.0% | 5d -5.4% | 1m -8.5% | 3m -16.8%
52-week range: 345.37 - 495.90 (now 0.0% of the way up)
Volatility: ATR(14) 6.66 (1.9% of price) | annualised 20d 28.5%
Volume: 0.33x the 20-day average
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
Cost of holding this fund instead of gold itself: 0.4% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund -16.8%, commodity -17.5%, gap +0.7% | 6 months: fund -17.3%, commodity -16.9%, gap -0.4% | 12 months: fund -7.1%, commodity -7.5%, gap +0.4%
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
Contract: GOLD - COMMODITY EXCHANGE INC. (positions as of 2026-11-10, published the following Friday)
Large speculators: net long 27.8% of open interest (404,725 contracts)
Change on the week: +1.8% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 260.30M | fund size: 89.90B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 90 minute budget before SLV was asked

<details><summary><b>News</b> — score n/a</summary>

- [Silver Linings Can Be Hard To Find](https://seekingalpha.com/article/4969396-silver-linings-can-be-hard-to-find)  
  <sub>10 hours ago</sub>  
  After rallying more than 500% from its September 2022 low to its record high on January 28th, the iShares Silver Trust has since given back nearly 60% of...
- [Gold, silver ETFs plunge up to 3% as bullion prices hit multi-month lows amid US Fed rate hike fears](https://www.moneycontrol.com/news/business/markets/gold-silver-etfs-plunge-up-to-3-as-bullion-prices-hit-multi-month-lows-amid-us-fed-rate-hike-fears-14083149.html)  
  <sub>10 hours ago</sub>  
  Gold and silver exchange-traded funds (ETFs) extended their losses on Wednesday, as a sharp selloff in international precious metal prices weighed on...
- [Silver ETFs Slide Up to 3.3%; Gold Funds Also Under Pressure](https://www.google.com/goto?url=CAESoAEBxCJF1xEOvRWgXdvjAdISkiX3At9LhHYeMpsbUOzok7ghJ0abx99y2VbW7VxNRbuPMUhpz7M8Pa7iGmaF7JK0hpVV-Ghnow7BMQBXYduYL7x5x8OeDgeCoGjBs_aoFBwhJMpfmd-e3C3EUe9bINZ8q7MVbCmlPuDgM916iJmXIm2C9ipxs3vnFedfec2qmL2XfMd3YvPy5JuSYAyAAxPD&gsessionid=q3z51rtizu4WasG67W-cwXkmqnES9OSScOuCFgHeBcWmEwepdf1H1Q)  
  <sub>8 hours ago</sub>  
  Mumbai, Nov 18: Gold and silver exchange-traded funds (ETFs) fell sharply in trade on Wednesday, with all 26 gold funds and all 19 silver funds lower.
- [GLD, SLV Sink To Near 14-Month Lows – But This Commodities Expert Sees A ‘Relative Bright Spot’](https://www.google.com/goto?url=CAESlwEBxCJF12ZJOI4oVZkfyqj3AuzmwTNCJpX7oYXTsROkcvPn3W3UOf05nji4a4ieUGLeZWTTRAVjvPi_a6j_VMXJKFz-JOfDu3frtUnelsC5gdU-Wlur0QdNf9mecS911D8-saTNh0dBNYKV7Czzd8nBIUJdqcPBlQYOanA7CzY86OGqlQgPgB_A_qkTxBugPXfSU6tATIgy&gsessionid=q3z51rtizu4WasG67W-cwXkmqnES9OSScOuCFgHeBcWmEwepdf1H1Q)  
  <sub>4 hours ago</sub>  
  Gold futures for December 2026 deliveries were down to $3773.80 per ounce, while silver futures expiring in December declined to $45.68 per ounce.
- [Silver below $50: How much further could it fall?](https://www.google.com/goto?url=CAESlAEBxCJF1wikuhiJAgFZs6TB53dITElrFosmMu04iNcZ_trTJQ8Xhr1IKl-pyZd4uv5NOK8_ILAg97qNVBwgbRKiTV87HYTSyCUe_FmGEbgL_m_BxP-1nb6l3g5LpCGIxkgEimYu6Ytzw7AZydr0IH3Q9vQmH_N48N326NNsGiS28h-rWISuTmSXtO0CcCTTwIYL1AoU&gsessionid=q3z51rtizu4WasG67W-cwXkmqnES9OSScOuCFgHeBcWmEwepdf1H1Q)  
  <sub>17 hours ago</sub>  
  (Kitco Commentary) - In this presentation, Jeffrey Christian of CPM Group looks at the gold price outlook and silver market as both metals remain under...
- [Current price of silver as of Tuesday, Nov. 17, 2026](https://www.google.com/goto?url=CAESfAHEIkXXKnP7GlkD4DWrgQMj5jAyIpa6E8XTAtpFYhV3s7VAmDTTDR5Zr-D6alNe8nTVOC0tNgPlGpt7SJCWnFhO7QbEB2-ht73IBlR_MIA9XUv9Vl-4NckZ8o-HjjPlEq4DWzroErdUZH5jGak4jG23Ha6_wLc7w2g4gbc&gsessionid=q3z51rtizu4WasG67W-cwXkmqnES9OSScOuCFgHeBcWmEwepdf1H1Q)  
  <sub>18 hours ago</sub>  
  If you're worried about increased inflation, adding precious metals like silver to your portfolio can be a smart choice.
- [Silver today: 2 analysts split between tight supply and fragile technicals](https://www.google.com/goto?url=CAEStQEBxCJF1yW1DUsIiVvvE51K2jFT0akYPzQD9FzfhvyJLnwsO20OLwjW-6Wq9DADE77UyeOF-Mc5Tew5GU2uyvwFn_gBd2ZM2Kf-qciMK00AKV_TkzJrrcBPvl9u7U0yn4y-f4I3885rRLuc5Ex46_Lcos1-BGgssP58TLIE-Vfm50b9czolyjS8G4acBKniHB2oaEVN2MD4TIXsoMDn1eYPprzGLIXJNCKi0RNqcoa7BVziXriN&gsessionid=q3z51rtizu4WasG67W-cwXkmqnES9OSScOuCFgHeBcWmEwepdf1H1Q)  
  <sub>4 hours ago</sub>  
  Silver (XAG/USD) is caught between a supportive long-term supply picture and a short-term chart that has yet to turn. Money Metals' Mike Maharrey highlights...
- [ICICI Prudential Silver ETF (SILVERIETF.NS) Seasonal returns chart](https://www.google.com/goto?url=CAESegHEIkXXFMjwwfMxZw6gqky8JLtKizMRSFpp2nOpbeIP3gOTvR7v1HkyDGuChPajBhcq2TWKaNburNlPhY6ipDnlCv7ubGurGWemlD2NdFkmxvjpwiH6I5SQmgFm-EXNmnJHZ4ng0F50oM7ryyLZGjdK33JXfQ5Oh0bA&gsessionid=q3z51rtizu4WasG67W-cwXkmqnES9OSScOuCFgHeBcWmEwepdf1H1Q)  
  <sub>4 hours ago</sub>  
  ICICI Prudential Silver ETF (SILVERIETF.NS) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [Which of This Week's Top 3 Pressured Commodity Funds Is Best Positioned: SPDR Gold Shares (NYSEARCA:GLD), United States Oil Fund (NYSEARCA:USO) or iShares Silver Trust (NYSEARCA:SLV)?](https://www.google.com/goto?url=CAESlgIBxCJF1_iRv97BnX3IQTiwOSjo8hvO5o9BtmyYUhGlyQ9OjzrZHmRFk6H2RUu7Gk6fJAfYS8x_nsaUyuP8iXdV5ZvAxGFd8G4TeDuPqElP0s01FafHKrkaqxEnRk8Qt8Y7JHcWZgdSEjUDb2drQqJ-C2prsQxMyX-hIF6ukCJMLpJWeecT2OMFMd5CWsfY8IvnvwvEmQzAM6046sFRg0JFFT250VhDZgLvUUVJq8E0vkF2kU_zNmtbtc0dnO3p3KKUs2hxipKuoE64y-hQf06laUDr5xOSYnYUKnuG8ZoCEgorLKCMu1-UiU8D85n39qvvYBsdHtr1OxCARCPEZe6Q9cj69q9DVAsb85LndPn6Jcv1X3WknA&gsessionid=q3z51rtizu4WasG67W-cwXkmqnES9OSScOuCFgHeBcWmEwepdf1H1Q)  
  <sub>21 hours ago</sub>  
  Which of This Week's Top 3 Pressured Commodity Funds Is Best Positioned: SPDR Gold Shares (NYSEARCA:GLD), United States Oil Fund (NYSEARCA:USO) or iShares...
- [Gold seen grinding higher to $4,650/oz by year-end 2027 on central bank buying - Goldman](https://www.google.com/goto?url=CAESuAEBxCJF13sGKin1ILl4zdWGswegsyn7nk6WeWrqFNgL5ey5lb62CZnRsbLdBX06kZUAtzerfhut4e57j17aky_YcalqdN_Hxd2s8fzIV71Vbvd03Gm4G5H1JNPN8ytT3ZNH8K2btE707BT-d3OGF0bvUiF09fpANyXbGlId1AEOwsdZXxnDiwfwUzFIAGfiTkaKXZJvllwHBhlB0AkTFXWTrVeWOK1UzReBimrwTMa6uhNF5XT3jGs-&gsessionid=q3z51rtizu4WasG67W-cwXkmqnES9OSScOuCFgHeBcWmEwepdf1H1Q)  
  <sub>16 hours ago</sub>  
  Gold's near-term performance likely will be slowed by expectations of higher interest rates, but central bank buying should push prices back above $4600 by...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 40.94 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 46.23 (-11.4%), 50d 51.79 (-20.9%), 200d 61.42 (-33.3%); 50d below 200d
Momentum: RSI(14) 26.5 | MACD -2.577 vs signal -2.299 (histogram -0.278)
Returns: 1d -4.0% | 5d -12.2% | 1m -21.4% | 3m -33.6%
52-week range: 40.94 - 105.60 (now 0.0% of the way up)
Volatility: ATR(14) 1.55 (3.8% of price) | annualised 20d 45.0%
Volume: 0.46x the 20-day average
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
Cost of holding this fund instead of silver itself: 1.1% a year -- the roll has been paying this fund
Measured: 3 months: fund -33.6%, commodity -33.8%, gap +0.2% | 6 months: fund -40.4%, commodity -40.6%, gap +0.2% | 12 months: fund -10.0%, commodity -11.0%, gap +1.1%
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
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-11-10, published the following Friday)
Large speculators: net long 3.1% of open interest (115,652 contracts)
Change on the week: -0.4% of open interest
Crowding: 5% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 341.45M | fund size: 13.98B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 90 minute budget before SOYB was asked

<details><summary><b>News</b> — score n/a</summary>

- [Will Soybeans Continue to Follow Oil and Oil Product Prices?](https://www.barchart.com/story/news/8882957/will-soybeans-continue-to-follow-oil-and-oil-product-prices)  
  <sub>19 hours ago</sub>  
  Soybean futures for January 2027 delivery were mostly traded in the teens through September 2026 before falling below $13 per bushel on October 14.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 25.79 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 25.92 (-0.5%), 50d 26.87 (-4.0%), 200d 25.33 (+1.8%); 50d above 200d
Momentum: RSI(14) 42.1 | MACD -0.288 vs signal -0.347 (histogram 0.059)
Returns: 1d -0.3% | 5d -0.6% | 1m -3.4% | 3m -1.5%
52-week range: 21.71 - 28.14 (now 63.5% of the way up)
Volatility: ATR(14) 0.28 (1.1% of price) | annualised 20d 14.7%
Volume: 0.09x the 20-day average
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
Cost of holding this fund instead of soybeans itself: 2.6% a year -- the roll has been paying this fund
Measured: 3 months: fund -1.5%, commodity +0.2%, gap -1.7% | 6 months: fund +2.8%, commodity +2.0%, gap +0.8% | 12 months: fund +8.4%, commodity +5.7%, gap +2.6%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-11-10, published the following Friday)
Large speculators: net long 12.1% of open interest (973,693 contracts)
Change on the week: -2.8% of open interest
Crowding: 32% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -2.3% (-922.77K) over 7d | 1 month: -9.0% (-3.89M) over 32d
Shares outstanding: 1.52M | fund size: 39.13M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 90 minute budget before UNG was asked

<details><summary><b>News</b> — score n/a</summary>

- [Lafung Holdings (01125): Potential spin-off of real estate investment trust for independent listing on the Shanghai Stock Exchange](https://www.moomoo.com/news/post/1004870379/lafung-holdings-01125-potential-spin-off-of-real-estate-investment)  
  <sub>Moomoo, 2 hours ago</sub>  
  LaiSun International (00191), Lai Sun Development (00488) and Lai Fung Holdings (01125) jointly announced that Lai Fung proposes to effect a proposed...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 10.25 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 9.69 (+5.7%), 50d 10.27 (-0.2%), 200d 10.96 (-6.5%); 50d below 200d
Momentum: RSI(14) 54.0 | MACD -0.021 vs signal -0.123 (histogram 0.102)
Returns: 1d +2.0% | 5d +0.2% | 1m -2.4% | 3m +2.3%
52-week range: 9.00 - 16.90 (now 15.8% of the way up)
Volatility: ATR(14) 0.38 (3.7% of price) | annualised 20d 43.3%
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
Cost of holding this fund instead of natural gas itself: -1.7% a year -- a steady drag
Measured: 3 months: fund +2.3%, commodity +18.6%, gap -16.2% | 6 months: fund -10.8%, commodity +7.9%, gap -18.7% | 12 months: fund -27.4%, commodity -25.7%, gap -1.7%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

```text
US inventories, week ending 2026-11-06 (published the following Wednesday)
  Natural gas: 3,862.0 billion cubic feet, +61.0 on the week (a build), 94% percentile over 52 weeks -- high for the time of year
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
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 13.7% of open interest (1,642,671 contracts)
Change on the week: -0.2% of open interest
Crowding: 2% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 12.08M | fund size: 123.81M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 90 minute budget before USO was asked

<details><summary><b>News</b> — score n/a</summary>

- [United States Oil Fund, LP (USO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/USO/)  
  <sub>Yahoo! Finance Canada, 13 hours ago</sub>  
  Find the latest United States Oil Fund, LP (USO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [U.S. crude stockpiles rose 5.3M barrels last week, API says (USO:NYSEARCA)](https://seekingalpha.com/news/4673965-u-s-crude-stockpiles-rose-5_3m-barrels-last-week-api-says)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  The American Petroleum Institute reportedly shows a build of 5.3M barrels of oil in US commercial stockpiles for the week ending November 13.
- [Which of This Week's Top 3 Pressured Commodity Funds Is Best Positioned: SPDR Gold Shares (NYSEARCA:GLD), United States Oil Fund (NYSEARCA:USO) or iShares Silver Trust (NYSEARCA:SLV)?](https://www.google.com/goto?url=CAESlgIBxCJF1ycQdfAVTu-Fg2RmsW816U6qBoaj2arJfrktzbvnIe6WhdWWK-5yjC521UxAgzQOruiA6F3Tp9ugIcH25dxLK8LoylbqtdA_OppX9AxV_Hww6awaAhdQ0C5B4aFqpEyBgeYG_9j_S0XDkfl4tuEWYjzcfxkjajz2IiIzP4s-aJD9N-gpNk4uaQuyV1c5FL0P5ZmvmXWR643DLJFYnHG4rTS-AOnQ1CSFlmRhhNnINSoyniAmAS52VfqqTNBRy8YBeyEhMR3SvIb_fvjjSI5Pm8Qz8QoBXtvxIjp3JofnlHL7tLbMkjcOAGoZr8GzuW7Hm8WdJXeivaBnVgPmk2fwfjS8WbG4kgGytwx-1mbuKnJlAQ&gsessionid=ebAAzF2UrCX9DagFZQrfuaMou1w1mtZOtMCDYFK01x6ak4_E0crbHA)  
  <sub>kalkine.ca, 21 hours ago</sub>  
  Which of This Week's Top 3 Pressured Commodity Funds Is Best Positioned: SPDR Gold Shares (NYSEARCA:GLD), United States Oil Fund (NYSEARCA:USO) or iShares...
- [Russian crude exports reach four-month high as Ukrainian drones slam refineries (USO:NYSEARCA)](https://www.google.com/goto?url=CAESxgEBxCJF17MX_O8PMlEeD2qOluPEn2rUjiPuG6uYjarDtu3FQCmm1v-AUmn6ODVdN-XsShf-RPdYf2R7ysFtE3SbdynOVXUPVLwadU-XD2EC-uFtWg1zBcdklJJx2YfRVZHkNJCjW07MVtpNPBP9Fo6tMoWTCDLiix2x1wMgXuWyBCSprMdCw5-2-kKTBT7dcRtcI7_3yxqRQMKQGA40zZl4YfLQZST1tjCnktun7rfj3t31cH4Ov3LJG1-W37u_nnNYgg_UkFw&gsessionid=ebAAzF2UrCX9DagFZQrfuaMou1w1mtZOtMCDYFK01x6ak4_E0crbHA)  
  <sub>Seeking Alpha, 14 hours ago</sub>  
  Russia loaded more than 30M barrels of crude oil onto tankers last week, the most since late July, as Ukraine ramped up its attacks on the country's...
- [Oil prices rise after fresh Middle East flareups; Trump says probing Iranian dirty bomb plot in D.C.](https://www.google.com/goto?url=CAESxQEBxCJF15FvoDtyMRZ9l-FBqAI5bB6JOIefSPLuuteMI7JdyuFtvu7oEwDpoURcSIiELXK4HqSlWFCL9ph8HqGjvkSaDxvH4VZjQ3IwQ-O2EzXDhUNX8UjDGv1u6f-nBzXfPtLm9HajAJrh82LhTlBJLz6gVY0mS0cDXq4YKpAjIwYWP-4eFaTqflCQ3YII6Q6aXA6jg91euyg6ceCfRbxFq0w5vb9X_TyIy8yML_AHpQwL9BbtOrqkULyFxyInUFY4W_V6Sg&gsessionid=ebAAzF2UrCX9DagFZQrfuaMou1w1mtZOtMCDYFK01x6ak4_E0crbHA)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Crude oil futures rose after swinging between gains and losses amid continued tanker attacks in the Middle East, rebounding from recent declines driven by...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 138.21 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 152.93 (-9.6%), 50d 152.42 (-9.3%), 200d 128.59 (+7.5%); 50d above 200d
Momentum: RSI(14) 35.8 | MACD -3.918 vs signal -1.960 (histogram -1.959)
Returns: 1d -1.4% | 5d -2.3% | 1m -13.9% | 3m +2.7%
52-week range: 66.17 - 169.53 (now 69.7% of the way up)
Volatility: ATR(14) 5.10 (3.7% of price) | annualised 20d 49.5%
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

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

```text
US inventories, week ending 2026-11-06 (published the following Wednesday)
  Crude oil: 414.4 million barrels, +4.7 on the week (a build), 21% percentile over 52 weeks
  Petrol: 210.8 million barrels, +1.8 on the week (a build), 35% percentile over 52 weeks
  Diesel: 103.3 million barrels, +4.1 on the week (a build), 21% percentile over 52 weeks
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
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-11-10, published the following Friday)
Large speculators: net long 1.3% of open interest (1,917,473 contracts)
Change on the week: +0.2% of open interest
Crowding: 28% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 8d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 119.10M | fund size: 16.46B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — no answer, no confidence given

**This one did not finish:** the full-model stage ran past its 90 minute budget before WEAT was asked

<details><summary><b>News</b> — score n/a</summary>

- [Wheat Rallying on Tuesday Following Black Sea Strikes](https://www.barchart.com/story/news/8881704/wheat-rallying-on-tuesday-following-black-sea-strikes)  
  <sub>21 hours ago</sub>  
  The wheat complex is posting gains across most of the three exchanges, following Black Sea events overnight. Chicago SRW futures are posting gains of 9 to...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.91% (+0.08 on the week) | 10-year 5.10% (+0.10 on the week) | 30-year 5.44% (+0.08 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 103.79 (+0.88 on the week)
Volatility (VIX): 24.33 (+6.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.83% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 21.60 (bar of 2026-11-18), from 502 daily bars
Trend: vs 20d SMA 22.06 (-2.1%), 50d 23.90 (-9.6%), 200d 23.62 (-8.6%); 50d above 200d
Momentum: RSI(14) 35.3 | MACD -0.608 vs signal -0.694 (histogram 0.085)
Returns: 1d -1.7% | 5d -2.6% | 1m -8.3% | 3m -14.9%
52-week range: 19.88 - 28.00 (now 21.2% of the way up)
Volatility: ATR(14) 0.40 (1.8% of price) | annualised 20d 18.9%
Volume: 0.10x the 20-day average
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
Cost of holding this fund instead of wheat itself: -10.8% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -14.9%, commodity -11.9%, gap -3.0% | 6 months: fund -13.3%, commodity -8.9%, gap -4.3% | 12 months: fund -0.2%, commodity +10.5%, gap -10.8%
A commodity fund holds futures, not wheat, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

```text
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 14.6% of open interest (553,579 contracts)
Change on the week: +1.6% of open interest
Crowding: 37% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +0.0% (71.47K) over 7d | 1 month: -7.0% (-17.57M) over 32d
Shares outstanding: 10.84M | fund size: 234.21M
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

