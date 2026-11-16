# Daily report

**16 Nov 2026, 18:33 Israel time (16:33 UTC)** · 80 names checked · 0 traded · 8 with a problem

**Answers with no explanation:** 12 of 49 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 3 | 12 | 1 |
| Whole-market funds | 14 | 0 | 11 | 3 |
| Sector and country funds | 41 | 0 | 37 | 4 |
| Commodities | 9 | 0 | 9 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| Poland (EPOL) · Sector or country | **Stop raised.** At +0.52R, following the price. Stop-loss raised 42.77 → 42.85. |
| Sweden (EWD) · Sector or country | **Stop raised.** At -0.05R, following the price. Stop-loss raised 50.94 → 50.98. |
| Brazil (EWZ) · Sector or country | **Stop raised.** At +0.58R, following the price. Stop-loss raised 34.10 → 33.49. |
| HDFC Bank (HDB) · Company | **Stop raised.** At +2.70R, following the price. Stop-loss raised 24.78 → 25.03. |
| JPMorgan Chase (JPM) · Company | **Stop raised.** At +0.05R, following the price. Stop-loss raised 330.54 → 331.83. |
| US regional banks (KRE) · Sector or country | **Stop raised.** At +0.07R, following the price. Stop-loss raised 69.92 → 70.08. |
| MercadoLibre (MELI) · Company | **Stop raised.** At +0.06R, following the price. Stop-loss raised 1612.69 → 1604.57. |
| Novo Nordisk (NVO) · Company | **Stop raised.** At +0.71R, following the price. Stop-loss raised 38.64 → 39.89. |
| Procter & Gamble (PG) · Company | **Stop raised.** At +1.72R, following the price. Stop-loss raised 162.86 → 165.90. |
| Royal Bank of Canada (RY) · Company | **Stop raised.** At +0.01R, following the price. Stop-loss raised 195.58 → 195.93. |
| Teva Pharmaceutical (TEVA) · Company | **Stop raised.** At +1.44R, following the price. Stop-loss raised 41.52 → 41.85. |
| Toyota (TM) · Company | **Stop raised.** At +0.06R, following the price. Stop-loss raised 204.30 → 205.44. |
| US banks and finance (XLF) · Sector or country | **Stop raised.** At +0.06R, following the price. Stop-loss raised 56.75 → 56.96. |
| US health care (XLV) · Sector or country | **Stop raised.** At +0.11R, following the price. Stop-loss raised 182.28 → 183.37. |
| Elbit Systems (ESLT) · Company | **Holding.** +0.45R, holding 5 shares. Stop-loss 682.06. |
| Canada (EWC) · Sector or country | **Holding.** -0.52R, holding 116 shares. Stop-loss 58.92. |
| South Korea (EWY) · Sector or country | **Holding.** -0.08R, holding 51 shares. Stop-loss 152.20. |
| Alphabet (Google) (GOOGL) · Company | **Holding.** -0.30R, holding 4 shares. Stop-loss 274.24. |
| Defence and aerospace (ITA) · Sector or country | **Holding.** -0.03R, holding 98 shares. Stop-loss 69.44. |
| Microsoft (MSFT) · Company | **Holding.** -0.65R, holding 9 shares. Stop-loss 512.86. |
| Nvidia (NVDA) · Company | **Holding.** +4.60R, holding 9 shares. Stop-loss 179.59. |
| US house builders (XHB) · Sector or country | **Holding.** +0.00R, holding 68 shares. Stop-loss 97.50. |
| US media and communication (XLC) · Sector or country | **Holding.** +2.03R, holding 47 shares. Stop-loss 104.93. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Exxon Mobil (XOM) · Company — BULLISH, confidence 0.68

**Result:** REJECTED · no room under the gross exposure limit

**In the model's own words:**

> Strong fundamentals, significant insider buying, and a material $12.5 B project commitment outweigh bearish technicals. Analyst consensus is modestly positive and the debt‑buyback adds shareholder‑friendly capital allocation. Overall view is bullish with moderate conviction.

**Main reasons it gave:**
- Insiders net bought 6.9 M shares (+369% of holdings) in last 180 days (Insider Activity)
- $12.5 B concrete project commitment announced (Simply Wall St)
- $3 B debt buyback launched across four bond series (Seeking Alpha)
- Fundamentals show low forward P/E 13.33 and 111% YoY earnings growth (Fundamentals)
- Technical indicators bearish: RSI 45.2, MACD negative, volume 0.06× 20‑day average (Technical)

<details><summary><b>News</b> — score +0.60</summary>

