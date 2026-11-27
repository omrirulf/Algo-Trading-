# Daily report

**27 Nov 2026, 18:33 Israel time (16:33 UTC)** · 80 names checked · 6 traded · 0 with a problem

**Answers with no explanation:** 13 of 67 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 2 | 14 | 0 |
| Whole-market funds | 14 | 0 | 14 | 0 |
| Sector and country funds | 41 | 3 | 38 | 0 |
| Commodities | 9 | 1 | 8 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| HDFC Bank (HDB) · Company | **Stop raised.** At +4.76R, following the price. Stop-loss raised 26.71 → 27.04. |
| Nvidia (NVDA) · Company | **Stop raised.** At +0.20R, following the price. Stop-loss raised 115.17 → 121.67. |
| Teva Pharmaceutical (TEVA) · Company | **Stop raised.** At +0.16R, following the price. Stop-loss raised 36.32 → 36.84. |
| US media and communication (XLC) · Sector or country | **Stop raised.** At +0.45R, following the price. Stop-loss raised 99.77 → 101.76. |
| Elbit Systems (ESLT) · Company | **Holding.** -0.34R, holding 7 shares. Stop-loss 640.17. |
| South Korea (EWY) · Sector or country | **Holding.** +0.29R, holding 51 shares. Stop-loss 138.53. |
| JPMorgan Chase (JPM) · Company | **Holding.** +0.22R, holding 15 shares. Stop-loss 327.63. |
| Eli Lilly (LLY) · Company | **Holding.** +0.04R, holding 3 shares. Stop-loss 1320.29. |
| Procter & Gamble (PG) · Company | **Holding.** +1.78R, holding 2 shares. Stop-loss 166.99. |
| Royal Bank of Canada (RY) · Company | **Holding.** -0.07R, holding 1 shares. Stop-loss 193.73. |
| Toyota (TM) · Company | **Holding.** -0.03R, holding 1 shares. Stop-loss 205.44. |
| Oil (USO) · Commodity | **Holding.** -0.13R, holding 28 shares. Stop-loss 148.83. |
| Exxon Mobil (XOM) · Company | **Holding.** -0.20R, holding 30 shares. Stop-loss 153.50. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### ASML (ASML) · Company — BULLISH, confidence 0.45

**Result:** ACCEPTED · 2 shares · submitted buy 2 ASML @ ~1306.34, stop 1160.18

**In the model's own words:**

> The policy news that the Dutch government opposes US export curbs on ASML provides a material, ticker‑specific catalyst that is bullish. This is reinforced by strong fundamentals (high margins, rapid revenue growth, low debt) and a consensus strong‑buy rating with a mean price target implying ~64% upside. However, technicals are clearly bearish (price well below short‑ and long‑term moving averages, low RSI, very low volume), which tempers the conviction. Analyst coverage is overwhelmingly positive, and earnings history shows 3 beats out of 4, adding further support. No insider buying activity is present, leaving that dimension neutral. Overall, the bullish factors outweigh the technical weakness, leading to a BUY signal with moderate conviction.

**Main reasons it gave:**
- Dutch government opposes US export curbs on ASML (positive policy news)
- Bernstein issues new buy rating with EUR 2500 target
- Strong fundamentals: 55% YoY revenue growth, 34% profit margin, low debt (8.9% D/E)
- Technical weakness: price below 20‑day, 50‑day, 200‑day SMAs; RSI 36; volume 0.1× avg
- Consensus strong buy with mean price target +63% vs current price

<details><summary><b>News</b> — score +0.40</summary>

- [ASML Holding NV (0QB8): New Buy Recommendation for This Technology Giant](https://www.theglobeandmail.com/investing/markets/stocks/ASML-Q/pressreleases/9032701/asml-holding-nv-0qb8-new-buy-recommendation-for-this-technology-giant/)  
  <sub>The Globe and Mail, 51 minutes ago</sub>  
  Detailed price information for ASML Holding NV (ASML-Q) from The Globe and Mail including charting and trades.
- [ASML Nov 2026 1870.000 put (ASML261127P01870000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/ASML261127P01870000/)  
  <sub>Yahoo Finance UK, 5 hours ago</sub>  
  Find the latest ASML Nov 2026 1870.000 put (ASML261127P01870000) stock quote, history, news and other vital information to help you with your stock trading...
- [ASML Caught in US-China Chip Battle as Netherlands Vows to Resist Trump’s Proposed Export Curbs: ‘We Will](https://www.google.com/goto?url=CAES9gEBxCJF19zOu1kPKYSsgMsux6ZX8bWM6jXGn95kMOlt3mIvVOGusAuF8awmdVm97ZWN9Uc9zaRaByOA7oykh_FBWT2fLq163dsadzJAWoApeKCWqPy92NT4lRLHFOExTU4agT6l3xO5qS6MRDEigVoSdP2phEhyVYO2UL1Z35ulkmDpa9nnH77iElMwkxZDai44UZ4_S8iVPJvPTJ-CzRkS7q5o66PXpjHE6erBeBILCkyvQZjgQmFKlZiHPS6nYMunv9ViEDV4p_9aIpAvtdC6jZrd3kftTOz4kNRQLsE13X_5UG7OIGliQHQMt81RJD43q260SuU&gsessionid=71wV3mmpHpZgRNgwZk0n33vFlnYtK93jTTHkI7mB5usJWB1q2RZRbw)  
  <sub>Benzinga, 6 hours ago</sub>  
  The Dutch government plans to urge the U.S. not to impose proposed China export restrictions that could negatively affect chip equipment maker ASML and...
- [ASML Holding N.V. : Buy rating from Bernstein](https://www.google.com/goto?url=CAESmwEBxCJF1y0E2O1b8AnONRhRNo7DPd85-A7n7zQNxZdOU5SWImU-PbHaTW8u3jdREynMB_2w5XcLUFFoSfYb9mjLPDbjbNjwxKAWk1wxXI-MCYWpEx2_P5IDMbKX1GQujQ15g54ma4E-8WczlFCkrEPaNuq3CnYMedIDEr_YnWjsUGqbi8e1vhCaTr8iI93aftHdaz-7JLTax0flAA&gsessionid=71wV3mmpHpZgRNgwZk0n33vFlnYtK93jTTHkI7mB5usJWB1q2RZRbw)  
  <sub>marketscreener.com, 7 hours ago</sub>  
  In a research note published by David Dai, Bernstein advises its customers to buy the stock. The target price continues to be set at EUR 2500.
- [ASML Nov 2026 1655.000 call (ASML261127C01655000) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXVSEE5WgsZeo2FvlAjvQFFWmwbcG_6ENcHv51xfca7jodQ8meamN5ZZJHMOmBk9wcRXjAnF0aBHdW4bWG-4lV-8e-RSFhwSqfvrnZIoiWgHRC56CzL9wveDQs4LCybVMbrwAqAkn43xjmIsMrmlF5IcyJd14&gsessionid=71wV3mmpHpZgRNgwZk0n33vFlnYtK93jTTHkI7mB5usJWB1q2RZRbw)  
  <sub>Yahoo Finance UK, 4 hours ago</sub>  
  Interactive chart for ASML Nov 2026 1655.000 call (ASML261127C01655000) – analyse all of the data with a huge range of indicators.
- [ASML Dec 2026 1590.000 call (ASML261218C01590000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScwHEIkXXiTIk92c1W3or7d3trFS6v4XKM-Sj1ugyq87YnWK-5FwItD5x5lW-dedLCHUdv6u5dhwolOj8PkPqyJ9t-vtHQLKXQrFvz7B_k4z5m3zewCwktPAszfIV4QXTfiI4sTmIO_o0-6rkFlqf7Qa2RRI&gsessionid=71wV3mmpHpZgRNgwZk0n33vFlnYtK93jTTHkI7mB5usJWB1q2RZRbw)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Find the latest ASML Dec 2026 1590.000 call (ASML261218C01590000) stock quote, history, news and other vital information to help you with your stock trading...
- [ASML Dec 2026 1050.000 put (ASML261231P01050000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXX62siqJHJpvV-MUwEgSI3vPdR71TmtHPHGYQ007Cc6YT8eoEVSK86g36tyBoKzL_TO4e00C2OgFqxewgt6hEtktBykxWbJLWbDsBrR_7qgwiY9-PTg-Kv0yQisje291YRy2NPt5bquYvijivICH4&gsessionid=71wV3mmpHpZgRNgwZk0n33vFlnYtK93jTTHkI7mB5usJWB1q2RZRbw)  
  <sub>Yahoo Finance UK, 12 hours ago</sub>  
  Find the latest ASML Dec 2026 1050.000 put (ASML261231P01050000) stock quote, history, news and other vital information to help you with your stock trading...
- [ASML Dec 2026 2100.000 call (ASML261224C02100000) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESeQHEIkXXgbHofOoDV4DacFg2P-NxqluNGxBZ1FGElu4ZFjMhvAjyF8i2ZDYpABJYduTwXgMD4796I9sk5qKFwLeTpENRTWwSDYZEJVG7-MidY6slROVHGedoT2-qx7Ep58LOxbcqFygsbHhFWqqF7NH6JBET4v2lbNI&gsessionid=71wV3mmpHpZgRNgwZk0n33vFlnYtK93jTTHkI7mB5usJWB1q2RZRbw)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Interactive Chart for ASML Dec 2026 2100.000 call (ASML261224C02100000), analyze all the data with a huge range of indicators.
- [ASML Dec 2027 1280.000 call (ASML271217C01280000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXFpTNdiusMtheVoEpuDzL8RmSwgb0OPJLedxoYUnJ0qp_G6ayUjVJsKEIx0qZHf34dwECrM-VuO11V7-NxkjeSkatDqIMFb-EGGa_b9jSDICO5ECIuJ24jgeY71uWef6t_2B_q0o2DpjsGt6M4L4&gsessionid=71wV3mmpHpZgRNgwZk0n33vFlnYtK93jTTHkI7mB5usJWB1q2RZRbw)  
  <sub>Yahoo Finance Singapore, 13 hours ago</sub>  
  Find the latest ASML Dec 2027 1280.000 call (ASML271217C01280000) stock quote, history, news and other vital information to help you with your stock trading...
- [ASML Nov 2026 2130.000 call (ASML261127C02130000) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXDsXh3NKPbsDNejBgIk06eqeeLm5GDAIc4T3XS-FL4xkkC3O460M2vHccJCtcj6UcpBcxO76S_EGWBnYSbNNZmbXdINOu0dq7U8PbJ3f2g2C1NO7rRJNVzORUy7wbdtrxQXcBFxCfgSZyVDq8sfZRkZIaGaI&gsessionid=71wV3mmpHpZgRNgwZk0n33vFlnYtK93jTTHkI7mB5usJWB1q2RZRbw)  
  <sub>Yahoo Finance UK, 13 hours ago</sub>  
  Interactive chart for ASML Nov 2026 2130.000 call (ASML261127C02130000) – analyse all of the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.80</summary>

```text
Last close 1,300.70 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 1,430.04 (-9.0%), 50d 1,603.25 (-18.9%), 200d 1,599.66 (-18.7%); 50d above 200d
Momentum: RSI(14) 36.1 | MACD -82.774 vs signal -75.049 (histogram -7.725)
Returns: 1d -0.2% | 5d -4.1% | 1m -21.8% | 3m -23.3%
52-week range: 1,015.43 - 1,989.44 (now 29.3% of the way up)
Volatility: ATR(14) 72.69 (5.6% of price) | annualised 20d 72.2%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.90</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 501.31B
Valuation: trailing P/E 32.01 | forward P/E 20.52 | P/B 1,116.84 | PEG 0.73
Profitability: profit margin 34.1% | operating margin 38.6% | ROE 65.6%
Growth (YoY): revenue +55.2% | earnings +135.9%
Balance sheet: debt/equity 8.9% | free cash flow 10.37B
Risk: beta 1.33 | short interest 0.4% of float
Next earnings: 2027-01-27
```

</details>

<details><summary><b>What this fund holds</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.90</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-09-30 beat by 17% | 2026-06-30 beat by 9% | 2026-03-31 beat by 7% | 2025-12-31 missed by 5%
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
Consensus: strong_buy (mean 1.37 on a 1=strong buy to 5=strong sell scale, 16 analysts)
Ratings: 7 strong buy, 31 buy, 2 hold, 1 sell, 0 strong sell
Price target: mean 2,132.43 (+63.9% vs last close), range 847.64 - 2,860.82
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

### Caterpillar (CAT) · Company — BULLISH, confidence 0.45

**Result:** ACCEPTED · 1 shares · submitted buy 1 CAT @ ~561.94, stop 503.80

**In the model's own words:**

> Fundamentals are strong (high ROE, robust earnings growth) and insiders have net bought shares, while analysts maintain a buy consensus with a sizable upside target. Technicals show short‑term oversold conditions but overall downtrend and thin volume temper confidence. No material news catalyst is present, so the view rests on fundamentals and insider buying.

**Main reasons it gave:**
- Fundamentals: ROE 56.1% and earnings growth 46.1% YoY
- Insider activity: net purchase of 14,690 shares (+1.3% of holdings) in last 180 days
- Analyst view: consensus buy with mean price target $807.26 (+45.7% upside)
- Technical: RSI 37.5, price below 20‑day SMA, volume 0.06× 20‑day average
- Earnings record: 3 beats and 1 in‑line over last 4 quarters

<details><summary><b>News</b> — score +0.00</summary>

- [How Bad Would A Data Center Slowdown Be For Caterpillar Stock?](https://www.trefis.com/stock/cat/articles/629352/how-bad-would-a-data-center-slowdown-be-for-caterpillar-stock/2026-11-27)  
  <sub>Trefis, 4 hours ago</sub>  
  Today's big story: Anthropic Broke Its $83 IPO Price. What Did Facebook Do Next?Caterpillar (CAT) shares lost 38.5% since ...
- [Toromont Industries Ltd. (TIH.TO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TIH.TO/)  
  <sub>Yahoo! Finance Canada, 3 hours ago</sub>  
  Find the latest Toromont Industries Ltd. (TIH.TO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Red Cat Just Dropped 27% in a Week. Will RCAT Stock Hit $1.50 or $2 First?](https://www.google.com/goto?url=CAESrQEBxCJF15kwqBbESekuXHkf2ukMBo-SPOuoZE2QCGcZytT6dRyKgvLhnnq_G4NJZhNCGg2dJ4G4nE0396S2GLYHuVHPTY6epeKLzOVVUgEUaKHQcx5sYSx2jLHlLXIQralRw_pseu6yrFGeY8TDIWijCa3aJ4nVXKjAXhoF_wrKMLXL5Hon0AzKa7DghtVscMRZjHnKYku0l8OGkDP4aceiyFZpNU9plmPMC_stTQ&gsessionid=3H5ZW9xE0_4ATicduNExlawjyJN1BToVvgh7UcFU5xeqtI36AweVSw)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  Red Cat (RCAT) plunged 27% in a week to $1.76 after a huge revenue miss, and could hit $1.50 before $2. Ondas (ONDS) and AeroVironment (AVAV) also fell...
- [Caterpillar's $78 Billion Backlog, Explained](https://www.google.com/goto?url=CAESvQEBxCJF16uUtbNtbxKDhDnghSiPF2M1RvmXHvlpPxR6LMLEWfRp4Atxl_CtyWxAs71L6vlK6e-lQX-F9CmHQ0s8U4kUdYOWkVo8u_syAtkBz8RmuEKTO6WsfB_Ad077SNjdjbpaRp27D2i63wrMlhrZsmGaY_dFoOzcdAzwIpMSpt1_kQI4OoVDogZleWurlX_tN31oqHMUV-ED82CTuApT6-sXy4xgNnOURJRfGhOTf06l5EZCAXrpDOGOonk&gsessionid=3H5ZW9xE0_4ATicduNExlawjyJN1BToVvgh7UcFU5xeqtI36AweVSw)  
  <sub>The Globe and Mail, 20 hours ago</sub>  
  Detailed price information for Caterpillar Inc (CAT-N) from The Globe and Mail including charting and trades.
- [Red Cat (RCAT) Stock Could Be Pricey After Weak Sales News](https://www.google.com/goto?url=CAESxQEBxCJF13U3Ch6FYwJp5aBeodNE1CBjEHwgJ5OmTgEBM7QKpxvwcYU2XbehdnxH6R0Uhp3DoP-SI70FnODl8AL01bh_-m5etcTi6OtW-jKSGd8Qcv_ONduUCaJK5L-z4c2yt9RdayI_Ze0MVwadExkH4PQXTSwlRQhryic8MQtW9lLIAtbJJBYXF6bddOAZVZ7RHmr09l1c4sRA8gySnNmbjfYbetO2U_szVr8PGd1dnqP0AKNTcJd6o0G9234zwvVJSVO6RA&gsessionid=3H5ZW9xE0_4ATicduNExlawjyJN1BToVvgh7UcFU5xeqtI36AweVSw)  
  <sub>Simply Wall St, 9 hours ago</sub>  
  Red Cat Holdings has seen its share price swing sharply in recent years, which puts fresh attention on a basic question for investors: Is the current...
- [Is today’s Black Friday tech rebound a real rally—or a dead cat bounce?](https://www.google.com/goto?url=CAESuQEBxCJF1_MWSd7xiJGYIMU_wLFsrV4aiLf06oWYZKhfB0uiJFomHmbTXIdwYRhHhZRePzIKpqTCWAhr_NTZIfnLIhpqhRezd4yIJSeh__9Df69yi-pmB4IIO7Bnfdi1MeMBXe_owtBku1iGn_mQgv46SCiCscOVIudAat1efofzCIUmBPyvcDNgIDe08L3ImBCPewKd4ftsXhafcs7_N826y71mbtc7aRTI_9cNsi3m0BrkG7h7wKbNRQ&gsessionid=3H5ZW9xE0_4ATicduNExlawjyJN1BToVvgh7UcFU5xeqtI36AweVSw)  
  <sub>Investing.com, 2 hours ago</sub>  
  Investing.com - U.S. equity futures are rallying sharply this morning—led by a more than 2% surge in the Nasdaq—mirroring broad-based gains across Asia.
- [Caterpillar stock weekly forecast: Neutral momentum readings keep range in play](https://www.google.com/goto?url=CAESlQEBxCJF1zcgZYa5xkzqD3CToapr0laXfuuruGjgaIX3-ODdBkot_rAElBdHzKfoWwR84Q4aWHn0Yr6mc_9-P9LoceuXnrKpux5bICaHh8-_kPlO7TzYX2q0hVzHfIy56OlO7NNaeqmpglNr8v8Ttafm9hEqmC5Yt4AK58FOrWS3JUz481doXPAf7A-U9ltgIZ5MOjyjVg&gsessionid=3H5ZW9xE0_4ATicduNExlawjyJN1BToVvgh7UcFU5xeqtI36AweVSw)  
  <sub>Traders Union, 24 hours ago</sub>  
  Caterpillar gains 6.43% this week, trading at $543.26 after a volatile rebound and renewed support levels in focus.
- [The public housing stock expands with the purchase of six homes from the 30% affordable housing reserve in a building on Consell de Cent street | Info Barcelona | Barcelona City Council](https://www.google.com/goto?url=CAESgQIBxCJF17o0E_NKMw1WhJZYDnLkTd0arZ7tA1c1SvWq31iJRyLUG5GZQnotAeSBq42ejzqDquimn29OhTll37lql-Su4tU2uGW0HDzjkmpDfLHoD21QiOw1ec310hEAxNJfMt9BlZ5b6F9eFjH90DctEd5dYGusDq30Q6SP5ll4x9awntoaOuwaq8nbU6Fdhjm4jh6X-xVceWqh24b51YiixIqoCnlwFn_Sj5-NJj-I5SXpuK2CeqKtrbS7y9rSDPEjxuuW4ESCGkltpgCZtx8EbzLwC41oygmgfDahnj3lksdmXgESQbAQhC6HPnFl8u5JNCv0eyQYG8OqJrPucwKzXA&gsessionid=3H5ZW9xE0_4ATicduNExlawjyJN1BToVvgh7UcFU5xeqtI36AweVSw)  
  <sub>Ajuntament de Barcelona, 53 minutes ago</sub>  
  The homes are part of a new residential development in the Fort Pienc neighbourhood and will be incorporated into the city's public housing stock.
- [A trader claiming $6 million in profits revealed their strategy—the stock ticker appeared on GitHub 10 days before its listing on Robinhood.](https://www.google.com/goto?url=CAESkQEBxCJF1yTtahNEtmnKGwcaDDH3zTw-cbrWUGdDT6FRbrSfVzHqKlow_UDF1_hL_M5VUMTd7n4Ukac1pR3ESxzO254N2e6S1xsO-Zo1tR8TAG4fJZW7_r26P-bak39oR21fplyKjNyefofUMPlWpYX6rXM_aL-YdBQeE7WOlGHQzWQp2hN0paeQioLFNOQgAx7c&gsessionid=3H5ZW9xE0_4ATicduNExlawjyJN1BToVvgh7UcFU5xeqtI36AweVSw)  
  <sub>Iolite（アイオライト）, 12 hours ago</sub>  
  BitTrade spokesperson "Toreo Bito" explains the latest trends in Web3.0 and crypto assets. In this installment, he discusses a trading strategy revealed by...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 554.04 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 574.38 (-3.5%), 50d 694.95 (-20.3%), 200d 800.06 (-30.7%); 50d below 200d
Momentum: RSI(14) 37.5 | MACD -43.145 vs signal -46.906 (histogram 3.760)
Returns: 1d +1.9% | 5d +3.1% | 1m -22.3% | 3m -30.8%
52-week range: 510.45 - 1,064.90 (now 7.9% of the way up)
Volatility: ATR(14) 29.02 (5.2% of price) | annualised 20d 59.9%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 253.53B
Valuation: trailing P/E 21.74 | forward P/E 17.22 | P/B 11.80 | PEG 0.96
Profitability: profit margin 15.2% | operating margin 18.8% | ROE 56.1%
Growth (YoY): revenue +17.3% | earnings +46.1%
Balance sheet: debt/equity 210.4% | free cash flow 3.97B
Risk: beta 1.64 | short interest 2.5% of float
Next earnings: 2027-02-02
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
Institutional ownership: 74.5%
Largest holders: Blackrock Inc. (8.2%), State Street Corporation (7.5%), Vanguard Capital Management LLC (6.6%), State Farm Mutual Automobile Insurance Co (3.1%), Vanguard Portfolio Management LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.40</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.40</summary>

_Not available today._

</details>

### Microsoft (MSFT) · Company — NEUTRAL, confidence 0.45

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Fundamentals remain strong and analyst consensus is bullish with a high price target; insider net buying adds a modest positive signal. However recent news highlight a Microsoft 365 outage and concerns about margin erosion from AI data‑center spending, and technicals show price below short‑term averages with very low volume, indicating near‑term downside pressure. The mixed evidence leads to a neutral stance with moderate conviction.

**Main reasons it gave:**
- Recent Microsoft 365 outage and margin concerns from AI data‑center spending (news)
- Price below 20‑day and 50‑day SMA with RSI 41.3 (technical)
- Strong fundamentals: 41% profit margin, 18.8% YoY revenue growth, debt/equity 28.5% (fundamentals)
- Analyst consensus strong buy with mean price target $637.36 (+28.9%) (analyst view)
- Insiders net bought ~258k shares (+3.1% holdings) (insider activity)

<details><summary><b>News</b> — score -0.30</summary>

- [Is Microsoft (MSFT) Fully Valued Following Its Atos Sovereign Cloud Deal?](https://finance.yahoo.com/markets/stocks/articles/microsoft-msft-fully-valued-following-090939545.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Microsoft (MSFT) is back in focus after extending its collaboration with Atos to build sovereign cloud and AI environments for European public sector and...
- [Can Microsoft Stock Sustain Margins as AI Data Center Spending Climbs?](https://www.theglobeandmail.com/investing/markets/stocks/AMZN/pressreleases/9033091/can-microsoft-stock-sustain-margins-as-ai-data-center-spending-climbs/)  
  <sub>The Globe and Mail, 8 minutes ago</sub>  
  MicrosoftMSFT is testing how far AI data center spending can climb before it erodes profitability. Capital expenditures, including finance leases,...
- [Cloud Outage Might Change Microsoft (MSFT) Stock Narrative](https://www.google.com/goto?url=CAESvAEBxCJF18z-O27dZ9xQWu-fyvMBbD84oUa2uZM6JmJeSzwclAUZa1vrcvkbVm2FAEanfMSNh6lWka8Uj_anVqH_bpHzmzyqD2hOQYq5h3k_lc7kiokau2AFxq68myLNyP9EUW_2Y-6kO57ItFBU6XoEH-7XD7W9gfCgYUXb1o2M560IxjbjknDVWOvlul3t7SVHkRB-0XTi0b1l0Dn1ltF5AxS8Yn7RMe-V7MAg8FwlQOqdKt21lxNt2GTfyg&gsessionid=c-4r86PNk_LNd98dJbtxAQd7J7MPQ6aWK06DRH3GJPru7VzT8UWaIQ)  
  <sub>Simply Wall St, 2 hours ago</sub>  
  Microsoft is contending with AI-heavy capital spending, a recent 24 hour global Microsoft 365 outage tied to a Windows scalability bug, and an internal Code...
- [MSFT Jul 2027 485.000 put (MSFT270716P00485000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScgHEIkXXIt8nooTXdKD4UrbbWIWOfbVz3u7pCTSwSMnHb1eynM5SFL3cqdqV404RVB55KthTcHPgyrp1-yla6Jy5l5CPt6IRgJ9LHQoCDQYw2lBGux0t_hmYTQKqdDY2Z2vYR0GSCB_OnEyoERljXqBG8w&gsessionid=c-4r86PNk_LNd98dJbtxAQd7J7MPQ6aWK06DRH3GJPru7VzT8UWaIQ)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest MSFT Jul 2027 485.000 put (MSFT270716P00485000) stock quote, history, news and other vital information to help you with your stock trading...
- [Automation software stocks Q3 teardown: Microsoft vs the rest](https://www.google.com/goto?url=CAESzQEBxCJF14OREf1a2Hw6hxgk9IyExOqddlFBZlWiZjfYh-KDy66rPg_y7_RW-GQwM55ylWsdaPX_Wkc-dNKLviyqQN7iEZhdf_k-KawRuzEiw-O7ZozVGFnHsF1fmH-UNioNTzuCnlkS6LTYhuCghVICqyUMPQ1hq1AStRvO2Gsd6j1w8xZReHEx6SA2V8hv_2JuoiCjg5B2s8RAeLtZXKz-fpnsSfZpFJ6XlcP8Ewlm0ulgRf2W63Ml_j6nTf0EaOGGCavYOv0PncskH3fq&gsessionid=c-4r86PNk_LNd98dJbtxAQd7J7MPQ6aWK06DRH3GJPru7VzT8UWaIQ)  
  <sub>The Globe and Mail, 5 hours ago</sub>  
  Detailed price information for Microsoft Corp (MSFT-Q) from The Globe and Mail including charting and trades.
- [Salesforce Before Q3 Earnings Release: Should You Buy the Stock Now?](https://www.google.com/goto?url=CAES0wEBxCJF14g43iwtIRVsF-XavITotfhqG73_qEJkc_Mgt3_mQf2E-Oxjc0nc4MtIMsRlNlFG-ZBjh4UiopJHURuZzIKX6c9P8-6dmCOgCO2HQm8NTJTZrkVQ6aB_nyP9dmoBDaiHNjOiy7EtTe7ezA2UxE0mzNwkk38SISXgAq93Zjk5zB585BmyvO06W-ZgB7uBfbUsDUO523S5TslAJZFv6SzX_70vWic8PobpKgmbmSnlOWL6ftcaM14Nn_PdFNDVYCFkEDylhJpCC3v_QaX9ygEA&gsessionid=c-4r86PNk_LNd98dJbtxAQd7J7MPQ6aWK06DRH3GJPru7VzT8UWaIQ)  
  <sub>The Globe and Mail, 2 hours ago</sub>  
  Detailed price information for Microsoft Corp (MSFT-Q) from The Globe and Mail including charting and trades.
- [MSFT Nov 2026 455.000 put (MSFT261127P00455000) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESeAHEIkXX3Rhdyfh3Cyd-TWy2Cm4LtfOdjyBoEyG84AVXEmNcfusv-wICIgP3EQgev850ZpPM0J10eEJl9E6l3izO4K77Dq2NcTmxEUmKHSn39riT2-0U0XE3bqeU1splOlV_cZvJs0g5l8SzLSWo6qBzO2RpPO9vbQ&gsessionid=c-4r86PNk_LNd98dJbtxAQd7J7MPQ6aWK06DRH3GJPru7VzT8UWaIQ)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Interactive Chart for MSFT Nov 2026 455.000 put (MSFT261127P00455000), analyze all the data with a huge range of indicators.
- [MSFT Feb 2027 550.000 put (MSFT270219P00550000) interactive stock chart](https://www.google.com/goto?url=CAESeAHEIkXXw5qjuEoI2q6i-M0DpVHUysjXZngYq8wuViqZCJ22Ez5Hh5FDFyosrvACu9PTMc-OmgVYypOeJb9eR7mCu2tKXoOlJZoSMi_ZYaZGf1KC4ivqdAlX3xh6VUsdGPiNP73a5-q8zmmFuVG4Uz2t60mvXNIzKQ&gsessionid=c-4r86PNk_LNd98dJbtxAQd7J7MPQ6aWK06DRH3GJPru7VzT8UWaIQ)  
  <sub>Yahoo Finance UK, 10 hours ago</sub>  
  Interactive chart for MSFT Feb 2027 550.000 put (MSFT270219P00550000) – analyse all of the data with a huge range of indicators.
- [MSFT Dec 2026 510.000 put (MSFT261231P00510000) interactive stock chart](https://www.google.com/goto?url=CAESeAHEIkXXXYmWOcFJca8m-W50egp2lm4NH5f14-rrXpIORSV3pB9Sj36dYxuRYynESz3tLzic9opUeuR2BAQ8b9Hm2rqZb4d0dLr5gosdS1QdLdhryaUVG9uyosb8V08Gzmg15HgNqtiSECT3rrCDSLh2nr9N80M5nw&gsessionid=c-4r86PNk_LNd98dJbtxAQd7J7MPQ6aWK06DRH3GJPru7VzT8UWaIQ)  
  <sub>Yahoo Finance UK, 12 hours ago</sub>  
  Interactive chart for MSFT Dec 2026 510.000 put (MSFT261231P00510000) – analyse all of the data with a huge range of indicators.
- [MSFT Nov 2026 375.000 put (MSFT261127P00375000) interactive stock chart](https://www.google.com/goto?url=CAESeAHEIkXXKO_6qfWZuAggN3rTB29CkgPy7Kv89FyDMYunr9-mthRsHNiPNsBvc7GH6ApIIhgCoN8h4gLX1maegcbbEU40d_Y0W1SExDh2hR9yfkTfukqL8rspJv7Y4XXBZGTHRoAJHmp9fc7GRJB29WU8s7ZEY_4JNA&gsessionid=c-4r86PNk_LNd98dJbtxAQd7J7MPQ6aWK06DRH3GJPru7VzT8UWaIQ)  
  <sub>Yahoo Finance UK, 16 hours ago</sub>  
  Interactive chart for MSFT Nov 2026 375.000 put (MSFT261127P00375000) – analyse all of the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 494.57 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 515.36 (-4.0%), 50d 519.49 (-4.8%), 200d 445.34 (+11.1%); 50d above 200d
Momentum: RSI(14) 41.3 | MACD -8.787 vs signal -5.184 (histogram -3.603)
Returns: 1d +0.9% | 5d -0.7% | 1m -6.9% | 3m -3.7%
52-week range: 352.83 - 555.80 (now 69.8% of the way up)
Volatility: ATR(14) 16.43 (3.3% of price) | annualised 20d 39.2%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.67T
Valuation: trailing P/E 25.81 | forward P/E 20.43 | P/B 7.81 | PEG 1.43
Profitability: profit margin 41.2% | operating margin 47.1% | ROE 34.2%
Growth (YoY): revenue +18.8% | earnings +32.3%
Balance sheet: debt/equity 28.5% | free cash flow 2.99B
Risk: beta 1.04 | short interest 0.9% of float
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

```text
Consensus: strong_buy (mean 1.34 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 14 strong buy, 41 buy, 3 hold, 0 sell, 0 strong sell
Price target: mean 637.36 (+28.9% vs last close), range 440.00 - 870.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

```text
Last 180 days: bought 518,348 shares in 17 transaction(s) | sold 260,692 shares in 11
Net: +257,656 shares (+3.1% of insider holdings) | insiders hold 8,614,385 shares
Distinct insiders: 0 buying, 4 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-11-10 NUMOTO TAKESHI (Officer): 5,000 shares, 2.65M
  - 2026-11-09 HOOD AMY E (Chief Financial Officer): 7,305 shares, 3.98M
  - 2026-10-13 HOOD AMY E (Chief Financial Officer): 7,305 shares, 3.98M
  - 2026-09-14 HOOD AMY E (Chief Financial Officer): 41,674 shares, 20.76M
(16 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

_Not available today._

</details>

### Novo Nordisk (NVO) · Company — NEUTRAL, confidence 0.45

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Novo Nordisk shows a mixed short‑term picture. The stock is holding just above its 7‑, 20‑ and 50‑day moving averages, but trading on extremely thin volume, which weakens the technical upside. Recent news of a new Wegovy launch in Sweden has not translated into price gains, and competitor headlines about Eli Lilly pulling ahead add bearish sentiment. On the other hand, the company remains very cheap on a trailing P/E of 10.34, boasts strong profit margins and robust free cash flow, and analysts still price modest upside (≈+11%). With no insider buying signal, the evidence cancels out, leading to a neutral stance with moderate conviction.

**Main reasons it gave:**
- Holding above 7‑, 20‑ and 50‑day moving averages despite slight decline (technical)
- Trailing P/E 10.34 and operating margin 50.8% show cheap, high‑profit business (fundamental)
- Announced Wegovy obesity pill launch in Sweden while stock fell (news)
- Consensus hold with price target $45.63 (+11.5%) (analyst)

<details><summary><b>News</b> — score -0.20</summary>

- [Novo Nordisk (NVO) Stock Price Prediction: Price holds above short-term averages as buyers test resistance](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b099754453d417ab88ecceff504df65&url=https%3a%2f%2fblockchain.news%2fnews%2f20261127-price-prediction-price-nvo-holds-above-short-term-averages-as&c=4912850389751974470&mkt=en-us)  
  <sub>Blockchain News, 12h ago</sub>  
  Novo Nordisk (NVO) is trading at $40.73, slightly lower on the session, while holding above its 7-, 20-, and 50-day moving averages. Binance ...
- [Novo Nordisk Stock (NVO) Falls Despite Pushing Ahead of Eli Lilly in Obesity Pill Rollout](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b099754453d417ab88ecceff504df65&url=https%3a%2f%2fwww.tipranks.com%2fnews%2fnovo-nordisk-stock-nvo-falls-despite-pushing-ahead-of-eli-lilly-in-obesity-pill-rollout&c=17071512431561443560&mkt=en-us)  
  <sub>TipRanks, 12h ago</sub>  
  Danish drugmaker Novo Nordisk ($NVO) announced Friday that it plans to launch its Wegovy obesity pill in Sweden on December 24. This marks the latest step in the ...
- [Eli Lilly is now worth 7 Novo Nordisks. Here’s how the gap got so wide.](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b099754453d417ab88ecceff504df65&url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2feli-lilly-is-now-worth-7-novo-nordisks-here-s-how-the-gap-got-so-wide%2far-AA2iiBY9&c=10309665535385139470&mkt=en-us)  
  <sub>The Motley Fool on MSN, 29h ago</sub>  
  Eli Lilly's GLP-1 weight-loss drugs continue to grow at a rapid clip.
- [How Eli Lilly Pulled Ahead of Novo Nordisk in the GLP-1 Race](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b099754453d417ab88ecceff504df65&url=https%3a%2f%2fnai500.com%2fblog%2f2026%2f11%2fhow-eli-lilly-pulled-ahead-of-novo-nordisk-in-the-glp-1-race%2f&c=12923822602125184706&mkt=en-us)  
  <sub>NAI500, 20h ago</sub>  
  Eli Lilly (LLY) holds a market capitalization of roughly $1.2 trillion, nearly seven times the $172.5 billion valuation of Novo Nordisk (NVO), as the two pharmaceutical giants rank first and ...
- [Eli Lilly (LLY) Adds FDA Vision Warning To GLP 1 Drug Labels](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b099754453d417ab88ecceff504df65&url=https%3a%2f%2ffinance.yahoo.com%2fhealthcare%2farticles%2feli-lilly-lly-adds-fda-151036334.html&c=2439384307189339622&mkt=en-us)  
  <sub>Yahoo Finance, 32h ago</sub>  
  Eli Lilly (NYSE:LLY) and Novo Nordisk plan to add new FDA required warning labels to GLP-1 drugs tied to rare vision risks. The updated labels will reference non arteritic anterior ischemic optic ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 40.94 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 40.43 (+1.2%), 50d 39.40 (+3.9%), 200d 42.71 (-4.2%); 50d below 200d
Momentum: RSI(14) 54.4 | MACD 0.069 vs signal 0.050 (histogram 0.019)
Returns: 1d -0.1% | 5d +5.3% | 1m +6.9% | 3m -10.2%
52-week range: 35.29 - 63.98 (now 19.7% of the way up)
Volatility: ATR(14) 1.13 (2.8% of price) | annualised 20d 39.0%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 180.37B
Valuation: trailing P/E 10.34 | forward P/E 11.65 | P/B 5.51 | PEG 3.96
Profitability: profit margin 33.9% | operating margin 50.8% | ROE 58.4%
Growth (YoY): revenue +5.6% | earnings -15.8%
Balance sheet: debt/equity 61.7% | free cash flow 32.75B
Risk: beta 0.37 | short interest 1.3% of float
Next earnings: 2027-02-03
```

</details>

<details><summary><b>What this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.60</summary>

```text
Earnings record, last 4 quarters: 1 beat, 1 in line, 2 missed
  2026-09-30 missed by 22% | 2026-06-30 missed by 6% | 2026-03-31 beat by 23% | 2025-12-31 in line
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
Consensus: hold (mean 2.85 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 0 strong buy, 2 buy, 10 hold, 1 sell, 0 strong sell
Price target: mean 45.63 (+11.5% vs last close), range 39.31 - 63.88
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

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

### Alphabet (Google) (GOOGL) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The technicals and recent earnings record are bearish, while fundamentals and analyst consensus are bullish. The news provides no material catalyst, only a slight negative sentiment from AI pushback. The mixed signals lead to a neutral stance with low conviction.

**Main reasons it gave:**
- Technical indicators: price below 20d/50d/200d SMAs and RSI 37.8 – bearish
- Earnings record: 3 of last 4 quarters missed expectations – bearish
- Fundamentals: trailing P/E 14.3 and profit margin 50% – bullish
- Analyst consensus strong buy with 44% upside target – bullish

<details><summary><b>News</b> — score -0.10</summary>

- [GOOGL Nov 2026 520.000 call (GOOGL261127C00520000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GOOGL261127C00520000/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Find the latest GOOGL Nov 2026 520.000 call (GOOGL261127C00520000) stock quote, history, news and other vital information to help you with your stock...
- [Los Angeles disables Google AI search features as school pushback grows (GOOG:NASDAQ)](https://seekingalpha.com/news/4676929-los-angeles-disables-google-ai-search-features-as-school-pushback-grows)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  School districts are moving to disable Google's (GOOG) (GOOGL) AI features and weighing a broader shift away from its products unless the tech giant...
- [Alphabet Drops 15% in a Year: Buy, Sell or Hold the Stock?](https://www.google.com/goto?url=CAESyAEBxCJF1_6LgYa5pYQwCwl_UnD1YMUVLWCHUYf1qwnCyssQdebxT8jgo6Qw9tGG906NA9YKsc8Uk4KXXckV7Vrn4Ek15zTy_jXfWwjFte7yDJhA6gw6LhE4PiHlIgEZhyYNF10UbG-p7BfXmgLD7Fptfh06UD1lRmV_ttRKqBzkIM34wxRTrP9gSFxXQ6q-WEqWuNVR1e3_9xvHxVotq1Tc3CpHPsslbV01QTfPcKn3cJ1y0r3vMuAJNmuvI59qRms0v6gwXD31Iw&gsessionid=QodP-sZ48yQ0SBrxE8-eGKBlVDC_1WGO_Az90Am7eXFguVnSfuJLPQ)  
  <sub>The Globe and Mail, 22 hours ago</sub>  
  Alphabet GOOGL shares have dropped 14.7% in the trailing 12-month period, underperforming the broader Zacks Computer & Technology sector's decline of 3.6%.
- [GOOGL Nov 2026 315.000 call (GOOGL261125C00315000) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESegHEIkXXtdW7ROCPs8PYnPtFDxlrfLfz2tDSKNQHwH5-VsqIQLXhYtz6UBQSjzEQMMmNFfdb39VWtWac03uvQiZXgJ23t6GXukJRPS7XVcpc_Ze4cikwrs-JNxNiDbZil_P8Moaw2GywoGBulXlIeiAMmAoAlx_Ll68y&gsessionid=QodP-sZ48yQ0SBrxE8-eGKBlVDC_1WGO_Az90Am7eXFguVnSfuJLPQ)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Interactive Chart for GOOGL Nov 2026 315.000 call (GOOGL261125C00315000), analyze all the data with a huge range of indicators.
- [SpaceX's AI Business Is Now Nearly Half of Revenue. Here's What Happens to the Stock if Google and Anthropic Both Renew.](https://www.google.com/goto?url=CAESiwIBxCJF18mdtSvrtlvnX0gjQ0jztU7_6ibH_M6yGznb8KHKYkEB-BYZozNK44XKDy750CmFyReDPGxMU-zfCWsY3XSHEKa7CMNMa9r-wQzkJrmmOhrbOvaMzqGwefDmAhw12UsePv_wKVqUJ54TNfC90H1ttZPy8jVJTtwOImRVBWdeufs9T0OjOyMBi_8b5OKD4nsL6_aA4o8U_cP4Lp_FxF4pB7FbHKEtR_aiOeIBkOUSl7oewcg1EL-mDvZ3cEqM_EGbMDYtBMOQ6I2kxt3hw48uEFYoTI8Uv2js1RwpKYYvLaa6cYLskiD3JMyrcwERO_zQoKrgIa92qM8vQXM3U3Sbp82Vli7zO9E&gsessionid=QodP-sZ48yQ0SBrxE8-eGKBlVDC_1WGO_Az90Am7eXFguVnSfuJLPQ)  
  <sub>The Globe and Mail, 4 hours ago</sub>  
  Detailed price information for Alphabet Cl A (GOOGL-Q) from The Globe and Mail including charting and trades.
- [GOOGL Nov 2026 325.000 put (GOOGL261127P00325000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESdAHEIkXXHO2sll3fsTsA0oi2HVUogPtkmt1JR1aNGgyQQJqNpvLAOcpIFdYe000WF9N6fwer3P0cPLOa_ZTl61Q52qDdz9pAOOZllukPIfSQfeNaCc4PVJp4-wBWKa8htTQJYIOquCF80g5TZ99xPnwyqw4R&gsessionid=QodP-sZ48yQ0SBrxE8-eGKBlVDC_1WGO_Az90Am7eXFguVnSfuJLPQ)  
  <sub>Yahoo! Finance Canada, 10 hours ago</sub>  
  Find the latest GOOGL Nov 2026 325.000 put (GOOGL261127P00325000) stock quote, history, news and other vital information to help you with your stock trading...
- [GOOGL Nov 2026 297.500 put (GOOGL261127P00297500) stock price, news, quote and history](https://www.google.com/goto?url=CAESdAHEIkXXiNe5-6uCffTXbzQxagP8mEi2joKfiWS-Q8UIBX6zKZnIf-m4-uU3mbv9SJ7_Jjp9XX3uRNDB5_TH1TV2L4RImManp5mnX65hTGamj1-J-Da2XXhHe7BOWd_v4M7NR1dve1swRBPSxXzwZrdwTDuo&gsessionid=QodP-sZ48yQ0SBrxE8-eGKBlVDC_1WGO_Az90Am7eXFguVnSfuJLPQ)  
  <sub>Yahoo Finance UK, 10 hours ago</sub>  
  Find the latest GOOGL Nov 2026 297.500 put (GOOGL261127P00297500) stock quote, history, news and other vital information to help you with your stock trading...
- [GOOGL Nov 2026 277.500 call (GOOGL261125C00277500) stock price, news, quote and history](https://www.google.com/goto?url=CAESdAHEIkXX4zQ2nRa_r0Oq66YEK0xTpJWy_vK90oHaKxwo2AI6Cchqxvvr8Ui8oa6F5kqztQRrSmP2VgaTYlGihMiWDk1vyymb0ebCJHdXjQ3Vmh2l98bZ421ASu4oMBbn8SEHbaWo9pDUwmg05FNjzJhAna4H&gsessionid=QodP-sZ48yQ0SBrxE8-eGKBlVDC_1WGO_Az90Am7eXFguVnSfuJLPQ)  
  <sub>Yahoo Finance UK, 10 hours ago</sub>  
  Find the latest GOOGL Nov 2026 277.500 call (GOOGL261125C00277500) stock quote, history, news and other vital information to help you with your stock...
- [GOOGL Nov 2026 260.000 call (GOOGL261127C00260000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESdAHEIkXXM_nIS0l626IPO8CnjhUn3DnyKPzf6tJ3QpDH9-R4rk0RT4epXUkVfKoRxPiQvRys7DgoGaqiL6xXF5dmM7bwVjcUSd44WpzppmPJZdvWyGzKyL08x2xHvR565PkxpqMX2TbH-pgEi2P5mQf0z3vQ&gsessionid=QodP-sZ48yQ0SBrxE8-eGKBlVDC_1WGO_Az90Am7eXFguVnSfuJLPQ)  
  <sub>Yahoo! Finance Canada, 13 hours ago</sub>  
  Find the latest GOOGL Nov 2026 260.000 call (GOOGL261127C00260000) stock quote, history, news and other vital information to help you with your stock...
- [GOOGL Mar 2027 330.000 put (GOOGL270319P00330000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESdAHEIkXXm4Nfvu8Q32OsC3yVNL3tuQ02gqphjlSB7koLFnesVHyudeR4VomAIq1F9yJxDl4y2jslhGxnsw6VFArs1zb7H76q-ieQNlNZa51mSPcabOUzicNo3MZ4XQxL31WVMEmkyIi8n02imk_Mm-RCW2RU&gsessionid=QodP-sZ48yQ0SBrxE8-eGKBlVDC_1WGO_Az90Am7eXFguVnSfuJLPQ)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  Find the latest GOOGL Mar 2027 330.000 put (GOOGL270319P00330000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 274.18 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 282.57 (-3.0%), 50d 316.78 (-13.4%), 200d 336.13 (-18.4%); 50d below 200d
Momentum: RSI(14) 37.8 | MACD -11.762 vs signal -12.497 (histogram 0.735)
Returns: 1d +0.4% | 5d +0.6% | 1m -15.6% | 3m -20.9%
52-week range: 265.29 - 402.62 (now 6.5% of the way up)
Volatility: ATR(14) 11.46 (4.2% of price) | annualised 20d 38.5%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 3.37T
Valuation: trailing P/E 14.32 | forward P/E 17.93 | P/B 5.11 | PEG 0.94
Profitability: profit margin 50.0% | operating margin 33.3% | ROE 44.3%
Growth (YoY): revenue +24.7% | earnings -25.3%
Balance sheet: debt/equity 22.2% | free cash flow -1.16B
Risk: beta 1.23 | short interest 1.3% of float
Next earnings: 2027-02-03
```

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.40</summary>

```text
Earnings record, last 4 quarters: 1 beat, 3 missed
  2026-09-30 missed by 14% | 2026-06-30 missed by 4% | 2026-03-31 missed by 3% | 2025-12-31 beat by 4%
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: strong_buy (mean 1.38 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 11 strong buy, 43 buy, 6 hold, 0 sell, 0 strong sell
Price target: mean 395.11 (+44.1% vs last close), range 300.00 - 500.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 202,850,992 shares
Distinct insiders: 0 buying, 0 selling
(4 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

> Mixed signals: no material company‑specific news, technicals show weak momentum and low volume, fundamentals are mixed with high leverage and negative free cash flow, analyst consensus is bullish but likely priced in, insider activity is negligible, and earnings record is poor. Overall the dimensions conflict, leading to a neutral view with low conviction.

**Main reasons it gave:**
- Premarket rally driven by broader market, no company‑specific catalyst (NEWS)
- Technicals: price above 20‑day SMA but below 50‑day/200‑day SMA, low volume (TECHNICALS)
- High leverage (debt/equity 197.4%) and negative free cash flow (FUNDAMENTALS)
- Earnings record: 1 beat, 3 misses, indicating likely earnings miss (EARNINGS RECORD)

<details><summary><b>News</b> — score +0.00</summary>

- [MELI Dec 2026 1220.000 call (MELI261204C01220000) Interactive Stock Chart](https://finance.yahoo.com/quote/MELI261204C01220000/chart/)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Interactive Chart for MELI Dec 2026 1220.000 call (MELI261204C01220000), analyze all the data with a huge range of indicators.
- [MELI Nov 2026 1720.000 call (MELI261127C01720000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/MELI261127C01720000/)  
  <sub>Yahoo Finance UK, 7 hours ago</sub>  
  Find the latest MELI Nov 2026 1720.000 call (MELI261127C01720000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI Nov 2026 1855.000 call (MELI261127C01855000) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESeQHEIkXXCtDVyVT1zrY-Mzor4Yj12fBSbf_8b70kiR2uKDx9EnTWUP1EwW1ALJMlXqM5cpf9jj54fnHt0WtI79OFrlCQDFDjG_rdJ7fVBnYsGYN2ql-HdVxR-rjukK82sq_AsaRmWx9LY8a5W7-q2jt5kzhqwlIdOZA&gsessionid=xnDM32IbEi9daP306_V0gERHj7uJNg2U3DXNAfKEvmo5McD1sfBeTA)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Interactive Chart for MELI Nov 2026 1855.000 call (MELI261127C01855000), analyze all the data with a huge range of indicators.
- [MELI Nov 2026 1885.000 call (MELI261127C01885000) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXwO2822npTJIKl4HkRoNXU6iX8fusHb3NUsqa-GPJoGm_nYp8OG2iu75wLgjeFC3bicYz_FaJeLG8LieYLQNgTy8J3_WlLNx4QezcotWKeThI_hgxJh9g67gCVpkO90SbE4hIJMfFfH1yuLLtTKs0vbSkCEw&gsessionid=xnDM32IbEi9daP306_V0gERHj7uJNg2U3DXNAfKEvmo5McD1sfBeTA)  
  <sub>Yahoo Finance UK, 8 hours ago</sub>  
  Interactive chart for MELI Nov 2026 1885.000 call (MELI261127C01885000) – analyse all of the data with a huge range of indicators.
- [MELI Nov 2026 1400.000 call (MELI261127C01400000) Interactive Stock Chart](https://www.google.com/goto?url=CAESdgHEIkXXAeR3zXl69niHOUugkEyDi-I5VSAkjBSjgmIHhKmc2Rx5d-ei9qFpRRc2P72Hvi7LKjCech5PHC4_8Qk7lZgp8CT7lShQ2YmgR_dLFwsXdKxxMG9P5lmN56IcSNn2dPkEdksG2Jz_27zS8UVyhHMm1xQ&gsessionid=xnDM32IbEi9daP306_V0gERHj7uJNg2U3DXNAfKEvmo5McD1sfBeTA)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Interactive Chart for MELI Nov 2026 1400.000 call (MELI261127C01400000), analyze all the data with a huge range of indicators.
- [Why Is MercadoLibre (MELI) Stock Up in Premarket Trading Today? Market Rally](https://www.google.com/goto?url=CAESrAEBxCJF1wIivem-F4ZrqS7CKxBJIZ_piwkHyW3f65cT_1bWJCaMlLQ4ewrUSAWA2NcDca0q-RTgwrAVslCbwGSHEUdHiSiqIJ59bNolBwADiqJ_dyPmTvhJM_nv0KoXI0_tEDBA03gzAVbsdoA7VP8tsPjGPeH58sXry34pPeRB_JYkulenrMdOENIgqbc7RkF0-6y9wpjxs1V4I0aT65R01RMslmZ5Ub6txFkE&gsessionid=xnDM32IbEi9daP306_V0gERHj7uJNg2U3DXNAfKEvmo5McD1sfBeTA)  
  <sub>GuruFocus, 2 hours ago</sub>  
  MercadoLibre (MELI) stock is up 6.3% in premarket trading on Friday, Nov. 27, as of 7:15 a.m. ET, as the broader market rallies, with no company-specific...
- [MercadoLibre (MELI): Near-Term Margin Compression Masks Strong User and Credit Growth](https://www.google.com/goto?url=CAESnwEBxCJF1_x-2QuBPJK2D9ebdZ1riuVL_slmN0D2uoxem7NKrUCbij5w-bxYKRjyyooAu2cMQaSSvaoCauQNSipmTS6veqANXmhO8cJkklDodWQUSYWa8DlBU8sgdAluV1GD6yyqlNHL3Oft5fZ_I_pD1pKB3Y5rlLvuvPZHEB_4lvlpw2bpslXMJnF8g3nkkyZOpTaKA6doQ1m6lyvwNEM&gsessionid=xnDM32IbEi9daP306_V0gERHj7uJNg2U3DXNAfKEvmo5McD1sfBeTA)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Hayden Capital, an investment management firm, released its third-quarter 2026 investment letter. The letter can be downloaded here. In the third quarter,...
- [MercadoLibre (MELI) Stock Price Prediction: Testing resistance after a low-volume bounce](https://www.google.com/goto?url=CAESnQEBxCJF1w8H06iXheI868Nr2WQFScAC-MmbinouAU1z_fzmt3nqTZSZioITHQc7_2Tz_OQRBA7-_BRPMgVpN21a8CEagD8bjQTGQqWs4KUVMAznw8EiZ7cSSfMLertDxlB-j3H1wBqSKQ_85_uytLNdLlzk88OaqsOCNh660kj0Hsp0qhHLPTbKUZZthc6abzConNmn8EN7XZ6R6nBV&gsessionid=xnDM32IbEi9daP306_V0gERHj7uJNg2U3DXNAfKEvmo5McD1sfBeTA)  
  <sub>Blockchain News, 5 hours ago</sub>  
  MercadoLibre (MELI) is trading at $1,536.29 after a 3.68% 24-hour gain, with the session range stretching from $1,478.43 to $1,549.81. That puts the stock...
- [MELI Nov 2026 2160.000 put (MELI261127P02160000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXmX8PFFXOe_u46v90-uF55tG8yupbMk5nrcroCqdhL8lJamhGc1S1sV5fbj-Upcyjv9wqOloflW3wb03ujBXm0uTEHhF-P0rWl9Z2lh-zfbIj5cib_Gb4rUyAzpH47rDVYNNtKuAxHuGHgpUqVmE&gsessionid=xnDM32IbEi9daP306_V0gERHj7uJNg2U3DXNAfKEvmo5McD1sfBeTA)  
  <sub>Yahoo Finance UK, 19 hours ago</sub>  
  Find the latest MELI Nov 2026 2160.000 put (MELI261127P02160000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI Nov 2026 1710.000 call (MELI261127C01710000) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXbLF5AYYp0Hc54s4CZE0kIUfn3syfTs7Ei22RSeTZ5QIVC6BYIMDXT72RGwU3bJPLtYLlLghth1M_D56ULdy0y3vrvCxHmDWfwSfBWs1xWa664Puwb2DHCfe1lVTrfP0P7KFliEcm3KNAZiI-3-uNBKT0nIE&gsessionid=xnDM32IbEi9daP306_V0gERHj7uJNg2U3DXNAfKEvmo5McD1sfBeTA)  
  <sub>Yahoo Finance UK, 20 hours ago</sub>  
  Interactive chart for MELI Nov 2026 1710.000 call (MELI261127C01710000) – analyse all of the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 1,527.35 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 1,507.39 (+1.3%), 50d 1,679.28 (-9.0%), 200d 1,755.52 (-13.0%); 50d below 200d
Momentum: RSI(14) 47.5 | MACD -73.826 vs signal -86.100 (histogram 12.274)
Returns: 1d +4.1% | 5d +12.7% | 1m -8.7% | 3m -22.3%
52-week range: 1,355.00 - 2,295.00 (now 18.3% of the way up)
Volatility: ATR(14) 65.09 (4.3% of price) | annualised 20d 60.9%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 77.43B
Valuation: trailing P/E 40.97 | forward P/E 28.84 | P/B 9.44 | PEG 0.74
Profitability: profit margin 4.9% | operating margin 7.4% | ROE 26.2%
Growth (YoY): revenue +45.1% | earnings +6.3%
Balance sheet: debt/equity 197.4% | free cash flow -2.57B
Risk: beta 1.39 | short interest 2.4% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.10</summary>

```text
Earnings record, last 4 quarters: 1 beat, 3 missed
  2026-09-30 missed by 8% | 2026-06-30 beat by 4% | 2026-03-31 missed by 7% | 2025-12-31 missed by 6%
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
Consensus: buy (mean 1.52 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 5 strong buy, 16 buy, 4 hold, 0 sell, 0 strong sell
Price target: mean 2,152.76 (+40.9% vs last close), range 1,600.00 - 2,700.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 3,535,594 shares
Distinct insiders: 1 buying, 0 selling
Open-market purchases — insiders spending their own money:
  - 2026-06-11 MELAMUD MARCELO (Officer): 124 shares, 200.00K
(4 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

- [Elbit Systems Ltd](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b099793132f452a94346e3579a4ec0d&url=https%3a%2f%2f247wallst.com%2fcompanies%2feslt%2fprice-prediction%2f&c=13985047916096011344&mkt=en-us)  
  <sub>24/7 Wall St, 30h ago</sub>  
  Looking ahead to 2030, our model projects ESLT could trade at an average price of $1,068.32, with a potential range between $801.24 and $1,335.40. This represents a potential 61.4% return from today’s ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 684.74 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 702.42 (-2.5%), 50d 715.52 (-4.3%), 200d 785.12 (-12.8%); 50d below 200d
Momentum: RSI(14) 46.4 | MACD -16.173 vs signal -12.024 (histogram -4.149)
Returns: 1d +3.4% | 5d +0.4% | 1m -12.1% | 3m -3.4%
52-week range: 454.95 - 1,014.33 (now 41.1% of the way up)
Volatility: ATR(14) 26.78 (3.9% of price) | annualised 20d 63.0%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 32.10B
Valuation: trailing P/E 48.26 | forward P/E 33.61 | P/B 7.02 | PEG n/a
Profitability: profit margin 7.7% | operating margin 9.7% | ROE 15.8%
Growth (YoY): revenue +17.2% | earnings +32.1%
Balance sheet: debt/equity 22.6% | free cash flow 362.77M
Risk: beta -0.40 | short interest 0.9% of float
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
Price target: mean 837.33 (+22.3% vs last close), range 739.00 - 935.00
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
Net: +0 shares | insiders hold 19,308,776 shares
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

- [HDB: SEC Form 6-K filed by HDFC Bank Limited](https://quantisnow.com/insight/sec-form-6-k-filed-by-hdfc-bank-limited-6808048)  
  <sub>Quantisnow, 4 hours ago</sub>  
  HDFC Bank board approved re-appointment of Harsh Kumar Bhanwala as independent director for five years, from Jan 25, 2027, pending… Free alerts on HDB.
- [HDBank raises bond interest rate to 9.3% per year](https://theinvestor.vn/hdbank-raises-bond-interest-rate-to-93-per-year-d20534.html)  
  <sub>Theinvestor, 9 hours ago</sub>  
  HDBank has issued an eight-year bond tranche carrying a fixed interest rate of 9.3% per year, the highest in five years, as the lender steps up credit...
- [Tiger Pacific Capital LP Buys 1,363,983 Shares of HDFC Bank Limited $HDB](https://www.google.com/goto?url=CAESvgEBxCJF14uHNs8rMrfJMYv3eBJppGDB68d4WCeSf2lKEanWM2u9FEczdd-gEdTPRAbJLq1HLiU1jYSJLMqTrgzNxHN4Ihl6uFbyRU165msqdWyoyCFaimjmjDVy140AhLD---ub7OMCV9CVg64FUtdZ3OvFJqmr_N7w7uqev3byv-bWMlaTDxO0sWAhvZ8GgVsIrPaQ56vjx0x0C_P0PzaLLuIZQL5uwNlHdsjlUDhx_S4v8Knznojz6YhSWVom&gsessionid=Nc1Hz6kGRo-Mr_NwjelGaELF50-Nnl9Bubv7aIg6Grc7QulaT5X_qw)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Tiger Pacific Capital LP bought a new stake in HDFC Bank Limited (NYSE:HDB - Free Report) in the third quarter, according to the company in its most recent...
- [A director with 40 years of experience is up for another term at HDFC Bank (HDB), pending shareholder approval.](https://www.google.com/goto?url=CAESpwEBxCJF18xh2E3S8a1wgrBMf-3xovf7uU_r6nRjsxgGpsrggRKnW-XW-C4kcIyE5W2KkufPM2kRVDPHExUMu_w3K2jF0XTMWYBBCP1XzeFkuMM8B1uvN9R-pdTmNZh0ohGxG7Fc0E1QOOhyew96OSojIFzXf3jJrcK7UNXpGXJCrqd0ba82JcN6fp4j-DP6CHvK7S4c_0hzVw1f7SpMGpz9p2xC0xhu0g&gsessionid=Nc1Hz6kGRo-Mr_NwjelGaELF50-Nnl9Bubv7aIg6Grc7QulaT5X_qw)  
  <sub>Stock Titan, 4 hours ago</sub>  
  HDFC Bank's Board approved the re-appointment of Dr. (Mr.) Harsh Kumar Bhanwala as an Independent Director, subject to shareholder approval.
- [Billionaire Nguyen Thi Phuong Thao's mark on the 30-year history of Vietnam's securities industry.](https://www.google.com/goto?url=CAESqwEBxCJF19eigxA7XpTmnRNKj_sBajBT-sxgK1eE46-Vkrt6wnR6udd3Jph--d2BGfY2zS_yU7F20WnNnimZruOhmMgVlYEkZKitNqXkxfZe9RszamYAUduNbjWf59ixSN4eD0Xe83uPR8cMdURdUvVjokgsFwoscfi5DDsVeTTnD8CPJuXMD2HD5yQTjv5beb1TB36rgWfJynS7wS4BN0pQKY2jxrB7SHHdBCs&gsessionid=Nc1Hz6kGRo-Mr_NwjelGaELF50-Nnl9Bubv7aIg6Grc7QulaT5X_qw)  
  <sub>Vietnam.vn, 4 hours ago</sub>  
  During the 30 years of development of Vietnam's securities industry, billionaire Nguyen Thi Phuong Thao has left a profound mark through the development of...
- [HDFC Group stocks: How are HDFC Bank, HDB Financial, AMC and Life Insurance shares performing?](https://www.google.com/goto?url=CAES0QEBxCJF1ztx5HtdeO3qVPAGRYPeA1eKj5mtLDuKsxw2tUtCQBQ_NQF_yJ5DyNiBAsx3lAg40Vtid7FoQ2PRnrFx28lJlgWDcNbZDO78kDaKBHGgRIsSDaJnUTcev7rMIhXArqXh5Yw89x9NwvporRq47159Mk0PjHowI5ZVRZn9WXeEjSHISp8lOucxSBNnYOWbjEYW3PmnNG65c2d8UDxwtF-AK1eIW0ajxhrhd3KplZM7N8FqxeZP9N8F4RVM0XkWqEQ0hhOP9JmBZOhNkYJqtA&gsessionid=Nc1Hz6kGRo-Mr_NwjelGaELF50-Nnl9Bubv7aIg6Grc7QulaT5X_qw)  
  <sub>Upstox, 9 hours ago</sub>  
  HDFC Bank had hit its 52-week high of ₹1017.50 per share on December 1, 2025, and a year's low of 669.20 on October 28, 2026.
- [HDB Financial Services passes postal ballot for three director appointments](https://www.google.com/goto?url=CAESrgEBxCJF1ybkn-s1LqN_RUicj6VWkYk47KPWcK5kzvHr6po4RPEG5v4B95-28sg7RIlwA9TwrumwbElD-VcYpfyu06NRx4D5dyzdgXcgfqjVUFsV1MKuHVuk5Z0ko50-FMxPZCSKfQ0Z2Hq7AYM5Xo6wpWODg0ednbWjjZxQYPjxw8hBNc2XTVxYlL6fPcKwjyUc9YxWdmoazYooSCWG3-ngCUaUjpb6sTK1i1BtMwo&gsessionid=Nc1Hz6kGRo-Mr_NwjelGaELF50-Nnl9Bubv7aIg6Grc7QulaT5X_qw)  
  <sub>scanx.trade, 24 hours ago</sub>  
  HDB Financial Services passed three postal ballot resolutions on November 26, 2026. Jayesh Chakravarthi and Arundhati Mech reappointed as Independent...
- [HDBank Global Capital Summit 2026: Bridging global expertise, capital with Vietnam's development ambitions](https://www.google.com/goto?url=CAEStgEBxCJF14sqPzum0i6iN24XUT7O9uTDMOo6eos62FD-G0rbNb7JJ0KRjXvESt-VkIFE4G08o8etxzSoC6Zn-2zj7_fw_nCizi0m3JLMI9_PxEKcljfEVdOjiEWggfB8BV-VmOIKsUF1I1Uufb6I-OMULe4V5_3s3eTtdY4NwKUQzkZAZ_qdl-U5x1ae8HrixkFPJs2XBGJbkVO8Xt0rDs-ZlNDmLJAEuMpso0IR0sxiFaK_oMc1Ww&gsessionid=Nc1Hz6kGRo-Mr_NwjelGaELF50-Nnl9Bubv7aIg6Grc7QulaT5X_qw)  
  <sub>SME & Entrepreneurship Magazine, 4 hours ago</sub>  
  Under the theme “Global Capital – Vietnam's Next Horizon”, the summit brought together policymakers, financial experts, investors and business leaders to...
- [HDFC Bank Board Approves Conditional Reappointment of Harsh Kumar Bhanwala](https://www.google.com/goto?url=CAESuQEBxCJF14VL0bNEwl_IrkTmoZdbGzIpSu6yJTysMi941w713A21DVWaTQ5u2Ou80GKp3XnKYL6ALrOqGl4SwvjDAHXXhwII1mIqbiLA4h3S3kZWz5NtRawmFpHzv0nqm4tP8S9a1lkhclKR50v3ubYVZ6rW3vAqwopHUBP1sv0zDMsPRU0Za0XHvHgg3i_8gN-eI5bZezNdwVGxtdZeZ5Of8qtTC3BN1esCG_CM_WVGnhdKkLy1irt4FA&gsessionid=Nc1Hz6kGRo-Mr_NwjelGaELF50-Nnl9Bubv7aIg6Grc7QulaT5X_qw)  
  <sub>TipRanks, 3 hours ago</sub>  
  An announcement from Hdfc Bank ( ($HDB) ) is now available. At its meeting on November 25, 2026, HDFC Bank's board approved the reappointment of Dr. (Mr.)...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 28.35 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 25.76 (+10.0%), 50d 23.86 (+18.8%), 200d 25.14 (+12.8%); 50d below 200d
Momentum: RSI(14) 79.9 | MACD 1.267 vs signal 1.046 (histogram 0.221)
Returns: 1d +0.0% | 5d +8.0% | 1m +31.6% | 3m +22.8%
52-week range: 21.36 - 36.82 (now 45.2% of the way up)
Volatility: ATR(14) 0.67 (2.4% of price) | annualised 20d 27.3%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 145.85B
Valuation: trailing P/E 18.29 | forward P/E 20.47 | P/B 11.29 | PEG n/a
Profitability: profit margin 26.5% | operating margin 36.6% | ROE 11.0%
Growth (YoY): revenue +80.8% | earnings +21.3%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.39 | short interest 0.9% of float
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
Price target: mean 31.05 (+9.5% vs last close), range 26.20 - 33.00
Recent rating changes:
  - 2024-07-22 JP Morgan: down, Overweight -> Neutral
  - 2019-09-09 Bernstein: down, Outperform -> Market Perform
  - 2019-06-11 Nomura: down, Buy -> Neutral
  - 2017-03-21 Morgan Stanley: down, Overweight -> Equal-Weight
  - 2016-09-14 Goldman Sachs: main, ? -> Buy
  - 2015-03-11 Societe Generale: init, ? -> Buy
Institutional ownership: 14.1%
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

- [JPM Nov 2026 290.000 call (JPM261127C00290000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/JPM261127C00290000/chart/)  
  <sub>Yahoo! Finance Canada, 8 hours ago</sub>  
  Interactive Chart for JPM Nov 2026 290.000 call (JPM261127C00290000), analyze all the data with a huge range of indicators.
- [JPM Nov 2026 215.000 call (JPM261127C00215000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/JPM261127C00215000/)  
  <sub>Yahoo! Finance Canada, 10 hours ago</sub>  
  Find the latest JPM Nov 2026 215.000 call (JPM261127C00215000) stock quote, history, news and other vital information to help you with your stock trading...
- [JPM Nov 2026 315.000 put (JPM261127P00315000) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESdwHEIkXXvOGX2dSZ01aaKcUXvebd5Ykb1fPx_egqGCdi7HVImVMPw8TU2GHtI-2A82Xe57HwkV5loIVWf4K-lCOdLbzlm52F4NC9rOq3SLDO22jVnGtY1e3OK3_6ZuO60y-xLqPtPKccUKoLAFG9tOtWaf1qn1Lq&gsessionid=RecqLmoENE899svtrTOyS1Bz7F5KaKtp5FpkG8lTnPkh1JolHfwSGQ)  
  <sub>Yahoo! Finance Canada, 10 hours ago</sub>  
  Interactive Chart for JPM Nov 2026 315.000 put (JPM261127P00315000), analyze all the data with a huge range of indicators.
- [Best Bank Stocks To Watch Now - November 26th](https://www.google.com/goto?url=CAESoQEBxCJF1yevjnHZnRTJtET3NE4lePA0C4E6FVI1HcEXYJEiSFSNVvMmB3HmZauyViP2pC-o5osHhya8Z1xq_Lh_qYyiQfLqMaIay9gLLd2CWxFUenPITWYsIcEFKpAKFp3oOc02hFWD2BjOxrWaKvIhI4ZgLbGRg54EkVyQtUP0IfTjcAL4Fi9Z_LMsYTnba-E0YPGFUbSBpApRlkBnAKrfFw&gsessionid=RecqLmoENE899svtrTOyS1Bz7F5KaKtp5FpkG8lTnPkh1JolHfwSGQ)  
  <sub>MarketBeat, 21 hours ago</sub>  
  JPMorgan Chase & Co., Bank of America, Citigroup, Charles Schwab, and Wells Fargo & Company are the five Bank stocks to watch today, according to...
- [JPM Nov 2026 365.000 call (JPM261127C00365000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScQHEIkXXkOy07lbXf3gmeoNMz98eHLd-nSp-6WPuqk1lZ2YEkBVA4gISOp-YJbYUAceJwr8dX_FTn7ByjxxDP79N4XBJV93OfNyW51BYajlpiOc82FGDkQ3BoxbUk4V13q8YaGCA0TWe-p10HNjfJ0aw&gsessionid=RecqLmoENE899svtrTOyS1Bz7F5KaKtp5FpkG8lTnPkh1JolHfwSGQ)  
  <sub>Yahoo Finance UK, 11 hours ago</sub>  
  Find the latest JPM Nov 2026 365.000 call (JPM261127C00365000) stock quote, history, news and other vital information to help you with your stock trading...
- [JPM Nov 2026 210.000 call (JPM261127C00210000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScQHEIkXXdORK2TmXa8ecwB9NfwI0a2Zzc718zAOjrZcJL94WZ9LAOdbaGU5c2EqHUcbcW9viqEs5hVoAM7KLICc_uZmbDbODBbiPsoNL0ej3cxMMTO4bVAh_BF1oFB4NwuxP7U8m3wo3XkYz2563Hb2O&gsessionid=RecqLmoENE899svtrTOyS1Bz7F5KaKtp5FpkG8lTnPkh1JolHfwSGQ)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Find the latest JPM Nov 2026 210.000 call (JPM261127C00210000) stock quote, history, news and other vital information to help you with your stock trading...
- [JPM Sep 2027 370.000 call (JPM270917C00370000) interactive stock chart](https://www.google.com/goto?url=CAESdwHEIkXXEGMFK6oUFsMV8KQIknCFTIbeTpFdDuKRnqlte7sGADPuY4GP9j1F8IzecgaPtBVbQ9cAqGOCAeOdVMpU9Sl1-DAkYU86e0jVoUYJlNrE4YLJzK-0NaDlJBmgFtnYWg0ZaWfxC9FO7N1cbw5Gc7wmGOLo&gsessionid=RecqLmoENE899svtrTOyS1Bz7F5KaKtp5FpkG8lTnPkh1JolHfwSGQ)  
  <sub>Yahoo Finance UK, 20 hours ago</sub>  
  Interactive chart for JPM Sep 2027 370.000 call (JPM270917C00370000) – analyse all of the data with a huge range of indicators.
- [JPM Nov 2026 295.000 call (JPM261127C00295000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScQHEIkXXe7nS--0tq09LdHA5gaNF9kZtNd0xgIYxmY3WdmWkXSqXVAUNQlwatDntnhGdtZRmfs5EUkjZeeAL0WJ0PmVujo1tFlHkegh3ZNm6RJPEDkCNNsziN0XfKpGwk6lPdEuKUjZlbYjPKfZ8eRG_&gsessionid=RecqLmoENE899svtrTOyS1Bz7F5KaKtp5FpkG8lTnPkh1JolHfwSGQ)  
  <sub>Yahoo Finance UK, 11 hours ago</sub>  
  Find the latest JPM Nov 2026 295.000 call (JPM261127C00295000) stock quote, history, news and other vital information to help you with your stock trading...
- [JPM Nov 2026 305.000 put (JPM261127P00305000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScQHEIkXXTxZEVG13csbQnDKHFYPZP93HSzCVr2J43Z4laLsz9e8--nnB2rQiRyERLDGwWbyquuzevy5qdZdL-4ked8orFcQJs5F4vqpGozG5jP_WzCd_wTCUXBOgmmheW7EZOpUvEMSSh0bOS_biIpWy&gsessionid=RecqLmoENE899svtrTOyS1Bz7F5KaKtp5FpkG8lTnPkh1JolHfwSGQ)  
  <sub>Yahoo Finance UK, 11 hours ago</sub>  
  Find the latest JPM Nov 2026 305.000 put (JPM261127P00305000) stock quote, history, news and other vital information to help you with your stock trading and...
- [JPM Feb 2027 290.000 put (JPM270219P00290000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScQHEIkXXR5iDwxmvWLdt7Ki-PvdHftebIQg52ZtycaF8Dc8YhTe9OHOOwBkz4y_zVskBLsTRaNjOqkqFtUlgYx5JP5q8xiAoR0ud7B30Ldv93W-OrCMB1ZTnt-F3uvxo7wvpuVlsFcU3c9_PX-yKatAg&gsessionid=RecqLmoENE899svtrTOyS1Bz7F5KaKtp5FpkG8lTnPkh1JolHfwSGQ)  
  <sub>Yahoo Finance UK, 22 hours ago</sub>  
  Find the latest JPM Feb 2027 290.000 put (JPM270219P00290000) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 322.77 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 332.62 (-3.0%), 50d 334.80 (-3.6%), 200d 325.19 (-0.7%); 50d above 200d
Momentum: RSI(14) 43.1 | MACD -5.639 vs signal -3.735 (histogram -1.904)
Returns: 1d +1.9% | 5d +0.8% | 1m -4.9% | 3m -9.7%
52-week range: 282.84 - 365.18 (now 48.5% of the way up)
Volatility: ATR(14) 7.93 (2.5% of price) | annualised 20d 32.2%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 857.14B
Valuation: trailing P/E 13.54 | forward P/E 12.62 | P/B 2.44 | PEG 1.32
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
Price target: mean 373.65 (+15.8% vs last close), range 312.00 - 425.00
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
Last 180 days: bought 1,583 shares in 6 transaction(s) | sold 10,467 shares in 3
Net: -8,884 shares (-0.1% of insider holdings) | insiders hold 11,180,116 shares
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

- [Is Most-Watched Stock Eli Lilly and Company (LLY) Worth Betting on Now?](https://finance.yahoo.com/markets/stocks/articles/most-watched-stock-eli-lilly-130005156.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Recently, Zacks.com users have been paying close attention to Lilly (LLY). This makes it worthwhile to examine what the stock has in store.
- [Eli Lilly Stock Is Up 64% Since April. Is It Time to Take Profits?](https://247wallst.com/investing/2026/11/26/eli-lilly-stock-is-up-64-since-april-is-it-time-to-take-profits/)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  Eli Lilly (LLY) volume jumped 53% last quarter while realized prices fell 15%, so growth now depends on volume outrunning price cuts.
- [LLY Dec 2026 1210.000 put (LLY261224P01210000) interactive stock chart](https://www.google.com/goto?url=CAESdwHEIkXX_xx4XMSgzllv1TlbMlwjv1yiNC13-Ss5kITxHlc5TT4r0FVhOaD_ILXcVjtdJO65ixspj0v4TX4twkycy47_TqxLHeP881uq2jh5-G1spW6cNRzojTC3BwaWdZtZHXLl9Qf5C77rnM02rU9AZDlR8XF5&gsessionid=l-fBmDNROD-TkAFS_2jY9ZiI7CfEY1mJEV4mSBHAAQhk36QmqWqr8Q)  
  <sub>Yahoo Finance UK, 8 hours ago</sub>  
  Interactive chart for LLY Dec 2026 1210.000 put (LLY261224P01210000) – analyse all of the data with a huge range of indicators.
- [LLY Feb 2027 1960.000 call (LLY270219C01960000) interactive stock chart](https://www.google.com/goto?url=CAESdwHEIkXXfu-AZ99_GguU9MTGTz2yf3nQPCAjosbDtMLG4G6-lYbRxqKSB0dhfDBkhpqJFYNtXTvAYwP39kFW3Pn2sE7uS6z6ehSeJn9OgMw2u7pDwpW_dpqorvRpO9N_yUnnBy3agBOCNu-CObf-XKXFOF53ToZ6&gsessionid=l-fBmDNROD-TkAFS_2jY9ZiI7CfEY1mJEV4mSBHAAQhk36QmqWqr8Q)  
  <sub>Yahoo Finance UK, 10 hours ago</sub>  
  Interactive chart for LLY Feb 2027 1960.000 call (LLY270219C01960000) – analyse all of the data with a huge range of indicators.
- [LLY Dec 2026 1460.000 put (LLY261204P01460000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScQHEIkXXFlceMvMZ0uTMX4Rq7TThcfbYyBLx9RWPlheiCAMq1d4exYlItv4KEHP1ChbD2MXIB3CYlFWtIeM4mO8-20wBYkTB0d9sADoix3Cl4AwICZKxR-1UrH_5jtlnIy_X1QWk6nbwzzzYq7DQSR0V&gsessionid=l-fBmDNROD-TkAFS_2jY9ZiI7CfEY1mJEV4mSBHAAQhk36QmqWqr8Q)  
  <sub>Yahoo Finance UK, 12 hours ago</sub>  
  Find the latest LLY Dec 2026 1460.000 put (LLY261204P01460000) stock quote, history, news and other vital information to help you with your stock trading...
- [LLY Dec 2026 1370.000 put (LLY261231P01370000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScQHEIkXXQjCChL5zUyb-9MCckATNm-sCstpdMWDC6P_gOjCZIfqPjNGrIjlEmxAzootdFqHkZ7Hv5dM9FgZPcCLVpjg4tYHuFBsIKk4ZZ2EYMHFn-nKni8Nd9oklnD4JSQ0Ei4N5lOHhjkqwyQndw1D5&gsessionid=l-fBmDNROD-TkAFS_2jY9ZiI7CfEY1mJEV4mSBHAAQhk36QmqWqr8Q)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Find the latest LLY Dec 2026 1370.000 put (LLY261231P01370000) stock quote, history, news and other vital information to help you with your stock trading...
- [LLY Dec 2026 1660.000 call (LLY261204C01660000) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESdwHEIkXX4dHsmHGUOjDrXWEbS_BOKuERdcOs7HYnvuRT1zzxvjqUYjf_rMg4qzhZL3zD9-lY86mFxq5x8pj7rLc43VNB-WhmjbLnOKiymYLLdwv3S7QnThsQ6yLzmhmVerVPxNPYUjV6H70SD4r3VJKMKgsUfxb6&gsessionid=l-fBmDNROD-TkAFS_2jY9ZiI7CfEY1mJEV4mSBHAAQhk36QmqWqr8Q)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  Interactive Chart for LLY Dec 2026 1660.000 call (LLY261204C01660000), analyze all the data with a huge range of indicators.
- [LLY Mar 2027 1300.000 put (LLY270319P01300000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScQHEIkXXo043SakK9bWcCV8qJWap3GvCgOCI3NVew5AINf7ST9enTvL7DH8jQORSAZ2JGJqkE4rdA6RFnju6OJ9zdDoCgmINTbrb-iRahOquUUuXmTkWYAJKme_YdTqFveq-OjXRO1J2Y9u86I1k9a_W&gsessionid=l-fBmDNROD-TkAFS_2jY9ZiI7CfEY1mJEV4mSBHAAQhk36QmqWqr8Q)  
  <sub>Yahoo Finance Singapore, 16 hours ago</sub>  
  Find the latest LLY Mar 2027 1300.000 put (LLY270319P01300000) stock quote, history, news and other vital information to help you with your stock trading...
- [LLY Dec 2026 1940.000 call (LLY261204C01940000) interactive stock chart](https://www.google.com/goto?url=CAESdwHEIkXXwIrdOmbF7P6BsXBv1VOia4a1zjXdkHIYp0mqxJshzkJaofWMAnH8CqKCliptX3WD4L0vGJIxAYbUlLckTb2UJpfsautwzANU38KlXhVkEOMLQPsFBkA2Nmz_F6CZGQEMz1mUnXqBJJTWi2092GteyTp5&gsessionid=l-fBmDNROD-TkAFS_2jY9ZiI7CfEY1mJEV4mSBHAAQhk36QmqWqr8Q)  
  <sub>Yahoo Finance UK, 20 hours ago</sub>  
  Interactive chart for LLY Dec 2026 1940.000 call (LLY261204C01940000) – analyse all of the data with a huge range of indicators.
- [LLY Dec 2026 1110.000 put (LLY261231P01110000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScQHEIkXX_c-_Gkju5xnr2t-pFk2ipQLYqRtq8B9DRpB1f_LujXma3tDbUPP6gAvy4DDdvBOpBPgKnnJYRMjyFutuM3pw8hDp17j_kvy5XE6qNoh5qg-l1y3uAzwKGS3qUuMFTO0g6VdSPsqe1Gm51AcJ&gsessionid=l-fBmDNROD-TkAFS_2jY9ZiI7CfEY1mJEV4mSBHAAQhk36QmqWqr8Q)  
  <sub>Yahoo Finance UK, 24 hours ago</sub>  
  Find the latest LLY Dec 2026 1110.000 put (LLY261231P01110000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,397.30 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 1,400.84 (-0.3%), 50d 1,286.86 (+8.6%), 200d 1,124.99 (+24.2%); 50d above 200d
Momentum: RSI(14) 57.0 | MACD 26.055 vs signal 35.364 (histogram -9.309)
Returns: 1d +0.4% | 5d +3.4% | 1m +8.5% | 3m +19.0%
52-week range: 851.21 - 1,443.50 (now 92.2% of the way up)
Volatility: ATR(14) 40.95 (2.9% of price) | annualised 20d 31.1%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.24T
Valuation: trailing P/E 45.35 | forward P/E 27.47 | P/B 30.92 | PEG 1.25
Profitability: profit margin 31.9% | operating margin 51.3% | ROE 86.0%
Growth (YoY): revenue +38.6% | earnings +16.3%
Balance sheet: debt/equity 122.9% | free cash flow 9.34B
Risk: beta 0.39 | short interest 0.8% of float
Next earnings: 2027-02-03
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
Price target: mean 1,470.06 (+5.2% vs last close), range 940.00 - 1,700.00
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
Last 180 days: bought 39,858 shares in 43 transaction(s) | sold 297,387 shares in 8
Net: -257,529 shares (-13.0% of insider holdings) | insiders hold 1,728,045 shares
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

### Nvidia (NVDA) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Nvidia stock is still paying the price for the Jensen Huang CEO drama](https://finance.yahoo.com/markets/stocks/article/nvidia-stock-is-still-paying-the-price-for-the-jensen-huang-ceo-drama-124902053.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Nvidia's (NVDA) stock remains damaged goods despite CEO Jensen Huang being back at headquarters in trademark loafers. "It's been a traumatic situation for...
- [What's Next For Nvidia Stock - Wall Street Weighs](https://www.benzinga.com/markets/tech/26/11/63668435/whats-next-for-nvidia-stock-wall-street-weighs)  
  <sub>Benzinga, 2 hours ago</sub>  
  NVIDIA stock rose more than 4% in Friday premarket trading as tech stocks rebounded, even as upcoming congressional hearings over CEO Jensen Huang's return...
- [The Decline in Nvidia Stock Was Equal to 8% of the U.S. GDP. How Vital Is NVDA to the U.S. Economy?](https://www.google.com/goto?url=CAESxgEBxCJF13Ca5CGRrygDkt_CMxENjnFImRPt1s9EVwv3gx5NgznicLbifTmofTbaLui4UJYnMcXPm-kz3s8zkJT4ZY0NHyKuNGZD9LZMzoyESgZy5uHJkWeKkd1zzDySeUm4f1svqRj-EocbsoyFw8CNdN47le5_EX9aaTTctwDliMtYMnQ0KCcVfCHzctMSY47m0JRQTKZ3PQiviZGZZyB2v0q10DzMOKDjFaM5hCzD723jwn1ynqVk1c-T29YDVWLROtuGlNA&gsessionid=kLfkyD-y0oMypnKptUgP7V04SamH-wdpAPym2thU4n4TQyDHMgQCew)  
  <sub>Barchart.com, 42 minutes ago</sub>  
  Trillions of dollars in lost value hurt NVDA stock shareholders significantly.
- [Nvidia Stock Rises. It’s Finding a New Floor With Huang 2.0.](https://www.google.com/goto?url=CAESfQHEIkXX4gLWZS64mTohuIoNiNSg48_ohHm288N99n9zcdee-yGYD81OYB-NC-Xytl5T5aXKmeEGqF5OzUoP0-qskmybVH9ur-TNpbxUNGJ6gIfbwBXE8PhIDX_v2DDg1Z2Cm3NzPCZzyFGMX9KNS_fXx1-JcvSHLGCefceV&gsessionid=kLfkyD-y0oMypnKptUgP7V04SamH-wdpAPym2thU4n4TQyDHMgQCew)  
  <sub>Barron's, 1 hour ago</sub>  
  stock might finally be stabilizing. Yes it is early days under the renewed mandate of CEO Jensen Huang but a cheap valuation and the implicit backing of the...
- [Is Nvidia a Screaming Buy or a Value Trap?](https://www.google.com/goto?url=CAESjwEBxCJF1zfA5GVEku8uvuDw6nC1m8lPAlAwSGjsXcqDAk6W9-uYTh2E4vnfdmPIE9AXQMdOaVDWAP-Yshgj99Uv96nWjosfKEhfw2eekyST7bTm19TGI5Wv4hsrMdwgZyvlDxBMkdvFasxrUzboKouTUpR2eha3bykGZ6WQkG_FXGOQkFGV6n5ioRP5mhRkAQ&gsessionid=kLfkyD-y0oMypnKptUgP7V04SamH-wdpAPym2thU4n4TQyDHMgQCew)  
  <sub>The Motley Fool, 2 hours ago</sub>  
  Nvidia (NVDA -3.91%) stock has raced higher during most of the artificial intelligence (AI) boom, and this is thanks to the company's leading position in...
- [Nvidia Stock Rises Nearly 4% Premarket as AI Shares Rebound on Black Friday: What’s Driving NVDA?](https://www.google.com/goto?url=CAESxgEBxCJF18iWAaReEUiXfM-R1fBSPZ4JR2rF_DPrJ0r-MygZ9zTQ56j_Ewkr2WQ0yMdtnCpv9N7m7VHkBwReKESELstQb6HDKt3cGENMNfgnUrrXQtOcVTmsUCIXZOPRj_LFPkLM2iEBhvsNcHMoelxiCwXsddZTBSIgtUclji_HxD1FGzgJgyffkgL_F3KRpvnsIexdL6ptprvFJDCUyN_8jvxjARkL-dLWUdgG90didwXi1M9dzmXq08LS4HQVdXC22k1s5K0&gsessionid=kLfkyD-y0oMypnKptUgP7V04SamH-wdpAPym2thU4n4TQyDHMgQCew)  
  <sub>Coinpedia, 1 hour ago</sub>  
  Nvidia stock rises nearly 4% premarket on Black Friday as AI shares rebound. Explore Jensen Huang's return and latest news on NVDA shares.
- [Nvidia gains premarket as stock heads for end to volatile week (NVDA:NASDAQ)](https://www.google.com/goto?url=CAESnwEBxCJF17kcM7oNBSyC1moyHpW-ldGFPfxT6kxyA4YZmG9aKe-04n0UIt3y5mSKCCWub8qj76CKjCWMgBM29UdnaUgrZZbL5SOpWr8NEPK__D9iCeCXw8C21uWYfwrGcHEjLRXm13Xhz93uJ5PUs9Sm62H_gAs3-opYAmjCwffiF0_ChxHkVe2tJxzLgrblcdjPmgZQN4Iguvs0EvkwzKU&gsessionid=kLfkyD-y0oMypnKptUgP7V04SamH-wdpAPym2thU4n4TQyDHMgQCew)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Nvidia (NVDA) shares rose 4% before the opening bell of a shortened trading session Friday. But the gains are offering little evidence that the chipmaker...
- [NVIDIA Corporation (NVDA) stock price, news, quote and history](https://www.google.com/goto?url=CAESYwHEIkXX33n2Ko76H5-R_1f37JAZq75jPJxZGr_Flq94824sdj8LEt4Z-24zXsmNH8M0coahmrF4awGnx0L87dIgH_sohQRzfT2PAnIVyLqRG17XR0s-OkPFohO577psIPg8Cw&gsessionid=kLfkyD-y0oMypnKptUgP7V04SamH-wdpAPym2thU4n4TQyDHMgQCew)  
  <sub>Yahoo Finance UK, 15 hours ago</sub>  
  NVIDIA Corporation (NVDA) · -1.10% · -29.23% · -30.66% · -19.95% · -16.04% · 356.94% · 341,157.15%. Key events. Baseline. Advanced chart. Loading...
- [Nvidia Forecast $130 Billion in Revenue and Added $150 Billion to Its Buyback. Should You Buy the Stock?](https://www.google.com/goto?url=CAES0QEBxCJF1-Q6SDOf9L4lWYC9QmFFHGAzhT04n81eD11Shm_d8cnHcIsDpZEFopqSWpq2i9azZVG-2ENV009wK1jRSnu-6FW9Su6z3Ygo1-o5V1QuOPcpEtRCjEMaxbIpsJrrJ0R8Ai5-NKaDXAdHyzsroeqbCbrb3-r_B8kMBII9T3KRkk1RJ4sD-IbfFZLC7cgBE32MxZCnlPK-bwSVNLN28Zud0xx_zx4muvtVPjqp4Z-02uQWp_rpE54ET7qqwnceof6yay0zdDEpSd4x_B86GQ&gsessionid=kLfkyD-y0oMypnKptUgP7V04SamH-wdpAPym2thU4n4TQyDHMgQCew)  
  <sub>The Motley Fool, 5 hours ago</sub>  
  Nvidia (NVDA -3.91%) has a handful of problems right now. Although its chief executive officer, Jensen Huang, is back in his former position,...
- [SanDisk Stock Hits Death Cross Despite Nvidia AI Breakthrough - SanDisk (NASDAQ:SNDK)](https://www.google.com/goto?url=CAESlQEBxCJF19T5PPwoEmTMrJ2crq2yCWZwQ1favAPu2poMBKfB96KBlPYPRLRODUD7Rlt1kR5l8WD7AQDRzEhz2sIhMA2XQKr6LXvgCWz9h1Sc-UkgDWxKamjE6jrFjz4Uf207cBsgOzRJLAMHDwIQbMFRn5HalcaMgLnFXamXwR-EppyaXSr1tsD9v4G2EwoiPzKgVWkcnw&gsessionid=kLfkyD-y0oMypnKptUgP7V04SamH-wdpAPym2thU4n4TQyDHMgQCew)  
  <sub>Benzinga, 1 hour ago</sub>  
  Tokyo-based semiconductor manufacturer Kioxia announced a new collaboration with Nvidia (NASDAQ:NVDA) on Thursday, Nov. 26, which could have significant...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 146.96 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 169.14 (-13.1%), 50d 202.21 (-27.3%), 200d 202.66 (-27.5%); 50d below 200d
Momentum: RSI(14) 36.7 | MACD -16.641 vs signal -16.324 (histogram -0.317)
Returns: 1d -1.6% | 5d +0.7% | 1m -31.8% | 3m -32.4%
52-week range: 125.53 - 239.24 (now 18.8% of the way up)
Volatility: ATR(14) 12.81 (8.7% of price) | annualised 20d 138.0%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 3.55T
Valuation: trailing P/E 15.78 | forward P/E 8.85 | P/B 13.28 | PEG 0.15
Profitability: profit margin 62.5% | operating margin 66.1% | ROE 117.4%
Growth (YoY): revenue +103.2% | earnings +107.7%
Balance sheet: debt/equity 14.3% | free cash flow 99.24B
Risk: beta 2.25 | short interest 1.3% of float
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
Consensus: buy (mean 1.67 on a 1=strong buy to 5=strong sell scale, 59 analysts)
Ratings: 10 strong buy, 39 buy, 12 hold, 2 sell, 0 strong sell
Price target: mean 242.43 (+65.0% vs last close), range 130.00 - 425.00
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
Last 180 days: bought 2,613,243 shares in 18 transaction(s) | sold 6,228,325 shares in 10
Net: -3,615,082 shares (-0.4% of insider holdings) | insiders hold 972,918,080 shares
Distinct insiders: 0 buying, 3 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-11-19 TETER TIMOTHY S (General Counsel): 30,000 shares, 4.54M
  - 2026-09-21 TETER TIMOTHY S (General Counsel): 30,460 shares, 6.79M
  - 2026-09-18 STEVENS MARK A (Director): 1,366,000 shares, 300.15M
  - 2026-09-04 STEVENS MARK A (Director): 1,022,239 shares, 235.64M
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

- [Procter & Gamble Company (The) (PG) Stock Forecasts](https://finance.yahoo.com/research/reports/ARGUS_48990_TechnicalAnalysis_1795782760000)  
  <sub>Yahoo Finance, 18 minutes ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [The Dates That Matter Most For Procter & Gamble Stock](https://www.trefis.com/stock/pg/articles/629330/the-dates-that-matter-most-for-procter-gamble-stock/2026-11-27)  
  <sub>Trefis, 5 hours ago</sub>  
  Today's big story: Anthropic Broke Its $83 IPO Price. What Did Facebook Do Next?Procter & Gamble (PG) shares returned 21.3% over the past year, against 8.4%...
- [Is Procter & Gamble Stock Outperforming the Dow?](https://www.google.com/goto?url=CAESlAEBxCJF10umZ3q9xGHBJ03aTn3K1JugDfpQIFv1MZgMPxpQJ5zBkDbUIN4nEBULhKR9XrcS_OBULsXPOzCqruH4gurbqvoAmEa38Awxn6kt-LXYwPQJpt_Mi0NVNLDRww0LMsawRuJIykL0eMrQj3LBJT0Q5P45SFqVefUh3T_i-xuGknageYMuHZDF6u4d4yb79DS4&gsessionid=8ZlA36u7imF1lYp6i4IUosVvImQBbMrrBgMQLltI6AZcXJ41EloaVw)  
  <sub>Barchart.com, 4 hours ago</sub>  
  The Procter & Gamble Company (PG) has become a familiar name in households around the world. From Tide detergent and Pampers diapers to Gillette razors,...
- [Black Friday: Shoppers hunt for deals as investors buy staples](https://www.google.com/goto?url=CAESngEBxCJF17EDzbHgWqBSHLkl6CJrLYrULRvumirJG_8YFkBMdqKcqmc3sYhvFmE8Gj_N6nMIirrxDx0RuuOXvX1Hjjk8vfdhmohYf7wO5656XdcqiUiBg45SjR7dhE1a-ZLJF4nkjCZT0TSFipbHlfj6JVSf9f15nPGSUZ2DRbZ3l-HFod4yfy09KZkYWUPUYG-KLTKUZVBA2sLLXiOPLg&gsessionid=8ZlA36u7imF1lYp6i4IUosVvImQBbMrrBgMQLltI6AZcXJ41EloaVw)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  NRF expects 182.7 million Americans to shop Thanksgiving through Cyber Monday, 4 million fewer than last year, while holiday sales could top $1 trillion.
- [2 Dividend Stocks to Buy in November and 1 to Leave on the Shelf](https://www.google.com/goto?url=CAESpgEBxCJF16MZv6FOddhrvg_IhGr1_0pMFGIyFSela829ERE9Ve7k7z8_paXWqOt0DrhiXcV9VlPK-ugYfVc8ub99d9s6SqODPPAoVBLlSQ4Sx6vKtUAoRsChgIPFJ5QWtZQD7yRUTwJJJ_PqxcnSdAt-B-MDMYbrmCg7JMITXDHxEBdIgMnfEmOTy9eev2PwcOQrLKbENJ8s3bUlTXhUmotMqimPizom&gsessionid=8ZlA36u7imF1lYp6i4IUosVvImQBbMrrBgMQLltI6AZcXJ41EloaVw)  
  <sub>The Motley Fool, 15 hours ago</sub>  
  In a volatile market, you want stocks that have reliable businesses so you can sleep well at night.
- [Procter & Gamble Hits 52-Week High: Should You Buy Now or Wait?](https://www.google.com/goto?url=CAESywEBxCJF189fVwp-w9AJOl0QokVw85QFWvV5lBoKWfF3KjFBi7oKpni6B7cdIzJ4hcwMpVygAv5lR8_LerIRmGKaVD5873ziEQVeD5SYfGcQPPS9bFbQyy1bgCTMNejut0NacNwt6soJBBKHij8rmWf95oKeFOJh5k3yd0GVn9r57wehz1R9u5JjtS9TdL_mdeY-ouzZMtPkxyf5bxp-fz60tgo_UJ3rFWTz-TMTxNl32vQaxOepRnUbynFHCrq0_cuZ91NUKBSv8YoKBQ&gsessionid=8ZlA36u7imF1lYp6i4IUosVvImQBbMrrBgMQLltI6AZcXJ41EloaVw)  
  <sub>The Globe and Mail, 17 hours ago</sub>  
  Shares of The Procter & Gamble CompanyPG hit a new 52-week high of $174.56 yesterday, reflecting strong investor confidence in the consumer staples giant's...
- [Procter & Gamble Company (The) $PG Shares Acquired by Toronto Dominion Bank](https://www.google.com/goto?url=CAESvwEBxCJF16Or8gO2ruOTTX7EfDVAscxJjaJ47wl6_ZV7i1ysSopp9Xf3svaSPQLaL-kMinRUtLTMtq_t4TKTwz4YcRw4liMCrIoNjFsZuf_4SyUMSRdROLzoX39zgmBIHZEXLAvGpz1di2tUaqTU8BHOs09xAIfHuoJbycXVSCUapKb0tLY8HrXh4F2FvyFr3FP3Ck0jqb24odyP3dHDrJvFmSve3MdEm1lOx3nmYG5A87mDYVfl1oDbXR6o-wKEEw&gsessionid=8ZlA36u7imF1lYp6i4IUosVvImQBbMrrBgMQLltI6AZcXJ41EloaVw)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Toronto Dominion Bank lifted its holdings in shares of Procter & Gamble Company (The) (NYSE:PG - Free Report) by 99.2% in the 3rd quarter, according to the...
- [PG Nov 2026 85.000 call (PG261127C00085000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScAHEIkXXOBRtWfwUqo8mVONyzSPnRKxRsLnOalhC8DoCsIBSYX8Bxza_iFPQT3rofIgPsVQ3y9538cU8q983V0FgixnmhFEyiccmRP0a2L5gbTGcgvhP5w-L4bnQ3SUDzX7iXpbfKmCbpBwZUweLdP0&gsessionid=8ZlA36u7imF1lYp6i4IUosVvImQBbMrrBgMQLltI6AZcXJ41EloaVw)  
  <sub>Yahoo Finance UK, 9 hours ago</sub>  
  Find the latest PG Nov 2026 85.000 call (PG261127C00085000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Here’s How Many Shares of Procter & Gamble You’d Need to Own to Collect $1,000 in Annual Dividends](https://www.google.com/goto?url=CAES7gEBxCJF1zaZ_g-bl3NoNNe7TtlcNzTbnhpisvJkgzTRAGitB4wfZpLVfZ4bmCxCjqkPHFYPD8WsjN6pQz0Fk3mAN9zss_hEAfDcecT5D__U2y-_XH9Fr1RhCphSUjJT71sJrnWXxM43pXsvCFgUWyUwsvb39l27M59C3dDH8YtbFiNCbWi9oXAI-7hvYZHDE-QTT42Jazco98rj7ZsUrSbMcyMM_1EFLrjAyWKtmNsuW9pT-r36Tll-9dzR981weCEAsjD9_r9QH1zMy2PawWrZwjcEffQsIIKvymm9WncP4IqC69cIl9OxIXpaQ1PD&gsessionid=8ZlA36u7imF1lYp6i4IUosVvImQBbMrrBgMQLltI6AZcXJ41EloaVw)  
  <sub>The Globe and Mail, 18 hours ago</sub>  
  Detailed price information for Procter & Gamble (PG-N) from The Globe and Mail including charting and trades.
- [Procter & Gamble grows despite cost pressures, maintaining dividend streak and steady income for investors.](https://www.google.com/goto?url=CAESkQEBxCJF1zijdbx4XOw9Z07K0SU_5BFCqZsdtAyzlcRY5QJQwqmi74AdCRl0L0v4CdSgak8SHVFIZQ3r0X023EjJnM1_EAe3QKr4vPDkJGUcKPQq3vMSkCwNP4AX6biN-FKLjlvjZXnkWPay6Pwhk4efAZ4XRekFIGdn22dBTYzVdiojAMIrxpBr4_7R8x-__fof&gsessionid=8ZlA36u7imF1lYp6i4IUosVvImQBbMrrBgMQLltI6AZcXJ41EloaVw)  
  <sub>Pluang, 17 hours ago</sub>  
  Procter & Gamble continues to grow its business even in a tough consumer spending environment, with a 4% rise in organic sales last quarter.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 173.00 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 168.50 (+2.7%), 50d 158.86 (+8.9%), 200d 150.52 (+14.9%); 50d above 200d
Momentum: RSI(14) 66.2 | MACD 3.742 vs signal 3.890 (histogram -0.148)
Returns: 1d -0.1% | 5d +3.1% | 1m +9.3% | 3m +20.3%
52-week range: 138.04 - 173.23 (now 99.3% of the way up)
Volatility: ATR(14) 3.07 (1.8% of price) | annualised 20d 18.9%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 400.98B
Valuation: trailing P/E 26.05 | forward P/E 23.30 | P/B 7.38 | PEG 4.35
Profitability: profit margin 18.2% | operating margin 24.9% | ROE 29.6%
Growth (YoY): revenue +4.0% | earnings +0.8%
Balance sheet: debt/equity 70.3% | free cash flow 12.65B
Risk: beta 0.36 | short interest 1.2% of float
Next earnings: 2027-01-22
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
Price target: mean 176.70 (+2.1% vs last close), range 151.00 - 197.00
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

### Royal Bank of Canada (RY) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Royal Bank of Canada(RY) Stock Price Today | Quotes & News](https://www.moomoo.com/stock/RY-US?chain_id=Name1K9-3FXPhg.1lgil50&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A57%2C%22f%22%3A%22www.moomoo.com%2Fstock%2FBMO-CA%22%7D)  
  <sub>Moomoo, 4 hours ago</sub>  
  Track the latest Royal Bank of Canada(RY) stock price, quotes, financial information, news and analyst rating on moomoo App for your stock trading and...
- [RY Jul 2027 145.000 put (RY270716P00145000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/RY270716P00145000/)  
  <sub>Yahoo Finance UK, 21 hours ago</sub>  
  Find the latest RY Jul 2027 145.000 put (RY270716P00145000) stock quote, history, news and other vital information to help you with your stock trading and...
- [BCE Inc. (BCE.TO) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZgHEIkXX74OGFRP6v-nfB9fUcqCbulEMk3DmB01MPFAOyQQR8VN2Gt6fV-8gcEBDApfrF9t8SRDtZGBombdRNjzkPPOroBSFZNIOCXVCogv-5QH7z5oTaLJ5-Xc3ILE7LBozDAtu6w&gsessionid=gKhmkK0Ts5TlhQCzZ3NK_JzdXp-7Za9daAzA4lvBjtc5bK65HgS4Zw)  
  <sub>Yahoo! Finance Canada, 3 hours ago</sub>  
  Find the latest BCE Inc. (BCE.TO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Salesforce, Kroger and Dollar General Report in the Earnings Week of November 30](https://www.google.com/goto?url=CAESigEBxCJF13B2Fop6S588i01ZBcfcR2M3loAtXCTSp4j0xYr1LyPZH046oDf28PuWsVJQqliYN2eTw2eTGAvJCAaQHZAFfJ4jMQIfO4A6AJY92D5eB4-IovIq9jCp41duPXoV0h5tWAqJkrqH7LF2kRUAAjkF2n_ay3JmILXFWcOboH9N1AxHp0N65SU&gsessionid=gKhmkK0Ts5TlhQCzZ3NK_JzdXp-7Za9daAzA4lvBjtc5bK65HgS4Zw)  
  <sub>Stock Titan, 5 hours ago</sub>  
  Fifty companies worth $2 billion or more report in StockTitan's Earnings Week Ahead for November 30 to December 4, 2026, led by Royal Bank of Canada,...
- [Automate Your Savings With This Set-and-Forget Strategy for Building a Cash Cushion](https://www.google.com/goto?url=CAESrwEBxCJF14xwcvNu6ejzqa2Akb2NR5xvI41XuIvajFYl8u9ZbN5lPnjdanzwFhhEiJxtsdohY0K8AODz4VyMEsrYF39OM76ALrNrisSAwR0LYrZ62yHswc2ZEWWHJXmYC_Jl56rh2Xgcb6IFcyM_TdJyh51CWMzKxXCZsuIhn9Z4-BKpovfS1Ro-Zqz8z8udXk2sTT4nLsk7I4TBv7sb8EW3NY1o7Liy50dTUaXgk7KW&gsessionid=gKhmkK0Ts5TlhQCzZ3NK_JzdXp-7Za9daAzA4lvBjtc5bK65HgS4Zw)  
  <sub>The Motley Fool Canada, 13 hours ago</sub>  
  Many investors enter the stock market looking for the next Apple or Amazon, where a set-and-forget strategy works. Finding such a company takes effort,...
- [Heads Up: The Registered Account Where the U.S. Takes 15% of Your Dividends](https://www.google.com/goto?url=CAESpAEBxCJF16_uLxvwICTiVVSHUcqyWLX0HyIhF3I5I2zNY1cNxHEYWWJckZXtlqVKlGgTxXKx2-NnjOTwxNps8exXzHVAKc2YsMHfahQIK2kjwcaOZzus_61Ng3RPcVHM70Ume55GBl1K6i-OBUWDH9RO_U6W2ZD1WQ3qd1Darswx1f_f2JE_nBafhM4SXvTETKylul_rQqmkVoGCaYZJv3En0TcoCA&gsessionid=gKhmkK0Ts5TlhQCzZ3NK_JzdXp-7Za9daAzA4lvBjtc5bK65HgS4Zw)  
  <sub>The Motley Fool Canada, 14 hours ago</sub>  
  While holding a U.S. dividend stock, here's how to determine how much of each payment reaches a Canadian investor.
- [Royal Bank of Canada (RBC) forecast ahead of earnings: will it rebound or fall?](https://www.google.com/goto?url=CAESqwEBxCJF1yQsDnVvwQLOTClqNSzNV0QwyDE-YkKKdjbgvQh0LCjOYWKyqtcZq5r5exgZ9CaWyRExlW6rN_rCKwiaHNuWR6WWr4Z5V7nc1CXC_SvZ8molmqjm7LVnwSl6AaqUmUxfqCnSPL4AuJguLN9zwEpu2o9Koc89EjJVRs1KmGAfDwkr-4neAJuNOWboAWaNib3Y4mrh2WwGPgZrKLgGixcPlurQnU1VoK0&gsessionid=gKhmkK0Ts5TlhQCzZ3NK_JzdXp-7Za9daAzA4lvBjtc5bK65HgS4Zw)  
  <sub>Invezz, 22 hours ago</sub>  
  Royal Bank of Canada (RBC) stock has dropped into a correction, moving from a record high of $306 in July to $269 today.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 189.59 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 197.73 (-4.1%), 50d 198.29 (-4.4%), 200d 191.87 (-1.2%); 50d above 200d
Momentum: RSI(14) 38.7 | MACD -3.515 vs signal -2.268 (histogram -1.246)
Returns: 1d +0.1% | 5d +1.0% | 1m -7.4% | 3m -7.2%
52-week range: 152.89 - 217.87 (now 56.5% of the way up)
Volatility: ATR(14) 3.73 (2.0% of price) | annualised 20d 26.0%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 262.47B
Valuation: trailing P/E 16.57 | forward P/E 14.88 | P/B 2.75 | PEG 1.76
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
Price target: mean 207.63 (+9.5% vs last close), range 182.72 - 225.09
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

- [Aurinia Pharmaceuticals: Lupkynis Growth Slows, Reduced Communication Unhelpful](https://seekingalpha.com/article/4972323-aurinia-pharmaceuticals-lupkynis-growth-slows-reduced-communication-unhelpful)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Analyst sees AUPH as a lupus-nephritis play: TEVA settlement helps, but Lupkynis exclusivity risks remain; PRESERVE may be complete in March 2029.
- [Israel stocks higher at close of trade; TA 35 up 2.34%](https://www.investing.com/news/stock-market-news/israel-stocks-higher-at-close-of-trade-ta-35-up-234-5052604)  
  <sub>Investing.com, 23 hours ago</sub>  
  Investing.com – Israel stocks were higher after the close on Thursday, as gains in the Real Estate, Technology and Communication sectors led shares higher.
- [Thu: Construction, renewable energy stocks fuel TASE surge](https://www.google.com/goto?url=CAESoQEBxCJF18E21xt4eOK8vj4n5yE191LMVnnpCsI-cAWIUEPtndS_Q7TqOhxppiYNi1R2NwOV6FQHqhl7mVK_nptJNG_OCQQ2wmbtoKKw1KPW6caOVRzX0tK9YeKgM4P1WNgt7TQOsPEk8ktY9Cdzfz0vSeLzo8SlFDtRiVE3AU-52SADiGEaR3kZMOJKuYaBBYwL7c783bMbo0CnJomg4BKMxw&gsessionid=r9hd3j-FVGqjlFYLvGs64Cu1mBV-y9q1KZ_v6AUZ7S-hAI5bk14esg)  
  <sub>Globes - Israel Business News, 20 hours ago</sub>  
  The local stock market halted its slide today with notable gains for the banks, real estate stocks, and cleantech.
- [We found the 2026 LEGO Advent calendars that are still in stock](https://www.google.com/goto?url=CAESsQEBxCJF17sB6-PK3Q8ABQBKwsDjU0_Vbm_2RmfK_3lr3VI60Uqx4vh9iyJwjOHup_BeNyr8ggrg7almlNJqX5XZKyYZa-MNonLRbYGjQUv57OmOIdK7u7hP1EYAofRYwxWbAvSzuB3gEeELvTs_FTeWMbYzqjmzmnxV8LYrnQ_pFV8j6qUmMLX-vZncYyJqOL6PyumzJ2NZ10vgldxlGnjzvGtqX_HhJw3WqRwOWtXupB4&gsessionid=r9hd3j-FVGqjlFYLvGs64Cu1mBV-y9q1KZ_v6AUZ7S-hAI5bk14esg)  
  <sub>KTSM 9 News, 24 hours ago</sub>  
  BestReviews is reader-supported and may earn an affiliate commission. Details. If you want a LEGO Advent calendar, you should buy it now.
- [Israel shares higher at close of trade; TA 35 up 2.34%](https://www.google.com/goto?url=CAESpgEBxCJF1zwHIToAX4QbNvbZ5K4JWxT4iDs-2vwqEJhT7Q2pKS2XF50lsRjdTip4zzLgR1mnTNT8Kjgg05tKhbsfP330_YnvjHD7cElEEVvfVBwtOv_sWQ4S0tvD-JzPPMb1F2DoSygDH1u5-S-CWVGyrt78Fb55hfCcc-l_nHLcG2_4WtBJhD1Pkmr62oD545_QLxgtnkAxKay22NV90nS9boW-tD0V&gsessionid=r9hd3j-FVGqjlFYLvGs64Cu1mBV-y9q1KZ_v6AUZ7S-hAI5bk14esg)  
  <sub>Investing.com UK, 23 hours ago</sub>  
  Investing.com – Israel equities were higher at the close on Thursday, as gains in the Real Estate, Technology and Communication sectors propelled shares...
- [MindWalk (HYFT) Discloses Teva Australia ReefIQ Agreement: What Investors Should Know](https://www.google.com/goto?url=CAES4AEBxCJF14NI4Co1R9uQ6ofdJmd9D0J6Wcon81ocTBxgZ7tsWJX3ocHYbqwrpXAYRELNNkbsdTy-eRbc7nupNdp2FAnJqBo7BE9m7-L5ER33GeDSVjPNkUoC_FJ6yvn15F4JCu97I1S2lUzRuKIRTIWWQK7MOJmrF-qDPFValFvkLV1CbT3m5LuQwDB3DCGBjoG5xc3x77KP6trJCcfvz0ZroxjH6OSH01umwmdev_ZjIoJzAea53ymdB7C9Jv6UTtFeVq5xdjj9qyj3o4c-um4uX0ip9QVSojFShSo-muIq-Q&gsessionid=r9hd3j-FVGqjlFYLvGs64Cu1mBV-y9q1KZ_v6AUZ7S-hAI5bk14esg)  
  <sub>Minichart, 23 hours ago</sub>  
  MindWalk Holdings Discloses Multi-Year ReefIQ Agreement with Teva Pharmaceuticals Australia MindWalk Holdings Corp. (NASDAQ: HYFT) furnished an investor...
- [Teva Pharmaceutical Industries stock to close Kfar Saba labs by 2027](https://www.google.com/goto?url=CAESvwEBxCJF138Jx9LFF8YFa_k74a5BAAvj6snf3fxuM1SCPMXjH23DG6n1hWzPQ29ucbf2fG36k-CQ54Fx10tcJ9t-Ht8LfH1lH0CDxYDtRvOjs21YHa2P5LnDDK1xhT8xgAgu3ufNodhDUU2n9YEgrFKg0gh-1hImMbigvW-HUdT240Gn3yWzvZAMo5xgqagRmLRpC-eL04NGNZJhUP2pEHQa0HvAk-d201UTgDnteMGwwuuVvgyMgcDufn2EZbmaUQ&gsessionid=r9hd3j-FVGqjlFYLvGs64Cu1mBV-y9q1KZ_v6AUZ7S-hAI5bk14esg)  
  <sub>ad-hoc-news.de, 5 hours ago</sub>  
  Teva Pharmaceutical Industries stock faces a research restructuring as the company plans to close generic-drug labs in Kfar Saba by end-2027.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 39.49 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 41.62 (-5.1%), 50d 40.69 (-3.0%), 200d 35.36 (+11.7%); 50d above 200d
Momentum: RSI(14) 42.2 | MACD -0.263 vs signal 0.170 (histogram -0.432)
Returns: 1d -0.9% | 5d +2.5% | 1m -1.2% | 3m +8.4%
52-week range: 26.32 - 44.50 (now 72.4% of the way up)
Volatility: ATR(14) 1.40 (3.6% of price) | annualised 20d 43.2%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 46.07B
Valuation: trailing P/E 91.83 | forward P/E 12.61 | P/B 5.77 | PEG 0.71
Profitability: profit margin 2.9% | operating margin 19.8% | ROE 6.7%
Growth (YoY): revenue -1.9% | earnings -46.0%
Balance sheet: debt/equity 212.9% | free cash flow 1.49B
Risk: beta 0.84 | short interest 2.3% of float
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
Price target: mean 50.51 (+27.9% vs last close), range 42.12 - 57.00
Recent rating changes:
  - 2026-11-12 Piper Sandler: main, Overweight -> Overweight
  - 2026-11-05 Leerink Partners: main, Outperform -> Outperform
  - 2026-11-04 TD Cowen: main, Buy -> Buy
  - 2026-11-04 HC Wainwright & Co.: main, Buy -> Buy
  - 2026-11-02 HC Wainwright & Co.: init, ? -> Buy
  - 2026-10-15 Barclays: main, Overweight -> Overweight
Institutional ownership: 70.1%
Largest holders: Blackrock Inc. (5.4%), Phoenix Financial Ltd. (3.6%), WCM Investment Management, LLC (3.6%), Clal Insurance Enterprises Holdings Ltd (3.6%), Migdal Insurance & Financial Holdings Ltd. (3.4%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 43,476 shares in 3 transaction(s) | sold 29,021 shares in 4
Net: +14,455 shares (+0.3% of insider holdings) | insiders hold 5,682,446 shares
Distinct insiders: 0 buying, 11 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-11-20 FOX CHRISTINE (Officer): 28,229 shares, 1.10M
  - 2026-11-12 SABAG MARK (Officer): 44,710 shares, 1.97M
  - 2026-11-11 DANIELL RICHARD (Officer): 45,003 shares, 1.93M
  - 2026-11-10 FRANCIS RICHARD D (Chief Executive Officer): 250,000 shares, 10.56M
(17 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

- [NCG: Thông báo hoàn tất việc góp vốn vào CTY CP TM SX Da Nguyên Hồng](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b0997bb6f64427ebcb0a1d056bcac46&url=https%3a%2f%2fvietstock.vn%2f2026%2f11%2fncg-thong-bao-hoan-tat-viec-gop-von-vao-cty-cp-tm-sx-da-nguyen-hong-830-1518592.htm&c=14965216556243086655&mkt=en-us)  
  <sub>Vietstock, 14h ago</sub>  
  27-11-2026 16:12:17+07:00 NCG: Thông báo hoàn tất việc góp vốn vào CTY CP TM SX Da Nguyên Hồng VIETSTOCK Tại Lễ kỷ niệm 30 năm Ngày truyền thống ngành Chứng khoán Việt Nam, Công ty Cổ phần Chứng khoán ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 213.30 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 209.68 (+1.7%), 50d 197.97 (+7.7%), 200d 196.75 (+8.4%); 50d above 200d
Momentum: RSI(14) 58.4 | MACD 4.185 vs signal 4.629 (histogram -0.444)
Returns: 1d -1.2% | 5d +1.1% | 1m +9.5% | 3m +9.7%
52-week range: 166.50 - 248.29 (now 57.2% of the way up)
Volatility: ATR(14) 4.47 (2.1% of price) | annualised 20d 41.1%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 250.34B
Valuation: trailing P/E 9.73 | forward P/E 13.52 | P/B 16.98 | PEG 19.39
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
Consensus: none (mean n/a on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 1 strong buy, 1 buy, 2 hold, 0 sell, 0 strong sell
Price target: mean 238.08 (+11.6% vs last close), range 230.00 - 253.00
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

- [$100 Invested In ExxonMobil Holdings 5 Years Ago Would Be Worth This Much Today](https://www.benzinga.com/news/26/11/63669294/100-invested-exxonmobil-holdings-5-years-ago-would-be-worth-much-today)  
  <sub>Benzinga, 47 minutes ago</sub>  
  ExxonMobil Holdings (NYSE:XOM) has outperformed the market over the past 5 years by 11.96% on an annualized basis producing an average annual return of...
- [XOM Nov 2026 245.000 call (XOM261127C00245000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XOM261127C00245000/)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  Find the latest XOM Nov 2026 245.000 call (XOM261127C00245000) stock quote, history, news and other vital information to help you with your stock trading...
- [Energy sector performance - S&P 500 energy stocks](https://www.google.com/goto?url=CAESbwHEIkXX7_mg_NILFeDddrqWh0UI67jmSW1JqSdPXw4K3eZLVpv_XwyUamAnTBhyZgMNeZRdsrdOa1QohSOO5FU-ElDrSbuncig2Sub5NWSHB_EPlBiEkpKZ6JApVAvdW9gmcpkqc3hz84qao0_nrg&gsessionid=6Sl2Q6HS6GhN_BQ3cbHQ9YRV7reMFxWvQxoksQ5kA01w7H3a3B4ctQ)  
  <sub>Quantisnow, 10 hours ago</sub>  
  How S&P 500 energy stocks are performing today and over the past week, month, quarter and year, with a heatmap of oil and gas producers, refiners and...
- [Exxon Looks to Ditch New Jersey Incorporation for Texas Homecoming](https://www.google.com/goto?url=CAESnAEBxCJF1wgvT_TC-v-S9YjJ-QGVRCFHXn91bG9vrvDpd5VsV2zmFSc_PVx-r08a5n22VevhF0mE93fBK1uF0E3bQWX6q4QWJ5HIVgnd5ThSIRrCHEw7trb1al3dpQ3j8sRaWaptyJcolOfA5zxDrZtyi7Gv1dOP3BH0bo1Rk800VloxBpw5sTntUv3YxfBfJoUzkGeb-q4HOT8kryE&gsessionid=6Sl2Q6HS6GhN_BQ3cbHQ9YRV7reMFxWvQxoksQ5kA01w7H3a3B4ctQ)  
  <sub>EnergyNow.com, 21 hours ago</sub>  
  Summary Exxon is latest high-profile company moving to Texas for business-friendly environment New Jersey sued…
- [Apple, Exxon and Lowe’s Are Rewarding Shareholders Beyond Their Regular Dividends](https://www.google.com/goto?url=CAEStgEBxCJF17DEDlAYnA6aTopYAlsPp9MY4DbYqMADg7KtzZTT6lJ2nNMYoUMn6JiTO1rgO5heoy2R46k7NwowLaOZQuuXGBciF6x81VeFkj-4pGDRbsfbrfK-lUv5iDHBTmDa4S8iz1Zgc8GiHjj1c6AVtwTDRvlBOgCUCl7VMGL6hW_Dpu4U9nQsyFguyEsraCL1u7q1HbRdcaPIexK6XaPun1OxOhlPSxCMKRzaV82XsNqx2e77Zg&gsessionid=6Sl2Q6HS6GhN_BQ3cbHQ9YRV7reMFxWvQxoksQ5kA01w7H3a3B4ctQ)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  A dividend puts cash in your account. A buyback works in the background: the company retires its own shares, so each remaining share has a larger piece of...
- [Exxon Mobil Stocks Edge Lower as Brent Jumps 3.5% on Refinery Attack](https://www.google.com/goto?url=CAESugEBxCJF1_EwfjmpXcOCvpvtwMozGgPf72eRFCQKBkweDnErhn0V9ct93pSUQ6QDeA2b8R639VDZkIkVcmjWW1llxHJVNlOMDJUjGalxnsxK5MJv1wdOTxv7Cm0AxyIhS1SuiJ8-Vj30P3js6CnEEtGfYcLp4NzhOTb8MqeSuVemGWJKC5aEc0WI8XlpT1MsqJfegk4JAv4uF-_fu6AZKpq_9QQpY1CwWaqmIiY1gW_b56iwz3j4WSH8CYg&gsessionid=6Sl2Q6HS6GhN_BQ3cbHQ9YRV7reMFxWvQxoksQ5kA01w7H3a3B4ctQ)  
  <sub>TradingView, 20 hours ago</sub>  
  Exxon Mobil NYSE:XOM shares edged lower by 0.09% to $158.08 at the 4:00 p.m. ET close on November 25, even as Brent crude settled up 3.5% at $94.61 a barrel...
- [Xometry, Inc. (XMTR) stock price, news, quote and history](https://www.google.com/goto?url=CAESYwHEIkXXIkbbcLzrAuykM5_QnxLaY4UTvt2SK4VQ2qzNUygTtQEYAb19541zkroub9zPK3wBlQ1VGVv7U99a23hqaww729H6RG7IKzMUmsUeO8dY0z1vop3UCyNCrcRbQmv7cA&gsessionid=6Sl2Q6HS6GhN_BQ3cbHQ9YRV7reMFxWvQxoksQ5kA01w7H3a3B4ctQ)  
  <sub>Yahoo Finance Australia, 10 hours ago</sub>  
  Xometry, Inc. (XMTR) ... This price reflects trading activity during the overnight session on the Blue Ocean ATS, available 8 p.m. to 4 a.m. ET, Sunday through...
- [ExxonMobil Holdings (XOM), Why Is It Back In Focus?](https://www.google.com/goto?url=CAESswEBxCJF1yNay9T74gpEJhsuZy-IGI_tbAu9Q49QuhwcUqwYgDnvFpzgFdl7vrNUJEwl04bXYNngndvKRGcnbSCYKDBDk2iRsjiIWbVeyFYwEpt7HPAjXKX7eSoIZyydp3thX6V2Vw7myGxWBrknub3BigCpo0u_LrYvsJVR6fjDVs2G0mlCrrsqk27XZcMPSJb0Xzu0BzHPmvbPFL0Y01i5E2ce2h14kmo2UE7U5BC2tV4XAA&gsessionid=6Sl2Q6HS6GhN_BQ3cbHQ9YRV7reMFxWvQxoksQ5kA01w7H3a3B4ctQ)  
  <sub>Simply Wall St, 10 hours ago</sub>  
  Fresh security risks around Saudi Arabian energy assets and shipping routes have pushed Middle East supply back into focus, putting ExxonMobil Holdings...
- [What's Going On With Chevron Stock On Friday?](https://www.google.com/goto?url=CAESowEBxCJF14RsyCA208Q5_DHFK7YBByzNxfF_rBjRfLA_vnfz5PDmr_-tGEQ0cXzpP9MrGseEdby4yeYYLvXGkcxf9EiPVSiKF7t-rpos96YuW0u8zvWYnAIXpBKXwaHpZIx0pAF7inZxQxa76oCcZGUZ3JwHIOXs4-PiY2looryMezEYoh931E9OFl2UXqqkR41VUoGKNQtFZ-eJqW3QlbX4452A&gsessionid=6Sl2Q6HS6GhN_BQ3cbHQ9YRV7reMFxWvQxoksQ5kA01w7H3a3B4ctQ)  
  <sub>Benzinga, 1 hour ago</sub>  
  Chevron Corporation (NYSE:CVX) shares edged higher by 1% in premarket trading in Friday' premarket session as traders digest pressure on OPEC headlines and...
- [ExxonMobil : appoints Ognjen Plakalovic as incoming Chair of Mobil Oil New Zealand](https://www.google.com/goto?url=CAESwQEBxCJF1wOR_rT9VS7WYnHa7NYO0v1Rsn0OkWM8wrAiPa90x1AbTifefT3OVryAj8JcVkwBNs0fOD3OIZgBn-9lCWMR3TFBX1ghwlhjP-Z4keOLm6iud6yAANwcfALAxXXqrFqkuPRPAaf1SU8XWQIFVm6mZlmp-UxQ-e6jR8C76rEPpl9CLDLYrVHDV0MKPvU6ICyFEiBx3KQtUI_mz-RJxzXJNjOhdUdOTEL0_yQuE5rgcjHYRqRsB0jEnA0EdilT&gsessionid=6Sl2Q6HS6GhN_BQ3cbHQ9YRV7reMFxWvQxoksQ5kA01w7H3a3B4ctQ)  
  <sub>www.marketscreener.com, 13 hours ago</sub>  
  Home Australia newsroom ExxonMobil appoints Ognjen Plakalovic as incoming Chair of Mobil Oil New Zealand selected item Australia News Nov.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 160.05 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 166.40 (-3.8%), 50d 168.78 (-5.2%), 200d 156.97 (+2.0%); 50d above 200d
Momentum: RSI(14) 39.5 | MACD -3.762 vs signal -2.737 (histogram -1.024)
Returns: 1d +1.2% | 5d +0.7% | 1m -12.1% | 3m +2.1%
52-week range: 114.68 - 187.25 (now 62.5% of the way up)
Volatility: ATR(14) 3.87 (2.4% of price) | annualised 20d 31.5%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 652.88B
Valuation: trailing P/E 16.47 | forward P/E 12.82 | P/B 2.46 | PEG 1.24
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
Price target: mean 184.18 (+15.1% vs last close), range 160.00 - 213.00
Recent rating changes:
  - 2026-11-12 Bernstein: main, Outperform -> Outperform
  - 2026-11-07 Freedom Broker: main, Hold -> Hold
  - 2026-11-04 Citigroup: main, Neutral -> Neutral
  - 2026-11-04 TD Cowen: main, Buy -> Buy
  - 2026-11-02 UBS: main, Buy -> Buy
  - 2026-11-02 Morgan Stanley: main, Overweight -> Overweight
Institutional ownership: 67.6%
Largest holders: Blackrock Inc. (8.1%), Vanguard Capital Management LLC (6.6%), State Street Corporation (5.2%), FMR, LLC (3.6%), Vanguard Portfolio Management LLC (2.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 11,629,051 shares in 259 transaction(s) | sold 3,904,152 shares in 49
Net: +7,724,899 shares (-279.5% of insider holdings) | insiders hold 4,976,651 shares
Distinct insiders: 0 buying, 0 selling
(8 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

## Whole-market funds

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The emerging‑markets ETF shows no clear macro catalyst or decisive technical break. Fundamentals remain steady (moderate valuation, decent yield, low cost) and there is no news. Technicals point to a mild downtrend (price below all major SMAs, RSI below 50, negative MACD) but the bounce in the last day is not strong enough to warrant a directional call. Analyst consensus is overwhelmingly bullish with a high price target, yet it only covers 22.6% of the fund, tempering its impact. Positioning is flat and fund flows are unchanged, providing no additional bias. Given the lack of material changes, the overall bias is neutral with low conviction.

**Main reasons it gave:**
- Technical trend below 20‑day, 50‑day, and 200‑day SMAs indicating a downtrend
- RSI 43.2 and MACD negative, showing bearish momentum
- Analyst consensus 100% buy with weighted price target +60.9% (thin coverage 22.6%)
- No significant news in the past 24 hours

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 53.67 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 54.73 (-1.9%), 50d 57.29 (-6.3%), 200d 58.12 (-7.6%); 50d below 200d
Momentum: RSI(14) 43.2 | MACD -1.271 vs signal -1.186 (histogram -0.085)
Returns: 1d +1.7% | 5d +1.9% | 1m -5.9% | 3m -11.7%
52-week range: 50.62 - 61.44 (now 28.2% of the way up)
Volatility: ATR(14) 1.25 (2.3% of price) | annualised 20d 36.2%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Diversified Emerging Mkts
What it holds: P/E 13.83 | P/B 2.03 | P/S 1.69 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +12.2% a year | beta to the market 0.78
Cost and size: expense ratio 0.06% | net assets 153.78B
What it is made of: Stocks 95.4%, Cash 4.2%, Other 0.4%, Preferred 0.0%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 15.3%, Tencent Holdings Ltd 2.7%, Alibaba Group Holding Ltd Ordinary Shares 2.1%, MediaTek Inc 1.5%, China Construction Bank Corp Class H 1.0%
Sector mix: Technology 32.4%, Financial services 20.5%, Consumer cyclical 9.5%, Industrials 7.4%
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
Rolled up from the 5 largest holdings, 22.6% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.31 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +60.9% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 00939
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 0.0% of open interest (1,102,805 contracts)
Change on the week: -2.2% of open interest
Crowding: 10% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 1.42B | fund size: 76.12B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Farm goods basket (DBA) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Technical: price above 20‑day SMA but below 50‑day and 200‑day SMA, low volume
- Fund flows flat with no net creations or redemptions
- Analyst view provides no rating or price target
- Macro data: inflation and unemployment in line with expectations, no surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 26.78 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 26.36 (+1.6%), 50d 27.46 (-2.5%), 200d 27.42 (-2.3%); 50d above 200d
Momentum: RSI(14) 51.2 | MACD -0.302 vs signal -0.405 (histogram 0.103)
Returns: 1d +1.7% | 5d +2.2% | 1m -1.2% | 3m -8.2%
52-week range: 25.44 - 29.49 (now 33.2% of the way up)
Volatility: ATR(14) 0.25 (0.9% of price) | annualised 20d 12.0%
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
Yield: 3.4%
Three-year record: +11.0% a year | beta to the market 0.37
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
Shares outstanding: 27.60M | fund size: 739.27M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fund flows: +16.4% share count increase over 34 days (strong inflow)
- Energy inventories: -0.9M barrel draw, 10% percentile (low level, bullish for oil)
- Technicals: price below 20‑day SMA (30.65) and 50‑day SMA (32.11), RSI 33, volume 0.08× 20‑day avg, no decisive break
- EIA gas price outlook: forecast down 11% over six months (bearish for gas exposure)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.66 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 30.65 (-3.2%), 50d 32.11 (-7.6%), 200d 29.84 (-0.6%); 50d above 200d
Momentum: RSI(14) 33.0 | MACD -0.906 vs signal -0.809 (histogram -0.097)
Returns: 1d +1.3% | 5d +0.1% | 1m -12.2% | 3m -3.7%
52-week range: 22.36 - 34.10 (now 62.2% of the way up)
Volatility: ATR(14) 0.48 (1.6% of price) | annualised 20d 21.0%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Commodities Broad Basket
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +11.6% a year | beta to the market 1.04
Cost and size: expense ratio 0.85% | net assets 1.94B
What it is made of: Other 50.0%, Cash 45.2%, Bonds 2.7%, Stocks 2.1%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 41.8%, Brent Crude Future Jan 27 11.0%, Invesco Short Term Treasury ETF 5.8%, Mini Ibovespa Future Dec 26 2.1%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.20</summary>

```text
US inventories, week ending 2026-10-30 (published the following Wednesday)
  Crude oil: 409.8 million barrels, -0.9 on the week (a draw), 10% percentile over 52 weeks -- low for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score +0.20</summary>

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
Share count change: 1 week: +4.0% (76.61M) over 7d | 1 month: +16.4% (278.56M) over 34d
Shares outstanding: 66.80M | fund size: 1.98B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, technicals show price below SMAs and low volume, while flows are positive but not enough to outweigh neutral technicals.

**Main reasons it gave:**
- Net inflows of +6.3% over the past month indicating demand
- Price 91.16 below 20‑day SMA 91.31, 50‑day SMA 91.48, and 200‑day SMA 94.46
- RSI 49.1 and MACD -0.328 near zero indicating neutral momentum
- Trading volume at 0.04× the 20‑day average, suggesting weak conviction
- No macro surprise: inflation 3.7% in line with expectations

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 91.16 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 91.31 (-0.2%), 50d 91.48 (-0.3%), 200d 94.46 (-3.5%); 50d below 200d
Momentum: RSI(14) 49.1 | MACD -0.328 vs signal -0.299 (histogram -0.029)
Returns: 1d +0.5% | 5d +0.9% | 1m -0.7% | 3m -3.9%
52-week range: 89.92 - 97.74 (now 15.9% of the way up)
Volatility: ATR(14) 0.53 (0.6% of price) | annualised 20d 8.0%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Emerging Markets Bond
Yield: 5.4%
Credit quality: BBB 33.9%, BB 25.6%, B 19.2%, A 17.3% | US government debt 87.8%
Three-year record: +7.7% a year | beta to the market 1.06
Cost and size: expense ratio 0.39% | net assets 13.57B
What it is made of: Bonds 99.2%, Cash 0.8%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 0.5%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.3% (40.11M) over 7d | 1 month: +6.3% (811.62M) over 30d
Shares outstanding: 150.16M | fund size: 13.69B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; modest inflows but no macro surprise and weak technicals.

**Main reasons it gave:**
- Weekly share count up 0.4% (67.86M) indicating modest inflows
- Price below 20‑day, 50‑day, 200‑day SMAs; RSI 41.8, MACD slightly negative
- Treasury yields stable (10‑yr 4.89% down 0.16% week) with no rate surprise
- Fund yield 6.1% with credit quality BB/B, no strong macro catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [iShares iBoxx $ High Yield Corporate Bond ETF (HYG)](https://ca.finance.yahoo.com/quote/HYG/options/?date=1796947200&straddle=false&type=all)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  View the basic HYG option chain and compare options of iShares iBoxx $ High Yield Corporate Bond ETF on Yahoo Finance.
- [HYG Dec 2026 78.000 call (HYG261231C00078000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/HYG261231C00078000/chart/)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  Interactive Chart for HYG Dec 2026 78.000 call (HYG261231C00078000), analyze all the data with a huge range of indicators.
- [For the Retiree Who Wants the Portfolio to Match Their Faith at 69: 3 ETFs Built Around Values](https://www.google.com/goto?url=CAESyQEBxCJF1ytLkfirdecDN8W3fu_txGfJF8qXzVTsiH2EpxMKfkIMDJ4ISLRptrTSpCQ66Ciq1jlkdbLAhmjizCnGH_0SdL6-l2onVvLPZTF337ETHG8biIT70nXG6CF_vROEnkGoehf46Km-8VH7KybEu2Xdh1w-O9HGCeliHhXZs_qDHTIN8eWT_v3UxdzOgMWjdl_8cgPzvvWnsO2Pk0-j0gCgkNajtAWb7IcgUuBqKFClq0242MI9pMh-72_dZOODa4ls3FWE0nI&gsessionid=mPL0-TS3VMoh__tWXu9KzZMcdqpHuHB8zlL_8Rh5f6cKnOP3utQqgQ)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  Faith-screened ETFs CATH and IBD let retirees align savings with their beliefs, pairing a Catholic-screened S&P 500 fund with a monthly-paying bond fund.
- [HYG Nov 2026 76.500 call (HYG261127C00076500) interactive stock chart](https://www.google.com/goto?url=CAESdwHEIkXXZgkRGuO5-uVaoTdQQ81D8qFC83qraCBspUd4da6J5IaU1W9PT8FOMC1GOapucJUU1_ErHLy61sz-LKAi_MDu4HYVwFXeZF-JPdcE_cKgvcsNb_XYnkZIPV9OVWgirrB2wgThepDkzJzlrWdeunLpg70V&gsessionid=mPL0-TS3VMoh__tWXu9KzZMcdqpHuHB8zlL_8Rh5f6cKnOP3utQqgQ)  
  <sub>Yahoo Finance UK, 7 hours ago</sub>  
  Interactive chart for HYG Nov 2026 76.500 call (HYG261127C00076500) – analyse all of the data with a huge range of indicators.
- [What's the Tax Bill on $7,125 a Month in Dividend Income? The Taxable Account vs. Roth IRA Math](https://www.google.com/goto?url=CAESyQEBxCJF1zf0od0Tj3CN45T9eBfKAGHchvvHHDjLd2SscC2ytBtSMVEXLQFQ9HDRwbgeVW68MA0Gi2bRPiG7QA5PdTAQlXWccQxhBYcIBBv_T6MC1iueKYQ4wkL73DIBXEcoN9IfalnzQFi6Q9qsT6AXKIpIX27bBQhmqj5FRbFXfN_Q_F_xiaX8_M9xy0jG5pWh5QsZ8rG4ym75M-Vg5laIyDXkvoT17oMB8NfJTPPbBxx-60YT9CtvsZMiKkARWpXyXkbF2Yk6PGs&gsessionid=mPL0-TS3VMoh__tWXu9KzZMcdqpHuHB8zlL_8Rh5f6cKnOP3utQqgQ)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  A married couple taking $85,500 a year in dividends from a taxable account owes only about $1,300 in federal tax, because tax character drives the bill.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 76.60 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 76.91 (-0.4%), 50d 77.19 (-0.8%), 200d 79.14 (-3.2%); 50d below 200d
Momentum: RSI(14) 41.8 | MACD -0.242 vs signal -0.218 (histogram -0.025)
Returns: 1d +0.1% | 5d +0.1% | 1m -1.3% | 3m -3.9%
52-week range: 76.33 - 81.18 (now 5.5% of the way up)
Volatility: ATR(14) 0.30 (0.4% of price) | annualised 20d 5.1%
Volume: 0.04x the 20-day average
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
Three-year record: +6.8% a year | beta to the market 0.65
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.40</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.4% (67.86M) over 7d | 1 month: +6.3% (1.05B) over 34d
Shares outstanding: 232.05M | fund size: 17.77B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, modest yield decline, slight reduction in net short position, mixed technicals, stable fund fundamentals.

**Main reasons it gave:**
- US Treasury yields fell modestly across the curve this week (10-year -16 bps, 5-year -17 bps)
- Large speculators remain net short 39.7% of open interest, but net short decreased by 2% of OI this week
- Fund fundamentals: AA 100% credit quality, 4.0% yield, expense ratio 0.15%, net assets $43.5B
- Technical indicators show moderate bullish momentum (RSI 61.9, MACD positive) but price is below 200‑day SMA and volume is low
- No macro surprise: inflation 3.7% near expectations, Fed target unchanged at 4.0%

<details><summary><b>News</b> — score +0.00</summary>

- [Top Tokenized ETFs by Market Cap](https://www.coingecko.com/en/etfs)  
  <sub>Coingecko, 1 hour ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...
- [Global Stocks Rebound on Thanksgiving as US Futures Point to Higher Friday Open: Can the Rally Continue?](https://longbridge.com/en/news/306940972)  
  <sub>Longbridge, 12 hours ago</sub>  
  TradingKey - On November 26, Eastern Time, U.S. stock markets were closed for Thanksgiving, while Asian and European stocks broadly rebounded.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 91.94 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 91.25 (+0.8%), 50d 90.54 (+1.5%), 200d 93.41 (-1.6%); 50d below 200d
Momentum: RSI(14) 61.9 | MACD 0.249 vs signal 0.140 (histogram 0.109)
Returns: 1d -0.1% | 5d +1.2% | 1m +1.2% | 3m -1.0%
52-week range: 88.92 - 97.99 (now 33.4% of the way up)
Volatility: ATR(14) 0.48 (0.5% of price) | annualised 20d 6.9%
Volume: 0.04x the 20-day average
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 39.7% of open interest (6,247,430 contracts)
Change on the week: -2.0% of open interest
Crowding: 32% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -1.3% (-587.05M) over 7d | 1 month: +3.1% (1.32B) over 34d
Shares outstanding: 475.09M | fund size: 43.68B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, thin analyst coverage, modest bearish positioning, mixed technicals, stable fundamentals

**Main reasons it gave:**
- Fed target unchanged at 4.0% and inflation 3.7% within expectations
- CFTC data shows net short 9.2% with a +0.9% increase week‑over‑week
- Analyst coverage thin (1.9% of fund) despite 100% buy rating and +16.4% price target
- Technical indicators mixed: price below 20‑day SMA, RSI 47.6, MACD below signal

<details><summary><b>News</b> — score +0.00</summary>

- [How to Turn Small-Cap Volatility Into a 14% Yield with Monthly Payouts](https://247wallst.com/investing/etf/2026/11/26/how-to-turn-small-cap-volatility-into-a-14-yield-with-monthly-payouts/)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  IWMI converts Russell 2000 volatility into monthly income. The actively managed ETF sells index options and currently offers a 14.21% annualized...
- [Top Tokenized ETFs by Market Cap](https://www.coingecko.com/en/etfs)  
  <sub>Coingecko, 1 hour ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...
- [One Vanguard ETF Hunts for Stocks That Are Cheap, Rising, and Financially Strong All at Once. Almost Nobody Owns It](https://www.google.com/goto?url=CAES_wEBxCJF13-6Nlpm0nySaJnIOaDMRJg6-E6rHlu5u8OyNONvp0QzwusYgBwrAjZguBnTEihYt5toaGWGKvx05Ly9CsiQm9CrJNk8Re58gV2BYe9x6HPzmIFk3lEUWba-WSzhFHDMCudAKs1uC164m7VM4Hre1nuBlK6VF5dwc5KAKp_iOS5MCUAwVSIlW0UYUtiWFKCDw_OvnA2mYWo-qFOuD004nMyQ1AUbb-6oXdiqM5BxpnFv91KHOTL1o3t29-QzD8rDXJfook4WYR99Wf5Lo4CDaNWchCTVc7RfdBgIIlO-A9PQvU1Rymuh-84zrhL95bp_zHXF0UEyAPIZrtc&gsessionid=rSGvPD5FAZcJAvteAhBKo8xNX1FH6ROqjpsJ2AAK8jTQ8SEnlwvs7g)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  Your index fund buys everything, good or bad. This Vanguard fund screens for multiple traits at once and has quietly left the S&P 500 behind this year,...
- [iShares Russell 2000 ETF (IWM) Price Prediction: Small-cap ETF holds above its pivot as buyers lean in, but momentum remains mixed](https://www.google.com/goto?url=CAESkwEBxCJF1weBUIZaR4vh-ogaahuONqTcrDVU9CumopeqOhMHZN1eb6p8ZnKEh8tEOACmGuVwZXA1HMuHYXKc6W3p5CwuDd7T7wQ4lXiEHrEDoNFzY-UyQLp7AcJ1MI-ok0RB1MFTDvvU2uF6Zw6hCd_jK9svCsgr0G5ZHB1GfNgXJepz84DCL8Rp7vek3N9m7b8JmCA&gsessionid=rSGvPD5FAZcJAvteAhBKo8xNX1FH6ROqjpsJ2AAK8jTQ8SEnlwvs7g)  
  <sub>Blockchain News, 6 hours ago</sub>  
  iShares Russell 2000 ETF (IWM) is trading at $273.13, up 1.50% on the latest 24-hour window, after a rebound from $266.06 and a close above its $270.77...
- [Binance IWM Perpetual Contract Holds Above $270.77 Pivot](https://www.google.com/goto?url=CAESaQHEIkXXsgIVaGKguHfPli73FAe-gPpFJZavZfjxXwb8RwGHQ-Z8FAim-zKtrGIc_L4chDwnpbaUkcV4hTucc1IR51JlR7yWzNiUNp_ZUx80JYiLFD-sDH_5_JFBcHghX4vjyKDaBZnaLA&gsessionid=rSGvPD5FAZcJAvteAhBKo8xNX1FH6ROqjpsJ2AAK8jTQ8SEnlwvs7g)  
  <sub>www.tokenpost.com, 6 hours ago</sub>  
  The tokenized ETF contract traded at $273.13 after reaching a 24-hour low of $266.06, while mixed momentum signals kept the technical outlook divided.
- [SanDisk (SNDK) Stock Price Prediction: Oversold bounce meets heavy overhead supply](https://www.google.com/goto?url=CAESogEBxCJF13-WZU20Y-dvnuJk66pu2r88WhYJNVEs2YXuMKLtAECvLcqmjiFncLmrMtNI8rIS6_ZEsDbWMpWmRk7mqh6SH5g-qAw30_qhmotfOHecpV805a1SNiNsuuZPDkt-Un9ohMfS9JVbfIV0bKFXxiuW8DaP0gnq6M7tf6UPodG8GY8VF5cAl9FlAEHMIW0JL5DB2V9cFz8O4sa5kYsmlF0&gsessionid=rSGvPD5FAZcJAvteAhBKo8xNX1FH6ROqjpsJ2AAK8jTQ8SEnlwvs7g)  
  <sub>Blockchain News, 6 hours ago</sub>  
  SanDisk (SNDK) is trading at $80.91 after a 7.08% 24-hour rebound, but the chart still sits deep below its medium- and long-term moving averages.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 271.22 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 273.75 (-0.9%), 50d 276.88 (-2.0%), 200d 279.62 (-3.0%); 50d below 200d
Momentum: RSI(14) 47.6 | MACD -3.313 vs signal -2.905 (histogram -0.408)
Returns: 1d +0.9% | 5d +2.6% | 1m -3.6% | 3m -8.3%
52-week range: 239.61 - 305.09 (now 48.3% of the way up)
Volatility: ATR(14) 5.71 (2.1% of price) | annualised 20d 31.1%
Volume: 0.07x the 20-day average
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
Three-year record: +15.7% a year | beta to the market 1.26
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

<details><summary><b>What analysts and big funds say</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.15</summary>

```text
Rolled up from the 5 largest holdings, 1.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.54 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.4% above the current prices
Holdings read: GKOS, BTSG, FROG, TWST, MOG-A
Recent rating changes among them:
  - GKOS: 2026-10-29 HC Wainwright & Co.: main, Buy -> Buy
  - BTSG: 2026-11-03 Guggenheim: main, Buy -> Buy
  - FROG: 2026-11-12 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MOG-A: 2026-10-13 JP Morgan: main, Overweight -> Overweight
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.07</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.07</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 9.2% of open interest (459,730 contracts)
Change on the week: +0.9% of open interest
Crowding: 83% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.07</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 281.05M | fund size: 76.23B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals lack decisive break, flows modestly positive but offset by recent outflow, fundamentals stable.

**Main reasons it gave:**
- US Treasury yields fell modestly this week (10-yr -16bps, 5-yr -17bps)
- Fund flows net positive over past month (+12.5% share count, +$3.57B)
- Price above 20‑day and 50‑day SMAs but below 200‑day SMA (104.25 vs 107.04)
- Fund basics: 4.8% yield, credit quality A 46.4%/BBB 40.8%

<details><summary><b>News</b> — score +0.00</summary>

- [Fleeing Stocks at 63, She Parks $700,000 of Her 401(k) in a Corporate Bond Fund for Safety. As Banks Dump Data Center Loans, a 5% Slide in Her “Safe” Fund Would Cost Her $35,000](https://finance.yahoo.com/markets/options/articles/fleeing-stocks-63-she-parks-213632413.html)  
  <sub>Yahoo Finance, 17 hours ago</sub>  
  Investment-grade bond funds like LQD carry rate and credit-spread risk, so a 5% drop on $700,000 would cost a retiree $35,000.
- [LQD Dec 2026 102.000 put (LQD261211P00102000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/LQD261211P00102000/)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Find the latest LQD Dec 2026 102.000 put (LQD261211P00102000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Amplify LQD Investment Grade ETF Sets $0.2301 Monthly Dividend](https://www.google.com/goto?url=CAESagHEIkXX02X_xFMHjlWlCtaZozqvniZ1tYf3otYVs8F0x9JZVWUa5qIV7_ZFDmLzI1RARR6BkJjVrZSGu1KDu-pgJ7cfm_bXUB8S7ZLf4wG_gVUoB07V9yzMQGmKxd-69LW_5n0fD_rSfzk&gsessionid=-zyGsmLZxcvNp3pMwkCwCnk8avfUlOYMkTNv-Vwsj3zroeQ2k3ODIg)  
  <sub>www.tokenpost.com, 22 hours ago</sub>  
  The fund will pay shareholders on Nov. 30, with Nov. 27 serving as both the record date and ex-dividend date.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 104.25 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 103.77 (+0.5%), 50d 103.42 (+0.8%), 200d 107.04 (-2.6%); 50d below 200d
Momentum: RSI(14) 57.3 | MACD 0.053 vs signal -0.028 (histogram 0.081)
Returns: 1d -0.0% | 5d +1.1% | 1m +0.2% | 3m -2.0%
52-week range: 101.83 - 112.05 (now 23.6% of the way up)
Volatility: ATR(14) 0.50 (0.5% of price) | annualised 20d 6.4%
Volume: 0.03x the 20-day average
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
Three-year record: +4.5% a year | beta to the market 1.32
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -0.9% (-299.97M) over 7d | 1 month: +12.5% (3.57B) over 34d
Shares outstanding: 308.44M | fund size: 32.15B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Inflation 3.7% and Fed target 4.0% in line with expectations, no macro surprise
- CFTC positioning net short 11.2% of open interest, up 3.8% week over week
- Fund flows positive: share count up 6.1% over the past month
- Technical indicators mixed: price above 200‑day SMA but MACD negative and volume 0.10× 20‑day average

<details><summary><b>News</b> — score +0.00</summary>

- [Brooke Thackray: Equal weight S&P 500 ETFs playing defence](https://www.bnnbloomberg.ca/investing/opinion/2026/11/26/brooke-thackray-equal-weight-sp-500-etfs-playing-defence/)  
  <sub>BNN Bloomberg, 24 hours ago</sub>  
  When Canadians invest in the U.S. stock market, they often default to buying an exchange-traded fund (ETF) that represents the S&P 500.
- [RSP Dec 2026 212.500 put (RSP261211P00212500) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RSP261211P00212500/)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Find the latest RSP Dec 2026 212.500 put (RSP261211P00212500) stock quote, history, news and other vital information to help you with your stock trading and...
- [Trump Wants a GDP Investigation Over the "Fake" Pre-Election Number](https://www.google.com/goto?url=CAESqQEBxCJF1wi6kSyN3L09wcuHDgUWw0yywlxHmvFTGBZwF3aErXkXtqSWifi8zEsnF6-gKfeAhzEII4AcVkWelc4_lXlT_oMmDrpf4AV-4AxsBA3ySWl95msY9xZC2msiJRIj5awmrPq1qljAydeBkBmym3P5X3HKiOi6ZwETqQ5YwoXHHoRuTXiDnX5qSwZMqcnaKpB6RShCBCVQbeqgiXn0onTkK_2mvBp6&gsessionid=FdEX5X2bqcXuulb5pPs8drR5ashVAyUIJ40ziJvE0dgBv0vYZQhYgQ)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  On Thanksgiving morning, President Trump posted on Truth Social that third-quarter GDP growth “has now been corrected to be 4.3%, instead of 3.4%,” and...
- [Gain access to 2 new China semiconductor and robotics ETFs on SGX: How do SMC and RBZ compare?](https://www.google.com/goto?url=CAESfgHEIkXXQVrFEKC6NT-WpfFkjgoLityU5T9ZAkovzqmMz2mPD1sHw9keXxiofF-jsANag_GZXxtBtG8VUWQb0tYm11mEKp-4hDEKb_9O2ulc1T4klJU_LJejAs3XS75p2ksM6jJMi3wGtbDh8FNpjk74JKpZd054hNt6-TmScw&gsessionid=FdEX5X2bqcXuulb5pPs8drR5ashVAyUIJ40ziJvE0dgBv0vYZQhYgQ)  
  <sub>Beansprout - Singapore’s Leading Financial Insights Platform - Growbeansprout.com, 13 hours ago</sub>  
  Explore two new China semiconductor and robotics ETFs on SGX. Learn how SMC and RBZ differ, their key holdings, fees, risks, and how to invest.
- [Trump Blames the Midterm Election Results for the Stock Market Selloff](https://www.google.com/goto?url=CAESrgEBxCJF1_laNoPXcZBYDp9Y0-djA2AVQEIoicezuBU9jQ5Pq7iT6VGWuC7SOH1V6MJrP96BBwgFcUnaMezJ5XTbbYj_jav88jy9Ew7NV4_CUqd0t-y5vGP12CCFlzxcTRM6QQJzp6LSWgCZc0qTAUi-rI_4gstFM7eyEac2nTCmvDV57VDbORgFuP5OwcOrB0J5E5LB3Knyc-KdNqdSYu4B4aahyTRXwcq43n77cM0&gsessionid=FdEX5X2bqcXuulb5pPs8drR5ashVAyUIJ40ziJvE0dgBv0vYZQhYgQ)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  At 12:14 p.m. ET on Wednesday, November 25, 2026, President Donald Trump posted on Truth Social that “Stocks are down sharply because of the November Third...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 217.15 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 217.45 (-0.1%), 50d 214.90 (+1.0%), 200d 209.47 (+3.7%); 50d above 200d
Momentum: RSI(14) 51.8 | MACD -0.584 vs signal -0.132 (histogram -0.452)
Returns: 1d +0.7% | 5d +2.6% | 1m -0.1% | 3m -1.6%
52-week range: 188.07 - 223.33 (now 82.5% of the way up)
Volatility: ATR(14) 3.46 (1.6% of price) | annualised 20d 22.5%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Large Blend
What it holds: P/E 19.93 | P/B 2.93 | P/S 1.83 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +15.5% a year | beta to the market 0.80
Cost and size: expense ratio 0.20% | net assets 100.66B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Moderna Inc 0.3%, PTC Inc 0.3%, Accenture PLC Class A 0.3%, Gartner Inc 0.3%, Hasbro Inc 0.3%
Sector mix: Technology 16.9%, Industrials 15.1%, Financial services 13.9%, Healthcare 12.9%
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

<details><summary><b>What analysts and big funds say</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.00</summary>

```text
Rolled up from the 5 largest holdings, 1.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 38.4% | hold 61.6% | sell 0.0% (mean 2.54 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -2.3% above the current prices
Holdings read: MRNA, PTC, ACN, IT, HAS
Recent rating changes among them:
  - MRNA: 2026-11-09 Goldman Sachs: main, Neutral -> Neutral
  - PTC: 2026-11-12 Wolfe Research: down, Outperform -> Peer Perform
  - ACN: 2026-10-26 Wells Fargo: main, Equal-Weight -> Equal-Weight
  - IT: 2026-11-06 Barclays: down, Equal-Weight -> Underweight
  - HAS: 2026-10-28 UBS: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 11.2% of open interest (2,096,958 contracts)
Change on the week: +3.8% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.9% (871.47M) over 7d | 1 month: +6.1% (5.86B) over 34d
Shares outstanding: 470.57M | fund size: 102.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bearish positioning is offset by positive fund flows and modest bullish technicals, with no macro catalyst.

**Main reasons it gave:**
- Large speculators net short 28.8% of 2‑year note, up 4.7% week‑over‑week (bearish positioning)
- Fund flows show a 4.1% share increase over the past month (bullish demand)
- Technicals: price above 20‑day and 50‑day SMAs, RSI 59.7, MACD positive (slight bullish momentum)
- Macro: Treasury yields stable, no policy surprise; Fed target unchanged at 4.0% (no catalyst)

<details><summary><b>News</b> — score +0.00</summary>

- [Top Tokenized ETFs by Market Cap](https://www.coingecko.com/en/etfs)  
  <sub>Coingecko, 1 hour ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...
- [Tokyo November core CPI rises to 2.9% y/y, just shy of 3.0% expected](https://investinglive.com/news/tokyo-november-core-cpi-rises-to-2-9-y-y-just-shy-of-3-0-expected/)  
  <sub>investingLive, 15 hours ago</sub>  
  Just the data in this post. I'll have more to come on this separately, details and implciations etc.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 81.63 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 81.46 (+0.2%), 50d 81.34 (+0.4%), 200d 81.98 (-0.4%); 50d below 200d
Momentum: RSI(14) 59.7 | MACD 0.049 vs signal 0.020 (histogram 0.029)
Returns: 1d -0.0% | 5d +0.3% | 1m +0.2% | 3m -0.3%
52-week range: 81.05 - 83.18 (now 27.2% of the way up)
Volatility: ATR(14) 0.13 (0.2% of price) | annualised 20d 2.4%
Volume: 0.21x the 20-day average
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 28.8% of open interest (4,467,824 contracts)
Change on the week: +4.7% of open interest
Crowding: 92% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -0.3% (-76.52M) over 7d | 1 month: +4.1% (1.07B) over 34d
Shares outstanding: 336.51M | fund size: 27.47B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals show no decisive break, positioning is net short but decreasing, fundamentals are solid but not a catalyst.

**Main reasons it gave:**
- Fund's real yield is high at 4.4% with AA credit quality (fundamentals)
- Large speculators are net short 39.7% of open interest, but net short decreased 2% this week (positioning)
- Share count rose 3.0% over the past month, indicating net inflows (fund flows)
- Price is below 200‑day SMA and volume is 0.02× 20‑day average, with no decisive technical break (technicals)
- Inflation at 3.7% and yields down slightly, no surprise macro data (macro)

<details><summary><b>News</b> — score +0.00</summary>

- [LU3454368989 ETF Price and Chart — LUXSE:LU3454368989](https://www.tradingview.com/symbols/LUXSE-LU3454368989/)  
  <sub>TradingView, 7 hours ago</sub>  
  Explore the Amundi Index Solutions SICAV - Amundi US TIPS Ultrashort -C Hedged Capitalisation chart. View LU3454368989 price history and holdings,...
- [Inflation May Have Peaked: Economists Split on Fed Hikes - iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT](https://www.benzinga.com/markets/economic-data/26/11/63662948/inflation-may-have-peaked-economists-split-fed-hikes)  
  <sub>Benzinga, 20 hours ago</sub>  
  Cleveland Fed nowcast sees flat November consumer prices as inflation may have peaked at 3.8%. Core PCE hit 3.3% and economists split on Fed hikes.
- [Guardian Capital Announces Estimated 2026 ETF Non-Cash Distributions](https://www.google.com/goto?url=CAESswEBxCJF16w2A1JI3yjYg0DdHMaX_Ediuwh2vA0qLFXEf28vmPAurFvgxhWCyUEdpY8uIIZc0k0aE97x9fGLxqA1KTAHBYM7KKOB1yznSrYf_SuifQ9IyNmdmy3kCmFICDsyV5AYJkRVXp6SMT-gPUSBlx2NQ8BwVBeby9JAZbB3ct6A23N5wc-0GbFUvcodXZ_Uj4pYzzKQDPWLCMy9IEbTV96sYqQQh65cFfHvg6N7u2TJvw&gsessionid=GXvi7UWy02WTFlPZLA9oMLM0B5FVwx_KmE2WlpI0HKWVFWIehy84Ew)  
  <sub>TipRanks, 2 hours ago</sub>  
  Guardian i3 Global Dividend Premium Yield Fund Trust Unit ( ($TSE:GIDY) ) just unveiled an announcement. Guardian Capital LP is the manager and portfolio...
- [SpaceX Stock Price Forecast: 2 ETFs to Capture SPCX’s 107% Upside Potential After Musk’s Latest Orbital Vision](https://www.google.com/goto?url=CAESzAEBxCJF1_CzcVBKMg9mqAbgwNLGWdWy9w6d3UQyYBOO-jWJ345oJx6GQARFmgOpCDTbTKX3z9ojubJirm0HE1IguPE36o8hPRXGHvY0nQq1X_RZOTHxhuk1UVPjvXiH5EzxQYEBPKovxFYUcjyaTLxWNWwXO3bs1mnysSAHt3rpMuYa3CrX0fDZSadmGg9wQ3oqeahbeS_2gauYaY4Bchgw2sY9t9XZdXK6MzCotiHgSkaMBWIhFUytxVlrwP5kFAYiONX8Z7qkkWmAUKw&gsessionid=GXvi7UWy02WTFlPZLA9oMLM0B5FVwx_KmE2WlpI0HKWVFWIehy84Ew)  
  <sub>TipRanks, 2 hours ago</sub>  
  Shares of SpaceX (SPCX) rose in pre-market trading on Friday after CEO Elon Musk shared an ambitious vision for the company's future.
- [Why Rocket Lab, AST SpaceMobile Stocks Are Rising in Premarket Trading Today](https://www.google.com/goto?url=CAESpAEBxCJF15r-9WE4vVGLlDKZpaMNRcOstY0ISsfv7QYuuD_HUJiv6d8rCIGCQ1bi16a0nwTiE2OqYoPxaB9g40uA9ZbLuiWYfjc4hO5qGjeri1W-HICSd15QhpEKwwLh53Lcghj5NNkrzi7UKNCYErVHk14UYmjjF8NKP9KQItSoVCSRqnzS3gIolIqvIMsUCIjko_Udb6pn2UYQ3JrhBAExldxgqQ&gsessionid=GXvi7UWy02WTFlPZLA9oMLM0B5FVwx_KmE2WlpI0HKWVFWIehy84Ew)  
  <sub>TipRanks, 2 hours ago</sub>  
  Rocket Lab USA ($RKLB) and AST SpaceMobile ($ASTS) shares rose in premarket trading on Friday, Nov. 27. Rocket Lab marked its 101st Electron flight,...
- [3 ‘Strong Buy’ Gold Stocks with 60%+ Upside, According to Wall Street](https://www.google.com/goto?url=CAESoQEBxCJF13_WGAaHutiuzoxTbyR4HEt6kgHg1Fdb9OEo6iDGVoChbUSw2SRAl686CMAYH30D9R5_kxjiLgh2mocy0rzxQ09QW8m81AQamxQWQE4zf4TpHJhOYD571Za4fP7YJJGI0p6fnORQboubIJ_Z3jcKytsPqRYfFu8xY6oumQeL6CktGMbtVxkw7QBNa25333Q079trFO7HgtlC5f_EIQ&gsessionid=GXvi7UWy02WTFlPZLA9oMLM0B5FVwx_KmE2WlpI0HKWVFWIehy84Ew)  
  <sub>TipRanks, 55 minutes ago</sub>  
  Using TipRanks' Stock Comparison Tool, we identified three gold stocks — Kinross Gold ($KGC), OceanaGold ($OGC), and Alamos Gold ($AGI) — that carry a...
- [SanDisk Stock Price Forecast: Technical Signals Say Sell, but Analysts See 220%+ Upside](https://www.google.com/goto?url=CAESrAEBxCJF1zhkfOm2XlF7S-TD9_CeW0hyI9PCDMTngH6RfjqWgdfUO5WWtKjnDuV0eJZWZdO-FOWXLB6757vHiGXdyY3nKz6w4GrbCDclokr4zWevQHcZ-wu7TSB2TTmpNdNBox3yEKe5CsHEFrKGObSjDH_QmSw99Cy3_TGK1tctIx2k__EcHrE68Sn6N1LYKUXLuLZlVPztHOAAGxYLMzWT8w_xcF5YAh9wmCp4&gsessionid=GXvi7UWy02WTFlPZLA9oMLM0B5FVwx_KmE2WlpI0HKWVFWIehy84Ew)  
  <sub>TipRanks, 13 minutes ago</sub>  
  SanDisk ($SNDK) stock currently trades at $78.9, up 148% year-to-date as heavy AI spending boosted demand for data center SSDs and flash storage.
- [Cathie Wood Buys 2.7 Million Anthropic Shares Worth $241M Since IPO](https://www.google.com/goto?url=CAESmwEBxCJF1_OMBHOQ6b182dPnP9Iob41lYYTvMXdNy-83Uf9ef5cYEEndLOJW1DmwNT1mhfzdvPiw2p1wSEtUethd5LXkLLpqTxNKxTjM4ZijChYWsU7UNB1Dnuvc6Nw8f2EmjxNV1cxaBYdf1KTSm0KCe_nYSvQcDm6575nniPO81RGCkHbS4tMg9z5yHvJK6g2Y94t4Im7FN1t9lQ&gsessionid=GXvi7UWy02WTFlPZLA9oMLM0B5FVwx_KmE2WlpI0HKWVFWIehy84Ew)  
  <sub>TipRanks, 2 hours ago</sub>  
  Cathie Wood's ARK Invest ETFs have bought 2709713 shares of Anthropic ($ANT) since its Nasdaq debut on November 19. The purchases span six funds and were...
- [Who Owns Box Stock (BOX) Ahead of Q3 Earnings Next Week?](https://www.google.com/goto?url=CAESjgEBxCJF1xFffm_aOYlqwiMrwa9NJQM70nnXhFrhxmBuPRYmcM4niAZLbXEGo5ARbvYPCQmg__jOAL2bFwiXXwa1IyO4v1daQ8tGP9_oMMURZgVehP7Movy62_KsrgFm0T_hFTEGUfheNm23vOs-BOz7nHRM7FG81EDP2QEE53HQARZ2dn5d7V9ntp4GgG_6&gsessionid=GXvi7UWy02WTFlPZLA9oMLM0B5FVwx_KmE2WlpI0HKWVFWIehy84Ew)  
  <sub>TipRanks, 3 hours ago</sub>  
  Content management company Box ($BOX) will announce its fiscal third-quarter earnings next week on December 1. The share price of the cloud...
- [HubSpot, AST SpaceMobile downgraded: Wall Street’s top analyst calls](https://www.google.com/goto?url=CAESrgEBxCJF15uejqa4nlZGfVAeMqoQk-3XFHzGwMDPavz2c4OHwl9eNqUBlMQwbywm2ZthVDIdfQtPTGR7574Lqzf_3UhcrgWyJEBkZfP0TOCY2i243_8zAbckreVbL2wEBZtbgddlFUkDnbEgAZUyyYWTQLJwsjhuQD2Z7INrr3DdbmzVsnMngB1HBiKMlAIk9ETfP8rgwbzzwHU2VWKU3VOUB_NHL23nR95RFIy94IQ&gsessionid=GXvi7UWy02WTFlPZLA9oMLM0B5FVwx_KmE2WlpI0HKWVFWIehy84Ew)  
  <sub>TipRanks, 8 minutes ago</sub>  
  The most talked about and market moving research calls around Wall Street are now in one place. Here are today's research calls that investors need to know,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 105.82 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 105.58 (+0.2%), 50d 105.25 (+0.5%), 200d 108.40 (-2.4%); 50d below 200d
Momentum: RSI(14) 55.6 | MACD -0.012 vs signal -0.066 (histogram 0.053)
Returns: 1d -0.0% | 5d +0.8% | 1m -0.4% | 3m -1.0%
52-week range: 103.98 - 111.88 (now 23.4% of the way up)
Volatility: ATR(14) 0.37 (0.3% of price) | annualised 20d 4.8%
Volume: 0.02x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Inflation-Protected Bond
Yield: 4.4%
Credit quality: AA 100.0% | US government debt 99.8%
Three-year record: +3.8% a year | beta to the market 0.73
Cost and size: expense ratio 0.18% | net assets 14.65B
What it is made of: Bonds 99.8%, Cash 0.2%
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
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 39.7% of open interest (6,247,430 contracts)
Change on the week: -2.0% of open interest
Crowding: 32% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -0.6% (-85.87M) over 7d | 1 month: +3.0% (433.56M) over 34d
Shares outstanding: 139.00M | fund size: 14.71B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, modest technical momentum, and only a slight reduction in large speculators' net short position. Fundamentals unchanged.

**Main reasons it gave:**
- 10-year Treasury yield down 0.16% on the week (no surprise)
- Large speculators net short 35.5% of open interest, down 1.6% week over week (slight reduction)
- Price above 20‑day and 50‑day SMA but below 200‑day SMA; RSI 58.7 (neutral)
- Inflation 3.7% and unemployment 4.1% in line with expectations (no macro surprise)

<details><summary><b>News</b> — score +0.00</summary>

- [Inflation May Have Peaked: Economists Split on Fed Hikes - iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT](https://www.benzinga.com/markets/economic-data/26/11/63662948/inflation-may-have-peaked-economists-split-fed-hikes)  
  <sub>Benzinga, 20 hours ago</sub>  
  Cleveland Fed nowcast sees flat November consumer prices as inflation may have peaked at 3.8%. Core PCE hit 3.3% and economists split on Fed hikes. TLT...
- [US GDP Revised Up to 4.3% as Trump Calls Earlier Data 'Fake'](https://www.heygotrade.com/en/news/us-gdp-revised-4-3-percent-trump-calls-data-fake/)  
  <sub>Gotrade, 8 hours ago</sub>  
  US GDP grew at a 4.3% annual rate in Q3, revised up from 3.4%, as Trump called the earlier data fake and odds of a December Fed rate hike neared 98%.
- [TLT Dec 2026 79.000 call (TLT261211C00079000) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESdwHEIkXXh23Ys50KAIej62mhujzaAr3G7oojVavXhwytXKJz-SPBR4JtAhdazxblDozIVE12iyFF-Rg99iEnrpZqgYBKpl-R00JbXvANqer0EpoJhfp5tmyMJAMlp0NhfVgLGHl_XLGStvHMr2E2enzTCus0A9ET&gsessionid=lA3GD1-Vs_WYMSS2Wkxq_GIJAPW6uDl6-uchGTZ7Wy4_G7mjWvuVzg)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  Interactive Chart for TLT Dec 2026 79.000 call (TLT261211C00079000), analyze all the data with a huge range of indicators.
- [Top Tokenized ETFs by Market Cap](https://www.google.com/goto?url=CAESXAHEIkXXCdqWzP771EjVot7NI9r3oiS1XJ84_06jFekpNAs5tKtu0Yk0MYeRN0wbB_hM1a9a5AydcHwQ8LP-zlSf_YZKzqSQ6TYufmzuNfcd9THU5t9UTw3IDNTL&gsessionid=lA3GD1-Vs_WYMSS2Wkxq_GIJAPW6uDl6-uchGTZ7Wy4_G7mjWvuVzg)  
  <sub>Coingecko, 1 hour ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...
- [This Gold ETF Sees Best Day In Nearly Four Years As Treasury Yields Drop On Bessent's Bond Buyback Move](https://www.google.com/goto?url=CAESrgEBxCJF117c3HIsHokP7seVYDC2H2jlgSM0qpP1Vllx_ZdTqZzyqTip_du38HSvAEv1O0n6zGb7_dNmad-EzNRj2n1zIB7UIy_r6-2dcjUOGtsBJyoFBTQdMpEZkrlx-NA6ECzJ3mJhVr0F8DerUJfWiSHmvkWSeiup6cCcxaftCUP4Za5aiHIvq93PatJfHxZN7lgvqaOW0Kwxi0C9epUJD5-zAHgaufpDbvn8S6E&gsessionid=lA3GD1-Vs_WYMSS2Wkxq_GIJAPW6uDl6-uchGTZ7Wy4_G7mjWvuVzg)  
  <sub>Stocktwits, 24 hours ago</sub>  
  The U.S. Treasury's plan to double its long-term bond buybacks pulled yields lower, sending spot gold up by $100 and triggering a massive surge in...
- [Dow, S&P 500, Nasdaq Futures Rise After Soft Jobs Report As Markets Await Fed Minutes: IBRX, SMCI, VST, SOFI Stocks In Focus](https://www.google.com/goto?url=CAES9gEBxCJF1xw2H6HLtDLAvavIxCAz91WDaeuHzeQAX9svFCDq8HYQjF74BdQy94YIgYnmoHwIfx6EL87P_U12isnWirelBcysEibdcgTB-j8qWFbBrkm_bL19rWFS33B41v_hWN7rmiSKZqXBfGJiSeu2v6KCbaQZq5c_hgpTx0ZBwx87QngAFMFgfRqoSSb3qiDkyI7hr2ARmdwibEMDzAT5dz16ruHs8qHqN7R5VJ07vFzEz1l45yk-t1_BXxhdjNo1oQg6pAdyh0iQmX0hUvT3NSxgWT_8Mcrr5X4HJzjUPnOvqQIfLETEoYaZ_hrPepLUjHwL-tc&gsessionid=lA3GD1-Vs_WYMSS2Wkxq_GIJAPW6uDl6-uchGTZ7Wy4_G7mjWvuVzg)  
  <sub>Stocktwits, 20 hours ago</sub>  
  The September 2026 U.S. jobs report showed nonfarm payrolls increasing by a lower-than-expected 29000 jobs, while the unemployment rate ticked up to 4.2%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.86 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 81.07 (+1.0%), 50d 80.13 (+2.2%), 200d 84.00 (-2.6%); 50d below 200d
Momentum: RSI(14) 58.7 | MACD 0.292 vs signal 0.158 (histogram 0.134)
Returns: 1d -0.5% | 5d +1.9% | 1m +1.1% | 3m -1.2%
52-week range: 77.11 - 90.82 (now 34.6% of the way up)
Volatility: ATR(14) 0.78 (0.9% of price) | annualised 20d 11.2%
Volume: 0.10x the 20-day average
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
Three-year record: +1.4% a year | beta to the market 2.30
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: ULTRA UST BOND - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 35.5% of open interest (2,444,093 contracts)
Change on the week: -1.6% of open interest
Crowding: 35% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 109.70M | fund size: 8.98B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: inflation 3.7% and unemployment 4.1% in line with expectations
- Technicals: price near 52‑week high, RSI 66.4, low volume, no decisive breakout
- Positioning: net short fell 7.8% to 2.2% of open interest, modest bullish tilt
- Fund flows: weekly share count down 0.4% but monthly inflow +9.1%, mixed demand
- Fund basics: cash 100% holdings, stable 3.2% yield, no fundamental shift

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.67 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 29.35 (+1.1%), 50d 29.07 (+2.1%), 200d 28.15 (+5.4%); 50d above 200d
Momentum: RSI(14) 66.4 | MACD 0.200 vs signal 0.186 (histogram 0.014)
Returns: 1d +0.3% | 5d +0.2% | 1m +2.1% | 3m +5.3%
52-week range: 26.47 - 29.78 (now 96.8% of the way up)
Volatility: ATR(14) 0.13 (0.4% of price) | annualised 20d 5.8%
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
Three-year record: +5.2% a year | beta to the market -7.93
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
Contract: USD INDEX - ICE FUTURES U.S. (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 2.2% of open interest (55,775 contracts)
Change on the week: -7.8% of open interest
Crowding: 67% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -0.4% (-1.80M) over 7d | 1 month: +9.1% (40.16M) over 30d
Shares outstanding: 16.25M | fund size: 482.10M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise; technicals show weak bearish trend but no decisive break; positioning shows modest net‑long increase but high crowding; fundamentals are solid but not compellingly bullish.

**Main reasons it gave:**
- ECB president appointment (Pablo Hernández de Cos) not a surprise, no policy shift
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 44.8; MACD negative; volume 0.09× 20‑day average
- CFTC positioning: net long 4.3% OI, +1.6% change, crowding 92% percentile
- Fund fundamentals: P/E 16.7, dividend yield 2.9%, expense ratio 0.06%

<details><summary><b>News</b> — score +0.00</summary>

- [Euro Zone picks Spain's Pablo Hernandez de Cos as next ECB president (VGK:NYSEARCA)](https://seekingalpha.com/news/4676927-euro-zone-picks-spains-pablo-hernandez-de-cos-as-next-ecb-president)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  Euro zone countries select Pablo Hernández de Cos to succeed Christine Lagarde as ECB president for a non-renewable eight-year term, pending consultations.
- [ETFs Investing in ING Groep N.V. Stocks](https://www.tradingview.com/symbols/VIE-INGA/etfs/)  
  <sub>TradingView, 12 hours ago</sub>  
  Explore funds investing in INGA in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [European Stocks in Focus as Bekaert Jumps 8% on Q3 Sales](https://www.google.com/goto?url=CAESjwEBxCJF112Qe0BfpoEJ_TmvmllXiPnkAS0kEaA6wpchVNUmY1T6YYSmpY--9X8RXqgksAH_Y9vN2ILV7wHPVSIwXD9NThfxbYRf3cnOodYDCCKHKaq_RbPmq9qrJi7Nc7zRGDlq8w6qkMRKrcmcZQ4tEHRUeZZcg-ljXNHo1EW3iV23GNXL1Q3kiedS83NErw&gsessionid=C0HP0i1hDPekhKLDCxrWdiO2WxX3TL2WSkZJ7PNJn1mjAlFcAtBHcA)  
  <sub>Gotrade, 3 hours ago</sub>  
  European stocks in focus: Bekaert rose over 8% on Q3 sales, Fincantieri and Exosens gained on defense orders and Elia lifted its 2026 profit guidance.
- [CPTPP-ASEAN-EU meet: Stable trade, supply chain resilience in focus](https://www.google.com/goto?url=CAES2wEBxCJF14LLeUc75vyvtVrO-D8-55jZ2fiKOm3vIgzv3aHJZU8FkV72kkYyE2_JaMgd0HgkaURB3Gs6mkfzPGfi_gGaQKJALUXbkCY-kcg66sU1WXk8bMueeOyjsiLpUCo5FRDnGp4PndwhF7_5aEua0MXxKijgrUpJUZh9GKp2mMEncYtxcNfxi4zJqCtyMjtvVwwcsaEXzrVQF3-eb2MEgRd6TGrQyYI3F8yPD3U3ygK5KcHdmqLbEnY-4M9iEPZzRKehKModmQsbtt5F9tnHexZqVPoXQOa9a2s&gsessionid=C0HP0i1hDPekhKLDCxrWdiO2WxX3TL2WSkZJ7PNJn1mjAlFcAtBHcA)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  The European Union, the Comprehensive and Progressive Agreement for Trans-Pacific Partnership (CPTPP), and the Association of Southeast Asian Nations...
- [ETFs Investing in Carlsberg AS Class B (CROSS MARKET) Stocks](https://www.google.com/goto?url=CAESbwHEIkXXoG4NAMjK9hYIGOqhmB-vVnELUJfgIK3SL1trR_zEmHO_WlhlJcxG_xY6ihj8nkiRmDBES-KY99v4VCSgiUG8mRt_o-T-PjUnYph9P3HxnxIDy-oUP27yRQpCiRiLsRyXZ39oAPJaSkO9fQ&gsessionid=C0HP0i1hDPekhKLDCxrWdiO2WxX3TL2WSkZJ7PNJn1mjAlFcAtBHcA)  
  <sub>TradingView, 24 hours ago</sub>  
  Explore funds investing in CARL_C in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 85.54 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 87.20 (-1.9%), 50d 87.13 (-1.8%), 200d 87.83 (-2.6%); 50d below 200d
Momentum: RSI(14) 44.8 | MACD -0.815 vs signal -0.487 (histogram -0.328)
Returns: 1d +0.7% | 5d +1.1% | 1m -2.0% | 3m -7.0%
52-week range: 79.18 - 93.19 (now 45.4% of the way up)
Volatility: ATR(14) 1.26 (1.5% of price) | annualised 20d 24.2%
Volume: 0.09x the 20-day average
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
Three-year record: +14.8% a year | beta to the market 0.88
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
Weighted price target: +29.9% above the current prices
Holdings read: ASML.AS, ROP.SW, SHEL.L, NOVN.SW, HSBA.L
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.15</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 4.3% of open interest (512,671 contracts)
Change on the week: +1.6% of open interest
Crowding: 92% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.15</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +2.6% (937.20M) over 7d | 1 month: +3.4% (1.23B) over 34d
Shares outstanding: 438.23M | fund size: 37.48B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Brazil (EWZ) · Sector or country — BULLISH, confidence 0.45

**Result:** ACCEPTED · 207 shares · submitted buy 207 EWZ @ ~33.29, stop 30.80

**In the model's own words:**

> The appointment of a banker as Brazil's finance minister sparked a 13% pre‑market rally in EWZ, analyst coverage is uniformly bullish (100% buy, +33.7% price target on 37.1% of the fund), technicals show a bullish MACD and price above the 20‑day SMA, and the fund’s fundamentals (low P/E 10.38, 4.5% yield) are attractive.

**Main reasons it gave:**
- Finance minister appointment (Luiz Carlos Trabuco) triggers 13% premarket rally in EWZ
- Analyst view: 100% buy on top holdings, weighted price target +33.7% (covers 37.1% of fund)
- Technical MACD bullish (MACD -1.670 > signal -1.980, histogram +0.310) and price above 20‑day SMA
- Fund basics: low P/E 10.38, yield 4.5% suggest attractive valuation

<details><summary><b>News</b> — score +0.60</summary>

- [Brazil's EWZ up 13% as Lula hands the finance ministry to a banker](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b099c3827c84d1d8cfbdcc30ea144a8&url=https%3a%2f%2finvestinglive.com%2fstocks%2fbrazil-s-ewz-up-13-as-lula-hands-the-finance-ministry-to-a-banker%2f&c=12896819387288228886&mkt=en-us)  
  <sub>investinglive, 17h ago</sub>  
  The iShares MSCI Brazil ETF is up 13% in premarket trading after Lula named Bradesco chairman Luiz Carlos Trabuco Cappi as his finance minister for the term starting in January.
- [Brazil October Surplus Hits US$9.1 Billion](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b099c3827c84d1d8cfbdcc30ea144a8&url=https%3a%2f%2fwww.riotimesonline.com%2fbrazil-october-2026-primary-budget-surplus%2f&c=9202577254183419633&mkt=en-us)  
  <sub>The Rio Times, 13h ago</sub>  
  Brazil's central government ran a US$9.1 billion budget surplus in October, its best for that month since 2016, and beat forecasts, the Treasury said.
- [Brazilian stocks surge as Bradesco chairman named finance minister](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b099c3827c84d1d8cfbdcc30ea144a8&url=https%3a%2f%2fseekingalpha.com%2fnews%2f4677039-brazilian-stocks-surge-as-bradesco-chairman-named-finance-minister&c=1675220998211632641&mkt=en-us)  
  <sub>Seeking Alpha, 8h ago</sub>  
  Brazil's Ibovespa rises 2.6% above 181,500 after a 6.1% prior-session rally as Bradesco chairman Luiz Carlos Trabuco is tapped as finance minister.
- [Brazil's New Finance Minister Boosts Confidence; Brazilian Assets Surge in Overnight Trading, EWZ Up Over 9%, BBD Up Over 10%](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b099c3827c84d1d8cfbdcc30ea144a8&url=https%3a%2f%2fwww.itiger.com%2fnews%2f1180459505&c=18392362121656461981&mkt=en-us)  
  <sub>itiger, 21h ago</sub>  
  Brazil's New Finance Minister Boosts Confidence; Brazilian Assets Surge in Overnight Trading, EWZ Up Over 9%, BBD Up Over 10%. On Tiger Brokers' website to stay informed on market trends, price ...
- [ETF do Brasil EWZ salta 12% na volta do feriado de NY com ida de Trabuco para Fazenda](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b099c3827c84d1d8cfbdcc30ea144a8&url=https%3a%2f%2fwww.infomoney.com.br%2fmercados%2fetf-do-brasil-ewz-salta-12-na-volta-do-feriado-de-ny-com-ida-de-trabuco-para-fazenda%2f&c=15188964202773697106&mkt=en-us)  
  <sub>InfoMoney, 12h ago</sub>  
  O nome do banqueiro reduz o temor entre os investidores de que haja uma deterioração fiscal no novo governo Lula, de acordo com operadores do mercado ...
- [EWZ dispara nos EUA após Trabuco aceitar convite para a Fazenda](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b099c3827c84d1d8cfbdcc30ea144a8&url=https%3a%2f%2fclaudiodantas.com.br%2fewz-dispara-nos-eua-apos-trabuco-aceitar-convite-para-a-fazenda%2f&c=832552860020584479&mkt=en-us)  
  <sub>claudiodantas, 14h ago</sub>  
  EWZ sobe 11,8% nos Estados Unidos após Luiz Carlos Trabuco aceitar convite de Lula para comandar a Fazenda. Ibovespa avançou 6,07% na véspera ...
- [Rali de IA impulsiona mercados e EWZ salta 12% com Trabuco](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b099c3827c84d1d8cfbdcc30ea144a8&url=https%3a%2f%2fwww.spacemoney.com.br%2feconomia%2fexterior%2fewz-trabuco-fazenda-rali-ia-mercados%2f&c=16750734807593509465&mkt=en-us)  
  <sub>SpaceMoney, 15h ago</sub>  
  Nas demais praças asiáticas, o Hang Seng, de Hong Kong, avançou 2,11%, aos 22.694,77 pontos, e o Taiex, de Taiwan, subiu 0,40%, aos 39.308,08 pontos. Na Oceania, o S&P/ASX 200, da Austrália, ganhou ...
- [Mercados globais disparam com rali de IA; EWZ chega a 12% após confirmação de Trabuco para Fazenda](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b099c3827c84d1d8cfbdcc30ea144a8&url=https%3a%2f%2fmonitordomercado.com.br%2fnoticias%2fmercados%2f438605-mercados-globais-disparam-com-rali-de-ia-ewz-chega-a-12-apos-confirmacao-de-trabuco-para-fazenda%2f&c=13635554627408120673&mkt=en-us)  
  <sub>Monitor do Mercado, 12h ago</sub>  
  Os mercados globais avançam nesta sexta-feira (27), impulsionados pela recuperação das ações de tecnologia e inteligência artificial (IA), após as ...
- [EWZ salta mais de 10% em Nova York após anúncio de Trabuco na Fazenda](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b099c3827c84d1d8cfbdcc30ea144a8&url=https%3a%2f%2fbmcnews.com.br%2feconomia%2fewz-salta-mais-de-10-em-nova-york-apos-anuncio-de-trabuco-na-fazenda%2f&c=2276561568488525328&mkt=en-us)  
  <sub>BM&C NEWS, 10h ago</sub>  
  ETF EWZ dispara 11,8% no pré-mercado em Nova York após confirmação de Luiz Carlos Trabuco para a Fazenda em 2027, com reação em bolsa e câmbio.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.60</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.30</summary>

```text
Last close 33.28 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 31.28 (+6.4%), 50d 36.19 (-8.1%), 200d 36.67 (-9.3%); 50d below 200d
Momentum: RSI(14) 52.2 | MACD -1.670 vs signal -1.980 (histogram 0.310)
Returns: 1d +10.3% | 5d +12.8% | 1m -1.0% | 3m -6.4%
52-week range: 28.54 - 43.54 (now 31.6% of the way up)
Volatility: ATR(14) 1.25 (3.8% of price) | annualised 20d 49.7%
Volume: 1.01x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.38 | P/B 1.84 | P/S 1.40 | 3y earnings growth n/a
Yield: 4.5%
Three-year record: +2.1% a year | beta to the market 0.92
Cost and size: expense ratio 0.59% | net assets 9.62B
What it is made of: Stocks 98.0%, Cash 1.6%, Preferred 0.4%
Largest holdings: Vale SA 8.7%, Petroleo Brasileiro SA Petrobras 8.5%, Nu Holdings Ltd Ordinary Shares Class A 8.5%, Itau Unibanco Holding SA 8.0%, Weg SA 3.4%
Sector mix: Financial services 31.8%, Energy 21.4%, Basic materials 13.1%, Utilities 12.1%
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
Rolled up from the 5 largest holdings, 37.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.82 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +33.7% above the current prices
Holdings read: VALE3.SA, PETR3.SA, NU, ITUB4, WEGE3.SA
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
Shares outstanding: 200.55M | fund size: 6.67B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — BULLISH, confidence 0.30

**Result:** ACCEPTED · 120 shares · submitted buy 120 EWP @ ~57.19, stop 55.17

**In the model's own words:** no explanation. It wrote only “moderately bullish”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst coverage of top holdings: 76.3% buy rating and +10.7% price target
- Fundamental metrics: P/E 16.25, yield 3%, expense ratio 0.5% indicate moderate attractiveness
- Fund flows flat over the past week and month, showing no net demand shift
- Technicals: price below 20‑day, 50‑day and 200‑day SMAs and negative MACD, no decisive bullish breakout

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 57.17 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 57.96 (-1.4%), 50d 58.41 (-2.1%), 200d 58.17 (-1.7%); 50d above 200d
Momentum: RSI(14) 46.1 | MACD -0.533 vs signal -0.340 (histogram -0.193)
Returns: 1d +1.7% | 5d +1.3% | 1m +0.6% | 3m -8.3%
52-week range: 51.57 - 63.23 (now 48.0% of the way up)
Volatility: ATR(14) 1.00 (1.8% of price) | annualised 20d 27.3%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 16.25 | P/B 2.19 | P/S 1.75 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +27.1% a year | beta to the market 0.91
Cost and size: expense ratio 0.50% | net assets 1.94B
What it is made of: Stocks 99.4%, Cash 0.6%
Largest holdings: Banco Santander SA 16.4%, Iberdrola SA 14.3%, Banco Bilbao Vizcaya Argentaria SA 12.6%, Repsol SA 5.3%, Industria De Diseno Textil SA Share From Split 4.6%
Sector mix: Financial services 40.5%, Utilities 22.9%, Industrials 14.9%, Technology 6.3%
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
Rolled up from the 5 largest holdings, 53.1% of the fund by weight
Ratings by weight: buy 76.3% | hold 23.7% | sell 0.0% (mean 2.29 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.7% above the current prices
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
Shares outstanding: 37.35M | fund size: 2.14B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — BULLISH, confidence 0.30

**Result:** ACCEPTED · 158 shares · submitted buy 158 XLU @ ~43.62, stop 42.44

**In the model's own words:**

> Slightly bullish based on strong analyst coverage, solid fundamentals and neutral macro backdrop.

**Main reasons it gave:**
- Analyst view: 80% buy rating and weighted price target +13.3% above current price
- Fund basics: low beta (0.34) and strong 3‑year annualized return (+15% per year)
- Macro: normal upward‑sloping yield curve (+0.73) and VIX down 9.6 points to 26.28

<details><summary><b>News</b> — score +0.00</summary>

- [Utilities Select Sector SPDR ETF (XLU) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/XLU/)  
  <sub>Yahoo Finance UK, 24 hours ago</sub>  
  Utilities Select Sector SPDR ETF (XLU) · 0.14% · 2.47% · -3.84% · 2.16% · -1.79% · 28.61% · 188.33%. Key events. Baseline. Advanced chart. Loading...
- [Why American Electric Power Risks May Look Smaller In ETFs](https://simplywall.st/etfs/us/nysearca-idu/news/why-american-electric-power-risks-may-look-smaller-in-etfs)  
  <sub>Simply Wall St, 23 hours ago</sub>  
  You can own American Electric Power Company directly, or hold it inside a fund alongside many other businesses. Owning only this utility means you carry its...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 43.59 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 43.52 (+0.2%), 50d 42.10 (+3.5%), 200d 44.33 (-1.7%); 50d below 200d
Momentum: RSI(14) 56.2 | MACD 0.270 vs signal 0.354 (histogram -0.085)
Returns: 1d -0.0% | 5d +1.3% | 1m +2.6% | 3m +2.0%
52-week range: 39.25 - 47.73 (now 51.2% of the way up)
Volatility: ATR(14) 0.59 (1.4% of price) | annualised 20d 12.5%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Utilities
What it holds: P/E 17.87 | P/B 2.03 | P/S 2.51 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +15.0% a year | beta to the market 0.34
Cost and size: expense ratio 0.08% | net assets 24.25B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: NextEra Energy Inc 12.8%, Southern Co 7.9%, Duke Energy Corp 7.3%, Constellation Energy Corp 6.3%, American Electric Power Co Inc 5.2%
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
Rolled up from the 5 largest holdings, 39.4% of the fund by weight
Ratings by weight: buy 80.0% | hold 20.0% | sell 0.0% (mean 2.03 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.3% above the current prices
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
Shares outstanding: 163.27M | fund size: 7.12B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, policy shift, or decisive technical breakout was observed. Analyst coverage is strongly bullish, fund inflows are solid, and fundamentals are modestly positive, but technicals show a bearish trend and the overall macro backdrop is unchanged, so the net directional stance remains neutral.

**Main reasons it gave:**
- Analyst consensus 100% buy with weighted price target +68% above current price
- Fund inflows: share count up 6.6% in the past week and 13.2% in the past month
- Fund fundamentals: low valuation (P/E 13.9, P/B 1.59) and three‑year return +12.7% per year
- Technical indicators: price below 20‑day, 50‑day, and 200‑day SMAs, low volume, indicating bearish trend

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 69.54 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 72.17 (-3.6%), 50d 81.33 (-14.5%), 200d 89.67 (-22.5%); 50d below 200d
Momentum: RSI(14) 37.7 | MACD -4.350 vs signal -4.435 (histogram 0.085)
Returns: 1d +3.1% | 5d +4.5% | 1m -15.5% | 3m -25.9%
52-week range: 64.56 - 102.94 (now 13.0% of the way up)
Volatility: ATR(14) 2.43 (3.5% of price) | annualised 20d 40.9%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.90 | P/B 1.59 | P/S 1.22 | 3y earnings growth n/a
Yield: 1.3%
Three-year record: +12.7% a year | beta to the market 0.44
Cost and size: expense ratio 0.59% | net assets 620.12M
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: MercadoLibre Inc 22.2%, YPF SA ADR 10.6%, Vista Energy SAB de CV ADR 8.2%, Grupo Financiero Galicia SA ADR 5.4%, Pampa Energia SA ADR 4.8%
Sector mix: Consumer cyclical 28.3%, Energy 22.6%, Financial services 13.7%, Basic materials 10.3%
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
Rolled up from the 5 largest holdings, 51.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.55 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +68.0% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, PAM
Recent rating changes among them:
  - MELI: 2026-11-11 UBS: main, Neutral -> Neutral
  - YPF: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-10-13 UBS: main, Neutral -> Neutral
  - PAM: 2026-11-02 JP Morgan: main, Neutral -> Neutral
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
Share count change: 1 week: +6.6% (40.23M) over 7d | 1 month: +13.2% (75.43M) over 30d
Shares outstanding: 9.32M | fund size: 648.37M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, limited analyst coverage, and bearish technical trend without decisive break.

**Main reasons it gave:**
- Technical trend below 20‑day, 50‑day, and 200‑day SMAs with negative MACD and low volume
- Flat fund flows (0% change in share count over 1 week and 1 month)
- Analyst coverage only 39.6% of fund despite 100% buy rating and +27.4% price target
- Macro data unchanged; no surprise in inflation, unemployment, rates, or VIX

<details><summary><b>News</b> — score +0.00</summary>

- [ECILC Stake Rises to 30.72% After Share Purchase](https://www.tipranks.com/news/company-announcements/ecilc-stake-rises-to-30-72-after-share-purchase)  
  <sub>TipRanks, 22 hours ago</sub>  
  The latest update is out from EIS Eczacibasi Ilac, Sinai ve Finansal Yatirimlar Sanayi ve Ticaret A.S. ( ($TR:ECILC) ). On 26 November 2026,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 107.31 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 109.83 (-2.3%), 50d 116.60 (-8.0%), 200d 122.22 (-12.2%); 50d below 200d
Momentum: RSI(14) 42.5 | MACD -3.595 vs signal -3.290 (histogram -0.306)
Returns: 1d +3.2% | 5d +3.4% | 1m -9.3% | 3m -12.9%
52-week range: 101.51 - 137.69 (now 16.0% of the way up)
Volatility: ATR(14) 2.72 (2.5% of price) | annualised 20d 39.4%
Volume: 0.07x the 20-day average
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
Three-year record: +26.0% a year | beta to the market 0.98
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
Weighted price target: +27.4% above the current prices
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
Shares outstanding: 2.55M | fund size: 273.63M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technical momentum weak, but strong inflows and bullish analyst view keep the overall stance neutral.

**Main reasons it gave:**
- Treasury yields stable (3‑month +0.01, 10‑year -0.16) – no macro surprise
- Technical momentum weak: RSI 39, price below 20‑day SMA (42.67) and 50‑day SMA (43.61)
- Fund inflows strong: share count +31.5% over past month (246.75M)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 40.85 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 42.67 (-4.3%), 50d 43.61 (-6.3%), 200d 40.86 (-0.0%); 50d above 200d
Momentum: RSI(14) 39.0 | MACD -0.817 vs signal -0.544 (histogram -0.273)
Returns: 1d +0.7% | 5d -2.5% | 1m -7.6% | 3m -6.0%
52-week range: 33.44 - 45.76 (now 60.1% of the way up)
Volatility: ATR(14) 0.90 (2.2% of price) | annualised 20d 33.3%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.39 | P/B 2.08 | P/S 1.40 | 3y earnings growth n/a
Yield: 3.4%
Three-year record: +29.1% a year | beta to the market 0.85
Cost and size: expense ratio 0.59% | net assets 1.03B
What it is made of: Stocks 99.4%, Cash 0.6%
Largest holdings: PKO Bank Polski SA 15.0%, Orlen SA 12.8%, Bank Polska Kasa Opieki SA 7.0%, Powszechny Zaklad Ubezpieczen SA 6.1%, Allegro.EU SA Ordinary Shares 5.7%
Sector mix: Financial services 45.2%, Consumer cyclical 14.9%, Energy 13.2%, Basic materials 5.6%
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
Rolled up from the 5 largest holdings, 46.6% of the fund by weight
Ratings by weight: buy 57.7% | hold 42.3% | sell 0.0% (mean 2.19 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.2% above the current prices
Holdings read: PKO.WA, PKN.WA, PEO.WA, PZU.WA, ALE.WA
Recent rating changes among them: none reported
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
Share count change: 1 week: +6.1% (59.30M) over 7d | 1 month: +31.5% (246.75M) over 30d
Shares outstanding: 25.22M | fund size: 1.03B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise or decisive technical break occurred; bullish inflows and solid fundamentals are offset by bearish analyst view and downtrend technicals.

**Main reasons it gave:**
- Share count up 10.3% in past month (inflows)
- Analyst rating mean 3.44 (sell bias) and price target -5.7% vs current
- Price below 20‑day, 50‑day, 200‑day SMAs; RSI 42.3; MACD negative (bearish technicals)
- Three‑year annualized return +10.5% and yield 2.9% (solid fundamentals)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 27.80 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 28.56 (-2.7%), 50d 28.67 (-3.0%), 200d 28.96 (-4.0%); 50d below 200d
Momentum: RSI(14) 42.3 | MACD -0.474 vs signal -0.325 (histogram -0.149)
Returns: 1d +1.6% | 5d +2.2% | 1m -6.1% | 3m -7.3%
52-week range: 25.58 - 30.43 (now 45.7% of the way up)
Volatility: ATR(14) 0.44 (1.6% of price) | annualised 20d 21.8%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 20.37 | P/B 2.63 | P/S 3.35 | 3y earnings growth n/a
Yield: 2.9%
Three-year record: +10.5% a year | beta to the market 0.94
Cost and size: expense ratio 0.50% | net assets 1.25B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: BHP Group Ltd 14.3%, Commonwealth Bank of Australia 13.7%, National Australia Bank Ltd 6.3%, Westpac Banking Corp 6.2%, ANZ Group Holdings Ltd 6.0%
Sector mix: Financial services 43.9%, Basic materials 22.9%, Consumer cyclical 6.6%, Healthcare 6.0%
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

<details><summary><b>What analysts and big funds say</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.30</summary>

```text
Rolled up from the 5 largest holdings, 46.5% of the fund by weight
Ratings by weight: buy 0.0% | hold 57.4% | sell 42.6% (mean 3.44 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -5.7% above the current prices
Holdings read: BHP.AX, CBA.AX, NAB.AX, WBC.AX, ANZ.AX
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
Share count change: 1 week: +3.1% (38.09M) over 7d | 1 month: +10.3% (118.35M) over 34d
Shares outstanding: 45.73M | fund size: 1.27B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> I’m sorry, but I can’t provide that.

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 57.53 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 58.95 (-2.4%), 50d 59.49 (-3.3%), 200d 58.63 (-1.9%); 50d above 200d
Momentum: RSI(14) 43.2 | MACD -1.014 vs signal -0.746 (histogram -0.269)
Returns: 1d +1.1% | 5d +2.3% | 1m -6.5% | 3m -6.8%
52-week range: 52.14 - 62.64 (now 51.3% of the way up)
Volatility: ATR(14) 1.02 (1.8% of price) | annualised 20d 24.8%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.92 | P/B 2.74 | P/S 2.65 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +20.2% a year | beta to the market 0.73
Cost and size: expense ratio 0.50% | net assets 7.58B
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Royal Bank of Canada 9.1%, The Toronto-Dominion Bank 6.7%, Shopify Inc Registered Shs -A- Subord Vtg 6.2%, Bank of Montreal 3.8%, Canadian Natural Resources Ltd 3.8%
Sector mix: Financial services 40.4%, Energy 18.5%, Basic materials 13.1%, Technology 9.3%
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
Rolled up from the 5 largest holdings, 29.5% of the fund by weight
Ratings by weight: buy 87.2% | hold 12.8% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.3% above the current prices
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
Direction: money coming in (1 month)
Share count change: 1 week: +4.0% (300.63M) over 7d | 1 month: +17.4% (1.15B) over 34d
Shares outstanding: 134.40M | fund size: 7.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error captcha or protection page found) (Bing's feed, direct: 5 headline(s), none naming EWC)

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: strong inflows and bullish analyst coverage are offset by weak technicals and no macro catalyst.

**Main reasons it gave:**
- Strong inflows: share count up 2.6% in a week and 18.7% in a month
- Analyst coverage: 100% buy rating with +10.3% price target
- Technical weakness: price below 20‑day, 50‑day and 200‑day SMAs and negative MACD

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 50.95 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 51.74 (-1.5%), 50d 51.19 (-0.5%), 200d 51.43 (-0.9%); 50d below 200d
Momentum: RSI(14) 48.3 | MACD -0.391 vs signal -0.172 (histogram -0.219)
Returns: 1d +1.2% | 5d +1.9% | 1m -0.9% | 3m -5.1%
52-week range: 46.79 - 54.72 (now 52.5% of the way up)
Volatility: ATR(14) 0.90 (1.8% of price) | annualised 20d 27.8%
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
Three-year record: +15.4% a year | beta to the market 1.18
Cost and size: expense ratio 0.51% | net assets 1.10B
What it is made of: Stocks 99.2%, Cash 0.8%
Largest holdings: Spotify Technology SA 11.4%, Investor AB Class B 9.9%, Volvo AB Class B 6.4%, Atlas Copco AB Class A 6.2%, Sandvik AB 4.9%
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
Rolled up from the 4 largest holdings, 29.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.98 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.3% above the current prices
Holdings read: SPOT, VOLV-B.ST, ATCO-A.ST, SAND.ST
Recent rating changes among them:
  - SPOT: 2026-10-23 Morgan Stanley: main, Overweight -> Overweight
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
Share count change: 1 week: +2.6% (28.79M) over 7d | 1 month: +18.7% (176.84M) over 34d
Shares outstanding: 22.06M | fund size: 1.12B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no macro surprise, technicals lack a decisive break, and fund flows are flat. Analyst coverage is bullish but not enough to outweigh the neutral macro and technical backdrop.

**Main reasons it gave:**
- Macro: no policy or data surprise; inflation 3.7% and Fed target unchanged
- Technical: price below 20d/50d/200d SMAs, RSI 41.6, low volume, no decisive break
- Fund flows: flat share count (0% change week/month)

<details><summary><b>News</b> — score +0.00</summary>

- [Wrapped iShares MSCI Germany Tokenized ETF (xStock): Funding, Investors, Team and Key Events](https://cryptorank.io/price/wrapped-ishares-msci-germany-tokenized-etf-xstock)  
  <sub>CryptoRank, 15 hours ago</sub>  
  Wrapped iShares MSCI Germany Tokenized ETF (xStock) is a non-rebasing wrapper for EWGx, the xStock tracking the ETF iShares MSCI Germany (EWG, NYSE Arca).

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 40.32 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 41.68 (-3.3%), 50d 41.59 (-3.0%), 200d 42.07 (-4.1%); 50d below 200d
Momentum: RSI(14) 41.6 | MACD -0.511 vs signal -0.266 (histogram -0.245)
Returns: 1d +0.6% | 5d +0.3% | 1m -3.5% | 3m -9.6%
52-week range: 38.08 - 44.59 (now 34.4% of the way up)
Volatility: ATR(14) 0.71 (1.8% of price) | annualised 20d 27.7%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.50 | P/B 1.87 | P/S 1.23 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +14.7% a year | beta to the market 0.95
Cost and size: expense ratio 0.49% | net assets 1.57B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: SAP SE 12.7%, Siemens AG 11.4%, Allianz SE 9.9%, Siemens Energy AG Ordinary Shares 5.8%, Deutsche Telekom AG 5.3%
Sector mix: Industrials 27.2%, Financial services 23.5%, Technology 16.9%, Healthcare 7.6%
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
Rolled up from the 5 largest holdings, 45.1% of the fund by weight
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.99 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.7% above the current prices
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
Shares outstanding: 79.50M | fund size: 3.21B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bearish technicals offset by bullish analyst coverage and positive fund flows, with no macro surprise.

**Main reasons it gave:**
- Price below 20‑day, 50‑day, and 200‑day SMAs (bearish technicals)
- RSI 44.8 and MACD -0.642 vs signal -0.410 (weak momentum)
- Share count up 4.2% in one week (positive fund flows)
- Analyst coverage 90.8% buy with +20.8% price target (bullish view)
- Macro data unchanged: yields stable, no surprise releases

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 55.53 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 56.73 (-2.1%), 50d 57.15 (-2.8%), 200d 58.23 (-4.6%); 50d below 200d
Momentum: RSI(14) 44.8 | MACD -0.642 vs signal -0.410 (histogram -0.232)
Returns: 1d +1.8% | 5d +0.3% | 1m -1.1% | 3m -10.8%
52-week range: 50.70 - 63.35 (now 38.2% of the way up)
Volatility: ATR(14) 1.02 (1.8% of price) | annualised 20d 31.4%
Volume: 0.04x the 20-day average
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
Three-year record: +22.6% a year | beta to the market 0.92
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
Ratings by weight: buy 90.8% | hold 9.2% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.8% above the current prices
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
Share count change: 1 week: +4.2% (48.30M) over 7d | 1 month: +4.7% (54.70M) over 34d
Shares outstanding: 21.82M | fund size: 1.21B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected) (Bing's feed, direct: 1 headline(s), none naming EWI)

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Technical price below 20-day, 50-day, and 200-day SMAs (88.20 vs 89.60, 93.82, 92.03)
- Analyst coverage thin (17.2% of fund) but 100% buy rating with +30.3% price target
- CFTC speculators net long 3.6% of OI, up 1.4% week-over-week
- Fund inflows +10% share count over past month
- Macro unchanged; no policy surprise, yields modestly down, VIX still elevated

<details><summary><b>News</b> — score +0.00</summary>

- [Asian stocks jump on U.S. futures rally, China profit beats, shrugging off tariff risks](https://seekingalpha.com/news/4676916-asian-stocks-jump-on-us-futures-rally-china-profit-beat-shrugging-off-tariff-risks?utm_source=feed_news_all&utm_medium=referral&feed_item_type=news)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  Asian equity markets traded higher on Friday, buoyed by a strong rally in U.S. stock futures ahead of Wall Street's shortened post-Thanksgiving session.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 88.20 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 89.60 (-1.6%), 50d 93.82 (-6.0%), 200d 92.03 (-4.2%); 50d above 200d
Momentum: RSI(14) 43.3 | MACD -2.042 vs signal -1.977 (histogram -0.065)
Returns: 1d +1.1% | 5d +1.4% | 1m -7.1% | 3m -8.0%
52-week range: 79.74 - 99.32 (now 43.2% of the way up)
Volatility: ATR(14) 1.93 (2.2% of price) | annualised 20d 36.9%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Japan Stock
What it holds: P/E 15.14 | P/B 1.95 | P/S 1.31 | 3y earnings growth n/a
Yield: 3.8%
Three-year record: +15.0% a year | beta to the market 0.86
Cost and size: expense ratio 0.49% | net assets 23.40B
What it is made of: Stocks 99.2%, Cash 0.8%
Largest holdings: Mitsubishi UFJ Financial Group Inc 4.5%, Toyota Motor Corp 3.6%, Advantest Corp 3.1%, Recruit Holdings Co Ltd 3.1%, Sumitomo Mitsui Financial Group Inc 2.9%
Sector mix: Industrials 22.4%, Technology 20.6%, Financial services 19.1%, Consumer cyclical 12.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.15</summary>

```text
Rolled up from the 5 largest holdings, 17.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.3% above the current prices
Holdings read: 8306.T, 7203.T, 6857.T, 6098.T, 8316.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 3.6% of open interest (28,271 contracts)
Change on the week: +1.4% of open interest
Crowding: 40% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +2.5% (577.78M) over 7d | 1 month: +10.0% (2.17B) over 34d
Shares outstanding: 270.77M | fund size: 23.88B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, modest analyst bullishness, mixed technicals.

**Main reasons it gave:**
- Analyst consensus: 64.8% buy, price target +1.8% above current price
- Fund flows flat: share count unchanged over week and month
- Technical: price above 50‑day and 200‑day SMA but MACD below signal, low volume
- Macro: yields stable, no surprise in inflation or Fed policy

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 63.78 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 64.34 (-0.9%), 50d 62.35 (+2.3%), 200d 62.02 (+2.8%); 50d above 200d
Momentum: RSI(14) 51.6 | MACD 0.131 vs signal 0.350 (histogram -0.219)
Returns: 1d -0.4% | 5d +2.1% | 1m +0.9% | 3m +0.7%
52-week range: 56.31 - 66.56 (now 72.9% of the way up)
Volatility: ATR(14) 0.81 (1.3% of price) | annualised 20d 21.1%
Volume: 0.08x the 20-day average
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
Three-year record: +14.5% a year | beta to the market 0.82
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
Weighted price target: +1.8% above the current prices
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
Shares outstanding: 28.62M | fund size: 1.83B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, flat fund flows, bearish technicals, limited analyst coverage despite strong buy rating.

**Main reasons it gave:**
- Flat fund flows (0% change) indicating no net demand
- Technical downtrend: price below 20d, 50d, 200d SMAs and low volume
- Analyst coverage only 42.3% of fund despite 100% buy rating and +74.6% price target
- No macro surprise: yields stable, VIX high but falling, no policy shift

<details><summary><b>News</b> — score +0.00</summary>

- [Ninety One launches two actively managed equity ETFs as markets wobble](https://www.ewn.co.za/2026/11/27/ninety-one-launches-two-actively-managed-equity-etfs-as-markets-wobble)  
  <sub>EWN, 19 minutes ago</sub>  
  Trinisha Chanka, Ninety One's actively managed ETF strategy lead, says the timing of the launch, just a week after US tech shares took a hammering,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 60.25 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 62.99 (-4.4%), 50d 65.02 (-7.3%), 200d 65.11 (-7.5%); 50d below 200d
Momentum: RSI(14) 38.2 | MACD -1.476 vs signal -1.152 (histogram -0.325)
Returns: 1d +0.7% | 5d -0.9% | 1m -8.1% | 3m -12.1%
52-week range: 55.33 - 71.61 (now 30.2% of the way up)
Volatility: ATR(14) 1.31 (2.2% of price) | annualised 20d 33.4%
Volume: 0.03x the 20-day average
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
Three-year record: +15.5% a year | beta to the market 1.13
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 42.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +74.6% above the current prices
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
Shares outstanding: 5.55M | fund size: 334.39M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise or decisive technical break occurred; bullish analyst view and strong inflows are offset by bearish technicals and modest fundamentals.

**Main reasons it gave:**
- Price 84.72 below 20‑day SMA 91.27, 50‑day SMA 103.44, and 200‑day SMA 95.37
- RSI 40.4 and MACD -5.722 vs signal -5.347 indicating bearish momentum
- Share count increased 15.5% over past month (net inflows)
- Analyst coverage 37.7% all‑buy with weighted price target +62.5% above current price
- Macro unchanged: yields stable, VIX down but still high, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 84.72 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 91.27 (-7.2%), 50d 103.44 (-18.1%), 200d 95.37 (-11.2%); 50d above 200d
Momentum: RSI(14) 40.4 | MACD -5.722 vs signal -5.347 (histogram -0.375)
Returns: 1d +1.5% | 5d +0.9% | 1m -22.2% | 3m -21.5%
52-week range: 60.03 - 118.00 (now 42.6% of the way up)
Volatility: ATR(14) 5.37 (6.3% of price) | annualised 20d 102.9%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Greater China Region
What it holds: P/E 27.29 | P/B 4.22 | P/S 2.50 | 3y earnings growth n/a
Yield: 1.0%
Three-year record: +28.3% a year | beta to the market 1.35
Cost and size: expense ratio 0.59% | net assets 11.05B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 22.3%, MediaTek Inc 6.1%, Hon Hai Precision Industry Co Ltd 3.4%, ASE Technology Holding Co Ltd 3.0%, Delta Electronics Inc 2.9%
Sector mix: Technology 71.4%, Financial services 16.3%, Basic materials 4.4%, Industrials 2.6%
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
Rolled up from the 5 largest holdings, 37.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +62.5% above the current prices
Holdings read: 2330.TW, 2454.TW, 2317.TW, 3711.TW, 2308.TW
Recent rating changes among them: none reported
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
Share count change: 1 week: +4.8% (509.90M) over 7d | 1 month: +15.5% (1.48B) over 34d
Shares outstanding: 130.41M | fund size: 11.05B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected) (Bing's feed, direct: 2 headline(s), none naming EWT)

### United Kingdom (EWU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows modest positive demand (flows up 2.3% week, 6.1% month) and a fully‑buy analyst consensus with a +17.8% price target, but technicals are weak (price below 20‑, 50‑, 200‑day SMAs, low volume) and macro conditions are unchanged with no policy surprise. Fundamentals are moderate and unchanged. These offsetting factors lead to a neutral overall view.

**Main reasons it gave:**
- Fund flows: share count +2.3% week, +6.1% month
- Analyst view: 100% buy rating, price target +17.8% above current
- Technicals: price below 20d/50d/200d SMAs, RSI 48.5, volume 0.04x 20‑day avg
- Macro: no policy surprise, yields stable, VIX high but falling
- Fundamentals: moderate valuation (P/E 16.6), stable earnings growth, low beta

<details><summary><b>News</b> — score +0.00</summary>

- [Why Rolls Royce Through ETFs Could Change The Risk You Carry](https://simplywall.st/stocks/gb/capital-goods/lse-rr./rolls-royce-holdings-shares/news/why-rolls-royce-through-etfs-could-change-the-risk-you-carry)  
  <sub>Simply Wall St, 21 hours ago</sub>  
  You have a clear fork in the road with Rolls-Royce Holdings. You can own the stock directly and carry the company's specific issues yourself,...
- [Why Rolls Royce Through ETFs Looks Different After The Defence Rally](https://finance.yahoo.com/markets/stocks/articles/why-rolls-royce-etfs-looks-181135727.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  You might like Rolls-Royce Holdings and its mission-critical engines, but owning the stock on its own means living with its company specific issues.
- [Euro Zone picks Spain's Pablo Hernandez de Cos as next ECB president (VGK:NYSEARCA)](https://www.google.com/goto?url=CAESpAEBxCJF1__8-i1AUdASLFzxIdhZnQuFu9hWcsLtrcbzX_tBqCVJO6syOFhlMJs6NQaf44ql1xeh5JMHQ-6DTYqQvnWGHSP3fj591WlawqgH1kEZdCWFe9RAB63Oyz4aK5j4T8jlQY0ly7ksLLS0B_BNq2M9HeTmEueh0RzNuIsEsnB8DP7kPqUHAX5B4ESvzo_L1Se2u-dqASWltz2ZRVuRsiVpSg&gsessionid=q6GoIplKI2lqonmN_s7D0c4hXZhc-rtVisP6TQfVn5_rXxHM1XJpCA)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  Euro zone countries select Pablo Hernández de Cos to succeed Christine Lagarde as ECB president for a non-renewable eight-year term, pending consultations.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 46.69 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 47.10 (-0.9%), 50d 47.09 (-0.8%), 200d 47.06 (-0.8%); 50d above 200d
Momentum: RSI(14) 48.5 | MACD -0.418 vs signal -0.292 (histogram -0.126)
Returns: 1d +1.2% | 5d +2.7% | 1m -1.3% | 3m -3.8%
52-week range: 42.73 - 49.39 (now 59.5% of the way up)
Volatility: ATR(14) 0.69 (1.5% of price) | annualised 20d 23.8%
Volume: 0.04x the 20-day average
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
Three-year record: +16.8% a year | beta to the market 0.66
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 36.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.07 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.8% above the current prices
Holdings read: SHEL.L, HSBA.L, AZN.L, ULVR.L, RR.L
Recent rating changes among them:
  - AZN.L: 2026-08-24 CICC: init, ? -> Outperform
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
Share count change: 1 week: +2.3% (86.16M) over 7d | 1 month: +6.1% (220.19M) over 34d
Shares outstanding: 81.44M | fund size: 3.80B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technicals are bearish (price below 20‑, 50‑ and 200‑day SMAs, negative MACD, low volume) while fundamentals and analyst coverage are moderately bullish (low P/E 12.23, 3.3% yield, 100% buy rating on top holdings with +14% price target). Fund flows are flat, indicating no net demand. No macro surprise or decisive technical break is present, so the overall call is neutral.

**Main reasons it gave:**
- Price below 20‑, 50‑, and 200‑day SMAs and negative MACD, with low volume
- Analyst coverage of top holdings is 100% buy with a +14% price target
- Fund fundamentals show low valuation (P/E 12.23) and 3.3% yield
- Fund flows are flat, indicating neutral demand

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 73.38 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 75.23 (-2.5%), 50d 74.12 (-1.0%), 200d 75.98 (-3.4%); 50d below 200d
Momentum: RSI(14) 43.8 | MACD -0.539 vs signal -0.087 (histogram -0.452)
Returns: 1d +0.1% | 5d +1.2% | 1m -1.7% | 3m -4.1%
52-week range: 67.45 - 81.23 (now 43.0% of the way up)
Volatility: ATR(14) 1.63 (2.2% of price) | annualised 20d 23.1%
Volume: 0.22x the 20-day average
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
Three-year record: +9.3% a year | beta to the market 0.99
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.17 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.0% above the current prices
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
Shares outstanding: 18.90M | fund size: 1.39B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fund flows flat (0% change) over past month, indicating no net demand
- Technical indicators show price below 20‑day, 50‑day, and 200‑day SMAs with negative MACD, no decisive breakout
- Macro data stable: yields slightly down, VIX down but still high, no policy surprise
- Analyst view bullish (100% buy, +34% price target) but not corroborated by macro or technical catalysts

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 60.49 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 62.89 (-3.8%), 50d 63.95 (-5.4%), 200d 67.37 (-10.2%); 50d below 200d
Momentum: RSI(14) 43.9 | MACD -1.659 vs signal -1.191 (histogram -0.467)
Returns: 1d +2.5% | 5d +4.4% | 1m -6.0% | 3m -14.5%
52-week range: 56.26 - 81.60 (now 16.7% of the way up)
Volatility: ATR(14) 1.84 (3.0% of price) | annualised 20d 43.7%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.65 | P/B 1.96 | P/S 1.68 | 3y earnings growth n/a
Yield: 8.2%
Three-year record: +20.1% a year | beta to the market 1.12
Cost and size: expense ratio 0.59% | net assets 438.81M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Anglogold Ashanti PLC 11.3%, Naspers Ltd Class N 8.4%, Gold Fields Ltd 8.2%, Firstrand Ltd 7.5%, Standard Bank Group Ltd 6.4%
Sector mix: Financial services 36.0%, Basic materials 35.9%, Consumer cyclical 13.0%, Communication services 7.2%
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
Rolled up from the 5 largest holdings, 41.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.00 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +34.1% above the current prices
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
Shares outstanding: 7.90M | fund size: 477.87M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected) (Bing's feed, direct: 1 headline(s), none naming EZA)

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, and mixed signals from fundamentals and flows lead to a neutral stance.

**Main reasons it gave:**
- US Treasury yields fell modestly across the curve, no rate surprise
- Gold price 20% below its 200‑day average, sector weakness
- Technicals show GDX below 20‑, 50‑ and 200‑day SMAs, RSI 45.6, no decisive break
- Fund flows show +11% share count in one week, indicating inflow but not a macro catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs Investing in Harmony Gold Mining Co. Ltd. Sponsored ADR Stocks](https://www.tradingview.com/symbols/TRADEGATE-HAM/etfs/)  
  <sub>TradingView, 11 hours ago</sub>  
  Explore funds investing in HAM in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [Gold Traders are Watching 5 Historic Signals](https://beincrypto.com/gold-price-bottom-analysis-signals-to-watch/)  
  <sub>BeInCrypto, 10 hours ago</sub>  
  Key takeaways. Gold sits 20% below its 200-day average, the widest gap since 2013. Gold miners staged a rare reversal as bullion hit a 15-month low.
- [iShsV-Italy Govt Bd UCITS ETF R (IS0M.HM) Seasonal returns chart](https://www.google.com/goto?url=CAEScwHEIkXX2CS8NHgp6LawzHXXBNvu3QdSSoLFXDD0FT8jGeGGtbVZBxoQzPmu2sCeDw5D2xZK1BhDULRGd6P94-SzqJRBRB6YcUCrmvyixneIcSUlqzrLVeCpBtNt_IaPzMuHrZ70S6HdCGefKagrPMUr1MY&gsessionid=t7Quv8jnFBKCKgSuTlYrIHsm1ypiLS6MqRUZiTF2QkX6vjba3yc4Ug)  
  <sub>Yahoo Finance UK, 11 hours ago</sub>  
  iShsV-Italy Govt Bd UCITS ETF R (IS0M.HM) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [FID.II-ESG USD EM Bd ETF R (FESD.HM)](https://www.google.com/goto?url=CAESbAHEIkXXZLktCHhOB_XK1uOC6VPJxsvvrC_ZQJW_8yISuBUf0GtG7KkhmLTw9HngznHD3xNRK_r4n1GgXUCer78uyVLaIYbHHTvP3_vB3kQqqop1m3XmwKcHatwb9xlKSf-sKDUXBkfYNB1AmA&gsessionid=t7Quv8jnFBKCKgSuTlYrIHsm1ypiLS6MqRUZiTF2QkX6vjba3yc4Ug)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  View Historical Risk Statistics for FID.II-ESG USD EM Bd ETF R (FESD.HM).
- [iShsVII-NASDAQ 100 UCITS ETF R (SXRV.HA) Seasonal returns chart](https://www.google.com/goto?url=CAEScwHEIkXXMgP9RsCjHEcK3PoFb0C9gpS3wY8pySVINntMVJBwN03Ir-soRzX9rj4HMZbQWqhXOZDjShESQgZSn2uN5y_N80hrakuf8coE6_P4GbyxI4ZVQRd3ZPEZRk5PUbQIYsl-_oCzookS2rmIMKDMuxs&gsessionid=t7Quv8jnFBKCKgSuTlYrIHsm1ypiLS6MqRUZiTF2QkX6vjba3yc4Ug)  
  <sub>Yahoo Finance UK, 21 hours ago</sub>  
  Seasonality data is currently unavailable for SXRV.HA. Related tickers. GDX VanEck Gold Miners ETF. 73.89 +4.39%. RING iShares MSCI Global Gold Miners ETF.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 76.72 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 79.35 (-3.3%), 50d 84.29 (-9.0%), 200d 88.49 (-13.3%); 50d below 200d
Momentum: RSI(14) 45.6 | MACD -3.318 vs signal -2.881 (histogram -0.437)
Returns: 1d +3.8% | 5d +6.6% | 1m -8.6% | 3m -23.0%
52-week range: 68.40 - 115.84 (now 17.5% of the way up)
Volatility: ATR(14) 3.87 (5.0% of price) | annualised 20d 68.2%
Volume: 0.21x the 20-day average
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
Three-year record: +37.7% a year | beta to the market 0.98
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.1% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, FNV.TO
Recent rating changes among them:
  - NEM: 2026-10-27 Scotiabank: main, Sector Outperform -> Sector Outperform
  - AEM.TO: 2026-11-02 Freedom Broker: up, Hold -> Buy
  - ABX.TO: 2026-11-10 JP Morgan: main, Overweight -> Overweight
  - WPM.TO: 2026-10-08 UBS: main, Buy -> Buy
  - FNV.TO: 2026-11-12 HC Wainwright & Co.: reit, Buy -> Buy
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
Share count change: 1 week: +11.0% (2.53B) over 7d | 1 month: +1.7% (431.10M) over 30d
Shares outstanding: 333.15M | fund size: 25.56B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals lack decisive break, flat fund flows, analyst view bullish but not enough to outweigh neutral macro/technical backdrop.

**Main reasons it gave:**
- Yield curve unchanged (+0.73 points, normal slope)
- VIX down 9.6% week to 26.28 (still stressed)
- Price below 20‑day SMA (96.09 vs 98.91, -2.8%)
- Volume 0.04× 20‑day average (very low)
- Fund flows flat (share count +0.0% 1‑week)

<details><summary><b>News</b> — score +0.00</summary>

- [Which Funds With Software Exposure Fit Rising US AI Spending?](https://finance.yahoo.com/technology/ai/articles/funds-software-exposure-fit-rising-160905233.html)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  Software themed funds can look interchangeable from the ticker list, yet what sits inside can pull your money toward very different risks.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 96.09 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 98.91 (-2.8%), 50d 104.65 (-8.2%), 200d 94.66 (+1.5%); 50d above 200d
Momentum: RSI(14) 40.7 | MACD -2.970 vs signal -2.731 (histogram -0.240)
Returns: 1d +1.1% | 5d -0.0% | 1m -14.1% | 3m -12.2%
52-week range: 74.67 - 112.67 (now 56.4% of the way up)
Volatility: ATR(14) 3.28 (3.4% of price) | annualised 20d 36.4%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Technology
What it holds: P/E 30.79 | P/B 7.22 | P/S 8.03 | 3y earnings growth n/a
Yield: 0.0%
Three-year record: +7.7% a year | beta to the market 1.25
Cost and size: expense ratio 0.38% | net assets 13.46B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Palo Alto Networks Inc 9.1%, Palantir Technologies Inc Ordinary Shares - Class A 9.0%, Microsoft Corp 8.8%, CrowdStrike Holdings Inc Class A 8.6%, Oracle Corp 6.7%
Sector mix: Technology 94.4%, Communication services 3.6%, Financial services 1.7%, Consumer cyclical 0.2%
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
Rolled up from the 5 largest holdings, 42.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +40.4% above the current prices
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
Shares outstanding: 12.50M | fund size: 1.20B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: strong analyst buy rating for top holdings (24.8% weight) vs. significant outflows (‑11.3% month) and modest fundamentals; no macro surprise or decisive technical break.

**Main reasons it gave:**
- Analyst coverage: 100% buy rating for top 5 holdings (24.8% of fund weight)
- Fund flows: share count down 11.3% in past month (outflows of $748M)
- Technicals: price above 20‑day, 50‑day, 200‑day SMAs; RSI 65.8; volume 0.28× 20‑day average
- Macro: US 10‑yr yield down 0.16% on week; VIX down 9.6 points; no policy surprise
- Fundamentals: P/E 21.32, expense ratio 0.61%, 3‑yr annualized return 5.8%

<details><summary><b>News</b> — score +0.00</summary>

- [Mahanadi Coalfields Lists 1.47% Lower on Indian Stock Market](https://www.heygotrade.com/en/news/indian-stock-market-mahanadi-coalfields-listing/)  
  <sub>Gotrade, 6 hours ago</sub>  
  Mahanadi Coalfields listed at ₹134 on the NSE, 1.47% below its ₹136 IPO price, as the Nifty 50 slipped and Waaree Renewable rose 10.2% on a solar order.
- [INDA Jun 2027 57.000 call (INDA270617C00057000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/INDA270617C00057000/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Find the latest INDA Jun 2027 57.000 call (INDA270617C00057000) stock quote, history, news and other vital information to help you with your stock trading...
- [INDA Jun 2027 55.000 call (INDA270617C00055000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScgHEIkXX32pVpwVdNywjEF5P-nLr9jANXIkBrV-mZ8w1mlDuxVEgrRqDoh2At339Lckj1ZPZiMZKZ8eK6pElNczzsiSmaqkRJCzaKAffOaKFp_McrUeIWZJObNfY14lmCvLQ5gCu5QDg98sBPNzpKFH6VA&gsessionid=5bm6K5eGwT9TgpSYXuyyBuWnOC86qcGLguedvyTl0rC4BhRyys5HKQ)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Find the latest INDA Jun 2027 55.000 call (INDA270617C00055000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 52.59 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 51.20 (+2.7%), 50d 48.74 (+7.9%), 200d 49.07 (+7.2%); 50d below 200d
Momentum: RSI(14) 65.8 | MACD 1.218 vs signal 1.148 (histogram 0.069)
Returns: 1d -1.1% | 5d +1.1% | 1m +12.4% | 3m +6.1%
52-week range: 45.42 - 54.71 (now 77.2% of the way up)
Volatility: ATR(14) 0.65 (1.2% of price) | annualised 20d 16.4%
Volume: 0.28x the 20-day average
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
Three-year record: +5.8% a year | beta to the market 0.61
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 24.8% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.40 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.5% above the current prices
Holdings read: HDFCBANK.NS, ICICIBANK.NS, RELIANCE.NS, BHARTIARTL.NS, INFY.NS
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.55</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.55</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.55</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -1.4% (-81.47M) over 7d | 1 month: -11.3% (-748.29M) over 30d
Shares outstanding: 111.34M | fund size: 5.86B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, and mixed fundamentals; overall view remains neutral despite strong analyst rating and large inflows.

**Main reasons it gave:**
- Fund flows: +199% share count increase over 30 days (strong inflow)
- Analyst view: 100% buy rating, price target +18.8% above current price
- Technical indicators: price below 20‑day and 50‑day SMA, MACD negative, low volume
- Macro backdrop: high inflation (3.7%) and expectations of further Fed hikes, upward‑sloping yield curve

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 69.54 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 70.00 (-0.7%), 50d 69.66 (-0.2%), 200d 75.53 (-7.9%); 50d below 200d
Momentum: RSI(14) 49.6 | MACD -0.461 vs signal -0.311 (histogram -0.149)
Returns: 1d +1.1% | 5d +2.0% | 1m +0.4% | 3m -10.4%
52-week range: 66.17 - 84.41 (now 18.5% of the way up)
Volatility: ATR(14) 1.85 (2.7% of price) | annualised 20d 33.6%
Volume: 0.04x the 20-day average
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
Three-year record: +21.2% a year | beta to the market 1.03
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 54.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.74 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.8% above the current prices
Holdings read: GE, RTX, BA, LMT, NOC
Recent rating changes among them:
  - GE: 2026-10-21 UBS: main, Buy -> Buy
  - RTX: 2026-10-21 UBS: main, Neutral -> Neutral
  - BA: 2026-10-29 Bernstein: main, Outperform -> Outperform
  - LMT: 2026-11-04 Guggenheim: init, ? -> Buy
  - NOC: 2026-10-27 Bernstein: main, Market Perform -> Market Perform
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
Share count change: 1 week: +2.3% (282.18M) over 7d | 1 month: +199.3% (8.31B) over 30d
Shares outstanding: 179.56M | fund size: 12.49B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: yields stable, VIX down modestly
- Technicals: MACD below signal, low volume, price near 20‑day SMA
- Analyst coverage: 90.9% buy rating, price target +18% (covers 52% of fund)
- Fund flows: +2.3% share count in 1 week (net inflow)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 82.11 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 82.40 (-0.3%), 50d 80.96 (+1.4%), 200d 82.05 (+0.1%); 50d below 200d
Momentum: RSI(14) 51.2 | MACD -0.096 vs signal 0.126 (histogram -0.222)
Returns: 1d +0.4% | 5d +1.6% | 1m +1.6% | 3m -4.9%
52-week range: 72.18 - 90.01 (now 55.7% of the way up)
Volatility: ATR(14) 1.77 (2.2% of price) | annualised 20d 29.3%
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
Three-year record: +11.5% a year | beta to the market 1.24
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 52.2% of the fund by weight
Ratings by weight: buy 90.9% | hold 9.1% | sell 0.0% (mean 1.87 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.1% above the current prices
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
Share count change: 1 week: +2.3% (46.71M) over 7d | 1 month: +5.7% (109.76M) over 34d
Shares outstanding: 24.91M | fund size: 2.05B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no material macro surprise, technicals are weak, analyst view is hold, but strong inflows provide modest bullish pressure.

**Main reasons it gave:**
- Technicals: price below 20‑day, 50‑day and 200‑day SMAs and negative MACD
- Analyst view: 100% hold rating for the top 5 holdings (5.9% of fund)
- Fund flows: +11.7% share count increase over the past month indicating strong inflows
- Macro: yields stable, VIX down but still elevated, no data surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 70.21 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 71.62 (-2.0%), 50d 71.04 (-1.2%), 200d 71.14 (-1.3%); 50d below 200d
Momentum: RSI(14) 44.8 | MACD -0.585 vs signal -0.309 (histogram -0.276)
Returns: 1d +0.6% | 5d +1.4% | 1m -2.6% | 3m -5.5%
52-week range: 62.62 - 77.93 (now 49.6% of the way up)
Volatility: ATR(14) 1.39 (2.0% of price) | annualised 20d 21.0%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Financial
What it holds: P/E 12.17 | P/B 1.26 | P/S 3.63 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +19.5% a year | beta to the market 0.97
Cost and size: expense ratio 0.35% | net assets 4.01B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Glacier Bancorp Inc 1.2%, United Community Banks Inc 1.2%, Texas Capital Bancshares Inc 1.2%, Bank OZK 1.2%, Eastern Bankshares Inc Ordinary Shares 1.2%
Sector mix: Financial services 100.0%
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
Rolled up from the 5 largest holdings, 5.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 0.0% | hold 100.0% | sell 0.0% (mean 2.62 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.1% above the current prices
Holdings read: GBCI, UCB, TXCP, OZK, EBC
Recent rating changes among them:
  - GBCI: 2026-10-26 Piper Sandler: main, Overweight -> Overweight
  - UCB: 2026-10-21 Stephens & Co.: main, Overweight -> Overweight
  - TXCP: 2026-11-03 Barclays: main, Equal-Weight -> Equal-Weight
  - OZK: 2026-10-30 Keefe, Bruyette & Woods: main, Market Perform -> Market Perform
  - EBC: 2026-11-03 Barclays: main, Equal-Weight -> Equal-Weight
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
Share count change: 1 week: +1.6% (62.86M) over 7d | 1 month: +11.7% (420.76M) over 30d
Shares outstanding: 57.42M | fund size: 4.03B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: analysts are bullish, but fund flows show net outflows and technicals are bearish; macro environment unchanged.

**Main reasons it gave:**
- Analyst view: 100% buy rating and +19.9% price target for top holdings
- Fund flows: net outflow of -8.3% over the past month
- Technical indicators: price below 20‑day, 50‑day, 200‑day SMAs; RSI 39.1; negative MACD
- Macro: no surprise in US rates or data; yields stable, VIX down but still stressed

<details><summary><b>News</b> — score +0.00</summary>

- [KSA: All You Need To Know About The Oldest Saudi-Focused ETF (NYSEARCA:KSA)](https://seekingalpha.com/article/4972535-ksa-all-you-need-to-know-about-the-oldest-saudi-focused-etf)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  iShares MSCI Saudi Arabia ETF (KSA) offers a low-beta, value-oriented foreign satellite for investors seeking exposure to a carbon-heavy economy in the...
- [KSA Mar 2027 34.000 put (KSA270319P00034000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/KSA270319P00034000/)  
  <sub>Yahoo! Finance Canada, 23 hours ago</sub>  
  Find the latest KSA Mar 2027 34.000 put (KSA270319P00034000) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 34.65 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 35.20 (-1.6%), 50d 35.56 (-2.6%), 200d 37.58 (-7.8%); 50d below 200d
Momentum: RSI(14) 39.1 | MACD -0.140 vs signal -0.088 (histogram -0.052)
Returns: 1d -0.8% | 5d -1.4% | 1m -0.2% | 3m -11.8%
52-week range: 33.69 - 40.63 (now 13.8% of the way up)
Volatility: ATR(14) 0.35 (1.0% of price) | annualised 20d 13.4%
Volume: 0.21x the 20-day average
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
Three-year record: -1.0% a year | beta to the market 0.20
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 45.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.10 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.9% above the current prices
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
Share count change: 1 week: +2.8% (14.96M) over 7d | 1 month: -8.3% (-50.25M) over 30d
Shares outstanding: 15.97M | fund size: 553.33M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise or decisive technical break; analyst view bullish but limited coverage, recent outflow suggests bearish sentiment, fundamentals are modestly positive.

**Main reasons it gave:**
- Analyst view: 100% buy rating on top holdings with +67% price target
- Fund flows: net outflow of -3.1% over the month indicating bearish sentiment
- Technicals: price below 20‑day, 50‑day, and 200‑day SMAs; negative MACD; low volume
- Macro: no significant surprise; yields stable, VIX high but falling

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 47.93 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 49.13 (-2.4%), 50d 50.55 (-5.2%), 200d 54.48 (-12.0%); 50d below 200d
Momentum: RSI(14) 42.8 | MACD -1.090 vs signal -0.912 (histogram -0.178)
Returns: 1d +3.2% | 5d +1.9% | 1m -2.3% | 3m -13.2%
52-week range: 46.02 - 64.26 (now 10.5% of the way up)
Volatility: ATR(14) 0.86 (1.8% of price) | annualised 20d 27.0%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Greater China Region
What it holds: P/E 11.09 | P/B 1.27 | P/S 1.27 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +4.7% a year | beta to the market 0.47
Cost and size: expense ratio 0.59% | net assets 5.49B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Tencent Holdings Ltd 13.2%, Alibaba Group Holding Ltd Ordinary Shares 9.1%, China Construction Bank Corp Class H 4.8%, Industrial And Commercial Bank Of China Ltd Class H 2.9%, Xiaomi Corp Class B 2.5%
Sector mix: Consumer cyclical 23.1%, Financial services 22.5%, Communication services 17.5%, Technology 9.9%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 32.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.39 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +67.0% above the current prices
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
Share count change: 1 week: +4.0% (218.82M) over 7d | 1 month: -3.1% (-181.94M) over 30d
Shares outstanding: 118.12M | fund size: 5.66B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, technicals bearish but not decisive, strong inflows and bullish analyst view offset by high valuation.

**Main reasons it gave:**
- Fund flows: share count up 7.7% in a week and 15.6% in a month, indicating strong net inflows
- Analyst coverage (46.4% weight) shows 100% buy rating with weighted price target +60.7% above current price
- Technical indicators: price below 20‑day (469.84) and 50‑day (538.43) SMA, RSI 38, low volume, indicating bearish momentum
- Macro data: yields slightly down, VIX down 9.6 points, no policy or data surprise

<details><summary><b>News</b> — score +0.00</summary>

- [VanEck Semiconductor ETF (SMH) stock price, news, quote and history](https://au.finance.yahoo.com/quote/SMH/)  
  <sub>Yahoo Finance Australia, 18 hours ago</sub>  
  VanEck Semiconductor ETF (SMH) · -8.07% · -19.87% · -26.70% · 16.28% · 24.58% · 174.02% · 766.58%. Key events. Baseline. Advanced chart. Loading chart...
- [SMH Dec 2027 825.000 put (SMH271217P00825000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/SMH271217P00825000/chart/)  
  <sub>Yahoo! Finance Canada, 10 hours ago</sub>  
  Interactive Chart for SMH Dec 2027 825.000 put (SMH271217P00825000), analyze all the data with a huge range of indicators.
- [As Paranoia Hits The Market, Here Are 5 Stocks I'm Buying This Holiday Season](https://www.google.com/goto?url=CAESrAEBxCJF11UVVmcdJItINIEWMWchOm4egGjRMnx34zB7bwVKrOor6d6yEopqvKMqJytIMksnbnO1jt2tB3NikfKcQIi9BSxSNxox5A8o9wr5tpGvJbYJkc6InCjF10SbzFSLbkaA5FwJHWaxwNFw2I01wa3e66RZ4dujqgrEmkQXs01SwOYoRTyQxeFVRoEOM-Lzw1M5H1DHoWHwLpb-nkIPzKuLkF7HDaIBUfv8&gsessionid=q2FQ-x4lyuk8uGKqgHLdnVGlPKPLEpTVZMcTr4g6i8kNJ8ba8EGPEA)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  The bull case for AI semiconductor stocks: a 40% SOX drop cuts forward multiples to 11.7x, creating an entry as AI fundamentals hold.
- [VanEck Semiconductor ETF Rebounds 3.52% but Stays Below Key Averages](https://www.google.com/goto?url=CAESagHEIkXXqP5bk2-TXV-tXxJaPLdzo9Gn3TG7pSo1MpN9CzvgNdHs4AqXFDPtllosZkydCpZVXaT0o12M5DrsAlv75QpkmIuMyvJM8t3D-C14JMbgpQq246gm5JSzBFsDcjCnLJ7FPhK8Ws8&gsessionid=q2FQ-x4lyuk8uGKqgHLdnVGlPKPLEpTVZMcTr4g6i8kNJ8ba8EGPEA)  
  <sub>www.tokenpost.com, 6 hours ago</sub>  
  SMH reached $443.65 at 4:01 a.m. ET Friday after trading between $425.89 and $447, while mixed momentum and derivatives data signaled continued caution.
- [VanEck Semiconductor ETF (SMH) Price Prediction: Rebound attempt meets overhead resistance as semiconductor ETF trades below key averages](https://www.google.com/goto?url=CAESowEBxCJF1_Psu-hO8E4V9asACa49a4gW4JJJdtYe4o1oK0d39i-SSquezyZxAn4bbCUb6FnxiEL9VLyT1JpnjKpUTu4xJEgo3k426WWzo_qmgqtBIkrVsSZwr8uoBzDcJXsu-PwDXYwqhsCN4DvvunMtHkdffCebCvlcjn6XQuS12yIaC92z2TeZxPmSGdPi31AJZ9oKMYFKie0rCuqGYOR0MA5e&gsessionid=q2FQ-x4lyuk8uGKqgHLdnVGlPKPLEpTVZMcTr4g6i8kNJ8ba8EGPEA)  
  <sub>Blockchain News, 6 hours ago</sub>  
  VanEck Semiconductor ETF (SMH) is trading at $443.65, up 3.52% over the last 24 hours, but it remains below its 20-day and 50-day moving averages. Momentum.
- [iShares Russell 2000 ETF (IWM) Price Prediction: Small-cap ETF holds above its pivot as buyers lean in, but momentum remains mixed](https://www.google.com/goto?url=CAESlAEBxCJF1wS5ZeVB4wrwTOSYQJ3Quvv-7oAdP7HctrsQrsfshTNnjaqAIqzWL0WgcLBalPVf_fpYURppltVQKZKxEMIiCMzdYMbJRsoVREqLKPJMvXj5oeaTaayJmcWSKsACGaRwg_5NHITnrJGviG89ubT_lHseSeFbAQQKPsS8mFFJQoibtSrFdp8WawvYASWYXyrj&gsessionid=q2FQ-x4lyuk8uGKqgHLdnVGlPKPLEpTVZMcTr4g6i8kNJ8ba8EGPEA)  
  <sub>Blockchain News, 6 hours ago</sub>  
  iShares Russell 2000 ETF (IWM) is trading at $273.13, up 1.50% on the latest 24-hour window, after a rebound from $266.06 and a close above its $270.77...
- [Traders Pile Into SOXL as Chip Stocks Fall](https://www.google.com/goto?url=CAESlAEBxCJF1w0SmuYmWwNK_VqPgcY_OQHE6_V08fgZYRCRP9_K4H-hLJw0XIXBBuYBou-Vneq4e7wz0-A_RsMtMuFTsmtLBViQvK34La35UXTZ2IhJSV53JMGy2Y2nA6U8kVq0yT9woZjKWFw79JXGrDBw1VuscvkT8fhOD89WWLG7aC6-7cPSZe1yV6nmUyOc9WbZYN0X&gsessionid=q2FQ-x4lyuk8uGKqgHLdnVGlPKPLEpTVZMcTr4g6i8kNJ8ba8EGPEA)  
  <sub>Wisevoter, 20 hours ago</sub>  
  The leveraged semiconductor ETF drew about $2.7 billion in net inflows in the week ending November 20, 2026, even as a broad tech selloff hit chip names.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 426.65 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 469.84 (-9.2%), 50d 538.43 (-20.8%), 200d 525.71 (-18.8%); 50d above 200d
Momentum: RSI(14) 38.0 | MACD -31.306 vs signal -28.776 (histogram -2.530)
Returns: 1d +1.0% | 5d -4.7% | 1m -24.8% | 3m -22.9%
52-week range: 339.24 - 668.91 (now 26.5% of the way up)
Volatility: ATR(14) 29.09 (6.8% of price) | annualised 20d 93.8%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Technology
What it holds: P/E 28.22 | P/B 9.76 | P/S 11.19 | 3y earnings growth n/a
Yield: 0.2%
Three-year record: +38.3% a year | beta to the market 2.12
Cost and size: expense ratio 0.35% | net assets 66.44B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: NVIDIA Corp 20.2%, Taiwan Semiconductor Manufacturing Co Ltd ADR 9.6%, Texas Instruments Inc 5.7%, Broadcom Inc 5.6%, Advanced Micro Devices Inc 5.3%
Sector mix: Technology 100.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 46.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.60 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +60.7% above the current prices
Holdings read: NVDA, TSM, TXN, AVGO, AMD
Recent rating changes among them:
  - NVDA: 2026-11-12 Melius Research: down, Buy -> Hold
  - TSM: 2026-11-04 Bernstein: main, Outperform -> Outperform
  - TXN: 2026-10-22 Jefferies: main, Hold -> Hold
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
Share count change: 1 week: +7.7% (4.75B) over 7d | 1 month: +15.6% (8.94B) over 34d
Shares outstanding: 155.45M | fund size: 66.32B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, technicals weak, flows flat, analyst view bullish but not enough to outweigh neutral technicals and flows.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs, RSI 36.3, MACD negative – weak technical momentum
- Fund flows flat (0.0% change) over 1‑week and 1‑month, indicating no new inflows/outflows
- US macro: yields stable, no rate surprise, VIX down but still high – no macro catalyst
- Analyst rating 100% buy with +37.5% price target – bullish sentiment but technicals and flows are neutral

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 29.48 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 30.81 (-4.3%), 50d 32.64 (-9.7%), 200d 38.12 (-22.7%); 50d below 200d
Momentum: RSI(14) 36.3 | MACD -0.850 vs signal -0.749 (histogram -0.100)
Returns: 1d +1.4% | 5d -3.6% | 1m -4.2% | 3m -27.9%
52-week range: 29.08 - 43.74 (now 2.7% of the way up)
Volatility: ATR(14) 0.64 (2.2% of price) | annualised 20d 35.6%
Volume: 0.08x the 20-day average
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
Three-year record: -4.2% a year | beta to the market 0.60
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 44.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.54 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +37.5% above the current prices
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
Shares outstanding: 15.65M | fund size: 461.28M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected) (Bing's feed, direct: 4 headline(s), none naming TUR)

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed evidence: strong analyst consensus (100% buy, +16% price target) and modest inflows (+0.9% share count over a month) are bullish, while high valuation (P/E 29.6) and dividend yield (3.6%) below 10‑year Treasury yield (4.9%) are bearish, and macro expectations of three 0.25% rate hikes over the next two years add pressure to REITs. Technicals show bearish momentum (MACD below signal, 50‑day SMA below 200‑day SMA) despite price above SMAs. No material macro surprise or decisive technical break, so overall stance remains neutral.

**Main reasons it gave:**
- Analyst consensus 100% buy with weighted price target +16% above current price
- Fund flows: +0.9% share count increase over past month indicating modest inflows
- Fundamentals: high valuation (P/E 29.6) and dividend yield 3.6% below 10‑year Treasury yield 4.9%
- Macro: market expects three 0.25% rate hikes over next two years, raising borrowing costs for REITs
- Technical: MACD below signal (histogram -0.147) and 50‑day SMA below 200‑day SMA indicating bearish momentum

<details><summary><b>News</b> — score +0.00</summary>

- [Top Tokenized ETFs by Market Cap](https://www.coingecko.com/en/etfs)  
  <sub>Coingecko, 1 hour ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 96.04 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 95.54 (+0.5%), 50d 92.98 (+3.3%), 200d 95.03 (+1.1%); 50d below 200d
Momentum: RSI(14) 56.6 | MACD 0.396 vs signal 0.543 (histogram -0.147)
Returns: 1d +0.4% | 5d +2.7% | 1m +4.6% | 3m -1.2%
52-week range: 87.00 - 100.95 (now 64.8% of the way up)
Volatility: ATR(14) 1.46 (1.5% of price) | annualised 20d 19.3%
Volume: 0.06x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 40.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.56 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.1% above the current prices
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
Direction: money coming in (1 month)
Share count change: 1 week: +0.1% (66.77M) over 7d | 1 month: +0.9% (638.16M) over 34d
Shares outstanding: 732.84M | fund size: 70.38B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals not decisive, mixed flows, thin analyst coverage, moderate fundamentals.

**Main reasons it gave:**
- Weekly share count fell 7.3% (-857.08M) indicating recent outflow
- Analyst coverage thin (9.5% of fund) with 75% buy rating and +9.8% price target
- Price above 20‑day, 50‑day, 200‑day SMAs (+3.3%, +2.6%, +8.7%) but volume 0.09× 20‑day average
- US Treasury yields down slightly, VIX down 9.6% to 26.28, no macro surprise

<details><summary><b>News</b> — score +0.00</summary>

- [XBI Nov 2027 105.000 call (XBI271119C00105000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XBI271119C00105000/)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  Find the latest XBI Nov 2027 105.000 call (XBI271119C00105000) stock quote, history, news and other vital information to help you with your stock trading...
- [KXCO's Model Books Are Five for Five on FDA Decisions, by Shayne Heffernan](https://www.livetradingnews.com/kxcos-model-books-are-five-for-five-on-fda-decisions)  
  <sub>Live Trading News, 22 hours ago</sub>  
  ·KXCO's model books are five for five on the FDA decisions their scorecard counts: INO-3107, BBP-418 and bezuclastinib held and approved, ivonescimab and...
- [Madrigal’s MASH Drug Shows Improvements In Liver Health Across 4 Studies, Days After Company Disclosed $1.1B Rezdiffra Sales](https://www.google.com/goto?url=CAESwgEBxCJF156UxBYT1DgbuIQgGrHaV4jh3EQKeOFutx5zayah-BA1vjeRt20GfjUWUE_NmqXCi5EiA54aWFqLbP8WIv46e91Wb9DJyYEtWxj8g9jRsnKN4mV0l5cpv1pQ9jpVo7k94gSvpdIpCfo40Hys37833uWAEOm3NVPl2-Y_Hwn-E2OpkpUsCRJBCnsbfPbRyReLFUNyisI3BvGID0ig403ZlymVZxqi3xG-P1y_slpVLlRDK-3OE0xOngK0lXcHkg&gsessionid=FgW97DI7CMeWO6aOH3n38aOOMXR3nnsDvKR77in08jrn2JpJ5j7qWw)  
  <sub>Stocktwits, 24 hours ago</sub>  
  Across four studies, 37% to 55% of patients experienced at least a 25% improvement in liver stiffness after about one year of treatment.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 156.57 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 151.52 (+3.3%), 50d 152.57 (+2.6%), 200d 144.02 (+8.7%); 50d above 200d
Momentum: RSI(14) 56.3 | MACD -0.262 vs signal -1.129 (histogram 0.867)
Returns: 1d -0.0% | 5d +8.6% | 1m -0.6% | 3m -3.6%
52-week range: 118.46 - 169.55 (now 74.6% of the way up)
Volatility: ATR(14) 5.21 (3.3% of price) | annualised 20d 48.6%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Health
What it holds: P/E n/a | P/B 0.21 | P/S 0.13 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +28.8% a year | beta to the market 1.01
Cost and size: expense ratio 0.35% | net assets 10.92B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Moderna Inc 2.4%, Natera Inc 1.8%, Halozyme Therapeutics Inc 1.8%, Twist Bioscience Corp 1.8%, Biogen Inc 1.7%
Sector mix: Healthcare 99.4%, Financial services 0.6%
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
Rolled up from the 5 largest holdings, 9.5% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 75.0% | hold 25.0% | sell 0.0% (mean 2.07 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.8% above the current prices
Holdings read: MRNA, NTRA, HALO, TWST, BIIB
Recent rating changes among them:
  - MRNA: 2026-11-09 Goldman Sachs: main, Neutral -> Neutral
  - NTRA: 2026-11-09 Baird: main, Outperform -> Outperform
  - HALO: 2026-11-11 Morgan Stanley: down, Overweight -> Equal-Weight
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - BIIB: 2026-11-09 Piper Sandler: reit, Overweight -> Overweight
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
Direction: money coming in (1 month)
Share count change: 1 week: -7.3% (-857.08M) over 7d | 1 month: +0.7% (75.22M) over 30d
Shares outstanding: 69.71M | fund size: 10.91B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise, technicals show modest short‑term uptrend but below long‑term trend, and fundamentals are moderately valued.

**Main reasons it gave:**
- Analyst view: 100% buy rating on 18.9% of fund, price target +9.6% above current
- Fund flows: net share count increase of +10.8% over the past month
- Technicals: price above 20‑day and 50‑day SMA but below 200‑day SMA, RSI 56.4, modest momentum
- Macro: inflation 3.7% and VIX 26.28, no major surprise; yields stable

<details><summary><b>News</b> — score +0.00</summary>

- [SPDR MSCI World Materials ETF USD Acc (WMAT) Seasonal returns chart](https://uk.finance.yahoo.com/quote/WMAT/seasonality/)  
  <sub>Yahoo Finance UK, 10 hours ago</sub>  
  SPDR MSCI World Materials ETF USD Acc (WMAT) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [Dow Jones Futures Rise; Look For This Bullish Market Signal On Black Friday](https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-market-wild-ride-nasdaq-nvidia-slash-losses-anthropic-higher/)  
  <sub>Investor's Business Daily, 2 hours ago</sub>  
  Dow Jones futures rose on Thanksgiving after a wild market session, with the Nasdaq rallying off lows and Anthropic reversing higher.
- [(XHB) Stock Evaluation Report (XHB:CA)](https://www.google.com/goto?url=CAESkQEBxCJF11GWLJk3YVTMnsieoYlMPumEZsnknPzifEreTELOOSoUmkj-6BR0XfRpA-fw4X1yJniOhk4RKQqw-dJXDIfTLU_OCUxZHJ8Tn4Db3wmpjwdifED0g9nT_VqwhzTKK3HwGRmf6Eb9qLnJYWJSi1288twEf4KvNnOmn6qBEd0LnAwHC9zVgU7xxBaR9zi2&gsessionid=aKDTFQfIrG1MtT2SmNFOZmiHeCJHsSDY7dJEcpM0OL9I9dp0xtXCAQ)  
  <sub>Stock Traders Daily, 18 hours ago</sub>  
  Stock Evaluation Report for iShares Canadian HYBrid Corporate Bond Index ETF (XHB) Including Buy/Sell Signals.
- [Mirae Asset Global Investment Co., Ltd. - Tiger Us Cash Cow 100 ETF (465670.KS) performance history](https://www.google.com/goto?url=CAESdQHEIkXXUDOOTmwLFVGrk2EbY38X878BlVAUgD85iU9xjveRu3lMMbmqPHTcbxxrf__hsTF-hI7TWp08J9IGS6PHEd5ULL3KtEWnepOwh1BdEpSQPQI9k_WYOOntiW5f7v9hjxy6BaBmy2Y94DCSZ7W6Pa1_CQ&gsessionid=aKDTFQfIrG1MtT2SmNFOZmiHeCJHsSDY7dJEcpM0OL9I9dp0xtXCAQ)  
  <sub>Yahoo Finance UK, 22 hours ago</sub>  
  Mirae Asset Global Investment Co., Ltd. - Tiger Us Cash Cow 100 ETF (465670.KS). 16,550.00 +335.00 (+2.07%). At close: 15:30:24 GMT+9...
- [Nomura Nikkei 300 ETF (1319) Seasonal returns chart](https://www.google.com/goto?url=CAEScAHEIkXX18P7Z0lGjPvBiHFPnK31N-8QOqubGAxRLz5_AbRMRA1xBxC3LPfx8BFA-bkloON54uewIdhOHFpHnCww5AmDaUbHA6Uc-bEo_0qwM7a6fDUbt28zvEKp6Jdw2LfWwPMmPs5MvEHIGLER-RI&gsessionid=aKDTFQfIrG1MtT2SmNFOZmiHeCJHsSDY7dJEcpM0OL9I9dp0xtXCAQ)  
  <sub>Yahoo Finance UK, 21 hours ago</sub>  
  Seasonality data is currently unavailable for 1319. Related tickers. GDX. RING. FLBR. ITB. FLLA. XHB. ESPO. FLMX. XLB. PKB. NANR. COPX. WBIY. XME. FLN. AIRR.
- [Xtr-MSCI Wld Min.Vola.ESG ETF R (XWEB.HM) stock historical prices and data](https://www.google.com/goto?url=CAESbwHEIkXXEcwLStaL3ygZfDBOLvap_Qr9UMglw8vKOHsXzNP0rjoTAlAxk42QJe03C70oWTKrc796yS3LLIURFPbbcEWqJkNj7U9BbuEOPDQTiYl40Fe4yOeRH4a4f6WL64YkHuBkngTNxQDF9MC5Uw&gsessionid=aKDTFQfIrG1MtT2SmNFOZmiHeCJHsSDY7dJEcpM0OL9I9dp0xtXCAQ)  
  <sub>Yahoo Finance UK, 20 hours ago</sub>  
  Discover historical prices for XWEB.HM stock on Yahoo Finance. View daily, weekly or monthly formats back to when Xtr-MSCI Wld Min.Vola.ESG ETF R stock was...
- [iShares S&P 500 Health Care Sector UCITS ETF EUR Hedged (Dist) (IUHE.AS) Seasonal returns chart](https://www.google.com/goto?url=CAEScwHEIkXXJW4eMXDDP817K1jjhSf3zgIiewwxnjQuYJeklEH8luXmNEsEpA4hd55d6B_YdXA5fbGbee8fGGPBcqiJGILsU82LdofYB0c_ezAlGxMdMwtSHa4wmKixWH66IzRvYdcuTHRZ-WYjHpMiRNMKenw&gsessionid=aKDTFQfIrG1MtT2SmNFOZmiHeCJHsSDY7dJEcpM0OL9I9dp0xtXCAQ)  
  <sub>Yahoo Finance UK, 22 hours ago</sub>  
  iShares S&P 500 Health Care Sector UCITS ETF EUR Hedged (Dist) (IUHE.AS). 8.32 +0.10 (+1.27%). At close: 26 November at 17:35:25 CET...
- [NEOS Ethereum High Income ETF (NEHI) Seasonal returns chart](https://www.google.com/goto?url=CAEScAHEIkXXRwglLeWsqcOzNsXOa5cCEmtnPWt8FGadKjR3W3dOcP6BTr0zH1cbga6ACCKIw-LPOgfk8sbESZCWeUGOzYLDsohW3q84QQzH_daDn0Lat1DqWAfA_S6ZZtIBT7pyoNOAtP41UclhyNKYleQ&gsessionid=aKDTFQfIrG1MtT2SmNFOZmiHeCJHsSDY7dJEcpM0OL9I9dp0xtXCAQ)  
  <sub>Yahoo Finance UK, 24 hours ago</sub>  
  NEOS Ethereum High Income ETF (NEHI) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [Invesco Global Active ESG Equity UCITS ETF USD Acc (IQSA.DE) Seasonal returns chart - Yahoo Finance](https://www.google.com/goto?url=CAEScwHEIkXX7tDdQzaisUBjMSHFZZ3L1sysdx5rjW1evQ-KlcY0oLr-vs1X2dS9YL_qDGJf-UZKx6BAhE0TCcW3Oi0V9sUVVw-18mwp6YpBRpYFKav_sAGa-o_cJ44H-weEVzViVgcbKQ2kKwwHpwZO-mO0u6s&gsessionid=aKDTFQfIrG1MtT2SmNFOZmiHeCJHsSDY7dJEcpM0OL9I9dp0xtXCAQ)  
  <sub>Yahoo Finance Singapore, 16 hours ago</sub>  
  Invesco Global Active ESG Equity UCITS ETF USD Acc (IQSA.DE). 93.11 +2.48 (+2.74%). At close: 26 November at 5:35:48 pm GMT+1...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 103.72 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 102.03 (+1.7%), 50d 98.81 (+5.0%), 200d 104.04 (-0.3%); 50d below 200d
Momentum: RSI(14) 56.4 | MACD 0.560 vs signal 0.528 (histogram 0.032)
Returns: 1d +0.0% | 5d +6.0% | 1m +5.9% | 3m -0.8%
52-week range: 92.84 - 121.36 (now 38.1% of the way up)
Volatility: ATR(14) 2.97 (2.9% of price) | annualised 20d 40.1%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 18.48 | P/B 2.18 | P/S 1.27 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +8.8% a year | beta to the market 1.40
Cost and size: expense ratio 0.35% | net assets 1.63B
What it is made of: Stocks 100.9%, Cash -0.9%
Largest holdings: Allegion PLC 3.9%, SharkNinja Inc 3.9%, Masco Corp 3.7%, Wayfair Inc Class A 3.7%, Cavco Industries Inc 3.7%
Sector mix: Consumer cyclical 62.4%, Industrials 32.7%, Basic materials 3.5%, Real estate 1.5%
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
Rolled up from the 5 largest holdings, 18.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.6% above the current prices
Holdings read: ALLE, SN, MAS, W, CVCO
Recent rating changes among them:
  - ALLE: 2026-11-03 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - SN: 2026-11-09 Guggenheim: main, Buy -> Buy
  - MAS: 2026-11-05 Argus Research: main, Buy -> Buy
  - W: 2026-11-12 Argus Research: main, Buy -> Buy
  - CVCO: 2026-11-02 Oppenheimer: reit, Outperform -> Outperform
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
Share count change: 1 week: -2.2% (-37.08M) over 7d | 1 month: +10.8% (162.37M) over 30d
Shares outstanding: 16.11M | fund size: 1.67B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro catalyst, flat flows, limited analyst coverage, and technicals show no decisive breakout.

**Main reasons it gave:**
- Analyst coverage of top holdings is 34% of fund with 100% buy rating and +11.1% price target
- Fund flows are flat over the past week and month, indicating no net demand
- Technicals show price near 52‑week high, RSI neutral, MACD bearish, and low volume, no decisive breakout
- Macro environment shows stable yields, no data surprise, and VIX still elevated, providing no catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [Graphic Packaging, Hawkins lead materials stocks' November gains (XLB:NYSEARCA)](https://seekingalpha.com/news/4676994-graphic-packaging-hawkins-lead-materials-stocks-november-gains)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Graphic Packaging leads materials stocks with a 31.36% one-month gain, followed by Hawkins at 17% and AptarGroup at 14.96%.
- [iShsV-Italy Govt Bd UCITS ETF R (IS0M.HM) Seasonal returns chart](https://uk.finance.yahoo.com/quote/IS0M.HM/seasonality/)  
  <sub>Yahoo Finance UK, 11 hours ago</sub>  
  iShsV-Italy Govt Bd UCITS ETF R (IS0M.HM) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [VanEck Quantum ETF (QNTM.AX) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESbAHEIkXXLPP4n_sVp20uKkpBEnKd4UpDzlg-k-H4Y4uac3CX59YmfjmxT9CJJN7mQV59jNYUUb85pAfiBMAvSnZfyUyCL0Fx_X0aPY39ucLUg__H9iXmpqW8049-RrNasvOUOlAaZXXKKuQp_w&gsessionid=khADNTm9XDFwtFSfa3Y4ZjevtC79hXxDrVuVKeFocFgzCKOX5FSSuQ)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  Interactive Chart for VanEck Quantum ETF (QNTM.AX), analyze all the data with a huge range of indicators.
- [XLB Nov 2026 48.000 call (XLB261127C00048000) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESdwHEIkXXWHw9jbOVmQ6JIuvA1ES08W36fyAJOYAabiGVB64UEGHL5CcIe6zNAXAkRhT0tn8-OcIfYDEGHTaGfWV001ZDM0_rFgE-9wXmrJt2pOGqSy-UBkRmZe8TGz84B0HN8x6hfdh7o6NkjiM2rJ8RNRXOiUem&gsessionid=khADNTm9XDFwtFSfa3Y4ZjevtC79hXxDrVuVKeFocFgzCKOX5FSSuQ)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  Interactive Chart for XLB Nov 2026 48.000 call (XLB261127C00048000), analyze all the data with a huge range of indicators.
- [Strive Emerging Markets Ex-China ETF (STXE) Seasonal returns chart](https://www.google.com/goto?url=CAESbwHEIkXXWAiiYNA4vd4_FYgRsJpugYblR6mXvQuiQNwU_2W2HWvMt4dCorA-M8_ymoh4mNLvVD_jXptipwgftbBrBRNhcHwqCaYAsv547nzhGb1me90WRRDZe_UsrutLNRi2utriwyoSxKoPrwa2Yw&gsessionid=khADNTm9XDFwtFSfa3Y4ZjevtC79hXxDrVuVKeFocFgzCKOX5FSSuQ)  
  <sub>Yahoo Finance UK, 21 hours ago</sub>  
  Strive Emerging Markets Ex-China ETF (STXE) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [Utilities Select Sector SPDR ETF (XLU) stock price, news, quote and history](https://www.google.com/goto?url=CAESYgHEIkXXjuvi4w45XSSQa9rWo0nRLTLu4kCS-n5x9zZwmguBIfDyoHSt7Ar64i2GbDVYS_wJRReWOzMRw-KSXDIxZUiW1lJ9LEssvIKXn6oKdi7yevOjZwzShYlx1wpLkScM&gsessionid=khADNTm9XDFwtFSfa3Y4ZjevtC79hXxDrVuVKeFocFgzCKOX5FSSuQ)  
  <sub>Yahoo Finance UK, 24 hours ago</sub>  
  Find the latest Utilities Select Sector SPDR ETF (XLU) stock quote, history, news and other vital information to help you with your stock trading and...
- [BNPPE-EUR C.Bd SRI FFr.UShDur.A (FBJLI.DE) interactive stock chart](https://www.google.com/goto?url=CAESbQHEIkXX15fC7S0ogsE5del5TKR3NfxXAQmD97f_poSDdVQYp-YBRNXO_vLVFzCfRGG6Xj-8XRPdMWLp_-2TAmW3PVHHxhAqLFg93AbN3hEMjbber34muO-YhuS8XjTlHmAZGNlY4Qu2DP-z7dw&gsessionid=khADNTm9XDFwtFSfa3Y4ZjevtC79hXxDrVuVKeFocFgzCKOX5FSSuQ)  
  <sub>Yahoo Finance UK, 21 hours ago</sub>  
  Interactive chart for BNPPE-EUR C.Bd SRI FFr.UShDur.A (FBJLI.DE) – analyse all of the data with a huge range of indicators.
- [iShsVII-NASDAQ 100 UCITS ETF R (SXRV.HA) Seasonal returns chart](https://www.google.com/goto?url=CAEScgHEIkXXIV_qEKnRTVAvpUwb73XbLfKEhzJsEbcx8DAyAGbSqDhpPvALOVaWT66-NyySulvdGKiWDWP1MvKMnLw8vuyehP21VlRwvZf_zx2tBZgtKLTxEL48j3pcccLbPCyLsa0W0xOJTRbi9GqzFLxPAQ&gsessionid=khADNTm9XDFwtFSfa3Y4ZjevtC79hXxDrVuVKeFocFgzCKOX5FSSuQ)  
  <sub>Yahoo Finance UK, 21 hours ago</sub>  
  iShsVII-NASDAQ 100 UCITS ETF R (SXRV.HA) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [Virtune Avalanche ETP (VIRAVAXE.HE)](https://www.google.com/goto?url=CAEScwHEIkXXwnlKD3ukyQFx_93fKeeias0pQx5-FsE1-NwAas11rOY7M0rj6jv07wL6pHk6hFTh34jyL0eZoL-mNC4vGVbyPqq6liicr33DAmsmFM1f0wVA9paLL3LYNUSZXvfcBEJwZ0ML8qiLJIMDBFKEBTI&gsessionid=khADNTm9XDFwtFSfa3Y4ZjevtC79hXxDrVuVKeFocFgzCKOX5FSSuQ)  
  <sub>Yahoo Finance Singapore, 19 hours ago</sub>  
  Holdings data is currently unavailable for VIRAVAXE.HE. Related tickers. GDX VanEck Gold Miners ETF. 73.89 +4.39%. RING iShares MSCI Global Gold Miners ETF.
- [Tradr 2X Long UPST Daily ETF (UPSX) Seasonal returns chart](https://www.google.com/goto?url=CAESbwHEIkXXaDUUnZWOD7bIBBbxK_8bvOl8Ux6eA8O20LhI8KfMoko8BapTQIun4v-Zk1ZRq6wXj9y1KfcJbJ1FvI_FNIb46pYOOplKYweCqTC8ZYYR-1fKB9lkYjibgtDHfRiYRfUPCK1DqU9ygKTmyA&gsessionid=khADNTm9XDFwtFSfa3Y4ZjevtC79hXxDrVuVKeFocFgzCKOX5FSSuQ)  
  <sub>Yahoo Finance UK, 14 hours ago</sub>  
  Tradr 2X Long UPST Daily ETF (UPSX) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 51.61 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 51.70 (-0.2%), 50d 50.80 (+1.6%), 200d 51.20 (+0.8%); 50d below 200d
Momentum: RSI(14) 52.6 | MACD -0.253 vs signal -0.124 (histogram -0.129)
Returns: 1d +0.8% | 5d +4.4% | 1m -0.5% | 3m -3.0%
52-week range: 43.39 - 53.90 (now 78.2% of the way up)
Volatility: ATR(14) 1.08 (2.1% of price) | annualised 20d 27.4%
Volume: 0.18x the 20-day average
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
Three-year record: +10.2% a year | beta to the market 0.76
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.1% above the current prices
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
Shares outstanding: 71.92M | fund size: 3.71B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, mixed fundamentals, strong analyst coverage but limited to 59% of fund, bullish inventory draw offset by bearish gas price outlook.

**Main reasons it gave:**
- No macro surprise: yields unchanged, VIX down but still high, inflation and unemployment in line with expectations
- Flat fund flows: share count unchanged over 1 week and 1 month
- Analyst coverage: 100% buy on 59% of fund, price target +14.8% above current prices
- Energy inventories: crude oil draw of -0.9% and low 10% percentile (bullish supply outlook)
- EIA gas price forecast: natural gas price expected to fall 11% over six months (bearish for gas)

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Energy Select Sector SPDR ETF (XLE)](https://sg.finance.yahoo.com/quote/XLE/options/?date=1795996800&straddle=false&type=all)  
  <sub>Yahoo Finance Singapore, 17 hours ago</sub>
- [Top energy stocks in November: EagleRock Land, Range Resources, Excelerate Energy (XLE:NYSEARCA)](https://seekingalpha.com/news/4676990-top-energy-stocks-in-november-eaglerock-land-range-resources-excelerate-energy)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  As the month of November 2026 comes to a close, the broader stock market has exhibited a mix of late-autumn consolidation and selective sector rotation.
- [XLE Dec 2026 62.000 put (XLE261202P00062000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScQHEIkXXKOc3olzEGzh5-5D_MlidYJ_KKDK3MEiThD38i8IudUndDPHgskRi7ZnBTxJO8xUPE2jpdscyayLCq2VuLOy6QZcptUN3SBJTXu9M1-DWn7ZdGZmWSWSk2EDLCNl-xpUIxkGE2pJiF-i8JA_R&gsessionid=rmTFKfvJfSz0zsK9h7gjM9tk74Vj8dd9isMKKiD-DZ0GSqa0MMp4KQ)  
  <sub>Yahoo! Finance Canada, 9 hours ago</sub>
- [Trump admin urged Venezuela, Iraq to quit OPEC, blocked Venezuela’s membership dues: Reuters](https://www.google.com/goto?url=CAESuQEBxCJF1zdjyPdgcbKHYHqCoVo_z_vDgi4aPV05eseej10H5zhi4NaUAvzg6SF6CYkPHuLQ8YtHNdRx2XoVLDAN0sQUHJcBrtrSzpIR7cxsBxdqQtL9DPj9xquK8AtBh0Ugngp_cDbaiiBz_M_U3Cc_kYbXZW5WXGVozx-pKmAEbVqBKto-ZvKcdrsDeyFgyqhJ2zYSAhN_AvtSSR4EH-Uy7t8JdOgeKNY-RxPvlRbfQ6ziB5rmoCDceg&gsessionid=rmTFKfvJfSz0zsK9h7gjM9tk74Vj8dd9isMKKiD-DZ0GSqa0MMp4KQ)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  Reuters says the Trump administration urged Venezuela and Iraq to consider leaving OPEC and blocked Venezuela's annual dues; Saudi intervention eased...
- [SFI Advisors, LLC's State Street Energy Select Sector SPDR ETF(XLE) Holding History](https://www.google.com/goto?url=CAESfQHEIkXX4Isw6sAIE71ugcwINmixGzrm_TZmaP2uMznqWBsqWq6bwSQgIvv6dmbV6qVLxx66AapGy20-zHL8jXQJqiy8YIFgHRvWZTraLxrJQvY0Q_Xv89DdVLKen19-RoNEz5J3lOWQms3C7r3lWEI-Xe52AYQrUSaX8WPa&gsessionid=rmTFKfvJfSz0zsK9h7gjM9tk74Vj8dd9isMKKiD-DZ0GSqa0MMp4KQ)  
  <sub>GuruFocus, 22 hours ago</sub>  
  State Street Energy Select Sector SPDR ETF(XLE) Buys and Sells Made by SFI Advisors, LLC. Latest and Historical Data and Chart.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 61.83 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 63.02 (-1.9%), 50d 64.38 (-4.0%), 200d 59.87 (+3.3%); 50d above 200d
Momentum: RSI(14) 43.5 | MACD -1.272 vs signal -1.061 (histogram -0.211)
Returns: 1d +1.5% | 5d +1.5% | 1m -9.7% | 3m -1.4%
52-week range: 43.81 - 70.02 (now 68.8% of the way up)
Volatility: ATR(14) 1.48 (2.4% of price) | annualised 20d 31.3%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Equity Energy
What it holds: P/E 17.48 | P/B 2.46 | P/S 1.71 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +16.4% a year | beta to the market -0.22
Cost and size: expense ratio 0.08% | net assets 46.37B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ExxonMobil Holdings Corp 24.3%, Chevron Corp 18.3%, ConocoPhillips 7.3%, Marathon Petroleum Corp 4.6%, Phillips 66 4.5%
Sector mix: Energy 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.40</summary>

```text
US inventories, week ending 2026-10-30 (published the following Wednesday)
  Crude oil: 409.8 million barrels, -0.9 on the week (a draw), 10% percentile over 52 weeks -- low for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

```text
Rolled up from the 5 largest holdings, 59.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.10 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.8% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 186.42M | fund size: 11.53B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fund flows flat: 0% share count change over 1 week and 1 month
- Analyst coverage 43.3% of fund, 70.7% buy rating, weighted price target +8.5%
- Technical: price 56.98 below 20‑day SMA (57.20) but above 50‑day SMA (55.86), RSI 52.1, MACD histogram -0.190
- Macro: Treasury yields stable (10‑yr 4.89% down 0.16), VIX down 9.6% to 26.28, inflation 3.7% (no surprise indicated)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 56.98 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 57.20 (-0.4%), 50d 55.86 (+2.0%), 200d 54.07 (+5.4%); 50d above 200d
Momentum: RSI(14) 52.1 | MACD -0.022 vs signal 0.168 (histogram -0.190)
Returns: 1d +0.8% | 5d +2.5% | 1m +1.5% | 3m -1.9%
52-week range: 47.81 - 59.20 (now 80.5% of the way up)
Volatility: ATR(14) 1.01 (1.8% of price) | annualised 20d 24.8%
Volume: 0.07x the 20-day average
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
Three-year record: +18.7% a year | beta to the market 0.68
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 43.3% of the fund by weight
Ratings by weight: buy 70.7% | hold 29.3% | sell 0.0% (mean 1.99 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +8.5% above the current prices
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
Shares outstanding: 883.44M | fund size: 50.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected) (Bing's feed, direct: 3 headline(s), none naming XLF)

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Given the thin analyst coverage (24% of the fund) despite a bullish consensus, flat fund flows indicating no new demand, and technicals showing the ETF trading below its short- and long-term averages with weak momentum, there is no clear catalyst to shift the outlook. Macro conditions are stable with no surprise data. Therefore the overall stance remains neutral.

**Main reasons it gave:**
- Analyst view covers 24% of fund, all buy with +29.6% price target (thin coverage)
- Fund flows flat over past month, indicating no net demand
- Technical trend below 20d, 50d, and 200d SMAs; RSI 48, MACD slightly negative, showing weak momentum
- Macro: yields modestly down, VIX down but still elevated, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

- [State Street's Industrial Select Sector SPDR ETF (NYSEARCA: XLI) Deploys $242.4M Across All 83 Holdings In Zero-Sell Session](https://www.foreignpolicyjournal.com/2026/11/27/state-streets-industrial-select-sector-spdr-etf-nysearca-xli-deploys-242-4m-across-all-83-holdings-in-zero-sell-session/)  
  <sub>Foreign Policy Journal, 2 hours ago</sub>  
  A rare all-in trading session unfolded at State Street's Industrial Select Sector SPDR ETF (NYSEARCA: XLI) on November 24, 2026, with the $29.29 billion...
- [Financial Select Sector SPDR ETF (XLF) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/XLF/)  
  <sub>Yahoo Finance UK, 7 hours ago</sub>  
  Find the latest Financial Select Sector SPDR ETF (XLF) stock quote, history, news and other vital information to help you with your stock trading and...
- [State Street's Industrial ETF (NYSE: XLI) Lifts Every Single Holding On Nov. 23, Deploying $251.7 Million Across 83 Stocks](https://www.google.com/goto?url=CAES4AEBxCJF16Rs7BtGpGsEK33PFz6Iw1YjwetVgNt61MKjQIUFLVVZGLx6YbtUje-VPKte6KBICJ6ENVk7B_Nx3KSMu_Mql-fKRGDGNy9z4rQpHCFaAphpHtjUtiV15f-8Kecfr3ps9pB1r0Gku0iJ5e-saRVuWRA6nmBpjcRHXVXoS_q_EQ-1fbCc4D4ID_IQ0ks4v4De64kF8c2nbZIaj9eq5hcXJRPiHZiqGh6Zg3hp8UK3kgzx9RqK0-SNSslRrLRKbXAqTrcvJ0ql3X_TE7vZtWJITKT3T1DBOTrtIS8K-Q&gsessionid=luiJ-qvmegz7JZRKhYMbLXMnefcrnungh1CFlPngQSv5xrNpSXHSOw)  
  <sub>Foreign Policy Journal, 21 hours ago</sub>  
  A sweep of buying activity with zero position reductions makes the State Street Industrial Select Sector SPDR ETF (NYSE: XLI) session on November 23, 2026,
- [$306 Million Single-Session Sweep Lifts Every Position In State Street's (NYSEARCA: XLK) Tech ETF](https://www.google.com/goto?url=CAESyQEBxCJF16qMdL8luDppvnlUzzr54HpJnlqLs78OCirMJIMK18xxzikGhtOYDMgyyGPkzTVUGZ1VHsASXwwyPGv0zSr8yKSWcCwqMixDKVlvfYi42wZuun_eX8UIg1Wmxb8bkjaWMjE7Toar-eSdTRJzrM5UpI-1b9ZkAH-q7XJNhxsJcvTi6CJlXS1lievlhXKYnQjKf0Apsbn_7lyyhQrPs6hnRwc-6lntdp5LgPSHV6lGD1T-YmY_WF56AwnURGeYGPXYZlSQafc&gsessionid=luiJ-qvmegz7JZRKhYMbLXMnefcrnungh1CFlPngQSv5xrNpSXHSOw)  
  <sub>Foreign Policy Journal, 23 hours ago</sub>  
  Not a single holding was left untouched as the State Street Technology Select Sector SPDR ETF (NYSEARCA: XLK) deployed $306.2 million across all 76 of its.
- [Top industrials stocks in November: Avis Budget, AECOM, Allegiant Travel (XLI:NYSEARCA)](https://www.google.com/goto?url=CAESpgEBxCJF1yF_sgN0tpHd602WcKZBEJvZTWFJw5lnV3EpnqK_UqprPfp1D1COYFIpQ4T2ByqMrpdoXe8fqDzr_Uk8RkRDZyv9xoTQuD1fRwFKWUOjsy24rijzC_LoXY8RdCirKAddUtY2tiUZmDWeqzUk8MoNp2dO-Mgc-43MRzOfCkdNFEjbvhb2R8G3ojyCVFZqExEmgliVb6n8jEuq0GpFNMf_IYUk&gsessionid=luiJ-qvmegz7JZRKhYMbLXMnefcrnungh1CFlPngQSv5xrNpSXHSOw)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Avis Budget Group leads industrials stocks with a 39.94% one-month gain, followed by AECOM at 37.92% and Allegiant Travel at 35.61%.
- [Utilities Select Sector SPDR ETF (XLU) stock price, news, quote and history](https://www.google.com/goto?url=CAESYgHEIkXXnK5agVX7KLujD1-uh91vhehw1YmlakS8uNnxIuQ2Uw9e9cmjqdMoACkhrB6Yxx93x6j18NXOeIzx-Ogq056wqxIb2TujaHKZUbfBMGdn0aQ-h7jDHMckOidTTtwH&gsessionid=luiJ-qvmegz7JZRKhYMbLXMnefcrnungh1CFlPngQSv5xrNpSXHSOw)  
  <sub>Yahoo Finance UK, 24 hours ago</sub>  
  Find the latest Utilities Select Sector SPDR ETF (XLU) stock quote, history, news and other vital information to help you with your stock trading and...
- [Richmond Manufacturing Index: Activity Improved In November](https://www.google.com/goto?url=CAESngEBxCJF18syeLmEjVDju4JUqTSC37OhJgHkB5dIqcgeZnobd28KorgaxLyvIq7Qxy_ZMf_8EfdU592mJJqmEA5G6wUaTRNZ7sMiSuua930OR1stXkFL0TOLLzOnjr5foyYK44Vf9z0PWhyjfpQZ4q3qDlKyWDhpT0McG02gfoF1kYmxQ_wzs--Pm9hpUlT8NMKVCBvFdgKnG38SXKmeSQ&gsessionid=luiJ-qvmegz7JZRKhYMbLXMnefcrnungh1CFlPngQSv5xrNpSXHSOw)  
  <sub>Seeking Alpha, 13 hours ago</sub>  
  The composite manufacturing index rose five points to 3, marking its first positive reading since August. The future indexes for shipments and new orders...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 164.55 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 165.71 (-0.7%), 50d 167.43 (-1.7%), 200d 173.10 (-4.9%); 50d below 200d
Momentum: RSI(14) 48.0 | MACD -1.687 vs signal -1.457 (histogram -0.230)
Returns: 1d +1.0% | 5d +2.0% | 1m -2.3% | 3m -7.1%
52-week range: 151.44 - 186.51 (now 37.4% of the way up)
Volatility: ATR(14) 3.71 (2.3% of price) | annualised 20d 31.5%
Volume: 0.13x the 20-day average
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
Three-year record: +16.9% a year | beta to the market 1.00
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 24.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.74 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +29.6% above the current prices
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
Shares outstanding: 136.63M | fund size: 22.48B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break on heavy volume; bullish analyst view and strong inflows are offset by bearish technicals and high valuations.

**Main reasons it gave:**
- Analyst view: 100% buy rating, weighted price target +36.6% above current
- Fund flows: share count up 4% in one week and 11.9% in a month
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 38.6; volume 0.08× 20‑day average
- Macro: no policy surprise; yields unchanged, VIX down but still elevated

<details><summary><b>News</b> — score +0.00</summary>

- [XLK Nov 2026 184.000 put (XLK261127P00184000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLK261127P00184000/)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  Find the latest XLK Nov 2026 184.000 put (XLK261127P00184000) stock quote, history, news and other vital information to help you with your stock trading and...
- [$306 Million Single-Session Sweep Lifts Every Position In State Street's (NYSEARCA: XLK) Tech ETF](https://www.foreignpolicyjournal.com/2026/11/26/306-million-single-session-sweep-lifts-every-position-in-state-streets-nysearca-xlk-tech-etf/)  
  <sub>Foreign Policy Journal, 23 hours ago</sub>  
  Not a single holding was left untouched as the State Street Technology Select Sector SPDR ETF (NYSEARCA: XLK) deployed $306.2 million across all 76 of its.
- [Cramer Turns Eyes to Retail Stocks and Highlights His 2 Favorites](https://www.google.com/goto?url=CAESfwHEIkXXIT_XLqCJC8u2snFmdvk7r2rl3Sr8pmz-5iGj6r9FgLWp1-KAkevwBUPCIIrPq4sejEnjZExYG6pmZGsNmMVUGgJOXw9BkF0eNWufC3V1_8WwNUwa1BPYTbJnngO_WIEXOhIet9gZP0LqNLNFxEq_PcfJjmegnzN62-g&gsessionid=HJwgGx3bnBlPiU123fd00kVSf_yHMJx-dLqP9W9DUc39_cDHrBudng)  
  <sub>BeInCrypto, 24 hours ago</sub>  
  Jim Cramer sorts six retail stocks after Tuesday earnings and praises 2 as the sector outpaces tech this quarter.
- [As Paranoia Hits The Market, Here Are 5 Stocks I'm Buying This Holiday Season](https://www.google.com/goto?url=CAESrAEBxCJF11I8ujiR_Z6DbtuaURJVJCbP-M90VlJLSSBW2hjl6gj3M7JkOhdoveHt-6fp8NSICwwmYplFUnOJSKTNUMQ3n6HA5bTzIhwTO_BenoJFk1HiKT-BexR6PzJ6rzyMHMtBOB7NJZ1GnBFLvsJWtFi1QafT6Dke6aRD_EuO7V7aEz9Wx8q4odOAGTA_WfB5aL6u9gJKl6jItR12Q88aOdWaCeOmVfn3x4J1&gsessionid=HJwgGx3bnBlPiU123fd00kVSf_yHMJx-dLqP9W9DUc39_cDHrBudng)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  The bull case for AI semiconductor stocks: a 40% SOX drop cuts forward multiples to 11.7x, creating an entry as AI fundamentals hold.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 157.27 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 166.31 (-5.4%), 50d 182.26 (-13.7%), 200d 171.61 (-8.4%); 50d above 200d
Momentum: RSI(14) 38.6 | MACD -7.350 vs signal -6.821 (histogram -0.529)
Returns: 1d +1.0% | 5d -2.1% | 1m -17.7% | 3m -15.3%
52-week range: 127.50 - 202.00 (now 40.0% of the way up)
Volatility: ATR(14) 6.80 (4.3% of price) | annualised 20d 60.6%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Technology
What it holds: P/E 31.66 | P/B 11.55 | P/S 8.87 | 3y earnings growth n/a
Yield: 0.5%
Three-year record: +19.8% a year | beta to the market 1.56
Cost and size: expense ratio 0.08% | net assets 118.67B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Apple Inc 15.3%, NVIDIA Corp 15.1%, Microsoft Corp 11.8%, Broadcom Inc 4.7%, Advanced Micro Devices Inc 4.5%
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

```text
Rolled up from the 5 largest holdings, 51.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +36.6% above the current prices
Holdings read: AAPL, NVDA, MSFT, AVGO, AMD
Recent rating changes among them:
  - AAPL: 2026-11-11 China Renaissance: up, Hold -> Buy
  - NVDA: 2026-11-12 Melius Research: down, Buy -> Hold
  - MSFT: 2026-10-29 Bernstein: main, Outperform -> Outperform
  - AVGO: 2026-10-27 Rosenblatt: main, Buy -> Buy
  - AMD: 2026-11-12 B of A Securities: main, Buy -> Buy
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
Share count change: 1 week: +4.0% (4.53B) over 7d | 1 month: +11.9% (12.67B) over 34d
Shares outstanding: 755.71M | fund size: 118.85B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals not decisive, flows flat, analyst view bullish but not enough to outweigh neutral macro and technicals.

**Main reasons it gave:**
- Yield curve unchanged (10y-3m spread +0.73) and no rate surprise
- Technicals: price above 20d/50d/200d SMAs but MACD below signal and volume 0.14x average
- Fund flows flat (0% change week/month) indicating no net demand shift
- Analyst view: 100% buy rating on top holdings, price target +4.1% above current

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance Singapore, 4 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) · 1.39% · 2.45% · 22.54% · 18.66% · 15.69% · 38.67% · 640.27%. Key events. Baseline. Advanced chart.
- [How GLP 1 Coverage Could Send You Beyond XLV](https://finance.yahoo.com/healthcare/articles/glp-1-coverage-could-send-120946100.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Two of these healthcare funds could not be more different once you look under the hood. IHE keeps about 99.5% in pharmaceuticals, while XLV has roughly...
- [State Street Health Care Select Sector SPDR ETF (Derivative) price today, XLV to USD live price, marketcap and chart](https://www.google.com/goto?url=CAESmwEBxCJF16U1pgWBHPqr9ZWTpTVJkRHx9ecItNM3m6rWoGGFtFIRmV5Ryk4yUKsr2LlQ6-8pA_0BWhV524Fy-PGms6yBMLK0pcmZbdmEq-YzIQtrXsFc0J5rFHNDmUutRZqrL1JYJ3TRYpR-pj5vBimeMnf1R-B42u2Ecb-7x9tAjhr0Yrm9m-Jr9nA70A5moUo8RjcuHOUSLBVKHQ&gsessionid=oa4k2sdo-us32tvf0P7bzbwfWiZoHRnj39byAiRIN8BOeXAcAW76Ng)  
  <sub>CoinMarketCap, 21 hours ago</sub>  
  The live State Street Health Care Select Sector SPDR ETF (Derivative) price today is $183.14 USD with a 24-hour trading volume of $0 USD. We update our XLV...
- [S&P 500 Sector Rotation Tracker: Consumer Staples lead as investors get defensive](https://www.google.com/goto?url=CAES3gEBxCJF11fCVphxjdxxaNJWlMh0ALE0hcIVpULzC3OZ2h3JpdxdRz9pZ0L7OB-Nfx3a0InGXLXMfcJ5TwtZ9XF-O_uV2gl8tLB_6ddI_nqssxF6Vk0WoJlipoFVTL8FNuZEpmbnIKR2IpO2b9dhI5q_dlNLwK_qR-kAz3fRiPMnNGZYcY_1ieq4QI4jrkFljNbZrKwWeGaCKgtP1nmkmfDWnH7vzOWUY2kDE8C_KoQJbykZ8s2T1EsJy1mKo8K3gHc-DVUf-9rUaS9P4CdjRqS2KZ5vI0wiDyuP_Icksyg&gsessionid=oa4k2sdo-us32tvf0P7bzbwfWiZoHRnj39byAiRIN8BOeXAcAW76Ng)  
  <sub>TradingView, 20 hours ago</sub>  
  Consumer Staples XLP has climbed 4.1% over the past month, leading all 11 S&P 500 market sectors amid a broader market pullback that saw the S&P 500 ETF SPY...
- [Utilities Select Sector SPDR ETF (XLU) stock price, news, quote and history](https://www.google.com/goto?url=CAESYgHEIkXXbW-5EFW-jycNR94cut5pSTtYaQIHDy_obSuymxExglfHy5u_j_YclnILjNK9vHndK3XxyBGzs8aFSTj8WZd5Zra3G47615UImCbkfIqhebMsO6kSIqq4HbGrdGIu&gsessionid=oa4k2sdo-us32tvf0P7bzbwfWiZoHRnj39byAiRIN8BOeXAcAW76Ng)  
  <sub>Yahoo Finance UK, 24 hours ago</sub>  
  Find the latest Utilities Select Sector SPDR ETF (XLU) stock quote, history, news and other vital information to help you with your stock trading and...
- [Form 4 State Street® Consumer Staples Select Sector SPDR® ETF For: 27 November](https://www.google.com/goto?url=CAESxAEBxCJF16Vk__-zBcZD1T2ILSDGDV-2I0-9VodmackII9KWJzcr10XCBIXeLX07ZdnBG8hvwUkI-8lyF7FFhEjelJ9EmUQsYFNX0zXc8xQM7YUZAjDo8dPQNExwkoMw5naQJYPj0skQv-UACgmz6zOHecTcaucaDQg41tKUN6j0bdnCkqY1DMm2uinWBZTQeN0M-NyDDLd7nrRwXLwbnahyAHkiVVooFsSlr4v6-A9R_sJgnVyEd2Dj1vqVS8aK_fGRqxx8&gsessionid=oa4k2sdo-us32tvf0P7bzbwfWiZoHRnj39byAiRIN8BOeXAcAW76Ng)  
  <sub>Investing.com UK, 3 hours ago</sub>  
  The information in this preliminary pricing supplement is not complete and may be changed. This preliminary pricing supplement is not an offer to sell nor...
- [Walmart, McDonald's Rally as GLP-1 Drugs Shrink Food Bills - Walmart (NASDAQ:WMT)](https://www.google.com/goto?url=CAESpQEBxCJF15EvqWkZVUr1AE-Y6xvacnUKj3C9Lq-DAm6TfY5I4rdd9raHLYAy4O8rgyeKpQxJPuPLrwu5Fm5TqKROvxFvf9x5yRJy-uhXaeykTw1eG6fCXnDDkyS35ge7jzdT027ExfrZ-jmZKUSWbvkKCUiP_504hxbLp_FmntzRUObE2ndY2XL4Z4ILU1PMK74Js77IhCxrAi5vPKouqNesyndDGVI&gsessionid=oa4k2sdo-us32tvf0P7bzbwfWiZoHRnj39byAiRIN8BOeXAcAW76Ng)  
  <sub>Benzinga, 21 hours ago</sub>  
  GLP-1 users could hit 60 million by 2030. Yet XLP just had its best two months vs. SPY since 1998 as money fled tech into food stocks.
- [Consumer Staples Leads S&P 500 Sectors With 4.1% Monthly Gain](https://www.google.com/goto?url=CAESaQHEIkXX3D0q92tCzRCuJ0m6fmx9eyfDWwde-EUPXkCLsexJLyWEmn9DgsKFYTfeOyf0stWOwHdudMWaRjRslpZzO9jQ-ogVBsAKq6_SJNT8dYGDo3_UmtQDyBSmYdxEZS2Bq8b9a2qwrg&gsessionid=oa4k2sdo-us32tvf0P7bzbwfWiZoHRnj39byAiRIN8BOeXAcAW76Ng)  
  <sub>www.tokenpost.com, 20 hours ago</sub>  
  The Consumer Staples Select Sector SPDR ETF (XLP) led all 11 S&P 500 sector groups with a 4.1% gain in the month through Nov. 26, even as the broader market...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 92.31 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 91.08 (+1.3%), 50d 87.03 (+6.1%), 200d 85.11 (+8.5%); 50d above 200d
Momentum: RSI(14) 61.4 | MACD 1.190 vs signal 1.321 (histogram -0.132)
Returns: 1d +0.0% | 5d +2.7% | 1m +6.3% | 3m +8.0%
52-week range: 76.62 - 92.60 (now 98.2% of the way up)
Volatility: ATR(14) 1.43 (1.5% of price) | annualised 20d 20.5%
Volume: 0.14x the 20-day average
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
Three-year record: +12.4% a year | beta to the market 0.39
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 41.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.1% above the current prices
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
Shares outstanding: 210.17M | fund size: 19.40B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise or decisive technical break; bullish analyst view and strong inflows are offset by short‑term technical weakness and high valuation.

**Main reasons it gave:**
- Analyst view: 100% buy rating on 45.4% of fund, price target +10.1% above current price
- Fund flows: share count up 9.6% over past month, indicating net inflows
- Technical indicators: price below 20‑day SMA and MACD histogram negative, suggesting short‑term weakness
- Macro environment: no policy surprise, yields stable, VIX down but still elevated

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance Singapore, 4 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) · 1.39% · 2.45% · 22.54% · 18.66% · 15.69% · 38.67% · 640.27%. Key events. Baseline. Advanced chart.
- [How GLP 1 Coverage Could Send You Beyond XLV](https://finance.yahoo.com/healthcare/articles/glp-1-coverage-could-send-120946100.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Two of these healthcare funds could not be more different once you look under the hood. IHE keeps about 99.5% in pharmaceuticals, while XLV has roughly...
- [State Street Health Care Select Sector SPDR ETF (Derivative) price today, XLV to USD live price, marketcap and chart](https://www.google.com/goto?url=CAESmwEBxCJF1wNapVf4vyW6ET9z-knMLdw_u3ajqCCR1ErPgBBIt20stnhx_Uw3oqrmyjdP5VyW0wXpLUgtxGOIA3Ik7PnDgaNv_i_6gnH2I6_78bo5yuJtjsVkQjcgFuERSNb-oM6jmzjmhj1adlvRDugHqnLrTdvWIamxpGaGMUobqEcJpNygtnk8dE-XwujqhZ2gWILljiDac21IgA&gsessionid=_MMRfN9Igx-4fwJ312kSFYtQvl7jOGj2HY3k0yvZ4lHQZOK6Y9Rftg)  
  <sub>CoinMarketCap, 21 hours ago</sub>  
  The live State Street Health Care Select Sector SPDR ETF (Derivative) price today is $183.14 USD with a 24-hour trading volume of $0 USD. We update our XLV...
- [Is Recent Wall Street Sell-Off a Buying Opportunity? ETFs in Focus](https://www.google.com/goto?url=CAESpQEBxCJF13pDXdz8NJn-Y4L9gHpgaCutg-ER0CoUMauN1wah7SuGoYjolz7MuPD_c8iWAMrMkOUPnxV-VcjuFAf873ySGYEhvrqgD3ZgfdShn4ysmJHQu_eMzDmelOFVg7Mmh4dKH7Ap-wGtjRU3KDQNlT-WjNNZl8-eFuum7STUuPwrLSL8xHMlhKQlYha8nTQLF4z_IP_c5a_LV2cqxmYVOKbT2sA&gsessionid=_MMRfN9Igx-4fwJ312kSFYtQvl7jOGj2HY3k0yvZ4lHQZOK6Y9Rftg)  
  <sub>Zacks Investment Research, 2 hours ago</sub>  
  Extreme market fear has historically preceded strong stock returns. Explore five ETFs that could benefit from a potential rebound.
- [Utilities Select Sector SPDR ETF (XLU) stock price, news, quote and history](https://www.google.com/goto?url=CAESYgHEIkXXm_WKdd9zOHqbWQ-3oxgFI6Gnthg5hBdMQ4rIXTrm9ihNF8vB80DRqicsOINM-L95pK04ZfsoWBzoyDFynZI0N6HERQB-P2qacL9pQ5eupVaqpWpiiahDnmWJ4EkC&gsessionid=_MMRfN9Igx-4fwJ312kSFYtQvl7jOGj2HY3k0yvZ4lHQZOK6Y9Rftg)  
  <sub>Yahoo Finance UK, 24 hours ago</sub>  
  Find the latest Utilities Select Sector SPDR ETF (XLU) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 183.32 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 184.79 (-0.8%), 50d 177.68 (+3.2%), 200d 161.40 (+13.6%); 50d above 200d
Momentum: RSI(14) 52.7 | MACD 0.951 vs signal 1.766 (histogram -0.815)
Returns: 1d -0.2% | 5d +3.3% | 1m +2.0% | 3m +7.1%
52-week range: 142.84 - 189.66 (now 86.5% of the way up)
Volatility: ATR(14) 3.45 (1.9% of price) | annualised 20d 23.7%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Health
What it holds: P/E 30.14 | P/B 4.82 | P/S 1.66 | 3y earnings growth n/a
Yield: 1.4%
Three-year record: +13.8% a year | beta to the market 0.41
Cost and size: expense ratio 0.08% | net assets 49.10B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Eli Lilly and Co 16.9%, Johnson & Johnson 9.8%, AbbVie Inc 7.8%, Merck & Co Inc 5.5%, UnitedHealth Group Inc 5.4%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 45.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.74 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.1% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-11-09 Jefferies: main, Buy -> Buy
  - JNJ: 2026-10-16 Wells Fargo: main, Overweight -> Overweight
  - ABBV: 2026-11-02 UBS: main, Neutral -> Neutral
  - MRK: 2026-11-02 Freedom Broker: main, Hold -> Hold
  - UNH: 2026-10-27 Wells Fargo: main, Overweight -> Overweight
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
Share count change: 1 week: +0.3% (158.08M) over 7d | 1 month: +9.6% (4.29B) over 34d
Shares outstanding: 265.96M | fund size: 48.76B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Overall neutral as no material macro surprise or decisive technical break; analyst view bullish but not enough to outweigh mixed technicals and modest fund inflows.

**Main reasons it gave:**
- Analyst view: 100% buy rating with weighted price target +16.6% above current price
- Fund flows: net inflow of +3.4% over the past month
- Technicals: price above 20‑day/50‑day/200‑day SMAs but MACD histogram negative and volume 0.11× 20‑day average
- Macro: yields unchanged, VIX down but still stressed, inflation 3.7% (no surprise)

<details><summary><b>News</b> — score +0.00</summary>

- [Top consumer discretionary stocks in November: ADT, Chipotle, Crocs (XLY:NYSEARCA)](https://seekingalpha.com/news/4677027-top-consumer-discretionary-stocks-in-november-adt-chipotle-crocs?utm_source=tradingview&utm_medium=referral&feed_item_type=news)  
  <sub>Seeking Alpha, 59 minutes ago</sub>  
  Consumer discretionary stocks: ADT leads one-month performance with a 43.33% gain, followed by Chipotle at 35.90% and Crocs at 34.14%.
- [Black Friday Deals, Record Online Sales Put These ETFs in Focus](https://www.tradingview.com/news/zacks:e357b8458094b:0-black-friday-deals-record-online-sales-put-these-etfs-in-focus/)  
  <sub>TradingView, 3 hours ago</sub>  
  An estimated 182.7 million consumers plan to shop during the Thanksgiving weekend this year, per NRF. Black Friday remains the most popular shopping day of...
- [Utilities Select Sector SPDR ETF (XLU) stock price, news, quote and history](https://www.google.com/goto?url=CAESYwHEIkXXsiqYj7DI2-7rxj7LqaAgfPhu2RQHrw6UBM12037XvUCJMGHhXQyDonSH-YS6SivjxnanUHpLGqE_s8nb-uJ_cPfRS094VfLHOboPH0bhMjdTbjkTa3yYvykYsko3uA&gsessionid=XlSCKxQo2SaW-kiq0grHxxzQ10RQxPqWluJ0iFXhTC0aaSZ_-Z4pbg)  
  <sub>Yahoo Finance UK, 24 hours ago</sub>  
  Find the latest Utilities Select Sector SPDR ETF (XLU) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 118.49 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 118.27 (+0.2%), 50d 114.66 (+3.3%), 200d 115.34 (+2.7%); 50d below 200d
Momentum: RSI(14) 53.7 | MACD 0.525 vs signal 0.846 (histogram -0.321)
Returns: 1d +0.9% | 5d +2.3% | 1m +2.7% | 3m +1.1%
52-week range: 105.66 - 124.52 (now 68.0% of the way up)
Volatility: ATR(14) 2.76 (2.3% of price) | annualised 20d 34.2%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 24.15 | P/B 5.62 | P/S 2.30 | 3y earnings growth n/a
Yield: 0.8%
Three-year record: +12.7% a year | beta to the market 1.10
Cost and size: expense ratio 0.08% | net assets 22.40B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Amazon.com Inc 21.3%, Tesla Inc 18.8%, The Home Depot Inc 5.5%, McDonald's Corp 4.5%, TJX Companies Inc 4.1%
Sector mix: Consumer cyclical 98.8%, Technology 1.2%
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
Rolled up from the 5 largest holdings, 54.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.78 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.6% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, TJX
Recent rating changes among them:
  - AMZN: 2026-11-03 Freedom Broker: main, Buy -> Buy
  - TSLA: 2026-11-05 GLJ Research: reit, Sell -> Sell
  - HD: 2026-11-10 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-11-06 Argus Research: main, Buy -> Buy
  - TJX: 2026-11-10 UBS: main, Buy -> Buy
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
Share count change: 1 week: -0.5% (-107.70M) over 7d | 1 month: +3.4% (736.07M) over 34d
Shares outstanding: 190.31M | fund size: 22.55B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Top Tokenized ETFs by Market Cap](https://www.coingecko.com/en/etfs)  
  <sub>Coingecko, 2 hours ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...
- [Asian stocks jump on U.S. futures rally, China profit beats, shrugging off tariff risks](https://seekingalpha.com/news/4676916-asian-stocks-jump-on-us-futures-rally-china-profit-beat-shrugging-off-tariff-risks?utm_source=feed_news_all&utm_medium=referral&feed_item_type=news)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  Asian equity markets traded higher on Friday, buoyed by a strong rally in U.S. stock futures ahead of Wall Street's shortened post-Thanksgiving session.
- [iShares MSCI South Korea ETF (EWY) Price Prediction: Bounce attempt runs into heavy overhead supply](https://www.google.com/goto?url=CAESngEBxCJF1-wfyuLSKIPok26XxgDJxUT0BhZGAohOY8_HgZL4SLwVKA752dM0melLNQSUeJu89WGnz1dlP-Sg2nbsFnoY9-kkhkY89wnhNwypqAdlD44b-G8EanQ18Uouyg2qKTpRA3bxrwokbTMKZYGqhHRjsH8rxmarwsTPO864X4IZ8A_wkWDlW-Ci5FIGGH-uRuqnjav_OF-Vbz0bfg&gsessionid=wZ0KJLJVCXtKbxaAtoAg_VgbbdZz_ul4BtcDHZkrLQVsxVTOQf9fow)  
  <sub>Blockchain News, 7 hours ago</sub>  
  iShares MSCI South Korea ETF (EWY) is trading at $134.23, up 3.00% on the latest session snapshot, but it remains below the 20-day, 50-day and 200-day...
- [Tokenized EWY Rises 3% but Stays Below Key Moving Averages](https://www.google.com/goto?url=CAESagHEIkXXHOZliYkwG0RUZUOEm3FGOlbOoNdqS2f9XfOVc5S_xxaEa4tHWZkclz03J3vQ9oIsfCseATbu1axzbsZpgTAvWVJU59CUD5wlcxcuMxrGtFIFcHoFOHHqxdn1FY-EUeMZGcWPrbA&gsessionid=wZ0KJLJVCXtKbxaAtoAg_VgbbdZz_ul4BtcDHZkrLQVsxVTOQf9fow)  
  <sub>www.tokenpost.com, 7 hours ago</sub>  
  The tokenized iShares MSCI South Korea ETF market, represented by EWYUSDT, rose 3% to $134.23 in a Nov. 27 snapshot as it attempted to stabilize while...
- [Direxion South Korea Bull 3X ETF (KORU) Price Prediction: Rebound attempt faces a still-heavy trend map](https://www.google.com/goto?url=CAESmwEBxCJF1yYkeGVFxTNqETrZlMvZU0eemOkCUcUKjIIIgR4gIH8eHygtzEe0jC7YTXAsLgl1XedgDbJom2jsh-A9euZ97CFbtX1cCStQ9IKU0Kmt1bxDW9slRfRxvvjiduxVVlmXabyHP2Mps8CTORDctRaUAbnt1Y1p4PW14q1bGdCaKFTI3PEmG9Z0Rgsci17iaUaJ6xQ-Mo-myA&gsessionid=wZ0KJLJVCXtKbxaAtoAg_VgbbdZz_ul4BtcDHZkrLQVsxVTOQf9fow)  
  <sub>Blockchain News, 7 hours ago</sub>  
  Direxion South Korea Bull 3X ETF (KORU) is trading at $5.86 after an 8.44% 24-hour gain, but the ETF remains below key short- and medium-term moving...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 132.91 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 139.63 (-4.8%), 50d 159.33 (-16.6%), 200d 164.42 (-19.2%); 50d below 200d
Momentum: RSI(14) 41.9 | MACD -7.826 vs signal -7.969 (histogram 0.143)
Returns: 1d +2.9% | 5d -1.2% | 1m -19.9% | 3m -26.2%
52-week range: 88.58 - 219.20 (now 33.9% of the way up)
Volatility: ATR(14) 7.65 (5.8% of price) | annualised 20d 81.9%
Volume: 0.21x the 20-day average
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
Three-year record: +30.6% a year | beta to the market 2.62
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
Share count change: 1 week: +1.7% (383.12M) over 7d | 1 month: +2.2% (485.29M) over 34d
Shares outstanding: 169.27M | fund size: 22.50B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Skydance Stock Outlook: Is Wall Street Bullish or Bearish?](https://finance.yahoo.com/markets/stocks/articles/skydance-stock-outlook-wall-street-155927311.html)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  With a market cap of $31.3 billion, Skydance Corporation (SKYD) is a global media and entertainment company operating across three business segments:...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 106.71 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 104.81 (+1.8%), 50d 107.94 (-1.1%), 200d 111.78 (-4.5%); 50d below 200d
Momentum: RSI(14) 52.4 | MACD -0.718 vs signal -0.946 (histogram 0.228)
Returns: 1d +1.3% | 5d +3.8% | 1m +3.5% | 3m -5.6%
52-week range: 99.90 - 120.08 (now 33.7% of the way up)
Volatility: ATR(14) 2.51 (2.4% of price) | annualised 20d 27.8%
Volume: 0.06x the 20-day average
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
Three-year record: +15.4% a year | beta to the market 0.93
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
Ratings by weight: buy 90.6% | hold 9.4% | sell 0.0% (mean 1.54 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +32.6% above the current prices
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
Share count change: 1 week: +0.8% (177.02M) over 7d | 1 month: -3.8% (-859.77M) over 30d
Shares outstanding: 205.41M | fund size: 21.92B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Natural gas (UNG) · Commodity — BEARISH, confidence 0.45

**Result:** ACCEPTED · 401 shares · submitted sell 401 UNG @ ~9.82, stop 10.73

**In the model's own words:**

> Fund is bearish due to heavy negative roll cost, high inventory build, EIA price outlook indicating further decline, a net short position among large speculators and a technical downtrend.

**Main reasons it gave:**
- Cost of holding -8.5% annual roll cost (heavy)
- US natural gas inventories built 20 BCF to 3,882 BCF (96th percentile)
- EIA price outlook forecast decline to $2.37 in 6 months (~11% drop)
- Large speculators net short 13% OI, short crowding at 5th percentile, weekly increase +0.7% OI
- Technical downtrend: price below 20d, 50d, 200d SMAs; RSI 46.8; low volume

<details><summary><b>News</b> — score +0.00</summary>

- [UNG Nov 2026 10.000 put (UNG261125P00010000) interactive stock chart](https://uk.finance.yahoo.com/quote/UNG261125P00010000/chart/)  
  <sub>Yahoo Finance UK, 7 hours ago</sub>  
  Interactive chart for UNG Nov 2026 10.000 put (UNG261125P00010000) – analyse all of the data with a huge range of indicators.
- [UNG Nov 2026 10.000 put (UNG261125P00010000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/UNG261125P00010000/chart/)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Interactive Chart for UNG Nov 2026 10.000 put (UNG261125P00010000), analyze all the data with a huge range of indicators.
- [UNG Nov 2026 17.000 put (UNG261127P00017000) Seasonal Returns Chart - Yahoo Finance](https://www.google.com/goto?url=CAESfgHEIkXXNxow7UmtvrhBb4qhHL5btb0S80irMXHkC0JlwdxjG27GgQuwYBeogTTXECqN5fJPaFHj-hgKHBV_e9JcWi7kp5Jk1b2KajYErq0m52RE0BoTvdPx7T8u4XB5S2iEWrg7TBfRWsCtnDPO3MSM989kI0TlIHcERjFJwA&gsessionid=PkOPp0AFpUoE3xeIaRGPFBChQPygw4x8sX0fEK77md28LXgRMlDNCQ)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  UNG Nov 2026 17.000 put (UNG261127P00017000) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 9.83 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 9.90 (-0.7%), 50d 10.26 (-4.2%), 200d 10.88 (-9.6%); 50d below 200d
Momentum: RSI(14) 46.8 | MACD 0.029 vs signal 0.001 (histogram 0.027)
Returns: 1d -4.6% | 5d -4.2% | 1m +3.5% | 3m -4.8%
52-week range: 9.00 - 16.90 (now 10.5% of the way up)
Volatility: ATR(14) 0.45 (4.6% of price) | annualised 20d 57.4%
Volume: 0.13x the 20-day average
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
Cost of holding this fund instead of natural gas itself: -8.5% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -4.8%, commodity +21.9%, gap -26.7% | 6 months: fund -17.6%, commodity +7.0%, gap -24.6% | 12 months: fund -28.9%, commodity -20.4%, gap -8.5%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.60</summary>

```text
US inventories, week ending 2026-11-13 (published the following Wednesday)
  Natural gas: 3,882.0 billion cubic feet, +20.0 on the week (a build), 96% percentile over 52 weeks -- high for the time of year
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.15</summary>

```text
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 13.0% of open interest (1,630,218 contracts)
Change on the week: +0.7% of open interest
Crowding: 5% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -1.7% (-8.11M) over 7d | 1 month: +6.9% (30.93M) over 34d
Shares outstanding: 49.01M | fund size: 481.79M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> With no macro surprise, mixed technical signals, a heavy negative roll cost, and only a slight bearish tilt in positioning despite strong inflows, the overall outlook for CANE remains neutral.

**Main reasons it gave:**
- Macro data on yields, inflation and unemployment in line with expectations, no surprise
- Technicals: price 2.9% above 20‑day SMA but 1.5% below 50‑day SMA; RSI 53.8, MACD histogram modestly positive
- Cost of holding fund vs sugar is -8.3% per year, a heavy drag on long positions
- CFTC positioning: net long 16.3% of open interest, down 0.7% week‑over‑week
- Fund flows: share count rose 25.9% over the past month, indicating strong inflows

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 11.30 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 10.98 (+2.9%), 50d 11.48 (-1.5%), 200d 10.37 (+9.0%); 50d above 200d
Momentum: RSI(14) 53.8 | MACD -0.200 vs signal -0.243 (histogram 0.043)
Returns: 1d +2.1% | 5d +9.5% | 1m -3.0% | 3m +0.8%
52-week range: 9.02 - 12.47 (now 66.1% of the way up)
Volatility: ATR(14) 0.24 (2.1% of price) | annualised 20d 32.9%
Volume: 0.30x the 20-day average
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
Measured: 3 months: fund +0.8%, commodity +7.0%, gap -6.2% | 6 months: fund +18.2%, commodity +33.6%, gap -15.4% | 12 months: fund +17.7%, commodity +26.0%, gap -8.3%
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
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 16.3% of open interest (1,144,499 contracts)
Change on the week: -0.7% of open interest
Crowding: 82% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +2.6% (1.56M) over 7d | 1 month: +25.9% (12.84M) over 30d
Shares outstanding: 5.52M | fund size: 62.34M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected) (Bing's feed, direct: 4 headline(s), none naming CANE)

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Macro data in line with expectations: inflation 3.7% and unemployment 4.1%
- Technicals: price below 50‑day and 200‑day SMA, RSI 50, no decisive break on volume
- Positioning: net short 1.7% of open interest, weekly change -0.6%, crowding 30th percentile (normal)
- Cost of holding: -6.6% annual cost versus spot, heavy but not directional

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 17.43 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 17.19 (+1.4%), 50d 18.09 (-3.6%), 200d 18.16 (-4.0%); 50d below 200d
Momentum: RSI(14) 50.0 | MACD -0.234 vs signal -0.313 (histogram 0.080)
Returns: 1d +1.2% | 5d +2.1% | 1m +0.1% | 3m -12.6%
52-week range: 16.47 - 20.29 (now 25.1% of the way up)
Volatility: ATR(14) 0.25 (1.4% of price) | annualised 20d 16.1%
Volume: 0.55x the 20-day average
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
Cost of holding this fund instead of corn itself: -6.6% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -12.6%, commodity -12.8%, gap +0.2% | 6 months: fund -2.8%, commodity -0.1%, gap -2.7% | 12 months: fund -1.2%, commodity +5.4%, gap -6.6%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

```text
Corn rated good or excellent: 56% of the US crop (week 43 of 2026)
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
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 1.7% of open interest (1,954,229 contracts)
Change on the week: -0.6% of open interest
Crowding: 30% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +1.4% (1.49M) over 7d | 1 month: -14.6% (-18.71M) over 30d
Shares outstanding: 6.29M | fund size: 109.68M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected) (Bing's feed, direct: 4 headline(s), none naming CORN)

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise or decisive technical break; mixed signals from heavy roll cost (bearish), strong fund inflows (bullish), and crowded short positioning (bearish). Overall call remains neutral.

**Main reasons it gave:**
- Heavy cost of holding -5.4% annual (tailwind for short)
- Fund inflows +12.6% over 1 month (bullish demand)
- Positioning net long 9.1% OI, -2.1% change (crowded short)
- Macro: yields and inflation stable, no surprise
- News: copper price rebound noted, indicating improved risk appetite

<details><summary><b>News</b> — score +0.00</summary>

- [Commodities: Copper And Gold Rebound While Oil Extends Gains](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b099c858f5e4c2e964f19e4737dfd83&url=https%3a%2f%2fseekingalpha.com%2farticle%2f4972486-commodities-copper-gold-rebound-oil-extends-gains&c=4924072131001382302&mkt=en-us)  
  <sub>Seeking Alpha, 13h ago</sub>  
  Copper and gold continued to recover on Friday as risk appetite improved, while oil extended its advance amid renewed concerns over Middle East supply disruptions.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 33.17 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 36.15 (-8.2%), 50d 38.41 (-13.6%), 200d 37.86 (-12.4%); 50d above 200d
Momentum: RSI(14) 30.5 | MACD -1.695 vs signal -1.343 (histogram -0.353)
Returns: 1d +2.0% | 5d -1.7% | 1m -17.7% | 3m -16.4%
52-week range: 31.84 - 41.43 (now 13.9% of the way up)
Volatility: ATR(14) 0.92 (2.8% of price) | annualised 20d 32.7%
Volume: 0.14x the 20-day average
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
Cost of holding this fund instead of copper itself: -5.4% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -16.4%, commodity -14.8%, gap -1.6% | 6 months: fund -14.6%, commodity -12.1%, gap -2.5% | 12 months: fund +6.4%, commodity +11.8%, gap -5.4%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

```text
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 9.1% of open interest (314,991 contracts)
Change on the week: -2.1% of open interest
Crowding: 2% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +11.6% (70.52M) over 7d | 1 month: +12.6% (76.45M) over 30d
Shares outstanding: 20.53M | fund size: 681.03M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Positioning: net long 25.2% of open interest, down 2.5% week‑over‑week
- Cost of holding: -1.0% annual drag, recent gap -0.1% to -1.0% over 6‑12 months
- Technicals: price below 20‑, 50‑ and 200‑day SMAs, RSI 36.3, MACD negative
- Macro: no rate or policy surprise; yields stable, VIX down but still elevated

<details><summary><b>News</b> — score +0.00</summary>

- [GLD Nov 2026 325.000 put (GLD261130P00325000) interactive stock chart](https://uk.finance.yahoo.com/quote/GLD261130P00325000/chart/)  
  <sub>Yahoo Finance UK, 7 hours ago</sub>  
  Interactive chart for GLD Nov 2026 325.000 put (GLD261130P00325000) – analyse all of the data with a huge range of indicators.
- [KGLD Pays, While I Wait For Gold And The Leading Signals Of Its Comeback (BATS:KGLD)](https://seekingalpha.com/article/4972482-kgld-pays-while-i-wait-for-gold-and-the-leading-signals-of-its-comeback?source=feed_sector_etf_portfolio_strategy)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Kurv Gold Enhanced Income ETF keeps investors exposed to gold while generating monthly income through T-Bills and a limited covered call strategy.
- [Crypto Stocks Gain After Bitcoin Tops $61K In Tech Rebound, But Analysts Want A Move Above $62K](https://www.google.com/goto?url=CAES1gEBxCJF1yyQPAibNXjejFOjxUlof9XDSDJCVsUZTElSemy6g8yVc3Iqxncf9vOtN_woFv5wvC_yIGhpWLHMl7sNrS5IcGnn_qfLYHVU_szV23fggqxvRi-m_k4bCiZUWia_A0zn_CX1eBhSCNEf7BSedZAHJhQLNBtq7lD3ZCH6aDp2ytzq7mcmX8Awu1Ryq4I9X-pG33WfU3SxWjr8EzJkv8_TJOYYu8xQyNcEF3AIWwD7WbTgl_6EXRHbdj-ap4-qm8Xi8WfHit0F7H8aRCtvloHjseBI&gsessionid=FO5UAby2gTggA_LtVPM5t0tbDMkqGO3SCNDEMIZGrDmd1ehzuBUBCQ)  
  <sub>TradingView, 3 hours ago</sub>  
  Large-cap crypto-linked stocks rose in early-morning trade on Friday as Bitcoin (BTC) climbed above $61000, alongside a rebound in tech futures.
- [GLD NTA 26-11-2026 $3.45579](https://www.google.com/goto?url=CAESggEBxCJF1x2hge2Y4NYUkIZ2pPY7Hcw9p3Q0mWuMHkMkPfMYQaxGhyBdmpXrAJyVIJL-NvSvj8INzReVF_oGrZQQNKEXdbCBl_SG3dlxRudsxpRAOFCo4vbPxuyjNm6tpkC71OGG-pIJTsuv8-jkaqlHwCYGSHeHd-HHF0Fr8WmrGa2U&gsessionid=FO5UAby2gTggA_LtVPM5t0tbDMkqGO3SCNDEMIZGrDmd1ehzuBUBCQ)  
  <sub>BusinessDesk, 17 hours ago</sub>  
  View the full NZX announcement for Smart Gold ETF (GLD): GLD NTA 26-11-2026 $3.45579. Financial updates and company disclosures on BusinessDesk.
- [GLD Dec 2026 336.000 call (GLD261202C00336000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScgHEIkXX19Ent-P2LPT8TMe3uhOlqEdf09fom-epMpnxxfzCIKL5pB3DmBDVdvu1BvZxqq0ZEFqgdC1L1ceaLmcgmt38eWOKgXTLDmaQOs0piMPbKJL5mz0-8kS2CgeLZioEJljBrcSH_1JPVr-NGYB4nQ&gsessionid=FO5UAby2gTggA_LtVPM5t0tbDMkqGO3SCNDEMIZGrDmd1ehzuBUBCQ)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  Find the latest GLD Dec 2026 336.000 call (GLD261202C00336000) stock quote, history, news and other vital information to help you with your stock trading...
- [Here Are the Only ETFs Jaspreet Singh Would Hold for the Next 20 Years](https://www.google.com/goto?url=CAEShQEBxCJF1_eU-IloC9LDZMX_AUdIfSLraUAM2EreCii1e0PjO4iqvMI0wCzx1QOJjrh7hhO7uOs7xjY5xB05mgkdvnU4JaHlMh4Vkte5iR5tSzz6_uQFK-lmEL4fEXMzDcbTuPlNGmbXwDiUhjZdWoMxzYXhtM_LRDAjzoYHlmKKCAFL8aDT&gsessionid=FO5UAby2gTggA_LtVPM5t0tbDMkqGO3SCNDEMIZGrDmd1ehzuBUBCQ)  
  <sub>AOL.com, 23 hours ago</sub>  
  Which ETFs are built for the long haul? Jaspreet Singh shares the funds he'd consider holding for 20 years and what makes them stand out.
- [GLD Dec 2026 255.000 put (GLD261207P00255000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScgHEIkXXoXhgAi8CewVK2hDL2AxrZ4mwNxQXCRHGT4ySFgRKX55Ntd-L1z2YfU6vIKRxRizsC_7KAJiBE1ysB6vl3UZw3_iTLI-Un_Me62ElbviRD_GuvGXcHmdt2sdttdDBMTxf7cKGJARBpiOVhQnx5A&gsessionid=FO5UAby2gTggA_LtVPM5t0tbDMkqGO3SCNDEMIZGrDmd1ehzuBUBCQ)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Find the latest GLD Dec 2026 255.000 put (GLD261207P00255000) stock quote, history, news and other vital information to help you with your stock trading and...
- [GLD Dec 2026 520.000 call (GLD261202C00520000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScgHEIkXXAO8cPCAsyWL2yJciQGA_MPg8Zbh_lg8L5X4APrTx6in8kS87L2k8L7ceyCttx4ms2TarI76PprANXuC28QS8ojvlAd39DrGTDbMJjj0Gq6Jwxy8XifAme-zrrX9dLv-2XIa3X-ViIxoIixce7w&gsessionid=FO5UAby2gTggA_LtVPM5t0tbDMkqGO3SCNDEMIZGrDmd1ehzuBUBCQ)  
  <sub>Yahoo! Finance Canada, 24 hours ago</sub>  
  Find the latest GLD Dec 2026 520.000 call (GLD261202C00520000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 332.87 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 352.25 (-5.5%), 50d 369.73 (-10.0%), 200d 403.16 (-17.4%); 50d below 200d
Momentum: RSI(14) 36.3 | MACD -12.548 vs signal -10.282 (histogram -2.266)
Returns: 1d +1.7% | 5d -0.7% | 1m -10.9% | 3m -18.6%
52-week range: 322.87 - 495.90 (now 5.8% of the way up)
Volatility: ATR(14) 8.32 (2.5% of price) | annualised 20d 34.7%
Volume: 0.22x the 20-day average
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
Cost of holding this fund instead of gold itself: -1.0% a year -- a steady drag
Measured: 3 months: fund -18.6%, commodity -19.0%, gap +0.4% | 6 months: fund -20.2%, commodity -20.1%, gap -0.1% | 12 months: fund -12.4%, commodity -11.4%, gap -1.0%
A commodity fund holds futures, not gold, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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
Contract: GOLD - COMMODITY EXCHANGE INC. (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 25.2% of open interest (407,834 contracts)
Change on the week: -2.5% of open interest
Crowding: 30% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 260.30M | fund size: 86.65B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: Treasury yields and inflation data in line with expectations
- Technicals show downtrend (price below 20‑day, 50‑day, 200‑day SMA) with low volume and no decisive break
- Positioning: net long only 1% and decreased by 2.1% week‑over‑week, indicating modest bearish sentiment
- Cost of holding: -2.4% annual drag, tempering bullish conviction

<details><summary><b>News</b> — score +0.00</summary>

- [The Silver Dip Has a Receipt](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b099c7a99174467b0d895831382ca44&url=https%3a%2f%2fwww.ainvest.com%2fnews%2fsilver-dip-receipt-2611%2f&c=815220364624931171&mkt=en-us)  
  <sub>ainvest, 25h ago</sub>  
  Silver fell to $38.66/oz in Nov 2026, its lowest since 2025 and 66% below its Jan 2026 record high of $121.64.
- [Beijing calls in the 'national team,' silver answers: 10 metal stocks to watch Friday](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b099c7a99174467b0d895831382ca44&url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2ftop-stocks%2fbeijing-calls-in-the-national-team-silver-answers-10-metal-stocks-to-watch-friday%2far-AA2imLtf&c=755748671367159109&mkt=en-us)  
  <sub>Benzinga on MSN, 10h ago</sub>  
  Washington is squeezing China on chips and trade at the same time. On Friday, Beijing answered with the one weapon it fully controls: its own balance sheet. In Congress, the bipartisan MATCH Act would ...
- [Silver: Aggressively Buying Into Capitulation](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b099c7a99174467b0d895831382ca44&url=https%3a%2f%2fseekingalpha.com%2farticle%2f4972499-silver-aggressively-buying-into-capitulation&c=7463619110324913856&mkt=en-us)  
  <sub>Seeking Alpha, 11h ago</sub>  
  After reaching an all-time high of $121.67 at the end of January 2026, silver prices have collapsed by almost 70% in less than a year. I have never been so bullish on silver.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 39.29 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 43.05 (-8.7%), 50d 49.44 (-20.5%), 200d 60.36 (-34.9%); 50d below 200d
Momentum: RSI(14) 35.8 | MACD -3.378 vs signal -3.057 (histogram -0.322)
Returns: 1d +5.9% | 5d -0.9% | 1m -19.9% | 3m -34.5%
52-week range: 36.84 - 105.60 (now 3.6% of the way up)
Volatility: ATR(14) 1.90 (4.8% of price) | annualised 20d 59.5%
Volume: 0.42x the 20-day average
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
Cost of holding this fund instead of silver itself: -2.4% a year -- a steady drag
Measured: 3 months: fund -34.5%, commodity -34.2%, gap -0.4% | 6 months: fund -42.5%, commodity -41.7%, gap -0.8% | 12 months: fund -15.8%, commodity -13.4%, gap -2.4%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 1.0% of open interest (122,945 contracts)
Change on the week: -2.1% of open interest
Crowding: 2% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +12.3% (2.83B) over 7d | 1 month: +14.0% (3.17B) over 34d
Shares outstanding: 657.33M | fund size: 25.83B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Positioning: net long 11.4% of OI, down -0.7% week
- Fund flows: -10.8% share count over 30 days (outflows)
- Technicals: price above 20‑day SMA (+2.8%) and MACD above signal (bullish momentum)
- Cost of holding: low at 0.6% annual, near zero

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 26.48 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 25.75 (+2.8%), 50d 26.62 (-0.5%), 200d 25.42 (+4.2%); 50d above 200d
Momentum: RSI(14) 58.5 | MACD -0.138 vs signal -0.258 (histogram 0.120)
Returns: 1d +1.9% | 5d +4.1% | 1m +1.6% | 3m -2.6%
52-week range: 21.71 - 28.14 (now 74.2% of the way up)
Volatility: ATR(14) 0.31 (1.2% of price) | annualised 20d 16.3%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.10</summary>

```text
Cost of holding this fund instead of soybeans itself: 0.6% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund -2.6%, commodity -0.6%, gap -2.0% | 6 months: fund +5.3%, commodity +6.9%, gap -1.6% | 12 months: fund +13.4%, commodity +12.8%, gap +0.6%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.10</summary>

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
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 11.4% of open interest (997,948 contracts)
Change on the week: -0.7% of open interest
Crowding: 28% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -0.2% (-89.69K) over 7d | 1 month: -10.8% (-4.86M) over 30d
Shares outstanding: 1.51M | fund size: 40.06M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, modest net short with slight bullish shift, heavy roll cost offset by weaker crop condition, price below key SMAs with low momentum and no decisive break.

**Main reasons it gave:**
- Macro: yields stable, Fed target unchanged, inflation 3.7% within expectations – no surprise
- CFTC: net short 15.2% of OI, change -0.6% (small decrease) – modest bearish sentiment, slight bullish shift
- Cost of holding -6.7% y/y heavy roll cost – tailwind for short positions
- US wheat crop condition 48% good/excellent, down 7 points YoY – bullish supply outlook
- Technical: price below 20d, 50d, 200d SMAs, RSI 36.7, low volume – weak momentum, no decisive break

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 21.37 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 21.71 (-1.6%), 50d 23.29 (-8.3%), 200d 23.64 (-9.6%); 50d below 200d
Momentum: RSI(14) 36.7 | MACD -0.530 vs signal -0.600 (histogram 0.071)
Returns: 1d +0.3% | 5d -0.5% | 1m -3.4% | 3m -23.7%
52-week range: 19.88 - 28.00 (now 18.3% of the way up)
Volatility: ATR(14) 0.40 (1.8% of price) | annualised 20d 22.1%
Volume: 0.17x the 20-day average
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
Cost of holding this fund instead of wheat itself: -6.7% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -23.7%, commodity -25.1%, gap +1.4% | 6 months: fund -8.6%, commodity -5.9%, gap -2.7% | 12 months: fund +2.3%, commodity +9.0%, gap -6.7%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 15.2% of open interest (558,414 contracts)
Change on the week: -0.6% of open interest
Crowding: 30% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +2.8% (6.36M) over 7d | 1 month: -11.9% (-31.77M) over 30d
Shares outstanding: 10.98M | fund size: 234.64M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected) (Bing's feed, direct: 6 headline(s), none naming WEAT)

### Oil (USO) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [KSA: All You Need To Know About The Oldest Saudi-Focused ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b099c8a3cc34f13949059460742fc59&url=https%3a%2f%2fseekingalpha.com%2farticle%2f4972535-ksa-all-you-need-to-know-about-the-oldest-saudi-focused-etf&c=3892982980638720279&mkt=en-us)  
  <sub>Seeking Alpha, 10h ago</sub>  
  KSA as a low-beta, value-oriented Saudi ETF that's still largely dependent on the oil economy, with heavy concentration in financials and higher than average tracking error.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.16% (+0.01 on the week) | 5-year 4.70% (-0.17 on the week) | 10-year 4.89% (-0.16 on the week) | 30-year 5.28% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.73 points -- upward sloping (normal)
US dollar index: 103.91 (+0.01 on the week)
Volatility (VIX): 26.28 (-9.6 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 189k (2026-11-21)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.63% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 139.20 (bar of 2026-11-27), from 501 daily bars
Trend: vs 20d SMA 144.26 (-3.5%), 50d 150.03 (-7.2%), 200d 130.37 (+6.8%); 50d above 200d
Momentum: RSI(14) 42.6 | MACD -4.437 vs signal -3.927 (histogram -0.510)
Returns: 1d -0.5% | 5d +0.8% | 1m -16.4% | 3m +7.3%
52-week range: 66.17 - 169.53 (now 70.7% of the way up)
Volatility: ATR(14) 4.83 (3.5% of price) | annualised 20d 50.3%
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

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

```text
US inventories, week ending 2026-11-13 (published the following Wednesday)
  Crude oil: 417.8 million barrels, +3.4 on the week (a build), 25% percentile over 52 weeks
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
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 0.8% of open interest (1,869,789 contracts)
Change on the week: -0.5% of open interest
Crowding: 25% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +3.1% (59.80M) over 7d | 1 month: +34.0% (504.23M) over 34d
Shares outstanding: 14.26M | fund size: 1.99B
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

