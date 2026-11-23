# Daily report

**23 Nov 2026, 17:40 Israel time (15:40 UTC)** · 80 names checked · 3 traded · 0 with a problem

**Answers with no explanation:** 7 of 70 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 7 | 9 | 0 |
| Whole-market funds | 14 | 0 | 14 | 0 |
| Sector and country funds | 41 | 0 | 41 | 0 |
| Commodities | 9 | 0 | 9 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| Brazil (EWZ) · Sector or country | **Stop raised.** At +1.21R, following the price. Stop-loss raised 31.36 → 31.27. |
| JPMorgan Chase (JPM) · Company | **Stop raised.** At +0.73R, following the price. Stop-loss raised 335.02 → 331.98. |
| Elbit Systems (ESLT) · Company | **Holding.** -0.66R, holding 7 shares. Stop-loss 640.17. |
| South Korea (EWY) · Sector or country | **Holding.** +0.06R, holding 51 shares. Stop-loss 143.75. |
| HDFC Bank (HDB) · Company | **Holding.** +3.31R, holding 51 shares. Stop-loss 26.52. |
| Eli Lilly (LLY) · Company | **Holding.** -0.41R, holding 3 shares. Stop-loss 1304.66. |
| MercadoLibre (MELI) · Company | **Holding.** +0.63R, holding 3 shares. Stop-loss 1505.92. |
| Procter & Gamble (PG) · Company | **Holding.** +1.08R, holding 2 shares. Stop-loss 165.90. |
| Toyota (TM) · Company | **Holding.** -0.42R, holding 1 shares. Stop-loss 205.44. |
| Exxon Mobil (XOM) · Company | **Holding.** -0.41R, holding 30 shares. Stop-loss 153.50. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Nvidia (NVDA) · Company — BULLISH, confidence 0.82

**Result:** ACCEPTED · 1 shares · submitted buy 1 NVDA @ ~168.77, stop 142.32

**In the model's own words:**

> Strong, material catalyst (CEO reinstatement) combined with robust fundamentals and a flawless earnings beat record outweighs bearish technicals and neutral insider activity.

**Main reasons it gave:**
- Jensen Huang reinstated as President & CEO (board announcement)
- Forward P/E 9.54 and profit margin 62.5% indicate cheap, high-quality business
- Four consecutive earnings beats
- Analyst consensus remains strong buy with mean price target +54% vs last close

<details><summary><b>News</b> — score +0.90</summary>

- [Nvidia stock jumps as DC makes stunning u-turn on Jensen Huang](https://finance.yahoo.com/markets/stocks/article/nvidia-stock-jumps-as-dc-makes-stunning-u-turn-on-jensen-huang-113419437.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  A not-so-subtle shift in tone in the Jensen Huang saga has sent Nvidia's (NVDA) stock reeling this month.
- [Nvidia Stock Soars as Jensen Huang Returns as CEO](https://www.benzinga.com/trading-ideas/movers/26/11/63526761/nvidia-stock-soars-as-jensen-huang-returns-as-ceo)  
  <sub>Benzinga, 27 minutes ago</sub>  
  Nvidia Corp. (NASDAQ:NVDA) shares jumped almost 29% in premarket trading on Monday after the chipmaker said Jensen Huang has returned as president and CEO,...
- [Nvidia Stock Jumped on Trump's Call to Rehire Jensen Huang. Don't Bet on It Happening.](https://www.google.com/goto?url=CAESvAEBxCJF13xcUfGCAqll4nZFx2Tgu_S5CGYgdgq2JhEFLjvg8II4Xk74enTFbL5bu5devZVI4G47nrmCXi7CwZyhYnR7pbf7YiXmXqAryhiv3pcUfsF8omv7nG0trDQEMYTxgn71SvPjW3hfzG3JMA_fz7S6JYoMYdi0YPKcx25YalTI5iWGAhc3VryfwHGRYfU78YvP0mmR0JSrWYrTp2TgLyCQ-3ni8yt45U4cIsFPZjtJQxaAN8jQzD895A&gsessionid=oWb1mniNEwr2ogvsoAXu5TDNTgp0EaeCW80dtG0-563LfidauBE39w)  
  <sub>The Motley Fool, 34 minutes ago</sub>  
  President Donald Trump wants Jensen Huang back at Nvidia (NVDA -14.01%), and investors apparently like the idea. Nvidia stock jumped 8% in premarket trading...
- [Hedge Fund Says the Stock Market Knows Your Weakest Moment — and Uses It Against You](https://www.google.com/goto?url=CAESuwEBxCJF14S8S10TMicVG8bDFi3zZt42cp_1ZgEta2goNqy1mWA0ri6xk2c_Bufv59MWE3UEfiPx_iPRyyBSopxRnmnQkqivaoIFli8blx3DKIUOmnkz44IUcohzienwBb-6cjbPsRYU4J-IJlaePu8zUmN7EmTSSq1NjvFQ_4WCXT5mLWsAmMiMqGe2neeYFyF_A55kgVwl_s6XWDd4KDwR9HtOSjeoYzSZ2BOxX0yUBqFJRJB4z205PwCO&gsessionid=oWb1mniNEwr2ogvsoAXu5TDNTgp0EaeCW80dtG0-563LfidauBE39w)  
  <sub>24/7 Wall St., 1 hour ago</sub>  
  NVIDIA (NVDA) beat revenue estimates with $116B, yet the stock still fell 17% in a week, a drop that illustrates Eric Peters' warning about humiliating...
- [NVDA: NVIDIA Corporation filed SEC Form 8-K: Leadership Update, Financial Statements and Exhibits](https://www.google.com/goto?url=CAEStAEBxCJF14A5dmzRechJE4QAaWz09kLscUJIXmCKKSP9J0NfKcDteFUxmPHxI9qGRDiT8M2Du8keSRZu1ZmT5wVGfO9I97P44nwsjIPfWPEPVSPsZExPSTS8blcpUMVkSJODFCajbBOWm6PbtOxfqqz7oNfQlrf5b76MPBzfqvZ9HL-DVnnL5hNyGHFyE5GSZPR0VJb7r6RnyulrAY_-9R3Zz9Q8cu389Hy3NR8zfQviBn8HuaQ&gsessionid=oWb1mniNEwr2ogvsoAXu5TDNTgp0EaeCW80dtG0-563LfidauBE39w)  
  <sub>Quantisnow, 40 minutes ago</sub>  
  SANTA CLARA, Calif.—November 23, 2026—NVIDIA (NASDAQ: NVDA) today announced that effective immediately, Jensen Huang has been reinstated as President and...
- [Nvidia Stock Surges as Trump Urges Board to Rehire Huang. Is the Selling Finally Over?](https://www.google.com/goto?url=CAESjAEBxCJF1-bIa4Xdc6B9n84QAyGZWCvWZ_PPevn5n0jW2x7PTTY0hKdk8YMWQ3YJwiihnZ0mXq-8KKisXkw4lMe-P6C47h79qIYLdNHGIemraKcxuPuJZ33RHILMCxlWAICnQnVKkGzAHybQqftZa-6nwrmojXVx06iecigzDU_Aj_Cpc9JQNHaLMXrn0Q&gsessionid=oWb1mniNEwr2ogvsoAXu5TDNTgp0EaeCW80dtG0-563LfidauBE39w)  
  <sub>Barron's, 3 hours ago</sub>  
  Nvidia stock jumped ahead of the open Monday as the chip maker looked set to snap a seven-day losing streak after President Donald Trump called for Jensen...
- [What Sent NVIDIA Stock Lower On Friday?](https://www.google.com/goto?url=CAESoAEBxCJF1xHI0sorGvpXpJLtvFm2renY6ECvnO_qrUz9L6TDsnppuTpGa3wd6vKmeFQOJKpg57MVDkridfPj-D1pnkam7XGgfPlWaueySmAPFL7YXwuD4S0dk2IeqGGq9yqUMeDcyMWEJ5LYJ6Vu7UBXbxsodaTBSfwVH7_F6XfIXwVidxHncGtEXmevqzp_rGy30groAYSE9FWurZC52Y_A&gsessionid=oWb1mniNEwr2ogvsoAXu5TDNTgp0EaeCW80dtG0-563LfidauBE39w)  
  <sub>Trefis, 7 hours ago</sub>  
  Today's big story: Reported SEC Probe: Could Nvidia Stock Fall To $92?NVIDIA (NVDA) stock fell 14.0% on Friday, November 20, 2026, while the S&P 500 lost...
- [Nvidia shares surge 30% as board announces Jensen Huang’s reinstatement](https://www.google.com/goto?url=CAESuwEBxCJF19obx_96J2Z3kbz79Shoac1I2gQ-8MBUmNL1TxK6Eas7sJU4apmEPhl8OaO3D8Co_j8oQ-n7LxbLEfdNBD4b9m9QRQdOWmKqHIsHssPcDKUmI7w6NkUMrTMsChDC5EEY3JcyqQnEwPPoMB3cTB-XADXjhlVAVbTbcgeBym8KG6ec1mJ7TwizlP8qQk2DIrtaVqdA4dPWPMfjqt79sS-hbvtMOXZ9pgJBrckh6yl2DD1ycFjuLIle&gsessionid=oWb1mniNEwr2ogvsoAXu5TDNTgp0EaeCW80dtG0-563LfidauBE39w)  
  <sub>Investing.com, 26 minutes ago</sub>  
  Investing.com -- Nvidia's board has reinstated co-founder Jensen Huang as president and CEO, reversing his departure just 11 days ago in a dramatic...
- [Nvidia's 10-Q Is Delayed. Here's What I'm Looking for When It Lands.](https://www.google.com/goto?url=CAESqgEBxCJF16e6-iwRYbty3ckTrDPb_gxP_3592JEMp7zt959IJfHy-iK7WHPNpVXWJYcdaikuoj3MpR0JiGqix6NQhQ0q7J4yNP6quFx8FeP8xk7HlWujRjXoLh-hf5MDmkelLxHI1iN3MeFVJxLac-oyJQOixmB7bno2R99PN2FoCjhuTHzWKw0KT25W9YRmApp7kCmUi3laI5j2bIFVjIEkNWuORnVLEoVMyA&gsessionid=oWb1mniNEwr2ogvsoAXu5TDNTgp0EaeCW80dtG0-563LfidauBE39w)  
  <sub>The Motley Fool, 1 hour ago</sub>  
  Nvidia's (NVDA -14.01%) first earnings report since the sudden resignation of Jensen Huang was as solid as investors could have hoped.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 158.30 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 178.57 (-11.4%), 50d 205.95 (-23.1%), 200d 203.21 (-22.1%); 50d above 200d
Momentum: RSI(14) 39.5 | MACD -18.615 vs signal -15.887 (histogram -2.728)
Returns: 1d +26.1% | 5d +1.4% | 1m -25.0% | 3m -25.7%
52-week range: 125.53 - 239.24 (now 28.8% of the way up)
Volatility: ATR(14) 12.92 (8.2% of price) | annualised 20d 120.3%
Volume: 0.62x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.90</summary>

```text
Sector: Technology / Semiconductors | market cap 3.82T
Valuation: trailing P/E 17.01 | forward P/E 9.54 | P/B 14.32 | PEG 0.15
Profitability: profit margin 62.5% | operating margin 66.1% | ROE 117.4%
Growth (YoY): revenue +103.2% | earnings +107.7%
Balance sheet: debt/equity 14.3% | free cash flow 99.24B
Risk: beta 2.25 | short interest 1.2% of float
Next earnings: 2026-11-17
```

</details>

<details><summary><b>What this fund holds</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.90</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-12-31 beat by 6% | 2026-09-30 beat by 4% | 2026-06-30 beat by 4% | 2026-03-31 beat by 4%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: buy (mean 1.81 on a 1=strong buy to 5=strong sell scale, 56 analysts)
Ratings: 11 strong buy, 34 buy, 16 hold, 2 sell, 0 strong sell
Price target: mean 244.18 (+54.3% vs last close), range 130.00 - 425.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 2,613,243 shares in 18 transaction(s) | sold 6,198,325 shares in 9
Net: -3,585,082 shares (-0.4% of insider holdings) | insiders hold 972,918,080 shares
Distinct insiders: 0 buying, 4 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-21 TETER TIMOTHY S (General Counsel): 30,460 shares, 6.79M
  - 2026-09-18 STEVENS MARK A (Director): 1,366,000 shares, 300.15M
  - 2026-09-04 STEVENS MARK A (Director): 1,022,239 shares, 235.64M
  - 2026-09-02 STEVENS MARK A (Director): 1,848,501 shares, 410.84M
(18 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### ASML (ASML) · Company — BULLISH, confidence 0.66

**Result:** REJECTED · no room for equity ASML under its 5% cap or the sleeve budget limit: equity 99032.21, price 1404.78, existing exposure 0.00, headroom 200.54

**In the model's own words:**

> Strong demand for EUV lithography, sizable share buybacks, and a robust analyst consensus outweigh the short‑term technical weakness, suggesting a near‑term upside.

**Main reasons it gave:**
- €557m share repurchase in one week (share buyback activity)
- Bernstein upgrade to Buy rating, target unchanged (analyst view)
- Revenue up 55% YoY, profit margin 34% and ROE 65.6% (fundamentals)
- Price 6‑15% below 20d/50d/200d SMAs, RSI 40.6 (technicals)

<details><summary><b>News</b> — score +0.60</summary>

- [ASML Stock Fell 25% In The AI Selloff, But Its Outlook Hasn’t Budged (NASDAQ:ASML)](https://www.google.com/goto?url=CAESrwEBxCJF1yzymPvkNthmvSL3jIIgPTUW7YjV6mMMNTKO-SMfesOTIlCXjydHKt1qN2NVXcIyLf93GVT182vncLTmAv-q0nT1WLMuauspbI2-mxfRFYGQsZvrnif_r1izLXZvPvtV_8UmXRjVU6W0-Ie93Tj-vvFRwRIcgBo3u7tKUB6IrURYofyL5FZwCuaXh05znij4QC_nfIlKxwQy1nal12OfuXYs9CwOqevZX_fX&gsessionid=ET_MGLwkEbevcGg-UAGyHIOkbLO4U8Bi8brB3GYEeksJjb_Sh0tiVw)  
  <sub>Seeking Alpha, 15 minutes ago</sub>  
  Analyst rates ASML Holding a Strong Buy: shares fell 25% in the AI selloff, while 20x annualized earnings and demand are expected to top supply through...
- [ASML reports transactions under its current share buyback program](https://www.quantisnow.com/insight/asml-reports-transactions-under-its-current-share-buyback-program-6803372)  
  <sub>Quantisnow, 46 minutes ago</sub>  
  ASML reports transactions under its current share buyback program VELDHOVEN, the Netherlands – ASML Holding N.V..
- [ASML Vs. Taiwan Semiconductor: Here’s Why You Choose One as Your AI-Anchor Now](https://www.google.com/goto?url=CAESnQEBxCJF14qnWpcF7n0Sb8b5g-Sdnifz39k2U6g7iQDmxctW4wcIaU3uEW5Z8AzYnaBqK3IVpINYBiFq4glcuNpQHxfqk0_VbWAH_7AjxyXuLfQNXUmbYq-Qr8WE_egvNyEoDjz0hYR_-2nByyj7xTxMDHWtA02pqFb731pnbNEAJHh_f7FPJimWSaytOUSdDCRXrksjqcQRDi4BZYeH&gsessionid=ET_MGLwkEbevcGg-UAGyHIOkbLO4U8Bi8brB3GYEeksJjb_Sh0tiVw)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  TSMC beats ASML as the AI anchor because it trades at 14 times forward earnings versus 20, with Taiwan risk the main exposure. ASML holds the scarcer asset:...
- [ASML repurchases 445,000 shares over five days in November](https://www.google.com/goto?url=CAEStAEBxCJF1-mvemzYv7h1PBTX6Q9A3ijovclcoZJGuSvwqd2UJEg2CHC0AI8m2MzRoAxar7WbgBERbrT_KX3rQ6pX1ZvxYiMHMzOgz4raJjxujmt8t19I1SPjrtnNDa58ei55AzdlMBVXg-eRytKbD40oMfS2jMPWs8wDyYPyJUCthZQw9Ao8_yaOKX_6Da9wLfuB3p9LPU4aVAcQoUjkss7hlbQIL3ZY1PzhHhfFyokLeoExWTQ&gsessionid=ET_MGLwkEbevcGg-UAGyHIOkbLO4U8Bi8brB3GYEeksJjb_Sh0tiVw)  
  <sub>StreetInsider, 48 minutes ago</sub>  
  ASML Holding N.V. (NASDAQ: ASML) repurchased 445,000 of its shares between Nov. 16 and Nov. 20, 2026, under its current share buyback program, according to...
- [ASML Holding N.V. : Receives a Buy rating from Bernstein](https://www.google.com/goto?url=CAESpwEBxCJF19mxz2YV1sWa1y1wnG2tVuunvFeOz_cwdgFWYjqCPCyfOEfanzRlETOGQ5SWCX8h_cHikVyUAcvjS94russIa9qNHJYxCSbjijO3IAbL5-RXhIFESeru-h-6HCs5Bwdq4UFx-75dC-B7FU4RpueqcpNJStUiwlAMWf5l54pNBlEMPC6S4msnBrLQ-S0q8o60TdFCoYJD7LvrlU1Ie9EC-GkI0w&gsessionid=ET_MGLwkEbevcGg-UAGyHIOkbLO4U8Bi8brB3GYEeksJjb_Sh0tiVw)  
  <sub>marketscreener.com, 30 minutes ago</sub>  
  Analyst Mark Newman from Bernstein research considers the stock attractive and recommends it with a Buy rating. The target price remains unchanged at EUR...
- [ASML reports €557m share buyback transactions last week By Investing.com](https://www.google.com/goto?url=CAESsAEBxCJF1-QC9GRT003cI7d-z11dx9fyZYgSpGWfmj7wDHo78GPVYzy0q3StAkaH_i_jA0wdP_st76FEmiqcm8pARbxImlKVxUfsXtRRKzncIxidRK0Oww9cf4LGUAcMZ_ziEbUKD8wzVIw-Na6TWSaBsusLp40y_8cseON50BdhSIeHGq0HlU-mUo5DTulARrgZmlq1_0FyDE-NROKwXWLtWBc_FTRAuXDHgyZjOKezzQ&gsessionid=ET_MGLwkEbevcGg-UAGyHIOkbLO4U8Bi8brB3GYEeksJjb_Sh0tiVw)  
  <sub>Investing.com Canada, 36 minutes ago</sub>  
  VELDHOVEN, the Netherlands - ASML Holding N.V. (NASDAQ:ASML) conducted share repurchase transactions totaling €557 million during the week of November 16-20...
- [2 Semiconductor Stocks to Buy No Matter Who Wins the AI Chip Race](https://www.google.com/goto?url=CAES1gEBxCJF14Ucf2XNqr5B-tCX-eMgbWCWqk1ntX_qpS4iKLprKEbNZEuWKvPLqzhywl5BaDrSV8ePhWiZG6ge8PTM-u587c_rGuBHHmf6V-dGUzx9zKH1GcTxjCnW2QM97rtiT1gZQMj1azCr75toA5Ummz34hN7LyRQz9xHynxIF3RiXrDxO2IWo_Plj0olL00BxuAtTMRmCaLgkRrjPT3SO94z10PBiYweURsdgHXk01_qRE0LaT6PBlQwoY8M7esZB35pg8cwxvkUFDNdh4yhhrBkvjG2e&gsessionid=ET_MGLwkEbevcGg-UAGyHIOkbLO4U8Bi8brB3GYEeksJjb_Sh0tiVw)  
  <sub>The Globe and Mail, 8 hours ago</sub>  
  Lam Research is posting record results even as its stock trades about half off its high. ASML says customer demand for its chipmaking machines will outrun...
- [ASML Holding N.V. (NASDAQ: ASML): Powering the AI Semiconductor Supercycle Through EUV Leadership, Pricing Strength and Expanding Capacity](https://www.google.com/goto?url=CAES6AEBxCJF15XiVYhcge2bYKPhwWk5EU0JlNF5stkGrFaw4g4DB8Nv7Lfqnvx95pTU3KoHy7YGf8WmLBAlzkjJZIS6pLOTLOitWzMxLTzPMZZXSfPIAdmogDZ7seNIEaIVJl9Gpi-IeLaBZnDPrPTW5ryCblEbht9sLOxDucVFpW9ZasZWnmOAoWiotfj1OXbdw7bgcWn4FcgNJk9xkc9GLMS07byCHXURGd37HdSbgyi5isjZDW7EW4XiNWUJqXQAnrvGuwda4vcs6ufHH1zfaEBawlYjwVxL2saR1RljBljLMp8LVoHaXhF0&gsessionid=ET_MGLwkEbevcGg-UAGyHIOkbLO4U8Bi8brB3GYEeksJjb_Sh0tiVw)  
  <sub>Kalkine, 3 hours ago</sub>  
  ASML Holding N.V. (NASDAQ: ASML): Powering the AI Semiconductor Supercycle Through EUV Leadership, Pricing Strength and Expanding Capacity.
- [ASML Feb 2027 2080.000 call (ASML270219C02080000) stock price, news, quote and history](https://www.google.com/goto?url=CAESdAHEIkXXnJzbjTWPp9ykZyKQNcmdf7kvI_Eu8r7Elz1aIe7VHaqU5vUPJmnmZe4rVqu65l66JmNMOe-bs0aGcaRRS9Y-A-lTpa0FSmwbdiPw5l8n7dBymVBHmIzblykrJ5n5XB8UGjiBpgsC5MLzY-E8AFlQ&gsessionid=ET_MGLwkEbevcGg-UAGyHIOkbLO4U8Bi8brB3GYEeksJjb_Sh0tiVw)  
  <sub>Yahoo Finance UK, 4 hours ago</sub>  
  Find the latest ASML Feb 2027 2080.000 call (ASML270219C02080000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 1,380.16 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 1,481.58 (-6.8%), 50d 1,620.85 (-14.8%), 200d 1,601.34 (-13.8%); 50d above 200d
Momentum: RSI(14) 40.6 | MACD -79.003 vs signal -68.908 (histogram -10.094)
Returns: 1d +9.0% | 5d -1.9% | 1m -12.2% | 3m -20.9%
52-week range: 966.57 - 1,989.44 (now 40.4% of the way up)
Volatility: ATR(14) 74.32 (5.4% of price) | annualised 20d 72.9%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.80</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 531.82B
Valuation: trailing P/E 33.95 | forward P/E 21.76 | P/B 1,184.82 | PEG 0.68
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

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

```text
Consensus: strong_buy (mean 1.37 on a 1=strong buy to 5=strong sell scale, 17 analysts)
Ratings: 7 strong buy, 31 buy, 2 hold, 1 sell, 0 strong sell
Price target: mean 2,100.71 (+52.2% vs last close), range 846.34 - 2,780.18
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

### Microsoft (MSFT) · Company — BULLISH, confidence 0.60

**Result:** REJECTED · no room for equity MSFT under its 5% cap or the sleeve budget limit: equity 99032.47, price 502.96, existing exposure 0.00, headroom 200.60

**In the model's own words:** no explanation. It wrote only “Buy”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Azure revenue rose 48% YoY in Q4 results
- Maia 300 AI chip unveiled supporting AI strategy
- Price below 20‑day and 50‑day SMA with negative MACD (technical weakness)
- Strong fundamentals: profit margin 41% and revenue growth 18.8% YoY

<details><summary><b>News</b> — score +0.50</summary>

- [Is Microsoft Stock Stronger Than It Looks?](https://www.trefis.com/stock/msft/articles/627857/is-microsoft-stock-stronger-than-it-looks/2026-11-23)  
  <sub>Trefis, 6 hours ago</sub>  
  Today's big story: Reported SEC Probe: Could Nvidia Stock Fall To $92?Microsoft (MSFT) holds a pile of commercial contracts that customers have signed but...
- [Bill Gates moved $1.8 billion in stock to Melinda the same day they announced their divorce — the rest is a secret](https://finance.yahoo.com/markets/stocks/articles/bill-gates-moved-1-8-110000763.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  Dividing up what you've built together can be one of the hardest parts of a divorce.
- [Weekly Recap: Azure revenue growth and Maia 300 AI chip unveiling](https://www.google.com/goto?url=CAESuwEBxCJF16EMJZuj0aF62y5Mgxcfi1ruTXCGW4GuX0tNnOlDW3exlTs3aQSu9adkLXjns1xyeIj1WLRk2d9Ewca0m4x4qcsNi9ROAqvn8Z_0PSXCR1v6s1-GYvLqz5tuG8Rx77z-cERNCS1GGOTECMk43-NWydBQRXaYmMScMbhipFPkl1aBEz04PyZoLgQT2U59gi6XWRn-Im4CqSY99Mng665bMP95GmH472K0NWRP3FVxzJFnHYlV2T4v&gsessionid=z5ACIKYXLCpesbXOqL20SPwlH0N8ISpmVV8lXL7ddkEAlSvZOBKiOg)  
  <sub>TradingView, 4 hours ago</sub>  
  Microsoft Corporation (NASDAQ:MSFT) said Azure revenue rose 48% to $33.2 billion in its Oct. 28 results, while capital spending hit $45.2 billion and free...
- [Microsoft Unaware Ballroom Donation Meant East Wing Demolition - Microsoft (NASDAQ:MSFT)](https://www.google.com/goto?url=CAESwgEBxCJF11m8UIma7BbgTp7XHAWB69Kika6gWX4fNWyEOUdFN8OmXEuM9CejDtBJCLjdQPUp7S-4KEblpYlK0wSBC7MxuAH4_MSBdXtntkFwZZ5RRSLhAbZ3CtGrDGuIiyQd5CI_7SUr4s9fS1_NigAIJrRdl9FLy41BpR1cWPOxhW4sAXolVy_yEW3W5yVbQzRvbC5BQWYp3tFyN4-N419je-ODxFB-lzPkoFNQj1NXItdQOYByDDwcok7z_I6tLbqxCg&gsessionid=z5ACIKYXLCpesbXOqL20SPwlH0N8ISpmVV8lXL7ddkEAlSvZOBKiOg)  
  <sub>Benzinga, 5 hours ago</sub>  
  Microsoft's Brad Smith says it partners where it can but did not know its reported $10M ballroom donation meant East Wing demolition.
- [Armitage and Superform build a stock-strategy franchise on SuperformOS By Chainwire](https://www.google.com/goto?url=CAESvgEBxCJF135-tjDmwVL3YuDUkUvsoA_rrP40BmctJF3EwZ13S6A9JYaGviD5B1gEL1H8pB0iyTo6eUKNdAL6G2A2He3-xwxoG--LKz0mShKLFLkn0ttR0FL1zvMUheB-5DnOu9ILg5ZNH6ag8jKu4zCmgjgNGH-kWzPv0iEjT_UlY_w8C1Fg0xWywR73RdFKrtDAl7OGAQ2_0kTH0mBhYOvDUpaSv5vpqeNS7BMiLN5EEZ46Zvor5TkMiqtY8rSi&gsessionid=z5ACIKYXLCpesbXOqL20SPwlH0N8ISpmVV8lXL7ddkEAlSvZOBKiOg)  
  <sub>Investing.com, 2 minutes ago</sub>  
  New York City, USA, November 23rd, 2026, Chainwire. Eight existing SuperStocks strategies move under Armitage's curation, with SuperformOS providing the...
- [Trading (MSFT) With Integrated Risk Controls (MSFT:CA)](https://www.google.com/goto?url=CAESoQEBxCJF1z9nUAzGX1xrL_RMtEyvIQW24Aklst2Q0JfENP1hABh8bge6UH0ZGX1Z01twQFs5KNmcY1k5CnzS8wzcp-brOGvcFsjtDrhW7WtSkWn5Fk1pj0FeKvm58f38_qI4v-Bq62cA8RW9Cxh87zCHkrZzJfHfGgXHYqzdTmXqAVBQSCytyN3RqjxSX7owmHEVPuyiGo25sdFTV1kQFlV9Dg&gsessionid=z5ACIKYXLCpesbXOqL20SPwlH0N8ISpmVV8lXL7ddkEAlSvZOBKiOg)  
  <sub>Stock Traders Daily, 10 hours ago</sub>  
  Check the time stamp on this data. Updated Proprietary Signals for Microsoft CDR (CAD Hedged) (MSFT:CA) available here (MSFT:CA stock signals).
- [Why Did Nvidia (NASDAQ:NVDA) Sink 14.01% While Alphabet (NASDAQ:GOOGL), Microsoft (NASDAQ:MSFT) and Amazon (NASDAQ:AMZN) Draw Washington's Attention?](https://www.google.com/goto?url=CAES6QEBxCJF18ghnbdSNWDUFmFRaivM-MQtwlRZvtnwP_Lyre1HqhyVs6nyVxx4CVeW8XiasIm_ZnCxd5IXWCHU1qRY3pv4dA4JXBdmS5qGAPl1LBYfO0CtL4l6aY7UqBGIkfJ3RHvcmGbGMpzK7tIHkWMzZuXaCrPs_KRnNJjCDXMff1ppS-pIyM05XbQytULUHb7YvfhEMSugvhbYNS9qqGuQhpY8ccWiyL7cbRk2Ua7HvkZHCwhUszFXue_cnpovRlM8MJmXZpf1Og74S_gIx1ipnJve52o0CYTztlCUQ_2nKXfNNPKZQkwuhw&gsessionid=z5ACIKYXLCpesbXOqL20SPwlH0N8ISpmVV8lXL7ddkEAlSvZOBKiOg)  
  <sub>Kalkine, 9 minutes ago</sub>  
  Why Did Nvidia (NASDAQ:NVDA) Sink 14.01% While Alphabet (NASDAQ:GOOGL), Microsoft (NASDAQ:MSFT) and Amazon (NASDAQ:AMZN) Draw Washington's Attention?
- [Microsoft Remains Attractively Valued as Azure and Cloud Drive Growth](https://www.google.com/goto?url=CAESqQEBxCJF1xEU-G8hCtmNqBy3QWTPjGPVEEPakLnX04KdtF_zys3Irhip-LPS8RWpValR0XXzIilssf6FAK2A9KXgeA8g20ybQNfszdaQ72pqlCszaGFowTHEpcn0KyfDkfMhlsojX7HU-Dt_3TSiszlTG6VgG6ilI4SOaFSPC1xLIye3VWb_O1zF1XDLDK-2VjVpWUw5MKdJ2DZG6bPDkBkKYrehNWjHLs3t&gsessionid=z5ACIKYXLCpesbXOqL20SPwlH0N8ISpmVV8lXL7ddkEAlSvZOBKiOg)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Technology stocks have witnessed a sharp correction in the recent past. The Nasdaq ($NASX) traded at highs of 27,599.9 on Oct. 6.
- [MSFT (NASDAQ:MSFT) Seven-Week Low Puts Long-Term Moving Average Support to the Test](https://www.google.com/goto?url=CAESxAEBxCJF15-4Eh5hCWdETgU01SAn7mepdGYLsnuR-rUq3fRozkuftVPlXmoXtPLuxXNSInePN9rp5JBHmq0lQKOrKi44ATZH28qu8wKQZk-paoiycES5-nBCkR0fn1f7avsrbk_oazWExa1AvXwNa4of1V6O0Br8lOexddSpZJjgupu36ymaP0VpZCPNLudAr0l1p2rHuS9S51ZXPz3sUTd8iD4UHFHdbMp-Ql7GSFsGXtWxFwWne0sPmuChX2NooeZI7qal&gsessionid=z5ACIKYXLCpesbXOqL20SPwlH0N8ISpmVV8lXL7ddkEAlSvZOBKiOg)  
  <sub>Kalkine Media, 7 hours ago</sub>  
  Microsoft Corporation (NASDAQ:MSFT) Technology Microsoft Corporation (NASDAQ:MSFT) 484.52 USD -13.780 ↓ 2.765% Last Updated at: 2026-11-20T21:00:00Z shares...
- [Microsoft Stock Tests $509 as Azure Growth and AI Safety Strategy Support the Bull Case](https://www.google.com/goto?url=CAESsQEBxCJF17C40GyRtq5NYuXRz_V8dSAg1xiJNKkWEACJOkut0uAncxyvBuxJFc4k6ApgtkteumwNAccjRGszO9G0T4LFszbeejw002wqvRZu6nsdNMCW2CuwcGMdlpIKgQV07io07n39HDo0ckrYKpap-MB8mBCYawU0CcKx1f51MQMhRvIUpkfI01NHfPzRdbpHDr1Iz44rJbQnWh0WH8HELGVx-4zz1DxvvnG05vX-0gA&gsessionid=z5ACIKYXLCpesbXOqL20SPwlH0N8ISpmVV8lXL7ddkEAlSvZOBKiOg)  
  <sub>TradingKey, 22 hours ago</sub>  
  TradingKey - MSFT closed at $505.41 after a 1.97% gain as Azure growth and AI adoption remain strong. Can $509.82 unlock $517.24-$522.45?

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 500.52 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 521.35 (-4.0%), 50d 519.74 (-3.7%), 200d 444.13 (+12.7%); 50d above 200d
Momentum: RSI(14) 42.9 | MACD -6.578 vs signal -1.935 (histogram -4.643)
Returns: 1d +3.3% | 5d -3.4% | 1m -4.6% | 3m +1.8%
52-week range: 352.83 - 555.80 (now 72.8% of the way up)
Volatility: ATR(14) 16.99 (3.4% of price) | annualised 20d 40.1%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.72T
Valuation: trailing P/E 26.12 | forward P/E 20.68 | P/B 7.90 | PEG 1.43
Profitability: profit margin 41.2% | operating margin 47.1% | ROE 34.2%
Growth (YoY): revenue +18.8% | earnings +32.3%
Balance sheet: debt/equity 28.5% | free cash flow 2.99B
Risk: beta 1.04 | short interest 0.8% of float
Next earnings: 2027-01-27
```

</details>

<details><summary><b>What this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.60</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 in line
  2026-09-30 in line | 2026-06-30 beat by 10% | 2026-03-31 beat by 3% | 2025-12-31 beat by 3%
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
Consensus: strong_buy (mean 1.36 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 13 strong buy, 41 buy, 4 hold, 0 sell, 0 strong sell
Price target: mean 636.12 (+27.1% vs last close), range 440.00 - 870.00
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

_Not available today._

</details>

### Royal Bank of Canada (RY) · Company — BEARISH, confidence 0.58

**Result:** ACCEPTED · 1 shares · submitted sell 1 RY @ ~188.95, stop 196.78

**In the model's own words:**

> Technical indicators show the stock trading below its 20‑day, 50‑day and 200‑day moving averages, RSI is in oversold territory but MACD is negative and volume is only 3 % of the 20‑day average, suggesting continued downside pressure in the short term. Recent analyst coverage from Erste Group cut FY2026 and FY2027 EPS estimates, adding bearish sentiment. While the broader analyst consensus remains bullish with an 11 % price‑target upside and insiders made modest purchases, the immediate technical weakness and negative earnings outlook outweigh the longer‑term fundamentals, leading to a bearish near‑term view with moderate conviction.

**Main reasons it gave:**
- Price below 20‑day (199.94), 50‑day (199.10) and 200‑day (191.63) SMAs
- RSI 33.3 and MACD negative (-3.342) indicating bearish momentum
- Volume at 0.03× 20‑day average, signaling low participation
- Erste Group Bank cut FY2026 and FY2027 EPS estimates
- Insiders bought ~745 shares on 2026‑10‑30 ($152k total)

<details><summary><b>News</b> — score -0.20</summary>

- [RBC Capital Markets Hosts Global TIMT Conference Featuring 100 Technology, Internet, Media and Telecom Leaders](https://quantisnow.com/insight/rbc-capital-markets-hosts-global-timt-conference-featuring-100-technology-6803425)  
  <sub>Quantisnow, 35 minutes ago</sub>  
  Two-day event convenes senior management and investors across software, internet, payments, hardware, datacenters and semiconductors to assess AI adoption.
- [Royal Bank of Canada stock falls amid sustained weak momentum and oversold technical signals](https://tradersunion.com/news/stocks/show/4373927-royal-bank-of-canada-down/)  
  <sub>Traders Union, 40 minutes ago</sub>  
  Royal Bank of Canada trades at C$263.05 today, down 2.38%. Technicals point to continued weakness and a high risk of further decline.
- [AI is moving from pilot projects into core business workflows, RBC analysts say.](https://www.google.com/goto?url=CAESsAEBxCJF18aw1rbINUnLLdXttsStCg-5N9AAGHozq-ZDJZuiFQMnU1x9ulZFXGrkLuXSmCvTTqGQ3W0DmGkSfAXG8p00u0RHqqzbw93_JF1-1nyfr_qGo7zh3rzWnkb5LVi9YAm06tT3S4QNwkRpg2ibVBb7OeOWr5HqlixsEZN1fNI32Blt-WLtVBcJ3To36rI7eeCuenq84KpkgzfrX9n7_7WCinpxfdYVes8UHwbxtQ&gsessionid=klE_KqDSqbaRUtoltyYD-MY4x2z3P6WWXpl5GFOYQjzADUuc1s0WtQ)  
  <sub>Stock Titan, 41 minutes ago</sub>  
  RBC Capital Markets (RY) wrapped up its Global Technology, Internet, Media and Telecommunications Conference, held November 17–18, 2026, in New York.
- [Royal Bank Of Canada's (NYSE: RY) Crypto-Linked Portfolio Swells To $256 Million As Digital Asset Bets Multiply](https://www.google.com/goto?url=CAES2QEBxCJF1-aOpt2i-ZQ-g0QD25RuMykJa3ONoNxOWrQr2POWRUzBM_fekNfM5pil9zJMdAM1cVJKmKlA6GPSieNrY8TvW7BsBjzeXheVK2vXhMiRVpuT2cZHgmDvCWGJ1XN6gHGSkPrTPPzvIB83MLZa5oem6gHyZsRmeWao_j8IBUyBWjXrZ_1V7tbg5sPu0Q5uDv-gnE2EVplM_7kim1Dm8dcKrwTfsul77rMKILVv364kHKU_yAkiOQ_YsM19kTl1BEQJozd_fBStPY8GtHdGDa4y67ENPB72&gsessionid=klE_KqDSqbaRUtoltyYD-MY4x2z3P6WWXpl5GFOYQjzADUuc1s0WtQ)  
  <sub>Foreign Policy Journal, 3 hours ago</sub>  
  With roughly $256 million allocated to crypto-linked equities, funds, and structured notes as of September 30, Canada's largest bank has made its digital.
- [Avoiding Lag: Real-Time Signals in (RY) Movement](https://www.google.com/goto?url=CAESuwEBxCJF12XyqBddJlAjfGlBtDwseEnZ7jIqdG8diS36gMxDxd9qeoAaK9F0mX6Wxp9jsW1YcUgbCvSG-ySz6Gm2MX5oiFqsvDEL2DUnPDvarLz92oDyxrmz5MkYk6NG3buNxSolaT794-O4RlSrVwyAe5FIBFXdgFHw3OMJ71OMqaj8YvGsL5aAobXP_Qj4WJDCnIQdc04vRKswNupHG3D7AiZGzm0a3Wbk1w-p7BfWsX2sxGf37-LL8M17&gsessionid=klE_KqDSqbaRUtoltyYD-MY4x2z3P6WWXpl5GFOYQjzADUuc1s0WtQ)  
  <sub>Stock Traders Daily, 6 hours ago</sub>  
  Price-action only: Royal Bank Of Canada (RY) movements set the tone for institutional models. Avoiding Lag: Real-Time Signals in (RY) Movement.
- [Harvest High Income Shares ETFs Announces November 2026 Distributions](https://www.google.com/goto?url=CAESuwEBxCJF11NXIpqlIHgOcK-0sfnFsQu6DEt4xJAg3NW_CIMm2rFIDwx0KmUO8UDXqMEbMU0t6l-GkAIx5elGNPGWkspB42C45_W0BCRtnag04sij3LwpvM4NWPoHIoskwzE8xWZjxbtfstA-roMIGw1NYRLs9H2e-HS1YBPBuF3gpRG5xGl3qgm7P_GDOTsqX5DiD7OMCGf2GezRQvIGrzGr6dpM-LtPhQ2wET7YBMxVWMyQRnN7ZzJrsTZs&gsessionid=klE_KqDSqbaRUtoltyYD-MY4x2z3P6WWXpl5GFOYQjzADUuc1s0WtQ)  
  <sub>Business Wire, 2 hours ago</sub>  
  Harvest Portfolios Group Inc. (“Harvest”) announces the following distributions for Harvest High Income Shares ETFs for the month ending November 30, 2026.
- [Erste Group Bank Analysts Decrease Earnings Estimates for RY](https://www.google.com/goto?url=CAESuQEBxCJF18Y9uLPclY5OY4BsSTU8dGapxi8dgsbGP1GMdnxb_SD4EfxeQPSARYQaPUUL-oGLtSNy_EphKQ2_TWJBkI5H5_BvtH1MV_cjKwPyVYRz0RAKOjRuLftHvr1Psb9GCh3IaVsf0x_kvj-D-NQikI1Faa4rJJ3Z-MJaWAp-qCT0wLK_UbfICaMMH1ktSWbG9Rjqbhv1zN23t3lTRRZSFQnkiNf8NWlhgdqxqTY1w2EQg8ktTUYpKA&gsessionid=klE_KqDSqbaRUtoltyYD-MY4x2z3P6WWXpl5GFOYQjzADUuc1s0WtQ)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Royal Bank Of Canada (NYSE:RY - Free Report) (TSE:RY) - Equities research analysts at Erste Group Bank dropped their FY2026 earnings per share estimates for...
- [Erste Group Bank Has Negative View of TSE:RY FY2027 Earnings](https://www.google.com/goto?url=CAESuQEBxCJF17_zhYx9EQYIWHSdpAXQItgizxd0AXhyFobwEHBsNOrJN39TM4cGNewG1tSYcKe_t0619O_l_yXallKas1hUh7A-oJO2bwCmaYz9R1dOqK7ZHVK_97ZNPHHS1jPd-zGvcl6_XfEtFc4yJW_N0mU6MGuEJcj2cFV7kSnFsjJ0boAP7fzkLRKTlHlXzZOwrmmStY1Om9emS9_tREW6DAd_1NbR5hUCCROJGFdsHvZTLOcbOPpE8Q&gsessionid=klE_KqDSqbaRUtoltyYD-MY4x2z3P6WWXpl5GFOYQjzADUuc1s0WtQ)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Royal Bank of Canada (TSE:RY - Free Report) (NYSE:RY) - Equities research analysts at Erste Group Bank cut their FY2027 EPS estimates for Royal Bank of...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 186.57 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 199.94 (-6.7%), 50d 199.10 (-6.3%), 200d 191.63 (-2.6%); 50d above 200d
Momentum: RSI(14) 33.3 | MACD -3.342 vs signal -1.138 (histogram -2.204)
Returns: 1d +1.7% | 5d -6.5% | 1m -7.3% | 3m -9.9%
52-week range: 149.71 - 217.87 (now 54.1% of the way up)
Volatility: ATR(14) 3.89 (2.1% of price) | annualised 20d 25.2%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 258.29B
Valuation: trailing P/E 16.31 | forward P/E 14.64 | P/B 2.71 | PEG 1.76
Profitability: profit margin 33.9% | operating margin 45.7% | ROE 16.2%
Growth (YoY): revenue +8.9% | earnings +12.8%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.92 | short interest n/a of float
Next earnings: 2026-12-03
```

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.40</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-09-30 in line | 2026-06-30 in line | 2026-03-31 beat by 3% | 2026-03-31 beat by 3%
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: buy (mean 2.21 on a 1=strong buy to 5=strong sell scale, 3 analysts)
Ratings: 4 strong buy, 4 buy, 5 hold, 0 sell, 1 strong sell
Price target: mean 207.69 (+11.3% vs last close), range 181.27 - 228.43
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

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

### Caterpillar (CAT) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room for equity CAT under its 5% cap or the sleeve budget limit: equity 99032.65, price 551.57, existing exposure 0.00, headroom 200.90

**In the model's own words:**

> The company reports a record backlog and strong power‑generation demand, and analysts maintain a buy consensus with a mean price target ~49% above current levels, indicating attractive upside. Fundamentals are solid with high margins, strong growth and a reasonable PEG, though leverage is high. Technicals are bearish—price sits well below its 20‑, 50‑ and 200‑day averages, RSI is low and volume is thin—capping conviction, but the bullish fundamentals and insider buying suggest a modest upside in the next few days.

**Main reasons it gave:**
- Record backlog and power‑generation demand remain strong (Kalkine Media)
- Insider purchase: director James C. Jr bought 1,000 shares
- Price below 20‑, 50‑ and 200‑day SMAs, RSI 32.9 (bearish technicals)
- Valuation: forward P/E 16.8, PEG 0.90 (moderately attractive)
- Analyst consensus: buy, mean target $807 (+49% upside)

<details><summary><b>News</b> — score +0.30</summary>

- [Why Is Caterpillar Stock Falling?](https://www.trefis.com/stock/cat/articles/627850/why-is-caterpillar-stock-falling/2026-11-23)  
  <sub>Trefis, 6 hours ago</sub>  
  Today's big story: Reported SEC Probe: Could Nvidia Stock Fall To $92?Caterpillar (CAT) stock fell 5.0% on Friday, November 20, 2026, while the S&P 500 lost...
- [As AI Stocks Plummet, Insiders Are Buying Into These 3 Names](https://www.marketbeat.com/articles/as-ai-stocks-plummet-insiders-are-buying-into-these-3-names/)  
  <sub>MarketBeat, 1 hour ago</sub>  
  Amid an AI stock sell-off, insiders at Intel, Coherent, and Caterpillar, including two CEOs, recently bought shares, signaling confidence despite sharp...
- [CAT (NYSE:CAT) Record Backlog and Power Generation Demand Tested by November Pullback](https://www.google.com/goto?url=CAESvgEBxCJF171qP6Y356QQC4gITbcz7Hq_RkBcu4voqGo7CidPB4rTZGcmUQBZLVcOPehRUBBbgFbk6cCv-zjcYGwnEyIsPpt-YnxH2Q3IWNUDeZxYjqEEsvUzD_YYgaOOpKPQqv5W2nqqg96ZvcZfcEkHodGBb235pJQs_R03QoDLzGx-RHeIlxGh_iEiFGXDaxiJWlE07qL-L-nm-7rUiwRczoJfJdTo2ofDJzLiXLnlw7ecnJNsDSwcU_xOXNrV&gsessionid=8fZrc6rqTWX8nSPZLlyjgc6bA01JfxeOLmmWPLUKV2ERDROPQ2Pg7A)  
  <sub>Kalkine Media, 7 hours ago</sub>  
  Caterpillar (NYSE:CAT) carries a record backlog as data center power demand surges, even as shares fall sharply amid AI spending concerns.
- [CAT Dec 2026 870.000 call (CAT261204C00870000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXeU51ng_HtmN4myWyrETBZb-8duhmZR8aOY6ekWmEGN7GyqPBMQME-rwCqP-sxw6S3BnMuFbx5uBMRke8_2M2FpVBv1QnG_kcwusV4hp19k4THK6demu2xCjA3VlVVfVxqu0gUbTthAkGKu3FiPg&gsessionid=8fZrc6rqTWX8nSPZLlyjgc6bA01JfxeOLmmWPLUKV2ERDROPQ2Pg7A)  
  <sub>Yahoo Finance UK, 7 hours ago</sub>  
  Find the latest CAT Dec 2026 870.000 call (CAT261204C00870000) stock quote, history, news and other vital information to help you with your stock trading...
- [GME Stock Heads For A Green Month: Wall Street Reportedly Sees A New Growth Story Beyond The Meme-Stock Hype](https://www.google.com/goto?url=CAES5gEBxCJF14g6aYgj_xsVskfx6_Zgbp_Szqhx8HTN-T42TkwYPYbVgZT8rGQ27xVwBCJqc5_06B8-5f1UNy2z6xwSmOPgBo3HAUGv8bZjxDGa3JR2K1s7xYFi_w0H0SsTyaZ-B9GILkUzomt3iBtRSyzcK7HqMHNNpubHdKETJ_QR3s37S9xu6NH8AKsHrPBNG8AqGupZZVgH01uSDTMn7WaRXH3mTIEt_kGLX0-fT-Nv-uQI2vv6l-uifNWs-Hp_csa-AokEtKOm6wh0hp7hyeC5B9q4C53pUZrsRX0UEbqP6IsSsWoDuw&gsessionid=8fZrc6rqTWX8nSPZLlyjgc6bA01JfxeOLmmWPLUKV2ERDROPQ2Pg7A)  
  <sub>TradingView, 9 hours ago</sub>  
  GameStop (GME) stock is on track for a green month as Wall Street sees a future beyond meme-stock hype. StoneX initiated coverage with a 'Buy' rating,...
- [CAT Nov 2026 400.000 call (CAT261127C00400000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScwHEIkXXIeHz2Te4tbydfz0kYNTeCSDLFAaNbCSiFCmMsQnjgivxApvID65Jj_nptuLp_JC7eAPw-pXXUHTwUAfeB29BFvymeaZte8gxnkIfh95zXsqRBWiY8_nqr3oe_KS1GbBeHMpSgA1wLl-pm_QVXNY&gsessionid=8fZrc6rqTWX8nSPZLlyjgc6bA01JfxeOLmmWPLUKV2ERDROPQ2Pg7A)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Find the latest CAT Nov 2026 400.000 call (CAT261127C00400000) stock quote, history, news and other vital information to help you with your stock trading...
- [CAT Nov 2026 400.000 put (CAT261127P00400000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScwHEIkXXMmY2LJMgfsp5VeqLNasnWSksyEVWKsFilBm5mQXz8ntNFD-UvvR126dZNXDvXDXHLmDvu3hJwiuGVSZdXVU3C5OY3aPVuG_QRukaj5pg8Qolfv2LbT9K92OX4P_xxtKGE4Ia_rGLyhzMvwICr8M&gsessionid=8fZrc6rqTWX8nSPZLlyjgc6bA01JfxeOLmmWPLUKV2ERDROPQ2Pg7A)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Find the latest CAT Nov 2026 400.000 put (CAT261127P00400000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Catapult Sports (ASX:CAT) Shares in Focus: What Does the ASX 300 Sports Tech Stock's Leading Division This Period Signal?](https://www.google.com/goto?url=CAES3wEBxCJF1-TNtTLTtO6DMkXvonpbG5LHX7Opn4Mln6DcpPOE_xUhhJLz34ZeoLxhs6LaJhwOkh3T2gnmcIWB_zaXazzDNR1iFS19PCXVMLzCJTZgCOugLMJPbY91oaI4SVTX8eWiZDRG5LMMwF-oO7cNKS3WWx03r_Xk3JZj-2_xSZ5zXlQpnSnWhrf344y9cWqOaP6wpJNtMP5PfKRI09JAOE7o4M7a6jBCAZj-GAeUstQFrEX4C8oQ6SPfKp4Ud88sHy5P5EjXqu9kxvNQcq-KbNSDewO8lBz4txnOIRxR&gsessionid=8fZrc6rqTWX8nSPZLlyjgc6bA01JfxeOLmmWPLUKV2ERDROPQ2Pg7A)  
  <sub>Kalkine Media, 14 hours ago</sub>  
  Catapult Sports (ASX:CAT) Technology Catapult Group International Ltd (ASX:CAT) 2.64 AUD -0.040 ↓ 1.493% Last Updated at: 2026-11-23T05:10:00Z is back on...
- [Caterpillar (CAT) Stock Price Prediction: Bearish structure meets an oversold bounce test](https://www.google.com/goto?url=CAESogEBxCJF1-HU8ONhOj5-wdwIBQNKfaaCKgIVDQx33SnTRfwXe0_z2FcGmZen-WPAqK0LVKxB1r0VDE5sTsQpsvS5NOb-PlxD52Qlv8w-ClAPMWFpcYlMC6w1QYo5RhzgxnmW3cEhri05O9Ri_R0Jy6yQWhwe9z0_5JVOc0xYnQ7NZSNU-mkm202ltFqvPm6N5prsr_STTWgGuxIemziYjCXMr8s&gsessionid=8fZrc6rqTWX8nSPZLlyjgc6bA01JfxeOLmmWPLUKV2ERDROPQ2Pg7A)  
  <sub>Blockchain News, 4 hours ago</sub>  
  Caterpillar (CAT) is trading at $532.23, modestly higher on the session, but the broader technical setup remains weak with price below the 7-, 20- and...
- [CAT DCF Analysis: Intrinsic Value $810 vs Price $510](https://www.google.com/goto?url=CAESlQEBxCJF1y4UfHJXNnsFzyOo_SPHIC5N06ojZOJKWxgq_HeUBFZbYDeviRnjlmpZjxbbqtvICIdAY9XKqDoe7h4oE5HA1j8N_-UzEJojGMidCZyI9AuKn1SfAdwiS0jbq1wnDJxKLBtZraYyxbQe5M3LIotPWohUsZTUGL5cYXB5gu3I2BLoawjhXnG2oyvnks03mz84Xg&gsessionid=8fZrc6rqTWX8nSPZLlyjgc6bA01JfxeOLmmWPLUKV2ERDROPQ2Pg7A)  
  <sub>GuruFocus, 2 hours ago</sub>  
  On November 23, 2026, we delve into the DCF analysis for Caterpillar Inc (CAT), a company currently facing notable price performance challenges.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 540.24 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 595.83 (-9.3%), 50d 709.34 (-23.8%), 200d 803.14 (-32.7%); 50d below 200d
Momentum: RSI(14) 32.9 | MACD -49.433 vs signal -48.620 (histogram -0.813)
Returns: 1d +5.8% | 5d -5.3% | 1m -21.4% | 3m -33.4%
52-week range: 510.45 - 1,064.90 (now 5.4% of the way up)
Volatility: ATR(14) 30.31 (5.6% of price) | annualised 20d 65.8%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 247.21B
Valuation: trailing P/E 21.20 | forward P/E 16.79 | P/B 11.51 | PEG 0.90
Profitability: profit margin 15.2% | operating margin 18.8% | ROE 56.1%
Growth (YoY): revenue +17.3% | earnings +46.1%
Balance sheet: debt/equity 210.4% | free cash flow 3.97B
Risk: beta 1.64 | short interest 2.0% of float
Next earnings: 2027-01-28
```

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.40</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 in line
  2026-09-30 in line | 2026-06-30 beat by 31% | 2026-03-31 beat by 19% | 2025-12-31 beat by 9%
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

```text
Consensus: buy (mean 1.97 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 2 strong buy, 15 buy, 11 hold, 1 sell, 0 strong sell
Price target: mean 807.26 (+49.4% vs last close), range 575.00 - 1,027.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

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

### Alphabet (Google) (GOOGL) · Company — BEARISH, confidence 0.50

**Result:** REJECTED · no room for equity GOOGL under its 5% cap or the sleeve budget limit: equity 99032.21, price 283.48, existing exposure 0.00, headroom 200.54

**In the model's own words:** no explanation. It wrote only “NEWS”, so the main reasons below are all it gave.

**Main reasons it gave:**
- News: multiple articles flagging sell‑off and AI spending concerns
- Technical: price 4% below 20‑day SMA, RSI 36.6, volume 0.15× 20‑day avg
- Earnings: 3 of last 4 quarters missed consensus
- Fundamentals: earnings down 25% YoY, free cash flow -$1.16B

<details><summary><b>News</b> — score -0.60</summary>

- [What's Wrong With Alphabet Stock?](https://www.fool.com/investing/2026/11/23/what-s-wrong-with-alphabet-stock/)  
  <sub>The Motley Fool, 2 hours ago</sub>  
  Shares of Alphabet (GOOG -2.59%)(GOOGL -2.70%) have been nosediving in recent months. The sell-off has gotten so extreme in recent months that the tech...
- [Alphabet (GOOGL) Stock Trades Below Fair Value Despite AI Chip Expansion](https://simplywall.st/stocks/us/media/nasdaq-googl/alphabet/news/alphabet-googl-stock-trades-below-fair-value-despite-ai-chip)  
  <sub>Simply Wall St, 2 hours ago</sub>  
  Alphabet has pulled back sharply in recent weeks after a strong multi year run. The question now is whether the current share price still lines up with what...
- [Google Can Spend $48 Billion More On AI From Its Own Cash. Is That Enough For Nvidia?](https://www.google.com/goto?url=CAESzgEBxCJF1_18Y4CqjrYZsV6_iH0EKNvsdoQDTK3sOOZne6qLBkFVrmRi-WgBlIYWLILWOquM_udypjs-lh4kdbeCERpKvM0PlMWriSHQR3sEAdfxG1yDd_eihFzmI6HQD04vpgeRh55IMNUgo8buSF1Crlh02rbR_XuT2cj8FXoR68TWL3IEJrRbLF6Jxt6nqRG3y1vgSGhdsFVydQQNxuMigfIAjb1sF9nYCB1uzLRAz1PpVe1GWVpsYU-VqfKgEg4FogiykfxCCKHgejFQew&gsessionid=1RFNiNd3eDsFYpzIreAyzUeZAtQSSsjCokElL-YTGrLXQYjWmEx58g)  
  <sub>Trefis, 8 hours ago</sub>  
  Today's big story: Reported SEC Probe: Could Nvidia Stock Fall To $92? Can Alphabet, Google's parent, pay for more AI spending next year from its own cash?
- [This under-the-radar penny stock could be set to surge in 2027](https://www.google.com/goto?url=CAESiwEBxCJF170m7LdZXTVd3jX5xvYp_KNKvx-eJA0ItMlg-Lv-letRvSHvx9EIzE5_WUemh4mHcwdWYsd014naQyDVQz0rTR-4XxD8PULwZ8AdAf5r-61i6LIM7wrX8p_4LM1-jNcMWD-U0N6UsE8M0MDkBXeAf9WgiWPf3q7PRJS_T6B8wKMuPh6vpdWV&gsessionid=1RFNiNd3eDsFYpzIreAyzUeZAtQSSsjCokElL-YTGrLXQYjWmEx58g)  
  <sub>Yahoo Finance UK, 6 hours ago</sub>  
  Zaven Boyrazian reviews a penny stock enjoying exceptional momentum across its business with skyrocketing revenue, earnings, and cash flow!
- [Meta vs Google Stock: $127.6B Quarter Frames the Debate](https://www.google.com/goto?url=CAESjwEBxCJF18NM_0uWdPTk-Alx4GVGLnxLFaGbpoGnbeVQ1ZLvrQD1PptHsPL2Q4rXfk86GGe3D2ld7WQVz-WKpPvPwUN8A0NUi0yhjRr4V5ANn2S7JvhlDKu0pztYIdXkMz516rMBI3SOjWzAsAlpV_QaI8RlHzbXDvy51eHCQM_uQ0-LB1Iqbg2zjHST4DEubQ&gsessionid=1RFNiNd3eDsFYpzIreAyzUeZAtQSSsjCokElL-YTGrLXQYjWmEx58g)  
  <sub>shattered.io, 22 hours ago</sub>  
  META vs GOOGL: Alphabet posted $127.6B revenue and 103% Cloud growth, Meta EPS hit $3.83. What the verified numbers show and miss.
- [Alphabet (GOOGL) Stock Price Forecast 2026: Cloud Hit $20B But FCF Collapsed — Buy or Short?](https://www.google.com/goto?url=CAESvAEBxCJF181eBVY64qXksoThEUWSQJz4mj-Y5C2241pw4g2shbQ6z6lXlLV5eRqcxG6uoODBxvWxU6Ojq2eC25XxMSu7lxlQgDAc8A9PFtDv_DFN5hzm6DQt3XSYkwE8Z47UtfSYed44ZfCxw-uqQ4F4ExSKLzTXfQ2LXNH7772-mfTqn8GDB0pLMQKSETt1t9rEJX4s2oF8E-tQY72NxUj5azz1rUoL51TzS5i6khv7aMnkcgo8Y9NnkHTx-A&gsessionid=1RFNiNd3eDsFYpzIreAyzUeZAtQSSsjCokElL-YTGrLXQYjWmEx58g)  
  <sub>TradingKey, 20 hours ago</sub>  
  The main reason the market is selling Alphabet stock down is the increased $190 billion 2026 capex guidance which has dropped Free Cash Flow margin down from 21...
- [Broadcom Stock (AVGO) Falls 12.2% on Reports of Google Cut (Nov 20)](https://www.google.com/goto?url=CAESigEBxCJF146Qc9y6ixG1SrCBrh6hXvY2zodBbGu7Mxe0OO5aSqoxshophtXK9tBiqOqvGGCvBmpTxJtrVJv7uYxg6ebO9eQ6XLexA9v3fbFDfCqHb10GDLexRYVYaHI1z9OTZliCeahFvTbv7x7eSKkdaPqxncMoL90F7igq6dpEtWDrFwtNTN0bSzU&gsessionid=1RFNiNd3eDsFYpzIreAyzUeZAtQSSsjCokElL-YTGrLXQYjWmEx58g)  
  <sub>Gotrade, 11 hours ago</sub>  
  Broadcom (AVGO) fell 12.19% to $304.41 on Nov 20 after an analyst said Google cut 2027 orders for Broadcom-designed TPU chips, unconfirmed so far.
- [Her $420,000 in Employer Stock Inside Her 401(k) Lost 11% in a Day. Rolling It Into an IRA Would Turn Her Long-Term Gain Into Ordinary Income](https://www.google.com/goto?url=CAES-AEBxCJF10rJiIYssQDg2FpThIAeDW_oVNB3xNm7Qfx7OszQFUQzlQmfiNguKHRAy-onQ88Ym5Hvl7jqcSqxhkgB7rnMEjy3LeWnuQ_RoEcE2C0dNEMiJpFi84g1PX3iOVK5AQQGoSzyOxGxA96sEOckYko9QF-egW_xCOsdYKrvgCzb0lpoU_06wiq1LKRyVHAeizWt__l3jolKhzSf4cUOtbwoBr_7KtcWDHvUY4cvRTHDi0lzWDQQuZ4Ua7U-JoyTY-SdGSyqLB_fUV3VJsUNGlSbpgpCnSacCNz8j2ICF5--4tFvhWZhl2yN99eb-tAMeYlYqI0oeA&gsessionid=1RFNiNd3eDsFYpzIreAyzUeZAtQSSsjCokElL-YTGrLXQYjWmEx58g)  
  <sub>24/7 Wall St., 17 hours ago</sub>  
  Rolling $420,000 of AVGO stock into an IRA converts $350,000 of gain into ordinary income, costing about $100,000 in federal tax at 24%.
- [The S&P 500 Just Had Its Worst Week in 18 Months. Is This a Buying Opportunity?](https://www.google.com/goto?url=CAES4AEBxCJF1wmjImTk7T-KMgCAsoMYegxWtJEFRq5yORitxa5_PSmVWA44SeWIhpMpvo6QZQ2KrGxuEag5IZj9bNN-vRASahtvxYIyIn3HxaU_3KJ33f93IlbdWMj1w7xQbhxm9fBo7sVwi32VP4v_GPCu3bQ1DRX5ds95z4jN4TZZT2UV8hbMYaJQQ8Hh4ifV1x74WIWLs-79j6JJgK9uraykWz7a1kPLhnSdi4V0bbflGpLgmcpBi_m4JSx7VCW8B2Ww5e6lhOLeGhjczAyds-yPGKfyAM6SpvMQUjf18kl_8w&gsessionid=1RFNiNd3eDsFYpzIreAyzUeZAtQSSsjCokElL-YTGrLXQYjWmEx58g)  
  <sub>The Globe and Mail, 6 hours ago</sub>  
  The S&P 500 sank nearly 9% last week, pushing it into correction territory. The sell-off was led by AI stocks amid worries about AI spending and fallout...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.70</summary>

```text
Last close 275.72 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 287.40 (-4.1%), 50d 320.83 (-14.1%), 200d 336.74 (-18.1%); 50d below 200d
Momentum: RSI(14) 36.6 | MACD -13.252 vs signal -13.099 (histogram -0.153)
Returns: 1d +3.9% | 5d -2.8% | 1m -13.9% | 3m -20.5%
52-week range: 265.29 - 402.62 (now 7.6% of the way up)
Volatility: ATR(14) 11.89 (4.3% of price) | annualised 20d 56.0%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 3.39T
Valuation: trailing P/E 14.40 | forward P/E 18.03 | P/B 5.14 | PEG 0.94
Profitability: profit margin 50.0% | operating margin 33.3% | ROE 44.3%
Growth (YoY): revenue +24.7% | earnings -25.3%
Balance sheet: debt/equity 22.2% | free cash flow -1.16B
Risk: beta 1.23 | short interest 1.5% of float
Next earnings: 2026-10-28
```

</details>

<details><summary><b>What this fund holds</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.30</summary>

```text
Earnings record, last 4 quarters: 1 beat, 3 missed
  2026-09-30 missed by 14% | 2026-06-30 missed by 4% | 2026-03-31 missed by 3% | 2025-12-31 beat by 4%
```

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

```text
Consensus: strong_buy (mean 1.34 on a 1=strong buy to 5=strong sell scale, 53 analysts)
Ratings: 10 strong buy, 43 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 397.13 (+44.0% vs last close), range 300.00 - 500.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 202,850,992 shares
Distinct insiders: 0 buying, 0 selling
(3 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score -0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.00</summary>

_Not available today._

</details>

### Novo Nordisk (NVO) · Company — BEARISH, confidence 0.45

**Result:** ACCEPTED · 5 shares · submitted sell 5 NVO @ ~38.92, stop 41.18

**In the model's own words:**

> Technicals show a clear bearish bias – price is below the 20‑day, 50‑day and 200‑day moving averages, RSI is under 50 (42.9) and MACD is negative, indicating downward momentum. Fundamentals are mixed: the stock trades at a historically cheap trailing P/E of 9.75, but earnings are falling (‑15.8% YoY) and the recent earnings record includes two consecutive misses, which weakens the upside case. Analyst consensus is neutral (hold) but recent downgrades from Morgan Stanley, Goldman Sachs and JP Morgan suggest a modest negative tilt. News coverage notes the cheap valuation and strong margins but provides no catalyst that would drive the stock higher in the short term. Insider activity shows no recent buying, offering no bullish signal. Combining these dimensions, the balance of evidence points to a modest bearish outlook over the next few days, but without a strong catalyst, conviction remains moderate.

**Main reasons it gave:**
- Price below 20‑day (40.10), 50‑day (39.49) and 200‑day (42.83) SMAs; RSI 42.9, MACD negative
- Trailing P/E 9.75 (cheap) but earnings down 15.8% YoY and two recent earnings misses
- Analyst consensus hold with recent downgrades (Morgan Stanley, Goldman Sachs, JP Morgan)
- News mentions cheap valuation and strong margins but no specific catalyst

<details><summary><b>News</b> — score +0.25</summary>

- [Bristol Myers Squibb vs. Novo Nordisk: Which Healthcare Stock Is a Better Buy for 2027?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b0450e844244336a043c40a89132736&url=https%3a%2f%2fwww.fool.com%2fcoverage%2fbetter-buy%2f2026%2f11%2f22%2fbristol-myers-squibb-vs-novo-nordisk-which-healthcare-stock-is-a-better-buy-for-2027%2f&c=10615420290970645176&mkt=en-us)  
  <sub>The Motley Fool, 29h ago</sub>  
  Novo Nordisk's profit margins are running far above Bristol Myers, yet the cheaper valuation tells a different story about where the value sits.
- [Will Novo Nordisk stock hold $35.78 support amid persistent downward momentum?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b0450e844244336a043c40a89132736&url=https%3a%2f%2ftradersunion.com%2fnews%2fstocks%2fshow%2f4368989-novo-nordisk-slides-2-73percent-today%2f&c=16974290578444999847&mkt=en-us)  
  <sub>tradersunion, 15h ago</sub>  
  Novo Nordisk trades at $37.81 today, slipping 2.73% as bearish momentum persists amid high volatility and technical pressure.
- [Novo Nordisk (NYSE: NVO) Trades At A Decade-Low Valuation Even As Its Wegovy Pill Dominates Oral GLP-1 Market](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b0450e844244336a043c40a89132736&url=https%3a%2f%2fwww.foreignpolicyjournal.com%2f2026%2f11%2f22%2fnovo-nordisk-nyse-nvo-trades-at-a-decade-low-valuation-even-as-its-wegovy-pill-dominates-oral-glp-1-market%2f&c=927281467827580171&mkt=en-us)  
  <sub>Foreign Policy Journal, 23h ago</sub>  
  A pharmaceutical company trading at a price-to-earnings ratio of roughly 10 times earnings, against a five-year average of 23 times, typically signals serious ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 38.60 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 40.10 (-3.7%), 50d 39.49 (-2.3%), 200d 42.83 (-9.9%); 50d below 200d
Momentum: RSI(14) 42.9 | MACD -0.193 vs signal 0.087 (histogram -0.280)
Returns: 1d +2.1% | 5d -7.2% | 1m -1.2% | 3m -20.7%
52-week range: 35.29 - 63.98 (now 11.5% of the way up)
Volatility: ATR(14) 1.11 (2.9% of price) | annualised 20d 37.1%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 170.12B
Valuation: trailing P/E 9.75 | forward P/E 10.99 | P/B 5.20 | PEG 3.96
Profitability: profit margin 33.9% | operating margin 50.8% | ROE 58.4%
Growth (YoY): revenue +5.6% | earnings -15.8%
Balance sheet: debt/equity 61.7% | free cash flow 32.75B
Risk: beta 0.37 | short interest 1.2% of float
Next earnings: 2027-02-03
```

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.10</summary>

```text
Earnings record, last 4 quarters: 1 beat, 1 in line, 2 missed
  2026-09-30 missed by 22% | 2026-06-30 missed by 6% | 2026-03-31 beat by 23% | 2025-12-31 in line
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

<details><summary><b>What analysts and big funds say</b> — score -0.20</summary>

```text
Consensus: hold (mean 2.85 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 0 strong buy, 2 buy, 10 hold, 1 sell, 0 strong sell
Price target: mean 45.56 (+18.0% vs last close), range 39.25 - 63.78
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

### Teva Pharmaceutical (TEVA) · Company — NEUTRAL, confidence 0.42

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The recent news offers no clear catalyst for TEVA; the most material items are a price slip below the 50‑day SMA and a newly announced fraud investigation, both mildly bearish, while sector‑wide FDA approvals are not ticker‑specific. Technicals show short‑term weakness (price below 20‑ and 50‑day SMAs, RSI 44.6, negative MACD, and volume at only 4% of the 20‑day average), suggesting a bearish near‑term bias. Fundamentals are mixed: forward P/E (12.8×) and PEG (0.71) hint at valuation comfort, but trailing P/E is sky‑high (93×), revenue is down 1.9%, earnings down 46%, and debt/equity is extremely elevated (212.9%), overall weighting bearish. Analyst consensus is strongly bullish (buy rating, 26% upside price target), providing a positive counterweight. Insider activity nets a tiny purchase (+0.3% of holdings) amid several sales; sales are weak evidence and buys are modest, so the signal is neutral. The dimensions therefore conflict, preventing a high‑conviction directional view. Given the mixed evidence, a neutral bias with modest conviction best reflects the current outlook.

**Main reasons it gave:**
- Price slipped below 50‑day SMA, indicating short‑term weakness (technical)
- Analyst consensus remains buy with mean price target $50.51 (+26% upside) (analyst)
- High debt/equity (212.9%) and earnings down 46% YoY raise fundamental concerns (fundamentals)
- Fraud investigation announced, adding potential negative catalyst (news)

<details><summary><b>News</b> — score -0.30</summary>

- [Teva's Mixed SMA Signals: Should You Stay Invested or Exit the Stock?](https://finance.yahoo.com/healthcare/articles/tevas-mixed-sma-signals-stay-121800089.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Teva Pharmaceutical Industries Limited TEVA stock slipped below its 50-day simple moving average (SMA) on Nov. 19, after consistently trading above this...
- [FDA Approval for TREPROSTINIL issued to ACTAVIS LABS](https://www.quantisnow.com/insight/fda-approval-for-treprostinil-issued-to-actavis-labs-6802875)  
  <sub>Quantisnow, 5 hours ago</sub>  
  Submission status for ACTAVIS LABS's drug TREPROSTINIL (ORIG-1) with active ingredient TREPROSTINIL has changed to 'Approval' on 11/20/2026.
- [Patients Gain New Treatment Options in a Busy Month for Drug Approvals](https://www.google.com/goto?url=CAESuwEBxCJF14mRIANKF-AbIx-__Uaw8yW6DxqcVEQ8Sr8dnYBTHJ_XEQg-BxfFH8UOWYlJM95znUZtBsO6Gf0exyLFDB-6vsGYGAFovDPt8UIfJ1tBlQnq_4h02fT7V9bgrizN3wHljjm7g8G8QRXhSxWkUQHHs5VWOMH6NTvVFxoaWq3Wt7YlJt-JhhNFKNJgdmJ8qlOHMQ6E1eikiD3B2Wjh76R1vH0TlhDpvedEhqX92OJWDwmUxFyrE0JG&gsessionid=3Zy6FFuEICWAcPq1Us9r1bKUG_9H1V6F7v19XEvCi-dlh8a_79BT7A)  
  <sub>PR Newswire, 2 hours ago</sub>  
  Biotech Today News Commentary BOSTON, Nov. 23, 2026 /PRNewswire/ -- November has been a busy month at the U.S. Food and Drug Administration.
- [TEVA Nov 2026 47.000 call (TEVA261127C00047000) stock price, news, quote and history](https://www.google.com/goto?url=CAESdAHEIkXXNqNlmFuV-jvpLOst18iKEgKjUin8V6d_NsRjt9do9z2evbT3PZGDAamZy7A0h2qSp5ZXGJtsnrx0HAYI894xp-6K7TNTpxvam8zCsSVr9WFgC2-9OzL_ZiY2hpNuVyvo4kPKkCJ2Dw1Cgv0qNNag&gsessionid=3Zy6FFuEICWAcPq1Us9r1bKUG_9H1V6F7v19XEvCi-dlh8a_79BT7A)  
  <sub>Yahoo Finance UK, 22 hours ago</sub>  
  Find the latest TEVA Nov 2026 47.000 call (TEVA261127C00047000) stock quote, history, news and other vital information to help you with your stock trading...
- [TEVA Investors Have Opportunity to Join Teva Pharmaceutical Industries Limited Fraud Investigation with SBS Law](https://www.google.com/goto?url=CAES6QEBxCJF1xqWCuKfC0oCD2lY5TQEv_4qZoJG9LTpZVezDAf3Ob1z4o8wCmzSYSD5iePedXPNEDJXId7ZqWSiurRp8hLIvW02Ujt2tQJqkGl-B7rmVAo-aDElckJZmCQmvjcLM1DbGxmizS-2h3IBPQ1BmnwGk3GOWS5YVVXHi-VaggXypRg9J3Vi__G7e68BLwE90XK3Ox_NfhdEAvzCfO1AxTtnfb1BmNbNFWrZ0i-mpwCjk33SJlqJ55aXaBoyH7byvDmisRh2inbBhiTbEkRGd_umVUIuyubqdrn1cTPwjCa_CTBQzYWNtg&gsessionid=3Zy6FFuEICWAcPq1Us9r1bKUG_9H1V6F7v19XEvCi-dlh8a_79BT7A)  
  <sub>FinancialContent, 20 hours ago</sub>  
  Schall, Brown & Schwartz LLP (“SBS”), a national shareholder rights litigation firm, announces that it is investigating claims on behalf of investors of...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 40.04 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 41.74 (-4.1%), 50d 40.65 (-1.5%), 200d 35.28 (+13.5%); 50d above 200d
Momentum: RSI(14) 44.6 | MACD 0.031 vs signal 0.503 (histogram -0.472)
Returns: 1d +2.1% | 5d -5.9% | 1m +1.6% | 3m +5.1%
52-week range: 24.21 - 44.50 (now 78.0% of the way up)
Volatility: ATR(14) 1.41 (3.5% of price) | annualised 20d 45.6%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 46.72B
Valuation: trailing P/E 93.12 | forward P/E 12.79 | P/B 5.86 | PEG 0.71
Profitability: profit margin 2.9% | operating margin 19.8% | ROE 6.7%
Growth (YoY): revenue -1.9% | earnings -46.0%
Balance sheet: debt/equity 212.9% | free cash flow 1.49B
Risk: beta 0.84 | short interest 2.4% of float
Next earnings: 2027-01-27
```

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.20</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-09-30 beat by 15% | 2026-06-30 missed by 92% | 2026-03-31 beat by 9% | 2025-12-31 beat by 39%
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

```text
Consensus: buy (mean 1.53 on a 1=strong buy to 5=strong sell scale, 14 analysts)
Ratings: 4 strong buy, 9 buy, 2 hold, 0 sell, 0 strong sell
Price target: mean 50.51 (+26.1% vs last close), range 42.12 - 57.00
Recent rating changes:
  - 2026-11-12 Piper Sandler: main, Overweight -> Overweight
  - 2026-11-05 Leerink Partners: main, Outperform -> Outperform
  - 2026-11-04 TD Cowen: main, Buy -> Buy
  - 2026-11-04 HC Wainwright & Co.: main, Buy -> Buy
  - 2026-11-02 HC Wainwright & Co.: init, ? -> Buy
  - 2026-10-15 Barclays: main, Overweight -> Overweight
Institutional ownership: 69.7%
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

- [ESLT Mar 2027 680.000 call (ESLT270319C00680000) interactive stock chart – Yahoo Finance](https://www.google.com/goto?url=CAESegHEIkXXW7HEXCAI3L-l3rfv23Xjwjdkg2Jptqgrqs69F5W8-w4l3uCyGw8zByBtRUKAKHzGOZFraHuPUQr2QVAmoSFOrWi-gPf5VP6TTRlmxoFSDkEWWT-CeBQMNGIiv5cYXX7JYcBj2BMrkxpa3yspJYYOPfRoJRQI&gsessionid=r7AoTsQ_jRSKdRi1PzRU8OXg0B9-N-EPvqKvTiBedmkc0QEesL3siQ)  
  <sub>Yahoo Finance Singapore, 11 hours ago</sub>  
  Interactive chart for ESLT Mar 2027 680.000 call (ESLT270319C00680000) – analyse all of the data with a huge range of indicators.
- [Weekly Recap: Record $33B backlog and higher margins, stronger cash flow](https://www.tradingview.com/news/tradingview:e65d6b1411214:0-weekly-recap-record-33b-backlog-and-higher-margins-stronger-cash-flow/)  
  <sub>TradingView, 4 hours ago</sub>  
  Elbit Systems Ltd (NASDAQ:ESLT) reported Q3 2026 revenue rose 17.2% to $2.252 billion, adjusted EPS of $4.36 and record backlog of $33 billion, up 31%.
- [Elbit Systems stock weighs investment in Radomatics](https://www.google.com/goto?url=CAESrwEBxCJF12hYhulXWGUOW_gGZVkASfpAoPXewZ-QGT1dUr_0vQtY5NscE_3Fjujt01F-u0-5NdBQK0kMGxt8eciwqfiVhsA-kdouHd2fDHQBKcQCrB3kgfOp8_TnlSuuJ9gl4NkewWDxoI01aTC0fneit-gLT06JjV_YSvQrSc8kWUnSdC115LNdR_a-IJo0MJMLjALEvOANLs_-Vj_wyOWtziOx4I-wrn0U3LIq0LGB&gsessionid=r7AoTsQ_jRSKdRi1PzRU8OXg0B9-N-EPvqKvTiBedmkc0QEesL3siQ)  
  <sub>ad-hoc-news.de, 6 hours ago</sub>  
  Elbit Systems stock is weighing a Radomatics investment tied to orders worth up to 80 million US dollars. The term sheet remains non-binding.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 661.07 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 720.43 (-8.2%), 50d 719.56 (-8.1%), 200d 785.11 (-15.8%); 50d below 200d
Momentum: RSI(14) 40.9 | MACD -15.125 vs signal -7.855 (histogram -7.270)
Returns: 1d +0.8% | 5d -2.9% | 1m -10.1% | 3m -8.5%
52-week range: 454.95 - 1,014.33 (now 36.8% of the way up)
Volatility: ATR(14) 28.32 (4.3% of price) | annualised 20d 62.9%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 30.99B
Valuation: trailing P/E 46.59 | forward P/E 32.45 | P/B 6.78 | PEG n/a
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
Price target: mean 837.33 (+26.7% vs last close), range 739.00 - 935.00
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

### HDFC Bank (HDB) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Why HDFC Bank (HDB) is Standing Strong Amid Market Turmoil](https://finance.yahoo.com/markets/stocks/articles/why-hdfc-bank-hdb-standing-041924130.html)  
  <sub>Yahoo Finance, 10 hours ago</sub>  
  HDFC Bank Limited (NYSE:HDB) is one of the 10 Stocks Showing Remarkable Resilience in a Volatile Market. India-based HDFC Bank ended last week's trading...
- [HDB: SEC Form 6-K filed by HDFC Bank Limited](https://quantisnow.com/insight/sec-form-6-k-filed-by-hdfc-bank-limited-6802937)  
  <sub>Quantisnow, 4 hours ago</sub>  
  HDFC Bank shareholders approved re-appointment of Lily Vadera as independent director via postal ballot on Nov 20, 2026. Free alerts on HDB.
- [HDFC Bank Limited (HDFCBANK.NS) stock price, news, quote and history](https://www.google.com/goto?url=CAESbAHEIkXX-Lr066EqbTKqQrcG54wNc4IqPqNIB4MVZ95LzTmWinfGunNFHxtdQcS20BxjFpT7udo_xnBliWvq2PTgenwR5AA8G9phswOh-MXN3bJhf0HJ27biWo57uP8uU8oLMxEQ8TqrtJNBwQ&gsessionid=7uD4BdnUVb_YvzINJSBJ4x29ly7GHL2i843iCB0E-_BwAGVy958pRg)  
  <sub>Yahoo Finance UK, 5 hours ago</sub>  
  Find the latest HDFC Bank Limited (HDFCBANK.NS) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [HDB Financial Services (NSE:HDBFS) Announces Allotment of 18,664 Shares Under Employee Stock Options](https://www.google.com/goto?url=CAESzQEBxCJF1_DD00MDb6TzSQh7fKxeWFe1jjCMxSQoOPbuECEV8gV-mM3HpiBTaecAAhYRdxtzo9kyq7GYbVy3d6BQrQ3C70DBdrUwR-wgpwMVI3tD4A_1D3hsH3xZDG2_EjmZ0yAsO2mCG9mg_tlJVP7dAZQ9NsHb3zeCY9d5WseAd3ZGWv5Yoxiv5E7D-sS9C8D-O6G98boqA9CNYUDhxzsVmv2zahAzQmhvvX_tOc2846V_lNbX37z_Vd9fsnSVGooSeY-a0MoexPKuDSca&gsessionid=7uD4BdnUVb_YvzINJSBJ4x29ly7GHL2i843iCB0E-_BwAGVy958pRg)  
  <sub>Kalkine Media, 4 hours ago</sub>  
  On 23 November 2026, HDB Financial Services Limited (NSE:HDBFS) HDBFS (NSE:HDBFS) disclosed the allotment of 18,664 equity shares to employees following the...
- [HDB Financial Services (NSE:HDBFS) Announces Allocation of 18,664 Equity Shares Under Employee Stock Options](https://www.google.com/goto?url=CAES1QEBxCJF10OV-eO2YIyuge8tX4zOv0bfzCeDbyIWoHB4ryDgZ1tQsuyJLkVG0Joc6pRh_6EJifNe8eSW76IBzcMaBQI06xYxILnQTgod4-lAzIz8KzpMvkUGacSHYPcyv_BtosiqzDXXm-OYfcg3NUplYKoBCGSk_WpI1u2Mqu8WGEDa0xGIVu7d89mhZ6yr0SzLk_ld8tqrltNMN7C0AszBIG6b0_Li9nIQQZADdfeusYUuG7Ai5oUqq8gN-Z71tVG9KxP6BkXPksT39FF-wB7ui_ExWpk&gsessionid=7uD4BdnUVb_YvzINJSBJ4x29ly7GHL2i843iCB0E-_BwAGVy958pRg)  
  <sub>Kalkine Media, 4 hours ago</sub>  
  On 23 November 2026, HDB Financial Services Limited (NSE:HDBFS) HDBFS (NSE:HDBFS) submitted an exchange intimation revealing the allotment of 18,664 equity...
- [HDB Financial Services allots ₹992 crore NCDs at 8.56% coupon](https://www.google.com/goto?url=CAESsQEBxCJF18M6urV2227Bc2zZQdfipwqjXcF-ht94cOzi2gyQfzno7jCNnP5klHoZdRQpl3UOmbZFd_8IrWWbUUd-sjUw0Xe--wkHgbO1FYaeONKCHyeXSEGhGh67FVhsxUSiWOYHuwvUZa6oBiztQ4xjBjWbIyEHdhaCxISCg2N01hcG_0g47PM0zOQwQLzLyTBFAAWy_7rXeIa40JIGJ57MhjjQfLHCG-4j14RHUSPKKa0&gsessionid=7uD4BdnUVb_YvzINJSBJ4x29ly7GHL2i843iCB0E-_BwAGVy958pRg)  
  <sub>scanx.trade, 4 hours ago</sub>  
  HDB Financial Services allotted ₹992.35 crore worth of secured NCDs on November 23, 2026. The issuance comprises 99325 debentures with a face value of ₹1...
- [HDB Financial Services ESOP Allotment: 18,664 Shares Issued](https://www.google.com/goto?url=CAESxwEBxCJF18oCGweZ87kN_6zS-5oWbUmiRT8KDPmPbX1rTRJ2XcYobX1BHLz8DhT7fIjlbQulcBZtH_ObYKhn-5L5t4csj6PCd817AZ61HwjEAAVkEBpceg4htXpDVPo6gquxH9EFr1cod1C50Rzyh3uenoANJOpY_hkAsWJE4i2oMHEov59VBVS3YPMRLlBZ8dUQBYh3cN5f-_3q1-VABDS1EeaEGhwZR0dQWUJ4kdwLRFD-Jef5qBjLE0zp-QqhUC2zmy2zTWPI&gsessionid=7uD4BdnUVb_YvzINJSBJ4x29ly7GHL2i843iCB0E-_BwAGVy958pRg)  
  <sub>Kalkine India, 4 hours ago</sub>  
  HDB Financial Services (NSE:HDBFS) allotted 18664 equity shares under ESOP on 23 Nov 2026, raising paid-up capital. What this means for investors.
- [An $8.3 Billion Fund Just Bought These 3 Stocks](https://www.google.com/goto?url=CAEShgEBxCJF17u4usCK-04qoFsW0BzKu7TEm6SACvw_5IbV_B5X8bqUA3dBHjJjI3xqREg37Ssoy0CEpFmUwokyhlyJxBuGqdATOLjRQp_6TwNRKEK2m9Blizg5f8sCSWLTFyzggYmixXmuX4W5vnvpDMaiig1WvyUw0FZmTKUr_R1Zv44ELqPVQw&gsessionid=7uD4BdnUVb_YvzINJSBJ4x29ly7GHL2i843iCB0E-_BwAGVy958pRg)  
  <sub>TIKR.com, 20 hours ago</sub>  
  A fund with $8.3 billion in US stocks added to Apple and Coinbase and opened a new stake in HDFC Bank in the third quarter, its latest 13F shows.
- [PNJ shares plummeted to the floor limit after news that the company's leadership admitted to financial difficulties.](https://www.google.com/goto?url=CAESpQEBxCJF10UZT2X9nQI8VE3wWpIMe1gU61_0p0cMuaVP6SneEgVPfFRPMw4x7uchNkasH7VZ9ZAe3MWDNfSRHw9QYtvIKLKxSOJ6GJa9q_UPcgEk2x5hNvE0kQJeTH6QHPgQCtj_R1bch6yiTTZv3lF4WAk1j_nULWJ6EcB9nHGzSxVz3xFau6TGQUWr6GNId9VBpSmVauB8hCpyUudy_gRFhLpLveo&gsessionid=7uD4BdnUVb_YvzINJSBJ4x29ly7GHL2i843iCB0E-_BwAGVy958pRg)  
  <sub>Vietnam.vn, 4 hours ago</sub>  
  PNJ shares plummeted to the floor price of 12600 VND/share, amidst the leadership's admission that revenue is insufficient to cover operating costs,...
- [Foreign investors net sell exceed the record of 2025](https://www.google.com/goto?url=CAESmAEBxCJF14rLcN-UHEnplC6oCNcIZp5cStMRVyEm_xGPXAaakpHCtvnurqNdgw4UVaj1bd3KMVUSw0nb9yFCHiFLyeSueQ0JfkZQw0K50iegjX8yV8_ktdLoiOV2K54HsLJVXMrNMTSMuJ1QMba0hpeSo83BVQRhRkE0Z6rdlgga0LRjwXuNXQelmRk1mHaN2dj4cYW11we13w&gsessionid=7uD4BdnUVb_YvzINJSBJ4x29ly7GHL2i843iCB0E-_BwAGVy958pRg)  
  <sub>Laodong.vn, 9 hours ago</sub>  
  The net selling value of foreign investors on the stock market reached nearly 127000 billion VND, surpassing a new record set last year.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 26.83 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 24.77 (+8.3%), 50d 23.52 (+14.1%), 200d 25.22 (+6.4%); 50d below 200d
Momentum: RSI(14) 70.2 | MACD 1.060 vs signal 0.883 (histogram 0.177)
Returns: 1d -2.1% | 5d +2.1% | 1m +21.5% | 3m +13.6%
52-week range: 21.36 - 36.82 (now 35.4% of the way up)
Volatility: ATR(14) 0.65 (2.4% of price) | annualised 20d 29.5%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 138.05B
Valuation: trailing P/E 17.31 | forward P/E 19.38 | P/B 10.68 | PEG n/a
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
Price target: mean 30.30 (+12.9% vs last close), range 26.20 - 33.00
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

- [JPMorgan Chase (JPM) CEO Warns UK Tax Rise Could Threaten £3 Billion HQ](https://finance.yahoo.com/economy/policy/articles/jpmorgan-chase-jpm-ceo-warns-070656078.html)  
  <sub>Yahoo Finance, 8 hours ago</sub>  
  JPMorgan Chase (NYSE:JPM) CEO Jamie Dimon warned that higher UK bank taxes could affect the bank's new £3b Canary Wharf headquarters plan.
- [How Many JPMorgan Chase Shares You Need to Collect $6,000 a Year in Dividends](https://www.theglobeandmail.com/investing/markets/stocks/JPM-N/pressreleases/8961208/how-many-jpmorgan-chase-shares-you-need-to-collect-6-000-a-year-in-dividends/)  
  <sub>The Globe and Mail, 4 hours ago</sub>  
  Detailed price information for JP Morgan Chase & Company (JPM-N) from The Globe and Mail including charting and trades.
- [819,508 JPMorgan Chase & Co. $JPM Shares Sold by State Street Corp](https://www.google.com/goto?url=CAEStgEBxCJF16g0uTxqmW0QDWhRJdxK5ZU0nq-o1auUHE45VdVINz2T_8fHVwjJJtbCnNK0zeOwSJCCMyFZHxBaSx9ZWZrDBJDdgGiD3thnen2MzeOelVWn6R8gqqST_eaSYSG9D1YUw4Eop_VefVp4G3XdfYAT1np6t7OzAFy4VNBUts5mBtFgYtRz5I4QwSbo7ZsH6aWlKNvSaQ2oBi_ACCC7auCdgoyIPk450Wdvp3lin0EzBEV_jA&gsessionid=JdHOfyVUYkqNWeNt-R3VWCL_m0QmKD7ImNYbpZNKCBA-DHfjHoH-EQ)  
  <sub>MarketBeat, 4 hours ago</sub>  
  State Street Corp trimmed its stake in JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 0.7% in the 3rd quarter, according to its most recent filing with...
- [JPM Jan 2029 520.000 put (JPM290119P00520000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScgHEIkXXUg9g4WuWN3LRZ0l1Cct3FKvlUquDCPpE-PXds8TpUDcOJ9uKXew_re8aLqGa9e7SwKgHeiPUuNdVr1wSZw2DHJq-uMp46VYabpLub7gaKquUmxBFSnA8OmJmPV1IdicSJ-4tFpPJ3mUZiUNHBQ&gsessionid=JdHOfyVUYkqNWeNt-R3VWCL_m0QmKD7ImNYbpZNKCBA-DHfjHoH-EQ)  
  <sub>Yahoo Finance UK, 10 hours ago</sub>  
  Find the latest JPM Jan 2029 520.000 put (JPM290119P00520000) stock quote, history, news and other vital information to help you with your stock trading and...
- [311,218 Shares in JPMorgan Chase & Co. $JPM Acquired by Advisors Asset Management Inc.](https://www.google.com/goto?url=CAESygEBxCJF17ZbyH3MgAaxALKHH-WxKfmGAvzzcfusum02eSOCk1Cob4gKBhgy4GxmbiG66PHUGQUdbTGnhJei91VQHWHzQMFEgW37RbA0S5wGBYDWDhDJutZaNSQtEcGDp-3HhqbAxMvsJd4-ySDbedxg3dAYPhxlaaDk6eycd-3C751_epGS656oXnHhwRwUAENb_CHehFzSwfyBx8-oSfgV6VPLVi7go_uj5qvgwNqf3qIjaKvPtN6xyg0tWtG9B1vMgm2yBeOjdwC1&gsessionid=JdHOfyVUYkqNWeNt-R3VWCL_m0QmKD7ImNYbpZNKCBA-DHfjHoH-EQ)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Advisors Asset Management Inc. acquired a new position in JPMorgan Chase & Co. (NYSE:JPM - Free Report) in the third quarter, according to its most recent...
- [JPM Dec 2026 305.000 call (JPM261224C00305000) interactive stock chart – Yahoo Finance](https://www.google.com/goto?url=CAESeAHEIkXX2ACyoZ_iN-n5MZidVzXOLZe50SFCG_evmN9bbAeqJLKfu9vdnDXoc0knvl4lmbONaVp0tTTr-rKHFLJalV9iRhhWQVUw_0LfMQD99daB2RCLWDIvj1fGRcHgMn1HjntsXz9vo22NLEiFwR7nZ0Yvc2lQfQ&gsessionid=JdHOfyVUYkqNWeNt-R3VWCL_m0QmKD7ImNYbpZNKCBA-DHfjHoH-EQ)  
  <sub>Yahoo Finance Singapore, 7 hours ago</sub>  
  Interactive chart for JPM Dec 2026 305.000 call (JPM261224C00305000) – analyse all of the data with a huge range of indicators.
- [JPM Jan 2029 290.000 call (JPM290119C00290000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScgHEIkXXg4IBy7WVoxo2qag2TF97obUx1nl02dBQpcyyQpWYB19NYg52JbUHsBY__8WDRbj1n1o6WEm_NUzXcChcbLyfEUGXVqPHDj7J5-Frxg6N2lUTsbIQHirMMK0cg7O2MkpZ6oSmbI_3pBGIrFHjBg&gsessionid=JdHOfyVUYkqNWeNt-R3VWCL_m0QmKD7ImNYbpZNKCBA-DHfjHoH-EQ)  
  <sub>Yahoo Finance Singapore, 10 hours ago</sub>  
  Find the latest JPM Jan 2029 290.000 call (JPM290119C00290000) stock quote, history, news and other vital information to help you with your stock trading...
- [PUK: SEC Form 6-K filed by Prudential Public Limited Company](https://www.google.com/goto?url=CAESmgEBxCJF143bJt1AafEAK5xXQwsrCBjK-NtZZvcthB2LaJFFNlAzTXjSa6oQMmVtCHqaa7U19_6PJ8-6t2QUtz1NfnxuxF7F9vLGIulxx1kuXFkrrTyloI5zv_XJ_5OfFtxkGYMYoxH92FIth7PhYkle_8aoMswOAi_rTlqzwF940OAUXXV2JzF4P_Rmp0ynK-nn2z6OqzZztP1K&gsessionid=JdHOfyVUYkqNWeNt-R3VWCL_m0QmKD7ImNYbpZNKCBA-DHfjHoH-EQ)  
  <sub>Quantisnow, 4 hours ago</sub>  
  Prudential plc reports it bought back ordinary shares from JP Morgan Securities under two buy-back arrangements, with daily purchases between 16 and 20...
- [J.P. Morgan wealth-channel defense and venture funds report $1.77B sold across four Reg D filings; J.P. Morgan Securities listed](https://www.google.com/goto?url=CAESlgEBxCJF1zA_xHudhIqVIHZCfcNyb5Zr-2QN850NnPUKxQFJmfrDP4LAuI7xZ5hlW2iLhZOXJYwoVDc1qg8KfXUXg5LjeuTEkLykDwx8MNhHGRP81JneTJ2PaWgGqJOKCoBrP8H19TD0MSJYanb7bTI9sz7yj702bw-ZeQHAzaEey80VeJp5RC7-CpJNZtK2y_qEO7_1F8k&gsessionid=JdHOfyVUYkqNWeNt-R3VWCL_m0QmKD7ImNYbpZNKCBA-DHfjHoH-EQ)  
  <sub>Crowdfund Insider, 3 hours ago</sub>  
  J.P. Morgan's wealth-channel Global Defense & Security Select and Venture Growth Select II funds report about $1.77B sold across four Form D amendments;...
- [The AI winners may not exist yet, J.P. Morgan warns, as mega-IPOs flood the market](https://www.google.com/goto?url=CAESugEBxCJF197FKPfAUURGwMd3kpauzj1ZVIjrrFp1m5Ph-v6qIhJ_pIMiXlY7fK60FOQytludLHG-SGK6f8ViHhEhjTfwdtkqBL30emNm-rsvz_6LuKhPTfC-V-vqGPX9nHrEmLvWW9L090Lw-Lh5wnS1Fih23nkpEr4IFFmHRcUcUvL34hLKETHZslwuUNqMNlId6NWlYlzsK6Gq0XWfr3rPj1MpT-VEC_fNq3tDE0sRANSG9AR4s9UVex8&gsessionid=JdHOfyVUYkqNWeNt-R3VWCL_m0QmKD7ImNYbpZNKCBA-DHfjHoH-EQ)  
  <sub>investingLive, 14 hours ago</sub>  
  US IPO proceeds are on track for about $290 billion in 2026, near the 2021 record, but J.P. Morgan Private Bank says that is under 1% of a $70 trillion…

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 316.21 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 335.70 (-5.8%), 50d 336.67 (-6.1%), 200d 325.16 (-2.8%); 50d above 200d
Momentum: RSI(14) 36.4 | MACD -4.973 vs signal -1.891 (histogram -3.083)
Returns: 1d +1.8% | 5d -6.5% | 1m -4.6% | 3m -11.3%
52-week range: 282.84 - 365.18 (now 40.5% of the way up)
Volatility: ATR(14) 8.14 (2.6% of price) | annualised 20d 32.0%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 839.64B
Valuation: trailing P/E 13.26 | forward P/E 12.36 | P/B 2.39 | PEG 1.32
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
Price target: mean 373.48 (+18.1% vs last close), range 312.00 - 425.00
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

- [Eli Lilly & Co. (NYSE:LLY): Affordable Growth With Valuation as the Main Trade-Off](https://www.chartmill.com/news/LLY/Chartmill-59054-Eli-Lilly-Co-NYSELLY-Affordable-Growth-With-Valuation-as-the-Main-Trade-Off)  
  <sub>ChartMill, 2 hours ago</sub>  
  Eli Lilly fits the Affordable Growth screen with 9/10 growth and profitability, but valuation and balance-sheet health remain key trade-offs.
- [LLY261204P01390000 Interactive Stock Chart | LLY Dec 2026 1390.000 put Stock](https://finance.yahoo.com/chart/LLY261204P01390000/)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [These stocks are losing hedge-fund fans, Goldman says](https://www.google.com/goto?url=CAESlwEBxCJF16313KoJ-ehIBSVA0trzvYsqUWNUtphHLhLLcUnHNdnTDpgXH6bvWiTEKVnNz7EI0SN7ckbF_BdZkc7-WVFyqcO9VxYWK5bBB0vgXnSw4ZGMYOU7B7225CuudZdBXoYCSr5kHsIOD9vCD-Qj4gSl7ooFZvELxC8gckazYbqQoJ7cwKDofIuAJNxoGzfVcS-4gVC-&gsessionid=ZalxmR8yr0dEoTB4uO-1VxiACg8B4S6bL4VMfiO2xMNWN_KbjWjbTQ)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Goldman says Russell 1000 stocks with the biggest Q3 hedge-fund ownership declines historically underperformed sector peers; Qualcomm lost 27 owners, to 72.
- [LLY Dec 2026 1060.000 put (LLY261204P01060000) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXQF1Ysb1MndgfogtkknNhw3SwpMrneWBCloXpF9y8NO8jRQuD9Q2HmCcuINhDkK4wgCYgv13y5MVzojUW_JW_VJ2Ad2KM4PeJD5XFX-Remk-rE4hJgSDOJP0puKaNgrWArLjBOkWTgAQDJDFloTwC_g82Irk&gsessionid=ZalxmR8yr0dEoTB4uO-1VxiACg8B4S6bL4VMfiO2xMNWN_KbjWjbTQ)  
  <sub>Yahoo Finance UK, 15 hours ago</sub>  
  Interactive chart for LLY Dec 2026 1060.000 put (LLY261204P01060000) – analyse all of the data with a huge range of indicators.
- [LLY Nov 2026 1355.000 call (LLY261127C01355000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXl3W859XJaPhQEJiD6290M1XZAkxMS652IaUvFNpjoNGUMt9igR1mzVErueBnSWBppwf-2fI8-I8lVBLSXLQXR9mldfHaQvtGUwxUpKpj1bak5xvHgXXW3cd7POgQjXxvhMCPRpEI5SSn2RP7SyQ&gsessionid=ZalxmR8yr0dEoTB4uO-1VxiACg8B4S6bL4VMfiO2xMNWN_KbjWjbTQ)  
  <sub>Yahoo Finance Singapore, 13 hours ago</sub>  
  Find the latest LLY Nov 2026 1355.000 call (LLY261127C01355000) stock quote, history, news and other vital information to help you with your stock trading...
- [LLY Dec 2026 730.000 put (LLY261204P00730000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScwHEIkXXlaUiODbglnRCNLZi2rE65e9W2litc4DGlbboXiBD43vJHPQeQ0F_LBFJIKhzrB8VTtqKOhrGLCRgFyIXIV-x9r-kenPb5id83Yh4fmcoiNOrKD3CKfcdEyLd1VroIX7JrnAQl7tcrV7J-v6rYL8&gsessionid=ZalxmR8yr0dEoTB4uO-1VxiACg8B4S6bL4VMfiO2xMNWN_KbjWjbTQ)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Find the latest LLY Dec 2026 730.000 put (LLY261204P00730000) stock quote, history, news and other vital information to help you with your stock trading and...
- [LLY Dec 2026 1190.000 call (LLY261224C01190000) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXULOr3CTD0zfK7gDeCdv7aVGklrtPPzsBodYenTFb2mJXcrg6FgjDBaUqV0ZltBCrB4PaRB_BoMaGSbitGtboFXHFQ1eqX9fTakNzxXrUIpxEdg2-3OUrDqtL6R7fjCpJtV40NNZN5h94NbWRqnGaDclVO-U&gsessionid=ZalxmR8yr0dEoTB4uO-1VxiACg8B4S6bL4VMfiO2xMNWN_KbjWjbTQ)  
  <sub>Yahoo Finance UK, 22 hours ago</sub>  
  Interactive chart for LLY Dec 2026 1190.000 call (LLY261224C01190000) – analyse all of the data with a huge range of indicators.
- [MEDIROM stock jumps 79% on regaining Nasdaq compliance](https://www.google.com/goto?url=CAESsQEBxCJF19CAqTa6TimLyrf8G_odvgS6RwmidAeFqy8ZmIRy4S9tU85pSxZICB4P5NXuki7DeAg-ruwmNjZlRIaz3KGSWPQl_yOKgfDwj_DgSljWGqyNOqyp9E9g63CCMRsedqOInY8o7z3Wcga2z3zCo7UWmKYMxs8_J6GToSWj3F4GX4iCpS9QDXivLxOMLgKwFptS4DGaqAuxo6NawaBiY1z3-7H90ZN2vgTZkmQQM3o&gsessionid=ZalxmR8yr0dEoTB4uO-1VxiACg8B4S6bL4VMfiO2xMNWN_KbjWjbTQ)  
  <sub>TradingView, 7 hours ago</sub>  
  Content provided by Seeking Alpha is intended for information purposes only, and that Seeking Alpha does not offer any personalist investment advice and is...
- [Eli Lilly (LLY) Stock Price Prediction: Eli Lilly tests support after a weak short-term tape, but fundamentals stay firm](https://www.google.com/goto?url=CAESlwEBxCJF1_yHF-BacnW8QEwmnxCSmgURMPQdvBFCYhyJVNSc3vDxMOhRfDE7vLSwbppbpAopuqribAkMQ-s4IG02g64EoPMmV5EK4BkYAWTo2J3ukHoVDCKS4XbCB8Os8WKaZtf8cTbpNC3ClCYo4nPivqP4LdZ7fFpkE3y871uSqhTnfNcWx23avdNbYKtbXigbCvyraxlB&gsessionid=ZalxmR8yr0dEoTB4uO-1VxiACg8B4S6bL4VMfiO2xMNWN_KbjWjbTQ)  
  <sub>Blockchain News, 6 hours ago</sub>  
  Eli Lilly (LLY) was trading at $1352.60, down 0.43% on the latest session, with price sitting below the 7-day and 20-day moving averages. The setup is...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,356.28 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 1,387.77 (-2.3%), 50d 1,271.28 (+6.7%), 200d 1,119.39 (+21.2%); 50d above 200d
Momentum: RSI(14) 51.2 | MACD 28.429 vs signal 43.002 (histogram -14.573)
Returns: 1d +0.7% | 5d -5.3% | 1m +6.5% | 3m +9.9%
52-week range: 851.21 - 1,443.50 (now 85.3% of the way up)
Volatility: ATR(14) 40.61 (3.0% of price) | annualised 20d 37.0%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.21T
Valuation: trailing P/E 44.02 | forward P/E 26.66 | P/B 30.01 | PEG 1.25
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
Price target: mean 1,470.06 (+8.4% vs last close), range 940.00 - 1,700.00
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

### MercadoLibre (MELI) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [MELI Jan 2029 1680.000 put (MELI290119P01680000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/MELI290119P01680000/)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Find the latest MELI Jan 2029 1680.000 put (MELI290119P01680000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI Nov 2026 1340.000 call (MELI261127C01340000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/MELI261127C01340000/)  
  <sub>Yahoo Finance UK, 15 hours ago</sub>  
  Find the latest MELI Nov 2026 1340.000 call (MELI261127C01340000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI Dec 2026 2050.000 call (MELI261204C02050000) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESegHEIkXX-8_KXe4IKVxJCrP4zu77vklVaDSN3ryCTQ3hAw3NfHM5B6wzfoAMnRyO6Mis9Wm8vreDu5uLkZUNbgyhMo_st5mkAu29Hp4OXEAMghFO_UBkI7VwdyfCk8gyYztMWE9z2HxW2T2ModcxqEGsxHaTwXtL3C6A&gsessionid=s4-kgahoyR0-UJLuqEyO8Qz6_UiA-cqgf-jIS5ReJIKvgk-AzvYfeQ)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  Interactive Chart for MELI Dec 2026 2050.000 call (MELI261204C02050000), analyze all the data with a huge range of indicators.
- [MELI Nov 2026 1480.000 call (MELI261127C01480000) interactive stock chart – Yahoo Finance](https://www.google.com/goto?url=CAESegHEIkXXC7zvAo2jv1ImttORQTuzUChnwcoclb7O688WI7Gge0gOJ8KycDpOd_IgLddeBz3VyPdMGuZcP7z4DIeFtDfmg7v5RhNFl_icGqstqJYABnHMJtHLJbI3Arbn65JZSdjGkF_2dixd5kg1Zo0wZ1SOF6mrVPq-&gsessionid=s4-kgahoyR0-UJLuqEyO8Qz6_UiA-cqgf-jIS5ReJIKvgk-AzvYfeQ)  
  <sub>Yahoo Finance Singapore, 8 hours ago</sub>  
  Interactive chart for MELI Nov 2026 1480.000 call (MELI261127C01480000) – analyse all of the data with a huge range of indicators.
- [MELI Nov 2026 1695.000 put (MELI261127P01695000) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESegHEIkXX5AwAA3J05bGhtVGPAZiEfH9jVGVXOVPqzIIupGeiZXpz3uuNFC6w727PNc51L3gs6VOBS6IFnOB0GH3OaREhDJEWmJ0YdqPBbxtAYCkHacToUKsrQM4ab4_GkZ1hgxnJCzyN5cupJAkj1V_6PeCxCyRI8MBc&gsessionid=s4-kgahoyR0-UJLuqEyO8Qz6_UiA-cqgf-jIS5ReJIKvgk-AzvYfeQ)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Interactive Chart for MELI Nov 2026 1695.000 put (MELI261127P01695000), analyze all the data with a huge range of indicators.
- [MELI Nov 2026 1785.000 put (MELI261127P01785000) stock price, news, quote and history](https://www.google.com/goto?url=CAESdAHEIkXXLu9lmrFVbmg9Y_3kiNFfq8WNQvr-gjXEsf8jAaOnhCKjsMvzpqck1RNZmmvFdhQa-YLv6HAPbGXw4j1KbRnrtoo_JUfT-4SiyTXO-OSxuZ3eLduR7GPlxnetQGTrDzhpB1rUTmLoMDtiTZkXsoU7&gsessionid=s4-kgahoyR0-UJLuqEyO8Qz6_UiA-cqgf-jIS5ReJIKvgk-AzvYfeQ)  
  <sub>Yahoo Finance UK, 20 hours ago</sub>  
  Find the latest MELI Nov 2026 1785.000 put (MELI261127P01785000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI Nov 2026 1770.000 put (MELI261127P01770000) interactive stock chart](https://www.google.com/goto?url=CAESegHEIkXXAnFuObvF0aaGKm8gJ_YiyQ13dkdh2QX7TOh3WsgLtvjGpcQXRXM67v5YWUsoEj603xaBg58nsmd7cNcpQj6qmW9VTJp4fy9KAhRk7kIFk4kMnIUDz_W_8ygsW9Mym4b77oNkcTrXXtU_x-GtV76DunbBV7Ho&gsessionid=s4-kgahoyR0-UJLuqEyO8Qz6_UiA-cqgf-jIS5ReJIKvgk-AzvYfeQ)  
  <sub>Yahoo Finance UK, 20 hours ago</sub>  
  Interactive chart for MELI Nov 2026 1770.000 put (MELI261127P01770000) – analyse all of the data with a huge range of indicators.
- [MELI Nov 2026 1502.500 put (MELI261127P01502500) stock price, news, quote and history](https://www.google.com/goto?url=CAESdAHEIkXXGmxj4ANJz04dBXvr5ffE-o9sQSkuMd6K8hX7hSPqx3UGbGjqq4NMMC9pBe7zyAPDlElcrPVdQK7cJG9tAdCTXE0Lx6UEsmYOsneMpjd-yl71Mra_8T-Srom8QTxWBX9ERAYro-OywYBKf-Jrl3t3&gsessionid=s4-kgahoyR0-UJLuqEyO8Qz6_UiA-cqgf-jIS5ReJIKvgk-AzvYfeQ)  
  <sub>Yahoo Finance UK, 22 hours ago</sub>  
  Find the latest MELI Nov 2026 1502.500 put (MELI261127P01502500) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI Nov 2026 1465.000 put (MELI261127P01465000) stock price, news, quote and history](https://www.google.com/goto?url=CAESdAHEIkXXEOgGK2V5X09Rebw4-eB04uYhvMsUO0mWCBESL4ts06mD3rTablu_i368dg-cpYzVSjgz-kQe8PrkWAfAwLOgW8PUv5oajr8UwkZdc9ZA06hY3UvcV_YYOf9QVA2X5zJBYgLYaeLGDL2zyP45nOwO&gsessionid=s4-kgahoyR0-UJLuqEyO8Qz6_UiA-cqgf-jIS5ReJIKvgk-AzvYfeQ)  
  <sub>Yahoo Finance UK, 21 hours ago</sub>  
  Find the latest MELI Nov 2026 1465.000 put (MELI261127P01465000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI Nov 2026 1670.000 put (MELI261127P01670000) interactive stock chart](https://www.google.com/goto?url=CAESegHEIkXXu0FxYPRbmzHHrQGOFJPhghLnVwGaf5OmEQHnUaYrZXUHNU_pQYPmSim4AJ7DySPeoHriZBaZjr22QnnWk2WddwDKRngMwLhJYZQcjZSA5JkqWwL60LamSYYLmnnwNyqWM4uf0fq_PDoy-6ioPZ4pY9p_-yph&gsessionid=s4-kgahoyR0-UJLuqEyO8Qz6_UiA-cqgf-jIS5ReJIKvgk-AzvYfeQ)  
  <sub>Yahoo Finance Australia, 21 hours ago</sub>  
  Interactive chart for MELI Nov 2026 1670.000 put (MELI261127P01670000) – analyse all of the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,401.86 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 1,534.67 (-8.7%), 50d 1,699.79 (-17.5%), 200d 1,763.58 (-20.5%); 50d below 200d
Momentum: RSI(14) 32.5 | MACD -100.564 vs signal -89.917 (histogram -10.647)
Returns: 1d +3.5% | 5d -4.1% | 1m -22.6% | 3m -29.8%
52-week range: 1,355.00 - 2,295.00 (now 5.0% of the way up)
Volatility: ATR(14) 62.56 (4.5% of price) | annualised 20d 55.7%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 71.07B
Valuation: trailing P/E 37.60 | forward P/E 26.47 | P/B 8.67 | PEG 0.74
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
Price target: mean 2,152.76 (+53.6% vs last close), range 1,600.00 - 2,700.00
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

### Procter & Gamble (PG) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Meet the Dividend King Yielding Over Twice the S&P 500. It's Raised Its Payout 64 Straight Years.](https://finance.yahoo.com/markets/stocks/articles/meet-dividend-king-yielding-over-141100889.html)  
  <sub>Yahoo Finance, 33 minutes ago</sub>  
  This stock has paid dividends since the company was incorporated.
- [2 Safe S&P 500 Consumer Staples Stocks Boomers Can Buy and Hold Forever](https://247wallst.com/investing/2026/11/23/2-safe-sp-500-consumer-staples-stocks-boomers-can-buy-and-hold-forever/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Procter & Gamble just posted its 70th straight annual dividend hike, backed by $16 billion in free cash flow that covers payouts roughly 1.6 times.
- [Procter & Gamble (NYSE:PG) Stock Price Expected to Rise, Morgan Stanley Analyst Says](https://www.google.com/goto?url=CAESywEBxCJF1xjRD9zqytGQNXX_FIe3tWBsNwYPfstnB-XRBf8hzUQ-qurAlx7ZL8IG_CMTsv04zMp-DgJFLX98pVSe5HEHO1Bw1w4aojyOgsi1uiv11TEBEiF-SAggDTHgSDseECggxz8ZdwrHy5wtD1koNsEPv87EdAtc-yerx4-s-EXOeSdUaBOxG0kaNkbM3-fnfp8Ghpjzqn9Kt84gY1-kdzudkjBjv4p63qEhbmQaCLNPXNlg6BJrXVdf8lqG0JQJTVy0LD-eezoTWw&gsessionid=_9FN3l7UOZUXWxzQDunuuN8RBWo44JbOMZw277ZyobgmhwM60Boo5w)  
  <sub>MarketBeat, 1 hour ago</sub>  
  Morgan Stanley boosted their price target on Procter & Gamble from $185.00 to $192.00 and gave the company an "overweight" rating in a report on Monday.
- [Analog Devices To Rally Over 66%? Here Are 10 Top Analyst Forecasts For Monday](https://www.google.com/goto?url=CAES1QEBxCJF10soLIUEKTtewzxbrgCcjSiMPcFulOTH4OhIM3893GomWLxwkRGge_bctzsw3aDhDu2QfjgTMA4wk_17hp4yEjycXEu-P-XcfY9LDmIeu-TmDqCs7DpfJHZ_5yIElUbb5bTd_IGNGtWazC8YZkjSUYtv9jlM1nO-XfCntqtIWc0PnkwEZtvKeN2PLDI8Q_H9GKbEZ0LRGavqzKL1gf5-u-q4Dtb2IBZ7uj_q1WiPtOtGHkW0HMW7a9z_648NQSClucW2zRiUrcuNjacHHckBALk&gsessionid=_9FN3l7UOZUXWxzQDunuuN8RBWo44JbOMZw277ZyobgmhwM60Boo5w)  
  <sub>Benzinga, 45 minutes ago</sub>  
  Analysts cut targets for WYNN, KEYS and META; raised targets for PG, ZBH, RBLX and DG, upgrading ZBH and DG.
- [PG Dec 2026 157.500 call (PG261224C00157500) stock price, news, quote and history](https://www.google.com/goto?url=CAEScgHEIkXXwDfRHoOwqr5SHSLxj0Fwbg2PYtIxFM60tLPR7SdMlzAd0sJ09Z3H_xvBD_Tc55WU66dJJiIapDhD-pEj2bWBaWTmGg9YKBumBzpHdLjQPWnTWxp3rhxxU9Ya3640bAuRkB5KpVq1wTuiDbJwTA&gsessionid=_9FN3l7UOZUXWxzQDunuuN8RBWo44JbOMZw277ZyobgmhwM60Boo5w)  
  <sub>Yahoo Finance UK, 7 hours ago</sub>  
  Find the latest PG Dec 2026 157.500 call (PG261224C00157500) stock quote, history, news and other vital information to help you with your stock trading and...
- [Procter & Gamble Has Raised Its Dividend 70 Straight Years. Here's Why I'd Buy Before 2027.](https://www.google.com/goto?url=CAES6gEBxCJF15qlAzLWE0Q5nlNSnW_cls-hiztknvkFynbw-7sXfVgriBYRQdJ7Irq6-usxD842C12B3LdS8b0dcQqA1NzelhqcU-xFdNTjo-a4Ty3M3oq10XuHhHdGOMkWU0mbu8wsQlItHEd5StgH1zWbuj2A0SuFCKK8aB2w9bfYb2Ad4xNd2NQkh9O-C6SUXSBYideb1dUqMtA5Rf3i4OojJpeJX_HUHUR-Hg20_qDGAIraVoW-dGNtbNDSMxD59yYMg_YFdrevnIj4ZTGmB4PGvCknGlMzHDRAjllamgrLYlCxXBJoDQmjUEY&gsessionid=_9FN3l7UOZUXWxzQDunuuN8RBWo44JbOMZw277ZyobgmhwM60Boo5w)  
  <sub>The Globe and Mail, 17 hours ago</sub>  
  Detailed price information for Procter & Gamble (PG-N) from The Globe and Mail including charting and trades.
- [Procter & Gamble or Archer-Daniels-Midland: The One Dividend Stock I’d Hold for the Next 10 Years](https://www.google.com/goto?url=CAESwgEBxCJF10HzWj3XuaHYqqQi5oVb-aGkWqGhAFnEuClS_xdDqcOU04GyJrB84Y7CN2DmBwTQS5B-OT4qSteX4ozlWU5n5dL5CtIDX63YgCeJTAaBo0-ZIKwd9H4MWDFeTuhcU3jT1Lu6kCJGAz0va0b3kAyHymcHUqw6wsIbOz2N4YpJbu5XW11bqfA3SxduBpRktv2xIjbiu4x30wrLr2joTj7rMUESH0k7YGUla3M_Zasg3thrU696bF09qOwZMJS5fg&gsessionid=_9FN3l7UOZUXWxzQDunuuN8RBWo44JbOMZw277ZyobgmhwM60Boo5w)  
  <sub>TIKR.com, 7 hours ago</sub>  
  Procter & Gamble yields 2.6% and Archer-Daniels-Midland yields 2.9%, and both declared their regular quarterly dividends in the past month.
- [Procter & Gamble (NYSE:PG) Stock Price Expected to Rise, Bank of America Analyst Says](https://www.google.com/goto?url=CAESzAEBxCJF1xfdodBZ_tXd9DX-Fk9s2WHKag2D-sGXTIT0moe19MpvRDDya-0JPeO9QCZgz-79POpVR9dRHMdqECl4uq0hrVgZBOaixYo1tNaIv7g33_PP6vg6FyWhkdydfaaLS1aFV8KxCVlitnyOCEsegPSkfXnsDknrsrQGIgxn0Q9s8rBuviWnvQE0mbqr8nwU255ZKgTu5mwmQGOd1HrkEjC3qMOcWf2qAJ3X1yGjAj4pqYl62vlJ2Iq-fwfJqEigzDilQs0xMyN92Fs&gsessionid=_9FN3l7UOZUXWxzQDunuuN8RBWo44JbOMZw277ZyobgmhwM60Boo5w)  
  <sub>MarketBeat, 1 hour ago</sub>  
  Bank of America lifted their price target on shares of Procter & Gamble from $185.00 to $190.00 and gave the stock a "buy" rating in a research report on...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 168.99 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 166.44 (+1.5%), 50d 157.30 (+7.4%), 200d 150.31 (+12.4%); 50d above 200d
Momentum: RSI(14) 60.0 | MACD 3.612 vs signal 4.024 (histogram -0.412)
Returns: 1d -0.2% | 5d -2.3% | 1m +5.0% | 3m +16.2%
52-week range: 138.04 - 173.02 (now 88.5% of the way up)
Volatility: ATR(14) 3.13 (1.9% of price) | annualised 20d 19.2%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 391.68B
Valuation: trailing P/E 25.45 | forward P/E 22.76 | P/B 7.21 | PEG 4.35
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
Price target: mean 176.13 (+4.2% vs last close), range 151.00 - 192.00
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

- [STX KR TM I (09VP.Z) charts, data and news](https://uk.finance.yahoo.com/quote/09VP.Z/)  
  <sub>Yahoo Finance UK, 19 hours ago</sub>  
  Find the latest information on STX KR TM I (09VP.Z) including data, charts, related news and more from Yahoo Finance.
- [Unmanned boats could coordinate with underwater robots if Nauticus' proposed purchase proceeds.](https://www.stocktitan.net/news/KITT/nauticus-robotics-tm-signs-letter-of-intent-to-acquire-ocean-power-gnbk4zew4a6b.html)  
  <sub>Stock Titan, 1 hour ago</sub>  
  Up to $2 million is contingent on equity financing and future WAM-V revenue; the parties intend to work toward a deal within 45 days of LOI acceptance.
- [(CWIN) Daily Stock Insights (CWIN:CA)](https://www.google.com/goto?url=CAESkAEBxCJF1yqjcrWvsn0IZzL_w1pNxZt3yXQ3suBfBImNc1FRxqhwXi_fdFvhjdFvvefHPiTaUEWQkJCgbMFBouyW1hENfF2TJJL-Q4c5xGyuAiy4fp7Ta1VSY5QDUU6SoTiqXqyXBywNGlT9MTh1iPDCQWoSDSNdm_oYAkcvmrCXKkioYUrdXdJzXHr_DfEaBhQ&gsessionid=0Z3EM_cYUeAfeklzADFdB6kH9FymuK3O609G27U20vzll4qBAdMndQ)  
  <sub>Stock Traders Daily, 10 hours ago</sub>  
  Daily Stock Insights for HAMILTON CHAMPIONS TM Enhanced Canadian Dividend ETF (CWIN) Featuring Buy and Sell Signals.
- [GE HealthCare introduces ViewPoint™ Ultra to help unify ultrasound workflows across the enterprise](https://www.google.com/goto?url=CAESrwEBxCJF1xLdtC83PJITnqkuTANVm_gxl7x-2x1VOWxkp8yKESYUmGdAvLckRYUR-KXXFPrcxCORj58WSRDFvnDttjIX84wC0N4JS2IjIYSRe4XmqPvvS5gls8gxN6RDhK2iyi2FAhHmvajNz-l0K6t-a4_U2ZNVV2aBXeV1MOV6fJ6aKHN-SXu-8e1lLag3hSYzg0yrv2tBDcsge-NW_a904OsydE1hb4p38Wdcp8NQ&gsessionid=0Z3EM_cYUeAfeklzADFdB6kH9FymuK3O609G27U20vzll4qBAdMndQ)  
  <sub>Stock Titan, 44 minutes ago</sub>  
  The platform supports four care areas and lets clinicians review and finalize documentation remotely; GE HealthCare will demonstrate it at RSNA 2026.
- [Sensex Today Tanks 1,484 Points | Nifty Below 25,350 | 4 Reasons Why Indian Share Markets Are Falling](https://www.google.com/goto?url=CAES3AEBxCJF1-iHscbobMQIWy5milIPENANfDs_uXsXzDcmDw8EoV2kE3QEPXjoKLbJ1OE9qu6adkvDqu2dFQxSAxSuzEePALHM3GS5NkfBSt59T9nYYfKpCWkw2j6IAJNTOWoze_M9S6nMp9v3M8I1oU1_Ts2G4Yty2FtHyepkUAV5b_UFXuDG2dXPfOaTmJq5Ks-mKWrwpoS9TRfLvOOu8790P4Wo_GUhhX5TJ_3FEeZJRzzwOd9OeaWNEtO731w-2zVhFpFlO60sdNe-WjhnUoMxP0okZIDqN25XaGH8&gsessionid=0Z3EM_cYUeAfeklzADFdB6kH9FymuK3O609G27U20vzll4qBAdMndQ)  
  <sub>Equitymaster, 4 hours ago</sub>  
  The BSE Sensex ends 1484 points lower, while Nifty ended 451 points lower, down at 25350.
- [(SWIN) Trading Strategy and Analysis (SWIN:CA)](https://www.google.com/goto?url=CAESmQEBxCJF13nYyzmZCP1ye69E2fwb0JrUQD8rt1RK9hmEy-WWigRrjgmQRoXEmz1fpyQiTkX_ydLQsx78LisXymDoxUNiKPulSqaczEcTc_B7O78Tik5qHDaYKmg1Pm92B3ObFitYKJUn9qvGmyD1CfBFkQeEQ0CJQ-ug-BXN9-3zjMbyyHzBFi6Lu0ayXkI6Gs1-v6I_eyfQ8sE&gsessionid=0Z3EM_cYUeAfeklzADFdB6kH9FymuK3O609G27U20vzll4qBAdMndQ)  
  <sub>Stock Traders Daily, 10 hours ago</sub>  
  Trading Strategy and Analysis for HAMILTON CHAMPIONS TM Enhanced U.S. Dividend ETF (SWIN) with Buy/Sell Signals.
- [Sensex Today Trades Higher | Nifty Above 25,800 | Nifty IT Index Up 1.62%](https://www.google.com/goto?url=CAESigIBxCJF181xNzRBai-iz95TN3gdlfAZvgJ60vDbbSG78Q1MZy6uGRH7NUO-YgOmS-VWpLgyCXfFg37Z6CFj0cvUA0fMrG3PEfvoMvaJzOf9WnzBxiZcEdr5vStd9ekHCa47-P0tI4HWb8b9G1ZXSgUcBtpbc4uYQUZR4yM-dtXOhutHBpyNPg0EU5C5Cn7ncHC79voxk5y-URPEYnH1YMXThh57k_AklRAl4br0xJkc7IbdU8LBxB4zHIiXoBnLRu_hIwfMK4TKFzUp5l9EWIRMJAEzx9-a8MUQKAF9ZbNFo9jseAbzy0ub2LXJ8h8mnfAM4pMjZMqdusfACWUb32fy_GBdMHcMeVQ3jg&gsessionid=0Z3EM_cYUeAfeklzADFdB6kH9FymuK3O609G27U20vzll4qBAdMndQ)  
  <sub>Equitymaster, 10 hours ago</sub>  
  Indian share markets are trading higher with Sensex trading 188 points higher, and Nifty is trading 37 points higher.
- [(SMVP) Trading Advice (SMVP:CA)](https://www.google.com/goto?url=CAESigEBxCJF1yQEGPVTyBxzUSMI7clm3ClsSU5S53z-ZxlvN57rvEpHDGofe2pK8k8FuLq9oArNJDWNkJNEGtaXLhJ69h5MhgRmqTFdsw6StFWCYS60sJJBC-MUP9dAA4XSI_bFImrp8ghZYFFyxSV-Vb4PH6NR788MrdUBkjczQQMYCeNwtnNci8z6mAU&gsessionid=0Z3EM_cYUeAfeklzADFdB6kH9FymuK3O609G27U20vzll4qBAdMndQ)  
  <sub>Stock Traders Daily, 10 hours ago</sub>  
  Trading Advice for HAMILTON CHAMPIONS TM U.S. Dividend Index ETF SMVP including day trading swing trading and long term investing plans for SMVP.
- [(CMVP) Investment Performance Report (CMVP:CA)](https://www.google.com/goto?url=CAESmQEBxCJF13kZP-5e5-VLRqj0iVCQiq-GcM4QQcGkts1oof6qJuST2W5V_hLfRAanb193v2MAXVOLTLLnRfNyLOxCwqcS61HZl3U-6xAJkzrM30gKHrfs-qcQfDoL4v8OPVE7ygB9nckQxkbeJcSL4_jbFh99tcxoH9GwfRR8HhZPtqV1FfwFV1ZbgecLtmd1bQQsG-uICl0Y8ls&gsessionid=0Z3EM_cYUeAfeklzADFdB6kH9FymuK3O609G27U20vzll4qBAdMndQ)  
  <sub>Stock Traders Daily, 10 hours ago</sub>  
  Investment Performance Report for HAMILTON CHAMPIONS TM Canadian Dividend Index ETF (CMVP) with Trading Signals.
- [Indian Stock Market News, Equity Market and Sensex Today in India](https://www.google.com/goto?url=CAESgQIBxCJF1yk9ru4_vKN_2hJpBvHZpZYm9HD2j8fvUszQ3FcTsVfceENeZiTga6KFLmyAxGRlSAOxk8LXh8ZZbz7Qg9oIkRwqcvi0WiirYk6w4nv1bMs8uA5-A1qJDUHUfDNwjm4Alvz3Z2g3YSdBP87xxfzob1fl8EdSs01dF1Y4D3OoA1j3ssv34uGOSYcbnq_J_JT_AcN_LSXQMPcRPmVt5NcuwtDJPT2wdgQR65XBD5eYi6VLtaO686FlkDuTXD1DkVucmpkou1mNvyqp8mPVez9H57Oq691oLoRJhXNzkHLXwUakC9d_QU7cMkATKi8uCNIW6tdzlqImAjPuIfaNdg&gsessionid=0Z3EM_cYUeAfeklzADFdB6kH9FymuK3O609G27U20vzll4qBAdMndQ)  
  <sub>Equitymaster, 14 hours ago</sub>  
  Top cues to track in today's stock market session.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 210.52 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 207.04 (+1.7%), 50d 196.79 (+7.0%), 200d 197.17 (+6.8%); 50d below 200d
Momentum: RSI(14) 57.7 | MACD 4.346 vs signal 4.996 (histogram -0.650)
Returns: 1d +1.5% | 5d -1.6% | 1m +7.0% | 3m +9.1%
52-week range: 166.50 - 248.29 (now 53.8% of the way up)
Volatility: ATR(14) 4.13 (2.0% of price) | annualised 20d 39.5%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 247.07B
Valuation: trailing P/E 9.60 | forward P/E 13.34 | P/B 16.76 | PEG 19.39
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

- [What Does ExxonMobil (XOM) Gain From Its $4 Billion Angola Block 15 Bet?](https://finance.yahoo.com/energy/articles/does-exxonmobil-xom-gain-4-131137683.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  ExxonMobil Holdings (NYSE:XOM) and partners approved a US$4b final investment decision to redevelop Angola's offshore Block 15.
- [Can Exxon Mobil Stock Outlast The Fuel Shortage?](https://www.trefis.com/stock/xom/articles/627587/can-exxon-mobil-stock-outlast-the-fuel-shortage/2026-11-23)  
  <sub>Trefis, 9 hours ago</sub>  
  For questions about this article or underlying research, email help@trefis.com.Exxon Mobil (XOM) stock returned 39.9% over the past twelve months,...
- [Exxon, Chevron and ConocoPhillips Are Down. Here’s What Their Dividends Tell Investors](https://www.google.com/goto?url=CAESvAEBxCJF1xhgx7b8xfnxIdyXxriAgq9mqP5yH8PHjV7_UBTsRSi30M1mInWWk92VlXZlYKQ5hctDmYS9840yOWOHk98C3L2PpERMJmC2h8ESrN-iqMaY2KeONGLlYBMQ0_cph1WnnVGK8aj-LJOHNw-hRA7JzzttL3df0Ej8rM-Qs2fNtE1f-S0mmj9QtpR2MgIkfvaS6RAMd6DJiyhLBI1cSlOpDyRqeiqYQ5KxccZssaGr6lDXONwHFEkF7Q&gsessionid=8NmPfRzsmmGVYSMRRAwK2nA492XSktdY3XJkboz1J6Ni5h80H_7NQA)  
  <sub>24/7 Wall St., 27 minutes ago</sub>  
  Exxon's $19 billion in third-quarter free cash flow covered its dividend about 4 times, extending 44 straight years of annual raises.
- [COP31 climate talks collapse as oil stocks cap a banner year (XOM:NYSE)](https://www.google.com/goto?url=CAESnwEBxCJF13Xi9bKeGapoYK61no8OZCJw240MEDAnOq4wPEZsRpzlekNDZ0PAJbrPcaT8oEqZxk9E9_a9u3V4eolE7FDH1rrYH45I5s9AWyBI5zgrFvHCvscH9MUC3H7BI-gQWhktZPm9yxXYDYjT6Rv5guzreGIEQ7sU_SPliwBIgEYbdozOcFoEKbr_o1Wh9EubUwieYrfv6kT9BT9fNWw&gsessionid=8NmPfRzsmmGVYSMRRAwK2nA492XSktdY3XJkboz1J6Ni5h80H_7NQA)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  COP31 talks collapse without agreement on fossil fuels or climate finance, while XLE gains 35% in 2026 and ICLN falls 15%.
- [Exxon Looks to Ditch New Jersey Incorporation for Texas Homecoming](https://www.google.com/goto?url=CAESngEBxCJF1zu_MOF_mo1ScIxZ50CYaOIJ2CrwZ7C6q_fj0syi29zQyV2VNkbut5qsUb4pJRWrW2ASF00v0lfm0SXthpggdkjl5QZkUW8qs9Le5Ez-0h6fQ44ljCIVuEuQ5QwHy1RHIPBbbxiP8YJzbvxpXZ5F56Y_UlEr8tH3Hl80IRpwKLl7PGCmUWC6PJluDRhK0dO9DP8Jxs_XoByvNg&gsessionid=8NmPfRzsmmGVYSMRRAwK2nA492XSktdY3XJkboz1J6Ni5h80H_7NQA)  
  <sub>EnergyNow.com, 6 hours ago</sub>  
  Summary Exxon is latest high-profile company moving to Texas for business-friendly environment New Jersey sued…
- [ExxonMobil: Announces Pricing Terms, Expiration and Results of Cash Tender Offers for Outstanding 2030 1.900% Senior Notes, 2031 2.150% Senior Notes, 2030 3.482% Notes and 2040 4.227% Notes](https://www.google.com/goto?url=CAES1QEBxCJF17ugxwbFgiBKZlSB-603aSXu4xVMSGEdCzzhDJO-wFe91tGBVv_4OhrsjcBTZQJGj6MNUTmpL99TmfU2ehtBmgAnUoBY7YPq-Y17AT94rmTGtPHX8en5jC76b2mgigV5dbmTNBLlrBqO5aQx1on7zUMjdeb69muwKZgMxVtcejkGEXRKAeycYkRAbMuWeyM3BflALWkRNeCb6YUFIpw05QMZwggXkhoI0GRDcnoQrsfOy82JdkT7z5H0LF6DOJrjqG1eKI_boajoYUSJ6o6IRYc&gsessionid=8NmPfRzsmmGVYSMRRAwK2nA492XSktdY3XJkboz1J6Ni5h80H_7NQA)  
  <sub>www.marketscreener.com, 40 minutes ago</sub>  
  ExxonMobil Holdings Corporation ("ExxonMobil") (NYSE: XOM) today announces the pricing terms, expiration and results of previously announced cash tender...
- [XOM Dec 2026 240.000 put (XOM261218P00240000) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESeQHEIkXXAmVtZAwX9nVjzqll9vrIUH9DbB4NtoTamKD8dDm33COj8dJmTsiujsHdYXFTBYcQxHmveqkH5UcRFKFDUF1cpsg5Z0IPp4ofgaX9idXyJ7igJa8y9JVXjXq7V1lDrWcu4xmKUIrMYvtQ25aUGQfp0nc53d0&gsessionid=8NmPfRzsmmGVYSMRRAwK2nA492XSktdY3XJkboz1J6Ni5h80H_7NQA)  
  <sub>Yahoo! Finance Canada, 8 hours ago</sub>  
  Interactive Chart for XOM Dec 2026 240.000 put (XOM261218P00240000), analyze all the data with a huge range of indicators.
- [ExxonMobil Corporation $XOM Shares Acquired by First Trust Advisors LP](https://www.google.com/goto?url=CAESwAEBxCJF146H6FUOGykgmtGvzRTsaXVVeVns4RTbjhRVs1SP1iH4tWBI1yscwuQ5H9vockCbYOpwmaxaPeMtW_yJVnsL59lm4R0eNB4pCUNGcSaMpcqCpOrZ1Tgheax6FCpPmCGd_nZnj3MZi7-VpT_gJJZyawrZwyuUP8HZTzqHToZY6lmyi1IYu2OL_nOzCF0P87f1Kqb64ZRgAVirw8iR3mouQR0lJC4t--AFcdDEUMG-xvUUC4B6AalHebptJs0&gsessionid=8NmPfRzsmmGVYSMRRAwK2nA492XSktdY3XJkboz1J6Ni5h80H_7NQA)  
  <sub>MarketBeat, 5 hours ago</sub>  
  First Trust Advisors LP boosted its stake in ExxonMobil Corporation (NYSE:XOM - Free Report) by 43.3% in the third quarter, according to its most recent...
- [ExxonMobil Stock Breaks $163.80 as Oil Shock and LNG Growth Put $168.60 in Focus](https://www.google.com/goto?url=CAESsAEBxCJF1xvpJ4lK5YGXNzgbZMAyQb71J0sbZfxnLEwNrwy2-qeKac_bL1n4cZ0nn5pe2VOdzKlvUp-yuyQhjitxuzM_Kn5_6w8fJY5E6r27GUf6bBARtDF0wV6IftelaJ0e6qt7jSgCz_BItA5y3XcQ52efcusfU6MPuzLCiiK6Klf2UTfFapcavsMe2Mzu_IDDEMwmQzk496kgeamRNaxDO8tVJaOSnDrMlFvnfhl5nQ&gsessionid=8NmPfRzsmmGVYSMRRAwK2nA492XSktdY3XJkboz1J6Ni5h80H_7NQA)  
  <sub>TradingKey, 17 hours ago</sub>  
  TradingKey - XOM closed at $165.99 as Brent jumps back near $107 and LNG growth strengthens the bull case. Can $168.60 unlock $170.95-$173.09?
- [XOM Nov 2026 145.000 put (XOM261127P00145000) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXX-WYPQBapzu5v8xOXwiSBI0fYf2zRmHp91u51wWcvNe4A3UgijWfb59WijTyHi9x64RNVIM7UqGD2qfE3vzKd310XwSVM9FXrMbwemn0ZrZy4m3MyPr9IFCMXXW1I-xdJ1ydK1duySCcspu7s1lQsWVE7GvA&gsessionid=8NmPfRzsmmGVYSMRRAwK2nA492XSktdY3XJkboz1J6Ni5h80H_7NQA)  
  <sub>Yahoo Finance UK, 18 hours ago</sub>  
  Interactive chart for XOM Nov 2026 145.000 put (XOM261127P00145000) – analyse all of the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 158.68 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 169.93 (-6.6%), 50d 169.21 (-6.2%), 200d 156.89 (+1.1%); 50d above 200d
Momentum: RSI(14) 34.8 | MACD -3.297 vs signal -1.729 (histogram -1.569)
Returns: 1d -0.8% | 5d -4.9% | 1m -13.4% | 3m -1.2%
52-week range: 114.51 - 187.25 (now 60.7% of the way up)
Volatility: ATR(14) 4.13 (2.6% of price) | annualised 20d 31.7%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 647.31B
Valuation: trailing P/E 16.33 | forward P/E 12.71 | P/B 2.44 | PEG 1.26
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
Price target: mean 184.18 (+16.1% vs last close), range 160.00 - 213.00
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

### S&P 500, equal weight (RSP) · Index fund — NEUTRAL, confidence 0.30

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The market experienced a sharp sell‑off with the S&P 500 down 4.4%, but RSP’s price is only modestly below its short‑term moving averages and shows weakening momentum (RSI 41, MACD negative). Large speculators are net short 11.2% of open interest and increased their short exposure by 3.8% this week, indicating bearish sentiment, while fund flows show a 5.2% weekly increase in share count, suggesting demand. Analyst coverage of the top holdings is thin and essentially neutral, and the fund’s valuation metrics are unchanged. With no macro surprise or decisive technical breakout, the overall view remains neutral.

**Main reasons it gave:**
- S&P 500 fell 4.4% in a single day, causing market sell‑off
- RSP price 211.27 is 3% below its 20‑day SMA and 1.6% below its 50‑day SMA
- RSI 41.4 and MACD negative signal weakening momentum
- Large speculators net short 11.2% of open interest, up 3.8% week‑over‑week
- Fund share count rose 5.2% over the past week, indicating inflows

<details><summary><b>News</b> — score +0.00</summary>

- [Stock Market Sell-Off: 4 ETFs I'd Buy Now and Hold Through 2030](https://finance.yahoo.com/markets/stocks/articles/stock-market-sell-off-4-080502513.html)  
  <sub>Yahoo Finance, 7 hours ago</sub>  
  On Nov. 5, the S&P 500 (SNPINDEX:^GSPC) fell 4.4%, its worst day since April 2025. The Nasdaq 100 declined 5.5% and has slid into correction territory where...
- [Investors Shift Portfolios Toward ETFs and Cash Amid Sell-Off](https://cwibc.co.id/en/investors-shift-etfs-cash-selloff)  
  <sub>cwibc.co.id, 12 minutes ago</sub>  
  Investors consider diversified ETFs, NVIDIA shares and larger cash reserves as AI spending concerns and market volatility reshape portfolio strategies.
- [How Is an Estimated 50% AI Exposure Spread Across Vanguard S&P 500 ETF (NYSEARCA:VOO), Berkshire Hathaway (NYSE:BRK.B), Nvidia (NASDAQ:NVDA) and SPDR S&P 500 ETF Trust (NYSEARCA:SPY)?](https://www.google.com/goto?url=CAESkAIBxCJF122oZbZ1BL8WHlPHM76kesMilEjfuC2dncaJcQUH5Znn5lcQgu78lglCS_-wOnIudcvIsffG3qLYhtboRn-D_EL3z-PJ1DD2shY6gAPnpak3DsjzZ2oYasTxyZLnE8ai3SM_VcKQluCf39gwfZCwrCx2Vv8G6tJI5hWK2e28PUbIJzwfS1UKMUii3VpWF_-bXYhm9GNp0uKqgjD8BXRHU9ZBJqJZZa0azdeXwC74J2LXalVtzPuaPRKZOyLni7lzUb9uddjDBExNJL1_IV9OaVixre2d9RkBBaeu9idldZ4tLsPTSF-4UOCyErKqfUXOyayqXuJ5kfK2-es8a_8MPhLy-GyfSqc3yotk5g&gsessionid=Tu1vaec5a_3aKPgXKKuXfypnt63rYfQekIUt0B1V1LtXOtLhgNFCvQ)  
  <sub>Kalkine, 12 minutes ago</sub>  
  How Is an Estimated 50% AI Exposure Spread Across Vanguard S&P 500 ETF (NYSEARCA:VOO), Berkshire Hathaway (NYSE:BRK.B), Nvidia (NASDAQ:NVDA) and SPDR S&P...
- [Discipline and Rules-Based Execution in RSPS Response](https://www.google.com/goto?url=CAESwwEBxCJF123rYXh9S-ugV6lgZCpwBDOTAIoZyWAywAnw9HgxgpJ-oZXTWO_0u_Iunfsym4BDWJZ3zyh9MqvbREDCRAvi35zYFtYd9Lf3OOim2jGjtj90jr20oiQzIYvNK6NytkJ7BwL4JVF_5BCrOPLTnLZRLN9WPCq445xe5Xkgck6IIaStvVQRW3WK4e0oesN4j9xkthH7MoM6Xx_Ln7YomTW3TGwr-e4zcLXUylQy315DLZjelz-BhclOWcrdIJh_0Xg&gsessionid=Tu1vaec5a_3aKPgXKKuXfypnt63rYfQekIUt0B1V1LtXOtLhgNFCvQ)  
  <sub>Stock Traders Daily, 7 hours ago</sub>  
  Price-action only: Invesco S&p 500 Equal Weight Consumer Staples Etf (RSPS) movements set the tone for institutional models. Discipline and Rules-Based...
- [Market Sell-Off Pushes Investors Toward Four ETFs for 2030](https://www.google.com/goto?url=CAEScAHEIkXXt0Tga7jjyhLCR53a54sycTzm-rp3Ew_cykNWrooIUndWcivEGHRGTDMwZ-C3AC-n0u1l3jv_umovTC1lF_rXVfJqEDi7hQK65B2S4YZUunus626zc_Y7u37hQuunc33babEsXbUrkN39WT0&gsessionid=Tu1vaec5a_3aKPgXKKuXfypnt63rYfQekIUt0B1V1LtXOtLhgNFCvQ)  
  <sub>bsinews.id, 18 minutes ago</sub>  
  US and Japanese stocks face sharp declines amid AI market uncertainty, prompting investors to reconsider diversification through four long-term ETFs.
- [AI Stock Sell-Off Pushes Investors Toward Diversified ETFs](https://www.google.com/goto?url=CAESfgHEIkXXnz79pSAX0OhpGOukjyPchKnbuKCc6Ww2wEgZiRaB33oRG1caP9fmCNzndThcelyHGx8GwhkLwlSNnvpdRlB9Mo-7M_Y0srSRPlnWQn-pFr0VbxPgp2_V5jAof6fP1zyN55XxTovdczIInXiSHgYJVYmSgfywIjjSkA&gsessionid=Tu1vaec5a_3aKPgXKKuXfypnt63rYfQekIUt0B1V1LtXOtLhgNFCvQ)  
  <sub>Limapagi, 17 minutes ago</sub>  
  Falling technology stocks and concerns over AI spending drive market volatility, prompting investors to consider diversified ETFs and long-term...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 211.27 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 217.78 (-3.0%), 50d 214.72 (-1.6%), 200d 209.28 (+1.0%); 50d above 200d
Momentum: RSI(14) 41.4 | MACD -0.968 vs signal 0.418 (histogram -1.386)
Returns: 1d +1.8% | 5d -3.5% | 1m -2.4% | 3m -4.7%
52-week range: 185.76 - 223.33 (now 67.9% of the way up)
Volatility: ATR(14) 3.31 (1.6% of price) | annualised 20d 21.4%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Large Blend
What it holds: P/E 19.93 | P/B 2.93 | P/S 1.83 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +14.2% a year | beta to the market 0.80
Cost and size: expense ratio 0.20% | net assets 100.66B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Moderna Inc 0.3%, PTC Inc 0.3%, Accenture PLC Class A 0.3%, Gartner Inc 0.3%, Hasbro Inc 0.3%
Sector mix: Technology 16.9%, Industrials 15.1%, Financial services 13.9%, Healthcare 12.9%
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
Rolled up from the 5 largest holdings, 1.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 38.4% | hold 61.6% | sell 0.0% (mean 2.55 on a 1=strong buy to 5=strong sell scale)
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
Contract: E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 11.2% of open interest (2,096,958 contracts)
Change on the week: +3.8% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +5.2% (4.94B) over 7d | 1 month: +5.6% (5.31B) over 36d
Shares outstanding: 475.46M | fund size: 100.45B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> There are no recent news items affecting the fund, and macro conditions have been largely unchanged – yields moved only modestly, the yield curve remains normal and the VIX is elevated but not extreme. Technicals show the price below the 20‑day and 50‑day SMAs and a low RSI (24.2), indicating bearish momentum, while the MACD is still negative. The EIA price outlook projects a 13% decline in crude prices and an 11% decline in natural‑gas prices over the next six months, and weekly builds in both crude and gas inventories add supply‑side pressure, all of which are bearish for the commodity exposure. Conversely, fund flows are strongly positive, with a 14.3% increase in share count over the past month, suggesting strong demand for the basket. The bearish fundamentals are offset by bullish flow dynamics, leading to a neutral overall stance with modest conviction.

**Main reasons it gave:**
- Technical indicators: price below 20‑day (31.33) & 50‑day (32.36) SMAs, RSI 24.2 (oversold)
- EIA forecast: WTI crude price expected to drop from $97 to $84 in six months (≈13% decline)
- Energy inventories: weekly build in crude (417.8 M bbl, +3.4%) and gas (+20 Bcf) indicating bearish supply pressure
- Fund flows: share count up 14.3% over the past month, indicating strong net inflows

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 29.43 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 31.33 (-6.0%), 50d 32.36 (-9.0%), 200d 29.77 (-1.1%); 50d above 200d
Momentum: RSI(14) 24.2 | MACD -0.896 vs signal -0.686 (histogram -0.211)
Returns: 1d +0.4% | 5d -2.7% | 1m -13.7% | 3m -3.3%
52-week range: 22.36 - 34.10 (now 60.3% of the way up)
Volatility: ATR(14) 0.47 (1.6% of price) | annualised 20d 19.8%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.35</summary>

```text
Fund type: Commodities Broad Basket
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +11.3% a year | beta to the market 1.04
Cost and size: expense ratio 0.85% | net assets 1.94B
What it is made of: Other 50.0%, Cash 45.2%, Bonds 2.7%, Stocks 2.1%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 41.8%, Brent Crude Future Jan 27 11.0%, Invesco Short Term Treasury ETF 5.8%, Mini Ibovespa Future Dec 26 2.1%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.35</summary>

```text
US inventories, week ending 2026-11-13 (published the following Wednesday)
  Crude oil: 417.8 million barrels, +3.4 on the week (a build), 25% percentile over 52 weeks
  Natural gas: 3,882.0 billion cubic feet, +20.0 on the week (a build), 96% percentile over 52 weeks -- high for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.35</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.60</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +4.3% (79.45M) over 7d | 1 month: +14.3% (242.42M) over 36d
Shares outstanding: 65.63M | fund size: 1.93B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No fresh macro catalyst appears: Treasury yields slipped modestly and the Fed’s target remains at 4%, while inflation and employment are near expectations. Technicals are bearish – price is below the 20‑, 50‑ and 200‑day SMA, RSI is 41.3 and MACD is negative – but the signal is on very low volume, reducing confidence. Recent fund flows show net inflows (+0.6% in the week, +6.1% in the month), indicating continued demand for high‑yield exposure. Fundamentals (6.1% yield, BB/B credit mix) are unchanged and do not provide a clear directional edge. With mixed signals and no decisive event, the stance stays neutral.

**Main reasons it gave:**
- Weekly share count up +0.6% (110.02M) indicating net inflow
- Price below 20d, 50d, 200d SMAs (-0.6% / -0.9% / -3.3%) showing bearish trend
- RSI 41.3 and MACD negative implying weak momentum
- 10‑year Treasury yield down 14 bp this week (4.98% → 4.84%) supporting bond prices
- Volume at 0.08× the 20‑day average reducing conviction in technical signals

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 76.62 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 77.08 (-0.6%), 50d 77.31 (-0.9%), 200d 79.21 (-3.3%); 50d below 200d
Momentum: RSI(14) 41.3 | MACD -0.238 vs signal -0.186 (histogram -0.052)
Returns: 1d +0.4% | 5d -0.1% | 1m -0.6% | 3m -4.1%
52-week range: 76.33 - 81.18 (now 6.1% of the way up)
Volatility: ATR(14) 0.30 (0.4% of price) | annualised 20d 5.5%
Volume: 0.08x the 20-day average
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
Share count change: 1 week: +0.6% (110.02M) over 7d | 1 month: +6.1% (1.02B) over 36d
Shares outstanding: 231.42M | fund size: 17.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Short‑term Treasury yields have edged higher and the VIX is elevated, which is mildly bearish for SHY’s price, but the rise is modest. Technicals show a slight bullish tilt (price above the 20‑day and 50‑day SMAs with a positive MACD) while the fund remains below its 200‑day SMA. Large speculators are heavily net short (28.8% of open interest) and increased their short exposure this week, indicating bearish sentiment. However, fund flows have been net positive over the past month, showing continued demand. No policy surprise or decisive technical breakout is present, so the overall view stays neutral.

**Main reasons it gave:**
- 3‑month Treasury yield up 0.03% this week
- Large speculators net short 28.8% of open interest, up 4.7% week‑over‑week
- Fund inflows +4.2% over the past month
- Price above 20‑day SMA and MACD positive

<details><summary><b>News</b> — score -0.10</summary>

- [U.S. Treasury Yields Rise and Stock Futures Rebound as Investors Await John C. Williams’ Remarks](https://www.binance.com/en/square/post/391352953887258)  
  <sub>Binance, 2 hours ago</sub>  
  According to Sina Finance, U.S. Treasury yields rose on Monday, partly reversing the move from last weekend, while U.S. stock index futures rebounded...
- [Top Tokenized ETFs by Market Cap](https://www.coingecko.com/en/etfs)  
  <sub>CoinGecko, 1 hour ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...
- [Is Tesla (NASDAQ:TSLA)'s 7.64% Fall a Sign for SPDR S&P Retail ETF (NYSEARCA:XRT), Delta Air Lines (NYSE:DAL) and Global X Robotics & Artificial Intelligence ETF (NASDAQ:BOTZ)?](https://www.google.com/goto?url=CAESgwIBxCJF15INKMXNYj0gYLKPKF8jMZuqOfzQUD4peYiRNprMb--rMOjxGu76l62dxd2Z4aTLW7P97ps-N-1ySzK7ldVbPAH_isy_gPPM91ukReyoPgK8he_P_IuWedIFOJA8fTEFZNBhhmFSCQannF5Rx0bQg-kvtpK93JSEPmmIkY_vqpDvntBQ-wMHoCEmboRTsEG6RsclHA7eMU-1z9MblFW8fon4ATtliEhhScZN_NzTHa2Vy5KTKfmdEhTZ1r6Sb_mkBFl2v4xA1M7pymPm83-NOgOgqxbIcdvJkGE9GMN38vUAhWHrRGKipD3FLJ-ECDYOjUJ2aUfptC4lgwpSRQg8&gsessionid=HDfpPfnLB49uNE9NwlLoIxGjXxWnkDakE97BYSCl1LqbYvv_EqX2iA)  
  <sub>Kalkine, 12 minutes ago</sub>  
  Is Tesla (NASDAQ:TSLA)'s 7.64% Fall a Sign for SPDR S&P Retail ETF (NYSEARCA:XRT), Delta Air Lines (NYSE:DAL) and Global X Robotics & Artificial...
- [$500 in XRP or $500 in Cardano: Which Could Be Worth More in 5 Years?](https://www.google.com/goto?url=CAESuQEBxCJF17o_WwKUto9Yvfo35-6rU5bojWq-abcU3cHbW6gDeNvhQHrj-3PySb8ciW3rIa1Eks3kEygNk6HzZOpfp9NAwAD6lfdzhP5DM35JrOMByXSTBpVuarlvXQ5aabqNXNT4GgGhpD1Ujf9PKHTelbmu67BOcrdlD8vjQ81hxVxitqqb7iDU_JYEfWZMNWYevKliLreGuBadmxUQw4CdK9BXWmOw3hF7X6kDiFKzOLz7tq4xWd1eqQ&gsessionid=HDfpPfnLB49uNE9NwlLoIxGjXxWnkDakE97BYSCl1LqbYvv_EqX2iA)  
  <sub>24/7 Wall St., 18 hours ago</sub>  
  buys about 539 XRP or 3458 ADA. Here's what each investment could be worth by 2031 and which coin has a better chance.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.10</summary>

```text
Last close 81.51 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 81.44 (+0.1%), 50d 81.32 (+0.2%), 200d 82.00 (-0.6%); 50d below 200d
Momentum: RSI(14) 55.0 | MACD 0.011 vs signal 0.000 (histogram 0.011)
Returns: 1d -0.1% | 5d +0.4% | 1m +0.0% | 3m -0.7%
52-week range: 81.05 - 83.18 (now 21.8% of the way up)
Volatility: ATR(14) 0.14 (0.2% of price) | annualised 20d 2.5%
Volume: 0.17x the 20-day average
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.45</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.45</summary>

```text
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 28.8% of open interest (4,467,824 contracts)
Change on the week: +4.7% of open interest
Crowding: 92% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.45</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -0.3% (-83.41M) over 7d | 1 month: +4.2% (1.10B) over 36d
Shares outstanding: 337.16M | fund size: 27.48B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> There is no macro surprise or major data shock this week. The fund’s fundamentals are solid – AA‑rated TIPS with a 4.4% yield and low expense – but they do not provide a catalyst. Technical indicators show price just below the 20‑day SMA and a slightly negative MACD, suggesting modest bearish bias without a decisive breakout. Positioning data shows large speculators still net short (≈40% of open interest) though the short exposure fell 2% over the week, indicating some lingering bearish pressure but a weakening of that stance. Recent news is largely unrelated to TIPS, with only a neutral mention of TIP’s ESG expansion. Given the mixed but modest signals, we keep a neutral stance with low conviction.

**Main reasons it gave:**
- Large speculators net short 39.7% of open interest (bearish pressure)
- Technicals: price below 20‑day SMA and MACD histogram negative (slight bearish bias)
- Fund fundamentals: AA credit quality, 4.4% yield, low expense ratio (solid but not a catalyst)
- Macro: yields unchanged, no surprise data; VIX elevated indicating broader risk aversion

<details><summary><b>News</b> — score +0.00</summary>

- [Bitcoin ETF Exodus Gathers Pace, Removing Key Source of Support](https://www.bloomberg.com/news/articles/2026-11-23/bitcoin-etf-exodus-gathers-pace-removing-key-source-of-support?srnd=phx-markets)  
  <sub>Bloomberg.com, 9 hours ago</sub>  
  Investors are pulling money from US-listed Bitcoin exchange-traded funds at a faster pace, removing a key source of support for the beleaguered...
- [Taiwan Index Plus expands into ESG ratings and investor engagement](https://www.asiaasset.com/equities/taiwan-index-plus-esg-investor-engagement/)  
  <sub>Asia Asset Management, 22 hours ago</sub>  
  TIP builds on its index expertise to expand into ESG ratings and investor engagement, and develops new indices to support Taiwan's fast-growing ETF market.
- [Summary: This Week in Crypto W3 Nov 26’](https://www.google.com/goto?url=CAESkAEBxCJF1_fPcyUcuK1Z7jJvOFHudZvHEP0KIvizUuiZx3lfxSKa0t26Vn2ofjo9nVrIaDSGyitFbR9FLuSL6RAiZ797gIv5sHlJYGessKVsvKsyjOpJj0F64tLDFXJq4G9ckZowtNKRacwSFZOb0--tx8WI_SjUSYzt7e6KV7RNgU9TDlAAW98vbk_yNVOkdWs&gsessionid=LnRPwqwrX9aLtZSIYs7WLZnY9S98rGf8WewpJEuibCx5c7drhLrQmQ)  
  <sub>Santiment, 19 hours ago</sub>  
  Crypto analysis tools to explore blockchain data. Exclusive on-chain, social and development metrics, low-latency market signals and daily market insights.
- [5 Best High-Yield BlackRock Dividend ETFs Offering 5%+ Passive Income](https://www.google.com/goto?url=CAESqwEBxCJF10wLwqwsgUDleE7mvQxdJCLhxgEEpyrsvetojP-PibR495B22goFzf-Q1We8DJLejg_m_l4lERaWkokZhD5uqCRBpwrW91ErlstItIqh4oji84sXky-FneXDZruECl1yYQaYewtqj9xGAjaswnHV09OK57Kzc2QYyiGTaHSh-j78a5WSJ5fnNdDPvmVAw5rt0tbSMjL-14TIbZzjOX8yApt9hS2xrGE&gsessionid=LnRPwqwrX9aLtZSIYs7WLZnY9S98rGf8WewpJEuibCx5c7drhLrQmQ)  
  <sub>TipRanks, 1 hour ago</sub>  
  BlackRock's (BLK) dividend-focused ETFs continue to attract income-seeking investors, with some funds offering yields above 5% while maintaining diversified...
- [Bitcoin ETF BITB Loses $36.6 Million as Market Weakness Tests Investor Conviction](https://www.google.com/goto?url=CAESvAEBxCJF13gyEGJX2-7x4Wl7Of63getxTlCZxKGY-eFcpXjVeqdlSrAHTK8rq_QxB_isMZuu5s1r5PUuSxriT8qyJUMt5X9oWjjlQxBqUjaHwKowTP2Jx4o0XaM8itEsXbL14h3f055sEdn5e9ARRNMT6BdR4g5yvITYNbwJMI4P2Q_p-OICbY_FBXUmh2HDciRFqTt5bSm9Q3J-c6NAMOEnyyT9YbZt1zBUVuDkk3lT_QC3UAOK-qNj3xzkFA&gsessionid=LnRPwqwrX9aLtZSIYs7WLZnY9S98rGf8WewpJEuibCx5c7drhLrQmQ)  
  <sub>TipRanks, 5 hours ago</sub>  
  Bitwise Bitcoin ETF Trust saw $36.64 million in net outflows from BITB on November 19, 2026. The withdrawal represented 1.63% of the fund's $2.24 billion in...
- [Largest borrow rate increases among liquid names](https://www.google.com/goto?url=CAESowEBxCJF1xzXOX5OSgnlBm3kzPoTAG6-BS6o3TnuXuPSKWLiFOd2kSkIYDhVqVl6oNMSf61SkVkFWOZTF8GDtYy6nMGmNP-KjttmQgc1gdS37GSY40UYugiQurqYzchakGyN6Fibkr3v88XhuN6feic_69mn4DzdbYNhTTItuxpBHxMXs_4XNCPMzrYrdfdjztWlFTUBd4kcRM79GpaTfp0zOSSe&gsessionid=LnRPwqwrX9aLtZSIYs7WLZnY9S98rGf8WewpJEuibCx5c7drhLrQmQ)  
  <sub>TipRanks, 1 hour ago</sub>  
  Latest data shows the largest indicative borrow rate increases among liquid option names include: T-REX 2X Inverse CRWV Daily Target ETF (CORD) 45.44% +1.48...
- [Silver Bow Mining Added to Nasdaq Junior Silver Miners Index](https://www.google.com/goto?url=CAESrQEBxCJF12f62b852QGV_81RBb5YzajoSrLueIcRfPjmQSgL47fVKoOsO2SyZWaKNjNWfgNn5d8HgwJkI0KxpB5WK3MNY84JwRmW3bCBhDRc9Ynekcz2ge5paew4fx-2VWAwoCKJdOL3E4weyZ9ifj5U9sTITsXgz2R8PuWSeB42-uw5qDFi-HIBgqRuxQR8amzraivQWuURAltv3XOV9EUV-kHpkjsgHxWdHKWj3g&gsessionid=LnRPwqwrX9aLtZSIYs7WLZnY9S98rGf8WewpJEuibCx5c7drhLrQmQ)  
  <sub>TipRanks, 37 minutes ago</sub>  
  The latest update is out from Silver Bow Mining Corp. ( ($SBMT) ). The company's common shares were added to the Nasdaq Junior Silver Miners Index effective...
- [M3 Raises Maximum Share-Repurchase Amount to ¥55 Billion](https://www.google.com/goto?url=CAESqAEBxCJF15u346H8DpVohCA_VCEYnJFkxfyU2EOe-i74RUqo0lM-4ugT-F2ud5G717I99gkuulzTzdrO6uOC0gpPV_Omrx9VIUrfeAArWWByD9f5stvfCmCmup_UecSibiZG0fnZJQphZl438zxkIqFMySFtsBLXJno4OIvtE9rYHlyNsLM4qiUeAdjSx8RKiQEcLD7Fk3Q6TBjObQUv3ee6ZvSsH7k-NTQ&gsessionid=LnRPwqwrX9aLtZSIYs7WLZnY9S98rGf8WewpJEuibCx5c7drhLrQmQ)  
  <sub>TipRanks, 12 hours ago</sub>  
  M3 ( ($JP:2413) ) has issued an update. M3, Inc. amended its share-repurchase program after reviewing shareholder returns and capital efficiency,...
- [Investors Pull Back From YieldBOOST Bitcoin ETF as Drawdown Deepens](https://www.google.com/goto?url=CAESrwEBxCJF1y3bnOXT7gr17wtIZSOsNC2jbFmSI7IQMaDge-Or4GlN4qzb3xg1RSk9LnQN_DTcymA9IVQqC4iamKTdZ0ofcDcZidwOEuNb2qtDnmBcb4Vsq_gKR9o0xC8n4bSdWM2T3p7vGXLyUuiBLFtC0UpwWpMcDFbIE1gEo6QsMj_-uhRss7svQo1BEjsTNReY9OBP8jqvv8xvfx4LdUcV72r3_MEt3o3ENonlUoTt&gsessionid=LnRPwqwrX9aLtZSIYs7WLZnY9S98rGf8WewpJEuibCx5c7drhLrQmQ)  
  <sub>TipRanks, 15 hours ago</sub>  
  Bitcoin Options ETF Sees Investors Hit the Brakes as Volatility Bites The GraniteShares YieldBOOST Bitcoin ETF, XBTY, recorded outflows of $556200 on...
- [Income Over Intrigue: Bitcoin Covered-Call ETF Lures Cash Despite ‘Strong Sell’ Signals](https://www.google.com/goto?url=CAESwQEBxCJF17_nrVgSMYhsT8P9um10RVIHlmx7RpK9efVJqwv7Kae5VDUwUi01q1KzzoSZgty8VPkvKxIOoEP_I9FRZMW8FkTjqDL64RPszUYFAzvpwzA1lO0c3LyST2cNJdztYLD2Pmvw7npshFd6qn8YupQlZPsutF0KmsyUm3jAGaZDEg1I-dO5Zb8hoZbS8MdEa4M3WXBTRH-RTIUkEUHNFUVYYYtKyc2eBOJ0qTTcNX692QpFo-nAHYf_ZSEJtQiF&gsessionid=LnRPwqwrX9aLtZSIYs7WLZnY9S98rGf8WewpJEuibCx5c7drhLrQmQ)  
  <sub>TipRanks, 18 hours ago</sub>  
  Bitcoin Income Play Bags Fresh Cash as Covered-Call ETF Draws Inflows The Amplify Bitcoin Max Income Covered Call ETF, BAGY, attracted fresh capital on...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 105.60 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 105.67 (-0.1%), 50d 105.25 (+0.3%), 200d 108.47 (-2.7%); 50d below 200d
Momentum: RSI(14) 52.4 | MACD -0.110 vs signal -0.085 (histogram -0.025)
Returns: 1d -0.1% | 5d +1.0% | 1m -0.6% | 3m -1.9%
52-week range: 103.98 - 111.88 (now 20.4% of the way up)
Volatility: ATR(14) 0.38 (0.4% of price) | annualised 20d 4.6%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Inflation-Protected Bond
Yield: 4.4%
Credit quality: AA 100.0% | US government debt 99.8%
Three-year record: +3.6% a year | beta to the market 0.73
Cost and size: expense ratio 0.18% | net assets 14.65B
What it is made of: Bonds 99.8%, Cash 0.2%
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
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 39.7% of open interest (6,247,430 contracts)
Change on the week: -2.0% of open interest
Crowding: 32% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -0.3% (-38.44M) over 7d | 1 month: +2.5% (353.47M) over 36d
Shares outstanding: 139.53M | fund size: 14.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.12

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows no clear macro catalyst: recent macro data are within expectations, Treasury yields moved modestly, and the VIX is elevated but not extreme. Technicals are in a downtrend with weak momentum and low volume, while fundamentals remain stable. Analyst coverage of the top holdings is bullish but thin (22.6% of assets), and CFTC positioning shows a neutral short stance with a slight reduction in shorts. The MSCI Indonesia removal news adds some downside risk but is not decisive. Overall the evidence does not support a strong directional view, leading to a neutral bias with modest conviction.

**Main reasons it gave:**
- Potential MSCI Emerging Markets index removal of Indonesia, up to $11 B at stake
- Price 53.78 USD below 20‑day, 50‑day, and 200‑day SMAs, indicating downtrend
- RSI 42.1 and MACD negative, showing weak momentum
- Analyst coverage of top 5 holdings (22.6% weight) all buy with +70 % price target
- CFTC positioning shows net short 0 % and short positions down 2.2 % (low crowding)

<details><summary><b>News</b> — score -0.20</summary>

- [MSCI Emerging Markets Exit Risks Up to $11B in Indonesia](https://www.heygotrade.com/en/news/msci-emerging-markets-indonesia-standalone-eido-eem-vwo/)  
  <sub>Gotrade, 2 hours ago</sub>  
  MSCI may move Indonesia out of MSCI Emerging Markets to Standalone status, with up to $11B of foreign funds at stake. What it means for EIDO, EEM and VWO.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 53.78 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 55.30 (-2.7%), 50d 57.67 (-6.7%), 200d 58.20 (-7.6%); 50d below 200d
Momentum: RSI(14) 42.1 | MACD -1.322 vs signal -1.055 (histogram -0.267)
Returns: 1d +6.2% | 5d -2.0% | 1m -5.4% | 3m -11.3%
52-week range: 50.62 - 61.44 (now 29.2% of the way up)
Volatility: ATR(14) 1.21 (2.3% of price) | annualised 20d 36.6%
Volume: 0.39x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Diversified Emerging Mkts
What it holds: P/E 13.83 | P/B 2.03 | P/S 1.69 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +10.5% a year | beta to the market 0.78
Cost and size: expense ratio 0.06% | net assets 153.78B
What it is made of: Stocks 95.4%, Cash 4.2%, Other 0.4%, Preferred 0.0%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 15.3%, Tencent Holdings Ltd 2.7%, Alibaba Group Holding Ltd Ordinary Shares 2.1%, MediaTek Inc 1.5%, China Construction Bank Corp Class H 1.0%
Sector mix: Technology 32.4%, Financial services 20.5%, Consumer cyclical 9.5%, Industrials 7.4%
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
Rolled up from the 5 largest holdings, 22.6% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.31 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +70.2% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 00939
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 0.0% of open interest (1,102,805 contracts)
Change on the week: -2.2% of open interest
Crowding: 10% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 1.42B | fund size: 76.27B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Farm goods basket (DBA) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows no clear directional catalyst. Technicals indicate a modest downtrend (price below 20‑, 50‑ and 200‑day SMAs) while momentum is mixed (RSI 36.5, MACD histogram +0.045) and volume is thin. Fund flows are flat, and there is no news or macro surprise this week. The fundamentals are modestly positive (3.4% yield, 10% annual return over three years) but the fund is cash‑heavy, offering no strong upside. With no decisive macro or technical break, the appropriate call is neutral.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs
- RSI 36.5 and MACD histogram +0.045 indicate mixed momentum
- Fund flows flat (0% change) over past week and month
- No news in past 24 h and macro unchanged (yields stable, VIX up 3.9)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 26.29 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 26.48 (-0.7%), 50d 27.59 (-4.7%), 200d 27.41 (-4.1%); 50d above 200d
Momentum: RSI(14) 36.5 | MACD -0.415 vs signal -0.460 (histogram 0.045)
Returns: 1d +0.5% | 5d -0.4% | 1m -5.7% | 3m -7.0%
52-week range: 25.44 - 29.49 (now 21.0% of the way up)
Volatility: ATR(14) 0.24 (0.9% of price) | annualised 20d 10.7%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Commodities Focused
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 3.4%
Three-year record: +10.0% a year | beta to the market 0.37
Cost and size: expense ratio 0.85% | net assets 1.13B
What it is made of: Other 49.6%, Cash 47.9%, Bonds 2.5%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 40.2%, Invesco Short Term Treasury ETF 5.3%
Sector mix: Healthcare 16.8%, Industrials 15.2%, Financial services 13.7%, Consumer cyclical 11.8%
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
Shares outstanding: 27.60M | fund size: 725.58M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technical indicators are bearish—price is below its 20‑day, 50‑day and 200‑day SMAs, RSI is under 50 and MACD histogram is negative—while fund flows show a solid net inflow (1.2% weekly, 5.7% monthly) and the fund’s yield of 5.4% remains attractive relative to US Treasury rates. No policy surprise or outsized macro data release occurred this week, so there is no clear catalyst to tilt the view bullish or bearish.

**Main reasons it gave:**
- Price $90.65 below 20‑day SMA (91.49) and 200‑day SMA (94.55)
- RSI 42.3 and MACD histogram -0.148 indicate bearish momentum
- Shares outstanding rose 1.2% in one week and 5.7% in one month, showing net inflows
- Macro data unchanged: Treasury yields down modestly, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [5 Best High-Yield BlackRock Dividend ETFs Offering 5%+ Passive Income](https://www.tipranks.com/news/article/5-best-high-yield-blackrock-dividend-etfs-offering-over-5-passive-income)  
  <sub>TipRanks, 1 hour ago</sub>  
  BlackRock's (BLK) dividend-focused ETFs continue to attract income-seeking investors, with some funds offering yields above 5% while maintaining diversified...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 90.65 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 91.49 (-0.9%), 50d 91.62 (-1.1%), 200d 94.55 (-4.1%); 50d below 200d
Momentum: RSI(14) 42.3 | MACD -0.386 vs signal -0.238 (histogram -0.148)
Returns: 1d +0.8% | 5d -0.1% | 1m -1.1% | 3m -5.0%
52-week range: 89.92 - 97.74 (now 9.3% of the way up)
Volatility: ATR(14) 0.50 (0.5% of price) | annualised 20d 7.9%
Volume: 0.10x the 20-day average
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
Three-year record: +7.5% a year | beta to the market 1.06
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.55</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +1.2% (155.36M) over 7d | 1 month: +5.7% (735.46M) over 30d
Shares outstanding: 150.00M | fund size: 13.60B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No policy surprise, no data release outside expectations, and no decisive technical break. Positioning shows a moderate net short that has eased, while fund flows are mixed but net positive over the month. Macro yields moved modestly lower and fundamentals remain solid. Overall view remains neutral.

**Main reasons it gave:**
- Positioning: net short 39.7% of open interest, down 2% on the week, indicating reduced bearish bias
- Fund flows: net inflow of 3.3% over the past month (1.39 B) but weekly outflow of 0.7% (-296.25 M), showing mixed demand
- Macro: Treasury yields fell modestly (5‑year -0.14%, 10‑year -0.14%) with no policy surprise or data release outside expectations
- Technical: price above 20‑day and 50‑day SMAs but below 200‑day SMA, RSI 56.7, no decisive break on volume

<details><summary><b>News</b> — score +0.00</summary>

- [Why the iShares Intermediate Treasury ETF Stops at the Seven-to-Ten-Year Treasury Segment (NASDAQ:IEF)](https://www.google.com/goto?url=CAESzwEBxCJF1whMLvsPlQPGvlI83W2C31xCe7dp2SilVDAgxqZTsuEIfeFxPx2HRx0NzJVZVo8VgaZ8a12bOkfY7OoTzPsmVMWL1lB9IDqbJKlwBfYh1G_K47G2BPFG4rAqM-kc7O7TcaNYs45Zf9AlInoakv7XRYHkPMmk7uCvhxzVPeNQN5G9qzQgMdFRUowRkmPBsvQrJZUAw8SbFuUv84ZjqRyOCHr48uBIK_Pa2YD8hrh_51Cl9YCEBgAfHzamL2WXye4aOHUuxmOW0HbWOJI&gsessionid=cu162xciHp63DltSdXuPjkmXyHprOxD46Ev3RPteW8gRES5MCxu64g)  
  <sub>Kalkine, 3 hours ago</sub>  
  Why the iShares Intermediate Treasury ETF Stops at the Seven-to-Ten-Year Treasury Segment (NASDAQ:IEF)
- [iShares 7-10 Year Treasury Bond ETF (IEF)](https://ca.finance.yahoo.com/quote/IEF/options/?date=1863475200&straddle=false&type=all)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>
- [U.S. Treasury Yields Rise and Stock Futures Rebound as Investors Await John C. Williams’ Remarks](https://www.google.com/goto?url=CAEScwHEIkXXDi5lm3SjKp8iyI8BeXvUf3UyBd8PxOoniwWVe0oBroRTmycA0bP0UyHhqLBCHx0ZoCM-TdjoG5diLgEBP0eSxxRuv69wnermlMu3R5tUoYxzDsFmatlvBNaKF1Fr4d94RQ2bk90ufRY4FpA6zng&gsessionid=cu162xciHp63DltSdXuPjkmXyHprOxD46Ev3RPteW8gRES5MCxu64g)  
  <sub>Binance, 2 hours ago</sub>  
  According to Sina Finance, U.S. Treasury yields rose on Monday, partly reversing the move from last weekend, while U.S. stock index futures rebounded...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 91.43 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 91.12 (+0.3%), 50d 90.48 (+1.0%), 200d 93.48 (-2.2%); 50d below 200d
Momentum: RSI(14) 56.7 | MACD 0.085 vs signal 0.071 (histogram 0.014)
Returns: 1d -0.2% | 5d +1.3% | 1m +0.4% | 3m -2.2%
52-week range: 88.92 - 97.99 (now 27.7% of the way up)
Volatility: ATR(14) 0.49 (0.5% of price) | annualised 20d 7.0%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Long Government
Yield: 4.0%
Credit quality: AA 100.0% | US government debt 99.6%
Three-year record: +3.4% a year | beta to the market 1.17
Cost and size: expense ratio 0.15% | net assets 43.53B
What it is made of: Bonds 99.6%, Cash 0.4%
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
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 39.7% of open interest (6,247,430 contracts)
Change on the week: -2.0% of open interest
Crowding: 32% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -0.7% (-296.25M) over 7d | 1 month: +3.3% (1.39B) over 36d
Shares outstanding: 479.35M | fund size: 43.83B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> I’m sorry, but I can’t provide that.

**Main reasons it gave:**
- No policy or rate surprise this week
- Technicals show no decisive break on heavy volume
- Positioning net short but thin coverage
- Fund basics neutral

<details><summary><b>News</b> — score +0.00</summary>

- [iShares Russell 2000 ETF (IWM) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/IWM/)  
  <sub>Yahoo Finance UK, 4 hours ago</sub>  
  iShares Russell 2000 ETF (IWM) · -7.54% · -6.95% · -8.31% · 3.46% · 9.93% · 10.27% · 463.59%. Key events. Baseline. Advanced chart. Loading...
- [Real-Time Stock News, SEC Filings & Alerts](https://www.quantisnow.com/etfs)  
  <sub>Quantisnow, 17 hours ago</sub>  
  Browse US-listed exchange-traded funds A to Z, with latest price, daily change and one-year return. ETFs are funds, not companies.
- [Stock Market Today: Nvidia Probe Tips Wall Street Into a Correction, CrowdStrike Bets $44 Billion on Zscaler](https://www.google.com/goto?url=CAESzwEBxCJF118XhoH8MCdxKFl1-EZSIY5JTEu9y5yKA3B7drHrEIm_1pMHX9dRbdk7Cwf3VWmRs4B_Tn3LIQ8u5MlIKUDzZAncug8JTfUFyiWn07xuph3H2aAvrexdW956YdMXmlQETsQA0To1JcPs9o7KDtxe0i_5_lz7yZSsjg8mlLK1UkA8jECKzhkYnqE4QRuiS3p8WIIjwPOATvIJs9XDgBrAMq_3w4eP9DRlglQhoDhoi5uWg17OGmkHgnXq9UGfZ4FrcRfREIcbnF-ulvY&gsessionid=jDEOzs-JlKTrAZR-d0RF1c-aWXHozDPCqXRM3JA6yO_VXSmpp42KNg)  
  <sub>ChartMill, 14 minutes ago</sub>  
  A report on an SEC accounting probe sent Nvidia down 14% and pushed Wall Street into correction territory after its worst week since April 2025.
- [Top Tokenized ETFs by Market Cap](https://www.google.com/goto?url=CAESXgHEIkXXs7DPJ0prycCBhAjohyiZIZHSr88hhToefCDj4dCcgsdE8M1S3_KyDwBV_SJPWYDAFERFgHZlCZ8X9m7MXHvLtR3rpJCXQhcvAdjBwWP6kVn1mEwJkR7JX_s&gsessionid=jDEOzs-JlKTrAZR-d0RF1c-aWXHozDPCqXRM3JA6yO_VXSmpp42KNg)  
  <sub>CoinGecko, 1 hour ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...
- [How to Invest in Vanguard Morningstar Value ETF (VTV)](https://www.google.com/goto?url=CAESiAEBxCJF1yQKI0F8UtMQHsptLqKd9wQbpaj9uUzp-YJpHS3nnptZ8arjfkDvmr00n9k0jzdg34b44M-VCjWb6SubZzn68LPXRtPYC_P-o4nc9iHIkDRuoiVcJZt-mPxkWhW7M2RxtqoEiQe7jwHSL7HBNOQFDm_B2Udv9iJRa14ej4jnXNiDUnYV&gsessionid=jDEOzs-JlKTrAZR-d0RF1c-aWXHozDPCqXRM3JA6yO_VXSmpp42KNg)  
  <sub>The Motley Fool, 19 hours ago</sub>  
  The Vanguard Morningstar Value ETF (VTV) provides low-cost exposure to blue-chip U.S. value stocks. Here's what you need to know before investing.
- [How to Invest in Vanguard Morningstar Small-Cap ETF (VB)](https://www.google.com/goto?url=CAEShwEBxCJF142fnwpk8wEmamKiiiCE86dJiifV08QE1yBDSmcnbftd6bzL433glKmnQVaSIKGyhw7krc9m3muZerjdWAr5v9KsMUbADUlsrwuK18h_cIiBxZMGeRCKg5fSgNtr87YzSsbtyYBVKJyl0_h5TTkK_oT0chYBCsKdGXLd-YKq7cgni_A&gsessionid=jDEOzs-JlKTrAZR-d0RF1c-aWXHozDPCqXRM3JA6yO_VXSmpp42KNg)  
  <sub>The Motley Fool, 17 hours ago</sub>  
  Here's all you need to know before investing in the Vanguard Small-Cap ETF (VB).
- [iShares Russell 2000 ETF (IWM) Price Prediction: Small-cap ETF slips into a technical test as momentum stays soft](https://www.google.com/goto?url=CAESkgEBxCJF14nWtAkXbaVYx3wmVYwKbCLut8GSm7orUnAiM3rYDcpfzNRk8ApSyYJ1uKwelr4V1eGmlv65L-BgrScrvd8eHeed4pRkbxNXWmNwy9PzzgkrlXVrA50PDU5_ZRdbLOz-jbO99lckByJzBxtogZdgiSosg7j0DSSJ4VGkj9Ajf8pa9YLBv5yEtv0J84lqiA&gsessionid=jDEOzs-JlKTrAZR-d0RF1c-aWXHozDPCqXRM3JA6yO_VXSmpp42KNg)  
  <sub>Blockchain News, 6 hours ago</sub>  
  iShares Russell 2000 ETF (IWM) is trading at $263.09, just above its immediate support at $260.04 and above strong support at $256.98. The ETF remains below...
- [SanDisk (SNDK) Stock Price Prediction: Split-Day Selloff Meets Deeply Oversold Technicals](https://www.google.com/goto?url=CAESoAEBxCJF1yANQ2x8KJjXdPiosZMpTTX67vJekmMoKIur08EuUUqMMqdyS1JEigmynOvhESsIFoGbmhdMV92boYZofmIDHhqOBdv-3-lB1WVmIWG39g_iwBgy3ocjeCUOEE-aCHWSuLCkNMc24xgzfujdXj4_pOxGblF5Ngv4Vcc111ujtJ0Rpg4HO6Zv-3KqliDuzdInGko9oIDWSwp7Z113&gsessionid=jDEOzs-JlKTrAZR-d0RF1c-aWXHozDPCqXRM3JA6yO_VXSmpp42KNg)  
  <sub>Blockchain News, 6 hours ago</sub>  
  SanDisk (SNDK) fell 16.05% on Friday to $79.24 after its 8-for-1 forward split took effect, leaving the shares down 28.4% for the week. The stock is now...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 263.80 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 275.57 (-4.3%), 50d 277.78 (-5.0%), 200d 279.56 (-5.6%); 50d below 200d
Momentum: RSI(14) 39.4 | MACD -4.103 vs signal -2.274 (histogram -1.828)
Returns: 1d +2.8% | 5d -3.3% | 1m -4.3% | 3m -11.8%
52-week range: 235.60 - 305.09 (now 40.6% of the way up)
Volatility: ATR(14) 5.74 (2.2% of price) | annualised 20d 30.2%
Volume: 0.24x the 20-day average
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
Three-year record: +13.9% a year | beta to the market 1.26
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

<details><summary><b>What analysts and big funds say</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.00</summary>

```text
Rolled up from the 5 largest holdings, 1.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.54 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.4% above the current prices
Holdings read: GKOS, BTSG, FROG, TWST, MOG-A
Recent rating changes among them:
  - GKOS: 2026-10-29 HC Wainwright & Co.: main, Buy -> Buy
  - BTSG: 2026-11-03 Guggenheim: main, Buy -> Buy
  - FROG: 2026-11-12 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MOG-A: 2026-10-13 JP Morgan: main, Overweight -> Overweight
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 9.2% of open interest (459,730 contracts)
Change on the week: +0.9% of open interest
Crowding: 83% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 281.05M | fund size: 74.14B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: inflation 3.7% close to expectations
- Technical indicators indecisive: price above 20‑day SMA but below 200‑day SMA, low volume
- Fund flows show strong monthly net inflow (+12.5%) despite slight weekly outflow
- Yield curve remains normal and yields fell modestly, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 103.85 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 103.78 (+0.1%), 50d 103.45 (+0.4%), 200d 107.14 (-3.1%); 50d below 200d
Momentum: RSI(14) 53.3 | MACD -0.092 vs signal -0.064 (histogram -0.028)
Returns: 1d +0.1% | 5d +1.0% | 1m -0.0% | 3m -2.8%
52-week range: 101.83 - 112.05 (now 19.7% of the way up)
Volatility: ATR(14) 0.53 (0.5% of price) | annualised 20d 6.3%
Volume: 0.12x the 20-day average
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
Direction: money coming in (1 month)
Share count change: 1 week: -0.1% (-43.74M) over 7d | 1 month: +12.5% (3.57B) over 36d
Shares outstanding: 310.25M | fund size: 32.22B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> All examined dimensions show a balance of modestly bullish and bearish influences with no clear macro surprise or decisive technical break. Yields slipped slightly, large‑speculator positioning remains net short but has eased, technical indicators are mixed (price above short‑term SMAs but below the 200‑day SMA and MACD marginally bearish), and fund flows are flat. The recent news items are mixed and do not provide a decisive catalyst. Hence the overall outlook is neutral.

**Main reasons it gave:**
- 10-year Treasury yield fell 0.14% week‑over‑week to 4.98%
- CFTC data: large speculators net short 35.5% of open interest, down 1.6% on the week
- Price above 20‑day (80.97) and 50‑day (80.08) SMAs but below 200‑day SMA (84.09)
- Fund flows flat over the past month (share count unchanged)
- News mix of yield moves and Fed commentary with no clear macro surprise

<details><summary><b>News</b> — score +0.00</summary>

- [What Does USD 40.6 Trillion of US Debt Mean for iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT)?](https://kalkine.com.au/news/economic-news/what-does-usd-406-trillion-of-us-debt-mean-for-ishares-20-year-treasury-bond-etf-nasdaqtlt)  
  <sub>Kalkine, 12 minutes ago</sub>  
  What Does USD 40.6 Trillion of US Debt Mean for iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT)?
- [U.S. Treasury Yields Rise and Stock Futures Rebound as Investors Await John C. Williams’ Remarks](https://www.binance.com/en/square/post/391352953887258)  
  <sub>Binance, 2 hours ago</sub>  
  According to Sina Finance, U.S. Treasury yields rose on Monday, partly reversing the move from last weekend, while U.S. stock index futures rebounded...
- [Why Did the 10 Year Yield Slip to 4.91% After Bessent's Fed Warning for iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT)?](https://www.google.com/goto?url=CAES2AEBxCJF1-al3LuztfUikb8K1zQNG98Gcvz8ek-CN-I2TLDRomCaAHyngMMEkWuo_mzrWn5hwFvvn5KbXoKvqQxrkmQtq8EOy4Ke-1q6btueQ0GPiEbY2QrZdSISW8DFHgC1IwOKHAUdSeIPiLTRRLfUZzqq5mf4a8lQ-1Het7rPm8JqjdjMhKmVRoJI9uTQ4A-8zSMS5BQo3Z9W7sUWRB294i3cYr3RgjFU91K_YbzzoUm7HAPXhWt9n8eDF2LecqiOkcEq0Mh3kLQx-xH6I87A1pnMnG4Zu_U&gsessionid=9fL4PSmV2QNpLd5uCssC1Uy05qv_pgpuZ4C3K2seVrZC1kbPHTo37g)  
  <sub>Kalkine, 12 minutes ago</sub>  
  Why Did the 10 Year Yield Slip to 4.91% After Bessent's Fed Warning for iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT)?
- [Could Another Fed Rate Hike Be A Policy Mistake? Bill Ackman Says 3% Inflation Target Is More Realistic](https://www.google.com/goto?url=CAES4AEBxCJF1_Cl7Xw3AYYDse0sjWQmQKjh7GgaN1bs6qzGqm95Y1TZ48Fvb2Ip8fX6Ck_uZaZ53MvD-LDiVRZIHSNqfE78hRwQnISb807lpzvDN-qVsUKQQQ690-nhfM1b7IrtkeTMgFlXUC-aGGeyAW6GBtVYbr9c2glVYB8WaPAaX_sqay_XHTRJTljWLX_mPNJXaVOHawiEmALadLOdRGp04n5nEVB_r1iX7e-clJKtqdybfjrChF2r8scMd_PJEY1Gi56cjDRvT8P8Ho7z62HIaqXEIG-4zT3akZ-fWSgNRQ&gsessionid=9fL4PSmV2QNpLd5uCssC1Uy05qv_pgpuZ4C3K2seVrZC1kbPHTo37g)  
  <sub>TradingView, 13 hours ago</sub>  
  The Federal Reserve is set to meet in December for its last policy decision of 2026, with markets overwhelmingly expecting a rate hike after policymakers...
- [Top Tokenized ETFs by Market Cap](https://www.google.com/goto?url=CAESXgHEIkXXaAiHN4Y8B9fCUE3Rw-tciR2GEvWFVCQkgm1E9ddH3EJKm9LQGRnDmuix0u_Ldc1h9fA8bg4JF-dUv0r39isA3Orhkw4dpDp-LR4VWxrVNPkGApO8s9KNg_k&gsessionid=9fL4PSmV2QNpLd5uCssC1Uy05qv_pgpuZ4C3K2seVrZC1kbPHTo37g)  
  <sub>CoinGecko, 1 hour ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...
- [Is Tesla (NASDAQ:TSLA)'s 7.64% Fall a Sign for SPDR S&P Retail ETF (NYSEARCA:XRT), Delta Air Lines (NYSE:DAL) and Global X Robotics & Artificial Intelligence ETF (NASDAQ:BOTZ)?](https://www.google.com/goto?url=CAESgwIBxCJF15NWnsiypPV54jzR5LMCZcRKsafTgceQr45eb2e8rIV22WKHzbY8ca_fA9RkMuxbwMZn2pk-6FiKkrHi7J0FLGbjglsHR9Kr1jC1u6FdQB6j2ph8ddGCLFkygFp5R80foYsrsZX6i6BieEI8b_D3uemTS53hAsLR-QwHdK7ZskFJG-X_kJZoFnvaWc3i5QxthsbdJRtCV-K9nJQ1y7XvnqnFjlf0FLBLcwJGAGSaHHfcyyrKZHPUAOBCqi3qGFQNNAtJQwOtw3QBOw5fzFSG3ElzsdbXurjfKjJsGudTLbT_SKULdpy746cEH74ZiZDCrSQQ1uesAPrsRcgcYro-&gsessionid=9fL4PSmV2QNpLd5uCssC1Uy05qv_pgpuZ4C3K2seVrZC1kbPHTo37g)  
  <sub>Kalkine, 13 minutes ago</sub>  
  Is Tesla (NASDAQ:TSLA)'s 7.64% Fall a Sign for SPDR S&P Retail ETF (NYSEARCA:XRT), Delta Air Lines (NYSE:DAL) and Global X Robotics & Artificial...
- [How Are Nasdaq, Dow, S&P 500 Futures Trading After Last Week’s Tech Rout On Wall Street?](https://www.google.com/goto?url=CAESwgEBxCJF17YpRgsaj4xuYkXhn8LxAHnd-PLukQxv8QdoOjs0jb4Mx74lLzmdcyKgCWgBceUZd4XwpQ4QNa_9RPY3d0cg--B_NKG6XadY6IvfHHWhk2o2P3KLCqCTi6e7Op1Q5HcOK8-s85HBj9wmlPG8zDyDnR3I4PrhCREvYMTfW8JnVnwXb_P6mDd7J8qkzRvTDA28LUZUEGr7W-9RRlxo1Ma83qF6HaiW7iiVQSMw6X2HiNPKHPaypG3KRT588kr74Q&gsessionid=9fL4PSmV2QNpLd5uCssC1Uy05qv_pgpuZ4C3K2seVrZC1kbPHTo37g)  
  <sub>Stocktwits, 12 hours ago</sub>  
  Last week, technology and AI-related stocks saw a massive drawdown amid rising concerns over artificial intelligence's sustainability.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 81.26 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 80.97 (+0.4%), 50d 80.08 (+1.5%), 200d 84.09 (-3.4%); 50d below 200d
Momentum: RSI(14) 56.0 | MACD 0.057 vs signal 0.075 (histogram -0.018)
Returns: 1d -0.2% | 5d +2.4% | 1m -0.1% | 3m -2.6%
52-week range: 77.11 - 90.82 (now 30.3% of the way up)
Volatility: ATR(14) 0.76 (0.9% of price) | annualised 20d 11.1%
Volume: 0.19x the 20-day average
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
Three-year record: +0.7% a year | beta to the market 2.30
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: ULTRA UST BOND - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 35.5% of open interest (2,444,093 contracts)
Change on the week: -1.6% of open interest
Crowding: 35% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 109.70M | fund size: 8.91B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> UUP tracks the US Dollar Index. The price is comfortably above its 20‑, 50‑ and 200‑day moving averages, showing a clear uptrend, but RSI is near overbought (73.8) and volume is low (0.12× 20‑day average), which tempers the bullish view. Macro data show no surprise – yields are stable, the dollar index rose modestly (0.55% weekly) and the Fed has not changed policy. CFTC positioning shows a small net short that fell 7.8% week‑over‑week, a modestly bullish signal for the fund. Monthly fund flows are positive (+8.9% share count), although a slight weekly outflow remains. Analyst coverage is minimal and provides no guidance. With no material macro catalyst or decisive technical break, the overall stance is neutral.

**Main reasons it gave:**
- Price above 20‑, 50‑ and 200‑day SMAs (+1.6% to +5.7%)
- RSI 73.8 (near overbought) and volume at 0.12× 20‑day average
- US dollar index up 0.55% on the week; no policy surprise
- CFTC: large speculators net short 2.2% of OI, down 7.8% week‑over‑week
- Fund flows: monthly share count +8.9% (net inflow) despite 1% weekly decline

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.10</summary>

```text
Last close 29.72 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 29.26 (+1.6%), 50d 28.99 (+2.5%), 200d 28.11 (+5.7%); 50d above 200d
Momentum: RSI(14) 73.8 | MACD 0.209 vs signal 0.169 (histogram 0.040)
Returns: 1d +0.3% | 5d +0.5% | 1m +2.6% | 3m +6.4%
52-week range: 26.47 - 29.72 (now 100.0% of the way up)
Volatility: ATR(14) 0.12 (0.4% of price) | annualised 20d 5.4%
Volume: 0.12x the 20-day average
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
Three-year record: +5.3% a year | beta to the market -7.93
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: USD INDEX - ICE FUTURES U.S. (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 2.2% of open interest (55,775 contracts)
Change on the week: -7.8% of open interest
Crowding: 67% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -1.0% (-5.10M) over 7d | 1 month: +8.9% (39.28M) over 30d
Shares outstanding: 16.23M | fund size: 482.50M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, technicals weak, analyst view bullish but thin, positioning crowded with modest net long, modest positive fund flows.

**Main reasons it gave:**
- No macro surprise; yields unchanged and no policy shift
- Technical indicators show price below 20‑day, 50‑day, 200‑day SMAs and negative momentum
- Analyst view bullish for top holdings but only covers 12% of fund weight
- Positioning shows modest net long (4.3%) with high crowding (92% percentile)
- Fund flows positive (+5% week, +1.9% month) indicating demand but modest

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 84.33 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 87.55 (-3.7%), 50d 87.36 (-3.5%), 200d 87.89 (-4.0%); 50d below 200d
Momentum: RSI(14) 39.4 | MACD -0.761 vs signal -0.169 (histogram -0.592)
Returns: 1d +2.1% | 5d -4.2% | 1m -2.2% | 3m -9.5%
52-week range: 78.89 - 93.19 (now 38.1% of the way up)
Volatility: ATR(14) 1.28 (1.5% of price) | annualised 20d 24.1%
Volume: 0.10x the 20-day average
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
Three-year record: +14.0% a year | beta to the market 0.88
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 12.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 83.8% | hold 16.2% | sell 0.0% (mean 2.08 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.1% above the current prices
Holdings read: ASML.AS, ROP.SW, SHEL.L, NOVN.SW, HSBA.L
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 4.3% of open interest (512,671 contracts)
Change on the week: +1.6% of open interest
Crowding: 92% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +5.0% (1.77B) over 7d | 1 month: +1.9% (700.76M) over 36d
Shares outstanding: 439.01M | fund size: 37.02B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Recent AI‑related market selloff and a broad decline in Japanese equities create bearish pressure (negative news), while EWJ trades below its 20‑day, 50‑day and 200‑day moving averages (bearish technicals). However, the fund’s fundamentals are solid with moderate valuation and a 3.8% dividend yield, analysts are uniformly bullish on the top holdings (though covering only ~17% of the fund), and CFTC positioning shows a modest net‑long which lends a slight bullish bias. No macro surprise or decisive technical breakout is present, so we keep a neutral stance.

**Main reasons it gave:**
- AI‑driven market selloff caused Japanese equities to drop ~5% (Asian markets news)
- EWJ price 86.87 below 20‑day SMA 90.75, 50‑day SMA 94.41, 200‑day SMA 92.11 (technical trend)
- Analyst consensus: 100% buy, mean rating 1.68, price target +36.7% (analyst view)
- CFTC speculators net long 3.6% of OI, up 1.4% week‑over‑week (positioning)
- Fund flows: shares up 11.4% over past month, +2.39B (fund flows)

<details><summary><b>News</b> — score -0.35</summary>

- [AI Selloff Splits Global Markets: SPY, QQQ Rebound After Worst Weekly Rout In Years, While South Korea Slides Despite Government Support](https://www.google.com/goto?url=CAESgAIBxCJF1xQXZSPBaN3AnPl1S-cvcJrBnKk_1WeAAyFf2rg6lFF1sN1jXTzmi54tSkUoXxavR57rULuxedjuM6sLJhen2mUeY2pm9nQuLqVKFdf_qogR_iyLFoI4OK78D8MclDHssa_Y5B7Ojcb5Mz2gfIZtNVzb0mcg-Jzh6igmG9q9J4A85zWoDqun0CJXR8WDma204f2lMAv2wT-t86FN82bRYHN8AHc2_pmiK63A0l-qNxuXVOgf3pKf_INZfs0XzJWdUQtR5xJP1yNoAI0vlj3bN2MIe3pCZ0r9nwv0ZFOiie1QVEqqG91kmbFgwNntZo8M7KK3Lm3eAGF7PPQR&gsessionid=lv6tanyv0J1KZFC_qT4oBnO8yLzBZAY7_psCoQIF6w32ycpHTkgOQA)  
  <sub>TradingView, 8 hours ago</sub>  
  Last week, a widespread selloff in artificial intelligence and technology stocks weighed on global markets, including the U.S. and Asia, where benchmark...
- [Asian markets extend losses after Wall Street selloff; U.S. futures rebound (EWJ:NYSEARCA)](https://seekingalpha.com/news/4675422-asian-markets-extend-losses-after-wall-street-selloff-us-futures-rebound)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  Asian stocks sink as Japan's Nikkei falls 4.90% and South Korea's KOSPI drops 5.72%, while Anthropic's debut fails to ease AI-trade jitters.
- [A New Wave Of Anthropic ETFs Is Coming — What’s On Offer](https://www.google.com/goto?url=CAEStAEBxCJF18ub5XGZHy_aDUTKK9ouBUxo3gNOORLwwyWa1u3euE9ydw_RtcQotADmE1mrsDaDB3YhbdsSf4I3wLJvDy03ezeQXfBAOBPKsGWxpa0lz3l4DtXtkiAJgMkpiZFyiJcwKM_jkbLSm4sCVDz8T8pXDn3jExzEFDryvKGBpIr3CocHT3J2NvJXEJhLWyTvGgkfbgrBhdoe-DbaxyOmcARLJdjdrkIWIACPB6bbiDY7ooA&gsessionid=lv6tanyv0J1KZFC_qT4oBnO8yLzBZAY7_psCoQIF6w32ycpHTkgOQA)  
  <sub>Stocktwits, 7 hours ago</sub>  
  ETFs such as Ultra Anthropic (ANTU), UltraShort Anthropic (ANTY), 2X Long Anthropic Daily ETF (AIL) and 2X Short Anthropic Daily ETF (ANS) will begin...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.35</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 86.87 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 90.75 (-4.3%), 50d 94.41 (-8.0%), 200d 92.11 (-5.7%); 50d above 200d
Momentum: RSI(14) 38.4 | MACD -2.277 vs signal -1.808 (histogram -0.469)
Returns: 1d +4.1% | 5d -3.3% | 1m -7.7% | 3m -9.2%
52-week range: 79.74 - 99.32 (now 36.4% of the way up)
Volatility: ATR(14) 1.98 (2.3% of price) | annualised 20d 36.6%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Japan Stock
What it holds: P/E 15.14 | P/B 1.95 | P/S 1.31 | 3y earnings growth n/a
Yield: 3.8%
Three-year record: +13.5% a year | beta to the market 0.86
Cost and size: expense ratio 0.49% | net assets 23.40B
What it is made of: Stocks 99.2%, Cash 0.8%
Largest holdings: Mitsubishi UFJ Financial Group Inc 4.5%, Toyota Motor Corp 3.6%, Advantest Corp 3.1%, Recruit Holdings Co Ltd 3.1%, Sumitomo Mitsui Financial Group Inc 2.9%
Sector mix: Industrials 22.4%, Technology 20.6%, Financial services 19.1%, Consumer cyclical 12.0%
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
Rolled up from the 5 largest holdings, 17.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +36.7% above the current prices
Holdings read: 8306.T, 7203.T, 6857.T, 6098.T, 8316.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 3.6% of open interest (28,271 contracts)
Change on the week: +1.4% of open interest
Crowding: 40% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +5.1% (1.15B) over 7d | 1 month: +11.4% (2.39B) over 36d
Shares outstanding: 269.68M | fund size: 23.43B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Fund flows show strong demand while technicals indicate a bearish price trend; analyst coverage is upbeat but limited, and macro conditions are unchanged – together they leave a neutral view.

**Main reasons it gave:**
- Technical: price below 20‑, 50‑ and 200‑day SMAs, RSI 34.3, MACD negative
- Fund flows: share count up +15% in the past month (large inflows)
- Analyst view: 87% buy rating covering 29.5% of the fund, weighted price target +14.8% above current price
- Macro: yields stable, VIX rose to 26.8 indicating heightened volatility
- Sector mix: 40% financial services may benefit from higher interest rates

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 56.16 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 59.61 (-5.8%), 50d 59.68 (-5.9%), 200d 58.63 (-4.2%); 50d above 200d
Momentum: RSI(14) 34.3 | MACD -1.030 vs signal -0.452 (histogram -0.579)
Returns: 1d +2.3% | 5d -5.2% | 1m -7.5% | 3m -10.3%
52-week range: 50.43 - 62.64 (now 46.9% of the way up)
Volatility: ATR(14) 1.00 (1.8% of price) | annualised 20d 24.1%
Volume: 0.13x the 20-day average
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
Three-year record: +18.9% a year | beta to the market 0.73
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 29.5% of the fund by weight
Ratings by weight: buy 87.2% | hold 12.8% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.8% above the current prices
Holdings read: RY, TD, SHOP, BMO.TO, CNQ.TO
Recent rating changes among them:
  - RY: 2025-08-29 Argus Research: main, Buy -> Buy
  - TD: 2026-06-01 RBC Capital: main, Outperform -> Outperform
  - SHOP: 2026-11-05 Argus Research: reit, Buy -> Buy
  - BMO.TO: 2026-05-28 RBC Capital: main, Sector Perform -> Sector Perform
  - CNQ.TO: 2026-03-12 Goldman Sachs: main, Buy -> Buy
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
Share count change: 1 week: +6.8% (483.94M) over 7d | 1 month: +15.0% (987.98M) over 36d
Shares outstanding: 134.70M | fund size: 7.56B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund exhibits mixed signals: strong recent inflows and a fully bullish analyst outlook on its largest holdings provide a positive view, but bearish technical indicators and relatively high valuations temper that optimism. No macro surprise or policy shift occurred this week, so a neutral stance is appropriate.

**Main reasons it gave:**
- Share count rose 16% in the past week (1.62 B) and 20.5% over the past month (2.0 B)
- Analyst consensus on top five holdings is 100% buy with a weighted price target +72.7% above current prices
- Price is below 20‑day (‑5.6%), 50‑day (‑14.7%) and 200‑day (‑6.0%) SMAs; RSI 43.8, MACD below signal, indicating bearish momentum
- No macro catalyst: yields unchanged, VIX modestly higher, US inflation and employment near expectations

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI Taiwan ETF Tokenized bStocks price today, EWTB to USD chart, marketcap and volume](https://cryptoslate.com/coins/ishares-msci-taiwan-etf-tokenized-bstocks/)  
  <sub>CryptoSlate, 36 minutes ago</sub>  
  iShares MSCI Taiwan ETF Tokenized bStocks price is $88.40 on Nov 23, 2026. Market cap $606.83K; 24h volume $173.58K.
- [A New Wave Of Anthropic ETFs Is Coming — What’s On Offer](https://stocktwits.com/news-articles/markets/equity/a-new-wave-of-anthropic-et-fs-is-coming-what-s-on-offer/cNbYMLjR9Sm)  
  <sub>Stocktwits, 7 hours ago</sub>  
  ETFs such as Ultra Anthropic (ANTU), UltraShort Anthropic (ANTY), 2X Long Anthropic Daily ETF (AIL) and 2X Short Anthropic Daily ETF (ANS) will begin...
- [SPY, QQQ Rebound As AI Selloff Hits South Korea Despite Government Support: What Investors Are Watching](https://www.google.com/goto?url=CAESsQEBxCJF17ho6aZQeCtnfGggTJmd67ZQXkiLplqrDb-GO-iR2LJc4ePSLEia1Ao5__PlvpTvOpJArDZHgMpHkKMXz92D9oZCeR5Xuo6nL1aHHTp-OKJnlGbUQtoAaOXExuB_3JP67EANwbdg_eT1FvVrCsGfUObtPV7hVJDmF5mYzFUTDCvVrTktMoMD-6Y8zbM2sOrJ4_Wzg_vsQe-jMkRgSv-8OyOnY3KrAHLCVMFKCXE&gsessionid=wqA300yJgplew_g2s-2kmx573ja0-MednVdTnjP19PSj-j2JIa4NEQ)  
  <sub>Stocktwits, 8 hours ago</sub>  
  In early Asian trading, Dow futures climbed 1.45%, while the S&P 500 futures gained 2.10% and Nasdaq-100 futures increased 3.02%.
- [PayPal Sale: Why This Analyst Sees A ‘Lower Likelihood’](https://www.google.com/goto?url=CAESsgEBxCJF1zUdAWjn0_cFYxfTjLe_edJgkOYcK0BQFOO-wz-bvVf5IDVs0Z9uzPp8SolirR7BQcrgbI-JuJVdo0LfZj9PchLhoWIoY8ZnSRC4pvJuYSkeHfuaUXAWZSLSFb2W3UFmUVzx-27HXagQHd4D0WdiyGwhiLskcA1yd76ldAynZdVuwBQoPMQgRozyCjIbO4FWQBq_etrGzbnkgRc7sROK58FdyQUuwWMMpue7ZutZ&gsessionid=wqA300yJgplew_g2s-2kmx573ja0-MednVdTnjP19PSj-j2JIa4NEQ)  
  <sub>Stocktwits, 7 hours ago</sub>  
  Clear Street said that PayPal's four senior executive appointments signal that there is "still a long way to go" for the company's turnaround effort.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 89.51 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 94.80 (-5.6%), 50d 104.93 (-14.7%), 200d 95.19 (-6.0%); 50d above 200d
Momentum: RSI(14) 43.8 | MACD -5.784 vs signal -4.881 (histogram -0.903)
Returns: 1d +19.7% | 5d -1.4% | 1m -14.7% | 3m -15.1%
52-week range: 60.03 - 118.00 (now 50.9% of the way up)
Volatility: ATR(14) 5.48 (6.1% of price) | annualised 20d 107.1%
Volume: 0.86x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Greater China Region
What it holds: P/E 27.29 | P/B 4.22 | P/S 2.50 | 3y earnings growth n/a
Yield: 1.0%
Three-year record: +23.5% a year | beta to the market 1.35
Cost and size: expense ratio 0.59% | net assets 11.05B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 22.3%, MediaTek Inc 6.1%, Hon Hai Precision Industry Co Ltd 3.4%, ASE Technology Holding Co Ltd 3.0%, Delta Electronics Inc 2.9%
Sector mix: Technology 71.4%, Financial services 16.3%, Basic materials 4.4%, Industrials 2.6%
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
Rolled up from the 5 largest holdings, 37.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +72.7% above the current prices
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
Share count change: 1 week: +16.0% (1.62B) over 7d | 1 month: +20.5% (2.00B) over 36d
Shares outstanding: 131.41M | fund size: 11.76B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technicals show the ETF trading above its short‑, medium‑ and long‑term moving averages with RSI 65.4 and a positive MACD, suggesting modest bullish momentum. However, the fund has experienced sizable outflows – 8% of shares in the past month (≈$506 M) – indicating net selling pressure. Analyst coverage is limited to about a quarter of the portfolio but is uniformly bullish (100% buy) with a +14.4% price target, providing some upside bias. The macro backdrop shows slightly higher US yields and an elevated VIX (26.8), reflecting broader market stress and no clear policy surprise. With mixed signals and no decisive macro catalyst, a neutral stance is appropriate.

**Main reasons it gave:**
- 1‑month outflows of -8% (-$506.6M) indicating net selling pressure
- Price above 20‑, 50‑, and 200‑day SMAs with RSI 65.4 and positive MACD, showing technical bullishness
- Analyst consensus 100% buy for 24.8% of holdings, weighted price target +14.4%
- US Treasury yields slightly higher and VIX at 26.8, reflecting elevated market stress
- No macro data surprise or policy shift this week

<details><summary><b>News</b> — score +0.00</summary>

- [How Do iShares MSCI Spain ETF (NYSEARCA:EWP), iShares MSCI India ETF (CBOE:INDA) and iShares MSCI New Zealand ETF (NASDAQ:ENZL) Connect to a USD 1.7 Billion Brookfield (NYSE:BN) Deal?](https://kalkine.com.au/news/announcements/how-do-ishares-msci-spain-etf-nysearcaewp-ishares-msci-india-etf-cboeinda-and-ishares-msci-new-zealand-etf-nasdaqenzl-connect-to-a-usd-17-billion-brookfield-nysebn-deal)  
  <sub>Kalkine, 20 minutes ago</sub>  
  How Do iShares MSCI Spain ETF (NYSEARCA:EWP), iShares MSCI India ETF (CBOE:INDA) and iShares MSCI New Zealand ETF (NASDAQ:ENZL) Connect to a USD 1.7 Billion...
- [What Does Tata Steel's USD 1.67 Billion APL Apollo Tubes Stake Mean for iShares MSCI India ETF (CBOE:INDA)?](https://kalkine.com.au/news/announcements/what-does-tata-steels-usd-167-billion-apl-apollo-tubes-stake-mean-for-ishares-msci-india-etf-cboeinda)  
  <sub>Kalkine, 19 minutes ago</sub>  
  What Does Tata Steel's USD 1.67 Billion APL Apollo Tubes Stake Mean for iShares MSCI India ETF (CBOE:INDA)?
- [What Would a Beijing Red-Chip Listing Rule Mean for KraneShares CSI China Internet ETF (NYSEARCA:KWEB)?](https://www.google.com/goto?url=CAESywEBxCJF17vlD_NpXbZ0vetywm_EGertRtVgMBPxUUY92drYysB_-Mne8EmlQKyXPuihfbWQb8wdDiWSGD3v_4tu1nxYDZwbp6RUe9gJW1l7lFLlElGgsvZqruoPQmQrjHEX5VaPolB5OgTEoBjIIswEn8BIeT-TvVyKFEyZxHk7BdtZC49NooM3lXSambDHPmdmceRbhAo708fV5gbUXKmbjRTxuvVTCL0zGJCLpdUhc67AqN9vdFpDXnr92NFSpRNuKdSwpUFywJTF1Q&gsessionid=fntDRAHGPAMzCdFIVEOJlb4_5axOSL0aDBJrli-dnIlfRxQM4Po5Ng)  
  <sub>Kalkine, 19 minutes ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports. Become a Kalkine member...
- [What Could Partners Group's NZD 1.2 Billion Purchase of Ferry Operator StraitNZ Signal for iShares MSCI New Zealand ETF (NASDAQ:ENZL)?](https://www.google.com/goto?url=CAES6AEBxCJF13owP2aEH6jdSrZaHmGELUlSTUtNUoqbdQxLRHw_tMm0XS1dHXVyVOlN-EaCuHPpnHLst9XOzXRIK8w4fxVw21-cVl2mjpAU-KTcVH6hNSYePzQ_KvdTNcdqfzQGozM5AqIv49eXnkmpEcpvBYy9CxdqjfzUMNhWBR0Buw7Jn0c-wznnV0rrqE3BjG1kNjAGOedefp04fYFq4-tyvauqUiy3CczQ-djhFzr8C7DikWvOsF49HS6jQHhbkFySXmjuF7pBn_FJpOwykWmvezNfUMvyXzkrKoQWsIcDbxmGYJNTd3Hw&gsessionid=fntDRAHGPAMzCdFIVEOJlb4_5axOSL0aDBJrli-dnIlfRxQM4Po5Ng)  
  <sub>Kalkine, 20 minutes ago</sub>  
  What Could Partners Group's NZD 1.2 Billion Purchase of Ferry Operator StraitNZ Signal for iShares MSCI New Zealand ETF (NASDAQ:ENZL)?
- [How Should Investors Weigh Tesla (NASDAQ:TSLA) and SpaceX Before a Possible Merger Announcement Next Month?](https://www.google.com/goto?url=CAESzwEBxCJF17lGCVje6nTBKQ48lMp3S3sU28E3F3OJrKTpwkucaaTSuKwbejMrJeV_Li12wXZiRPlPgFPZItCBJMh4zobCWBu7NrYWc-RE5cVXrFgyyfOCHY995tXUEUKWMF4N-XQO83JQJdIr3HNaMq4JE9aLGQ7xJ3p8ssXNM4gUPXi1680Rid5ju8-_KZ1Sv5NOmAAhQroa-v-Q_Kh2NNhohGq5AZzGbnbr1Tfuxa6WY09upRhwIRWowxREuQ3AJIQaPiYegPLX50gBr2V2pgI&gsessionid=fntDRAHGPAMzCdFIVEOJlb4_5axOSL0aDBJrli-dnIlfRxQM4Po5Ng)  
  <sub>Kalkine, 20 minutes ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Aland Equity Group Receives First $374,000 Management Fee Payment from Elm Grove Fund](https://www.google.com/goto?url=CAESugEBxCJF17yhFMtltZaJOzRQQPTJi31fna1x3346aT0RlcTy41_JLcE6se1HVtCWQCXyOfkn9vvuNgeCIUKZjGSfWwKeFuYz47AfeS4frS1n6BCm6vHqEzYRTTP3EQ9slcwv1stFB4ok_wLkERztR99foEvqkjHGjqbWqeqfZV2kkHiZ4nltqnWXfLOrIOMEg0xqj2tuR95YLt47cNvIciDtU4p6DDHVFo3g8USyp2qyDCzviCUnFvdB_98&gsessionid=fntDRAHGPAMzCdFIVEOJlb4_5axOSL0aDBJrli-dnIlfRxQM4Po5Ng)  
  <sub>Kalkine, 16 hours ago</sub>  
  Aland Equity Group Limited (ASX:AEG) has received its first $374000 investment management fee from the Aland Elm Grove Estate Fund following shareholder...
- [Barkly Rare Earths Records Highest-Grade Intercept at 18,086 ppm TREO over 0.5 m in Phase 1 Drilling](https://www.google.com/goto?url=CAESygEBxCJF19s3h7FLuM76VK0-sbMVl7Qxu8fWF1IJHUrs_paNwVe267JU1nJUjVuSPhB04iK_Qcnr5pzVrRPerDUw5EgGUrfSLrb8H0OLdW4-B57NugFeYuOPnF2jbs_wJ_-gr7FJo7AysSMY1l1lmbjqHeplhmxumgeL5OA5zFlc6WTjVkosYG_4P5NUwMtFdtEcMB881D0XqwZNvY11gemwGV8gAkwk6k1FZGZMqL_DoTy7BRKVVzB3dZuGvbWGFv2DAM4hLxtPEKvz&gsessionid=fntDRAHGPAMzCdFIVEOJlb4_5axOSL0aDBJrli-dnIlfRxQM4Po5Ng)  
  <sub>Kalkine, 16 hours ago</sub>  
  Barkly Rare Earths Limited (ASX:BAK) has reported assay results for a further 38 holes from the Phase 1 drilling programme at its Barkly Project in the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.25</summary>

```text
Last close 51.95 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 50.31 (+3.3%), 50d 48.43 (+7.3%), 200d 49.08 (+5.9%); 50d below 200d
Momentum: RSI(14) 65.4 | MACD 1.187 vs signal 1.068 (histogram 0.119)
Returns: 1d -1.8% | 5d +0.8% | 1m +11.8% | 3m +3.4%
52-week range: 45.42 - 54.71 (now 70.3% of the way up)
Volatility: ATR(14) 0.62 (1.2% of price) | annualised 20d 16.0%
Volume: 0.31x the 20-day average
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
Three-year record: +5.8% a year | beta to the market 0.61
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 24.8% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.37 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.4% above the current prices
Holdings read: HDFCBANK.NS, ICICIBANK.NS, RELIANCE.NS, BHARTIARTL.NS, INFY.NS
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.60</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -0.8% (-46.74M) over 7d | 1 month: -8.0% (-506.62M) over 30d
Shares outstanding: 112.54M | fund size: 5.85B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Recent macro data showed no unexpected policy shifts, while technicals indicate bearish pressure (price below key SMAs, RSI 40.5, MACD negative). However, strong recent inflows and modestly favorable fundamentals and analyst views offset the downside, leaving no clear material catalyst for a directional call.

**Main reasons it gave:**
- Inflation 3.7% and Fed target unchanged at 4%, no policy surprise
- KRE price below 20‑day SMA, RSI 40.5 and MACD negative, indicating bearish momentum
- Share count up 4.6% in one week and 9.4% in one month, showing net inflows
- Analyst coverage thin (5.9% of fund) with 50% buy, 50% hold and modest price target (+14.9%)

<details><summary><b>News</b> — score +0.20</summary>

- [These are the favorite stocks of financial-sector hedge funds - Goldman (KRE:NYSEARCA)](https://seekingalpha.com/news/4675597-these-are-the-favorite-stocks-of-financial-sector-hedge-funds-goldman?utm_source=tradingview&utm_medium=referral&feed_item_type=news)  
  <sub>Seeking Alpha, 13 minutes ago</sub>  
  Goldman Sachs finds Valley National Bancorp is the top financials-specialist hedge fund holding, owned by 41% of 23 funds screened.
- [Bank stocks set to bounce back after Friday's crash](https://www.google.com/goto?url=CAESrgEBxCJF13cw4pEZQyMesAhUIsEMiyVeVpTMqPGl-nZmtpmBnLtssORCftB3tNfMacvSgXMgRtQksNloz3NV94_iUYN4oiCJHE5LhgbM6G0ONKwf6sLzm6JfVRDZjzM2VnZUX78u4HrhU20u6EArmAPiY7VlJl0iBeTsusLHGHVAkUH6R9LSsmuttpsi9F0p29Tw0BguZ7qRhz89LVMChKFVLNAnkpJKiwA-7tWSnMI&gsessionid=8ImZ28e-djWmU-1gadXIalaZmOGqIdpW9E-aC54mntpP3IDSLUvBqA)  
  <sub>TradingView, 35 minutes ago</sub>  
  Bank stocks are poised to open solidly in the green after tumbling along with the broader market on Friday.Last week, large bank stocks exhibited a rare...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 69.51 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 72.01 (-3.5%), 50d 71.24 (-2.4%), 200d 71.18 (-2.3%); 50d above 200d
Momentum: RSI(14) 40.5 | MACD -0.528 vs signal -0.044 (histogram -0.484)
Returns: 1d +1.7% | 5d -3.7% | 1m -4.1% | 3m -6.5%
52-week range: 61.61 - 77.93 (now 48.4% of the way up)
Volatility: ATR(14) 1.49 (2.1% of price) | annualised 20d 21.2%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Financial
What it holds: P/E 12.17 | P/B 1.26 | P/S 3.63 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +17.9% a year | beta to the market 0.97
Cost and size: expense ratio 0.35% | net assets 4.01B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Glacier Bancorp Inc 1.2%, United Community Banks Inc 1.2%, Texas Capital Bancshares Inc 1.2%, Bank OZK 1.2%, Eastern Bankshares Inc Ordinary Shares 1.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.12</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.12</summary>

```text
Rolled up from the 5 largest holdings, 5.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 50.1% | hold 49.9% | sell 0.0% (mean 2.45 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.9% above the current prices
Holdings read: GBCI, UCB, TXCP, OZK, EBC
Recent rating changes among them:
  - GBCI: 2026-10-26 Piper Sandler: main, Overweight -> Overweight
  - UCB: 2026-10-21 Stephens & Co.: main, Overweight -> Overweight
  - TXCP: 2026-11-03 Barclays: main, Equal-Weight -> Equal-Weight
  - OZK: 2026-10-30 Keefe, Bruyette & Woods: main, Market Perform -> Market Perform
  - EBC: 2026-11-03 Barclays: main, Equal-Weight -> Equal-Weight
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
Share count change: 1 week: +4.6% (176.22M) over 7d | 1 month: +9.4% (345.69M) over 30d
Shares outstanding: 57.78M | fund size: 4.02B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technicals show a short‑term downtrend with price below the 20‑day and 50‑day SMAs, while inventories and the EIA price outlook indicate bearish supply and lower oil prices. Analyst coverage is bullish but only covers ~59% of the fund, and fund flows are flat, suggesting neutral demand. No macro surprise or decisive technical break emerged, so we maintain a neutral stance with low conviction.

**Main reasons it gave:**
- Price 60.67 below 20‑day SMA (64.17) and 50‑day SMA (64.62) – short‑term bearish trend
- Energy inventories all show builds (crude +3.4 M bbl, nat gas +20 Bcf) – bearish supply outlook
- Analyst consensus 100% buy with weighted price target +17% (covers 59% of fund) – bullish analyst view
- EIA forecasts WTI price down ~13% over six months – bearish price outlook
- Fund flows flat (0% change weekly/monthly) – neutral demand

<details><summary><b>News</b> — score +0.00</summary>

- [Why ExxonMobil’s Risks May Look Smaller Inside 3 ETFs](https://simplywall.st/etfs/us/nysearca-hdv/news/why-exxonmobils-risks-may-look-smaller-inside-3-etfs)  
  <sub>Simply Wall St, 2 hours ago</sub>  
  You can own ExxonMobil Holdings outright or let it sit inside a fund that blends it with other businesses. Holding just ExxonMobil means you wear company...
- [Why Owning ConocoPhillips Through ETFs Could Make Sense Now](https://simplywall.st/etfs/us/nysearca-vde/news/why-owning-conocophillips-through-etfs-could-make-sense-now)  
  <sub>Simply Wall St, 3 hours ago</sub>  
  You can own ConocoPhillips outright, or you can hold it inside a fund that mixes it with other energy businesses. Holding a single stock means you carry its...
- [Which 3 ETFs Best Fit ExxonMobil After Its Angola Move?](https://www.google.com/goto?url=CAESmAEBxCJF132XUwLq5a_o0tEXLap4aGWWhOk3_nfN-Ig5D06MYDLW1wMFhkJMBB_F-uY1k_dALATlZewSxhoa1SJqT697osnX2cp2s6-6E88nUy7FiAgcoWEeZrb0OsIKhO9_2JIuAfi5laUEEKSZCx-DcIazfYixYyt9lfSFxtXll-na-bFiTLf-kRvQXnJT-ecczAWMohECpg&gsessionid=2s7bJY3-o4NG0sS-8hICT6q5nVtUmZ8unVejFUk158NnFlfKiFbhUQ)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  If you like ExxonMobil Holdings for its global oil and gas reach, owning only the single stock means your money rises and falls entirely with its own issues...
- [Hedge funds short single stocks at fastest weekly pace since 2022 - Goldman](https://www.google.com/goto?url=CAESxgEBxCJF1_IIzRsbv_-c1oNOSCv-kBvUC6A1-QQv7oy-cTkjWLfxSplqJEOVf2JbwS7A4sMrBYC1ibPd_RtH0WOGtN-HRdy0q6NF09WJgrkokT3Qe5_uYbZZhL6skaT0PgwM2qCG2qJodwMd49oAExMLqHXcx0GyZN9eExsgUDUHzb3ElBVPc9z9N4p4OIz85KQl56W15BOhB_feiXxOw1xfW7qaan4HfGG1A0XK65l5i9nAcFasshZNnqW_u3sMr57I1sT6ALc&gsessionid=2s7bJY3-o4NG0sS-8hICT6q5nVtUmZ8unVejFUk158NnFlfKiFbhUQ)  
  <sub>TradingView, 26 minutes ago</sub>  
  Hedge funds net sold U.S. equities AMEX:SPY NASDAQ:QQQ AMEX:DIA for a third straight week driven by heavy single-stock shorting that outpaced long buying by...
- [Wrapped Energy Select Sector SPDR Fund Tokenized ETF (xStock): Funding, Investors, Team and Key Events](https://www.google.com/goto?url=CAESlAEBxCJF11-WFMf1SCTaBuP_WxEEkT_XFNnfygGLXDhhTyTA-TtkvTvVBiCt7jdsrfBxqjIa1bel-xhSjaBjeOO435pLcKRtvoA5-uSVv0DrjxQdcUqTF1NPQ9ice34KENNsEbXrMVNfj3KH3-0Waiis8B3eoea6mlBKJnNMZsZu-6nIKVYqzQU-wKuhzSmwbs6fG5wo&gsessionid=2s7bJY3-o4NG0sS-8hICT6q5nVtUmZ8unVejFUk158NnFlfKiFbhUQ)  
  <sub>CryptoRank, 5 hours ago</sub>  
  wXLEx wraps XLEx, the xStock linked to shares of State Street's Energy Select Sector SPDR ETF (NYSE Arca: XLE). The fund tracks the Energy Select Sector...
- [COP31 climate talks collapse as oil stocks cap a banner year (XOM:NYSE)](https://www.google.com/goto?url=CAESnwEBxCJF14k6OXe-c0RthI1v64uN6XFxdIWx7ezPtnarWE-ixCJAcKcGFWGjwNlzBPL0QvW-r_4VWALAYFsnG49AUnJUB75GOtxejJqVJIgSZfrCDpjXZtgrTXka_X7TJqatZQaSrKcDezKUy9nZlp-mQ7XMbfU5sD4Kmc21l5ebgbYaq4_Kich0zN8ILgfr8149rBl-PYPO1R0zSSK62eY&gsessionid=2s7bJY3-o4NG0sS-8hICT6q5nVtUmZ8unVejFUk158NnFlfKiFbhUQ)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  COP31 talks collapse without agreement on fossil fuels or climate finance, while XLE gains 35% in 2026 and ICLN falls 15%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 60.67 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 64.17 (-5.4%), 50d 64.62 (-6.1%), 200d 59.77 (+1.5%); 50d above 200d
Momentum: RSI(14) 35.5 | MACD -1.245 vs signal -0.794 (histogram -0.451)
Returns: 1d +0.3% | 5d -4.7% | 1m -12.5% | 3m -2.2%
52-week range: 43.81 - 70.02 (now 64.3% of the way up)
Volatility: ATR(14) 1.48 (2.4% of price) | annualised 20d 30.4%
Volume: 0.18x the 20-day average
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
Three-year record: +16.2% a year | beta to the market -0.22
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
US inventories, week ending 2026-11-13 (published the following Wednesday)
  Crude oil: 417.8 million barrels, +3.4 on the week (a build), 25% percentile over 52 weeks
  Petrol: 215.9 million barrels, +5.2 on the week (a build), 56% percentile over 52 weeks
  Diesel: 104.9 million barrels, +1.6 on the week (a build), 33% percentile over 52 weeks
  Natural gas: 3,882.0 billion cubic feet, +20.0 on the week (a build), 96% percentile over 52 weeks -- high for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 59.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.10 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.1% above the current prices
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
Shares outstanding: 186.42M | fund size: 11.31B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Macro conditions are unchanged – Treasury yields are flat and there is no surprise data. The VIX is higher, indicating more market stress, but no policy shock. Technicals show the price slightly below the 20‑day SMA and a bearish MACD divergence, suggesting modest downside momentum, yet volume is low and there is no decisive break. Analyst coverage is bullish (80% buy, price target +13.3%), but fund flows are flat, indicating no net demand. The mixed signals and lack of a clear catalyst lead to a neutral stance.

**Main reasons it gave:**
- US Treasury yields unchanged this week (3‑month +0.03, 5‑year -0.14, 10‑year -0.14)
- VIX risen to 26.76, indicating higher market stress
- Technical: price below 20‑day SMA (-0.9%) and MACD below signal (histogram -0.160)
- Analyst consensus: 80% buy, weighted price target +13.3% above current price
- Fund flows flat: share count unchanged over the past month

<details><summary><b>News</b> — score +0.00</summary>

- [3 Funds With Electric Utility Exposure As Data Center Power Outruns The Grid](https://www.google.com/goto?url=CAESlwEBxCJF1wJLV0osynuR66JqxT9TofSdD7cLZqjzwhcVdtKc3-P47glRrtCQb9b2murW4s7o9znnj4b_XTRcR-1nPX8EBINtDbnM3-4l-LZaVSJfwPrDOFSEuLiVxjdSr3l7yLkzvm1oR4eQFbTTnd8jTLPIWZxOTthkkCxj0DCtGS3BNqs2oVzepU66bK6BAGv3kBWV1zHd&gsessionid=uFHTaLoFh4atDe2f4FpY5CN6MNipekHnIKzycrRKuAfIQ1eycH4Erg)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  How different can three funds with heavy electric utility exposure really be, and which mix actually fits what you want from the power story?
- [ETFs Bought $155.7 Million of Dominion Energy (D) on Nov. 19](https://www.gurufocus.com/news/9214498/etfs-bought-1557-million-of-dominion-energy-d-on-nov-19?utm_source=yahoo_finance&utm_medium=syndication&utm_campaign=headlines&r=caf6fe0e0db70d936033da5461e60141)  
  <sub>GuruFocus, 3 hours ago</sub>  
  ETF flows into Dominion Energy extended a five-day buying streak on Thursday, Nov. 19, with a net $155.7 million added. Thirty-five ETFs bought the stock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 43.03 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 43.40 (-0.9%), 50d 41.97 (+2.5%), 200d 44.34 (-3.0%); 50d below 200d
Momentum: RSI(14) 50.2 | MACD 0.268 vs signal 0.428 (histogram -0.160)
Returns: 1d +0.8% | 5d -2.5% | 1m +1.1% | 3m -0.7%
52-week range: 39.25 - 47.73 (now 44.5% of the way up)
Volatility: ATR(14) 0.62 (1.4% of price) | annualised 20d 13.3%
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
Three-year record: +14.5% a year | beta to the market 0.34
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

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
Shares outstanding: 163.27M | fund size: 7.02B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.15

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst consensus and strong inflows contrast with bearish technicals and elevated market volatility; no macro surprise or decisive breakout, so we stay neutral.

**Main reasons it gave:**
- Share count rose 12.2% in one week (7.32B) indicating strong inflows
- Price trades below 20‑day, 50‑day, and 200‑day SMAs (453 vs 490.06, 545.74, 525.43) with RSI 41 and negative MACD
- Analyst consensus: 100% buy, weighted price target +50.5% above current price
- VIX rose 3.9% week to 26.76, indicating heightened market stress

<details><summary><b>News</b> — score -0.25</summary>

- [VanEck Semiconductor ETF (SMH) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/SMH/)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>  
  VanEck Semiconductor ETF (SMH) · -17.81% · -26.78% · -29.15% · 10.12% · 17.86% · 156.28% · 720.64%. Key Events. Baseline. Advanced Chart. Loading chart...
- [Jensen Huang's return to Nvidia puts spotlight on ETFs with the biggest exposure to the stock](https://seekingalpha.com/news/4675586-jensen-huangs-return-to-nvidia-puts-spotlight-on-etfs-with-the-biggest-exposure-to-the-stock)  
  <sub>Seeking Alpha, 14 minutes ago</sub>  
  Nvidia shares jump nearly 29% after the board reinstates Jensen Huang as CEO; NVDW has the largest ETF allocation at 20.48%.
- [Should You Invest in the State Street SPDR S&P Semiconductor ETF (XSD)?](https://www.google.com/goto?url=CAESmAEBxCJF17YXBjuNgvsGQu2HIpJL1-cPEyEusuvFdn9s0E3nwqlyzMqYiongTdBeECemRNu4ePYVZAWT_lyc--CP8T20w1gJIeRVTLoYY9sWJDEgv04OJ_SqmEgNECzEkReFg7sQ9c1nd9aDbYC4tZmY5HCN5w8C3fjOwPkklSxVG9ZnN86lgfjyA-AGVE1NOx57zMx1Mjf8fg&gsessionid=ExHdDocRttJMW12AaR-GA8iNA8PSthODfSMArUVpaXMEVo1dIvBdKQ)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  If you're interested in broad exposure to the Technology - Semiconductors segment of the equity market, look no further than the State Street SPDR S&P...
- [Wall Street Fear Gauge Hits March High As Anthropic (ANT) IPO Surge Fails To Calm AI Spending Anxiety](https://www.google.com/goto?url=CAES0gEBxCJF16GhKdey5esuiaF3vtB8lnSgnUizAiTv4VbTG7Hf_fqCAet2X89plqi8Mo2DQwP41ZAYFTWYqI9WtUEzl23APV27NRKeeAlZgZTMM8NdtHrazOXkKfCzNfs7JpKgMv0pyVfQzwNKN6jNRubVN1dJjikTaQKhawHaZ0naHOjQ_Vsk8l0HcJM3iJMOe346szuewYK7ByNSRh1jOFEwz41MVu8trnIgEPVtJxnMVpCWwDXNLj6ZPOJuvZfT-OKRcGzHeJWGlj6bRMboC-L_PAo&gsessionid=ExHdDocRttJMW12AaR-GA8iNA8PSthODfSMArUVpaXMEVo1dIvBdKQ)  
  <sub>Foreign Policy Journal, 23 hours ago</sub>  
  Wall Street's volatility index climbed to its highest level since March on Thursday, a signal that Anthropic's (ANT) market debut did little to soothe.
- [The Best Semiconductor ETFs After The November 2026 Chip Selloff](https://www.google.com/goto?url=CAEScQHEIkXXgpWeAlVZlRfQnTiN-vSzDwAeiAaDmjwJedxmWH46wgN6F4EAtOQnNJmKiJP6_UN2rsSAvxvlDrXEAXzXxLofoxdbycgLm68kWerEz96iWWOx2-rGP1LbbUWXvTYd1t0ZoT1a3G2FQ27hVx9l&gsessionid=ExHdDocRttJMW12AaR-GA8iNA8PSthODfSMArUVpaXMEVo1dIvBdKQ)  
  <sub>Stocks Down Under, 8 hours ago</sub>  
  Chip stocks have been hammered, with SOXX down about 34.5% since 30 September, yet still up roughly 55% for the calendar year. An ETF saves you from picking...
- [Top Tokenized ETFs by Market Cap](https://www.google.com/goto?url=CAESXgHEIkXX5wwn_7QngWBw4Xxbm6OvBFdc03r8z6JNbEWD1QT-KusCMAN6X0PtcJCsaKl2C5NGYmKM-vXu7CDZybn7gym6hMs84r9YMl2aT8gjtueuUUaWkSiNeWPBp6c&gsessionid=ExHdDocRttJMW12AaR-GA8iNA8PSthODfSMArUVpaXMEVo1dIvBdKQ)  
  <sub>CoinGecko, 1 hour ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...
- [Trader Places $93 Million Bet Against Chip Stocks](https://www.google.com/goto?url=CAESiwEBxCJF1136L-ChRlzc7UcKjHzh7u6mJs_FaIb2QHxdKdi7NI1ncdZDv6Kmg4784vgLB7XEHzFUJkg6QfuaacJj0enGx_XLI3MS367TLzKufBlyWG3Jet-sI8w1xhe_4ajxong9b2dxRjMDoSJZGoRdcXSbOomBKPSg618-Gax2twZ6J83z96Do8xC3&gsessionid=ExHdDocRttJMW12AaR-GA8iNA8PSthODfSMArUVpaXMEVo1dIvBdKQ)  
  <sub>varindia, 22 hours ago</sub>  
  As Wall Street's AI sell-off deepened Friday, one options trader placed a striking wager: a near-$100 million bet that semiconductor stocks still have...
- [Citadel Reports Surge in US Equity Volatility as Traders Brace for Major Options Expiry](https://www.google.com/goto?url=CAESjQEBxCJF152HKM5QY4kneP1LktkgeQq6C_zCQfX9AMMssfu8KnHv08HbDAlyGmHKA3njlNtgXnWbC3ivMDbocr4YAVNmaAN46AW9p9ZjFtDGUHMO2wWuqVHLDgYwyZ0DQPfQxwT01bDH6WXik1caf55KsI18DEakImWO8tobUoD5kHmigeyuzQWoC6Vof9Y&gsessionid=ExHdDocRttJMW12AaR-GA8iNA8PSthODfSMArUVpaXMEVo1dIvBdKQ)  
  <sub>Yahoo Finance UK, 24 hours ago</sub>  
  US stock markets have experienced their sharpest volatility since April 2025, according to Citadel's Scott Rubner, with technology and semiconductor shares...
- [VanEck Semiconductor ETF (SMH) Price Prediction: Semiconductor ETF Stays Heavy Below Key Trend Lines as Buyers Probe Support](https://www.google.com/goto?url=CAESnwEBxCJF1xdCAftipAkQmlroW3BUPYA-8oXwgG_SV4za5HuQe3l6ddpjXrNwtxXZoXN3PUII-FgO-wfDKWXBt8MBwG0MuMcaBVCqnEYkOXNUmj-KvBkWR0_ialfF2uB97SQh2GbKJTGx_nFiNgF0ZGzDNbFgLetnmH8Ld99NS7cy-eJotoK0fur87GQFb-7pd9Ip7gIqm2VuZ4xRRU3FCZw&gsessionid=ExHdDocRttJMW12AaR-GA8iNA8PSthODfSMArUVpaXMEVo1dIvBdKQ)  
  <sub>blockchain.news, 6 hours ago</sub>  
  VanEck Semiconductor ETF (SMH) is trading at $425.72, up 3.09% over 24 hours, but it remains below its 7-, 20- and 50-day moving averages.
- [iShares Russell 2000 ETF (IWM) Price Prediction: Small-cap ETF slips into a technical test as momentum stays soft](https://www.google.com/goto?url=CAESkgEBxCJF14miNU7RTx8BEhbPbQX3WFyJ8L9SWiGIi9TIA0i0YJ67wP76wluye7Cse52VRcIjovzbqKBcoRouNaAyQuf0-Wn3Lzex1v7pHz5j8fIwameM8O6mt29CC1KRjsTfEMc5r62stcLGOa3bO1I_R3ZT9x6Dp-n2dKG3mBQKn1vUf1LDe3H9dVQ4XQ4GkVYZsw&gsessionid=ExHdDocRttJMW12AaR-GA8iNA8PSthODfSMArUVpaXMEVo1dIvBdKQ)  
  <sub>Blockchain News, 6 hours ago</sub>  
  iShares Russell 2000 ETF (IWM) is trading at $263.09, just above its immediate support at $260.04 and above strong support at $256.98. The ETF remains below...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.25</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 453.00 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 490.06 (-7.6%), 50d 545.74 (-17.0%), 200d 525.43 (-13.8%); 50d above 200d
Momentum: RSI(14) 41.0 | MACD -30.265 vs signal -26.609 (histogram -3.656)
Returns: 1d +13.2% | 5d -1.9% | 1m -14.1% | 3m -18.5%
52-week range: 326.13 - 668.91 (now 37.0% of the way up)
Volatility: ATR(14) 29.21 (6.4% of price) | annualised 20d 88.4%
Volume: 0.36x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

```text
Fund type: Technology
What it holds: P/E 28.22 | P/B 9.76 | P/S 11.19 | 3y earnings growth n/a
Yield: 0.2%
Three-year record: +35.0% a year | beta to the market 2.12
Cost and size: expense ratio 0.35% | net assets 66.44B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: NVIDIA Corp 20.2%, Taiwan Semiconductor Manufacturing Co Ltd ADR 9.6%, Texas Instruments Inc 5.7%, Broadcom Inc 5.6%, Advanced Micro Devices Inc 5.3%
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 46.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.63 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +50.5% above the current prices
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
Share count change: 1 week: +12.2% (7.32B) over 7d | 1 month: +16.7% (9.60B) over 36d
Shares outstanding: 148.49M | fund size: 67.26B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.12

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals show slight short‑term weakness but no decisive break, fundamentals are stable, analyst consensus is moderately bullish but covers less than half the fund, and fund flows are flat; overall the evidence points to a neutral stance.

**Main reasons it gave:**
- Yield curve remains upward sloping (+0.82) – no inversion (macro)
- Price below 20‑day SMA (-2.7%) and MACD negative (technical)
- Analyst coverage 43.3% of fund, 70.7% buy, price target +11% (analyst view)
- Fund flows flat over past week and month (0% change) (fund flows)

<details><summary><b>News</b> — score -0.05</summary>

- [These are the favorite stocks of financial-sector hedge funds - Goldman (KRE:NYSEARCA)](https://seekingalpha.com/news/4675597-these-are-the-favorite-stocks-of-financial-sector-hedge-funds-goldman?utm_source=tradingview&utm_medium=referral&feed_item_type=news)  
  <sub>Seeking Alpha, 13 minutes ago</sub>  
  Goldman Sachs finds Valley National Bancorp is the top financials-specialist hedge fund holding, owned by 41% of 23 funds screened.
- [Hedge funds short single stocks at fastest weekly pace since 2022 - Goldman](https://www.tradingview.com/news/seekingalpha:799793739094b:0-hedge-funds-short-single-stocks-at-fastest-weekly-pace-since-2022-goldman/)  
  <sub>TradingView, 26 minutes ago</sub>  
  Hedge funds net sold U.S. equities AMEX:SPY NASDAQ:QQQ AMEX:DIA for a third straight week driven by heavy single-stock shorting that outpaced long buying by...
- [PNC Financial Services Stock Outlook: Is Wall Street Bullish or Bearish?](https://www.google.com/goto?url=CAESogEBxCJF13oJHY9p-mmxM4wWJ1SnxidGwghHg2e7xhWbgdtQCMzFRE5DdtEz-LobgA0rRILI-EoddsJpbQupjZs-TpMNNCk0CLL8VnJyO4T_4-tglHnwuFB5qKLjGwHdVFh0DJ5WPxt5ZBDoyi-pT20v2eDnXSAbJESTi5fveyv3gSl-lbQyjjiEHQrKZMlu3RAF6Z0i0oZZSB53fKVd8ej5_X0&gsessionid=m_84afhGqWVrZbcRJGe2z0LZjiaZ-0uXXvSHcF2VJSMuEaMqcxSFLQ)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  PNC Financial Services' shares have outpaced the broader market, with Wall Street's outlook tilted toward the bullish side.
- [iShares Russell 2000 ETF (IWM) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXX7hCX7oEaRIJXc6Xm8Cigtib8BN_CnSNW51ByOZR9sE12wwgN6i_6EB3x9GCTqDN_tQZ6jXKd6hg58VcarDI0KbaCwJXG8zPTZBMLtaa3OcSGITo9KY44wEoYbe29dUM&gsessionid=m_84afhGqWVrZbcRJGe2z0LZjiaZ-0uXXvSHcF2VJSMuEaMqcxSFLQ)  
  <sub>Yahoo Finance UK, 4 hours ago</sub>  
  Find the latest iShares Russell 2000 ETF (IWM) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.05</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 55.64 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 57.17 (-2.7%), 50d 55.84 (-0.4%), 200d 54.02 (+3.0%); 50d above 200d
Momentum: RSI(14) 44.3 | MACD -0.024 vs signal 0.372 (histogram -0.396)
Returns: 1d +2.0% | 5d -4.4% | 1m -0.5% | 3m -4.6%
52-week range: 47.81 - 59.20 (now 68.7% of the way up)
Volatility: ATR(14) 0.99 (1.8% of price) | annualised 20d 24.9%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Financial
What it holds: P/E 15.26 | P/B 2.28 | P/S 3.26 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +17.6% a year | beta to the market 0.68
Cost and size: expense ratio 0.08% | net assets 53.58B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Berkshire Hathaway Inc Class B 12.7%, JPMorgan Chase & Co 11.2%, Visa Inc Class A 8.8%, Mastercard Inc Class A 6.5%, Bank of America Corp 4.1%
Sector mix: Financial services 98.2%, Technology 1.6%, Industrials 0.3%
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
Rolled up from the 5 largest holdings, 43.3% of the fund by weight
Ratings by weight: buy 70.7% | hold 29.3% | sell 0.0% (mean 2.00 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.0% above the current prices
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
Shares outstanding: 883.44M | fund size: 49.15B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.10

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: positive German PMI and bullish analyst view versus bearish technicals and a risk‑off macro backdrop lead to a neutral stance with low conviction.

**Main reasons it gave:**
- German flash PMI 55.0 indicates expansion
- Price below 20d/50d/200d SMAs, RSI 39.2, MACD negative, volume 0.07x avg => bearish technicals
- Analyst consensus: 78% buy, weighted price target +24.8% above price
- VIX 26.76 (+3.9) and dollar index 104.10 (+0.55) signal higher volatility and risk‑off sentiment
- Fund flows flat (0% change) indicating no new demand

<details><summary><b>News</b> — score +0.20</summary>

- [How Much Weight Does Germany's Flash PMI of 55.0 Carry Against France's Drop to 46.2 for iShares MSCI Germany ETF (NYSEARCA:EWG)?](https://kalkine.com.au/news/economic-news/how-much-weight-does-germanys-flash-pmi-of-550-carry-against-frances-drop-to-462-for-ishares-msci-germany-etf-nysearcaewg)  
  <sub>Kalkine, 18 minutes ago</sub>  
  How Much Weight Does Germany's Flash PMI of 55.0 Carry Against France's Drop to 46.2 for iShares MSCI Germany ETF (NYSEARCA:EWG)?
- [How Does China's Margin Ratio Cut to 80% Affect iShares China Large-Cap ETF (NYSEARCA:FXI)?](https://kalkine.com.au/news/mutual-funds-etfs/how-does-chinas-margin-ratio-cut-to-80-affect-ishares-china-large-cap-etf-nysearcafxi)  
  <sub>Kalkine, 18 minutes ago</sub>  
  How Does China's Margin Ratio Cut to 80% Affect iShares China Large-Cap ETF (NYSEARCA:FXI)?
- [What Would the S&P 500 Under Every 2026 Forecast Mean for iShares Core S&P 500 ETF (NYSEARCA:IVV)?](https://www.google.com/goto?url=CAESwwEBxCJF14dIG84-H4PHhUr3tA2xDfFF0dCEWRuBtvRfR4gEKoik7r9J1FxEJMfJ7O_Bj0yyV1Yn7gxQVwCFvZR67Y0hu4oIB7yn67YW-Azd_uV2ezbTBTL-8HxxK4ISfxYdz_Ogjz2nGaAzgMFX-LY0C4N6-AEtW7rbc5PQHnc76K6EQxGRQ-t8ywAuHUx1ydLlyYGRdQDswOhH5QJsXo67VN05nCCsfIPdobNzZ33TXzfVMqo4S39pUPcbE5xQkA1yrRY&gsessionid=7HkUBAKhPaPGw7rAPaT3vxGSNppHqC72n6DhFH0XPOz39WXRLgtlUQ)  
  <sub>Kalkine, 18 minutes ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 40.06 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 41.94 (-4.5%), 50d 41.73 (-4.0%), 200d 42.13 (-4.9%); 50d below 200d
Momentum: RSI(14) 39.2 | MACD -0.394 vs signal -0.050 (histogram -0.345)
Returns: 1d +2.3% | 5d -5.3% | 1m -2.1% | 3m -9.9%
52-week range: 38.08 - 44.59 (now 30.5% of the way up)
Volatility: ATR(14) 0.75 (1.9% of price) | annualised 20d 28.5%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.50 | P/B 1.87 | P/S 1.23 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +14.0% a year | beta to the market 0.95
Cost and size: expense ratio 0.49% | net assets 1.57B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: SAP SE 12.7%, Siemens AG 11.4%, Allianz SE 9.9%, Siemens Energy AG Ordinary Shares 5.8%, Deutsche Telekom AG 5.3%
Sector mix: Industrials 27.2%, Financial services 23.5%, Technology 16.9%, Healthcare 7.6%
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
Rolled up from the 5 largest holdings, 45.1% of the fund by weight
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.99 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.8% above the current prices
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
Shares outstanding: 79.50M | fund size: 3.19B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.10

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technicals show a downtrend with price below the 20‑, 50‑ and 200‑day SMAs and bearish momentum (RSI 38, MACD negative). Analysts are unanimously bullish, assigning a weighted price target ~16% above current levels. Fund flows are flat and macro data show no surprising policy or inflation shifts, leaving the overall stance neutral.

**Main reasons it gave:**
- Price 49.26 below 20d SMA 51.83 (-5%)
- RSI 38 and MACD negative indicating bearish momentum
- Analyst consensus 100% buy with weighted price target +15.8% above current
- Fund flows flat with no net share creation or redemption

<details><summary><b>News</b> — score +0.00</summary>

- [Hedge funds short single stocks at fastest weekly pace since 2022 - Goldman](https://www.tradingview.com/news/seekingalpha:799793739094b:0-hedge-funds-short-single-stocks-at-fastest-weekly-pace-since-2022-goldman/)  
  <sub>TradingView, 29 minutes ago</sub>  
  Hedge funds net sold U.S. equities AMEX:SPY NASDAQ:QQQ AMEX:DIA for a third straight week driven by heavy single-stock shorting that outpaced long buying by...
- [Nucor Stock Outlook: Is Wall Street Bullish or Bearish?](https://finance.yahoo.com/markets/stocks/articles/nucor-stock-outlook-wall-street-083508570.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Charlotte, North Carolina-based Nucor Corporation (NUE) manufactures and sells steel and steel products. The company has a market cap of $53.9 billion and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 49.26 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 51.83 (-5.0%), 50d 50.76 (-3.0%), 200d 51.22 (-3.8%); 50d below 200d
Momentum: RSI(14) 38.0 | MACD -0.444 vs signal 0.058 (histogram -0.502)
Returns: 1d +1.9% | 5d -4.3% | 1m -4.0% | 3m -8.1%
52-week range: 43.17 - 53.90 (now 56.7% of the way up)
Volatility: ATR(14) 1.02 (2.1% of price) | annualised 20d 24.8%
Volume: 0.15x the 20-day average
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
Three-year record: +8.4% a year | beta to the market 0.76
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 34.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.8% above the current prices
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
Shares outstanding: 71.92M | fund size: 3.54B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst coverage and strong inflows are offset by weak technicals and no macro surprise.

**Main reasons it gave:**
- Strong inflows: share count up 8.9% in one week and 13.2% in one month
- Analyst coverage: 51.1% of fund weighted 100% buy with price target +75% above current
- Technical indicators: price below 20‑day, 50‑day, 200‑day SMAs; RSI 27.2 (oversold); low volume
- Macro environment: no surprise in yields, inflation, or policy; VIX elevated but stable
- Fund fundamentals: moderate valuation (P/E 13.9), low yield (1.3%), solid 3‑year return (+12.6% per year)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 67.09 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 74.32 (-9.7%), 50d 82.89 (-19.1%), 200d 90.09 (-25.5%); 50d below 200d
Momentum: RSI(14) 27.2 | MACD -4.848 vs signal -4.297 (histogram -0.551)
Returns: 1d +3.9% | 5d -4.9% | 1m -23.0% | 3m -29.7%
52-week range: 64.56 - 102.94 (now 6.6% of the way up)
Volatility: ATR(14) 2.26 (3.4% of price) | annualised 20d 36.5%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.90 | P/B 1.59 | P/S 1.22 | 3y earnings growth n/a
Yield: 1.3%
Three-year record: +12.6% a year | beta to the market 0.44
Cost and size: expense ratio 0.59% | net assets 620.12M
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: MercadoLibre Inc 22.2%, YPF SA ADR 10.6%, Vista Energy SAB de CV ADR 8.2%, Grupo Financiero Galicia SA ADR 5.4%, Pampa Energia SA ADR 4.8%
Sector mix: Consumer cyclical 28.3%, Energy 22.6%, Financial services 13.7%, Basic materials 10.3%
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
Rolled up from the 5 largest holdings, 51.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.61 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +75.0% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, PAM
Recent rating changes among them:
  - MELI: 2026-11-11 UBS: main, Neutral -> Neutral
  - YPF: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-10-13 UBS: main, Neutral -> Neutral
  - PAM: 2026-11-02 JP Morgan: main, Neutral -> Neutral
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
Share count change: 1 week: +8.9% (50.97M) over 7d | 1 month: +13.2% (72.63M) over 30d
Shares outstanding: 9.31M | fund size: 624.49M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, strong analyst coverage but bearish technical indicators lead to a neutral outlook.

**Main reasons it gave:**
- Technical trend: price below 20‑day, 50‑day and 200‑day SMAs (‑6.3% to ‑14.2%)
- Momentum indicators: RSI 35.9 and MACD negative (‑3.712 vs ‑2.856)
- Analyst consensus: 100% buy on 39.6% of fund weight, weighted price target +29.1%
- Fund flows: flat share count (+0.0% week, +0.0% month)
- Macro: no rate surprise; yields slightly down, VIX up but no extreme move

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 105.12 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 112.13 (-6.3%), 50d 117.72 (-10.7%), 200d 122.48 (-14.2%); 50d below 200d
Momentum: RSI(14) 35.9 | MACD -3.712 vs signal -2.856 (histogram -0.856)
Returns: 1d +3.6% | 5d -4.0% | 1m -12.3% | 3m -14.4%
52-week range: 100.50 - 137.69 (now 12.4% of the way up)
Volatility: ATR(14) 2.69 (2.6% of price) | annualised 20d 40.6%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.09 | P/B 2.45 | P/S 2.45 | 3y earnings growth n/a
Yield: 1.6%
Three-year record: +25.8% a year | beta to the market 0.98
Cost and size: expense ratio 0.59% | net assets 838.23M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Teva Pharmaceutical Industries Ltd 12.6%, Bank Leumi Le-Israel BM 8.6%, Bank Hapoalim BM 7.8%, Elbit Systems Ltd 5.6%, Tower Semiconductor Ltd 5.1%
Sector mix: Financial services 34.6%, Technology 18.0%, Healthcare 13.1%, Industrials 10.8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

```text
Rolled up from the 5 largest holdings, 39.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.00 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +29.1% above the current prices
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
Shares outstanding: 2.55M | fund size: 268.06M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows solid fundamentals, a bullish analyst rating, and strong inflows, but technicals indicate short‑term weakness and there were no macro surprises to drive a clear directional bias; thus the overall outlook remains neutral.

**Main reasons it gave:**
- Fund flows: share count +29.3% over past month indicating net inflows
- Technical: price 41.42 below 20‑day SMA 43.20 (-4.1%) and RSI 40.2 (bearish momentum)
- Analyst view: average rating 2.19 (near strong buy) and weighted price target +12% above current price
- Macro: no recent data surprise; inflation 3.7% and Fed target unchanged

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 41.42 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 43.20 (-4.1%), 50d 43.84 (-5.5%), 200d 40.82 (+1.5%); 50d above 200d
Momentum: RSI(14) 40.2 | MACD -0.620 vs signal -0.330 (histogram -0.290)
Returns: 1d +4.0% | 5d -5.3% | 1m -4.8% | 3m -7.3%
52-week range: 32.94 - 45.76 (now 66.1% of the way up)
Volatility: ATR(14) 0.87 (2.1% of price) | annualised 20d 32.8%
Volume: 0.07x the 20-day average
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
Three-year record: +27.8% a year | beta to the market 0.85
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

<details><summary><b>What analysts and big funds say</b> — score +0.41</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.41</summary>

```text
Rolled up from the 5 largest holdings, 46.6% of the fund by weight
Ratings by weight: buy 57.7% | hold 42.3% | sell 0.0% (mean 2.19 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.0% above the current prices
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
Share count change: 1 week: +4.4% (42.23M) over 7d | 1 month: +29.3% (229.13M) over 30d
Shares outstanding: 24.42M | fund size: 1.01B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Fund flows show strong buying pressure (7.5% weekly share increase), but technicals are in a downtrend (price below 20‑, 50‑ and 200‑day SMAs, RSI 33.3) and analyst consensus is modestly bearish (57.4% hold, 42.6% sell, mean rating 3.45). Macro risk‑off signals (VIX 26.8, upward‑sloping yield curve) add further downside pressure, while fundamentals remain neutral. With mixed indicators and no clear macro catalyst, we keep a neutral stance.

**Main reasons it gave:**
- Weekly share count up 7.5% (+86.9M) indicating strong inflows
- Price below 20‑, 50‑ and 200‑day SMAs; RSI 33.3 (bearish momentum)
- Analyst consensus: 57.4% hold, 42.6% sell, mean rating 3.45 (slightly bearish)
- VIX 26.8 (+3.9 on week) and normal upward‑sloping yield curve suggest risk‑off environment

<details><summary><b>News</b> — score +0.00</summary>

- [How Could Australia's CPI and Tokyo's CPI Shape iShares MSCI Australia ETF (NYSEARCA:EWA) This Week?](https://kalkine.com.au/news/economic-news/how-could-australias-cpi-and-tokyos-cpi-shape-ishares-msci-australia-etf-nysearcaewa-this-week)  
  <sub>Kalkine, 19 minutes ago</sub>  
  How Could Australia's CPI and Tokyo's CPI Shape iShares MSCI Australia ETF (NYSEARCA:EWA) This Week?
- [Why Did All Three Major US Indexes Slide Into Correction, and Where Does iShares Core S&P 500 ETF (NYSEARCA:IVV) Stand?](https://kalkine.com.au/news/economic-news/why-did-all-three-major-us-indexes-slide-into-correction-and-where-does-ishares-core-sp-500-etf-nysearcaivv-stand)  
  <sub>Kalkine, 19 minutes ago</sub>  
  Why Did All Three Major US Indexes Slide Into Correction, and Where Does iShares Core S&P 500 ETF (NYSEARCA:IVV) Stand?
- [What Could a Neutral Call From a Major Bank Mean for Vanguard Total Stock Market ETF (NYSEARCA:VTI)?](https://www.google.com/goto?url=CAESyAEBxCJF1_RdK3atPr5hq30GUKH1tQM1fWsDitfKlFZkYn0g-soWyoMjfCQZZjIjDRBtVkL2KTw7dAcfG-qUDUQ_FuCi0DjlrZRtdTQfRVU2vPYJ6N1_7bKRR-VTdQqybGWUdZko4i5BLtPa7rCLimrdpbvOeHrlTFCafmcDoyv8aHk7xzg859tcjA3PVd4pGzqFBeHGeuXzuxiy92Iqk_m06MpfWe_tprYYHdQLJoz_sTqIBMAv2pWl7Wvly8OZLUGKhLxt9pqM8g&gsessionid=EDi0FlumGOcZKdoCzB4haNOHqU3U44K3m3wgC2it5V-tWOXX-e8OKw)  
  <sub>Kalkine, 19 minutes ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports. Become a Kalkine member...
- [How Could a 2.8% Global Growth Forecast for 2027 Affect Vanguard Total World Stock ETF (NYSEARCA:VT)?](https://www.google.com/goto?url=CAESxwEBxCJF1_yDBytvvzMs9fpm9IM5cR4nTRkOb0XvOrCW5bxCEI-k-fwdQirRp9uSVcc8oNfL3BoXLvbf8xrcqULu2FGWgDCtFZzcO697XcwBQEUrBnhHXG4i5srLxpJffoIR0UjjszxW49HU0cZx_GERARtZoMbWi0_40czB9eCeda1__kG2CYG0o54--vH-dh3cK9WSuOBtAXN49Eeswnervr20kXm-Zyd3sUurcetTVAsvQeLTD3RVjttKGL8qmt3vREfKMYgN&gsessionid=EDi0FlumGOcZKdoCzB4haNOHqU3U44K3m3wgC2it5V-tWOXX-e8OKw)  
  <sub>Kalkine, 19 minutes ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports. Become a Kalkine member...
- [Why Did the 10 Year Yield Slip to 4.91% After Bessent's Fed Warning for iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT)?](https://www.google.com/goto?url=CAES2AEBxCJF11SEOlpmlog1Usnflnt6JEaDQjLEsaGjS5lsgHROR4zCdnnJk29GvNDZiDNUebqYVf8vrz0Hf9wx0MQVhsJHR5Tj-XUQ6-naemok0P3zSWFEJpI6sUXlPRDhth2mTpj5z5_bHMBhOv1Aw7ep9yAm0_4VieQ1deb62u5vhQo4vCagr6F3bD-p4BANtYKv16UiJa8Th2HYXfw3wcg4NX_4mbAJwFkTWty8DDymGSXzIFNCREcsFTynTZ0Ly3OipovjwyPANr_qgMEDlgW5b8WNbHyAmDk&gsessionid=EDi0FlumGOcZKdoCzB4haNOHqU3U44K3m3wgC2it5V-tWOXX-e8OKw)  
  <sub>Kalkine, 19 minutes ago</sub>  
  Why Did the 10 Year Yield Slip to 4.91% After Bessent's Fed Warning for iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT)?
- [What Would the S&P 500 Under Every 2026 Forecast Mean for iShares Core S&P 500 ETF (NYSEARCA:IVV)?](https://www.google.com/goto?url=CAESxAEBxCJF16r3ASHY1Rn3f2tDGQsjZLz2XXPOPlPZSrUPOMTDp6IVcr_hovWHS1rreAvozhIh1dsAVjxq_uxwKWVScEJ37sygMJNYv04e-pKiCGVms6sETeybckD5LQoed0opjUrRVMqtGDtI7rMtpx9eNvXEZqDtXhmK9-cI-eKr18WaUrBTjOOSuZMXHRtNc7Ue7HxL_vGBlBoHLk05V6VnjiOP_RQDJef7-d8ZQT9COSQX05EAGxg1QkGNBEaEsh-Ub5N9&gsessionid=EDi0FlumGOcZKdoCzB4haNOHqU3U44K3m3wgC2it5V-tWOXX-e8OKw)  
  <sub>Kalkine, 19 minutes ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [How Does Japan's Labour Thanksgiving Day Closure on November 23 Shape the Outlook for iShares MSCI Japan ETF (NYSEARCA:EWJ)?](https://www.google.com/goto?url=CAES3wEBxCJF1wKj01tBM00RyR0Fkei92UGLnOZdi5k1nyAtfc3KHFCnE8MwFXVdh-d7WLC1aibxxct9iOowin1IsmsTi8fdEkmudpoq10lEjSxkh7RU-mAX7R5ZMjaGRy0ksLxn8P9JynaLsLsUI_yuVZsniLwvG4lXWk4DnLKcq0H_-2E51YosowXcECbMCsNaPcR6EZjiiruWQarH3Kx9BdieNmHZEoJ6OHXnlQBI3mPiPkcY2rBd8wY0fVFFoQUf1ZIujcpynFrwgxXxOA_utO6QxaVBBJutglHTlA5Kmpd0&gsessionid=EDi0FlumGOcZKdoCzB4haNOHqU3U44K3m3wgC2it5V-tWOXX-e8OKw)  
  <sub>Kalkine, 19 minutes ago</sub>  
  How Does Japan's Labour Thanksgiving Day Closure on November 23 Shape the Outlook for iShares MSCI Japan ETF (NYSEARCA:EWJ)?

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 27.23 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 28.87 (-5.7%), 50d 28.75 (-5.3%), 200d 28.98 (-6.1%); 50d below 200d
Momentum: RSI(14) 33.3 | MACD -0.454 vs signal -0.171 (histogram -0.283)
Returns: 1d +1.9% | 5d -4.7% | 1m -6.5% | 3m -10.5%
52-week range: 25.33 - 30.43 (now 37.2% of the way up)
Volatility: ATR(14) 0.42 (1.5% of price) | annualised 20d 21.3%
Volume: 0.09x the 20-day average
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
Three-year record: +9.8% a year | beta to the market 0.94
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

<details><summary><b>What analysts and big funds say</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.25</summary>

```text
Rolled up from the 5 largest holdings, 46.5% of the fund by weight
Ratings by weight: buy 0.0% | hold 57.4% | sell 42.6% (mean 3.45 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -2.3% above the current prices
Holdings read: BHP.AX, CBA.AX, NAB.AX, WBC.AX, ANZ.AX
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
Share count change: 1 week: +7.5% (86.90M) over 7d | 1 month: +9.0% (103.30M) over 36d
Shares outstanding: 45.91M | fund size: 1.25B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows modestly bullish fundamentals and strong recent inflows, but technical indicators are bearish and there is no new macro surprise or news catalyst. With mixed signals and no decisive technical break, a neutral stance is warranted.

**Main reasons it gave:**
- No news found in past 24h
- Price below 20‑, 50‑ and 200‑day SMAs, RSI 41.6 (bearish technicals)
- Share count +19% over past month, indicating strong inflows
- Analyst consensus 100% buy with weighted price target +12.3%

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 49.93 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 51.91 (-3.8%), 50d 51.24 (-2.6%), 200d 51.48 (-3.0%); 50d below 200d
Momentum: RSI(14) 41.6 | MACD -0.367 vs signal 0.058 (histogram -0.425)
Returns: 1d +3.0% | 5d -3.9% | 1m -0.9% | 3m -8.1%
52-week range: 46.06 - 54.72 (now 44.7% of the way up)
Volatility: ATR(14) 0.90 (1.8% of price) | annualised 20d 28.1%
Volume: 0.03x the 20-day average
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
Three-year record: +14.3% a year | beta to the market 1.18
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 33.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.99 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.3% above the current prices
Holdings read: SPOT, VOLV-B.ST, ATCO-A.ST, SAND.ST, ASSA-B.ST
Recent rating changes among them:
  - SPOT: 2026-10-23 Morgan Stanley: main, Overweight -> Overweight
  - ASSA-B.ST: 2015-12-09 Barclays: main, ? -> Equal-Weight
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
Share count change: 1 week: +5.0% (52.01M) over 7d | 1 month: +19.0% (175.63M) over 36d
Shares outstanding: 22.06M | fund size: 1.10B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technicals show the price below key moving averages, a weak RSI, and negative MACD, but low volume reduces the reliability of the bearish signal. Fundamentals are solid with moderate valuation and a strong three‑year performance. Analyst coverage is overwhelmingly bullish with a +21.5% price target. Recent fund flows are positive, showing a 5.1% share count increase over the past week. No macro surprise or policy shift was observed, so the overall stance remains neutral.

**Main reasons it gave:**
- Price below 20d, 50d and 200d SMAs
- RSI at 39.8 indicating near‑oversold momentum
- Analyst consensus 90.8% buy with +21.5% price target
- Share count rose 5.1% in the past week (creations)
- No macro surprise: yields down slightly, VIX up modestly

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 54.85 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 56.89 (-3.6%), 50d 57.50 (-4.6%), 200d 58.27 (-5.9%); 50d below 200d
Momentum: RSI(14) 39.8 | MACD -0.516 vs signal -0.200 (histogram -0.317)
Returns: 1d +1.8% | 5d -4.6% | 1m -0.2% | 3m -13.0%
52-week range: 50.70 - 63.35 (now 32.8% of the way up)
Volatility: ATR(14) 0.99 (1.8% of price) | annualised 20d 30.5%
Volume: 0.02x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.58 | P/B 1.75 | P/S 1.42 | 3y earnings growth n/a
Yield: 3.4%
Three-year record: +22.0% a year | beta to the market 0.92
Cost and size: expense ratio 0.50% | net assets 1.19B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: UniCredit SpA 16.4%, Intesa Sanpaolo 13.8%, Enel SpA 11.7%, Eni SpA 5.5%, Generali 4.8%
Sector mix: Financial services 50.9%, Utilities 18.2%, Industrials 11.9%, Consumer cyclical 8.4%
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
Rolled up from the 5 largest holdings, 52.1% of the fund by weight
Ratings by weight: buy 90.8% | hold 9.2% | sell 0.0% (mean 2.14 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.5% above the current prices
Holdings read: UCG.MI, ISP.MI, ENEL.MI, ENI.MI, G.MI
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
Share count change: 1 week: +5.1% (57.43M) over 7d | 1 month: +4.1% (46.13M) over 36d
Shares outstanding: 21.56M | fund size: 1.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> There is no fresh news affecting the fund, the technical picture is mixed (price above the 50‑day and 200‑day SMAs but below the 20‑day SMA, RSI 45.4 and MACD histogram negative), fundamentals are modestly positive (reasonable valuation and strong three‑year performance), analyst coverage is mildly bullish (64.8% buy and a +4.3% price target), and fund flows are flat, while macro data show no surprise. All factors lead to a neutral outlook.

**Main reasons it gave:**
- No news in the past 24 hours
- Technical indicators mixed: price below 20‑day SMA but above 50‑day and 200‑day SMAs; RSI 45.4 and MACD histogram negative
- Analyst consensus 64.8% buy with weighted price target +4.3% above current price
- Flat fund flows (share count unchanged) indicating no recent demand shift
- Macro backdrop unchanged: Treasury yields slightly down, no policy surprise, VIX modestly higher

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 62.74 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 64.30 (-2.4%), 50d 62.13 (+1.0%), 200d 62.02 (+1.2%); 50d above 200d
Momentum: RSI(14) 45.4 | MACD 0.109 vs signal 0.563 (histogram -0.454)
Returns: 1d +1.5% | 5d -3.0% | 1m -0.5% | 3m -3.0%
52-week range: 56.31 - 66.56 (now 62.7% of the way up)
Volatility: ATR(14) 0.84 (1.3% of price) | annualised 20d 21.1%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Focused Region
What it holds: P/E 23.89 | P/B 4.18 | P/S 2.64 | 3y earnings growth n/a
Yield: 1.7%
Three-year record: +13.7% a year | beta to the market 0.82
Cost and size: expense ratio 0.50% | net assets 3.02B
What it is made of: Stocks 99.0%, Cash 1.0%
Largest holdings: Roche Holding AG Ordinary Shares new 15.0%, Novartis AG Registered Shares 12.9%, Nestle SA 11.4%, UBS Group AG Registered Shares 5.8%, Zurich Insurance Group AG 4.6%
Sector mix: Healthcare 40.1%, Financial services 19.2%, Consumer defensive 13.5%, Industrials 11.2%
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
Rolled up from the 5 largest holdings, 49.6% of the fund by weight
Ratings by weight: buy 64.8% | hold 35.2% | sell 0.0% (mean 2.46 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.3% above the current prices
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

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technicals show the price trading below its 20‑day, 50‑day and 200‑day moving averages and MACD is negative, indicating mild downside pressure, but the one‑day rally is modest and volume is very low, so no decisive break. Analyst coverage of the five largest holdings (42.3% of the fund) is uniformly buy with a hefty +64% price target, but it covers less than half of the fund, limiting the impact. Share‑count flows have been flat for the past month, suggesting no net demand. Macro conditions are unchanged – yields marginally lower, curve still upward, VIX elevated but no surprise data – providing no strong directional cue. With no clear catalyst, the overall view remains neutral.

**Main reasons it gave:**
- Price 60.74 below 20‑day (63.78), 50‑day (65.39) and 200‑day (65.15) SMAs
- Analyst consensus 100% buy on 42.3% of fund, weighted price target +64.1%
- Weekly and monthly share count flat (0% change), indicating neutral flow
- Low volume at 0.03× 20‑day average, suggesting limited market participation

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 60.74 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 63.78 (-4.8%), 50d 65.39 (-7.1%), 200d 65.15 (-6.8%); 50d above 200d
Momentum: RSI(14) 38.6 | MACD -1.331 vs signal -0.868 (histogram -0.464)
Returns: 1d +4.1% | 5d -3.9% | 1m -4.8% | 3m -12.5%
52-week range: 55.33 - 71.61 (now 33.2% of the way up)
Volatility: ATR(14) 1.34 (2.2% of price) | annualised 20d 34.1%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.38 | P/B 2.46 | P/S 1.73 | 3y earnings growth n/a
Yield: 4.4%
Three-year record: +14.7% a year | beta to the market 1.13
Cost and size: expense ratio 0.50% | net assets 597.52M
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ASML Holding NV 21.9%, ING Groep NV 8.6%, Prosus NV Ordinary Shares - Class N 4.7%, ASM International NV 3.8%, Nebius Group NV Shs Class-A- 3.4%
Sector mix: Technology 30.4%, Financial services 21.1%, Consumer defensive 11.8%, Industrials 11.0%
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
Rolled up from the 5 largest holdings, 42.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +64.1% above the current prices
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
Shares outstanding: 5.55M | fund size: 337.08M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows modest bearish technical signals (price below multiple SMAs, weak momentum and very low volume) while macro conditions are risk‑off (high VIX, strong dollar). Fundamentals remain solid and analyst consensus is bullish, but there is no material macro surprise, earnings catalyst, or decisive technical breakout to justify a directional shift. Flows are flat, indicating no new investor conviction. Hence a neutral stance is appropriate.

**Main reasons it gave:**
- Price $56.42 below 20‑day SMA $58.04, 50‑day SMA $58.68 and 200‑day SMA $58.17
- RSI 40.8 and MACD -0.445 (negative) indicate bearish momentum
- VIX 26.76, up 3.9 points weekly, reflects heightened market volatility
- Analyst coverage: 76.3% buy rating with weighted price target +11.9% above current price

<details><summary><b>News</b> — score +0.00</summary>

- [How Do iShares MSCI Spain ETF (NYSEARCA:EWP), iShares MSCI India ETF (CBOE:INDA) and iShares MSCI New Zealand ETF (NASDAQ:ENZL) Connect to a USD 1.7 Billion Brookfield (NYSE:BN) Deal?](https://www.google.com/goto?url=CAESjwIBxCJF10rt3xWmqMqej6mXbrUnLZO0xTY-XeCdymupZpItJM3vXvpiSsjZpXPRiaVoGJNnpJG7yAn4BJyT9EJwTwsm-C3jSnJvXMFWjKEZ5JP8eD7IJn3wa-C6wl9LAgxa5Ts2-0GtOvcpy2POd3zuzO1rNb1owpdOhPzGkxIXu4_StSAlFdxwj3Mgb7cZyv2o9zA95gVaLarv1mp2eZiT4wB5enKOGqvll1RMf1pmo0XzHgT5yg18-QLgxQQDeO1Pwwgg8DMmDvS-R6ninw_cvuXDJgYhK4dZmus-xZG1QkvS12lhk6_keHIB2I2JB7ogCQOHoQEdqsF7Ch3pGC7g9hPFEjCl_xleQNP47r9F&gsessionid=LjQS6poVMJ42K3j3s-wjjfFCwHBgN_FN0T6_e50mMUhK23PblzF0uw)  
  <sub>Kalkine, 20 minutes ago</sub>  
  How Do iShares MSCI Spain ETF (NYSEARCA:EWP), iShares MSCI India ETF (CBOE:INDA) and iShares MSCI New Zealand ETF (NASDAQ:ENZL) Connect to a USD 1.7 Billion...
- [What Could Partners Group's NZD 1.2 Billion Purchase of Ferry Operator StraitNZ Signal for iShares MSCI New Zealand ETF (NASDAQ:ENZL)?](https://kalkine.com.au/news/announcements/what-could-partners-groups-nzd-12-billion-purchase-of-ferry-operator-straitnz-signal-for-ishares-msci-new-zealand-etf-nasdaqenzl)  
  <sub>Kalkine, 20 minutes ago</sub>  
  What Could Partners Group's NZD 1.2 Billion Purchase of Ferry Operator StraitNZ Signal for iShares MSCI New Zealand ETF (NASDAQ:ENZL)?
- [What Does Tata Steel's USD 1.67 Billion APL Apollo Tubes Stake Mean for iShares MSCI India ETF (CBOE:INDA)?](https://www.google.com/goto?url=CAESzAEBxCJF143w62z4xwdTwCuvqmliZ5XfZJO99OF8U2gbUGg_YpdMiBLt-aU7VFf3dCYT1NaBhZu5G9gvavHNFOZdMg1B4POu7TpAwcEPMW_OWEZwlUoGjQgFpZth1vlWS_2UpOkd3m7gJxDdQfu_Sw1ovp2t2Lh_zrYHL8PeV-23FML1IbHCiqFpfMdjB4wHgdzrkQoNOeYKGJwZUvWVJXvJ2Ay2GeLWhBo6hocc9y1c-s8YMGPACpoyzUpQ7NiGLu0xkfp3qJU52baEcvI&gsessionid=LjQS6poVMJ42K3j3s-wjjfFCwHBgN_FN0T6_e50mMUhK23PblzF0uw)  
  <sub>Kalkine, 19 minutes ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [What Would a Beijing Red-Chip Listing Rule Mean for KraneShares CSI China Internet ETF (NYSEARCA:KWEB)?](https://www.google.com/goto?url=CAESygEBxCJF13s51bg6vl-hSd3WAMrdoJ6b6BMcGrxaCzKt603CLvPxHsu2YqilQPEn80srOlbGqnVV2xFP4p9GyH5z46lMcgqW1NBONp9K7l_ZJnOFWWH4ePKQonJ0iCHNXfiG7KlfooF9ZKfJG7JZXt894kKNqx_pErJB6BIlat4nOCHA_QNXwFQ3-PnPT2DZFdQrsadNG46L0sto6lmGYzwoD4QHcSVTb18SAxnf8XXP6W91kAz20L81sWsTq2ki3B92qXgvf-EmDz18&gsessionid=LjQS6poVMJ42K3j3s-wjjfFCwHBgN_FN0T6_e50mMUhK23PblzF0uw)  
  <sub>Kalkine, 19 minutes ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports. Become a Kalkine member...
- [How Should Investors Weigh Tesla (NASDAQ:TSLA) and SpaceX Before a Possible Merger Announcement Next Month?](https://www.google.com/goto?url=CAESzgEBxCJF172JkiRk13IVQIPmp-qQdjZJ546I4SXr4Q0jqZ7MOWadbLbyQafbaJ_y6kTZQFpZZuj2TvsWglW2CgG0utqDWo5hdTk5C3sNQItD4f_Zr19m8lu1QDFRgIMBDhHt7qq6nl6AVXOubBAMH094p_QZS_7NydbA9MDkemnOx-HRZlIt1LsnjFzLvf9aZZUXkX1HXAjg3S6oIsvn6e0-QcBgo4koAHVIq5MLoICprBaOVCHq6pl2SibqQQtqB44g5uL-s8u7xmnkLjHVtg&gsessionid=LjQS6poVMJ42K3j3s-wjjfFCwHBgN_FN0T6_e50mMUhK23PblzF0uw)  
  <sub>Kalkine, 20 minutes ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [How Does ConocoPhillips (NYSE:COP) Signed USD 4.425 Billion Deal Stack Up Against United States Brent Oil Fund (NYSEARCA:BNO), BHP Group (NYSE:BHP) and Ashland (NYSE:ASH)?](https://www.google.com/goto?url=CAESgwIBxCJF10tOGyrM-ADiZcl6BY-fXxDIm5GtvIzedkNbFIsG7rVXdIXr5A-baGYcmgnSdMr-M-EORObDFRHeutaf5IjGtMK1ZvSvUBLRsTC7TpQuiLtVW96wIMhoztzJZmv60KylsrcmfbayCx8VSUTm9VtYR-wL18HbZ-NErDrNMp1j5k5LRr9mbkU2aEOpvHGKkKfhfVgolbpk4fNCZCEbO1yzsY9GhD62OgBGmLFwaetSgJjtjqtp6cLh-ob1szsnQ18seIlRT5dgP8S-KSFp1c5WsmvCfCEl6-ckygVK3D95Q47Whtplx_N0IlGRz5UoHx8KLIH4GWo5_YmBN4ZyCGsO&gsessionid=LjQS6poVMJ42K3j3s-wjjfFCwHBgN_FN0T6_e50mMUhK23PblzF0uw)  
  <sub>Kalkine, 20 minutes ago</sub>  
  How Does ConocoPhillips (NYSE:COP) Signed USD 4.425 Billion Deal Stack Up Against United States Brent Oil Fund (NYSEARCA:BNO), BHP Group (NYSE:BHP) and...
- [Aland Equity Group Receives First $374,000 Management Fee Payment from Elm Grove Fund](https://www.google.com/goto?url=CAESuQEBxCJF15n5BosiMIXBymkAkB-2denC_K1YZZAuqaC2mdWHPZPINCXzRKSWVG3b7qP-qkoQfQhYnsWrdhHV5d7A-djuQDlAjjfMNQsk9Z1wOJQ9eVZ_EzdKvf1mKTqXzwwPtJdR56xvW7IBXLPcfRVvwiYnKQ6CM6LXx7rdUPjw98rSxwehmPJnCgPMMNW9ll1z1d4dSsrOritho-FQ6qn3KwG70sRAaCx2go789gy6Dv3JvyJVTl9mPQ&gsessionid=LjQS6poVMJ42K3j3s-wjjfFCwHBgN_FN0T6_e50mMUhK23PblzF0uw)  
  <sub>Kalkine, 16 hours ago</sub>  
  Aland Equity Group Limited (ASX:AEG) has received its first $374000 investment management fee from the Aland Elm Grove Estate Fund following shareholder...
- [Barkly Rare Earths Records Highest-Grade Intercept at 18,086 ppm TREO over 0.5 m in Phase 1 Drilling](https://www.google.com/goto?url=CAESyQEBxCJF1_JDRwX2521R0zqxFSJg4futhv_kPGDicrY2K6NQIZDukrrjnqlf0gsjSqbT2c-s9mRhMvSh1VgyneToMwGPpgaVuiHaN-DPcoegjQ8_533gOaNRBhCEZhnKuodlE_SH7T8crCF_IZnnyvTfx165ZlOVXxNZLeI2CUteXUgBvTzeMEWh1Bixj3r00Gcqf-fDvqpZSDSXFoOG8hrUvUyupTAilj9Si7HfrwaqCobDFpt3Y2KMsF-HsfC_8WTcc2MB-mAqV8A&gsessionid=LjQS6poVMJ42K3j3s-wjjfFCwHBgN_FN0T6_e50mMUhK23PblzF0uw)  
  <sub>Kalkine, 16 hours ago</sub>  
  Barkly Rare Earths Limited (ASX:BAK) has reported assay results for a further 38 holes from the Phase 1 drilling programme at its Barkly Project in the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 56.42 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 58.04 (-2.8%), 50d 58.68 (-3.9%), 200d 58.17 (-3.0%); 50d above 200d
Momentum: RSI(14) 40.8 | MACD -0.445 vs signal -0.155 (histogram -0.290)
Returns: 1d +1.8% | 5d -4.6% | 1m -1.9% | 3m -10.7%
52-week range: 49.73 - 63.23 (now 49.6% of the way up)
Volatility: ATR(14) 0.99 (1.8% of price) | annualised 20d 27.2%
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
Three-year record: +26.8% a year | beta to the market 0.91
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 53.1% of the fund by weight
Ratings by weight: buy 76.3% | hold 23.7% | sell 0.0% (mean 2.29 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.9% above the current prices
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
Shares outstanding: 37.35M | fund size: 2.11B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technicals show a modest downtrend and weak momentum, while strong fund inflows and a bullish analyst consensus provide positive support. Macro indicators are stable with no surprising data, leading to a neutral stance.

**Main reasons it gave:**
- Price 45.47 below 20‑day (47.27), 50‑day (47.18) and 200‑day (47.07) SMAs
- RSI 38.2 and MACD -0.469 vs signal -0.137 indicate weak momentum
- Share count increased +5.1% over the past week, indicating net inflows
- Analyst consensus 100% buy with +20.1% weighted price target for top holdings
- Macro data aligned with expectations (inflation 3.7% below Fed target, no rate surprise)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 45.47 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 47.27 (-3.8%), 50d 47.18 (-3.6%), 200d 47.07 (-3.4%); 50d above 200d
Momentum: RSI(14) 38.2 | MACD -0.469 vs signal -0.137 (histogram -0.332)
Returns: 1d +1.6% | 5d -4.4% | 1m -4.3% | 3m -7.9%
52-week range: 41.92 - 49.39 (now 47.5% of the way up)
Volatility: ATR(14) 0.69 (1.5% of price) | annualised 20d 23.2%
Volume: 0.04x the 20-day average
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
Three-year record: +16.1% a year | beta to the market 0.66
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

```text
Rolled up from the 5 largest holdings, 36.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.07 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.1% above the current prices
Holdings read: SHEL.L, HSBA.L, AZN.L, ULVR.L, RR.L
Recent rating changes among them:
  - AZN.L: 2026-08-24 CICC: init, ? -> Outperform
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
Share count change: 1 week: +5.1% (181.33M) over 7d | 1 month: +5.1% (180.39M) over 36d
Shares outstanding: 82.29M | fund size: 3.74B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows a modestly bearish technical picture, with price below key moving averages and negative momentum, while fundamentals appear relatively attractive (low P/E, decent yield) and analyst consensus is strongly bullish (+16.9% price target). However, there is no macro surprise or new data to drive a directional shift, and fund flows are flat, indicating no net demand. Given the mixed signals and lack of a clear catalyst, a neutral stance is appropriate.

**Main reasons it gave:**
- Price 73.19 below 20‑day SMA 75.53 (downtrend)
- RSI 40.8 and MACD negative indicating weak momentum
- Analyst consensus 100% buy with +16.9% price target
- Flat fund flows (share count unchanged) showing neutral demand
- No macro surprise; yields stable and VIX elevated at 26.8

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 73.19 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 75.53 (-3.1%), 50d 74.18 (-1.3%), 200d 76.10 (-3.8%); 50d below 200d
Momentum: RSI(14) 40.8 | MACD -0.239 vs signal 0.330 (histogram -0.569)
Returns: 1d +1.4% | 5d -4.2% | 1m -2.8% | 3m -6.0%
52-week range: 66.04 - 81.23 (now 47.1% of the way up)
Volatility: ATR(14) 1.51 (2.1% of price) | annualised 20d 21.9%
Volume: 0.15x the 20-day average
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
Three-year record: +8.5% a year | beta to the market 0.99
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 47.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.9% above the current prices
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

> No macro surprise, flat fund flows, weak technicals, and a bullish analyst view that only covers 41.8% of the fund.

**Main reasons it gave:**
- Flat fund flows: 0% change in share count over week and month
- Technical weakness: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 38.2; MACD negative
- No macro catalyst: Treasury yields unchanged, VIX up modestly, no policy surprise
- Analyst view bullish but covers only 41.8% of the fund (100% buy, +40.4% price target)

<details><summary><b>News</b> — score +0.00</summary>

- [EZA: Your Gateway To Investing In South Africa (NYSEARCA:EZA)](https://seekingalpha.com/article/4971070-eza-your-gateway-to-investing-in-south-africa)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  The iShares MSCI South Africa ETF (EZA) offers a concentrated, high-income South African equity portfolio for investors with aggressive risk appetites.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 59.17 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 63.62 (-7.0%), 50d 64.49 (-8.3%), 200d 67.62 (-12.5%); 50d below 200d
Momentum: RSI(14) 38.2 | MACD -1.575 vs signal -0.694 (histogram -0.881)
Returns: 1d +5.2% | 5d -6.1% | 1m -6.3% | 3m -18.4%
52-week range: 56.26 - 81.60 (now 11.5% of the way up)
Volatility: ATR(14) 1.82 (3.1% of price) | annualised 20d 42.7%
Volume: 0.08x the 20-day average
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
Three-year record: +17.8% a year | beta to the market 1.12
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.98 on a 1=strong buy to 5=strong sell scale)
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
Shares outstanding: 7.90M | fund size: 467.40M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Gold miners ETF GDX faces mixed signals: bearish macro news as gold prices fell to a 14‑month low and technicals show the price well below its short‑ and long‑term moving averages with weak momentum, but analyst coverage is overwhelmingly positive (100% buy on 42% of the fund) with a +33.8% price target, and recent inflows (+13.9% week‑over‑week) indicate strong demand for the exposure. No policy surprise or decisive technical breakout on heavy volume occurred, so the overall stance remains neutral.

**Main reasons it gave:**
- Gold price fell to a 14‑month low (news)
- GDX price below 20‑, 50‑ and 200‑day SMAs; RSI 37.7; MACD negative (technical)
- Analyst consensus 100% buy on 42% of fund weight; price target +33.8% (analyst view)
- Share count up 13.9% week‑over‑week (+$2.92B) indicating inflows (fund flows)

<details><summary><b>News</b> — score -0.60</summary>

- [YieldMax Gold Miners ETF (GDXY) down 23% since ...](https://pluang.com/en/news-feed/gdxy-terlalu-diperdagangkan-dengan-pelindung-minimal-setelah-emas-mencapai-3500)  
  <sub>Pluang, 22 hours ago</sub>  
  The YieldMax Gold Miners Option Income Strategy ETF (GDXY) has declined about 23% in total returns since May. Its strategy of fully overwritten call spreads...
- [GDXY: Fully Overwritten, Barely Cushioned - What’s Left After Gold Hit $3,500](https://seekingalpha.com/article/4970936-gdxy-fully-overwritten-barely-cushioned-whats-left-after-gold-hit-3500)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  YieldMax Gold Miners Option Income Strategy ETF (GDXY) remains a cautious Hold: its option overlay offers limited protection while constraining rebounds.
- [Global X Silver Miners ETF (SIL) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXXkWdtxWj28aRfAWroruUPAiNk9a0bD73Ujf5RmssFYDDOdmWcLIO18rLSeU7t9XwXVzDuZO9sLt1AlM1V52JsCAyyjUldg52_TnmgJnlaVEUj1wtiAs1SmZJQP0yp8Lw&gsessionid=0-IynSg4bUnJ7jRSsqS2j8pkJC70ho1VGr0SOb7E_k3_PmOD0pqVew)  
  <sub>Yahoo Finance Singapore, 18 hours ago</sub>  
  Find the latest Global X Silver Miners ETF (SIL) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [AI Rout Turns Gold Into Source Of Cash: What Comes Next?](https://www.google.com/goto?url=CAESrwEBxCJF16RMBbO02d-RWKxZ9kaci-uP2i-ZrQ9e28cDLabJHJkU7xeCWxSick-7LVCQv7lVoMfAQKIfjWlRQ7-wWfbbOyWFIzR1r91yvi6VVkUTSJahy568YN6EitapuL3rfSbJlehtVPmQJ8gwRvdiAMIict7ML-VqU9uF6nfcxSEbJoO_ayep1U7HDSpS0Str-jytdMwcO1ZfU6LqF0qybspBIrFPtFddI_Kiz35i&gsessionid=0-IynSg4bUnJ7jRSsqS2j8pkJC70ho1VGr0SOb7E_k3_PmOD0pqVew)  
  <sub>Benzinga, 20 hours ago</sub>  
  Gold fell to a 14-month low on Friday as a rout in technology shares prompted investors to sell bullion to cover losses elsewhere.
- [Massif Capital Q3 2026 Letter To Investors](https://www.google.com/goto?url=CAESkAEBxCJF15KjISfXsI-UTyJL3sbFUm51x7aDgDLZEQtPeXMAEu17oDn5LqyWVshT9kWDQwAXRz1AezYq5it-CiGZjM1fqXdnOG3gI6-Ygepj3mJ9qDp0dQLdsgPWuTJtLShByfk0_tO0SAN9O3EbZv9UxSws6NkhZ4yacLdZEWF2FbwyswbMDCmsfAPyjnCQGkI&gsessionid=0-IynSg4bUnJ7jRSsqS2j8pkJC70ho1VGr0SOb7E_k3_PmOD0pqVew)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  During the third quarter of 2026, the Massif Capital Real Assets Strategy fell 2.07% net of fees, bringing year-to-date returns to 8.5% net of fees.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.60</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.70</summary>

```text
Last close 72.58 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 80.66 (-10.0%), 50d 85.50 (-15.1%), 200d 88.94 (-18.4%); 50d below 200d
Momentum: RSI(14) 37.7 | MACD -3.503 vs signal -2.269 (histogram -1.234)
Returns: 1d +6.1% | 5d -8.1% | 1m -9.5% | 3m -31.2%
52-week range: 68.40 - 115.84 (now 8.8% of the way up)
Volatility: ATR(14) 3.78 (5.2% of price) | annualised 20d 66.1%
Volume: 0.31x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Equity Precious Metals
What it holds: P/E 12.25 | P/B 2.71 | P/S 3.99 | 3y earnings growth n/a
Yield: 0.8%
Three-year record: +35.4% a year | beta to the market 0.98
Cost and size: expense ratio 0.51% | net assets 23.82B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Newmont Corp 11.6%, Agnico Eagle Mines Ltd 11.3%, Barrick Mining Corp 8.2%, Wheaton Precious Metals Corp 5.5%, Franco-Nevada Corp 5.5%
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 42.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.70 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +33.8% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, FNV.TO
Recent rating changes among them:
  - NEM: 2026-10-27 Scotiabank: main, Sector Outperform -> Sector Outperform
  - AEM.TO: 2026-11-02 Freedom Broker: up, Hold -> Buy
  - ABX.TO: 2026-11-10 JP Morgan: main, Overweight -> Overweight
  - WPM.TO: 2026-10-08 UBS: main, Buy -> Buy
  - FNV.TO: 2026-11-12 HC Wainwright & Co.: reit, Buy -> Buy
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
Share count change: 1 week: +13.9% (2.92B) over 7d | 1 month: +8.7% (1.91B) over 30d
Shares outstanding: 331.06M | fund size: 24.03B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technical indicators are bearish (price below 20‑ and 50‑day SMAs, RSI 37, MACD negative) while analyst coverage is strongly bullish (100% buy, +39% price target). Macro data show no surprise and fund flows are flat, providing no clear directional catalyst. The mix of these factors leads to a neutral stance.

**Main reasons it gave:**
- Price below 20‑day SMA (101.14) and 50‑day SMA (105.23)
- RSI(14) at 37.1 indicating weak momentum
- Analyst ratings 100% buy with weighted price target +39.4% above current price
- Fund flows flat: 0% share count change week and month
- Macro: yields unchanged, VIX up to 26.76 indicating stressed market

<details><summary><b>News</b> — score +0.10</summary>

- [Anthropic Stock Trend, Jensen Huang’s Potential Return As Nvidia CEO And Dell’s Q4 Results To Keep Tech Investors Busy This Week](https://www.tradingview.com/news/stocktwits:c532c2006094b:0-anthropic-stock-trend-jensen-huang-s-potential-return-as-nvidia-ceo-and-dell-s-q4-results-to-keep-tech-investors-busy-this-week/)  
  <sub>TradingView, 9 hours ago</sub>  
  Investors will track ANT's first-week run for valuation sustainability and potential read-throughs for other AI stocks. Dell's report on Tuesday will test...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 94.83 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 101.14 (-6.2%), 50d 105.23 (-9.9%), 200d 94.49 (+0.4%); 50d above 200d
Momentum: RSI(14) 37.1 | MACD -3.191 vs signal -2.424 (histogram -0.767)
Returns: 1d +3.5% | 5d -4.2% | 1m -14.3% | 3m -6.9%
52-week range: 74.67 - 112.67 (now 53.0% of the way up)
Volatility: ATR(14) 3.37 (3.6% of price) | annualised 20d 36.7%
Volume: 0.11x the 20-day average
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
Three-year record: +6.5% a year | beta to the market 1.25
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 42.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.59 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +39.4% above the current prices
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
Shares outstanding: 12.50M | fund size: 1.19B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Macro data shows stable yields and no surprise in inflation or unemployment, while the technicals indicate a bearish trend (price below 20-day, 50-day and 200-day SMAs and negative MACD), but the fund has experienced very strong inflows (+204% share count in 30 days) and analysts rate 100% of the major holdings as buy with a +22% price target, resulting in a balanced view and a neutral directional call.

**Main reasons it gave:**
- Technical: price 67.90 below 20-day SMA 70.12 (-3.2%) and 50-day SMA 69.81 (-2.7%)
- Technical: MACD -0.529 below signal -0.134 indicating bearish momentum
- Fund flows: share count +204.1% over 30 days (8.16 B) signaling strong inflows
- Analyst view: 100% buy ratings with weighted price target +22% above current price
- Macro: yields stable (10-year 4.98% -0.14 wk), VIX up to 26.76, no data surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Is Tesla (NASDAQ:TSLA)'s 7.64% Fall a Sign for SPDR S&P Retail ETF (NYSEARCA:XRT), Delta Air Lines (NYSE:DAL) and Global X Robotics & Artificial Intelligence ETF (NASDAQ:BOTZ)?](https://kalkine.com.au/news/general-news/is-tesla-nasdaqtslas-764-fall-a-sign-for-spdr-sp-retail-etf-nysearcaxrt-delta-air-lines-nysedal-and-global-x-robotics-artificial-intelligence-etf-nasdaqbotz)  
  <sub>Kalkine, 16 minutes ago</sub>  
  Is Tesla (NASDAQ:TSLA)'s 7.64% Fall a Sign for SPDR S&P Retail ETF (NYSEARCA:XRT), Delta Air Lines (NYSE:DAL) and Global X Robotics & Artificial...
- [What Hit Tesla (NASDAQ:TSLA), United States Oil Fund (NYSEARCA:USO), iShares Bitcoin Trust (NASDAQ:IBIT) and SPDR Gold Shares (NYSEARCA:GLD) as Bitcoin Slid to USD 55,106?](https://kalkine.com.au/news/general-news/what-hit-tesla-nasdaqtsla-united-states-oil-fund-nysearcauso-ishares-bitcoin-trust-nasdaqibit-and-spdr-gold-shares-nysearcagld-as-bitcoin-slid-to-usd-55106)  
  <sub>Kalkine, 16 minutes ago</sub>  
  What Hit Tesla (NASDAQ:TSLA), United States Oil Fund (NYSEARCA:USO), iShares Bitcoin Trust (NASDAQ:IBIT) and SPDR Gold Shares (NYSEARCA:GLD) as Bitcoin Slid...
- [Himalaya Shipping Enters New Time Charter for Mount Ita](https://www.google.com/goto?url=CAESqAEBxCJF16rdN0wdQN24mxq0HPgo-y8FC6C05LbNp4d5mifcHhaxI6r3L0F-F7krOaRBoAQHsyoSowMVQJDzujnI2UnJXypEd17NHSsSnwQbJQK2m5aXhTrXzPsNpQT6wBDq73rSCyFPyrOPHTWfs4pSMzZAOroi6O1o160GVChltnYdv7Rr8VmTspQdtgPsRIj_NPUsDOQWzJj11ns0wmOUbgco26_rmHU&gsessionid=b3vyoEoGCBaA4nCJquIEKs6LaAONBLmhAgExom1OgWQMDAWe0spslQ)  
  <sub>TipRanks, 2 hours ago</sub>  
  Himalaya Shipping Ltd. ( ($HSHP) ) has provided an announcement. Himalaya Shipping Ltd. is an independent bulk carrier company incorporated in Bermuda and...
- [ETFs Are Net Sellers of General Electric (GE) on Nov. 19](https://www.google.com/goto?url=CAESmQEBxCJF18Jzv-z1TRNWJWsheP5GThjzFKp7XCtYbwBAN29zMUCQmJK9hhI3g9lwpNpl3HWVQ9xxcO8yVjlIJiE0iAUK3hhlL-BqxoL7-gIP6y8HVQT_HdZ8tRAdq_iD4u9VEzTnNYWo88srUh4zgUcbSRGmudiMAnvvKLi8ihrwv6kM__16xib3xwgrVJEBQXAhA6FBguwM3mY&gsessionid=b3vyoEoGCBaA4nCJquIEKs6LaAONBLmhAgExom1OgWQMDAWe0spslQ)  
  <sub>GuruFocus, 3 hours ago</sub>  
  ETF flows out of General Electric (GE) extended to a third straight session last Thursday, when funds sold a net $143.0 million of the stock.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 67.90 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 70.12 (-3.2%), 50d 69.81 (-2.7%), 200d 75.66 (-10.3%); 50d below 200d
Momentum: RSI(14) 43.2 | MACD -0.529 vs signal -0.134 (histogram -0.395)
Returns: 1d +2.6% | 5d -2.7% | 1m +0.7% | 3m -13.1%
52-week range: 66.08 - 84.41 (now 9.9% of the way up)
Volatility: ATR(14) 1.87 (2.8% of price) | annualised 20d 34.2%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Industrials
What it holds: P/E 30.89 | P/B 5.67 | P/S 2.83 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +20.1% a year | beta to the market 1.03
Cost and size: expense ratio 0.37% | net assets 12.22B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: GE Aerospace 20.0%, RTX Corp 17.2%, Boeing Co 6.8%, Lockheed Martin Corp 5.7%, Northrop Grumman Corp 5.1%
Sector mix: Industrials 100.0%
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
Rolled up from the 5 largest holdings, 54.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.74 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.0% above the current prices
Holdings read: GE, RTX, BA, LMT, NOC
Recent rating changes among them:
  - GE: 2026-10-21 UBS: main, Buy -> Buy
  - RTX: 2026-10-21 UBS: main, Neutral -> Neutral
  - BA: 2026-10-29 Bernstein: main, Outperform -> Outperform
  - LMT: 2026-11-04 Guggenheim: init, ? -> Buy
  - NOC: 2026-10-27 Bernstein: main, Market Perform -> Market Perform
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
Share count change: 1 week: +5.0% (583.80M) over 7d | 1 month: +204.1% (8.16B) over 30d
Shares outstanding: 179.08M | fund size: 12.16B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technicals indicate a downtrend and weak momentum, but low volume limits the strength of that signal. Analyst coverage is strongly bullish (90.9% buy, +22% price target) and fund flows are positive (+5% share count over the month), while macro data show no surprise and news coverage is neutral. The mixed evidence and lack of a decisive macro catalyst lead to a neutral stance.

**Main reasons it gave:**
- Technical downtrend: price 80.14 below 20‑day (82.40), 50‑day (80.92) and 200‑day (82.06) SMAs, RSI 44.3, MACD below signal
- Analyst consensus: 90.9% buy, weighted price target +22.1% above current price
- Fund flows: share count up 5% over past month (+95.32M shares)

<details><summary><b>News</b> — score +0.00</summary>

- [Should You Invest in the iShares U.S. Transportation ETF (IYT)?](https://ca.finance.yahoo.com/news/invest-ishares-u-transportation-etf-102002865.html)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>  
  Sector ETF report for IYT.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 80.14 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 82.40 (-2.7%), 50d 80.92 (-1.0%), 200d 82.06 (-2.3%); 50d below 200d
Momentum: RSI(14) 44.3 | MACD -0.094 vs signal 0.370 (histogram -0.464)
Returns: 1d +1.9% | 5d -4.6% | 1m -0.0% | 3m -8.2%
52-week range: 70.03 - 90.01 (now 50.6% of the way up)
Volatility: ATR(14) 1.77 (2.2% of price) | annualised 20d 30.0%
Volume: 0.02x the 20-day average
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
Three-year record: +10.4% a year | beta to the market 1.24
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

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

```text
Rolled up from the 5 largest holdings, 52.2% of the fund by weight
Ratings by weight: buy 90.9% | hold 9.1% | sell 0.0% (mean 1.87 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.1% above the current prices
Holdings read: UNP, UBER, CSX, UPS, NSC
Recent rating changes among them:
  - UNP: 2026-11-05 Baird: down, Outperform -> Neutral
  - UBER: 2026-11-06 UBS: main, Buy -> Buy
  - CSX: 2026-10-27 Susquehanna: main, Positive -> Positive
  - UPS: 2026-10-28 UBS: main, Buy -> Buy
  - NSC: 2026-10-23 Citigroup: main, Neutral -> Neutral
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
Share count change: 1 week: +3.3% (62.81M) over 7d | 1 month: +5.0% (95.32M) over 36d
Shares outstanding: 24.78M | fund size: 1.99B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows no recent news and macro conditions are largely unchanged: yields are stable, the yield curve is normal and the VIX is elevated but not shifting policy. Technicals are slightly bearish (price below 20‑, 50‑ and 200‑day SMAs, RSI 42.5) while the analyst consensus on the top holdings is uniformly buy with a +19.5% price target, indicating moderate bullishness but covering only 45% of the fund. Fund flows reveal net outflows of –7.3% over the past month, a bearish sign of reduced investor demand. Valuation metrics (P/E 14.1, low beta 0.20) are neutral. The mixed signals lead to a neutral overall stance.

**Main reasons it gave:**
- Analyst coverage of top holdings: 100% buy, price targets +19.5% (ANALYST VIEW OF THE HOLDINGS)
- Fund flows: net outflows of -7.3% over the past month (FUND FLOWS)
- Technical indicators: price below 20‑day SMA and RSI 42.5, indicating slight bearish momentum (TECHNICALS)
- No recent news items found (NEWS)
- Fund fundamentals: P/E 14.14, low beta 0.20, indicating neutral valuation (FUND BASICS)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 34.93 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 35.17 (-0.7%), 50d 35.71 (-2.2%), 200d 37.65 (-7.2%); 50d below 200d
Momentum: RSI(14) 42.5 | MACD -0.046 vs signal -0.065 (histogram 0.018)
Returns: 1d -0.1% | 5d -2.5% | 1m +3.7% | 3m -11.0%
52-week range: 33.69 - 40.63 (now 17.9% of the way up)
Volatility: ATR(14) 0.34 (1.0% of price) | annualised 20d 14.7%
Volume: 0.41x the 20-day average
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
Three-year record: -1.3% a year | beta to the market 0.20
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 45.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.10 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.5% above the current prices
Holdings read: 1120.SR, 2222.SR, 1180.SR, 7010.SR, 1211.SR
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
Share count change: 1 week: +1.8% (9.68M) over 7d | 1 month: -7.3% (-43.47M) over 30d
Shares outstanding: 15.72M | fund size: 549.03M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund faces a neutral outlook: macro conditions are unchanged with no policy surprise, technicals remain bearish but without a decisive break, recent positive news and analyst coverage provide modest upside, and short‑term inflows counterbalance flat longer‑term flows, leaving no material catalyst to shift stance.

**Main reasons it gave:**
- Beijing state‑backed funds bought record 90B yuan in ETFs to support Chinese market
- Price below 20‑, 50‑, and 200‑day SMAs; RSI 32.9 and MACD negative
- Share count rose 6.1% in the past week, indicating fresh inflows
- Analyst consensus 100% buy with weighted price target +73.8% for top holdings covering 32.6% of fund

<details><summary><b>News</b> — score +0.20</summary>

- [Beijing steps up market rescue with record 90B yuan ETF purchases (FXI:NYSEARCA)](https://www.google.com/goto?url=CAESowEBxCJF12-xGdILUdsQVCGPVOrQtV3qwqGb3o1kbq8HlJlghakrbOW1h42ndFTXqcrgYuZlCUDZtWKCIGvHTh78M9slceNfupIe0vQzjqeCmL2ZJENIsrA8ap8YFBJtKjIEkgmvOmUVo95-JimZ3_5qDrw2adfhf8MbgG-cSxAtG9lFm9ELf50fBkJZUE3CD7gNFdqoPnIa5MPa8ver9-hL0PCg&gsessionid=CoDr_0kx9Y1aw_-nstCsKl_Utsy6AAJHY8Vu-kMXqdyFnvNc7KTojQ)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  China's state-backed funds invested a record 90B yuan ($13.5B) in ETFs on Friday, stepping up efforts to support the country's stock market as a prolonged...
- [A New Wave Of Anthropic ETFs Is Coming — What’s On Offer](https://stocktwits.com/news-articles/markets/equity/a-new-wave-of-anthropic-et-fs-is-coming-what-s-on-offer/cNbYMLjR9Sm)  
  <sub>Stocktwits, 7 hours ago</sub>  
  ETFs such as Ultra Anthropic (ANTU), UltraShort Anthropic (ANTY), 2X Long Anthropic Daily ETF (AIL) and 2X Short Anthropic Daily ETF (ANS) will begin...
- [SPY, QQQ Rebound As AI Selloff Hits South Korea Despite Government Support: What Investors Are Watching](https://www.google.com/goto?url=CAESsAEBxCJF10UGf40KWww1cjNI5FynKHVGhSrCoagPBgOpuc0x3ykw38ZXPCpMP49e6Udk-Ju_lpgUQQdfShXIosQlRTZSa6L5BPjg9jxR53dYazSxgDuGMYyKOF1SQ4czKeMd_aHEaitxLZji3KwaCWkJHUsuLcdwxB-TZshtOzx4SOCm3Go1GxrLk9wRE7LNtAmzV0YKQ_jXwftjUtORnvcOKRMWM5xyPiDHMmcbPlVBhQ&gsessionid=CoDr_0kx9Y1aw_-nstCsKl_Utsy6AAJHY8Vu-kMXqdyFnvNc7KTojQ)  
  <sub>Stocktwits, 8 hours ago</sub>  
  In early Asian trading, Dow futures climbed 1.45%, while the S&P 500 futures gained 2.10% and Nasdaq-100 futures increased 3.02%.
- [PayPal Sale: Why This Analyst Sees A ‘Lower Likelihood’](https://www.google.com/goto?url=CAESsQEBxCJF19f0ZCJPboDGl_GJaBhqCQlplR6oRlpgGR_UPnGa8kRJq_dxfaVgIv1M3QxhlDZTma3J3FqffkMr0DT8ALMnG8uOYKmAjM8KOXNHyIL9Pk3rppX-iY50wR-wHw8WHHuxieZcaEtWYvyZu8GP6jOqhCC1ZZXmMtUtGTFsdobiY-92KJcAtzpYNelAoaFCAq-ZtWvgXqHV5yPQoKlGcK95sx8RfOvHya9zbHXD1Xw&gsessionid=CoDr_0kx9Y1aw_-nstCsKl_Utsy6AAJHY8Vu-kMXqdyFnvNc7KTojQ)  
  <sub>Stocktwits, 7 hours ago</sub>  
  Clear Street said that PayPal's four senior executive appointments signal that there is "still a long way to go" for the company's turnaround effort.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 47.03 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 49.43 (-4.9%), 50d 50.89 (-7.6%), 200d 54.70 (-14.0%); 50d below 200d
Momentum: RSI(14) 32.9 | MACD -1.055 vs signal -0.707 (histogram -0.348)
Returns: 1d +2.2% | 5d -4.1% | 1m -4.0% | 3m -14.7%
52-week range: 46.02 - 64.26 (now 5.5% of the way up)
Volatility: ATR(14) 0.76 (1.6% of price) | annualised 20d 23.7%
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
Three-year record: +4.0% a year | beta to the market 0.47
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
Weighted price target: +73.8% above the current prices
Holdings read: 0700.HK, 9988.HK, 00939, 01398, 1810.HK
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
Direction: flat (1 month)
Share count change: 1 week: +6.1% (315.50M) over 7d | 1 month: -0.3% (-16.88M) over 30d
Shares outstanding: 116.81M | fund size: 5.49B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Flat fund flows (0% net change over 1 month)
- Price below 20‑day SMA (31.02) and 50‑day SMA (33.13); RSI 35.4 (near oversold)
- Analyst coverage 44.9% of fund, all buy with +37.6% price target
- VIX up 3.9 points to 26.76 (stressed market) with no surprise macro data

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.81 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 31.02 (-3.9%), 50d 33.13 (-10.0%), 200d 38.29 (-22.2%); 50d below 200d
Momentum: RSI(14) 35.4 | MACD -0.696 vs signal -0.686 (histogram -0.010)
Returns: 1d +0.8% | 5d -7.1% | 1m -3.0% | 3m -26.0%
52-week range: 29.53 - 43.74 (now 2.0% of the way up)
Volatility: ATR(14) 0.64 (2.1% of price) | annualised 20d 34.1%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 11.63 | P/B 1.01 | P/S 0.62 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: -4.0% a year | beta to the market 0.60
Cost and size: expense ratio 0.59% | net assets 146.42M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Aselsan Elektronik Sanayi Ve Ticaret AS 13.3%, Tupras-Turkiye Petrol Rafineleri AS 10.9%, Bim Birlesik Magazalar AS 9.8%, Akbank TAS 6.2%, Turk Hava Yollari AO 4.6%
Sector mix: Industrials 30.8%, Financial services 16.9%, Consumer defensive 12.9%, Energy 10.9%
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
Rolled up from the 5 largest holdings, 44.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +37.6% above the current prices
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
Shares outstanding: 15.65M | fund size: 466.53M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Macro conditions unchanged and no macro surprise; no news; technicals show slight bearish momentum but no decisive break; analyst coverage is strongly bullish and recent inflows are positive, however without a macro catalyst the appropriate view is neutral.

**Main reasons it gave:**
- Analyst consensus 100% buy with weighted price target +16.6% above current price
- Weekly share count increase +3.2% (2.14B) indicating inflows
- Price below 20‑day SMA (-1.5%) and MACD histogram -0.451 indicating bearish momentum
- No macro surprise: yields unchanged, Fed target unchanged, VIX modestly higher
- No news in past 24h

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 93.71 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 95.12 (-1.5%), 50d 92.88 (+0.9%), 200d 94.99 (-1.4%); 50d below 200d
Momentum: RSI(14) 46.9 | MACD 0.287 vs signal 0.737 (histogram -0.451)
Returns: 1d +1.2% | 5d -2.6% | 1m +1.1% | 3m -5.6%
52-week range: 87.00 - 100.95 (now 48.1% of the way up)
Volatility: ATR(14) 1.46 (1.6% of price) | annualised 20d 20.7%
Volume: 0.14x the 20-day average
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
Three-year record: +9.3% a year | beta to the market 0.92
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

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

```text
Rolled up from the 5 largest holdings, 40.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.56 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.6% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2026-11-11 UBS: main, Buy -> Buy
  - PLD: 2026-11-02 Wells Fargo: main, Overweight -> Overweight
  - EQIX: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - AMT: 2026-11-05 Argus Research: reit, Buy -> Buy
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
Share count change: 1 week: +3.2% (2.14B) over 7d | 1 month: +2.0% (1.35B) over 36d
Shares outstanding: 743.11M | fund size: 69.63B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Sector news showed a >6% selloff in biotech, pushing sentiment bearish, while short‑term technical indicators (price below 20‑ and 50‑day SMAs, RSI 44.8, MACD negative) also hint at bearish momentum. However the fund’s valuation is cheap (P/B 0.21, P/S 0.13) with strong three‑year performance, analysts are largely bullish on the top holdings (75% buy, +11.7% price target), and recent inflows (+12% share count in a month) signal demand. With mixed signals and no macro surprise, the overall call is neutral.

**Main reasons it gave:**
- Biotech sector down >6% after FDA rejection news (sector selloff)
- Price below 20‑day and 50‑day SMA, RSI 44.8, MACD negative (technical bearish momentum)
- Share count up 12% over the past month, indicating strong inflows
- Analyst coverage of top holdings 75% buy, weighted price target +11.7% (analyst bullish but thin)
- Fund valuation cheap: P/B 0.21, P/S 0.13, 3‑year annual return +24.3% (fundamentals positive)

<details><summary><b>News</b> — score -0.45</summary>

- [Biotech Funds Slide Into Thanksgiving Week — Capricor’s FDA Fight And Back-To-Back Drug Decisions Top Watchlist](https://www.tradingview.com/news/stocktwits:b9ecda636094b:0-biotech-funds-slide-into-thanksgiving-week-capricor-s-fda-fight-and-back-to-back-drug-decisions-top-watchlist/?mobileapp_new=true)  
  <sub>TradingView, 12 hours ago</sub>  
  After a selloff that sent biotech funds down over 6%, investors are heading into Thanksgiving week with Capricor contesting an FDA rejection, two drugmakers...
- [How to Invest in iShares Biotechnology ETF (IBB)](https://www.fool.com/investing/how-to-invest/etfs/how-to-invest-in-ibb-etf/)  
  <sub>The Motley Fool, 21 hours ago</sub>  
  The iShares Biotechnology ETF (IBB) provides exposure to healthcare innovation with a focus on the biggest firms by market cap.
- [Bitcoin’s Worst November Since 2018? $4B In Spot ETF Outflows Deepen Crypto Selloff](https://www.google.com/goto?url=CAESsQEBxCJF14pkSMWH5Pf81AYbUB7Tps7k1s7EvkKntQrjnCW0lX_a1wQbub6kRt7Bmgw_oBNCX55dp_pEAlwugSCjUU2CxqLjIeo4fMcNPmTSyLzwy7LrK6moRj7lK2pJwEezqfsUrFybDvilDauCy354Emm2Ulgn2kLDVI1oyDlyhpJUODp2vzzKArfRVhtonoFRomgY6KTbtSJ6-Uz8sEDJ-kbaTqEFd1f9gxQjbZGwj4k&gsessionid=SN38G2hFSxKAO9WRIKQyAVROlNPkzfHXxXJq3hiChg6PSY5ynkfjOQ)  
  <sub>Stocktwits, 10 hours ago</sub>  
  Bitcoin (BTC) was on course for its worst November since 2018 after U.S. spot Bitcoin exchange-traded funds (ETFs) shed over $4 billion this month,...
- [SLS Stock Logs Best Week In 6 Years — Why Did The CEO Sell Shares After Its Leukemia Trial Win?](https://www.google.com/goto?url=CAESswEBxCJF1-gngqXuikXWLybHISrtWEiNPwxJINKBGDsUGjk0YyL_bfOldrGMeLLKPkdEerxb6dDtWbehfjjXLRWEtgG3lem2c4Nx_bY600KPsuIbo91pTVAeJ5zIYRHlcfdHED77Cf-kmyQCrKXvO1yTwlA7chMS4_cy2lD02rK-78705JAaV6X64AFDp3Gc-RimPjLys6_TzDMlN-bedCzbaTFvFXZx14PkkIKx6gFglzFnkQ&gsessionid=SN38G2hFSxKAO9WRIKQyAVROlNPkzfHXxXJq3hiChg6PSY5ynkfjOQ)  
  <sub>Stocktwits, 10 hours ago</sub>  
  CEO Angelos Stergiou sold 26606 shares worth about $510250 to cover taxes on a stock award triggered by the Regal trial win.
- [NVDA Stock Rebounds Overnight: Trump Backs Jensen Huang’s Return As Nvidia CEO](https://www.google.com/goto?url=CAES6wEBxCJF1_s54Yd0S4qWR7I4ZqiEHzvWj4uFZCNAfa2YePGolcbU20w4XWqJh6fSBgfZqhQrkqKTPqVLTU0UzHbug_fi6DjSOlquSIvcOFo-ZD83W7wb0YOhex91eC8i8_sN_MjTdNwMi2VkVa9l0NNbP2vb6XMj0iuy2_tZr5fSFHIJZ1d_Yx8qKZKZknaoD-7lSXn1Aba1PM6UD-QZyEvrOz7KxvsJsSh3ziSVIonBuGHLywjx-sgPRHfvKNz10fciJlQKWDJGCCUJlMzLpfcCuoZR4gyO-st-p2YIxZyfTzKBJulYTGHcg4-s&gsessionid=SN38G2hFSxKAO9WRIKQyAVROlNPkzfHXxXJq3hiChg6PSY5ynkfjOQ)  
  <sub>Stocktwits, 11 hours ago</sub>  
  I hope the Board of Nvidia rehires Jensen Huang,” Trump posted on Truth Social on Sunday.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.45</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 146.22 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 151.48 (-3.5%), 50d 152.48 (-4.1%), 200d 143.55 (+1.9%); 50d above 200d
Momentum: RSI(14) 44.8 | MACD -2.506 vs signal -1.479 (histogram -1.027)
Returns: 1d +4.3% | 5d +0.2% | 1m -2.2% | 3m -13.5%
52-week range: 116.65 - 169.55 (now 55.9% of the way up)
Volatility: ATR(14) 5.00 (3.4% of price) | annualised 20d 43.1%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.45</summary>

```text
Fund type: Health
What it holds: P/E n/a | P/B 0.21 | P/S 0.13 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +24.3% a year | beta to the market 1.01
Cost and size: expense ratio 0.35% | net assets 10.92B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Moderna Inc 2.4%, Natera Inc 1.8%, Halozyme Therapeutics Inc 1.8%, Twist Bioscience Corp 1.8%, Biogen Inc 1.7%
Sector mix: Healthcare 99.4%, Financial services 0.6%
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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 9.5% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 75.0% | hold 25.0% | sell 0.0% (mean 2.06 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.7% above the current prices
Holdings read: MRNA, NTRA, HALO, TWST, BIIB
Recent rating changes among them:
  - MRNA: 2026-11-09 Goldman Sachs: main, Neutral -> Neutral
  - NTRA: 2026-11-09 Baird: main, Outperform -> Outperform
  - HALO: 2026-11-11 Morgan Stanley: down, Overweight -> Equal-Weight
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - BIIB: 2026-11-09 Piper Sandler: reit, Overweight -> Overweight
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.55</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +5.0% (522.95M) over 7d | 1 month: +12.1% (1.19B) over 30d
Shares outstanding: 75.78M | fund size: 11.08B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technicals show the ETF trading below its 20‑day and 200‑day averages with negative MACD, while recent volume is very low, suggesting bearish pressure. However, recent fund flows are strongly positive (+12.1% share count increase in the past month) and analyst coverage of the top holdings, though thin (18.9% of weight), is uniformly bullish with price targets +13.5%. No macro surprise (rates unchanged, no policy shock) occurred, leaving the overall outlook balanced and neutral.

**Main reasons it gave:**
- Shares outstanding rose 12.1% in the past month (≈177 M shares added)
- Analyst coverage of top 5 holdings (18.9% of fund) is 100% buy with price targets +13.5%
- Price is below 20‑day SMA and 200‑day SMA; MACD negative (-0.098 vs signal 0.653)
- Volume is only 5% of its 20‑day average, indicating low trading activity

<details><summary><b>News</b> — score +0.00</summary>

- [Should You Invest in the Invesco Building & Construction ETF (PKB)?](https://ca.finance.yahoo.com/news/invest-invesco-building-construction-etf-102002394.html)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  The Invesco Building & Construction ETF (PKB) was launched on October 26, 2005, and is a passively managed exchange traded fund designed to offer broad...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 98.34 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 101.44 (-3.1%), 50d 98.44 (-0.1%), 200d 104.28 (-5.7%); 50d below 200d
Momentum: RSI(14) 46.4 | MACD -0.098 vs signal 0.653 (histogram -0.752)
Returns: 1d +1.8% | 5d -2.6% | 1m -0.0% | 3m -7.6%
52-week range: 92.84 - 121.36 (now 19.3% of the way up)
Volatility: ATR(14) 2.91 (3.0% of price) | annualised 20d 40.0%
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
Three-year record: +6.3% a year | beta to the market 1.40
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 18.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.5% above the current prices
Holdings read: ALLE, SN, MAS, W, CVCO
Recent rating changes among them:
  - ALLE: 2026-11-03 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - SN: 2026-11-09 Guggenheim: main, Buy -> Buy
  - MAS: 2026-11-05 Argus Research: main, Buy -> Buy
  - W: 2026-11-12 Argus Research: main, Buy -> Buy
  - CVCO: 2026-11-02 Oppenheimer: reit, Outperform -> Outperform
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
Share count change: 1 week: +3.5% (56.07M) over 7d | 1 month: +12.1% (176.95M) over 30d
Shares outstanding: 16.67M | fund size: 1.64B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The communications‑sector ETF XLC gets strong bullish sentiment from analysts (90.6% buy rating, weighted price target +37.5%) and recent net inflows (+4.7% weekly share count), but its price is under the 20‑, 50‑ and 200‑day moving averages, RSI is at 40 and MACD is negative, indicating a bearish technical stance, and market volatility is elevated (VIX 26.8). No macro surprise or decisive technical breakout is present, so the overall view remains neutral.

**Main reasons it gave:**
- Technical: price below 20‑day, 50‑day and 200‑day SMAs – bearish trend
- Technical: RSI 40 and MACD negative – modest downside momentum
- Analyst: 90.6% buy rating and weighted price target +37.5% – strong bullish sentiment
- Flows: weekly share count +4.7% (≈$1B) indicating net inflows

<details><summary><b>News</b> — score -0.20</summary>

- [Hedge funds short single stocks at fastest weekly pace since 2022 - Goldman](https://www.tradingview.com/news/seekingalpha:799793739094b:0-hedge-funds-short-single-stocks-at-fastest-weekly-pace-since-2022-goldman/)  
  <sub>TradingView, 27 minutes ago</sub>  
  Hedge funds net sold U.S. equities AMEX:SPY NASDAQ:QQQ AMEX:DIA for a third straight week driven by heavy single-stock shorting that outpaced long buying by...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 102.02 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 104.30 (-2.2%), 50d 108.36 (-5.9%), 200d 111.95 (-8.9%); 50d below 200d
Momentum: RSI(14) 40.0 | MACD -1.292 vs signal -1.023 (histogram -0.269)
Returns: 1d +2.0% | 5d -4.5% | 1m -3.3% | 3m -9.9%
52-week range: 99.90 - 120.08 (now 10.5% of the way up)
Volatility: ATR(14) 2.38 (2.3% of price) | annualised 20d 26.1%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Communications
What it holds: P/E 15.87 | P/B 3.10 | P/S 2.22 | 3y earnings growth n/a
Yield: 1.4%
Three-year record: +13.5% a year | beta to the market 0.93
Cost and size: expense ratio 0.08% | net assets 21.45B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Meta Platforms Inc Class A 22.0%, Alphabet Inc Class A 11.1%, Alphabet Inc Class C 8.9%, The Walt Disney Co 5.6%, Comcast Corp Class A 4.9%
Sector mix: Communication services 100.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.85</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.85</summary>

```text
Rolled up from the 5 largest holdings, 52.5% of the fund by weight
Ratings by weight: buy 90.6% | hold 9.4% | sell 0.0% (mean 1.53 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +37.5% above the current prices
Holdings read: META, GOOGL, GOOG, DIS, CMCSA
Recent rating changes among them:
  - META: 2026-10-22 UBS: main, Buy -> Buy
  - GOOGL: 2026-11-02 Wells Fargo: main, Overweight -> Overweight
  - GOOG: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - DIS: 2026-10-16 Citigroup: main, Buy -> Buy
  - CMCSA: 2026-10-26 Freedom Broker: main, Hold -> Hold
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
Share count change: 1 week: +4.7% (957.49M) over 7d | 1 month: +2.1% (440.27M) over 30d
Shares outstanding: 208.75M | fund size: 21.30B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technicals show modest bearishness (price under multiple SMAs, negative MACD) but analyst coverage on the top holdings is bullish (100% buy, +31% price target) albeit thin, and fund flows are flat with no macro surprise, leading to a neutral overall outlook.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs and MACD histogram negative
- Analyst ratings: 100% buy on top holdings, weighted price target +31% (coverage 24%)
- Fund flows flat: share count unchanged week‑over‑week and month‑over‑month
- Macro data stable: no policy surprise, yields modestly lower, VIX up but no major shock

<details><summary><b>News</b> — score +0.00</summary>

- [Select Sector SPDR Trust - State Street Industrial Select Sector SPDR ETF (ARCA:XLI) Stock Price](https://simplywall.st/etf/arca/xli)  
  <sub>Simply Wall St, 6 hours ago</sub>  
  Find the latest The Select Sector SPDR Trust - State Street Industrial Select Sector SPDR ETF (ARCA:XLI) stock price, share price history, and explore other...
- [ETF Holdings: Up to 42% Sits in Apple, Microsoft and Nvidia](https://www.techloy.com/insight-loop-newsletter-november-22-2026-etf-holdings-apple-microsoft-nvidia/)  
  <sub>Techloy, 23 hours ago</sub>  
  Apple, Microsoft and Nvidia make up 11.9% to 42.3% of SPY, QQQ, VTI, VT and XLK. Check how much of your ETF money sits in the same 3 stocks.
- [ETFs Are Net Sellers of General Electric (GE) on Nov. 19](https://www.google.com/goto?url=CAESmQEBxCJF14rf1Dr2fNOhHmTDLssBAhuI-9sqz3sHa80irmZk68TUkzc40R1R3jHHRVtLdILIW9PrH5WJ_mKRPQz2g6eqwTDcr7siawdP-dHSDdEMyRR1y_PZLJP2-wfA8a4_Sr8u0hdS69UpSxnujJpKKfhqcTyPUjEpXEkgtokaQnaSS8M9zVd6Vdo4iPGToTXQDR2ujwokWhc&gsessionid=qW4pUH8e656-RhEJlMkRwjsGp7zMxFl6-Osc7HlWrBsHPOa_NiVMFQ)  
  <sub>GuruFocus, 3 hours ago</sub>  
  ETF flows out of General Electric (GE) extended to a third straight session last Thursday, when funds sold a net $143.0 million of the stock.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 161.19 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 166.52 (-3.2%), 50d 167.75 (-3.9%), 200d 173.26 (-7.0%); 50d below 200d
Momentum: RSI(14) 41.4 | MACD -1.988 vs signal -1.126 (histogram -0.862)
Returns: 1d +3.1% | 5d -2.7% | 1m -2.1% | 3m -9.6%
52-week range: 149.63 - 186.51 (now 31.3% of the way up)
Volatility: ATR(14) 3.68 (2.3% of price) | annualised 20d 30.2%
Volume: 0.10x the 20-day average
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
Three-year record: +15.5% a year | beta to the market 1.00
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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 24.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +31.0% above the current prices
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
Shares outstanding: 136.63M | fund size: 22.02B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technical indicators show bearish momentum (price below SMAs, RSI 39.5, negative MACD) but there is no decisive break on heavy volume. The macro backdrop is unchanged with no surprise in policy or data releases. Analyst coverage of the top holdings is overwhelmingly bullish (100% buy, weighted price target +31.6% above price) and fund flows are strongly positive (+8% weekly, +14% monthly). Fundamentals show high valuations and a neutral growth outlook, which does not provide a clear directional edge. With these mixed signals and no macro catalyst, a neutral stance is warranted.

**Main reasons it gave:**
- RSI 39.5 and price below 20‑day SMA indicate bearish momentum
- Fund inflows +8% weekly and +14% monthly show strong demand
- Analyst consensus 100% buy with weighted price target +31.6% above price
- Macro data stable (Fed target unchanged, yields steady, no surprise data)

<details><summary><b>News</b> — score +0.00</summary>

- [ETF Holdings: Up to 42% Sits in Apple, Microsoft and Nvidia](https://www.techloy.com/insight-loop-newsletter-november-22-2026-etf-holdings-apple-microsoft-nvidia/)  
  <sub>Techloy, 23 hours ago</sub>  
  Apple, Microsoft and Nvidia make up 11.9% to 42.3% of SPY, QQQ, VTI, VT and XLK. Check how much of your ETF money sits in the same 3 stocks.
- [Should You Invest in the State Street SPDR S&P Semiconductor ETF (XSD)?](https://finance.yahoo.com/markets/stocks/articles/invest-state-street-spdr-p-102002291.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  If you're interested in broad exposure to the Technology - Semiconductors segment of the equity market, look no further than the State Street SPDR S&P...
- [How Does China's Margin Ratio Cut to 80% Affect iShares China Large-Cap ETF (NYSEARCA:FXI)?](https://www.google.com/goto?url=CAESwQEBxCJF1-9Dz52bApmLGti1uopJTe5d3S0OmH4ymqQKrHeU928o52-_p1BbIPeFqxMsFbpaoUtdSCSKHJI_prie5368m2E0idq7hvEd4P8OfU5_rrNz3PnRc_B2phETz2B0EUGBDy-mJxCTR1XeNCsd2McJ8-X2X4GCwkVtdgOLqh-69fIJYS2COsE35lumqs4luWGWVIREs_S7kfcN76GWlp9hB6hgyT37vWVghYWqWcxnCBStriVgbPfSsk0i-CHh&gsessionid=fpGY5rb3kQXk-bwbHxpvowCUOI7xSd5Db95FJSFfaacyDF3HxMuXfA)  
  <sub>Kalkine, 15 minutes ago</sub>  
  How Does China's Margin Ratio Cut to 80% Affect iShares China Large-Cap ETF (NYSEARCA:FXI)?

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 160.68 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 171.18 (-6.1%), 50d 183.94 (-12.6%), 200d 171.40 (-6.3%); 50d above 200d
Momentum: RSI(14) 39.5 | MACD -7.404 vs signal -6.300 (histogram -1.105)
Returns: 1d +7.8% | 5d -2.5% | 1m -12.3% | 3m -11.6%
52-week range: 127.50 - 202.00 (now 44.5% of the way up)
Volatility: ATR(14) 6.87 (4.3% of price) | annualised 20d 58.2%
Volume: 0.20x the 20-day average
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
Three-year record: +17.9% a year | beta to the market 1.56
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 51.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +31.6% above the current prices
Holdings read: AAPL, NVDA, MSFT, AVGO, AMD
Recent rating changes among them:
  - AAPL: 2026-11-11 China Renaissance: up, Hold -> Buy
  - NVDA: 2026-11-12 Melius Research: down, Buy -> Hold
  - MSFT: 2026-10-29 Bernstein: main, Outperform -> Outperform
  - AVGO: 2026-10-27 Rosenblatt: main, Buy -> Buy
  - AMD: 2026-11-12 B of A Securities: main, Buy -> Buy
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
Share count change: 1 week: +8.1% (8.89B) over 7d | 1 month: +13.8% (14.40B) over 36d
Shares outstanding: 738.38M | fund size: 118.64B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No clear bullish or bearish catalyst emerges: macro data is in line with expectations, technicals show mixed signals with price above longer‑term averages but MACD below its signal, analyst coverage is uniformly positive but not a material catalyst, and fund flows are flat. The balance of evidence supports a neutral stance.

**Main reasons it gave:**
- Flat fund flows (0% change over 1 week and 1 month)
- Technicals: price above 50‑day and 200‑day SMA but MACD below signal
- Macro data: inflation 3.7% and unemployment 4.1% in line with expectations, yields unchanged
- Analyst coverage: 100% buy rating on top holdings, weighted price target +5.5%

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Consumer Staples Select Sector SPDR ETF (XLP)](https://ca.finance.yahoo.com/quote/XLP/options/?date=1796947200&straddle=false&type=all)  
  <sub>Yahoo! Finance Canada, 9 hours ago</sub>  
  View the basic XLP option chain and compare options of State Street Consumer Staples Select Sector SPDR ETF on Yahoo Finance.
- [3 ETFs that could outperform the S&P 500 if the AI crash continues](https://invezz.com/nz/news/2026/11/23/3-etfs-that-could-outperform-the-sandampp-500-if-the-ai-crash-continues/)  
  <sub>Invezz, 6 hours ago</sub>  
  Three defensive ETFs—XLP, XLV and USMV—beat the S&P 500 during Wall Street's AI sell-off. How they held up and which risks remain.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 89.97 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 90.35 (-0.4%), 50d 86.51 (+4.0%), 200d 85.04 (+5.8%); 50d above 200d
Momentum: RSI(14) 52.5 | MACD 1.107 vs signal 1.454 (histogram -0.347)
Returns: 1d -0.5% | 5d -2.8% | 1m +1.9% | 3m +4.0%
52-week range: 76.62 - 92.60 (now 83.6% of the way up)
Volatility: ATR(14) 1.48 (1.6% of price) | annualised 20d 20.9%
Volume: 0.32x the 20-day average
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
Three-year record: +12.2% a year | beta to the market 0.39
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 41.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +5.5% above the current prices
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
Shares outstanding: 210.17M | fund size: 18.91B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Analyst consensus is strongly bullish and inflows are robust, but technical momentum is weak (price below 20‑day SMA, RSI below 50, MACD below signal) and valuation metrics (P/E ~30) suggest a modest overvaluation. Macro data show no surprise and no decisive technical break on volume. With no clear macro catalyst, the overall stance remains neutral.

**Main reasons it gave:**
- Defensive ETF XLV outperformed S&P 500 during recent AI sell‑off (news)
- Technical: price below 20‑day SMA, RSI 44.3, MACD below signal (bearish momentum)
- Analyst view: 100% buy rating on top holdings, weighted price target +13.2%
- Fund flows: share count increased 5.8% week‑over‑week, indicating strong inflows

<details><summary><b>News</b> — score +0.20</summary>

- [3 ETFs that could outperform the S&P 500 if the AI crash continues](https://invezz.com/nz/news/2026/11/23/3-etfs-that-could-outperform-the-sandampp-500-if-the-ai-crash-continues/)  
  <sub>Invezz, 6 hours ago</sub>  
  Three defensive ETFs—XLP, XLV and USMV—beat the S&P 500 during Wall Street's AI sell-off. How they held up and which risks remain.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 178.80 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 184.32 (-3.0%), 50d 176.72 (+1.2%), 200d 160.98 (+11.1%); 50d above 200d
Momentum: RSI(14) 44.3 | MACD 0.860 vs signal 2.502 (histogram -1.642)
Returns: 1d +0.9% | 5d -4.8% | 1m -0.3% | 3m +2.0%
52-week range: 142.84 - 189.66 (now 76.8% of the way up)
Volatility: ATR(14) 3.41 (1.9% of price) | annualised 20d 22.5%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

```text
Fund type: Health
What it holds: P/E 30.14 | P/B 4.82 | P/S 1.66 | 3y earnings growth n/a
Yield: 1.4%
Three-year record: +13.0% a year | beta to the market 0.41
Cost and size: expense ratio 0.08% | net assets 49.10B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Eli Lilly and Co 16.9%, Johnson & Johnson 9.8%, AbbVie Inc 7.8%, Merck & Co Inc 5.5%, UnitedHealth Group Inc 5.4%
Sector mix: Healthcare 100.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 45.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.2% above the current prices
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
Share count change: 1 week: +5.8% (2.71B) over 7d | 1 month: +8.2% (3.75B) over 36d
Shares outstanding: 276.72M | fund size: 49.48B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed information: recent news highlights weakness in consumer stocks and a broader short‑selling surge, while technicals show short‑term softness (price below 20‑day SMA, MACD negative, low volume). At the same time, analyst coverage remains uniformly bullish with a +17.4% price‑target premium, and fund flows show a strong weekly net inflow (+3.9%). No macro surprise or decisive technical breakout is present, so the overall view remains neutral.

**Main reasons it gave:**
- Technical: price below 20‑day SMA, MACD negative, volume 0.16× 20‑day average
- News: consumer sector stocks losing sheen amid AI‑led selloff
- Analyst view: 100% buy coverage of top holdings, weighted price target +17.4%
- Fund flows: share count up 3.9% weekly (≈$851 M) indicating net inflow

<details><summary><b>News</b> — score -0.40</summary>

- [Consumer Stocks Snap Winning Streaks As AI Selloff Rocks Markets — TSN, PDD, TJX Buck Trend](https://www.tradingview.com/news/stocktwits:7f77676ee094b:0-consumer-stocks-snap-winning-streaks-as-ai-selloff-rocks-markets-tsn-pdd-tjx-buck-trend/?mobileapp_new=true)  
  <sub>TradingView, 5 hours ago</sub>  
  Consumer stocks lost their sheen last week as a tech-led selloff dragged the whole market lower. Tyson Foods (TSN), PDD Holdings (PDD) and TJX Companies...
- [Hedge funds short single stocks at fastest weekly pace since 2022 - Goldman](https://www.google.com/goto?url=CAESxgEBxCJF13mxmZspW5YwkMHnbjhSGjSvflql6-am7wAtO7aJJVOPgZAW1HmUP3WlCHRIACpFJsXQU9ymNsiBizswFHMy0XGc8QOm9mS1os7ueCT4rZmPS6bXFXFiuLrT3olJSLblu9NasDkf3VpqirRd0Sr_0a0RnoGHIFkWjENTreS3DwpmafboaGQygue5FATZ52SsiOmX3HuuIf-D1v9-9sNRkoFBx9j3QkjOltMM6rDxba8djdnPpgI8AVvoe0gUdBmWuR8&gsessionid=Ghb8tb76D_l7MJ6nI8ZUWLBkUOqNOjGw7E-hJzMXCQNJ1Hc2kfXtXw)  
  <sub>TradingView, 28 minutes ago</sub>  
  Hedge funds net sold U.S. equities AMEX:SPY NASDAQ:QQQ AMEX:DIA for a third straight week driven by heavy single-stock shorting that outpaced long buying by...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.40</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 116.26 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 117.90 (-1.4%), 50d 114.23 (+1.8%), 200d 115.34 (+0.8%); 50d below 200d
Momentum: RSI(14) 49.1 | MACD 0.445 vs signal 1.165 (histogram -0.719)
Returns: 1d +3.4% | 5d -1.6% | 1m +2.8% | 3m -1.4%
52-week range: 105.66 - 124.52 (now 56.2% of the way up)
Volatility: ATR(14) 2.70 (2.3% of price) | annualised 20d 33.4%
Volume: 0.16x the 20-day average
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
Three-year record: +11.1% a year | beta to the market 1.10
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

<details><summary><b>What analysts and big funds say</b> — score +1.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +1.00</summary>

```text
Rolled up from the 5 largest holdings, 54.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.4% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, TJX
Recent rating changes among them:
  - AMZN: 2026-11-03 Freedom Broker: main, Buy -> Buy
  - TSLA: 2026-11-05 GLJ Research: reit, Sell -> Sell
  - HD: 2026-11-10 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-11-06 Argus Research: main, Buy -> Buy
  - TJX: 2026-11-10 UBS: main, Buy -> Buy
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
Share count change: 1 week: +3.9% (851.09M) over 7d | 1 month: +2.1% (458.81M) over 36d
Shares outstanding: 193.30M | fund size: 22.47B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [What Does a 294.4% Surge in South Korea's Chip Exports Signal for iShares MSCI South Korea ETF (NYSEARCA:EWY)?](https://www.google.com/goto?url=CAESzAEBxCJF15gjYQf2ysU8vLnF5Eb-4jtKRFkV55GfAOgA_-O4i1ggHssV_SIa8EyowHjUtMOjL9FxMmNoJTq13LnAosCvfrfibqa1Elbr9LZW6hNK75YZoX3BKXYu0tmmBxKs3Mj8kYpv2BOeShl5EMIJr28hw5gRyM3Pbg7epzeXC2oTxNscLDEiaHh-knLYunfhCaKNe3jRI9ywshm0btE9QLX7HtaRR5QeZBIByH1dXKr8gcseJVal3z826x5ekCI9f2HyRRDJ6FQrfyg&gsessionid=PDrFd6k3ht4Z4YCj7LHum9hjaFMR-hHbnkDrHkjjYd9RdVw-mYuJ1A)  
  <sub>Kalkine, 21 minutes ago</sub>  
  What Does a 294.4% Surge in South Korea's Chip Exports Signal for iShares MSCI South Korea ETF (NYSEARCA:EWY)?
- [Money Exits U.S.-Listed Korea ETFs While Retail Investors Bet Triple](https://en.sedaily.com/market/2026/11/23/money-exits-us-listed-korea-etfs-while-retail-investors-bet)  
  <sub>Seoul Economic Daily, 6 hours ago</sub>  
  U.S.-listed Korea ETFs EWY and KORU saw $175 million in net outflows over a month, while Korean retail investors bought triple-leveraged funds.
- [South Korea's KOSPI drops 5% as AI fears trigger broader stock sell-off (KRWX:BATS)](https://www.google.com/goto?url=CAES9QEBxCJF14RXiDujEuuTx5oN6_ck2kPBCmDwojLICJNNMrbzWWnQshhK38HnqUjAyCuete6V9PAFvci_1p7_Fvy2vuCSyJy0X15LyfEvegSPL-IyGCf-Wv-aLU8zIeZBfUDaegteCvUx9p47L5vMSepMEZACMBxHO_xbMGrLuTRCvN-Lh0zS8sM9xGxS075c6Vovdu4ptwf7j802yZbRu_G9tqRVmFqfKfukQMfg8aRmoG_I0yffJ54beh1ghD-lLFyWUHWC8cZbprBpj2yCb2vsGrDxWjFfrYJPT_Dq1eq7EWPFnW_7IKK_gw9e3nIOlKvama6yCQ&gsessionid=PDrFd6k3ht4Z4YCj7LHum9hjaFMR-hHbnkDrHkjjYd9RdVw-mYuJ1A)  
  <sub>Seeking Alpha, 11 hours ago</sub>  
  South Korean stocks: KOSPI falls 5.41% Monday, down 17% in November as AI spending and export curbs weigh; authorities prepare a 10T-won fund.
- [iShares MSCI South Korea ETF (EWY) Price Prediction: Bearish trend clashes with a rebound attempt near support](https://www.google.com/goto?url=CAESnAEBxCJF1-ZGsky0yfD4fhnK5FRxRzaW75ENMefeCojPjEBtkl381A01AgpQJPbYSMPa5tICWgpcRVQ_Q6rU4cUbB8G7pmbcJ3pBd77zwNzeOqbdvgLXWDaWe5azeB-lhwN7O8p1inS7LPtf0J2_M1QE8NsCoG-ih98PIw0ZrnSbH3jVBt7vTCTpDQ2e_SRZy6fRKdiIvBj0VnruLmo&gsessionid=PDrFd6k3ht4Z4YCj7LHum9hjaFMR-hHbnkDrHkjjYd9RdVw-mYuJ1A)  
  <sub>Blockchain News, 7 hours ago</sub>  
  iShares MSCI South Korea ETF (EWY) is trading at $127.82 after a 1.32% rise, but the ETF remains below its short-, medium- and long-term moving averages...
- [Direxion South Korea Bull 3X ETF (KORU) Price Prediction: Bears still control the tape, but the fund is scraping key support](https://www.google.com/goto?url=CAESmQEBxCJF1-vSSRJF0jipgBaznVg28o0aHc423pacm6GuE-6X0AouBx2L9aIa9eBiJ2VVP6JzBHFit6VFNJs3gKPGAFJqZQYlbX-ew1o77QWCzcTSwKlBVy43RFJ9Z0PXCVoTW27MjwVD5GwiafQ0k4ZCvcHuXGdRp39eNBaZF0Xem8o2ISnxuOeRQ96X1rj63azhYj8oV9oPti8&gsessionid=PDrFd6k3ht4Z4YCj7LHum9hjaFMR-hHbnkDrHkjjYd9RdVw-mYuJ1A)  
  <sub>Blockchain News, 7 hours ago</sub>  
  Direxion South Korea Bull 3X ETF (KORU) is trading at $5.24, up 4.07% on the day, but the structure remains fragile with price still below every major...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 135.19 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 144.22 (-6.3%), 50d 162.15 (-16.6%), 200d 164.36 (-17.7%); 50d below 200d
Momentum: RSI(14) 41.9 | MACD -8.258 vs signal -7.901 (histogram -0.357)
Returns: 1d +9.7% | 5d -1.0% | 1m -10.6% | 3m -25.0%
52-week range: 88.58 - 219.20 (now 35.7% of the way up)
Volatility: ATR(14) 7.88 (5.8% of price) | annualised 20d 83.7%
Volume: 0.39x the 20-day average
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
Three-year record: +27.8% a year | beta to the market 2.62
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
Share count change: 1 week: +9.0% (1.86B) over 7d | 1 month: +5.5% (1.19B) over 36d
Shares outstanding: 166.83M | fund size: 22.55B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [EWZ Dec 2026 28.000 put (EWZ261211P00028000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/EWZ261211P00028000/chart/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Interactive Chart for EWZ Dec 2026 28.000 put (EWZ261211P00028000), analyze all the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 29.27 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 31.70 (-7.6%), 50d 36.60 (-20.0%), 200d 36.79 (-20.4%); 50d below 200d
Momentum: RSI(14) 29.3 | MACD -2.185 vs signal -2.039 (histogram -0.146)
Returns: 1d +2.6% | 5d -5.3% | 1m -31.3% | 3m -18.4%
52-week range: 28.54 - 43.54 (now 4.9% of the way up)
Volatility: ATR(14) 1.03 (3.5% of price) | annualised 20d 29.7%
Volume: 0.21x the 20-day average
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
Three-year record: -0.2% a year | beta to the market 0.92
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
Weighted price target: +43.5% above the current prices
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
Shares outstanding: 200.55M | fund size: 5.87B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Gold (GLD) · Commodity — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Gold prices have been falling sharply and technicals show a downtrend, but there are no macro surprises, the cost of holding the ETF is essentially neutral, and the modest reduction in large‑speculator net long positions does not provide a clear directional edge. With mixed news sentiment and low trading volume, the safest view is neutral.

**Main reasons it gave:**
- Gold down ~22% in three months (BigGo Finance)
- RSI 35.5 and price below 20‑d, 50‑d, 200‑d SMAs (technicals)
- Large speculators net long 25.2% but fell 2.5% week‑over‑week (CFTC)
- Cost of holding -0.7% p.a., effectively zero (cost of holding)

<details><summary><b>News</b> — score -0.30</summary>

- [Why Did Bitcoin Drop 13.85% in a Week as United States Gasoline Fund (NYSEARCA:UGA), United States Oil Fund (NYSEARCA:USO), SPDR Gold Shares (NYSEARCA:GLD) and iShares Bitcoin Trust (NASDAQ:IBIT) Fell Too?](https://kalkine.com.au/news/mutual-funds-etfs/why-did-bitcoin-drop-1385-in-a-week-as-united-states-gasoline-fund-nysearcauga-united-states-oil-fund-nysearcauso-spdr-gold-shares-nysearcagld-and-ishares-bitcoin-trust-nasdaqibit-fell-too)  
  <sub>Kalkine, 23 minutes ago</sub>  
  Why Did Bitcoin Drop 13.85% in a Week as United States Gasoline Fund (NYSEARCA:UGA), United States Oil Fund (NYSEARCA:USO), SPDR Gold Shares (NYSEARCA:GLD)...
- [Gold Sinks 22% in Three Months as Safe-Haven Status Comes Under Fire](https://finance.biggo.com/news/daa966b9-7b26-419e-aec0-affe810b46b3)  
  <sub>BigGo Finance, 4 hours ago</sub>  
  Gold has fallen 21.6% and silver 38.7% since the start of September, putting both metals on course for their worst three-month stretches in decades.…
- [GLD NTA 20-11-2026 $3.50483](https://www.google.com/goto?url=CAESgwEBxCJF123AKCKSXnikASgjAfsKygXbczAjSdaQcLH1UlFvvcHspxlhhiRidS9EphGqfVoeQSuzGh1rb_gTCdHjT98QNLKVAROVGYX-H_lmhT5rHUlV1sfRn-yqwUSEBwdcbLXrkxNggejhbxOv2ZNmJvzfPekGHiEusiHJNuGywdAfww&gsessionid=xOJCK4gxqfF46ghH825a3CIu8aBrRxRYzxtz3mR8V5jjunnkuxklzQ)  
  <sub>BusinessDesk, 17 hours ago</sub>  
  View the full NZX announcement for Smart Gold ETF (GLD): GLD NTA 20-11-2026 $3.50483. Financial updates and company disclosures on BusinessDesk.
- [What Hit Tesla (NASDAQ:TSLA), United States Oil Fund (NYSEARCA:USO), iShares Bitcoin Trust (NASDAQ:IBIT) and SPDR Gold Shares (NYSEARCA:GLD) as Bitcoin Slid to USD 55,106?](https://www.google.com/goto?url=CAESggIBxCJF18ILdsX6oZB5drxiQNhh6RNgAgeMyDMK4reB4T6J_DLtAYTakKcQ8SgtC2cgZgqZ3wycEV50fHKDqlWDOq0F-15coLNTmu6c4ZFq7fHncTlWi7JGYCM7rpKKGNrnkz2nLdtbpndnulbNjWnHSCRSt21vLFPtxpe_HFEX1agxCbXK_oKF6JbCpv4rvI9wRPgDKTlaFYe23-PWytHHZSR_7wWQYnDxwSVa0LscYSwtSj_clLlUEgI__c31W0BWdp6Qs22XJaCLgl352seyU97oQLRvxTLkRHvAmZARcw1HI7JyaEXaoilp8P0n3cbJJNFmcLpTPvBgsMlJM7xgwbA&gsessionid=xOJCK4gxqfF46ghH825a3CIu8aBrRxRYzxtz3mR8V5jjunnkuxklzQ)  
  <sub>Kalkine, 23 minutes ago</sub>  
  What Hit Tesla (NASDAQ:TSLA), United States Oil Fund (NYSEARCA:USO), iShares Bitcoin Trust (NASDAQ:IBIT) and SPDR Gold Shares (NYSEARCA:GLD) as Bitcoin Slid...
- [Peter Schiff Says Gold’s 35% Crash Is a ‘Fire Sale’ Ahead of a Financial Crisis: ‘You Got to Buy Now’](https://www.google.com/goto?url=CAES2AEBxCJF14pnI4OREx5SlUYa6k5B36VT-XGdyiR2LFHpSlCFmP33Bi9mKYnOaPQyHZuEyQf7fbvV-Ko5ALJ6R4W-eFJw7txPUZsYqkC-mNMub62HaP63qpHfJxBtIuoGhr0iRutAYN2nUbpxz-LD_9IsYJcP4U9_SFSbN8PJgo6AUi48aYtzS17QYeLTfnseTYlQ5wY7YqDe_uzhH62-HC8GBLoZb7MAmR6euctufwjHNeD4fu1nKAsc5hF69I-3B4fc_IGdlSgxtmtZkyGXRarILwMAxbYPiTk&gsessionid=xOJCK4gxqfF46ghH825a3CIu8aBrRxRYzxtz3mR8V5jjunnkuxklzQ)  
  <sub>TradingView, 7 hours ago</sub>  
  Gold's steep pullback may offer investors a rare buying opportunity before the next financial crisis, according to veteran economist Peter Schiff,...
- [Bond Funds Cushion 60 40 Portfolios During Stock Market Selloff](https://www.google.com/goto?url=CAESdgHEIkXXfgwIQT7i_t6td6yhVaX0SxjbTtzn7zQPbougggO9ODSt4RxXDToWDZDTI1W6AffW0EF5-W-tI4hU_IxdOy0QvmoMSX-mXuPybYyAxkwGa5Gweg1m3Vog44F_sf8mvYZS1K9ipYzqFqrI6PfKO3rclDc&gsessionid=xOJCK4gxqfF46ghH825a3CIu8aBrRxRYzxtz3mR8V5jjunnkuxklzQ)  
  <sub>cwibc.co.id, 34 minutes ago</sub>  
  U.S. bond funds gained during the November 16-20 stock selloff, limiting losses for 60/40 portfolios as the S&P 500 and gold declined.
- [Gold Price Recovery Expected Amid Market Volatility (GLD)](https://www.google.com/goto?url=CAESmwEBxCJF12iqftyHephjMTnOOU62uHUE5FWhlv3EkHH6iqRiiFFR834GUsaUFYs0YICNrOAzewU8qVq9z_FTikQhcKsp1I4gkfg-O9JEgTx-kXnriuBkNPsyHV2Y92Eq2Rte8OMQtkOjSM3fnkj_w8BP-sSIcm9sg6RZWilxZRFz9HEDJ4HRKhOjsOHI3JMXENzu_1Y2CGDjufTY_Q&gsessionid=xOJCK4gxqfF46ghH825a3CIu8aBrRxRYzxtz3mR8V5jjunnkuxklzQ)  
  <sub>GuruFocus, 2 hours ago</sub>  
  On November 23, 2026, Goldman Sachs reported a significant decline in gold prices, dropping approximately 8% last week, primarily due to a sharp downturn in...
- [Lost money on a gold fund this year? The tax rule most gold investors don't know, and the December 31 dead](https://www.google.com/goto?url=CAES9QEBxCJF1wXryzZPimClL0HBOtuLof8L3I-Qh3z-FOJOr2KnT_dXlgUVz758jHo4XCQlWyHMJZK3JkcGvTTGBELgxlQA7DU4orOnt-5fJhVSQhNUqs3NQcXksjcSNy4OaqCu9WWrcItgS52kK2DQqG2v1Mus3cyeqDcNHZGXNifG0iS_A2pgAKuZO8nE4RLkV-O6RxguJ6waKIFKznLb1KtXS9AUr6utemRVsx3I3bQWvdVXvwoGUiLOJPKwCI-EjWk6Cp9dWx1lJ5-5qSV8QKrliUdQJpnjZ-6Pz9rKmt112dXJYI4IERdfphcM3bVI35pHqqzjKw&gsessionid=xOJCK4gxqfF46ghH825a3CIu8aBrRxRYzxtz3mR8V5jjunnkuxklzQ)  
  <sub>The Economic Times, 20 hours ago</sub>  
  Gold ETF investors sitting on losses have until December 31 to sell and potentially offset capital gains on their 2026 tax returns.
- [Robinhood on-chain: iShares Silver Trust token supply rises as trading reaches $686,858](https://www.google.com/goto?url=CAESawHEIkXXiKTjK-bmo9ws3jS5Aq3EUJHnmf9vWY6JC_0S8xEjKYTezUr0NUw7jZALEoahOJ89rdP7HLR8-20ufg8ifDdmfdQEc4LFvHQRnpdb-yYK8T9rOnpr4-2DgUr84zeBB04sSvUcPuZR&gsessionid=xOJCK4gxqfF46ghH825a3CIu8aBrRxRYzxtz3mR8V5jjunnkuxklzQ)  
  <sub>www.tokenpost.com, 2 hours ago</sub>  
  SLV token supply increased by 1732 as 24-hour trading value reached $686858. Alphabet Class A led holder-wallet gains among the listed tokenized stocks in...
- [Gold Losing Its Safe-Haven Status? Morningstar Says The Precious Metal Is Trading More Like A Speculative Asset](https://www.google.com/goto?url=CAESvwEBxCJF147C8BhFhANwWCcVHBFAqpuB9T2WhMgOPDJLmvi3bWv1lWeTW7PVppgaabQ074hU5V1dRN-0w8Lkk3RmDsoJxA8SIe_PdqPfvuNpoOcY50HzlNmdeg1NVsFDIdzCxgPJm68VB2rHEStzT9m9ltQpw1YBus5mcCWsmo6MI22au6x6LbkcSkwWci-3o3t0M89L_D5CG-I2pZJ_8UCBw8lX-EIB0nFKVobebPa9T3tE_7vbMZhU5De4b9uzxQ&gsessionid=xOJCK4gxqfF46ghH825a3CIu8aBrRxRYzxtz3mR8V5jjunnkuxklzQ)  
  <sub>Stocktwits, 11 hours ago</sub>  
  Amy C. Arnott, a portfolio strategist at Morningstar, said on Friday that gold has been trading more like a speculative asset rather than a safe haven.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.30</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 336.36 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 358.85 (-6.3%), 50d 373.77 (-10.0%), 200d 405.23 (-17.0%); 50d below 200d
Momentum: RSI(14) 35.5 | MACD -11.176 vs signal -8.037 (histogram -3.138)
Returns: 1d +4.2% | 5d -4.7% | 1m -8.2% | 3m -21.4%
52-week range: 322.87 - 495.90 (now 7.8% of the way up)
Volatility: ATR(14) 7.97 (2.4% of price) | annualised 20d 35.4%
Volume: 0.33x the 20-day average
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
Cost of holding this fund instead of gold itself: -0.7% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund -21.4%, commodity -21.8%, gap +0.3% | 6 months: fund -18.8%, commodity -18.4%, gap -0.3% | 12 months: fund -10.3%, commodity -9.5%, gap -0.7%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: GOLD - COMMODITY EXCHANGE INC. (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 25.2% of open interest (407,834 contracts)
Change on the week: -2.5% of open interest
Crowding: 30% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 260.30M | fund size: 87.56B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Fund shows bearish fundamentals – a large build in weekly US natural‑gas inventories, an EIA forecast of roughly 11% price decline over six months, and a heavy -10.4% annual roll‑cost drag – and technicals indicate price below the 50‑day and 200‑day averages with a recent 7.1% one‑day drop. However there is no macro surprise or decisive technical breakout, and the crowded short position could be near a reversal. With no clear catalyst, we stay neutral with low conviction.

**Main reasons it gave:**
- Weekly US natural gas inventories built 20 Bcf to 3,882 Bcf (96th percentile) – bearish supply
- EIA price outlook projects ~11% decline over six months (from $2.66 to $2.37) – bearish price expectation
- Cost of holding fund shows -10.4% annual drag from roll cost – heavy negative carry
- Technicals: price $9.81 below 50‑day ($10.27) and 200‑day ($10.91) SMAs, recent 1‑day drop of 7.1% – short‑term weakness
- CFTC positioning: large speculators net short 13% of OI, crowding short with a +0.7% increase – bearish sentiment

<details><summary><b>News</b> — score +0.00</summary>

- [UNG Nov 2026 15.500 put (UNG261125P00015500) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/UNG261125P00015500/)  
  <sub>Yahoo Finance Singapore, 11 hours ago</sub>  
  Find the latest UNG Nov 2026 15.500 put (UNG261125P00015500) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 9.81 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 9.79 (+0.1%), 50d 10.27 (-4.6%), 200d 10.91 (-10.1%); 50d below 200d
Momentum: RSI(14) 46.7 | MACD 0.031 vs signal -0.040 (histogram 0.071)
Returns: 1d -7.1% | 5d -0.1% | 1m +2.4% | 3m -4.2%
52-week range: 9.00 - 16.90 (now 10.2% of the way up)
Volatility: ATR(14) 0.43 (4.4% of price) | annualised 20d 55.1%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.45</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.45</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.45</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.45</summary>

```text
Cost of holding this fund instead of natural gas itself: -10.4% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -4.2%, commodity +26.6%, gap -30.8% | 6 months: fund -10.1%, commodity +21.2%, gap -31.3% | 12 months: fund -32.0%, commodity -21.6%, gap -10.4%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.45</summary>

```text
US inventories, week ending 2026-11-13 (published the following Wednesday)
  Natural gas: 3,882.0 billion cubic feet, +20.0 on the week (a build), 96% percentile over 52 weeks -- high for the time of year
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
Share count change: 1 week: +1.6% (7.44M) over 7d | 1 month: +20.3% (80.67M) over 36d
Shares outstanding: 48.79M | fund size: 478.39M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Inflation 3.7% above target but no surprise
- Cost of holding -8.1% annual, heavy roll cost
- Share count +31.6% over 1 month, strong inflows
- Large speculators net long 16.3% OI, down -0.7% week
- Price 10.44 below 20d SMA 11.06, RSI 33 (oversold)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 10.44 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 11.06 (-5.7%), 50d 11.49 (-9.2%), 200d 10.34 (+1.0%); 50d above 200d
Momentum: RSI(14) 33.0 | MACD -0.321 vs signal -0.242 (histogram -0.079)
Returns: 1d +2.0% | 5d -4.5% | 1m -14.1% | 3m -6.1%
52-week range: 9.02 - 12.47 (now 41.1% of the way up)
Volatility: ATR(14) 0.21 (2.1% of price) | annualised 20d 27.1%
Volume: 0.09x the 20-day average
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
Measured: 3 months: fund -6.1%, commodity +0.6%, gap -6.7% | 6 months: fund +6.5%, commodity +19.5%, gap -13.0% | 12 months: fund +10.4%, commodity +18.6%, gap -8.1%
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
Share count change: 1 week: +6.6% (3.70M) over 7d | 1 month: +31.6% (14.27M) over 30d
Shares outstanding: 5.69M | fund size: 59.40M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise or policy shift; technicals show the price below its 20‑day, 50‑day and 200‑day SMAs and RSI is low, but there is no decisive break on volume. Cost of holding the fund is heavily negative (~‑9% annual), which is a bearish drag on long exposure. CFTC data shows a modest reduction in net short positions (-0.6% week), a slight bullish tilt, but recent fund outflows (‑13.6% share count over the month) indicate weaker demand. With mixed signals and no clear catalyst, we keep a neutral stance.

**Main reasons it gave:**
- Inflation 3.7% and unemployment 4.1% on target, no macro surprise
- Price 17.05 below 20‑day SMA 17.22, 50‑day SMA 18.26, 200‑day SMA 18.17 – downtrend
- Cost of holding fund vs corn: -9.3% annual, heavy negative carry
- CFTC net short 1.7% of OI, weekly change -0.6% (short positions fell) – modest bullish tilt

<details><summary><b>News</b> — score +0.00</summary>

- [Corn Starting Thanksgiving Week with Gains](https://www.barchart.com/story/news/8964217/corn-starting-thanksgiving-week-with-gains)  
  <sub>Barchart.com, 1 hour ago</sub>  
  Corn price action is up 3 to 4 cents in early Monday trade. Futures close the Friday session with contracts down 1 ¼ to 4 ½ cents across the board,...
- [New Black Sea Wheat and Corn Futures Introduced to Hedge Grain R](https://www.gurufocus.com/news/9214395/new-black-sea-wheat-and-corn-futures-introduced-to-hedge-grain-risks)  
  <sub>GuruFocus, 5 hours ago</sub>  
  On November 23, 2026, the European exchange announced the launch of new Black Sea wheat and corn futures, aimed at enhancing trading efficiency and risk...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 17.05 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 17.22 (-1.0%), 50d 18.26 (-6.6%), 200d 18.17 (-6.1%); 50d above 200d
Momentum: RSI(14) 38.2 | MACD -0.318 vs signal -0.356 (histogram 0.038)
Returns: 1d +0.9% | 5d -0.9% | 1m -3.6% | 3m -13.0%
52-week range: 16.47 - 20.29 (now 15.2% of the way up)
Volatility: ATR(14) 0.24 (1.4% of price) | annualised 20d 15.2%
Volume: 0.41x the 20-day average
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
Cost of holding this fund instead of corn itself: -9.3% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -13.0%, commodity -9.5%, gap -3.5% | 6 months: fund -6.2%, commodity -1.0%, gap -5.2% | 12 months: fund -3.1%, commodity +6.2%, gap -9.3%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.20</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 1.7% of open interest (1,954,229 contracts)
Change on the week: -0.6% of open interest
Crowding: 30% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +0.3% (279.43K) over 7d | 1 month: -13.6% (-16.87M) over 30d
Shares outstanding: 6.28M | fund size: 107.13M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance due to mixed signals: bearish positioning and cost of holding versus strong fund inflows and no decisive technical break.

**Main reasons it gave:**
- Positioning: net long down 2.1% of OI, crowded short (2% percentile) indicating bearish tilt
- Fund flows: share count up 10% in the past week, indicating strong demand
- Cost of holding: -2.7% annual drag on long positions
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs and RSI 35, no decisive break on volume

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 34.63 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 37.28 (-7.1%), 50d 38.80 (-10.8%), 200d 37.92 (-8.7%); 50d above 200d
Momentum: RSI(14) 35.0 | MACD -1.412 vs signal -1.012 (histogram -0.400)
Returns: 1d +5.2% | 5d -3.9% | 1m -11.3% | 3m -15.0%
52-week range: 31.07 - 41.43 (now 34.4% of the way up)
Volatility: ATR(14) 0.85 (2.5% of price) | annualised 20d 35.3%
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
Cost of holding this fund instead of copper itself: -2.7% a year -- a steady drag
Measured: 3 months: fund -15.0%, commodity -14.8%, gap -0.2% | 6 months: fund -11.3%, commodity -10.1%, gap -1.1% | 12 months: fund +12.5%, commodity +15.3%, gap -2.7%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.35</summary>

```text
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 9.1% of open interest (314,991 contracts)
Change on the week: -2.1% of open interest
Crowding: 2% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.35</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +10.0% (61.70M) over 7d | 1 month: +8.9% (55.15M) over 30d
Shares outstanding: 19.56M | fund size: 677.20M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance as no material macro surprise or decisive technical break; mixed signals from positioning, flows, and fundamentals.

**Main reasons it gave:**
- Fund flows: share count +17.1% week over week
- Positioning: net long down 2.1% week, crowding short at 2% percentile
- Technicals: price 39.51, below 20d/50d/200d SMAs, RSI 31.6, MACD -3.191
- Macro: no policy surprise, dollar index up 0.55, VIX up 3.9

<details><summary><b>News</b> — score +0.00</summary>

- [October’s Silver Slump Creates an Opportunity to Buy the Dip](https://etfdb.com/gold-silver-investing-content-hub/october-silver-slump-creates-opportunity-buy-dip/)  
  <sub>ETF Database, 30 minutes ago</sub>  
  The price of silver plummeted in October, but Sprott's research shows that investors seemed eager to buy into the dip.
- [Silver & Its Miners: The Pullback Is A Buying Opportunity (NYSEARCA:SIL)](https://seekingalpha.com/article/4971066-silver-and-its-miners-the-pullback-is-a-buying-opportunity)  
  <sub>Seeking Alpha, 29 minutes ago</sub>  
  I maintain a long-term buy on silver and miners: the pullback from over $120/oz to about $41/oz offers an attractive entry point.
- [Gold Sinks 22% in Three Months as Safe-Haven Status Comes Under Fire](https://www.google.com/goto?url=CAESgAEBxCJF1zFZ2SiyLAdNevPUEYRgnzZL0vtxPPFGXpXjC6z_SKQbEmNQ-bpRaBLyNZR821hp95DTUAw0H1oQwf10PO2GnVAu1m82eOAJ_hkBJNyy-pzwZFn-_UPBPIoniSouPVBwV2M1FmxKA0YIMAu49JDNMWxmEU3a44fVzAZ0RQ&gsessionid=rrq4beFkshZgOGZp1yn0Jv7anxhzEokvq87FX1yA0PMyWSmZ3y-gKw)  
  <sub>BigGo Finance, 4 hours ago</sub>  
  Gold has fallen 21.6% and silver 38.7% since the start of September, putting both metals on course for their worst three-month stretches in decades.…
- [News by CNBC TV18 on TradingView, 2026-11-23 — cnbctv:41e33c76b094b:0](https://www.google.com/goto?url=CAESdQHEIkXXIZAeoEjmZop01tky6FV3oqb17S3_2vz7pkcs947FkC8g8MkTvJwq7r3CKqB4qwQWibr-5U0iWSfAbufR-xAVATzeq-wcZVZzO0MwGO9rBf9JB4oLq5YU1DQH5OUPhjaaHcDOnMmJWWReAbJjqYx0-w&gsessionid=rrq4beFkshZgOGZp1yn0Jv7anxhzEokvq87FX1yA0PMyWSmZ3y-gKw)  
  <sub>TradingView, 5 hours ago</sub>  
  DSP Mutual Fund plans to gradually increase its exposure to gold and silver after maintaining an underweight position in the two metals since the launch of...
- [Global X Silver Miners ETF (SIL) stock price, news, quote and history](https://www.google.com/goto?url=CAESZAHEIkXXSY_MHWdAzW8RsgRF_HauWeP_cBClh5pUbDngfLiK37JZLHnOfvhtuMyvKkHQm2zwOAt1EIbEbC7bBUUt2gHQSo56wym6kaMlZCnl6Kq7xtxQB3xEzkyE9NlcAQGkgPM&gsessionid=rrq4beFkshZgOGZp1yn0Jv7anxhzEokvq87FX1yA0PMyWSmZ3y-gKw)  
  <sub>Yahoo Finance Singapore, 18 hours ago</sub>  
  Global X Silver Miners ETF (SIL) ... This price reflects trading activity during the overnight session on the Blue Ocean ATS, available 8 p.m. to 4 a.m. ET,...
- [Global X Funds Global X Silver Miners Etf (Post Rev Spl (SIL) Stock Price | Quotes & News](https://www.google.com/goto?url=CAES_QEBxCJF183mMzijLzcYSYcxFhkkZoCbGGLwI_mq_pHYHePbHvsz9K_8dUtttcp7TxhkH5SRWF1rtCS4q9KKjM4s0tMYmHEwxgaSOQOrPTJNa0Yq75UyOXsqqecruxRRcjEFk75GXPrjz7IExzwyB4o4l4BH7Hf71Mb4PNQJhDgLR7HCsdgE7XstPlhykO3nLmBovQ4WHqVe3KuGS7hJwqblmUrlFZVVtTkAJ9QC--TfIuA1leGvvRgv1BSW00cPnyJrsJZU-H9nHRRmnV0ePfT4sVUMDffKj8cFaG6DG4g9wpfPy_xvtzpCacOiZu8pVbJe0_NmaVOgXCn5fMAY&gsessionid=rrq4beFkshZgOGZp1yn0Jv7anxhzEokvq87FX1yA0PMyWSmZ3y-gKw)  
  <sub>Moomoo, 19 hours ago</sub>  
  Track the latest Global X Funds Global X Silver Miners Etf (Post Rev Spl (SIL) price, quotes, financial information, news, and analyst ratings on moomoo App...
- [Current price of silver as of Monday, Nov. 23, 2026](https://www.google.com/goto?url=CAESfAHEIkXXTtWbEkNVnR4zOVTnMUSYXTWvdVhZmtCL2oF5DM9q5ZL-oMIkwTWXq17xZ2Vmm4ctEg3Bexra_WBvHpu5hq_Zpo2naicxMkhQtaQsH6dtbggOoJdYBNsTaNtg9WtH9AMvHOOVeNhuplDJ_3jUcZIwN3SVU2Bz1uw&gsessionid=rrq4beFkshZgOGZp1yn0Jv7anxhzEokvq87FX1yA0PMyWSmZ3y-gKw)  
  <sub>Fortune, 1 hour ago</sub>  
  If you're worried about increased inflation, adding precious metals like silver to your portfolio can be a smart choice.
- [Gold and Silver Price Forecast: Strong Dollar Caps Rebound Before PCE](https://www.google.com/goto?url=CAEStAEBxCJF14z0q0OmE0CySdXC3ar5rzYQ1G5n9zJWJ0wK1J6ewneyCS2oqWDBoL0dAdZYDvJn78FWKlTA7Q30GkPqBr7VXivbSvmOeLv5aPWjATMARYoeSQk6r1U_doppt_EFXoLPWDetGgiNWoNnw7nnG-BZeHuPKAgQ1s1fkT4P6WmuwUhpTCAfSkyCooV95q0efixf7QsC5a41-vEyLw95iDvpnGetTOE8uFeM52M__mkUAts&gsessionid=rrq4beFkshZgOGZp1yn0Jv7anxhzEokvq87FX1yA0PMyWSmZ3y-gKw)  
  <sub>FXEmpire, 4 hours ago</sub>  
  Gold and silver rebound after sharp losses, but the strong US dollar keeps prices under pressure as traders await Wednesday's PCE inflation data.
- [Silver Bow Mining Joins Nasdaq Junior Silver Miners Index](https://www.google.com/goto?url=CAESzQEBxCJF18uVaVe4akaMRZEbupzb2VrGjRZmKIIDQ3nUJTw-hGPdSLcFxaW5T4vwqC3CS4-_jrD4geVYb6BqO6dOIz9lPe2S3Y4_lRG41ZRcua2JJ4Aa7JSinyhHjookC6s-FOjEsa52rY804QsOhZxzsw4lC2RWGMue9-pqEl1p_pIA6PIiWvH67cM87Gz0zEcl6E4UMZXx_jcorb0l9K8M6y4yxpBABwFMYn9ZSZVBceekGxIYGCgg_dy0hBN4Swr_t32dfnLqAQ-Nkuba&gsessionid=rrq4beFkshZgOGZp1yn0Jv7anxhzEokvq87FX1yA0PMyWSmZ3y-gKw)  
  <sub>The Globe and Mail, 2 hours ago</sub>  
  Index inclusion raises profile as underground exploration advances efforts to expand Rainbow Block's 170-million-ounce silver equivalent Inferred Mineral...
- [Silver price today: Silver rises, according to FXStreet data](https://www.google.com/goto?url=CAESvAEBxCJF10SE79TZVw1MTVqHeLeaql-aJHN0VuB1E-I3aSaA0Afi-gwshntpSNbcwOXdYIwnYob5CCxwUx4hMqX2fbZyji8wnKXQC4g5BvY4KoRStpZm9pYYgOSDBIEZtHwMfC0muYfc9QxcEdbr1fBjVXCLp5E0X5yk1GRsHWeQy-tZPSFPLSjnEP4OGDS5jQHsZ5THFXn0CN9TiE6_01FI_RNDNKCP4f0r0LCK9c2W5Vp_5Vzgwxe5o8vxsw&gsessionid=rrq4beFkshZgOGZp1yn0Jv7anxhzEokvq87FX1yA0PMyWSmZ3y-gKw)  
  <sub>www.tmgm.com, 5 hours ago</sub>  
  Silver prices (XAG/USD) rose on Monday, according to FXStreet data. Silver trades at $42.60 per troy ounce, up 3.96% from the $40.97 it cost on Friday.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 39.51 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 44.69 (-11.6%), 50d 50.66 (-22.0%), 200d 60.92 (-35.1%); 50d below 200d
Momentum: RSI(14) 31.6 | MACD -3.191 vs signal -2.682 (histogram -0.508)
Returns: 1d +6.9% | 5d -6.8% | 1m -18.9% | 3m -36.6%
52-week range: 36.97 - 105.60 (now 3.7% of the way up)
Volatility: ATR(14) 1.75 (4.4% of price) | annualised 20d 55.6%
Volume: 0.51x the 20-day average
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
Cost of holding this fund instead of silver itself: -0.5% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund -36.6%, commodity -36.5%, gap -0.1% | 6 months: fund -43.3%, commodity -42.9%, gap -0.5% | 12 months: fund -13.7%, commodity -13.2%, gap -0.5%
A commodity fund holds futures, not silver, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

```text
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 1.0% of open interest (122,945 contracts)
Change on the week: -2.1% of open interest
Crowding: 2% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +17.1% (3.59B) over 7d | 1 month: +12.5% (2.72B) over 36d
Shares outstanding: 620.04M | fund size: 24.50B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Macro data stable: inflation 3.7% and unemployment 4.1% within expectations
- Positioning net long 11.4% of OI, down 0.7% week, indicating slight reduction in bullish bets
- Fund flows: -9.3% share count over month, indicating net outflows
- Technical indicators mixed: price above 20‑day SMA (+0.1%) but below 50‑day SMA (-3.6%), RSI 44.8
- Cost of holding low at 0.9% annual, no directional bias

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 25.78 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 25.76 (+0.1%), 50d 26.73 (-3.6%), 200d 25.37 (+1.6%); 50d above 200d
Momentum: RSI(14) 44.8 | MACD -0.276 vs signal -0.323 (histogram 0.047)
Returns: 1d +0.8% | 5d +0.0% | 1m -3.8% | 3m -1.9%
52-week range: 21.71 - 28.14 (now 63.3% of the way up)
Volatility: ATR(14) 0.29 (1.1% of price) | annualised 20d 15.0%
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
Cost of holding this fund instead of soybeans itself: 0.9% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund -1.9%, commodity +0.1%, gap -2.0% | 6 months: fund +3.5%, commodity +3.6%, gap -0.2% | 12 months: fund +10.5%, commodity +9.5%, gap +0.9%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 11.4% of open interest (997,948 contracts)
Change on the week: -0.7% of open interest
Crowding: 28% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +0.8% (330.89K) over 7d | 1 month: -9.3% (-4.05M) over 30d
Shares outstanding: 1.54M | fund size: 39.69M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> All three analytical dimensions (news, technicals, fundamentals) tilt modestly bearish, but no clear macro surprise, decisive technical break, or other material catalyst has emerged. The CFTC positioning shows a slight reduction in net long exposure, while inventories are building and the EIA outlook is for falling crude prices, reinforcing bearish fundamentals. However, strong recent fund inflows indicate notable demand for the exposure, offsetting the bearish bias. Given the mixed evidence and the absence of a decisive catalyst, a neutral stance with low conviction is appropriate.

**Main reasons it gave:**
- Crude oil inventories built 3.4 M barrels (weekly build)
- EIA forecasts WTI to fall from $97 to $84 in six months (bearish)
- USO price 8.1% below 20‑day SMA and 9.7% below 50‑day SMA; MACD negative
- CFTC net long 0.8% of open interest, down 0.5% week‑over‑week
- Fund shares increased 27.9% over the past month (large inflows)

<details><summary><b>News</b> — score -0.15</summary>

- [Why Did Bitcoin Drop 13.85% in a Week as United States Gasoline Fund (NYSEARCA:UGA), United States Oil Fund (NYSEARCA:USO), SPDR Gold Shares (NYSEARCA:GLD) and iShares Bitcoin Trust (NASDAQ:IBIT) Fell Too?](https://kalkine.com.au/news/mutual-funds-etfs/why-did-bitcoin-drop-1385-in-a-week-as-united-states-gasoline-fund-nysearcauga-united-states-oil-fund-nysearcauso-spdr-gold-shares-nysearcagld-and-ishares-bitcoin-trust-nasdaqibit-fell-too)  
  <sub>Kalkine, 24 minutes ago</sub>  
  Why Did Bitcoin Drop 13.85% in a Week as United States Gasoline Fund (NYSEARCA:UGA), United States Oil Fund (NYSEARCA:USO), SPDR Gold Shares (NYSEARCA:GLD)...
- [Real-Time Stock News, SEC Filings & Alerts](https://www.quantisnow.com/etfs)  
  <sub>Quantisnow, 17 hours ago</sub>  
  Browse US-listed exchange-traded funds A to Z, with latest price, daily change and one-year return. ETFs are funds, not companies.
- [What Hit Tesla (NASDAQ:TSLA), United States Oil Fund (NYSEARCA:USO), iShares Bitcoin Trust (NASDAQ:IBIT) and SPDR Gold Shares (NYSEARCA:GLD) as Bitcoin Slid to USD 55,106?](https://www.google.com/goto?url=CAESggIBxCJF10qpX-UQ7kaZFWb8X5vYebEXm6fpnsr9ux2evzpRNhXViETxZ0xY7owOMva9X9C6HNu97o97uiQu2mtGPHvq5tF8T8QmRRYWbMGbCFUioE24mYxyQ9f7rkYo_q8o55vEBQ9_sDUujueGoJmOQANCinqotYhypcKF60FO9n_7OPHXvS17xbp-jUB4Uk8ACvpy-XTDjF7SkqME7zxgOJQK-jdru36XPKJtthjXk3yyPdmh7CLDFC11E2260c8w25fHsTWxlG1OJQ_cwQm29WaK6DAWZYdHz2O1RhR2ddMlCThZo_GqLXJ5vasnZ_fEPpyGjeZJLv-WEESAI8Ex_TE&gsessionid=9lmbspG9DqVy4ZYE-Mkyc18gjYeogUXeT1zUMnhADVS-IGoUhp9oig)  
  <sub>Kalkine, 24 minutes ago</sub>  
  What Hit Tesla (NASDAQ:TSLA), United States Oil Fund (NYSEARCA:USO), iShares Bitcoin Trust (NASDAQ:IBIT) and SPDR Gold Shares (NYSEARCA:GLD) as Bitcoin Slid...
- [Crude oil price analysis as Iran’s IRGC seeks to challenge the US blockade](https://www.google.com/goto?url=CAESrQEBxCJF14k9oQtWiV98rvbGwDdZAB4sjTTsnyWzuk9tE3cHSrTDTeREluXEH0L7Sji2O_ySJieRUzojRsYjr-jCzoC_0gUAvrA7PS4cIfJ05B6DRpB-StfCglCYq1pXlqCZ_VRukTXLw_fc1zcjjElZCoshuyvXGlO8EpabEpCLEt6EG5n058a_4Kz-tipTkOoJH6GFpVzssSXk0yMSsOJaihlmWcxfARf2p9pG1g&gsessionid=9lmbspG9DqVy4ZYE-Mkyc18gjYeogUXeT1zUMnhADVS-IGoUhp9oig)  
  <sub>Invezz, 8 hours ago</sub>  
  Crude oil prices remained under pressure on Monday as investors assessed the state of the ongoing US-Iran war.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.15</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 136.63 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 148.63 (-8.1%), 50d 151.27 (-9.7%), 200d 129.49 (+5.5%); 50d above 200d
Momentum: RSI(14) 36.6 | MACD -4.560 vs signal -3.184 (histogram -1.376)
Returns: 1d -2.1% | 5d -2.4% | 1m -19.4% | 3m +8.3%
52-week range: 66.17 - 169.53 (now 68.2% of the way up)
Volatility: ATR(14) 5.03 (3.7% of price) | annualised 20d 46.9%
Volume: 0.19x the 20-day average
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

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.50</summary>

```text
US inventories, week ending 2026-11-13 (published the following Wednesday)
  Crude oil: 417.8 million barrels, +3.4 on the week (a build), 25% percentile over 52 weeks
  Petrol: 215.9 million barrels, +5.2 on the week (a build), 56% percentile over 52 weeks
  Diesel: 104.9 million barrels, +1.6 on the week (a build), 33% percentile over 52 weeks
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
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-11-17, published the following Friday)
Large speculators: net long 0.8% of open interest (1,869,789 contracts)
Change on the week: -0.5% of open interest
Crowding: 25% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +6.3% (115.22M) over 7d | 1 month: +27.9% (423.51M) over 36d
Shares outstanding: 14.20M | fund size: 1.94B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Macro: yields stable, no policy surprise; VIX up but no major data shock
- Technical: price below 20‑day, 50‑day, 200‑day SMAs, RSI 35, no decisive break
- Positioning: net short 15.2% of OI, slight reduction week over week
- Cost of holding: -10.1% annual, heavy roll cost penalizes longs
- Crop condition: 48% good/excellent, down 7 points YoY, bullish supply

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.15% (+0.03 on the week) | 5-year 4.79% (-0.14 on the week) | 10-year 4.98% (-0.14 on the week) | 30-year 5.34% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.82 points -- upward sloping (normal)
US dollar index: 104.10 (+0.55 on the week)
Volatility (VIX): 26.76 (+3.9 on the week) -- stressed
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 203k (2026-11-14)
Policy and expectations: Fed target 4.00% | market expects 2.1% inflation over 10 years
Rate path: 2-year Treasury 4.76% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 21.32 (bar of 2026-11-23), from 500 daily bars
Trend: vs 20d SMA 21.84 (-2.3%), 50d 23.59 (-9.6%), 200d 23.63 (-9.8%); 50d below 200d
Momentum: RSI(14) 35.1 | MACD -0.596 vs signal -0.655 (histogram 0.059)
Returns: 1d -0.5% | 5d -1.4% | 1m -6.6% | 3m -16.8%
52-week range: 19.88 - 28.00 (now 17.8% of the way up)
Volatility: ATR(14) 0.40 (1.9% of price) | annualised 20d 22.2%
Volume: 0.09x the 20-day average
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
Cost of holding this fund instead of wheat itself: -10.1% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -16.8%, commodity -14.0%, gap -2.8% | 6 months: fund -12.0%, commodity -7.2%, gap -4.8% | 12 months: fund +1.8%, commodity +11.9%, gap -10.1%
A commodity fund holds futures, not wheat, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.20</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-11-17, published the following Friday)
Large speculators: net short 15.2% of open interest (558,414 contracts)
Change on the week: -0.6% of open interest
Crowding: 30% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +0.6% (1.45M) over 7d | 1 month: -9.5% (-24.43M) over 30d
Shares outstanding: 10.92M | fund size: 232.94M
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

