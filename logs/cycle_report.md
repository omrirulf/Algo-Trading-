# Daily report

**17 Nov 2026, 17:03 Israel time (15:03 UTC)** · 80 names checked · 0 traded · 60 with a problem

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 0 | 10 | 6 |
| Whole-market funds | 14 | 0 | 0 | 14 |
| Sector and country funds | 41 | 0 | 10 | 31 |
| Commodities | 9 | 0 | 0 | 9 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| South Korea (EWY) · Sector or country | **Stop raised.** At +0.15R, following the price. Stop-loss raised 152.20 → 148.87. |
| Brazil (EWZ) · Sector or country | **Stop raised.** At +0.62R, following the price. Stop-loss raised 33.49 → 33.34. |
| HDFC Bank (HDB) · Company | **Stop raised.** At +2.91R, following the price. Stop-loss raised 25.03 → 25.27. |
| MercadoLibre (MELI) · Company | **Stop raised.** At +0.18R, following the price. Stop-loss raised 1604.57 → 1580.76. |
| Nvidia (NVDA) · Company | **Stop raised.** At +5.08R, following the price. Stop-loss raised 179.59 → 174.60. |
| Poland (EPOL) · Sector or country | **Holding.** -0.08R, holding 96 shares. Stop-loss 42.85. |
| Sweden (EWD) · Sector or country | **Holding.** -0.58R, holding 134 shares. Stop-loss 50.98. |
| Alphabet (Google) (GOOGL) · Company | **Holding.** -0.63R, holding 4 shares. Stop-loss 274.24. |
| Defence and aerospace (ITA) · Sector or country | **Holding.** -0.26R, holding 98 shares. Stop-loss 69.44. |
| JPMorgan Chase (JPM) · Company | **Holding.** -0.77R, holding 4 shares. Stop-loss 331.83. |
| US regional banks (KRE) · Sector or country | **Holding.** -0.32R, holding 97 shares. Stop-loss 70.08. |
| Novo Nordisk (NVO) · Company | **Holding.** -0.11R, holding 124 shares. Stop-loss 39.89. |
| Procter & Gamble (PG) · Company | **Holding.** +1.60R, holding 2 shares. Stop-loss 165.90. |
| Royal Bank of Canada (RY) · Company | **Holding.** -0.70R, holding 6 shares. Stop-loss 195.93. |
| Teva Pharmaceutical (TEVA) · Company | **Holding.** +0.61R, holding 36 shares. Stop-loss 41.85. |
| Toyota (TM) · Company | **Holding.** +0.00R, holding 1 shares. Stop-loss 205.44. |
| US house builders (XHB) · Sector or country | **Holding.** -0.28R, holding 68 shares. Stop-loss 97.50. |
| US media and communication (XLC) · Sector or country | **Holding.** +1.65R, holding 47 shares. Stop-loss 104.93. |
| US banks and finance (XLF) · Sector or country | **Holding.** -0.46R, holding 120 shares. Stop-loss 56.96. |
| US health care (XLV) · Sector or country | **Holding.** -0.43R, holding 37 shares. Stop-loss 183.37. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### ASML (ASML) · Company — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [ASML Plunged 17% Lower Over 3 Months: This Wall Street Desk Expects 88% Gains Over the Next 12](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc677efab54e9da474ae4380d6d75e&url=https%3a%2f%2f247wallst.com%2finvesting%2f2026%2f11%2f16%2fasml-plunged-17-lower-over-3-months-this-wall-street-desk-expects-88-gains-over-the-next-12%2f&c=15547900453919885348&mkt=en-us)  
  <sub>24/7 Wall St., 29h ago</sub>  
  ASML posted record revenue and still got hammered by sector-wide AI fears, with no company-specific bad news to blame. Why one bank sees far more upside than the consensus, and what could still derail ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,404.37 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 1,532.74 (-8.4%), 50d 1,647.12 (-14.7%), 200d 1,601.95 (-12.3%); 50d above 200d
Momentum: RSI(14) 36.1 | MACD -63.839 vs signal -58.052 (histogram -5.787)
Returns: 1d -0.2% | 5d -6.9% | 1m -14.7% | 3m -19.8%
52-week range: 966.57 - 1,989.44 (now 42.8% of the way up)
Volatility: ATR(14) 63.32 (4.5% of price) | annualised 20d 65.2%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 541.27B
Valuation: trailing P/E 34.56 | forward P/E 22.15 | P/B 1,205.86 | PEG 0.79
Profitability: profit margin 34.1% | operating margin 38.6% | ROE 65.6%
Growth (YoY): revenue +55.2% | earnings +135.9%
Balance sheet: debt/equity 8.9% | free cash flow 10.37B
Risk: beta 1.33 | short interest 0.3% of float
Next earnings: 2027-01-27
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
Price target: mean 2,108.35 (+50.1% vs last close), range 850.43 - 2,793.63
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

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 1,915,500 shares
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

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Why Is Red Cat Holdings Stock Falling 25.8% in Pre-Market Trading?](https://finance.yahoo.com/markets/stocks/articles/why-red-cat-holdings-stock-112801210.html)  
  <sub>3 hours ago</sub>  
  Red Cat Holdings (NASDAQ:RCAT) shares declined 25. 8% in pre-market trading on Tuesday after the defence drone manufacturer reported third-quarter revenue...
- [Why Is Red Cat Stock Falling Tuesday?](https://www.benzinga.com/trading-ideas/movers/26/11/63335376/why-is-red-cat-stock-falling-tuesday)  
  <sub>2 hours ago</sub>  
  Red Cat Holdings, Inc. (NASDAQ:RCAT) stock plunged in Tuesday's premarket session after the defense drone maker missed third-quarter earnings estimates and...
- [Red Cat Plunges 34% After Revenue Miss, Pulled Guidance and Needham Target Cut; Ondas and AeroVironment Dip](https://www.google.com/goto?url=CAESlwEBxCJF17OpVDDA30X624wl2ue4Rbj4TdXu8NLo3BsCTw2A8H3GK5tjPeQQ5o6NerEOUhc6j7o16geoWUnH3Z43RKjqXvUP6KGdDYaSAP8ZZTEAUCdG7F5ZZVxAXRJ9nbFohfiGcF_s5M3s9k6AQ9YIauQHXF54t7MKaZz3qcNwN1-CCYcwOMr_fHZQcX3r-5D8NrpgaCe7&gsessionid=xoO15mJSeCfSaKnuP87DOWV5d8dLimkf9qd-alResMTJ91Jgj5HVNQ)  
  <sub>25 minutes ago</sub>  
  While Red Cat tumbles, its drone-sector rivals barely flinch. Why are investors treating a withdrawn revenue target and a failed Pentagon evaluation as one...
- [Michael Burry Cashed In Caterpillar Puts After a Nearly 4x Gain Even as CAT Stock Fell 10% in Its Worst Week in 18 Months. Is Caterpillar Still Overvalued, or Did Burry Just Lock In the Easy Money?](https://www.google.com/goto?url=CAESqQIBxCJF1wvxD9fihd4A0JgGn3RdeEZQ0Nr8miZZeOrkuLp5Aew_ZfZ1JwAxIRMTh4cci-m1ZfvRH7PDE5wZWKm1GR5-yDrSvuCR44d7yFo26k9Cz_4lDLZ8opS9PxNmjXTXShcAkXTpSMx6uy5hMPBP_myIhb6r5pskEtTS30FYEtjNTw4scqM7Ad-Gw5rV-uWK0MJxLkF_6cPjnMGUOfHHLBMIvHvsWW8QaOrKtNWGyVFTWCtOT8N_dqzY-BVpEvRE7ZltB8Zb9FzrxQxmZAXAV0AGmy40bLy_pc5fZVHE0gncwYHavywqQLnzMANiNSoWtYA_CGqgNj-bV0x9TSe4sJgZjsOX3yZD0Ip3VBhmCyVrgL5ZIxwFa87Lqfs3JXPSyRTMuEG4ouY&gsessionid=xoO15mJSeCfSaKnuP87DOWV5d8dLimkf9qd-alResMTJ91Jgj5HVNQ)  
  <sub>18 hours ago</sub>  
  Caterpillar (CAT -4.95%) has quickly fallen 44% from its highs, which is the largest drawdown for the construction equipment company in the last 10 years.
- [What Has Changed In Caterpillar’s Story?](https://www.google.com/goto?url=CAESngEBxCJF11ZdwaAIGEU_pPy7HBGuYI_gsOasE--KFfUqJVIGlDlY1bmLBkA_hm485LXvq_GyjWw7jx7nKStwK8vbqLaayjiqFTENLU9rgUA6_5SXdKhRZFySQm6Oy0A8qwEgXvd-Gz6yFMHmw3x4VlTa36RSUKJXOU11jzKzCp8m7vDBKE70zSgBEBTSCI29bjGohT1o7RmPIECgvPuN3Q&gsessionid=xoO15mJSeCfSaKnuP87DOWV5d8dLimkf9qd-alResMTJ91Jgj5HVNQ)  
  <sub>16 hours ago</sub>  
  For questions about this article or underlying research, email help@trefis.com. Caterpillar (CAT) stock trades at 23.3 times earnings, against 21.9 for the...
- [Why is Red Cat Holdings stock plummeting today?](https://www.google.com/goto?url=CAESqAEBxCJF19SR_8Bg8Bj6df9-1ePksG0zE6rHi2GLIv3lEhk346D3bVpnvRLIDFdmOU9eeEdSwDNh7YlTlOfGb2QRmIpFSerhDskJ_i5f5UhIu0e7qYwi6xpR6T4D53YvPm1bHdDYM55sKPTpOnB_E8LNCTxLKl0_lh6A3DEgh0b1wbWxGZ_CQ4XYHe9mBg2RcXDS2k3hYv4tJebGTLBea1kltWENvfVfxWU&gsessionid=xoO15mJSeCfSaKnuP87DOWV5d8dLimkf9qd-alResMTJ91Jgj5HVNQ)  
  <sub>5 hours ago</sub>  
  Investing.com -- Red Cat Holdings stock plunged 25.8% in pre-open trading after the defense drone maker reported a deeply disappointing fiscal third quarter...
- [Michael Burry boosts Adobe stake, exits Oracle, Caterpillar puts (ADBE:NASDAQ)](https://www.google.com/goto?url=CAESoAEBxCJF10x9ZxSw2u3Ahwzt9HlvRA7gist6JbWi3zBIgCaCWybpvBxj6kS1nnMCCe2DewZTkJt-YAgkLO1wiQx3LuhpPciBd7kbs4ni7HDdq09RPWuKWAnHs8SPJ3LefhTdPEzxRZHXE07J1SOCnQvmVyKmso-7nNzkTKdyPHqgfB8QyJ63HGOcRVXhf35kOn_-JKVQExv3swccHHt7Vjyp&gsessionid=xoO15mJSeCfSaKnuP87DOWV5d8dLimkf9qd-alResMTJ91Jgj5HVNQ)  
  <sub>5 hours ago</sub>  
  'The Big Short' investor Michael Burry said on Monday he increased his stake in Adobe (ADBE) at an approximate price of $246. ADBE closed 1.2% higher on...
- [“Trades Basically Like an AI Stock”: Caterpillar Just Dropped 22% in a Month. Sell, or Load Up?](https://www.google.com/goto?url=CAESrwEBxCJF1_AEJFTn6iTLq349Vpi8VaNeBMRT6ZSLS7bsaECcYcR8yrr-uyHg38TjvkSAVCzE8ZamH6NQCDVDeuW08VEfTg0UuV7Fg8NlU7oS2ZmKiCbl6vY-5kOtRCWtOA1-gDWqOQLXuC3nA_4YWcT2aeC6lvWYeDyfeD9CGqL8XHl76K9yNHuf4p4qbv2gkssVdWLVtNFzXhoSt4qqnCsqQ0PT0QBIhe8vAQG-mibw&gsessionid=xoO15mJSeCfSaKnuP87DOWV5d8dLimkf9qd-alResMTJ91Jgj5HVNQ)  
  <sub>37 minutes ago</sub>  
  Caterpillar stock is down 22% in the past month. A soft fourth-quarter outlook started the drop, and an AI-power selloff that also hit GE Vernova deepened...
- [Red Cat Stock Tanks After Q3 Earnings Miss Estimates, Revenue Guidance Withdrawn](https://www.google.com/goto?url=CAESjgEBxCJF16b9OHIJ35-AN4sFuoybU9ygMOki28Vxc7dhbWW6dAj-5YqfenJcqWh2-1tCjt8fUyxpmEJknpai7iFmYVHzh80JtWg8nhDuH5regd6Oa0P_4VTuryGMzBTqTtn5iz-3iZ-A-VdIkCO2elAALQzTbP8SJqDoWWGrYrMEbC3KKmhWbkucom7J1LLT&gsessionid=xoO15mJSeCfSaKnuP87DOWV5d8dLimkf9qd-alResMTJ91Jgj5HVNQ)  
  <sub>17 hours ago</sub>  
  Red Cat Holdings Inc. (NASDAQ:RCAT) posted its third-quarter fiscal 2026 results after Monday's closing bell, missing estimates on the top and bottom lines.
- [Why Is RCAT Stock Plunging More Than 24% Overnight?](https://www.google.com/goto?url=CAESmQEBxCJF15a-eQs_SzjcLacXPxknDCcSmdZZ5w5Q6xcms245JJ02vbjkFBy8v8b0w6In08M9_2Ce8xeLha14JQc6gTkchkt8VL1PsR2P_f95_BjIY7RgEZSOlAezTU1tnuL5GrOGxNrF1hXpaTX_16MUegPpe9pzqfQ6mrAs38LMgQNQJUSAlsIIgR-Z8uCPnPtfxDBjNfe7uuQ&gsessionid=xoO15mJSeCfSaKnuP87DOWV5d8dLimkf9qd-alResMTJ91Jgj5HVNQ)  
  <sub>9 hours ago</sub>  
  Red Cat's revenue rose 22% year-over-year to $11.77 million, but came in well below analysts' expectations of $40.68 million.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 580.07 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 630.12 (-7.9%), 50d 731.05 (-20.7%), 200d 806.44 (-28.1%); 50d below 200d
Momentum: RSI(14) 34.0 | MACD -46.074 vs signal -48.047 (histogram 1.973)
Returns: 1d +1.7% | 5d -0.8% | 1m -20.1% | 3m -28.9%
52-week range: 546.13 - 1,064.90 (now 6.5% of the way up)
Volatility: ATR(14) 27.94 (4.8% of price) | annualised 20d 62.1%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 265.44B
Valuation: trailing P/E 22.77 | forward P/E 18.03 | P/B 12.36 | PEG 1.05
Profitability: profit margin 15.2% | operating margin 18.8% | ROE 56.1%
Growth (YoY): revenue +17.3% | earnings +46.1%
Balance sheet: debt/equity 210.4% | free cash flow 3.97B
Risk: beta 1.64 | short interest 2.0% of float
Next earnings: 2027-01-28
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 in line
  2026-09-30 in line | 2026-06-30 beat by 31% | 2026-03-31 beat by 19% | 2025-12-31 beat by 9%
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
Consensus: buy (mean 1.97 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 2 strong buy, 15 buy, 11 hold, 1 sell, 0 strong sell
Price target: mean 807.26 (+39.2% vs last close), range 575.00 - 1,027.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

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

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Elbit Systems (ESLT) · Company — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Elbit Systems (ESLT) Surpasses Q3 Earnings Estimates](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc67f58ab54ff18b9cf7b0bceb4968&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2felbit-systems-eslt-surpasses-q3-111001591.html&c=15801718634677216083&mkt=en-us)  
  <sub>Yahoo Finance, 12h ago</sub>  
  Elbit (ESLT) delivered earnings and revenue surprises of +9.82% and -1.29%, respectively, for the quarter ended September 2026. Do the numbers hold clues to what lies ahead for the stock?
- [Elbit: Q3 Earnings Snapshot](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc67f58ab54ff18b9cf7b0bceb4968&url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2felbit-q3-earnings-snapshot%2far-AA2hAJLA&c=10411508955015321339&mkt=en-us)  
  <sub>Midland Daily News on MSN, 15h ago</sub>  
  HAIFA, Israel (AP) — HAIFA, Israel (AP) — Elbit Systems Ltd. (ESLT) on Tuesday reported profit of $177.9 million in its third quarter. The Haifa, Israel-based company said it had profit of $3.70 per ...
- [Elbit Systems Earnings Preview: Eleven Straight Beats Raise the Bar](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc67f58ab54ff18b9cf7b0bceb4968&url=https%3a%2f%2f247wallst.com%2fcards%2feleven-straight-quarterly-eps-beats-the-last-four-by-double-eslt-earnings-calendar-01m7mbth6az2a6tn8442as9t2d&c=3032400527803381658&mkt=en-us)  
  <sub>24/7 Wall St., 14h ago</sub>  
  Eleven straight quarterly EPS beats, the last four by double-digit margins, set a high bar for Elbit Systems ahead of its earnings report before the open. Consensus sits at $3.94 EPS.
- [Elbit Systems beats analysts; order book reaches new peak](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc67f58ab54ff18b9cf7b0bceb4968&url=https%3a%2f%2fen.globes.co.il%2fen%2farticle-elbit-systems-beats-analysts-order-book-reaches-new-peak-1001563733&c=10058189428018329463&mkt=en-us)  
  <sub>Globes, 12h ago</sub>  
  Elbit Systems (TASE: ESLT; Nasdaq: ESLT) has concluded yet another quarter with an increase in its order backlog, to a record $33 billion. The defense company recorded 17.2% revenue growth in the ...
- [Elbit Systems stock reports strong third-quarter results and outlook](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc67f58ab54ff18b9cf7b0bceb4968&url=https%3a%2f%2fwww.ad-hoc-news.de%2fboerse%2fnews%2fcorporate-news%2felbit-systems-stock-reports-strong-third-quarter-results-and-outlook%2f70525913&c=11230753349139572568&mkt=en-us)  
  <sub>Ad Hoc News, 12h ago</sub>  
  Elbit Systems stock posted double-digit third-quarter growth and a record backlog. Management expects further revenue growth and margin expansion in 2027. Revenue reached 2.2521 billion US dollars in ...
- [Elbit Systems Ltd](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc67f58ab54ff18b9cf7b0bceb4968&url=https%3a%2f%2f247wallst.com%2fcompanies%2feslt%2fprice-prediction%2f&c=13985047916096011344&mkt=en-us)  
  <sub>24/7 Wall St, 26h ago</sub>  
  Looking ahead to 2030, our model projects ESLT could trade at an average price of $1,085.61, with a potential range between $814.20 and $1,357.01. This represents a potential 53.6% return from today’s ...
- [Morning Movers: Elbit jumps, JD.com falls after quarterly results](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc67f58ab54ff18b9cf7b0bceb4968&url=https%3a%2f%2fwww.tipranks.com%2fnews%2fthe-fly%2fmorning-movers-elbit-jumps-jd-com-falls-after-quarterly-results-thefly-news&c=15057006816877844359&mkt=en-us)  
  <sub>TipRanks, 9h ago</sub>  
  Stock futures are mixed as investors brace for Nvidia’s quarterly earnings after the closing bell, with continued weakness in semiconductor stocks weighing on ...
- [Elbit sees opportunities from end of US military aid to Israel](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc67f58ab54ff18b9cf7b0bceb4968&url=https%3a%2f%2fwww.marketscreener.com%2fnews%2felbit-systems-sees-benefit-from-end-of-us-aid-to-israel-q3-profit-jumps-ce785edcd98df723&c=14791692527983875438&mkt=en-us)  
  <sub>MarketScreener, 9h ago</sub>  
  Elbit Systems Ltd. Reports Earnings Results for the Third Quarter and Nine Months Ended September 30, 2026 CI 07:15am Elbit Systems Third-Quarter Results Rise Amid Broad-Based Segment Strength MT ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 732.85 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 736.14 (-0.4%), 50d 723.68 (+1.3%), 200d 785.39 (-6.7%); 50d below 200d
Momentum: RSI(14) 51.3 | MACD -5.115 vs signal -1.881 (histogram -3.233)
Returns: 1d +7.7% | 5d -1.0% | 1m -3.5% | 3m -2.6%
52-week range: 454.95 - 1,014.33 (now 49.7% of the way up)
Volatility: ATR(14) 29.94 (4.1% of price) | annualised 20d 67.0%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 34.36B
Valuation: trailing P/E 55.14 | forward P/E 39.37 | P/B 7.77 | PEG n/a
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
Price target: mean 838.92 (+14.5% vs last close), range 738.50 - 960.00
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

### Alphabet (Google) (GOOGL) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Market is Aware of Alphabet’s (GOOGL) Successful Founder Transition: Now What Lies Ahead?](https://finance.yahoo.com/markets/stocks/articles/market-aware-alphabet-googl-successful-134934914.html)  
  <sub>Yahoo Finance, 52 minutes ago</sub>  
  We just published a list of 10 Stocks that Have Survived Major Founder Transitions, and Alphabet Inc. (NASDAQ:GOOGL) ranked 9th on this list.
- [Alphabet Stock Down Nearly 17%: What Decides It Now?](https://www.trefis.com/stock/googl/articles/625697/alphabet-stock-down-nearly-17-what-decides-it-now/2026-11-17)  
  <sub>Trefis, 3 hours ago</sub>  
  For questions about this article or underlying research, email help@trefis.com.If you own Alphabet (GOOGL), the past month has been hard: the stock lost...
- [Alphabet (GOOGL) Stock Quotes, Company News And Chart Analysis](https://www.google.com/goto?url=CAESrAEBxCJF1_M-8neI0-uMu7I6RtT8BvvAuK135pvsFQETtlTIN1LI_qrrP9vU22UcGrWF8FDGerMKF8z79owFnn-5uQyH2OHej4wR94PSCR-akJroTTAuQX1vmVYReHEzN7_bVFJDD7Dp29b-b_luxAUbJu7iC-OckfRC91msMz6dM1X-gHqlD9x5NnGvEtgRR32ilLAOmmASGy04dTpALu4_cXi4QIln_QD_81BH&gsessionid=_vNn5VR7Q8PYjWjDMrosTuPZi5eHI32ZQoI5NNsI9MvKzSGDQ26sMg)  
  <sub>Investor's Business Daily, 19 hours ago</sub>  
  Alphabet (GOOGL) Stock Quotes, Company News And Chart Analysis · Google Stock: Alphabet News & Analysis · Related news · Berkshire Hathaway Slashes This Top 5...
- [Alphabet: The Funding Scare Is The Bull Case](https://www.google.com/goto?url=CAESjAEBxCJF10FaMxl8cUR98j6XwPGuGOYaGV1sPT-bZY9UBzdAh8k7VquvYg4D02Qs6umY6hVvhye4p-TcDa1mE0FjtiANfo8wJ8TR-rj187YMKSqb2pVxhZNFi-wR4FQpbF6fwYux1fxQVamk3xdaJNmnp-4uNkKb2emVM1rjQC07bUeAfLPt0y9pn_89Pg&gsessionid=_vNn5VR7Q8PYjWjDMrosTuPZi5eHI32ZQoI5NNsI9MvKzSGDQ26sMg)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  Analyst rates Alphabet (GOOGL) a Buy at Microsoft's valuation: revenue rose 25%, and slower capex could restore cash flow as AI builders lose growth.
- [Why We Prefer Alphabet Stock Over Meta Right Now](https://www.google.com/goto?url=CAESnAEBxCJF1ztBVldHfZR7-i5rnYQnHyJvuf1LWY7ywdTLtdsK6ugRlRUKk_b_4H5js-vOSkaA8GG1hV7cIqxzuKNI37trK39Qa2NOs0tQzwOkvrvbZT9ERkundvqK5aQkxPR8MHO3w9S2zKOMEjJPu4IXUGzUgynxaLZYbiIEULGn4VMvqx9uToeCokX0TNq6OQNPj1oacKm79U8htnk&gsessionid=_vNn5VR7Q8PYjWjDMrosTuPZi5eHI32ZQoI5NNsI9MvKzSGDQ26sMg)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  Our Monday piece, Should You Be Worried About Meta Stock?, opened on a split result: Meta Platforms (META) grew revenue 26% in its September quarter,...
- [Alphabet makes $10 billion Anthropic investment: Can GOOGL avoid deeper losses?](https://www.google.com/goto?url=CAESkwEBxCJF16_iOPTfFA0TX7KJY1m86nXAexdV9BEX8aEi2zbUBgcSFlr0WVCXVby-zabbJFox0RSN3JnfgTIzMtspYKYOM3wPgBPLqx3vKkwI3P4auvdDEX9KhvL69Al5bJEuiuHSHC-OX4qQ-YEhXI6cIPpUiAZDucJj8AVMcwmk56hZVF1QhDx4QwiMQ0tycCROWbI&gsessionid=_vNn5VR7Q8PYjWjDMrosTuPZi5eHI32ZQoI5NNsI9MvKzSGDQ26sMg)  
  <sub>Traders Union, 6 minutes ago</sub>  
  Highlights. Alphabet invested $10 billion in Anthropic, acquiring 135 million shares in a private placement ahead of the IPO. A $200 billion infrastructure...
- [Alphabet Inc Class A (GOOGL) Stock Analysis & Forecast](https://www.google.com/goto?url=CAESdQHEIkXXVnOGkqBsoaJ6rCx9REFE9uq0rpP7Q7aV49SUU8vhybw1iBNypx_JtrU8SBXBVz6LF5t7Xfa-PkiIgxayhczXUOTzlVMqVQDetum8OWN0XJVYuI4GyLQ7v2P95k_AFzHzjlbC70L4wpXEvzhX9ykyXg&gsessionid=_vNn5VR7Q8PYjWjDMrosTuPZi5eHI32ZQoI5NNsI9MvKzSGDQ26sMg)  
  <sub>TradingKey, 15 hours ago</sub>  
  You will find the latest Alphabet Inc Class A (GOOGL) stock analysis, including valuation, earnings outlook, analyst forecasts, technical trends and key...
- [ServiceNow Stock’s (NOW) Historic Sell-Off May Have Gone Too Far](https://www.google.com/goto?url=CAES0QEBxCJF14lRAtZMT_ZB2tvwoCyZOKl6NumK5YDtywsLp4NI5-rtGb3MUBY1Ta6WSXfRZuC3BYpLTc44kSkxIdGgTgFv2O5VHqL1rey9HoOc8Zc2_p6lfe8YV7456Xm7jJNhm0YI47BIQDo388ONZ7FNQe0H3ev5zihgwJVNaCC4exoN-8e-op3197LdmH5T0auqr_5SSW4AJ-VQ2nAgJv140rnjlpguSf9GYkuJDyb0s0NceEpRgTbaUuGYzykPHNcdO900MkrsdYrR_kgROj6NYQ&gsessionid=_vNn5VR7Q8PYjWjDMrosTuPZi5eHI32ZQoI5NNsI9MvKzSGDQ26sMg)  
  <sub>The Globe and Mail, 57 minutes ago</sub>  
  ServiceNow (NOW) stock's historic sell-off looks excessive to me. The enterprise workflow software provider disappointed investors with its Q3 earnings and...
- [Can Google Afford AI Without Nvidia?](https://www.google.com/goto?url=CAESngEBxCJF16dZ_5je87Kb8xN8YgGj1l7mDiDAUCTTODw5k656Dbq3HJffx6A7aO4fQHY-WuxMMDvVEQZXim1zeRQ-pYHpAZF24OarFvigX1sislVgwSDpAY82R26zbhS8RHMb7NEsCKy3J4wsklasiAWaJeu7c_rE_3U_-nl7dkdEshfDBicslMGgvmG6SSMup8rFkb25mgi92WkuZQbirg&gsessionid=_vNn5VR7Q8PYjWjDMrosTuPZi5eHI32ZQoI5NNsI9MvKzSGDQ26sMg)  
  <sub>Trefis, 6 hours ago</sub>  
  Today's big story: Could Nvidia Stock Fall 50%? Follow The Cash This morning you probably asked Google something and got a written answer instead of ten...
- [SPY, AMD And Google Stock Fall Premarket Ahead Of Nvidia Earnings](https://www.google.com/goto?url=CAESpQEBxCJF12FHGNCMYfmEeim-kUpn-op8l9XsLVbkkCFHZDRaV4SWqWl7WcpkJ3dqNR_QNxXOZ33wF50Xv5YHIoVWOt9yEbRKYB3XWFrY8F3kfFx2BwoieX1uBXIGosikEF3FWM8jJQXeyT7XXL6SNbOWnUZCynhNBT6UoNkxJYWRLKw-2MqAQXAL5EYYPd-ghyQTs1lotLk1VJ1FdsEni09Gtu71dWY&gsessionid=_vNn5VR7Q8PYjWjDMrosTuPZi5eHI32ZQoI5NNsI9MvKzSGDQ26sMg)  
  <sub>Coinpedia, 18 hours ago</sub>  
  The SPDR S&P 500 ETF Trust (SPY) fell 0.35% in premarket trading on Monday to $751.76, down $2.61 from its last close of $754.37, as AI-linked stocks.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 282.16 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 297.49 (-5.2%), 50d 325.97 (-13.4%), 200d 337.90 (-16.5%); 50d below 200d
Momentum: RSI(14) 33.7 | MACD -12.305 vs signal -13.112 (histogram 0.807)
Returns: 1d -0.5% | 5d -1.8% | 1m -18.0% | 3m -18.1%
52-week range: 273.50 - 402.62 (now 6.7% of the way up)
Volatility: ATR(14) 9.91 (3.5% of price) | annualised 20d 52.5%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 3.47T
Valuation: trailing P/E 14.73 | forward P/E 18.59 | P/B 5.26 | PEG 1.04
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

- [HDFC Bank Limited (HDB) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/HDB/)  
  <sub>22 hours ago</sub>  
  HDFC Bank Limited (HDB) · 1.84% · 11.71% · 7.51% · -27.87% · -27.87% · -25.94% · 3,525.52%. Key Events. Baseline. Advanced Chart. Loading chart...
- [HDFC Bank Limited (HDFCBANK.NS) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/HDFCBANK.NS/)  
  <sub>23 hours ago</sub>  
  Find the latest HDFC Bank Limited (HDFCBANK.NS) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [SEC Filings for Nov 16, 2026 - 10-K, 10-Q, 8-K Forms](https://www.google.com/goto?url=CAESdgHEIkXX-O6sUIWAxs-lWxCpupsTHWhnn6aeHBpeJTLmwAgdlzuzcAGw1lMISWcnK7FOYILqYZzidCDBXrFn43X-IdA3VMSffCarpcj3tLoFAkwZK-NqFXCwawi7wmboQBzEgjLt7yDD_NBUTexBhUggETYHD5E&gsessionid=AfjQhaiqyQtIRF0RYFzWSMNeAOR577VJUfEnBEMCCrPc5QIKMni8ug)  
  <sub>19 hours ago</sub>  
  SEC filings for November 16, 2026 including 10-K annual reports, 10-Q quarterly reports, 8-K material events, and Form 4 insider trades.
- [Ex-employee of HDB co-owned firm gets over 8 months' jail for taking $50k bribe, Singapore News](https://www.google.com/goto?url=CAESpQEBxCJF1_ZcHmcdBpg-MprQHPpte_en_95uQx0RcDUrYlEoGZxWk0C6Mx0g-_nb3c5mrOG-Tni5LaQGEjqA-7RbYuiXhpgIAn5uVzHMb7B-GTTA-7EPR8ggdeuoSK1CdALUied8gQCHT9TDzz_l17A2M2vrl5awOpTJxggcgO9lByZJx4Pwh8c3tFLKaTWFHdJSTlosi_Tl2Qs3F8jrYf9qOBQfvuk&gsessionid=AfjQhaiqyQtIRF0RYFzWSMNeAOR577VJUfEnBEMCCrPc5QIKMni8ug)  
  <sub>6 hours ago</sub>  
  SINGAPORE — An employee of a property maintenance company co-owned by HDB received a bribe of $50000 from the sole director of another firm.
- [Newborns among 140 evacuated after fire breaks out in Boon Keng HDB flat, Singapore News](https://www.google.com/goto?url=CAESfwHEIkXXyOL32Gh5xvgmOaFDO4ewyXY6ZxzDuE_bbQw1TWz36SJp0gfmEy_kysOqafldU5Sd6zBIqg9nWyXmXqLOCJv1TavhvEwRlAHU4p8Ol8TRlKlSqER_7sRabjBcbJgN7CTRb7qVWO11y6Cxzo3zZ1K21Fkk6l5szOopEww&gsessionid=AfjQhaiqyQtIRF0RYFzWSMNeAOR577VJUfEnBEMCCrPc5QIKMni8ug)  
  <sub>12 hours ago</sub>  
  Around 140 people, including two newborns, were evacuated from an HDB block in Boon Keng on Monday (Nov 16) after a fire broke out in a unit on the 23rd...
- [Woman, 18, jumps from Woodlands HDB ledge, Singapore News](https://www.google.com/goto?url=CAESgQEBxCJF16SLtT6OWbXRfvAKP0YZE37rJt9CtMYpVPzqaXbnTBM5MkdVJUn1HYqrZj0cJ1571lIBbcrcXZ4xto6JBywwvmqgJcQCS7azdQzdcorIzCV9UMtwsggo8af8MsU6Mwp9JuyNbnvKHmVgdt29bHvNxXL7gito3_GhoWin4yg&gsessionid=AfjQhaiqyQtIRF0RYFzWSMNeAOR577VJUfEnBEMCCrPc5QIKMni8ug)  
  <sub>10 hours ago</sub>  
  An 18-year-old woman was apprehended under the Mental Health (Care and Treatment) Act after jumping from the 16th-floor corridor ledge of an HDB block in...
- [An Binh Securities (ABS) recommends a portfolio of potential stocks for November, expecting the VN-Index to reach 1,870 points.](https://www.google.com/goto?url=CAESxgEBxCJF18P1EgER_bmyW2bidBrhm5i8rxM6xUxb7bVhzAlMGIyUgQcxNQevXybCMF8HXzbeN0Z8xaTxuseympx5nMv7lAGFz8cjIg5lhRet3-BAI8gRn_YKCjH3EInnJFbPCF1FcOlRRAECQVTEignFDgV8-Vw6piTw336K6wG4f1sKsZ-q-y4AFhABIA1-CExPRub21RqZMlFnHfw96bjjqYQNkL2RfLIn8cfBB7PVQ30SwJ02TpabGN8KJXzqMwSgI9xWklo&gsessionid=AfjQhaiqyQtIRF0RYFzWSMNeAOR577VJUfEnBEMCCrPc5QIKMni8ug)  
  <sub>12 hours ago</sub>  
  An Binh Securities Joint Stock Company (ABS)'s November 2026 strategic report noted that the market is showing many positive signs to enter a recovery phase...
- [Bedroom fire at Boon Keng Road HDB flat: One resident taken to hospital, 140 evacuated, including two newborns](https://www.google.com/goto?url=CAES2wEBxCJF1zMhSR94A2kephzLSn8DYQISkPBvzwPvkUg7JOvY2QphPOMSOkffUO88QmQwHUiAb2ANtGzw-OAVji2jIajM8cYF_aBB9L8zgoA-80BNAPKlkouwSoNqFp-OzjZ6pzCA0MlTQPvQXKxodojHqtohHRjSik4gwgWtZcD0XllguKvO-9Q-5qHs47DwqDfmkL09azk65mTW2H8O7dlweYmI8SRkQgAJkhLjQiXUKlXV-xsN6T3Duu_ntuF7elLspGV3GtY_H0UYYhV7W_AaMgsltfe8eGhcP7Y&gsessionid=AfjQhaiqyQtIRF0RYFzWSMNeAOR577VJUfEnBEMCCrPc5QIKMni8ug)  
  <sub>10 hours ago</sub>  
  A bedroom fire at an HDB flat in Boon Keng Road prompted the emergency evacuation of about 140 residents, with one occupant taken to hospital for smoke...
- [Daily roundup: Singaporeans invited to shape Long Island recreation and connectivity plans from January 2027 — and other top stories today](https://www.google.com/goto?url=CAESsQEBxCJF14ccbGvRjdR7_0-5NQV9MdDi-lppAwGQyZaoJhLU-186yva2qakURxzu_x-P7ySqo2fTCJIqq6vUqzmNNbZLRy44t3MSPKyX0xBJit-EO1qw97spSb2UerXm0-5EDMFkIeiyM7ILK-EpbXTut8ZejW751seivSFEMZSmberULf3BgzZHlJ4Eld1sn24yuYXuXDPWcwnMwzJBOj694mUAWfAs1Ze9EMRoO2uyZqc&gsessionid=AfjQhaiqyQtIRF0RYFzWSMNeAOR577VJUfEnBEMCCrPc5QIKMni8ug)  
  <sub>5 hours ago</sub>  
  Stay in the know with a recap of our top stories today.1. Singaporeans invited to shape Long Island recreation and connectivity plans from January...
- [HDFC Bank stock: Board reappoints executive director](https://www.google.com/goto?url=CAESrwEBxCJF19IkBI24_OKpwmx4v9pJ6HIctindF-x_MtwTM1rZqg5_d-8YBZ4fsFT7RBh6EiKgxn51waqGe7wfZP8eN38BY_aGbZtBbuNIlC1f_J9Zm5U1Uib6ectntFcRT9nxyDgNSPDCmvwe9G13SQQbVOqzrLTAboB2Vz3CKcRBnJWVYFtUNZ1EFCPlL_jefBk8kQcuN8xLPpUsXTrlm1sPe2hUhHi2JD_HeZ4XWWxA&gsessionid=AfjQhaiqyQtIRF0RYFzWSMNeAOR577VJUfEnBEMCCrPc5QIKMni8ug)  
  <sub>11 minutes ago</sub>  
  HDFC Bank stock enters a new leadership phase after the board approved V. Srinivasa Rangan for another year. Shareholder ratification is next.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 26.39 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 23.89 (+10.5%), 50d 23.19 (+13.8%), 200d 25.37 (+4.0%); 50d below 200d
Momentum: RSI(14) 74.0 | MACD 0.972 vs signal 0.681 (histogram 0.290)
Returns: 1d +0.4% | 5d +1.6% | 1m +14.3% | 3m +13.9%
52-week range: 21.36 - 37.13 (now 31.9% of the way up)
Volatility: ATR(14) 0.57 (2.2% of price) | annualised 20d 29.2%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 135.75B
Valuation: trailing P/E 17.03 | forward P/E 19.06 | P/B 10.51 | PEG n/a
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
Price target: mean 30.30 (+14.8% vs last close), range 26.20 - 33.00
Recent rating changes:
  - 2024-07-22 JP Morgan: down, Overweight -> Neutral
  - 2019-09-09 Bernstein: down, Outperform -> Market Perform
  - 2019-06-11 Nomura: down, Buy -> Neutral
  - 2017-03-21 Morgan Stanley: down, Overweight -> Equal-Weight
  - 2016-09-14 Goldman Sachs: main, ? -> Buy
  - 2015-03-11 Societe Generale: init, ? -> Buy
Institutional ownership: 14.2%
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

### JPMorgan Chase (JPM) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Bank of America vs. JPMorgan Chase: Which Financial Stock Is a Better Buy for 2027?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc679bd7f741a3838d69e5849853bf&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2fbank-america-vs-jpmorgan-chase-132902173.html&c=17409191605277849506&mkt=en-us)  
  <sub>Yahoo Finance, 9h ago</sub>  
  Bank of America trades at 1.1 times book value versus JPMorgan's 2.5, but JPMorgan's scale and net margin may justify the premium for some investors.
- [JPMorgan Chase CFO to Step Down](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc679bd7f741a3838d69e5849853bf&url=https%3a%2f%2fwww.wsj.com%2flivecoverage%2fnvidia-earnings-stock-market-news-11-17-2026%2fcard%2fjpmorgan-chase-cfo-to-step-down-HOS55F4XmSZnlidt5ibf&c=4980107190032714476&mkt=en-us)  
  <sub>The Wall Street Journal, 23h ago</sub>  
  JPMorgan Chase's finance chief is stepping down. The nation's largest bank said that Jeremy Barnum, CFO since 2021, informed the company he intended to conclude his tenure. Barnum has been a prominent ...
- [Dow, S&P 500, Nasdaq Futures Mixed Ahead Of Much-Anticipated Nvidia Earnings, Anthropic IPO: SLS, BABA, JPM, OMER In Focus](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc679bd7f741a3838d69e5849853bf&url=https%3a%2f%2fstocktwits.com%2fnews-articles%2fmarkets%2fequity%2fdow-s-and-p-500-nasdaq-futures-mixed-ahead-of-much-anticipated-nvidia-earnings-anthropic-ipo-sls-baba-jpm-omer-in-focus%2fcNba1SfR9gr&c=7501602095876659429&mkt=en-us)  
  <sub>Stocktwits, 19h ago</sub>  
  Anthropic’s public listing, expected on Wednesday, could top $1.4 trillion in valuation, stoking a key test for Wall Street's AI appetite.
- [JPMorgan Chase names Bregje de Best as next CFO](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc679bd7f741a3838d69e5849853bf&url=https%3a%2f%2fcryptobriefing.com%2fjpmorgan-chase-and-co-executive-change-cfo-succession-2026-11%2f&c=12578733038299374466&mkt=en-us)  
  <sub>Crypto Briefing, 9h ago</sub>  
  Bregje de Best will succeed Jeremy Barnum as CFO after Q1 2027 reporting in a JPMorgan Chase & Co executive change at JPMorgan Chase & Co ...
- [JPMorgan Chase: Software Bug Impacting Transactions](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc679bd7f741a3838d69e5849853bf&url=https%3a%2f%2fwww.wsj.com%2flivecoverage%2fstock-market-today-dow-sp-500-nasdaq-11-16-2026%2fcard%2fjpmorgan-chase-software-bug-impacting-transactions-KQ3fRmz4LE7KRBr0CPNq&c=267037276112986742&mkt=en-us)  
  <sub>The Wall Street Journal, 21h ago</sub>  
  JPMorgan Chase said a software bug was disrupting transactions, but customers still have access to their accounts and funds. “JPMorganChase has e ...
- [JPMorgan Chase says temporary software bug is affecting consumer banking](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc679bd7f741a3838d69e5849853bf&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2fmarkets%2fjpmorgan-chase-says-temporary-software-bug-is-affecting-consumer-banking%2far-AA2hzxgz&c=459743143069352142&mkt=en-us)  
  <sub>CNBC on MSN, 24h ago</sub>  
  CNBC's Eamon Javers reported there was no indication of bad actors involved and likewise no indication that a bug was impacting multiple banks at the same time.
- [No indication bad actors are involved with JPMorgan Chase technical issue](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc679bd7f741a3838d69e5849853bf&url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fno-indication-bad-actors-are-involved-with-jpmorgan-chase-technical-issue%2fvi-AA2hzg8w&c=3662328553338683845&mkt=en-us)  
  <sub>CNBC on MSN, 25h ago</sub>  
  CNBC's Eamon Javers joins 'Closing Bell Overtime' with the latest on reported outages at major banks including JPMorgan Chase and Bank of America.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 334.11 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 339.22 (-1.5%), 50d 339.63 (-1.6%), 200d 325.15 (+2.8%); 50d above 200d
Momentum: RSI(14) 45.0 | MACD 0.390 vs signal 0.528 (histogram -0.138)
Returns: 1d -1.2% | 5d -2.3% | 1m +0.2% | 3m -6.5%
52-week range: 282.84 - 365.18 (now 62.3% of the way up)
Volatility: ATR(14) 7.20 (2.2% of price) | annualised 20d 28.2%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 887.28B
Valuation: trailing P/E 14.01 | forward P/E 13.07 | P/B 2.53 | PEG 1.47
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
Price target: mean 373.48 (+11.8% vs last close), range 312.00 - 425.00
Recent rating changes:
  - 2026-11-02 UBS: main, Buy -> Buy
  - 2026-10-15 Citigroup: main, Neutral -> Neutral
  - 2026-10-14 Truist Securities: main, Hold -> Hold
  - 2026-10-14 Barclays: main, Overweight -> Overweight
  - 2026-10-14 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-14 Morgan Stanley: main, Equal-Weight -> Equal-Weight
Institutional ownership: 75.3%
Largest holders: Blackrock Inc. (7.7%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.7%), Vanguard Portfolio Management LLC (2.7%), Bank of America Corporation (2.6%)
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

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Was Eli Lilly Stock’s 45% Run Visible Early?](https://www.trefis.com/stock/lly/articles/625554/was-eli-lilly-stocks-45-run-visible-early/2026-11-17)  
  <sub>6 hours ago</sub>  
  For questions about this article or underlying research, email help@trefis.com.Eli Lilly (LLY) stock returned 45.3% in the six months from May 18 to...
- [Eli Lilly is trouncing Nvidia — and the weight-loss drug trade is beating AI again](https://finance.yahoo.com/markets/article/eli-lilly-is-trouncing-nvidia--and-the-weight-loss-drug-trade-is-beating-ai-again-170530198.html)  
  <sub>22 hours ago</sub>  
  Since its Oct. 6 record, Nvidia has shed more than $1.7 trillion in market value. Eli Lilly has added more than $250 billion over the same stretch,...
- [A $1.5 Billion Reason Why Eli Lilly Stock Is in Focus](https://www.google.com/goto?url=CAESnQEBxCJF12V5wpo3qZNTaXYqKcxmXOwzxJZREJSCn0ra6cXsvQs2kgzx9WuxTWxOzMkZT11gakrvOeJaPQ-wyuU68bhT44YZaWxX-RtnwTCt15h0GCerhan4FyqM1I9asl_qjfLRZ-Ind7OFyMPSPykMd54ZiHxrH84R81Pm5o1ChNUVon-AzT2WvNLWEiferUAlKQanFlNrHxY7WfDy&gsessionid=TE-gD72cJksDvOYIXTBM9idVShwwRF0O99VAi2bQR5VmrRof5VR97g)  
  <sub>1 hour ago</sub>  
  Eli Lilly announces $1.5 billion deal to acquire Calytrix Bio. Here's what the transaction really means for LLY shares.
- [LLY Nov 2026 1370.000 call (LLY261120C01370000) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXYlc-afv73Jk6k7XkZhHYxwPH3Hcm3K9xhmoborzS64DWouLM9VH3hzj_fMwV_g_Y5Lu77iPak5ege6MQx5fTZoOpI1Q3Xf0YCz2XruBc51Jp34EwXTstvhci0bNYOEWidQCW7dADXi-OSYIbOKNQtgfScxw&gsessionid=TE-gD72cJksDvOYIXTBM9idVShwwRF0O99VAi2bQR5VmrRof5VR97g)  
  <sub>17 hours ago</sub>  
  Interactive chart for LLY Nov 2026 1370.000 call (LLY261120C01370000) – analyse all of the data with a huge range of indicators.
- [LLY Dec 2026 1340.000 call (LLY261211C01340000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXq8ZIbm1iThUvCRh3l_4HUits5wU7_TGMShMnV91hl8AojZcEDzN8KGgUGIBwxPVLPT4mTN1he34HbaXBxy8VnDVyBSMed0VE4JnSonFjBr8xsBSau2S9rRPGXXFg-9pt1zU3uYPZaymeDeVB_xI&gsessionid=TE-gD72cJksDvOYIXTBM9idVShwwRF0O99VAi2bQR5VmrRof5VR97g)  
  <sub>18 hours ago</sub>  
  Find the latest LLY Dec 2026 1340.000 call (LLY261211C01340000) stock quote, history, news and other vital information to help you with your stock trading...
- [Eli Lilly & Co (LLY) Receives a Buy from Barclays](https://www.google.com/goto?url=CAESvwEBxCJF1-VB1M9kBJ2h2qmwMziKc-LksxNtLRvEYLDvzWVa1kVNQEkH2zmnwXXJA4Rusynw2eIcNyKXgrh6UWPZtV6-9dBnEfY5_uViNr7JHQBQW_DliFtBBJu169hn1Wq4cJQQRPJOxpTqU6l3ua2uGMjOzL7PAjZ6Xz4FVRRJ7P7eIqm4frhHqYsgetSF3xFKsCReY1nLXI6zJRKdYBd52tZS0quxeMQQl5-m7NErs6QWrzWTr_cQt9WKcYyDHg&gsessionid=TE-gD72cJksDvOYIXTBM9idVShwwRF0O99VAi2bQR5VmrRof5VR97g)  
  <sub>5 hours ago</sub>  
  Detailed price information for Eli Lilly and Company (LLY-N) from The Globe and Mail including charting and trades.
- [LLY Nov 2026 2080.000 call (LLY261127C02080000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXauXlY-4r3vd7JC-BV4S0ABT03_9ih1gA05JttxkGAzmQU7WZRVfIBJOZJq08CMUhBdl2fLhlYllQ_fE_0ZDmcmfypXi5BOgRzY1yClnp6GPZePycTMaXTZ9D4HaUF4bQVJmJOuy91Jp3e1Lj4wQ&gsessionid=TE-gD72cJksDvOYIXTBM9idVShwwRF0O99VAi2bQR5VmrRof5VR97g)  
  <sub>18 hours ago</sub>  
  Find the latest LLY Nov 2026 2080.000 call (LLY261127C02080000) stock quote, history, news and other vital information to help you with your stock trading...
- [LLY Nov 2026 1375.000 call (LLY261120C01375000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXX5FyO3hycwoAEz4DXdvH7ns0FqctbiVyP0msOexCqeKSzSsvsfv_9mPyrKwN6ibLkvz-jUbztpSmbv0rl2W-reYL1eig6tG8yc26LqwnoPAXFKj63Ip0Jkp0yKOXR_XxoAYc22l71pccXIjuBkxU&gsessionid=TE-gD72cJksDvOYIXTBM9idVShwwRF0O99VAi2bQR5VmrRof5VR97g)  
  <sub>19 hours ago</sub>  
  Find the latest LLY Nov 2026 1375.000 call (LLY261120C01375000) stock quote, history, news and other vital information to help you with your stock trading...
- [LLY Nov 2026 1420.000 put (LLY261120P01420000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXpTsNwWZ_9BoGg47gjp_huE8aQX1w9nRRVVCoDBQfEjZuWpHY7D_Q11d5Z7nSBZrodSjL1MQCtE1La9Us1YuIQ0d_ldT8Aup522N4C94DlSM8lf200zrvQBOE2EXzFzEel8ZNLMBdWpkVBm2720g&gsessionid=TE-gD72cJksDvOYIXTBM9idVShwwRF0O99VAi2bQR5VmrRof5VR97g)  
  <sub>19 hours ago</sub>  
  Find the latest LLY Nov 2026 1420.000 put (LLY261120P01420000) stock quote, history, news and other vital information to help you with your stock trading...
- [LLY Nov 2026 1285.000 put (LLY261120P01285000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXCVLvBbWzgqQXCux2Rv2HLO_aUS1EwkNJFwAw9GX41GbvrnOi1xmL7rKqEmO7CH5cR37j4tUMvRwnPuVn1pb-VxmyeBB8Lqau4mwJtZs9bx1gqq-cWUp91JSzexTeDq90665POLMvCzwVJIJ-P_8&gsessionid=TE-gD72cJksDvOYIXTBM9idVShwwRF0O99VAi2bQR5VmrRof5VR97g)  
  <sub>19 hours ago</sub>  
  Find the latest LLY Nov 2026 1285.000 put (LLY261120P01285000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,425.68 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 1,372.91 (+3.8%), 50d 1,252.76 (+13.8%), 200d 1,113.20 (+28.1%); 50d above 200d
Momentum: RSI(14) 65.4 | MACD 53.614 vs signal 54.026 (histogram -0.412)
Returns: 1d -0.4% | 5d -0.5% | 1m +14.9% | 3m +11.4%
52-week range: 851.21 - 1,443.50 (now 97.0% of the way up)
Volatility: ATR(14) 42.96 (3.0% of price) | annualised 20d 36.9%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.27T
Valuation: trailing P/E 46.26 | forward P/E 28.06 | P/B 31.54 | PEG 1.33
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
Price target: mean 1,468.57 (+3.0% vs last close), range 940.00 - 1,700.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 38,018 shares in 36 transaction(s) | sold 313,215 shares in 9
Net: -275,197 shares (-13.7% of insider holdings) | insiders hold 1,728,045 shares
Distinct insiders: 0 buying, 4 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-11-02 HAKIM ANAT (General Counsel): 5,000 shares, 7.01M
  - 2026-08-17 JONSSON PATRIK (Officer): 6,500 shares, 7.64M
  - 2026-08-10 ZAKROWSKI DONALD A (Officer): 2,000 shares, 2.37M
  - 2026-08-07 HAKIM ANAT (General Counsel): 5,000 shares, 5.95M
(32 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

- [MercadoLibre, Inc. (MELI) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/MELI/latest-news/)  
  <sub>13 hours ago</sub>  
  Nu Holdings Slides After Brazil's Election: Is the Sell-Off Overdone? Zacks •...
- [Michael Burry Buys More Of Adobe And MercadoLibre; Exits ORCL, CAT Puts](https://finance.yahoo.com/markets/stocks/articles/michael-burry-buys-more-adobe-224400666.html)  
  <sub>16 hours ago</sub>  
  Burry continues to hold a large put position in the VanEck Semiconductor ETF, along with puts on the Nasdaq 100, Nvidia, MetLife, and Palantir.
- [MercadoLibre, Inc. (MELI) latest stock news and headlines – Yahoo Finance](https://www.google.com/goto?url=CAESagHEIkXXdkmgJ52Zqdg2yosC43T-jRsogCjFGguwGqR0zb1tQLSmXGB4LxUqIoXyMjRSQcdYiPtylRiYB_Am8UUJGdUHYcsZZJMY9PwS8cArF3kv1V9mFSu7ABnI6FPfjhhooSNuR3mAdg4&gsessionid=h0EvKknLVFhop8or48zlgnjYkZxvuXxjLKX_BES8Zuwl8zJmiuXTnQ)  
  <sub>23 hours ago</sub>  
  MercadoLibre, Inc. (MELI).
- [MELI Mar 2027 1950.000 put (MELI270319P01950000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESdAHEIkXXSEYvd0iEzRrB0ANdRlJ1gczbEQZK52sNVVZp1b7rcAPw8Mw2hG_0R2j3vZJBeIdEsT7BAobqNFE0dCWy9w11N9AdPjyX__WRaj4rDh2gJe6tIZdabVWQnOYaRzxie8JXQl8KGuuxmr6qC909--gD&gsessionid=h0EvKknLVFhop8or48zlgnjYkZxvuXxjLKX_BES8Zuwl8zJmiuXTnQ)  
  <sub>15 hours ago</sub>  
  Find the latest MELI Mar 2027 1950.000 put (MELI270319P01950000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI261204C01780000 Interactive Stock Chart | MELI Dec 2026 1780.000 call Stock](https://www.google.com/goto?url=CAEScAHEIkXXdh6wR0M2sgprhqLld7_QdJZ6VizARiF_7l9vPAOMx-N41DbtOfsmZONQdPRAZ_8IqcoEzYfonYoZ6vLh5gogP9MrMmoUR4S4SLdNBFwSbdfeeDBlqDN-16XwDHdGXwxJNSZRGSeGyw-O920&gsessionid=h0EvKknLVFhop8or48zlgnjYkZxvuXxjLKX_BES8Zuwl8zJmiuXTnQ)  
  <sub>20 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [MELI Dec 2026 2050.000 call (MELI261211C02050000) interactive stock chart](https://www.google.com/goto?url=CAESegHEIkXXs166bcpOAoOFMqqOl5mxZ8_h4PQrwTbncPuOJIUB8TksmoxquTduxoTqzu4uf4LkyVIYiqXAm-krBVQ9F-Sjl_CtDvJOUYLtGD_f_XUy4ZTDUJH_VW5TS7cqtJ2fHMLvRAbS_7wqZo7s9KNlHGhkN_zAKmOO&gsessionid=h0EvKknLVFhop8or48zlgnjYkZxvuXxjLKX_BES8Zuwl8zJmiuXTnQ)  
  <sub>14 hours ago</sub>  
  Interactive chart for MELI Dec 2026 2050.000 call (MELI261211C02050000) – analyse all of the data with a huge range of indicators.
- [MELI Nov 2026 1950.000 call (MELI261120C01950000) interactive stock chart](https://www.google.com/goto?url=CAESegHEIkXX0A4FSIsDRBPMeBnvONhusg75RxJ5DA0jCuqEy1IjHEYdDOKFV1qsYpJfpvUEqE0Og_ihJYeS508BwS31iUu41AVB00N3t_T88vETBZduxvLhrHPx4dpyuazgcIzQzxT127ptPLv5H_hhuqIrks8HBwSg-rm0&gsessionid=h0EvKknLVFhop8or48zlgnjYkZxvuXxjLKX_BES8Zuwl8zJmiuXTnQ)  
  <sub>15 hours ago</sub>  
  Interactive chart for MELI Nov 2026 1950.000 call (MELI261120C01950000) – analyse all of the data with a huge range of indicators.
- [MELI Dec 2026 1560.000 put (MELI261204P01560000) interactive stock chart](https://www.google.com/goto?url=CAESegHEIkXXTsh5bN0G5iVCZ4NO17cnZgQRnkuYx9P1resA2Ao9SNIpHl82vkwBKWy4dlx6szLw6UxgIqVJGV0KY3EmmcGpw8Dg5M_KlxGvWJpEIO0yK31LvCnhica8juLod2u6mcnJkdZ6H4kb5BjlaQT6EW0brOx5Di4K&gsessionid=h0EvKknLVFhop8or48zlgnjYkZxvuXxjLKX_BES8Zuwl8zJmiuXTnQ)  
  <sub>17 hours ago</sub>  
  Interactive chart for MELI Dec 2026 1560.000 put (MELI261204P01560000) – analyse all of the data with a huge range of indicators.
- [MercadoLibre, Inc. (MELI34.SA) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESagHEIkXXAndb6X9OtZzYwIg99qtwaadRVbNrbKsAfHg1qo9YUnneLvJf0KhY6Xiwej2bBpRS26vi0WE87Fkv9MjV9hxntrYD2xo8PnsXDOnsBNlv_nXrRcolUuB5QfJzk1jgSputdzWJMjc&gsessionid=h0EvKknLVFhop8or48zlgnjYkZxvuXxjLKX_BES8Zuwl8zJmiuXTnQ)  
  <sub>23 hours ago</sub>  
  Find the latest MercadoLibre, Inc. (MELI34.SA) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [MELI261120P02460000 Interactive Stock Chart | MELI Nov 2026 2460.000 put Stock - Yahoo Finance](https://www.google.com/goto?url=CAEScwHEIkXX-tjBlzl_s27hHxe5UAZYkkYoSjKVk9E33s3b8PPhncvUtw2FmGjngsUWLWe-EEdgC539rRliU_TecvPCI_cTALEoKWxcaRvl_49RG9vGwSLjJg9ovU63_kkcbwL7F7WTRyJ0aoVuyL-bayfVY3c&gsessionid=h0EvKknLVFhop8or48zlgnjYkZxvuXxjLKX_BES8Zuwl8zJmiuXTnQ)  
  <sub>10 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,455.00 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 1,616.74 (-10.0%), 50d 1,741.05 (-16.4%), 200d 1,776.78 (-18.1%); 50d below 200d
Momentum: RSI(14) 31.3 | MACD -89.212 vs signal -75.917 (histogram -13.295)
Returns: 1d -0.5% | 5d -2.4% | 1m -20.9% | 3m -23.8%
52-week range: 1,455.00 - 2,295.00 (now 0.0% of the way up)
Volatility: ATR(14) 61.10 (4.2% of price) | annualised 20d 57.1%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 73.76B
Valuation: trailing P/E 39.03 | forward P/E 26.73 | P/B 9.00 | PEG 0.81
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
Price target: mean 2,194.30 (+50.8% vs last close), range 1,600.00 - 2,800.00
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

### Microsoft (MSFT) · Company — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Microsoft (MSFT) is One of Our Top Picks That Evolved Successfully After Its Founder Transition](https://finance.yahoo.com/markets/stocks/articles/microsoft-msft-one-top-picks-134716523.html)  
  <sub>Yahoo Finance, 53 minutes ago</sub>  
  We just published a list of 10 Stocks that Have Survived Major Founder Transitions, and Microsoft Corp. (NASDAQ:MSFT) ranked 10th on this list.
- [Quant ratings on Bill Ackman’s Pershing Square Q3 holdings: AMZN, MSFT, META, MA, V](https://seekingalpha.com/news/4673462-quant-ratings-on-bill-ackmans-pershing-square-q3-holdings-amzn-msft-meta-ma-v)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Pershing Square Capital Management (PS), the fund run by billionaire hedge fund manager Bill Ackman, revealed its Q3 holdings for 2026 in its latest Form...
- [MSFT shares remain in contained range as momentum indicators send conflicting cues: weekly analysis](https://www.google.com/goto?url=CAESlAEBxCJF12rZQnSlRMfzPruELgrl7uXU3HdfgI2bSbNtZxTjHsThEWZJrMx7DJkzrJ6U4ds7nR9XaEfdCmabAndj9ueJoK6crOdEvXcTvFrm08S36b3fdOgX4faIsT3QNfufyRaX_XPx_KCO9S4VDjHgToY0I6s4Pyq5_GYNYscpU2o0To1CIxt0dVzcXlsungJGxPtQ&gsessionid=X-WBQnO_sf2R80VGJO52ezabOOcGxF9J04MlPIIhbOeJQh3JIPDdiw)  
  <sub>Traders Union, 38 minutes ago</sub>  
  Shares of Microsoft Corporation (MSFT) are trading near $518 after slipping more than 1% over the past week as momentum shows signs of stalling below...
- [Microsoft (MSFT) Is One of NVIDIA’s Biggest Customers, and a Growing Rival](https://www.google.com/goto?url=CAESnwEBxCJF1zCQX9GO_LUnqLefgEWiy79OgUmuFO0n1qvWIQKTcCO_tzWMUXBqZst__LlMpM6djiVhEZ1PKPXxmNkI44H1RsJ5YRpFTYPvfBK78VZsIDxlGBpX6IiNNhd8ohlqYy2230ZgYHjGF6-khHdxLspAdLSFT82XE1jPG4GDxNfzrv5axNHANuEaBUkE7AZ91nI0TP5NA9MDoQbtZyI&gsessionid=X-WBQnO_sf2R80VGJO52ezabOOcGxF9J04MlPIIhbOeJQh3JIPDdiw)  
  <sub>Yahoo Finance, 17 hours ago</sub>  
  We just published our list of the 10 Stocks to Buy Following Jensen Huang's Departure, and Microsoft Corporation (NASDAQ:MSFT) rounds it out at number 10.
- [Is Cerebras Stock Still a Buy After Its Microsoft Deal?](https://www.google.com/goto?url=CAESywEBxCJF15m6rJtMZGWRxlN6RcOqIlrSlxDqEO2LrjbzTa_kLp0FxK18mLeHQAPSGMsIKwUNFF5Rsj475KpjapCFSXaXH0t0BFSeBg3aDxtzvZbP19zKks6_NIxDIN1JQj6EvpmK-z-iv5wydE4_A6yBCyGAmBsU2w-6FmBX3dEfMXPKINDCVeEosWk_532J7NkXqqyCn8w8QAIxGvLahwne8X3GsChP_yDRjvvtuZZKfyZZKAZEYPoyJK-t4F0mIu2KfW-eXuaKlRR0bA&gsessionid=X-WBQnO_sf2R80VGJO52ezabOOcGxF9J04MlPIIhbOeJQh3JIPDdiw)  
  <sub>The Globe and Mail, 6 hours ago</sub>  
  Detailed price information for Microsoft Corp (MSFT-Q) from The Globe and Mail including charting and trades.
- [Microsoft's (NASDAQ: MSFT) $677 Billion Backlog Makes The Case For A 24.6% Rally Despite Anthropic Pressure](https://www.google.com/goto?url=CAES1AEBxCJF1_mtncjj_JvZRVmyUCK9YxBM6lqhJQKVysS2RbSP7y2LOruVSh26_wQ9OVnGwCcQ37epbXIJFPTttAvReDmy9JRETT-ciWhzt-AvFcP0_iegMAs1mk-LIsHQ_40B0hfsQkgzePq5K6ljLWw2D9H0OPL728UxeRSVc0840YqkahVBLmT7lZ3GwmIvMzgYA1yi0RAZvMWe_tv3cH1ZfuHsZ8TyOxgGPb9Ubjulcl678EnTa7IekaIGU9hLt7xGlxfjMl6jOWeguxb8zY4TrZpXLQ&gsessionid=X-WBQnO_sf2R80VGJO52ezabOOcGxF9J04MlPIIhbOeJQh3JIPDdiw)  
  <sub>Foreign Policy Journal, 15 hours ago</sub>  
  A signed commercial backlog of $677 billion gives Microsoft (NASDAQ: MSFT) a visibility advantage that the market appears to be discounting as competitive.
- [Microsoft Stocks Move Lower as $1 Billion Anthropic Bet Precedes Ignite](https://www.google.com/goto?url=CAESwAEBxCJF13cdMTNLDxbk7VHUEdfzQxad566C-UkoU72zgAiDTaHr5bYJLfdQw4xNeIlseVsBhP4zRk51wBXRz8i7aV8jwFABBFvJ59EtVY0zXBJrEKG9Dh0jddYnjKiRq5-5fowU4yKsM5ysH0fAkXFr712mt_n-ynuc7pMeDbfRx6yjiDjoNuCb1RT6SpKErg30p2PRtH4044LGDHx0P6LYo7596mAEcGbMy6ZihO8OQ-kC7o6YW1pu1dHzIGw4TII&gsessionid=X-WBQnO_sf2R80VGJO52ezabOOcGxF9J04MlPIIhbOeJQh3JIPDdiw)  
  <sub>TradingView, 19 hours ago</sub>  
  Microsoft NASDAQ:MSFT shares moved 0.41% lower to $521.71 at 9:40 a.m. ET on November 16 in regular trading, outperforming a weak chip complex.
- [Microsoft's Outage Barely Moved Its Stock, But a Bigger Risk May Be Building](https://www.google.com/goto?url=CAESrAEBxCJF1xDbF_Ie-OdkHnWNeVp4K9uqn4EqEBwfAtcWGlRjYKGyYpZ52XWApHXMLBMIKtCHwLWRs8GOE1g5vbFruWfzjVYn0QzxZTd3HHvJXRE7zwbqMnvn-jXmfv1rGuEr8cpGSBVFCvsjqwAPM0BbKHnYn0vL8iH6lqeM_Rtlt0ze-lFrkucSd-PhN2Rg9xTwxvZFYtHyCVG3j0Y_1PYN9jMQpvaLs_Sc-gma&gsessionid=X-WBQnO_sf2R80VGJO52ezabOOcGxF9J04MlPIIhbOeJQh3JIPDdiw)  
  <sub>MarketBeat, 1 hour ago</sub>  
  A two-day Outlook and Teams outage left MSFT stock largely unscathed, but it could pressure Microsoft's enterprise pricing power and Copilot adoption ahead...
- [Microsoft (MSFT) Stock Looks Like A Bargain On Its 60% 5 Year Run](https://www.google.com/goto?url=CAESvgEBxCJF1xO-WJQD3J4T0qh4xQrKCauhCTaECM0pUV1byzJkzmmdYmctyyrWAbgyrk_UIL2cu67dN7wEVY5fXRkSzkZHd9QJiZgcA6VaxGnHSvzgp-ccXhS6eBgn6Un2KrfsObdZljRmQS35BA4lkao_q7a5NhFpeHPB8QfkmWWrgsdw6dK5Yi9qgcZfLUJhVs7EHlnWZJHxtc243y39whIsgc6gxumJlGHhtq95aui9n3ZUblq06HFGDQdNozIU&gsessionid=X-WBQnO_sf2R80VGJO52ezabOOcGxF9J04MlPIIhbOeJQh3JIPDdiw)  
  <sub>Simply Wall St, 22 hours ago</sub>  
  Microsoft shares closed at US$523.88, and after a 60.3% gain over the past 5 years, the live question for investors is whether that price can be supported...
- [PRGS or MSFT: Which Is the Better Value Stock Right Now?](https://www.google.com/goto?url=CAESmgEBxCJF18NzSXChdyfnrtlVGPG_-sQCRbs10o51j-GCzAnA6uIdsC17qrm1gbcr-0d3LpCyeH10Ws48Z4ygE27MxAYJSe5_FzfN1-BgvhOh2rEuCx7Vct8NMTZUjE2TZ0xBXVwpLooPzustfJGsF6nV8f8m4GKQL1rWw8QGBNeo-Wykawd02L2pN2mVmgm8aTV5xemPZCH7lr8e&gsessionid=X-WBQnO_sf2R80VGJO52ezabOOcGxF9J04MlPIIhbOeJQh3JIPDdiw)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  Investors interested in stocks from the Computer - Software sector have probably already heard of Progress Software (PRGS) and Microsoft (MSFT).

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 512.01 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 527.62 (-3.0%), 50d 519.72 (-1.5%), 200d 442.30 (+15.8%); 50d above 200d
Momentum: RSI(14) 44.0 | MACD -0.282 vs signal 2.564 (histogram -2.846)
Returns: 1d -1.2% | 5d -4.0% | 1m -4.0% | 3m +5.7%
52-week range: 352.83 - 555.80 (now 78.4% of the way up)
Volatility: ATR(14) 14.34 (2.8% of price) | annualised 20d 37.1%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.80T
Valuation: trailing P/E 26.72 | forward P/E 21.16 | P/B 8.08 | PEG 1.55
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
Price target: mean 636.12 (+24.2% vs last close), range 440.00 - 870.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

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

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Nvidia (NVDA) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [NVIDIA Corporation (NVDA) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/NVDA/)  
  <sub>9 hours ago</sub>  
  NVIDIA Corporation (NVDA) · -12.61% · -27.08% · -30.70% · -16.28% · -17.89% · 416.97% · 356,791.43%. Key Events. Baseline. Advanced Chart. Loading...
- [Should Nvidia bring Jensen Huang back, as Silicon Valley's elite are demanding?](https://finance.yahoo.com/technology/article/should-nvidia-bring-jensen-huang-back-as-silicon-valleys-elite-are-demanding-200000408.html)  
  <sub>5 hours ago</sub>  
  Something pretty remarkable is happening in Silicon Valley right now. One shouldn't be surprised, considering the profit motives of many invested in the AI...
- [Prediction: The Stock Market Will Make a Big Move on Nov. 18 (Hint: Nvidia Will Be the Catalyst)](https://www.google.com/goto?url=CAESngEBxCJF10Bc1Pmg7R8gd_dX98B7u8-LfX55huEqXM5cZuL-JJy8fDBxKab4kYPUNokYibuAvD-d1XtV3TzVVPVC4PkzXG6HD9XWt-PNDW-MacwyQDDdvKQ4bTAUk-UIaIXH3pEFfQqczMcKX9kY3NkXgVV1ZZ77zZ6D-a8RENgbPVgyq23CnOQHMnhzTnEohMr0T68E1JDSvuac-Ekjrw&gsessionid=MD_NkK9gBUmtHsep7W9lvlxWM1JzsQo2fPcQ1ctaQFXIF94LrZavHQ)  
  <sub>5 hours ago</sub>  
  Nvidia (NASDAQ:NVDA) has been one of the market's most influential companies during the artificial intelligence boom, but the stock has struggled in 2026.
- [Jim Simons’ Firm Sold 7 Million Nvidia Shares Before the Fall. A 67-Year-Old Holding 4,900 Has Until Tonight](https://www.google.com/goto?url=CAESlAEBxCJF19zL8CcOXJSmUyMbOzxrR_Y_UFru4Z6dHi7Bon12MMmSrxG3pihnBT3Fe5cYTs3t3K9tgEBXNj5xMeDEqb9ZD1NMuuH2feJMWfri8MrVmmW8aAI7J5NdimN5TijDny4nWEZu7SFP4IM1saj6k42VV0YLvY1muEZq4CQ_lS-z2SwhtBGl3NEBkYrFCAnwU9Ya&gsessionid=MD_NkK9gBUmtHsep7W9lvlxWM1JzsQo2fPcQ1ctaQFXIF94LrZavHQ)  
  <sub>4 hours ago</sub>  
  Renaissance Technologies cut its Nvidia stake from 7091256 shares on June 30 to 23170 on Sept. 30, its filings show. For a 67-year-old with $761656 in...
- [Nvidia Stock Fell Below $170. Here’s Why It Could Be a Screaming Buy.](https://www.google.com/goto?url=CAESmQEBxCJF120PMzJAKvMXCS2ffSwkQP6kqrmzhoBbsjomyexYMJXAYpfpP60Ys2v-2za67u6W-E-29B293mYEiFDYOE_hZdzjKHlOAEV_vOahaVJGdDl8jJ3HEtQp1lTgV7ZHdo5syeB8H9q9IEbk4DronbWEbeAO-s-2yjixmBFj-Qq1T2tT91K2zn78J-nRev9GmkrIcgU_UQc&gsessionid=MD_NkK9gBUmtHsep7W9lvlxWM1JzsQo2fPcQ1ctaQFXIF94LrZavHQ)  
  <sub>5 hours ago</sub>  
  The bigger they are, the harder they fall. That adage is playing out before investors' eyes with Nvidia (NASDAQ:NVDA). Throughout most of the past year,...
- [Nvidia stock valuation looks 'draconian,' even without Jensen Huang: Analyst](https://www.google.com/goto?url=CAESxgEBxCJF12tC5QUp1d_Np3ZzHju-ns4j92s8JJfPUKXiCwShRbdQZMDJ2tfWfd5vwPAWWHP40tCmbEQsa1MdCypKkbA-j5aW7yqL8fk0dy-TKfdXFYQ0sYLufrvtDG_BIKys3UXxpGONsGWMkLq2ldKySm3qecnVLnCz1OhPrT_oHRyiiXkagwVcs3zxiHwscA8122iBCWg5l_mbKt0OL3FqVFUZ2VJDCAqH9235KbGyuPi5C19vFA5HXJyjTJu7L81tG3xr6gA&gsessionid=MD_NkK9gBUmtHsep7W9lvlxWM1JzsQo2fPcQ1ctaQFXIF94LrZavHQ)  
  <sub>5 hours ago</sub>  
  When the forward price-to-earnings ratio on Nvidia (NVDA) is six points below that of slow-growing, struggling food giant PepsiCo (PEP) — as is currently...
- [Nvidia to report Q3 earnings amid Huang scandal](https://www.google.com/goto?url=CAESqAEBxCJF12bTodpEVycelS0RRWbbo3ydP_4VARUF1-AFUA7yqGx8Ir7wzoes8GFQXmuQ98dRaXzGvaQ1jr4swyAk78u4Xe3fm9Xc1LasrrgjIWb_ZaVYAlOuUTKOqXzFWpmcbMatbCRHJ_N69fLOQw28vZ9LxqGUuBVPZSyJLv9anUKpjzRKTO_I2f1QlLfwS4SND9fd1qNrYRvnyMxQU7eagWejrMQfpSM&gsessionid=MD_NkK9gBUmtHsep7W9lvlxWM1JzsQo2fPcQ1ctaQFXIF94LrZavHQ)  
  <sub>5 hours ago</sub>  
  Nvidia will report its third quarter results after the bell on Tuesday, its first major public event since former CEO Jensen Huang stepped down amid an...
- [Jensen Huang started closing the Bank of Nvidia months before he left — here’s what’s still open: Chart of the Day](https://www.google.com/goto?url=CAESxQEBxCJF138YnROthbApMldjIIMEeqkRYs3hIwYDJXRrGAdqMa6Cfqix0khmwd1dki5ezMbPNHICetvSnw6wmi3D-WVNH5OiCoRKZXYIm6jkYmAf_aNWM4hLNoGoDyaoE2rIN6Bg_F3VlnJ_GCjfDUNT_lrWjLmU5wIpe8SnpEjNYqtsFi177exiYrG6HTWZG4yl11L-VJrzHem_fduhV4ieWiS7tKJq2C9Jbhdibike-YGkR1j7kUgf692qxTiCuYNJtj3mRQ&gsessionid=MD_NkK9gBUmtHsep7W9lvlxWM1JzsQo2fPcQ1ctaQFXIF94LrZavHQ)  
  <sub>2 hours ago</sub>  
  Nvidia started pulling back on lending under Jensen Huang, and Colette Kress inherits a bank that's mostly closed.
- [CoreWeave Answered the Biggest Question About AI Stocks. Now Nvidia Has to Confirm It.](https://www.google.com/goto?url=CAESogEBxCJF132ej9Qg06BFouDc-FUWooj_ntVfN1pmEOiJbBKxmelSeOBUesSKsfeFjjLP082QwBCoCHFGNrbkr5cY8d31Zf8dsxQBTYHADNUGadVaBQX6FJZXvKcyOxSVarOebJCnmKjHBLuVRobrOIM0P6x1cYQtMFCtadOae2eZ48YF2WmrohgbOvnA3PUJ__vi8f5rHXrL_AkcdAdy59CaWqc&gsessionid=MD_NkK9gBUmtHsep7W9lvlxWM1JzsQo2fPcQ1ctaQFXIF94LrZavHQ)  
  <sub>4 hours ago</sub>  
  It's been a rough few weeks for AI stocks. On Nov. 5 alone, the Nasdaq Composite fell 5.5%, which left it about 12% below the record it set in October.
- [Nvidia Directors Rule Out Huang’s Return as Company Prepares to Report Earnings](https://www.google.com/goto?url=CAESoAEBxCJF1-CmrtbcnFysZHZQjBzLvNsdbxAL3ASb-dYHwJVhsMEY9dHHMfMPDd2m-pO6puK8EjZ7lz282Jsw6xPQfuW_xXeIiJy3W3Xw9rMmJ0H9t4LScO1ColS49ZEAjjpDIu9fh4dS-RLvV_9tyf0s4mveSSU6fm7H9AwvhB38BQ7MAItAJxCEflSDRlE-Tj3itk1tbveqp4B2dh1HHzWm&gsessionid=MD_NkK9gBUmtHsep7W9lvlxWM1JzsQo2fPcQ1ctaQFXIF94LrZavHQ)  
  <sub>14 hours ago</sub>  
  Nvidia's (NASDAQ: $NVDA) board is not considering reinstating co-founder Jensen Huang as CEO, according to pe...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 155.94 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 192.61 (-19.0%), 50d 211.77 (-26.4%), 200d 203.87 (-23.5%); 50d above 200d
Momentum: RSI(14) 22.7 | MACD -16.119 vs signal -12.155 (histogram -3.964)
Returns: 1d -0.1% | 5d -7.7% | 1m -28.2% | 3m -28.3%
52-week range: 155.94 - 239.24 (now 0.0% of the way up)
Volatility: ATR(14) 9.34 (6.0% of price) | annualised 20d 52.7%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 3.77T
Valuation: trailing P/E 19.71 | forward P/E 9.83 | P/B 16.44 | PEG 0.20
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
Consensus: buy (mean 1.69 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 11 strong buy, 36 buy, 14 hold, 1 sell, 0 strong sell
Price target: mean 267.65 (+71.6% vs last close), range 130.00 - 515.00
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

- [NVO261120C00042000 Interactive Stock Chart | NVO Nov 2026 42.000 call Stock](https://finance.yahoo.com/chart/NVO261120C00042000)  
  <sub>18 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [(NVO) Trading Signals (NVO:CA)](https://news.stocktradersdaily.com/canada/nvo-trading-signals_20261117_d07286)  
  <sub>1 hour ago</sub>  
  Buy and Sell Signals for Novo Resources Corp. NVO that help investors manage their investment in NVO.
- [NVO's Hemophilia A Treatment Gets EC Nod, Data Presented on CagriSema](https://www.google.com/goto?url=CAESmwEBxCJF1wXSS6vnmHwSshtA8Pd2rHP9pNR7J4Zcmrorg3pECPLxwpuWHrQC3-M0JRRBrCCiCUcpyEQecJYqOgAQhmTbVPCDBFdZ6jSg3CDs7U-oqn4ymucjnee3np6pLoAHhzYJ7KGK0W_nwQwhwhntfIEvQvWFp-aScWq6jN3Uy0RZ8xdHSNOkxOGrysZCQFMwwvkHRuV-dJDFqw&gsessionid=-aiTlklwj5ZgXlmCq3n01e32R7M0NC-YDASmQ6oqATrKsX4twDo_0g)  
  <sub>22 hours ago</sub>  
  Novo NVO announced that the European Commission (EC) has granted marketing authorization for Frehemgo (denecimig) for routine prophylaxis to prevent or...
- [Johnson & Johnson vs. Novo Nordisk: Steady Uptrend vs. Flat Revenue](https://www.google.com/goto?url=CAES0gEBxCJF18uwvKB1gmXpUW-B6xyCri6KBMhXSHx1p1HRf5yVduuen04cVNAbtVuwGwK6WJ3XetEd6HvnVwreWcHnO-0c228US1x8sWeuioAuep_II0JjvemETtLtEkt3_MgWBOiU7Xr68Vdpig-BIxqYfhSiL6rye8zynuS0nFbKqLjTyGBxvUzs5WHKTIDh2oNR738ZNGFvATPTonCZui2m8BL96jnFSJpjIYH86_SsunVg4d6sJRAGbaQqnN6hFuD1GKv7h8O1X2Nj9enFiwNNbtE&gsessionid=-aiTlklwj5ZgXlmCq3n01e32R7M0NC-YDASmQ6oqATrKsX4twDo_0g)  
  <sub>3 hours ago</sub>  
  Detailed price information for Novo Nordisk A/S ADR (NVO-N) from The Globe and Mail including charting and trades.
- [Novo launches the new Novocare®: Free support program connects people with Wegovy® in addition to home delivery, everyday support, wellness partners and rewards](https://www.google.com/goto?url=CAEStgEBxCJF14e8tswPPSgmYje2rMLQBUChIscdfNpDfXRPdDBTPhZ9yRioHMvso2fkr2DV7o4cuGOhAstbZx4p2iSGGyk_coeYthAUXIDe6xQU60ctbfrsYwQAjHSgZ9bFSYZkNafzOwvX82MkFOeTu7xIjDIRcc-ec_Gc5UHnEr9rRDne0si_IMRt1Ia-UxjrzNEBjpH_QW4XdaRYs3hvrdzGQ4dmUxzP6uvftDDZXZQ1VrlyZUKZjA&gsessionid=-aiTlklwj5ZgXlmCq3n01e32R7M0NC-YDASmQ6oqATrKsX4twDo_0g)  
  <sub>2 hours ago</sub>  
  Novo Nordisk (NVO) launched a redesigned Novocare free membership program offering Wegovy treatment information and support through a website and app.
- [Buybacks at Novo Nordisk (NVO) total 43.7 million B shares; treasury holdings equal 1.3%.](https://www.google.com/goto?url=CAESrAEBxCJF12CNR2S1nnSSh-JX8iiB5WhMNHu-dTMnelljzcx7ksStPh6RWwICIziIH1XdNgUXrdNLNUSOX1FRR7NsMXxezRHYbZfRToLx6KwPMRlz75aQaleOmBNROj7NcP8BkjiMGYHRQHZqqBOaN9YA43PCa7mjDJ2EWkXHYWmzBkvogtOH9u92XIHnJgnSSWgB5Zi_9iLPB65ovzkxNS6U1bMT97efr9cV_W37&gsessionid=-aiTlklwj5ZgXlmCq3n01e32R7M0NC-YDASmQ6oqATrKsX4twDo_0g)  
  <sub>22 hours ago</sub>  
  Novo Nordisk A/S (NVO) reported repurchases under its overall share repurchase programme of up to DKK 15 billion, scheduled over a 12-month period beginning...
- [NVO261113P00028000 Interactive Stock Chart | NVO Nov 2026 28.000 put Stock - Yahoo Finance](https://www.google.com/goto?url=CAEScgHEIkXXYbXl6w9anUZIsF2-zB5cMdRAnVMFi8ob2gYRX7emQPtw_hIdVCeRv7pwY_sIJ3xIaeW1DSi96qx9K5GOsUHzAZ3Fwa59Zg3Hd8K_gdJLN0aYNTnoOgWssNbUZrrf0RcEjSlmEUFsc6k3M4M8Lg&gsessionid=-aiTlklwj5ZgXlmCq3n01e32R7M0NC-YDASmQ6oqATrKsX4twDo_0g)  
  <sub>21 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [NVO261113C00043500 interactive stock chart | NVO Nov 2026 43.500 call stock](https://www.google.com/goto?url=CAEScgHEIkXXk_OAX9bx0nLKNXM5tBUwNGMqbMuV99FvNBY-KSZjNS4Bal2j7B6Q8VK-cPDMatLEYt3x3sp-Z6Z5u84mcUtsB3mYKk92kxPVamzDruosjoXNcETUmL0nrdzzsT4KOd011mN4bsuy5MddAbBJPA&gsessionid=-aiTlklwj5ZgXlmCq3n01e32R7M0NC-YDASmQ6oqATrKsX4twDo_0g)  
  <sub>17 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [NVO: SEC Form 6-K filed by Novo Nordisk A/S](https://www.google.com/goto?url=CAESjQEBxCJF18d01vR6aK8BnRFf2sMiuoLtYt5EuAMp9v8szne3p8s_52MPuIzawm9igxfcXfbeQylLUWK2kO_tZwtFVOZhn_cHXjq_nS9Q9NQvuHqk3k_5lgRODYxAarW2isQ9mGlyIRsM9BOHTdQy6OjNdK3gULwV4F-KHl9kikozKK0_TmLI_HelNCgE2xo&gsessionid=-aiTlklwj5ZgXlmCq3n01e32R7M0NC-YDASmQ6oqATrKsX4twDo_0g)  
  <sub>22 hours ago</sub>  
  Novo Nordisk reported that it bought back B shares in the week to 13 November 2026 as part of its share repurchase programme, with the cumulative total...
- [NVO261113P00034000 interactive stock chart | NVO Nov 2026 34.000 put stock](https://www.google.com/goto?url=CAEScgHEIkXXnCj2ngePM1xizFKrlZngo5nR5_d6s2a2uc9pWim5yTY5tx-YRNZ5Yx-IxeiXcYlFzp_vJ2mtIsTulRefT_uv_8d4YYJxljbcDGTcGvGYjhApYAOCkCsWOQg190lfQhQeQyIQcHqi3Ky3NwhZvQ&gsessionid=-aiTlklwj5ZgXlmCq3n01e32R7M0NC-YDASmQ6oqATrKsX4twDo_0g)  
  <sub>21 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 40.38 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 40.18 (+0.5%), 50d 39.89 (+1.2%), 200d 43.00 (-6.1%); 50d below 200d
Momentum: RSI(14) 50.3 | MACD 0.373 vs signal 0.239 (histogram 0.134)
Returns: 1d -2.9% | 5d -0.8% | 1m +5.1% | 3m -13.1%
52-week range: 35.29 - 63.98 (now 17.7% of the way up)
Volatility: ATR(14) 1.08 (2.7% of price) | annualised 20d 33.9%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 177.95B
Valuation: trailing P/E 10.20 | forward P/E 11.74 | P/B 5.44 | PEG 4.31
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
Price target: mean 45.73 (+13.3% vs last close), range 39.43 - 64.07
Recent rating changes:
  - 2026-10-12 BMO Capital: main, Market Perform -> Market Perform
  - 2026-09-11 Morgan Stanley: down, Equal-Weight -> Underweight
  - 2026-03-02 Goldman Sachs: down, Buy -> Neutral
  - 2026-02-24 JP Morgan: down, Overweight -> Neutral
  - 2026-01-09 CICC: init, ? -> Outperform
  - 2025-12-08 Argus Research: down, Buy -> Hold
Institutional ownership: 10.1%
Largest holders: Dodge & Cox Inc. (0.6%), LOOMIS SAYLES & CO L P (0.5%), Arrowstreet Capital, Limited Partnership (0.5%), Franklin Templeton, Inc. (0.4%), Morgan Stanley (0.4%)
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

- [Dividend Reliability Might Change The Case For Investing In Procter & Gamble Stock (PG)](https://finance.yahoo.com/markets/stocks/articles/dividend-reliability-might-change-case-020854981.html)  
  <sub>Yahoo Finance, 13 hours ago</sub>  
  Procter & Gamble continues to draw attention for its long record of dividend reliability, with recent commentary highlighting a 70 year streak of dividend...
- [P&G (PG) Stock Hits New 52-Week High](https://247wallst.com/cards/p-g-pg-enriched-price-move-01m7kc2e5wezv9swy6v417cmvc)  
  <sub>24/7 Wall St., 5 hours ago</sub>  
  P&G's fresh high at $173.14 tops the prior peak set just three sessions earlier, capping a steep autumn climb in a stock income investors treat as defensive...
- [Public Storage Stock Price Prediction: Today, Tomorrow, Next Week (PSA-PG)](https://www.google.com/goto?url=CAEShgEBxCJF18mSKwz-IuL8fZGAkfOJnQKzszNcoGTRDkPZiof64tLRM2FmSKX8YzGBdgAxmrL5yiQm15ZiZL7Oz9zcB1PPB-rAwlro5s4gWGPEk2hwy_5f1FWXtB3fCzdzC9TWexdGMnIzWpgkn-6jfd4zD3DzZuLtkQyEj3j3vO9L6fgLTFDzvg&gsessionid=tBlxSD_kqVODF1hX8OeF-lbJ_XXGHBeWtvCUKmYBtA0mfuFG9R0eJQ)  
  <sub>Traders Union, 1 hour ago</sub>  
  According to analytical forecasts, PSA-PG may move to $17.18 within a week and $17.06 within four weeks.
- [From Lumberjacks to Jacked Snowmen, Old Spice Delivers 24/7 Holiday...](https://www.google.com/goto?url=CAESpQEBxCJF1-8XXg3oE81Wc997MAi6-FCGidA3nTVJcOSW-ap5AWVcCNtf-2tgBabJDl8AD5HUrycT1r4-xSn0sBr0yC130yXF5JdkS9wGInollZLgFphqzT4eIFhG2Q2wy8y2_9urxlyahm6MlrCdjFFCS5OoDh6S4_x0u2sMU7wWN_SzOMMBvD-nzBcR9HEFgefde-kGs3tc98-IvvXQlzWy4r-TSNo&gsessionid=tBlxSD_kqVODF1hX8OeF-lbJ_XXGHBeWtvCUKmYBtA0mfuFG9R0eJQ)  
  <sub>Quantisnow, 28 minutes ago</sub>  
  Smellebrate the holidays with the Old Spice Holidudes Collection, a limited seasonal lineup of men's deodorant, body wash, and 2-in-1 shampoo scents that...
- [National Bank of Canada (NA-PG.TO) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESaQHEIkXXpaZjsveD5EFCol-TWzlFTV7BlxJW6Ns6DkwKYcvF5DhafqCh70EhKddMkTUKHEqvs7ufbDnrMnRBbf2WOOe9CJq0FroybUmc2OeROcjMEs9SUIOgBAzfI5eQPumDfd2mJZ77hw&gsessionid=tBlxSD_kqVODF1hX8OeF-lbJ_XXGHBeWtvCUKmYBtA0mfuFG9R0eJQ)  
  <sub>Yahoo! Finance Canada, 12 hours ago</sub>  
  National Bank of Canada (NA-PG.TO) · 0.58% · -1.51% · -2.43% · -2.76% · -1.44% · 2.36% · 4.79%. Key...
- [5 Consumer Staples Stocks Reaching New Highs as Markets Retreat](https://www.google.com/goto?url=CAEStAEBxCJF13CevDnZvDMeNGJGUQX1yNr0SAzTcvWi0F4FXICUhdd6gTQXg4FxTOPQgrV3d-E2hdWzi0ucJent_E1-2HwCSgW3gEqgr7EwybD1bkFeoDwheewqhvPKdc6OUtHajdSsMYjL4qptJhesJiguFSMKJboR-Aud2GMJxJu1uazDYgzw39dZT06pX9Kr7iXoGI1_jx1dhS9Ox9FLX9NKl5j3OBqwxDKlrWv4F9yie0K7Nmo&gsessionid=tBlxSD_kqVODF1hX8OeF-lbJ_XXGHBeWtvCUKmYBtA0mfuFG9R0eJQ)  
  <sub>TradingView, 16 hours ago</sub>  
  Consumer staples stocks showed impressive resilience amid Monday's broader market selloff, with investors gravitating toward defensive companies that offer...
- [Procter & Gamble Company (The) $PG Stock: Bessemer Group Inc. Reduces Holdings](https://www.google.com/goto?url=CAESwgEBxCJF17bqCMAABw0txUHlVoCRTMpZq03pJRiQit1bGMz1nCsKyOLMnrm7N542qMbLlpwyuZsy45n7lMXkyFV1G5MmXCI4YbtORs7SZT4i9ivgnnNxxAPA4sYxq1q0cI4pmtAn9cwgfjPH3HTU0w56wEhbyCy2imRqVXxH7dkNZIgi1rVJeveEjp0SWMf35MjPQX1fo5FRT2nJug0WkMjpdInN2jbPGiDeibVAuF5dGE3_DQ7kPhif-kQRAHTQo7LpfA&gsessionid=tBlxSD_kqVODF1hX8OeF-lbJ_XXGHBeWtvCUKmYBtA0mfuFG9R0eJQ)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Bessemer Group Inc. reduced its position in Procter & Gamble Company (The) (NYSE:PG - Free Report) by 34.2% during the 3rd quarter, according to its most...
- [PG Sep 2027 90.000 call (PG270917C00090000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScgHEIkXXub-9Bt22y9qCZWupsmL7DAZ3DMtA57jF72gwHJshayTwoIgvDI8uv_MsUhHsnSKLnEivYhazSYIw9otpl0MDxTrcVmHfUT9cY867ZQgETxb8DID67K20UH4e13lev0ViU5CbCpKEeyd48zuAog&gsessionid=tBlxSD_kqVODF1hX8OeF-lbJ_XXGHBeWtvCUKmYBtA0mfuFG9R0eJQ)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  Find the latest PG Sep 2027 90.000 call (PG270917C00090000) stock quote, history, news and other vital information to help you with your stock trading and...
- [RenaissanceRe Holdings Ltd. (RNR-PG) Stock Price Prediction for 2026, 2030-2040](https://www.google.com/goto?url=CAESdQHEIkXXJu2RlCuAvu3jbGwGCGFAmYHF61SpXH3PQR4gmB_mWdzCoq1gqDykguO8ZrBwX3Mphx9nVc7cXPJNY7v-DeVnhGtxliGQon9i6Jx-5PjDXz_aK6JW6fgbE0TEs1RakJVP0RGorx-yIfoVsfcF-QL6HA&gsessionid=tBlxSD_kqVODF1hX8OeF-lbJ_XXGHBeWtvCUKmYBtA0mfuFG9R0eJQ)  
  <sub>Traders Union, 21 hours ago</sub>  
  According to analytical forecasts, the price of RNR-PG may reach $13.13 by the end of 2026, and it is expected to be $7.06 by the end of 2029.
- [PG Foils Q2FY27 Results: Net profit down 20.6% YoY to ₹11.40 crore](https://www.google.com/goto?url=CAESsgEBxCJF19k_7enSELT25CQkMhrsqcGVWO-CzXKfNiW55XAusAYVufVDGwZH7mF_i7iKaxOVjG2YUmcp8HDFGglWss7nFGrt3Z4FiDdMpCQoZV346eo17uwXOdY7yzXv-613oyu_WlCeeua455gfGr3i1n6FnDrcGjCx3RvurCLGFI_M6ORM7AeScf28qUOeVP12j9I7fklBRmnyOwuVK6F2PPy3avL5ZjoVSuldgtN35gvK&gsessionid=tBlxSD_kqVODF1hX8OeF-lbJ_XXGHBeWtvCUKmYBtA0mfuFG9R0eJQ)  
  <sub>scanx.trade, 5 hours ago</sub>  
  Net profit declined 20.6% YoY to ₹11.40 crore in Q2FY27. Income from operations fell to ₹10.63 crore from ₹12.56 crore in Q2FY26.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 171.96 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 164.80 (+4.3%), 50d 155.32 (+10.7%), 200d 150.08 (+14.6%); 50d above 200d
Momentum: RSI(14) 69.1 | MACD 4.540 vs signal 4.204 (histogram 0.336)
Returns: 1d -0.6% | 5d +2.0% | 1m +9.0% | 3m +19.1%
52-week range: 138.04 - 173.02 (now 97.0% of the way up)
Volatility: ATR(14) 3.19 (1.9% of price) | annualised 20d 29.2%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 398.57B
Valuation: trailing P/E 25.90 | forward P/E 23.19 | P/B 7.33 | PEG 4.36
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
Price target: mean 174.26 (+1.3% vs last close), range 151.00 - 190.00
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

### Royal Bank of Canada (RY) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Royal Bank of Canada (RY.TO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RY.TO/)  
  <sub>Yahoo! Finance Canada, 8 hours ago</sub>  
  Royal Bank of Canada (RY.TO) · -0.91% · 2.03% · 13.14% · 22.09% · 39.05% · 115.37% · 4,172.00%. Key Events. Baseline. Advanced Chart. Loading...
- [Royal Bank of Canada shares technical analysis: Support pressure builds near C$282.6 support](https://tradersunion.com/news/stocks/show/4285441-royal-bank-of-canada-drops/)  
  <sub>Traders Union, 40 minutes ago</sub>  
  Royal Bank of Canada trades at C$285.69, down 1.02% today. Get the latest on RY performance, technicals, and investor highlights.
- [RY: Royal Bank of Canada 13F adds holdings, $663.8B total value](https://www.google.com/goto?url=CAESlQEBxCJF1z8I22C8_FTPNQ2O86sKWLzLdBx3ZnTrLwLt03mFHFC3dLNiK52D2SUNU-bUhUWDIbsZGqKPfBHU44dr2v5lZNlVXXUjlUmztbHDGQDzX8UsMhsQ4Vda6h_6ZPOgpeLm3TzXg1d1ozjPn6leLaBdg-xrZUJKctHDhA-UiYgS54EgCiW6Nr7r2LZVcCajHyeLbA&gsessionid=nmgSjD9uDwY8Oc3BXuoasqy0d3Y2c7bnpLSrUc0Xqp-u9O6amIE4kA)  
  <sub>Quantisnow, 19 hours ago</sub>  
  RBC amended Q3 2026 13F adding holdings entries; $663.8B reported across 27,032 positions, no new trading signal. Information table entries: 27,032.
- [Royal Bank Of Canada (NYSE:RY) Stock Crosses Below Fifty Day Moving Average - Time to Sell?](https://www.google.com/goto?url=CAES0AEBxCJF1ylp4K_5KGuYSDNorKv46xwECTfM6eP_kQGvXzm8cbIKZNRFVXQMPcFmks7y_V-tQesWIUBT0KItMNH2txvcdHUpsvHWPBTxgpFe_DlkuJBgqmbT_GwJOaNwRje53w9njwjnmLHVYnohgfKjYXZEKwJuDvufaaAbxc2huOtnMREIOMwA1Mdb1gKCP3yDTXk-CH3RyrdgN84RKKQa4c8eFLGexDLN7pe1DvksPM4-BRHDVGOrESKyQv3phzaN_URKBMyulHnlMmQQjbrg&gsessionid=nmgSjD9uDwY8Oc3BXuoasqy0d3Y2c7bnpLSrUc0Xqp-u9O6amIE4kA)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Royal Bank Of Canada (NYSE:RY - Get Free Report) TSE: RY shares passed below its fifty day moving average during trading on Monday. The stock has a fifty...
- [The Toronto-Dominion Bank (TD) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESbwHEIkXXrytqLMdvtavc335pQEJDV5PKMYh4jpC0kdEzfn3ztQuRsceHsxts_7nkOaaEx_E6YVgv4lfIp4TfBFD2sBlja1xJ9_kVbb5PQKp5dxcyOp7s2-CD7QT1etWkVzyo9MBhzJKRfUZdR5iFIw&gsessionid=nmgSjD9uDwY8Oc3BXuoasqy0d3Y2c7bnpLSrUc0Xqp-u9O6amIE4kA)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  Find the latest The Toronto-Dominion Bank (TD) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Across 27,032 entries, Royal Bank of Canada (RY) reports $664B in holdings.](https://www.google.com/goto?url=CAESnwEBxCJF16C8SbSIVWc8Vz6xa_Tl2267f7URaBIWG5Hw_AtsamBxU3qM-8OhhxjxYi3P7rQFZFU9J_71-81ryqWA3UcJpQa4HLnIw3zko0SSkPl3u7tFqB9272lti6nS8eOsdMDgaOobhMiyBvx1pWHEa4xoLxl7A_h3JR6X1WWiHrYplDSZFBhG4vBXpofu_FtJgNlLM72LZm_IdS6VlXg&gsessionid=nmgSjD9uDwY8Oc3BXuoasqy0d3Y2c7bnpLSrUc0Xqp-u9O6amIE4kA)  
  <sub>Stock Titan, 19 hours ago</sub>  
  Twenty other managers are included in the report summary. The amendment adds holdings entries to Royal Bank of Canada's institutional holdings report.
- [Royal Bank Of Canada (NYSE:RY) Sees Large Decline in Short Interest](https://www.google.com/goto?url=CAESvAEBxCJF10fYhk_vY5woPZy_g_J56kOG3UTDDmJEIQykDB3A44Ugb9PLFbP7htnc1dbarztIHFVKq9iB14095Ng6L7C4iTjyzhQl3YMHoxF94f4GjwU3wVm9Ad6erwUCuQ12gKmcfviVVYXv-M-KDImkKlvV2t49i8ZNht1KJ33rAg3fYhJOHs3xIo6Nin6kZu3jTN2uKVPr5Ze-VYcq9jfq9LAv1TorP7lcmMzMB1-MCRCVuhqM5GebeG8xiQ&gsessionid=nmgSjD9uDwY8Oc3BXuoasqy0d3Y2c7bnpLSrUc0Xqp-u9O6amIE4kA)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Royal Bank Of Canada (NYSE:RY - Get Free Report) (TSE:RY) was the recipient of a large decline in short interest during the month of October.
- [The Toronto-Dominion Bank (TD) Latest Stock News & Headlines - Yahoo Finance](https://www.google.com/goto?url=CAESaAHEIkXXZRr1jDfiLGTrNLBjRap90UlFgwFYFe0b47fcnyYKI7KjsWHyTav0XNujLAtzi918jUTgaMYqtwsFEYyoOVOBFB_TcT2s4nU0aT0qz-hZhK5uYiqoN4XB8uDWhYdREghwgBxZ&gsessionid=nmgSjD9uDwY8Oc3BXuoasqy0d3Y2c7bnpLSrUc0Xqp-u9O6amIE4kA)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Get the latest The Toronto-Dominion Bank (TD) stock news and headlines to help you in your trading and investing decisions.
- [2 TSX Giants to Buy for Decades of Growth and Dividends](https://www.google.com/goto?url=CAESlgEBxCJF11KJ-ycG4KDYx0JpBdQVQ1ZKZZHFSN8hVb-8mijaEHQGHQK5MeOEcGZXtD6pgZ4-aLcxb-tXjeWRe7MooVJ0AevoSDuSGxrd8IoMrWYWksrtY-PjPvHWgWqQBdG8WVMYnM0VX4JNlY2rL4IBFWcFwhODtAr1m0yMe8_omkHFwos9VGM1V_YxRFL7hYMcd_Ds6cE&gsessionid=nmgSjD9uDwY8Oc3BXuoasqy0d3Y2c7bnpLSrUc0Xqp-u9O6amIE4kA)  
  <sub>The Motley Fool Canada, 13 hours ago</sub>  
  Royal Bank of Canada (TSX:RY) and another dividend giant worth buying up for decades.
- [3 Canadian Dividend Stocks With Yields Over 2%](https://www.google.com/goto?url=CAESugEBxCJF1wcvUeJtIkXpPsCC7vtCxVKzUsKMqe9GMW-RjF_LtArSQUfnK5jJ4HtvegDuuWgWIPw71x55KEmiuUAvf8PP3kxsfHxKOXbQfmE8cci-_py3coemFl4L0gbIjBAbkl0-snM_Apdcv8-4HmqbIe2hs-_XuMnRqAHwsndQF4TdewpCz5v2tZ2DlRCUVlTyQUo2d-TWF8VWysoK23at37mWJN5IiUJ0FF5q2LVjwkEWx2R7EAdH9tw&gsessionid=nmgSjD9uDwY8Oc3BXuoasqy0d3Y2c7bnpLSrUc0Xqp-u9O6amIE4kA)  
  <sub>Simply Wall St, 23 hours ago</sub>  
  Central banks keep reminding investors that interest rates can move higher when inflation stays sticky. That kind of backdrop often nudges people toward...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 197.43 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 202.98 (-2.7%), 50d 200.64 (-1.6%), 200d 191.30 (+3.2%); 50d above 200d
Momentum: RSI(14) 42.1 | MACD 0.086 vs signal 0.758 (histogram -0.672)
Returns: 1d -1.1% | 5d -2.5% | 1m +0.6% | 3m -4.9%
52-week range: 147.13 - 217.87 (now 71.1% of the way up)
Volatility: ATR(14) 3.31 (1.7% of price) | annualised 20d 20.8%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 273.33B
Valuation: trailing P/E 17.26 | forward P/E 15.50 | P/B 2.87 | PEG 1.93
Profitability: profit margin 33.9% | operating margin 45.7% | ROE 16.2%
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
Consensus: buy (mean 2.21 on a 1=strong buy to 5=strong sell scale, 3 analysts)
Ratings: 4 strong buy, 4 buy, 5 hold, 0 sell, 1 strong sell
Price target: mean 208.56 (+5.6% vs last close), range 182.03 - 229.38
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

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

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

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Teva Pharmaceutical (TEVA) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Glenview ups stakes in Meta, Teva; cuts CVS, Block in Q3; exits DKS, STM (META:NASDAQ)](https://seekingalpha.com/news/4673467-glenview-ups-stakes-in-meta-teva-cuts-cvs-block-in-q3-exits-dks-stm?source=generic_rss)  
  <sub>4 hours ago</sub>  
  Glenview Capital's latest 13F shows it exited Dick's Sporting Goods; four major hedge funds divested, while it added 2.48 million Teva shares.
- [Teva settles US states' drug price-fixing case](https://www.reuters.com/legal/litigation/teva-settles-us-states-drug-price-fixing-case-2026-11-16/)  
  <sub>22 hours ago</sub>  
  Teva Pharmaceutical Industries has settled long-running litigation by most US states accusing the drugmaker and dozens ​of other defendants of conspiring to...
- [FDA Approval for AMIFAMPRIDINE PHOSPHATE issued to TEVA PHARMS INC](https://www.google.com/goto?url=CAESqQEBxCJF11d44LsheJsiZ4c4xYvqepTur-Ggr0ZwmgdBX67pUN8pXFtKLYqEh5S55cDKe4k2RvEIsbjXkApNjCnKsy2dsVcyaeCESLaT7CJZ17uuhb0yxMqz3Ufw_vsZoVJzNbiPZlaeBrq9J-IFfgeohxN7V12DMM8wRlZGb1EXYtizw1EkTvpp4e20Np2lmYiuuxE01qFZa0kTq2KoSGezZhrhy_MTXy6W&gsessionid=pG6LykSp2ycoa_kDen3H4fI5wzEliLjHNIBWjujz3LcjxQm6nuPxgw)  
  <sub>9 hours ago</sub>  
  Submission status for TEVA PHARMS INC's drug AMIFAMPRIDINE PHOSPHATE (ORIG-1) with active ingredient AMIFAMPRIDINE PHOSPHATE has changed to 'Approval' on...
- [Teva to join Russell 1000 large-cap index](https://www.google.com/goto?url=CAESkwEBxCJF14WizUmNrYtKi0t2SDOFfcHV9M868NNacHkogpKnov7e4X6k8W72xRasnuY5Q95fBVGf0IJESU4PdBbTeJ4LZnUYWAsfTUiPRy3PKEyMQ2bkcABTz_08YckahUum9UCUfY-ZmnMhf84AvRh1mGvvj5nDPS0M8XUyEpjsZ_xCIfQs5Kt8DQfVSo6L1RzDodE&gsessionid=pG6LykSp2ycoa_kDen3H4fI5wzEliLjHNIBWjujz3LcjxQm6nuPxgw)  
  <sub>2 hours ago</sub>  
  Currently, the largest companies in the Russell 1000 include Apple, Nvidia, Microsoft, Alphabet (Google), Amazon, and SpaceX.
- [New Analyst Forecast: $TEVA Given $54 Price Target](https://www.google.com/goto?url=CAESlQEBxCJF158O7RfauOzQRvGdbvBREypsX6gQ8keZVLw5jd0G7uCuRZW18mp6vsc-Bfy9SyIXLszJb_4nv3Z2GL1833yNAqI2Zghi5RKqXEpuYLt-KeTz3KPtvqXTenBMqAEKcHOxo6HeiAVLwe9SE9bKug65eL1mtXONDLUmHU_sqJnQw356M28kDF8k5q4t4WAYOq7j-g&gsessionid=pG6LykSp2ycoa_kDen3H4fI5wzEliLjHNIBWjujz3LcjxQm6nuPxgw)  
  <sub>2 hours ago</sub>  
  We just received data on a new analyst forecast for $TEVA. Douglas Tsao from HC Wainwright & Co. set.
- [Teva Pharmaceutical Industries (TEVA) Could Be 13% Undervalued Following FDA Approval For IGALMI](https://www.google.com/goto?url=CAES3gEBxCJF1-MhLM28fJuQK2PHDDAsqpNSPwyzG2Je_NwHLjRxTavtihMx-j86jq_2Cf9LBcPFIiELCpOxtHq1i0PPAQakN1NdWwXaRncUcgX7-VX-RjUUYG8t_ktbu_9T3B6sfXpTJ9Z9M5ez5Qnh2ficWyDSmyJ8JUbPWtmR8-92yT55Mrgh7TWQsBIbx36bp8b9YP9aeuOyej_9dnD7pmQSKmIQmL_YF3BiGKZEumWtilJOjeG8QU9OjP18YsXUbzEGW10iwz5Lnf6AthKxNWpw0zTku6dG3d8IDJkXGkA&gsessionid=pG6LykSp2ycoa_kDen3H4fI5wzEliLjHNIBWjujz3LcjxQm6nuPxgw)  
  <sub>5 hours ago</sub>  
  Teva Pharmaceutical Industries (NYSE:TEVA) just secured U.S. FDA approval for at-home use of IGALMI sublingual film, the first treatment cleared for...
- [FDA Clears Teva's Newly Acquired At-Home Agitation Treatment in Schizophrenia and Bipolar Disorder](https://www.google.com/goto?url=CAESzwEBxCJF12yECpcrTflEaf9jT2RGAjLRprTqiFmXh9__AHULZFZELsGL137dAU_coNC8oPZcSzoqk4okACXa0r-Ofw2ytPWCpv-DuLcXWmZGUg5N3rzpao4FMFztKkkAp8lshWEbfHfaQ2XtfQ85zG3qD-HVmYvuPVqgwr5H4Qbidd7tHS93BRGX-D9gloRpw1Q9cmpBQPULSH1Su0UjbS6qSaL9p_0hLDV5q6NxDT1U1aU0Hu0t5kyK0KpnKgwb6KnpAbw_ues2hs8T4kPxwD4&gsessionid=pG6LykSp2ycoa_kDen3H4fI5wzEliLjHNIBWjujz3LcjxQm6nuPxgw)  
  <sub>21 hours ago</sub>  
  The FDA approved Teva's IGALMI sublingual film as the first at-home treatment for adult agitation in schizophrenia or bipolar disorder.
- [Teva Pharmaceutical Industries' (TEVA) Buy Rating Reaffirmed at HC Wainwright](https://www.google.com/goto?url=CAESxQEBxCJF16iGoljWu60ng398j0GBlzYp-8xYsVSIDqVQmTlJpXx3oDW2q3Ka1PJObpa3z9ujnvZqR-bRg7p5FCFCcz7kH73rPRhZ5EJBGGe1_LjZjjbUAHi8FStC65GbeLFsBQiU2uZ48YMAhT7M1J5sOEAeKy79j1f6GWINq8IsW76SJprxgUWnvC-BOjy32o7nX9qtug6_4PkT_tjEfxuEQ89Bi-cud9c9ThlIxAt4i-94G5q6639dIPhozDYGco6TJ6QwgQ&gsessionid=pG6LykSp2ycoa_kDen3H4fI5wzEliLjHNIBWjujz3LcjxQm6nuPxgw)  
  <sub>2 hours ago</sub>  
  HC Wainwright reaffirmed a "buy" rating and issued a $54.00 price objective on shares of Teva Pharmaceutical Industries in a report on Tuesday.
- [A reported 56.6 million-share stake in Teva (TEVA) spans funds, accounts and partnerships.](https://www.google.com/goto?url=CAESwAEBxCJF13dgoOf4W0F5BDI2tax54RMHKMDMdJUl1PIBWGNSF3-9VSvhaNeJ2p55K7F9cELV0AKAA5Bx2Ii01uAwVrWC23R_tOSCSkOSyqzlN-h5qO08alm39mq8Og_-3h2VsN8hxS5jlVmSttrglK3OAQS9eDC53TpcqaauM_x-2f2dXf-iWv8O9RBvIShmM0xT0WVn_3zLdMiNVWC57OC6fMuwneqhNDqK-wwDJSkYFZUelk9M7I0stzZ-71DM2CQ&gsessionid=pG6LykSp2ycoa_kDen3H4fI5wzEliLjHNIBWjujz3LcjxQm6nuPxgw)  
  <sub>19 hours ago</sub>  
  Phoenix Financial Ltd. reported beneficial ownership of 56,550,148.77 TEVA ordinary shares, equal to 4.85% of the class. The reported holdings were as of...
- [FDA Approval for IGALMI issued to TEVA](https://www.google.com/goto?url=CAESjQEBxCJF10TBrXKGASekukUOsbtD3o46g-TpSX3FA1_FVtzEGXsA-Zv2StwZ1xjQH8F2vVCa1s1-EDl3Sw-LR1e49B3Vi6I5n4lQ2h8VaHTXp85iZslWxxZEBBRFTG2w4U6ClxhbA9dj0ewEJmsMyA6PpcZFyxkJ_y-oIE_9JoVms2Mv_A0w291wnCnSFGA&gsessionid=pG6LykSp2ycoa_kDen3H4fI5wzEliLjHNIBWjujz3LcjxQm6nuPxgw)  
  <sub>19 hours ago</sub>  
  Submission status for TEVA's drug IGALMI (SUPPL-3) with active ingredient DEXMEDETOMIDINE HYDROCHLORIDE has changed to 'Approval' on 11/13/2026.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 42.25 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 41.73 (+1.3%), 50d 40.42 (+4.5%), 200d 35.18 (+20.1%); 50d above 200d
Momentum: RSI(14) 53.6 | MACD 0.843 vs signal 0.823 (histogram 0.020)
Returns: 1d -0.8% | 5d -0.4% | 1m +2.3% | 3m +12.8%
52-week range: 24.21 - 44.50 (now 88.9% of the way up)
Volatility: ATR(14) 1.22 (2.9% of price) | annualised 20d 32.4%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 49.30B
Valuation: trailing P/E 98.26 | forward P/E 13.53 | P/B 6.18 | PEG 1.03
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
Price target: mean 50.29 (+19.0% vs last close), range 42.12 - 57.00
Recent rating changes:
  - 2026-11-12 Piper Sandler: main, Overweight -> Overweight
  - 2026-11-05 Leerink Partners: main, Outperform -> Outperform
  - 2026-11-04 TD Cowen: main, Buy -> Buy
  - 2026-11-04 HC Wainwright & Co.: main, Buy -> Buy
  - 2026-11-02 HC Wainwright & Co.: init, ? -> Buy
  - 2026-10-15 Barclays: main, Overweight -> Overweight
Institutional ownership: 69.3%
Largest holders: Blackrock Inc. (5.4%), Phoenix Financial Ltd. (3.6%), WCM Investment Management, LLC (3.6%), Clal Insurance Enterprises Holdings Ltd (3.6%), Menora Mivtachim Holdings Ltd. (3.4%)
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

### Toyota (TM) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Atlas Signal Initiates Coverage of High Roller Technologies: ROLR(TM) Prediction-Markets Platform Goes Live on iPhone for U.S. Customers](https://finance.yahoo.com/markets/stocks/articles/atlas-signal-initiates-coverage-high-133000356.html)  
  <sub>1 hour ago</sub>  
  ROLR is positioned in a prediction market forecast to exceed $1 trillion in annual trading volume by 2030ROLR: Prediction Markets, a native iPhone app,...
- [Texas project is designed to make about 23.2 million gallons of sustainable jet fuel yearly with Plug Power's new system.](https://www.stocktitan.net/news/PLUG/plug-launches-gen-eco-tm-scale-an-integrated-electrolyzer-plant-1tguthwmtwuv.html)  
  <sub>3 hours ago</sub>  
  Plug Power (NASDAQ: PLUG) launched GenEco Scale, an integrated electrolyzer plant offering, with Arcadia eFuels as its first customer.
- [(CMVP) Stock Market Analysis (CMVP:CA)](https://www.google.com/goto?url=CAESkQEBxCJF1y5RAVlsY_JI1K7uM0ZFJIvbzuuYl5gkok5tcZN4WInKfFSHoHb9JTfatixNZY4B-xnxq_w4So4xyT-ixWO3r1CKBnSuUP37eZ33PQWYcEyuqPv8-0jY7Xbr3sOgV-EvCv-7qmc_onuWuBkqUrZ9HEf83i9AMrx_2z1WE3GfnLEf1XoBctW82ZN044W8&gsessionid=Xf2II4QCtIgz6sOM7CVZy8Ua0rZmAm73JN3Y37Zyb2NuJnL_VI8WyQ)  
  <sub>8 hours ago</sub>  
  Stock Market Analysis for HAMILTON CHAMPIONS TM Canadian Dividend Index ETF (CMVP) Highlighting Key Trading Opportunities.
- [Wrap Technologies (NASDAQ: WRAP) Announces Military-Standard Certification of Frenel Imaging Detection Sy](https://www.google.com/goto?url=CAESzAEBxCJF16d_CTgJUvsiQ0SfgElosun5He0tneYQQhePPyIh5wn_wlSx8mYpfG63J_TfmaOJeRtplEabtg_e-ayCUywz46lDw--OaD3I-tGjFK5XpaIkxBOJXWyZdEHLUBE8DLGXYSsRf3lExFsqtw6OKAATjNR8YsyGS9qrpMg3yzTpcYXAqjmGIPvdb77fE4xgoErkE_pP6Z45ZNR_tDTzmnyTS6ikwlVTkvAX3Dk40-d8Wo5NUnzZYiIMZh1B0VqIJ0nABNV6sDrFCF4&gsessionid=Xf2II4QCtIgz6sOM7CVZy8Ua0rZmAm73JN3Y37Zyb2NuJnL_VI8WyQ)  
  <sub>22 hours ago</sub>  
  Austin, Texas, United States, November 16th, 2026, FinanceWireWrap Technologies (NASDAQ:WRAP) announced that its WrapShield(TM) detection partner,...
- [Sensex Today Ends 427 Points Higher | Nifty Above 25,350 | Nifty Bank Hits Record High](https://www.google.com/goto?url=CAESzgEBxCJF1zSPMaF60P6DFdvhpGH4tCa6zsS8lWjI7bdyzqO2EJ0RWnw4q8OHAEGqrko99a05xcG5l0ouShLCqRvmL3gAQ9VBwbofPgVw3X-tKmsZqI0xxdqRFM1y5MNvRUeMkZ8EZ56R6rZhQNPaQHXiifkwZzr-F_CsknArp_MGuX_TkRLTZs7Ma31bA3st0z-RXx-LOb-6dgNbfhwJrRQxzrlev0elb9D7fwx3TK3Nvh6mg0n3rxLFDDCbuuInkKJVcJX909k5H15aQwbB6Q&gsessionid=Xf2II4QCtIgz6sOM7CVZy8Ua0rZmAm73JN3Y37Zyb2NuJnL_VI8WyQ)  
  <sub>4 hours ago</sub>  
  Indian markets ended higher with the Sensex closing up by 427 points while the Nifty gained 96 points.
- [TM Jan 2027 100.000 put (TM270115P00100000) Seasonal Returns Chart](https://www.google.com/goto?url=CAESewHEIkXXkjt0sFJjxJpPJdBQHGb1U3wcXyFbs7fwO2Xec7_6KZfBMKo8afFcA5NnlHB8K4RLpckpaaSyrinI3_UWr8W4i3R1jTN-PevyO4NU2akOQzNhen3abbQhgS4Q9BCEoJfFrdXqLJuq7Zbbssj33e5yQo1gKuGKJw&gsessionid=Xf2II4QCtIgz6sOM7CVZy8Ua0rZmAm73JN3Y37Zyb2NuJnL_VI8WyQ)  
  <sub>22 hours ago</sub>  
  TM Jan 2027 100.000 put (TM270115P00100000) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [Greenwich LifeSciences Announces Acceptance of Abstracts at SABCS 2026](https://www.google.com/goto?url=CAEStgEBxCJF1-e0vkMkdzaLItXbkT8DGn7CHfsvEYzoKZf-v0m0-aW7rdmIJTWJ9bWnwizqmL2SU7DdE4tuI6eXr9wGXZVgu6HEArT8RQKmUBKz1ffPXsEmGfVyI8YAiTNjN-jlqdYWbg6U60VMDoPafM_oNK8IdzBMeott569bVQyWdL9uaYCopTCm06j3A3_5_sM6vo9yf9Zbhm4uyF41w89NOJ23WXImg4G49v2PcxyeI2MbwFoMbg&gsessionid=Xf2II4QCtIgz6sOM7CVZy8Ua0rZmAm73JN3Y37Zyb2NuJnL_VI8WyQ)  
  <sub>4 hours ago</sub>  
  Stock Titan provides an ultra-fast stock market news feed and multiple tools for traders and investors.
- [(SMVP) Equity Market Report (SMVP:CA)](https://www.google.com/goto?url=CAESkAEBxCJF1_6A0nPL-Ci1sujjXzlXWd_7g_OJD59trmkiuzejQTNBb_RPo26R55W9c0VvQUNZ2tof4BxXQ91SwDecaVH6zVtqc8e_RtLDUtPyAsADKF65l1TgEvgkBAMoJToQuxNN3_TWQDbRLFbnEsnK4yw5gUnJ1h3Q8j0pIjQikSyU4yCmrWNQ2Qjc24oWOTo&gsessionid=Xf2II4QCtIgz6sOM7CVZy8Ua0rZmAm73JN3Y37Zyb2NuJnL_VI8WyQ)  
  <sub>8 hours ago</sub>  
  Equity Market Report for HAMILTON CHAMPIONS TM U.S. Dividend Index ETF (SMVP) with Buy and Sell Signals.
- [A California plant will be first in the U.S. to use DuPont modules designed to use less energy to treat wastewater.](https://www.google.com/goto?url=CAEStAEBxCJF15p4fqWW0TIIelNV_CzPZ3-4PnL9IPFf210jN28IXcYotHB8sgnj1fG-ZC6VPyoej1BIhLtyoyWCQe5WZUXvBAEwTouOF0BZ3xb70yY5OQgtk_co73upsi9GlC5F89t3D5iggkWhAPPKMZa0WnyrWvvpyP1THtFrLb-PzZxH8rNikcd_6jNyp6hj5wiZMlmI29i0jyDYq7W4Ttn_JypfSBrldCVZMlVluWGC02H4Tro&gsessionid=Xf2II4QCtIgz6sOM7CVZy8Ua0rZmAm73JN3Y37Zyb2NuJnL_VI8WyQ)  
  <sub>43 minutes ago</sub>  
  DuPont (DD) announced that its OxyMem wastewater treatment modules have been selected for an upgrade to California's Windsor Water Reclamation Facility.
- [How the (CWIN) price action is used to our Advantage (CWIN:CA)](https://www.google.com/goto?url=CAESqQEBxCJF1xSCPZpcvrHUyler6rdXuSYAdDO9WkloNAJ4lftF2zYhfONIywuT1uP5Ko8xn4oa2JI0tGbLHDQZ0LmgRdTZ7-jfyh8HcHud59LOp2lUQzA5hoFKkCXQP5J48WBBHUn5MmY2fR3RrhVwqGVM_yOOxLvZWmLViKIv79M5yHsjb8DZmfLCrpH9FGUqcJn2KlS5DpSvbK3JQiYkrEaQ0Ehm1spLCkY0&gsessionid=Xf2II4QCtIgz6sOM7CVZy8Ua0rZmAm73JN3Y37Zyb2NuJnL_VI8WyQ)  
  <sub>8 hours ago</sub>  
  How the price action of HAMILTON CHAMPIONS TM Enhanced Canadian Dividend ETF CWIN is used to our Advantage.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 213.73 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 204.49 (+4.5%), 50d 195.60 (+9.3%), 200d 197.74 (+8.1%); 50d below 200d
Momentum: RSI(14) 64.3 | MACD 5.933 vs signal 5.293 (histogram 0.640)
Returns: 1d -0.1% | 5d -0.5% | 1m +10.1% | 3m +13.2%
52-week range: 166.50 - 248.29 (now 57.7% of the way up)
Volatility: ATR(14) 4.32 (2.0% of price) | annualised 20d 38.8%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 250.83B
Valuation: trailing P/E 9.75 | forward P/E 13.54 | P/B 17.01 | PEG 19.89
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
Price target: mean 238.08 (+11.4% vs last close), range 230.00 - 253.00
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

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Why Pay More For Exxon Mobil Stock Than Chevron?](https://www.trefis.com/stock/xom/articles/625652/why-pay-more-for-exxon-mobil-stock-than-chevron/2026-11-17)  
  <sub>4 hours ago</sub>  
  For questions about this article or underlying research, email help@trefis.com.Exxon Mobil (XOM) stock costs more for each dollar of profit than any of five...
- [What's Going On With ExxonMobil Stock Monday?](https://www.benzinga.com/markets/large-cap/26/11/63305551/whats-going-on-with-exxonmobil-stock-monday)  
  <sub>22 hours ago</sub>  
  ExxonMobil starts oil production at Guyana's Uaru project and launches a $3B debt buyback, while XOM stock dips amid broader market sell-off.
- [Fund Update: New $776.0M $XOM stock position opened by AQR CAPITAL MANAGEMENT LLC](https://www.google.com/goto?url=CAESrwEBxCJF1xcR1Qx3WRdkua-ZRwapqK48z9NemGuW7Vrwg2T1_WzhQ7HSte0sggME1_xpkoi8MitVPn2ZG2ctr9Qu6WEav3_R2m5ZPkLEvXmPs6gd64pv7QirFuwir2Pm6-KLH5FntRE8VoyEqP4euQGj2xxBmTyefKIsMj5jNHwK8LNBGL5_WIMlDfFHTueEHTBjyfnpND3xIx1j19XZfAUv0J52bAqLeoZbZHFp0gGK&gsessionid=kZKz9T5Qj1LhZffMalXTdz2fuvQKSPrA1UTMOfBGYlXlvdLC4MFlTg)  
  <sub>16 hours ago</sub>  
  AQR CAPITAL MANAGEMENT LLC has opened a new $776.0M position in $XOM, per a new SEC 13F filing. This.
- [ExxonMobil Corporation $XOM Stock Sold by HighTower Advisors LLC](https://www.google.com/goto?url=CAESuQEBxCJF1xhuzVAsm5aTrEBlsJegsoE8MVlnySIuwS7QiILxu2hlxBsUkIS0x_7j8aphL8mZWyEU45ZcCXOy-3wcUWNjHdjTFTlwlJG7tdknqtHUa0i03R-C2tDtJLlhxOtXVjWIaDMkIqu_RR2gMBthj9HU3iAFKDQUHiXtiHWnIg5bHdx4ObVYYIm_Yrw0lt-I0LJatBYD0kqxAGUAygYgsK8u4-ExFTCVT6SCHQBduwSnZauQacDrAw&gsessionid=kZKz9T5Qj1LhZffMalXTdz2fuvQKSPrA1UTMOfBGYlXlvdLC4MFlTg)  
  <sub>3 hours ago</sub>  
  HighTower Advisors LLC decreased its holdings in ExxonMobil Corporation (NYSE:XOM - Free Report) by 6.8% in the 3rd quarter, according to the company in its...
- [Can ExxonMobil's Longtail Project Unlock Guyana's Growth Potential?](https://www.google.com/goto?url=CAESpgEBxCJF11dSQvNQdAeLLXhjAcOLsuquDp9PcKMbFRNGuLKlOyrnfYSxtNbUI-AbNi_qVznmQRviyVCAqmi1hs92XGmXUcFh1RtcRy48N2N_QvJfDTWFEJ5OxfhPVWl7Gx6b-3SynNEchkzSawYMSHqgBt2-eGbYDvF_vhtFCWGq0Gl-vNAoVZPMMpfFRxscv73f2XlDqzL8vaINTYE16MLJIfL88Z0Z&gsessionid=kZKz9T5Qj1LhZffMalXTdz2fuvQKSPrA1UTMOfBGYlXlvdLC4MFlTg)  
  <sub>20 hours ago</sub>  
  XOM advances its eighth Guyana development with the Longtail project, aiming for a 2030 startup and major gas processing and condensate production capacity.
- [ExxonMobil’s new offshore vessel is expected to reach 250,000 barrels a day in early 2027.](https://www.google.com/goto?url=CAESswEBxCJF16y2FB6iPwnkWJ4_iZL07VPLe_ap8CVgbGTUfN3Oa02pWjVzoNfExW_vkCahIKlKeHaqC5Z9Ri3JEff794nH-P2RJYMqP3vwyc-SFGy7ejAbRRm-GV2IHUqcoD6pV0x5oO5IPnUT-XzrRdmPAq_pIaL4mvsalCfjCTai3I6AKV6lsdC0BPJuWKgnjILDPy7LwGxlmVWOAHW1yavFmu85wPx3I4nBcwRpWo7O7BmbgQ&gsessionid=kZKz9T5Qj1LhZffMalXTdz2fuvQKSPrA1UTMOfBGYlXlvdLC4MFlTg)  
  <sub>23 hours ago</sub>  
  Errea Wittu has 2 million barrels of storage capacity; since 2015, ExxonMobil and Stabroek partners have spent over $3.9B with Guyanese vendors.
- [How Is ExxonMobil (NYSE:XOM) Advancing Its Longtail Project in Guyana?](https://www.google.com/goto?url=CAESqgEBxCJF11rPAmPFFeKkpuANb_GZ9bONGegwgw_Novq3Bo8QIk2gulO0YHW21WIjpZnklPsGeSDf4xTswFajAgbSw5vgUcqTx-jiXpxm4Q6AyzIqYytmoZnZX5FdOlSES9X8IAzRIWDLeT_XaxH1jvAhuDdfHlf-h9l9DKe8RPw1tfxRfiV7iC_UOjlwn-vCIeSCdksyRkWcZ0y-Gs77xEjGQB0DuAbk9pge1w&gsessionid=kZKz9T5Qj1LhZffMalXTdz2fuvQKSPrA1UTMOfBGYlXlvdLC4MFlTg)  
  <sub>9 hours ago</sub>  
  ExxonMobil reached a final investment decision on Longtail, Another Stabroek block development offshore Guyana, after government approval of the plan.
- [ExxonMobil (NYSE:XOM) Stock Price Down 2.1% - Here's Why](https://www.google.com/goto?url=CAESqgEBxCJF13387WdJdO9-K_7iRZM6EvMJtqwMQLr4J4hYHiqTYemhsf8xp8aaZnkeVXd2HeXAt3eBu3DCaW0ee8zuAtFjsH-qsrnD_j7lAewfQ5zrgx4EEKmwk34R3nyTJ3ziFcsxH0ztCUQ5oLBejKJ8c8nk5RN6hzXxf_XPecra9ziM-PswfcFLVYrSAiXxzn-foomHshl-lutFVlYob82sbFiM54WP41lNWQ&gsessionid=kZKz9T5Qj1LhZffMalXTdz2fuvQKSPrA1UTMOfBGYlXlvdLC4MFlTg)  
  <sub>16 hours ago</sub>  
  Shares of ExxonMobil Corporation (NYSE:XOM - Get Free Report) dropped 2.1% on Monday. The stock traded as low as $166.45 and last traded at $166.9660.
- [Oil Stocks To Follow Now - November 16th](https://www.google.com/goto?url=CAESngEBxCJF19b0sYIK1weN7p5xDgn_QDgAFHUIZwbqF_jPY0qcaTrP9nHIlq0Ed1dlEB8rwBpqT3SBt7nSlIr5AczwgILfLLCTAMTQnL4k_FHHrii_z62blDhnHsVmLXPl5Kmz5qvXP1c0TrKdYgpauySLDkJqL1qcGH-xd-AKkiMAhqe6BynnmfLSiMQtcMQKv8GBYrCzZsYCyJEU5RAQfg&gsessionid=kZKz9T5Qj1LhZffMalXTdz2fuvQKSPrA1UTMOfBGYlXlvdLC4MFlTg)  
  <sub>20 hours ago</sub>  
  ExxonMobil, Chevron, Marathon Petroleum, Valero Energy, ConocoPhillips, Phillips 66, and Diamondback Energy are the seven Oil stocks to watch today,...
- [How Boomers Can Turn $150,000 Into Passive Income With These 4 Energy Dividend Stocks](https://www.google.com/goto?url=CAESvAEBxCJF17npjbQ_GDtTIIX9ThVvR5URK1HABFq0AKExIcQMOHsG7znh2gqlhOXpR6Ah1KmJTf6NjSFoLV3sRopABhK1Mbcn0VkI9rYjS7Pz0MMulO-G0KZB1q6lyUrmxs0MY2j9n5HpVAbvQNgnB2M9TGTTPoW7p_Tnc_5-4bvWmh5xXXcXN13h9u2g1HzYZ8temVcnjm9e-49JvvuqzDd2kCGCdSGhxuJ31g1D0X9l6MOQemDAqDGXRA99DQ&gsessionid=kZKz9T5Qj1LhZffMalXTdz2fuvQKSPrA1UTMOfBGYlXlvdLC4MFlTg)  
  <sub>2 hours ago</sub>  
  Retirees run into the same math problem sooner or later. Social Security and pension checks rarely stretch as far as a paycheck did, and selling shares to...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 169.08 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 174.32 (-3.0%), 50d 169.69 (-0.4%), 200d 156.64 (+7.9%); 50d above 200d
Momentum: RSI(14) 46.7 | MACD -1.214 vs signal -0.121 (histogram -1.093)
Returns: 1d +1.3% | 5d +2.8% | 1m -5.2% | 3m +2.6%
52-week range: 114.51 - 187.25 (now 75.0% of the way up)
Volatility: ATR(14) 4.15 (2.5% of price) | annualised 20d 32.0%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 689.71B
Valuation: trailing P/E 17.40 | forward P/E 13.48 | P/B 2.59 | PEG 1.34
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
Price target: mean 184.18 (+8.9% vs last close), range 160.00 - 213.00
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

### Farm goods basket (DBA) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 26.57 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 26.83 (-1.0%), 50d 27.83 (-4.5%), 200d 27.41 (-3.1%); 50d above 200d
Momentum: RSI(14) 37.8 | MACD -0.449 vs signal -0.486 (histogram 0.037)
Returns: 1d +0.7% | 5d +1.2% | 1m -5.8% | 3m -6.1%
52-week range: 25.44 - 29.49 (now 27.9% of the way up)
Volatility: ATR(14) 0.24 (0.9% of price) | annualised 20d 9.9%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Commodities Focused
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 3.4%
Three-year record: +10.2% a year | beta to the market 0.37
Cost and size: expense ratio 0.85% | net assets 1.13B
What it is made of: Other 49.6%, Cash 47.9%, Bonds 2.5%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 40.2%, Invesco Short Term Treasury ETF 5.3%
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
Rolled up from the 2 largest holdings, 45.5% of the fund by weight
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 27.60M | fund size: 733.33M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 30.44 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 32.19 (-5.4%), 50d 32.66 (-6.8%), 200d 29.66 (+2.6%); 50d above 200d
Momentum: RSI(14) 29.7 | MACD -0.671 vs signal -0.439 (histogram -0.232)
Returns: 1d +0.6% | 5d -1.0% | 1m -9.6% | 3m -1.0%
52-week range: 22.36 - 34.10 (now 68.9% of the way up)
Volatility: ATR(14) 0.48 (1.6% of price) | annualised 20d 20.5%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Commodities Broad Basket
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +13.0% a year | beta to the market 1.04
Cost and size: expense ratio 0.85% | net assets 1.94B
What it is made of: Other 50.0%, Cash 45.2%, Bonds 2.7%, Stocks 2.1%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 41.8%, Brent Crude Future Jan 27 11.0%, Invesco Short Term Treasury ETF 5.8%, Mini Ibovespa Future Dec 26 2.1%
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

```text
Rolled up from the 4 largest holdings, 60.6% of the fund by weight
Ratings by weight: buy n/a | hold n/a | sell n/a (mean n/a on a 1=strong buy to 5=strong sell scale)
Weighted price target: n/a above the current prices
Holdings read: AGPXX, BRNH27, TBLL, WINZ26
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
Share count change: 1 week: +2.4% (45.13M) over 10d | 1 month: +10.0% (174.79M) over 32d
Shares outstanding: 63.13M | fund size: 1.92B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [iShares J.P. Morgan USD Emerging Markets Bond ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc68cfc5be40cf849759c163141081&url=https%3a%2f%2fmarkets.ft.com%2fdata%2fetfs%2ftearsheet%2fsummary%3fs%3dEMB%3aNMQ%3aUSD&c=14444127834652429199&mkt=en-us)  
  <sub>Financial Times, 26h ago</sub>  
  The investment seeks to track the investment results of the J.P. Morgan Emerging Markets Bond Index Global Diversified Core composed of U.S. dollar-denominated, emerging market bonds. The fund will ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 90.63 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 91.73 (-1.2%), 50d 91.87 (-1.4%), 200d 94.67 (-4.3%); 50d below 200d
Momentum: RSI(14) 37.9 | MACD -0.209 vs signal -0.088 (histogram -0.121)
Returns: 1d -0.1% | 5d -1.5% | 1m -0.5% | 3m -4.7%
52-week range: 90.14 - 97.74 (now 6.4% of the way up)
Volatility: ATR(14) 0.48 (0.5% of price) | annualised 20d 7.2%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Emerging Markets Bond
Yield: 5.4%
Credit quality: BBB 33.5%, BB 25.3%, B 19.5%, A 17.7% | US government debt 87.8%
Three-year record: +9.0% a year | beta to the market 1.06
Cost and size: expense ratio 0.39% | net assets 13.57B
What it is made of: Bonds 99.2%, Cash 0.8%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 0.5%
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
Share count change: 1 week: +0.9% (115.32M) over 7d | 1 month: +4.8% (617.01M) over 31d
Shares outstanding: 148.88M | fund size: 13.49B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Junk Bonds, Emerging Markets and Foreign Debt: 3 Monthly Checks and the Risk Behind Them](https://247wallst.com/investing/etf/2026/11/16/junk-bonds-emerging-markets-and-foreign-debt-3-monthly-checks-and-the-risk-behind-them/)  
  <sub>18 hours ago</sub>  
  HYG and EMB skipped January at the last year-end, so retirees budgeting monthly should set aside December cash to cover the gap.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 76.74 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 77.19 (-0.6%), 50d 77.49 (-1.0%), 200d 79.29 (-3.2%); 50d below 200d
Momentum: RSI(14) 39.7 | MACD -0.158 vs signal -0.130 (histogram -0.028)
Returns: 1d +0.0% | 5d -0.6% | 1m -0.1% | 3m -3.7%
52-week range: 76.73 - 81.18 (now 0.1% of the way up)
Volatility: ATR(14) 0.30 (0.4% of price) | annualised 20d 5.4%
Volume: 0.04x the 20-day average
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
Three-year record: +7.5% a year | beta to the market 0.65
Cost and size: expense ratio 0.49% | net assets 17.71B
What it is made of: Bonds 99.3%, Cash 0.5%, Preferred 0.2%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 1.1%
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
Share count change: 1 week: +0.2% (30.37M) over 10d | 1 month: +5.6% (936.73M) over 32d
Shares outstanding: 230.25M | fund size: 17.67B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [iShares Trust - iShares 7-10 Year Treasury Bond ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc685915b24885ae7fe4cad92b4e95&url=https%3a%2f%2fmoney.usnews.com%2finvesting%2fstocks%2fief-ishares-trust-ishares-year-treasury-bond-etf&c=10365585631847091437&mkt=en-us)  
  <sub>U.S. News & World Report, 23h ago</sub>  
  U.S. News compares companies to their industry peers based on a variety of company fundamentals, performance metrics and investor preferences to help you find the right stocks for your investing style ...
- [债券指数ETF-iShares Barclays 7-10年收涨0.22%，成交额7.35亿美元](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc685915b24885ae7fe4cad92b4e95&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fusstock%2fnotice%2f2026-11-17%2fdoc-iniyyrkr5639768.shtml&c=5463462626089568996&mkt=en-us)  
  <sub>新浪财经, 17h ago</sub>  
  11月17日，债券指数ETF-iShares Barclays 7-10年（IEF）收涨0.22%，报90.24美元，成交额7.35亿美元，市值429.54亿美元。 声明：市场有风险，投资需谨慎。本文基于第三方数据库发布，不代表新浪财经观点，任何在本文出现的信息均只作为参考，不构成个人投资建议。如有出入请以实际公告为准。如有疑问，请联系biz@staff.sina.com.cn。

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 90.17 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 91.06 (-1.0%), 50d 90.49 (-0.4%), 200d 93.57 (-3.6%); 50d below 200d
Momentum: RSI(14) 41.6 | MACD -0.047 vs signal 0.126 (histogram -0.173)
Returns: 1d -0.1% | 5d -0.9% | 1m +0.1% | 3m -3.4%
52-week range: 88.92 - 97.99 (now 13.8% of the way up)
Volatility: ATR(14) 0.46 (0.5% of price) | annualised 20d 7.2%
Volume: 0.04x the 20-day average
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
Three-year record: +3.4% a year | beta to the market 1.17
Cost and size: expense ratio 0.15% | net assets 43.53B
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
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 37.8% of open interest (6,095,194 contracts)
Change on the week: +0.3% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +2.2% (929.99M) over 10d | 1 month: +4.2% (1.75B) over 32d
Shares outstanding: 483.61M | fund size: 43.61B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [iShares Russell 2000 (IWM) Sells Glaukos and JFrog on Friday](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc682a780c4fb2b867ec4946153ccd&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2fishares-russell-2000-iwm-sells-110411961.html&c=2152387974579807185&mkt=en-us)  
  <sub>Yahoo Finance, 12h ago</sub>  
  iShares Russell 2000 Index Fund ( IWM) extended a one-sided stretch of ETF activity on Friday, Nov. 13, selling $232.3 million of stock and buying nothing. The fund increased no positions and ...
- [iShares Russell 2000 ETF (IWM) Price Prediction: Small-cap ETF stalls below its short-term averages as selling pressure builds](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc682a780c4fb2b867ec4946153ccd&url=https%3a%2f%2fblockchain.news%2fnews%2f20261116-price-prediction-iwm-small-cap-etf-stalls-below-its&c=10578200440160522315&mkt=en-us)  
  <sub>Blockchain News, 29h ago</sub>  
  Shares Russell 2000 ETF (IWM) is trading at $276.36, just below its short- and medium-term moving averages, while momentum remains soft and Binance ...
- [FESM: Good Track Record, But Limited Upside Now](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc682a780c4fb2b867ec4946153ccd&url=https%3a%2f%2fseekingalpha.com%2farticle%2f4968920-fesm-good-track-record-but-limited-upside-now&c=12357846252456657041&mkt=en-us)  
  <sub>Seeking Alpha, 15h ago</sub>  
  The Fidelity Enhanced Small Cap Core ETF ( FESM ), launched on 12/20/2007 as a mutual fund and converted to an ETF in November 2023, provides exposure to the small-cap segment of the U.S. equity ...
- [Should iShares Core S&P Small-Cap ETF (IJR) Be on Your Investing Radar?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc682a780c4fb2b867ec4946153ccd&url=https%3a%2f%2fwww.ainvest.com%2fnews%2fishares-core-small-cap-etf-ijr-investing-radar-2611%2f&c=13716145928164403245&mkt=en-us)  
  <sub>ainvest, 10h ago</sub>  
  The iShares Russell 2000 ETF (IWM) and the Vanguard Morningstar Small-Cap ETF (VB) track a similar index. While iShares Russell 2000 ETF has $75.01 billion in assets, Vanguard Morningstar Small-Cap ...
- [iShares Russell 2000 Value ETF (IWN) Buys $50.9 Million More Black Hills on Friday](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc682a780c4fb2b867ec4946153ccd&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2fishares-russell-2000-value-etf-110446563.html&c=17976331474145119423&mkt=en-us)  
  <sub>Yahoo Finance, 12h ago</sub>  
  The fund added $69.6 million in new positions across 1,318 holdings, led by a $50.9 million increase in Black Hills Corp.
- [Monday’s Charts – Technicals Deteriorate as the Nasdaq Tests Its Uptrend Line](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc682a780c4fb2b867ec4946153ccd&url=https%3a%2f%2fpro.thestreet.com%2fmarket-commentary%2fmondays-charts-technicals-deteriorate-as-the-nasdaq-tests-its-uptrend-line&c=12817011125701219932&mkt=en-us)  
  <sub>TheStreet Pro, 23h ago</sub>  
  The Nasdaq Composite and Russell 2000 closed on uptrend lines, while the VIX jumps and gold, copper, and bitcoin fall again.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 272.44 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 278.29 (-2.1%), 50d 279.86 (-2.7%), 200d 279.53 (-2.5%); 50d above 200d
Momentum: RSI(14) 42.4 | MACD -1.139 vs signal -0.744 (histogram -0.395)
Returns: 1d -0.2% | 5d -2.9% | 1m +0.4% | 3m -9.7%
52-week range: 229.11 - 305.09 (now 57.0% of the way up)
Volatility: ATR(14) 4.67 (1.7% of price) | annualised 20d 25.0%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Small Blend
What it holds: P/E 16.28 | P/B 1.99 | P/S 1.23 | 3y earnings growth n/a
Yield: 1.0%
Three-year record: +19.3% a year | beta to the market 1.26
Cost and size: expense ratio 0.19% | net assets 75.49B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Glaukos Corp 0.5%, BrightSpring Health Services Inc 0.4%, JFrog Ltd Ordinary Shares 0.3%, Twist Bioscience Corp 0.3%, Moog Inc Class A 0.3%
Sector mix: Healthcare 21.0%, Financial services 18.2%, Technology 14.0%, Industrials 12.7%
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
Rolled up from the 5 largest holdings, 1.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.45 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.2% above the current prices
Holdings read: GKOS, BTSG, FROG, TWST, MOG-A
Recent rating changes among them:
  - GKOS: 2026-10-29 HC Wainwright & Co.: main, Buy -> Buy
  - BTSG: 2026-11-03 Guggenheim: main, Buy -> Buy
  - FROG: 2026-11-12 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MOG-A: 2026-10-13 JP Morgan: main, Overweight -> Overweight
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 10.1% of open interest (440,576 contracts)
Change on the week: +2.2% of open interest
Crowding: 77% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 281.05M | fund size: 76.57B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 102.68 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 103.86 (-1.1%), 50d 103.54 (-0.8%), 200d 107.27 (-4.3%); 50d below 200d
Momentum: RSI(14) 37.9 | MACD -0.146 vs signal 0.034 (histogram -0.180)
Returns: 1d -0.1% | 5d -1.2% | 1m -0.2% | 3m -3.7%
52-week range: 101.83 - 112.05 (now 8.3% of the way up)
Volatility: ATR(14) 0.55 (0.5% of price) | annualised 20d 7.0%
Volume: 0.02x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Corporate Bond
Yield: 4.8%
Credit quality: A 46.7%, BBB 40.5%, AA 11.9%, AAA 0.9%
Three-year record: +4.8% a year | beta to the market 1.32
Cost and size: expense ratio 0.14% | net assets 32.00B
What it is made of: Bonds 99.2%, Cash 0.8%, Convertible 0.0%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 0.5%
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
Share count change: 1 week: +1.8% (553.33M) over 10d | 1 month: +12.9% (3.66B) over 32d
Shares outstanding: 311.46M | fund size: 31.98B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Invesco S&P 500 Equal Weight ETF (RSP)](https://ca.finance.yahoo.com/quote/RSP/options/?date=1796947200&straddle=false&type=all)  
  <sub>19 hours ago</sub>  
  View the basic RSP option chain and compare options of Invesco S&P 500 Equal Weight ETF on Yahoo Finance.
- [RDVI: The Dividend ETF Beating The S&P 500, And Almost Nobody Knows How (Rating Upgrade)](https://seekingalpha.com/article/4968925-rdvi-the-dividend-etf-beating-the-s-and-p-500-and-almost-nobody-knows-how)  
  <sub>7 hours ago</sub>  
  In my opinion, the FT Vest Rising Dividend Achievers Target Income ETF offers a balanced approach by overwriting roughly 20 percent of its portfolio,...
- [Is an Equal-Weight S&P 500 Fund Safer Right Now Than the One You Own?](https://www.google.com/goto?url=CAESsAEBxCJF1xcfyR0WdCCF0Kg0qT1YYf0gaXre-5oFCDQqR-NZMsEdXNaX8yRG7Gqfg03wrCWmuab4VicYuXeuizAbjFFPqISYHjF0TvIiGKlBGm0sIJOr8aJbABAryDuRdJn0IqRf2rAugcoreZl2YcJAwcDrf3lJRFMIYXUbdqFLOyvFjQFm-Tc4SHptcWNarrDrdfOdorLlJIE8Xd-YcgCi26o753GOyNxBTfU3QbY7tA&gsessionid=o0bjgfltsrVRN0UA5_2S4XCC3oR_jUAr-1DKyYvSnTSAMsERXj3dhQ)  
  <sub>24 hours ago</sub>  
  Many investors own S&P 500 index funds because they view them as a diversified investment. In one sense, it's true, since you'll have exposure to about 500...
- [Markets Shrug Off Nvidia Turmoil, For Now](https://www.google.com/goto?url=CAESjgEBxCJF1_hXp659T9FRGPgwgHHuVHr6VuQhHrOfQIfvQES1h6mAwuKDBc70KXL580oEEtnyTIUdx87chyBxlglcxfK45r9v5hhx2IxI5mfSzw8kvfJz1pmvZOOZk5ZmyRoxOCCsyHggfADCSW_4t0dOZefFnebeEzEmDeKvS3Uxz8pL6lRV1CpaFMT9l1uC&gsessionid=o0bjgfltsrVRN0UA5_2S4XCC3oR_jUAr-1DKyYvSnTSAMsERXj3dhQ)  
  <sub>24 hours ago</sub>  
  Fears of an AI bubble have lingered on Wall Street for some time, and the Nvidia turmoil that erupted into public view last week appeared to open the door...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 218.50 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 219.06 (-0.3%), 50d 215.02 (+1.6%), 200d 209.06 (+4.5%); 50d above 200d
Momentum: RSI(14) 51.1 | MACD 1.363 vs signal 1.546 (histogram -0.184)
Returns: 1d -0.2% | 5d -1.1% | 1m +2.4% | 3m -1.6%
52-week range: 182.18 - 223.33 (now 88.3% of the way up)
Volatility: ATR(14) 2.59 (1.2% of price) | annualised 20d 17.7%
Volume: 0.05x the 20-day average
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
Three-year record: +18.2% a year | beta to the market 0.80
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
Weighted price target: -3.7% above the current prices
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
Direction: money coming in (1 month)
Share count change: 1 week: -1.9% (-1.95B) over 10d | 1 month: +1.1% (1.07B) over 32d
Shares outstanding: 455.21M | fund size: 99.46B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 81.25 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 81.43 (-0.2%), 50d 81.32 (-0.1%), 200d 82.02 (-0.9%); 50d below 200d
Momentum: RSI(14) 43.9 | MACD -0.033 vs signal 0.007 (histogram -0.040)
Returns: 1d +0.0% | 5d -0.1% | 1m -0.1% | 3m -1.0%
52-week range: 81.05 - 83.18 (now 9.2% of the way up)
Volatility: ATR(14) 0.13 (0.2% of price) | annualised 20d 2.4%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Short Government
Yield: 3.6%
Credit quality: AA 100.0% | US government debt 99.8%
Three-year record: +3.9% a year | beta to the market 0.25
Cost and size: expense ratio 0.15% | net assets 27.44B
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
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 33.5% of open interest (4,489,282 contracts)
Change on the week: -1.0% of open interest
Crowding: 77% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.6% (166.33M) over 10d | 1 month: +4.4% (1.17B) over 32d
Shares outstanding: 338.12M | fund size: 27.47B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [ETFs, Swaps, Perps Offer Back Door to Anthropic ‘Stock’ Pre-IPO](https://www.bloomberg.com/news/articles/2026-11-17/etf-cef-swap-perp-investors-get-slice-of-anthropic-before-ipo?srnd=homepage-americas)  
  <sub>2 hours ago</sub>  
  Anthropic PBC's much-anticipated Nasdaq debut isn't expected until later this week, but retail traders are already finding ways to get a piece of the AI...
- [Bitcoin stalls below $65,000 after weekend selloff as Nvidia earnings loom](https://www.coindesk.com/markets/2026/11/17/bitcoin-remains-penned-in-near-usd64-000-even-as-etf-outflow-streak-ends)  
  <sub>3 hours ago</sub>  
  Bitcoin (BTC) is down a further 1.0% since midnight UTC at around $64200, with its bounce from the weekend selloff stalled and pressure building on all...
- [iShares $ TIPS 0-5 ETF GBP H Dist (TI5G.L) Seasonal returns chart](https://www.google.com/goto?url=CAEScwHEIkXXlymyoDHVhlktzxv2p0CLHz0l3G4ZfkNXWRrhUIB0p8KDrvYTs6ReSobiVS5jGK3wO_Gfw89QYBoF4kijyts8JeX-FGNLUbAgyesedBDqHzC6y_zWHBZ5YL48chWvR-3juOGPJRiUX-HHBXAGO98&gsessionid=59e8nQIWQvJUstjE4GgrbHrFeQoNRGeta4wTaFfZg_rg6i4NrfrS3Q)  
  <sub>15 hours ago</sub>  
  iShares $ TIPS 0-5 ETF GBP H Dist (TI5G.L) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [iShares USD TIPS UCITS ETF (TPSAA.XC) Company Profile & Facts - Yahoo Finance](https://www.google.com/goto?url=CAEScQHEIkXX1-yqJaznmKF1ofaFaqu-S32U-Ans9SLcRrEZEqeB2Bk1PMoBSRaMRLmwOEN42UNypyXbEq-L8u-PtNuSPPa6ws6J7Fa3ZdNIdtNxlGlbh_ZZJFN8TkCd0hlFAG2cy7B8a97J57N-XkV__8GS&gsessionid=59e8nQIWQvJUstjE4GgrbHrFeQoNRGeta4wTaFfZg_rg6i4NrfrS3Q)  
  <sub>16 hours ago</sub>  
  See the company profile for iShares USD TIPS UCITS ETF (TPSAA.XC) including business summary, industry/sector information, number of employees,...
- [BMO Short-Term US TIPS Index ETF (USD Units) (ZTIP-U.TO) Seasonal returns chart](https://www.google.com/goto?url=CAESdgHEIkXXQaLFPE3OX8JPWGHOm-TBVRfN6LBkBu12egq6SGYgyQZP3RbQOnIIOGECeNdsSa62oO-IR2jw81RAtjTh085gORLJnVNwFkX7KrHqKrC0H1fUQZlCUYa8LyehGN4etdWvp1VZeZfbqt-Bj1j9eqvtvQY&gsessionid=59e8nQIWQvJUstjE4GgrbHrFeQoNRGeta4wTaFfZg_rg6i4NrfrS3Q)  
  <sub>19 hours ago</sub>  
  BMO Short-Term US TIPS Index ETF (USD Units) (ZTIP-U.TO) seasonal returns chart provides the mean and median returns by month to inform your investment...
- [VTIP: 2x Margin Over Inflation Of A Year Ago Is Attractive (NASDAQ:VTIP)](https://www.google.com/goto?url=CAESsgEBxCJF15ALFyayUAtoC3mYoN1dZwrnW4R2Px-b9gac3rpER79hy_PZ4VVpKBXPyCnkLt87omOoFQvJhDVk_IK7l2RxO_57g19XWPLe60X02_clc6lkzBR_t4ieR642oOMARVEKBXboFjga29BwBEM4gjX_LQaTIuzmHdUBiAAOAAxeFQHvRLQPxZ3_GyQfK9JPhuQ5K1CNHWma0tMMP6gPY6irRhEv7Dopmo5P2UKZyvxa&gsessionid=59e8nQIWQvJUstjE4GgrbHrFeQoNRGeta4wTaFfZg_rg6i4NrfrS3Q)  
  <sub>18 hours ago</sub>  
  Vanguard's VTIP holds the Treasury Inflation-Protected Securities due within five years for a 0.03% fee. I compare it with other short-term TIPS funds and...
- [Morgan Stanley Enters Europe’s Active ETF Market With Four Funds](https://www.google.com/goto?url=CAESwAEBxCJF18uXlwWpJXXx902hl1nPrnRnzbkIr2i4mMdvUH8uuH92rh6EeGd3IorB39tiDbt3WI6ISoMBbWb95V86oTSjzv1sglwo3ubBfkxdungfag9QyRGrltlTnG04AD7JRWINFXLPirn-o7hATjyzsF3si0zuk_UF7bC_5EOyMBKhJwtcrSnR0sY4sH0_ARR7AGzl_OOa0emFit0d7-HnUSWgFOXGx-xce_crFlnFE9e7wyua5fUkpAS1XPVVRTY&gsessionid=59e8nQIWQvJUstjE4GgrbHrFeQoNRGeta4wTaFfZg_rg6i4NrfrS3Q)  
  <sub>10 hours ago</sub>  
  Morgan Stanley's investment manager has launched four actively-managed exchange-traded funds in Europe, joining rivals in a bid to benefit from the...
- [Want to Play Nvidia Earnings Without Buying the Stock? This $64B ETF Makes NVDA Its Largest Holding](https://www.google.com/goto?url=CAESvAEBxCJF1z9g__Vanu9HrfhBFpJ8VHbtn0uZalIfDGOYcpT2ORh7mhxPiAY51mrO5zSG6ff_OD0ELzfnktXh72F18_1Ua8J-iLGgJqEWl7ywynt0-8lZ1TUg_D_weqYmV2Q5fPLYs7FW65RKbMPOEtHeQxG9SCCf5GRWS7kXnqYvZjra6uD3iFfXAWMHlOTkvyvkW81Uj8sMCPY-nRLFfva8ctB8j9-VYtaKloNkvS7jrlMon6EJDve82z0weA&gsessionid=59e8nQIWQvJUstjE4GgrbHrFeQoNRGeta4wTaFfZg_rg6i4NrfrS3Q)  
  <sub>3 hours ago</sub>  
  Nvidia ($NVDA) will report its fiscal third-quarter earnings after the market closes today, November 17. Investors who want exposure to the chipmaker...
- [3 ETFs with Room for 10% or More Gains, According to AI Analyst](https://www.google.com/goto?url=CAESmAEBxCJF12ppjfXcX7ZSPFH5SEhvlQw-ILccZJ_dx_NUcmSRqV1pONaje3KeYnfCOseJN2yhEATmimLuQoATzGr2DPZeFClj3kvNiRcBZU1hGTayeTbvYRJJKqR6dc2DmhsAj2Py3Q04wI8DILhGW__hpC_eQgLoTmnbhlQD2WKmf3Jg16eF6FC06mH9VH04P5B80P1m-WGHMQ&gsessionid=59e8nQIWQvJUstjE4GgrbHrFeQoNRGeta4wTaFfZg_rg6i4NrfrS3Q)  
  <sub>18 hours ago</sub>  
  Exchange-traded funds (ETFs) offer investors broad exposure to leading companies through a single route. However, the market is crowded with thousands of...
- [Invesco QQQ Trust ETF Falls as Nvidia Crisis Drags Down Tech Stocks](https://www.google.com/goto?url=CAESngEBxCJF132dZdC-sfZ0klak-9evveARdz0IWsUwUS3MDxNaDKzilLJl9b4tq4MFlzJtLbefieHKMZJhgqUGw3f_SHpitct7KgH2CKYs9m0mHX-qSFkKXo5NFs_6EIfl9EdErEZEHtH0GKPCr-86WIc5zu1M0jvWCZ-NUWXLuCKd0yf8TadyQgcVoWw0etDZP_1hCFGas8vebPLUkvimyA&gsessionid=59e8nQIWQvJUstjE4GgrbHrFeQoNRGeta4wTaFfZg_rg6i4NrfrS3Q)  
  <sub>18 hours ago</sub>  
  Invesco QQQ Trust ETF ($QQQ), which tracks the Nasdaq-100 index (NDX), fell 3% to about $662 on Monday afternoon. This came as the leadership crisis at U.S....

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 104.57 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 105.82 (-1.2%), 50d 105.31 (-0.7%), 200d 108.58 (-3.7%); 50d below 200d
Momentum: RSI(14) 32.9 | MACD -0.203 vs signal 0.012 (histogram -0.215)
Returns: 1d +0.0% | 5d -0.7% | 1m -0.7% | 3m -2.7%
52-week range: 103.98 - 111.88 (now 7.5% of the way up)
Volatility: ATR(14) 0.36 (0.3% of price) | annualised 20d 4.6%
Volume: 0.32x the 20-day average
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
Three-year record: +3.6% a year | beta to the market 0.73
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
Direction: money coming in (1 month)
Share count change: 1 week: +1.6% (232.86M) over 10d | 1 month: +2.9% (415.39M) over 32d
Shares outstanding: 140.16M | fund size: 14.66B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Why 5% Bond Yields Are More Attractive Than The S&P 500, And Will Be For A While (SPY)](https://seekingalpha.com/article/4968770-why-5-percent-bond-yields-are-more-attractive-than-sp500-and-will-be-for-while)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  The bull case for hedged bonds: a 5% target baseline offers a head start as 5-10 year S&P 500 returns may be closer to 0% than 15%.
- [Options Whale Alert: $4.72M Bullish Long Call Opened on $TLT](https://www.moomoo.com/news/post/1004797254/options-whale-alert-4-72m-bullish-long-call-opened-on)  
  <sub>Moomoo, 15 hours ago</sub>  
  iShares20+ Year Treasury Bond ETF(TLT.US)$ closed flat 0.00% at $79.38. A trader bought 54285 Feb 19, 2027 $83.00 calls to open a Long Call.
- [Tudor adds Iridium, exits Teck, boosts SPY stakes among Q3 trades (IRDM:NASDAQ)](https://www.google.com/goto?url=CAESogEBxCJF10NlLFhxVrGoGq42iOzVsWe0II-Gvaf3jLvhVnBqC0EFsh-VJipc2Wk9ewXwm3VCrCUC9xn6c22UktDakGyhITuhRXvHlcSd8woJQi3vM0qEHl6fsCoB1bvgA4geRL31B32oUsMRRTOTyiBahgbWNNrGJfex6Wpmxevv4eynJMhTYCWSBQcgM1ai0OSyOQe_PcL9xDwIGuptkXbWaQk&gsessionid=pD7YRM-2d6ErmMKAUw_EZJvAVSr1187LYzNHtTS47eyTQaciIMFQsQ)  
  <sub>Seeking Alpha, 15 hours ago</sub>  
  Paul Tudor Jones' Tudor investment's 13F shows a new 3.95M-share Iridium Communications stake worth $189.3M, SPY up to 1.51M shares and IVV down to 322.8K.
- [Bank of America's Q3 Holdings Revealed: Nvidia Stays on Top, JPMorgan Stake Cut by Nearly 30%](https://www.google.com/goto?url=CAESgAEBxCJF18L1gyqtgJwJacW9a5N124Cx7jFuPeTtgybN9orvgmP2hNL8x2PF5URi418ersw2q2lAEZAk2W9a0NdpYLMA1RABKETFbimIImw3TEWFcRIjToF2GZ_Aw0LU4Fna6--q2WebpwP_YDiIbab9yvKzNu8IzJ-UGLWodxPEeA&gsessionid=pD7YRM-2d6ErmMKAUw_EZJvAVSr1187LYzNHtTS47eyTQaciIMFQsQ)  
  <sub>BigGo Finance, 6 hours ago</sub>  
  13F filings disclosed by the U.S. Securities and Exchange Commission show that, as of September 30, 2026, Bank of America's total holdings in the…
- [From November OPEX to Early December: A Strong Record With a Lopsided Average](https://www.google.com/goto?url=CAESpgEBxCJF14Eyrc3IWfPAIutHjeIO9eFCz_07ZK57ZuO2rt1FPMVAlWeUgaHMHo3zqOcXmD0eU6nirEXHy1dshSCFdmbpVbCraHBozabHy9pbh_ocDeKlviyFGcubqRN-FM4MC43KB7ziHqFvvd1oiFAzHT-aUFnptkV84GsqN1W8k9hFYLB35gCTXxeuefQr8GkoXPjaitnoIKehuzj01Hm2BxqkMecz&gsessionid=pD7YRM-2d6ErmMKAUw_EZJvAVSr1187LYzNHtTS47eyTQaciIMFQsQ)  
  <sub>See It Market, 12 hours ago</sub>  
  November options expiration lands on Friday, November 20 this year. Historically, the two weeks that follow have been one of the more consistent stretches...
- [BofA Q3 Portfolio: NVIDIA Remains Number One, Apple Reduced, JPMorgan Cut by Nearly 30%](https://www.google.com/goto?url=CAESrgEBxCJF10V-NqNJXVXGOwIYBm1PCUFjm09jtdPAJ8VuvpRe3ajB5wuEkVwV1KPefpEtXfUUEa8PXlKdSV9JMLFtKyc-F4v_IC8zDig4MVzmdCE6rv2Si04-HpujI7sJBB2PK3QFBj7vm9q1sxP1kVp4qvCDWAuQStKVNdQ5-DpMES_m_LLJRTv6RtmfEbR_kGhNeoWZwH2BWrc-gV9QbktGLD0pHkhHwr5yfOGq-2g&gsessionid=pD7YRM-2d6ErmMKAUw_EZJvAVSr1187LYzNHtTS47eyTQaciIMFQsQ)  
  <sub>KuCoin, 7 hours ago</sub>  
  Smart Finance APP learned that, according to disclosures by the U.S. Securities and Exchange Commission (SEC), Bank of America ( BAC.
- [Bank of America's Q3 Holdings: NVIDIA (NVDA.US) Remains Top Position, Apple (AAPL.US) Reduced, JPMorgan (JPM.US) Cut by Nearly 30%](https://www.google.com/goto?url=CAESoAEBxCJF194-L-UcHzcdk7SM_nIdlIprHjCE0g29_qSVO57_8AhLiTvvTH7Ongj1kMYyQfmP3CCAoIQnOAsq71f4tNnIxva9tdEgDLkpqBFo5-YUot820pXTKzb0iL_-OqoEm2U7-KTOzuf9ip_VoVuLQom2WORTdzFOdOLsjjpUz5qly9LidU1Pou3PpJhkQGp3ll7NXS20lKnP2r5YEG5H&gsessionid=pD7YRM-2d6ErmMKAUw_EZJvAVSr1187LYzNHtTS47eyTQaciIMFQsQ)  
  <sub>Moomoo, 7 hours ago</sub>  
  Accordingto disclosures by the U.S. Securities and Exchange Commission (SEC), Bank of America (BAC.US) filed its third-quarter holdings report (13F) as of...
- [Dow, S&P 500, Nasdaq Futures Mixed Ahead Of Much-Anticipated Nvidia Earnings, Anthropic IPO: SLS, BABA, JPM, OMER In Focus](https://www.google.com/goto?url=CAES9QEBxCJF1_LmIUvKCpErmtI8zismXvAN6RJmT5MTSvlLHaynmRjwSwnd31Wknk53DxJi9S1KcNJqvofksapj7YNhC-Q80Qfr_eV4pN4F5jjw-aeGO8lRrgf8DGJZOQcz2h0rid7s2Fd6MUgJ3WiArBGqI4BdU25yiRpVMuS1yqBYI6RMPGykv2CWObPdmGcuyPqbpiE_VnofsQPQQEzWmzkD-8WrDVn_7VkoEj1I-OVK6XAt6ULf_pkfasH-x44MQxIED1bP5XEh7Uiw-VuznnPciLDDrnK975eyGmIUZhM_r3ns6eETNO-MuTA6K1_in3ys4Se1FQ&gsessionid=pD7YRM-2d6ErmMKAUw_EZJvAVSr1187LYzNHtTS47eyTQaciIMFQsQ)  
  <sub>Stocktwits, 11 hours ago</sub>  
  Anthropic's public listing, expected on Wednesday, could top $1.4 trillion in valuation, stoking a key test for Wall Street's AI appetite.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 79.31 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 81.05 (-2.1%), 50d 80.10 (-1.0%), 200d 84.22 (-5.8%); 50d below 200d
Momentum: RSI(14) 38.5 | MACD -0.108 vs signal 0.205 (histogram -0.313)
Returns: 1d -0.1% | 5d -1.9% | 1m -0.2% | 3m -4.5%
52-week range: 77.11 - 90.82 (now 16.0% of the way up)
Volatility: ATR(14) 0.73 (0.9% of price) | annualised 20d 11.8%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Long Government
Yield: 4.8%
Credit quality: AA 100.0% | US government debt 99.5%
Three-year record: +0.9% a year | beta to the market 2.30
Cost and size: expense ratio 0.15% | net assets 47.52B
What it is made of: Bonds 99.5%, Cash 0.5%
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
Contract: ULTRA UST BOND - CHICAGO BOARD OF TRADE (positions as of 2026-11-10, published the following Friday)
Large speculators: net short 33.9% of open interest (2,403,991 contracts)
Change on the week: -0.7% of open interest
Crowding: 48% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 109.70M | fund size: 8.70B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Play US dollar's biggest weekly gain in two months with these ETFs](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc6903872a454fad9234d7d9b60f1f&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2feconomy%2fplay-us-dollar-s-biggest-weekly-gain-in-two-months-with-these-etfs%2far-AA2hyOOj&c=5398108913179603099&mkt=en-us)  
  <sub>Zacks Investment Research on MSN, 32h ago</sub>  
  The U.S. dollar logged its strongest weekly gain in two months on Friday, hovering near a 19-month high as stronger-than-expected inflation data and hawkish comments from Federal Reserve officials ...
- [Invesco DB US Dollar Index Bullish Fund](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc6903872a454fad9234d7d9b60f1f&url=https%3a%2f%2fmarkets.ft.com%2fdata%2fetfs%2ftearsheet%2fsummary%3fs%3dUUP%3aASE&c=5312942789168424140&mkt=en-us)  
  <sub>FT Markets, 26h ago</sub>  
  The performance data shown in tables and graphs on this page is calculated in USD of the fund/index/average (as applicable), on a Bid To Bid / Nav to Nav basis, with gross dividends re-invested on ...
- [美元ETF-PowerShares DB收涨0.2%，成交额5669.86万美元](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc6903872a454fad9234d7d9b60f1f&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fusstock%2fnotice%2f2026-11-17%2fdoc-iniyyvsr2324621.shtml&c=4675033692704226171&mkt=en-us)  
  <sub>新浪财经, 23h ago</sub>  
  11月17日，美元ETF-PowerShares DB（UUP）收涨0.2%，报29.56美元，成交额5669.86万美元，市值4.51亿美元。 声明：市场有风险，投资需谨慎。本文基于第三方数据库发布，不代表新浪财经观点，任何在本文出现的信息均只作为参考，不构成个人投资建议。如有出入请以实际公告为准。如有疑问，请联系biz@staff.sina.com.cn。

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 29.57 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 29.12 (+1.5%), 50d 28.86 (+2.5%), 200d 28.06 (+5.4%); 50d above 200d
Momentum: RSI(14) 70.9 | MACD 0.173 vs signal 0.126 (histogram 0.047)
Returns: 1d +0.0% | 5d +1.4% | 1m +2.0% | 3m +6.1%
52-week range: 26.47 - 29.57 (now 100.0% of the way up)
Volatility: ATR(14) 0.12 (0.4% of price) | annualised 20d 5.3%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Trading--Miscellaneous
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +4.4% a year | beta to the market -7.93
Cost and size: expense ratio 0.75% | net assets 481.36M
What it is made of: Cash 100.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 49.5%
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
Rolled up from the 1 largest holdings, 49.5% of the fund by weight
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
Contract: USD INDEX - ICE FUTURES U.S. (positions as of 2026-11-10, published the following Friday)
Large speculators: net long 5.5% of open interest (51,440 contracts)
Change on the week: -1.2% of open interest
Crowding: 82% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -1.2% (-5.63M) over 7d | 1 month: +10.3% (45.18M) over 31d
Shares outstanding: 16.33M | fund size: 482.83M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Morgan Stanley’s Europe Call Puts These ETFs on the Radar - Vanguard FTSEEuropean ETF (ARCA:VGK)](https://www.benzinga.com/etfs/emerging-market-etfs/26/11/63314882/wall-street-looks-beyond-us-stocks-morgan-stanleys-europe-call-puts-these-etfs-on-the-radar)  
  <sub>Benzinga, 19 hours ago</sub>  
  Morgan Stanley sees 15% upside for European stocks by 2027, putting European ETFs in focus as investors diversify beyond US equities.
- [France protests: Unions call for nationwide public-sector strike](https://seekingalpha.com/news/4673465-france-protests-unions-call-for-nationwide-public-sector-strike)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  France's third nationwide public-sector strike since September is expected Tuesday, with up to 300000 people protesting for across-the-board pay rises.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 87.39 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 88.06 (-0.8%), 50d 87.79 (-0.5%), 200d 87.96 (-0.7%); 50d below 200d
Momentum: RSI(14) 46.5 | MACD 0.261 vs signal 0.285 (histogram -0.024)
Returns: 1d -0.7% | 5d -2.5% | 1m +1.1% | 3m -5.2%
52-week range: 77.90 - 93.19 (now 62.1% of the way up)
Volatility: ATR(14) 1.07 (1.2% of price) | annualised 20d 20.3%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Europe Stock
What it holds: P/E 17.26 | P/B 2.24 | P/S 1.59 | 3y earnings growth n/a
Yield: 2.9%
Three-year record: +18.7% a year | beta to the market 0.88
Cost and size: expense ratio 0.06% | net assets 37.08B
What it is made of: Stocks 99.0%, Cash 0.7%, Other 0.3%
Largest holdings: ASML Holding NV 4.5%, HSBC Holdings PLC 2.2%, Roche Holding AG Ordinary Shares new 1.9%, Shell PLC 1.8%, Novartis AG Registered Shares 1.7%
Sector mix: Financial services 25.4%, Industrials 19.5%, Healthcare 12.1%, Technology 9.4%
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
Rolled up from the 5 largest holdings, 12.1% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 85.7% | hold 14.3% | sell 0.0% (mean 2.04 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.1% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, SHEL.L, NOVN.SW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-11-10, published the following Friday)
Large speculators: net long 2.8% of open interest (506,737 contracts)
Change on the week: +5.4% of open interest
Crowding: 87% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -0.8% (-307.17M) over 10d | 1 month: -3.2% (-1.22B) over 32d
Shares outstanding: 416.75M | fund size: 36.42B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [ETFs Investing in Banco Bradesco SA Pfd Stocks](https://www.tradingview.com/symbols/HAN-BRE/etfs/)  
  <sub>TradingView, 23 hours ago</sub>  
  Explore funds investing in BRE in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 54.56 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 56.19 (-2.9%), 50d 58.28 (-6.4%), 200d 58.28 (-6.4%); 50d below 200d
Momentum: RSI(14) 36.5 | MACD -0.806 vs signal -0.813 (histogram 0.007)
Returns: 1d -0.5% | 5d -3.4% | 1m -6.0% | 3m -9.1%
52-week range: 52.42 - 61.44 (now 23.7% of the way up)
Volatility: ATR(14) 0.89 (1.6% of price) | annualised 20d 24.6%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Diversified Emerging Mkts
What it holds: P/E 16.13 | P/B 2.13 | P/S 1.85 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +15.8% a year | beta to the market 0.78
Cost and size: expense ratio 0.06% | net assets 153.78B
What it is made of: Stocks 95.8%, Cash 4.0%, Other 0.1%, Preferred 0.0%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 15.7%, Tencent Holdings Ltd 2.8%, Alibaba Group Holding Ltd Ordinary Shares 2.1%, MediaTek Inc 1.9%, Delta Electronics Inc 0.9%
Sector mix: Technology 33.8%, Financial services 19.5%, Consumer cyclical 9.3%, Industrials 7.5%
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
Rolled up from the 5 largest holdings, 23.5% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.32 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +65.5% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 2308.TW
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 1.42B | fund size: 77.37B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Argentina (ARGT) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [ARGT: Argentina Is A Great Opportunity, But Beware The Political Risk](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc6b06d10c47629723bf9685b222f7&url=https%3a%2f%2fseekingalpha.com%2farticle%2f4968980-argt-argentina-is-a-great-opportunity-but-beware-the-political-risk&c=2998249418644975549&mkt=en-us)  
  <sub>Seeking Alpha, 12h ago</sub>  
  Analyst calls ARGT a political bet to size accordingly: the ETF is down 28% from its January high as country risk drives the fall.
- [Argentina Stocks Fall 4.3% as Banks Slide | Argentina Market Report, Nov 16](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc6b06d10c47629723bf9685b222f7&url=https%3a%2f%2fwww.riotimesonline.com%2fargentina-markets-merval-peso-monday-november-16-2026%2f&c=4724352897350946780&mkt=en-us)  
  <sub>The Rio Times, 21h ago</sub>  
  Argentina's Merval fell 4.3% to 81,476 on Monday as banks slid and country risk rose to about 855 points. The peso held near 1,550 per US dollar.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 71.19 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 78.13 (-8.9%), 50d 85.23 (-16.5%), 200d 90.64 (-21.5%); 50d below 200d
Momentum: RSI(14) 26.1 | MACD -4.123 vs signal -3.725 (histogram -0.398)
Returns: 1d +0.9% | 5d -3.4% | 1m -18.1% | 3m -22.1%
52-week range: 70.55 - 102.94 (now 2.0% of the way up)
Volatility: ATR(14) 2.09 (2.9% of price) | annualised 20d 34.4%
Volume: 0.12x the 20-day average
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
Three-year record: +23.9% a year | beta to the market 0.44
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.60 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +68.2% above the current prices
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
Share count change: 1 week: +0.2% (1.38M) over 7d | 1 month: +1.9% (11.24M) over 31d
Shares outstanding: 8.41M | fund size: 598.55M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 110.38 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 115.45 (-4.4%), 50d 119.24 (-7.4%), 200d 122.80 (-10.1%); 50d below 200d
Momentum: RSI(14) 39.0 | MACD -2.366 vs signal -2.100 (histogram -0.266)
Returns: 1d +0.8% | 5d -3.8% | 1m -7.8% | 3m -10.3%
52-week range: 99.40 - 137.69 (now 28.7% of the way up)
Volatility: ATR(14) 2.38 (2.2% of price) | annualised 20d 37.0%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.09 | P/B 2.45 | P/S 2.45 | 3y earnings growth n/a
Yield: 1.6%
Three-year record: +32.9% a year | beta to the market 0.98
Cost and size: expense ratio 0.59% | net assets 838.23M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Teva Pharmaceutical Industries Ltd 12.6%, Bank Leumi Le-Israel BM 8.6%, Bank Hapoalim BM 7.8%, Elbit Systems Ltd 5.6%, Tower Semiconductor Ltd 5.1%
Sector mix: Financial services 34.6%, Technology 18.0%, Healthcare 13.1%, Industrials 10.8%
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.00 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.5% above the current prices
Holdings read: TEVA.TA, LUMI.TA, POLI.TA, ESLT.TA, TSEM.TA
Recent rating changes among them:
  - TEVA.TA: 2026-11-12 Piper Sandler: main, Overweight -> Overweight
  - ESLT.TA: 2026-10-05 Jefferies: main, Hold -> Hold
  - TSEM.TA: 2026-11-03 Wedbush: main, Neutral -> Neutral
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
Shares outstanding: 2.55M | fund size: 281.47M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 43.27 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 43.73 (-1.1%), 50d 44.15 (-2.0%), 200d 40.75 (+6.2%); 50d above 200d
Momentum: RSI(14) 45.8 | MACD -0.119 vs signal -0.140 (histogram 0.021)
Returns: 1d -1.1% | 5d -1.1% | 1m -1.9% | 3m -3.0%
52-week range: 32.56 - 45.76 (now 81.1% of the way up)
Volatility: ATR(14) 0.68 (1.6% of price) | annualised 20d 25.0%
Volume: 0.02x the 20-day average
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
Three-year record: +36.4% a year | beta to the market 0.85
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
Weighted price target: +7.0% above the current prices
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
Share count change: 1 week: -2.7% (-28.37M) over 7d | 1 month: +23.2% (190.42M) over 31d
Shares outstanding: 23.35M | fund size: 1.01B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error response body was rejected) (Bing's feed, direct: 3 headline(s), none naming EPOL)

### Australia (EWA) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 28.37 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 29.26 (-3.0%), 50d 28.92 (-1.9%), 200d 29.00 (-2.2%); 50d below 200d
Momentum: RSI(14) 38.6 | MACD -0.035 vs signal 0.084 (histogram -0.119)
Returns: 1d -0.7% | 5d -3.5% | 1m -1.6% | 3m -5.3%
52-week range: 24.95 - 30.43 (now 62.4% of the way up)
Volatility: ATR(14) 0.35 (1.2% of price) | annualised 20d 17.5%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 20.37 | P/B 2.63 | P/S 3.35 | 3y earnings growth n/a
Yield: 2.9%
Three-year record: +14.5% a year | beta to the market 0.94
Cost and size: expense ratio 0.50% | net assets 1.25B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: BHP Group Ltd 14.3%, Commonwealth Bank of Australia 13.7%, National Australia Bank Ltd 6.3%, Westpac Banking Corp 6.2%, ANZ Group Holdings Ltd 6.0%
Sector mix: Financial services 43.9%, Basic materials 22.9%, Consumer cyclical 6.6%, Healthcare 6.0%
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
Rolled up from the 5 largest holdings, 46.5% of the fund by weight
Ratings by weight: buy 0.0% | hold 57.4% | sell 42.6% (mean 3.45 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -6.2% above the current prices
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
Direction: money coming in (1 month)
Share count change: 1 week: +0.5% (5.51M) over 10d | 1 month: +2.0% (23.31M) over 32d
Shares outstanding: 42.94M | fund size: 1.22B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [World Markets Watchlist: November 16, 2026](https://www.etftrends.com/china-insights-content-hub/world-markets-watchlist-november-16-2026/)  
  <sub>ETF Trends, 16 hours ago</sub>  
  Our global markets watchlist tracks nine prominent indexes from economies around the world. The list includes the S&P 500 from the U.S..
- [Canada, China extend tariff relief measures through 2028 (EWC:NYSEARCA)](https://seekingalpha.com/news/4673527-canada-china-extend-tariff-relief-measures-through-2028)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Canada and China have agreed to expand trade cooperation, with Beijing providing tariff relief on approximately C$400M ($280M) of Canadian exports,...
- [Energy World adjourns 2026 annual general meeting](https://www.google.com/goto?url=CAESogEBxCJF1zXjE1n8Bb0cEWPfUXRqJnJbQE5PxQF_7DvV5qW2l8tOSTcSGpwlycsro5M8U8RDdAInRhDCGe6XCipw_Eoxtvn_XuuZgmp0VcftFZwk0kVZfasMXuGwFNrd6EYeXC9WU5vFvdWmd_Lb-PAGWeqxfYqREqbkhO0LAwBf6y9JQu_NG3vV9hHdEHepElV6wg6_obyW8wLI3JePdlhyhQE&gsessionid=mpIhfbotv_CcBLXurNcBX6QG1CpwPsmyoFeeCO6YGafLJTMti1-hgQ)  
  <sub>TipRanks, 12 hours ago</sub>  
  The latest announcement is out from Energy World Corporation Ltd ( ($AU:EWC) ). Energy World Corporation Ltd (ASX: EWC) said its 2026 annual general meeting...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 59.15 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 60.60 (-2.4%), 50d 60.04 (-1.5%), 200d 58.60 (+0.9%); 50d above 200d
Momentum: RSI(14) 41.8 | MACD -0.143 vs signal 0.059 (histogram -0.202)
Returns: 1d -0.2% | 5d -1.9% | 1m -1.9% | 3m -4.3%
52-week range: 49.91 - 62.64 (now 72.6% of the way up)
Volatility: ATR(14) 0.79 (1.3% of price) | annualised 20d 18.7%
Volume: 0.05x the 20-day average
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
Three-year record: +23.9% a year | beta to the market 0.73
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
Weighted price target: +8.0% above the current prices
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
Share count change: 1 week: +0.2% (15.33M) over 10d | 1 month: +7.8% (539.88M) over 32d
Shares outstanding: 126.23M | fund size: 7.47B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 51.97 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 52.10 (-0.2%), 50d 51.42 (+1.1%), 200d 51.54 (+0.8%); 50d below 200d
Momentum: RSI(14) 49.5 | MACD 0.348 vs signal 0.412 (histogram -0.064)
Returns: 1d +0.0% | 5d -2.5% | 1m +2.2% | 3m -1.8%
52-week range: 45.38 - 54.72 (now 70.6% of the way up)
Volatility: ATR(14) 0.76 (1.5% of price) | annualised 20d 22.5%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.53 | P/B 2.82 | P/S 2.81 | 3y earnings growth n/a
Yield: 3.5%
Three-year record: +20.7% a year | beta to the market 1.18
Cost and size: expense ratio 0.51% | net assets 1.10B
What it is made of: Stocks 99.2%, Cash 0.8%
Largest holdings: Spotify Technology SA 11.4%, Volvo AB Class B 6.4%, Atlas Copco AB Class A 6.2%, Sandvik AB 4.9%, Assa Abloy AB Class B 4.9%
Sector mix: Industrials 44.1%, Financial services 25.0%, Communication services 15.2%, Technology 6.9%
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
Rolled up from the 5 largest holdings, 33.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.97 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.5% above the current prices
Holdings read: SPOT, VOLV-B.ST, ATCO-A.ST, SAND.ST, ASSA-B.ST
Recent rating changes among them:
  - SPOT: 2026-10-23 Morgan Stanley: main, Overweight -> Overweight
  - ASSA-B.ST: 2015-12-09 Barclays: main, ? -> Equal-Weight
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
Share count change: 1 week: +0.2% (1.97M) over 10d | 1 month: +13.0% (125.02M) over 32d
Shares outstanding: 20.95M | fund size: 1.09B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 41.88 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 42.19 (-0.7%), 50d 41.95 (-0.2%), 200d 42.19 (-0.7%); 50d below 200d
Momentum: RSI(14) 47.3 | MACD 0.203 vs signal 0.209 (histogram -0.006)
Returns: 1d -1.0% | 5d -2.5% | 1m +2.1% | 3m -4.9%
52-week range: 38.08 - 44.59 (now 58.4% of the way up)
Volatility: ATR(14) 0.67 (1.6% of price) | annualised 20d 24.3%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.50 | P/B 1.87 | P/S 1.23 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +19.9% a year | beta to the market 0.95
Cost and size: expense ratio 0.49% | net assets 1.57B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: SAP SE 12.7%, Siemens AG 11.4%, Allianz SE 9.9%, Siemens Energy AG Ordinary Shares 5.8%, Deutsche Telekom AG 5.3%
Sector mix: Industrials 27.2%, Financial services 23.5%, Technology 16.9%, Healthcare 7.6%
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
Rolled up from the 5 largest holdings, 45.1% of the fund by weight
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.97 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.9% above the current prices
Holdings read: SAP.DE, SIE.DE, ALV.DE, ENR.DE, DTE.DE
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 79.50M | fund size: 3.33B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 57.31 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 56.99 (+0.6%), 50d 58.00 (-1.2%), 200d 58.30 (-1.7%); 50d below 200d
Momentum: RSI(14) 48.7 | MACD 0.156 vs signal -0.013 (histogram 0.169)
Returns: 1d -0.3% | 5d -3.3% | 1m +3.5% | 3m -8.8%
52-week range: 50.70 - 63.35 (now 52.3% of the way up)
Volatility: ATR(14) 0.87 (1.5% of price) | annualised 20d 28.3%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.58 | P/B 1.75 | P/S 1.42 | 3y earnings growth n/a
Yield: 3.4%
Three-year record: +27.2% a year | beta to the market 0.92
Cost and size: expense ratio 0.50% | net assets 1.19B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: UniCredit SpA 16.4%, Intesa Sanpaolo 13.8%, Enel SpA 11.7%, Eni SpA 5.5%, Generali 4.8%
Sector mix: Financial services 50.9%, Utilities 18.2%, Industrials 11.9%, Consumer cyclical 8.4%
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
Rolled up from the 5 largest holdings, 52.1% of the fund by weight
Ratings by weight: buy 90.8% | hold 9.2% | sell 0.0% (mean 2.17 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.0% above the current prices
Holdings read: UCG.MI, ISP.MI, ENEL.MI, ENI.MI, G.MI
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
Share count change: 1 week: -1.8% (-21.20M) over 10d | 1 month: -1.2% (-14.77M) over 32d
Shares outstanding: 20.46M | fund size: 1.17B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Japan's Q3 GDP Shrinks 0.1%: A Blip or Warning for ETF Investors?](https://es.tradingview.com/news/zacks:5b8ccb4ca094b:0-japan-s-q3-gdp-shrinks-0-1-a-blip-or-warning-for-etf-investors/)  
  <sub>24 hours ago</sub>  
  Japan's economy unexpectedly contracted in the third quarter of 2026, with the country's real GDP falling at an annualized rate of 0.1%—the first negative...
- [Asian markets slide as tech stocks tumble on US-China tensions, caution ahead of Nvidia earnings](https://seekingalpha.com/news/4673438-asian-markets-slide-as-tech-stocks-tumble-on-us-china-tensions-caution-ahead-of-nvidia-earnings)  
  <sub>8 hours ago</sub>  
  Asian stock markets traded lower on Tuesday as technology stocks led a broader decline amid escalating US-China tech tensions and investor caution ahead of...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 89.14 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 92.44 (-3.6%), 50d 95.30 (-6.5%), 200d 92.14 (-3.3%); 50d above 200d
Momentum: RSI(14) 36.9 | MACD -1.535 vs signal -1.399 (histogram -0.136)
Returns: 1d -0.8% | 5d -1.4% | 1m -6.2% | 3m -6.0%
52-week range: 79.49 - 99.32 (now 48.6% of the way up)
Volatility: ATR(14) 1.57 (1.8% of price) | annualised 20d 29.8%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Japan Stock
What it holds: P/E 15.14 | P/B 1.95 | P/S 1.31 | 3y earnings growth n/a
Yield: 3.8%
Three-year record: +18.3% a year | beta to the market 0.86
Cost and size: expense ratio 0.49% | net assets 23.40B
What it is made of: Stocks 99.2%, Cash 0.8%
Largest holdings: Mitsubishi UFJ Financial Group Inc 4.5%, Toyota Motor Corp 3.6%, Advantest Corp 3.1%, Recruit Holdings Co Ltd 3.1%, Sumitomo Mitsui Financial Group Inc 2.9%
Sector mix: Industrials 22.4%, Technology 20.6%, Financial services 19.1%, Consumer cyclical 12.0%
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
Rolled up from the 5 largest holdings, 17.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +28.2% above the current prices
Holdings read: 8306.T, 7203.T, 6857.T, 6098.T, 8316.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-10, published the following Friday)
Large speculators: net long 2.2% of open interest (27,258 contracts)
Change on the week: -5.8% of open interest
Crowding: 27% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -2.9% (-687.86M) over 10d | 1 month: +6.1% (1.31B) over 32d
Shares outstanding: 256.88M | fund size: 22.90B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 64.12 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 64.43 (-0.5%), 50d 61.97 (+3.5%), 200d 62.01 (+3.4%); 50d below 200d
Momentum: RSI(14) 52.4 | MACD 0.789 vs signal 0.958 (histogram -0.169)
Returns: 1d -0.9% | 5d -2.3% | 1m +3.4% | 3m -0.5%
52-week range: 55.69 - 66.56 (now 77.6% of the way up)
Volatility: ATR(14) 0.80 (1.2% of price) | annualised 20d 19.4%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

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
Rolled up from the 5 largest holdings, 49.6% of the fund by weight
Ratings by weight: buy 64.8% | hold 35.2% | sell 0.0% (mean 2.45 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +0.4% above the current prices
Holdings read: ROP.SW, NOVN.SW, NESN.SW, UBSG.SW, ZURN.SW
Recent rating changes among them:
  - UBSG.SW: 2026-04-20 Barclays: up, Underweight -> Equal-Weight
  - ZURN.SW: 2016-09-20 Bankhaus Lampe: down, Hold -> Sell
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
Shares outstanding: 28.62M | fund size: 1.84B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 62.83 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 64.59 (-2.7%), 50d 65.98 (-4.8%), 200d 65.17 (-3.6%); 50d above 200d
Momentum: RSI(14) 39.2 | MACD -0.546 vs signal -0.489 (histogram -0.057)
Returns: 1d -0.6% | 5d -4.1% | 1m -2.9% | 3m -9.3%
52-week range: 55.33 - 71.61 (now 46.1% of the way up)
Volatility: ATR(14) 1.08 (1.7% of price) | annualised 20d 26.9%
Volume: 0.02x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.38 | P/B 2.46 | P/S 1.73 | 3y earnings growth n/a
Yield: 4.4%
Three-year record: +20.7% a year | beta to the market 1.13
Cost and size: expense ratio 0.50% | net assets 597.52M
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ASML Holding NV 21.9%, ING Groep NV 8.6%, Prosus NV Ordinary Shares - Class N 4.7%, ASM International NV 3.8%, Nebius Group NV Shs Class-A- 3.4%
Sector mix: Technology 30.4%, Financial services 21.1%, Consumer defensive 11.8%, Industrials 11.0%
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
Rolled up from the 5 largest holdings, 42.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.58 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +60.0% above the current prices
Holdings read: ASML.AS, INGA.AS, PRX.AS, ASM.AS, NBIS
Recent rating changes among them:
  - NBIS: 2026-11-04 Citigroup: main, Buy -> Buy
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
Shares outstanding: 5.55M | fund size: 348.71M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 58.39 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 58.28 (+0.2%), 50d 59.09 (-1.2%), 200d 58.17 (+0.4%); 50d above 200d
Momentum: RSI(14) 47.8 | MACD 0.182 vs signal -0.000 (histogram 0.182)
Returns: 1d -1.3% | 5d -3.2% | 1m +1.8% | 3m -6.4%
52-week range: 49.37 - 63.23 (now 65.1% of the way up)
Volatility: ATR(14) 0.91 (1.6% of price) | annualised 20d 24.8%
Volume: 0.01x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 16.25 | P/B 2.19 | P/S 1.75 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +32.7% a year | beta to the market 0.91
Cost and size: expense ratio 0.50% | net assets 1.94B
What it is made of: Stocks 99.4%, Cash 0.6%
Largest holdings: Banco Santander SA 16.4%, Iberdrola SA 14.3%, Banco Bilbao Vizcaya Argentaria SA 12.6%, Repsol SA 5.3%, Industria De Diseno Textil SA Share From Split 4.6%
Sector mix: Financial services 40.5%, Utilities 22.9%, Industrials 14.9%, Technology 6.3%
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
Ratings by weight: buy 76.3% | hold 23.7% | sell 0.0% (mean 2.29 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +7.4% above the current prices
Holdings read: SAN.MC, IBE.MC, BBVA.MC, REP.MC, ITX.MC
Recent rating changes among them:
  - SAN.MC: 2023-11-08 JP Morgan: main, Neutral -> Neutral
  - REP.MC: 2020-01-29 RBC Capital: up, Underperform -> Outperform
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
Shares outstanding: 37.35M | fund size: 2.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Chip-Dollar: Deutsche Bank Says Chips Now Prop Up the Dollar - VanEck Semiconductor ETF (NASDAQ:SMH)](https://www.benzinga.com/markets/forex/26/11/63303886/chip-dollar-deutsche-bank-chips-replace-petrodollar-dollar-risk)  
  <sub>22 hours ago</sub>  
  Deutsche Bank says the chip-dollar is replacing the petrodollar, as Asian chip surpluses flow into US stocks, not Treasuries. A riskier prop. SMH.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 89.25 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 99.16 (-10.0%), 50d 106.98 (-16.6%), 200d 94.89 (-5.9%); 50d above 200d
Momentum: RSI(14) 35.2 | MACD -4.347 vs signal -3.909 (histogram -0.438)
Returns: 1d -1.7% | 5d -5.7% | 1m -16.8% | 3m -14.8%
52-week range: 60.03 - 118.00 (now 50.4% of the way up)
Volatility: ATR(14) 3.96 (4.4% of price) | annualised 20d 67.5%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Greater China Region
What it holds: P/E 27.29 | P/B 4.22 | P/S 2.50 | 3y earnings growth n/a
Yield: 1.0%
Three-year record: +37.1% a year | beta to the market 1.35
Cost and size: expense ratio 0.59% | net assets 11.05B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 22.3%, MediaTek Inc 6.1%, Hon Hai Precision Industry Co Ltd 3.4%, ASE Technology Holding Co Ltd 3.0%, Delta Electronics Inc 2.9%
Sector mix: Technology 71.4%, Financial services 16.3%, Basic materials 4.4%, Industrials 2.6%
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
Rolled up from the 5 largest holdings, 37.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +62.3% above the current prices
Holdings read: 2330.TW, 2454.TW, 2317.TW, 3711.TW, 2308.TW
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
Share count change: 1 week: -11.0% (-1.25B) over 10d | 1 month: +3.5% (343.34M) over 32d
Shares outstanding: 112.92M | fund size: 10.08B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 47.35 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 47.74 (-0.8%), 50d 47.37 (-0.0%), 200d 47.10 (+0.5%); 50d above 200d
Momentum: RSI(14) 47.4 | MACD 0.090 vs signal 0.143 (histogram -0.053)
Returns: 1d -0.5% | 5d -1.3% | 1m +0.0% | 3m -2.5%
52-week range: 41.34 - 49.39 (now 74.7% of the way up)
Volatility: ATR(14) 0.60 (1.3% of price) | annualised 20d 20.0%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 16.62 | P/B 2.25 | P/S 1.41 | 3y earnings growth n/a
Yield: 3.1%
Three-year record: +19.9% a year | beta to the market 0.66
Cost and size: expense ratio 0.50% | net assets 3.73B
What it is made of: Stocks 98.5%, Other 1.0%, Cash 0.5%
Largest holdings: Shell PLC 9.9%, HSBC Holdings PLC 9.3%, AstraZeneca PLC 8.9%, Unilever PLC 4.4%, Rolls-Royce Holdings PLC 4.4%
Sector mix: Financial services 23.2%, Consumer defensive 15.3%, Energy 14.3%, Healthcare 13.9%
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
Rolled up from the 5 largest holdings, 36.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.08 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.1% above the current prices
Holdings read: SHEL.L, HSBA.L, AZN.L, ULVR.L, RR.L
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
Direction: money going out (1 month)
Share count change: 1 week: -0.5% (-19.22M) over 10d | 1 month: -0.8% (-31.10M) over 32d
Shares outstanding: 77.66M | fund size: 3.68B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 77.64 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 76.05 (+2.1%), 50d 74.40 (+4.4%), 200d 76.21 (+1.9%); 50d below 200d
Momentum: RSI(14) 61.6 | MACD 0.875 vs signal 0.785 (histogram 0.090)
Returns: 1d +1.6% | 5d +0.2% | 1m +3.0% | 3m +3.3%
52-week range: 65.87 - 81.23 (now 76.6% of the way up)
Volatility: ATR(14) 1.29 (1.7% of price) | annualised 20d 15.2%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 12.23 | P/B 1.88 | P/S 1.40 | 3y earnings growth n/a
Yield: 3.3%
Three-year record: +13.3% a year | beta to the market 0.99
Cost and size: expense ratio 0.50% | net assets 1.56B
What it is made of: Stocks 99.3%, Cash 0.7%
Largest holdings: Grupo Mexico SAB de CV Class B 14.9%, Grupo Financiero Banorte SAB de CV Class O 11.2%, Fomento Economico Mexicano SAB de CV Units Cons. Of 1 Shs-B- And 4 Shs-D- 8.9%, America Movil SAB de CV Ordinary Shares - Class B 7.9%, Cemex SAB de CV Cert Part Ord Repr 2 Shs-A- & 1 Shs-B- 4.6%
Sector mix: Consumer defensive 25.1%, Basic materials 24.7%, Financial services 18.1%, Industrials 12.7%
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
Rolled up from the 5 largest holdings, 47.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.0% above the current prices
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 18.90M | fund size: 1.47B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Chip-Dollar: Deutsche Bank Says Chips Now Prop Up the Dollar - VanEck Semiconductor ETF (NASDAQ:SMH)](https://www.benzinga.com/markets/forex/26/11/63303886/chip-dollar-deutsche-bank-chips-replace-petrodollar-dollar-risk)  
  <sub>Benzinga, 22 hours ago</sub>  
  Deutsche Bank says the chip-dollar is replacing the petrodollar, as Asian chip surpluses flow into US stocks, not Treasuries. A riskier prop. SMH.
- [iShares MSCI South Korea ETF NAV Fell 4.56% on Nov. 16](https://www.tokenpost.com/news/investing/59330)  
  <sub>TOKENPOST, 3 hours ago</sub>  
  The iShares MSCI South Korea ETF (EWY) had a net asset value of $135.94 Monday, Nov. 16, after a one-day drop of $6.49, or 4.56%.
- [iShares MSCI South Korea ETF (EWY) Price Prediction: Bearish Trend Meets Heavy Positioning as South Korea ETF Sits Below Key Averages](https://www.google.com/goto?url=CAESoAEBxCJF17ffPcXb5jB5WYolKDWbGSlbReRc25szZqziZ2B4joPP7NNcnWtOszwOfMs0kPv5d9sJNT3gqEC4tsWOkVki9bvkGyyF3a4RfNFBsWXaixwkIpuVKZubIFdTte2sm7x9MMkF6M303pDFXGT7nowFCulp4I96L7lkmD4YBl5NYq64WFNJewPKdlMnu0ynfv1aq3NfD9RZWvQHrFgh&gsessionid=iISW_or8l9mDqaqGnjF0QgBu9FHojQ7ST5z8voqBf37JrwawmqfbpQ)  
  <sub>Blockchain News, 3 hours ago</sub>  
  iShares MSCI South Korea ETF (EWY) is trading at $135.79, down 2.83% over 24 hours, with price still below its short-, medium-, and long-term moving...
- [Direxion South Korea Bull 3X ETF (KORU) Price Prediction: Leveraged Korea exposure is breaking down, but positioning remains crowded](https://www.google.com/goto?url=CAESogEBxCJF15mTmm7GSXpZIrnRr-q2XY0jNCdv1LTbe9srrNo0ElQwQe4YNtqkpuF5kBFyyvvSz1aCXYptZaJGKXxZyJ-NwYcRuBRV5hyYafuNl3U5Ym_3jOxgUd4nyb5xkOBDBBHM8YSyt1rcs8zSGBX8AdnY9RNnaFROIdUJQdPaAZSWeAW373JORYrfctqqb6IWzimmEtQNHzYhUNhA2H63ljI&gsessionid=iISW_or8l9mDqaqGnjF0QgBu9FHojQ7ST5z8voqBf37JrwawmqfbpQ)  
  <sub>Blockchain News, 3 hours ago</sub>  
  Direxion South Korea Bull 3X ETF (KORU) is trading at $6.55, down 8.52% over the last 24 hours, after failing to hold above its short-term moving averages.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 135.01 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 148.21 (-8.9%), 50d 166.32 (-18.8%), 200d 164.16 (-17.8%); 50d above 200d
Momentum: RSI(14) 37.0 | MACD -7.767 vs signal -7.533 (histogram -0.233)
Returns: 1d -1.1% | 5d -3.0% | 1m -13.8% | 3m -22.6%
52-week range: 88.53 - 219.20 (now 35.6% of the way up)
Volatility: ATR(14) 6.91 (5.1% of price) | annualised 20d 71.9%
Volume: 0.11x the 20-day average
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
Three-year record: +37.0% a year | beta to the market 2.62
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
Direction: money going out (1 month)
Share count change: 1 week: -6.2% (-1.40B) over 10d | 1 month: -0.9% (-201.08M) over 32d
Shares outstanding: 156.57M | fund size: 21.14B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [ETFs Investing in Banco Bradesco SA Pfd Stocks](https://www.tradingview.com/symbols/HAN-BRE/etfs/)  
  <sub>23 hours ago</sub>  
  Explore funds investing in BRE in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 31.19 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 33.89 (-8.0%), 50d 37.31 (-16.4%), 200d 36.95 (-15.6%); 50d above 200d
Momentum: RSI(14) 31.9 | MACD -1.981 vs signal -1.888 (histogram -0.093)
Returns: 1d +0.9% | 5d -3.0% | 1m -25.6% | 3m -9.0%
52-week range: 30.92 - 43.54 (now 2.1% of the way up)
Volatility: ATR(14) 1.06 (3.4% of price) | annualised 20d 73.2%
Volume: 0.08x the 20-day average
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
Three-year record: +5.9% a year | beta to the market 0.92
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
Weighted price target: +35.8% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 200.55M | fund size: 6.26B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [iシェアーズ MSCI ジャパン高配当利回り ETF【1478】：株価・株式情報（夜間PTS含む）](https://finance.yahoo.co.jp/quote/1478.T)  
  <sub>6 hours ago</sub>  
  iシェアーズ MSCI ジャパン高配当利回り ETF【1478】の株価、チャート、最新の関連ニュース、掲示板、みんなの評価などをご覧いただけます。前日終値、高値、安値は...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 63.46 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 64.79 (-2.0%), 50d 65.43 (-3.0%), 200d 67.93 (-6.6%); 50d below 200d
Momentum: RSI(14) 43.9 | MACD -0.064 vs signal 0.082 (histogram -0.146)
Returns: 1d +0.7% | 5d -6.4% | 1m -1.8% | 3m -9.7%
52-week range: 60.43 - 81.60 (now 14.3% of the way up)
Volatility: ATR(14) 1.46 (2.3% of price) | annualised 20d 31.3%
Volume: 0.05x the 20-day average
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
Three-year record: +25.5% a year | beta to the market 1.12
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
Weighted price target: +30.7% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 7.90M | fund size: 501.33M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [VanEck Gold Miners ETF (GDX) Options Chain - Yahoo Finance](https://ca.finance.yahoo.com/quote/GDX/options/?date=1795564800&straddle=false&type=all)  
  <sub>24 hours ago</sub>  
  View the basic GDX option chain and compare options of VanEck Gold Miners ETF on Yahoo Finance.
- [Form 4 VanEck Gold Miners ETF For: 16 November By Investing.com](https://ca.investing.com/news/stock-market-news/form-4-vaneck-gold-miners-etf-for-16-november-93CH-4961974)  
  <sub>18 hours ago</sub>  
  Filed Pursuant to Rule 424(b)(2) Registration Statement No. 333-285508. (To Product Supplement No. EQUITY STR-1 dated July 15,
- [VanEck Launches Pivotal Trends ETF (PIVT), Turning Its Highest Conviction Views into a Single Investment Strategy](https://www.google.com/goto?url=CAES5QEBxCJF192U0FIZPCdOXY0epzZ50MRlUFMM4stIvQ3XXCAHiwom6u9wiY_XRkvNJ66ydw1tIQpkAPcMwQt_IaZwYAmB4stVcm57IZGXWP-yyAzhXU_Dsx7xa97-6B7z24u9F_1BzDDFkopr8fssweFGEjykWKui1bk-hY5KA_j11G_qX32ly9w48iwjE4dBqpl42bOqmQb9bGWmN_Tv4rwqKNyFx3_2ZFAzDdvKIURoTmxTrgQ-Ek9hMDgi8ZelqqI9OhW88SuJrpk763nsBqhTsXVdbCV7zcZstD5EcwH6Jv1W1l87&gsessionid=x-8O0IPSRJziVvjS2KglRpKN7B-6r_P440N45TgPcpshDacCbwi8nQ)  
  <sub>2 hours ago</sub>  
  VanEck today launched the VanEck Pivotal Trends ETF (Nasdaq: PIVT), an actively managed ETF that brings together the firm's highest conviction,...
- [Gold and silver settle at new 52-week lows as U.S. rate hike bets boost dollar (GLD:NYSEARCA)](https://www.google.com/goto?url=CAES8QEBxCJF176aNjSG5aAHnRCMcQCVeZVP4MdmvXxJ4F-8HBCZajH_Wsl9g59T9d-H-C5iQKhdmHcVRylJAjdAAXZJ0M3h6yT5RDUCobAxdY97VTaIIBdMQV0ftmoYYy2zWGpO1kGb6BFcMsdjEme92wc6pzhCDIeqgtTf51Vzx3p61CF0boK_pcX9vlgN-XSrGA3TxPJIk7S-YwiJiisAVH9_Go6zRXOvArO0Tu0o_tuPze_A8gFpy7HQPOKVXK_YaQAQSB8tkZUsgqR8SNx0qzS2fv2SYtHF7XdLkfnnvv8fNFr2JTn8BlQxnRaAs0K8pFbe&gsessionid=x-8O0IPSRJziVvjS2KglRpKN7B-6r_P440N45TgPcpshDacCbwi8nQ)  
  <sub>16 hours ago</sub>  
  Gold and silver fell to their lowest levels in more than a year as the dollar traded near its highest since April 2025 amid rising expectations of prolonged...
- [GDX Dec 2026 91.500 put (GDX261204P00091500) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXUJyGsLH3enuSGADTP3mUFvLzuosXZcL3CsPKvbggh2kRtD4Zmn9rkKlKWvaNLmUs5dEdmzsB1qt_a5USUlYi2f02X0hdvVHQ3LSDDoxLw0A8NdvJQzLn0N8Xi2_XeWBWVsHFYyLMj3-LWvj-Z9A&gsessionid=x-8O0IPSRJziVvjS2KglRpKN7B-6r_P440N45TgPcpshDacCbwi8nQ)  
  <sub>4 hours ago</sub>  
  Find the latest GDX Dec 2026 91.500 put (GDX261204P00091500) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 80.93 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 82.82 (-2.3%), 50d 87.51 (-7.5%), 200d 89.44 (-9.5%); 50d below 200d
Momentum: RSI(14) 44.4 | MACD -1.316 vs signal -1.234 (histogram -0.081)
Returns: 1d +2.5% | 5d -6.4% | 1m -6.4% | 3m -16.8%
52-week range: 70.74 - 115.84 (now 22.6% of the way up)
Volatility: ATR(14) 3.38 (4.2% of price) | annualised 20d 59.3%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Equity Precious Metals
What it holds: P/E 12.25 | P/B 2.71 | P/S 3.99 | 3y earnings growth n/a
Yield: 0.8%
Three-year record: +46.2% a year | beta to the market 0.98
Cost and size: expense ratio 0.51% | net assets 23.82B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Newmont Corp 11.6%, Agnico Eagle Mines Ltd 11.3%, Barrick Mining Corp 8.2%, Wheaton Precious Metals Corp 5.5%, Franco-Nevada Corp 5.5%
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
Rolled up from the 5 largest holdings, 42.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.71 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.7% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, FNV.TO
Recent rating changes among them:
  - NEM: 2026-10-27 Scotiabank: main, Sector Outperform -> Sector Outperform
  - AEM.TO: 2026-11-02 Freedom Broker: up, Hold -> Buy
  - ABX.TO: 2026-11-10 JP Morgan: main, Overweight -> Overweight
  - WPM.TO: 2026-10-08 UBS: main, Buy -> Buy
  - FNV.TO: 2026-11-12 HC Wainwright & Co.: reit, Buy -> Buy
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
Share count change: 1 week: +7.1% (1.56B) over 7d | 1 month: -7.1% (-1.80B) over 31d
Shares outstanding: 291.95M | fund size: 23.63B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Forget Nvidia — S&P 500's 8,900 Target Puts These ETFs in Play - State Street SPDR S&P 500 ETF Trust (ARC](https://www.benzinga.com/etfs/broad-u-s-equity-etfs/26/11/63304335/wall-street-sees-sp-500-at-8900-putting-these-etfs-in-play)  
  <sub>22 hours ago</sub>  
  Wall Street sees the S&P 500 climbing to 8900. Discover which sector ETFs could benefit as investors look beyond Big Tech and the AI trade.
- [Domino's Pizza, Inc. (DPZ) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/DPZ/)  
  <sub>15 hours ago</sub>  
  Find the latest Domino's Pizza, Inc. (DPZ) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 97.17 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 104.22 (-6.8%), 50d 105.90 (-8.2%), 200d 94.26 (+3.1%); 50d above 200d
Momentum: RSI(14) 34.8 | MACD -2.247 vs signal -1.650 (histogram -0.598)
Returns: 1d -1.8% | 5d -3.2% | 1m -8.3% | 3m -5.5%
52-week range: 74.67 - 112.67 (now 59.2% of the way up)
Volatility: ATR(14) 2.84 (2.9% of price) | annualised 20d 31.1%
Volume: 0.07x the 20-day average
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
Three-year record: +11.5% a year | beta to the market 1.25
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
Weighted price target: +38.2% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 12.50M | fund size: 1.21B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Traders pour cash into BlackRock’s India ETF as AI rout deepens](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc6aa745e54fde98d0e7d2b5f8889d&url=https%3a%2f%2fwww.msn.com%2fen-in%2fnews%2fother%2ftraders-pour-cash-into-blackrock-s-india-etf-as-ai-rout-deepens%2far-AA2hAbzV&c=10527642329677728339&mkt=en-us)  
  <sub>The Economic Times on MSN, 19h ago</sub>  
  Investors poured over $316 million into BlackRock’s iShares MSCI India ETF last week, its largest weekly inflow since June 2025, as AI-related volatility drove diversification away from ...
- [India ETFs among global winners in October as AI-hardware sell-off hits Taiwan, Korea](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc6aa745e54fde98d0e7d2b5f8889d&url=https%3a%2f%2fwww.thehindubusinessline.com%2fmarkets%2findia-etfs-among-global-winners-in-october-as-ai-hardware-sell-off-hits-taiwan-korea%2farticle71710338.ece&c=16368109973275922584&mkt=en-us)  
  <sub>The Hindu BusinessLine, 13h ago</sub>  
  India ETFs shine globally in October 2026 as AI/hardware sell-off hits Taiwan/Korea, with Sensex-based funds rising up to 14%.
- [Indian equity ETFs lead global gains October 2026, tech lags](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc6aa745e54fde98d0e7d2b5f8889d&url=https%3a%2f%2fwww.newsbytesapp.com%2fnews%2fbusiness%2findian-equity-etfs-lead-global-gains-october-2026-tech-lags%2ftldr&c=10544665668190484030&mkt=en-us)  
  <sub>NewsBytes, 13h ago</sub>  
  Indian equity ETFs surged in October 2026, with gains up to 14%, while semiconductor and AI-linked funds in Taiwan and Korea saw declines of 20–31%.
- [Invesco Mutual Fund launches banking ETF, metal index fund; NFOs open on November 16](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc6aa745e54fde98d0e7d2b5f8889d&url=https%3a%2f%2fwww.cnbctv18.com%2fpersonal-finance%2finvesco-mutual-fund-launches-banking-etf-metal-index-fund-nfos-open-on-november-16-20035933.htm&c=11877462285021327212&mkt=en-us)  
  <sub>CNBCTV18, 12h ago</sub>  
  Invesco Mutual Fund launched the Invesco India BSE Top 10 Banks ETF and Invesco India Nifty Metal Index Fund, offering targeted passive sector exposure.
- [Foreign outflows from India-focused offshore funds ease but persist in Q3 2026](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc6aa745e54fde98d0e7d2b5f8889d&url=https%3a%2f%2fwww.thehindubusinessline.com%2fmarkets%2fforeign-outflows-from-india-focused-offshore-funds-ease-but-persist-in-q3-2026%2farticle71711586.ece&c=13813098624039714108&mkt=en-us)  
  <sub>The Hindu BusinessLine, 17h ago</sub>  
  Foreign institutional investors turned net buyers during the quarter, logging net inflows of $1.48 billion into Indian equities, a sharp reversal from the $15.1 billion outflow in the prior quarter.
- [Global funds buy Indian stocks despite $3.9 billion offshore withdrawals: Why are investors taking different bets?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc6aa745e54fde98d0e7d2b5f8889d&url=https%3a%2f%2fwww.msn.com%2fen-in%2fmoney%2ftopstories%2fglobal-funds-buy-indian-stocks-despite-39-billion-offshore-withdrawals-why-are-investors-taking-different-bets%2far-AA2hCIY3&c=2529521269945979718&mkt=en-us)  
  <sub>Business Today on MSN, 10h ago</sub>  
  Global funds continued buying Indian equities even as India-focused offshore funds and ETFs recorded $3.9 billion in outflows during the September 2026 quarter. Morningstar's report highlights how ...
- ['World's largest AI hedge': Why global investors are rushing back to Indian stocks](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc6aa745e54fde98d0e7d2b5f8889d&url=https%3a%2f%2fwww.moneycontrol.com%2fnews%2fbusiness%2fworld-s-largest-ai-hedge-why-global-investors-are-rushing-back-to-indian-stocks-14082174.html&c=15920215383361334215&mkt=en-us)  
  <sub>Moneycontrol, 16h ago</sub>  
  BlackRock's iShares MSCI India ETF attracted over $316 million last week, its biggest inflow since June 2025, as investors shifted away from AI-heavy markets in Taiwan and South Korea.
- [Argentina Adds 4 China, India, AI Products](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc6aa745e54fde98d0e7d2b5f8889d&url=https%3a%2f%2fwww.riotimesonline.com%2fbyma-adds-four-new-cedears-china-india-ai%2f&c=7938362093648331654&mkt=en-us)  
  <sub>The Rio Times, 13h ago</sub>  
  BYMA added four CEDEARs, local certificates of foreign assets, on 17 November tied to China tech, India, US small companies and AI.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 51.88 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 49.28 (+5.3%), 50d 48.13 (+7.8%), 200d 49.10 (+5.7%); 50d below 200d
Momentum: RSI(14) 76.2 | MACD 1.174 vs signal 0.900 (histogram 0.275)
Returns: 1d +0.6% | 5d +0.3% | 1m +9.5% | 3m +4.7%
52-week range: 45.42 - 54.83 (now 68.7% of the way up)
Volatility: ATR(14) 0.51 (1.0% of price) | annualised 20d 15.8%
Volume: 0.07x the 20-day average
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
Three-year record: +5.3% a year | beta to the market 0.61
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
Weighted price target: +13.6% above the current prices
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
Share count change: 1 week: -0.3% (-19.49M) over 7d | 1 month: -8.2% (-524.68M) over 31d
Shares outstanding: 113.96M | fund size: 5.91B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Should you invest in the Invesco Aerospace & Defense ETF (PPA)?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc69b43e784b25b16fa2cdbb350b0c&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2ftop-stocks%2fshould-you-invest-in-the-invesco-aerospace-defense-etf-ppa%2far-AA2hC50H&c=66895750491222696&mkt=en-us)  
  <sub>Zacks Investment Research on MSN, 13h ago</sub>  
  Designed to provide broad exposure to the Industrials - Aerospace & Defense segment of the equity market, the Invesco Aerospace & Defense ETF (PPA) is a passively managed exchange traded fund launched ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 70.03 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 70.22 (-0.3%), 50d 70.20 (-0.2%), 200d 75.85 (-7.7%); 50d below 200d
Momentum: RSI(14) 48.1 | MACD 0.203 vs signal 0.134 (histogram 0.069)
Returns: 1d +0.4% | 5d -3.2% | 1m +1.1% | 3m -14.6%
52-week range: 66.08 - 84.41 (now 21.6% of the way up)
Volatility: ATR(14) 1.76 (2.5% of price) | annualised 20d 31.9%
Volume: 0.03x the 20-day average
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
Three-year record: +23.9% a year | beta to the market 1.03
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

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -3.5% (-430.30M) over 7d | 1 month: +187.7% (7.81B) over 31d
Shares outstanding: 171.01M | fund size: 11.98B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [The freight recovery continued in October - Cass Index report](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc69c4fecb470a8db05d512e9c543f&url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fthe-freight-recovery-continued-in-october-cass-index-report%2far-AA2hxvih&c=13392304387921787313&mkt=en-us)  
  <sub>Seeking Alpha on MSN, 32h ago</sub>  
  The October Cass Transportation Index report indicated that the freight cycle is shifting into a higher gear as strengthening volume and rising costs factored in. The shipments component of the Cass ...
- [Should You Invest in the State Street SPDR S&P Transportation ETF (XTN)?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc69c4fecb470a8db05d512e9c543f&url=https%3a%2f%2fwww.ainvest.com%2fnews%2finvest-state-street-spdr-transportation-etf-xtn-2611%2f&c=7307146302484859336&mkt=en-us)  
  <sub>ainvest, 31h ago</sub>  
  State Street SPDR S&P Transportation ETF carries a Zacks ETF Rank of 3 (Hold), which is based on expected asset class return, expense ratio, and momentum, among other factors. Thus, XTN is a good ...
- [iShares U.S. Transportation ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc69c4fecb470a8db05d512e9c543f&url=https%3a%2f%2fmarkets.businessinsider.com%2fetfs%2fishares-us-transportation-etf-us4642871929&c=16585904539700472462&mkt=en-us)  
  <sub>Business Insider, 21h ago</sub>  
  Copyright © 2026 Insider Inc and finanzen.net GmbH (Imprint). All rights reserved. Registration on or use of this site constitutes acceptance of our Terms of Service ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 83.57 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 82.47 (+1.3%), 50d 81.07 (+3.1%), 200d 82.07 (+1.8%); 50d below 200d
Momentum: RSI(14) 55.1 | MACD 0.791 vs signal 0.659 (histogram 0.132)
Returns: 1d -0.5% | 5d -0.3% | 1m +5.3% | 3m -3.5%
52-week range: 68.14 - 90.01 (now 70.6% of the way up)
Volatility: ATR(14) 1.43 (1.7% of price) | annualised 20d 27.4%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Industrials
What it holds: P/E 19.04 | P/B 4.01 | P/S 1.38 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +14.8% a year | beta to the market 1.24
Cost and size: expense ratio 0.37% | net assets 2.00B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Union Pacific Corp 18.7%, Uber Technologies Inc 13.8%, CSX Corp 10.0%, United Parcel Service Inc Class B 4.9%, Norfolk Southern Corp 4.8%
Sector mix: Industrials 85.3%, Technology 14.7%
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

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -2.0% (-40.15M) over 10d | 1 month: +1.5% (29.70M) over 32d
Shares outstanding: 23.95M | fund size: 2.00B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [区域银行指数ETF-SPDR KBW收跌0.76%，成交额11.64亿美元](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc692e861546589750d0508894f3ff&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fusstock%2fnotice%2f2026-11-17%2fdoc-iniyyrkt7895289.shtml&c=16347676899338907425&mkt=en-us)  
  <sub>新浪财经, 17h ago</sub>  
  11月17日，区域银行指数ETF-SPDR KBW（KRE）收跌0.76%，报72.19美元，成交额11.64亿美元，市值43.17亿美元。 声明：市场有风险，投资需谨慎。本文基于第三方数据库发布，不代表新浪财经观点，任何在本文出现的信息均只作为参考，不构成个人投资建议。如有出入请以实际公告为准。如有疑问，请联系biz@staff.sina.com.cn。

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 71.96 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 72.60 (-0.9%), 50d 71.61 (+0.5%), 200d 71.25 (+1.0%); 50d above 200d
Momentum: RSI(14) 48.6 | MACD 0.289 vs signal 0.384 (histogram -0.095)
Returns: 1d -0.3% | 5d -1.5% | 1m +3.9% | 3m -4.1%
52-week range: 58.63 - 77.93 (now 69.1% of the way up)
Volatility: ATR(14) 1.34 (1.9% of price) | annualised 20d 19.8%
Volume: 0.09x the 20-day average
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
Three-year record: +23.9% a year | beta to the market 0.97
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
Weighted price target: +11.6% above the current prices
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
Share count change: 1 week: -0.7% (-27.70M) over 7d | 1 month: +1.4% (54.58M) over 31d
Shares outstanding: 55.09M | fund size: 3.96B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [OCEANE Enters Saudi Market with SNB Capital to Provide Liquidity for SAB Invest Hong Kong ETF (9411)](https://www.aninews.in/news/business/oceane-enters-saudi-market-with-snb-capital-to-provide-liquidity-for-sab-invest-hong-kong-etf-941120261117143155)  
  <sub>6 hours ago</sub>  
  Riyadh [Saudi Arabia], November 17 (ANI): OCEANE Global for Market Making LLC ("OCEANE"), an Abu Dhabi-based ETF market-making firm, today announced its...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 35.97 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 34.93 (+3.0%), 50d 35.95 (+0.1%), 200d 37.74 (-4.7%); 50d below 200d
Momentum: RSI(14) 58.1 | MACD 0.075 vs signal -0.159 (histogram 0.234)
Returns: 1d +0.4% | 5d +1.1% | 1m +2.4% | 3m -5.6%
52-week range: 33.69 - 40.63 (now 32.9% of the way up)
Volatility: ATR(14) 0.34 (0.9% of price) | annualised 20d 16.6%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.14 | P/B 1.71 | P/S 2.83 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +0.8% a year | beta to the market 0.20
Cost and size: expense ratio 0.75% | net assets 556.97M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Al Rajhi Bank 14.1%, Saudi Arabian Oil Co 12.5%, Saudi National Bank 8.2%, Saudi Telecom Co 6.2%, Saudi Arabian Mining Co 4.3%
Sector mix: Financial services 41.3%, Energy 13.5%, Basic materials 12.7%, Communication services 8.9%
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
Rolled up from the 5 largest holdings, 45.3% of the fund by weight
Ratings by weight: buy 90.6% | hold 9.4% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.4% above the current prices
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
Direction: money going out (1 month)
Share count change: 1 week: -2.3% (-13.02M) over 7d | 1 month: -7.4% (-44.46M) over 31d
Shares outstanding: 15.44M | fund size: 555.55M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 48.63 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 49.91 (-2.5%), 50d 51.38 (-5.3%), 200d 54.98 (-11.5%); 50d below 200d
Momentum: RSI(14) 34.3 | MACD -0.487 vs signal -0.410 (histogram -0.077)
Returns: 1d -0.8% | 5d -4.8% | 1m -4.4% | 3m -12.2%
52-week range: 48.63 - 64.26 (now 0.0% of the way up)
Volatility: ATR(14) 0.67 (1.4% of price) | annualised 20d 21.6%
Volume: 0.09x the 20-day average
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
Three-year record: +7.6% a year | beta to the market 0.47
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
Weighted price target: +78.1% above the current prices
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
Share count change: 1 week: +4.9% (252.68M) over 7d | 1 month: -4.5% (-254.39M) over 31d
Shares outstanding: 110.96M | fund size: 5.40B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [VanEck Semiconductor ETF (SMH) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/SMH/)  
  <sub>Yahoo! Finance Canada, 3 hours ago</sub>  
  VanEck Semiconductor ETF (SMH) · -5.23% · -14.43% · -16.98% · 27.14% · 33.89% · 207.22% · 847.49%. Key Events. Baseline. Advanced Chart. Loading chart...
- [AI Bets: Splitting the Stack](https://etfdb.com/equity-etf-content-hub/ai-bets-splitting-stack/)  
  <sub>ETF Database, 32 minutes ago</sub>  
  The recent fallout in Nvidia (NVDA) and chip stocks — punctuated by an 11% plunge in the VanEck Semiconductor ETF (SMH B) on November 5 — has exposed a...
- [VanEck Semiconductor ETF (SMH) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXXiheIPLN1BvXLT-G7Sc0YiWvhYeTwK9t1jr6L1O3mH1RxlarKbO8-mOMHT62KLMBO-jvvYVDBajaVgYeUnh55kW2XgTOdlAZ6FqODqacKokP17gm2hnHciga9BVt0XRc&gsessionid=VWv8fORuLuZ1niXobqk6KxiDYiXkW6bkJL0i4n04XbU0mrgQGjiWuA)  
  <sub>Yahoo Finance Singapore, 18 hours ago</sub>  
  VanEck Semiconductor ETF (SMH) · -5.23% · -14.43% · -16.98% · 27.14% · 33.89% · 207.22% · 847.49%. Key events. Baseline. Advanced chart. Loading chart...
- [Has The AI Bubble Popped? (NASDAQ:SMH)](https://www.google.com/goto?url=CAESfgHEIkXX9bs_dc2Y2GCBqfVsgxi0FrXymtBqGV9l1mbQRRgQ3af5gPv7vxBzTwhLNm6dkB0vXQ0-hFYpjinehpotN6bFZ-X_ArtoahNgIW2VAbYLKMRCeDLGBZvCWjOOaunfGDxnZNeHbMo1FMzm2gQImUX1LaHoTJ7JmvszJA&gsessionid=VWv8fORuLuZ1niXobqk6KxiDYiXkW6bkJL0i4n04XbU0mrgQGjiWuA)  
  <sub>Seeking Alpha, 38 minutes ago</sub>  
  Analyst sees VanEck Semiconductor ETF as a mixed AI trade: shares could recover, but a break below $445 could expose downside toward its 100-week moving...
- [Best semiconductor ETFs: SMH leads on cost, liquidity and momentum](https://www.google.com/goto?url=CAESuwEBxCJF14hosuJCgS1j2BdMhHN96PW7-bPk4Ywn0spexRnZrKBCjNfK2Amcrc-LrTyjpAtEnrjciSU0UDD0I7Y7s0pgsTEjUy8A_3ic11rl1OoUXeBdtqR2EKGCC0yQyzm5yAwkkBlU1rXrsM0bnZ-PZ0kYcbQA1K52TtDTp5nR2Kc37oo-boGVRXUIuDSZwDrEdxxav1sF2UNrt9fleQ8F_Lkwmkz0BhY9z-bADnUBvYrNzpwxQzsZvOZ1&gsessionid=VWv8fORuLuZ1niXobqk6KxiDYiXkW6bkJL0i4n04XbU0mrgQGjiWuA)  
  <sub>Investing.com, 18 hours ago</sub>  
  Investing.com -- No single chip ETF stands out as "the best" right now, but VanEck Semiconductor ETF (SMH) screens as the strongest all-round candidate on...
- [Forget Nvidia Stock at $160 per Share. Buy This Semiconductor ETF Instead.](https://www.google.com/goto?url=CAESrwEBxCJF1wmgPjVy4hvuPUau5YPc1-KTLxaMr-MufUkbvEQC0Ga1wVqvhzA0-7I8Y5lutUSsaFrlBygvVCwf7geNjP9Jvvfe7L-bxjrs29h4wNfrj7NecZEqy8CsYRScMB3yd5By__UuNgcLnRAz0Wdq7hPInWFAc9V2p6GN9dCKRPP6_YJx880Ik9fex4tZuiKRKtpkamJrl4Ou9moK2twCmGh8QpPsZckfAGfiZH1z&gsessionid=VWv8fORuLuZ1niXobqk6KxiDYiXkW6bkJL0i4n04XbU0mrgQGjiWuA)  
  <sub>The Motley Fool, 2 hours ago</sub>  
  Nvidia's business is booming, but its headlines aren't. Here's a way to stay invested in AI chips without leaning on one company.
- [Chip Stocks Are Having Their Worst Two Months Since 2008](https://www.google.com/goto?url=CAESoQEBxCJF11KAkxXXc1p8sENy2T13gINe716I5h9g49_gXGd0U5b57dV8Wg4la6YKeTqdAA1hrzPM7xqw3p5X3qgJ0g_yjldyBK46xzi3HEB4UolUpqwSaJMbNqhOjZTsC7eZC1FlK5xGztO-cCpdz4u_isMOoZ5zpsEoCpaf__gBNMYCrXfukqFmZE609iALtAXjLO2mCZMTPhGfcJdzqQvYZA&gsessionid=VWv8fORuLuZ1niXobqk6KxiDYiXkW6bkJL0i4n04XbU0mrgQGjiWuA)  
  <sub>24/7 Wall St., 46 minutes ago</sub>  
  SOXX and SMH each plunged about 5% as chip stocks suffered their worst two-month stretch since 2008, with NVIDIA's earnings now looming.
- [Chip-Dollar: Deutsche Bank Says Chips Now Prop Up the Dollar - VanEck Semiconductor ETF (NASDAQ:SMH)](https://www.google.com/goto?url=CAESsgEBxCJF12nLjX16hHK3-2uNWKfFUVL_yJ3ThT8gF7vtSx5vY78_XFJgbMu1Sujxje8uEYs62yMXBQF60U1mPBj1lGlRd59IDs0YAey-Gy4I0HlNTyBPJzBQVWE5v3Qvm7bhE-hyli0KTMFGYdzmp3BUkMbx0FvoqtsXpoOwyIJt8xfWTH3CK6V5F7hxaVKqPPzhh0hu5Hm32lWcB6sayZTCJg2Spk-DP9dtjxZm4Y6Zi3fI&gsessionid=VWv8fORuLuZ1niXobqk6KxiDYiXkW6bkJL0i4n04XbU0mrgQGjiWuA)  
  <sub>Benzinga, 22 hours ago</sub>  
  Deutsche Bank says the chip-dollar is replacing the petrodollar, as Asian chip surpluses flow into US stocks, not Treasuries. A riskier prop. SMH.
- [Situational Awareness Revives AI Portfolio After Summer Collapse — Here Are Its New Stock Bets](https://www.google.com/goto?url=CAES1wEBxCJF1xnlEDfFKIN8mNKydY2q-G8lqpHvbEaxafcR1_7Rfg5DDTLBQrwlPCH9XzrSI8xgsU-ke8270WJEh507lPGlaZILEXyi1e96745GyWIBRQVxKBt6uNXKi9wQpN4pzcv8ZhoAId8Ffn9Yd18lDSqHlIBR6O6i4aKMXKY6W7innD7tEOGsGEsOmaRJkzYY0jS0rPhRHWWmAFgfJczuNK7nmGggpfYcJ28rA0L7OpBXTqidwBbd6EeQ1jNdIPcK7eEWG_BwdN8KST9uwO38R4_wss1-sQ&gsessionid=VWv8fORuLuZ1niXobqk6KxiDYiXkW6bkJL0i4n04XbU0mrgQGjiWuA)  
  <sub>TradingView, 9 hours ago</sub>  
  Situational Awareness, the AI fund that nearly wound down over the summer after a sharp pullback in chip stocks, is back in the business.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 463.70 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 509.68 (-9.0%), 50d 555.50 (-16.5%), 200d 524.46 (-11.6%); 50d above 200d
Momentum: RSI(14) 36.2 | MACD -25.054 vs signal -22.908 (histogram -2.146)
Returns: 1d +0.4% | 5d -4.1% | 1m -15.5% | 3m -17.3%
52-week range: 325.10 - 668.91 (now 40.3% of the way up)
Volatility: ATR(14) 23.10 (5.0% of price) | annualised 20d 67.4%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Technology
What it holds: P/E 28.22 | P/B 9.76 | P/S 11.19 | 3y earnings growth n/a
Yield: 0.2%
Three-year record: +46.7% a year | beta to the market 2.12
Cost and size: expense ratio 0.35% | net assets 66.44B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: NVIDIA Corp 20.2%, Taiwan Semiconductor Manufacturing Co Ltd ADR 9.6%, Texas Instruments Inc 5.7%, Broadcom Inc 5.6%, Advanced Micro Devices Inc 5.3%
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
Rolled up from the 5 largest holdings, 46.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.58 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +55.4% above the current prices
Holdings read: NVDA, TSM, TXN, AVGO, AMD
Recent rating changes among them:
  - NVDA: 2026-11-12 Melius Research: down, Buy -> Hold
  - TSM: 2026-11-04 Bernstein: main, Outperform -> Outperform
  - TXN: 2026-10-22 Jefferies: main, Hold -> Hold
  - AVGO: 2026-10-27 Rosenblatt: main, Buy -> Buy
  - AMD: 2026-11-12 B of A Securities: main, Buy -> Buy
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
Share count change: 1 week: -8.3% (-5.77B) over 10d | 1 month: +7.2% (4.27B) over 32d
Shares outstanding: 136.49M | fund size: 63.29B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [iShares MSCI Turkey ETF (TUR)](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc6ae11313462184edad67a0066d4c&url=https%3a%2f%2ffinance.yahoo.com%2fquote%2fTUR%2fpress-releases%2f&c=1706393195087887909&mkt=en-us)  
  <sub>Yahoo Finance, 26h ago</sub>  
  The above button links to Coinbase. Yahoo Finance is not a broker-dealer or investment adviser and does not offer securities or cryptocurrencies for sale or facilitate trading. Coinbase pays us for ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 31.68 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 31.21 (+1.5%), 50d 33.93 (-6.6%), 200d 38.51 (-17.7%); 50d below 200d
Momentum: RSI(14) 45.6 | MACD -0.470 vs signal -0.802 (histogram 0.332)
Returns: 1d -1.3% | 5d -0.3% | 1m -0.4% | 3m -22.1%
52-week range: 29.53 - 43.74 (now 15.1% of the way up)
Volatility: ATR(14) 0.60 (1.9% of price) | annualised 20d 33.6%
Volume: 0.02x the 20-day average
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
Three-year record: +0.6% a year | beta to the market 0.60
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
Weighted price target: +29.2% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 15.65M | fund size: 495.79M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [The Housing Market Is Finally Turning (BATS:ITB)](https://seekingalpha.com/article/4968975-the-housing-market-is-finally-turning?source=generic_rss)  
  <sub>2 hours ago</sub>  
  Remain neutral-bearish on homebuilders and would avoid housing REITs and ETFs; persistent stagnation and margin pressure limit aggregate opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 96.00 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 94.93 (+1.1%), 50d 92.97 (+3.3%), 200d 94.94 (+1.1%); 50d below 200d
Momentum: RSI(14) 57.1 | MACD 1.128 vs signal 1.075 (histogram 0.053)
Returns: 1d -0.2% | 5d -1.1% | 1m +5.8% | 3m -2.6%
52-week range: 87.00 - 100.95 (now 64.5% of the way up)
Volatility: ATR(14) 1.33 (1.4% of price) | annualised 20d 18.7%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Real Estate
What it holds: P/E 28.38 | P/B 2.42 | P/S 4.62 | 3y earnings growth n/a
Yield: 3.6%
Three-year record: +13.1% a year | beta to the market 0.92
Cost and size: expense ratio 0.13% | net assets 69.46B
What it is made of: Stocks 98.9%, Cash 0.8%, Other 0.3%
Largest holdings: Vanguard Real Estate II Index 14.5%, Welltower Inc 9.1%, Prologis Inc 6.9%, Equinix Inc 5.7%, American Tower Corp 4.3%
Sector mix: Real estate 99.5%, Communication services 0.3%, Energy 0.1%, Industrials 0.0%
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
Rolled up from the 5 largest holdings, 40.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.5% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2026-11-11 UBS: main, Buy -> Buy
  - PLD: 2026-11-02 Wells Fargo: main, Overweight -> Overweight
  - EQIX: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - AMT: 2026-11-05 Argus Research: reit, Buy -> Buy
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
Share count change: 1 week: +1.8% (1.21B) over 10d | 1 month: -1.2% (-817.31M) over 32d
Shares outstanding: 720.15M | fund size: 69.13B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Should you invest in the VanEck biotech ETF (BBH)?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc69438e794c71a26e7000a3266373&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2fgeneral%2fshould-you-invest-in-the-vaneck-biotech-etf-bbh%2far-AA2hBzSY&c=8685010539323390300&mkt=en-us)  
  <sub>Zacks Investment Research on MSN, 12h ago</sub>  
  Launched on December 20, 2011, the VanEck Biotech ETF (BBH) is a passively managed exchange traded fund designed to provide a broad exposure to the Healthcare - Biotech segment of the equity market.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 146.85 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 153.00 (-4.0%), 50d 153.60 (-4.4%), 200d 143.17 (+2.6%); 50d above 200d
Momentum: RSI(14) 42.7 | MACD -1.095 vs signal -0.336 (histogram -0.760)
Returns: 1d +0.7% | 5d -5.3% | 1m -0.7% | 3m -13.4%
52-week range: 113.83 - 169.55 (now 59.3% of the way up)
Volatility: ATR(14) 4.77 (3.2% of price) | annualised 20d 39.3%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Health
What it holds: P/E n/a | P/B 0.21 | P/S 0.13 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +31.1% a year | beta to the market 1.01
Cost and size: expense ratio 0.35% | net assets 10.92B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Moderna Inc 2.4%, Natera Inc 1.8%, Halozyme Therapeutics Inc 1.8%, Twist Bioscience Corp 1.8%, Biogen Inc 1.7%
Sector mix: Healthcare 99.4%, Financial services 0.6%
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
Rolled up from the 5 largest holdings, 9.5% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 75.0% | hold 25.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.1% above the current prices
Holdings read: MRNA, NTRA, HALO, TWST, BIIB
Recent rating changes among them:
  - MRNA: 2026-11-09 Goldman Sachs: main, Neutral -> Neutral
  - NTRA: 2026-11-09 Baird: main, Outperform -> Outperform
  - HALO: 2026-11-11 Morgan Stanley: down, Overweight -> Equal-Weight
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - BIIB: 2026-11-09 Piper Sandler: reit, Overweight -> Overweight
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
Share count change: 1 week: +1.1% (120.95M) over 7d | 1 month: +2.7% (282.52M) over 31d
Shares outstanding: 72.51M | fund size: 10.65B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Best ETFs for a Divided DC](https://www.kiplinger.com/investing/etfs/best-etfs-for-a-divided-dc)  
  <sub>1 hour ago</sub>  
  The next two years will see a Democratic Congress clash with a Republican president. That could be a surprisingly productive environment for these ETFs.
- [The Housing Market Is Finally Turning (BATS:ITB)](https://seekingalpha.com/article/4968975-the-housing-market-is-finally-turning?source=generic_rss)  
  <sub>2 hours ago</sub>  
  Remain neutral-bearish on homebuilders and would avoid housing REITs and ETFs; persistent stagnation and margin pressure limit aggregate opportunities.
- [DekaLux Team- GlobalSelect (FKQA.MU) latest stock news and headlines](https://www.google.com/goto?url=CAESbQHEIkXXj-NoAAJqKLkso6uH5chkLXil-ESD9iRg3M-Dc5dQPFZ_EerEmudBvsP9WH0e4_ClP0Q6zWT7AWlZdkRbvxW5oPYPUCrd5J4BDrHTudsDSAY3XINz_GUV2vGWgG1eAfG1O7n5rJyTbhE&gsessionid=Ci1iCHxx1Pzt3uuFBP9nHe0eI8hcTyGU1u3PjKOqYpPnJcxDym2XKw)  
  <sub>24 hours ago</sub>  
  Munich - Delayed Quote • EUR. DekaLux Team- GlobalSelect (FKQA.MU). 415.27 -4.94 (-1.18%). As of 8:07:43 CET. Market open. Related ETF news...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 101.69 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 101.45 (+0.2%), 50d 98.48 (+3.3%), 200d 104.62 (-2.8%); 50d below 200d
Momentum: RSI(14) 51.9 | MACD 1.119 vs signal 1.332 (histogram -0.212)
Returns: 1d +0.7% | 5d -1.4% | 1m +8.0% | 3m -6.0%
52-week range: 92.84 - 121.36 (now 31.0% of the way up)
Volatility: ATR(14) 2.73 (2.7% of price) | annualised 20d 39.1%
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
Three-year record: +10.7% a year | beta to the market 1.40
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
Weighted price target: +8.9% above the current prices
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
Share count change: 1 week: +0.2% (3.06M) over 7d | 1 month: +3.7% (57.72M) over 31d
Shares outstanding: 15.98M | fund size: 1.62B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 51.90 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 52.29 (-0.7%), 50d 50.90 (+2.0%), 200d 51.26 (+1.2%); 50d below 200d
Momentum: RSI(14) 50.2 | MACD 0.343 vs signal 0.504 (histogram -0.161)
Returns: 1d +0.8% | 5d -1.8% | 1m +1.9% | 3m -1.2%
52-week range: 42.23 - 53.90 (now 82.9% of the way up)
Volatility: ATR(14) 0.90 (1.7% of price) | annualised 20d 21.3%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Natural Resources
What it holds: P/E 21.94 | P/B 2.74 | P/S 1.71 | 3y earnings growth n/a
Yield: 1.6%
Three-year record: +12.7% a year | beta to the market 0.76
Cost and size: expense ratio 0.08% | net assets 8.45B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Linde PLC 12.8%, Newmont Corp 6.1%, Vulcan Materials Co 5.1%, Ecolab Inc 5.1%, Air Products and Chemicals Inc 4.9%
Sector mix: Basic materials 82.3%, Consumer cyclical 17.7%
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
Shares outstanding: 71.92M | fund size: 3.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected) (Bing's feed, direct: 3 headline(s), none naming XLB)

### US media and communication (XLC) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Disney bets on streaming and content to drive FY27 growth — raises dividend, targets $9B buyback](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc6965c8f54197820e3406b727f3e4&url=https%3a%2f%2fwww.msn.com%2fen-in%2fnews%2fother%2fdisney-bets-on-streaming-and-content-to-drive-fy27-growth-raises-dividend-targets-9b-buyback%2far-AA2hD5WK&c=5296345256429191213&mkt=en-us)  
  <sub>Asianet Newsable on MSN, 9h ago</sub>  
  Disney expects about $11 billion in free cash flow and 8% growth in total segment operating income in fiscal 2027.
- [State Street Communication Services Select Sector SPDR ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc6965c8f54197820e3406b727f3e4&url=https%3a%2f%2fwww.wsj.com%2fmarket-data%2fquotes%2fetf%2fMX%2fXLC&c=9973890150073057195&mkt=en-us)  
  <sub>Wall Street Journal, 23h ago</sub>  
  No news for XLC in the past two years. Stocks: Real-time U.S. stock quotes reflect trades reported through Nasdaq only; comprehensive quotes and volume reflect trading in all markets and are delayed ...
- [State Street® Communication Services Select Sector SPDR® ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc6965c8f54197820e3406b727f3e4&url=https%3a%2f%2fmarkets.businessinsider.com%2fetfs%2fstate-street-communication-services-select-sector-spdr-etf-us81369y8527&c=13538095965419772856&mkt=en-us)  
  <sub>Business Insider, 21h ago</sub>  
  Historical Prices for State Street® Communication Services Select Sector SPDR® ETF Sustainability Rating Copyright © 2026 Insider Inc and finanzen.net GmbH ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 106.13 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 105.11 (+1.0%), 50d 109.17 (-2.8%), 200d 112.23 (-5.4%); 50d below 200d
Momentum: RSI(14) 47.4 | MACD -0.440 vs signal -1.029 (histogram 0.590)
Returns: 1d -0.6% | 5d -1.5% | 1m -3.6% | 3m -4.7%
52-week range: 99.90 - 120.08 (now 30.9% of the way up)
Volatility: ATR(14) 1.97 (1.9% of price) | annualised 20d 23.0%
Volume: 0.08x the 20-day average
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
Three-year record: +18.1% a year | beta to the market 0.93
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
Weighted price target: +32.8% above the current prices
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
Share count change: 1 week: -3.6% (-774.82M) over 7d | 1 month: -2.9% (-635.73M) over 31d
Shares outstanding: 197.36M | fund size: 20.95B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [What State Street Energy SPDR ETF (XLE) Bought: Exxon Leads on Nov. 13](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc6917e34a463f94eaf231315c3e58&url=https%3a%2f%2ffinance.yahoo.com%2fenergy%2farticles%2fstate-street-energy-spdr-etf-110403957.html&c=13732862203939100256&mkt=en-us)  
  <sub>Yahoo Finance, 12h ago</sub>  
  State Street Energy Select Sector SPDR ETF (XLE) is an equity fund in the Equity Theme - Natural Resources category, holding 21 stocks with 78.9% of assets in its 10 largest holdings. All of its ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 64.39 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 65.78 (-2.1%), 50d 64.97 (-0.9%), 200d 59.61 (+8.0%); 50d above 200d
Momentum: RSI(14) 47.7 | MACD -0.569 vs signal -0.340 (histogram -0.229)
Returns: 1d +1.1% | 5d +3.5% | 1m -5.0% | 3m +1.3%
52-week range: 43.81 - 70.02 (now 78.5% of the way up)
Volatility: ATR(14) 1.52 (2.4% of price) | annualised 20d 31.4%
Volume: 0.08x the 20-day average
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
Three-year record: +19.3% a year | beta to the market -0.22
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
  Petrol: 210.8 million barrels, +1.8 on the week (a build), 35% percentile over 52 weeks
  Diesel: 103.3 million barrels, +4.1 on the week (a build), 21% percentile over 52 weeks
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

```text
Rolled up from the 5 largest holdings, 59.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.10 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.8% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 186.42M | fund size: 12.00B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Which Sectors Do Well Amid 5% 10-Year Treasury Yields?](https://www.etftrends.com/sector-investing-content-hub/which-sectors-well-amid-5-percent-10-year-treasury-yields/)  
  <sub>ETF Trends, 18 hours ago</sub>  
  Inflation is remaining persistent and the latest CPI and PPI reports are coming in hot. So the 10-year U.S. Treasury yield may be sitting around the 5%...
- [Broad Sector Exposure Through The Fidelity MSCI Financials Index ETF (FNCL)](https://seekingalpha.com/article/4962758-fncl-broad-sector-exposure-through-the-fidelity-msci-financials-index-etf)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  Fidelity MSCI Financials Index ETF tracks an MSCI index of U.S. financials of all sizes. Its classification counts Visa, Mastercard, and other payment...
- [Webcast: The evolving income playbook: Putting sectors to work | ETF Trends](https://www.google.com/goto?url=CAESygEBxCJF16-raFFbcjYXbdwoHqtCNiC0uBilLQLinCMUXT6cuA2kY0OmAY_dBYeWPUP7p6wmKQST-mZoqO4h73BYO7HYJukMjoW0Yh63-0WVlpmyUpWlgMCyoCZzU_FENuXMwIu7R-3m77xxDopo4LLX0JpQRNb2akbQH-YnbJAX5NGEx9YsYJ9N24Ms2Ie-fR-DZM7vMCgNzwckd5aPQ2brS6_klkMgSOqNpjvXTnkd-YNDNfeo__jRfXRG_dqoQ3D5S5v6XP5zbL4N&gsessionid=rLHVjf1FuWn6XCmw-DAcpcRoQt4RgJdAbA-6UH8vsBzMHw44OXjjGA)  
  <sub>Advisor Perspectives, 20 hours ago</sub>  
  Traditional sources of income are facing growing challenges. Declining dividend yields, shifting macro policy, and persistent bond volatility have made...
- [Forget Nvidia — S&P 500's 8,900 Target Puts These ETFs in Play - State Street SPDR S&P 500 ETF Trust (ARC](https://www.google.com/goto?url=CAESugEBxCJF1yoRYObJJH95LhdK2-Xsp-PYmNQsuWDHQStiLXVMPVeKYVc2zhQRkmz_zeeovkQNCboBwCPN9_miXbJfAXBRxXUoQPY3nzAxmhjoTh2H3I95nMdQhJFvUrVcgqiGYfxzJzWwK_MlEdzXPls3AO6_KP-l3WBUhX-tbru1x2lqrknbIQ10xZc1__H3Gx_2btP5sRF5FJO_n7jbugrgVOsgR0vxSyspIAtZtjCNUQhMpPAVJOj0vwM&gsessionid=rLHVjf1FuWn6XCmw-DAcpcRoQt4RgJdAbA-6UH8vsBzMHw44OXjjGA)  
  <sub>Benzinga, 22 hours ago</sub>  
  Wall Street sees the S&P 500 climbing to 8900. Discover which sector ETFs could benefit as investors look beyond Big Tech and the AI trade.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 57.87 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 57.33 (+0.9%), 50d 55.98 (+3.4%), 200d 53.99 (+7.2%); 50d above 200d
Momentum: RSI(14) 55.5 | MACD 0.716 vs signal 0.681 (histogram 0.035)
Returns: 1d -0.5% | 5d -0.7% | 1m +5.1% | 3m +0.7%
52-week range: 47.81 - 59.20 (now 88.3% of the way up)
Volatility: ATR(14) 0.86 (1.5% of price) | annualised 20d 21.6%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Financial
What it holds: P/E 15.26 | P/B 2.28 | P/S 3.26 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +22.0% a year | beta to the market 0.68
Cost and size: expense ratio 0.08% | net assets 53.58B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Berkshire Hathaway Inc Class B 12.7%, JPMorgan Chase & Co 11.2%, Visa Inc Class A 8.8%, Mastercard Inc Class A 6.5%, Bank of America Corp 4.1%
Sector mix: Financial services 98.2%, Technology 1.6%, Industrials 0.3%
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
Rolled up from the 5 largest holdings, 43.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.86 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.8% above the current prices
Holdings read: BRK-B, JPM, V, MA, BAC
Recent rating changes among them:
  - BRK-B: 2026-10-22 UBS: main, Buy -> Buy
  - JPM: 2026-11-02 UBS: main, Buy -> Buy
  - V: 2026-11-11 Bernstein: main, Outperform -> Outperform
  - MA: 2026-11-11 Bernstein: main, Outperform -> Outperform
  - BAC: 2026-11-02 UBS: main, Buy -> Buy
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
Shares outstanding: 883.44M | fund size: 51.12B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Consumer Staples Beat Tech by Most Since 2001: XLP vs XLK - State Street Consumer Staples Select Sector S](https://www.benzinga.com/etfs/sector-etfs/26/11/63338658/consumer-staples-xlp-tech-xlk-rotation-since-2001)  
  <sub>Benzinga, 59 minutes ago</sub>  
  Consumer staples fund XLP has beaten tech fund XLK by 39.5% in seven weeks, the widest gap since March 2001.
- [Weekly ETF flows: seven of 11 sectors record outflows; technology leads inflows](https://www.tradingview.com/news/seekingalpha:c04723886094b:0-weekly-etf-flows-seven-of-11-sectors-record-outflows-technology-leads-inflows/)  
  <sub>TradingView, 1 hour ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 Trust AMEX:SPY, saw inflows of $320.13M for the week ending November 13, while its price increased by...
- [ValuEngine Weekly Market Commentary With Strategy Notes](https://www.google.com/goto?url=CAESsAEBxCJF18bAdGfqVlNM-epOaBbw4Orwp4LmDRvDDGeaNiYMXFs8Qttbjn438CA2LWb-lJ49T8rgWklgtlkAWNx-W6GapwGm93vLx9AjF82YcmYAuKz_1-a3Q2FNGKFHVauXCW_WJ2qz60NpTgiY6Lj9BbAVh0ad99oAf-6KaK7XBhEk7pVDl5u6epkimRJkI8EHtZYILh3CWQEBm7otPx3EpNi97SHMZHEcy55TSGV-Ig&gsessionid=SRrJMv3JKZ9ZIA9S0AkkhV4faUEzs4CerOUcROFwenCdLf0KyefV1w)  
  <sub>Seeking Alpha, 45 minutes ago</sub>  
  Despite a choppy finish on Thursday-Friday, US equities snapped a multi-week losing streak to post their first weekly gain since early Oct. All 11 Select...
- [$214.8M Buying Sweep Lifts Every Position In State Street's Industrial ETF (NYSEARCA: XLI)](https://www.google.com/goto?url=CAESxAEBxCJF17vPbCdpsS63kIGQo_qrdB7tD4ZB3-Y4PI9EH0H5RRMvENd5r9eCrHkG70eggc7aenzQ5fCfghphraFweON8oqPkgirEnmiwe2qSHqeuLQx9gkkQ5vyAxb-TYxY5HXCOB8HnNv5sICIRJh8wF6-_tp6TQUB8RtTpZoIUJaOmK4JoMsQkPtodgc17G2wc4d_lDeVa33U264n1hpnWfnW9RKbwP8rc0dn1YGqSqLrxHCczz6FhQmFEvFHZGhF1y4Zl&gsessionid=SRrJMv3JKZ9ZIA9S0AkkhV4faUEzs4CerOUcROFwenCdLf0KyefV1w)  
  <sub>Foreign Policy Journal, 22 hours ago</sub>  
  A rare all-in trading session left the $31.21 billion State Street Industrial Select Sector SPDR ETF (NYSEARCA: XLI) with gains across every one of its 83.
- [Forget Nvidia—Wall Street Sees S&P 500 at 8,900, Putting These ETFs in Play](https://www.google.com/goto?url=CAESwwEBxCJF15fVLWYBEMo9134VcEKGSAERQ3B_VBeESXUso8tnsfoRWmUCbnN8XywrA5Oph45CFMKjrEhXOVN04tX9tBUW4fclvV5-pzhMNloBPoDsxkpwS0IiSJaObrxz1e89qYLjCceMIcSDkOnJgVKrW9FUH7PyKuK7jXbVW05PmwJywg6lf5vy7eNn_CP6Im56xN33AFz2u-IQVvZQ1EpeE1d88X8YZ7C-Aa0E-7UrPRibqf_BT1Q4--eiHKW4CXi1DCM&gsessionid=SRrJMv3JKZ9ZIA9S0AkkhV4faUEzs4CerOUcROFwenCdLf0KyefV1w)  
  <sub>TradingView, 22 hours ago</sub>  
  Nvidia Corp NASDAQ:NVDA may be dominating the headlines after Jensen Huang's shock exit last week, but Wall Street's next big call is about something much...
- [Andersen Group leads industrial stocks with biggest Q3 earnings surprise (XLI:NYSEARCA)](https://www.google.com/goto?url=CAESqwEBxCJF167EvfD4pNHmWSe0fQcmO8ID3yZ44xOX4beXttBWU7yJ7-TmVchev7C3qFFbYif9fuFRsX4g1QasbLynggM36T7R0HS8VZbVjZ_UoaJYBeqHjzQ63nalJ0BmIKxyVBXi0Gp-JnnZhiohb58R9c1DTQT9VSz8dPAjpLIjlCnhktM_rAwcIudaAbSKByF9A7R_tv0p557_MqZuYkv9kIM7s-r-5n9xOkE&gsessionid=SRrJMv3JKZ9ZIA9S0AkkhV4faUEzs4CerOUcROFwenCdLf0KyefV1w)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Andersen Group tops Q3 industrial EPS surprises at $6.04, ahead of United Rentals at $1.52 and Sterling Infrastructure at $1.41.
- [Webcast: The evolving income playbook: Putting sectors to work | ETF Trends](https://www.google.com/goto?url=CAESygEBxCJF1x6K2rKA3O7JsrEIBRLGcWAZ7m_i2J3X-US3qHBF8Nmssuge5OJNsJ2wcLi64VWeXqiNiC5s0RvHZxo4FtMD8I1b92IHR8qSMhKiGnfRZwPTCS73RXGAoEv2PY-uxVzf_RqFw9oz6MdHZ4Dhe1Rxev-fndrPI1E3BOZ2bxnWUhwf11IUUAu9UbkcuqjFBS4Xp-IXzR3oBIa6vR2EAgd5V9NOu48FB04oQvfPObn_1_mnNlNoUzWBv8oWDnDseHWyCIuTSskq&gsessionid=SRrJMv3JKZ9ZIA9S0AkkhV4faUEzs4CerOUcROFwenCdLf0KyefV1w)  
  <sub>Advisor Perspectives, 20 hours ago</sub>  
  Traditional sources of income are facing growing challenges. Declining dividend yields, shifting macro policy, and persistent bond volatility have made...
- [Is Wall Street Bullish or Bearish on Ferguson Enterprises Stock?](https://www.google.com/goto?url=CAESqAEBxCJF18zeN8l70EhfDUatZK241K3lZvwWIfWG8C3gXWtb1Keg9a2tgtIcuVip-K-mr1kAoI9ziydqzQUp_ruMcHad5H0-38tt96K8j7VPIiHqppNSMdN9L1_byw9eUI-dg8Vp2RekfqPoxLea7eddFYkxvZpR4rmqEM5eNG08ua3c0NyVcOk_pnBtQUVezXmYmRm2bIzPwbwHvt1Q3U7Q0CY_HeshOn8&gsessionid=SRrJMv3JKZ9ZIA9S0AkkhV4faUEzs4CerOUcROFwenCdLf0KyefV1w)  
  <sub>Barchart.com, 5 hours ago</sub>  
  Ferguson Enterprises has lagged behind the broader market over the past year, yet analysts remain cautiously optimistic about the stock's prospects.
- [State Street Materials Select Sector SPDR ETF (XLB) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZAHEIkXXhYAhtbjkWIcIFpaG1b93xg6Oz2qBnIP2pUC3PYWRuo40I-LePJIHdPpfyItBdliC_9er3Um_hfD0wdcVSTyo6tMRkZSHC-zamqkJIi7xcu_4HnjHKM4PbHtBXn2TnFk&gsessionid=SRrJMv3JKZ9ZIA9S0AkkhV4faUEzs4CerOUcROFwenCdLf0KyefV1w)  
  <sub>Yahoo! Finance Canada, 23 hours ago</sub>  
  Find the latest State Street Materials Select Sector SPDR ETF (XLB) stock quote, history, news and other vital information to help you with your stock...
- [What Are Wall Street Analysts' Target Price for AMETEK Stock?](https://www.google.com/goto?url=CAESpAEBxCJF13StMISIEdbYKDUkdzxGbUYJvTtvx0N8yZd6GafGbaHao1fun8tE2x6rpkrp7xwRzHSqQzHVThINhJ-fUDwZWVIgRNAZGk099m0dItRKcRy4zDt1_qwJyM73c4fuLd9VM0l1H1Hw2jBdZu-rIf4sQz7i1hKbuV7Bxgpm3SCDxWLSfrOSRfRBusN85DEMmamBPdg9J8hnWUTl0OYbEP6BSQ&gsessionid=SRrJMv3JKZ9ZIA9S0AkkhV4faUEzs4CerOUcROFwenCdLf0KyefV1w)  
  <sub>Barchart.com, 2 hours ago</sub>  
  Berwyn, Pennsylvania-based AMETEK, Inc. (AME) manufactures and sells electronic instruments (EIG) and electromechanical (EMG) devices in the United States...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 166.59 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 167.76 (-0.7%), 50d 168.61 (-1.2%), 200d 173.45 (-4.0%); 50d below 200d
Momentum: RSI(14) 46.6 | MACD -0.435 vs signal -0.475 (histogram 0.040)
Returns: 1d +0.6% | 5d -1.3% | 1m -0.1% | 3m -8.4%
52-week range: 147.83 - 186.51 (now 48.5% of the way up)
Volatility: ATR(14) 3.06 (1.8% of price) | annualised 20d 26.1%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Industrials
What it holds: P/E 26.85 | P/B 6.33 | P/S 2.84 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +19.7% a year | beta to the market 1.00
Cost and size: expense ratio 0.08% | net assets 31.20B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: GE Aerospace 5.9%, Caterpillar Inc 5.4%, RTX Corp 5.1%, GE Vernova Inc 4.3%, Union Pacific Corp 3.4%
Sector mix: Industrials 93.0%, Technology 6.5%, Basic materials 0.4%, Consumer cyclical 0.2%
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
Rolled up from the 5 largest holdings, 24.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.4% above the current prices
Holdings read: GE, CAT, RTX, GEV, UNP
Recent rating changes among them:
  - GE: 2026-10-21 UBS: main, Buy -> Buy
  - CAT: 2026-11-10 Evercore ISI Group: main, Outperform -> Outperform
  - RTX: 2026-10-21 UBS: main, Neutral -> Neutral
  - GEV: 2026-11-11 JP Morgan: main, Overweight -> Overweight
  - UNP: 2026-11-05 Baird: down, Outperform -> Neutral
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
Shares outstanding: 136.63M | fund size: 22.76B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Consumer Staples Beat Tech by Most Since 2001: XLP vs XLK - State Street Consumer Staples Select Sector S](https://www.benzinga.com/etfs/sector-etfs/26/11/63338658/consumer-staples-xlp-tech-xlk-rotation-since-2001)  
  <sub>Benzinga, 58 minutes ago</sub>  
  Consumer staples fund XLP has beaten tech fund XLK by 39.5% in seven weeks, the widest gap since March 2001.
- [Which Sectors Do Well Amid 5% 10-Year Treasury Yields?](https://www.etftrends.com/sector-investing-content-hub/which-sectors-well-amid-5-percent-10-year-treasury-yields/)  
  <sub>ETF Trends, 18 hours ago</sub>  
  Inflation is remaining persistent and the latest CPI and PPI reports are coming in hot. So the 10-year U.S. Treasury yield may be sitting around the 5%...
- [FDTX: Technology Dashboard For November (NASDAQ:FDTX)](https://www.google.com/goto?url=CAESowEBxCJF1zIIZUkdehhkTRVsd9SNl84uAjUepDnDPzIwQzzyuNCOeESXGllD3Gtt0HLGXwY0nbz2_HtUfK2W_bAYtCk1F3Kwo0vq00GCEQzRN4Ct3zj6O2bUUNhSJ-dvknjLBRFs73ulUUbp7UVPhUXP0pMB6ttn0IZhQ_KUyZ9r_d8NzDx51iwo2tfuTyw4mdIbSTgRV7hMy8EPiDoxXT2vta_j&gsessionid=hHAZcymNs8N7qra-KZwExRzTMPNopOGlKV-lcpFiGMOrQNVNpOj_3w)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  Fidelity Disruptive Technology ETF offers active, global technology exposure, but results have yet to justify its higher fee versus XLK.
- [Weekly ETF flows: seven of 11 sectors record outflows; technology leads inflows](https://www.google.com/goto?url=CAESygEBxCJF110THc_JWMxPadha0zb1cBoc0KI_V-0LibiTVXVtZALNWtGxKC18s5hZvZ_Plt_aU2h_Yi5W1xFGFN261mssRr0k-zKUysEkI0jjI7-uZcOQsXpuPOvxoMdfGNr-lO_3ymKMHiZaGY67FB3hzcb3i25PtkcZBIo597P8GEHoquAOlaaT5M4j492Uhn88YlvluWc-CdcEWfprWpzh-oPfmEyJIHfsjO2AAuz9PhtiMq09Bnd2tWRFenz-kTar7o5GQ8-Q9TWF&gsessionid=hHAZcymNs8N7qra-KZwExRzTMPNopOGlKV-lcpFiGMOrQNVNpOj_3w)  
  <sub>TradingView, 1 hour ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 Trust AMEX:SPY, saw inflows of $320.13M for the week ending November 13, while its price increased by...
- [VanEck Semiconductor ETF (SMH) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXXFOd8OiSJ5UdavB_MnfjhGRvR3b3Xd9g4Urn2fgHxWBwFU4zhrpsl9w3_tClZF3Tmtd91dXe8HQOXoBEP85pB9LGDCrBH2QMhW0EQytP-LZ6z-diiq7jNqXITkm5ygoA&gsessionid=hHAZcymNs8N7qra-KZwExRzTMPNopOGlKV-lcpFiGMOrQNVNpOj_3w)  
  <sub>Yahoo Finance UK, 17 hours ago</sub>  
  Find the latest VanEck Semiconductor ETF (SMH) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Markets Shrug Off Nvidia Turmoil, for Now](https://www.google.com/goto?url=CAESkQEBxCJF15VUwDINhfgCEk2bpcWfkEdgp60rBbmn0tTPoxuf0QFZAGA8ztEYqrFjhFKG4C0PmNd_dCf72FA5hdAOcea6x1CSYDu9gz4M_4LddtGqe7dQ5eEn0hXZbXwCWyEa1A5eizU83NGbPtT9BpPXjkWsN76j9EMXBsuxAw0NoyPAl1Bi6vFXPpvTmZ9nN7eK&gsessionid=hHAZcymNs8N7qra-KZwExRzTMPNopOGlKV-lcpFiGMOrQNVNpOj_3w)  
  <sub>Investing.com UK, 24 hours ago</sub>  
  Market Analysis by James Picerno covering: S&P 500, NVIDIA Corporation, NASDAQ Composite, Invesco S&P 500® Equal Weight ETF. Read James Picerno's Market...
- [Semtech Shares Fall Nearly 10% as Technology Stocks Weaken](https://www.google.com/goto?url=CAESawHEIkXXvEEJRtobqReUN4GhlQyFQfWrN0zJswoZBMSzRcwghGsG0stOcYbO-vtSaObMDApZ9jqVhIksOk5lNVihYfj5IVrsEv5ewlReA2feCazz3oFgmt2ldeYWQaGE_TfOumwDFN8etehO&gsessionid=hHAZcymNs8N7qra-KZwExRzTMPNopOGlKV-lcpFiGMOrQNVNpOj_3w)  
  <sub>www.tokenpost.com, 23 hours ago</sub>  
  The shares were down $11.17 by 10:32 a.m. ET, roughly an hour into trading; technology ETF XLK was also lower.
- [Bloom Energy (BE) Shares Drop Nearly 8% Amid Tech Sector Selloff on November 16, 2026](https://www.google.com/goto?url=CAEStQEBxCJF122chS7Mst8kwAsmXvfD2B9ayWx0ObwUtJZao82B4ep-tddfnk79xChWIHEgSg2ziGy3R1d7oIupDp56PApnJPKAXapkROPWJrSWveFqaW_3sW-oF2qzx1ok17UhxSLL7WK8pQtkjZ-3tztWxf6zVWdBug100UTSFiE30cB9i0n4ASqDwA1jQxmKOIw3OXwDQXf28gaEVwZMVrj8UMipxzdAe49wnqKbDqayVk0cA51j&gsessionid=hHAZcymNs8N7qra-KZwExRzTMPNopOGlKV-lcpFiGMOrQNVNpOj_3w)  
  <sub>GuruFocus, 22 hours ago</sub>  
  On November 16, 2026, Bloom Energy Corp (NYSE: BE) saw its stock price decline sharply by almost 8%, closing at $177.51 after falling $14.48 during the...
- [Semtech (SMTC) Shares Drop 10% Amid Tech Selloff on November 16, 2026](https://www.google.com/goto?url=CAESpQEBxCJF15aGgA3H0x571g2NdU1WSpOiCnv50J1BQmdCTDHy4bZt6swJ8fTBuMVVFcWCvrRjvvTfIdFoHATdkMpYKPh_Gylz6-emu2LFiMb2jt8csuQDxG69ZUMsWZToJJRHJ_41E2ZKUciv7NCCBd_s0nndKMSIt2xJRX70R6UNLvvF_isqAfYT_HB_W8WL0-UsMmc4RLtYQrUljg3gt_TubtS4GGQ&gsessionid=hHAZcymNs8N7qra-KZwExRzTMPNopOGlKV-lcpFiGMOrQNVNpOj_3w)  
  <sub>GuruFocus, 22 hours ago</sub>  
  On November 16, 2026, Semtech Corporation (ticker: SMTC) saw its stock price decline sharply by approximately 10%, trading near $103.42 an hour into the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 164.41 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 176.54 (-6.9%), 50d 186.18 (-11.7%), 200d 171.02 (-3.9%); 50d above 200d
Momentum: RSI(14) 34.9 | MACD -5.944 vs signal -5.219 (histogram -0.726)
Returns: 1d -0.2% | 5d -2.7% | 1m -11.6% | 3m -10.5%
52-week range: 127.50 - 202.00 (now 49.6% of the way up)
Volatility: ATR(14) 5.29 (3.2% of price) | annualised 20d 45.5%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Technology
What it holds: P/E 31.66 | P/B 11.55 | P/S 8.87 | 3y earnings growth n/a
Yield: 0.5%
Three-year record: +24.8% a year | beta to the market 1.56
Cost and size: expense ratio 0.08% | net assets 118.67B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Apple Inc 15.3%, NVIDIA Corp 15.1%, Microsoft Corp 11.8%, Broadcom Inc 4.7%, Advanced Micro Devices Inc 4.5%
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
Rolled up from the 5 largest holdings, 51.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.70 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +33.8% above the current prices
Holdings read: AAPL, NVDA, MSFT, AVGO, AMD
Recent rating changes among them:
  - AAPL: 2026-11-11 China Renaissance: up, Hold -> Buy
  - NVDA: 2026-11-12 Melius Research: down, Buy -> Hold
  - MSFT: 2026-10-29 Bernstein: main, Outperform -> Outperform
  - AVGO: 2026-10-27 Rosenblatt: main, Buy -> Buy
  - AMD: 2026-11-12 B of A Securities: main, Buy -> Buy
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
Share count change: 1 week: -4.7% (-5.61B) over 10d | 1 month: +7.5% (7.95B) over 32d
Shares outstanding: 697.10M | fund size: 114.61B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Lock In the Consumer Staples Sector With This ETF](https://pro.thestreet.com/trade-ideas/lock-in-the-consumer-staples-sector-with-this-etf)  
  <sub>RealMoney Pro, 36 minutes ago</sub>  
  Monday was another rough day for the major indexes. On the other hand, it was a pretty good day for the consumer staples sector.
- [Consumer Staples Beat Tech by Most Since 2001: XLP vs XLK - State Street Consumer Staples Select Sector S](https://www.benzinga.com/etfs/sector-etfs/26/11/63338658/consumer-staples-xlp-tech-xlk-rotation-since-2001)  
  <sub>Benzinga, 60 minutes ago</sub>  
  Consumer staples fund XLP has beaten tech fund XLK by 39.5% in seven weeks, the widest gap since March 2001.
- [iShs III-Flex.Inc.Bd Act.ETF R (IFLX.MU) stock price, news, quote and history](https://www.google.com/goto?url=CAESaAHEIkXXgr78WgAEi1nzk6Ve6SsRobsXGQdJ3MocaT9BfbmIs11b1aK_o-Q_-ONQRRf8VooRiTBIjrmK69iS8bRyM6rApWTlyHObCAiZypSDQWg71F4WiELdd6w5uv0Izm_3XgORCans&gsessionid=ziJbdq00QKCVlDZxxHF1HQvsXdDzkkgT_MtpaKwU12C136e6WwtStg)  
  <sub>Yahoo Finance Australia, 2 hours ago</sub>  
  Find the latest iShs III-Flex.Inc.Bd Act.ETF R (IFLX.MU) stock quote, history, news and other vital information to help you with your stock trading and...
- [Sector Update: Consumer](https://www.google.com/goto?url=CAESfwHEIkXXyVW6ZRhfwDsykYgLntHO-pZjUkN5rjBucNkcRyM6D60ur-MXCG0nHQTRy4EPZ7eQvPIyUamNIEHDupoQMey6DxgGZo6KN0I4pMTXlzhQT0pxXVMV5FF6GslFbQYNuAcB6H8RXf9VJqqFmP-JpvpAc_H9aW221v8pyyA&gsessionid=ziJbdq00QKCVlDZxxHF1HQvsXdDzkkgT_MtpaKwU12C136e6WwtStg)  
  <sub>Moomoo, 46 minutes ago</sub>  
  Consumerstocks were declining premarket Tuesday, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) down 0.9% and the State Street Consumer...
- [Which Sectors Do Well Amid 5% 10-Year Treasury Yields?](https://www.google.com/goto?url=CAESrgEBxCJF17cNtOn11vy8TBEfNAPkC-sQqUtGhNVi1nKJ1p27wXFhIWvONCRcoPSPGyJjJVKNBZIBwTRHJUg-flDCUa_d2Xbk0IZzL5BQDwWUJ6cmYKrnBipVCnPPu4Q0NvZLwpxnGbm7XD7Mv3rNTZ3Cdy-QNlPVM1F1M1CNCwwSSFmO6MSBdKlxxcQyUoUcEVOHzepWfBYWJjFMKNLUWwo-sPrPqnZykY2W1ls3PcA&gsessionid=ziJbdq00QKCVlDZxxHF1HQvsXdDzkkgT_MtpaKwU12C136e6WwtStg)  
  <sub>ETF Trends, 18 hours ago</sub>  
  Inflation is remaining persistent and the latest CPI and PPI reports are coming in hot. So the 10-year U.S. Treasury yield may be sitting around the 5%...
- [Your $300,000 in XLY Holds $125,585 in Amazon and Tesla Alone](https://www.google.com/goto?url=CAESpgEBxCJF1zUSXR3ONa42Rc4B9HR1Q7KqgokYyhVB7-Piyr3lfDyqST48xRaaA98_cAM2jCiszfqxJtFcXsgYBMzDaFu-0wx9HkQNVuTh_B63rS_LtIiJfK59BtKNmlcFlMZapoRv9CwQYCQPt67smGwi4zToVgO2VwRXZS5NdWFzECI8Wg1D6jSkVRKzKMh7hgPWoYVm-MMlIlTQJNbU9Dc-dsOfwWOA&gsessionid=ziJbdq00QKCVlDZxxHF1HQvsXdDzkkgT_MtpaKwU12C136e6WwtStg)  
  <sub>24/7 Wall St., 16 hours ago</sub>  
  A fund named for everyday American spending looks diversified until you open its holdings filing. Two familiar companies quietly steer the whole ride,...
- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXXQXfDm6njRA4KFRDEY2fxAwq8a0p_QympHFhxe1X_sTJK_8MQiEmeedCMDTj4r2F0Bz98-Bin5XrQ8pC6gkpy4dQzmpI5X6VhMZHFmHXesnoFcMnXvxPAR70UicI4PMs&gsessionid=ziJbdq00QKCVlDZxxHF1HQvsXdDzkkgT_MtpaKwU12C136e6WwtStg)  
  <sub>Yahoo Finance UK, 23 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) ... This price reflects trading activity during the overnight session on the Blue Ocean ATS, available 8...
- [Defensives Lead Sectors Monday As Growth Trails](https://www.google.com/goto?url=CAESpQEBxCJF198MoktENfcYp_KJoWfKXDRXuN2q6ryscsgoSfgrp4_Y6KCGrF8a9STuteiqszZCtKNU1zWlaPeRgn-s3miRFiDwfCdeDWz_YizzTce2hA7lTysIaJaOE3681nCSEB0p8r2Y6XPP4r1GRrjuqQL7bjya95RaHBzgYcASvPjpf_0h8pzseloFRTUd77L93F6fOgueRx42kFW1yIngvCM0Srg&gsessionid=ziJbdq00QKCVlDZxxHF1HQvsXdDzkkgT_MtpaKwU12C136e6WwtStg)  
  <sub>Benzinga, 23 hours ago</sub>  
  Four sectors are higher and seven are lower in Monday's regular session, with defensive sectors holding the top three positions. The leaders are clustered...
- [MUF-Amundi Topix II UCITS ETF A (JPNH.DU) Latest Stock News & Headlines - Yahoo Finance](https://www.google.com/goto?url=CAESbQHEIkXXO4fvn-O2o40_pJG5enuMA4kDF1CAnX8AUQrEJPATJQ2LhyPzZ6jMzPsYRDbiB3kPiQDnrkAtdZOSzufzVYv4vXmLlcBKlu3FCS_twrh7Iul4DVfPjbhk61ftzCSGvL38iAWg9PrbmQI&gsessionid=ziJbdq00QKCVlDZxxHF1HQvsXdDzkkgT_MtpaKwU12C136e6WwtStg)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Get the latest MUF-Amundi Topix II UCITS ETF A (JPNH.DU) stock news and headlines to help you in your trading and investing decisions.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 92.49 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 89.99 (+2.8%), 50d 85.98 (+7.6%), 200d 84.97 (+8.8%); 50d above 200d
Momentum: RSI(14) 65.1 | MACD 1.783 vs signal 1.699 (histogram 0.084)
Returns: 1d -0.1% | 5d +1.6% | 1m +6.1% | 3m +6.9%
52-week range: 76.51 - 92.60 (now 99.3% of the way up)
Volatility: ATR(14) 1.43 (1.5% of price) | annualised 20d 23.8%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Consumer Defensive
What it holds: P/E 24.06 | P/B 4.52 | P/S 1.32 | 3y earnings growth n/a
Yield: 2.5%
Three-year record: +13.1% a year | beta to the market 0.39
Cost and size: expense ratio 0.08% | net assets 15.03B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Walmart Inc 11.1%, Costco Wholesale Corp 9.1%, Procter & Gamble Co 7.6%, Coca-Cola Co 7.4%, Philip Morris International Inc 6.6%
Sector mix: Consumer defensive 97.0%, Financial services 1.5%, Consumer cyclical 1.5%
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +1.2% above the current prices
Holdings read: WMT, COST, PG, KO, PM
Recent rating changes among them:
  - WMT: 2026-11-12 BTIG: reit, Buy -> Buy
  - COST: 2026-11-11 Bernstein: main, Outperform -> Outperform
  - PG: 2026-10-26 Barclays: main, Equal-Weight -> Equal-Weight
  - KO: 2026-10-28 Freedom Broker: main, Hold -> Hold
  - PM: 2026-11-03 Stifel: main, Buy -> Buy
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
Shares outstanding: 210.17M | fund size: 19.44B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Tudor adds Iridium, exits Teck, boosts SPY stakes among Q3 trades](https://www.tradingview.com/news/seekingalpha:8d0d1723e094b:0-tudor-adds-iridium-exits-teck-boosts-spy-stakes-among-q3-trades/?mobileapp_new=true)  
  <sub>TradingView, 15 hours ago</sub>  
  Paul Tudor Jones' Tudor investment took a new stake in Iridium Communications NASDAQ:IRDM, shed its Teck Resources class B stock (TECK.
- [Forget Nvidia — S&P 500's 8,900 Target Puts These ETFs in Play - State Street SPDR S&P 500 ETF Trust (ARC](https://www.benzinga.com/etfs/broad-u-s-equity-etfs/26/11/63304335/wall-street-sees-sp-500-at-8900-putting-these-etfs-in-play)  
  <sub>Benzinga, 22 hours ago</sub>  
  Wall Street sees the S&P 500 climbing to 8900. Discover which sector ETFs could benefit as investors look beyond Big Tech and the AI trade.
- [AI Bets: Splitting the Stack](https://www.google.com/goto?url=CAESfgHEIkXXK5hJYwwAlSxXrwlC1Vxpmal4soOSzdlfXPi-zp2bl69DXp4sljuJ1RHG5cQTi8SJeP_EauC3uFgf0PROrc9A4zYmMuYyh2YfH_MUhzu1qSmMOM_r3MFfI7HOjak7ZpA3UR1wcV3j6ZVUt0Nhi1ryLN23W29uqw1W4Q&gsessionid=TslekhiqpJ2lLjgdoKkvkj2spZnC-JJVT88UQiTFIC4wjd6umg2ImQ)  
  <sub>ETF Database, 33 minutes ago</sub>  
  Over the past month, markets have pulled the AI trade apart layer by layer, fracturing performance across ETFs and subsectors.
- [Best ETFs for a Divided DC](https://www.google.com/goto?url=CAESgAEBxCJF19z0tFhUnrScLLNRTs22MWCvdyPTzmXrXxjzAGqRekSXaTe0HBTpxCv9Amljr0t7rkrLOcgZy-wNHKo-a5PuVcXDj6410TWqLihdv8f6FKRUmJ7ePl0FHLlHoV0DWiZqdg-nimmxr7BOXwOsQJLMScFUbr4YTqoUbacjFQ&gsessionid=TslekhiqpJ2lLjgdoKkvkj2spZnC-JJVT88UQiTFIC4wjd6umg2ImQ)  
  <sub>Kiplinger, 1 hour ago</sub>  
  The next two years will see a Democratic Congress clash with a Republican president. That could be a surprisingly productive environment for these ETFs.
- [Tudor adds Iridium, exits Teck, boosts SPY stakes among Q3 trades (IRDM:NASDAQ)](https://www.google.com/goto?url=CAESogEBxCJF168QNjsKUKlPOi9YP6X8XzkDUD3FCHR3DlmLY7giMSZmbwNYQLp19fXsCYlyNslfQT7sL2Cm0W_icVfsIuJkWUjC-dQFoPJBNnGBMFC8OZdiXc8h_tvBGFvHLQIcHwYjFYVfjS2KtWBIyQC2iXhK8t4KPGlfg6CNtxcfFhJZTCsFTj8CwbG7vyI50oFD1uWhs5yZGI9vBqkipOHBXY8&gsessionid=TslekhiqpJ2lLjgdoKkvkj2spZnC-JJVT88UQiTFIC4wjd6umg2ImQ)  
  <sub>Seeking Alpha, 15 hours ago</sub>  
  Paul Tudor Jones' Tudor investment's 13F shows a new 3.95M-share Iridium Communications stake worth $189.3M, SPY up to 1.51M shares and IVV down to 322.8K.
- [Paul Tudor Jones's Top Q3 2026 Move: iShares Core S&P 500 ETF at a -1.37% Portfolio Impact](https://www.google.com/goto?url=CAESuAEBxCJF10WZtqlmPTkarcXUExdcb-21fDabBmLhvHeS4YT-Z8KSMwXfZBKXGw3cfNTCvErTYguINIOCVk2AK1VreK6CwBJaBlXUkeN8UHv9Ky0e_WNk1txYtRXvKg75Yqzt9gba5_-c8Gnri6MQRTCUHZpTFsAgq6oLWsnKnMnGEU3c05_Fhd2KsTz3gDB85tO6kJ0QzMaLWuxEDaNuoxnUljdIa_HFPh65cV97On5eyi0x1bGZTohs&gsessionid=TslekhiqpJ2lLjgdoKkvkj2spZnC-JJVT88UQiTFIC4wjd6umg2ImQ)  
  <sub>GuruFocus, 14 hours ago</sub>  
  A Deep Dive Into Tudor Investment's Latest 13F Filing, Including New Buys, Key Increases and Major ExitsPaul Tudor Jones (Trades, Portfolio) recently...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 43.87 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 43.31 (+1.3%), 50d 41.92 (+4.6%), 200d 44.34 (-1.1%); 50d below 200d
Momentum: RSI(14) 62.1 | MACD 0.565 vs signal 0.546 (histogram 0.020)
Returns: 1d -0.6% | 5d +0.3% | 1m +6.1% | 3m -0.3%
52-week range: 39.25 - 47.73 (now 54.5% of the way up)
Volatility: ATR(14) 0.57 (1.3% of price) | annualised 20d 12.8%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Utilities
What it holds: P/E 17.87 | P/B 2.03 | P/S 2.51 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +17.3% a year | beta to the market 0.34
Cost and size: expense ratio 0.08% | net assets 24.25B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: NextEra Energy Inc 12.8%, Southern Co 7.9%, Duke Energy Corp 7.3%, Constellation Energy Corp 6.3%, American Electric Power Co Inc 5.2%
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
Ratings by weight: buy 80.0% | hold 20.0% | sell 0.0% (mean 2.03 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.5% above the current prices
Holdings read: NEE, SO, DUK, CEG, AEP
Recent rating changes among them:
  - NEE: 2026-10-23 Barclays: main, Equal-Weight -> Equal-Weight
  - SO: 2026-10-22 HSBC: init, ? -> Buy
  - DUK: 2026-10-22 HSBC: init, ? -> Hold
  - CEG: 2026-10-30 Morgan Stanley: main, Overweight -> Overweight
  - AEP: 2026-11-02 Barclays: main, Equal-Weight -> Equal-Weight
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
Shares outstanding: 163.27M | fund size: 7.16B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance Singapore, 23 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) · 0.27% · 6.86% · 30.14% · 21.99% · 24.38% · 41.41% · 661.07%. Key events. Baseline. Advanced chart.
- [PJP: Healthcare Sector Dashboard For November](https://seekingalpha.com/article/4968784-pjp-healthcare-sector-dashboard-for-november)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Analyst sees Invesco Pharmaceuticals ETF as a long-term or tactical option; it beat XLV in the past year but lagged from July 2015 to July 2025.
- [Defensives Lead Sectors Monday As Growth Trails](https://www.google.com/goto?url=CAESpQEBxCJF15TiSV4foiWTvauWe8P2P8ZW8Y1h-epxbmiC2TN57clF9_6apMMqc8Mvnd-aGwrCUfYlbSt5q4OJcZf6eMG9BpejnsuUfCaX7vRwJUQqhdO73Fp_gloBbMUeYo4WRcf9xknBGgNnpitgImBgBx0S4wIU25sHiainHvmOP5XxN0wylrEiQbP2DM3hfcwraGc2jJgOgizS3IGCpDhTvvXy4_Q&gsessionid=0-KOdZzzoL2yzMesTPRIvDNOQJToFcqDo2UIWaOxXm6xnnuhhn83Yg)  
  <sub>Benzinga, 23 hours ago</sub>  
  Four sectors are higher and seven are lower in Monday's regular session, with defensive sectors holding the top three positions. The leaders are clustered...
- [Healthcare equipment undervalued; pharma/biotec...](https://www.google.com/goto?url=CAEShAEBxCJF1_Yb0PAiYIsZd1UreFheLeHAzjI9t1wFsILdb0RXgs_VUsnugVRCpDA4YSgNhuXv-be6tMIf37hDmElLmUux_o5vmQCw6-3d0Jidb7KYEVpBYLFFzijci7GuhpY5eKXVRE9o2QccUADb_9berV3L29B039oiL41RzJiG2NId-4Y&gsessionid=0-KOdZzzoL2yzMesTPRIvDNOQJToFcqDo2UIWaOxXm6xnnuhhn83Yg)  
  <sub>Pluang, 1 hour ago</sub>  
  The healthcare equipment sector is currently undervalued compared to historical averages, while the pharmaceutical and biotechnology sectors are...
- [Top-Ranked ETFs That Are Worth Adding to Your Investment Radar](https://www.google.com/goto?url=CAESmgEBxCJF142gTMqT_tTywfk36Sq-V3tf2oZuh0IEjhQ9LdLXZEyyjyYwR8F0sn4-moyd_ZGSeD25LVUao7rgfx1VLLrIQkUnmMC6ttDg3RJ-6n_dShgCF69KxFfXd9JP2LnoJ0CyaEkwEGv2ibAxvI4bXfCnAuBzWGhTaS_2rvjLPPm94y7qD1lUclk3pZ9nVQ_uYS3aMEeJ8jLj&gsessionid=0-KOdZzzoL2yzMesTPRIvDNOQJToFcqDo2UIWaOxXm6xnnuhhn83Yg)  
  <sub>Yahoo Finance, 24 hours ago</sub>  
  Market uncertainty is rising, but investment opportunities remain. Explore these top-ranked ETFs across healthcare, dividends, value and GARP.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 186.49 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 184.59 (+1.0%), 50d 175.76 (+6.1%), 200d 160.52 (+16.2%); 50d above 200d
Momentum: RSI(14) 59.7 | MACD 3.617 vs signal 3.859 (histogram -0.242)
Returns: 1d -0.7% | 5d -1.3% | 1m +6.2% | 3m +6.2%
52-week range: 142.84 - 189.66 (now 93.2% of the way up)
Volatility: ATR(14) 3.29 (1.8% of price) | annualised 20d 19.8%
Volume: 0.13x the 20-day average
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
Three-year record: +16.0% a year | beta to the market 0.41
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
Weighted price target: +6.5% above the current prices
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
Share count change: 1 week: -2.1% (-1.02B) over 10d | 1 month: +1.7% (811.12M) over 32d
Shares outstanding: 260.08M | fund size: 48.50B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Your $300,000 in XLY Holds $125,585 in Amazon and Tesla Alone](https://247wallst.com/investing/etf/2026/11/16/your-300000-in-xly-holds-125585-in-amazon-and-tesla-alone/)  
  <sub>24/7 Wall St., 16 hours ago</sub>  
  A fund named for everyday American spending looks diversified until you open its holdings filing. Two familiar companies quietly steer the whole ride,...
- [ETF XLY holds 42% of assets in Amazon and Tesla, concentrating $125K of a $300K portfolio in two stocks.](https://pluang.com/en/news-feed/xly-etf-memegang-125585-di-amazon-dan-tesla-risiko-konsentrasi)  
  <sub>Pluang, 15 hours ago</sub>  
  The State Street Consumer Discretionary Select Sector SPDR ETF (XLY) holds 41.86% of its assets in just two companies: Amazon (22.22%) and Tesla (19.64%),...
- [Forget Nvidia — S&P 500's 8,900 Target Puts These ETFs in Play - State Street SPDR S&P 500 ETF Trust (ARC](https://www.google.com/goto?url=CAESugEBxCJF18Qa86bn8EG9AWrMtAAPxFgR8KZOy4U3ZiDxO8yBzXJUmXy_NkWp2qSoYsqcX9YiG_02jmnzY8Gqm-rBFQmZvS3BFHkmOWuDT7PrUGICIdcUr5rIEZ2qESZvsJ8NLXysiNNLAhjtEJV66hSlGQUia0LwgcSTODqS1Zpk7xlq1aQK7OXAijeEAz7QWYeYjttxD9jhvdznpYOigq1V8V_q71ONP7b2DzPjoktivNRFLrj1n7gSeVw&gsessionid=V_pPBDj6CPqOiNwMIAVn6iCS6BpvQ8kTnxCCzyLQBLx__Yr5eH_ATA)  
  <sub>Benzinga, 22 hours ago</sub>  
  Wall Street sees the S&P 500 climbing to 8900. Discover which sector ETFs could benefit as investors look beyond Big Tech and the AI trade.
- [ValuEngine Weekly Market Commentary With Strategy Notes](https://www.google.com/goto?url=CAESnQEBxCJF10Y5URZyLmZl2MPey2La6j2KgHAyJkMdlwCQUE-Bl7UHb7NoSR2jHQqrAVNVGBaaM5DK03sjc48tpio64TtDkwjbVngKJvNwrKdjp3f2xD9JkWMsYjrjF7x-qJDuS2iyCy-VMbxoz1XNpL-ODRmotDXlr-Af2TDjtS086SqYzfw0ihTEJrVe6Y5ybujIODSVhGftFiiGIP8W&gsessionid=V_pPBDj6CPqOiNwMIAVn6iCS6BpvQ8kTnxCCzyLQBLx__Yr5eH_ATA)  
  <sub>Seeking Alpha, 46 minutes ago</sub>  
  Despite a choppy finish on Thursday-Friday, US equities snapped a multi-week losing streak to post their first weekly gain since early Oct. All 11 Select...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 118.41 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 117.67 (+0.6%), 50d 113.98 (+3.9%), 200d 115.41 (+2.6%); 50d below 200d
Momentum: RSI(14) 54.3 | MACD 1.615 vs signal 1.711 (histogram -0.096)
Returns: 1d +0.2% | 5d -2.2% | 1m +3.5% | 3m -0.2%
52-week range: 105.66 - 124.52 (now 67.6% of the way up)
Volatility: ATR(14) 2.15 (1.8% of price) | annualised 20d 27.3%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 24.15 | P/B 5.62 | P/S 2.30 | 3y earnings growth n/a
Yield: 0.8%
Three-year record: +14.9% a year | beta to the market 1.10
Cost and size: expense ratio 0.08% | net assets 22.40B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Amazon.com Inc 21.3%, Tesla Inc 18.8%, The Home Depot Inc 5.5%, McDonald's Corp 4.5%, TJX Companies Inc 4.1%
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
Rolled up from the 5 largest holdings, 54.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.7% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, TJX
Recent rating changes among them:
  - AMZN: 2026-11-03 Freedom Broker: main, Buy -> Buy
  - TSLA: 2026-11-05 GLJ Research: reit, Sell -> Sell
  - HD: 2026-11-10 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-11-06 Argus Research: main, Buy -> Buy
  - TJX: 2026-11-10 UBS: main, Buy -> Buy
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
Share count change: 1 week: -1.9% (-434.61M) over 10d | 1 month: -1.4% (-315.06M) over 32d
Shares outstanding: 186.70M | fund size: 22.11B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Sugar (CANE) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 11.02 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 11.37 (-3.1%), 50d 11.58 (-4.9%), 200d 10.31 (+6.8%); 50d above 200d
Momentum: RSI(14) 40.1 | MACD -0.211 vs signal -0.172 (histogram -0.039)
Returns: 1d +0.8% | 5d +0.7% | 1m -10.0% | 3m -2.0%
52-week range: 9.02 - 12.47 (now 58.0% of the way up)
Volatility: ATR(14) 0.20 (1.8% of price) | annualised 20d 28.0%
Volume: 0.02x the 20-day average
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
Cost of holding this fund instead of sugar itself: -6.6% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -2.0%, commodity +4.4%, gap -6.3% | 6 months: fund +9.1%, commodity +22.1%, gap -12.9% | 12 months: fund +15.9%, commodity +22.5%, gap -6.6%
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
Share count change: 1 week: -1.0% (-579.51K) over 7d | 1 month: +22.6% (10.74M) over 31d
Shares outstanding: 5.29M | fund size: 58.27M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Corn Extending Gains to Tuesday Morning](https://www.barchart.com/story/news/8874524/corn-extending-gains-to-tuesday-morning)  
  <sub>2 hours ago</sub>  
  Corn is trading with spillover support from wheat, as contracts are up 1 to 3 cents. Futures posted fractional to 3 ¼ cent gains on Monday, with futures...
- [Corn, Beans & Wheat at a Crossroads: Where to Trade and Where to Hedge](https://www.barchart.com/story/news/8862080/corn-beans-wheat-at-a-crossroads-where-to-trade-and-where-to-hedge)  
  <sub>18 hours ago</sub>  
  A review of 7-, 14-, and 21-day exponential moving averages shows momentum beginning to diverge across corn, soybean, and wheat futures.
- [Will Jensen Huang’s Chinese Spy Scandal Hurt Corn, Soybean and Wheat Prices?](https://www.google.com/goto?url=CAESsgEBxCJF1_h9Ftqb6mx8Bn0ZZSj85BL9V5Rs-rhX5IHd0A6CF4fUVPF7H1emYz19xOLjJSFNfhoQFlk0KCp0-AsMc-fRqVZ0H8O8IayEBuYLgMWSa9NuKsG3dSSx3kWaAx6bB72d1Dkf2WgUgxqaIOk_JUsEES9v5KIMAZBdd_rTGhhrDdCOAy4mLEigqeNxTx5_MCFt38iMNupaLDhDXD5UzaPxK5YpJHWI6Ip6OwEkeCSf&gsessionid=Gqoep9XKxEAFmPzPGofuoe-jxfz-4vY7YbNVGUE1_Z6q9bvG0w9owA)  
  <sub>19 hours ago</sub>  
  Some traders are worried the Nvidia CEO-alleged Chinese spy affair scandal could cause this week's negotiations to derail around trade of semiconductors...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 17.33 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 17.38 (-0.3%), 50d 18.49 (-6.3%), 200d 18.18 (-4.6%); 50d above 200d
Momentum: RSI(14) 39.7 | MACD -0.330 vs signal -0.391 (histogram 0.060)
Returns: 1d +0.8% | 5d -0.1% | 1m -3.7% | 3m -7.6%
52-week range: 16.47 - 20.29 (now 22.6% of the way up)
Volatility: ATR(14) 0.23 (1.3% of price) | annualised 20d 12.9%
Volume: 0.30x the 20-day average
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
Cost of holding this fund instead of corn itself: -8.2% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -7.6%, commodity -4.5%, gap -3.1% | 6 months: fund -7.5%, commodity -4.9%, gap -2.6% | 12 months: fund -3.2%, commodity +5.0%, gap -8.2%
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
Share count change: 1 week: +0.2% (244.30K) over 7d | 1 month: -11.6% (-14.22M) over 31d
Shares outstanding: 6.25M | fund size: 108.27M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [The best copper stocks to buy and hold for decades](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc6b3259b94ea1a2a059079b72eb4b&url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fthe-best-copper-stocks-to-buy-and-hold-for-decades%2far-AA2hybbn&c=9580546677153570607&mkt=en-us)  
  <sub>The Motley Fool on MSN, 30h ago</sub>  
  Copper benefits from the electrification-of-everything megatrend on the demand side and from ongoing constraints on the supply side.
- [Monday’s Charts – Technicals Deteriorate as the Nasdaq Tests Its Uptrend Line](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc6b3259b94ea1a2a059079b72eb4b&url=https%3a%2f%2fpro.thestreet.com%2fmarket-commentary%2fmondays-charts-technicals-deteriorate-as-the-nasdaq-tests-its-uptrend-line&c=12817011125701219932&mkt=en-us)  
  <sub>TheStreet Pro, 24h ago</sub>  
  The Nasdaq Composite and Russell 2000 closed on uptrend lines, while the VIX jumps and gold, copper, and bitcoin fall again.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 36.09 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 38.34 (-5.9%), 50d 39.25 (-8.0%), 200d 37.97 (-5.0%); 50d above 200d
Momentum: RSI(14) 31.6 | MACD -0.843 vs signal -0.580 (histogram -0.263)
Returns: 1d +0.2% | 5d -4.4% | 1m -8.8% | 3m -8.4%
52-week range: 30.77 - 41.43 (now 49.9% of the way up)
Volatility: ATR(14) 0.64 (1.8% of price) | annualised 20d 24.8%
Volume: 0.11x the 20-day average
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
Cost of holding this fund instead of copper itself: -3.4% a year -- a steady drag
Measured: 3 months: fund -8.4%, commodity -7.7%, gap -0.7% | 6 months: fund -4.1%, commodity -2.9%, gap -1.2% | 12 months: fund +15.2%, commodity +18.6%, gap -3.4%
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
Share count change: 1 week: +2.4% (15.55M) over 7d | 1 month: +1.5% (9.82M) over 31d
Shares outstanding: 18.09M | fund size: 652.98M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Institutional Flow in SPDR Gold Shares (GLD): 77% of the Options Money Is in Puts](https://www.moomoo.com/community/feed/institutional-flow-in-spdr-gold-shares-gld-77-of-the-117630781882373)  
  <sub>Moomoo, 7 hours ago</sub>  
  SPDR Gold ETF (GLD.US)$ : Runner-up: $1.2M on 360 put contracts expiring Nov 16. $GLD: $214.4M in options premium, with $48.3M on calls and $166.2M o...
- [Weekly ETF flows: seven of 11 sectors record outflows; technology leads inflows](https://www.tradingview.com/news/seekingalpha:c04723886094b:0-weekly-etf-flows-seven-of-11-sectors-record-outflows-technology-leads-inflows/)  
  <sub>TradingView, 1 hour ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 Trust AMEX:SPY, saw inflows of $320.13M for the week ending November 13, while its price increased by...
- [SPDR Gold Shares (GLD) Institutional Flow at the Close, Monday Nov. 16: 77% of the Options Money in Puts](https://www.google.com/goto?url=CAESrgEBxCJF16BRR6ap2C6EQGOSGlOal3Q_W51iTA_7Ws15iSSW_Zox5qaaFb_2UW7QxSFsCKt2ep3gER2cOqAqQE8rPr32KinxrSorh0anSL5zx9htP9qHoWo-LWH4ShcNvn-HX97XfpIGqLEyI99_rILZBszDPhhOJFHdPAt5QRRQYpOkUtWvuHjj7KdaSkOcdgLDt5UGl-kQwPQ3mBhhMGQ_PgGgUNp5tmCEYPdxXaw&gsessionid=3bTLxCgabEIBd4GhPwX9AVogkBMxzaULa9TXyl8-7Jqs6I9iD0mUaw)  
  <sub>Moomoo, 11 hours ago</sub>  
  SPDR Gold ETF (GLD.US)$ drew $214.4M in options premium: calls $48.3M, puts $166.2M (77% puts). The biggest single trade: $3.4M on 7917 call contrac...
- [Real-Time Stock News, SEC Filings & Alerts](https://www.google.com/goto?url=CAESXAHEIkXX06kgB_TMk95S6EtcgDFEhIfx5WBLYomAF1_HChPI-8Ab55W4jXL8KK5pRVq59mAISqjo-mxCNKtICyPS-AzHDkPeEhEqCDk_Pg91wVQD7MwhcJoov3Xh&gsessionid=3bTLxCgabEIBd4GhPwX9AVogkBMxzaULa9TXyl8-7Jqs6I9iD0mUaw)  
  <sub>Quantisnow, 22 hours ago</sub>  
  Browse US-listed exchange-traded funds A to Z, with latest price, daily change and one-year return. ETFs are funds, not companies.
- [Gold and silver settle at new 52-week lows as U.S. rate hike bets boost dollar (GLD:NYSEARCA)](https://www.google.com/goto?url=CAESrwEBxCJF15ZY7Zn-hS22XQk_utjwJ5mz96g8aussbqXUQaIQ_HkruhJxoA1rdJrRa9dIQU6P6-m66MEHFqEeFf0Q759FSKd_Ps6IQpyQELkKurPn6DGWl9NxlKpZzxbaJxex6tRnfQfX4L2aZFfZG1kwxuWnuPcnoPiZdXp4KxWYiKofYS_fyZDxqUWamwwsojLgB299vii4YWg2qutWxu5oaTNUHL_803Ktiu-0J_Me&gsessionid=3bTLxCgabEIBd4GhPwX9AVogkBMxzaULa9TXyl8-7Jqs6I9iD0mUaw)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  Gold and silver fell to their lowest levels in more than a year as the dollar traded near its highest since April 2025 amid rising expectations of prolonged...
- [GLD NTA 16-11-2026 $3.70205](https://www.google.com/goto?url=CAESgwEBxCJF15kRiMjfTz-pritTUGu1YWtbZBXBU7aw_s-qHqhi-K_LGjS0BSV6soSgHUpfIfu7eP4EWVzIf1qB_8b9cQYjN7tzSQcqvCeGFbMXEGn9g0Pz7dqxATc6Cc9uHCNr5sLESzOGSbQDmQJrWCHn6JuQ-bQcZIN2zEfB3FvyEnszrg&gsessionid=3bTLxCgabEIBd4GhPwX9AVogkBMxzaULa9TXyl8-7Jqs6I9iD0mUaw)  
  <sub>BusinessDesk, 17 hours ago</sub>  
  View the full NZX announcement for Smart Gold ETF (GLD): GLD NTA 16-11-2026 $3.70205. Financial updates and company disclosures on BusinessDesk.
- [Why Central Bank Buying Is Keeping Gold Afloat As More Fed Hikes Are Expected](https://www.google.com/goto?url=CAESxwEBxCJF1wizKzKJp7LjKMowATXI271F0xoAnHz6eQ6xvD_GGCrXUQgbNxqV99wHfBkeqC6jLX8bzg2SrWOUnD3BWo9Emi9NN2P27FGn-wYhGk5OAVldvmqyvckMzWGqGZJDV4BLkc3SFev62c4d9I6XKaNKwfkxKDGJ-d0x87HWKIlPLBhREEHvmUqrLXALjfwiOu9OkCL3BdSAbRYiMYl17QC1N45yn2COiKXnukAy7Qmd3riuP81pebcyWgTBTbXrhJgXbEuk&gsessionid=3bTLxCgabEIBd4GhPwX9AVogkBMxzaULa9TXyl8-7Jqs6I9iD0mUaw)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  The bull case for gold: central-bank buying, inflation and federal debt support a 10% allocation, while speculative positioning leaves room for a shakeout.
- [GLD Dec 2026 358.000 call (GLD261211C00358000) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXDJto5mHDUOCnpfbRl6eKWT39mJJJKzdSJ7qpi3vTTs7S0qZTPq2qX_Q_S-JMEp660wo0aU32_nJJ-sld4mntytG9FYrY0aeuLeQCO3J4c1x9TYhWZlMbaRbeScktT1ezKe4eK0AO923zhj4GbvNitEntXv4&gsessionid=3bTLxCgabEIBd4GhPwX9AVogkBMxzaULa9TXyl8-7Jqs6I9iD0mUaw)  
  <sub>Yahoo Finance UK, 4 hours ago</sub>  
  Interactive chart for GLD Dec 2026 358.000 call (GLD261211C00358000) – analyse all of the data with a huge range of indicators.
- [Harvard, Dartmouth keep Bitcoin ETF stakes steady as fund gains 42% in Q3](https://www.google.com/goto?url=CAESagHEIkXXNnpg9nwzidteHjTs1g5dfpCJ0MfTWvo0wwn2b01LbVoTTmMCwEs5yW0PMwjaZmn1WkmCBHM2GlCoqC0Nu5myEq6-xCFTM66ZirpyJD3Y-E6oKOt1qFeok1tlnqbpZPPJIEA17fE&gsessionid=3bTLxCgabEIBd4GhPwX9AVogkBMxzaULa9TXyl8-7Jqs6I9iD0mUaw)  
  <sub>Cryptonews.net, 22 hours ago</sub>  
  Harvard University and Dartmouth College reported unchanged share counts in BlackRock's spot Bitcoin exchange-traded fund (ETF) at the end of the third...
- [Harvard and Dartmouth Keep Bitcoin ETF Share Counts Steady as Q3 Values Rise](https://www.google.com/goto?url=CAESxAEBxCJF167yZqc2s_LS5vZf2yoY810v5hPmm2o4yNJmYZhZ4eRKStWwmJK4gY5DB7QJk3GPSt0JThGfYvFWemYBwNtrnxuTv6jixhVBBUl_Iu8eOIUFevI5ntybipdlJAmHukyKBcU_lgW1_24phk1saelgKGoonQC5dySQBmZWLyOBzvAfeoij2eJKOzOi35V24jImkoB2N8i8uV0IXD_wtA43w_-GGSNCuROPq2nZ9F5A5KoFcdcrLURBcMGW9UDfNZ7L&gsessionid=3bTLxCgabEIBd4GhPwX9AVogkBMxzaULa9TXyl8-7Jqs6I9iD0mUaw)  
  <sub>TradingView, 14 hours ago</sub>  
  Harvard sharply increased its reported GLD share count, while Dartmouth also retained Ether and Solana fund positions.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 353.93 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 366.26 (-3.4%), 50d 378.91 (-6.6%), 200d 407.59 (-13.2%); 50d below 200d
Momentum: RSI(14) 37.5 | MACD -6.276 vs signal -5.205 (histogram -1.071)
Returns: 1d +0.3% | 5d -4.2% | 1m -6.8% | 3m -14.5%
52-week range: 352.93 - 495.90 (now 0.7% of the way up)
Volatility: ATR(14) 6.41 (1.8% of price) | annualised 20d 28.1%
Volume: 0.19x the 20-day average
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
Measured: 3 months: fund -14.5%, commodity -14.8%, gap +0.4% | 6 months: fund -14.0%, commodity -14.2%, gap +0.2% | 12 months: fund -5.9%, commodity -5.5%, gap -0.4%
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 260.30M | fund size: 92.13B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Weekly ETF flows: seven of 11 sectors record outflows; technology leads inflows](https://www.tradingview.com/news/seekingalpha:c04723886094b:0-weekly-etf-flows-seven-of-11-sectors-record-outflows-technology-leads-inflows/)  
  <sub>1 hour ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 Trust AMEX:SPY, saw inflows of $320.13M for the week ending November 13, while its price increased by...
- [Current price of silver as of Tuesday, Nov. 17, 2026](https://fortune.com/article/current-price-of-silver-11-17-2026/)  
  <sub>1 hour ago</sub>  
  If you're worried about increased inflation, adding precious metals like silver to your portfolio can be a smart choice.
- [Squeezing Blood (or Income) From Stones](https://www.google.com/goto?url=CAEShQEBxCJF13SwHI0AAQnkb4xFqXdqaRgwxpSc5yvNwgtknaJK8qp0PHMGafN2qH_Pwktipj7pgpd80z5N_k3UiGw5z3032dp24VxQzxf3tNdXjgJMZSytOAl73d1mD8kn1h28qX-x6Qrp9e6qKwocT1Ax2ipCeijDhgodDLxc2TJz9DHSrVyy&gsessionid=wP-2eR2R0iBCLE2oQbfXHkLhUVvUfQdLtD7s0HJH_k5FT9eR933vpA)  
  <sub>19 hours ago</sub>  
  Historically, investors have reached for gold and silver as go-to “safe haven” assets to hedge inflation or macroeconomic volatility.
- [Discovery Mining Ltd. (DSV.TO) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZwHEIkXX4O7jfG9lNMD9o1rHQOq_kNfySCfHh0djvkenwYJdc7O50FJHa_p6_0ReUc5_dqRcCMb_OCY82aZ47rk41VkmlIbC8ZixYoz7wKJcT6fF0m9PhNagEJml6Svi-qgJG6l6HO8&gsessionid=wP-2eR2R0iBCLE2oQbfXHkLhUVvUfQdLtD7s0HJH_k5FT9eR933vpA)  
  <sub>16 hours ago</sub>  
  Find the latest Discovery Mining Ltd. (DSV.TO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Gold and silver settle at new 52-week lows as U.S. rate hike bets boost dollar (GLD:NYSEARCA)](https://www.google.com/goto?url=CAESrwEBxCJF18dJDUHmHUxq-x-fVfNlUjl1WTUnKsS3UVbTJ0uh39ni9jYXb3ltta76ZAQz3THfEttPOeAhD64bUnc_sAIgMXH-sUxzdOCG1xQtnInpnyoBppHtCHw8NasMK3-Eeg8MMK-MXHH4yCHhMsgsrEZYyDzH9A6SCsSC5BrM9FajBW3kLdMIqQkkZaXJV8EfcsFTXmr7va5nSHwThdUlMxCjxoT5bHqYfpa90al_&gsessionid=wP-2eR2R0iBCLE2oQbfXHkLhUVvUfQdLtD7s0HJH_k5FT9eR933vpA)  
  <sub>16 hours ago</sub>  
  Gold and silver fell to their lowest levels in more than a year as the dollar traded near its highest since April 2025 amid rising expectations of prolonged...
- [Silver Price Forecast: Bearish potential appears intact despite XAG/USD rebound above $47.00](https://www.google.com/goto?url=CAES0wEBxCJF18pUR0_ihzePN0RIwScAEY6JnZQIE_MVqd1PnEB2hGSiIuKRXeMooaI1q1rXJJkR8AVWh8pbyV0x2rv7nb5fD7pi_2vJh8qeKgv_3kKmyCjftoXzpSnwzGu6E1fNmM9Krpn7PkYV3DQ7Au2r0msw6DRvLkj1fAouZ3nC0_nGahS0-OMAhb_TJ1kX1lxhXxXIqKwznFzN9l7KeY0kydsUnTlZoSwNTi8LniCtj5ehrsXHD_lF0BFGqHa8ev4IyF6jcMsb4E2jaHY4uRhia8bU&gsessionid=wP-2eR2R0iBCLE2oQbfXHkLhUVvUfQdLtD7s0HJH_k5FT9eR933vpA)  
  <sub>12 hours ago</sub>  
  Silver (XAG/USD) finds modest support in Tuesday's Asian session, breaking a three-day losing streak after hitting its lowest level since October 2025 the...
- [Silver Bullion Trust ETF Non-Currency Hedged Units (SBT-B.TO) Seasonal returns chart](https://www.google.com/goto?url=CAESdQHEIkXXNx7jc9rrN-SOVIM5Fw1FEN4JsTyry1zNj5muxg7zh6OwXLOnomPHLkbrC-QaZT7TkudeSN_MAfuTt1LBPBILChxAVUoFB3vr8rZFa7rBDQsD937PMau7WYgnoDaAHthnRu7fpYlzw8diUHFepSsPPA&gsessionid=wP-2eR2R0iBCLE2oQbfXHkLhUVvUfQdLtD7s0HJH_k5FT9eR933vpA)  
  <sub>23 hours ago</sub>  
  Silver Bullion Trust ETF Non-Currency Hedged Units (SBT-B.TO) seasonal returns chart provides the mean and median returns by month to inform your investment...
- [Lumina Metals Joins the Silver Institute and Its Shares Are Added to the Nasdaq Junior Silver Miners Index](https://www.google.com/goto?url=CAES5wEBxCJF1_9mNnMAxF3NV0gVSpCvIydEChARBDvqs_pjYQZgcK9kAjDA_1-0Pnp5WPxutKFXPhgKyil4pApijCT4lWCZsYZiMwUmGmt_uyeD5jruWK8nZcWCloZWQtm56bTETHD3ZjxaM3HxxUxiQdnsyIiMsDo0nJyqzIYCtUoxd8RDoOy7YmugJA6sOntHonKdPSXOLegHFuttWuWgRMoew7fDlmRMfmfVog-_bSdVlvfQCIxPlDAEvQCFNQZHlg_w9Wg_L4Sq_wFIemywLLqKI29IzDDJQu34kB-f8_Dwf9h07iIp5cY&gsessionid=wP-2eR2R0iBCLE2oQbfXHkLhUVvUfQdLtD7s0HJH_k5FT9eR933vpA)  
  <sub>18 hours ago</sub>  
  LMCU (WSE: LMCU) ("Lumina" or the "Company") is pleased to announce it has joined The Silver Institute, an international association representing companies...
- [Dr. Copper’s New Diagnosis: AI & Power Grid Demand](https://www.google.com/goto?url=CAESnwEBxCJF14_Juv9Eo-eJpxrj_7EUhJ6-JjozCKlbv-h52eZvlDJTqWvi5naxpzEWVzvoEMI776inOKFMbWSR2lJD9y9IQ-lXUiyW-1UDPLyJRuSTkLmAvaT7wD-J_NG3RcAmV1UIfBG41o6Oa76Q8Q7A1IWR1znS_s-RDCfg0JrbYxUkwxgdGWTPjVXuVzaP8rzy9dclnmzpkrH2TGA7HbY&gsessionid=wP-2eR2R0iBCLE2oQbfXHkLhUVvUfQdLtD7s0HJH_k5FT9eR933vpA)  
  <sub>24 hours ago</sub>  
  Copper has historically been a material used for traditional infrastructure, but now is necessary for AI, electrification, and clean energy.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 43.08 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 46.82 (-8.0%), 50d 52.20 (-17.5%), 200d 61.61 (-30.1%); 50d below 200d
Momentum: RSI(14) 32.0 | MACD -2.360 vs signal -2.223 (histogram -0.137)
Returns: 1d +1.6% | 5d -7.3% | 1m -16.4% | 3m -28.2%
52-week range: 42.39 - 105.60 (now 1.1% of the way up)
Volatility: ATR(14) 1.52 (3.5% of price) | annualised 20d 44.6%
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
Cost of holding this fund instead of silver itself: -0.4% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund -28.2%, commodity -27.5%, gap -0.7% | 6 months: fund -35.6%, commodity -36.3%, gap +0.7% | 12 months: fund -6.3%, commodity -5.8%, gap -0.4%
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
Direction: money coming in (1 month)
Share count change: 1 week: +5.6% (1.26B) over 10d | 1 month: +1.2% (284.57M) over 32d
Shares outstanding: 557.72M | fund size: 24.03B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Dividend SOYB - Jadwal & Riwayat Dividen Saham](https://ajaib.co.id/saham-amerika/aset/SOYB/corporate-actions/dividend)  
  <sub>11 hours ago</sub>  
  ETF komoditas yang memberikan eksposur terhadap harga kedelai melalui investasi pada kontrak berjangka kedelai. SummaryCorp.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 25.99 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 25.97 (+0.1%), 50d 26.91 (-3.4%), 200d 25.32 (+2.7%); 50d above 200d
Momentum: RSI(14) 46.1 | MACD -0.296 vs signal -0.360 (histogram 0.064)
Returns: 1d +0.9% | 5d +0.3% | 1m -2.9% | 3m -0.6%
52-week range: 21.71 - 28.14 (now 66.6% of the way up)
Volatility: ATR(14) 0.29 (1.1% of price) | annualised 20d 15.0%
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
Cost of holding this fund instead of soybeans itself: 0.1% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund -0.6%, commodity +1.2%, gap -1.8% | 6 months: fund +2.8%, commodity +2.2%, gap +0.6% | 12 months: fund +11.3%, commodity +11.1%, gap +0.1%
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
Share count change: 1 week: -2.3% (-928.93K) over 7d | 1 month: -9.4% (-4.06M) over 31d
Shares outstanding: 1.51M | fund size: 39.29M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 9.78 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 9.67 (+1.2%), 50d 10.26 (-4.7%), 200d 10.97 (-10.8%); 50d below 200d
Momentum: RSI(14) 46.7 | MACD -0.071 vs signal -0.152 (histogram 0.082)
Returns: 1d -0.4% | 5d -6.1% | 1m -6.5% | 3m -2.3%
52-week range: 9.00 - 16.90 (now 9.9% of the way up)
Volatility: ATR(14) 0.37 (3.7% of price) | annualised 20d 45.5%
Volume: 0.05x the 20-day average
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
Cost of holding this fund instead of natural gas itself: -0.2% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund -2.3%, commodity +9.3%, gap -11.6% | 6 months: fund -17.8%, commodity -1.2%, gap -16.6% | 12 months: fund -32.8%, commodity -32.6%, gap -0.2%
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
Direction: money coming in (1 month)
Share count change: 1 week: -8.3% (-44.29M) over 10d | 1 month: +22.7% (90.14M) over 32d
Shares outstanding: 49.78M | fund size: 486.82M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected) (Bing's feed, direct: 10 headline(s), none naming UNG)

### Oil (USO) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [United States Oil Fund, LP (USO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/USO/)  
  <sub>24 hours ago</sub>  
  Find the latest United States Oil Fund, LP (USO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Real-Time Stock News, SEC Filings & Alerts](https://www.quantisnow.com/etfs)  
  <sub>22 hours ago</sub>  
  Browse US-listed exchange-traded funds A to Z, with latest price, daily change and one-year return. ETFs are funds, not companies.
- [Oil prices sink amid rising expectations of global supply surplus (USO:NYSEARCA)](https://www.google.com/goto?url=CAESpAEBxCJF13l-7j-SDsMSzWTT79CJKsRiHlAdHESuaY_dQoOXHWi8EcGXTthaLCVNVTLQogLSUtXzYXMok-gVW6mI6lYIep3qSkDGMfUMa3hYQV3AnEC_FFtx69miN2S5jG8pCLgSZqSSQrmTtbyKXDc_-U34kjOKxpO2j_qI_eA008pMA_boHs6M8r-_YyGC-S4V8ekDpeCgUST3PKQfOc5yb0tSug&gsessionid=sUxxFM_Z3o_ddPQTx_tSe8PIJJYm_T5eeYiPj4oCdXCUwHQDaXWheQ)  
  <sub>14 hours ago</sub>  
  Crude oil futures fell sharply as the market increasingly expects a global surplus as flows from the Middle East recover, while signs of lower demand in...
- [Daily Market Overview · Hot Topics Focus (Morning Briefing 26/11/17)](https://www.google.com/goto?url=CAESZgHEIkXX_8Z52apRhLNqrnPjInE54Jgr6HOgw6mY7GCQ-aSEHwcMBkrJaKQX9p_JGVMOv-oUIDdtC96U_uWTwaNeP4C4isDuucfgket0WCbzIhulfp2MvfRs07-2XnHHODbpmnNqAQ&gsessionid=sUxxFM_Z3o_ddPQTx_tSe8PIJJYm_T5eeYiPj4oCdXCUwHQDaXWheQ)  
  <sub>14 hours ago</sub>  
  Nov 17, 2026 (Tue) | HK Stocks / US Stocks | Data as of 09:00 HKT 01 US plugs 'rent compute' loophole, five-nation chip license policy focus · Reuters...
- [U.S. average diesel prices drop below $6/gal for first time since September (CL1:COM:Commodity)](https://www.google.com/goto?url=CAES7gEBxCJF1zWgGSNuL5Qj-RCz_1FkQMgCwpF-Vc7oc3MfQ9NC3Qwediyzqb62nRooMwv_PhNKCqnle6ISR2CU49t6K6jyNUnf6L175MOubfl88pNRwS5CczPV0C8rOPsRPNIKJRY0kinHf_YVd0iBVhappuu6QnAoTA3W-0P_C1i2sj2tK819IjWgb1tJFhcEuIIFHEp--naRBvV_lQwrXqSAStBX03_av04Mk71QMcKdafxaM4HfcmUkof8rxJbvSi1XGQyHuF9zT-hHlfNOCZ3cclyjTwm9WW-Mn2WsAJ01U1HeFyEzevxEinVmmD3q&gsessionid=sUxxFM_Z3o_ddPQTx_tSe8PIJJYm_T5eeYiPj4oCdXCUwHQDaXWheQ)  
  <sub>23 hours ago</sub>  
  US retail diesel prices fell below $6/gal for the first time since early September, and the national average for regular gasoline fell below $4/gal for the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 142.41 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 154.11 (-7.6%), 50d 152.70 (-6.7%), 200d 128.29 (+11.0%); 50d above 200d
Momentum: RSI(14) 40.6 | MACD -3.337 vs signal -1.435 (histogram -1.902)
Returns: 1d +1.7% | 5d +0.7% | 1m -11.4% | 3m +8.8%
52-week range: 66.17 - 169.53 (now 73.8% of the way up)
Volatility: ATR(14) 5.27 (3.7% of price) | annualised 20d 50.0%
Volume: 0.13x the 20-day average
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
Direction: money coming in (1 month)
Share count change: 1 week: +2.1% (40.19M) over 10d | 1 month: +20.9% (329.91M) over 32d
Shares outstanding: 13.42M | fund size: 1.91B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 503: {"error":{"message":"Model `openai/gpt-oss-120b` is not ready to serve requests yet. The deployment may still be starting up or is not fully provisioned. Please retry shortly.","type":"api_error","param":null,"code":null}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [AI 'like wheat' could become the 'lifeblood of our economy' — essential but not very profitable, says economist Justin Wolfers](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc6ba361ec42cab3aa7fbfdda875f5&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2feconomy%2fai-like-wheat-could-become-the-lifeblood-of-our-economy-essential-but-not-very-profitable-says-economist-justin-wolfers%2far-AA2hBjP3&c=4846407813967420694&mkt=en-us)  
  <sub>Benzinga on MSN, 14h ago</sub>  
  Economist Justin Wolfers states that artificial intelligence (AI) services may become crucial to the economy but fail to generate high profits due to market competition, functioning much like the ...
- [Teucrium 2x Daily Wheat ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc6ba361ec42cab3aa7fbfdda875f5&url=https%3a%2f%2fmarkets.businessinsider.com%2fetfs%2fteucrium-2x-daily-wheat-etf-us53656g2820&c=2324053413144968507&mkt=en-us)  
  <sub>Business Insider, 21h ago</sub>  
  Copyright © 2026 Insider Inc and finanzen.net GmbH (Imprint). All rights reserved. Registration on or use of this site constitutes acceptance of our Terms of Service ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.04 on the week) | 5-year 4.97% (+0.16 on the week) | 10-year 5.15% (+0.16 on the week) | 30-year 5.49% (+0.14 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.60 (+1.37 on the week)
Volatility (VIX): 22.84 (+3.4 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 22.01 (bar of 2026-11-17), from 501 daily bars
Trend: vs 20d SMA 22.13 (-0.5%), 50d 23.99 (-8.3%), 200d 23.62 (-6.8%); 50d above 200d
Momentum: RSI(14) 40.0 | MACD -0.622 vs signal -0.714 (histogram 0.093)
Returns: 1d +1.8% | 5d +1.2% | 1m -7.8% | 3m -13.1%
52-week range: 19.88 - 28.00 (now 26.2% of the way up)
Volatility: ATR(14) 0.40 (1.8% of price) | annualised 20d 19.3%
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
Cost of holding this fund instead of wheat itself: -9.1% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -13.1%, commodity -11.9%, gap -1.2% | 6 months: fund -12.7%, commodity -10.2%, gap -2.5% | 12 months: fund +4.6%, commodity +13.7%, gap -9.1%
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
Share count change: 1 week: -0.5% (-1.14M) over 7d | 1 month: -7.9% (-20.27M) over 31d
Shares outstanding: 10.74M | fund size: 236.30M
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