- [ExxonMobil Holdings Corporation (XOM) Is a Trending Stock: Facts to Know Before Betting on It](https://finance.yahoo.com/markets/stocks/articles/exxonmobil-holdings-corporation-xom-trending-130004383.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Exxon (XOM) has been one of the stocks most watched by Zacks.com users lately. So, it is worth exploring what lies ahead for the stock.
- [This Spanish Oil Stock Is Beating Exxon and Chevron. Wall Street Sees More Upside.](https://www.barrons.com/articles/repsol-oil-stock-beating-exxon-and-chevron-wall-street-sees-more-upside-597252ad)  
  <sub>Barron's, 4 hours ago</sub>  
  European oil stocks are still much cheaper than American ones.
- [Fund Update: New $787.3M $XOM stock position opened by ENVESTNET ASSET MANAGEMENT INC](https://www.google.com/goto?url=CAESuAEBxCJF1_8pL4xEB5gLN9gu4l_fFo99Es9xR7uZnle6QKrB01uwG-Cvjwsxebe8aBe9_yRpM4BjiUvJE-iA5pNdR-vxaJspoDOXEs2YLGLXRT4FqQYjyuOglW_7q7Pm7tbP2RRL1MqIOWZ6Jhit1ceL0pXtkKYvaJ3BDkGfls8EV7c30MzCvLipBPbXsJNDJxFfrLnQ0nnPZb1INTNll2iNQYhPPOG5v_OPo3AYtfH1ajR0XfiER7U6&gsessionid=Cg9r0iPw23kJMnNW6M55Ldc5YLg37aE2dsUR9gUBvBaaZDG_4QqfOQ)  
  <sub>Quiver Quantitative, 46 minutes ago</sub>  
  ENVESTNET ASSET MANAGEMENT INC has opened a new $787.3M position in $XOM, per a new SEC 13F filing.
- [ExxonMobil launches $3B debt buyback across four bond series](https://www.google.com/goto?url=CAESnQEBxCJF1_pO70hw7i9tSoH4kghCInQ80A1qRpfcpAEhzrnkyWKA6MLmUa4aXwU2ERVhYhUfqqDxhpVInQStlwUEvTFSyGJGRFE-CZct53i2w_2KksvBRi9B1S6VYgytCktEdZb-tpz2edrHLJEE3gEtb35CRjbH2kyHzKTsv8Ao0OyAqErsaQKoCc06sVFZGlI_rsk13CsXLn3he65C&gsessionid=Cg9r0iPw23kJMnNW6M55Ldc5YLg37aE2dsUR9gUBvBaaZDG_4QqfOQ)  
  <sub>Seeking Alpha, 18 minutes ago</sub>  
  ExxonMobil (XOM) announced on Monday that its wholly owned subsidiaries, Pioneer Natural Resources and Exxon Mobil Corporation, had launched cash tender...
- [XOM Nov 2026 90.000 call (XOM261113C00090000) interactive stock chart](https://www.google.com/goto?url=CAESeAHEIkXXmJ0HXbEh5us0RUNXXsgpYXW_Qsm5vWdnEWh3rcXBT8lvA8AAXaTt7bMgeSPi2mThZ9egpeybWbs2nNk73XavnwGzTMWk_3254Pr8WhS7JDd2j2ZjpflBsGJDdNBkuDCuoMHMk4uQQLTJzqKM8caHe-1W7Q&gsessionid=Cg9r0iPw23kJMnNW6M55Ldc5YLg37aE2dsUR9gUBvBaaZDG_4QqfOQ)  
  <sub>Yahoo Finance UK, 9 hours ago</sub>  
  Interactive chart for XOM Nov 2026 90.000 call (XOM261113C00090000) – analyse all of the data with a huge range of indicators.
- [ExxonMobil Stock Breaks $163.80 as Oil Shock and LNG Growth Put $168.60 in Focus](https://www.google.com/goto?url=CAESrwEBxCJF11von7NO6Jf6h2IapST8QF-cYpBdmo5alT3nWiEwVS8bYlzXGJ_Asfos_gAIFxTwTl1P4FNTjFLCBLT8EZZ5qCCUt0oHQcmbWrXjECIaMf9Q9DQuolZA1XXm4clORrFcuqN1E5v15yJDcus2WV39W6flv2PWVN8EB1v2D8AMTPZiJ4j9BWtM0f-RF_39tKxGZf18fHqIJsInJ36X3xLg-nZeQPyvGey-EOxo&gsessionid=Cg9r0iPw23kJMnNW6M55Ldc5YLg37aE2dsUR9gUBvBaaZDG_4QqfOQ)  
  <sub>TradingKey, 16 hours ago</sub>  
  TradingKey - XOM closed at $165.99 as Brent jumps back near $107 and LNG growth strengthens the bull case. Can $168.60 unlock $170.95-$173.09?
- [ProVise Management Group LLC Makes New $27.28 Million Investment in ExxonMobil Corporation $XOM](https://www.google.com/goto?url=CAES1gEBxCJF1-HGEhTK2cLlwjssqVq30K3nziHtDVxZwLpj6b-jZ16zj0Sygzb98S5zNI9dXVeLAEBG9shpqH49CZngfv5n1LJdBSbiFPh4tY5Qzdbfmoes0LwP7mYml4Lzi4NiV87PSON9cu7jSXNXuQq416AWfta-agqFJm6k1BK5nZzfl37ed2ipa0c5E_QTe7ewVoubz0fNMVYXQ3wXTxoGMmfVfIT2maO2HlLMHNUkNXN19kYWR4xk3Ohr_rECOAViYfOBruGtMF9i6XzWdNVhC4lU3Rn-&gsessionid=Cg9r0iPw23kJMnNW6M55Ldc5YLg37aE2dsUR9gUBvBaaZDG_4QqfOQ)  
  <sub>MarketBeat, 1 hour ago</sub>  
  ProVise Management Group LLC bought a new stake in ExxonMobil Corporation (NYSE:XOM - Free Report) during the 3rd quarter, according to the company in its...
- [Exxon Mobil Earnings Call Highlights Growth and Resilience](https://www.google.com/goto?url=CAESywEBxCJF15VlMM3_JIBo0Bypx48jBU5YzvFszsHqKcblpUHZwTChOlSK9U0O-5RMNwtxHWQuf3t0VCDlt4CkYMlv6hc4AhAX5ge6ncgE76os_fhCaZoYZoeenSU9yb1m7brayWQ0KIyqXnJu6Ceeoan3yJtR9TnUlqfAtoi13SsQwiH3vaDfF7p14v0o04TgBWeheK3mLKSEBoxGWapAmx_tMMQ5I4OoL6EFHo35sRLTZnVd9MESKD28onAnjd0wToeuubLs8v1WxbWXTA&gsessionid=Cg9r0iPw23kJMnNW6M55Ldc5YLg37aE2dsUR9gUBvBaaZDG_4QqfOQ)  
  <sub>The Globe and Mail, 14 hours ago</sub>  
  Detailed price information for Exxonmobil Holdings Corp (XOM-N) from The Globe and Mail including charting and trades.
- [Precision Trading with Yieldmax Xom Option Income Strategy Etf (XOMO) Risk Zones](https://www.google.com/goto?url=CAES2wEBxCJF1wUOTqi0MU36wY97MVdgNI6f9yJ9UaUKDhCZUeFaWRL9T-UCuL0FZD9Vft_vUNDpe_Zu9FVW9m7bV6EveeOFlKcpHMuck7z_3AaBQfEMZix0f5aEpjfDIls0u6Lz8fbmG4Fi3QT1TUuBriseLVgwuqk_5pup1IbxKklBX0rlP-91B0-ORy68aPwSG9ZtEeZ9D17PDiJHtpA3NS9ty7KosEfQK-MJgW-qycuWEFnGsmHMEbMj84GkHhZWz6itLvNzKJgafYp_gjhGnFItawdAoXMnqFnIdMs&gsessionid=Cg9r0iPw23kJMnNW6M55Ldc5YLg37aE2dsUR9gUBvBaaZDG_4QqfOQ)  
  <sub>Stock Traders Daily, 10 hours ago</sub>  
  Key findings for Yieldmax Xom Option Income Strategy Etf (NASDAQ: XOMO). Positive Near-Term Sentiment May Erode Mid-Term Weak Bias Within Long-Term Strength...
- [What ExxonMobil Doubters Got Wrong](https://www.google.com/goto?url=CAESqQEBxCJF12W6v9w-p0UiZ18wuD1-GYdh9aZbZCqYdM7o4gsTtAMLUQ2n2bFJGaaVMagmIde4TcykiyBxx8-GBTqAd1M2NgMOthNmAcrk-pfNzLbztESdDCt_N9-LiPyAAhskkBPCLJLb5c8_mPRkr_jFfcmRj0LXCL8wqTiMRKXWwkpuwi3L5RdPFlAfOGNR79FSQ_9jlGeDbNeJojvqntt57t9KZMDeIg9g&gsessionid=Cg9r0iPw23kJMnNW6M55Ldc5YLg37aE2dsUR9gUBvBaaZDG_4QqfOQ)  
  <sub>Simply Wall St, 15 hours ago</sub>  
  The freshest headline for ExxonMobil is not about a megamerger or a lawsuit. It is a green light on a concrete project, a US$12.5b commitment to the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 168.51 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 174.84 (-3.6%), 50d 169.56 (-0.6%), 200d 156.50 (+7.7%); 50d above 200d
Momentum: RSI(14) 45.2 | MACD -1.087 vs signal 0.178 (histogram -1.265)
Returns: 1d -1.2% | 5d +2.3% | 1m -5.8% | 3m +1.8%
52-week range: 114.51 - 187.25 (now 74.2% of the way up)
Volatility: ATR(14) 4.24 (2.5% of price) | annualised 20d 30.9%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.70</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 687.39B
Valuation: trailing P/E 17.34 | forward P/E 13.33 | P/B 2.59 | PEG 1.34
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
Price target: mean 184.18 (+9.3% vs last close), range 160.00 - 213.00
Recent rating changes:
  - 2026-11-12 Bernstein: main, Outperform -> Outperform
  - 2026-11-07 Freedom Broker: main, Hold -> Hold
  - 2026-11-04 Citigroup: main, Neutral -> Neutral
  - 2026-11-04 TD Cowen: main, Buy -> Buy
  - 2026-11-02 UBS: main, Buy -> Buy
  - 2026-11-02 Morgan Stanley: main, Overweight -> Overweight
Institutional ownership: 67.4%
Largest holders: Blackrock Inc. (8.1%), Vanguard Capital Management LLC (6.6%), State Street Corporation (5.2%), FMR, LLC (3.6%), Vanguard Portfolio Management LLC (2.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.80</summary>

```text
Last 180 days: bought 10,818,651 shares in 251 transaction(s) | sold 3,904,152 shares in 49
Net: +6,914,499 shares (+369.3% of insider holdings) | insiders hold 8,770,329 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.80</summary>

_Not available today._

</details>

### ASML (ASML) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the gross exposure limit

**In the model's own words:**

> Buyback transaction provides a positive catalyst, fundamentals are strong, analysts are overwhelmingly bullish, earnings record shows consistent beats, but technicals are currently bearish with price below SMAs and low volume, tempering conviction.

**Main reasons it gave:**
- Share buyback transaction reported (positive catalyst)
- Strong fundamentals: high margins, 55% YoY revenue growth, low debt/equity
- Analyst consensus strong buy with 46.8% upside price target
- Technical weakness: price below 20d/50d/200d SMAs, RSI 38.2, low volume
- Earnings record: 3 beats out of last 4 quarters

<details><summary><b>News</b> — score +0.40</summary>

- [ASML reports transactions under its current share buyback program](https://finance.yahoo.com/markets/stocks/articles/asml-reports-transactions-under-current-130000950.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>
- [Prediction: Berkshire Hathaway Could Use Its $377.4 Billion of Cash to Buy This Monopoly Artificial Intelligence (AI) Stock Next](https://www.fool.com/investing/2026/11/16/berkshire-hathaway-is-sitting-on-usd377-4-billion-of-cash-here-s-the-artificial-intelligence-ai-stock-greg-abel-could-buy-next/)  
  <sub>The Motley Fool, 5 hours ago</sub>  
  Over the last year, Berkshire Hathaway (BRKA +0.47%)(BRKB +0.53%) has become a surprising participant in the artificial intelligence (AI) revolution.
- [ASML Dec 2026 1360.000 call (ASML261218C01360000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESdAHEIkXXWlRUZ6LYKzEoywGsos7c8COnMzNdDxDb-GkjGgbLKDZ6H9NCYyLdmtgRoMyb71MyaR9oWN4h_10OBaZo8ygPqY-ldpvsh0GNgDXbyOcBoqRM-Ggd0SfR-gV9GZ7Gr4Eb6MEFqYdw92xSTTSTanuM&gsessionid=d__3znvSMl4ynSS6uoYH82KLxtWDmeZyXOqzABwpUMf3TcVhd_QOPA)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>
- [How to buy ASML Holding N.V. - New York Registry Shares (ASML) in United States](https://www.google.com/goto?url=CAESqAEBxCJF1wf2rLjlj8_bHJzL28Gw0o7YqArLHibQ95FxOC3BHv_l_GH2U73VZqUoByA1d401aB0PKoIjgwoqe7OUCQ0ZJM2u9OZsykZvZb_HZzOgd_bhighBurj9hEvU0r8jGdjDnt_svIbYgsgRYpP1JCp3_eiQFvIP2SAk6x_jjSjuFqQLTySoQmpT2nrV7PnLB77GERX4PAZBFTFSIvYlBwxPNYcCyQM&gsessionid=d__3znvSMl4ynSS6uoYH82KLxtWDmeZyXOqzABwpUMf3TcVhd_QOPA)  
  <sub>OKX, 8 hours ago</sub>  
  OKX Europe - Discover how to buy ASML Holding N.V. - New York Registry Shares (ASML) in United States easily on a centralized crypto exchange, peer-to-peer...
- [ASML Jun 2028 1020.000 put (ASML280616P01020000) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESdAHEIkXXG4TxDWfOmUdDkGYn0C9xkYVocFTymssXXvcbjzvyLV1RZ6K0zwjEpcxVVhloOHYngmUnBurvxtbHEsjT0tXR62cMS5suqdA-LbCLJbhz8uQ-75tSPclKllFk5W-jY0e7Rdsq32EEmX1FKWh7wuSn&gsessionid=d__3znvSMl4ynSS6uoYH82KLxtWDmeZyXOqzABwpUMf3TcVhd_QOPA)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>
- [ASML Jan 2027 1550.000 put (ASML270115P01550000) stock price, news, quote and history](https://www.google.com/goto?url=CAESdAHEIkXXQzslgZnKfzkIgc-FEqsWGOOItpyc0Zo2DDbnpfgubW8C-L952JK_FQTgXrDj08H7Qv1Cb1NvbOUbRa8wfker6KKwoiJksdUwXEP5f_h_tprLa-uO4eLlOARu7OUZSll90ZB816vq4OOngu0vQGJE&gsessionid=d__3znvSMl4ynSS6uoYH82KLxtWDmeZyXOqzABwpUMf3TcVhd_QOPA)  
  <sub>Yahoo Finance Australia, 13 hours ago</sub>
- [ASML Nov 2026 1730.000 put (ASML261113P01730000) interactive stock chart](https://www.google.com/goto?url=CAESegHEIkXX-jPeUZuHAw067BvippNeaN0jKOwvDDUgNh36SCQXfQ0t99e8RKeTo2n_nxFBcfi94Jtz3rBpaTV_fyrF9L-GEcj2U8pmjzu1TDjYnJgKNRsBg0GxlDm2ZK5DlqNXCuFabUgyEhTEyFFZ3mGKOCuubZk8klLK&gsessionid=d__3znvSMl4ynSS6uoYH82KLxtWDmeZyXOqzABwpUMf3TcVhd_QOPA)  
  <sub>Yahoo Finance Australia, 18 hours ago</sub>
- [Check In 15 - Beyond Chip Designers, ASML & TSMC](https://www.google.com/goto?url=CAESngEBxCJF16npgYvDpSaEn9IRQhVJxx1RrbRt8R4z6MoGuGfI5Ot7Kj1e4_BknJ1laqJcZmsBvYwkX6sNw1dnZDMNxBPphFJxZ6wq-B7wfA_a7mYtPARAYN8IfZubiJ94AEdja921juESM2ftTZ0_tvRvfyLoyHoIRJM5_bfuzR-c6Qix1LfTQRfPlKVhxem_hPSltmvwdJHCmPO1H7tsKw&gsessionid=d__3znvSMl4ynSS6uoYH82KLxtWDmeZyXOqzABwpUMf3TcVhd_QOPA)  
  <sub>Moomoo, 6 hours ago</sub>  
  Chip designers have been making quite a number of headlines recently, but people rarely talk about the irreplaceable tollbooths at the very bottom of ...
- [ASML Jan 2028 2360.000 call (ASML280121C02360000) interactive stock chart](https://www.google.com/goto?url=CAESegHEIkXXHuB3EXOHn6cs3UOTvW8WtM3p1qZdQD4bq-gil_YSyW7UWq7jVJcy7ubf_m-Lg9lylhOcZaVJmFaF2Fg62pumVFqZlFVyFxVPB5Zrnoep_5ppU1t-jm8YgySkZKfvxa4pO7pYo-vEDKIMrw-yReQqWu4BAUIi&gsessionid=d__3znvSMl4ynSS6uoYH82KLxtWDmeZyXOqzABwpUMf3TcVhd_QOPA)  
  <sub>Yahoo Finance UK, 22 hours ago</sub>
- [Nvidia shares plummeted amid a sell-off in AI companies](https://www.google.com/goto?url=CAESgQEBxCJF17vMmfig_V5EjyHE3FXKdx1zJv6iRWg6k-sUbXf9T7BLJtOFlmvLXHOGks2K_yI6N0Vchgzouhy8Gj-lh_GsNzAr5rp9KNR1Gm4nyMhzgAZhtgZLl9qvCCKBh4BsOFWty1QLcEqF_b3TRzWKxWEbEk3tRAxXsbHipSefTRI&gsessionid=d__3znvSMl4ynSS6uoYH82KLxtWDmeZyXOqzABwpUMf3TcVhd_QOPA)  
  <sub>UkrMedia News, 1 hour ago</sub>  
  Global stock markets came under pressure on 16 November due to a fresh wave of sell-offs in technology shares. The resignation of Nvidia founder Jensen...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 1,439.28 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 1,545.69 (-6.9%), 50d 1,654.98 (-13.0%), 200d 1,602.30 (-10.2%); 50d above 200d
Momentum: RSI(14) 38.2 | MACD -57.857 vs signal -56.087 (histogram -1.771)
Returns: 1d -3.7% | 5d -4.9% | 1m -12.3% | 3m -20.2%
52-week range: 966.57 - 1,989.44 (now 46.2% of the way up)
Volatility: ATR(14) 65.51 (4.6% of price) | annualised 20d 63.3%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.80</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 554.72B
Valuation: trailing P/E 35.42 | forward P/E 22.70 | P/B 1,235.84 | PEG 0.79
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: strong_buy (mean 1.37 on a 1=strong buy to 5=strong sell scale, 17 analysts)
Ratings: 7 strong buy, 31 buy, 2 hold, 1 sell, 0 strong sell
Price target: mean 2,112.30 (+46.8% vs last close), range 852.03 - 2,798.86
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 12,131,500 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Eli Lilly (LLY) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the gross exposure limit

**In the model's own words:**

> Positive obesity pipeline news combined with strong fundamentals and a record of earnings beats outweighs technical overbought signals and neutral insider activity.

**Main reasons it gave:**
- ObesityWeek 2026: new clinical data on Zepbound, Foundayo, EloraTZP, retatrutide
- Teen obesity trial shows substantial weight reductions for Zepbound
- Strong fundamentals: profit margin 31.9%, ROE 86%, revenue growth 38.6% YoY
- Four consecutive earnings beats (12%–38% beats) in last four quarters
- Technical: RSI 71.3 (overbought) and volume 0.10x 20‑day average suggests caution

<details><summary><b>News</b> — score +0.60</summary>

- [Eli Lilly and Company (LLY) is Attracting Investor Attention: Here is What You Should Know](https://finance.yahoo.com/markets/stocks/articles/eli-lilly-company-lly-attracting-130005731.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Lilly (LLY) has been one of the stocks most watched by Zacks.com users lately. So, it is worth exploring what lies ahead for the stock.
- [What Does Eli Lilly (LLY) Reveal At ObesityWeek 2026 About Its Growth Path?](https://ca.finance.yahoo.com/news/does-eli-lilly-lly-reveal-111339437.html)  
  <sub>Yahoo! Finance Canada, 3 hours ago</sub>  
  Eli Lilly (NYSE:LLY) released new clinical data at ObesityWeek 2026 on Zepbound, Foundayo, EloraTZP, and retatrutide. The update included late-stage obesity...
- [LLY Nov 2026 1365.000 call (LLY261120C01365000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXVcU4jNbPJmKK8GUcrikGlVFL83AKNZ_C2f4j_l1ddfc7pxi4meSL7YtnTvgZwIbxaxKwLSXTkJFKE088eqXCAv6OKjEMzOxrZw-aHym5xmJ3nA1CdAFQ6JZTi6wRGCMRGiXRs8cSXnxxR2hFLWs&gsessionid=MYul3v7LwVzNf2cbHwWw2W9a4rj-dPhqT58T98qUF9PaP0U-SGzBMQ)  
  <sub>Yahoo Finance UK, 3 hours ago</sub>  
  Find the latest LLY Nov 2026 1365.000 call (LLY261120C01365000) stock quote, history, news and other vital information to help you with your stock trading...
- [LLY Jan 2028 740.000 put (LLY280121P00740000) Seasonal Returns Chart - Yahoo Finance](https://www.google.com/goto?url=CAESfwHEIkXXgU09wzOxBcwtLfMB6ayxcdaz6LlEak5t_NnMY4dfO4uziQmwnP4IU9An_UB2tXjILwCPR4AzSqGO3fGCMPk0xMo9u1JeKYwpi48QDm30bjlW1K8G15eOqWM9Qb_LrdoamsJkglpJFtsyP7ZOgSWAVAp7Outy0_RKrus&gsessionid=MYul3v7LwVzNf2cbHwWw2W9a4rj-dPhqT58T98qUF9PaP0U-SGzBMQ)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  LLY Jan 2028 740.000 put (LLY280121P00740000) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [LLY Nov 2026 1430.000 call (LLY261120C01430000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXqeNObeB1yuuMvgh2PmaxDcEdPGIq8jYIEbgP14466xv5xEIJTiw7NtEREahcpLfpQm8ZEl22g5TOgs5z3O23Q3fDFzAgzf_1IZ5hgb5KP3xQV8GGoI5HmbFSt0fx5GFxPHKPA-8rhWGXyi1_5xw&gsessionid=MYul3v7LwVzNf2cbHwWw2W9a4rj-dPhqT58T98qUF9PaP0U-SGzBMQ)  
  <sub>Yahoo Finance Australia, 11 hours ago</sub>  
  Find the latest LLY Nov 2026 1430.000 call (LLY261120C01430000) stock quote, history, news and other vital information to help you with your stock trading...
- [LLY Nov 2026 1230.000 put (LLY261127P01230000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXiL0mFA2oWLHGP6MtcwXVrHBkqpyraUfn1FfMkLqH1v73p1pryQC-iUgx7o9WoXGISKutXb6iHITnCEp90b0A0Y7N8IwV0ZxdkramP6n1OO3vCbQYWofUzM8iLPohTZyUIJXdrby8fg8iXccmNVI&gsessionid=MYul3v7LwVzNf2cbHwWw2W9a4rj-dPhqT58T98qUF9PaP0U-SGzBMQ)  
  <sub>Yahoo Finance UK, 15 hours ago</sub>  
  Find the latest LLY Nov 2026 1230.000 put (LLY261127P01230000) stock quote, history, news and other vital information to help you with your stock trading...
- [About Eli Lilly & Co Tokenized Stock (Coinbase)](https://www.google.com/goto?url=CAESnwEBxCJF1_3VA6JTmaN19TZqxVK4btv7UaQRM9uH_Oifj8LAGeCo8lDUfEW5C51n5udjbqiUUFCOb75ZAsW9yD4aisZgOGiiv77eYBruGxupsbbaieS9ezk6v8ADM4cxwotBqsh7QltyDTdcXtEAQZ9CDc3cohUI_dl3N7vrKCS_lPrs3nMmiUPdf2w_LsqCML8qhsvHqOw8JMYr8CIBULo&gsessionid=MYul3v7LwVzNf2cbHwWw2W9a4rj-dPhqT58T98qUF9PaP0U-SGzBMQ)  
  <sub>Coinbase, 5 hours ago</sub>  
  Eli Lilly & Co Tokenized Stock (Coinbase) (LLYC) Price ARS Today is ARS 2247335.10. News, predictions, charts, market cap, buy, sell, convert, and invest on...
- [LLY Nov 2026 1205.000 put (LLY261113P01205000) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXwwM3CgWOgSW4aayc25kpGt24JySJcaoQ9ao62QkVfSS4HePudi5oXXOk1RqUNEutDqVwubaS3aQXGMO7HvpsBcHYc28ariLZJnzaoLFmh2Y9U1YxP-lJnR4H99OahvDVRjH-3Gk4a1FgMuFBvLKQfeHPh5A&gsessionid=MYul3v7LwVzNf2cbHwWw2W9a4rj-dPhqT58T98qUF9PaP0U-SGzBMQ)  
  <sub>Yahoo Finance UK, 17 hours ago</sub>  
  Interactive chart for LLY Nov 2026 1205.000 put (LLY261113P01205000) – analyse all of the data with a huge range of indicators.
- [Lilly’s Zepbound shows promise in teen obesity trial (LLY:NYSE)](https://www.google.com/goto?url=CAESlwEBxCJF1yHYqJigKWiZpOl4PB5P2s2VNpTGJM54sk102o7E3eC6QgYV-Uf3trjwPhU9xjCvcezDiwnOjbHtaSuFYQdoVSgJVIuIHUTV0VG-iiYIPPt1HArA_CzcMhvO3wstFtX5bwWpxYW4nIGlLr1B8TscOmlfE7cMtbug6S6oKIWl-DVfFDBV5uCVDNDsTuJEfyXXAkdy&gsessionid=MYul3v7LwVzNf2cbHwWw2W9a4rj-dPhqT58T98qUF9PaP0U-SGzBMQ)  
  <sub>Seeking Alpha, 15 hours ago</sub>  
  Eli Lilly's (LLY) Zepbound helped adolescents with obesity or excess weight and related health conditions achieve substantial weight reductions in a new...
- [GMED,CWK,LLY,COLD,MDT,ULS,PFE | Stock Prices | Quote Comparison - Yahoo Finance](https://www.google.com/goto?url=CAESfwHEIkXXxv05LylcJYjjiSrwS_wsat6e2KdME19W-pzyTW7aHuPwDezII1PtDcKiblQ8ZTthprrpQ-wriDbjE_Ir8JM6msRLnkUyY1yK92EAcGQsmNMozpcG269rDOmctDZdpegWrjLskUFWSkhpMKv444ZGTDpNfwy23OYNrHM&gsessionid=MYul3v7LwVzNf2cbHwWw2W9a4rj-dPhqT58T98qUF9PaP0U-SGzBMQ)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  View and compare GMED,CWK,LLY,COLD,MDT,ULS,PFE on Yahoo Finance.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 1,458.62 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 1,367.16 (+6.7%), 50d 1,247.26 (+16.9%), 200d 1,111.43 (+31.2%); 50d above 200d
Momentum: RSI(14) 71.3 | MACD 57.947 vs signal 54.559 (histogram 3.388)
Returns: 1d +1.0% | 5d +3.3% | 1m +16.0% | 3m +19.0%
52-week range: 851.21 - 1,458.62 (now 100.0% of the way up)
Volatility: ATR(14) 43.42 (3.0% of price) | annualised 20d 37.7%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.30T
Valuation: trailing P/E 47.34 | forward P/E 28.71 | P/B 32.28 | PEG 1.33
Profitability: profit margin 31.9% | operating margin 51.3% | ROE 86.0%
Growth (YoY): revenue +38.6% | earnings +16.3%
Balance sheet: debt/equity 122.9% | free cash flow 9.34B
Risk: beta 0.39 | short interest 0.8% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.50</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-09-30 beat by 18% | 2026-06-30 beat by 38% | 2026-03-31 beat by 27% | 2025-12-31 beat by 12%
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
Consensus: buy (mean 1.65 on a 1=strong buy to 5=strong sell scale, 29 analysts)
Ratings: 5 strong buy, 20 buy, 4 hold, 1 sell, 1 strong sell
Price target: mean 1,463.40 (+0.3% vs last close), range 940.00 - 1,700.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 38,018 shares in 36 transaction(s) | sold 313,215 shares in 9
Net: -275,197 shares (-9.8% of insider holdings) | insiders hold 2,529,716 shares
Distinct insiders: 0 buying, 4 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-11-02 HAKIM ANAT (General Counsel): 5,000 shares, 7.01M
  - 2026-08-17 JONSSON PATRIK (Officer): 6,500 shares, 7.64M
  - 2026-08-10 ZAKROWSKI DONALD A (Officer): 2,000 shares, 2.37M
  - 2026-08-07 HAKIM ANAT (General Counsel): 5,000 shares, 5.95M
(32 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Caterpillar (CAT) · Company — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 429: {"error":{"message":"Model busy, retry later","type":"invalid_request_error","param":null,"code":"engine_overloaded"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Is Trending Stock Caterpillar Inc. (CAT) a Buy Now?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afb166910cd46d1a7bae2a1fe2bc148&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2ftrending-stock-caterpillar-inc-cat-130004520.html&c=14219233623988463901&mkt=en-us)  
  <sub>Yahoo Finance, 10h ago</sub>  
  Zacks.com users have recently been watching Caterpillar (CAT) quite a bit. Thus, it is worth knowing the facts that could determine the stock's prospects.
- [A Key Power Supplier to AI Data Centres Has Record Orders. Its Stock Is Down 44%](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afb166910cd46d1a7bae2a1fe2bc148&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2fkey-power-supplier-ai-data-032819810.html&c=16685345841947893419&mkt=en-us)  
  <sub>Yahoo Finance, 19h ago</sub>  
  Caterpillar stock is down 44% since June, even as data center demand pushed its order backlog to a record $78 billion.
- [I've owned this stock for a decade. AI slowdown fears gave me an opportunity to buy more](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afb166910cd46d1a7bae2a1fe2bc148&url=https%3a%2f%2fwww.cnbc.com%2f2026%2f11%2f15%2fcaterpillar-buy-kevin-simpson.html&c=6885071749528019500&mkt=en-us)  
  <sub>CNBC, 24h ago</sub>  
  Caterpillar is an established business with exposure to the infrastructure needed to power AI and the broader economy.
- [eBay, Amazon, Caterpillar and more on CNBC’s ‘Final Trades’](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afb166910cd46d1a7bae2a1fe2bc148&url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2febay-amazon-caterpillar-and-more-on-cnbc-s-final-trades%2far-AA2hxnvL&c=2178423439556148879&mkt=en-us)  
  <sub>Benzinga on MSN, 10h ago</sub>  
  On CNBC’s “Halftime Report Final Trades,” Jim Lebenthal, partner and chief market strategist at Cerity Partners, said eBay Inc. (NASDAQ:EBAY) has great fundamentals. Lending support to his choice, ...
- [Caterpillar seen as buy on AI infrastructure exposure after share decline](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afb166910cd46d1a7bae2a1fe2bc148&url=https%3a%2f%2ftradersunion.com%2fnews%2fstocks%2fshow%2f4259663-caterpillar-buy-ai-infrastructure-shares%2f&c=13394735181269333846&mkt=en-us)  
  <sub>tradersunion, 23h ago</sub>  
  Caterpillar is seen as a buy after its share decline, with strong AI infrastructure exposure, robust cash flow, and growth in dividends supporting its outlook.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 590.81 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 638.40 (-7.5%), 50d 736.31 (-19.8%), 200d 807.10 (-26.8%); 50d below 200d
Momentum: RSI(14) 34.0 | MACD -45.780 vs signal -48.216 (histogram 2.436)
Returns: 1d -1.6% | 5d -1.3% | 1m -19.2% | 3m -29.7%
52-week range: 546.13 - 1,064.90 (now 8.6% of the way up)
Volatility: ATR(14) 28.28 (4.8% of price) | annualised 20d 59.7%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 270.33B
Valuation: trailing P/E 23.19 | forward P/E 18.36 | P/B 12.58 | PEG 1.05
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
Price target: mean 807.26 (+36.6% vs last close), range 575.00 - 1,027.00
Recent rating changes:
  - 2026-11-10 Evercore ISI Group: main, Outperform -> Outperform
  - 2026-11-02 Freedom Broker: main, Buy -> Buy
  - 2026-11-02 DA Davidson: main, Neutral -> Neutral
  - 2026-10-30 JP Morgan: main, Overweight -> Overweight
  - 2026-10-30 Citigroup: main, Buy -> Buy
  - 2026-10-30 Wells Fargo: main, Overweight -> Overweight
Institutional ownership: 74.0%
Largest holders: Blackrock Inc. (8.2%), State Street Corporation (7.5%), Vanguard Capital Management LLC (6.6%), State Farm Mutual Automobile Insurance Co (3.1%), Vanguard Portfolio Management LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 47,091 shares in 10 transaction(s) | sold 32,401 shares in 1
Net: +14,690 shares (+0.8% of insider holdings) | insiders hold 1,917,319 shares
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

<details><summary><b>News</b> — score n/a</summary>

- [Weekly Recap: PULS contract win and third-quarter 2026 earnings estimates](https://www.tradingview.com/news/tradingview:c2478efcf57de:0-weekly-recap-puls-contract-win-and-third-quarter-2026-earnings-estimates/)  
  <sub>TradingView, 4 hours ago</sub>  
  Elbit Systems Ltd (NASDAQ:ESLT) won a five-year contract worth roughly $260 million to supply PULS rocket artillery systems and munitions to an undisclosed...
- [ESLT Nov 2026 590.000 put (ESLT261120P00590000) interactive stock chart](https://uk.finance.yahoo.com/quote/ESLT261120P00590000/chart/)  
  <sub>Yahoo Finance UK, 24 hours ago</sub>  
  Interactive chart for ESLT Nov 2026 590.000 put (ESLT261120P00590000) – analyse all of the data with a huge range of indicators.
- [Buy 4 Drone Technology Bigwigs to Enhance Your Portfolio Returns](https://www.google.com/goto?url=CAESpgEBxCJF1-7nkdMKeSB5YGQtCeHVQgjmp-1XaFWd9sk9mb2PPTYIaFAqxU6zVqCwHw9oH3Ryz0eaF-qxbCrEAnhXAaTR0ap5vqPGsdfPXqFqkbw-z_Mh1Sqzh4Nvc8vXag-YcGewSBaXcCge_fxgfLq2bSHjFZqIi163qJ9xTMGJtWj-k2PWHdCs2bLu3F4jiXpXcgxP9y-dvEm38tUk6ZW3eKvwdJT4&gsessionid=8_TxovjmUyuAa9IeXNEii296FiMyzT3hymPNmOC9icdxJU43-q8XoA)  
  <sub>Zacks Investment Research, 39 minutes ago</sub>  
  ESLT supplies advanced night-vision and defense technologies for military aircraft and platforms worldwide. CW benefits from rising nuclear, naval defense...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 689.46 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 737.15 (-6.5%), 50d 723.37 (-4.7%), 200d 785.25 (-12.2%); 50d below 200d
Momentum: RSI(14) 43.4 | MACD -6.184 vs signal -0.934 (histogram -5.250)
Returns: 1d -2.4% | 5d -4.5% | 1m -8.7% | 3m -13.4%
52-week range: 454.95 - 1,014.33 (now 41.9% of the way up)
Volatility: ATR(14) 27.21 (3.9% of price) | annualised 20d 60.2%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 32.32B
Valuation: trailing P/E 51.88 | forward P/E 37.04 | P/B 7.31 | PEG n/a
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
Price target: mean 838.92 (+21.7% vs last close), range 738.50 - 960.00
Recent rating changes:
  - 2026-10-05 Jefferies: main, Hold -> Hold
  - 2026-08-19 JP Morgan: main, Neutral -> Neutral
  - 2026-06-24 Jefferies: main, Hold -> Hold
  - 2026-05-27 Jefferies: main, Hold -> Hold
  - 2026-05-27 JP Morgan: main, Neutral -> Neutral
  - 2026-04-13 JP Morgan: main, Neutral -> Neutral
Institutional ownership: 26.5%
Largest holders: Clal Insurance Enterprises Holdings Ltd (3.5%), Vanguard Capital Management LLC (1.6%), Van Eck Associates Corporation (1.2%), Y.D. More Investments Ltd (1.1%), Altshuler Shaham Ltd (1.1%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 19,401,344 shares
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

- [More pain for NVDA? Top supply chain analyst says new OpenAI, Anthropic chip orders boost Google’s TPU outlook](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afb161c4ed54937a38fe883737e46ab&url=https%3a%2f%2fwww.msn.com%2fen-in%2fmoney%2fgeneral%2fmore-pain-for-nvda-top-supply-chain-analyst-says-new-openai-anthropic-chip-orders-boost-google-s-tpu-outlook%2far-AA2hvLXX&c=6510443847331823541&mkt=en-us)  
  <sub>Asianet Newsable on MSN, 17h ago</sub>  
  The orders extend Google TPU shipment visibility to 2029, while Nvidia GPUs and other AI accelerators mostly have visibility through 2027 or 2028, according to Ming-Chi Kuo.
- [Google launches 4 AI semiconductor 'TPU' systems in one year: Cloud revenue up 103%, inventory up 5.5x](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afb161c4ed54937a38fe883737e46ab&url=https%3a%2f%2fnote.com%2fcalm_finch1102%2fn%2fna92f4fbf95f6%3fhl%3den&c=2808099930321050414&mkt=en-us)  
  <sub>note, 22h ago</sub>  
  Google announced new systems for its AI semiconductor, the 'TPU (Tensor Processing Unit)'. These are the 'TPU 8tx' and 'TPU 8i Max', both of which are reconfigured from existing chips. Combined with ...
- [郭明錤：谷歌(GOOGL.US)TPU订单能见度已看至2029年 OpenAI、Anthropic合计需求达2600万颗](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afb161c4ed54937a38fe883737e46ab&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fhkstock%2fggscyd%2f2026-11-16%2fdoc-iniywwzi2509318.shtml&c=15311621465812496772&mkt=en-us)  
  <sub>新浪财经, 23h ago</sub>  
  天风国际证券知名分析师郭明錤周一发文称，受益于OpenAI及Anthropic强劲的新订单，谷歌(GOOGL.US)TPU芯片出货能见度已延伸至2029年，明显优于英伟达(NVDA.US)GPU及其他AI芯片供应商。在AI算力需求持续增长、英伟达管理层接班问题存在不确定性的背景下，谷歌TPU正加速拓展外部客户，AI芯片市场竞争格局或迎来新的变化。 郭明錤在社交平台上表示，根据其最新产业调查，Ope ...
- [【机构持仓】先锋领航资本管理增持谷歌A类股](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afb161c4ed54937a38fe883737e46ab&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fusstock%2fnotice%2f2026-11-16%2fdoc-iniyxiri2793550.shtml&c=14715260466142640675&mkt=en-us)  
  <sub>新浪财经, 23h ago</sub>  
  最新披露的机构持仓数据显示，先锋领航资本管理于最新季度调整了对谷歌A类股（GOOGL）的持仓。 主要变动如下： 持仓变化：增持187.74万股 仓位变化幅度：0.49% 最新持股：3.85亿股 占公司流通股比例：6.54% 截至目前，公司共有8076家机构持股。 其中： 前20大机构合计持股22.19亿股，占总股本37.69%。 较上一季度提升1.41个百分点，机构持仓集中度呈现提升趋势。 声明： ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 288.43 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 300.63 (-4.1%), 50d 327.19 (-11.8%), 200d 338.23 (-14.7%); 50d below 200d
Momentum: RSI(14) 36.6 | MACD -11.919 vs signal -13.239 (histogram 1.320)
Returns: 1d -2.5% | 5d +0.1% | 1m -15.3% | 3m -16.2%
52-week range: 273.50 - 402.62 (now 11.6% of the way up)
Volatility: ATR(14) 10.13 (3.5% of price) | annualised 20d 51.5%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 3.55T
Valuation: trailing P/E 15.06 | forward P/E 19.00 | P/B 5.38 | PEG 1.04
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
Price target: mean 400.37 (+38.8% vs last close), range 300.00 - 500.00
Recent rating changes:
  - 2026-11-02 Wells Fargo: main, Overweight -> Overweight
  - 2026-10-30 Citigroup: main, Buy -> Buy
  - 2026-10-30 Wells Fargo: main, Overweight -> Overweight
  - 2026-10-29 Bernstein: main, Market Perform -> Market Perform
  - 2026-10-29 RBC Capital: main, Outperform -> Outperform
  - 2026-10-29 UBS: main, Neutral -> Neutral
Institutional ownership: 80.5%
Largest holders: Blackrock Inc. (7.8%), Vanguard Capital Management LLC (6.5%), FMR, LLC (4.2%), State Street Corporation (4.1%), Geode Capital Management, LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 212,071,488 shares
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

- [HDFC Bank (HDB) gets approval for a one-year executive director term starting November 23, 2026.](https://www.stocktitan.net/sec-filings/HDB/6-k-hdfc-bank-ltd-current-report-foreign-issuer-ba634accb167.html)  
  <sub>3 hours ago</sub>  
  Existing remuneration applies under the Reserve Bank of India's November 12 approval for the executive director's term starting November 23, 2026.
- [Jupiter India I Acc (0P0000U20R.L) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/0P0000U20R.L/)  
  <sub>10 hours ago</sub>  
  Find the latest Jupiter India I Acc (0P0000U20R.L) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [NINE MASTS CAPITAL Ltd Sells 2,011,805 Shares of HDFC Bank Limited $HDB](https://www.google.com/goto?url=CAESvwEBxCJF1wp2kO_kfc2g5UraE4GwH5fsmchP6F1xcCM_TE6raKGqQDk1eL5HJ-GxBXOVMNYV8iBQnyb2FYlhqEyGmXC55Qtry2Kyfvck99YGEVq3-Fyqa91XtaQJRYgwGwG56LxFIYPI7tCuDMIYFTkGCRLwCjGWs0lueRku16wIQ8r-Mu50ttS-OM-Ys9bNfceyYRKxk5YgcayMfOaj-GTFYHthBkE7NCt2Yqh4JNWedsNsn1Q6L9SooeFP4jZ5lg&gsessionid=cK1PpDt9onHUAMwGDk2bepgZeEvog8wg3jVtrq-hnox3C-Phz5iwFQ)  
  <sub>3 hours ago</sub>  
  NINE MASTS CAPITAL Ltd trimmed its position in shares of HDFC Bank Limited (NYSE:HDB - Free Report) by 51.5% during the 3rd quarter, according to its most...
- [HDFC Bank (HDB) approves Rangan’s one-year reappointment, subject to shareholder approval.](https://www.google.com/goto?url=CAESqQEBxCJF1xXk13zxCV7PTy8EGZydHQRrGxOo5pO2ePGYqAlgTBJRDiIOdUsWW7oEegXNcw0BxNG7Bm5p0FX8xdk6jzF4HTd1GUNi4NQh6CJCMm8UJ2sIl5ksCjYe2YfEeUVf7o6VowbYlVKZaKCvRZAK5rBrIvAeaAGSEbSQvi6_hiLYNo2VdLb5RXKSv_fSgd4CB046SoueqcMx8gOtDdR2HJm6gcK9pTrO&gsessionid=cK1PpDt9onHUAMwGDk2bepgZeEvog8wg3jVtrq-hnox3C-Phz5iwFQ)  
  <sub>3 hours ago</sub>  
  HDFC Bank Limited (HDB) said its board approved the reappointment of V. Srinivasa Rangan as a Whole-time Director, designated Executive Director,...
- [HDB Financial Services schedules investor meetings with BofA, ICICI Securities](https://www.google.com/goto?url=CAESswEBxCJF12jgql3rSC4BP-7n30dFJrNePBy8MGitFCb5CrUdY9rETYBVnNI9QI4zqKitsQzKz-DcWb0v4b0A2B9s1HGl2Gqp0YItRWSCOX4LyBsmep9jh8TcQKMZcdITfWh26KatqmYtdINrFZFvmNUVsYiOlSFTX5OUr_mQGUXH-41CwzvSuzQnlFcU2gmbwYleRsv7cT0ixSsGtYBaF2Ty6ppRJJ7HlaXV1MOf5rkTSyvzqA&gsessionid=cK1PpDt9onHUAMwGDk2bepgZeEvog8wg3jVtrq-hnox3C-Phz5iwFQ)  
  <sub>7 hours ago</sub>  
  HDB Financial Services scheduled analyst meetings with BofA Securities and ICICI Securities. Meetings span from November 24, 2026, to December 4, 2026.
- [Stock market this week (November 16-20): Awaiting impetus from interest rates and capital flows.](https://www.google.com/goto?url=CAESogEBxCJF19nu_ajys9zf3OTkIsCW-_pN2o_FJlZvPsXLJPraFtdY6mHIJj394BCHYDZL2PJH3Upyq52ej-8LaI-0pP9Ph02BuLKGgDeKABDOGOHSE2zCeSIxp0Yo_OO36ZSf6kquhtRzbkBekzmF6AgM2IyWNtykJ9ovY8xn8UnSzR9Pvdh_b_ouq7DCCiqyCVoa8blBN6mn2SZVc6VFs3QijBU&gsessionid=cK1PpDt9onHUAMwGDk2bepgZeEvog8wg3jVtrq-hnox3C-Phz5iwFQ)  
  <sub>12 hours ago</sub>  
  (Inspection) - Despite ending a two-week losing streak, the VN-Index's recovery remains fragile due to weak liquidity. During the trading week of November...
- [HDB Financial Services HDBFS Investor Meetings November 2026](https://www.google.com/goto?url=CAESxAEBxCJF1zQvadU-5nCNdDfpf5ShAkcz8L0Y-_C_LJHBJvSzwMP9VaiE4Mis-IkfMWK-07h5fhDTduPQAKGNLd2KNP2k6t3zoBmWNlwkz_-ZMyLUaRvA8S7D7qfdP5g4g8IYMng_3d433lYZKxtSsVXvxHytbUXF2P9TGb2dov6fxkfU41iza_9_1GD9IuJmOP6nnmYhMWrKQfanSteQwdAGTodArpurK4eqVXOfLTloVfYJduX_YFm5QuS3JoXio5ZJwUVT&gsessionid=cK1PpDt9onHUAMwGDk2bepgZeEvog8wg3jVtrq-hnox3C-Phz5iwFQ)  
  <sub>7 hours ago</sub>  
  HDB Financial Services (NSE:HDBFS) disclosed an analyst and institutional investor meeting schedule for late November and early December 2026.
- [Prime Supermarket picks LEAFIO AI for Singapore rollout](https://www.google.com/goto?url=CAESjwEBxCJF17U3e0MpgWG7cX4cfe_BTUpQwsH7Jfsyjl8_wTrA3XPZyIyjL-PsqB1hXGwOY8-nPYIL9Kabt_WjHKrSzoyzDph2VLiviK64YaPWnwI87gNUfx59UGZgPs9yu0bVfmMKL8R5u8yPe67utTShW0d5byBHUIO3uCUHcrbQVfuYkjFnSPdt5r73Ym3Rzg&gsessionid=cK1PpDt9onHUAMwGDk2bepgZeEvog8wg3jVtrq-hnox3C-Phz5iwFQ)  
  <sub>10 hours ago</sub>  
  The rollout will unify replenishment, shelf planning and promotions across 28 stores, reducing manual work for Singapore's largest family-owned grocery...
- [Stock market liquidity has shrunk, with trading volume not exceeding 5,000 billion VND throughout the entire morning session.](https://www.google.com/goto?url=CAESlwEBxCJF1xXjJbSrTkvknX1iwQhuJRQNt58CbH4iFz0ou1d20t3q-O1i5zRK55T0zK2J7YyG-NfykOjerxTQ2lpzd7CrcLCDxUK07raIT5p9Mi4K8lV7apswU00G8YcjHefM0EHbXvAaYuwcfNHdtnAajEDYeHsCBDV34J5tmMawgqldF72AzWaQdGqBreVKWwQ4KjjLyEdI&gsessionid=cK1PpDt9onHUAMwGDk2bepgZeEvog8wg3jVtrq-hnox3C-Phz5iwFQ)  
  <sub>5 hours ago</sub>  
  Stock market liquidity remained low, with the total trading value across all three exchanges on the morning of November 16th not reaching 5000 billion VND,...
- [HDFC Bank Board Approves Proposed One-Year Reappointment of Rangan](https://www.google.com/goto?url=CAESswEBxCJF17yjDluTdX662whDSy8lnv6zLo2M-Ex9Cfmpbl5JhXCGM6Cx_VfRkYrNwgQYGXUa4k9Yo6CWMqbmR8VwbG94Rh-oDjjmZka45_Aq_YJDVKoqSQCyh3d-_oUKBwMmPKj1NDEYAzojSuigHhjRM0k-hCr8G8IOVEmZD_hZ8kExEhTc4FzxW3FeJ-YEB2YcFvUudwW4rKPKfNliL63H38Of9XAOhUzWc3mOXnATGBWALg&gsessionid=cK1PpDt9onHUAMwGDk2bepgZeEvog8wg3jVtrq-hnox3C-Phz5iwFQ)  
  <sub>2 hours ago</sub>  
  Hdfc Bank ( ($HDB) ) has provided an announcement. HDFC Bank is a bank with its principal executive office in Mumbai, India. On November 13, 2026, the board...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 26.18 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 23.72 (+10.4%), 50d 23.11 (+13.3%), 200d 25.41 (+3.0%); 50d below 200d
Momentum: RSI(14) 72.9 | MACD 0.920 vs signal 0.607 (histogram 0.313)
Returns: 1d +1.4% | 5d +1.4% | 1m +9.8% | 3m +13.0%
52-week range: 21.36 - 37.13 (now 30.6% of the way up)
Volatility: ATR(14) 0.58 (2.2% of price) | annualised 20d 29.1%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 134.67B
Valuation: trailing P/E 16.89 | forward P/E 18.90 | P/B 10.42 | PEG n/a
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
Price target: mean 30.30 (+15.7% vs last close), range 26.20 - 33.00
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
Net: +0 shares | insiders hold 6,935,974 shares
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

- [JPMorgan vs. Truist: Which Bank Stock Has More Upside in 2027?](https://www.theglobeandmail.com/investing/markets/stocks/JPM/pressreleases/8854690/jpmorgan-vs-truist-which-bank-stock-has-more-upside-in-2027/)  
  <sub>The Globe and Mail, 34 minutes ago</sub>  
  Detailed price information for JP Morgan Chase & Company (JPM-N) from The Globe and Mail including charting and trades.
- [JPM Dec 2026 110.000 call (JPM261218C00110000) Seasonal returns chart - Yahoo Finance](https://sg.finance.yahoo.com/quote/JPM261218C00110000/seasonality/)  
  <sub>Yahoo Finance Singapore, 8 hours ago</sub>  
  JPM Dec 2026 110.000 call (JPM261218C00110000) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [JPMorgan Chase & Co. $JPM Stock: M&G PLC Lowers Stake](https://www.google.com/goto?url=CAESqQEBxCJF12B4qzQJ2X1SI8Pe25zbTWYLwD0XtL0sRZufSPsflpLuBBAHLxuCI2e_S58ZGEirNPTFFkAB618X-054tcPUqgEBQ3J0SRF98MqfOjEvP0um_Qt5kXOiW90ddlnO0AHpOBemZOW8CVaiWT2mNuj8oos-0QU-S8hgfdNdqO6KonAQnVP58O0AZ7OZ1L48CNQJnbYINO_xkWv2w-uTIRABysC3mCTA&gsessionid=sD_aZ3Imziez4bfG3NqsUQgfdZQWdup6KsbHa55avO-iMvOYjZ93Kg)  
  <sub>MarketBeat, 3 hours ago</sub>  
  M&G PLC cut its stake in JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 40.5% in the third quarter, according to the company in its most recent Form 13F...
- [JPM Nov 2026 357.500 call (JPM261120C00357500) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXTXBeoYYLpnS2-UcQBvzBE19SUrQEWUa8OlZwhnj8jhWTthKB4aQyUyVKekpA96HBsHPyaZ9ODIubV9fFl49cNs9Q3gN6bBeTifYZGmoIpvx-7uCFlrXtGupQaen6QjBzdoiFbKzxgQrC5KkC3lo&gsessionid=sD_aZ3Imziez4bfG3NqsUQgfdZQWdup6KsbHa55avO-iMvOYjZ93Kg)  
  <sub>Yahoo Finance UK, 19 hours ago</sub>  
  Find the latest JPM Nov 2026 357.500 call (JPM261120C00357500) stock quote, history, news and other vital information to help you with your stock trading...
- [JPMorgan Chase & Co. $JPM Shares Sold by Fulcrum Asset Management LLP](https://www.google.com/goto?url=CAESuwEBxCJF14C3rVcNriiV7YFrvWoiinXeYdX919UHX6J2XE9Q8bWxUqw3ZAjaRc1UySYvC3LSdSq5OGgrM_7Bacl51Xw-ScuEUZUUfyozvwFNfeCXctA8U-KHaT-jJ2vcU-cXdUqX7rQXT4uGgKs22hwO5uj6TbO9tnIKYd7qvJstxphezn_CcvlGny1AXloi7L74cGVAmry9YZIvs5V6qfEP2q4_dvfFKtYxHOKBMvHXlDcX_UN7Y4zQUrt7&gsessionid=sD_aZ3Imziez4bfG3NqsUQgfdZQWdup6KsbHa55avO-iMvOYjZ93Kg)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Fulcrum Asset Management LLP cut its stake in JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 100.0% during the 3rd quarter, according to its most recent...
- [JPM Dec 2026 315.000 put (JPM261204P00315000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXX04VJ1yOjsSaLhRsoMy0MYc2HyEh7NRwkE611rbhBH2V5-bfenZM5ksxJJQ5t8ODWp_LbNu0YA7r8e6jnOvM0WcMAGwBlcPZZS5mrTUbpvH7O8Fw6H18F37bULD_Oi0M_aaShBF85NsZjUI4nAyg&gsessionid=sD_aZ3Imziez4bfG3NqsUQgfdZQWdup6KsbHa55avO-iMvOYjZ93Kg)  
  <sub>Yahoo Finance UK, 21 hours ago</sub>  
  Find the latest JPM Dec 2026 315.000 put (JPM261204P00315000) stock quote, history, news and other vital information to help you with your stock trading and...
- [JPMorgan Chase & Co. $JPM Shares Sold by King Luther Capital Management Corp](https://www.google.com/goto?url=CAESwwEBxCJF18YoBHY83fI6cLMBKJrQHCnpx_aNyW9qr5nPE2ZyG3Q-0ZImC4WtWvd_2J0q2h-db6V2fWy5LTEdPShN9hj-xFK19xVLZ8AYGMAUShYxsfCRo87NEKlZokir5ZFvgakS9wK0VbwFnOMeJUCRm08TAwRaeVLE2kKdEXSdtOBrk92CRnbUcSUeWEW2bfdZV2WE-iNc9N2haMYNEd8ByjafV9iZgFK51SPJCqFaEMC_snhOJg7AoTRV-g8JVVpVRxs&gsessionid=sD_aZ3Imziez4bfG3NqsUQgfdZQWdup6KsbHa55avO-iMvOYjZ93Kg)  
  <sub>MarketBeat, 5 hours ago</sub>  
  King Luther Capital Management Corp lessened its holdings in shares of JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 5.2% during the 3rd quarter,...
- [JPM261120C00342500 Interactive Stock Chart | JPM Nov 2026 342.500 call Stock - Yahoo Finance](https://www.google.com/goto?url=CAEScgHEIkXXaa642kn_5_K_JrmBryaNCAHq_qTzMrsTtgvj0AxmtMJLKxGuxFStlSWMizDM9GO08bqAlYL1oaIylY45BjEtVy8vLcvZRin0itOsuT4xuPgIWlVZxzX11V7GgwNvV37CzFmkVQ--UkKAG5OadA&gsessionid=sD_aZ3Imziez4bfG3NqsUQgfdZQWdup6KsbHa55avO-iMvOYjZ93Kg)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [JPM Dec 2026 375.000 put (JPM261218P00375000) interactive stock chart](https://www.google.com/goto?url=CAESeQHEIkXXZokP5CtoimKKTShCCTJttB-aFULLT0tW2VSmiuKu468lJ2BG8VooVfTG3BZ-tqKhZf_pRIviX2FbiqEZcSk7ZkoNhaYxXUu__U4kJp1fFbojeo7vd2SicwFHqStMsMwUe8Gh-DdkKjRT4Vw24oN4vxfWp5M&gsessionid=sD_aZ3Imziez4bfG3NqsUQgfdZQWdup6KsbHa55avO-iMvOYjZ93Kg)  
  <sub>Yahoo Finance UK, 22 hours ago</sub>  
  Interactive chart for JPM Dec 2026 375.000 put (JPM261218P00375000) – analyse all of the data with a huge range of indicators.
- [2 Safe S&P 500 Financial Dividend Stocks Boomers Can Buy and Hold Forever](https://www.google.com/goto?url=CAESsQEBxCJF19HrqRHDQ4Ne_wyhbbmL5gdAtTXWPJHaGcWm7MU3T_4x1vmV-adTNnAXGIZvcgvs2qkbVPQgZjwdmbkr5Thrv8g81Q77FL6KbIKLx4tgE4NpNSMjo3ugDboKH75e-Y5zeR023y-GTAAWl4pb5FMngqkzHaFzn4VINWDZp4Wi4-7uKrrbx4-w_vTZTrOZxuzRBZgh8eZYtvdd7Oc_xY3JaXtnQ54ycp0-hhESBlE&gsessionid=sD_aZ3Imziez4bfG3NqsUQgfdZQWdup6KsbHa55avO-iMvOYjZ93Kg)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  JPMorgan and BlackRock pair rising dividends with huge earnings, yielding about 2% each, making them anchors for retirees seeking growing income.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 344.99 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 339.62 (+1.6%), 50d 340.15 (+1.4%), 200d 325.06 (+6.1%); 50d above 200d
Momentum: RSI(14) 54.8 | MACD 1.551 vs signal 0.671 (histogram 0.880)
Returns: 1d -0.3% | 5d +0.9% | 1m +1.6% | 3m -5.0%
52-week range: 282.84 - 365.18 (now 75.5% of the way up)
Volatility: ATR(14) 6.75 (2.0% of price) | annualised 20d 26.5%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 916.16B
Valuation: trailing P/E 14.47 | forward P/E 13.49 | P/B 2.61 | PEG 1.47
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
Price target: mean 373.48 (+8.3% vs last close), range 312.00 - 425.00
Recent rating changes:
  - 2026-11-02 UBS: main, Buy -> Buy
  - 2026-10-15 Citigroup: main, Neutral -> Neutral
  - 2026-10-14 Truist Securities: main, Hold -> Hold
  - 2026-10-14 Barclays: main, Overweight -> Overweight
  - 2026-10-14 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-14 Morgan Stanley: main, Equal-Weight -> Equal-Weight
Institutional ownership: 75.8%
Largest holders: Blackrock Inc. (7.7%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.7%), Vanguard Portfolio Management LLC (2.7%), Bank of America Corporation (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 1,583 shares in 6 transaction(s) | sold 15,935 shares in 4
Net: -14,352 shares (-0.1% of insider holdings) | insiders hold 14,897,970 shares
Distinct insiders: 0 buying, 2 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-10 LEOPOLD ROBIN (Officer): 2,500 shares, 882.03K
  - 2026-08-11 LEOPOLD ROBIN (Officer): 2,500 shares, 903.52K
  - 2026-06-22 FRIEDMAN STACEY R. (General Counsel): 5,467 shares, 1.81M
  - 2026-05-20 FRIEDMAN STACEY R. (General Counsel): 5,468 shares, 1.64M
(6 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

- [MercadoLibre stock: JPMorgan and Morgan Stanley cut price targets](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afb16885855441680ecf89f34e748d6&url=https%3a%2f%2fwww.ad-hoc-news.de%2fboerse%2fnews%2fcorporate-news%2fmercadolibre-stock-jpmorgan-and-morgan-stanley-cut-price-targets%2f70520769&c=7695739303521172534&mkt=en-us)  
  <sub>Ad Hoc News, 9h ago</sub>  
  JPMorgan and Morgan Stanley lowered their price targets for MercadoLibre in a report published by iProUP on Sunday, November 15. The revisions sharpen the focus on whether the Latin American ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,472.77 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 1,638.49 (-10.1%), 50d 1,750.69 (-15.9%), 200d 1,780.29 (-17.3%); 50d below 200d
Momentum: RSI(14) 32.4 | MACD -87.071 vs signal -72.423 (histogram -14.648)
Returns: 1d -1.3% | 5d -3.9% | 1m -19.7% | 3m -17.2%
52-week range: 1,472.77 - 2,295.00 (now 0.0% of the way up)
Volatility: ATR(14) 63.78 (4.3% of price) | annualised 20d 58.2%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 74.66B
Valuation: trailing P/E 39.51 | forward P/E 27.74 | P/B 9.11 | PEG 0.81
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
Price target: mean 2,204.55 (+49.7% vs last close), range 1,600.00 - 2,800.00
Recent rating changes:
  - 2026-11-11 UBS: main, Neutral -> Neutral
  - 2026-11-09 JP Morgan: main, Neutral -> Neutral
  - 2026-11-05 Scotiabank: main, Sector Outperform -> Sector Outperform
  - 2026-11-05 StoneX: main, Buy -> Buy
  - 2026-11-05 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-11-05 BTIG: main, Buy -> Buy
Institutional ownership: 81.0%
Largest holders: Capital Research Global Investors (6.0%), BAILLIE GIFFORD & CO (5.8%), Capital International Investors (3.9%), Capital World Investors (3.7%), Morgan Stanley (3.1%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 3,631,918 shares
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

- [Why the Microsoft Outage Came at the Worst Possible Time for the Stock](https://www.barrons.com/articles/microsoft-stock-office-outage-365-a8356c9e)  
  <sub>Barron's, 2 hours ago</sub>  
  A global outage hit the company's Outlook, Teams, and Copilot AI assistant, impacting users across more than 70 countries, according to outage tracker...
- [Microsoft (MSFT) Strikes AI Deal That Broadens Its Chip Supplier Base](https://finance.yahoo.com/technology/ai/articles/microsoft-msft-strikes-ai-deal-061353570.html)  
  <sub>Yahoo Finance, 8 hours ago</sub>  
  Microsoft (NasdaqGS:MSFT) has entered a new AI partnership with Cerebras that shifts part of its chip focus away from Nvidia. The arrangement centers on...
- [Microsoft: Assessing The Threat To Office Tools, Reiterate Buy](https://www.google.com/goto?url=CAESogEBxCJF16O60rqWMK0FW0Kc6Lb9d3PVi32x7RDLnLpAv-gOnw3TozMZsnMU0L12GlNQR-09ZtPVXF28XS7qFpvS3BsyunB9Piy559oGAHiesxvRIgz5HlI76uu6Gh1W8Gfy9ELHS-Ez07qKPmdF5cRB7TE7Vn5qf3ESSULdMbCmpnAbcLjcAhk1qQpSlztZyUtQx5Hhz4B4HYEACWpK3dpB-LE&gsessionid=5rCfUmfJAyt5nDwZlPDWVBBnusZPBkRvoTag8yrew-AgnGjPnpRn8A)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Microsoft remains a Buy despite a global outage and Anthropic's productivity-tool launch; the entry point is less attractive after the summer rally. MSFT's...
- [Has Microsoft Stock Become A Different Bet?](https://www.google.com/goto?url=CAESpAEBxCJF14KIkslO7vGCSM6UfpHseWZ8GL-0JCCEujyoiYzD7azDxPXmx0LMna9f3_UX-MNsO96TjeUEwpuu9rU_dBVN9sCqWW6TwH4GD72g0g32ZxtO7Mps1oZbdQGQSUk1CTnO7zMeMI3IZQ5wLB2V6MzrbXugzUCUZd_ieYtyOHV1Sh1ml4AX1nI4KU-j6SVVmuGd0gMQWah7Zi06w_5ugy0JzA&gsessionid=5rCfUmfJAyt5nDwZlPDWVBBnusZPBkRvoTag8yrew-AgnGjPnpRn8A)  
  <sub>Trefis, 7 hours ago</sub>  
  For questions about this article or underlying research, email help@trefis.com.Microsoft (MSFT) stock trades at 27.3 times earnings, against 21.9 for the...
- [One Magnificent Seven Stock Looks Ready for Its Next Big Move](https://www.google.com/goto?url=CAESpgEBxCJF1ysUOXrF-8ow3TW_XVjleVcP2goz1tKy1cAw-dHWlRmOb5wgqou8GSaA_462ESsdjMrvSZ6nhGm6ffaW7ujbAurstQ9V3dkDdOZWLvnMOwIaxFmqYZp0OzQN3-FSQGQhgMH55rObDhFoLuhAqHOQpHy7ECGHgRMBaq5e3W8-89_DxwL23NqBAvR_KJDIxv8CzqCqsv_59ViHRTD38oiV_8BW&gsessionid=5rCfUmfJAyt5nDwZlPDWVBBnusZPBkRvoTag8yrew-AgnGjPnpRn8A)  
  <sub>24/7 Wall St., 33 minutes ago</sub>  
  Microsoft (MSFT) trades near $521 after a rough week, yet a $649 price target implies roughly 25% upside on Azure's 48% growth.
- [MSFT 261116 590.00P (MSFT261116P590000) Stock Options Chain | Quotes & News](https://www.google.com/goto?url=CAEScAHEIkXXLk4aDW8M_b5QQyFEX8C1EXdIq-H5MX11kAGmFUVGkK_rDE9T5dzNpZtmOBfMz8xCwIltGBbRksdov7Pllk_z_WXyvtPot-wh4G-MkpXuRJAnFiO4UEK0l-_fFgcW0JC18jaDZtUzCLw76M4&gsessionid=5rCfUmfJAyt5nDwZlPDWVBBnusZPBkRvoTag8yrew-AgnGjPnpRn8A)  
  <sub>Moomoo, 6 hours ago</sub>  
  Track real-time MSFT 261116 590.00P (MSFT261116P590000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [Tokenized Stocks: Binance Pays MSFT and AMAT Dividends](https://www.google.com/goto?url=CAESsgEBxCJF18Iwz-uGMkpnsGmypq28oCyuVFFMAr5W_tN4ZcQ_c4IUuiAvpTJqmldcrBOaelwHx2r-DE5McS6MFHtTTRzJR2_kSW94XhTatph7gBxLfJ2ywAR5tc5alfEkMdCcAYKpVQZCtP0Yr7g41K6NTI0_l5If2JSDiqEw9HpC04n7Y72HgdVtOrki2DE4xLYRXCIYKV2kg1L80sCVz33tEjhVXDo9wsQEXtjVIZOf49Mp&gsessionid=5rCfUmfJAyt5nDwZlPDWVBBnusZPBkRvoTag8yrew-AgnGjPnpRn8A)  
  <sub>Tokenist, 2 hours ago</sub>  
  Binance will reinvest Microsoft and Applied Materials dividends into tokenized stocks MSFTB and AMATB. Here's what holders will receive.
- [Stock Market Today: Jensen Huang Eyes a Comeback as Nvidia Closes Its Worst Week Since April 2025](https://www.google.com/goto?url=CAESyAEBxCJF1xpJvKPOgj1683GQHfAPUCDF0PIeeCqIY91klix9FCGK-SocnQpJZSz1pNCAfba4NEssXU6VCNuEnxR4ncap58bAVBLdgxn4IadEVz4PunRQwUcKr4u_7mI8wN4PWytt5-pKUiM040IbXBWLdjfwY0NUBQbYHsuwkdpkmBsNq6BzSNO3jX4E9fag_VT7828rHoK0l8_mjp65aQRHZXcvI6HAxQa4SrvVtxqCcDn2aSPGZqIryn8uYfkuAZOQQBvkWuLbGw&gsessionid=5rCfUmfJAyt5nDwZlPDWVBBnusZPBkRvoTag8yrew-AgnGjPnpRn8A)  
  <sub>ChartMill, 1 hour ago</sub>  
  Nvidia fell again Friday and lost about $600 billion in market value in a week. Now Jensen Huang is reportedly exploring a return. Chip stocks slid...
- [Nvidia Stock's 'Icarus' Fall Isn’t Over Yet, But Microsoft, Apple Show Path to Recovery, Says Top Strateg](https://www.google.com/goto?url=CAES6gEBxCJF1y2qWmfw4SKNhA6JQXXffEnoDZT9xfcbR27s7VJJASLu0GXKnd_8Y8i6AZ7uMlE9z0nyHSTKc8dO_E0qsuTTx1S17dmukPZ4m5CxrNJM00TaoFeKgzLuMQmt1jt9_ZYchB9ZrSQCpfz9jSZZt-XoeSc-JxFqxibrlP6NQdgd69eGIxLI-PnRwPCNinZftrVFzRE6f5fgKOGlQ43i0xe3NLioaMJsgM9qvyaOTXAMQ8D8y4T7YMwNVMC8axG5GJkle7PMl2a9jHi3Dx5PLztecdCqtcBVE48tgAdUMgmlopFGbGJVwVQ&gsessionid=5rCfUmfJAyt5nDwZlPDWVBBnusZPBkRvoTag8yrew-AgnGjPnpRn8A)  
  <sub>Benzinga, 2 hours ago</sub>  
  JPMorgan's Michael Cembalest says Microsoft's and Apple's recoveries offer hope for Nvidia despite AI competition and market-share losses.
- [Nebius Stock Falls 10% After Q3 Earnings: Should You Buy Now?](https://www.google.com/goto?url=CAESrwEBxCJF15LKieKqZHDq2tobWt8lCHicyVoxtkYcj56JV2nRq4xJSl2Z5ta12ioHK6YnP2WKNbGENj7c7U8L79cU1HW8ELKoPbKkfB--gpVf8Z1PWI3N0xdzK2Pr-IHmWN8PJLTcF7yDBY1EWqK1ZoFu9locknwRU9IATilZcQWLy_MzMNLzC8WFNZgiIIf44RSsPCwHgNuzFmpR2iOh3gQLBJzT3MWKfqYmf04jQD_o&gsessionid=5rCfUmfJAyt5nDwZlPDWVBBnusZPBkRvoTag8yrew-AgnGjPnpRn8A)  
  <sub>TradingView, 45 seconds ago</sub>  
  Shares of Nebius Group N.V. NBIS have declined 10% since the company reported third-quarter 2026 results on Nov. 12. Despite the recent pullback, the stock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 519.65 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 528.69 (-1.7%), 50d 519.40 (+0.0%), 200d 441.87 (+17.6%); 50d above 200d
Momentum: RSI(14) 47.0 | MACD 1.135 vs signal 3.302 (histogram -2.167)
Returns: 1d -0.8% | 5d -4.7% | 1m -1.8% | 3m +7.9%
52-week range: 352.83 - 555.80 (now 82.2% of the way up)
Volatility: ATR(14) 14.73 (2.8% of price) | annualised 20d 36.9%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.86T
Valuation: trailing P/E 27.12 | forward P/E 21.48 | P/B 8.20 | PEG 1.55
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
Price target: mean 636.12 (+22.4% vs last close), range 440.00 - 870.00
Recent rating changes:
  - 2026-10-29 Bernstein: main, Outperform -> Outperform
  - 2026-10-29 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-29 Citigroup: main, Buy -> Buy
  - 2026-10-29 DA Davidson: main, Buy -> Buy
  - 2026-10-29 TD Cowen: main, Buy -> Buy
  - 2026-10-29 Scotiabank: main, Sector Outperform -> Sector Outperform
Institutional ownership: 76.4%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.3%), FMR, LLC (2.7%), Geode Capital Management, LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 518,348 shares in 17 transaction(s) | sold 261,954 shares in 12
Net: +256,394 shares (+1.6% of insider holdings) | insiders hold 16,560,413 shares
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

- [Nvidia stock falls as Jensen Huang reportedly weighs CEO comeback, Musk backs return](https://finance.yahoo.com/markets/article/nvidia-stock-steady-as-jensen-huang-reportedly-weighs-ceo-comeback-musk-backs-return-015644730.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Nvidia (NVDA) stock futures fell 3% on Monday as investors digested a report that supporters of Jensen Huang are lobbying for his return to the AI chip...
- [NVIDIA Corporation (NVDA) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/NVDA/)  
  <sub>Yahoo! Finance Canada, 3 hours ago</sub>  
  NVIDIA Corporation (NVDA) · -12.75% · -28.74% · -27.89% · -12.68% · -12.85% · 435.87% · 372,128.59%. Key Events. Baseline. Advanced Chart. Loading...
- [Nvidia Stock Is Down 32%. Is It a No-Brainer Buy at $163 or a Value Trap?](https://www.google.com/goto?url=CAESsAEBxCJF11fZnOJ3cogJf5xi_R4G1LQOiFtVVD_0_trRPvaSD7iIyjJT2BFayJxJHRLEBSvadmx8Y-3Oef2NP2yCd0B5iBpWgflRUdaEO-ha53WRIc3zlTubvMcD9T1eqbsOx2f_HppDPNdpquYptZkRufxhn1tRyKb71IXARnq8EZyzqkKabPFkCTzCgJVhxKK8r8Ugvoro2vMGOli5xBdutd_jHGPyyMmceJqCYoPi_w&gsessionid=6_E2aGTCPc6ZIkGzDnFAJxPKJzieZ3Uc1VUXlK2otd77aXYIFLGF8w)  
  <sub>The Motley Fool, 2 hours ago</sub>  
  Nvidia (NVDA -2.01%) has gone from one of Wall Street's hottest artificial intelligence stocks to one of its biggest sources of anxiety.
- [Nvidia gets two more price target cuts from analysts ahead of earnings](https://www.google.com/goto?url=CAESqAEBxCJF17IkqVSCkdIEFg7SZRxEgY8-jK9hiJswSSht2G4yhXgmLq3sDzDkr_zQGR034WB0X0fQ0BOzPdT_TJhDR7neLdyoXpnsF3xRPdBIpM6PnYdP5TpHN8nwKLzZ-JKsqRR5coS5hCW7xCCSdqSXTikZ_0YinWHJGPjXl_G4A-1zXD-19gfwJHeXHP6sj0xon3qYllOgK_8kcS3JAFW_bY3leMYz8q0&gsessionid=6_E2aGTCPc6ZIkGzDnFAJxPKJzieZ3Uc1VUXlK2otd77aXYIFLGF8w)  
  <sub>CNBC, 2 hours ago</sub>  
  Nvidia has received two more price target cuts from shops on the Street following the departure of its long-time CEO, Jensen Huang.
- [Nvidia Stock Falls Again. It Doesn’t Need a Jensen Huang Comeback to Thrive.](https://www.google.com/goto?url=CAESjwEBxCJF15Spb3SPzfUmYdRzz9DR8arYABu_PEeeygjB98hVxMyIM3ETvkw2iIzl9yZjkZU_2LoxQphgffDF-V6gYUwd7LUTD-mtdUlIjMnr_BaHliK7B2JYGMfY83gYUr0YLEdG3poxUATX4l4dci-j1HP8w9F0RmkklDaXLCB-K4A5Z3ZshVn5FPKjBX15qA&gsessionid=6_E2aGTCPc6ZIkGzDnFAJxPKJzieZ3Uc1VUXlK2otd77aXYIFLGF8w)  
  <sub>Barron's, 2 hours ago</sub>  
  has begun. Shareholders shouldn't count on a return, but that doesn't mean the chip maker's stock can't rebound. Nvidia shares were down 2.8% at $158.27 in...
- [Trump held as much as $62 million in Nvidia stock as his team eased China chip rules](https://www.google.com/goto?url=CAESfAHEIkXXd0tas5fs0WsVqQ8-bB1njdpWLem7kLy2xE626gNVo46503fDjw1hnNXuCvNOhMRARmj_KRxB8fgGYXvXPXeX9AbuXe5-1GJtKXpjTcHZ8ThIxkyHrh9B9jZfkcJTbDIrieIVZh-HTDwCO2wEux0iYVBN7-xvWMs&gsessionid=6_E2aGTCPc6ZIkGzDnFAJxPKJzieZ3Uc1VUXlK2otd77aXYIFLGF8w)  
  <sub>Quartz, 1 hour ago</sub>  
  President Donald Trump owned Nvidia $NVDA shares worth somewhere from $13 million to $62 million at the close of August, according to an analysis of his...
- [NVIDIA Corporation (NVDA) stock price, news, quote and history](https://www.google.com/goto?url=CAESZQHEIkXX5o5xzDUT3wX9-IOIDo_iVFIvJI7ou4UhQ4DFgGEMCAtXz59aitrbxVSCWX9Z7wUhnudo6yJGyX3Ef4aulne7EoQGuzwU7sW168EOtvhmHbptfTTbh0rWQd56xICkYqtZ&gsessionid=6_E2aGTCPc6ZIkGzDnFAJxPKJzieZ3Uc1VUXlK2otd77aXYIFLGF8w)  
  <sub>Yahoo Finance UK, 4 hours ago</sub>  
  372,128.59% · Previous close 166.19 · Open 169.89 · Bid 160.01 x 300 · Ask 166.48 x 200 · Day's range 158.39 - 170.00 · 52-week range 148.80 - 243.37 · Volume...
- [NVIDIA Falls 4% Ahead of Earnings as Elon Musk Joins Calls to Reinstate Jensen Huang; AMD Drops 6%, Taiwan Semiconductor Slides 5%](https://www.google.com/goto?url=CAESmwEBxCJF10rGVTAAgeawL26dEYy3z64qB9so4hvPJ5vMqNUxTkUlbeYmKmPPBBiGDe_uHuRl3Uup5Yfblyz5L5k-4MlwRcX2-2QmBzBbfSgumS3AjAMwtD-nPMPRcTvB0vbzn_uXjf5hlXvz3_teqh0QAZqUOacgmhsTrME3tKXx53_xyAucCG3AammAsYfaPF84cu7312QgNcXL1g&gsessionid=6_E2aGTCPc6ZIkGzDnFAJxPKJzieZ3Uc1VUXlK2otd77aXYIFLGF8w)  
  <sub>Yahoo Finance, 30 minutes ago</sub>  
  Wall Street is pricing a leadership shock and a looming earnings test into NVIDIA (NASDAQ:NVDA) all at once. NVIDIA stock is at $157.01, down 4% in morning...
- [Buy Nvidia stock or wait? A guide to making the call on any stock.](https://www.google.com/goto?url=CAESygEBxCJF18y3hY4YmvqwVEf6RxSiGx9Zx8hs_svrZ3Ply-x_VjlkqqW3KP4GZH11TE5mLP5gLVE7Stv31jpwcs4bqQh-krmnnic5ybwLtpqq7YUAOSQCRXUTA0fq5VFezvnQclSZ2M1vtaMRjOSSS4SarEBV3OzHC0PEUBJ-KkozAdpaobDSdTj08iwSasKnlZy5g4y3tZdZ-UI0tu7_RGBJWwciSYCG5DzBNOLEzYpnO3QySr0eAG7Z4kln_3nFF4uyjiyXQnZyXbEF&gsessionid=6_E2aGTCPc6ZIkGzDnFAJxPKJzieZ3Uc1VUXlK2otd77aXYIFLGF8w)  
  <sub>Yahoo Finance, 41 minutes ago</sub>  
  Nvidia's CEO Jensen Huang resigned, pushing NVDA stock to a multiyear low. Use this 7-question guide to decide whether the dip is a buying opportunity.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 161.76 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 195.92 (-17.4%), 50d 213.28 (-24.2%), 200d 204.04 (-20.7%); 50d above 200d
Momentum: RSI(14) 24.5 | MACD -14.931 vs signal -11.074 (histogram -3.857)
Returns: 1d -0.7% | 5d -9.5% | 1m -24.5% | 3m -26.4%
52-week range: 161.76 - 239.24 (now 0.0% of the way up)
Volatility: ATR(14) 9.61 (5.9% of price) | annualised 20d 51.9%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 3.91T
Valuation: trailing P/E 20.45 | forward P/E 10.21 | P/B 17.06 | PEG 0.20
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
Consensus: buy (mean 1.64 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 11 strong buy, 36 buy, 14 hold, 1 sell, 0 strong sell
Price target: mean 268.76 (+66.1% vs last close), range 130.00 - 515.00
Recent rating changes:
  - 2026-11-12 Melius Research: down, Buy -> Hold
  - 2026-11-12 DA Davidson: main, Buy -> Buy
  - 2026-11-12 Craig-Hallum: down, Buy -> Hold
  - 2026-11-12 B of A Securities: main, Buy -> Buy
  - 2026-11-12 BMO Capital: main, Outperform -> Outperform
  - 2026-11-12 Baird: reit, Neutral -> Neutral
Institutional ownership: 71.2%
Largest holders: Blackrock Inc. (8.1%), Vanguard Capital Management LLC (6.4%), State Street Corporation (4.2%), FMR, LLC (3.9%), Geode Capital Management, LLC (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 2,613,243 shares in 18 transaction(s) | sold 6,198,325 shares in 9
Net: -3,585,082 shares (-0.4% of insider holdings) | insiders hold 1,001,596,032 shares
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

- [Novo Nordisk Shares Gain 2.4% Following Additional CagriSema Weight-Loss Trial Analyses](https://finance.yahoo.com/healthcare/articles/novo-nordisk-shares-gain-2-110923533.html)  
  <sub>4 hours ago</sub>  
  Novo Nordisk (NYSE:NVO) shares rose 2. 4% after the Danish pharmaceutical company presented additional findings from its REDEFINE 1 clinical trial,...
- [SA Asks: What are the most attractive Big Pharma stocks right now? (LLY:NYSE)](https://seekingalpha.com/news/4672799-sa-asks-what-are-the-most-attractive-big-pharma-stocks-right-now)  
  <sub>19 hours ago</sub>  
  Stephen Ayers: When it comes to Big Pharma stocks, I'm still interested in obesity names like Eli Lilly (LLY) and Novo Nordisk (NVO).
- [NVO Nov 2026 49.000 put (NVO261120P00049000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXh0e9_irtsdxbPmJUQscfOK8uWiRpuOvWryVSKrx7nZz4QFxfwDZ22zvuyPs4mKKNplZE9fkS3-MMEqZRgveoaaNlodXHysAUxA-xWmorNigKIVAFujA43aNM4x7R1VBPmvY_rqQsQw8c9F3DTsU&gsessionid=3XW6nxrivTlj6o1kq5HK0aqRWe60pgZbz0k5KpO_S8TKhqTXeufi1w)  
  <sub>22 hours ago</sub>  
  Find the latest NVO Nov 2026 49.000 put (NVO261120P00049000) stock quote, history, news and other vital information to help you with your stock trading and...
- [NVO Dec 2026 41.000 call (NVO261211C00041000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXmMWH4ppTyrBa0Bm3kBDOUkRmONpimf5ucn10h9aYey9m2AAotV8-4rRRdzdWP_0BTcDeQqkjnk0mFk_kuN81OIH_qET8BxJo6r5GXHYDFdiA3poBri2Eq9jf_4zWNea5YtVuQei-WBwxNam5uM8&gsessionid=3XW6nxrivTlj6o1kq5HK0aqRWe60pgZbz0k5KpO_S8TKhqTXeufi1w)  
  <sub>19 hours ago</sub>  
  Find the latest NVO Dec 2026 41.000 call (NVO261211C00041000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Novo Nordisk reports additional CagriSema weight-loss findings (NVO:NYSE)](https://www.google.com/goto?url=CAESoQEBxCJF1wdjzFB183ULmgMdp5KymH4CVo9aZ8SZ0OphjsjyhaytqmEDDK1yYYCyTuzGUwXn6Rt1TeQTOBMpjdN0Gnp7S03-6Wmv_XR8FH039N5CdY_8Ip1W8-7n4PKURrKn5sT6HeizmCSAI4KF4q2o9ClPkI1OZokcb_4R9RSrACHL-9PBr_I_VBJeLxPhP_keR5iNK2LWk8fDGM7wXaDIwg&gsessionid=3XW6nxrivTlj6o1kq5HK0aqRWe60pgZbz0k5KpO_S8TKhqTXeufi1w)  
  <sub>19 hours ago</sub>  
  Novo Nordisk (NVO) said two additional analyses of its late-stage REDEFINE 1 trial found differing weight-loss patterns and improvements in daily...
- [NVO261120P00033000 Interactive Stock Chart | NVO Nov 2026 33.000 put Stock - Yahoo Finance](https://www.google.com/goto?url=CAEScgHEIkXXVaDhkTk3EAXIgKtq8YvUvPNm832guNLP0ZQLHQPeGkKLcYG7dYlbUofFq43uNR4LxUs9y6-qLg46_8tfvkQ9e7fEjGJqollrmtAPhXS8-WoH9KgFVE8D5g75Y5nZ71fpUrzHI9Z3xqOqF6oK1w&gsessionid=3XW6nxrivTlj6o1kq5HK0aqRWe60pgZbz0k5KpO_S8TKhqTXeufi1w)  
  <sub>20 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [NVO Nov 2026 32.000 put (NVO261120P00032000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScwHEIkXXXPoOLKnRxz4TZsGRaOa58Bx31-JrrVaSuFJyFSdEoRdTbSf-sgJ8bMXwzbVxXI-t55q7rwtVyNk4PAAzVptD7WyZ6auoQgOQteWMBAF1v8DeuMSZIwIAPK3f84UcAfcslW8B-9T134woERVD-O0&gsessionid=3XW6nxrivTlj6o1kq5HK0aqRWe60pgZbz0k5KpO_S8TKhqTXeufi1w)  
  <sub>23 hours ago</sub>  
  Find the latest NVO Nov 2026 32.000 put (NVO261120P00032000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Will Novo Nordisk stock break $42.4 resistance amid continued buyer support?](https://www.google.com/goto?url=CAESkQEBxCJF13NMdJPelgCa_GJIkXyQlKeXPhizyxsGcn_mrtQ1RsKGf2__7ovuBs2mKDGPvxocoGJCgGTjzfF1_YsFwgE9bISOh8-z9d2ZvNVIvQy64QJSt_NM9GCIVjljMGn2AeyZl_uZcE3UKSXDE_LXobFJBysPevvQ7bTrLQSbcfY4ToAfteajRckm6mc4IG6Q&gsessionid=3XW6nxrivTlj6o1kq5HK0aqRWe60pgZbz0k5KpO_S8TKhqTXeufi1w)  
  <sub>7 hours ago</sub>  
  Novo Nordisk gains 2.44% today to $41.64 after a bullish Q3 earnings call and strong technical momentum.
- [Novo Nordisk stock rises on CagriSema weight loss data By Investing.com](https://www.google.com/goto?url=CAESsAEBxCJF13Y4jyHs2JwGuxNSD_gCWQR66yUyQozKL6swhEAnWAXI6PplwPXtQG8lc_UfT9enzpBLxol8JjafyYfa6age494kbrMFKxblSxUIqERV1pVann8BWxTyoNSjsmilDN_n7HP6rxffU1ykJHdWFMZ1ud0qIprg_VRzY8liMrQaheR06LF0yvU9f2LRxUR8-3YIHpzJA_ydl7eJLcyzI-uBrvdqBwvfFDsgcZEwFw&gsessionid=3XW6nxrivTlj6o1kq5HK0aqRWe60pgZbz0k5KpO_S8TKhqTXeufi1w)  
  <sub>6 hours ago</sub>  
  Investing.com -- Novo Nordisk (NYSE:NVO) shares rose 2.4% after the company presented additional analyses from its REDEFINE 1 trial showing early responders...
- [Lilly’s Zepbound shows promise in teen obesity trial (LLY:NYSE)](https://www.google.com/goto?url=CAESlwEBxCJF1-GPMxLKfNZ8mPx0F7iuXJg9PrwbHTtDfbtnL_RT9kmpZpveCJtdqeWm2CMKHflGcHeqkYWrsTD0UA3BtcQT98tWzkI7Vp0NzLpQvg4WkorwROoK6PlJwV_6_AqIt-Zn5Mgi-F6W0MZ8AJunx36aXWk2TmLQrWDr524yRa9F6wr_qbRT6CfLggPF-RrBI54g7tZk&gsessionid=3XW6nxrivTlj6o1kq5HK0aqRWe60pgZbz0k5KpO_S8TKhqTXeufi1w)  
  <sub>15 hours ago</sub>  
  Eli Lilly's Zepbound trial finds adolescents lost about 40 pounds on average over 18 months; approval for younger patients remains uncertain.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 41.85 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 40.14 (+4.3%), 50d 39.99 (+4.6%), 200d 43.09 (-2.9%); 50d below 200d
Momentum: RSI(14) 59.1 | MACD 0.456 vs signal 0.210 (histogram 0.246)
Returns: 1d +0.5% | 5d +1.1% | 1m +7.8% | 3m -8.4%
52-week range: 35.29 - 63.98 (now 22.9% of the way up)
Volatility: ATR(14) 1.05 (2.5% of price) | annualised 20d 32.6%
Volume: 0.50x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 184.49B
Valuation: trailing P/E 10.57 | forward P/E 12.17 | P/B 5.64 | PEG 4.31
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
Price target: mean 45.46 (+8.6% vs last close), range 39.52 - 64.21
Recent rating changes:
  - 2026-10-12 BMO Capital: main, Market Perform -> Market Perform
  - 2026-09-11 Morgan Stanley: down, Equal-Weight -> Underweight
  - 2026-03-02 Goldman Sachs: down, Buy -> Neutral
  - 2026-02-24 JP Morgan: down, Overweight -> Neutral
  - 2026-01-09 CICC: init, ? -> Outperform
  - 2025-12-08 Argus Research: down, Buy -> Hold
Institutional ownership: 10.0%
Largest holders: Dodge & Cox Inc. (0.6%), LOOMIS SAYLES & CO L P (0.5%), Arrowstreet Capital, Limited Partnership (0.5%), Franklin Templeton, Inc. (0.4%), Morgan Stanley (0.4%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 4,321,060 shares
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

- [PG Nov 2026 172.500 call (PG261120C00172500) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/PG261120C00172500/)  
  <sub>13 hours ago</sub>  
  Find the latest PG Nov 2026 172.500 call (PG261120C00172500) stock quote, history, news and other vital information to help you with your stock trading and...
- [P&G to Webcast Presentation From P&G Investor Day 2026, November 19](https://finviz.com/news/416785/pg-to-webcast-presentation-from-pg-investor-day-2026-november-19)  
  <sub>3 hours ago</sub>  
  CINCINNATI--(BUSINESS WIRE)--The Procter & Gamble Company (NYSE:PG) will webcast the presentation from the P&G Investor Day 2026 in Cincinnati,...
- [PG Nov 2026 162.500 put (PG261120P00162500) interactive stock chart](https://www.google.com/goto?url=CAESeAHEIkXX9YMUC0x3GyzIFjC-6dgGTbJkV0aEzNgyskD77hHXydxWPlBRdreGPthSdQQMxcaoc9Wve91fr044RUzbMP4f_wMn2c98tEFQuVTGCWV-jxCU_jVGNRId1kGCqPbqy3E1y90J5gIecuEIR7UF3SJwNKr-8Q&gsessionid=WbiCRtSCe6dOs7kvXKDhaV0GmrEK26OCAoOQmUBZS3FF9g0Hd-Ig1Q)  
  <sub>13 hours ago</sub>  
  Interactive chart for PG Nov 2026 162.500 put (PG261120P00162500) – analyse all of the data with a huge range of indicators.
- [Why Investors Should Own Businesses That Can Win Under Any Administration](https://www.google.com/goto?url=CAES2gEBxCJF14ned1Sxr_TlwzPQgySqwoekDKoyvH5m9lVtQI814XX1RFqfqQdz_hErZBTgjdZYOnDA6kv75ITaHoqTmBow6hmapTtpyhI7VSiHQ4NNhRHnVk7s-uN3Lj6NxPY7IrDfj1CVV_k6DU0maeoLC-zx6S4K1HgsEeo99f7WCNG3731s4C7wAe8j7qj24efHF4VxHSet5psDFkuy-nUF2a1l6Lxmvns4gzOtQX3Xo6BRDZ24wH1eyKW4RAepzn95uP09t4pDseI3z1A0is2NCcp1OPBknrFyew&gsessionid=WbiCRtSCe6dOs7kvXKDhaV0GmrEK26OCAoOQmUBZS3FF9g0Hd-Ig1Q)  
  <sub>18 hours ago</sub>  
  Detailed price information for Procter & Gamble (PG-N) from The Globe and Mail including charting and trades.
- [4 Durable Dividend Stocks Retirees Can Count On for Passive Income](https://www.google.com/goto?url=CAESqwEBxCJF1z7kMDPXt-IF62jEAJv8cjMdAQiss3-AetDw6Oj1TAKAeWbS5Uno-qxK5oqsLIw-cVzRoxW8A8PieMSrmvPTgx6RhxBBriJVVE7cNI1HuyzX0q6-Oomew6rJT4YJszXOaQXCVE9nslj6SnRdWN2kzfjLFsiTn2jhKxB6H6CWsJvX6S7xD7tdEKZcc-7n0yxjn4Msmm7vdupzTSYBSnFgyODchZHAEgY&gsessionid=WbiCRtSCe6dOs7kvXKDhaV0GmrEK26OCAoOQmUBZS3FF9g0Hd-Ig1Q)  
  <sub>24 hours ago</sub>  
  Johnson & Johnson and Procter & Gamble have raised dividends for 64 and 70 straight years, backed by $21 billion and $16 billion in free cash flow.
- [Procter & Gamble Company (The) $PG Shares Sold by Mawer Investment Management Ltd.](https://www.google.com/goto?url=CAESxwEBxCJF11FJDw7_vZMx-nzZmpUqFEfm8aXmXLlxYW99msVlY0o1BRqUkR6ZdX7CIobCkFW90XIQwgXQSzsH1QTt9Zk4lTR6i2LkPHIn08SMXVvN43LBPi8MakndgjlV4lmVIvZbodliwRdVRzM7-aFl7cu1vfmtQ4uTVlwc9f6DH-i7FBahjqn9834R5wJU-Ij_S6dDnE5yGfexz4c2a6Gx2qAc3zguzfsyjqQFp-DCbscr_fBigT1roMGGPtO0cjdk1D_jwHfg&gsessionid=WbiCRtSCe6dOs7kvXKDhaV0GmrEK26OCAoOQmUBZS3FF9g0Hd-Ig1Q)  
  <sub>21 hours ago</sub>  
  Mawer Investment Management Ltd. lowered its stake in Procter & Gamble Company (The) (NYSE:PG - Free Report) by 45.5% during the third quarter, according to...
- [UBP PG Active Income AP USD C (0P00019BEX) Seasonal Returns Chart - Yahoo Finance](https://www.google.com/goto?url=CAESdwHEIkXX8P0yEx2ID57ZP_OMmh1yp-69aJmRU5up8O9Dky9n4ruyn3yXF806k0rmE9-JlVDEm5pT-LDRyq91TgGXKRk1ladtSh5_71S3KH6SsRRhRSCivMir2GXdA-VGTZfO-q6MIAz027VfBE1oTiJr7Rm2iLx5&gsessionid=WbiCRtSCe6dOs7kvXKDhaV0GmrEK26OCAoOQmUBZS3FF9g0Hd-Ig1Q)  
  <sub>14 hours ago</sub>  
  OTC Markets OTCPK - Delayed Quote • USD. UBP PG Active Income AP USD C (0P00019BEX). 149.99 +0.47 (+0.31%). At close: November 5 at 4:00:00 p.m. EST...
- [PG Nov 2026 210.000 call (PG261120C00210000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScgHEIkXX79TDTxLiVAkJF7u8uJb-jZwnb_U8V5BHY6YVQLl7VSJw5QMeiqzmMBiFzmZuhOwBh81ZOosHhxNSr52ujOKmmAXdNTQMZp7BJEvJgLQ6YN7iz09U1dKR42EKX_xSIvKSsWvo6DQTzB3m4uFt2A&gsessionid=WbiCRtSCe6dOs7kvXKDhaV0GmrEK26OCAoOQmUBZS3FF9g0Hd-Ig1Q)  
  <sub>21 hours ago</sub>  
  Find the latest PG Nov 2026 210.000 call (PG261120C00210000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Raymond James Adjusts Price Target on Procter & Gamble to $185 From $180](https://www.google.com/goto?url=CAEStgEBxCJF1_e2zu7kUCBKOzfs7fe7X_jM5Q4098ET1o0R7ab4AYAKT-t3EpcuJnpVb6FAw2g15XHdPMd0eP2M2KJ0fn8oO2eh8mlFWyZOeOS59vXxEINKdmTFY5cpdeQ32aF2-SH0EV63RN-F8ijLtbv_Nq1a8L5MT9xUmBsglSHaNSnewq4K9TjpaIqNC9exOesjzbzM6m_MWvCUevYWe2wlKBGoTAou7jwOk7VEovEix929nVlX7Q&gsessionid=WbiCRtSCe6dOs7kvXKDhaV0GmrEK26OCAoOQmUBZS3FF9g0Hd-Ig1Q)  
  <sub>4 hours ago</sub>  
  Procter & Gamble Company has an average rating of overweight and mean price target of $174.57, according to analysts polled by FactSet.
- [PG Nov 2026 148.000 put (PG261120P00148000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScgHEIkXXpiQbPrDKdLgyF-mtf63AM7J4qRdl1FWOVBGjSax1qexV0Tv9xoJQ4CqDdYvjQNu0mC3FZO2OpB9zHMEiYOa5KHJYkfU53TBEXsaekhoamp-pfFiqOrLeuG0SRwuqMs-bobtEfB5VVUvxZkE7jw&gsessionid=WbiCRtSCe6dOs7kvXKDhaV0GmrEK26OCAoOQmUBZS3FF9g0Hd-Ig1Q)  
  <sub>21 hours ago</sub>  
  Find the latest PG Nov 2026 148.000 put (PG261120P00148000) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 172.44 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 164.14 (+5.1%), 50d 154.78 (+11.4%), 200d 149.98 (+15.0%); 50d above 200d
Momentum: RSI(14) 71.5 | MACD 4.433 vs signal 4.111 (histogram 0.322)
Returns: 1d +1.6% | 5d +2.4% | 1m +8.2% | 3m +20.2%
52-week range: 138.04 - 172.44 (now 100.0% of the way up)
Volatility: ATR(14) 3.28 (1.9% of price) | annualised 20d 28.8%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 399.68B
Valuation: trailing P/E 25.97 | forward P/E 23.31 | P/B 7.35 | PEG 4.36
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
Price target: mean 174.04 (+0.9% vs last close), range 151.00 - 190.00
Recent rating changes:
  - 2026-10-26 Barclays: main, Equal-Weight -> Equal-Weight
  - 2026-10-26 Piper Sandler: main, Neutral -> Neutral
  - 2026-10-23 Freedom Broker: up, Hold -> Buy
  - 2026-10-23 UBS: main, Buy -> Buy
  - 2026-10-23 Citigroup: main, Buy -> Buy
  - 2026-10-23 BNP Paribas: main, Outperform -> Outperform
Institutional ownership: 71.9%
Largest holders: Blackrock Inc. (8.4%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.4%), Geode Capital Management, LLC (2.9%), Vanguard Portfolio Management LLC (2.8%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 322,138 shares in 48 transaction(s) | sold 233,622 shares in 27
Net: +88,516 shares (+1.4% of insider holdings) | insiders hold 6,373,903 shares
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

- [Sun Life Financial Inc. (SLF) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/SLF/)  
  <sub>Yahoo! Finance Canada, 3 hours ago</sub>  
  Find the latest Sun Life Financial Inc. (SLF) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [What Canada’s new real-time payment system means for the banks, your wages and your cheque book](https://ca.finance.yahoo.com/news/canada-real-time-payment-system-114746593.html)  
  <sub>Yahoo! Finance Canada, 3 hours ago</sub>  
  The payment system, which launched on Monday with select financial institutions, is run by Payments Canada.
- [(RY) Strategic Equity Report (RY:CA)](https://www.google.com/goto?url=CAESkQEBxCJF10N35ZefUrE7oYLPlFAhTDQLWVl6jYfx96VL-uRrFeVnty-wIc_sTgy1YXThr5p2KkV9X8EhQ14DW81x-tpHMNLj-8RVewwW16c4yMcUglA2uiyoQ592BhjnUGsZYatQvgJycNrxi_W899LJb6cHxtuBF4pR7YS_0Oi2nJ_EpaVQNFDc_O1fXfLB8XQE&gsessionid=0biHl0Cb0IdWzZQaLiSHO_-o5U72vl5nZMuZhbKbOujrd983siwEHw)  
  <sub>Stock Traders Daily, 14 hours ago</sub>  
  Strategic Equity Report for Royal Bank of Canada (RY) with Trading Signals.
- [Royal Bank Of Canada $RY Shares Acquired by Alberta Investment Management Corp](https://www.google.com/goto?url=CAESyAEBxCJF120LO0eG3Z9GzQ6k5K8wWcsRp1BQ8WLiPvH29ZOg2NdysEihk2yZzmsFVOfuwlNXZMkwu6hTEcvdLvwjJgwvDR1Lk2Z7FIOJnniTpdDaweaW8-C6boeQHAf5IbqNJUKqb2ds6rFpXVl_KTpGAHMbUwCQg8aqkA6njKRjSq7EpWvXu8uVBGuD17q-tp5yIcnAAIgUKoVFMfuMqSg3krfCHwj3E6gpbDeyQJUtQ2VqoqTUGFJ0s3vfSih9Hdj69Uk745yy9A&gsessionid=0biHl0Cb0IdWzZQaLiSHO_-o5U72vl5nZMuZhbKbOujrd983siwEHw)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Alberta Investment Management Corp raised its stake in shares of Royal Bank Of Canada (NYSE:RY - Free Report) (TSE:RY) by 49.8% during the 3rd quarter,...
- [Royal Bank of Canada (TSX:RY) Sees Active Share Turnover as Investors Assess Market Participation](https://www.google.com/goto?url=CAESvgEBxCJF14bxOKTkK0N1W66Cunb5m4OfDUeafENqi86RewBnqXIuqqwfxTCttM_tw0eCyl283FhPWUwAvJu_ye9MoMe3oy5iGHzYhqLPPFO4h3EV7D8PslAg3HSLmZXL4NKDRP-nGOzmUSUqWlgPhHzkLQ8xZ5h3ZtjFd5sVIwaIGaWR51BJB9w412JIuub19WrsDQ25vFRUx8ZZuc5Lo1biHC9C7MhRzOxlGjHt6BKbg3XhGdI-nfKX-ZH_lfya&gsessionid=0biHl0Cb0IdWzZQaLiSHO_-o5U72vl5nZMuZhbKbOujrd983siwEHw)  
  <sub>kalkine.ca, 3 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [RY Jan 2029 180.000 call (RY290119C00180000) stock price, news, quote and history](https://www.google.com/goto?url=CAEScgHEIkXXBybmvjjC2IwyBIkSl6oPKd7V1Fg_pDcGPrDgr5Qd0DwVsvAV4W3OVNJFoG1FFL7jnzly01d8R5ZkFyEPZ9mamrfbbCgxdKqSenBr_iPSmioAFyHHwLcXCrBJpIIP9fECo5ItIcGC9etliOD5gw&gsessionid=0biHl0Cb0IdWzZQaLiSHO_-o5U72vl5nZMuZhbKbOujrd983siwEHw)  
  <sub>Yahoo Finance UK, 19 hours ago</sub>  
  Find the latest RY Jan 2029 180.000 call (RY290119C00180000) stock quote, history, news and other vital information to help you with your stock trading and...
- [RY DCF Analysis: Intrinsic Value $162 vs Price $202](https://www.google.com/goto?url=CAESlAEBxCJF14wlfiTP0kIKAoI1ep3dW-_IEG042PWtDKXJVRQH4RLAGaAxuocjwUbk0vhYQWzQMcmM-G5-0YyryiJqoPMNzUTiPMFxM4EqEfrBTTGrxvCxAmZXva3HWH2xHHed38pjeW4y1fReFHmcmPr937pPgjOwggUrelsinNokJQlpoR8KT5jUhCuMOBnJb8GV2Z1P&gsessionid=0biHl0Cb0IdWzZQaLiSHO_-o5U72vl5nZMuZhbKbOujrd983siwEHw)  
  <sub>GuruFocus, 2 hours ago</sub>  
  On November 16, 2026, we delve into the DCF analysis for Royal Bank of Canada (RY), a stock that has shown impressive price performance with a year-to-date...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 202.11 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 203.18 (-0.5%), 50d 200.92 (+0.6%), 200d 191.17 (+5.7%); 50d above 200d
Momentum: RSI(14) 50.0 | MACD 0.726 vs signal 0.966 (histogram -0.240)
Returns: 1d -0.1% | 5d -1.0% | 1m +2.2% | 3m -5.1%
52-week range: 146.56 - 217.87 (now 77.9% of the way up)
Volatility: ATR(14) 3.14 (1.6% of price) | annualised 20d 20.3%
Volume: 0.01x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 279.80B
Valuation: trailing P/E 17.67 | forward P/E 15.86 | P/B 2.93 | PEG 1.93
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
Price target: mean 208.54 (+3.2% vs last close), range 182.01 - 229.37
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
Net: +0 shares | insiders hold 498,394 shares
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

- [U.S. FDA Approves IGALMI® as First At-Home Acute Treatment for Agitation Associated with Schizophrenia, Schizoaffective Disorder, or Bipolar I or II Disorder in Adults](https://finance.yahoo.com/healthcare/articles/u-fda-approves-igalmi-first-130000462.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>
- [US FDA approves at-home use of BioXcel's agitation drug](https://www.reuters.com/legal/litigation/us-fda-approves-at-home-use-bioxcels-agitation-drug-2026-11-16/)  
  <sub>Reuters, 22 minutes ago</sub>  
  The US Food and Drug Administration on Monday approved at-home use of BioXcel Therapeutics' drug, Igalmi, ​for agitation associated with schizophrenia or...
- [FDA Approves Igalmi for Agitation Associated With Schizophrenia, Schizoaffective Disorder, or Bipolar I or II Disorder](https://www.google.com/goto?url=CAES2AEBxCJF19WZQKOmjgVYYPmxjni22n16KTEpxisQSZTw8WdMqxZHyzeZOeyGPDbsMh5ygcrysRL-cHCFaaHKGGpHfveYgV68RWOy76zotTq-OHH9sOt07UyhpRDGYE9k8M1dvC4Lmx5FbAm5o06ULbkKyMdo6U1Y0ToljZ3kRK7FjaaV8Ie701HYqeOQC6pdd2NGV9_pIoluoFtzEb9j1zD_sTYiR5s9QHrKcA8PU2A4qlnR-h5QvGunq05AFezbUjEAJWnqEfVU2sdOlms1m2Gdv9-SAzi0AeE&gsessionid=_xnvitBU5MXgTL7CosSlH7VI9gssW8hzJjVvajuSnRKCOWddzCAesA)  
  <sub>Psychiatric Times, 14 minutes ago</sub>  
  The US Food and Drug Administration (FDA) today approved Teva Pharmaceuticals' dexmedetomidine (Igalmi) sublingual film for at-home use.
- [FDA Expands Dexmedetomidine for At-Home Use](https://www.google.com/goto?url=CAESiAEBxCJF15uyr2laQ2xh9_6820Hmn08SFycu3TAuS4kesebP4DkOI7pco17eHJ77_u3C8B4ONjoqKAIvM8FQ-PaeZgl9pkqkCqrS0hRIE12Tcq2r0KnBQnROVB9C0rh000Gq6OS7Eyr36Nhx_Wz1Q42ShpuMY2aOsE1hzzt56NmoQn-hyXbcs_Rl&gsessionid=_xnvitBU5MXgTL7CosSlH7VI9gssW8hzJjVvajuSnRKCOWddzCAesA)  
  <sub>Drug Topics, 56 minutes ago</sub>  
  For patients with schizophrenia or bipolar I or II disorder, dexmedetomidine use will no longer require provider supervision.
- [FDA Approval for LAMOTRIGINE issued to ACTAVIS ELIZABETH](https://www.google.com/goto?url=CAESnAEBxCJF1_0i0_vX9w1NChzEjK2gf1B9-XXi6o9MzySGcsJmsYYm19LcqE2gQGmj5mSe4pMGhraZzyAHFTaNvufVni64k8rFXlnCu_frhJGBib8PZxbtYQ9d4pTXehRky48lJ7aHtVb59bYUjqJwPQdJ8b7hC4ROlXwE5vFw5jFVDSJHCKZOAopZtT6Cie86L2EXZTBMERpXVLm2sB4&gsessionid=_xnvitBU5MXgTL7CosSlH7VI9gssW8hzJjVvajuSnRKCOWddzCAesA)  
  <sub>Quantisnow, 3 hours ago</sub>  
  Submission status for ACTAVIS ELIZABETH's drug LAMOTRIGINE (SUPPL-18) with active ingredient LAMOTRIGINE has changed to 'Approval' on 11/05/2026.
- [Teva Pharmaceutical Industries Ltd. $TEVA Stock Sold by William Blair Investment Management LLC](https://www.google.com/goto?url=CAES2AEBxCJF1-9IQgshMmTkqhp9pLr9H1QjMi0HFBGJx9w4bkfladufkqZ2Kxs4z8lbs6psRkrwuX-1G7URTNWbAJa3N84Dv6QLgsZARWScI5nikzgBi26w0j0s5LyYwkIt0pCp6_hZfjSbDl-qnMcm8gnlJHkcXCRzyGed7eUiM0mD-ATq_rCKS6C_-n9z861Np5R0MNkXEqiYGVQiNrzWTobok35QBOPa1V5pMINo6RpwtiCEgBXUFzCj_F6cULg_RHy8WPSR5k-CZrTwzf-gNIdzvEKAipauDh0&gsessionid=_xnvitBU5MXgTL7CosSlH7VI9gssW8hzJjVvajuSnRKCOWddzCAesA)  
  <sub>MarketBeat, 1 hour ago</sub>  
  William Blair Investment Management LLC cut its stake in Teva Pharmaceutical Industries Ltd. (NYSE:TEVA - Free Report) by 7.2% in the third quarter,...
- [MedinCell at Jefferies Global Healthcare Conference: royalty growth takes center stage](https://www.google.com/goto?url=CAES0AEBxCJF19ZGQJwC7YLZvDplAT5gw3cvyeQYQNTfXfMSf4KIJ3nGYFniET0kJloUUkEsXANKmYwSCHlN92uaOmngTB6juXEIdwJjyJ89IAJ--i4GaPOpCjYbrB-jV7ZBKVyZIbch3GUB5uJvrN5JRCKD8xFqs-HTAM1X-SEMMM-kv9UK2viofLuV_fYy0DTQqfcr6_k_ej-jfzX4CXKvKBXfJ8sHwOn3H9jTY_NTgNaB70FDZn2QV0EThF9HIeJlLqU99AMKUW_-JDn3MPnAYgQp&gsessionid=_xnvitBU5MXgTL7CosSlH7VI9gssW8hzJjVvajuSnRKCOWddzCAesA)  
  <sub>Investing.com Canada, 4 hours ago</sub>  
  MedinCell (MEDCL) used Monday, 16 November 2026, at the Jefferies Global Healthcare Conference to outline a clear strategic shift: the company is moving...
- [Teva Pharmaceutical Industries Ltd. $TEVA Stock Purchased by Migdal Insurance & Financial Holdings Ltd.](https://www.google.com/goto?url=CAES3QEBxCJF17ww_ziyDeX2WO2Lg_q6gkpcLNDQrI0VmVP6AEhPUzgJvMdFurG7BkB2tOsHFZSUpMS30yM-G-HoCfodVym-WeEolJWZMaHp9HtGa2IRwADRxN98BPj6bB0nnQ0-3RXwClbC6FdGsSvLYD-x3Y0EOzkZnJhNDpLnLS0NtHNhUX_bkzggv1FqXCNmjeEpG90xnAm2iq-nzogbNna1ZQcphhOQSmRxpcxdh5tCQU8Yqq-A090ePpZ-EuWJ-Nygw9e97O1zL9_HsnZ6yWEbLjOCJzerno75u5ImqA&gsessionid=_xnvitBU5MXgTL7CosSlH7VI9gssW8hzJjVvajuSnRKCOWddzCAesA)  
  <sub>MarketBeat, 21 hours ago</sub>  
  Migdal Insurance & Financial Holdings Ltd. increased its stake in shares of Teva Pharmaceutical Industries Ltd. (NYSE:TEVA - Free Report) by 1.3% during the...
- [Alvotech (NASDAQ:ALVO) Stock Moved Up to Hold by Wall Street Zen](https://www.google.com/goto?url=CAESuQEBxCJF18h9XHHXSfnkliaaGE3C28DL7SySSJ1MmzIBVDlA0xrF99ZT3ih8GCPFBru6vd7wCp_BQnyXFBWiBnqBdecj2e_MwHFXbw_oXLGKaPKWsUtmL-SOQZ4mCkkCAluQh2_I_N5y_o_OPP68_frq9J1mk2hMv-h6_lrNDpK0fc32ENofzqaeW2U6u7sfJ1V5yZT-nxsdCH3MzgORV_rAtr43RVWOBvahAMIJpBnoPbR-UKN3pVWdHw&gsessionid=_xnvitBU5MXgTL7CosSlH7VI9gssW8hzJjVvajuSnRKCOWddzCAesA)  
  <sub>MarketBeat, 23 hours ago</sub>  
  Wall Street Zen raised Alvotech from a "sell" rating to a "hold" rating in a research note on Sunday.
- [Teva Pharmaceutical Industries stock: TD Cowen keeps Buy rating](https://www.google.com/goto?url=CAESugEBxCJF1yf3Za3asYmviSNWlT9L46x5769CiD2-0QqGK3BnwCyrNuFwYxdNd0xrXDozVaGP0DedzyAi2CJfuJY3oOPaz_iHsC89zn5WSUCTT_3Y8TMSXlLFVHK4ZPWspG6qheM48UwJXFv_daqM5882hx1xgVPMw4bAcRExFr2XCA1X0ydP_1EyUNfsJiYsMCcT_E4SXq6fcbZyxO4xS_GgMwl__Y8BRq5P4vBtWEcDBdoi2T6ygPnSmrs&gsessionid=_xnvitBU5MXgTL7CosSlH7VI9gssW8hzJjVvajuSnRKCOWddzCAesA)  
  <sub>ad-hoc-news.de, 5 hours ago</sub>  
  Teva Pharmaceutical Industries stock drew a reiterated Buy rating from TD Cowen. The analyst set a USD 57 target, while TipRanks cited a Strong Buy...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 44.22 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 41.74 (+5.9%), 50d 40.34 (+9.6%), 200d 35.15 (+25.8%); 50d above 200d
Momentum: RSI(14) 66.7 | MACD 1.070 vs signal 0.844 (histogram 0.226)
Returns: 1d -0.6% | 5d +2.9% | 1m +6.5% | 3m +20.9%
52-week range: 24.21 - 44.50 (now 98.6% of the way up)
Volatility: ATR(14) 1.16 (2.6% of price) | annualised 20d 28.1%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 51.59B
Valuation: trailing P/E 102.83 | forward P/E 14.16 | P/B 6.47 | PEG 0.71
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
Price target: mean 50.29 (+13.7% vs last close), range 42.12 - 57.00
Recent rating changes:
  - 2026-11-12 Piper Sandler: main, Overweight -> Overweight
  - 2026-11-05 Leerink Partners: main, Outperform -> Outperform
  - 2026-11-04 TD Cowen: main, Buy -> Buy
  - 2026-11-04 HC Wainwright & Co.: main, Buy -> Buy
  - 2026-11-02 HC Wainwright & Co.: init, ? -> Buy
  - 2026-10-15 Barclays: main, Overweight -> Overweight
Institutional ownership: 58.9%
Largest holders: Blackrock Inc. (5.4%), Phoenix Financial Ltd. (3.6%), WCM Investment Management, LLC (3.6%), Clal Insurance Enterprises Holdings Ltd (3.6%), Menora Mivtachim Holdings Ltd. (3.4%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 43,476 shares in 3 transaction(s) | sold 29,021 shares in 4
Net: +14,455 shares (+0.2% of insider holdings) | insiders hold 7,362,676 shares
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

- [Toyota Motor (TSE:7203) Plans 400,000 Robots Across Its Global Factories](https://finance.yahoo.com/technology/articles/toyota-motor-tse-7203-plans-200549244.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Toyota Motor (TSE:7203) outlined a multiyear, multibillion plan to overhaul its global factories with expanded robotics and software.
- [Pony.ai, Toyota roll out fully driverless robotaxis in Guangzhou (PONY:NASDAQ)](https://seekingalpha.com/news/4672829-ponyai-toyota-roll-out-fully-driverless-robotaxis-in-guangzhou)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  Pony AI (PONY) and Toyota Motor (TM) have launched fully driverless commercial robotaxi services in Guangzhou, China, using their jointly developed...
- [(HBND) Equity Trading Insights (HBND:CA)](https://www.google.com/goto?url=CAESkwEBxCJF10RnzgCDv5If1ZCR1ba2CbfpeISxiTpKi0TjVis0gvZiiKEiOtWxSe5stpY-qMzj7PA1DwolfLaarqxZpVr8vJ6a4mAgaNC_PYoei4SvItSV_6tQd9N-Nj2ii5hCy17Bmm4ERXcFErxNWsFiVfJhqu_DLVLzxI_yqmWLV5A559J2Ds0lGWm9jrVvHJk_E6E&gsessionid=uB3nJPUq8dcs9V4Q6IT4y8F2pnSxjKM1uB6LbEwDwUiYcE5TZC_MQA)  
  <sub>Stock Traders Daily, 3 hours ago</sub>  
  Equity Trading Insights for Hamilton U.S. Bond YIELD MAXIMIZER TM ETF (HBND) Featuring Key Buy and Sell Signals.
- [One Netlist design reuses existing computer memory; another aims to protect data if power fails.](https://www.google.com/goto?url=CAEStwEBxCJF1_RasQGp5EThVgpxXi_gVEKKxceNzUeoOfassNgVDVmjP9OZHjilRhCFPctwjKUIIvaW-DKUYg-vBzeYudUNPaDBDW_iA8zR9DDxLPs_nD1Ma8TLaeqlZGKVjuklYdnsBzQHiN5oVDpbBA7q3eaDBzY4JKwlBipUMKaMqkhdIbwvtJxaEbhx3VJex18hgviv9OG0uzaGaFnG-17YeanbmOmf90ep20pyVdlgk3uw3_LQ-nY&gsessionid=uB3nJPUq8dcs9V4Q6IT4y8F2pnSxjKM1uB6LbEwDwUiYcE5TZC_MQA)  
  <sub>Stock Titan, 2 hours ago</sub>  
  The concepts target AI cache, databases and virtual machines. Netlist will show them Nov. 17–19 at Booth 1218; they are not generally available products.
- [Sell Alert: 5 Stocks Analysts Downgraded on Thursday](https://www.google.com/goto?url=CAESigEBxCJF1_i4K368DfqqVGN0TD-wIq33W1oyxjrOCUI4xAuOmoKrdiu_1V_guM37Vtenvf51eSXa8FHZHim2mYFOn6fR28NmKP3-digFlPjP0nKs-VAW4vm44zKhThzm4aGdfmy9ntaBV8sAwTrjzJhYqTYfK_LH1CBU4o9S1SADJw6K3rFTgqYQhBw&gsessionid=uB3nJPUq8dcs9V4Q6IT4y8F2pnSxjKM1uB6LbEwDwUiYcE5TZC_MQA)  
  <sub>Yahoo Finance UK, 12 hours ago</sub>  
  Chip stocks took the hardest hit on November 5, when the Philadelphia Semiconductor Index slumped 12.2%, its biggest one-day drop since April 2025.
- [Sensex Today Ends 318 Points Higher | Nifty Above 25,200 | BSE Insurance Index Up 1.15%](https://www.google.com/goto?url=CAESzQEBxCJF1_2EZgZAnPxAEmcE5nA2RXP-YEV_3To709k7GsfsYx6qDoDN_6p14Eaj33Hv6h4QG4xYMmwIqCxIuEN49YW5fK4JrsXJ4GALsr5D6K6mcFX4E5XHsD3W21WYiVrZwT9Za41pflXvundnIZYeiiwJXQAlM15noYYzI8mLgvEgt9l3_VSEgsqQiluQWK4lJ7oNgQGgZjWV8GtePkQ0oJ1_khaLPW_NOx_W37-k1Ao8010fTtcaHUObLuBEcO3MfB89L2sTk1Q55UCk&gsessionid=uB3nJPUq8dcs9V4Q6IT4y8F2pnSxjKM1uB6LbEwDwUiYcE5TZC_MQA)  
  <sub>Equitymaster, 4 hours ago</sub>  
  The BSE Sensex ends 312 points higher, while Nifty ended 75 points higher, up at 25220.
- [FDA Clears MiniMed Fit™ -- World's First and Only Tubeless Insulin Pump with Up to Seven-Day Wear and Zero Interruptions](https://www.google.com/goto?url=CAEStgEBxCJF17XZ4zSYyPhRGgu8TIIlDcoJVKMBKSpD372ThkxBn-DQRQe_3vp_ZugwYLq70ukdbVbD0yahdpA_jd7-Z7wUX8z4ZBKnEymx8XSeFqxWamw3K5AtaAzT8y1_WjiflMkIWztUfoCpJCmYFfFg6N5N-KE5wse-oMqBLoLGR2OmZz2UloWC0ZZBQqoJGlsiBMILsSDe6BQ32v0pXG-yghNDzO7L2DOp70EEqqVunbiflykcCA&gsessionid=uB3nJPUq8dcs9V4Q6IT4y8F2pnSxjKM1uB6LbEwDwUiYcE5TZC_MQA)  
  <sub>Stock Titan, 38 minutes ago</sub>  
  MiniMed (Nasdaq: MMED) received FDA clearance for MiniMed Fit, its first tubeless insulin pump, for people with diabetes ages 7 and older.
- [Sensex Today Trades Higher | Nifty Above 25,200 | Asian Paints & Bharti Airtel Top Gainers](https://www.google.com/goto?url=CAES0QEBxCJF10AuKbeQevFgZIunLmWQPVFfG2W0zslUfpvZTcr82ibsM9gLFybMFWHcVhlDwpu0t010oCfnO2UVQzs9rmWhvN7MIpgZbZZYHVGtZgtinbHQZyuevaL0i8U0cPDyiS957_Ud9_yPLEerPtTbORn0PVhA3xDvIPc1eu3BfKAKb61_9wy0K_ALgtIjVHVPcFGScaXKK2-S3d6j6sCYVXdI0tHbJhGib4s8vV6SeUZPubyqooxlhwda_69u951l3tBWjUZ9kZqjpN5CrGvCrw&gsessionid=uB3nJPUq8dcs9V4Q6IT4y8F2pnSxjKM1uB6LbEwDwUiYcE5TZC_MQA)  
  <sub>Equitymaster, 10 hours ago</sub>  
  Indian share markets are trading higher with Sensex trading 416 points higher, and Nifty is trading 95 points higher.
- [Turtlemint Q2 FY27 Results | Oil India Q2 FY27 Results | Top Buzzing Stocks Today](https://www.google.com/goto?url=CAESygEBxCJF10ywdCMVgZAMlVFbOwbv5YMnZl6nIPluOiPq-u7iMYTo9E_OpiB6FePrMB8reSDL-M7LDM1KyThP2kgShyA_TGQI0mqq7KufnERCltsqz1dO2eOQbZDBvzbPkRRNdhcIReDXOMHWJ3eGLtn9YcxePSUNGFg71JBGY08Md0fIrf2nJ-znSphgw_4XEwGHMDFpED1Y60XQ862gkk3kczNCqBFINmZ3jzHHOK_Fx5OG5Zec_gli-sDp_oTvJ9wEWJG9fFD_l8GO&gsessionid=uB3nJPUq8dcs9V4Q6IT4y8F2pnSxjKM1uB6LbEwDwUiYcE5TZC_MQA)  
  <sub>Equitymaster, 14 hours ago</sub>  
  The benchmark indices opened on a negative note but remained volatile throughout the session, eventually closing almost red on Friday.
- [Rivian may have an unexpected solution to high car prices](https://www.google.com/goto?url=CAESoQEBxCJF1ytTSsXWh2HuZS2dg9aiRS6Jw2e4CV7jX_MqF5yIcOam5qEAgFv2BHuNuMJM-EFSuGJvPC4wZxdVUuiKIXXylX-xWf8SyB5yUB64TOWgGBgHADBZQgZvopaqjx6tGL7kN1aavXnhf_7C9gIFq3tK76aHFF14yj0EHZAMom6qRQ21tVsnlzzEkcGizR8txqemdwOwVNWm5LeCLZqNXQ&gsessionid=uB3nJPUq8dcs9V4Q6IT4y8F2pnSxjKM1uB6LbEwDwUiYcE5TZC_MQA)  
  <sub>TheStreet, 5 hours ago</sub>  
  Rivian spinoff Also is shipping a $3500 electric bike aimed at drivers priced out of a $51000 car market. Here's what it means for RIVN investors.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 214.08 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 203.64 (+5.1%), 50d 195.16 (+9.7%), 200d 197.83 (+8.2%); 50d below 200d
Momentum: RSI(14) 64.7 | MACD 6.018 vs signal 5.137 (histogram 0.882)
Returns: 1d +0.8% | 5d -2.0% | 1m +10.0% | 3m +13.7%
52-week range: 166.50 - 248.29 (now 58.2% of the way up)
Volatility: ATR(14) 4.53 (2.1% of price) | annualised 20d 38.8%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 251.25B
Valuation: trailing P/E 9.76 | forward P/E 13.57 | P/B 17.04 | PEG 19.89
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
Price target: mean 238.08 (+11.2% vs last close), range 230.00 - 253.00
Recent rating changes:
  - 2026-11-12 Freedom Broker: down, Buy -> Hold
  - 2025-11-07 Freedom Broker: down, Buy -> Hold
  - 2025-02-04 Macquarie: up, Neutral -> Outperform
  - 2024-06-14 Erste Group: down, Buy -> Hold
  - 2023-07-11 Morgan Stanley: down, Overweight -> Equal-Weight
  - 2022-10-06 UBS: down, Buy -> Neutral
Institutional ownership: 2.4%
Largest holders: Fisher Asset Management, LLC (0.5%), Morgan Stanley (0.2%), FMR, LLC (0.1%), Goldman Sachs Group Inc (0.1%), Northern Trust Corporation (0.1%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 1,319,163 shares
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

> Neutral outlook – no material macro surprise, flat fund flows, and no analyst rating; technicals show downtrend but no decisive break.

**Main reasons it gave:**
- Yield curve remains upward sloping (+1.00 points) – no inversion
- US dollar index up 1.86% on the week
- RSI(14) at 31.5 – oversold but no decisive technical break
- Fund flows flat (share count change +0.0% over 1 week)
- Analyst view provides no rating (no buy/hold/sell) – neutral

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 26.36 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 26.91 (-2.0%), 50d 27.88 (-5.4%), 200d 27.40 (-3.8%); 50d above 200d
Momentum: RSI(14) 31.5 | MACD -0.488 vs signal -0.495 (histogram 0.007)
Returns: 1d -0.7% | 5d +1.0% | 1m -6.6% | 3m -5.9%
52-week range: 25.44 - 29.49 (now 22.8% of the way up)
Volatility: ATR(14) 0.24 (0.9% of price) | annualised 20d 9.3%
Volume: 0.05x the 20-day average
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
Three-year record: +10.2% a year | beta to the market 0.37
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
Shares outstanding: 27.60M | fund size: 727.67M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Most dimensions point to a neutral outlook: technicals are bearish, macro conditions are unfavourable for emerging‑market bonds, but fund flows are positive and fundamentals are modestly attractive. No material policy surprise or decisive technical break occurred, so the overall call remains neutral.

**Main reasons it gave:**
- Positive fund flows: +0.5% share count in 1 week and +4.3% in 1 month
- Technical indicators bearish: price below 20‑day, 50‑day, 200‑day SMAs; RSI 41.2; MACD negative
- Macro environment bearish for bonds: rising Treasury yields and elevated inflation

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 91.02 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 91.77 (-0.8%), 50d 91.95 (-1.0%), 200d 94.70 (-3.9%); 50d below 200d
Momentum: RSI(14) 41.2 | MACD -0.117 vs signal -0.053 (histogram -0.064)
Returns: 1d -0.1% | 5d -1.6% | 1m -0.5% | 3m -3.8%
52-week range: 90.14 - 97.74 (now 11.6% of the way up)
Volatility: ATR(14) 0.48 (0.5% of price) | annualised 20d 7.1%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.5% (67.58M) over 7d | 1 month: +4.3% (553.65M) over 30d
Shares outstanding: 148.29M | fund size: 13.50B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error response body was rejected) (Bing's feed, direct: 2 headline(s), none naming EMB)

### US company bonds, riskier (HYG) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Net inflows: share count up 5.6% over the past month
- US Treasury yields rose (10‑year +0.27% week) increasing discount rates for high‑yield bonds
- Technical indicators weak: price below 20‑day, 50‑day, 200‑day SMAs; RSI 42.4; low volume

<details><summary><b>News</b> — score +0.00</summary>

- [iShares iBoxx $ High Yield Corporate Bond ETF (HYG)](https://ca.finance.yahoo.com/quote/HYG/options/?date=1807833600&straddle=false&type=all)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  View the basic HYG option chain and compare options of iShares iBoxx $ High Yield Corporate Bond ETF on Yahoo Finance.
- [CCC Bonds Could Be A Big Bargain In High-Yield Credit](https://www.dividend.com/fixed-income-channel/ccc-bonds-could-be-big-bargain-in-high-yield-credit/)  
  <sub>Dividend.com, 45 minutes ago</sub>  
  Despite ongoing bond market volatility, higher yields and diversified fixed-income strategies, including systematic investing and multi-sector ETFs,...
- [Higher rates burden Washington, not corporate America or households](https://www.google.com/goto?url=CAESpQEBxCJF15Hu13yksrzI3k-fLkdBH-LGNAVyNlGWT2oxq1m8acV673k_teels6QzBC8sUYIf0Nh9Qhtw5uA0sFWTZP-YEa3iwWj-LhhpW7qyX4kWcO3WuUy6X4AFvtfEAL3M8IvtP_fRf2W00r27IP1GBlbUjkXXO-SrO8ASCr44Gl-L0ZGm5j9cgggANwJwbO_AEZLUu4c_16ZjEfmVwoxPt7UjTsQ&gsessionid=z5G8y7p57Qi2blO0CoIB8I6GuqtpVijjj4EJzhlI79zlqWqfD3H8vA)  
  <sub>Seeking Alpha, 31 minutes ago</sub>  
  Apollo Global Management's chief economist Torsten Slok highlights a striking divergence in how the recent monetary tightening cycle has played out across...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 76.92 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 77.21 (-0.4%), 50d 77.54 (-0.8%), 200d 79.31 (-3.0%); 50d below 200d
Momentum: RSI(14) 42.4 | MACD -0.123 vs signal -0.120 (histogram -0.003)
Returns: 1d -0.0% | 5d -0.8% | 1m +0.1% | 3m -3.3%
52-week range: 76.81 - 81.18 (now 2.5% of the way up)
Volatility: ATR(14) 0.30 (0.4% of price) | annualised 20d 5.3%
Volume: 0.02x the 20-day average
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
Three-year record: +7.5% a year | beta to the market 0.65
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.1% (9.91M) over 7d | 1 month: +5.6% (935.07M) over 32d
Shares outstanding: 229.98M | fund size: 17.69B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; macro and technical factors offset each other, with modest bearish pressure from rising yields and net short positioning but supportive fund inflows and high credit quality.

**Main reasons it gave:**
- 10-year Treasury yield rose 0.27% on the week, pressuring bond prices
- CFTC data shows large speculators net short 38% of open interest, change -0.2% week
- Price below 20‑day, 50‑day, and 200‑day SMAs; RSI 41.6; volume 0.05× 20‑day average
- Share count increased +2% weekly and +3.8% monthly, indicating net inflows
- Higher rates burden Washington (commentary) highlighting pressure on government bonds

<details><summary><b>News</b> — score +0.00</summary>

- [Top Tokenized ETFs by Market Cap](https://www.coingecko.com/en/etfs)  
  <sub>CoinGecko, 1 hour ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...
- [Higher rates burden Washington, not corporate America or households](https://seekingalpha.com/news/4673020-higher-rates-burden-washington-not-corporate-america-or-households)  
  <sub>Seeking Alpha, 30 minutes ago</sub>  
  Apollo Global Management's chief economist Torsten Slok highlights a striking divergence in how the recent monetary tightening cycle has played out across...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 90.19 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 91.06 (-1.0%), 50d 90.53 (-0.4%), 200d 93.60 (-3.6%); 50d below 200d
Momentum: RSI(14) 41.6 | MACD 0.002 vs signal 0.168 (histogram -0.166)
Returns: 1d +0.2% | 5d -1.8% | 1m -0.3% | 3m -3.0%
52-week range: 88.92 - 97.99 (now 14.0% of the way up)
Volatility: ATR(14) 0.47 (0.5% of price) | annualised 20d 7.2%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Long Government
Yield: 4.0%
Credit quality: AA 100.0% | US government debt 99.6%
Three-year record: +3.4% a year | beta to the market 1.17
Cost and size: expense ratio 0.15% | net assets 43.53B
What it is made of: Bonds 99.6%, Cash 0.4%
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
Share count change: 1 week: +2.0% (837.71M) over 7d | 1 month: +3.8% (1.57B) over 32d
Shares outstanding: 482.59M | fund size: 43.52B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material policy surprise, data release, or decisive technical break occurred. Rising yields are mildly negative for bonds, but strong inflows and solid fund fundamentals offset the technical weakness, leading to a neutral overall view.

**Main reasons it gave:**
- 10-year Treasury yield rose 27 bps this week
- LQD share count increased 12.4% over the past month
- ETF price below 20‑day, 50‑day, and 200‑day SMAs
- RSI at 40.7 and MACD negative, indicating weak momentum

<details><summary><b>News</b> — score +0.00</summary>

- [Higher rates burden Washington, not corporate America or households](https://seekingalpha.com/news/4673020-higher-rates-burden-washington-not-corporate-america-or-households)  
  <sub>Seeking Alpha, 31 minutes ago</sub>  
  Apollo Global Management's chief economist Torsten Slok highlights a striking divergence in how the recent monetary tightening cycle has played out across...
- [Which Bond ETF Is the Better Buy: Vanguard’s Total Bond Market BND or iShares’ Corporate IGIB?](https://www.fool.com/coverage/etfs/2026/11/15/which-bond-etf-is-the-better-buy-vanguard-s-total-bond-market-bnd-or-ishares-corporate-igib/)  
  <sub>The Motley Fool, 23 hours ago</sub>  
  One fund casts a wide net across government and corporate debt, while the other zeroes in on intermediate corporate bonds with a richer yield.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 102.93 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 103.89 (-0.9%), 50d 103.60 (-0.6%), 200d 107.31 (-4.1%); 50d below 200d
Momentum: RSI(14) 40.7 | MACD -0.067 vs signal 0.081 (histogram -0.148)
Returns: 1d +0.1% | 5d -1.7% | 1m -0.5% | 3m -2.7%
52-week range: 101.83 - 112.05 (now 10.8% of the way up)
Volatility: ATR(14) 0.57 (0.6% of price) | annualised 20d 7.1%
Volume: 0.02x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.40</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +1.5% (473.18M) over 7d | 1 month: +12.4% (3.54B) over 32d
Shares outstanding: 310.67M | fund size: 31.98B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, no decisive technical breakout, and mixed but modestly bearish signals from analysts, speculators, and recent outflows. The overall view remains neutral.

**Main reasons it gave:**
- Analyst coverage thin (1.4% weight) with weighted price target -6% relative to current price
- CFTC large speculators net short 18.7% of open interest, indicating bearish sentiment but not extreme
- Fund share count fell 2.6% in the past week, showing modest outflows
- Technical indicators show price near 52‑week high but RSI neutral (56.8) and low volume, no decisive breakout
- Macro data unchanged: Treasury yields rose modestly, curve remains upward sloping, VIX stable

<details><summary><b>News</b> — score +0.00</summary>

- [What Invesco S&P 500 Equal Weight ETF (RSP) Bought: Moderna Leads on Nov. 12](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afb16bea74440b5b26a9946794cec61&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2finvesco-p-500-equal-weight-110506567.html&c=12750909077701692829&mkt=en-us)  
  <sub>Yahoo Finance, 12h ago</sub>  
  Invesco S&P 500 Equal Weight ETF (RSP) is an Equity US fund in the Equity asset class holding 503 stocks, with just 2.7% of assets in its 10 largest holdings. Technology accounts for 16.6% of ...
- [Nvidia Crisis Sparks AI Bubble Fears as Markets Show Resilience](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afb16bea74440b5b26a9946794cec61&url=https%3a%2f%2faskfuzz.ai%2fdiscover%2fnews%2fglobal%2fmarkets-show-resilience-despite-nvidia-turmoil-and-ai-bubble-fears&c=14069961314013433881&mkt=en-us)  
  <sub>askfuzz.ai, 10h ago</sub>  
  Despite Nvidia's CEO Jensen Huang resigning amid scandal and the company losing $573 billion in market value, major US equity indices showed resilience with the S&P 500 posting its best week since ...
- [The Week Ahead – Have We Seen the Q4 Bottom?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afb16bea74440b5b26a9946794cec61&url=https%3a%2f%2fpro.thestreet.com%2fmarket-commentary%2fthe-week-ahead-have-we-seen-the-q4-bottom&c=11328770225143414314&mkt=en-us)  
  <sub>TheStreet Pro, 26h ago</sub>  
  Dip buyers powered the S&P 500 even as rate-hike bets nearly doubled. Now Nvidia’s first report under its interim CEO, retail sales, FOMC minutes and a score of Fed speakers put the rebound to the ...
- [【机构持仓】摩根士丹利美邦公司增持平均加权指数ETF-Rydex S&P](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afb16bea74440b5b26a9946794cec61&url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fusstock%2fnotice%2f2026-11-16%2fdoc-iniyxiri2824708.shtml&c=734196401775892614&mkt=en-us)  
  <sub>新浪财经, 14h ago</sub>  
  最新披露的机构持仓数据显示，摩根士丹利美邦公司于最新季度调整了对平均加权指数ETF-Rydex S&P（RSP）的持仓。 主要变动如下： 持仓变化：增持85.16万股 仓位变化幅度：3.06% 最新持股：2870.52万股 占公司流通股比例：6.05% 截至目前，公司共有3155家机构持股。 其中： 前20大机构合计持股1.81亿股，占总股本38.35%。 较上一季度提升1.03个百分点，机构持仓 ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 220.99 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 219.03 (+0.9%), 50d 215.02 (+2.8%), 200d 208.97 (+5.8%); 50d above 200d
Momentum: RSI(14) 56.8 | MACD 1.736 vs signal 1.625 (histogram 0.111)
Returns: 1d -0.1% | 5d +0.0% | 1m +3.2% | 3m +0.5%
52-week range: 182.18 - 223.33 (now 94.3% of the way up)
Volatility: ATR(14) 2.56 (1.2% of price) | annualised 20d 17.6%
Volume: 0.10x the 20-day average
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
Three-year record: +18.2% a year | beta to the market 0.80
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

<details><summary><b>What analysts and big funds say</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.20</summary>

```text
Rolled up from the 5 largest holdings, 1.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 38.4% | hold 61.6% | sell 0.0% (mean 2.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -6.0% above the current prices
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
Contract: E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 18.7% of open interest (1,986,532 contracts)
Change on the week: +1.7% of open interest
Crowding: 68% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: -2.6% (-2.66B) over 7d | 1 month: +0.3% (265.63M) over 32d
Shares outstanding: 452.10M | fund size: 99.91B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Treasury yields rose modestly this week (3‑month +0.10, 5‑year +0.30, 10‑year +0.27) but short‑term duration limits price impact
- CFTC data shows net short 32.5% of open interest with a -2.5% change, indicating modest bearish positioning but no extreme crowding
- Fund share count increased 0.6% over the week, indicating modest inflows but not a large shift
- Technical indicators (RSI 42.9, MACD slightly negative, price below 20‑day SMA) show slight bearish bias but no decisive break
- Macro data (inflation 3.7%, unemployment 4.1%) within expectations, no surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Higher rates burden Washington, not corporate America or households](https://seekingalpha.com/news/4673020-higher-rates-burden-washington-not-corporate-america-or-households)  
  <sub>Seeking Alpha, 30 minutes ago</sub>  
  Apollo Global Management's chief economist Torsten Slok highlights a striking divergence in how the recent monetary tightening cycle has played out across...
- [Top Tokenized ETFs by Market Cap](https://www.coingecko.com/en/etfs)  
  <sub>CoinGecko, 1 hour ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.22 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 81.44 (-0.3%), 50d 81.32 (-0.1%), 200d 82.03 (-1.0%); 50d below 200d
Momentum: RSI(14) 42.9 | MACD -0.027 vs signal 0.017 (histogram -0.043)
Returns: 1d +0.1% | 5d -0.4% | 1m -0.2% | 3m -1.0%
52-week range: 81.05 - 83.18 (now 8.2% of the way up)
Volatility: ATR(14) 0.13 (0.2% of price) | annualised 20d 2.4%
Volume: 0.08x the 20-day average
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
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 32.5% of open interest (4,464,182 contracts)
Change on the week: -2.5% of open interest
Crowding: 78% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.6% (171.34M) over 7d | 1 month: +4.4% (1.17B) over 32d
Shares outstanding: 338.19M | fund size: 27.47B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The macro environment shows modest yield increases and a slight bearish positioning, but no clear catalyst or decisive technical break justifies a directional bias.

**Main reasons it gave:**
- 10-year Treasury yield rose 27 bps this week, pressuring long bond prices
- CFTC data shows net short 33.3% of open interest, indicating bearish positioning
- Price below 20‑day, 50‑day, and 200‑day SMAs with RSI 40.2, showing slight bearish momentum
- Fund flows flat over the past month, no net inflow or outflow

<details><summary><b>News</b> — score +0.00</summary>

- [TLT 261116 74.00C (TLT261116C74000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/TLT261116C74000-US)  
  <sub>Moomoo, 4 hours ago</sub>  
  Options money in $iShares 20+ Year Treasury Bond ETF (TLT.US)$ : $20.6M calls vs $23.1M puts, $43.7M in all (53% puts). Heaviest bet: 5,910 put contracts...
- [Institutional Flow in iShares 20+ Year Treasury (TLT): 53% of the Options Money Is in Puts](https://www.moomoo.com/community/feed/institutional-flow-in-ishares-20-year-treasury-tlt-53-of-117624324751765)  
  <sub>Moomoo, 10 hours ago</sub>  
  Options money in $iShares 20+ Year Treasury Bond ETF (TLT.US)$ : $20.6M calls vs $23.1M puts, $43.7M in all (53% puts). Heaviest bet: 5910 put contra...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 79.50 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 81.09 (-2.0%), 50d 80.16 (-0.8%), 200d 84.25 (-5.6%); 50d below 200d
Momentum: RSI(14) 40.2 | MACD 0.002 vs signal 0.285 (histogram -0.283)
Returns: 1d +0.2% | 5d -3.0% | 1m -0.7% | 3m -2.6%
52-week range: 77.11 - 90.82 (now 17.5% of the way up)
Volatility: ATR(14) 0.76 (1.0% of price) | annualised 20d 12.2%
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
Three-year record: +0.9% a year | beta to the market 2.30
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
Shares outstanding: 109.70M | fund size: 8.72B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US dollar index up 1.86% on the week, no surprise macro data
- UUP price above 20‑day, 50‑day, 200‑day SMAs with RSI 69.7 but volume 0.07× 20‑day average
- CFTC data shows net long 6.7% of open interest, change +0.2% (modest bullish bias)
- Fund flows: 1‑week share count down 1.4% but 1‑month up 10.9% (mixed demand)

<details><summary><b>News</b> — score +0.00</summary>

- [UUP Mar 2027 34.000 put (UUP270319P00034000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/UUP270319P00034000/chart/)  
  <sub>Yahoo! Finance Canada, 10 hours ago</sub>  
  Interactive Chart for UUP Mar 2027 34.000 put (UUP270319P00034000), analyze all the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.52 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 29.09 (+1.5%), 50d 28.83 (+2.4%), 200d 28.05 (+5.3%); 50d above 200d
Momentum: RSI(14) 69.7 | MACD 0.155 vs signal 0.114 (histogram 0.042)
Returns: 1d +0.1% | 5d +1.9% | 1m +2.1% | 3m +4.9%
52-week range: 26.47 - 29.52 (now 100.0% of the way up)
Volatility: ATR(14) 0.12 (0.4% of price) | annualised 20d 5.5%
Volume: 0.07x the 20-day average
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
Three-year record: +4.4% a year | beta to the market -7.93
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
Share count change: 1 week: -1.4% (-7.03M) over 7d | 1 month: +10.9% (47.41M) over 30d
Shares outstanding: 16.41M | fund size: 484.32M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; mixed signals across dimensions.

**Main reasons it gave:**
- Analyst ratings: 85.7% buy, weighted price target +24.7% (thin coverage 12.1% of fund)
- Positioning: net short on MSCI EAFE futures fell by 2.8% of open interest (slight bullish shift)
- Fund flows: share count down 3.4% over past month (bearish outflows)
- Technicals: price above 20‑day, 50‑day, 200‑day SMAs and MACD positive, but volume at 0.05× 20‑day average

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 88.98 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 88.10 (+1.0%), 50d 87.89 (+1.2%), 200d 87.97 (+1.1%); 50d below 200d
Momentum: RSI(14) 53.9 | MACD 0.458 vs signal 0.306 (histogram 0.152)
Returns: 1d -0.1% | 5d -1.1% | 1m +1.9% | 3m -2.8%
52-week range: 77.90 - 93.19 (now 72.5% of the way up)
Volatility: ATR(14) 1.03 (1.2% of price) | annualised 20d 19.8%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

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
Rolled up from the 5 largest holdings, 12.1% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 85.7% | hold 14.3% | sell 0.0% (mean 2.04 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.7% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, SHEL.L, NOVN.SW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 2.6% of open interest (505,889 contracts)
Change on the week: -2.8% of open interest
Crowding: 22% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -0.5% (-195.70M) over 7d | 1 month: -3.4% (-1.32B) over 32d
Shares outstanding: 418.07M | fund size: 37.20B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error response body was rejected) (Bing's feed, direct: 2 headline(s), none naming VGK)

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US Treasury yields rose modestly across the curve (+0.10 to +0.30% weekly) with no policy surprise
- VWO price below 20‑day, 50‑day, and 200‑day SMAs (down 2‑5%) and RSI 39.6, indicating bearish momentum
- CFTC speculators net long only 1.1% of open interest, change +0.6%, low crowding (22% percentile)
- Analyst coverage thin (23.5% of fund) despite 100% buy rating and +61% price target
- Fund flows flat (0% change) over 1 month, indicating no net demand shift

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 55.27 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 56.39 (-2.0%), 50d 58.42 (-5.4%), 200d 58.29 (-5.2%); 50d above 200d
Momentum: RSI(14) 39.6 | MACD -0.700 vs signal -0.809 (histogram 0.109)
Returns: 1d -2.0% | 5d -2.4% | 1m -4.8% | 3m -7.3%
52-week range: 52.42 - 61.44 (now 31.6% of the way up)
Volatility: ATR(14) 0.91 (1.6% of price) | annualised 20d 23.8%
Volume: 0.05x the 20-day average
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
Three-year record: +15.8% a year | beta to the market 0.78
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 23.5% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.32 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +61.4% above the current prices
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
Shares outstanding: 1.42B | fund size: 78.38B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: the streamed answer ran past the 480s ceiling (gave up after 3 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 30.47 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 32.36 (-5.9%), 50d 32.71 (-6.9%), 200d 29.63 (+2.8%); 50d above 200d
Momentum: RSI(14) 27.5 | MACD -0.627 vs signal -0.378 (histogram -0.249)
Returns: 1d -1.1% | 5d -1.7% | 1m -9.7% | 3m -0.0%
52-week range: 22.36 - 34.10 (now 69.0% of the way up)
Volatility: ATR(14) 0.49 (1.6% of price) | annualised 20d 19.7%
Volume: 0.11x the 20-day average
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
Share count change: 1 week: +2.1% (38.93M) over 7d | 1 month: +8.6% (151.77M) over 32d
Shares outstanding: 62.93M | fund size: 1.92B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 429: {"error":{"message":"Model busy, retry later","type":"invalid_request_error","param":null,"code":"engine_overloaded"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Opinion: How to use options to bet against Big Tech, while keeping risk in check](https://www.marketwatch.com/story/how-to-use-options-to-bet-against-big-tech-while-keeping-risk-in-check-a2609641)  
  <sub>MarketWatch, 2 hours ago</sub>  
  One way to bet on the continued move away from Big Tech is by buying options that give you the right to both buy and sell certain market ETFs.
- [Real-Time Stock News, SEC Filings & Alerts](https://www.quantisnow.com/etfs)  
  <sub>Quantisnow, 12 hours ago</sub>  
  Browse US-listed exchange-traded funds A to Z, with latest price, daily change and one-year return. ETFs are funds, not companies.
- [How to Use Options to Bet Against Big Tech, While Keeping Risk in Check](https://www.google.com/goto?url=CAESmQEBxCJF15GJIHpY2fENdkv-m5TIyiuwhfwHtvhS8_NEM3wV-iXEu8RGbwSz2SMrLgVAS8Q7GCBeS1I6IqJestnqhE4LBJIe9wiU1M-jUAbTUtqE1TDdbD0mMIfvMFcRqLeNkJKkuDyz5KBZLIW9Yw69BwtS4aujW_bUSFFN6p0O4h_BWtT8TmG6DZzBmZZtBdrQ8_CStnm6x1I&gsessionid=impQ0keNsQPd-GRiIiGK4Tg5dQ5a90h92RNXDWi9VE-koClRQLCsuQ)  
  <sub>Moomoo, 1 hour ago</sub>  
  ByLawrence G. McMillan Buying call options on the S&P 500 equal-weight ETF while buying a put option on the S&P 500 ETF is one way to bet that Big Tech will...
- [IWMI: Option Layer Netted Zero, Now The Rate Test (BATS:IWMI)](https://www.google.com/goto?url=CAESlQEBxCJF17E3JOJtIF9onwM0vYbH7X6adyHJ2PtJbz_hT7ihECkk2V54y2YgQV9RSN0IK0NhEQFfUAWGgaU4SHijq29gMxvh0HvmdW-a5hsesSFScTyY0uQ4nluOHphar7nuyW2Ia30wDYKivhu3f5xBFcae3SjjBj_EiaBWJrpWAAyhFrbF1Rn7keDttbNULCkzAA9-ZQ&gsessionid=impQ0keNsQPd-GRiIiGK4Tg5dQ5a90h92RNXDWi9VE-koClRQLCsuQ)  
  <sub>Seeking Alpha, 44 minutes ago</sub>  
  Downgrade NEOS Russell 2000 High Income ETF (IWMI) to Sell from Hold; despite its roughly 11% gain since March, forward total returns look negative.
- [Top Tokenized ETFs by Market Cap](https://www.google.com/goto?url=CAESXgHEIkXXpm7_WLww8vIl8rwZoEXCv5J86nCliG_g2JnS_jFpCeP6kbY_aHGb673i-kmRQX1p7oK3NhHx55GZWpanxpvqYyW9zi8TML1d0IfKPnIzWQOBabQkg53PWpI&gsessionid=impQ0keNsQPd-GRiIiGK4Tg5dQ5a90h92RNXDWi9VE-koClRQLCsuQ)  
  <sub>CoinGecko, 1 hour ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...
- [Buy Year 3 Of The Presidential Cycle (NYSEARCA:SPY)](https://www.google.com/goto?url=CAESigEBxCJF1yJ74plnzSO9ImpWFNVbrcX7_1vFLRlwD5qrvG_VKra-f9xgm0O9Ckq7HHw4gSpeAvQF1I6-iooQWa4bJcmATUrqnGn7FTF5NMFv-jB_lzgQ_5NbouG_F--34S0QkOZwXGrJG4nMYLiTfKud5rFJ3Rf4PNQsc9qVo6MG8kPQn0o7cwS4Tw4&gsessionid=impQ0keNsQPd-GRiIiGK4Tg5dQ5a90h92RNXDWi9VE-koClRQLCsuQ)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Presidential third years averaged 21% S&P 500 total returns since 1949; the first six months averaged 12.6% across 18 observations.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 276.29 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 278.63 (-0.8%), 50d 280.37 (-1.5%), 200d 279.49 (-1.1%); 50d above 200d
Momentum: RSI(14) 46.3 | MACD -0.480 vs signal -0.592 (histogram 0.111)
Returns: 1d -0.5% | 5d -2.2% | 1m +2.2% | 3m -8.0%
52-week range: 229.11 - 305.09 (now 62.1% of the way up)
Volatility: ATR(14) 4.69 (1.7% of price) | annualised 20d 25.0%
Volume: 0.08x the 20-day average
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.48 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.2% above the current prices
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
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 12.3% of open interest (449,399 contracts)
Change on the week: -1.8% of open interest
Crowding: 67% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 281.05M | fund size: 77.65B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 429: {"error":{"message":"Model busy, retry later","type":"invalid_request_error","param":null,"code":"engine_overloaded"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Forget SCHD: These 3 Income ETFs Offer 12%+ Yields and Up to 30% Upside](https://www.tipranks.com/news/forget-schd-these-3-income-etfs-offer-12-yields-and-up-to-30-upside)  
  <sub>TipRanks, 57 minutes ago</sub>  
  The Schwab U.S. Dividend Equity ETF ($SCHD) remains a popular dividend ETF, thanks to its focus on high-quality companies and low fees.
- [SpaceX Stock Forecast: 2 ETFs to Capture SPCX’s 56% Upside Potential After Historic Starship Catch](https://www.tipranks.com/news/spacex-stock-2-etfs-to-consider)  
  <sub>TipRanks, 3 hours ago</sub>  
  SpaceX ($SPCX) remains a closely watched stock in the space sector, with analysts seeing about 56% upside over the next 12 months. The stock is drawing...
- [Can AI Review Your Investment Portfolio? What It Can and Can’t Tell You](https://www.google.com/goto?url=CAEShgEBxCJF10iCV1gYhWB1bu-IOcKLH1jb6JQilUafnde3spuyREKKx6asX_xfO2kpD_lzVXxeL0Lcd5D79K1YDjYntq_ELeyWzv1kdSRJdQI7nMUJyxTfeza75C35RtJaqpXgFSiR7Ws0hCiBMaJVXtsuMTeRv3cQNATr919HRfSeTOyljTI4fw&gsessionid=IvAF8U-Hn0ZSitdV7NhbeToNPbcsOwq_JSurPAYIEtQnwk_BwYbpAg)  
  <sub>Online Tech Tips, 23 hours ago</sub>  
  An AI portfolio review can check concentration, ETF overlap, and SEC filings. Learn where chatbots guess wrong and how to share your own holdings safely.
- [3 Nvidia-Heavy ETFs to Watch Ahead of Q3 Earnings – One Offers 55% Upside](https://www.google.com/goto?url=CAESoQEBxCJF18aLvkql-m7LHdK2Q0osc-blKNBfUjCtVOZow-N0CIAcSncCnUJsUkW-Vodi2BQzT9dTHJopnuwDt7uHw_YR4yHyy_uKh-10aLB2OPdVqQ1SAEvMuStumuuyCyJR51k6n3TXA2sP2NCHyR_L64KUlBguCOULB4RJAjNZYABPKAqqj40r8rFemdE6CBZ2S7PFgBsD-8TS32j0QpSLdQ&gsessionid=IvAF8U-Hn0ZSitdV7NhbeToNPbcsOwq_JSurPAYIEtQnwk_BwYbpAg)  
  <sub>TipRanks, 4 hours ago</sub>  
  Nvidia ($NVDA) will report its fiscal Q3 results on November 17. Analysts expect earnings per share to rise about 90% to $2.47, while revenue is forecast to...
- [Notable open interest changes for November 16th](https://www.google.com/goto?url=CAESngEBxCJF1zPZDof7VTDKyfWquy1ww3PdA2sVQWJL_pJrlP6fIeD1yy7qI4yEEqUQnJlgobK5okuiuosBpYPBy8JRY7sA_NFb0Co4mOceQG9K4A9TSuaFqX6EkE3aFclJ8mlAXlzRHc7N3BvVEqLoLYZL0IJYvOsUSE-MRvMCMgnNlmA9D8YRS-zWk4t9v7T0ermZZbIM0dgYTvxLp3DiOw&gsessionid=IvAF8U-Hn0ZSitdV7NhbeToNPbcsOwq_JSurPAYIEtQnwk_BwYbpAg)  
  <sub>TipRanks, 45 minutes ago</sub>  
  Friday's total option volume of 78.2 million contracts resulted in net open interest growth of 7.28 million calls and 4.88 million puts.
- [CCIAM Reports Poll Results From Further Adjourned AGM](https://www.google.com/goto?url=CAESpgEBxCJF1yyiCB_9rL1X6wgfJV81scK3wvLh6uHq9Uwuw4Lntb2hGnRlOXAqLazCZZGt2KoijffZe2sMMGaDPW2N8xpeYn-citIVYtWmptTh6wes2g17Ivw9Etu9d0w3s7GdVJhAraOUVtFnk4x0r87zWgyj6T9qvRptZy-PxsbBVRmOkPuBimxB00TiEk9m6s7X-8Y1OVr9EZ1ZyAYIQY7i4EM44lRM&gsessionid=IvAF8U-Hn0ZSitdV7NhbeToNPbcsOwq_JSurPAYIEtQnwk_BwYbpAg)  
  <sub>TipRanks, 49 minutes ago</sub>  
  CCIAM Future Energy Ltd. ( ($HK:0145) ) has provided an update. At the further adjourned annual general meeting held on 16 November 2026, CCIAM Future...
- [Bitfire Group Announces US$10 Million Bitcoin ETF Order](https://www.google.com/goto?url=CAESpwEBxCJF1yVchggEkOuD1nk-CZ5skT3gfndOyNx13RSBCTpb9cz-VlRLbyrtKYQVn1oARvLZwbeG7tlZWPVlub4MxWoLEUOkr9_1v1cMQGZsmG8C4IZgobA-B2DMdCryowO_GF5HO3wh3RiiFZeO5k8YPqvLEm78d78UFRz73y2N8lV2kaGmNr9zvo_wHSN78AwRVqWQgSyBtVQiFLy0-505Ai31bKa3Eg&gsessionid=IvAF8U-Hn0ZSitdV7NhbeToNPbcsOwq_JSurPAYIEtQnwk_BwYbpAg)  
  <sub>TipRanks, 4 hours ago</sub>  
  The latest announcement is out from New Huo Technology Holdings Limited ( ($HK:1611) ). Bitfire Group Holdings, formerly Sinohope Technology Holdings,...
- [Fidelity’s Ethereum ETF Feels a Small Outflow as ETH Technicals Turn Bearish](https://www.google.com/goto?url=CAEStwEBxCJF12yuMET8H5aciiHSbKI5GwrTwEqKEa1uiVTEjzNfj0PcRNOcAStBfzzXyNuPBKe8K4Yaiwi2glegysepzSyhJiZNraWAfwLdEXIstIDZIa9oQHUFvr2h0getKXQAAhT-bbMse40-KmzuIWfIIQEi2Hl-PkCG6B8riDb02wcZx5crC-nc_abeiIaIdHcIpiofBprJ_DHzOCjZuAnUUYb2eesgwMAzlxSBOOvYFNpIKIfBC-A&gsessionid=IvAF8U-Hn0ZSitdV7NhbeToNPbcsOwq_JSurPAYIEtQnwk_BwYbpAg)  
  <sub>TipRanks, 16 hours ago</sub>  
  Fidelity Ethereum Fund ETF (FETH) recorded a $502222 outflow on November 13, 2026. The withdrawal represented 0.0417% of its $1203825415 in assets under...
- [SoundHound AI Stock Forecast: How Much Upside Do Analysts See Post-Q3 Earnings?](https://www.google.com/goto?url=CAESqAEBxCJF1z9tLTqzCGuEjQ-4uaqRKCmXX-NDi4ZV1wKFXtm1rGLaoBol_ucq-8hJWVDkKP0rSc7pi-J0WqkzIiVNlb8rM79UcUD3bBRxm1lt-0c2hVscFm6NECC7MsL5Sp5hmUtC-UThrkvA-E7tcCRqHsbSeV3IBwbbQoGo1CKYmEZSphr19cOXWjd3hJ3pkeAuhgZbT5b6HqUqOIBpAVVHraUrGz5PWPY&gsessionid=IvAF8U-Hn0ZSitdV7NhbeToNPbcsOwq_JSurPAYIEtQnwk_BwYbpAg)  
  <sub>TipRanks, 55 minutes ago</sub>  
  U.S.-based voice AI company SoundHound AI ($SOUN) reported better-than-expected Q3 2026 results, with revenue rising 48.5% year-over-year to a record $62.4...
- [Excelland Robotics Proposes Full Circulation of 134,135,796 Unlisted Shares](https://www.google.com/goto?url=CAESugEBxCJF1y6FdxV8AhbxN2AMukWGgJ7bQp017P_WBjMsff7375DpZukySZpqVSUmL4b9D8uHBb7jiIp-TQuqRcxmj96yFWW4Fiq_MGIKszGmlWntvrfu4AT7u6pD45AOylQRKDQ668nreECZwlJ8ruvCfMFj9DU4MOo0BhQD-hhbQYesxxd0COj2SKw3Za4J1xJXg9hkRUKGwLsjGtXgpgb3vrL1E_HTPupgnaVUH1_T8wSmwjS8QxLxWCc&gsessionid=IvAF8U-Hn0ZSitdV7NhbeToNPbcsOwq_JSurPAYIEtQnwk_BwYbpAg)  
  <sub>TipRanks, 59 minutes ago</sub>  
  Excelland Robotics (Wuxi) Co. Ltd. Class H ( ($HK:3231) ) has shared an update. Excelland Robotics (Wuxi) Co. Ltd. is a PRC-incorporated joint stock company...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 104.68 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 105.87 (-1.1%), 50d 105.36 (-0.7%), 200d 108.61 (-3.6%); 50d below 200d
Momentum: RSI(14) 34.7 | MACD -0.141 vs signal 0.068 (histogram -0.208)
Returns: 1d +0.1% | 5d -1.3% | 1m -0.8% | 3m -2.2%
52-week range: 103.98 - 111.88 (now 8.8% of the way up)
Volatility: ATR(14) 0.38 (0.4% of price) | annualised 20d 4.7%
Volume: 0.04x the 20-day average
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
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 38.0% of open interest (5,947,433 contracts)
Change on the week: -0.2% of open interest
Crowding: 52% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +1.4% (205.78M) over 7d | 1 month: +2.6% (364.83M) over 32d
Shares outstanding: 139.90M | fund size: 14.64B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance due to mixed signals: macro risk-off (rising US yields, stronger dollar) and downtrend technicals, offset by modest inflows and bullish analyst coverage limited to ~51% of the fund.

**Main reasons it gave:**
- US Treasury yields rose across the curve (+0.10 to +0.30) indicating higher rates
- Dollar index increased 1.86% on the week, strengthening against other currencies
- Price below 20‑day, 50‑day, and 200‑day SMAs; RSI 25.3 (oversold) showing a downtrend with no decisive reversal
- Share count up 6% over the past month (net inflows) indicating modest demand

<details><summary><b>News</b> — score +0.00</summary>

- [Global X MSCI Argentina ETF (ARGT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/ARGT/)  
  <sub>Yahoo! Finance Canada, 3 hours ago</sub>  
  Global X MSCI Argentina ETF (ARGT) · 0.11% · -16.83% · -16.45% · -19.32% · -18.17% · 109.76% · 143.40%. Key Events. Baseline. Advanced...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 72.01 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 79.00 (-8.9%), 50d 85.75 (-16.0%), 200d 90.78 (-20.7%); 50d below 200d
Momentum: RSI(14) 25.3 | MACD -3.977 vs signal -3.602 (histogram -0.375)
Returns: 1d -2.4% | 5d -4.4% | 1m -18.2% | 3m -19.2%
52-week range: 72.01 - 102.94 (now 0.0% of the way up)
Volatility: ATR(14) 2.07 (2.9% of price) | annualised 20d 32.1%
Volume: 0.04x the 20-day average
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
Three-year record: +23.9% a year | beta to the market 0.44
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 51.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.60 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +65.8% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, PAM
Recent rating changes among them:
  - MELI: 2026-11-11 UBS: main, Neutral -> Neutral
  - YPF: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-10-29 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-10-13 UBS: main, Neutral -> Neutral
  - PAM: 2026-11-02 JP Morgan: main, Neutral -> Neutral
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
Share count change: 1 week: +2.2% (13.28M) over 7d | 1 month: +6.0% (34.88M) over 30d
Shares outstanding: 8.55M | fund size: 615.57M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, technicals bearish but low volume, analyst view bullish but limited coverage, and flat fund flows.

**Main reasons it gave:**
- US Treasury yields rose across the curve (+0.10 to +0.30) indicating a hawkish macro backdrop
- ETF price below 20d, 50d, 200d SMAs and RSI 39 with low volume (0.04x avg) showing bearish technicals
- Analyst coverage of top holdings 100% buy with +28.6% price target, covering 39.6% of fund weight
- Fund flows flat (0% change) indicating neutral investor demand

<details><summary><b>News</b> — score +0.00</summary>

- [17LIVE Announces Final Adjusted Maximum Promote Shares](https://www.tipranks.com/news/company-announcements/17live-announces-final-adjusted-maximum-promote-shares)  
  <sub>TipRanks, 4 hours ago</sub>  
  The latest update is out from 17LIVE Group Limited ( ($SG:LVR) ). 17LIVE Group announced that its Final Adjusted Maximum Promote Shares total 9307320,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 111.02 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 116.06 (-4.3%), 50d 119.56 (-7.1%), 200d 122.86 (-9.6%); 50d below 200d
Momentum: RSI(14) 39.0 | MACD -2.157 vs signal -2.010 (histogram -0.148)
Returns: 1d -1.2% | 5d -2.9% | 1m -7.2% | 3m -9.2%
52-week range: 99.40 - 137.69 (now 30.3% of the way up)
Volatility: ATR(14) 2.38 (2.1% of price) | annualised 20d 36.4%
Volume: 0.04x the 20-day average
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
Three-year record: +32.9% a year | beta to the market 0.98
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 39.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.00 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +28.6% above the current prices
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
Shares outstanding: 2.55M | fund size: 283.10M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals not decisive, analyst view slightly bearish, flows modestly positive, fundamentals solid.

**Main reasons it gave:**
- Analyst rating: 57.4% hold, 42.6% sell, mean rating 3.45 (sellish)
- Weighted price target -8.5% vs current price
- Fund flows: +1.0% share count increase over past month
- Technicals: price below 20d, 50d, 200d SMAs; RSI 45.2; volume 0.05x 20‑day average
- Macro: US inflation 3.7% and Fed target unchanged; yields up modestly

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 28.90 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 29.32 (-1.4%), 50d 28.96 (-0.2%), 200d 29.00 (-0.4%); 50d below 200d
Momentum: RSI(14) 45.2 | MACD 0.058 vs signal 0.119 (histogram -0.061)
Returns: 1d -0.7% | 5d -2.6% | 1m +0.6% | 3m -2.4%
52-week range: 24.95 - 30.43 (now 72.0% of the way up)
Volatility: ATR(14) 0.33 (1.1% of price) | annualised 20d 16.9%
Volume: 0.05x the 20-day average
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
Three-year record: +14.5% a year | beta to the market 0.94
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

<details><summary><b>What analysts and big funds say</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.40</summary>

```text
Rolled up from the 5 largest holdings, 46.5% of the fund by weight
Ratings by weight: buy 0.0% | hold 57.4% | sell 42.6% (mean 3.45 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -8.5% above the current prices
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
Share count change: 1 week: -0.1% (-726.99K) over 7d | 1 month: +1.0% (11.73M) over 32d
Shares outstanding: 42.72M | fund size: 1.23B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error response body was rejected) (Bing's feed, direct: 1 headline(s), none naming EWA)

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The analyst view is bullish (78% buy, +16% price target) while fund flows are flat (0% change) indicating no net demand. Technicals show price above key SMAs with modest momentum but very low volume, and macro data show rising yields with no surprise. The mix of a bullish analyst stance, neutral flow and modest technicals leads to a neutral overall call.

**Main reasons it gave:**
- Analyst coverage 78% buy, price target +16% above current price
- Flat fund flows (0% change) indicating no net demand
- Technical: price above 20‑day, 50‑day, 200‑day SMAs, modest momentum, very low volume
- Macro: US Treasury yields rising across curve, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 42.74 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 42.19 (+1.3%), 50d 41.99 (+1.8%), 200d 42.20 (+1.3%); 50d below 200d
Momentum: RSI(14) 54.5 | MACD 0.307 vs signal 0.218 (histogram 0.089)
Returns: 1d -0.4% | 5d -0.6% | 1m +2.8% | 3m -2.1%
52-week range: 38.08 - 44.59 (now 71.7% of the way up)
Volatility: ATR(14) 0.59 (1.4% of price) | annualised 20d 23.6%
Volume: 0.05x the 20-day average
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
Three-year record: +19.9% a year | beta to the market 0.95
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 45.1% of the fund by weight
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.97 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.2% above the current prices
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
Shares outstanding: 79.50M | fund size: 3.40B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected) (Bing's feed, direct: 1 headline(s), none naming EWG)

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, mixed technicals, modest outflows offsetting bullish analyst view, fundamentals modestly positive.

**Main reasons it gave:**
- Analyst view: 90.8% buy, weighted price target +11.6% above current price
- Fund flows: 1.9% share outflow over past month
- Technicals: price 2.2% above 20‑day SMA, MACD bullish, volume 0.02× 20‑day average
- Macro: US Treasury yields up modestly, curve normal, VIX 20.47 (elevated)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 58.19 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 56.96 (+2.2%), 50d 58.10 (+0.2%), 200d 58.30 (-0.2%); 50d below 200d
Momentum: RSI(14) 53.7 | MACD 0.260 vs signal -0.044 (histogram 0.305)
Returns: 1d -0.2% | 5d -1.8% | 1m +3.1% | 3m -7.2%
52-week range: 50.70 - 63.35 (now 59.2% of the way up)
Volatility: ATR(14) 0.87 (1.5% of price) | annualised 20d 27.9%
Volume: 0.02x the 20-day average
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
Three-year record: +27.2% a year | beta to the market 0.92
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 52.1% of the fund by weight
Ratings by weight: buy 90.8% | hold 9.2% | sell 0.0% (mean 2.17 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.6% above the current prices
Holdings read: UCG.MI, ISP.MI, ENEL.MI, ENI.MI, G.MI
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
Share count change: 1 week: -1.5% (-18.52M) over 7d | 1 month: -1.9% (-23.15M) over 32d
Shares outstanding: 20.51M | fund size: 1.19B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: Treasury yields rose modestly and VIX unchanged
- Technical indicators: price 90.70 below 20‑day SMA (92.80) and RSI 40.9
- Analyst coverage thin (17.2% of fund) despite 100% buy rating and +25.7% price target
- CFTC positioning net long 8% with a weekly increase of +4.7% of open interest

<details><summary><b>News</b> — score +0.00</summary>

- [Pictet raises Japan allocation as it looks beyond AI stocks (EWJ:NYSEARCA)](https://seekingalpha.com/news/4672813-pictet-raises-japan-allocation-as-it-looks-beyond-ai-stocks)  
  <sub>16 hours ago</sub>  
  Pictet's Dynamic Allocation fund raises Japan exposure to 10% from 8%, as Ramjee sees banks offering diversification beyond AI leaders.
- [Asian markets mostly lower as weak Japan GDP, soft China data, and Nvidia caution weigh](https://seekingalpha.com/news/4672821-asian-markets-mostly-lower-as-weak-japan-gdp-soft-china-data-and-nvidia-caution-weigh)  
  <sub>8 hours ago</sub>  
  Asian equity markets traded mostly lower on Monday, weighed down by weaker U.S. stock futures, elevated Treasury yields, and uncertainty over the Federal...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 90.70 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 92.80 (-2.3%), 50d 95.50 (-5.0%), 200d 92.13 (-1.5%); 50d above 200d
Momentum: RSI(14) 40.9 | MACD -1.375 vs signal -1.352 (histogram -0.023)
Returns: 1d -1.2% | 5d -0.9% | 1m -4.4% | 3m -4.9%
52-week range: 79.49 - 99.32 (now 56.5% of the way up)
Volatility: ATR(14) 1.57 (1.7% of price) | annualised 20d 29.3%
Volume: 0.06x the 20-day average
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
Three-year record: +18.3% a year | beta to the market 0.86
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 17.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.7% above the current prices
Holdings read: 8306.T, 7203.T, 6857.T, 6098.T, 8316.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-11-03, published the following Friday)
Large speculators: net long 8.0% of open interest (26,231 contracts)
Change on the week: +4.7% of open interest
Crowding: 55% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -3.1% (-736.81M) over 7d | 1 month: +6.3% (1.39B) over 32d
Shares outstanding: 256.47M | fund size: 23.26B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat flows, modest analyst bullishness offset by slight downside price target and near‑52‑week high.

**Main reasons it gave:**
- Flat fund flows (0% change) indicating neutral demand
- Analyst ratings: 64.8% buy, 35.2% hold, weighted price target -1.3% vs current price
- Technical trend above 20‑, 50‑, 200‑day SMAs but MACD histogram negative and volume 0.05× 20‑day average
- Macro: no surprise in US data; yields up modestly, dollar up, VIX moderate – no catalyst

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 65.14 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 64.40 (+1.1%), 50d 61.92 (+5.2%), 200d 62.01 (+5.0%); 50d below 200d
Momentum: RSI(14) 59.4 | MACD 0.938 vs signal 1.007 (histogram -0.070)
Returns: 1d +0.5% | 5d -0.9% | 1m +4.6% | 3m +3.5%
52-week range: 55.69 - 66.56 (now 86.9% of the way up)
Volatility: ATR(14) 0.80 (1.2% of price) | annualised 20d 19.8%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

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
Rolled up from the 5 largest holdings, 49.6% of the fund by weight
Ratings by weight: buy 64.8% | hold 35.2% | sell 0.0% (mean 2.45 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -1.3% above the current prices
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
Shares outstanding: 28.62M | fund size: 1.86B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, modestly bullish analyst coverage on 42% of holdings, solid fundamentals, but technicals are neutral with low volume; overall view remains neutral.

**Main reasons it gave:**
- Analyst view: 100% buy on 42% of holdings, weighted price target +57% above current prices
- Fund flows: share count unchanged (0% change) over 1 week and 1 month
- Fund basics: P/E 18.38, dividend yield 4.4%, 3‑year annualized return +20.7% per year
- Technicals: price near 20‑day SMA, RSI 47.2, volume 0× 20‑day average (very low)
- Macro: US yields rose modestly, no surprise data; VIX at 20.5 (elevated)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 64.76 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 64.78 (-0.0%), 50d 66.14 (-2.1%), 200d 65.18 (-0.6%); 50d above 200d
Momentum: RSI(14) 47.2 | MACD -0.304 vs signal -0.450 (histogram 0.146)
Returns: 1d +0.0% | 5d -1.5% | 1m -0.3% | 3m -7.5%
52-week range: 55.33 - 71.61 (now 57.9% of the way up)
Volatility: ATR(14) 1.05 (1.6% of price) | annualised 20d 25.5%
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
Three-year record: +20.7% a year | beta to the market 1.13
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 42.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.58 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +57.3% above the current prices
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
Shares outstanding: 5.55M | fund size: 359.42M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no clear macro surprise, flat fund flows, mixed technicals with low volume, and only moderate bullish analyst coverage.

**Main reasons it gave:**
- Fund flows flat: 0% share count change over 1 week and 1 month, indicating no net demand
- Macro: US Treasury yields rose across the curve and dollar index up 1.86% on the week, a potentially negative backdrop for European equities
- Technical: price above 20‑day, 50‑day, and 200‑day SMAs with positive MACD, but volume is only 0.02× 20‑day average, suggesting weak conviction
- Analyst view: 76.3% buy rating covering 53% of the fund and a +6% price target, indicating moderate bullish sentiment but limited coverage

<details><summary><b>News</b> — score +0.00</summary>

- [ETF iShares europei: Regno Unito in testa, Italia quasi ferma](https://www.borsamagazine.it/azioni/ETF-iShares-europei-Regno-Unito-in-testa-Italia-quasi-ferma/)  
  <sub>Borsa Magazine, 6 hours ago</sub>  
  Nei dati del 13 novembre 2026, i cinque ETF iShares europei salgono: Regno Unito e Spagna guidano i rialzi, Germania prima per volumi e Italia appena...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 59.83 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 58.29 (+2.6%), 50d 59.18 (+1.1%), 200d 58.16 (+2.9%); 50d above 200d
Momentum: RSI(14) 56.9 | MACD 0.304 vs signal -0.035 (histogram 0.339)
Returns: 1d +0.0% | 5d -0.6% | 1m +2.7% | 3m -3.6%
52-week range: 49.37 - 63.23 (now 75.5% of the way up)
Volatility: ATR(14) 0.87 (1.5% of price) | annualised 20d 24.2%
Volume: 0.02x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

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
Shares outstanding: 37.35M | fund size: 2.23B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, mixed fund flows, bullish analyst view limited to ~38% of holdings, fundamentals mixed (high valuation, heavy tech exposure). Overall neutral stance.

**Main reasons it gave:**
- Analyst consensus: 100% buy with +59% price target (covers 37.7% of fund)
- Fund flows mixed: weekly outflow -10.8% (-$1.25B) vs monthly inflow +5.2% (+$0.51B)
- Technical indicators bearish: price below 20‑day SMA (-8.9%), RSI 37, low volume (0.30× 20‑day avg)
- Macro backdrop unchanged: yields rising, VIX elevated, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

- [Options on The Week | The Rebound's Fuel Is Fading, All Eyes on Nvidia Earnings and Anthropic IPO](https://www.moomoo.com/community/feed/options-on-the-week-the-rebound-s-fuel-is-fading-117624790188038)  
  <sub>Moomoo, 8 hours ago</sub>  
  by Monta HONG, CFA | Options Strategist The $S&P 500 Index (.SPX.US)$ gained 2.5% on last week, and $CBOE Volatility S&P 500 Index (.VIX.US)$ down 24%...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 91.21 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 100.08 (-8.9%), 50d 107.43 (-15.1%), 200d 94.79 (-3.8%); 50d above 200d
Momentum: RSI(14) 37.0 | MACD -4.003 vs signal -3.793 (histogram -0.209)
Returns: 1d -6.3% | 5d -4.6% | 1m -14.2% | 3m -12.6%
52-week range: 60.03 - 118.00 (now 53.8% of the way up)
Volatility: ATR(14) 4.07 (4.5% of price) | annualised 20d 67.0%
Volume: 0.30x the 20-day average
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
Three-year record: +37.1% a year | beta to the market 1.35
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 37.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +59.2% above the current prices
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
Direction: money coming in (1 month)
Share count change: 1 week: -10.8% (-1.25B) over 7d | 1 month: +5.2% (509.87M) over 32d
Shares outstanding: 113.27M | fund size: 10.33B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, no decisive technical break, modest bearish fund outflows offset by strong analyst consensus.

**Main reasons it gave:**
- Analyst consensus 100% buy with weighted price target +12.8% above current price
- Fund outflows of -1% over the past month (net money leaving)
- Price above 20d, 50d, 200d SMA but low volume and no decisive technical break
- Macro data stable: yields up modestly, inflation 3.7% in line with expectations

<details><summary><b>News</b> — score +0.00</summary>

- [UK's Burnham: Brexit has not worked; we lost more than we ‌gained](https://seekingalpha.com/news/4672840-uk-pm-burnham-brexit-has-not-worked?source=generic_rss)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Brexit has not worked, UK Prime Minister Andy Burnham is expected to say at the Lord Mayor's Banquet on Monday, ahead of a European Union summit in Brussels...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 48.10 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 47.79 (+0.7%), 50d 47.40 (+1.5%), 200d 47.10 (+2.1%); 50d above 200d
Momentum: RSI(14) 54.0 | MACD 0.176 vs signal 0.164 (histogram 0.012)
Returns: 1d +0.3% | 5d -0.5% | 1m +0.2% | 3m -0.1%
52-week range: 41.34 - 49.39 (now 84.0% of the way up)
Volatility: ATR(14) 0.59 (1.2% of price) | annualised 20d 20.0%
Volume: 0.02x the 20-day average
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
Three-year record: +19.9% a year | beta to the market 0.66
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 36.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.08 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.8% above the current prices
Holdings read: SHEL.L, HSBA.L, AZN.L, ULVR.L, RR.L
Recent rating changes among them:
  - AZN.L: 2026-08-24 CICC: init, ? -> Outperform
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
Share count change: 1 week: +0.3% (11.07M) over 7d | 1 month: -1.0% (-38.75M) over 32d
Shares outstanding: 78.30M | fund size: 3.77B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, modest technical signal with low volume, and analyst coverage limited to 47.5% of the fund despite a bullish rating. These factors balance out, leading to a neutral overall view.

**Main reasons it gave:**
- Flat fund flows: 0% share count change over 1 week and 1 month
- Technicals: price 0.3% above 200‑day SMA, volume 0.08× 20‑day average
- Macro: yields up modestly, dollar up 1.86% on week, VIX 20.47 (elevated but stable)
- Analyst coverage limited to 47.5% of fund, 100% buy rating, +10.7% price target

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 76.45 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 75.94 (+0.7%), 50d 74.38 (+2.8%), 200d 76.20 (+0.3%); 50d below 200d
Momentum: RSI(14) 55.4 | MACD 0.852 vs signal 0.763 (histogram 0.089)
Returns: 1d -0.9% | 5d -1.4% | 1m +2.0% | 3m +2.7%
52-week range: 65.87 - 81.23 (now 68.9% of the way up)
Volatility: ATR(14) 1.29 (1.7% of price) | annualised 20d 14.2%
Volume: 0.08x the 20-day average
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
Three-year record: +13.3% a year | beta to the market 0.99
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
Weighted price target: +10.7% above the current prices
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
Shares outstanding: 18.90M | fund size: 1.44B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technical downtrend with price below SMAs and low volume; analyst consensus bullish (100% buy, +29.8% price target) but covering only 41.8% of the fund; fundamentals strong (low P/E 10.65, high yield 8.2%, strong 3‑year record); fund flows flat indicating neutral demand.

**Main reasons it gave:**
- Technical downtrend: price below 20d, 50d, 200d SMAs and low volume (0.19x avg)
- Analyst consensus: 100% buy rating with +29.8% price target
- Fund fundamentals: low P/E 10.65, high yield 8.2%, strong 3‑year record +25.5% per year
- Fund flows flat: no net creations/redemptions indicating neutral demand

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 64.00 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 64.94 (-1.4%), 50d 65.61 (-2.5%), 200d 67.99 (-5.9%); 50d below 200d
Momentum: RSI(14) 45.1 | MACD 0.165 vs signal 0.134 (histogram 0.031)
Returns: 1d -0.9% | 5d -7.5% | 1m -2.0% | 3m -4.6%
52-week range: 60.43 - 81.60 (now 16.9% of the way up)
Volatility: ATR(14) 1.46 (2.3% of price) | annualised 20d 30.5%
Volume: 0.19x the 20-day average
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
Three-year record: +25.5% a year | beta to the market 1.12
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
Weighted price target: +29.8% above the current prices
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
Shares outstanding: 7.90M | fund size: 505.60M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: yields up modestly, dollar stronger, VIX unchanged
- Technical RSI 39.4 and MACD negative, but volume 0.06x avg – no decisive break
- Analyst view 100% buy with +35% price target – bullish but not material
- Fund flows flat (0.0% change) – no net demand

<details><summary><b>News</b> — score +0.00</summary>

- [Nvidia’s All-Important Q3 Report, China Tech Results, Anthropic IPO And Microsoft Ignite To Keep Investors Hooked This Week](https://www.tradingview.com/news/stocktwits:15b46db5e094b:0-nvidia-s-all-important-q3-report-china-tech-results-anthropic-ipo-and-microsoft-ignite-to-keep-investors-hooked-this-week/)  
  <sub>TradingView, 8 hours ago</sub>  
  Investors head into a crucial week, with Nvidia's (NVDA) all-important quarterly report on the deck, amid the mayhem caused by the unceremonious departure...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 99.94 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 104.75 (-4.6%), 50d 106.03 (-5.7%), 200d 94.22 (+6.1%); 50d above 200d
Momentum: RSI(14) 39.4 | MACD -1.930 vs signal -1.485 (histogram -0.445)
Returns: 1d -1.2% | 5d -1.5% | 1m -4.2% | 3m -2.0%
52-week range: 74.67 - 112.67 (now 66.5% of the way up)
Volatility: ATR(14) 2.87 (2.9% of price) | annualised 20d 30.4%
Volume: 0.06x the 20-day average
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
Three-year record: +11.5% a year | beta to the market 1.25
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.60 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +35.2% above the current prices
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
Shares outstanding: 12.50M | fund size: 1.25B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows mixed signals: strong analyst optimism on its top holdings (100% buy, +13.9% price target) but covering only 24.8% of the portfolio, significant net outflows (-9.7% share count in the past month) indicating bearish investor sentiment, bullish technicals (price above 20‑day, 50‑day and 200‑day SMAs, high RSI) tempered by low volume, and macro headwinds from a stronger US dollar and rising Treasury yields that pressure emerging‑market equities. These factors largely offset each other, leading to a neutral overall stance.

**Main reasons it gave:**
- Analyst view: 100% buy rating on top holdings with +13.9% price target (covers 24.8% of fund)
- Fund flows: share count down 9.7% in past month, indicating net outflows
- Technicals: price above 20‑day, 50‑day and 200‑day SMAs, RSI 74.8 (overbought) and low volume
- Macro: US dollar index up 1.86% and Treasury yields rising, adding pressure on emerging‑market equities

<details><summary><b>News</b> — score +0.20</summary>

- [India stands to gain as investors look beyond AI, Jefferies’ Wood says (INDA:BATS)](https://seekingalpha.com/news/4672794-india-stands-to-gain-as-investors-look-beyond-ai-jefferies-wood-says)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Analyst sees India benefiting from AI stock rotation, with $7.2 billion in net foreign buying; easing Iran tensions could lift non-U.S..

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.30</summary>

```text
Last close 51.60 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 49.08 (+5.1%), 50d 48.08 (+7.3%), 200d 49.11 (+5.1%); 50d below 200d
Momentum: RSI(14) 74.8 | MACD 1.151 vs signal 0.831 (histogram 0.320)
Returns: 1d +0.3% | 5d +0.4% | 1m +8.3% | 3m +4.5%
52-week range: 45.42 - 54.83 (now 65.7% of the way up)
Volatility: ATR(14) 0.52 (1.0% of price) | annualised 20d 15.8%
Volume: 0.08x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 24.8% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.37 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.9% above the current prices
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
Share count change: 1 week: -2.9% (-174.03M) over 7d | 1 month: -9.7% (-629.23M) over 30d
Shares outstanding: 113.44M | fund size: 5.85B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, no decisive technical break, and mixed fund‑flow signals keep the overall view neutral despite a strong analyst buy rating and modestly bullish technicals.

**Main reasons it gave:**
- Fed target unchanged at 4.00% and Treasury yields rose across curve (+0.10 to +0.27% weekly)
- Analyst coverage 90.9% buy with weighted price target +15.3% above current price
- Fund flows net inflow 2.1% over month but outflow -1.8% over week, indicating mixed demand
- Price above 20-day, 50-day, 200-day SMAs; RSI 58; MACD positive, but volume 0.03x 20-day average

<details><summary><b>News</b> — score +0.00</summary>

- [Union Pacific Stock: Analyst Estimates & Ratings](https://www.barchart.com/story/news/8853813/union-pacific-stock-analyst-estimates-ratings)  
  <sub>Barchart.com, 2 hours ago</sub>  
  Union Pacific has significantly outperformed the broader market, while analysts remain moderately optimistic about its future growth prospects.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.30</summary>

```text
Last close 84.33 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 82.31 (+2.5%), 50d 81.06 (+4.0%), 200d 82.05 (+2.8%); 50d below 200d
Momentum: RSI(14) 58.0 | MACD 0.844 vs signal 0.631 (histogram 0.212)
Returns: 1d +0.7% | 5d +0.7% | 1m +5.4% | 3m -2.1%
52-week range: 68.14 - 90.01 (now 74.0% of the way up)
Volatility: ATR(14) 1.46 (1.7% of price) | annualised 20d 27.3%
Volume: 0.03x the 20-day average
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
Three-year record: +14.8% a year | beta to the market 1.24
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

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

```text
Rolled up from the 5 largest holdings, 52.2% of the fund by weight
Ratings by weight: buy 90.9% | hold 9.1% | sell 0.0% (mean 1.87 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.3% above the current prices
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
Share count change: 1 week: -1.8% (-36.27M) over 7d | 1 month: +2.1% (41.19M) over 32d
Shares outstanding: 24.00M | fund size: 2.02B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: analysts are bullish, but fund outflows are bearish and technicals are neutral.

**Main reasons it gave:**
- Analyst view: 90.6% buy, weighted price target +16% above current price
- Fund flows: -6.1% outflow over past month (13.5M shares)
- Technical: price below 50‑day (36.00) and 200‑day (37.76) SMA, MACD positive, volume 0.04× 20‑day average
- Macro: yields up modestly, no rate surprise; curve normal

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 35.78 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 34.87 (+2.6%), 50d 36.00 (-0.6%), 200d 37.76 (-5.2%); 50d below 200d
Momentum: RSI(14) 55.4 | MACD 0.033 vs signal -0.218 (histogram 0.250)
Returns: 1d -0.6% | 5d +0.9% | 1m +1.9% | 3m -6.0%
52-week range: 33.69 - 40.63 (now 30.1% of the way up)
Volatility: ATR(14) 0.35 (1.0% of price) | annualised 20d 17.2%
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
Three-year record: +0.8% a year | beta to the market 0.20
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
Ratings by weight: buy 90.6% | hold 9.4% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.0% above the current prices
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
Share count change: 1 week: -2.4% (-13.52M) over 7d | 1 month: -6.1% (-36.12M) over 30d
Shares outstanding: 15.44M | fund size: 552.50M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; macro risk‑off environment, downtrend technicals, and recent outflows offset bullish analyst view and attractive fundamentals.

**Main reasons it gave:**
- 1‑month net outflow of -4% shares (money going out)
- Price below 20‑day, 50‑day, and 200‑day SMAs, indicating downtrend
- Macro: rising yields and strong dollar, risk‑off environment
- Analyst coverage 32.6% of fund, 100% buy rating with +71% price target

<details><summary><b>News</b> — score +0.00</summary>

- [How to Buy Shein Stock in 2026](https://www.fool.com/investing/how-to-invest/stocks/how-to-invest-in-shein-stock/)  
  <sub>The Motley Fool, 20 hours ago</sub>  
  Shein has quickly become one of the most popular fashion brands in the world. This article explores the ins and outs of investing in this fast-growing,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 49.45 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 50.04 (-1.2%), 50d 51.50 (-4.0%), 200d 55.05 (-10.2%); 50d below 200d
Momentum: RSI(14) 39.1 | MACD -0.357 vs signal -0.384 (histogram 0.027)
Returns: 1d -0.2% | 5d -4.0% | 1m -3.4% | 3m -9.9%
52-week range: 48.96 - 64.26 (now 3.2% of the way up)
Volatility: ATR(14) 0.66 (1.3% of price) | annualised 20d 21.2%
Volume: 0.07x the 20-day average
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
Three-year record: +7.6% a year | beta to the market 0.47
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 32.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.42 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +71.1% above the current prices
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
Share count change: 1 week: +3.5% (184.58M) over 7d | 1 month: -4.0% (-225.98M) over 30d
Shares outstanding: 110.10M | fund size: 5.44B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as macro headwinds, weak technicals and recent outflows offset bullish analyst view and strong fund fundamentals.

**Main reasons it gave:**
- Week outflow: -11.1% shares (-$7.79B) over 7 days
- Technical: price below 20d, 50d, 200d SMAs; RSI 36.9; MACD negative
- Macro: yields rising (10y 5.13% +0.27% week) and market expects 4 Fed hikes
- Analyst view: 100% buy, +52.3% price target, covering 46.4% of fund
- Fund fundamentals: high valuation (P/E 28.22, P/B 9.76) and beta 2.12

<details><summary><b>News</b> — score +0.00</summary>

- [VanEck Semiconductor ETF (SMH) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/SMH/)  
  <sub>Yahoo! Finance Canada, 2 hours ago</sub>  
  VanEck Semiconductor ETF (SMH) · 4.91% · -17.24% · -14.97% · 33.98% · 36.91% · 223.31% · 898.46%. Key Events. Baseline. Advanced Chart. Loading chart for...
- [Time to Buy the Dip in NVIDIA Despite Leadership Turmoil? ETFs in Focus](https://www.tradingview.com/news/zacks:a51e75ee8094b:0-time-to-buy-the-dip-in-nvidia-despite-leadership-turmoil-etfs-in-focus/)  
  <sub>TradingView, 3 hours ago</sub>  
  NVIDIA NVDA may close below a $4 trillion market capitalization for the first time since July 2025 amid the Jensen Huang ouster saga.
- [If Staying in Nvidia Stock Scares You, You Might Want To Consider This ETF](https://www.google.com/goto?url=CAESngEBxCJF19fu7WqunxyNJk5_Jd9ncmFaY16Ti2K7KtbJGSSTd1EybiesmmKRVsrdFUPb8e2b_QjUwSRSrutd30f7KZLUSmFKBymwvhU6zwSQn2u2dhEDHq3Ri1AGEgOriYJceWaDLGWvY_JtZIkPZnwipUinLTHnUBoj-6N3IEfZluHeiNYcb2jis2_5cyKvJfPNZ42u0oZ4M1mMvrDJuQ&gsessionid=aaTEYu9eZUh40iXPgGnu9BUZHOndZz3jLbfYxqa7OlWnTWVkf31QYw)  
  <sub>Yahoo Finance, 58 minutes ago</sub>  
  Nvidia's troubles may suggest that ETF investing is more suitable for some investors.
- [SMH 261113 390.00C (SMH261113C390000) Stock Options Chain | Quotes & News](https://www.google.com/goto?url=CAESbgHEIkXX2Cx0t2vH8AUAIyQPfLF7T0V4RMCqT7ggSufJIby_wIGQbJhBoC1Mr_T7VMj8ob1zdUDxjcJG_4Ln-dxsPGcBD-gSmAT4VXXo1l_WsmwG6yXp0iNpJt1e1NIdcDMEb02AeDt1zrfT8E5q&gsessionid=aaTEYu9eZUh40iXPgGnu9BUZHOndZz3jLbfYxqa7OlWnTWVkf31QYw)  
  <sub>Moomoo, 19 hours ago</sub>  
  $VanEck Semiconductor ETF (SMH.US)$ · $NVIDIA (NVDA.US)$ CEO resigned, and the stock dropped about 13% in five days. Other chip stocks fell with it.
- [Forget SCHD: These 3 Income ETFs Offer 12%+ Yields and Up to 30% Upside](https://www.google.com/goto?url=CAESnQEBxCJF10qPKWlOvwAKCd-Y_R2itHsj_QMkcHjVfM6i4vsYFIQyRSCFl0xl18HnhtIAFJVIL2HXtfaR5XqGgkBoQS_9DimaPO3fGfciL9xY9vDP00dwHPGiF1vKOMeTEZnnzlWkQCVttr-OSZ8ZqtpYOx70-fKhgVEHCjnmcUZg3iEgTlSr5bDxnxizVrZZ2h_Wicp91WenwZyoEUeI&gsessionid=aaTEYu9eZUh40iXPgGnu9BUZHOndZz3jLbfYxqa7OlWnTWVkf31QYw)  
  <sub>TipRanks, 60 minutes ago</sub>  
  The Schwab U.S. Dividend Equity ETF ($SCHD) remains a popular dividend ETF, thanks to its focus on high-quality companies and low fees.
- [3 Nvidia-Heavy ETFs to Watch Ahead of Q3 Earnings – One Offers 55% Upside](https://www.google.com/goto?url=CAESoAEBxCJF17sQOh5XK4pa8_gmRbKpH3QAwRpSqbnxH4nNaoPw2ZEfKjvKj1BlFSzHYozawNGF8P5nVniMP60vJAXYEFdgiKTc3WRgpv1GjfQd_XtcPpcgmbDUoojjw2F4Odd6JDKzglfa88iYzMTgLT4tZo3ZtkLG3EhbM_r2gSbfUpalz6HrQJAgUUDod-zS-sQJMvoBMoxgdKcYSj9Q-bA4&gsessionid=aaTEYu9eZUh40iXPgGnu9BUZHOndZz3jLbfYxqa7OlWnTWVkf31QYw)  
  <sub>TipRanks, 4 hours ago</sub>  
  Nvidia ($NVDA) will report its fiscal Q3 results on November 17. Analysts expect earnings per share to rise about 90% to $2.47, while revenue is forecast to...
- [Notable open interest changes for November 16th](https://www.google.com/goto?url=CAESnQEBxCJF10cn0vAu5acu8jma8WD55eNP8FBHmbcOLq-fX16vpHXhbkK5X5oBS7gahf8G5VK30W6VXWi5lm41-E2g2I_RQQl-i44D3GnjTp_9U_Ne1mZrp7I3AMp60m_Nn35Wv3DCHzMkTlxYxBckyRR1YapVjf7Yc1gtutb-ovs7tEMNp8kuVTOxg5m4rF6Y1nEIpukfC6_njunrD_sI&gsessionid=aaTEYu9eZUh40iXPgGnu9BUZHOndZz3jLbfYxqa7OlWnTWVkf31QYw)  
  <sub>TipRanks, 47 minutes ago</sub>  
  Friday's total option volume of 78.2 million contracts resulted in net open interest growth of 7.28 million calls and 4.88 million puts.
- [Pony AI, Toyota launch fully driverless commercial services for bZ4X Robotaxi](https://www.google.com/goto?url=CAESugEBxCJF16bHwlmdJrj1e79OOK8UoLHA8vAouu11Fl02DqyTGbDLG3ce1HjKfR6JS-CNMEfKEw45Uqr_wBgsKbbg2LR0WKpwqNouxQSEjmaHE4AFsQoYG0ofm1nJ5Ofike-2Yml2zDGhJVLeNxk9XQjIontXC12prG9vIYStgKzZVU3Y5OJKeFb43tbokxSppvaoqdXMLabTwLlFEf_MdvG7wEUAfRktLehSJUhs7SFEL5FTnIOQakjYVEU&gsessionid=aaTEYu9eZUh40iXPgGnu9BUZHOndZz3jLbfYxqa7OlWnTWVkf31QYw)  
  <sub>TipRanks, 4 hours ago</sub>  
  Pony AI (PONY) and Toyota (TM) announced the launch of fully driverless commercial services with their collaboratively developed bZ4X Robotaxi.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 469.82 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 514.21 (-8.6%), 50d 557.86 (-15.8%), 200d 524.22 (-10.4%); 50d above 200d
Momentum: RSI(14) 36.9 | MACD -23.639 vs signal -22.245 (histogram -1.395)
Returns: 1d -3.5% | 5d -3.6% | 1m -13.0% | 3m -17.5%
52-week range: 325.10 - 668.91 (now 42.1% of the way up)
Volatility: ATR(14) 24.21 (5.2% of price) | annualised 20d 66.1%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.30</summary>

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
Rolled up from the 5 largest holdings, 46.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.56 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +52.3% above the current prices
Holdings read: NVDA, TSM, TXN, AVGO, AMD
Recent rating changes among them:
  - NVDA: 2026-11-12 Melius Research: down, Buy -> Hold
  - TSM: 2026-11-04 Bernstein: main, Outperform -> Outperform
  - TXN: 2026-10-22 Jefferies: main, Hold -> Hold
  - AVGO: 2026-10-27 Rosenblatt: main, Buy -> Buy
  - AMD: 2026-11-12 B of A Securities: main, Buy -> Buy
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
Direction: money coming in (1 month)
Share count change: 1 week: -11.1% (-7.79B) over 7d | 1 month: +6.6% (3.87B) over 32d
Shares outstanding: 132.34M | fund size: 62.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: strong analyst buy rating (+27% price target) is offset by flat fund flows, price below medium‑ and long‑term SMAs with low volume, and a macro backdrop of a strong dollar and normal upward‑sloping yield curve with no surprise data. Fundamentals show low valuation but modest 3‑yr return, providing no clear directional edge.

**Main reasons it gave:**
- Analyst view: 100% buy on top holdings, weighted price target +27% above current
- Fund flows: flat share count change (0% week, 0% month) indicating neutral demand
- Technicals: price below 50‑day (34.11) and 200‑day (38.56) SMAs, low volume (0.09× 20‑day avg)
- Macro: normal upward‑sloping yield curve, strong dollar (+1.86% week), no data surprise
- Fund basics: low valuation (P/E 11.6, P/B 1.01) but modest 3‑yr return (+0.6%/yr) and 2.8% yield

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 32.19 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 31.26 (+3.0%), 50d 34.11 (-5.6%), 200d 38.56 (-16.5%); 50d below 200d
Momentum: RSI(14) 49.4 | MACD -0.500 vs signal -0.884 (histogram 0.384)
Returns: 1d -0.0% | 5d -0.2% | 1m -0.9% | 3m -18.7%
52-week range: 29.53 - 43.74 (now 18.7% of the way up)
Volatility: ATR(14) 0.60 (1.9% of price) | annualised 20d 34.5%
Volume: 0.09x the 20-day average
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
Three-year record: +0.6% a year | beta to the market 0.60
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 44.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.1% above the current prices
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

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US Treasury yields rose across the curve (+0.10 to +0.27) with no surprise
- VIX at 20.47, elevated but stable
- ETF price below 20‑day and 50‑day SMAs, MACD negative, RSI 44.6
- Analyst coverage thin (9.5% weight) despite 75% buy rating and +9% price target
- Fund flows: +5.6% net inflow over month, -1.8% outflow over week

<details><summary><b>News</b> — score +0.00</summary>

- [Biotech ETFs Face Crucial FDA Week as Drug Catalysts Loom - State Street SPDR S&P Biotech ETF (ARCA:XBI)](https://www.benzinga.com/etfs/sector-etfs/26/11/63290811/biotech-etfs-brace-for-fda-showdown-two-drug-decisions-could-test-investor-sentiment?utm_source=googlefinance)  
  <sub>24 minutes ago</sub>  
  XBI and IBB lagged SPY and QQQ as two FDA decisions and fresh Alzheimer's and obesity-drug data put biotech ETFs in focus.
- [Which Healthcare ETF Is the Better Buy: State Street’s Pharma Fund XPH or iShares’ Biotech Fund IBB?](https://finance.yahoo.com/healthcare/articles/healthcare-etf-better-buy-state-183954069.html)  
  <sub>20 hours ago</sub>  
  State Street SPDR S&P Pharmaceuticals ETF (NYSEMKT:XPH) and iShares Biotechnology ETF (NASDAQ:IBB) both offer targeted healthcare exposure, but they differ...
- [Three FDA Decisions Loom After Summit’s Rejection — Capricor, Savara, Alzheimer’s Data Top Biotech’s Watchlist](https://www.google.com/goto?url=CAES5QEBxCJF10VxQ0uhzGJQa8kXe3sUxgHmkpUrQqYjGl4He3XTRuZ6A4Q_h_UcCzWvHw7dV6LP8Ypm8RaykeX0qXK15_RqCVmOtchT9RdaYc3Zw9v2G4Ycntcq_0V2qQwsTXp9qLs7VRZGDu0krgmkG5H-0wqdlWI7RCw1gkZDUEAxzcy4bsi8BvHmKW1g0yWmr3g-NuHPh_kd90SxvShJr6lX5lyu-E3pSTaALB3HDRjFHcX5Kh6kIDBd5bhDv8Zc9v9GUMqfzWGBhKc1IZgsF4IeOVMFf2Chi6Y2LYOVsrHtgxl1dsua&gsessionid=hAMDZnWUreM3GkbiFKtIXsVRbvQe6ctp_OVsTKb45AClQISH9acFmg)  
  <sub>12 hours ago</sub>  
  The regulatory stakes in biotech firms rise this week as Capricor and Savara near FDA decisions, while Alzheimer's presentations and obesity-drug updates...
- [XBI Mar 2027 184.000 call (XBI270319C00184000) Interactive Stock Chart - Yahoo Finance](https://www.google.com/goto?url=CAESeQHEIkXX9llZrs3sVC6Cb6qBlSRnIVxwcrvlw0AZxjfy3oUixjHplMjq6lgtANk8tLR69rnuYIB0uKcip8H6pBoebqADDz94hTXTVLpBoV3rBafnoFhAQi10ey5bF0cC7AbhodWM5yBaU6jh-9VpavQSicV_o38HO0k&gsessionid=hAMDZnWUreM3GkbiFKtIXsVRbvQe6ctp_OVsTKb45AClQISH9acFmg)  
  <sub>19 hours ago</sub>  
  Interactive Chart for XBI Mar 2027 184.000 call (XBI270319C00184000), analyze all the data with a huge range of indicators.
- [Burry Questions Nvidia’s China Revenue Reporting](https://www.google.com/goto?url=CAES-AEBxCJF10_-ZckNdhpuYsPL_sAPyFpzbfRtNOlAKns294gN6O8z6GdMz2Z5pmI_LKJOA-4MieBrR4dJpwBlQVT0cTu97_Se1T4tnGr6g73bmgKz3jSQlptw-P7LtCvZQ1hjxy8ZSM85SAUrlccht0UL_3b_oSzhKzip9YtjAPYMI0zoY3mWGd_jzZGFgTKwto_A8sSvQYWXtNLhTquomqoAcZMwVKOXe674dtP_n7E2NRBha8meU_cW3pETsw1LELCTjPo9KkczUmD6QbTWSXYIH2cWH0WlzBs6gu7LZgNILUIBtEgTxMnZ5LpuNn9gmO-AuSuANsxRQA&gsessionid=hAMDZnWUreM3GkbiFKtIXsVRbvQe6ctp_OVsTKb45AClQISH9acFmg)  
  <sub>20 hours ago</sub>  
  Burry highlighted that Nvidia last year moved its revenue reporting from counting sales by billing location to headquarters location,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 149.13 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 153.48 (-2.8%), 50d 153.97 (-3.1%), 200d 143.09 (+4.2%); 50d above 200d
Momentum: RSI(14) 44.6 | MACD -0.460 vs signal -0.094 (histogram -0.366)
Returns: 1d -0.9% | 5d -5.0% | 1m +3.3% | 3m -6.9%
52-week range: 113.83 - 169.55 (now 63.4% of the way up)
Volatility: ATR(14) 4.73 (3.2% of price) | annualised 20d 40.1%
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
Three-year record: +31.1% a year | beta to the market 1.01
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

<details><summary><b>What analysts and big funds say</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.15</summary>

```text
Rolled up from the 5 largest holdings, 9.5% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 75.0% | hold 25.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.0% above the current prices
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
Share count change: 1 week: -1.8% (-194.60M) over 7d | 1 month: +5.6% (567.31M) over 30d
Shares outstanding: 72.20M | fund size: 10.77B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals mixed, flat flows, limited analyst coverage, and direct buy/sell signal ignored as unreliable.

**Main reasons it gave:**
- No policy or rate surprise; yields rose modestly across the curve
- Technical indicators mixed: price above SMAs but MACD bearish, low volume, no decisive break
- Fund flows flat over the past week and month, indicating no net demand shift
- Analyst coverage limited to 34% of fund, showing bullish view but insufficient to drive overall call
- Disregarded direct buy/sell signal from trading report as unreliable

<details><summary><b>News</b> — score +0.00</summary>

- [XME: Materials Dashboard For November (NYSEARCA:XME)](https://seekingalpha.com/article/4968559-xme-materials-dashboard-for-november?source=feed_all_articles)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  The State Street SPDR S&P Metals & Mining ETF offers exposure to the materials subsector with the most attractive value and quality scores.
- [Long Term Trading Analysis for (XLB) (XLB:CA)](https://news.stocktradersdaily.com/canada/long-term-trading-analysis-for-xlb-_20261115_de6eb8)  
  <sub>Stock Traders Daily, 10 hours ago</sub>  
  Trading Report for iShares Core Canadian Long Term Bond Index ETF XLB With Buy and Sell Signals.
- [Are Wall Street Analysts Bullish on CF Industries Stock?](https://www.google.com/goto?url=CAESoAEBxCJF1-yiz06JGTpzHbInP9k8LemcuBECe2j_RmS7GHVTdUA5C-099TFMmPaxx0a5YvLpzwqJpWGMfbtoR5EcUbobvlOdphnetgAeXp4xHWUI-92k1ms1Tmz9NaJV-P0FXRSG1kwwevNayldYDq4nmjsSZZBv9FUDQ_JmUSytQeZyHplYmdFoJuthknvgv-uSehkEoFZ-6g-7VEWb60Rl&gsessionid=8prx1f2TkWmB_OcbFVK2731mg-LkV_jgk2kcqF7V1Wl0p86DDHgoPQ)  
  <sub>Barchart.com, 1 hour ago</sub>  
  Northbrook, Illinois-based CF Industries Holdings, Inc. (CF) manufactures and sells hydrogen and nitrogen products for energy, fertilizer,...
- [XLB Jan 2028 38.500 call (XLB280121C00038500) Seasonal Returns Chart - Yahoo Finance](https://www.google.com/goto?url=CAESfwHEIkXX4JAqPTW90xTDKoeyZFR-rn-IQ_-HXIx3aNWxdPQTE1L2bHW0NSlQ84idLlS1AV_nWGhYqTxYKAN7VLtq-BFomZVg49U9A3zvZy-vQ48Flo7_rnw-kbt94VJgXMlutk9FUvx-X2EYvxaZHkrJcol3hbuJwcSqAgQOS0g&gsessionid=8prx1f2TkWmB_OcbFVK2731mg-LkV_jgk2kcqF7V1Wl0p86DDHgoPQ)  
  <sub>Yahoo! Finance Canada, 9 hours ago</sub>  
  XLB Jan 2028 38.500 call (XLB280121C00038500) seasonal returns chart provides the mean and median returns by month to inform your investment strategy.
- [DuPont de Nemours Stock: Is Wall Street Bullish or Bearish?](https://www.google.com/goto?url=CAESogEBxCJF1zxkHfu49NeQtz87_ch94gQrQunnFbCud-U-JNulu584b2dAOwRYqqNxf2FoBjCdSQbTyYRs2-1vee_HoPkftCCbFWFweFMlXl7agR9aM-X6nclMhwvwJHGEKiFBk3aQxX9_uCHYjdCRikmfGj25GnrcWFhzuYs3bnFCWzP3cUC6w7mK4olkGcR7zCQRiqTOK9ckdW8vV_pm3FOPYV0&gsessionid=8prx1f2TkWmB_OcbFVK2731mg-LkV_jgk2kcqF7V1Wl0p86DDHgoPQ)  
  <sub>Barchart.com, 2 hours ago</sub>  
  DuPont de Nemours has outperformed the broader market over the past year, while Wall Street analysts maintain a moderately optimistic outlook on the stock's...
- [Auxly Cannabis Group Inc. (XLY.TO) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZwHEIkXXCfRsKb0l9J-xJ5Xu_Gw6YNQrUDEVUsKRTd0YmsMJqpOXfuGsQW4Fc4Ff_Igwd9QY4ch91Mh3eyXDhu03ldlFbg-LpuNx-qu7PcYeWuYnfy-MqitZRchON5qDIqcQwL4mpoI&gsessionid=8prx1f2TkWmB_OcbFVK2731mg-LkV_jgk2kcqF7V1Wl0p86DDHgoPQ)  
  <sub>Yahoo! Finance Canada, 10 hours ago</sub>  
  Find the latest Auxly Cannabis Group Inc. (XLY.TO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Reliance leads materials stocks with biggest Q3 earnings surprise (XLB:NYSEARCA)](https://www.google.com/goto?url=CAESpAEBxCJF1wKx13dvXgPqkkYqLKHtJTBG3B9vO_ceri9zQ1SHRHcXlQg54moh3uuXrHVRm732IIvUV-bBq5uhzuijCC7QVVQq4XHy2bUwPeqaSyuzneBr3RAgQxSap_E-ra7TjGHOuFvLDvH4mVbnRoDssPZpYzoNjlFcft_3R8_D17Xwk6mTd4GJ50NbqmDcMDRvGzhjmUrqRzC15FsOlpLSE9cDOA&gsessionid=8prx1f2TkWmB_OcbFVK2731mg-LkV_jgk2kcqF7V1Wl0p86DDHgoPQ)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Reliance leads eight materials stocks with a Q3 EPS surprise of $1.19, ahead of Alcoa at $0.31 and Quaker Chemical at $0.29 as earnings season nears its...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 52.07 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 52.29 (-0.4%), 50d 50.92 (+2.3%), 200d 51.26 (+1.6%); 50d below 200d
Momentum: RSI(14) 51.3 | MACD 0.452 vs signal 0.554 (histogram -0.102)
Returns: 1d -0.3% | 5d -1.6% | 1m +2.3% | 3m +0.6%
52-week range: 42.23 - 53.90 (now 84.3% of the way up)
Volatility: ATR(14) 0.87 (1.7% of price) | annualised 20d 20.4%
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
Three-year record: +12.7% a year | beta to the market 0.76
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.3% above the current prices
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
Shares outstanding: 71.92M | fund size: 3.75B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral – no material macro surprise, flat fund flows, technicals lack a decisive break, and mixed fundamentals.

**Main reasons it gave:**
- Flat fund flows over the past week and month indicate no net demand
- No macro surprise: yields rose modestly, dollar up, VIX stable
- Technical indicators show price below 50‑day and 200‑day SMA, RSI near 50, no decisive break
- Analyst coverage thin (24% of fund) but all buy with +24.5% price target
- Fund fundamentals: high P/E (26.85) and low yield (1.1%) suggest modest valuation concerns

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Friday as Producer Inflation Trails Forecasts](https://www.moomoo.com/news/post/1004601462/exchange-traded-funds-equity-futures-higher-pre-bell-friday-as)  
  <sub>Moomoo, 9 hours ago</sub>  
  Thebroad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.4% and the actively traded Invesco QQQ Trust (QQQ) was 0.2% higher in Friday's...
- [BTIG Strategist Puts Staples’ Edge Over Tech at 33%, Widest in About 25 Years](https://www.tokenpost.com/news/investing/58381)  
  <sub>www.tokenpost.com, 1 hour ago</sub>  
  XLP rose 10.9% in October while XLK fell 8.3%; BTIG Chief Technical Strategist Jonathan Krinsky compared the sector split with the early dot-com bust.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 168.15 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 167.90 (+0.2%), 50d 168.82 (-0.4%), 200d 173.47 (-3.1%); 50d below 200d
Momentum: RSI(14) 49.2 | MACD -0.155 vs signal -0.445 (histogram 0.289)
Returns: 1d -0.4% | 5d -0.4% | 1m +0.2% | 3m -8.4%
52-week range: 147.83 - 186.51 (now 52.5% of the way up)
Volatility: ATR(14) 3.03 (1.8% of price) | annualised 20d 25.2%
Volume: 0.12x the 20-day average
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
Three-year record: +19.7% a year | beta to the market 1.00
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
Shares outstanding: 136.63M | fund size: 22.97B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise or decisive technical break; technicals are bearish, but analyst coverage and fundamentals are bullish and flows show net inflow over the month.

**Main reasons it gave:**
- Technical indicators: price below 20‑day SMA, RSI 36.9, MACD negative, low volume indicating bearish momentum
- Fund flows: net inflow over 1‑month (+6.7% share count) but recent week outflow (-6.6%)
- Analyst coverage: 100% buy rating, weighted price target +31.5% above current price
- Fundamentals: P/E 31.66, 3‑year record +24.8% annualized, high growth but high valuation
- Macro: Treasury yields rising, no policy surprise, VIX elevated at 20.47

<details><summary><b>News</b> — score +0.00</summary>

- [SocGen's Albert Edwards warns liquidity squeeze, inflation threaten AI stock rally (XLK:NYSEARCA)](https://seekingalpha.com/news/4672790-socgens-albert-edwards-warns-liquidity-squeeze-inflation-threaten-ai-stock-rally)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  The bear case for AI stocks: tightening liquidity and fading earnings upgrades could pressure shares as inflation revives risk of Fed hikes above 200 basis.
- [Markets Shrug Off Nvidia Turmoil, for Now](https://www.investing.com/analysis/markets-shrug-off-nvidia-turmoil-for-now-200691661)  
  <sub>Investing.com, 2 hours ago</sub>  
  Market Analysis by James Picerno covering: S&P 500, NVIDIA Corporation, NASDAQ Composite, Invesco S&P 500® Equal Weight ETF. Read James Picerno's Market...
- [BTIG flags consumer staples beating tech by 33%, the widest gap in about 25 years](https://www.google.com/goto?url=CAEShgEBxCJF1896es5ceg2hume7zctTxZiYDCiMiCa6iuSfCNlqloY98dC0gVQntgh-DXPeiaID7zJMOUH4W07RfwMq_Cej_R8HXeU8NHVe2q5RlGmfoGolBveCQ3N4rqaEZCDaFjTNbnPsfyDOZ9s58p_ubRyV84XlNM2nJFWZQCgRUzGgfD-hsQ&gsessionid=f4KeHaTXh5ThaSF2S83CWrAmwonjpZSr6PCbcWRlljHuEuIgG8uW2g)  
  <sub>Crypto Briefing, 2 hours ago</sub>  
  Jonathan Krinsky notes the last time defensives lapped tech this hard was the opening stretch of the dot-com bust. by Vivian Nguyen.
- [Chart of the Day 11/16/26: It's Not Just Fall. It's "Value Season!"](https://www.google.com/goto?url=CAESrwEBxCJF147WazRmJMOeJRg8cEIKJngA9uV-KqvSXlWhDWFk3mvdsEEtuQYPFw40vb392qQLWpWnq9AQN-COrHCVcY-4ZW_X4_Dhs6B1qZED99wKMh4h8aJ-Ec1ch92qvVBqBb9dB2fQ8lUgDQASrDFAePZGbUpvkEKYgAuRUQcRLP-wErkQvpBh3LWuhcY7txXPHyWF5yWg_LYPzOJSKfvJ_9pE0iTI8GyyQOaTGx4g&gsessionid=f4KeHaTXh5ThaSF2S83CWrAmwonjpZSr6PCbcWRlljHuEuIgG8uW2g)  
  <sub>www.moneyshow.com, 10 hours ago</sub>  
  The first real cold front of the fall just pushed through South Florida, and I enjoyed the vibe shift it brought with it. Speaking of change, did you see...
- [BTIG Strategist Puts Staples’ Edge Over Tech at 33%, Widest in About 25 Years](https://www.google.com/goto?url=CAESawHEIkXX72OV9m1OPVbBMZLVxcEiQ8e-JWuWFfOEPu4ajIG-jrKI2-ciFc16bmHR5ffq2qNqoun5gfdZXvs1Os17RL1iO-EXjRrvqNI6FaB-6JeZspoh6HwryUmPETcquambRU6BU12pxBE_&gsessionid=f4KeHaTXh5ThaSF2S83CWrAmwonjpZSr6PCbcWRlljHuEuIgG8uW2g)  
  <sub>www.tokenpost.com, 1 hour ago</sub>  
  XLP rose 10.9% in October while XLK fell 8.3%; BTIG Chief Technical Strategist Jonathan Krinsky compared the sector split with the early dot-com bust.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 167.17 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 177.72 (-5.9%), 50d 186.70 (-10.5%), 200d 170.93 (-2.2%); 50d above 200d
Momentum: RSI(14) 36.9 | MACD -5.511 vs signal -4.999 (histogram -0.513)
Returns: 1d -1.8% | 5d -2.2% | 1m -8.9% | 3m -9.9%
52-week range: 127.50 - 202.00 (now 53.2% of the way up)
Volatility: ATR(14) 5.48 (3.3% of price) | annualised 20d 44.7%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

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
Rolled up from the 5 largest holdings, 51.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +31.5% above the current prices
Holdings read: AAPL, NVDA, MSFT, AVGO, AMD
Recent rating changes among them:
  - AAPL: 2026-11-11 China Renaissance: up, Hold -> Buy
  - NVDA: 2026-11-12 Melius Research: down, Buy -> Hold
  - MSFT: 2026-10-29 Bernstein: main, Outperform -> Outperform
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
Share count change: 1 week: -6.6% (-8.04B) over 7d | 1 month: +6.7% (7.15B) over 32d
Shares outstanding: 683.07M | fund size: 114.19B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – bullish analyst view and solid fundamentals are offset by flat fund flows and a macro backdrop of higher yields and expected rate hikes that pressure utilities.

**Main reasons it gave:**
- Analyst coverage of top holdings is 80% buy with a weighted price target +8.3% above current prices
- Technical indicators show price above 20‑day and 50‑day SMAs, RSI 68, positive MACD, but volume is only 0.09× the 20‑day average
- Fund flows are flat over the past week and month, indicating no net demand shift
- Macro environment: higher yields and expectations of further rate hikes pressure utilities
- Fund fundamentals: moderate valuation (P/E 17.9), 2.8% yield, strong 3‑year performance (+17.3%/yr) but not enough to outweigh macro headwinds

<details><summary><b>News</b> — score +0.20</summary>

- [4 Utilities Mutual Fund Picks to Ride Rising Power Demand](https://www.tradingview.com/news/zacks:66de045d9094b:0-4-utilities-mutual-fund-picks-to-ride-rising-power-demand/)  
  <sub>TradingView, 3 hours ago</sub>  
  The U.S. utilities sector has staged a remarkable comeback since the end of September, with the State Street Utilities Select Sector SPDR ETF (XLU)...
- [NextEra Energy, Inc. (NEE) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/NEE/)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>  
  Find the latest NextEra Energy, Inc. (NEE) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [BUI: Earnings Cover 2 Years Of Payouts, Still A Buy After The Pullback](https://www.google.com/goto?url=CAESpQEBxCJF101FSsuRZ1vZKv02ZVxEOpT11Ou89MQFVacfyi-6DSSRTE-bv868EuXyr_qHYp4w4D10VAxGqZ7EiRMPUmuALXqpOUT2evkR2r-8A2-61DPWDLUkX4XS1FmhcbrGEZ471OFdjQSd_ENKTGEPOekBfT0OfVp_oKykpKFhns9PtFiJkptCQyF_SWUKys-j_JGgnt-Uwa6TAdr7pNOqRicg-Ow&gsessionid=hWlEHhmhAMlP37Hr9Xr39U1eMLCed76QcaM20fibTuOuGbAqjvbUpw)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  BlackRock Utilities Infrastructure & Power Opportunities Trust remains a Buy: its below-average price-to-NAV valuation and AI-driven power demand support...
- [Are Wall Street Analysts Bullish on Eversource Energy Stock?](https://www.google.com/goto?url=CAESpQEBxCJF1z-nZ5Vd9kU8ET2jV-SBuQzZXQC6cy2nccyLVnq07OyMMVDVRxZWpf1VeCYKj7ebwoAEvR2JzfnBTo74ykhnUlgUDPq6OsXPh4yh9tixg8VOHMINxqL29RYp-5L0JH-rEQ2FHD25gQswRs7v7V3ez_fBxTASdXjUb4NFniXiGPOQXG9RqQ5uiOg2tgpbfA0k85YgNJaGfnzfe-34jT0TGhI&gsessionid=hWlEHhmhAMlP37Hr9Xr39U1eMLCed76QcaM20fibTuOuGbAqjvbUpw)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  Eversource Energy has underperformed the broader market despite higher earnings guidance and long-term growth targets, while analyst sentiment remains...
- [ETFs Are Net Sellers of NextEra Energy Units (NEE) on Thursday](https://www.google.com/goto?url=CAESoAEBxCJF11ZbAFIU_X9B_qNb851fs2jYnyI_T4HcpGfcmtHG_N3P-gFNWEnSIcwcuBr4iz86U89H-RnIhe9G1BRBxpz-61lnF9A69vyDn2hiEGwT6Cr_lteKW613L28qQE475iRUGcr1qaWDtSREu14RPCyAzdneBameMZwKCt4s2_QFcRf7l-r16xQEsi9aljs9mB-1csXlDLRp5VNg-5bY&gsessionid=hWlEHhmhAMlP37Hr9Xr39U1eMLCed76QcaM20fibTuOuGbAqjvbUpw)  
  <sub>GuruFocus, 4 hours ago</sub>  
  PFF drove the move, cutting its NextEra Energy Units stake by $149.6 million last Thursday as ETF activity turned negative. More funds traded the other way,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.30</summary>

```text
Last close 44.30 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 43.22 (+2.5%), 50d 41.92 (+5.7%), 200d 44.33 (-0.1%); 50d below 200d
Momentum: RSI(14) 68.1 | MACD 0.600 vs signal 0.544 (histogram 0.056)
Returns: 1d +0.6% | 5d +1.2% | 1m +5.0% | 3m +0.6%
52-week range: 39.25 - 47.73 (now 59.6% of the way up)
Volatility: ATR(14) 0.58 (1.3% of price) | annualised 20d 12.9%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

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
Rolled up from the 5 largest holdings, 39.4% of the fund by weight
Ratings by weight: buy 80.0% | hold 20.0% | sell 0.0% (mean 2.04 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +8.3% above the current prices
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
Shares outstanding: 163.27M | fund size: 7.23B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst view offset by bearish fund outflows and mixed technicals, with no macro surprise.

**Main reasons it gave:**
- Fund flows show net outflows of -2.3% in the past week and -1.3% over the past month
- Analyst coverage of top holdings is 100% buy with a weighted price target +15.9% above current levels
- Technicals: price above 20‑day SMA, 50‑day SMA below 200‑day SMA, low volume, RSI 56, MACD positive
- Macro: Treasury yields rose across the curve, inflation at 3.7% above target, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Auxly Cannabis Group Inc. (XLY.TO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLY.TO/)  
  <sub>Yahoo! Finance Canada, 10 hours ago</sub>  
  Find the latest Auxly Cannabis Group Inc. (XLY.TO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Do Wall Street Analysts Like Ball Corporation Stock?](https://www.barchart.com/story/news/8855374/do-wall-street-analysts-like-ball-corporation-stock)  
  <sub>Barchart.com, 36 minutes ago</sub>  
  Ball Corporation has outpaced the broader market over the past year, and analysts remain moderately optimistic about the stock's prospects.
- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Friday as Producer Inflation Trails Forecasts](https://www.google.com/goto?url=CAESpwEBxCJF11OauEjdddNY3GCkDc7x8yyot1bZzXrKg3cbmTtqBrBO_5Vdu47eQEor1VgRWV758oxqamBwtDISWYHvCJCz2aPj8cX9H-SQyFIwFBvVLg70S8mLdcEDT41_QYrGO2OyVenkvVZs9pzk4sciIN43pEoxBieaGlo1PQvdEQum9IlVe7Z40XjoMgr0h4Vpm56Nr9g0kEgaAhobQtyxGpmOegyj1Q&gsessionid=xHd3qrBYsGNBMeLyal2rmsLeutAJZ5TfddijncnoqEFslk37R_p79w)  
  <sub>Moomoo, 9 hours ago</sub>  
  Thebroad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.4% and the actively traded Invesco QQQ Trust (QQQ) was 0.2% higher in Friday's...
- [Consumer Defensive Stocks Extend Winning Streak To 6 Weeks As SPY, QQQ Rebound: TTD, CHTR, TSLA Lead Gains](https://www.google.com/goto?url=CAES4QEBxCJF13FrpF4qvZ57bzVZTPA2I0Lpk26M0ADqHfwW7GJ2y4J9FMbz4IVY8CoOP7GFTJYhdl05ZOFi4H4m0JjZj2Cku0lUhRE9zSHjPZOQMxhi36uPNNhzsSGgwxyJ2jhkqaGx-b02YnkkE5ExHeEH0z8Lb2_QtSFIsTyWkQL605IaL4anhFUg939Qxj4xwHgtqpc3K_u6CPafRy2OZSsOSu-4L5AlT0AiEqaj4RRwCCQ2MLoj9u-slTY9yLdHvHDXyx9LuyabbKwcRTtyFaz1JwtKPQhnu5KqM4iXtyCT2I8&gsessionid=xHd3qrBYsGNBMeLyal2rmsLeutAJZ5TfddijncnoqEFslk37R_p79w)  
  <sub>TradingView, 14 hours ago</sub>  
  Consumer stocks kept their winning ways last week, though this time the broader market gained pace. The Trade Desk (TTD), Charter Communications (CHTR) and...
- [What Are Wall Street Analysts' Target Price for General Motors Stock?](https://www.google.com/goto?url=CAESrAEBxCJF1wP3geVCp3YxeprN2ij2MiycWMvz1IAfDAJ_oHnIh7J6vL0RvFKKo64iHIgqsxcD3JTCTIu-3ZtJS4NSNDE2E7rJmQ54hLfDedWIlm-panbDmirKxU5EeApbgODJ17PRMQiuZSjDX4t91QWDcJ9TlBC6tgF_RZjuv97yrrruTU6aIN-P5LiqmXWBopVfYGOu6o-zf1PLubD-33Rzf2N8T0w7AbXCXopE&gsessionid=xHd3qrBYsGNBMeLyal2rmsLeutAJZ5TfddijncnoqEFslk37R_p79w)  
  <sub>Barchart.com, 8 hours ago</sub>  
  General Motors has outperformed the broader market, supported by earnings growth, raised cash flow guidance, buybacks, and increasingly bullish analyst...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 118.95 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 117.56 (+1.2%), 50d 113.91 (+4.4%), 200d 115.43 (+3.1%); 50d below 200d
Momentum: RSI(14) 56.0 | MACD 1.844 vs signal 1.748 (histogram 0.097)
Returns: 1d -0.9% | 5d -1.7% | 1m +5.8% | 3m +2.2%
52-week range: 105.66 - 124.52 (now 70.5% of the way up)
Volatility: ATR(14) 2.15 (1.8% of price) | annualised 20d 27.0%
Volume: 0.12x the 20-day average
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
Three-year record: +14.9% a year | beta to the market 1.10
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 54.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.9% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, TJX
Recent rating changes among them:
  - AMZN: 2026-11-03 Freedom Broker: main, Buy -> Buy
  - TSLA: 2026-11-05 GLJ Research: reit, Sell -> Sell
  - HD: 2026-11-10 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-11-06 Argus Research: main, Buy -> Buy
  - TJX: 2026-11-10 UBS: main, Buy -> Buy
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
Share count change: 1 week: -2.3% (-521.45M) over 7d | 1 month: -1.3% (-299.60M) over 32d
Shares outstanding: 185.98M | fund size: 22.12B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 44.15 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 43.80 (+0.8%), 50d 44.21 (-0.1%), 200d 40.73 (+8.4%); 50d above 200d
Momentum: RSI(14) 52.5 | MACD -0.055 vs signal -0.138 (histogram 0.083)
Returns: 1d +0.1% | 5d +0.8% | 1m -0.9% | 3m +1.2%
52-week range: 32.56 - 45.76 (now 87.8% of the way up)
Volatility: ATR(14) 0.66 (1.5% of price) | annualised 20d 24.6%
Volume: 0.09x the 20-day average
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
Ratings by weight: buy 51.3% | hold 48.7% | sell 0.0% (mean 2.23 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +5.2% above the current prices
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
Share count change: 1 week: -0.6% (-6.63M) over 7d | 1 month: +23.1% (193.64M) over 30d
Shares outstanding: 23.40M | fund size: 1.03B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error response body was rejected) (Bing's feed, direct: 2 headline(s), none naming EPOL)

### Canada (EWC) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Energy World Corporation: Controller sellers issue cleansing notice after share sale](https://www.tipranks.com/news/company-announcements/energy-world-corporation-controller-sellers-issue-cleansing-notice-after-share-sale)  
  <sub>16 hours ago</sub>  
  Energy World Corporation Ltd ( ($AU:EWC) ) has issued an update. Energy World Corporation Ltd's controller, comprising Energy World Developments Pty Limited...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 59.92 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 60.71 (-1.3%), 50d 60.10 (-0.3%), 200d 58.58 (+2.3%); 50d above 200d
Momentum: RSI(14) 46.5 | MACD -0.005 vs signal 0.120 (histogram -0.125)
Returns: 1d -0.3% | 5d -1.7% | 1m -1.1% | 3m -2.7%
52-week range: 49.91 - 62.64 (now 78.6% of the way up)
Volatility: ATR(14) 0.79 (1.3% of price) | annualised 20d 18.5%
Volume: 0.04x the 20-day average
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
Weighted price target: +6.2% above the current prices
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
Share count change: 1 week: +0.1% (6.41M) over 7d | 1 month: +6.1% (433.32M) over 32d
Shares outstanding: 126.08M | fund size: 7.55B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Substantial Holder Notice Records Share-Interest Changes](https://www.tipranks.com/news/company-announcements/substantial-holder-notice-records-share-interest-changes)  
  <sub>TipRanks, 15 hours ago</sub>  
  Energy World Corporation Ltd ( ($AU:EWC) ) has shared an update. A Form 605 notice records that Energy World International Ltd, Energy World Developments...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 52.49 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 52.08 (+0.8%), 50d 51.45 (+2.0%), 200d 51.55 (+1.8%); 50d below 200d
Momentum: RSI(14) 53.2 | MACD 0.461 vs signal 0.436 (histogram 0.025)
Returns: 1d -0.4% | 5d -2.0% | 1m +2.5% | 3m +0.2%
52-week range: 45.38 - 54.72 (now 76.1% of the way up)
Volatility: ATR(14) 0.75 (1.4% of price) | annualised 20d 22.0%
Volume: 0.01x the 20-day average
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
Weighted price target: +8.4% above the current prices
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
Share count change: 1 week: +0.5% (5.66M) over 7d | 1 month: +12.2% (119.80M) over 32d
Shares outstanding: 21.02M | fund size: 1.10B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Top Tokenized ETFs by Market Cap](https://www.coingecko.com/en/etfs)  
  <sub>CoinGecko, 1 hour ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...
- [Asian markets mostly lower as weak Japan GDP, soft China data, and Nvidia caution weigh](https://seekingalpha.com/news/4672821-asian-markets-mostly-lower-as-weak-japan-gdp-soft-china-data-and-nvidia-caution-weigh)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  Asian equity markets traded mostly lower on Monday, weighed down by weaker U.S. stock futures, elevated Treasury yields, and uncertainty over the Federal...
- [iShares MSCI South Korea ETF (EWY) Price Prediction: Bears Still Own the Trend, but Sellers Are Losing Steam Near Support](https://www.google.com/goto?url=CAESlQEBxCJF1y2U2UHWNtMbCI6fqVALMxT4ZrpHBjm9I7ocOJe_JPO5efZlLEPT_uXul_I79dTXsgRkZfZNHuxWX6NsZacSKC60XlRSCOAEMCQcXovnk5Ik__oQhSzCZvNGDFAjbUBJ12oRXO4g2WX7jxAZPdTRpo-SJe1qSNdTEJEQ7qcILI7pzkX7HaWepCZ5l_GMKAkz7Q&gsessionid=D2T0EGkJWsFVD54qAwEhENFpgnDkQFNKGnqMjt3Ctjw9GQxw1Afi3A)  
  <sub>Blockchain News, 4 hours ago</sub>  
  iShares MSCI South Korea ETF (EWY) is trading at $139.70, below its short- and medium-term moving averages, with momentum still negative but not outright...
- [Direxion South Korea Bull 3X ETF (KORU) Price Prediction: Leveraged Korea exposure is trying to stabilize after a sharp reset](https://www.google.com/goto?url=CAESngEBxCJF15-kreBEQbosGlOSBQS_36yk09nSEbK570O9vHYCCD9DSV7BP9V3ptTJou0gAupTc3cr9l1OZGfVAXVCOKwY9lEFVAGyx_GhZ3rsBQUnwnijJNR3ALnxwTdoCg3OEL1yer5mWjbDrdqdicmNN7t0Zz64lSoEv76V5h7oAg5vL2MKK1S_ASmlrXIr5wqoAS5J5d6hQkLsKek03Q&gsessionid=D2T0EGkJWsFVD54qAwEhENFpgnDkQFNKGnqMjt3Ctjw9GQxw1Afi3A)  
  <sub>blockchain.news, 4 hours ago</sub>  
  Direxion South Korea Bull 3X ETF (KORU) is trading at $7.16 after a 0.84% 24-hour gain, but the broader setup remains damaged: price is still below every...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 138.31 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 149.25 (-7.3%), 50d 167.45 (-17.4%), 200d 164.10 (-15.7%); 50d above 200d
Momentum: RSI(14) 38.8 | MACD -7.384 vs signal -7.447 (histogram 0.063)
Returns: 1d -3.1% | 5d -2.7% | 1m -8.1% | 3m -18.7%
52-week range: 88.53 - 219.20 (now 38.1% of the way up)
Volatility: ATR(14) 7.18 (5.2% of price) | annualised 20d 71.3%
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
Direction: money coming in (1 month)
Share count change: 1 week: -8.3% (-1.92B) over 7d | 1 month: +3.5% (709.94M) over 32d
Shares outstanding: 153.08M | fund size: 21.17B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Top Tokenized ETFs by Market Cap](https://www.coingecko.com/en/etfs)  
  <sub>CoinGecko, 1 hour ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 31.51 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 34.51 (-8.7%), 50d 37.47 (-15.9%), 200d 36.98 (-14.8%); 50d above 200d
Momentum: RSI(14) 31.8 | MACD -1.958 vs signal -1.856 (histogram -0.103)
Returns: 1d -2.2% | 5d -3.4% | 1m -24.7% | 3m -6.5%
52-week range: 30.97 - 43.54 (now 4.3% of the way up)
Volatility: ATR(14) 1.07 (3.4% of price) | annualised 20d 73.5%
Volume: 0.06x the 20-day average
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
Weighted price target: +33.8% above the current prices
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
Shares outstanding: 200.55M | fund size: 6.32B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 429: {"error":{"message":"Model busy, retry later","type":"invalid_request_error","param":null,"code":"engine_overloaded"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Best and worst ETFs of the last five years revealed](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afb181d8b4e4f82a0f62bf2f7dc91f9&url=https%3a%2f%2fwww.news.com.au%2ffinance%2fmarkets%2fbest-and-worst-etfs-of-the-last-five-years-revealed%2fnews-story%2fc9342dcb04222ef716f83286434ffcfb&c=8196969844615629004&mkt=en-us)  
  <sub>news.com.au, 23h ago</sub>  
  The best and worst ETFs of the last five years have been revealed, with gold, semiconductors and the AI boom helping clock “incredible gains” for the best performers.
- [Goldminen mit relativer Stärke](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afb181d8b4e4f82a0f62bf2f7dc91f9&url=https%3a%2f%2fwww.goldseiten.de%2fartikel%2f720933--Goldminen-mit-relativer-Staerke.html%3fseite%3d1&c=17356849590541279898&mkt=en-us)  
  <sub>Goldseiten, 16h ago</sub>  
  Gemessen an zwei sehr langfristigen gleitenden Durchschnittslinien befindet sich das Gold in einem lupenreinen Bullenmarkt. Zuletzt wurde lediglich der deutlich ansteigende 100-Wochen-Durchschnitt noc ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 81.55 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 83.21 (-2.0%), 50d 87.91 (-7.2%), 200d 89.52 (-8.9%); 50d below 200d
Momentum: RSI(14) 44.3 | MACD -1.013 vs signal -1.172 (histogram 0.159)
Returns: 1d -0.1% | 5d -10.8% | 1m -7.0% | 3m -8.3%
52-week range: 70.74 - 115.84 (now 24.0% of the way up)
Volatility: ATR(14) 3.38 (4.1% of price) | annualised 20d 57.4%
Volume: 0.13x the 20-day average
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
Weighted price target: +20.8% above the current prices
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
Share count change: 1 week: +4.8% (1.09B) over 7d | 1 month: -2.1% (-499.59M) over 30d
Shares outstanding: 290.77M | fund size: 23.71B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [(ITA) Price Dynamics and Execution-Aware Positioning](https://news.stocktradersdaily.com/news_release/151/ITA_Price_Dynamics_and_Execution-Aware_Positioning_111626094401_1794840241.html)  
  <sub>Stock Traders Daily, 5 hours ago</sub>  
  Price-action only: Ishares U.s. Aerospace & Defense Etf (ITA) movements set the tone for institutional models. (ITA) Price Dynamics and Execution-Aware...
- [How to Buy Boeing Stock (BA) in 2026](https://www.fool.com/investing/how-to-invest/stocks/how-to-invest-in-boeing-stock/)  
  <sub>The Motley Fool, 20 hours ago</sub>  
  Boeing ranks as one of the biggest aerospace and defense stocks on the market.
- [My Two Wishes for This Market](https://www.google.com/goto?url=CAESfwHEIkXXygAxs83klJq9M7DMaS3r3us_Hy1w0NHnp-Kp8XGp22jg8qViE254NqeBZzvDgEYfSX-yerIW_sJTqbZli7KTzBXaxXGdT13Pu_OpeBv38an3ZVCL4-E--XRBNgAUQ-V8Evt7jXnP45pIBEsLZV3phq7lupGs7TsNR2c&gsessionid=IrWZwBpHAmNcznXBluB_tuThy-oVPMa9dfDE4DUYL4baf_mcPp9GEg)  
  <sub>RealMoney Pro, 18 hours ago</sub>  
  Stocks keep finding somewhere to hide. Here's why that needs to stop. Let's also look at Meta, Citi, TLT, drone ETFs and more.
- [U.S., Russia to oppose binding rules for autonomous weapons](https://www.google.com/goto?url=CAESmgEBxCJF19kUw-Kvop3XNo-o0nDJ1OZjU_NhqA8R5ufkZt8gtnYvSQi4WvQj2d5QRbMZwtdaplLKOaAsV_wT8S5i-WwC9EgmriJawwkEv5Lf64ipz8hr-1xsFEJ9zY301REpmhkvFngbpzO5_QLDGyHnGIOtlJihjkzzR_71xS9HlWu7wF8KxWN5FN92Mj1EWit9zrU-rWmTMdoc&gsessionid=IrWZwBpHAmNcznXBluB_tuThy-oVPMa9dfDE4DUYL4baf_mcPp9GEg)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  UN members weigh a two-year mandate to negotiate binding rules for autonomous weapons talks. Read more.
- [FTAI Aviation (FTAI) Sees $479.6 Million in Net ETF Buying on No](https://www.google.com/goto?url=CAESowEBxCJF14ReEalbqvQvPtoaBKLaT5o8rpT8-6v0N2R0C-EVEN27heH95t3RgZdSdMyTqEqgyEJKS7CRlS4bBD1yDbyWdYiVkmySA1xP_zWSJ5KZobaf4hkyxUw067SItCE9cdeVt-xJO4aqF7RNL2x3D3WShy-9hAm90Edir-3-rHCvaEP1Kk9f671aUgjXc3xSlXcniowobO0rIFxbkVT9Cw06&gsessionid=IrWZwBpHAmNcznXBluB_tuThy-oVPMa9dfDE4DUYL4baf_mcPp9GEg)  
  <sub>GuruFocus, 3 hours ago</sub>  
  The iShares U.S. Aerospace & Defense ETF (ITA) led the move, adding $169.4 million of FTAI Aviation stock in Thursday's session.
- [Market’s Either-Or Rotation Risks a Pullback as Sentiment Nears Panic](https://www.google.com/goto?url=CAESmwEBxCJF1w9ysKoZ4gZ1RMDpyFv7O_LKfegOs1IorfnUcVBhs5OgbFvcTIdyc22YkaP1PguNDxIhZJtdA70A8aV-CKTRPkY2jldiThq5wcoCKezDUxlv3Fc99SRsxyNLAl2TnOvXtoCVofBGVQUhSgVHfce7jBqhWiDla3YW0UylfUvO5v2JEOjGOdCb24WjZMs8DKIZn9Y3RNZ7EA&gsessionid=IrWZwBpHAmNcznXBluB_tuThy-oVPMa9dfDE4DUYL4baf_mcPp9GEg)  
  <sub>SSBCrack, 15 hours ago</sub>  
  A technical market outlook is calling for a sharp decline to break what it describes as an “Either/Or” market, in which gains in one group of stocks have.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 71.26 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 70.23 (+1.5%), 50d 70.32 (+1.3%), 200d 75.89 (-6.1%); 50d below 200d
Momentum: RSI(14) 52.3 | MACD 0.410 vs signal 0.141 (histogram 0.269)
Returns: 1d -0.3% | 5d -0.6% | 1m +2.3% | 3m -15.2%
52-week range: 66.08 - 84.41 (now 28.3% of the way up)
Volatility: ATR(14) 1.72 (2.4% of price) | annualised 20d 30.7%
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
Weighted price target: +16.8% above the current prices
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
Share count change: 1 week: -5.1% (-646.54M) over 7d | 1 month: +189.5% (7.95B) over 30d
Shares outstanding: 170.48M | fund size: 12.15B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Which Bank ETF Is the Better Buy: State Street’s Regional Banking KRE or First Trust’s FTXO?](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afb178ace4341278ad97fb11f1107b0&url=https%3a%2f%2ffinance.yahoo.com%2fmarkets%2fstocks%2farticles%2fbank-etf-better-buy-state-164318300.html&c=4995188365278588869&mkt=en-us)  
  <sub>Yahoo Finance, 30h ago</sub>  
  The cost gap is wide, but the bigger difference lies in which banks each fund holds and how far each has fallen during market stress.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 72.63 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 72.55 (+0.1%), 50d 71.67 (+1.3%), 200d 71.24 (+2.0%); 50d above 200d
Momentum: RSI(14) 52.4 | MACD 0.402 vs signal 0.415 (histogram -0.013)
Returns: 1d -0.2% | 5d -1.1% | 1m +4.0% | 3m -5.5%
52-week range: 58.63 - 77.93 (now 72.5% of the way up)
Volatility: ATR(14) 1.34 (1.8% of price) | annualised 20d 20.6%
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
Weighted price target: +10.7% above the current prices
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
Share count change: 1 week: -0.2% (-7.77M) over 7d | 1 month: +3.0% (115.58M) over 30d
Shares outstanding: 55.25M | fund size: 4.01B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: the streamed answer ran past the 480s ceiling (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [ETFs Investing in SL Green Realty Corp. Stocks](https://www.tradingview.com/symbols/DUS-GEI/etfs/)  
  <sub>TradingView, 2 hours ago</sub>  
  Explore funds investing in GEI in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [Top Tokenized ETFs by Market Cap](https://www.coingecko.com/en/etfs)  
  <sub>CoinGecko, 1 hour ago</sub>  
  Discover the top ETFs (exchange-traded funds) by tokenized market cap. Track ETF prices alongside their tokenized prices, market cap, and volume on...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 96.85 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 94.77 (+2.2%), 50d 92.98 (+4.2%), 200d 94.92 (+2.0%); 50d below 200d
Momentum: RSI(14) 61.3 | MACD 1.256 vs signal 1.072 (histogram 0.185)
Returns: 1d +0.4% | 5d -0.5% | 1m +5.5% | 3m -0.8%
52-week range: 87.00 - 100.95 (now 70.6% of the way up)
Volatility: ATR(14) 1.34 (1.4% of price) | annualised 20d 19.3%
Volume: 0.09x the 20-day average
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
Weighted price target: +13.3% above the current prices
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
Share count change: 1 week: +1.8% (1.23B) over 7d | 1 month: -1.7% (-1.19B) over 32d
Shares outstanding: 720.30M | fund size: 69.76B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 102.09 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 101.23 (+0.8%), 50d 98.48 (+3.7%), 200d 104.66 (-2.5%); 50d below 200d
Momentum: RSI(14) 52.8 | MACD 1.326 vs signal 1.402 (histogram -0.076)
Returns: 1d +0.0% | 5d -3.7% | 1m +7.6% | 3m -3.6%
52-week range: 92.84 - 121.36 (now 32.4% of the way up)
Volatility: ATR(14) 2.71 (2.7% of price) | annualised 20d 39.3%
Volume: 0.07x the 20-day average
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.1% above the current prices
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
Share count change: 1 week: +2.5% (39.94M) over 7d | 1 month: +5.8% (90.48M) over 30d
Shares outstanding: 16.10M | fund size: 1.64B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected) (Bing's feed, direct: 0 headline(s), none naming XHB)

### US media and communication (XLC) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [State Street Communication Services Select Sector SPDR ETF](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afb17b68bbc424999c1f3168515003d&url=https%3a%2f%2fwww.wsj.com%2fmarket-data%2fquotes%2fetf%2fMX%2fXLC&c=9973890150073057195&mkt=en-us)  
  <sub>Wall Street Journal, 23h ago</sub>  
  No news for XLC in the past two years. Stocks: Real-time U.S. stock quotes reflect trades reported through Nasdaq only; comprehensive quotes and volume reflect trading in all markets and are delayed ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 107.95 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 105.37 (+2.4%), 50d 109.30 (-1.2%), 200d 112.31 (-3.9%); 50d below 200d
Momentum: RSI(14) 53.0 | MACD -0.354 vs signal -1.159 (histogram 0.805)
Returns: 1d -0.7% | 5d +0.5% | 1m -2.1% | 3m -2.3%
52-week range: 99.90 - 120.08 (now 39.9% of the way up)
Volatility: ATR(14) 1.98 (1.8% of price) | annualised 20d 22.3%
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
Weighted price target: +30.4% above the current prices
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
Share count change: 1 week: -3.0% (-663.89M) over 7d | 1 month: -1.4% (-305.96M) over 30d
Shares outstanding: 199.36M | fund size: 21.52B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 429: {"error":{"message":"Model busy, retry later","type":"invalid_request_error","param":null,"code":"engine_overloaded"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [XLEI Vs PEO: The Energy Income Trade For 2027 (NYSEARCA:XLEI)](https://seekingalpha.com/article/4968400-xlei-vs-peo-the-energy-income-trade-for-2027?source=generic_rss)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  The State Street Energy Select Sector SPDR Premium Income ETF (XLEI) and Adams Natural Resources Fund (PEO) both earn Buy ratings.
- [VanEck Semiconductor ETF (SMH) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/SMH/)  
  <sub>Yahoo! Finance Canada, 2 hours ago</sub>  
  Find the latest VanEck Semiconductor ETF (SMH) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Is Wall Street Bullish or Bearish on ONEOK Stock?](https://www.google.com/goto?url=CAESmQEBxCJF11QSRcVWGtQQhMPn-1_iwHl7zPc48UgzCf81snUnrWXnrseO0p_DneKdke7edDnLoDYNAMMUxwQVAzkyIxqoIT4S-KMM-Ovub4q0JjaPUEunsLfeSPnNT0qPsbfzkUyBOkmwLgxvuBBXD_Kn7ffgQqgVXp6AnFLr_iMs846Z5bDqJnUl5n6v4cGKc1U5RF_wTU2dkMo&gsessionid=Xs_lB0WVKYIATexqVOmuIPYFP7PndHuf8N-eY-55DBtP88NPnN0_sQ)  
  <sub>Barchart.com, 4 hours ago</sub>  
  Over the past year, ONEOK has outperformed the broader market, and analysts remain moderately bullish about the stock's prospects.
- [As Q3 earnings season nears end, these 10 energy stocks stand out for EPS beats (XLE:NYSEARCA)](https://www.google.com/goto?url=CAESsQEBxCJF1ydWey4zyKB3dWFQRUzXvOrq6AD3fS9FcFIUSi7HcDRGDFekj5ypsgEubrK_A3EfxN-WqJM0iScBwpB6wC5sfYQEVm3ZAVxVRXKpjfl9NKru6OdrdNZPu_V2cLKGo547MaE6bQnEBZiTvalPQwkA3DlZhJZWc2WeaYUq5RuZaCeUsmjpE7rPGeGwz3bGeYTwTszMEhiOulis93MaC2QgHshemERI08ze5qHw18I&gsessionid=Xs_lB0WVKYIATexqVOmuIPYFP7PndHuf8N-eY-55DBtP88NPnN0_sQ)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Delek US Holdings leads oil and gas companies in third-quarter EPS surprises at $5.43, ahead of Par Pacific at $4.04 and HF Sinclair at $3.92.
- [AI infrastructure sell-off erases $4.2T from industrial, energy stocks (XLE:NYSEARCA)](https://www.google.com/goto?url=CAESpwEBxCJF17S0rioI9bCUWqPAa5DSXrAIGGx4fnoy9z1kq6YyqsmcRboJWEuK_jzAW9ekt46VRb1En8xmFa85rjGC8mxXpStegNuXafMLOhR4rONM9nXrZf4siyrT5pgHuVAXybralXcHoLDwxF4oA16zQ7AS01HqeoqZwQkrcfH6pRI68QRehNkeWziOnpunZn7AIpPYD4azf4vnxsY4IHK2-ItRrxJ97A&gsessionid=Xs_lB0WVKYIATexqVOmuIPYFP7PndHuf8N-eY-55DBtP88NPnN0_sQ)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  Manufacturers, utilities and miners have lost $4.2 trillion in market value since June as AI infrastructure enthusiasm fades; Caterpillar fell 44%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 64.14 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 65.99 (-2.8%), 50d 64.99 (-1.3%), 200d 59.54 (+7.7%); 50d above 200d
Momentum: RSI(14) 46.3 | MACD -0.581 vs signal -0.276 (histogram -0.305)
Returns: 1d -1.3% | 5d +3.6% | 1m -6.0% | 3m +0.7%
52-week range: 43.81 - 70.02 (now 77.6% of the way up)
Volatility: ATR(14) 1.55 (2.4% of price) | annualised 20d 30.7%
Volume: 0.16x the 20-day average
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
Weighted price target: +10.4% above the current prices
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
Shares outstanding: 186.42M | fund size: 11.96B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [UBS ETF (CH)-UBS Palladium ETFN (UFU2.HA) latest stock news and headlines](https://uk.finance.yahoo.com/quote/UFU2.HA/news/)  
  <sub>20 hours ago</sub>  
  Get the latest UBS ETF (CH)-UBS Palladium ETFN (UFU2.HA) stock news and headlines to help you in your trading and investment decisions.
- [Glbl X DAX Covered Call ETF R (DYLD.MU) latest stock news and headlines](https://uk.finance.yahoo.com/quote/DYLD.MU/news/)  
  <sub>12 hours ago</sub>  
  Munich - Delayed Quote • EUR. Glbl X DAX Covered Call ETF R (DYLD.MU). 14.72 0.00 (0.00%). At close: 13 November at 8:00:55 CET. Related ETF news...
- [XLF Dec 2026 52.500 put (XLF261204P00052500) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAEScwHEIkXXf5ygKBSzh_9vlho3MGFHTbXPnEQiTBAq-1A9agMn8tMzHgCe8_aAGewu-wcAOPZ9Sd7SHqAq_sLz1-rqkH7o_77INDOw5woCsQuWJA7AtDDo26aRRUsT1fUAyGxgOQjff0v1hGdK5PXPzRo8J2U&gsessionid=pY6TYUOprZTU0mcB-5zBc5EnKYOwPK3TPIL0n2HixhS6xEp30N6LSw)  
  <sub>8 hours ago</sub>  
  Find the latest XLF Dec 2026 52.500 put (XLF261204P00052500) stock quote, history, news and other vital information to help you with your stock trading and...
- [HCM Select 50 ETF (FIFT) interactive stock chart](https://www.google.com/goto?url=CAESawHEIkXX-KIwpnKwgrT-S8Cx4c4E63YEDyxOnk2dAWpelM_p-zzL2SG3ynLJgOpFSu0oEcRRMvbekIE768mBjK_f8X0E-DstRWJvW9XOnHqZFXwnHOEtjZwkDvRm_X3fm58C7CSPfgWk2B7Z&gsessionid=pY6TYUOprZTU0mcB-5zBc5EnKYOwPK3TPIL0n2HixhS6xEp30N6LSw)  
  <sub>13 hours ago</sub>  
  Interactive chart for HCM Select 50 ETF (FIFT) – analyse all of the data with a huge range of indicators.
- [L&G Emerging Markets Corporate Bond (USD) Screened UCITS ETF USD Accumulating (EMAU.SW)](https://www.google.com/goto?url=CAESbQHEIkXXmzj_U7tIotfUdrv2TCgOnygGCDrdHD6eB9z8Zyxas0JSECl0ZtbhFsumSbGBVA4RlWzuL9dXGpRVoUx00uRX2BGwdy79C4cyhxKS8kdHZfUxMyD-ZGPf0qsKsvm4pqivOhOJ7t3uK5U&gsessionid=pY6TYUOprZTU0mcB-5zBc5EnKYOwPK3TPIL0n2HixhS6xEp30N6LSw)  
  <sub>21 hours ago</sub>  
  Get the latest L&G Emerging Markets Corporate Bond (USD) Screened UCITS ETF USD Accumulating (EMAU.SW) stock news and headlines to help you in your trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 58.63 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 57.24 (+2.4%), 50d 55.98 (+4.7%), 200d 53.97 (+8.6%); 50d above 200d
Momentum: RSI(14) 61.4 | MACD 0.806 vs signal 0.679 (histogram 0.127)
Returns: 1d -0.1% | 5d +1.1% | 1m +5.6% | 3m +1.4%
52-week range: 47.81 - 59.20 (now 95.0% of the way up)
Volatility: ATR(14) 0.85 (1.4% of price) | annualised 20d 21.3%
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
Weighted price target: +5.2% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 883.44M | fund size: 51.80B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 429: {"error":{"message":"Model busy, retry later","type":"invalid_request_error","param":null,"code":"engine_overloaded"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [BTIG flags consumer staples beating tech by 33%, the widest gap in about 25 years](https://cryptobriefing.com/btig-consumer-staples-outperform-tech-warning/)  
  <sub>Crypto Briefing, 2 hours ago</sub>  
  Jonathan Krinsky notes the last time defensives lapped tech this hard was the opening stretch of the dot-com bust. by Vivian Nguyen.
- [SCHD Dethrones VIG: Why $27 Billion Inflow Made Me Cautious Of Dividend ETFs (Rating Downgrade)](https://seekingalpha.com/article/4968510-schd-dethrones-vig-why-27-billion-inflow-made-me-cautious-of-dividend-etfs-rating-downgrade)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  We downgrade the Schwab U.S. Dividend Equity ETF to Hold and the Vanguard Dividend Appreciation ETF to Buy as the rotation's runway shortens.
- [Tradr 2X Long AAOI Daily ETF (AAOX) stock price, news, quote and history](https://www.google.com/goto?url=CAESZQHEIkXXCpesr8SOlZoOZfONxzBDuefPHuyg9hacUA6jO_epUkwF_-41BnVlanLPrsehNcIx8vYVugCV0YIgtNlgdy7kOQp-68VTKCC1blMp23Slq7O7gmgMpyoNr3IYbib2U8e7&gsessionid=LpKSCiqL5fQrPOPzTS5dlQatVTnhO4Rt2otDPe9s-JOaY_UC25-1Yg)  
  <sub>Yahoo Finance Singapore, 3 hours ago</sub>  
  Find the latest Tradr 2X Long AAOI Daily ETF (AAOX) stock quote, history, news and other vital information to help you with your stock trading and...
- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Friday as Producer Inflation Trails Forecasts](https://www.google.com/goto?url=CAESpwEBxCJF1xPulyZxT6HVygY2HD7x071EYulX1XNDyWJdugiF5qRF7N8ab3HKVhK9DqN0FpZYItLH8lyi7L9ccJqEJGgixcz5-VJ7-OH4uKG-uIagDLB5vWVU329FRcIPxkD2lGt72qTCZ-WuXhY3mBveI-aMp8hnRa9e8WkF0ePQAuuZ1XeIHxQxJdOPbIM2JKIisILbVCja1iNQm9SiSOhOLP-pvpYPbA&gsessionid=LpKSCiqL5fQrPOPzTS5dlQatVTnhO4Rt2otDPe9s-JOaY_UC25-1Yg)  
  <sub>Moomoo, 9 hours ago</sub>  
  Thebroad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.4% and the actively traded Invesco QQQ Trust (QQQ) was 0.2% higher in Friday's...
- [BTIG Strategist Puts Staples’ Edge Over Tech at 33%, Widest in About 25 Years](https://www.google.com/goto?url=CAESawHEIkXXUc4_-TriJYclwMWbTvEspJ1lLUIkYjpRtRqhhn-ls1pxvjTneJO6sgW_xtwWEGsTuyauu2nwS49x_wygwtTLMS_o3WkFRhipuAK1LM5f09H3TzmihERNBvDxGLuZU-gOVHTrZCxW&gsessionid=LpKSCiqL5fQrPOPzTS5dlQatVTnhO4Rt2otDPe9s-JOaY_UC25-1Yg)  
  <sub>www.tokenpost.com, 1 hour ago</sub>  
  XLP rose 10.9% in October while XLK fell 8.3%; BTIG Chief Technical Strategist Jonathan Krinsky compared the sector split with the early dot-com bust.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 92.97 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 89.77 (+3.6%), 50d 85.82 (+8.3%), 200d 84.93 (+9.5%); 50d above 200d
Momentum: RSI(14) 66.7 | MACD 1.811 vs signal 1.684 (histogram 0.127)
Returns: 1d +0.7% | 5d +2.3% | 1m +6.1% | 3m +8.6%
52-week range: 76.51 - 92.97 (now 100.0% of the way up)
Volatility: ATR(14) 1.47 (1.6% of price) | annualised 20d 23.8%
Volume: 0.19x the 20-day average
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +1.0% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 210.17M | fund size: 19.54B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Glbl X DAX Covered Call ETF R (DYLD.MU) latest stock news and headlines](https://uk.finance.yahoo.com/quote/DYLD.MU/news/)  
  <sub>Yahoo Finance UK, 12 hours ago</sub>  
  Munich - Delayed Quote • EUR. Glbl X DAX Covered Call ETF R (DYLD.MU). 14.72 0.00 (0.00%). At close: 13 November at 8:00:55 CET. Related ETF news...
- [Tradr 2X Long AAOI Daily ETF (AAOX) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/AAOX/)  
  <sub>Yahoo Finance Singapore, 3 hours ago</sub>  
  Find the latest Tradr 2X Long AAOI Daily ETF (AAOX) stock quote, history, news and other vital information to help you with your stock trading and...
- [UBS ETF (CH)-UBS Palladium ETFN (UFU2.HA) latest stock news and headlines](https://www.google.com/goto?url=CAESbQHEIkXXdCjv9H_yOxthnl5MnfjmrYNK5KhN7CNO8sFA63intKCej7ijTJcbqHbSJBzBjgtkNP1jpVk5rJr3zuIOnKWpPFS67DbikkmKurousKz02eap9hfZukBY6okywue8_x-YLVUQq5y0T28&gsessionid=oMqOKKwIly6eRzimC8ZX7E-9AxPwvJRTJk_FiZ_qbdevJiXC1x5r-A)  
  <sub>Yahoo Finance UK, 20 hours ago</sub>  
  Get the latest UBS ETF (CH)-UBS Palladium ETFN (UFU2.HA) stock news and headlines to help you in your trading and investment decisions.
- [Biotech ETFs Face Crucial FDA Week as Drug Catalysts Loom - State Street SPDR S&P Biotech ETF (ARCA:XBI)](https://www.google.com/goto?url=CAESywEBxCJF1-T1skGgMc9buFI9VBn88Trr7d6bLPvSiGcv6CIHWTbd0SQndI8fjy32i1amW6biZAaj9MmphHZzdYZtOLH4os2YorJE9WOcqEwf11huZ99DDnNJ-7SbCNUotWWx-qKpWgwpX6sankL_3AW9noHbc9wJOTR89Jmdy39ZiN1_Q1Hw68x--lap01PS6MV4sLLX3BWzGycVCy9pSCL6MXKpE2fHrlBFnJcrBP86l9XP5mBsuaH9G6Dzcm8x7FNWoBMYdjNOGyU9TQ&gsessionid=oMqOKKwIly6eRzimC8ZX7E-9AxPwvJRTJk_FiZ_qbdevJiXC1x5r-A)  
  <sub>Benzinga, 24 minutes ago</sub>  
  XBI and IBB lagged SPY and QQQ as two FDA decisions and fresh Alzheimer's and obesity-drug data put biotech ETFs in focus.
- [L&G Emerging Markets Corporate Bond (USD) Screened UCITS ETF USD Accumulating (EMAU.SW)](https://www.google.com/goto?url=CAESbQHEIkXX-xGH8pOdE4bX1IM9OFJrC4NQ_YzHkVi8sHGP9AjdKKXI9x10N6THIcaJV5KKp7D30LxA8XtgCPIuaUQLg1lz2hATdTMFu0kitt5dIYwgtVCHrB_55CG6l0jgqg9ph5nT8rOGNXVkBOE&gsessionid=oMqOKKwIly6eRzimC8ZX7E-9AxPwvJRTJk_FiZ_qbdevJiXC1x5r-A)  
  <sub>Yahoo Finance UK, 21 hours ago</sub>  
  Get the latest L&G Emerging Markets Corporate Bond (USD) Screened UCITS ETF USD Accumulating (EMAU.SW) stock news and headlines to help you in your trading...
- [Xtr.II-ESG Gl Govt Bd A (XGVC.MU) interactive stock chart](https://www.google.com/goto?url=CAESbgHEIkXX7ODvfj9tB72wtobkVR9JALvtItwz0ZFox-q830C5j_lI33w9qpnY-X2LNbWoCEmO5zZy5sMwI2xsivpMfdUpv1kqdXWNbvYMdf34dXXppvkfM_Texnu9Gvp6klbdaZzdN1ofDT4DBuYz&gsessionid=oMqOKKwIly6eRzimC8ZX7E-9AxPwvJRTJk_FiZ_qbdevJiXC1x5r-A)  
  <sub>Yahoo Finance UK, 20 hours ago</sub>  
  Interactive chart for Xtr.II-ESG Gl Govt Bd A (XGVC.MU) – analyse all of the data with a huge range of indicators.
- [WISDOMTREE ISSUER WSDMTR CLOUD (KLWD.AQ) interactive stock chart](https://www.google.com/goto?url=CAESbgHEIkXXAWiIoUVWjCgYY7vjmMbR5NlWPgilMuUZA88ik_gxr9w22Q8hfOQfEQgzGzHbNErus9QNWcYD3L3isKFRTrzXCCAs1gruCX2hRJrT7P9ifGOcPaSB0JHEZgikgJBBkRVuZ9nXDj9K29mM&gsessionid=oMqOKKwIly6eRzimC8ZX7E-9AxPwvJRTJk_FiZ_qbdevJiXC1x5r-A)  
  <sub>Yahoo Finance UK, 15 hours ago</sub>  
  Interactive chart for WISDOMTREE ISSUER WSDMTR CLOUD (KLWD.AQ) – analyse all of the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 190.40 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 184.38 (+3.3%), 50d 175.42 (+8.5%), 200d 160.38 (+18.7%); 50d above 200d
Momentum: RSI(14) 69.1 | MACD 4.099 vs signal 3.960 (histogram 0.139)
Returns: 1d +0.8% | 5d +1.1% | 1m +7.7% | 3m +12.2%
52-week range: 142.84 - 190.40 (now 100.0% of the way up)
Volatility: ATR(14) 3.26 (1.7% of price) | annualised 20d 20.7%
Volume: 0.10x the 20-day average
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
Weighted price target: +3.0% above the current prices
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
Share count change: 1 week: -1.5% (-758.62M) over 7d | 1 month: +3.0% (1.43B) over 32d
Shares outstanding: 261.58M | fund size: 49.81B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- CFTC positioning: net long 18.8% of OI, down 0.9% week‑over‑week, 90th percentile crowding
- Fund flows: share count up 23.5% over the past month
- Cost of holding: -7.6% annual roll cost versus sugar spot
- Technicals: price 11.04 below 20‑day SMA (11.44) and 50‑day SMA (11.59), RSI 39.4
- Macro: Treasury yields rose modestly, dollar up 1.86%, VIX at 20.5

<details><summary><b>News</b> — score +0.00</summary>

- [Sugar Prices Face Seasonal Headwinds: Will Energy Markets Add More Selling Pressure?](https://www.barchart.com/story/news/8854893/sugar-prices-face-seasonal-headwinds-will-energy-markets-add-more-selling-pressure)  
  <sub>Barchart.com, 56 minutes ago</sub>  
  Sugar may not attract the same attention as crude oil, gold, or the stock indexes. Still, experienced commodity traders know some of the most interesting...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 11.04 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 11.44 (-3.5%), 50d 11.59 (-4.8%), 200d 10.31 (+7.1%); 50d above 200d
Momentum: RSI(14) 39.4 | MACD -0.206 vs signal -0.161 (histogram -0.045)
Returns: 1d -0.9% | 5d +0.5% | 1m -10.4% | 3m -1.3%
52-week range: 9.02 - 12.47 (now 58.6% of the way up)
Volatility: ATR(14) 0.20 (1.8% of price) | annualised 20d 27.2%
Volume: 0.02x the 20-day average
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
Cost of holding this fund instead of sugar itself: -7.6% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -1.3%, commodity +4.8%, gap -6.0% | 6 months: fund +11.2%, commodity +24.2%, gap -13.1% | 12 months: fund +19.1%, commodity +26.7%, gap -7.6%
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
Share count change: 1 week: +1.3% (745.98K) over 7d | 1 month: +23.5% (11.21M) over 30d
Shares outstanding: 5.34M | fund size: 58.93M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, modest bearish tilt from positioning and fund outflows, heavy cost of holding discourages long exposure.

**Main reasons it gave:**
- Positioning: net long 0.5% of OI, down -3.9% week
- Fund flows: -10.9% share count over 1 month (outflows)
- Cost of holding: -7.1% annual cost vs commodity (heavy roll cost)
- Technicals: price below 20d, 50d, 200d SMAs, RSI 32.2 (downtrend)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 17.09 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 17.41 (-1.8%), 50d 18.54 (-7.8%), 200d 18.18 (-6.0%); 50d above 200d
Momentum: RSI(14) 32.2 | MACD -0.368 vs signal -0.407 (histogram 0.040)
Returns: 1d -0.5% | 5d -0.4% | 1m -6.0% | 3m -7.2%
52-week range: 16.47 - 20.29 (now 16.2% of the way up)
Volatility: ATR(14) 0.23 (1.3% of price) | annualised 20d 12.6%
Volume: 0.29x the 20-day average
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
Cost of holding this fund instead of corn itself: -7.1% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -7.2%, commodity -4.1%, gap -3.1% | 6 months: fund -8.8%, commodity -6.9%, gap -1.9% | 12 months: fund -6.5%, commodity +0.6%, gap -7.1%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.40</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-11-03, published the following Friday)
Large speculators: net long 0.5% of open interest (1,918,622 contracts)
Change on the week: -3.9% of open interest
Crowding: 45% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +0.3% (371.39K) over 7d | 1 month: -10.9% (-13.07M) over 30d
Shares outstanding: 6.27M | fund size: 107.11M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error response body was rejected) (Bing's feed, direct: 4 headline(s), none naming CORN)

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Price below 20‑day, 50‑day, and 200‑day SMAs; RSI 33.2 (bearish technicals)
- Share count up ~1% over the past month, indicating net inflows
- Cost of holding -2.4% annual drag on long exposure
- Positioning: net long 10.6% of OI, down 1.4% week‑over‑week, crowded short (2% percentile)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 36.49 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 38.55 (-5.3%), 50d 39.35 (-7.2%), 200d 37.97 (-3.9%); 50d above 200d
Momentum: RSI(14) 33.2 | MACD -0.736 vs signal -0.507 (histogram -0.229)
Returns: 1d -0.1% | 5d -5.0% | 1m -7.6% | 3m -6.9%
52-week range: 30.77 - 41.43 (now 53.7% of the way up)
Volatility: ATR(14) 0.65 (1.8% of price) | annualised 20d 24.7%
Volume: 0.15x the 20-day average
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
Cost of holding this fund instead of copper itself: -2.4% a year -- a steady drag
Measured: 3 months: fund -6.9%, commodity -6.5%, gap -0.4% | 6 months: fund -5.0%, commodity -3.3%, gap -1.6% | 12 months: fund +16.7%, commodity +19.2%, gap -2.4%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-11-03, published the following Friday)
Large speculators: net long 10.6% of open interest (327,850 contracts)
Change on the week: -1.4% of open interest
Crowding: 2% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +1.1% (7.24M) over 7d | 1 month: +1.0% (6.37M) over 30d
Shares outstanding: 17.77M | fund size: 648.65M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance given mixed signals: macro pressures on gold are bearish but no clear surprise or decisive technical break; positioning shows slight unwinding, while low cost of holding is mildly supportive of a long.

**Main reasons it gave:**
- US Treasury yields rose (10‑yr +27 bps), raising real yields and pressure on gold
- Technicals: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 38.5, MACD negative, indicating bearish momentum
- CFTC positioning: net long 26% of OI, down 0.6% week‑over‑week, suggesting slight unwinding of longs
- Cost of holding low at 0.5% annual, reducing drag for a long position

<details><summary><b>News</b> — score +0.00</summary>

- [Harvard, Dartmouth keep Bitcoin ETF stakes steady as fund gains 42% in Q3](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afb18eb1b824413b5a5de547bdc8e9c&url=https%3a%2f%2fcointelegraph.com%2fnews%2fharvard-dartmouth-bitcoin-etf-ibit-up-q3&c=15968316985806849495&mkt=en-us)  
  <sub>Cointelegraph, 14h ago</sub>  
  Harvard and Dartmouth held Bitcoin ETF stakes worth $144.1 million and $9.5 million in Q3, while Harvard boosted its gold ETF holdings.
- [Gold Is Down 30%. The Real Question Is Who Sets the Price.](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afb18eb1b824413b5a5de547bdc8e9c&url=https%3a%2f%2fwww.ainvest.com%2fnews%2fgold-30-real-question-sets-price-2611%2f&c=14001600483940810571&mkt=en-us)  
  <sub>ainvest, 16h ago</sub>  
  Gold fell 30% in 2026 as Fed rate hikes pushed real yields above 2.6%, making bonds more attractive than non-yielding gold.
- [Bank of Korea Expands Gold Bets, ETF Holdings Near 490 Billion Won](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afb18eb1b824413b5a5de547bdc8e9c&url=https%3a%2f%2fen.sedaily.com%2feconomy%2f2026%2f11%2f16%2fbank-of-korea-expands-gold-bets-etf-holdings-near-490&c=519253876872776935&mkt=en-us)  
  <sub>en.sedaily, 16h ago</sub>  
  The Bank of Korea's gold ETF holdings neared 490 billion won at the end of September as the central bank expanded its gold exposure this year.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 356.04 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 367.60 (-3.1%), 50d 379.89 (-6.3%), 200d 407.97 (-12.7%); 50d below 200d
Momentum: RSI(14) 38.5 | MACD -5.660 vs signal -4.888 (histogram -0.772)
Returns: 1d +0.2% | 5d -6.2% | 1m -6.8% | 3m -10.7%
52-week range: 354.89 - 495.90 (now 0.8% of the way up)
Volatility: ATR(14) 6.61 (1.9% of price) | annualised 20d 28.0%
Volume: 0.11x the 20-day average
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
Cost of holding this fund instead of gold itself: 0.5% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund -10.7%, commodity -12.2%, gap +1.6% | 6 months: fund -14.9%, commodity -14.9%, gap -0.0% | 12 months: fund -7.0%, commodity -7.5%, gap +0.5%
A commodity fund holds futures, not gold, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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
Shares outstanding: 260.30M | fund size: 92.68B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US Treasury yields rose modestly across the curve, no policy surprise
- Technical indicators show price well below 20‑, 50‑ and 200‑day SMAs, RSI 29.2, but no decisive breakout on volume
- CFTC data shows net long 3.5% of OI, change +0.6% week‑over‑week, crowding indicates short bias but not a clear signal
- Fund flows show a 4% share count decline over the past month, indicating outflows
- Cost of holding the fund is 1.1% per year, a modest drag for long positions

<details><summary><b>News</b> — score +0.00</summary>

- [SLV’s $149,842 Gain on a $300,000 Sale Could Be Taxed as a Collectible, Not a Stock](https://247wallst.com/investing/etf/2026/11/15/slvs-149842-gain-on-a-300000-sale-could-be-taxed-as-a-collectible-not-a-stock/)  
  <sub>24/7 Wall St., 13 hours ago</sub>  
  SLV holds physical silver in a grantor trust, so the IRS taxes its gains as collectibles at up to 28%, not stock fund rates. The 28% rate is only a ceiling:...
- [Silver ETFs crash up to 5% today as global demand forecast to fall 5% in 2026; gold ETFs also decline](https://www.google.com/goto?url=CAES4AEBxCJF180VMoh6raqShIZvx9JG4vRKzh0HJnKh5AeVOMwvH_coKHStn3rhw8cAHFs9FArEbelwvfnzMwhn5pZl9uB71LYD4AL-KFZV6cKvt23YmaV7LKU5LUgvM7WBcFkFWZGQdWqA1Cn0nOWyi7UJ95vv7DmKSOF_Qlb9Uf71ESgfhRK2keGxJ1GzfWeE2Ia2mHZc0RcUcDcuIW-kjiSJVZxWyjtFYMcAjYpLEi-3XqMadAQUyXwGvsnkPuhXxzCaPQjmuYwN7Ki4_Hy02d0Q9748I2j1ad9ppbNujF0dTA&gsessionid=oUtK_2glR8EoOM-2dsJ7ig0PDoi2Xoe5wkA4veuLqB0hdB4gEjK_cg)  
  <sub>Moneycontrol.com, 6 hours ago</sub>  
  Silver exchange-traded funds (ETFs) plunged nearly 5 percent on Monday, November 16, amid a sharp correction in precious metal prices and fresh concerns...
- [Silver ETFs fall nearly 5% as global demand concerns grow | Industrial demand is expected to fall 3% | Inshorts](https://www.google.com/goto?url=CAESpAEBxCJF1_XmINx7vo6SH_A2KsS3Nt_4S_icgJSZB70vLEAjZFyN8E8sFB6dIITosWrqYMwYu6mhILquoVS1pndcZmw26ZZLWRSveedWn4wLfzTo211MqVmnyXVz7Egr3oBH2syCQhjo7VVlZ_hM0cZmSJATejg8OudxgTxc2ugIymFrgNARbs6YxX-HX7JldDhIhsR_KsV7gOkABLrfK-261TWEnA&gsessionid=oUtK_2glR8EoOM-2dsJ7ig0PDoi2Xoe5wkA4veuLqB0hdB4gEjK_cg)  
  <sub>Inshorts, 5 hours ago</sub>  
  Silver ETFs fell nearly 5 on Monday, tracking a sharp decline in precious metal prices amid concerns over global demand. A report forecast a 5 drop in...
- [Silver ETF Crash Along with gold and silver ETFs also crash Big shock to investors](https://www.google.com/goto?url=CAESsAEBxCJF131DxfcyJGlDGPwdz9ikGfyxdGt6WROjNdsX88KxO9d_npFRqirm86aOo1GXu9yEQcRFMeBVDLze503qj_wag4XYon2bmUXCDfpbqfzbWLNnsO3VPKy7vHXGjI1VCvL5cbVwvT4iuOwJ1IW3p3Xgnn50Wuc89XpXTz8TUx9idTMwDg308wfoSKltI1vIm5BROTMeu_tOkBsJ2PI31dWpDYJpe8pHCTgxF6J3kw&gsessionid=oUtK_2glR8EoOM-2dsJ7ig0PDoi2Xoe5wkA4veuLqB0hdB4gEjK_cg)  
  <sub>Sandesh, 6 hours ago</sub>  
  Gold and silver prices continue to decline, while investors in gold and silver ETFs are also facing significant losses amid the ongoing fall in precious...
- [Silver could hit $75 an ounce next year as macro headwinds ease: BofA](https://www.google.com/goto?url=CAESuwEBxCJF14n4kd1Ckx9yPJyftUTjuDBimjZoUGJyYKsvHMMJ23j7u0sXQFjesTkONhL8tCPZxsE8vUw1yP-5I3cVRH61mQeNUsDojh9eMT1w-g73bgJnWWE-_QXV_ZHVhKZq37ze5-upmK6XpHY3OwqutrnZ2IXzNO5SycINAhn4iYhrEX6m2t6_qigA_FDDVaw_eHUnnVv4UaaBDZQ1B_qTH5SRyQb8Q9CCcWjaTvJzEi2bcaZjcMYuWM-T&gsessionid=oUtK_2glR8EoOM-2dsJ7ig0PDoi2Xoe5wkA4veuLqB0hdB4gEjK_cg)  
  <sub>StreetInsider, 3 hours ago</sub>  
  Investing.com -- Silver could climb to $75 an ounce next year as macro headwinds that have weighed on precious metals ease, according to Bank of America.
- [Silver price today: Silver declines, FXStreet data shows](https://www.google.com/goto?url=CAESuwEBxCJF1y0ANs1tgiRMY8E5UZtCU0gXlKaHMQuGVAOv2HHv_eM0YxH7DEqqQ5KP4TL5L9Far_PwJvlHqOMNNjUOjzOfjBJZgrDcFRVb8mwlXZb_Nf3_Z65J9_JvScNANeJ7CHgWiYfSfRx_HpETE5bn0wJB-wBRnNvqaoKyvSJBVNeM5D2QD2cv2TaSU8Sdf3kWKz7rScMtsV0fJ1IB2tROrJPoukqC5UpIP54KXRqID_4UG_rjCSLYxbk6&gsessionid=oUtK_2glR8EoOM-2dsJ7ig0PDoi2Xoe5wkA4veuLqB0hdB4gEjK_cg)  
  <sub>www.tmgm.com, 5 hours ago</sub>  
  Silver (XAG/USD) came under pressure on Monday, with FXStreet data showing a 2.77% decline from Friday's $48.88 to $47.52 per troy ounce.
- [First Majestic Silver Corp. (AG.TO) Stock Price, News, Quote & History](https://www.google.com/goto?url=CAESZQHEIkXX4XXCmxM8ZCY-v0XsYH64dmDXpcv4Q40U3lJ4LOVdPe-l3PklzfMa4RH4Be5WWCjPJAhYebLR_nBWZDX81lWsprOs1W8C9q-ZHtIOJ2Hel6vT1f4nYM9FOxggQrh6nkjQ&gsessionid=oUtK_2glR8EoOM-2dsJ7ig0PDoi2Xoe5wkA4veuLqB0hdB4gEjK_cg)  
  <sub>Yahoo! Finance Canada, 23 hours ago</sub>  
  Find the latest First Majestic Silver Corp. (AG.TO) stock quote, history, news and other vital information to help you with your stock trading and...
- [Silver Price Forecast: Can XAG/USD halt its slide below $47.50 as it hits fresh YTD lows?](https://www.google.com/goto?url=CAESzAEBxCJF1zOI2oc7lNayi5AEhs0YGXWIvtpK89KQvHBZ9c_WHJlFnamsYMo2ybYM6OER60sGeCdLImWsDAibAVTwbY6ma7iTed3QjUZFoQy_FGeuls4SAmLpYQX0c2-3NT57QZMwT1rfEmtQtw4QMywlfG_4Hr2EesRof71bAPLURtiGh7UxdxFVLpAh3XXsnmeW8xixWvh9lTn7WbYjqB-J4DzMv7m9jlnfjM--V_DT4yZRDE3vPa-3pg0MqqQEHlqbY45r55qNZ5PdW6E&gsessionid=oUtK_2glR8EoOM-2dsJ7ig0PDoi2Xoe5wkA4veuLqB0hdB4gEjK_cg)  
  <sub>www.tmgm.com, 7 hours ago</sub>  
  Silver (XAG/USD) slips further below the mid-$47.00s in Monday's early European session, touching its lowest level since November 2025.
- [Silver price today, November 16, 2026: Silver under pressure from several unfavorable factors.](https://www.google.com/goto?url=CAESmAEBxCJF1-TAUAMEiMR9J_-OuHup7J0Wvhf2S5-REog4zwFIJHAwgtsRa5_D09IBbB1Cv9UKEH_2nvAndxdAPBrt6cRX_i_NIV9A3Fs0xajsHMa0Xg0oWs3sPnkbztnLpSFTNoRtkblhRxKHuK1vqUEIPhKLhs3OXmmGfSX6yRxhlysx3t_wa5wzF_yVphhZaWm1LgpjN3JnNg&gsessionid=oUtK_2glR8EoOM-2dsJ7ig0PDoi2Xoe5wkA4veuLqB0hdB4gEjK_cg)  
  <sub>Vietnam.vn, 15 hours ago</sub>  
  Today's silver price (November 16, 2026) declined due to pressure from ETF outflows and rising US bond yields.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 42.67 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 47.29 (-9.8%), 50d 52.53 (-18.8%), 200d 61.75 (-30.9%); 50d below 200d
Momentum: RSI(14) 29.2 | MACD -2.278 vs signal -2.184 (histogram -0.094)
Returns: 1d -3.3% | 5d -11.4% | 1m -17.2% | 3m -25.7%
52-week range: 42.67 - 105.60 (now 0.0% of the way up)
Volatility: ATR(14) 1.53 (3.6% of price) | annualised 20d 43.8%
Volume: 0.28x the 20-day average
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
Cost of holding this fund instead of silver itself: 1.1% a year -- the roll has been paying this fund
Measured: 3 months: fund -25.7%, commodity -26.2%, gap +0.5% | 6 months: fund -39.0%, commodity -38.8%, gap -0.2% | 12 months: fund -10.0%, commodity -11.1%, gap +1.1%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-11-03, published the following Friday)
Large speculators: net long 3.5% of open interest (115,583 contracts)
Change on the week: +0.6% of open interest
Crowding: 8% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +0.2% (40.32M) over 7d | 1 month: -4.0% (-933.36M) over 32d
Shares outstanding: 529.30M | fund size: 22.59B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance due to lack of macro surprise and no decisive technical break, despite modest bearish behavioural signals.

**Main reasons it gave:**
- Positioning: net long decreased by 4.9% of open interest week‑over‑week
- Fund flows: share count down 7.6% over the past month, indicating outflows
- Cost of holding: low annual cost of 0.4%, minimal drag on performance
- Technicals: price below 20‑day SMA, RSI 42, no decisive break in momentum
- Macro: yields rose modestly, dollar up, VIX moderate, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 25.82 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 26.01 (-0.7%), 50d 26.95 (-4.2%), 200d 25.30 (+2.1%); 50d above 200d
Momentum: RSI(14) 42.1 | MACD -0.328 vs signal -0.375 (histogram 0.047)
Returns: 1d -0.6% | 5d +2.4% | 1m -3.9% | 3m +0.1%
52-week range: 21.71 - 28.14 (now 63.9% of the way up)
Volatility: ATR(14) 0.29 (1.1% of price) | annualised 20d 14.5%
Volume: 0.20x the 20-day average
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
Cost of holding this fund instead of soybeans itself: 0.4% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +0.1%, commodity +2.3%, gap -2.2% | 6 months: fund +2.6%, commodity +1.3%, gap +1.3% | 12 months: fund +8.9%, commodity +8.5%, gap +0.4%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

```text
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-11-03, published the following Friday)
Large speculators: net long 14.9% of open interest (959,576 contracts)
Change on the week: -4.9% of open interest
Crowding: 43% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -1.5% (-589.68K) over 7d | 1 month: -7.6% (-3.23M) over 30d
Shares outstanding: 1.53M | fund size: 39.42M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected) (Bing's feed, direct: 2 headline(s), none naming SOYB)

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Crowded net short position (13.4% OI) with slight reduction (-1.2% OI)
- US natural gas inventories high (94th percentile) with a 61 BCF build
- EIA price outlook mixed: short-term rise to $3.03 in 3 months, then decline to $2.37 in 6 months
- Technical downtrend (price below 50‑day and 200‑day SMA) and low volume

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 9.83 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 9.70 (+1.3%), 50d 10.27 (-4.3%), 200d 10.98 (-10.5%); 50d below 200d
Momentum: RSI(14) 47.4 | MACD -0.065 vs signal -0.173 (histogram 0.108)
Returns: 1d -3.2% | 5d -2.5% | 1m -7.8% | 3m -2.7%
52-week range: 9.00 - 16.90 (now 10.5% of the way up)
Volatility: ATR(14) 0.38 (3.9% of price) | annualised 20d 45.5%
Volume: 0.08x the 20-day average
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
Cost of holding this fund instead of natural gas itself: -1.6% a year -- a steady drag
Measured: 3 months: fund -2.7%, commodity +13.8%, gap -16.4% | 6 months: fund -14.8%, commodity +4.4%, gap -19.2% | 12 months: fund -33.6%, commodity -32.0%, gap -1.6%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.30</summary>

```text
US inventories, week ending 2026-11-06 (published the following Wednesday)
  Natural gas: 3,862.0 billion cubic feet, +61.0 on the week (a build), 94% percentile over 52 weeks -- high for the time of year
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 13.4% of open interest (1,678,554 contracts)
Change on the week: -1.2% of open interest
Crowding: 2% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -11.6% (-61.70M) over 7d | 1 month: +16.1% (65.50M) over 32d
Shares outstanding: 48.03M | fund size: 472.14M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error response body was rejected) (Bing's feed, direct: 9 headline(s), none naming UNG)

### Oil (USO) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Energy inventories show builds in crude (+4.7M barrels), gasoline (+1.8M), diesel (+4.1M) – bearish supply excess
- EIA price outlook forecasts WTI to fall from $97 to $84 in six months (~13% decline) – bearish
- CFTC positioning: net long decreased by 0.5% of open interest, net long only 1.1% – slight bearish
- Fund flows: share count up 17.5% over past month, indicating inflows – bullish

<details><summary><b>News</b> — score +0.00</summary>

- [USO Dec 2026 143.000 put (USO261204P00143000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/USO261204P00143000/chart/)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>
- [Real-Time Stock News, SEC Filings & Alerts](https://www.quantisnow.com/etfs)  
  <sub>Quantisnow, 12 hours ago</sub>  
  Browse US-listed exchange-traded funds A to Z, with latest price, daily change and one-year return. ETFs are funds, not companies.
- [Where Smart Money Flows | A Market Rebound, a Split AI Trade, and Mixed ASX Momentum](https://www.google.com/goto?url=CAESpgEBxCJF16UQI68cnuCKYjUVAIwC9ud8m0meoEgAm01CQG5W30hkqKGiDY9WOV2C05lcLOzrTJqn-AfyMlzAGAvJDbpdRi1dW9VhZ8FS7cuD2GBdrM6mEunfve0yoYT_42R-mSWvSdhv4W6v2Nk5dx8DjNtNY4BSiLYa3kOprGgY1Fk3NGhYfYr-eyR2q9H_3h0Xb7RhoNxw-JHxb0g8jIHiwgvhbGgm&gsessionid=hRtVWwgjUD1BjLxYz81pIMd0U2YAN_Hxw6PblmmdZALqYWmjQo7Cyg)  
  <sub>Moomoo, 9 hours ago</sub>  
  Weekly Market Update U.S. equities recovered last week, but the headline rebound masked a sharp split within the AI trade. The $S&P 500 Index (.SPX.US...
- [BITCOIN: On-Chain Handoff — Reading Who Sells to Whom para CRYPTO:BTCUSD de khushaljain023](https://www.google.com/goto?url=CAESoQEBxCJF1_Q-GtElS1X1ZjsAQ8DxEmrRUzi9jfcbGkH7zYkTY4nPsgSGg0O_nR6iuku95c5sxOu4YJq-_7_uPi0cEdEThCr4Rg3n8RSS0Hc-FEAMyiTFP52kODA7kzBsCDBZxrvJm7UTsCdCxtSx6ns2kDsbFSgLk7Q-VhsqwXHhkhG8uiBReq73SS2Nnen9SIteCypYtpMZpSAhSrTIz9dd-A&gsessionid=hRtVWwgjUD1BjLxYz81pIMd0U2YAN_Hxw6PblmmdZALqYWmjQo7Cyg)  
  <sub>TradingView, 6 hours ago</sub>  
  Bitcoin's Blockchain Is a Public Ledger. It Tells You What Holders Are Doing Before Price Tells You. Exchange netflow, MVRV, SOPR and dormant supply are not...
- [Peter Schiff advirtió que Ethereum podría caer a $1.000](https://www.google.com/goto?url=CAESjQEBxCJF15-k_c-Xhv7CanZslLLoK2gGWB7r5P5KWlaAbFXu_SqT8mvOy4LrXYkLcrHqfP2SUQjzwBCmWYKD1OO1mh_ySpA5wteS3W1t_gr5dIjE40KSZRHlv7jgFI1Ih7w9BamxCOlBaYGomTWPvh2LuRVncyfmr_EjcAGCup71m67BoV9Aq3kAEcHI64M&gsessionid=hRtVWwgjUD1BjLxYz81pIMd0U2YAN_Hxw6PblmmdZALqYWmjQo7Cyg)  
  <sub>Incrypted, 4 hours ago</sub>  
  El economista Peter Schiff dijo que Ethereum podría caer hasta alrededor de $1,000 si el precio rompe el soporte en $1,600. También criticó los ETF de...
- [Bitcoin se desploma: ETF de Blackrock pierde u$s2.000 M y el mercado busca piso](https://www.google.com/goto?url=CAEStQEBxCJF16BnyK7ntA1ajDm6yUZAR9WsQctBrd8GSifHTEiMHP1BVpe87FBtqtnL66FEpU_6BZAJQOtdn2bJ8TlaaJDq31P9ztGkxJ137r6Aoa7wlrdFTwfOizDBnVPkuegwgEMzM0ihvrp-aYj1UUfR6ZaptdrpSmsOAKIijM7zIoNt6jOpMBbMsdYCwpS24uL0uM_BLAjQgn3_W5GSTZhLg4ex7FjSnYBBafoX6xVwIcpfY9md&gsessionid=hRtVWwgjUD1BjLxYz81pIMd0U2YAN_Hxw6PblmmdZALqYWmjQo7Cyg)  
  <sub>Rosario Finanzas, 6 hours ago</sub>  
  Bitcoin experimenta una fuerte caída, impactando al ETF de Blackrock que registra una pérdida de u$s2.000 millones. El mercado de criptomonedas busca...
- [[Robinhood onchain] USO token issuance rises by $0.15 million as Nvidia adds 249 holder wallets](https://www.google.com/goto?url=CAESawHEIkXX-y1kauYgjf3XW3IdHQAJ1Hwjpk2GgCvL8Rxlif0Cy4Xxver4iCezs7w9znA4iJtPwJ0IijCu_t-kArJv2j4MI19y8XPjp4_KyO9SvPj6ig-jccKrWNPtr3nZOvvrq0O2KqxPcg8_&gsessionid=hRtVWwgjUD1BjLxYz81pIMd0U2YAN_Hxw6PblmmdZALqYWmjQo7Cyg)  
  <sub>www.tokenpost.com, 2 hours ago</sub>  
  USO token supply increased by $0.15 million, while Nvidia added 249 holder wallets. Aggregate trading volume across 200 tokens fell 9.6% to $73.26 million.
- [XRP cae bajo USD $1 mientras aumentan las salidas de ETF: análisis del 16 de noviembre de 2026](https://www.google.com/goto?url=CAESwgEBxCJF10dH7aHXaUfp7twB1I5t8tmrtwXFt2fNPnvRfF1kE-o4Qy8HrVMetyvK2tEFPjOzIwIaMgddztq9cGOYb68RiqCOAifJGNyq0iOgsr9AbZS2iWDkKhHHzFCmsaHFASD31J_2p30y-XYnH4R4KE4c0bTL8y1qWetvwbN6NsYTA7IOnJoEpbLiBAyZ9exFDeaNGg7Pbjo4j8ohN_y0OD7wKwqRQkig7hkpk4a89hj8BaRfbJHoZiMQesZVAKE-_Q&gsessionid=hRtVWwgjUD1BjLxYz81pIMd0U2YAN_Hxw6PblmmdZALqYWmjQo7Cyg)  
  <sub>DiarioBitcoin, 10 hours ago</sub>  
  XRP cotiza en USD $0,957891 y permanece por debajo de sus principales medias móviles, mientras una lectura de RSI de 19,5 sugiere sobreventa.
- [JPMorgan refuerza apuesta por el ETF bitcoin de BlackRock y Coinbase](https://www.google.com/goto?url=CAESbQHEIkXXnqLhGKVB1fC8q7ettjTX8o-BBcP55kM-RB83Mz0d-zSujjyDoPw-cPrNbMStGIzMlM_jotvZm-X1-lSPMbvfZ_vQmyYEHMBK7pyWKoEuoCPOQ0QiOvUHgM29vjWd5_pUPGfCjANtBDs&gsessionid=hRtVWwgjUD1BjLxYz81pIMd0U2YAN_Hxw6PblmmdZALqYWmjQo7Cyg)  
  <sub>Cryptonews.net, 6 hours ago</sub>  
  JPMorgan posee 131 millones de dólares en acciones de Strategy La exposición declarada de JPMorgan al mercado público de criptomonedas creció durante el...
- [¿Por qué caen tanto las cripto? Pierden 310.000 millones en 5 días](https://www.google.com/goto?url=CAEShgEBxCJF14iNgHx3WxV5SA-WgaOnkUCgWJtkt9C5Dxmfi7rcFIu0SbbrKhJnXkBm6AieAd4W3fYRHN18oQQDYDAMKj0vgvvTtR1Ck9lGCrVRQPfWzxsK-xY2_k6ralv80s6VXrYixl2HYz4WmrvKFP3OOA_VsGkBZzksnLVgDBmMj474KIQnow&gsessionid=hRtVWwgjUD1BjLxYz81pIMd0U2YAN_Hxw6PblmmdZALqYWmjQo7Cyg)  
  <sub>Observatorio Blockchain, 4 hours ago</sub>  
  Las cripto pierden 310.000 millones de dólares de valor en 5 días. Analizamos las salidas de ETF, los tipos y la caída de las stablecoins.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 142.24 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 155.13 (-8.3%), 50d 152.82 (-6.9%), 200d 127.97 (+11.2%); 50d above 200d
Momentum: RSI(14) 39.2 | MACD -2.968 vs signal -0.925 (histogram -2.044)
Returns: 1d -2.3% | 5d -0.3% | 1m -12.1% | 3m +8.9%
52-week range: 66.17 - 169.53 (now 73.6% of the way up)
Volatility: ATR(14) 5.46 (3.8% of price) | annualised 20d 48.4%
Volume: 0.20x the 20-day average
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

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.60</summary>

```text
US inventories, week ending 2026-11-06 (published the following Wednesday)
  Crude oil: 414.4 million barrels, +4.7 on the week (a build), 21% percentile over 52 weeks
  Petrol: 210.8 million barrels, +1.8 on the week (a build), 35% percentile over 52 weeks
  Diesel: 103.3 million barrels, +4.1 on the week (a build), 21% percentile over 52 weeks
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
Share count change: 1 week: +1.7% (31.57M) over 7d | 1 month: +17.5% (282.94M) over 32d
Shares outstanding: 13.36M | fund size: 1.90B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral – mixed evidence with no clear macro surprise or decisive technical break. Heavy roll cost penalizes longs, slight reduction in net short positions, tighter crop outlook versus last year, and recent fund outflows balance each other.

**Main reasons it gave:**
- Heavy cost of holding (-8.6% annual) penalizes long positions
- Large speculators net short 16.3% of OI, short position fell 2.1% this week
- US wheat crop good/excellent 48%, down 7 points YoY, indicating tighter supply
- Fund share count down 6.7% over the month, indicating net outflows

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.13% (+0.10 on the week) | 5-year 4.95% (+0.30 on the week) | 10-year 5.13% (+0.27 on the week) | 30-year 5.47% (+0.21 on the week)
Yield curve, 10-year minus 3-month: +1.00 points -- upward sloping (normal)
US dollar index: 103.51 (+1.86 on the week)
Volatility (VIX): 20.47 (+0.5 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.1% (2026-10-01) | jobless claims 200k (2026-11-07)
Policy and expectations: Fed target 4.00% | market expects 2.2% inflation over 10 years
Rate path: 2-year Treasury 4.86% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 21.61 (bar of 2026-11-16), from 500 daily bars
Trend: vs 20d SMA 22.21 (-2.7%), 50d 24.09 (-10.3%), 200d 23.61 (-8.5%); 50d above 200d
Momentum: RSI(14) 32.3 | MACD -0.675 vs signal -0.738 (histogram 0.063)
Returns: 1d -1.1% | 5d -0.2% | 1m -10.0% | 3m -12.5%
52-week range: 19.88 - 28.00 (now 21.3% of the way up)
Volatility: ATR(14) 0.39 (1.8% of price) | annualised 20d 17.9%
Volume: 0.16x the 20-day average
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
Cost of holding this fund instead of wheat itself: -8.6% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -12.5%, commodity -11.8%, gap -0.7% | 6 months: fund -13.6%, commodity -11.8%, gap -1.7% | 12 months: fund +0.7%, commodity +9.4%, gap -8.6%
A commodity fund holds futures, not wheat, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.20</summary>

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
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-11-03, published the following Friday)
Large speculators: net short 16.3% of open interest (534,858 contracts)
Change on the week: -2.1% of open interest
Crowding: 28% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +1.5% (3.42M) over 7d | 1 month: -6.7% (-16.75M) over 30d
Shares outstanding: 10.86M | fund size: 234.60M
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

